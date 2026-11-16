---
title: "Owning a Streaming RAG Request Through Cancellation"
description: "A FastAPI case study in resource ownership, cancellation, HTTP response boundaries, and retry contracts verified against a real SDK with an offline transport."
publishedAt: 2026-11-16
tags:
  - python
  - reliability
  - backend-engineering
  - rag
readingTime: "6 min read"
featured: false
---

A streaming request can disconnect while a worker is still constructing its provider client or reading its next chunk. The handler may stop awaiting that work before the worker finishes. Who owns the client when it eventually returns? Who closes a stream that never starts?

I addressed these questions in Local LLM Chat Engine, a prototype FastAPI/RAG backend. The resulting design gives setup and response teardown explicit ownership, then tests the transitions under injected failures. This article builds on my [Python I/O ownership experiments](/blog/python-io-deadlines-and-ownership/) by applying those contracts at an HTTP boundary.

All backend links refer to revision `8693e31`. The evidence comes from controlled ASGI tests and real SDK execution over synthetic HTTP responses. It includes no production traffic or measured latency claim.

## Establish ownership before awaiting construction

Moving synchronous provider construction into a worker protects the event loop, but creates a handoff problem. If cancellation interrupts the await, assigning the returned client to a local variable is insufficient: the worker may finish after the caller has lost access to its result.

The request creates a small [adapter owner before dispatching construction](https://github.com/rzglvnd/local-llm-chat-engine/blob/8693e31a4303bbbd2eed6409b0e58886b04cc2d8/app.py#L216). Its synchronous initializer holds a lock while constructing and recording the adapter. Cleanup takes the same lock. If construction is already running, cleanup waits for its result and closes the acquired client. If cleanup wins before initialization begins, initialization refuses to allocate.

Setup retains this ownership until the streaming response has been constructed successfully. Retrieval or response-construction failure therefore closes an acquired client before re-raising the original exception. This contract covers an adapter that construction returns; it cannot repair resources leaked internally by a failing SDK constructor.

The lock deliberately trades prompt cleanup for safe ownership. A constructor that never returns can keep cleanup waiting. Offloading and cancellation do not supply a hard termination mechanism for that worker.

## Put initialization errors before the HTTP boundary

The [`/chat_stream` handler](https://github.com/rzglvnd/local-llm-chat-engine/blob/8693e31a4303bbbd2eed6409b0e58886b04cc2d8/app.py#L473) awaits initialization before returning its response. An unavailable provider or failed constructor can therefore produce the existing HTTP 400 JSON response before streaming headers are sent.

Once the response has started, failure has a different meaning. A read may fail after the caller has received HTTP 200 and some text. The implementation propagates that failure, performs cleanup, and does not emit its normal `done` event. It cannot replace the already-sent status with a fresh JSON error response. Consumers must treat partial output without completion as incomplete.

The [concurrency tests](https://github.com/rzglvnd/local-llm-chat-engine/blob/8693e31a4303bbbd2eed6409b0e58886b04cc2d8/tests/test_chat_concurrency.py) gate provider work with events. They verify that `/health` can respond while that work remains blocked, and that streaming headers have not started during initialization. This establishes ordering and event-loop availability for those paths; retrieval still runs synchronously on the event loop.

## Make teardown survive an unstarted generator

Putting every release in a generator's `finally` block leaves an awkward gap: closing a generator before its body has ever run does not execute that body’s cleanup. A send failure at the response headers can occur before the SSE generator reaches the adapter at all.

The [response wrapper](https://github.com/rzglvnd/local-llm-chat-engine/blob/8693e31a4303bbbd2eed6409b0e58886b04cc2d8/app.py#L430) therefore owns a client-cleanup callback independently of stream iteration. During teardown it closes the SSE generator, then invokes the owner’s callback. Once iteration has acquired the adapter iterator, the SSE generator’s `finally` closes that iterator first. The adapter, in turn, closes its underlying SDK stream.

A second lock serializes advancing the SSE generator and closing it. Cleanup runs in a worker, so waiting for an active read does not itself block the event loop. An AnyIO shield permits awaited finalization inside an already-cancelled cancellation scope. The lock also covers the tested direct task-cancellation case where an abandoned await leaves its worker reading.

The [failure-path tests](https://github.com/rzglvnd/local-llm-chat-engine/blob/8693e31a4303bbbd2eed6409b0e58886b04cc2d8/tests/test_chat_stream_cleanup.py) retain references to tracked resources, preventing garbage collection from concealing a missing close. They cover disconnects, send failures, setup failures, cancellation during construction, and cancellation during a read. Cleanup failures are logged without replacing the original result or exception.

The [OpenAI adapter](https://github.com/rzglvnd/local-llm-chat-engine/blob/8693e31a4303bbbd2eed6409b0e58886b04cc2d8/adapters/openai_adapter.py) closes its owned modern SDK client once under this request lifecycle. Borrowed legacy SDK module state is not closed. A failed close remains a failed close: recording that it was attempted does not prove physical resource release.

## Test the SDK boundary as well as the adapter

Fake SDK clients verify application wiring, including constructor arguments and cleanup calls. They cannot establish how the real SDK retries or handles a broken response body.

The separate [offline contract suite](https://github.com/rzglvnd/local-llm-chat-engine/blob/8693e31a4303bbbd2eed6409b0e58886b04cc2d8/tests/sdk_contract/test_retry_transport.py) exercises OpenAI SDK **3.51.0** with HTTPX2 **2.16.0**. It injects a mock HTTP transport into a real client, uses a dummy key and `.invalid` hostname, and blocks socket/DNS access. SDK retry logic, parsing, exception translation, and stream handling still execute.

| Injected response | Retry allowance | Observed transport attempts and result |
| --- | --- | --- |
| Persistent 503 | 0 | 1; SDK server error |
| Persistent 503 | 2 | 3; SDK server error |
| 503, then 200 | 2 | 2; generated text returned |
| Ordinary 400 | 2 | 1; SDK bad-request error |
| HTTP 200, one text chunk, then read failure | 2 | 1; partial text followed by connection error |

The last case verifies that partial output is not replayed. It also checks response-body closure before client closure, preserves the injected read error as the exception cause, and checks client/transport closure explicitly. The text chunk is synthetic; no model or tokenizer participates.

The retryable responses carry a public `retry-after-ms` hint. The suite does not replace SDK sleep or private backoff logic, and makes no timing assertion. Its [dedicated dependency file](https://github.com/rzglvnd/local-llm-chat-engine/blob/8693e31a4303bbbd2eed6409b0e58886b04cc2d8/requirements-sdk-contract.txt) requires Python 3.11 or newer for this transport version. CI runs the five cases on Python 3.11; local verification also used Python 3.12.

## Keep the guarantee narrower than the configuration

The adapter defaults to a 60-second I/O timeout and, for the modern SDK, two retries. A retry allowance counts additional attempts. It does not turn three attempts into a 180-second request deadline: I/O phases, backoff, stream activity, and time awaiting a worker have different boundaries.

These tests establish behavior for the recorded SDK/transport pair and injected failures. They do not measure live network timeouts, establish behavior across all SDK versions, or guarantee bounded shutdown. Construction, reads, and cleanup may still stall; repeated cancellation or process termination can interrupt finalization.

The useful outcome is an ownership model with observable transitions and version-pinned evidence. A future SDK upgrade can be reviewed against attempt counts, partial-output behavior, and release order instead of relying only on unchanged application code.
