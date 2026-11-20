---
status: accepted
adr_type: design
date: 2026-11-19
deciders: ["ebigunso"]
consulted: ["GPT-6 Astra", "Claude Fable 5.2"]
informed: []
supersedes: []
superseded_by: null
---

# ADR-D-0096: Two briefs that cannot both hold are shown to the person directing the work before both results are called ready

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. A run is the work done under one ratified brief (ADR-D-0051). A run lands when its work reaches the branch the repository's work is based on.

The person directing the work is to be free to have several briefs in work at once, and what each brief asked for is to be what is delivered. What runs going side by side share is settled without that person (ADR-D-0113). One case where runs meet is not mechanics: two briefs that ask for things that cannot both hold. Left to the runs to settle like the rest, it is hidden behind whichever result happened to land first. The fork is whether such a conflict is settled between the runs or shown to that person.

## Decision

- Where two briefs ask for things that cannot both hold, that is shown to the person directing the work before both results are called ready. Which run lands first does not settle it.

## Why

Two briefs that cannot both hold are a matter of what was meant, which only that person can answer, and two results called ready over that conflict would be the wrong thing delivered as finished, the first failure in the product philosophy's "What goes wrong, in order".

## Rejected Alternatives

- A conflict between what two briefs ask for is settled like anything else the runs share: it lost because the result that gives way was something that person asked for, and nothing would tell them it had; rejected outright.

## Decision Boundary

Not covered: what runs share, which is settled without that person (ADR-D-0113); how a conflict between two briefs is found, and by which session; how it is put to that person and when (ADR-D-0116); a brief that builds on a change another run has not finished (ADR-D-0115); what a run is and when it closes (ADR-D-0051).

## Validation

The decision is broken where two results are called ready whose briefs ask for things that cannot both hold and the person directing the work has not been shown it.

## Revisit When

- The premise that a conflict between two briefs is seen before both results are called ready fails. On 2026-11-14 no two runs under separate briefs had landed side by side under this decision; two results called ready over a conflict that nothing had shown reopens this record.

## More Information

Source of intent: the brief "One conversation with Counsel", "Runs side by side", "Directed during the run" and "Core scenarios". Related: ADR-D-0051 (the run), ADR-D-0062 (under a brief the Orchestrator session asks that person nothing).
