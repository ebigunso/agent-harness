# Plan: Worker UI Probes

- status: done
- generated: 2026-05-09
- last_updated: 2026-05-09
- work_type: mixed

## Goal
- Make bounded Worker-owned UI probes a first-class implementation feedback mechanism while preserving independent Reviewer-owned UI/E2E acceptance evidence.

## Definition of Done
- `worker-ui-probes` skill exists.
- Worker definitions across Copilot, Claude, and Codex allow bounded UI probes for assigned UI/frontend work.
- Reviewer definitions state Worker probes are not a substitute for Reviewer validation.
- Worker report contract and validator support optional `ui_probes`.
- Existing non-UI Worker reports remain valid.

## Scope / Non-goals
- Scope:
  - Add Worker UI probe policy skill.
  - Update Worker and Reviewer agent definitions.
  - Update orchestration UI validation policy references.
  - Extend report schema and validator for optional `ui_probes`.
- Non-goals:
  - Do not allow Workers to replace Reviewer acceptance evidence.
  - Do not require UI probes for non-UI tasks.
  - Do not add external-site browser probing by default.

## Context (workspace)
- Related files/areas:
  - `plugins/coding-agent-orchestration-harness/skills/worker-ui-probes/SKILL.md`
  - `plugins/coding-agent-orchestration-harness/agents/Worker.md`
  - `plugins/coding-agent-orchestration-harness/agents/Reviewer.md`
  - `plugins/coding-agent-orchestration-harness/claude/agents/harness-worker.md`
  - `plugins/coding-agent-orchestration-harness/claude/agents/harness-reviewer.md`
  - `plugins/coding-agent-orchestration-harness/codex/agent-templates/harness_worker.toml`
  - `plugins/coding-agent-orchestration-harness/codex/agent-templates/harness_reviewer.toml`
  - `plugins/coding-agent-orchestration-harness/skills/subagent-report-contract/SKILL.md`
  - `plugins/coding-agent-orchestration-harness/skills/subagent-report-contract/scripts/validate_worker_report.py`
- Existing patterns or references:
  - `skills/playwright-e2e-evidence/SKILL.md`
  - `skills/subagent-report-contract/references/schema.yaml`
  - `skills/orchestration-harness/references/ui-validation-policy.md`
- Repo reference docs consulted:
  - `docs/coding-agent/rules/index.md`
  - `docs/coding-agent/rules/common.md`
  - `docs/coding-agent/rules/worker.md`
  - `docs/coding-agent/rules/orchestrator.md`

## Open Questions (max 3)
- Q1: resolved. Workers may use the runtime-default local browser/UI tooling for implementation-local probes when assigned UI/frontend work; require the plan or Orchestrator prompt to name the provider when probe evidence is expected as required validation.

## Assumptions
- A1: Worker probes are local implementation checks and must be reported in Worker YAML when materially used.
- A2: Reviewer owns independent acceptance evidence unless the Orchestrator or user explicitly waives/reassigns it.
- A3: Codex templates are source templates and bootstrap freshness work will handle installed stale copies later.
- A4: Reviewer-owned acceptance evidence should remain more formal than Worker implementation probes.

## Tasks

### Task_1: Add Worker UI Probes Skill
- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/worker-ui-probes/SKILL.md`
- depends_on: []
- description: |
  Add a shared skill defining when and how Workers may run bounded UI probes.
- acceptance:
  - Skill frontmatter describes bounded Worker UI probes.
  - Core rules limit probes to assigned UI/frontend work or explicit Orchestrator assignment.
  - Skill states probes are local, bounded, implementation-facing, and do not satisfy Reviewer validation automatically.
  - Evidence expectations list base URL/command, flow/screen, result, fixes, and artifact path when present.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Review skill for clear Worker/Reviewer boundary."

### Task_2: Update Worker Definitions
- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/agents/Worker.md`
  - `plugins/coding-agent-orchestration-harness/claude/agents/harness-worker.md`
  - `plugins/coding-agent-orchestration-harness/codex/agent-templates/harness_worker.toml`
- depends_on: [Task_1]
- description: |
  Update Worker wording to allow bounded UI probes for UI/frontend work and require probe evidence when used.
- acceptance:
  - Any "no browser automation" wording is removed or replaced.
  - Worker may use browser/UI tooling for implementation-local checks when assigned.
  - Worker may not claim Reviewer-owned validation is satisfied.
  - Worker reports probe evidence when probes materially affect implementation.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Review Worker definitions for consistent bounded probe permission."

### Task_3: Update Reviewer Definitions
- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/agents/Reviewer.md`
  - `plugins/coding-agent-orchestration-harness/claude/agents/harness-reviewer.md`
  - `plugins/coding-agent-orchestration-harness/codex/agent-templates/harness_reviewer.toml`
- depends_on: [Task_1]
- description: |
  Update Reviewer wording to preserve independent validation authority.
- acceptance:
  - Reviewer definitions state Worker probes are useful implementation evidence.
  - Reviewer definitions state Worker probes are not a substitute for Reviewer-owned validation.
  - If UI/E2E validation is required, Reviewer independently verifies required evidence.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Review Reviewer definitions for independent acceptance evidence ownership."

### Task_4: Update UI Validation Policy
- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/SKILL.md`
  - `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/ui-validation-policy.md`
