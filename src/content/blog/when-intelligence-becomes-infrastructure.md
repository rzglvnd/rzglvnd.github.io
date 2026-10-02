---
title: "When Intelligence Becomes Infrastructure"
description: "A look toward a future of cooperating AI systems—and the authority, memory, and human choices that will shape it."
publishedAt: 2026-10-02
tags:
  - ai-systems
  - future-of-ai
  - governance
  - software-architecture
readingTime: "7 min read"
featured: false
---

Imagine an ordinary Tuesday in 2032.

A maintenance system notices an unusual pattern in a piece of equipment. A planning agent moves a service window. A procurement agent reserves a replacement part. A scheduling agent rearranges a team’s afternoon. A customer-facing system updates a delivery estimate.

By the time someone opens a dashboard, five systems have changed the organization’s plans.

The decisions may all be reasonable. The equipment may even get repaired before it fails.

Then someone asks: **Who authorized the extra cost?**

The maintenance system identified a risk. The planner interpreted urgency. Procurement acted on the planner’s request. Each component can explain its own step. Yet the organization may struggle to explain how an observation became a commitment.

This is an imagined future, not a prediction with a deadline. But it is the future I find useful to design against: ordinary systems making connected decisions, quietly, at a scale that makes individual supervision impractical.

In [A Programmer’s Guide to Trustworthy Intelligence](/blog/a-programmers-guide-to-trustworthy-intelligence/), I argued that trust needs evidence, boundaries, and accountability. The next question is what those ideas might require when intelligence becomes part of the infrastructure around us.

## The scarce resource could become legitimate authority

If capable models become cheaper and easier to deploy, more tasks will become technically possible. An organization might have abundant capacity to analyze, propose, negotiate, and coordinate.

Permission to act will remain a separate question.

A system may understand a contract without having authority to accept it. It may identify an operational problem without having permission to interrupt service. It may propose a better schedule without knowing which commitments people consider non-negotiable.

I expect the distinction between capability and authority to become one of the defining concerns of software architecture.

That would change the questions buyers ask. Alongside “How capable is this agent?” they would ask “What can we safely authorize it to do, under what conditions, and how would we know when those conditions stop holding?”

The valuable product would include a credible answer.

## Every delegation should carry a budget of authority

Return to the maintenance example. Suppose the planning agent can request a replacement part, but its authority is limited to a particular asset, a spending ceiling, and a short time window.

When it delegates to procurement, that scope should travel with the request. Procurement should receive only the permissions needed to complete the purchase. Delegating again should never silently expand them.

The resulting record would let someone reconstruct the chain from the original authorization to the final commitment.

I think of this as a budget of authority. Money is one dimension, but so are time, data access, affected systems, and the right to create obligations for other people.

A useful delegation record might identify:

- The person or policy that authorized the work.
- The resources and actions covered by that authorization.
- The limits, expiry, and conditions requiring escalation.
- Whether further delegation is allowed.
- The evidence needed to confirm completion.

The difficult engineering work would happen where these records meet actual tools. A document saying “spend no more than this amount” is insufficient if the payment interface accepts any amount the model supplies. Enforcement must happen at the point of action.

Even then, several individually valid actions could exceed a shared limit. Five agents must not each interpret the same remaining budget as exclusively theirs. Coordination, reservations, and atomic checks would matter as much as the wording of the policy.

My earlier article on [agent handoffs](/blog/most-agents-fail-at-handoffs-not-reasoning/) focused on workflow boundaries. In this future, those boundaries would also become the places where authority must be preserved.

## Organizations would need a memory of decisions

Consider what happens six months after our imaginary repair.

The model has changed. The original documents have been revised. A policy has been replaced. The person who approved the maintenance budget has moved to another team.

An audit log may show that a tool ran successfully. That alone cannot explain why the action was legitimate at the time.

An organization would need to preserve the relevant decision context: which policy applied, what information supported the action, which uncertainty remained, and who accepted the trade-off.

