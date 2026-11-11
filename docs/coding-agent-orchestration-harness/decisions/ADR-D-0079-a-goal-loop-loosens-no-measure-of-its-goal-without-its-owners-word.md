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

# ADR-D-0079: A goal loop loosens no measure of its goal without its owner's word

## Context and Problem Statement

Terms used here: a goal run is a run in goal mode, in which a loop works toward a stated goal condition. The goal's owner is the person whose goal it is. The gap is the distance left to the goal condition, where the condition yields one that can be counted. A plateau is a stretch of the run in which that count does not move, and a plateau counts as progress only on an argument that what was learned brings the goal nearer (ADR-D-0077).

A goal run has two measures of its progress: how the gap to the goal is read, and the bar a plateau argument must clear. A loop working toward a goal can appear to near it by measuring it more kindly. The fork is whether the loop may change these measures while it runs, and in which direction.

## Decision

- How the gap to the goal is read, and the bar a plateau argument must clear to count as progress, are part of the goal condition.
- The loop may tighten either freely during the run.
- Loosening either needs the word of the goal's owner: the loop stops and waits for that decision, and a loosening is never made silently.

## Why

The measures are what the loop's progress is judged by, so a loosening of either during a run has to be visible and has to wait for the goal's owner. Holding the guard on the goal condition alone leaves one thing to protect, under a rule plain enough to apply: tighter is free, looser is not.

## Decision Boundary

Not covered: that the loop never changes its goal, the invariants its condition names included (ADR-D-0087); what progress is measured against and that the reading of the gap is settled before the loop starts (ADR-D-0077); that the loop never changes its authority envelope (ADR-D-0086); who judges whether a plateau argument clears the bar (ADR-D-0080); the name of the escalation level at which the loop stops, how the owner is reached, what the owner may decide there, and how the goal file records its measures and a change to them, all of which goal mode's text states.

## Validation

The decision is broken where:

- the way the gap is read, or the bar for a plateau argument, was loosened during a run without the loop stopping for its owner's decision;
- either was loosened silently.

A tightening made by the loop does not break it.

## Revisit When

- The premise that the measures of a goal are something the loop's pursuit of that goal presses on, so that a loosening by the loop cannot be left unseen, no longer holds. ADR-D-0011, dated 2026-07-16, names no trial of this premise.

## More Information

Replaces ADR-D-0011 at the protection of the goal's measures; ADR-D-0077 and ADR-D-0078 replace the rest of it. ADR-D-0011 states no alternative for this decision, so this record has no rejected alternatives. Design: `docs/coding-agent-orchestration-harness/design/goal-mode-design.md`.
