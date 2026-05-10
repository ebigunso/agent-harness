# Plan: Contract-First Validators And Fixtures

- status: done
- generated: 2026-05-09
- last_updated: 2026-05-09
- work_type: code

## Goal
- Add balanced, contract-first validators and minimal fixtures to block malformed plans/reports/package structure and false completion without validating exact prose or execution strategy.

## Definition of Done
- Package validator exists and passes on the plugin.
- Plan validator exists with `--mode strict|balanced|relaxed`, default `balanced`.
- Worker report validator supports message-file extraction, task-contract checks, task id format, blocker rules, waiver checks, and optional `ui_probes`.
- Closeout validator integration is covered by smoke tests when available.
- Smoke test runner exits 0 when expected passes and failures match fixtures.

## Scope / Non-goals
- Scope:
  - Add validators and fixtures.
  - Extend existing Worker report validator.
  - Add smoke test runner.
  - Compile-check Python scripts.
- Non-goals:
  - Do not enforce exact wording or response transcript style.
  - Do not make validators depend on live runtime tools.
  - Do not require PyYAML-free parsing if PyYAML is already the validator dependency.

## Context (workspace)
- Related files/areas:
  - `plugins/coding-agent-orchestration-harness/scripts/validate_harness_package.py`
  - `plugins/coding-agent-orchestration-harness/scripts/run_validation_smoke_tests.py`
  - `plugins/coding-agent-orchestration-harness/skills/plan-format/scripts/validate_plan.py`
  - `plugins/coding-agent-orchestration-harness/skills/subagent-report-contract/scripts/validate_worker_report.py`
  - `plugins/coding-agent-orchestration-harness/skills/wave-integration/scripts/validate_closeout.py`
  - `plugins/coding-agent-orchestration-harness/tests/fixtures/`
- Existing patterns or references:
  - `skills/subagent-report-contract/scripts/validate_worker_report.py`
  - `skills/plan-format/references/plan-template.md`
  - `skills/plan-format/references/validation-items.md`
  - `skills/orchestration-harness/references/validation-strictness.md`
- Repo reference docs consulted:
  - `docs/coding-agent/rules/index.md`
  - `docs/coding-agent/rules/common.md`
  - `docs/coding-agent/rules/orchestrator.md`

## Open Questions (max 3)
- Q1: resolved. Package validator should warn by default in balanced mode when adapter workflow-duplication detection is uncertain, and fail only for clear deterministic duplication markers.

## Assumptions
- A1: Balanced mode hard-fails malformed contracts and missing ownership but only warns on subjective quality.
- A2: Fixture tests can assert invalid examples fail by checking non-zero exit codes.
- A3: Validator output should be clear enough for agents to fix reports/plans without reading the source.
- A4: Adapter duplication detection is partly heuristic and must follow the non-brittle validation philosophy.

## Tasks

### Task_1: Add Package Validator
- type: test
- owns:
  - `plugins/coding-agent-orchestration-harness/scripts/validate_harness_package.py`
- depends_on: []
- description: |
  Validate plugin manifests, referenced paths, role map consistency, skill frontmatter, Codex templates, bootstrap compile, and adapter workflow duplication heuristics.
- acceptance:
  - Manifests parse as JSON.
  - Manifest referenced agent/skill paths exist.
  - Runtime role map references physical agents/templates that exist.
  - Each `skills/*/SKILL.md` exists and has frontmatter.
  - Codex template files exist.
  - Codex bootstrap script compiles.
  - New referenced skills such as `worker-ui-probes` and `wave-integration` are not missing.
  - Adapter duplication checks avoid exact prose validation.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "python -m py_compile plugins/coding-agent-orchestration-harness/scripts/validate_harness_package.py"
  - kind: command
    required: true
    owner: worker
    detail: "python plugins/coding-agent-orchestration-harness/scripts/validate_harness_package.py"
  - kind: review
    required: true
    owner: reviewer
    detail: "Review validator rules for contract-first scope and low brittleness."

### Task_2: Add Plan Validator
- type: test
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/plan-format/scripts/validate_plan.py`
- depends_on: []
- description: |
  Add plan contract validator with strict, balanced, and relaxed modes.
- acceptance:
  - Default mode is `balanced`.
  - Required sections are checked.
  - Task ids use `Task_1`, `Task_2`, etc.
  - Each task has `type`, `owns`, `depends_on`, `acceptance`, and `validation`.
  - Dependencies reference existing tasks and cycles fail.
  - Task Waves include all tasks exactly once.
  - Validation items include `kind`, `required`, `owner`, and `detail`.
  - UI-impact plans require Reviewer-owned E2E/visual validation or explicit waiver.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "python -m py_compile plugins/coding-agent-orchestration-harness/skills/plan-format/scripts/validate_plan.py"
  - kind: command
    required: true
    owner: worker
    detail: "python plugins/coding-agent-orchestration-harness/skills/plan-format/scripts/validate_plan.py --file plugins/coding-agent-orchestration-harness/tests/fixtures/valid-plan.md --mode balanced"
  - kind: review
    required: true
    owner: reviewer
    detail: "Review plan validator for balanced-mode behavior."

### Task_3: Extend Worker Report Validator
- type: test
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/subagent-report-contract/scripts/validate_worker_report.py`
- depends_on: []
- description: |
  Extend the existing Worker report validator with stricter contract checks and message-file support.
