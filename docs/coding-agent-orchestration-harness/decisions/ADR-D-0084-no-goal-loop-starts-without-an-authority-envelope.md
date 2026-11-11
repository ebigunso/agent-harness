---
status: proposed
adr_type: design
date: 2026-11-11
deciders: ["ebigunso"]
consulted: ["Claude Opus 5.5", "Claude Fable 5.2"]
informed: []
supersedes: ["ADR-D-0066-a-goal-loops-forbidden-set-is-a-criterion-and-its-envelope-is-fixed-before-the-loop-and-never-changed-by-it.md"]
superseded_by: null
---

# ADR-D-0084: No goal loop starts without an authority envelope

## Context and Problem Statement

Terms used here: a goal loop is the loop of a run in goal mode, which works toward a stated goal condition. The authority envelope is the boundary of a goal loop's autonomy.

A goal loop decides for itself, between the moments at which a human looks at the work, what to attempt and what to change. The fork is whether a loop may start on its goal alone, its limits being worked out as questions arise, or whether the limits of what it may decide are set down before it takes any step.

## Decision

- No goal loop starts without an authority envelope. The envelope is fixed before the loop starts.
- An envelope consists of a decision scope, what the loop may change freely, and a forbidden set.

## Why

A goal loop acts autonomously between human touchpoints, so the boundary of its autonomy has to exist before the loop takes any step: a boundary drawn after the loop has started is drawn after actions it would have bounded.

## Decision Boundary

Not covered: how the forbidden set is defined (ADR-D-0085); whether the loop may change its envelope (ADR-D-0086); who authorizes an envelope and on what conditions (ADR-D-0064, ADR-D-0065); how a decision scope is expressed, how the envelope is recorded and what the loop does at its boundary, which goal mode's text states; what else a goal carries beside its envelope before its loop starts, which goal mode's text states; how a goal run is graded against the value documents (ADR-D-0082).

## Validation

The decision is broken where:

- a goal loop took a step with no envelope fixed for it;
- a loop ran under an envelope that lacked a decision scope or a forbidden set.

## Revisit When

- The premise that the engines running goal loops offer no boundary of their own worth relying on no longer holds: platform engines gain native envelope or boundary primitives worth delegating to. On 2026-09-07 none had.

## More Information

Replaces ADR-D-0066 together with ADR-D-0085 and ADR-D-0086: this record holds that an envelope exists before the loop starts and what it consists of. ADR-D-0066 states no rejected alternative to this decision, so this record has no such section. Design: `docs/coding-agent-orchestration-harness/design/goal-mode-design.md`, "Authority envelope". Related: ADR-D-0073 (the goal lifecycle), ADR-D-0064 and ADR-D-0065 (who authorizes an envelope, and on what conditions).
