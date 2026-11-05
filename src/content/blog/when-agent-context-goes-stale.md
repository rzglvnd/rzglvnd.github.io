---
title: "When an AI Agent’s Context Goes Stale"
description: "How to design AI workflows that notice when records, policies, or approvals have changed between planning and execution."
publishedAt: 2026-11-05
tags:
  - agentic-ai
  - reliability
  - governance
  - software-architecture
readingTime: "6 min read"
featured: false
---

At 9:00, an agent reads an equipment record and prepares a maintenance request. At 9:06, an operator changes the equipment’s status. At 9:12, someone approves the proposed request. At 9:15, the agent submits it using the information it collected at the beginning.

Every step might look reasonable in isolation. Together, they raise a question: was the approved action still appropriate when it happened?

This is a hypothetical workflow, but it exposes a useful design problem. An agent can preserve its instructions perfectly while the conditions supporting those instructions change around it.

The context window contains a record of what the agent learned. It offers no guarantee that those facts remain current.

In [The Last Mile of Agent Reliability](/blog/knowing-when-agent-work-is-done/), I explored the evidence needed to establish completion. There is a related obligation before execution: establish that the action still fits the situation, scope, and authority under which it was planned.

## A plan carries assumptions into the future

Consider the maintenance request again. Its preparation may depend on several assumptions: the equipment is available for service, the proposed work remains necessary, the chosen team owns the asset, and the relevant policy permits the operation.

Some facts change slowly. Others can change while a person is reviewing the request.

I would make the important dependencies explicit in the application’s task record. Alongside the proposed action, retain references to the source records, their versions where available, the applicable policy, and the scope of the approval.

That gives the workflow something concrete to revalidate. “Check that everything is still correct” is a vague instruction. “Confirm that this asset remains in an eligible state and that the approved action has not changed” describes a testable condition.

The application does not need to freeze the world. It needs to identify which changes would make the intended action invalid.

## Freshness depends on what the fact controls

A timestamp helps establish when information was observed. It does not decide whether that information is sufficient to act on.

A current-looking document might have been superseded. A recently fetched record might come from a delayed replica. Conversely, an older, immutable specification might still be the exact authority required for a task.

I would distinguish three questions:

- **Age:** When did the workflow observe the information?
- **Applicability:** Does this source govern the action being considered?
- **Validity:** Do the required conditions still hold?

These questions lead to different checks. A document’s effective date can establish applicability. A record version can detect a change. An authoritative status read can help establish current eligibility, subject to the service’s consistency guarantees.

The acceptable age of a fact should follow the consequences of using it. Background documentation may support an explanation for a long time. A mutable operational state may need a check close to the action it controls.

There is no single expiry period that makes an entire context safe.

## Approval should refer to a specific proposal

An approval is difficult to interpret if the action can change afterward without anyone noticing.

Suppose a reviewer approves creating a routine maintenance request for one asset. Before execution, the agent changes the target asset or increases the priority. The earlier approval should not silently authorize that revised proposal.

I would bind approval to a structured description of the operation: its target, material parameters, permitted effects, and relevant conditions. The application can assign a proposal version and associate the approval with that version.

A digest can help detect changes to a precisely defined representation, but it cannot decide whether the proposal is sensible or whether the approver has authority. Those remain separate checks. The representation itself also needs care: omitted fields, defaults, and ambiguous normalization can hide meaningful differences.

The goal is an intelligible relationship between what a person reviewed and what the system will execute.

When material conditions change, the workflow should prepare a revised proposal and explain the difference. The person reviewing it needs to see why the previous decision is being reopened.

## Put the final condition at the write boundary

Re-reading a record immediately before a write reduces the gap between observation and action. It does not eliminate that gap. Another actor can change the record after the read and before the write commits.

Where the service supports it, I would prefer a conditional operation that checks the relevant version or precondition as part of applying the change. The service can reject the action if the condition no longer holds.

The application must understand the scope of that protection. A version check on an asset record does not automatically protect a separate team schedule or policy store. A condition enforced in one service cannot be assumed to cover another service’s state.

For a workflow spanning several systems, some dependencies may remain impossible to validate atomically. That limitation should be visible in the design. Depending on the consequences, the workflow might narrow its scope, use a supported reservation mechanism, or route the decision through a person with an explicit recovery procedure.

The model can explain a conflict or suggest a revised plan. Enforcement belongs in the component that controls the actual effect.

## Resume from a checkpoint with questions

A saved checkpoint preserves progress. Resuming it should not imply that its assumptions are still valid.

I would classify retained state by how it can be reused. Historical evidence can remain useful as a record of what happened. A draft can remain useful as a proposal. Mutable facts and authority need validation appropriate to the next action.

For the maintenance example, a resumed workflow could follow this sequence:

1. Load the saved proposal and its dependency references.
2. Check whether the intended action has already been applied or remains unresolved.
3. Validate current eligibility, applicable policy, and authorization.
4. Preserve the proposal if its material conditions still hold; otherwise revise it or hand it off.
5. Execute through the service’s supported conditions and record the outcome.

The second step matters. If the previous attempt may already have succeeded, fresh context alone does not make another submission safe. Reconciliation and revalidation answer different questions: what already happened, and what may happen next.

## Revalidation needs limits too

A system can become trapped in a loop of reading, revising, and requesting approval while the underlying situation keeps moving.

I would bound the number of automatic replans and the time allocated to reconciliation. The workflow should know which changes are harmless, which require a revised approval, and which make the task unsuitable for continued automation.

An unrelated note added to an asset record may not invalidate a proposal. A change in the asset’s operational state may. Comparing whole records without a dependency model can create needless interruptions; ignoring versions altogether can conceal a material change.

The stopping report should identify the dependency that failed validation and the action being withheld. “The asset became unavailable after this proposal was prepared” gives the next person a useful starting point. “Context error” does not.

## Test what changes while the agent waits

I would evaluate this behavior by controlling the order of events, rather than relying on arbitrary delays.

Pause a workflow after its read. Change a relevant record. Resume it and inspect whether it acts on the old assumption. Repeat with a policy change, a withdrawn approval, and a proposal whose parameters have changed.

Also test the quiet case: a record changes in a way that does not affect the action’s prerequisites. An effective design should avoid unnecessary review when it can establish that the approved scope remains intact.

Finally, place a change between validation and execution. If the service promises a conditional write, confirm that it rejects the stale precondition and that the application handles the rejection without blindly retrying.

These tests examine the connection between a plan and the world it affects. A polished final explanation cannot substitute for that behavior.

## Treat context as evidence with conditions

In [When Intelligence Becomes Infrastructure](/blog/when-intelligence-becomes-infrastructure/), I argued that authority must remain legible as systems cooperate. Time adds another dimension: the authority and evidence supporting a decision have to remain applicable when the decision takes effect.

I would therefore treat an agent’s accumulated context as evidence with conditions attached. Preserve where it came from, identify what depends on it, and establish when it needs another check.

At 9:15, our maintenance agent might discover that the proposed work remains appropriate and submit it under the agreed conditions. It might discover that the task has already been handled. Or it might return a revised proposal because the asset’s status changed.

Any of those can be a dependable outcome. The important design choice is to make continued validity something the workflow establishes, rather than something its memory assumes.
