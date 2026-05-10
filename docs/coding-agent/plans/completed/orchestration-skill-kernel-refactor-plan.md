# Plan: Orchestration Skill Kernel Refactor

- status: done
- generated: 2026-05-09
- last_updated: 2026-05-09
- work_type: docs

## Goal
- Refactor `orchestration-harness/SKILL.md` into a shorter canonical kernel with progressive references while preserving all existing hard rules and orchestration semantics.

## Definition of Done
- `orchestration-harness/SKILL.md` is materially shorter and still usable as the entrypoint.
- Longer procedures are moved to focused references.
- The kernel still contains the five hard gates and visible completion blockers.
- Required linked skills remain discoverable from the kernel.

## Scope / Non-goals
- Scope:
  - Shorten the orchestration skill.
  - Add lifecycle, dispatch, UI validation, closeout, and final response references.
  - Preserve existing Orchestrator/Researcher/Worker/Reviewer semantics.
- Non-goals:
  - Do not change runtime agent files in this plan.
  - Do not weaken non-trivial plan/research/reviewer requirements.
  - Do not create a second canonical workflow source.

## Context (workspace)
- Related files/areas:
  - `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/SKILL.md`
  - `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/`
- Existing patterns or references:
  - `skills/plan-format/references/*.md`
  - `skills/subagent-strategy/references/*.md`
  - `docs/coding-agent-orchestration-harness/decisions/ADR-D-0001-canonical-harness-workflow-location.md`
- Repo reference docs consulted:
  - `docs/coding-agent/rules/index.md`
  - `docs/coding-agent/rules/common.md`
  - `docs/coding-agent/rules/orchestrator.md`

## Open Questions (max 3)
- Q1: resolved. Preserve the current skill section order broadly, but group the shorter kernel under the five hard gates to simplify review and reduce semantic drift.

## Assumptions
- A1: The current orchestration skill contains the intended hard rules and is the semantic baseline.
- A2: Reference extraction should move detail, not remove obligations.
- A3: The kernel should remain readable without opening every reference.
- A4: The rewritten skill should feel like a compressed version of the current workflow, not a rearranged workflow.

## Tasks

### Task_1: Inventory Existing Hard Rules
- type: research
- owns:
  - `docs/coding-agent/plans/completed/orchestration-skill-kernel-refactor-plan.md`
- depends_on: []
- description: |
  Build a checklist of current orchestration skill hard rules before editing.
- acceptance:
  - Checklist covers plan gate, research dispatch, dispatch integrity, validation, UI/E2E, review, git, rulebook, improvement loop, troubleshooting, closeout, and final response.
  - Checklist distinguishes kernel-visible rules from reference-level procedure.
- validation:
  - kind: review
    required: true
    owner: orchestrator
    detail: "Confirm all old hard rules are accounted for before edit."

### Task_2: Add Procedure References
- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/lifecycle-gates.md`
  - `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/dispatch-guidance.md`
  - `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/ui-validation-policy.md`
  - `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/completion-closeout.md`
  - `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/final-response-contract.md`
- depends_on: [Task_1]
- description: |
  Move detailed procedures from the skill into progressive-disclosure reference files.
- acceptance:
  - Lifecycle reference contains plan/research/replan details.
  - Dispatch reference contains Researcher/Worker/Reviewer prompt guidance.
  - UI validation reference contains the Worker probe, Researcher UI research, and Reviewer acceptance evidence tiers.
  - Closeout reference contains final done/blocked checks.
  - Final response reference contains the user-facing report contract.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Review references against the hard-rule inventory for semantic preservation."

### Task_3: Rewrite Orchestration Skill Kernel
- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/SKILL.md`
- depends_on: [Task_2]
- description: |
  Rewrite the skill entrypoint as a compact Orchestrator kernel with routing to detailed references.
- acceptance:
  - Kernel states "You are the workspace Orchestrator."
  - Kernel includes stable role model and runtime role-map instruction.
  - Kernel visibly includes Plan Gate, Research Dispatch Gate, Dispatch Integrity Gate, Validation Gate, and Completion Closeout Gate.
  - Kernel visibly states missing required evidence means blocked, not done.
  - Kernel visibly states shared-state Git mutations stay Orchestrator-controlled.
  - Kernel links to all required supporting skills.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Review shortened kernel for usability and semantic parity."

### Task_4: Run Drift And Link Checks
- type: test
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/SKILL.md`
  - `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/*.md`
- depends_on: [Task_3]
- description: |
  Validate that the refactor did not break reference paths or duplicate full workflow into adapters.
- acceptance:
  - All referenced files exist.
  - Required support skill names are present in the kernel.
  - No runtime adapter receives a full workflow copy as part of this plan.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "python plugins/coding-agent-orchestration-harness/scripts/validate_harness_package.py, after package validator exists; until then use rg/path review."
  - kind: review
    required: true
    owner: reviewer
    detail: "Reviewer confirms semantic preservation from old skill to kernel+references."

## Task Waves (explicit parallel dispatch sets)

- Wave 1 (parallel): [Task_1]
- Wave 2 (parallel): [Task_2]
- Wave 3 (parallel): [Task_3]
- Wave 4 (parallel): [Task_4]

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
- Restore the previous `orchestration-harness/SKILL.md` and remove newly extracted references if semantic parity fails.

## Progress Log (append-only)

- 2026-05-09 00:00 Plan drafted: [Task_1, Task_2, Task_3, Task_4]
  - Summary: Initial implementation plan created.
  - Validation evidence: Plan format self-check.
  - Notes: Awaiting approval before execution.
- 2026-05-09 00:00 Plan approved and started: [Task_1, Task_2, Task_3, Task_4]
  - Summary: User accepted the open-question recommendation and requested implementation.
  - Validation evidence: User approval in conversation.
  - Notes: Dedicated branch `codex-orchestration-skill-kernel-refactor`, stacked on `codex-architecture-rationale-shared-references`.
- 2026-05-09 00:00 Wave 1 completed: [Task_1]
  - Summary: Inventoried hard rules from the current orchestration skill and preserved them across the kernel/reference split.
  - Validation evidence: Manual semantic review against current skill sections.
  - Notes: Governance/safety rules were kept visible in the kernel.
- 2026-05-09 00:00 Wave 2 completed: [Task_2]
  - Summary: Added lifecycle, dispatch, UI validation, closeout, and final response references.
  - Validation evidence: `Get-ChildItem plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references`.
  - Notes: Existing role/status/validation references from the prior branch remain in the same reference folder.
- 2026-05-09 00:00 Wave 3 completed: [Task_3]
  - Summary: Replaced the long orchestration skill with a 157-line kernel containing stable role model, five hard gates, UI validation model, routing table, governance/safety, and final response summary.
  - Validation evidence: `rg` confirmed hard gates and required supporting skill routes are visible in `SKILL.md`.
  - Notes: The kernel remains usable without opening every reference.
- 2026-05-09 00:00 Wave 4 completed: [Task_4]
  - Summary: Completed drift and link checks available before the package validator exists.
  - Validation evidence: `rg` checks for required routes and `Get-ChildItem` reference-file existence.
  - Notes: Package validator is introduced by a later plan, so manual path/link review was used.

## Decision Log (append-only; re-plans and major discoveries)

- 2026-05-09 00:00 Decision:
  - Trigger / new insight: Current orchestration skill is canonical but long.
  - Plan delta (what changed): Dedicated a plan to kernel/reference extraction.
  - Tradeoffs considered: Keep enough in the kernel for runtime reliability while moving long procedures out.
  - User approval: yes

## Notes
- Risks:
  - Over-shortening the kernel could reduce compliance. Keep hard gates visible.
- Edge cases:
  - References should not become another source of conflicting policy.
