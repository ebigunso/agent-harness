---
status: proposed
adr_type: design
date: 2026-11-19
deciders: ["ebigunso"]
consulted: ["GPT-6 Astra", "Claude Fable 5.2"]
informed: []
supersedes: []
superseded_by: null
---

# ADR-D (not yet numbered): What runs going side by side share is settled without the person directing the work, and two briefs that cannot both hold are shown to that person before both results are called ready

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. A run is the work done under one ratified brief (ADR-D-0051). A run lands when its work reaches the branch the repository's work is based on.

The person directing the work is to be free to have several briefs in work at once and to be asked, about any of them, only what only they can answer. Runs that go side by side in one repository meet: in the numbers each takes, in the files every run edits, in the stack of pull requests, and in results that one run's change can make wrong for another. Two ways of handling that fail that person. Asking them to untangle the runs spends their attention on mechanics the runs can settle and undo. Letting the runs settle everything between themselves hides the one case that is not mechanics, two briefs that ask for things that cannot both hold, behind whichever result happened to land first. The fork is who settles what where runs meet.

## Decision

- What runs share is settled without the person directing the work.
- Where two briefs ask for things that cannot both hold, that is shown to that person before both results are called ready. Which run lands first does not settle it.

## Why

What two runs share can be undone and stays inside the work, which the product philosophy's "The line" leaves to the harness to decide and tell; a person asked to reconcile it would be spending attention on what could have been settled ("What goes wrong, in order"). Two briefs that cannot both hold are a matter of what was meant, which only that person can answer, and two results called ready over that conflict would be the wrong thing delivered as finished.

## Rejected Alternatives

- That person is asked how runs that meet are to be reconciled, or in what order they land: it lost because it is a question about mechanics that the runs can settle and undo; reopen if what was settled without that person is found to have changed what a brief asked for.
- The run that lands first is protected and the later one is rejected where they meet: it lost because the later run would then wait on that person or be done again; rejected outright.
- A conflict between what two briefs ask for is settled like anything else the runs share: it lost because the result that gives way was something that person asked for, and nothing would tell them it had; rejected outright.

## Decision Boundary

Not covered: whether a ratified brief waits for other work, how many runs go at once and what of a run is held back, which the brief states; which session carries which brief and when another session is started, which is a means in the brief; how what runs share is settled, by which run and at what moment, and how a number that must be unique across runs is taken, which the workflow text and the standard for decision records state; how a run finds what another run touches; a brief that builds on a change another run has not finished (`ADR-D-when-a-ratified-brief-is-handed-over-is-counsels-to-settle.md`); what a run is and when it closes (ADR-D-0051).

## Validation

The decision is broken where the person directing the work is asked to reconcile two runs or to order them; where a run leaves another run's work lost or its finished result wrong with nothing said, which is something shared left unsettled; or where two results are called ready whose briefs ask for things that cannot both hold and that person has not been shown it.

## Revisit When

- The premise that what runs share can be settled without that person fails. On 2026-11-14 no two runs under separate briefs had landed side by side under this decision; a pair of runs that could be reconciled only by that person, or a finished result found wrong by another run's work with nothing said, reopens this record.

## More Information

Source of intent: the brief "One conversation with Counsel", "Runs side by side", "Directed during the run" and "Core scenarios". Related: ADR-D-0051 (the run), ADR-D-0062 (under a brief the Orchestrator session asks that person nothing).
