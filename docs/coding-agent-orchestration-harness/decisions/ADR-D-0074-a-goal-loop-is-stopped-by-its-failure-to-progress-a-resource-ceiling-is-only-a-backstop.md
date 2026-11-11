---
status: proposed
adr_type: design
date: 2026-11-11
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1", "Claude Fable 5.2"]
informed: []
supersedes: ["ADR-D-0028-a-goal-loop-ends-on-stall-not-on-resource-consumption.md"]
superseded_by: null
---

# ADR-D-0074: A goal loop is stopped by its failure to progress; a resource ceiling is only a backstop

## Context and Problem Statement

Something has to stop a goal loop that keeps running without getting closer to its goal. Resource budgets (tokens, wall-clock time, turn counts) are the conventional answer, but they measure the rate of consumption, which changes with every model release and platform, and not the failure they are meant to catch. The fork is whether the defence against a runaway loop is a budget or an obligation to progress.

## Decision

- A goal loop continues only while it demonstrably reduces its expected distance to the goal.
- A stall triggers an escalation at which the loop stops and waits for the user. Stopping there is a successful termination.
- The user may set resource ceilings as coarse backstops. No ceiling is the mechanism relied on to stop a loop that is not progressing.

## Why

Runaway spend, thrash and unattended divergence share one core, continuing without learning; a budget number chosen for one model is wrong for another, while "not getting closer" stays true across all of them.

## Rejected Alternatives

- Mandatory resource budgets as the primary defence: it lost because a budget measures the rate of consumption and not the failure; reopen if consumption rates become stable enough across models and platforms that a budget tracks the failure as well as stall detection does.
- No defence beyond a person's check-ins: rejected outright; the loop exists to run between them.

## Decision Boundary

Invariant: no resource ceiling is load-bearing for termination; the stall escalation is.

Not covered: how progress and stall are measured (ADR-D-0011), who judges them (ADR-D-0029), and the escalation levels, the kinds of ceiling and how one is recorded, which goal mode's text states.

## Validation

- Stall escalations in the journal refer to the concrete history of the gap, not to narrative claims.
- A goal file carries a ceiling only marked as a backstop; a run that ended on a ceiling is reviewed as a miss of stall detection.

## Revisit When

- The premise that the rate at which a loop consumes resources differs from one model and platform to another, so that no budget number tracks the failure, no longer holds. The record of 2026-09-08 names no models checked.
- Stall detection firing systematically too early or too late for a category of goals does not reopen this record; it reopens the measurement (ADR-D-0011).

## More Information

Replaces ADR-D-0028 in full. Design: `docs/coding-agent-orchestration-harness/design/goal-mode-design.md`, the section on the authority envelope.
