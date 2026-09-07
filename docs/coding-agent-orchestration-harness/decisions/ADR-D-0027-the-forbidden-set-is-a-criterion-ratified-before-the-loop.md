---
status: proposed
adr_type: design
date: 2026-09-07
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1"]
informed: []
supersedes: ["ADR-D-0010-authority-envelope-and-progress-obligation.md"]
superseded_by: null
---

# ADR-D-0027: A goal loop's forbidden set is a criterion, ratified before the loop and immutable during it

## Context and Problem Statement

A goal-mode loop acts autonomously between human touchpoints, so the boundary of its autonomy has to exist before the first iteration. The fork is how the boundary is expressed: as a list of forbidden actions, which rots as tools and action types appear, or as a criterion new actions are judged against; and when it may change.

## Decision

Every goal is accepted only with a user-ratified authority envelope: a decision scope (paths, components, operation classes the loop may change freely) and a forbidden set defined by one criterion, not a list: any action that is irreversible or outward-facing is outside the envelope, and a new action type is judged against the criterion. The envelope is recorded in the goal file and is immutable during the run; renegotiating it is a human moment, never a loop decision.

## Why

A list is silently incomplete the day a new tool appears, and an envelope the loop may amend is not a boundary; the criterion keeps judging actions nobody enumerated, and immutability keeps the judgment out of the optimizer's hands.

## Rejected Alternatives

- An enumerated forbidden-action list: reopen if platforms gain a native, complete action taxonomy the harness can bind to.
- Envelope renegotiation by the loop with journaling: rejected outright; the party under goal pressure would be widening its own permissions.

## Decision Boundary

Invariant: the forbidden set is a criterion; the envelope is ratified by the user before the loop starts and does not change during the run.

Not covered: the example action classes named as illustrations, the goal-file format, how borderline judgments are journaled, and what happens at the boundary (escalation levels), which the goal-mode reference owns.

## Validation

- Every goal file carries scope and the forbidden-set acknowledgment before the loop starts.
- A forbidden-class action taken autonomously is a critical defect at retrospective; envelope changes mid-run are envelope violations.

## Revisit When

- Trials show the criterion is ambiguous for a recurring action class; that class is then named as an illustration, and the criterion stays.
- Platform engines gain native envelope or boundary primitives worth delegating to (none on 2026-09-07).

## More Information

Replaces ADR-D-0010 together with ADR-D-0028. Design: `docs/coding-agent-orchestration-harness/design/goal-mode-design.md`, pillar 1. Progress and stall: ADR-D-0011, ADR-D-0028. Who judges: ADR-D-0029.
