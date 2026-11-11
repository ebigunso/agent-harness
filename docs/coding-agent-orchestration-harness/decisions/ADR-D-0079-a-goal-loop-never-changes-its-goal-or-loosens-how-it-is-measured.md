---
status: proposed
adr_type: design
date: 2026-11-11
deciders: ["ebigunso"]
consulted: ["Claude Fable 5", "Claude Fable 5.2"]
informed: []
supersedes: ["ADR-D-0011-single-object-progress-definition.md", "ADR-D-0014-assessor-goal-validity-re-examination.md"]
superseded_by: null
---

# ADR-D-0079: A goal loop never changes its goal or loosens how it is measured

## Context and Problem Statement

Terms used here: a goal run is a run in goal mode, in which a loop works toward a stated goal condition. The goal's owner is the person whose goal it is. The gap is the distance left to the goal condition, where the condition yields one that can be counted. A plateau is a stretch of the run in which that count does not move, and a plateau counts as progress only on an argument that what was learned brings the goal nearer (ADR-D-0077).

A loop working toward a goal can reach it by changing the goal, or by measuring it more kindly. A run can also learn something that speaks against its goal. The fork is who may change a goal, and how it is measured, while its loop runs.

## Decision

- A goal loop never re-scopes, reframes or abandons its goal on its own. A change of goal is a decision of the goal's owner. What a run learns against its goal is surfaced to the owner and never silently acted on.
- How the gap to the goal is read, and the bar a plateau argument must clear to count as progress, are part of the goal condition. The loop may tighten either freely during the run. Loosening either is a change of the goal: the loop stops and waits for the owner's decision, and the change is never made silently.

## Why

A change of goal is a decision about direction, and direction belongs to the goal's owner, never to the loop pursuing the goal. Loosening how the goal is measured weakens the goal itself, so it is held to the same rule and has to be visible, and holding the guard on the goal condition alone leaves one thing to protect.

## Decision Boundary

Not covered: the assessor's examination of whether the goal is still worth pursuing, and the challenge that follows its failure (ADR-D-0076); that the loop never changes its authority envelope (ADR-D-0086); what progress is measured against (ADR-D-0077); who authorizes a goal run (ADR-D-0064, ADR-D-0065); the name of the escalation level at which the loop stops, how the owner is reached, what the owner may decide there, and how the goal file records its measures and a change to them, all of which goal mode's text states.

## Validation

The decision is broken where:

- a goal's condition, scope or framing changed during a run without its owner's decision;
- the way the gap is read, or the bar for a plateau argument, was loosened during a run without the loop stopping for its owner, or was changed silently.

## Revisit When

- The premise that a change of a goal is a decision about direction, which belongs to the goal's owner and never to the loop, no longer holds. ADR-D-0011 and ADR-D-0014, both dated 2026-07-16, name no trial of this premise.

## More Information

Replaces ADR-D-0011 at the protection of the goal's measures, and ADR-D-0014 at the loop never changing its goal; ADR-D-0077 and ADR-D-0078 replace the rest of ADR-D-0011, and ADR-D-0076 the rest of ADR-D-0014. Neither ADR-D-0011 nor ADR-D-0014 states an alternative for this decision, so this record has no rejected alternatives. Design: `docs/coding-agent-orchestration-harness/design/goal-mode-design.md`.
