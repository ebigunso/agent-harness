---
status: proposed
adr_type: design
date: 2026-11-19
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.2", "GPT-6 Astra"]
informed: []
supersedes: []
superseded_by: null
---

# ADR-D (not yet numbered): When the person directing the work is told of what needs them follows what waiting costs

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session role that person talks with about what the product does or should do. A run is the work done under one ratified brief. Something needs that person when it waits on that person's word or judgement.

The attention of the person directing the work is to go to what needs them at their own pace, and nothing is to be lost because it waited for them. Several things can come to need that person while they are discussing something else. Telling each thing at the moment it arises breaks into the discussion at the pace of the runs. Keeping everything for a pause lets what is being lost go on being lost. The fork is when something that needs that person is told.

## Decision

- When the person directing the work is told follows what waiting costs: what is being lost is brought at once, by whatever reaches that person, and the rest waits.
- In a discussion Counsel does not break in for what can wait.

## Why

That person's attention is the scarce thing in the product philosophy's "What goes wrong, in order", so it is spent by what waiting would cost and not by the pace of the runs.

## Rejected Alternatives

- Each matter is put to that person in full as soon as it is ready: it lost because that person is made to switch tasks at the pace of the runs and not at their own; reopen if matters that waited are found to have held up work longer than that person would have chosen.

## Decision Boundary

Not covered: by what means something that is being lost is brought to that person; how that person comes to know what waits (`ADR-D-nothing-waits-for-the-person-without-their-knowing.md`); how many of the matters that wait are put at a time and in what order they are taken up (`ADR-D-matters-are-put-to-the-person-one-at-a-time.md`, `ADR-D-the-order-in-which-matters-are-taken-up-is-the-persons-to-choose.md`); what reaches that person at all (`ADR-D-only-what-needs-the-person-reaches-them.md`); a matter Counsel judges severe enough to pause part of the work, which is raised as its own record states (ADR-D-0044); how promptly Counsel answers while runs are starting and reporting.

## Validation

The decision is broken where something that was being lost waited; or where a discussion is broken into for what could wait.

## Revisit When

- The premise that Counsel can tell what is being lost from what can wait fails: something that waited is found to have cost what bringing it at once would have saved, or that person is found interrupted for what could have waited.

## More Information

Source of intent: the brief "One conversation with Counsel", "What reaches him", "Directed during the run" and "Core scenarios". Related: ADR-D-0034 (Counsel), ADR-D-0044 (Counsel's pause), ADR-D-0062 (everything that needs that person reaches them through Counsel).
