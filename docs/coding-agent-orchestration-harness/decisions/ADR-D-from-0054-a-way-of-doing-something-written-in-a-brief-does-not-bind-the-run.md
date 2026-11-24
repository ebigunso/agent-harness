---
status: proposed
adr_type: design
date: 2026-11-24
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1", "Claude Fable 5.2"]
informed: []
supersedes: ["ADR-D-0054-a-briefs-statements-bind-by-kind-and-a-departure-from-a-means-is-a-finding-not-a-conflict.md"]
superseded_by: null
---

# ADR-D-XXXX: A way of doing something written in a brief does not bind the run; what the work must give and its constraints do

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session role that person talks with about what the product does or should do. A brief is the ratified statement of what one piece of work must give and why. A run is the work done under one ratified brief. The value audit is the independent grading of a run's plan and result against the value documents, which are the brief and the philosophies. An item is one thing of a plan or a result that the audit grades.

A brief states what the work must give and why, and leaves how to those doing the work. In discussion the person directing the work and Counsel often also settle a way of getting there, and that person wants it used unless a better one turns up: it is the best way known when the brief is ratified. Written as a statement like any other, it binds like any other: the audit grades a plan against it, and a plan that found a better way is held for going against the brief. Left out, what the discussion settled is lost. The fork is how a brief carries a way of doing something without that way becoming a requirement.

## Decision

- A statement of a brief has a kind, which says how it binds: it is something the work must give, or a constraint that holds regardless, or a means, which is a way settled in discussion to get what the work must give.
- What the work must give and a constraint bind the run, and the audit grades against them as it grades against any statement.
- A means does not bind. The run builds from it and may better it.
- An item that follows a means is supported by it, as by any statement.
- An item that departs from a means is judged on what the means serves, the thing the work must give. The departure is by itself no ground for holding the item: it does not put the item against the brief, and it does not leave the item without support.
- A departure from a means is recorded as a finding and read by the test for every finding (`ADR-D-from-0053-a-finding-that-would-change-what-someone-experiences-reaches-the-person-at-once.md`). One that changes what the person directing the work would experience is escalated with the part it concerns held, as that record states, and reaches that person as a question about the better way, not as a breach. One that changes nothing that person would experience is not raised: the audit grades the item against what the means was for, and that is the end of it.
- A statement with no kind binds, so a brief written without kinds is read with every statement binding.
- The kind is ratified with the statement. Nobody but the person directing the work makes something the work must give, or a constraint, into a means.

## Why

The engineering philosophy's "What it aspires to" has what someone meets settled before the means: "The two are kept apart so that either can change without the other." Someone who settled a way of doing something in discussion wants it used unless a better one turns up, and wants to hear when the change is one that person would notice, not each time the mechanics are refined, which is the failure the product philosophy's "What goes wrong, in order" names "The person's attention, spent on what could have been settled": binding the run to the first way found would have the work stop at its own improvements, and dropping the way from the brief would throw away what the discussion found. Judging a departure on what the means was for keeps the check on the thing that person actually wants. A statement with no kind binds so that a brief written without kinds reads as it did when it was ratified.

## Rejected Alternatives

- Every statement of a brief binds alike: it lost because a better way found during the work is then held as going against the brief, and the person directing the work is asked to approve a deviation instead of being shown an improvement; reopen if departures from means are found to be the run avoiding work the brief asked for.
- Means are left out of the brief and kept in the notes of the discussion: it lost because the audit and the Orchestrator do not rely on the notes, so the settled way would reach the run only as hearsay; reopen if means in briefs are found to constrain plans as if they bound.
- No departure from a means is raised: it lost because a departure can change what that person experiences, and that is that person's to decide; reopen if the departures raised are found to be ones that person consistently waves through unread.
- Every departure from a means is raised: it lost because a mechanical refinement of a means then comes to that person as a decision, which is the step-by-step steering a brief exists to end; reopen if departures the audit graded without raising are found to have changed what that person experienced.
- The audit decides whether a statement is a means from its wording: rejected outright; what binds is that person's to say, and is ratified with the statement.

## Decision Boundary

Not covered: the test by which a finding is read, how one is escalated and its part held, and the audit's comparison of the reading (`ADR-D-from-0053-a-finding-that-would-change-what-someone-experiences-reaches-the-person-at-once.md`); the audit itself and what its grades hold (ADR-D-0052); the conditions for authorizing a plan (ADR-D-0065); the philosophies, whose statements have no kinds; how a kind is marked on a statement, the brief's form, its provenance tags and its scenarios; the names of the audit's grades and of the reasons it gives for them, and how a departure is noted in a verdict, all of which the plugin's text states.

## Validation

The decision is broken where:

- an item was held solely for departing from a means;
- an item that departed from a means was let through without being judged on what the means serves;
- something the work must give, or a constraint, was treated by a run or by an audit as open to bettering, or a statement with no kind was read as a means;
- a means was treated by a plan or by an audit as binding;
- a departure from a means that changed what the person directing the work would experience did not reach that person, or reached that person as a breach to approve;
- a departure that changed nothing that person would experience was brought to that person as a decision;
- a statement ratified as something the work must give, or as a constraint, became a means without that person's word.

## Revisit When

- Departures from means are found to be the run avoiding work the brief asked for.
- Departures the audit graded without raising are found to have changed what the person directing the work experienced.
- Means in briefs are found treated as binding by plans or by audits.
- On 2026-10-04 one brief carried kinds and one departure from a means had been raised, by hand, before this text existed, and the person directing the work found it too mechanical to have been brought as a decision, which is why only a departure that changes the experience is raised; a verdict that holds an item solely for departing from a means reopens this record.

## More Information

Replaces ADR-D-0054 in full; accepted together with `ADR-D-from-0053-a-finding-that-would-change-what-someone-experiences-reaches-the-person-at-once.md`, which states the test for a finding and what follows from its reading. Source of intent: `docs/coding-agent/briefs/completed/design-led-long-runs-brief.md`, its kind marks, "What a design is" and "A better design noticed mid-flight". This record decides nothing that brief states as a means; that a statement with no kind binds is not from that brief. Related: ADR-D-0065 (authorization), ADR-D-0052 (the value audit).
