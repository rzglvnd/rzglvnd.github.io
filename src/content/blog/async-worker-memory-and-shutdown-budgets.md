---
title: "Designing Explicit Memory and Shutdown Budgets for an Async Worker"
description: "A measured case study of admission, cooperative shutdown, bounded outcome history, and diagnostic payload limits in a Python worker."
publishedAt: 2026-10-14
tags:
  - python
  - reliability
  - backend-engineering
  - performance
readingTime: "6 min read"
featured: false
---

In my Python systems lab, limiting a worker's queue left another source of growth: the identifiers and failure details retained after jobs finished. Controlling the backlog addressed one stage of the worker's lifetime. Understanding its memory behavior required following ownership through admission, execution, and reporting.

I developed a [single async worker](https://github.com/rzglvnd/python-system-lab/blob/3377d518621c1e9bbfdfe8bf506aa7e5ae9a32cb/queued_worker.py) with explicit contracts for each stage, then measured its allocations. With 100 retained failures and 4,096-character messages, a 128-character message cap reduced median current traced allocations from **468,626 to 71,826 bytes**. Larger source messages still raised peak allocations.

The [implementation and shutdown contract](https://github.com/rzglvnd/python-system-lab/blob/3377d518621c1e9bbfdfe8bf506aa7e5ae9a32cb/docs/worker_shutdown.md) describe an in-memory lab that queues string identifiers. It has no durable queue, restart recovery, or production deployment. Its value is making the boundaries small enough to test and the claims specific enough to measure.

## Admission establishes responsibility

A producer waiting for capacity has not yet submitted accepted work. Acceptance occurs when the worker enqueues the identifier. The lifecycle check, duplicate check, capacity check, and enqueue contain no `await`, so another coroutine on the same event loop cannot interleave closure with that final admission operation. This interface assumes one event loop; it is not thread-safe.

The waiting interface retries admission after a capacity notification. That notification reserves no slot: competing producers must recheck capacity and duplicate detection. Closure wakes waiting producers so they can receive an admission error. Cancellation while waiting does not accept the job; after acceptance, cancelling the producer cannot retract it.

A reserved control slot lets synchronous `close()` append its stop marker even when waiting jobs fill their capacity. This prevents a full backlog from obstructing the operation that stops new admissions. Creating a shutdown coroutine alone does not close admission until that coroutine runs.

The [admission tests](https://github.com/rzglvnd/python-system-lab/blob/3377d518621c1e9bbfdfe8bf506aa7e5ae9a32cb/tests/test_worker_admission.py) coordinate producers and handlers with events, including competing waiters and closure after a capacity notification. Timing watchdogs detect hangs; event ordering establishes the behavior under test.

Backpressure also depends on producers. Spawning unlimited tasks that wait to submit would retain their arguments and task state outside the bounded queue. The benchmark therefore uses one producer that awaits submissions in sequence.

## Shutdown has a drain budget

Shutdown closes admission, allows accepted work to drain, and requests cancellation when the grace period expires. It then awaits the worker, including its cleanup. The grace period limits draining; cooperative cancellation and cleanup can extend the total shutdown time. A handler that blocks the event loop or ignores cancellation can prevent shutdown from finishing.

The report distinguishes completed, failed, interrupted, and unstarted jobs. Queue bookkeeping remains separate: `task_done()` means an item has been accounted for, including discarded work. A successful queue `join()` does not establish successful business execution.

For supported shutdown paths, lifetime accounting satisfies:

```text
accepted = completed + failed + interrupted + unstarted
```

An interrupted job may already have changed an external system. Retrying it safely requires an idempotency or reconciliation design beyond this worker. If deployment requires a hard termination deadline, that decision also belongs outside the cooperative worker, with an explicit recovery policy for lost or uncertain work.

## Retention changes the meaning of a report

A finite `history_limit` retains the latest outcomes across all four categories in one shared history. Lifetime counters remain independent. A report can therefore preserve the total number of failures while omitting an earlier failure's details. `omitted_outcomes` makes that loss visible.

Identifiers are evicted with their outcomes. Duplicate detection covers waiting jobs, the running job, and retained history; it permits an identifier to be submitted again after eviction. That is a bounded detection window, not durable idempotency. Retaining every identifier would preserve lifetime duplicate rejection at a growing memory cost.

With finite history N and waiting capacity M, the worker stores at most N + M + 1 job identifiers, including the running job. Caller-held report snapshots and waiting producer tasks have separate ownership. The [retention tests](https://github.com/rzglvnd/python-system-lab/blob/3377d518621c1e9bbfdfe8bf506aa7e5ae9a32cb/tests/test_worker_retention.py) exercise eviction, ID reuse, immutable reports, and accounting across shutdown paths.

Payload size needs its own policy. `max_job_id_bytes` rejects oversized UTF-8 identifiers before acceptance or a capacity wait. `max_error_message_chars` instead retains a prefix of an exception message and records `message_truncated`. The separate flag preserves the character budget and distinguishes a complete short message from shortened diagnostics.

The units are deliberate: IDs use encoded bytes; messages use Python Unicode code points. A combining sequence can be split by the message cap. Truncation also leaves any sensitive information in the retained prefix intact.

## Measure retained and temporary allocations separately

I ran **81 fresh-process trials**: three source-message widths, three caps, three retention policies, and three repetitions. Each trial processed 1,000 failing jobs with capacity for 16 waiting IDs. Cap and retention-policy order rotated between repetitions. The unrestricted baseline used the same source version as the capped cases.

The table selects the 100-outcome policy. Values are median traced bytes on CPython 3.13.7, 64-bit Windows 11.

| Source message / retained cap | Current bytes | Peak bytes |
| :--- | ---: | ---: |
| 4,096 characters / unrestricted | 468,626 | 487,860 |
| 4,096 characters / 128 | 71,826 | 91,060 |
| 4,096 characters / 0 | 54,926 | 74,160 |
| 128 characters / 128 | 71,826 | 80,007 |

At cap 128, increasing source width from 128 to 4,096 left current allocations unchanged in these trials. Peak allocations rose from 80,007 to 91,060 bytes. Full messages were still constructed, hashed with temporary concatenation and encoding, and carried by exceptions before the worker shortened the retained details. This workload does not isolate the cost of exception formatting or slicing alone.

Tracing began after imports and event-loop creation. Sampling kept both the stopped worker and its report alive, without forced garbage collection. Every trial checked the full source checksum, processed and outcome counts, retained lengths, and retained truncation counts. A cap could not make skipped work disappear from those checks.

The [complete report](https://github.com/rzglvnd/python-system-lab/blob/3377d518621c1e9bbfdfe8bf506aa7e5ae9a32cb/reports/worker-error-caps-2026-10-14.md) and [raw trials](https://github.com/rzglvnd/python-system-lab/blob/3377d518621c1e9bbfdfe8bf506aa7e5ae9a32cb/reports/worker-error-caps-2026-10-14.json) preserve reproduction commands, ranges, environment metadata, and source hashes. These measurements cover traced Python allocations, not process RSS, all native allocations, throughput, or a universal memory bound.

For an ingestion or agent-execution service, I would specify these contracts separately: when work becomes accepted, how admission stops, what survives a process failure, which diagnostic details may be discarded, and how uncertain side effects are recovered. Each contract needs its own evidence. Queue capacity, retention count, and payload limits can then become defensible operational choices rather than a single ambiguous promise that the worker is bounded.
