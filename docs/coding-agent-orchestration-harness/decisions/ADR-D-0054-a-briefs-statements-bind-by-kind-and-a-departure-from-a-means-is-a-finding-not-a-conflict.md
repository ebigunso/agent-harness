---
status: accepted
adr_type: design
date: 2026-10-04
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1"]
informed: []
supersedes: []
superseded_by: null
depends_on: ["ADR-D-0041-a-ratified-brief-authorizes-a-plan-only-through-a-closed-plan-review-and-a-value-audit-that-holds-nothing-above-the-run.md", "ADR-D-0053-a-design-level-finding-is-escalated-by-the-orchestrator-with-the-part-it-concerns-held.md"]
---

# ADR-D-0054: A brief's statements bind by kind: what the work must give and its constraints bind, a means does not, and a plan that departs from a means is graded on what the means serves, never held as a conflict, and reaches the person directing the work only when it changes what that person would experience

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session the person directing the work opens for value discussion, separate from any Orchestrator session. The Orchestrator session is a session that holds the Orchestrator role (ADR-D-0020) and plans, dispatches and reports the work.

A brief states what the work must give and why, and leaves how to the Orchestrator. In discussion the person directing the work and Counsel often also settle a way of getting there, and writing it down is useful: it is the best way known when the brief was ratified. Written as an ordinary statement, it binds like every other: the audit grades a plan against it, and a plan that found a better way is held for conflicting with the brief. Left out, what was settled is lost. The fork is how a brief carries a way of doing something without that way becoming a requirement.

## Decision

- Each statement of a brief has a kind: something the work must give, a constraint, or a means.
- What the work must give and a constraint bind the run and the audit grades against them as it grades against any statement.
- A means is a way settled in discussion to get what a gives-statement asks for. The run builds from it and may better it. It does not bind.
- An item that follows a means is supported by it, as by any statement.
- An item that departs from a means is graded on the gives-statement the means serves, and the departure is not a conflict between statements and not a want of support.
- A departure from a means is recorded as a finding and read by the test for every finding (ADR-D-0053). One that changes what the person directing the work would experience is escalated with the part held, and reaches that person as a question about the better way, not as a breach. One that changes nothing that person would experience is not raised: the audit grades the item against what the means was for, and that is the end of it.
- A statement with no kind binds, so a brief written without kinds is read with every statement binding.
- The kind is ratified with the statement; nobody but the person directing the work makes a gives-statement or a constraint into a means.

## Why

Someone who settled a way of doing something in discussion wants it used unless a better one turns up, and wants to hear when the change is one that person would notice, not each time the mechanics are refined: binding the run to the first way found would have the work stop at its own improvements, and dropping the way from the brief would throw away what the discussion found. Grading a departure on what the means was for keeps the check on the thing that person actually wants.

## Rejected Alternatives

- Every statement of a brief binds alike: it lost because a better way found during the work is then held as a conflict, and the person directing the work is asked to approve a deviation instead of being shown an improvement; reopen if departures from means are found to be the run avoiding work the brief asked for.
- Means are left out of the brief and kept in the discussion notes: it lost because the audit and the Orchestrator do not rely on the notes, so the settled way would reach the run only as hearsay; reopen if means in briefs are found to constrain plans as if they bound.
- No departure from a means is raised: it lost because a departure can change what that person experiences, and that is that person's to decide; reopen if the departures raised are found to be ones that person consistently waves through unread.
- Every departure from a means is raised, as the brief first stated it: it lost because a mechanical refinement of a means then comes to that person as a decision, which is the step-by-step steering a brief exists to end; reopen if departures the audit graded without raising are found to have changed what that person experienced.
- The audit decides whether a statement is a means from its wording: rejected outright; what binds is that person's to say, and is ratified with the statement.

## Decision Boundary

Invariant: gives-statements and constraints bind; a means supports an item that follows it and never holds an item that departs from it; a departure is raised to the person directing the work only when it changes what that person would experience, and is otherwise settled by its grade; a statement with no kind binds; the Decision list states the rest.

Not covered: the brief's form, its provenance tags and its scenarios, which the document forms state; how a finding is recorded, escalated and compared (ADR-D-0053); the grade names and their definitions, which the audit's mandate owns; the conditions for authorizing a plan (ADR-D-0041); the philosophies, whose statements have no kinds.

## Validation

- The brief form states the three kinds and that an unmarked statement binds.
- The audit's mandate grades a departure from a means on the statement the means serves, not as a conflict or a want of support, and its comparison identifies as bearing on the design only a departure that changes what someone experiences.
- No verdict holds an item solely for departing from a means.

## Revisit When

- Departures from means are found to be the run avoiding work the brief asked for.
- Departures the audit graded without raising are found to have changed what the person directing the work experienced.
- Means in briefs are found treated as binding by plans or by audits.
- On 2026-10-04 one brief carried kinds and one departure from a means had been raised, by hand, before this text existed, and the person directing the work found it too mechanical to have been brought as a decision, which is why only a departure that changes the experience is raised; a verdict that holds an item solely for departing from a means reopens this record.

## More Information

Source of intent: `docs/coding-agent/briefs/active/design-led-long-runs-brief.md`, its kind marks, "What a design is" and "A better design noticed mid-flight". This record fixes nothing the brief states as a means; that an unmarked statement binds is the run's own addition, made so that briefs written before kinds existed read as they did. Related: ADR-D-0053 (findings), ADR-D-0041 (authorization), ADR-D-0052 (the audit).
