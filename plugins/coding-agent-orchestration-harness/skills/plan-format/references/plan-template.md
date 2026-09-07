# Plan Template (Execution Plan, Task_X format)

Copy this structure into:
- `docs/coding-agent/plans/active/<kebab>-plan.md`

Keep it readable. Prefer short bullets and links over long narratives.

Never hard-wrap prose mid-sentence in committed plan/doc files — keep one sentence, paragraph, or list item per line.

---

# Plan: <Title>

- status: draft | approved | in_progress | done
- generated: <YYYY-MM-DD>
- last_updated: <YYYY-MM-DD>
- work_type: code | docs | slides | research | mixed

## Goal
- <what success looks like>

## Definition of Done
- <concrete criteria>

## Scope / Non-goals
- Scope:
- Non-goals:

## Compatibility stance (required if a contract/interface/persisted format is touched)
- surface: <contract/interface/format being changed>
- stance: break | preserve | migrate | ask-user
- justification: <locatable consumer(s) per core-principles, or "consumers unverifiable on boundary-crossing surface" for ask-user>
- (per-task notes only if stances differ across tasks)

## Context (workspace)
- Related files/areas:
- Existing patterns or references:
- Design record consulted and deviations from its acceptance:

## Open Questions (max 3)
- Q1:
- Q2:
- Q3:

## Assumptions
- A1: <claim> — source: <file:line | design record path | unverified, checked by Task_N>
- A2:
- Hypothesis (only for fix-shaped plans where the cause is not yet established): <cause> ; falsified by: <observation>

## Tasks

### Task_1: <Task title>
- type: design
- owns:
  - docs/...
- depends_on: []
- description: |
  <what to decide/produce>
- acceptance:
  - <criterion>
- validation:
  - kind: review
    required: true
    owner: orchestrator
    detail: "Plan updated with decision + tradeoffs"

### Task_2: <Task title>
- type: impl
- owns:
  - src/...
- depends_on: [Task_1]
- description: |
  <what to implement>
- acceptance:
  - <criterion>
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "<repo command, e.g., npm run test:unit>"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review vs acceptance criteria"

### Task_3: <UI E2E/visual validation (required if UI impacted)>
- type: review
- owns: []
- depends_on: [Task_2]
- description: |
  Run browser-based E2E/visual checks per the E2E spec below.
  Collect evidence under the provider-defined artifact root.
- acceptance:
  - Reviewer status is APPROVED
  - Required evidence captured under the provider-defined artifact root
- validation:
  - kind: e2e
    required: true
    owner: reviewer
    detail: "Run the E2E spec in this plan using the selected browser automation provider"

## Task Waves (explicit parallel dispatch sets)

Interpretation:
- Tasks listed in the same wave are intended to be dispatched in parallel by default,
  when `owns` are disjoint and dependencies are met.
- Waves are executed sequentially.

- Wave 1 (parallel): [Task_1]
- Wave 2 (parallel): [Task_2]
- Wave 3 (parallel): [Task_3]

## E2E / Visual Validation Spec (optional; required if UI impacted)

- provider:
- artifact_root:
- base_url:
- app_start_command:
- readiness_check:
- flows:
- viewports:
- evidence_requirements:
- known_flakiness:

## Rollback / Safety
- <how to revert or disable changes>

## Progress Log (append-only)

Append-only editing rule (applies to both logs below): when appending an entry, anchor the edit on the previous entry and reproduce it (or anchor on the section's tail marker) so the edit inserts rather than replaces, and verify afterward that the log grew.

- <YYYY-MM-DD HH:MM> Wave N completed: [Task_X, ...]
  - Summary:
  - Validation evidence:
  - Notes:

## Decision Log (append-only; re-plans and major discoveries)

- <YYYY-MM-DD HH:MM> Decision:
  - Trigger / new insight:
  - Plan delta (what changed):
  - Tradeoffs considered:
  - User approval: yes/no (link to discussion if applicable)
  - Record proposed: <path or none; acceptance state> (per `durable-docs-authoring/references/adr.md`)

## Notes
- Risks:
- Edge cases:
