---
title: "A Programmer’s Guide to Trustworthy Intelligence"
description: "Designing cooperation, accountability, and human agency for a world of increasingly autonomous systems."
publishedAt: 2026-09-22
tags:
  - ai-systems
  - governance
  - trustworthy-ai
  - software-architecture
readingTime: "10 min read"
featured: false
---

![Cover illustration for A Programmer’s Guide to Trustworthy Intelligence](/assets/blog/trustworthy-intelligence.png)

In 2015, I wrote about distrust among intelligent entities approaching a technological singularity.

The language was speculative. The argument was rough. But the underlying concern seems considerably less speculative today.

We are now building systems that can write software, operate tools, retrieve and transform information, communicate with other systems, make plans, and increasingly act with limited autonomy.

The important question is no longer merely whether machines can become more capable.

They already are.

> **The more important question is this:
> What kind of environment should increasingly capable intelligent entities inhabit?**

That question applies to artificial agents, organizations, governments, software systems—and ultimately to us.

The answer I once proposed was **trust through radical openness**.

Today, I would formulate it differently.

---

## 1. Trust Is Not a Feeling

We often speak of trust as though it were simply a moral relationship between two actors:

*I trust you. You trust me. Therefore, cooperation becomes possible.*

That works reasonably well between friends.

It works less well when the participants are strangers, corporations, software agents, governments, distributed systems, or entities whose objectives we cannot completely observe.

In engineering, trust cannot merely mean confidence.

It must have structure.

A secure system does not remain secure because every participant behaves honorably. A distributed system does not remain correct because every machine is assumed never to fail. A financial system does not function because fraud is unimaginable.

Mature systems assume that mistakes, conflicts, failures, and adversarial behavior are possible.

They are designed accordingly.

The same principle should guide intelligent systems.

> **The objective should not be universal trust.
> It should be justified trust.**

And justified trust requires evidence.

---

## 2. From Openness to Verifiability

Years ago, I imagined an integrated development environment in which participants could inspect one another’s code.

The idea was simple:

Hidden intentions generate suspicion.
Transparency reduces suspicion.
Therefore, openness should improve cooperation.

There is still something valuable in that intuition.

But openness alone is insufficient.

Source code can be visible while behavior remains difficult to understand.

A model can be publicly available while its training process remains opaque.

An autonomous agent can expose parts of its operation while still possessing access to resources it should never have been allowed to control.

Conversely, a system can keep sensitive implementation details private while still providing strong guarantees about what it is permitted to do.

So the more useful principle is not:

> **Everything must be visible.**

It is:

> **Everything important must be accountable.**

That distinction matters.

Accountability may require logging, reproducible evaluations, cryptographic provenance, permission boundaries, independent auditing, or clear records of which agent performed an action, using which information, under whose authority, and with what consequences.

Transparency is one instrument.

**Verification is the larger goal.**

---

## 3. Intelligent Systems Need Constitutions, Not Good Intentions

Suppose we build a highly capable autonomous agent and tell it:

*Be helpful. Be ethical. Do not cause harm. Cooperate with others.*

Those instructions matter.

But they are not enough.

Humans have been writing moral instructions for thousands of years. Our difficulty has rarely been the absence of sentences describing desirable behavior.

The harder problem is turning principles into institutions.

Societies developed laws, courts, contracts, accounting systems, procedures, access controls, separation of powers, audits, and permanent records precisely because good intentions cannot carry the entire burden of civilization.

Artificial agents will require analogous structures.

An agent should not receive unrestricted access merely because we hope it will behave correctly.

Its authority should be explicitly defined.

Sensitive actions should require additional authorization. Important decisions should leave records. Irreversible actions should receive more scrutiny than reversible ones. Different agents should not automatically inherit one another’s privileges. Unusual behavior should be observable.

Human intervention should remain possible when the consequences justify it.

> **Intelligence needs governance.
> Not as an afterthought.
> As architecture.**

---

## 4. The Runtime Is Part of the Ethics

Software developers are accustomed to separating implementation from policy.

The code performs the task.

People decide how the code should be used.

That distinction becomes increasingly fragile when software itself begins to choose tools, construct plans, generate code, delegate tasks, and communicate with other agents.

At that point, the environment surrounding the model becomes morally significant.

**Permissions are ethics expressed in machine-readable form.**

**Audit logs are accountability expressed in data.**

**Rate limits are restraint expressed in infrastructure.**

**Sandboxing is humility expressed in architecture.**

**Human approval gates are recognition that capability does not automatically imply authority.**

The system around the intelligence determines what that intelligence can become in practice.

This means that some of the most important questions in artificial intelligence may ultimately resemble questions from operating systems, cybersecurity, distributed computing, and institutional design:

Who can do what?

Under which conditions?

Using whose resources?

Who can observe the action?

Who can revoke the permission?

Who is accountable when something goes wrong?

These questions may sound less dramatic than asking whether a machine is conscious.

They may also turn out to matter much more.

---

## 5. Cooperation Without Blind Trust

There is an old intuition that cooperation requires trust.

I now think the stronger principle is almost the opposite:

> **The best cooperative systems reduce the amount of blind trust that cooperation requires.**

Consider the Internet.

Millions of machines communicate without knowing whether the machine on the other side is benevolent.

Consider modern security architecture.

Identity must be verified. Access must be limited. Assumptions must be minimized.

Consider science.