- depends_on: [Task_1, Task_2, Task_3]
- description: |
  Add the three-tier UI model to orchestration guidance.
- acceptance:
  - Policy defines UI probe, UI research, and UI acceptance evidence tiers.
  - Owners are Worker, Researcher, and Reviewer respectively.
  - Required Reviewer-owned UI/E2E validation remains required for UI-impacting non-trivial work unless waived.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Review UI policy for clear tier ownership and no validation shortcut."

### Task_5: Extend Worker Report Contract
- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/subagent-report-contract/SKILL.md`
  - `plugins/coding-agent-orchestration-harness/skills/subagent-report-contract/references/schema.yaml`
  - `plugins/coding-agent-orchestration-harness/skills/subagent-report-contract/references/examples.md`
- depends_on: [Task_1]
- description: |
  Document optional top-level `ui_probes` report evidence.
- acceptance:
  - Contract describes optional `ui_probes` list.
  - Fields include `base_url`, `flow`, `result`, `evidence`, and `notes`.
  - Contract states `ui_probes` does not satisfy Reviewer-owned validation automatically.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Review contract docs for backward compatibility and clear optionality."

### Task_6: Extend Worker Report Validator
- type: test
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/subagent-report-contract/scripts/validate_worker_report.py`
- depends_on: [Task_5]
- description: |
  Add optional `ui_probes` shape validation without requiring it for non-UI tasks.
- acceptance:
  - `ui_probes` is optional.
  - If present, it must be a list of mappings.
  - Probe result must be `pass`, `fail`, or `skipped`.
  - Existing valid reports without `ui_probes` still pass.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "python -m py_compile plugins/coding-agent-orchestration-harness/skills/subagent-report-contract/scripts/validate_worker_report.py"
  - kind: command
    required: true
    owner: worker
    detail: "python plugins/coding-agent-orchestration-harness/skills/subagent-report-contract/scripts/validate_worker_report.py --file plugins/coding-agent-orchestration-harness/tests/fixtures/valid-worker-report.yaml, after fixtures exist"
  - kind: review
    required: true
    owner: reviewer
    detail: "Review validator changes for backward compatibility."

## Task Waves (explicit parallel dispatch sets)

- Wave 1 (parallel): [Task_1]
- Wave 2 (parallel): [Task_2, Task_3, Task_5]
- Wave 3 (parallel): [Task_4, Task_6]

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
- Revert Worker/Reviewer wording and remove `ui_probes` validator support. Since `ui_probes` is optional, rollback should not affect existing reports.

## Progress Log (append-only)

- 2026-05-09 00:00 Plan drafted: [Task_1, Task_2, Task_3, Task_4, Task_5, Task_6]
  - Summary: Initial implementation plan created.
  - Validation evidence: Plan format self-check.
  - Notes: Awaiting approval before execution.
- 2026-05-09 00:00 Plan approved and started: [Task_1, Task_2, Task_3, Task_4, Task_5, Task_6]
  - Summary: User accepted the open-question recommendation and requested implementation.
  - Validation evidence: User approval in conversation.
  - Notes: Dedicated branch `codex-worker-ui-probes`, stacked on `codex-runtime-adapter-alignment`.
- 2026-05-09 00:00 Wave 1 completed: [Task_1]
  - Summary: Added `worker-ui-probes` skill with bounded local probe policy and evidence expectations.
  - Validation evidence: Manual frontmatter and policy review.
  - Notes: Skill states probes do not satisfy Reviewer-owned validation.
- 2026-05-09 00:00 Wave 2 completed: [Task_2, Task_3, Task_5]
  - Summary: Updated Worker definitions, Reviewer definitions, and Worker report contract docs/schema/examples for optional `ui_probes`.
  - Validation evidence: `rg` confirmed Worker/Reviewer probe boundary wording and no stale `no browser automation` wording in target files.
  - Notes: Existing non-UI reports remain valid because `ui_probes` is optional.
- 2026-05-09 00:00 Wave 3 completed: [Task_4, Task_6]
  - Summary: Confirmed orchestration UI policy already uses the three-tier model and extended validator shape checks for optional `ui_probes`.
  - Validation evidence: `python -m py_compile plugins/coding-agent-orchestration-harness/skills/subagent-report-contract/scripts/validate_worker_report.py`; valid stdin YAML with `ui_probes` passed; invalid probe result failed clearly.
  - Notes: Fixture-based validation is deferred to the validator fixtures plan.

## Decision Log (append-only; re-plans and major discoveries)

- 2026-05-09 00:00 Decision:
  - Trigger / new insight: Existing Worker tooling and desired behavior need clearer policy.
  - Plan delta (what changed): Added first-class Worker UI probe plan.
  - Tradeoffs considered: Allow implementation feedback while preserving independent Reviewer validation.
  - User approval: yes

## Notes
- Risks:
  - Poor wording could imply Worker probes satisfy acceptance. State the boundary repeatedly and consistently.
- Edge cases:
  - If a Worker probe finds a failure outside `owns`, Worker should report it rather than expand scope.
