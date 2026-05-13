# Plan: Report Schema Split

- status: draft
- generated: 2026-05-14
- last_updated: 2026-05-14
- work_type: mixed

## Goal

- Split repo-local rule candidates from harness-global migration candidates in Worker/Reviewer reporting contracts and validators.

## Definition of Done

- `rule_candidates` no longer supports or documents `intended_home`.
- `rule_candidates` are documented and validated as repo-local only.
- `harness_migration_candidates` is documented and validated as the only report-level route for cross-repo harness improvements.
- `lesson_candidates[*].promotion_target` is validated against `repo_rule | harness_migration | troubleshooting | residual_risk`.
- Worker report fixtures and smoke tests cover the new schema.

## Scope / Non-goals

- Scope:
  - Update the subagent report contract prose, schema reference, validator, fixtures, and smoke-test expectations.
  - Preserve existing validation behavior unrelated to candidate routing.
- Non-goals:
  - Do not update rulebook routing or rule-suite templates; that is covered by the Rulebook Rule-File Cleanup plan.
  - Do not update runtime Reviewer/Worker adapter wording; that is covered by the Runtime Agent Boundary And Adapter Updates plan.
  - Do not implement actual promotion from reports into files.

## Context (workspace)

- Related files/areas:
  - `plugins/coding-agent-orchestration-harness/skills/subagent-report-contract/SKILL.md`
  - `plugins/coding-agent-orchestration-harness/skills/subagent-report-contract/references/schema.yaml`
  - `plugins/coding-agent-orchestration-harness/skills/subagent-report-contract/references/examples.md`
  - `plugins/coding-agent-orchestration-harness/skills/subagent-report-contract/scripts/validate_worker_report.py`
  - `plugins/coding-agent-orchestration-harness/tests/fixtures/*.yaml`
  - `plugins/coding-agent-orchestration-harness/tests/fixtures/*.md`
  - `plugins/coding-agent-orchestration-harness/scripts/run_validation_smoke_tests.py`
- Existing patterns or references:
  - Existing Worker report validator uses enum-style constants and clear exit codes.
  - Existing smoke tests validate both valid and expected-invalid fixtures.
- Repo reference docs consulted:
  - `docs/coding-agent/plans/completed/contract-first-validators-and-fixtures-plan.md`

## Open Questions (max 3)

- Q1: resolved. Old reports with `intended_home` should fail hard immediately; this is an intentional design break.

## Assumptions

- A1: `harness_migration_candidates` is optional, but if present must be a list of fully shaped entries.
- A2: `example` on `rule_candidates` is required by shape and may be an empty string.
- A3: The validator should reject unknown candidate categories rather than warning.

Required-check waiver
- What is waived: Reviewer-owned UI/E2E/visual evidence for this report-schema and fixture-update plan.
- Why waived now: The plan may edit an existing fixture whose filename contains `ui`, but it does not change a user interface, browser flow, or visual surface.
- Risk accepted and impact: No visual regression evidence will be collected because there is no UI behavior under test.
- Mitigation and follow-up: Use command validation, fixture validation, smoke tests, and Reviewer diff review for this schema-only change.
- Owner and expiration: Orchestrator; expires when this plan is completed.

## Tasks

### Task_1: Update Report Contract Documentation

- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/subagent-report-contract/SKILL.md`
  - `plugins/coding-agent-orchestration-harness/skills/subagent-report-contract/references/schema.yaml`
  - `plugins/coding-agent-orchestration-harness/skills/subagent-report-contract/references/examples.md`
- depends_on: []
- description: |
  Rewrite the candidate and lesson sections so repo rule candidates and harness migration candidates are distinct report fields with no shared destination enum.
- acceptance:
  - `rule_candidates` fields are `audience`, `id`, `rule`, `rationale`, `scope`, and `example`.
  - `rule_candidates` prose says candidates are always repo-local.
  - `harness_migration_candidates` fields are `id`, `category`, `proposed_home`, `generalized_rule`, `trigger`, `evidence_from_repo`, `rationale`, and `suggested_change`.
  - Harness migration categories match the target enum.
  - Lesson promotion targets are documented as `repo_rule | harness_migration | troubleshooting | residual_risk`.
  - Documentation contains no `intended_home`, `global_candidate`, `global-skill`, or `references/*` as promotion targets.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "Run targeted `rg` checks in subagent-report-contract docs for removed tokens: `intended_home`, `global_candidate`, `global-skill`, `references/*`."
  - kind: review
    required: true
    owner: worker
    detail: "Manually compare documented fields with the validator field lists before handing off."

### Task_2: Update Worker Report Validator

- type: test
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/subagent-report-contract/scripts/validate_worker_report.py`
- depends_on: [Task_1]
- description: |
  Remove intended-home validation, add harness migration candidate validation, and validate the new lesson promotion target enum.
- acceptance:
  - `ALLOWED_INTENDED_HOME` is removed.
  - `ALLOWED_LESSON_PROMOTION_TARGET` contains only `repo_rule`, `harness_migration`, `troubleshooting`, and `residual_risk`.
  - `ALLOWED_MIGRATION_CATEGORY` contains `review`, `validation`, `orchestration`, `delegation`, `rulebook`, `troubleshooting`, `adapter`, `validator`, and `other`.
  - `validate_rule_candidates` rejects missing repo-local fields and rejects `intended_home`.
  - `validate_harness_migration_candidates` rejects missing fields and invalid categories.
  - `lesson_candidates[*].promotion_target` is required when a lesson candidate is present and must match the enum.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "Run `python -m py_compile plugins/coding-agent-orchestration-harness/skills/subagent-report-contract/scripts/validate_worker_report.py`."
  - kind: command
    required: true
    owner: worker
    detail: "Run targeted `rg` checks in the validator for removed token `ALLOWED_INTENDED_HOME`."

### Task_3: Update Fixtures And Smoke Tests

- type: test
- owns:
  - `plugins/coding-agent-orchestration-harness/tests/fixtures/valid-worker-report.yaml`
  - `plugins/coding-agent-orchestration-harness/tests/fixtures/valid-worker-report-reviewer-candidate.yaml`
  - `plugins/coding-agent-orchestration-harness/tests/fixtures/valid-ui-worker-report-with-probes.yaml`
  - `plugins/coding-agent-orchestration-harness/tests/fixtures/valid-worker-message.md`
  - `plugins/coding-agent-orchestration-harness/tests/fixtures/invalid-worker-report-missing-validation.yaml`
  - `plugins/coding-agent-orchestration-harness/tests/fixtures/invalid-worker-report-done-with-failed-required-validation.yaml`
  - `plugins/coding-agent-orchestration-harness/scripts/run_validation_smoke_tests.py`
- depends_on: [Task_2]
- description: |
  Bring existing valid fixtures onto the new schema and add at least one expected-invalid case for removed or invalid candidate routing.
- acceptance:
  - Existing valid fixtures pass with the new schema.
  - At least one fixture or smoke-test case proves `intended_home` is rejected.
  - At least one fixture or smoke-test case proves invalid `promotion_target` is rejected.
  - At least one valid fixture includes a `harness_migration_candidates` entry.
  - Fixtures stay minimal and readable.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "Run `python plugins/coding-agent-orchestration-harness/scripts/run_validation_smoke_tests.py`."
  - kind: review
    required: true
    owner: reviewer
    detail: "Review fixture coverage for the intentional schema break and the new migration candidate shape."

### Task_4: Final Contract Consistency Review

- type: review
- owns: []
- depends_on: [Task_1, Task_2, Task_3]
- description: |
  Review the documentation, validator, and fixtures as one contract.
- acceptance:
  - Documentation, schema reference, examples, validator, fixtures, and smoke tests agree on field names and enums.
  - No removed destination strings remain in the subagent report contract surface.
  - Reviewer confirms backward-incompatible behavior is intentional and clear.
- validation:
  - kind: command
    required: true
    owner: reviewer
    detail: "Run `python plugins/coding-agent-orchestration-harness/scripts/run_validation_smoke_tests.py` or review Worker evidence from the same command."
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review against acceptance criteria."

## Task Waves (explicit parallel dispatch sets)

- Wave 1 (parallel): [Task_1]
- Wave 2 (parallel): [Task_2]
- Wave 3 (parallel): [Task_3]
- Wave 4 (parallel): [Task_4]

## E2E / Visual Validation Spec

- Not applicable. This plan changes report contracts, documentation, validators, and fixtures only.

## Rollback / Safety

- Revert the report contract, validator, fixture, and smoke-test changes together to avoid schema drift.
- If downstream plans have already adopted the new schema, do not roll back this plan alone.

## Progress Log (append-only)

- 2026-05-14 Plan drafted.
  - Summary: Added implementation plan for separating repo-local rule candidates from harness migration candidates in the report contract.
  - Validation evidence: Plan-format self-check.
  - Notes: Awaiting approval before execution.

## Decision Log (append-only; re-plans and major discoveries)

- 2026-05-14 Decision: Treat removal of `intended_home` as an intentional hard break.
  - Trigger / new insight: The hand-off document explicitly asks for a clean structural split.
  - Plan delta (what changed): Fixtures and validators will reject the old shape instead of accepting it as legacy.
  - Tradeoffs considered: Backward compatibility would preserve ambiguity; hard break makes routing precise.
  - User approval: yes.

## Notes

- Risks:
  - Adapter docs may still mention old lesson targets until the dependent runtime-adapter plan executes.
  - Package validation guards should be added only after all dependent docs are updated.
- Edge cases:
  - Empty `rule_candidates` and empty `harness_migration_candidates` should remain valid.