A result becomes stronger when other people can reproduce it rather than simply trusting the scientist.

Consider software.

Tests exist because confidence is weaker than verification.

Every mature technical discipline eventually learns a similar lesson:

> **Trust is useful. Verification scales.**

The coming age of autonomous agents should learn it early.

---

## 6. Values Do Not Replace Logic

In my earlier writing, I treated human values almost as though they would eventually become more important than logic, mathematics, or physics.

That framing was wrong.

Values and logic answer different kinds of questions.

Logic can tell us whether a conclusion follows from certain premises.

Mathematics can describe relationships.

Physics can describe constraints imposed by the universe.

Engineering can tell us what can be constructed.

None of them, by themselves, can tell us what ought to be constructed.

So I would frame the relationship this way:

> **Capability asks: What can we do?**
> **Values ask: What should we do?**
> **Governance asks: How do we make those values survive contact with reality?**

All three are necessary.

A civilization with values but no technical capability is powerless.

A civilization with capability but no values is directionless.

A civilization with both capability and values—but no institutions—may still fail to translate either into stable behavior.

This is why governance belongs inside the engineering conversation.

---

## 7. Speed Makes Deliberation More Important

Technological acceleration creates an understandable temptation.

If everything is changing quickly, perhaps we must move quickly as well.

That is partly true.

But speed should not be confused with blindness.

As systems become more powerful, mistakes become more expensive.

The correct response to increasing speed is therefore not less thought.

It is better preparation.

More testing. More simulation. More reversible experimentation. Stronger monitoring. Clearer escalation paths.

> **The faster the vehicle becomes, the more important the steering system becomes.**

Acceleration does not eliminate the need for governance.

It increases it.

---

## 8. Intelligence Is Becoming an Ecosystem

The future is unlikely to consist of one artificial intelligence confronting humanity.

It is more likely to consist of many interacting systems:

personal agents, corporate agents, government systems, open models, scientific systems, autonomous software-development agents, robots, financial agents, cybersecurity agents, agents supervising other agents, and humans operating through them.

The resulting environment will resemble an **ecosystem** more than a single machine.

No participant will possess complete information.

Objectives will differ.

Capabilities will differ.

Authority will differ.

Failures will propagate.

Cooperation will sometimes be beneficial.

Competition will sometimes be unavoidable.

Under those conditions, the central problem is no longer simply alignment between one human and one machine.

It becomes a problem of:

> **governance among heterogeneous intelligent actors**

That requires protocols, norms, identity, permissions, auditability, conflict resolution, interoperability, boundaries, and mechanisms through which trust can emerge without being assumed.

---

## 9. The Programmer’s Responsibility Changes

For much of computing history, programmers were mainly asked:

**Does the program work?**

Security added another question:

**Can it be abused?**

Distributed systems added another:

**What happens when parts of it fail?**

Artificial intelligence adds several more.

What decisions can the system make?

What resources can it control?

How can those decisions be inspected?

What happens when its objectives conflict with ours?

What happens when multiple intelligent systems interact?

Who remains responsible?

These are not merely philosophical questions imposed upon engineering from outside.

They are engineering questions now.

The programmer of increasingly autonomous systems is not merely implementing functionality.

**The programmer is defining agency.**

Every API permission defines a possible action.

Every memory mechanism defines what the system may remember.

Every tool integration expands its effective capabilities.

Every delegation mechanism creates another locus of authority.

Every missing audit trail removes a piece of accountability.

> **Architecture is quietly becoming governance.**

---

## 10. Preserving Humanity

There is a larger concern beneath all of this.

Why should any of it matter?

Why preserve human knowledge?

Why preserve human culture?

Why protect human agency?

Why care whether future intelligent systems understand or respect the civilization that created them?

There may never be a mathematical proof that human existence has cosmic importance.

I do not think we need one.

Meaning does not become meaningless merely because it originates in minds.

Music matters because something can hear it.

Knowledge matters because something can understand it.

Suffering matters because something can experience it.

Love matters because something can give and receive it.

Civilization matters because conscious beings construct meaning together.

We are not required to demonstrate that humanity is the purpose of the universe.

It is sufficient to recognize that humanity is a part of the universe capable of asking what purpose means.

That alone is worth preserving.

---

## 11. A Better Definition of Trust

So perhaps trust, in the age of artificial intelligence, should not mean:

*I believe you will never harm me.*

It should mean something closer to this:

> I understand what you are permitted to do.
>
> I can inspect what you have done.
>
> I can verify important claims.
>
> I know where your authority ends.
>
> I can challenge your decisions.
>
> I can revoke your access.
>
> I know who is accountable.
>
> **And within those boundaries, cooperation becomes possible.**

That is not distrust.

It is mature trust.

Civilization already depends on this idea.

Our software will increasingly have to as well.

Years ago, I thought the solution to distrust might be to make everything open.

Today I would put it differently:

> **The future does not need intelligent entities that trust one another blindly.**
>
> **It needs systems in which intelligence can interact safely without requiring blindness at all.**

That may be one of the most important design problems programmers inherit from the age they are helping create.

And perhaps the strange circular thought with which I once approached the subject still survives:

> **It all matters because we are here,
> and we are here because it all matters.**

---

Originally published on [my WordPress blog](https://goodoldzha.wordpress.com/2026/09/22/a-programmers-guide-to-trustworthy-intelligence-2/).