This does not require retaining every conversation forever. Unrestricted retention would create its own privacy and security problems. It requires deciding which evidence is necessary, how long to keep it, and who can inspect it.

Nor should a fluent explanation generated afterward be treated as a substitute for a contemporaneous record. A plausible account of a decision is weaker evidence than the inputs, approvals, and outcomes captured when it happened.

The purpose of this memory would extend beyond blame. It would help people learn. If a workflow repeatedly escalates the same exception, perhaps the policy needs clarification. If it repeatedly makes costly but technically compliant decisions, perhaps the objective is poorly specified.

Institutional memory could become a practical source of improvement for intelligent systems.

## The emergency stop would need an organization behind it

Stopping one process is straightforward compared with stopping a network of commitments.

By the time a human intervenes, a request may have entered a queue, a supplier may have reserved stock, another agent may have copied data, and a customer may have received a promise.

Revoking a credential can prevent future access. It cannot erase information already disclosed or automatically unwind an agreement.

So the future “stop” button would need several clearly defined behaviors: stop accepting new work, interrupt pending actions where possible, revoke delegated permissions, and identify commitments that require recovery.

Some actions could be reversed. Others would need compensation, correction, or a conversation with the affected person. The system should make that distinction visible before an incident.

This is one reason I remain interested in the quieter parts of engineering: idempotency, queues, transaction boundaries, recovery procedures, and explicit state transitions. They give abstract promises of control a concrete meaning.

An organization that cannot recover from a decision has less practical control than its approval screen suggests.

## Human attention would become a design constraint

There is a tempting response to every uncomfortable edge case: ask a human.

At sufficient scale, that response becomes a queue nobody can responsibly process.

An approval request consumes attention. If the request lacks context, the reviewer must reconstruct it. If the interface presents dozens of similar requests, careful review becomes harder. If approving is effortless while questioning requires investigation, the system creates pressure toward acceptance.

I would therefore treat human attention as a limited resource in the architecture.

Routine actions could operate within narrow, explicit authority. Decisions that introduce a new commitment, exceed an agreed limit, or affect someone’s rights would need a more deliberate path. The review should expose the proposed action, supporting evidence, uncertainty, consequences, and available alternatives.

People must also be able to change the objective itself. A human who can only approve or reject a machine’s chosen plan has a restricted form of control.

Meaningful agency includes the ability to say: this is the wrong problem to optimize.

## The future could divide along the quality of its institutions

I can imagine two organizations using equally capable models and achieving very different results.

In one, permissions accumulate, exceptions become permanent, and nobody owns the decisions between systems. Automation increases activity while making responsibility harder to locate.

In the other, authority is scoped, evidence is retained deliberately, failures are recoverable, and people can challenge both actions and objectives. Automation expands what the organization can accomplish without making its behavior incomprehensible.

Model quality would still matter. So would data, economics, and the suitability of the work. But institutional quality could explain a substantial part of the difference.

This builds on my argument that [agentic AI needs an operating model](/blog/agentic-ai-needs-an-operating-model/). Over time, that operating model could become as consequential as the intelligence it surrounds.

## What I would build toward

I would begin with one bounded workflow and make its authority legible. I would trace a request through every handoff, identify where it can create a commitment, and test what happens when permission is withdrawn midway through execution.

I would ask whether the record is sufficient for someone who was absent to understand the outcome. I would test recovery as seriously as successful completion. And I would measure the attention required from the people expected to supervise it.

These choices do not require certainty about which models will dominate or how quickly autonomy will advance. They remain useful across several plausible futures.

The future I would like to help build is one in which capable systems make cooperation easier and leave people with more room to exercise judgment.

On that ordinary Tuesday in 2032, the equipment gets repaired. The commitments stay within the authority granted. An exception reaches someone with enough context to decide. Months later, the organization can still explain what happened.

Nothing spectacular needs to occur.

Perhaps that will be one of the clearest signs of progress: intelligence becoming powerful enough to be useful, and accountable enough to become ordinary.
