# Plan: Valid Canonical UI Waiver Fixture

- status: in_progress
- generated: 2026-05-10
- last_updated: 2026-05-10
- work_type: docs

## Goal
- Validate that canonical required-check waivers can waive UI validation.

## Definition of Done
- Frontend fixture docs are updated with a canonical waiver.

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
- What is waived: Reviewer-owned UI/E2E evidence for this fixture-only frontend docs plan.
- Why waived now: The fixture validates plan parsing behavior and does not change a real UI.
- Risk accepted and impact: A real visual regression would not be caught by this fixture.
- Mitigation and follow-up: Use real Reviewer-owned E2E evidence for non-fixture UI plans.
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
