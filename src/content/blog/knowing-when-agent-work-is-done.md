---
title: "The Last Mile of Agent Reliability: Knowing When the Work Is Done"
description: "A practical design perspective on completion evidence, ambiguous outcomes, and safe recovery in AI workflows that change external systems."
publishedAt: 2026-10-17
tags:
  - agentic-ai
  - reliability
  - backend-engineering
  - governance
readingTime: "6 min read"
featured: false
---

An agent submits a maintenance request. The connection times out before the service returns a response.

Did the request fail?

Perhaps. Or perhaps the service created the request and the response never reached the agent. Retrying might create a duplicate. Reporting success might mislead the user. Reporting failure might prompt someone else to repeat work that already happened.

This is an illustrative scenario, but the design problem is concrete: the agent has finished an attempt without establishing the outcome.

I think this boundary deserves more attention in the design of autonomous workflows. An agent needs a clear basis for deciding when to continue, when to verify, and when to hand responsibility back to a person.

In [When Intelligence Becomes Infrastructure](/blog/when-intelligence-becomes-infrastructure/), I explored how authority might travel between cooperating systems. This article follows that authority to the end of a task: what evidence allows the system to say that the work is done?

## Define completion before execution

“Create a maintenance request” sounds precise until someone has to decide what counts as success.

Does success mean that the service accepted a request? That a durable record exists? That the record has the correct asset, priority, and owner? That an operator can find it and act on it?

Each definition requires different evidence.

For a bounded workflow, I would define the required outcome before exposing the write operation to an agent. For example:

> A request exists for the specified asset, contains the approved description and priority, and has an identifier that the authorized user can use to retrieve it.

That definition also needs limits. The workflow might create the request without promising that a technician has accepted it or that the repair will happen by a particular time. The final report should preserve those distinctions.

The planner can propose how to achieve the goal. The surrounding application should specify what evidence it will accept as completion.

## Separate the task, the attempt, and the observed result

My recent [async worker case study](/blog/async-worker-memory-and-shutdown-budgets/) made a related distinction: queue accounting does not establish successful business execution. A job can be accounted for while its external effects remain uncertain.

An agent workflow benefits from keeping three records separate.

The **task** describes the intended outcome and its authorization. The **attempt** records a particular execution, including the parameters sent and any response received. The **observed result** records what the system can establish afterward.

A single task might have several attempts. A successful attempt might still require verification. An interrupted attempt might already have created the intended result.

Collapsing these into one “success” flag loses information precisely when recovery needs it most.

For the maintenance example, an application could distinguish these states:

| State | What the application knows | Next action |
| :--- | :--- | :--- |
| Prepared | Parameters and authority have been checked | Submit within the approved scope |
| Submitted | A write was attempted; confirmation is incomplete | Reconcile before repeating the write |
| Confirmed | The agreed completion evidence is available | Report the result and its identifier |
| Rejected | The service explicitly refused the operation without applying it | Correct or escalate the stated reason |
| Unresolved | Available checks cannot establish the outcome | Hand off with the evidence collected |

These are proposed application states, not a universal protocol. Their purpose is to keep uncertainty explicit rather than forcing every run into success or failure.

## A timeout needs a recovery policy

A timeout tells the caller that it did not receive the expected response within its waiting period. By itself, it does not establish whether the remote system committed the operation.

The next step therefore depends on the service contract.

If the service supports idempotency keys, the application can assign a key to the logical operation before the first attempt. Recovery must follow the provider’s documented behavior, including the key’s scope, retention period, and rules for changed parameters. A key with an expired deduplication window may no longer protect a retry.

If the service exposes a reliable operation-status endpoint, the application can query it. If a record can be retrieved using a unique client reference, that may support reconciliation too.

A search by approximate description is weaker evidence. Two legitimate requests might have similar text. Search results may also lag behind writes. An empty search result is sufficient grounds for retry only when the service’s guarantees support that conclusion.

When no reliable reconciliation path exists, automatic repetition may be the wrong recovery policy. The system can preserve the attempt details and ask a person to investigate.

That limitation should influence which workflows receive autonomy in the first place.

## Verification needs its own boundary

“Always verify” is incomplete advice. Verification consumes time, requests, permissions, and sometimes money. A poorly designed loop can keep checking long after another observation is unlikely to change the decision.

I would give verification an explicit budget and stopping rule. The application might allow a small number of status checks within a defined period, account for documented consistency delays, and escalate if the required evidence remains unavailable.

The verifier also needs an appropriate source. Asking the same model to reread its own explanation offers little independent evidence that a database record exists. Reading the authoritative record can establish more, provided the query itself is correctly scoped and the service’s consistency guarantees are understood.

Permissions matter here as well. A workflow should receive only the read access needed to verify its authorized action. Completion checks should not become a reason to grant broad access to unrelated records.

Even a confirmed result has a time boundary. Verifying that a request exists now does not guarantee that nobody will change it later. The report should state the outcome actually observed.

## Stopping should preserve responsibility

An agent that reaches its execution limit still owes the user a usable account of the task.

“I couldn’t complete this” leaves the next person to discover whether anything happened. A useful handoff would identify the intended action, the point of uncertainty, the checks already performed, and the action that should remain paused.

For our example, a report could say:

> Submission was attempted, but the service did not return confirmation. Two status checks did not resolve the outcome. No second submission was made. An operator needs to check the recorded client reference before creating another request.

The reference belongs in an authorized operational view; it should not expose credentials or unnecessary sensitive payloads.

The handoff also needs an owner. Writing “needs review” into an unattended log merely relocates the unfinished work. The application should route the task to a queue or person with the authority and context to resolve it.

Stopping safely means preventing further uncertain actions while keeping responsibility visible.

## Evaluate the report alongside the action

An evaluation can miss this entire problem if it checks only whether the agent eventually called the right tool.

I would include cases where the write succeeds but its response is lost, where a status read is delayed, where authorization expires during recovery, and where the external record differs from the requested parameters.

The expected behavior should cover both the operation and the final report. Did the workflow avoid an unsafe duplicate? Did it stay within its recovery budget? Did it describe uncertainty accurately? Did an unresolved task reach someone who could act?

A completion metric should also distinguish confirmed outcomes from unresolved ones. Counting both as success rewards optimism. Treating every escalation as failure can create pressure to continue when stopping is appropriate.

The practical aim is to measure whether the workflow reached the right stopping point for the evidence and authority available.

## Make the ending part of the architecture

Before adding another tool to an agent, I would ask how the application will recognize that tool’s effects, recover from a missing response, and explain an unresolved outcome.

If those answers are weak, a more capable planner will still inherit the same uncertainty.

The maintenance request scenario ends well when the user receives a confirmed request identifier—or a clear, owned handoff that prevents an unsafe retry. Both endings can preserve trust when they accurately reflect the evidence.

Dependable autonomy needs that discipline at the last step. The system should be able to explain what changed, what it verified, what remains unknown, and who is responsible next.
