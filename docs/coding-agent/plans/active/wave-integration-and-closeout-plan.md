# Plan: Wave Integration And Closeout

- status: in_progress
- generated: 2026-05-09
- last_updated: 2026-05-09
- work_type: mixed

## Goal
- Make Orchestrator-owned Worker wave integration and closeout checks explicit so Worker reports, validation evidence, blockers, and Reviewer context are consistently reconciled.

## Definition of Done
- `wave-integration` skill exists.
- Integration checklist and Reviewer packet template exist.
- Orchestration guidance routes to wave integration after Worker waves and before Reviewer dispatch.
- Closeout validator exists as a lightweight contract check.

## Scope / Non-goals
- Scope:
  - Add `wave-integration` skill and references.
  - Add Reviewer packet guidance.
  - Add `validate_closeout.py`.
  - Route orchestration skill to wave integration.
- Non-goals:
  - Do not add a new Integrator subagent.
  - Do not make the closeout validator infer arbitrary prose perfectly.
  - Do not move plan lifecycle ownership away from Orchestrator.

## Context (workspace)
- Related files/areas:
  - `plugins/coding-agent-orchestration-harness/skills/wave-integration/`
  - `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/SKILL.md`
  - `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/dispatch-guidance.md`
  - `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/completion-closeout.md`
- Existing patterns or references:
  - `skills/subagent-report-contract/SKILL.md`
  - `skills/plan-format/references/execution-plan-lifecycle.md`
  - `skills/subagent-strategy/references/dispatch-checklists.md`
- Repo reference docs consulted:
  - `docs/coding-agent/rules/index.md`
  - `docs/coding-agent/rules/common.md`
  - `docs/coding-agent/rules/orchestrator.md`

## Open Questions (max 3)
- Q1: resolved. `validate_closeout.py` should require a structured JSON/YAML summary file from the start, with the plan file used as contextual input.

## Assumptions
- A1: The Orchestrator remains the only writer for shared plan lifecycle state.
- A2: The first closeout validator can be lightweight and contract-based.
- A3: Reviewer dispatch should include a packet rather than forcing Reviewer to reconstruct context.
- A4: Closeout validation is high-stakes enough that explicit structured state is preferable to brittle markdown inference.

## Tasks

### Task_1: Add Wave Integration Skill
- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/wave-integration/SKILL.md`
- depends_on: []
- description: |
  Add a first-class Orchestrator-owned integration checklist skill.
- acceptance:
  - Skill frontmatter describes Worker wave integration.
  - Skill states it is used after Worker waves, before Reviewer dispatch, or before closeout.
  - Skill states it does not create a new mutation-capable subagent.
  - Skill points to checklist and Reviewer packet references.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Review skill trigger and ownership boundary."

### Task_2: Add Integration Checklist
- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/wave-integration/references/integration-checklist.md`
- depends_on: [Task_1]
- description: |
  Add checklist for parsing Worker reports, validating contracts, reconciling owns, blockers, rules, lessons, progress logs, and next dispatch.
- acceptance:
  - Checklist includes all requested nine integration steps.
  - Checklist requires report validation against subagent-report-contract.
  - Checklist requires Worker-owned required validations to pass or be waived.
  - Checklist tells Orchestrator to decide follow-up Worker versus Reviewer.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Review checklist for completeness and executable order."

### Task_3: Add Reviewer Packet Template
- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/wave-integration/references/reviewer-packet-template.md`
- depends_on: [Task_1]
- description: |
  Add a concise template for handing Worker wave context to Reviewer.
- acceptance:
  - Template includes phase/wave, objective, tasks, changed files, acceptance criteria, required validation, Worker evidence, Worker UI probes, waivers, blockers, and risk areas.
  - Template is reference material, not a new required output file unless the Orchestrator chooses to create one.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Review packet template for enough context to support independent review."

### Task_4: Route Orchestration Guidance To Wave Integration
- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/SKILL.md`
  - `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/dispatch-guidance.md`
  - `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/completion-closeout.md`
- depends_on: [Task_2, Task_3]
- description: |
  Add hard instruction that after each Worker wave and before Reviewer dispatch, Orchestrator runs wave-integration checklist.
- acceptance:
  - Kernel or dispatch guidance includes the wave-integration route.
  - Reviewer dispatch guidance references the Reviewer packet.
  - Closeout guidance uses wave-integration before final done report.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Review routing for integration-before-review and integration-before-closeout behavior."

### Task_5: Add Lightweight Closeout Validator
- type: test
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/wave-integration/scripts/validate_closeout.py`
- depends_on: [Task_4]
- description: |
  Add a lightweight validator that reads a plan file and JSON/YAML summary file to block false completion.
- acceptance:
  - Validator checks all tasks done or waived.
  - Validator checks required validation pass or waived.
  - Validator checks no unresolved blockers.
  - Validator checks Reviewer approval or waiver for non-trivial work.
  - Validator checks active plan status is updated before final done report.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "python -m py_compile plugins/coding-agent-orchestration-harness/skills/wave-integration/scripts/validate_closeout.py"
  - kind: review
    required: true
    owner: reviewer
    detail: "Review validator scope to ensure it is contract-based and not transcript/prose-based."

## Task Waves (explicit parallel dispatch sets)

- Wave 1 (parallel): [Task_1]
- Wave 2 (parallel): [Task_2, Task_3]
- Wave 3 (parallel): [Task_4]
- Wave 4 (parallel): [Task_5]

## E2E / Visual Validation Spec (optional; required if UI impacted)

- provider: none
- artifact_root: none
- base_url: none
- app_start_command: none
- readiness_check: none
- flows: none
- viewports: none
- evidence_requirements: none
- known_flakiness: none

## Rollback / Safety
- Remove `wave-integration` skill and closeout validator, then remove routing lines from orchestration references.

## Progress Log (append-only)

- 2026-05-09 00:00 Plan drafted: [Task_1, Task_2, Task_3, Task_4, Task_5]
  - Summary: Initial implementation plan created.
  - Validation evidence: Plan format self-check.
  - Notes: Awaiting approval before execution.
- 2026-05-09 00:00 Plan approved and started: [Task_1, Task_2, Task_3, Task_4, Task_5]
  - Summary: User accepted the open-question recommendation and requested implementation.
  - Validation evidence: User approval in conversation.
  - Notes: Dedicated branch `codex-wave-integration-closeout`, stacked on `codex-worker-ui-probes`.

## Decision Log (append-only; re-plans and major discoveries)

- 2026-05-09 00:00 Decision:
  - Trigger / new insight: Integration is dense enough to need first-class Orchestrator checklist support.
  - Plan delta (what changed): Added a dedicated integration and closeout plan.
  - Tradeoffs considered: Kept integration Orchestrator-owned instead of adding a new subagent.
  - User approval: yes

## Notes
- Risks:
  - Closeout validator could become brittle if it tries to infer too much from markdown.
- Edge cases:
  - Waivers must include explicit evidence; skipped is not the same as waived.
