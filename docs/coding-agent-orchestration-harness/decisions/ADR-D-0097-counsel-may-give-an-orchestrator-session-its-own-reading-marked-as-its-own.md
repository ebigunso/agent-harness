---
status: accepted
adr_type: design
date: 2026-11-19
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1", "Claude Fable 5.2", "GPT-6 Astra"]
informed: []
supersedes: ["superseded/ADR-D-0043-counsel-speaks-to-the-orchestrator-only-in-the-words-of-the-person-directing-the-work--superseded-by-ADR-D-0097.md"]
superseded_by: null
depends_on: ["ADR-D-0034-counsel-is-a-separate-session-at-the-level-of-behaviour-and-decisions.md", "ADR-D-0112-the-persons-word-reaches-an-orchestrator-session-in-it-or-by-counsels-quoted-relay.md"]
---

# ADR-D-0097: Counsel may give an Orchestrator session its own reading of what the person directing the work wants, marked as its own, on a question whose options that person would tell apart

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session role that person talks with about what the product does or should do. The Orchestrator session is a session that holds the Orchestrator role and plans, dispatches and reports the work. A run is the work done under one ratified brief. A reading is Counsel's own account of what that person wants where that person's words do not say it.

Two things are wanted together. The direction of the work stays with the person directing it, because Counsel holds none of that person's authority (ADR-D-0034). And what was meant is what gets built, without that person being brought every point their words left open. Counsel heard the discussion a brief came from, and an Orchestrator session did not. A Counsel that may speak to an Orchestrator session only by quoting serves the first and fails the second: a point the words do not explicitly cover goes to that person, or goes back undecided to a session that then infers it knowing less than Counsel does. A Counsel that answers freely in its own words fails the first, and one that is asked about every small thing ends up managing tasks in place of advising. The fork is whether Counsel may say anything of its own to an Orchestrator session about what is wanted, and what keeps that from becoming direction of the work.

## Decision

- Counsel may give an Orchestrator session its own reading of what the person directing the work wants, marked as its own, when it is asked or when it sees the work departing from what that person said.
- A reading carries none of that person's authority. The Orchestrator session weighs it as it weighs its own inferences. That person is told of it in Counsel's read of the result at closeout, and not at the time it is given.
- A reading that would materially change the intended result, anything that cannot be undone or that reaches outside the work, and anything that person reserved still come to that person.
- A question reaches Counsel only when its options differ in what that person would experience, the test that decides whether a question reaches that person (ADR-D-0059). Where they do not, the call is the Orchestrator's own: Counsel says so to it and gives no answer on the matter.
- This decides what Counsel may answer, and adds nothing to what Counsel is asked.

## Why

A reading marked as Counsel's and weighed as an inference gives an Orchestrator session the better-informed guess without lending it an authority Counsel does not hold, and telling that person of it at closeout is the telling that the product philosophy's "The line" requires of a decision made for someone, at a moment that does not spend their attention on what can still be changed ("What goes wrong, in order"). The test on what is asked is what keeps the session that person talks with at the level of what is wanted: a Counsel that settles how tasks are done is directing the work.

## Rejected Alternatives

- Counsel speaks to an Orchestrator session only in that person's words and gives no reading of its own, as ADR-D-0043 had it: it lost because a point the words do not explicitly cover then costs that person's attention or is inferred by the session that knows least of what was meant; reopen if readings marked as Counsel's are found acted on as that person's decisions.
- Counsel's reading is given unmarked: rejected outright; an Orchestrator session could not tell it from that person's word, and it would claim an authority Counsel does not hold (ADR-D-0034).
- That person is told of each reading at the time it is given: it lost because a reading that can be undone and stays inside the work would then interrupt that person at the pace of the run; reopen if readings told at closeout are found to have changed a result in a way that person would have stopped.
- Counsel answers whatever an Orchestrator session asks: it lost because a Counsel that settles questions whose options that person would never tell apart is deciding tasks; reopen if calls left to the Orchestrator session are found to have been decisions of direction.

## Decision Boundary

Not covered: what Counsel gives as that person's (ADR-D-0100); that Counsel never says how the work is done or in what order, a reading included (ADR-D-0102); where Counsel's advice on direction goes (ADR-D-0103); how a reading is marked and how an Orchestrator session records one; what Counsel's read at closeout holds besides; what counts as a material change to the intended result in a given case, which is judged against the brief; what the Orchestrator escalates and at what level; how a message travels between sessions.

## Validation

The decision is broken where a reading reached an Orchestrator session unmarked, or was acted on there as that person's decision; where a reading was given and that person was not told of it at closeout; where a reading that materially changed the intended result, or touched what cannot be undone, what reaches outside or what that person reserved, was acted on without having come to that person; or where Counsel answered a question whose options do not differ in what that person would experience.

## Revisit When

- The premise that Counsel can give a reading without coming to direct the work fails: Counsel is found answering about tasks, or the questions come often enough that Counsel is in effect directing the work. Nothing had exercised the decision on 2026-11-19.
- The premise that an Orchestrator session weighs a marked reading as it weighs its own inferences fails: one is found to have been acted on as that person's decision.

## More Information

With ADR-D-0100, ADR-D-0102 and ADR-D-0103, replaces ADR-D-0043 in full. Changed here: ADR-D-0043 let nothing of Counsel's own reach an Orchestrator session about the work, and this record lets Counsel give its own reading, marked, on the conditions above. Source of intent: the brief "One conversation with Counsel", "Directed during the run".
