# Plan: Invalid Fixture

- status: in_progress
- generated: 2026-05-09
- last_updated: 2026-05-09
- work_type: docs

## Goal
- Validate missing owner failure.

## Definition of Done
- Task fails validation.

## Scope / Non-goals
- Scope: fixture only.
- Non-goals: real implementation.

## Tasks

### Task_1: Update fixture docs
- type: docs
- owns:
  - `docs/example.md`
- depends_on: []
- description: |
  Update fixture docs.
- acceptance:
  - Fixture docs are updated.
- validation:
  - kind: review
    required: true
    detail: "Review fixture docs."

## Task Waves (explicit parallel dispatch sets)

- Wave 1 (parallel): [Task_1]

## Progress Log (append-only)

- 2026-05-09 00:00 Drafted.

## Decision Log (append-only; re-plans and major discoveries)

- 2026-05-09 00:00 Decision:
  - Fixture created.
