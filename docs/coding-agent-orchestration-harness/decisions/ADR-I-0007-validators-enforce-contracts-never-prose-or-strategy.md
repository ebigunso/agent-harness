---
status: proposed
adr_type: implementation
date: 2026-09-07
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1"]
informed: []
supersedes: ["ADR-I-0003-contract-first-validation-strategy.md"]
superseded_by: null
---

# ADR-I-0007: Validators enforce contracts, required evidence, and completion state, never prose or strategy

## Context and Problem Statement

The harness has to prevent malformed plans and reports, missing validation evidence, unsafe shared-state Git mutations, and false "done" states, and it does so with scripts. Scripts can also be pointed at wording, task decomposition, prompt text, and strategy choices, where they become brittle and start failing on legitimate variation. The fork is where the validator's authority stops.

## Decision

Validators hard-fail malformed contracts (package structure, role maps, plan and task contracts, report contracts), missing required evidence, and unresolved completion state. They never fail on exact prose, task decomposition, prompt wording, or strategy choices; those are reviewer-owned, and a validator may at most warn or explain about them.

## Why

A validator that matches prose fails on every honest rewording and is then loosened or ignored, taking the contract checks down with it; keeping validators on contracts keeps them trustworthy enough to block.

## Rejected Alternatives

- Validate only by human review: rejected outright; false completion and malformed contracts are exactly what humans miss under load.
- Validate transcript or prose behavior: reopen if runtime adapters and reports become generated from one shared source, where exact structural checks become reliable.

## Decision Boundary

Invariant: no validator fails a plan, report, or package on wording, decomposition, or strategy; every hard failure names a contract field, a required evidence item, or a completion-state condition.

Not covered: the default strictness mode and its name, the warning categories, and which fixtures the smoke tests carry, which live in the validation-strictness reference and the scripts.

## Validation

- Smoke tests carry valid and invalid fixtures; every invalid fixture fails on a named contract or evidence condition.
- Review of a validator change asks whether the new failure names a contract field or a wording.

## Revisit When

- Repeated reviewer findings show an advisory check needs to become a hard rule; that moves a condition into the contract, it does not admit prose matching.
- Adapters and reports become generated from a shared source (not the case on 2026-09-07).

## More Information

Replaces ADR-I-0003 in full. Applied by ADR-D-0031 (the completion report is reviewer-verified prose). Reference: `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/validation-strictness.md`.