- acceptance:
  - `--message-file` extracts exactly one YAML code block and rejects extra prose or multiple/missing YAML blocks.
  - Optional `--task-contract` compares report validation results against assigned Task_X validation.
  - `task_id` must match `^Task_[1-9][0-9]*$`.
  - `blocked` or `failed` status requires non-empty `blockers`.
  - Required Worker-owned skipped validation requires waiver evidence.
  - Optional `ui_probes` shape is validated.
  - Raw YAML mode does not reject extra prose because it only parses YAML input.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "python -m py_compile plugins/coding-agent-orchestration-harness/skills/subagent-report-contract/scripts/validate_worker_report.py"
  - kind: review
    required: true
    owner: reviewer
    detail: "Review Worker report validator for backward compatibility and clear failures."

### Task_4: Add Validator Fixtures
- type: test
- owns:
  - `plugins/coding-agent-orchestration-harness/tests/fixtures/valid-worker-report.yaml`
  - `plugins/coding-agent-orchestration-harness/tests/fixtures/invalid-worker-report-missing-validation.yaml`
  - `plugins/coding-agent-orchestration-harness/tests/fixtures/invalid-worker-report-done-with-failed-required-validation.yaml`
  - `plugins/coding-agent-orchestration-harness/tests/fixtures/valid-plan.md`
  - `plugins/coding-agent-orchestration-harness/tests/fixtures/invalid-plan-missing-validation-owner.md`
  - `plugins/coding-agent-orchestration-harness/tests/fixtures/valid-ui-worker-report-with-probes.yaml`
- depends_on: [Task_2, Task_3]
- description: |
  Add minimal valid and invalid fixtures documenting expected validator behavior.
- acceptance:
  - Valid fixtures pass their validators.
  - Invalid fixtures fail for the intended reason.
  - Fixtures stay small and readable.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "python plugins/coding-agent-orchestration-harness/scripts/run_validation_smoke_tests.py, after Task_5"
  - kind: review
    required: true
    owner: reviewer
    detail: "Review fixtures for expected behavior coverage."

### Task_5: Add Smoke Test Runner
- type: test
- owns:
  - `plugins/coding-agent-orchestration-harness/scripts/run_validation_smoke_tests.py`
- depends_on: [Task_1, Task_2, Task_3, Task_4]
- description: |
  Add a simple runner that executes package validator, plan validator, Worker report validator, and Python compile checks.
- acceptance:
  - Runner exits 0 when expected passes/fails are correct.
  - Runner prints clear command summaries.
  - Runner validates both valid and invalid fixtures.
  - Runner compiles new Python scripts.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "python -m py_compile plugins/coding-agent-orchestration-harness/scripts/run_validation_smoke_tests.py"
  - kind: command
    required: true
    owner: worker
    detail: "python plugins/coding-agent-orchestration-harness/scripts/run_validation_smoke_tests.py"
  - kind: review
    required: true
    owner: reviewer
    detail: "Reviewer checks smoke runner expected-pass/expected-fail logic."

## Task Waves (explicit parallel dispatch sets)

- Wave 1 (parallel): [Task_1, Task_2, Task_3]
- Wave 2 (parallel): [Task_4]
- Wave 3 (parallel): [Task_5]

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
- Remove new validators and fixtures, leaving existing Worker report validator behavior intact if extension causes compatibility issues.

## Progress Log (append-only)

- 2026-05-09 00:00 Plan drafted: [Task_1, Task_2, Task_3, Task_4, Task_5]
  - Summary: Initial implementation plan created.
  - Validation evidence: Plan format self-check.
  - Notes: Awaiting approval before execution.
- 2026-05-09 00:00 Plan approved and started: [Task_1, Task_2, Task_3, Task_4, Task_5]
  - Summary: User accepted the open-question recommendation and requested implementation.
  - Validation evidence: User approval in conversation.
  - Notes: Dedicated branch `codex-contract-validators-fixtures`, stacked on `codex-wave-integration-closeout`.
- 2026-05-09 00:00 Wave 1 completed: [Task_1, Task_2, Task_3]
  - Summary: Added package validator, plan validator, and extended Worker report validator.
  - Validation evidence: Python compile checks passed through `run_validation_smoke_tests.py`; package validator passed; plan valid/invalid fixtures behaved as expected; Worker raw YAML, message-file, task-contract, and `ui_probes` paths behaved as expected.
  - Notes: Package validator warns for uncertain adapter duplication heuristics and fails deterministic structure issues.
- 2026-05-09 00:00 Wave 2 completed: [Task_4]
  - Summary: Added valid and invalid plan/report fixtures plus a Worker message-file fixture and task-contract fixture for validator coverage.
  - Validation evidence: Smoke runner exercised all fixtures with expected exit codes.
  - Notes: Extra fixtures support `--message-file` and `--task-contract` coverage beyond the minimum fixture list.
- 2026-05-09 00:00 Wave 3 completed: [Task_5]
  - Summary: Added `run_validation_smoke_tests.py` to compile validators and execute package/plan/report validation checks.
  - Validation evidence: `python plugins/coding-agent-orchestration-harness/scripts/run_validation_smoke_tests.py` exited 0.
  - Notes: Expected invalid-fixture errors are printed during the smoke run and treated as pass conditions.

## Decision Log (append-only; re-plans and major discoveries)

- 2026-05-09 00:00 Decision:
  - Trigger / new insight: Harness needs strict contract validation without brittle prose matching.
  - Plan delta (what changed): Validators and fixtures grouped into one plan.
  - Tradeoffs considered: Hard-fail contracts; warn or skip subjective strategy checks.
  - User approval: yes

## Notes
- Risks:
  - Markdown plan parsing can become brittle. Prefer clear section/task heuristics and helpful errors.
- Edge cases:
  - PyYAML dependency is already used by the Worker report validator; keep dependency behavior consistent.
