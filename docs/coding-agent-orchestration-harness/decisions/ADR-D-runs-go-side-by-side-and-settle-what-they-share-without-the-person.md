---
status: proposed
adr_type: design
date: 2026-11-14
deciders: ["ebigunso"]
consulted: ["GPT-6 Astra", "Claude Fable 5.2"]
informed: []
supersedes: []
superseded_by: null
---

# ADR-D (not yet numbered): A ratified brief does not wait for the runs in progress; runs go side by side, and what they share is settled without the person directing the work

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session role that person talks with about what the product does or should do. A run is the work done under one ratified brief (ADR-D-0051). A run lands when its work reaches the branch the repository's work is based on.

Until 2026-11-12 a brief handed over while another run was in progress waited for that run. Letting two runs go at once in one repository removes the wait and makes them meet: in the numbers each takes, in the files every run edits, in the stack of pull requests, and in results that one run's change can make wrong for the other. The fork is whether a ratified brief queues behind the work in progress, and, if it does not, who untangles the runs where they meet.

## Decision

- A brief ratified while other runs are in progress does not wait for them.
- How many runs go at once is the harness's to decide. The harness may hold part of a run back where running it at that moment would collide with another run or slow all of them; that is its decision and no question to the person directing the work, and it is not a bound on what the work may cost.
- What two runs share is settled without that person, by the run that lands later, which brings its own work onto what landed first.
- Each run keeps the other runs' work intact, a run validates the revision it delivers, and no run silently makes another's finished result wrong.
- Where two briefs ask for things that cannot both hold, that is shown to that person before both results are called ready. Which run lands first does not settle it.

## Why

That person said on 2026-11-12: "What I want, is the freedom to ask for anything at any moment, and barring machine capability limits, I am free of bottle necks. The best outcome is where I am the bottle neck, not the machinery", and on 2026-11-11: "The pain is the wait before a brief starts." Runs that needed that person to untangle them would only move the wait from the start of a brief to its end, and what two runs share can be undone and stays inside the work, which the product philosophy's "The line" leaves to the harness to decide and tell. Two briefs that cannot both hold are a matter of what was meant, which only that person can answer. Of how many go at once that person said on 2026-11-12: "The harness can decide here".

## Rejected Alternatives

- A ratified brief waits until the run in progress has finished: it lost because the wait is spent on the machinery and not on anything that person has to say or judge; reopen if runs side by side are found to deliver results that are wrong because of each other more often than a queue would have delayed them.
- That person is asked how runs that meet are to be reconciled, or in what order they land: it lost because it is a question about mechanics that the runs can settle and undo; reopen if what the later run settled is found to have changed what an earlier brief asked for.
- The run that lands first is protected and the later one is rejected where they meet: it lost because the later run would then wait on that person or be done again; rejected outright.

## Decision Boundary

Not covered: how a run finds what another run touches, and what each tells Counsel on taking a brief; how the later run brings its work onto the earlier, and how a number that must be unique across runs is taken, which the workflow text and the standard for decision records state; which session does each run's work, which is a means in the brief; a brief that builds on a change another run has not finished, which is held (`ADR-D-when-a-ratified-brief-is-handed-over-is-counsels-to-settle.md`); whether anything bounds how many runs go at once, where the default is that nothing does: a default that could change with this record standing, which the workflow text states (the `orchestration-harness` value-level operation reference, Runs Side By Side); what happens when the machine's limit for a period is reached; how money is handled in a goal run; what a run is and when it closes (ADR-D-0051).

## Validation

The decision is broken where a ratified brief that builds on nothing unfinished starts only after another run has ended; where the person directing the work is asked to reconcile two runs, to order them, or to say how many may go; where a run delivers a revision it did not validate, or leaves another run's finished result wrong without saying so; or where two results are called ready whose briefs ask for things that cannot both hold and that person has not been shown it.

## Revisit When

- The premise that the run landing later can bring its work onto what landed first without that person fails. On 2026-11-14 no two runs under separate briefs had landed side by side under this decision; a pair of runs that could be reconciled only by that person, or a finished result found wrong by another run's work with nothing said, reopens this record.

## More Information

Source of intent: the brief "One conversation with Counsel", "Who it is for and why", "Runs side by side" and "Core scenarios". Related: ADR-D-0051 (the run), ADR-D-0062 (under a brief the Orchestrator session asks that person nothing).
