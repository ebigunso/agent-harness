# Plan: Architecture Rationale And Shared References

- status: done
- generated: 2026-05-09
- last_updated: 2026-05-09
- work_type: docs

## Goal
- Document the non-obvious harness architecture assumptions and add shared role/status/validation references that reduce runtime drift without duplicating the canonical orchestration workflow.

## Definition of Done
- New ADRs exist with the same frontmatter style as existing decisions.
- Role map, status model, and validation strictness references exist under `orchestration-harness/references/`.
- `orchestration-harness/SKILL.md` links to the references.
- New rationale does not contradict ADR-D-0001, ADR-I-0001, or ADR-I-0002.

## Scope / Non-goals
- Scope:
  - Add ADR-D-0002 through ADR-D-0005 and ADR-I-0003.
  - Add shared references for role names, status vocabulary, and validation strictness.
  - Add concise links from the orchestration skill.
- Non-goals:
  - Do not change runtime behavior in this plan.
  - Do not duplicate the full orchestration workflow into ADRs or adapters.
  - Do not rename public agent names.

## Context (workspace)
- Related files/areas:
  - `docs/coding-agent-orchestration-harness/decisions/`
  - `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/SKILL.md`
  - `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/`
- Existing patterns or references:
  - `ADR-D-0001-canonical-harness-workflow-location.md`
  - `ADR-I-0001-runtime-adapter-layout.md`
  - `ADR-I-0002-codex-bootstrap-and-loader-strategy.md`
- Repo reference docs consulted:
  - `docs/coding-agent/rules/index.md`
  - `docs/coding-agent/rules/common.md`
  - `docs/coding-agent/rules/orchestrator.md`

## Open Questions (max 3)
- Q1: resolved. ADR decider should remain `ebigunso`; consulted should be `GPT-5.5 Pro` because the implementation hand-off was written by GPT-5.5 Pro as part of a discussion with the maintainer.

## Assumptions
- A1: Existing Copilot physical names remain compatibility surfaces for this pass.
- A2: Claude and Codex namespaced physical names remain the preferred pattern.
- A3: ADRs are maintainer rationale; runtime operational rules stay in skills/references.
- A4: ADR consultation metadata should use the stable name `GPT-5.5 Pro` for this batch.

## Tasks

### Task_1: Add Design ADRs
- type: docs
- owns:
  - `docs/coding-agent-orchestration-harness/decisions/ADR-D-0002-explicit-orchestrator-entrypoint.md`
  - `docs/coding-agent-orchestration-harness/decisions/ADR-D-0003-runtime-namespaced-role-identities.md`
  - `docs/coding-agent-orchestration-harness/decisions/ADR-D-0004-worker-ui-probes-vs-reviewer-evidence.md`
  - `docs/coding-agent-orchestration-harness/decisions/ADR-D-0005-runtime-prompt-budgeting.md`
- depends_on: []
- description: |
  Add design ADRs explaining explicit Orchestrator entrypoint, runtime role namespacing, Worker UI probes versus Reviewer evidence, and runtime prompt budgeting.
- acceptance:
  - Each ADR has the existing ADR frontmatter fields and accepted status.
  - Each ADR explains why the design exists, not just what files change.
  - ADR-D-0001 remains valid and is not contradicted.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Review ADRs for frontmatter consistency and compatibility with existing ADR decisions."

### Task_2: Add Validation Strategy ADR
- type: docs
- owns:
  - `docs/coding-agent-orchestration-harness/decisions/ADR-I-0003-contract-first-validation-strategy.md`
- depends_on: []
- description: |
  Add implementation ADR for contract-first validation, strict completion checks, and balanced default runtime validation.
- acceptance:
  - ADR documents strict contract/completion checks and flexible prose/strategy checks.
  - ADR names `balanced` as the default runtime-facing validation mode.
  - ADR does not require exact transcript or wording validation.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Review ADR-I-0003 for consistency with validator implementation plans."

### Task_3: Add Shared Role And Status References
- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/runtime-role-map.md`
  - `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/status-model.md`
  - `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/validation-strictness.md`
- depends_on: [Task_1, Task_2]
- description: |
  Add role mapping, status vocabulary, and hard/soft/advisory validation rule references.
- acceptance:
  - Runtime role map includes Copilot, Claude, and Codex physical names.
  - Status model distinguishes Worker, Reviewer, validation, and plan statuses.
  - Validation strictness reference defines hard, soft, and advisory rules.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Review references for ambiguity reduction without full workflow duplication."

### Task_4: Link References From Orchestration Skill
- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/SKILL.md`
- depends_on: [Task_3]
- description: |
  Add concise links from the orchestration skill to the new role/status/validation references.
- acceptance:
  - Skill points to each new reference.
  - Skill remains the canonical runtime policy.
  - No full adapter workflow duplication is introduced.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "python plugins/coding-agent-orchestration-harness/scripts/validate_harness_package.py, after the package validator exists; until then perform manual path/link review."
  - kind: review
    required: true
    owner: reviewer
    detail: "Review links and ensure references are reachable and scoped."

## Task Waves (explicit parallel dispatch sets)

- Wave 1 (parallel): [Task_1, Task_2]
- Wave 2 (parallel): [Task_3]
- Wave 3 (parallel): [Task_4]

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
- Remove the new ADR/reference files and revert the orchestration skill link edits.

## Progress Log (append-only)

- 2026-05-09 00:00 Plan drafted: [Task_1, Task_2, Task_3, Task_4]
  - Summary: Initial implementation plan created.
  - Validation evidence: Plan format self-check.
  - Notes: Awaiting approval before execution.
- 2026-05-09 00:00 Plan approved and started: [Task_1, Task_2, Task_3, Task_4]
  - Summary: User accepted recommendations and requested implementation branches/PRs.
  - Validation evidence: User approval in conversation.
  - Notes: Dedicated branch `codex-architecture-rationale-shared-references`.
- 2026-05-09 00:00 Wave 1 completed: [Task_1, Task_2]
  - Summary: Added design ADRs for explicit Orchestrator entrypoint, role namespacing, Worker UI probes, runtime prompt budgeting, and implementation ADR for contract-first validation.
  - Validation evidence: ADR frontmatter/path review; consulted metadata uses `GPT-5.5 Pro` for this batch.
  - Notes: ADR links kept self-contained for this branch.
- 2026-05-09 00:00 Wave 2 completed: [Task_3]
  - Summary: Added runtime role map, status model, and validation strictness references.
  - Validation evidence: `Test-Path` returned true for all three reference files.
  - Notes: References reduce ambiguity without duplicating the full orchestration workflow.
- 2026-05-09 00:00 Wave 3 completed: [Task_4]
  - Summary: Linked the new references from `orchestration-harness/SKILL.md`.
  - Validation evidence: `rg -n "runtime-role-map|status-model|validation-strictness" plugins/coding-agent-orchestration-harness/skills/orchestration-harness/SKILL.md`.
  - Notes: Package validator is not available yet; manual path/link review used per plan.

## Decision Log (append-only; re-plans and major discoveries)

- 2026-05-09 00:00 Decision:
  - Trigger / new insight: Implementation hand-off requested rationale and shared references first.
  - Plan delta (what changed): Created a dedicated plan for ADR/reference work.
  - Tradeoffs considered: Kept runtime behavior changes out of this plan to preserve reviewability.
  - User approval: yes

## Notes
- Risks:
  - ADRs could accidentally restate runtime procedure. Keep rationale concise and refer to skills.
- Edge cases:
  - Package validator may not exist when Task_4 first lands; use manual review until validator wave lands.
