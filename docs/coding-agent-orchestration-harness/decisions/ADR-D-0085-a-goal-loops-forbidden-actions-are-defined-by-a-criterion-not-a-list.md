---
status: accepted
adr_type: design
date: 2026-11-11
deciders: ["ebigunso"]
consulted: ["Claude Opus 5.5", "Claude Fable 5.2"]
informed: []
supersedes: ["superseded/ADR-D-0066-a-goal-loops-forbidden-set-is-a-criterion-and-its-envelope-is-fixed-before-the-loop--superseded-by-ADR-D-0084.md"]
superseded_by: null
depends_on: ["ADR-D-0084-no-goal-loop-starts-without-an-authority-envelope.md"]
---

# ADR-D-0085: A goal loop's forbidden actions are defined by a criterion, not a list

## Context and Problem Statement

Terms used here: a goal loop is the loop of a run in goal mode. The authority envelope is the boundary of a goal loop's autonomy, and its forbidden set is what the loop may not do on its own (ADR-D-0084).

An envelope has to say which actions are outside it. The fork is how that is expressed: as a list of forbidden actions, or as a criterion each action is judged against, including kinds of action that did not exist when the envelope was written.

## Decision

- The forbidden set is defined by one criterion, not a list: any action that is irreversible or outward-facing is outside the envelope.
- A new kind of action is judged against the criterion.

## Why

A list of forbidden actions is silently incomplete the day a new tool appears, while a criterion keeps judging actions nobody enumerated.

## Rejected Alternatives

- An enumerated forbidden-action list: it lost because a list is incomplete the day a new tool appears; reopen if platforms gain a native, complete action taxonomy the harness can bind to.

## Decision Boundary

Not covered: that an envelope exists before the loop starts and what it consists of (ADR-D-0084); whether the loop may change its envelope (ADR-D-0086); who authorizes an envelope and on what conditions (ADR-D-0064, ADR-D-0065); the kinds of action named as illustrations of the criterion, how a borderline judgement is journaled and what the loop does when an action falls outside the envelope, which goal mode's text states; how a goal run is graded against the value documents (ADR-D-0082).

## Validation

The decision is broken where:

- a goal loop took an irreversible or outward-facing action on its own;
- an action was treated as inside the envelope because no list named it.

## Revisit When

- The criterion is found ambiguous for a recurring kind of action in a way that naming that kind as an illustration does not settle.

## More Information

Replaces ADR-D-0066 together with ADR-D-0084 and ADR-D-0086: this record holds how the forbidden set is defined. Design: `docs/coding-agent-orchestration-harness/design/goal-mode-design.md`, "Authority envelope". Related: ADR-D-0084 (the envelope), ADR-D-0073 (the goal lifecycle, whose test of shape asks that such actions can be kept out of the loop).
