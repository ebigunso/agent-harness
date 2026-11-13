---
status: accepted
adr_type: design
date: 2026-11-11
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1", "Claude Fable 5.2"]
informed: []
supersedes: ["superseded/ADR-D-0029-the-optimizer-never-judges-its-own-continuation--superseded-by-ADR-D-0080.md"]
superseded_by: null
---

# ADR-D-0081: A goal loop whose continuation the evidence does not justify stops and escalates

## Context and Problem Statement

Terms used here: a goal run is a run in goal mode, in which a loop works toward a stated goal condition. The journal is the run's append-only record of its iterations and their evidence.

A judgement of whether a goal loop continues is often made on evidence that settles nothing: the run has neither clearly progressed nor clearly stalled. Whoever judges needs a rule for that case, and the two errors open to it are not alike. The fork is which side carries the burden of proof: continuing, or stopping.

## Decision

Continuation bears the burden of proof. Where the run's evidence does not justify continuing, the judgement is to stop and escalate to a human; a judgement that could go either way goes against continuing. This binds whoever judges a goal loop's continuation.

## Why

A wrong stop costs one human touch, while a wrong continuation compounds. The doubtful case is therefore resolved toward the error that is cheap and seen at once.

## Decision Boundary

Not covered: who judges continuation (ADR-D-0080); what progress is measured against and what counts as a stall (ADR-D-0077, ADR-D-0078); the level at which the loop escalates and how the question reaches the human, which goal mode's text states.

## Validation

The decision is broken where a loop continued on a judgement whose evidence did not justify continuing, or a judgement treated the absence of proof of a stall as a reason to continue.

## Revisit When

- The premise that a wrong stop costs one human touch while a wrong continuation compounds no longer holds.

## More Information

Replaces ADR-D-0029 at which way an unsettled judgement falls; ADR-D-0080 replaces it at who judges continuation. Related: ADR-D-0074 (the stall rule). Design: `docs/coding-agent-orchestration-harness/design/goal-mode-design.md`, pillar 4.
