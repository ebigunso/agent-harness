---
status: proposed
adr_type: design
date: 2026-11-11
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1", "Claude Fable 5.2"]
informed: []
supersedes: ["ADR-D-0029-the-optimizer-never-judges-its-own-continuation.md"]
superseded_by: null
---

# ADR-D-0080: Whether a goal loop continues is judged by a party other than the optimizer

## Context and Problem Statement

Terms used here: a goal run is a run in goal mode, in which a loop works toward a stated goal condition. The optimizer is the agent pursuing the goal. The journal is the run's append-only record of its iterations and their evidence.

A goal loop must repeatedly decide whether it is still making progress and whether to continue or escalate. The agent pursuing the goal is under goal pressure, and any criterion loose enough to need judgement gives it room to rationalize continuing. The fork is who makes the continuation judgement: the optimizer itself, a mechanical check over the journal, or an independent party.

## Decision

- Whether a goal loop continues is judged by an independent assessor, a party other than the optimizer. The optimizer never judges its own continuation.
- The assessor is charged with the accuracy of its assessment, not with the goal being reached.
- The assessor forms its judgement from the run's recorded evidence and never from the optimizer's working context. What the optimizer reports about its own progress is not evidence: the assessor establishes for itself how far the run stands from its goal.

## Why

The agent pursuing a goal is under pressure to reach it, and any criterion loose enough to need judgement gives it room to rationalize continuing. The one party that cannot be trusted to weigh a stop against a continuation is the one whose work would stop, so the judgement goes to a party that has no stake in the goal and does not inherit the optimizer's view of the run.

## Rejected Alternatives

- Self-assessment by the optimizer against well-defined criteria: it lost because the conflicted party sits in the judge's seat; rejected outright.
- Mechanical stall detection over journal labels the optimizer writes itself: it lost because wording drift defeats matching over such labels; reopen if journals gain machine-verified structure that wording drift cannot defeat.

## Decision Boundary

Not covered: which way the judgement falls where the evidence does not settle it (ADR-D-0081); what progress is measured against and what counts as a stall (ADR-D-0077, ADR-D-0078); the assessor's examination of whether the goal is still worth pursuing (ADR-D-0076); how the assessor is packaged (ADR-D-0050); the inputs the assessor reads, how it establishes the distance to the goal, how it judges circling and progress claimed on a plateau, its cadence, the form of its verdict and the wording of its dispatch, all of which goal mode's text states.

## Validation

The decision is broken where:

- the optimizer decided, or recorded a verdict on, its own continuation;
- a continuation verdict rests on figures the optimizer reported, or on the optimizer's working context;
- the party judging continuation is answerable for the goal being reached.

## Revisit When

- Platform evaluator hooks become expressive enough to host a judgement of a run's whole trajectory natively. None did on 2026-09-07.

## More Information

Replaces ADR-D-0029 at who judges continuation; ADR-D-0081 replaces it at which way an unsettled judgement falls. Related: ADR-D-0074 (the stall rule), ADR-D-0073 (the goal lifecycle). Design: `docs/coding-agent-orchestration-harness/design/goal-mode-design.md`, pillar 4.
