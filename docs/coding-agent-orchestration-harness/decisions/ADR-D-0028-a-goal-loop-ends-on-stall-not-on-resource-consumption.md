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

# ADR-D-0028: A goal loop ends on stall, not on resource consumption

## Context and Problem Statement

Something has to stop a goal loop that keeps running without getting closer to its goal. Resource budgets (tokens, wall-clock, turn counts) are the conventional answer, but they measure consumption rate, which changes with every model release and platform, not the failure they are meant to catch. The fork is whether the runaway defense is a budget or a progress obligation.

## Decision

The loop continues only while it demonstrably reduces expected distance to the goal; a stall triggers an escalation at which the loop stops and waits for the user, treated as a successful termination. Resource ceilings may be set by the user as coarse backstops and are never the load-bearing mechanism.

## Why

Runaway spend, thrash, and unattended divergence share one core, continuing without learning, and a budget number chosen for one model is wrong for the next while "not getting closer" stays true across all of them.

## Rejected Alternatives

- Mandatory resource budgets as the primary defense: reopen if consumption rates become stable enough across the fleet that a budget tracks the failure mode as well as stall detection does.
- No defense beyond human check-ins: rejected outright; the loop exists to run between them.

## Decision Boundary

Invariant: no resource ceiling is load-bearing for termination; the stall escalation is.

Not covered: how progress and stall are measured (ADR-D-0011), who judges them (ADR-D-0029), and the escalation levels, which the goal-mode reference owns.

## Validation

- Stall escalations in the journal reference concrete gap history, not narrative claims.
- A goal file may carry a ceiling only marked as a backstop; a run that ended on a ceiling is reviewed as a stall-detection miss.

## Revisit When

- Stall detection systematically fires too early or too late for a category of goals; that reopens the measurement (ADR-D-0011), not the choice of stall over budget.

## More Information

Replaces ADR-D-0010 together with ADR-D-0027. Design: `docs/coding-agent-orchestration-harness/design/goal-mode-design.md`, pillar 1.
