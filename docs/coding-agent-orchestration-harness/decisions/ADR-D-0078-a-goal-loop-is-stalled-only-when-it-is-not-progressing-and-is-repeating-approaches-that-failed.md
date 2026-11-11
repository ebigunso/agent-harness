---
status: proposed
adr_type: design
date: 2026-11-11
deciders: ["ebigunso"]
consulted: ["Claude Fable 5", "Claude Fable 5.2"]
informed: []
supersedes: ["ADR-D-0011-single-object-progress-definition.md"]
superseded_by: null
---

# ADR-D-0078: A goal loop is stalled only when it is not progressing and is repeating approaches that failed

## Context and Problem Statement

Terms used here: a goal run is a run in goal mode, in which a loop works toward a stated goal condition. The journal is the run's append-only record of its iterations and their evidence. The gap is the distance left to the goal condition, where the condition yields one that can be counted. A plateau is a stretch of the run in which that count does not move.

A stall stops a goal loop (ADR-D-0074), so what counts as one decides which loops are stopped. Real progress often leaves the count flat, or worse, for a while: diagnosis, building a harness, a refactor midway. The fork is whether a flat count is a stall, or whether a stall is something narrower.

## Decision

- A goal loop is stalled only when three things hold together: the gap to its goal has not moved; nothing credibly links what the loop learned to the goal; and its attempts are going round approaches that already failed.
- No one of the three alone is a stall. A plateau on which the loop is learning toward its goal is progress, however long the count stays flat.

## Why

Plateau work that is real progress must not be stopped as a stall, so a count standing still is not enough to call one. Asking for an explicit argument linking what was learned to the goal puts the plateau question where it can be judged, and lets such work be recognized as progress on its merits instead of being exempted by a looser standard.

## Decision Boundary

Not covered: what a stall triggers (ADR-D-0074); what progress is measured against and how a plateau counts as progress (ADR-D-0077); who judges whether a loop is stalled (ADR-D-0080) and which way doubt resolves (ADR-D-0081); over how many iterations the three are read, how repetition of failed approaches is recognized and what the journal records, all of which goal mode's text states.

## Validation

The decision is broken where:

- a loop was held to be stalled while one of the three did not hold, a flat count with credible learning toward the goal being the case in point;
- a loop in which all three held was not counted as stalled.

## Revisit When

- The premise that the three together separate a stalled loop from a working one no longer holds: trials show the test misfiring systematically, stopping loops that were progressing or passing loops that were not. ADR-D-0011, dated 2026-07-16, names no trial of this premise.

## More Information

Replaces ADR-D-0011 at what counts as a stall; ADR-D-0077 and ADR-D-0079 replace the rest of it. ADR-D-0011 states no alternative for this decision, so this record has no rejected alternatives. Design: `docs/coding-agent-orchestration-harness/design/goal-mode-design.md`.
