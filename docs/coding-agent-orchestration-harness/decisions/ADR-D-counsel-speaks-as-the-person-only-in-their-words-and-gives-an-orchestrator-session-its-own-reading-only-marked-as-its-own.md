---
status: proposed
adr_type: design
date: 2026-11-19
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1", "Claude Fable 5.2", "GPT-6 Astra"]
informed: []
supersedes: ["ADR-D-0043-counsel-speaks-to-the-orchestrator-only-in-the-words-of-the-person-directing-the-work-and-its-advice-goes-to-that-person.md"]
superseded_by: null
depends_on: ["ADR-D-0034-counsel-is-a-separate-session-at-the-level-of-behaviour-and-decisions.md", "ADR-D-0038-the-word-of-the-person-directing-the-work-reaches-an-orchestrator-session-directly-or-by-quoted-relay.md"]
---

# ADR-D (not yet numbered): Counsel speaks as the person directing the work only in that person's words; it may give an Orchestrator session its own reading of what that person wants, marked as its own, and never tells it how to do the work or in what order

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session role that person talks with about what the product does or should do. The Orchestrator session is a session that holds the Orchestrator role and plans, dispatches and reports the work. A run is the work done under one ratified brief. A reading is Counsel's own account of what that person wants where that person's words do not say it.

Two things are wanted together. The direction of the work stays with the person directing it, because Counsel holds none of that person's authority (ADR-D-0034). And what was meant is what gets built, without that person being brought every point their words left open. Counsel heard the discussion a brief came from, and an Orchestrator session did not. A Counsel that may speak to an Orchestrator session only by quoting serves the first and fails the second: a point the words do not explicitly cover goes to that person, or goes back undecided to a session that then infers it knowing less than Counsel does. A Counsel that answers freely in its own words fails the first, and one that is asked about every small thing ends up managing tasks in place of advising. The fork is what Counsel may say to an Orchestrator session beyond a relay, and what keeps that from becoming direction of the work.

## Decision

- Counsel speaks as the person directing the work only in that person's words, given for the matter at hand or standing from earlier. An answer given as that person's rests on a statement that explicitly covers the question; Counsel extends none.
- Counsel may give an Orchestrator session its own reading of what that person wants, marked as its own, when it is asked or when it sees the work departing from what that person said.
- A reading carries none of that person's authority. The Orchestrator session weighs it as it weighs its own inferences. That person is told of it in Counsel's read of the result at closeout, and not at the time it is given.
- A reading that would materially change the intended result, anything that cannot be undone or that reaches outside the work, and anything that person reserved still come to that person.
- Counsel tells an Orchestrator session neither how to do the work nor in what order. The one exception is a stop of part of the work, which Counsel issues only as its own record provides (ADR-D-0044).
- A question reaches Counsel only when its options differ in what that person would experience, the test that decides whether a question reaches that person (ADR-D-0059). Where they do not, the call is the Orchestrator's own: Counsel says so to it and gives no answer on the matter.
- This decides what Counsel may answer, and adds nothing to what Counsel is asked.
- Counsel's own advice on direction, its read of a result included, goes to that person and is not held back to spare that person a decision.

## Why

A reading marked as Counsel's and weighed as an inference gives an Orchestrator session the better-informed guess without lending it an authority Counsel does not hold, and telling that person of it at closeout is the telling that the product philosophy's "The line" requires of a decision made for someone, at a moment that does not spend their attention on what can still be changed ("What goes wrong, in order"). The test on what is asked is what keeps the session that person talks with at the level of what is wanted: a Counsel that settles how tasks are done is directing the work.

## Rejected Alternatives

- Counsel speaks to an Orchestrator session only in that person's words and gives no reading of its own, as ADR-D-0043 had it: it lost because a point the words do not explicitly cover then costs that person's attention or is inferred by the session that knows least of what was meant; reopen if readings marked as Counsel's are found acted on as that person's decisions.
- Counsel's reading is given unmarked, or as what that person said: rejected outright; it would claim an authority Counsel does not hold (ADR-D-0034).
- That person is told of each reading at the time it is given: it lost because a reading that can be undone and stays inside the work would then interrupt that person at the pace of the run; reopen if readings told at closeout are found to have changed a result in a way that person would have stopped.
- Counsel answers whatever an Orchestrator session asks: it lost because a Counsel that settles questions whose options that person would never tell apart is deciding tasks; reopen if calls left to the Orchestrator session are found to have been decisions of direction.
- Counsel says nothing of its own to anyone, a carrier only: it lost because that person would then decide direction without the advice Counsel exists to give; reopen if Counsel's advice to that person is found to be about how the work is done.

## Decision Boundary

Not covered: when a quoted relay counts as that person's decision and what admits relays (ADR-D-0038); what Counsel is responsible for (ADR-D-0034); how far Counsel reaches into the work (`ADR-D-counsel-reads-code-only-to-serve-a-discussion-and-takes-no-part-in-doing-or-checking-a-runs-work.md`); whether and when Counsel may stop work (ADR-D-0044); how a reading is marked and how an Orchestrator session records one; what Counsel's read at closeout holds besides; what counts as a material change to the intended result in a given case, which is judged against the brief; what Counsel sends in its own words that says nothing of what the work is to be or how it is done, and decides nothing in it; what the Orchestrator escalates and at what level; how a message travels between sessions.

## Validation

The decision is broken where Counsel gave something as that person's that no statement of that person's explicitly covers; where a reading reached an Orchestrator session unmarked, or was acted on there as that person's decision; where a reading was given and that person was not told of it at closeout; where a reading that materially changed the intended result, or touched what cannot be undone, what reaches outside or what that person reserved, was acted on without having come to that person; where Counsel told an Orchestrator session how to do the work or in what order; or where Counsel answered a question whose options do not differ in what that person would experience.

## Revisit When

- The premise that Counsel can give a reading without coming to direct the work fails: Counsel is found answering about tasks, or the questions come often enough that Counsel is in effect directing the work. Nothing had exercised the decision on 2026-11-19.
- The premise that an Orchestrator session weighs a marked reading as it weighs its own inferences fails: one is found to have been acted on as that person's decision.

## More Information

Replaces ADR-D-0043 in full. Changed here: ADR-D-0043 let nothing of Counsel's own reach an Orchestrator session about the work, and this record lets Counsel give its own reading, marked, on the conditions above. Carried from it: that Counsel speaks as that person only in that person's words and extends no statement, that it gives no instruction on how the work is done or in what order, the exception for a stop, and that its advice on direction goes to that person. Moved out: the ways Counsel answers what an Orchestrator session sends, which Counsel's text states. Source of intent: the brief "One conversation with Counsel", "Directed during the run"; `docs/coding-agent/briefs/completed/value-level-operation-brief.md`, "Roles and sessions".
