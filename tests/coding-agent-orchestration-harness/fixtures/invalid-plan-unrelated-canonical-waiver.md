# Plan: Invalid Unrelated Canonical Waiver Fixture

- status: in_progress
- generated: 2026-05-10
- last_updated: 2026-05-10
- work_type: docs

## Goal
- Validate that an unrelated canonical waiver does not waive UI validation.

## Definition of Done
- Frontend fixture docs are updated.

## Scope / Non-goals
- Scope: fixture only.
- Non-goals: real implementation.

## Context (workspace)
- Related files/areas:
  - `docs/example.md`

## Open Questions (max 3)
- None.

## Assumptions
- None.

Required-check waiver
- What is waived: Package validator execution for this fixture-only plan.
- Why waived now: The fixture validates waiver scope matching and does not need package validation.
- Risk accepted and impact: Package structure issues would not be caught by this fixture.
- Mitigation and follow-up: Run package validation for real package changes.
- Owner and expiration: Orchestrator ; fixture-only test case.

## Tasks

### Task_1: Update frontend fixture docs
- type: docs
- owns:
  - `docs/example.md`
- depends_on: []
- description: |
  Update frontend fixture docs.
- acceptance:
  - Frontend fixture docs are updated.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Review fixture docs."

## Task Waves (explicit parallel dispatch sets)

- Wave 1 (parallel): [Task_1]

## Rollback / Safety
- Revert fixture docs.

## Progress Log (append-only)

- 2026-05-10 00:00 Drafted.

## Decision Log (append-only; re-plans and major discoveries)

- 2026-05-10 00:00 Decision:
  - Fixture created.
