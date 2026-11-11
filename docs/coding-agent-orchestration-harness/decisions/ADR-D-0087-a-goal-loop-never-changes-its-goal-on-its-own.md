---
status: proposed
adr_type: design
date: 2026-11-11
deciders: ["ebigunso"]
consulted: ["Claude Fable 5", "Claude Fable 5.2"]
informed: []
supersedes: ["ADR-D-0014-assessor-goal-validity-re-examination.md"]
superseded_by: null
---

# ADR-D-0087: A goal loop never changes its goal on its own

## Context and Problem Statement

Terms used here: a goal run is a run in goal mode, in which a loop works toward a stated goal condition. The goal is what the run is to reach: its condition, with the invariants the condition names as not to be weakened on the way, its scope and its framing. The goal's owner is the person whose goal it is.

A loop working toward a goal can reach it by changing the goal. A run can also learn something that speaks against its goal: a requirement that no longer holds, a condition that no longer measures what was meant. The fork is who may change a goal while its loop runs, and what the loop does with what it learns against it.

## Decision

- A goal loop never re-scopes, reframes or abandons its goal on its own. A change of goal is a decision of the goal's owner.
- The invariants the goal condition names are part of the goal: the loop weakens none of them on its own.
- What a run learns against its goal is surfaced to the owner and never silently acted on.

## Why

A change of goal is a decision about direction, and direction belongs to the goal's owner, never to the loop pursuing the goal. Holding every change of goal for the owner keeps that ownership whole: a change of direction always passes through a person.

## Decision Boundary

Not covered: how the gap to the goal is read and the bar a plateau argument must clear, which the loop may tighten freely and loosens only with the owner's word (ADR-D-0079); the assessor's examination of whether the goal is still worth pursuing, and the challenge that follows its failure (ADR-D-0076); that the loop never changes its authority envelope (ADR-D-0086); who authorizes a goal run (ADR-D-0064, ADR-D-0065); which invariants a goal condition names, the level at which the loop stops, how the owner is reached and what the owner may decide there, all of which goal mode's text states.

## Validation

The decision is broken where:

- a goal's condition, scope or framing changed during a run without its owner's decision;
- an invariant the goal condition names was weakened during a run without its owner's decision;
- a loop abandoned its goal on its own, or acted on what it learned against the goal without surfacing it.

A tightening by the loop of how the gap to the goal is read, or of the bar a plateau argument must clear, does not break it (ADR-D-0079).

## Revisit When

- The premise that a change of a goal is a decision about direction, which belongs to the goal's owner and never to the loop, no longer holds. ADR-D-0014, dated 2026-07-16, names no trial of this premise.

## More Information

Replaces ADR-D-0014 at the loop never changing its goal; ADR-D-0076 replaces the rest of it. ADR-D-0014 states no alternative for this decision, so this record has no rejected alternatives. Design: `docs/coding-agent-orchestration-harness/design/goal-mode-design.md`.
