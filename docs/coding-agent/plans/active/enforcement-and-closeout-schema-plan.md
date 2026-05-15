# Plan: Enforcement And Closeout Schema

- status: draft
- generated: 2026-05-16
- last_updated: 2026-05-16
- work_type: mixed

## Goal
- Add structure-only package validation for the remaining routing surfaces and extend closeout validation to model optional governance follow-ups.

## Definition of Done
- Package validator guards packet template routing for the new latent-risk reference files.
- Package validator guards Reviewer prompt snippet vocabulary for the newer lenses.
- Package validator guards wave integration aggregation of `harness_migration_candidates`.
- Closeout validator accepts optional governance summary fields.
- Closeout validation has fixture coverage for base valid, governance-valid, and governance-invalid summaries.
- Smoke validation runs the closeout validator against those fixtures, including an expected failure for invalid governance shape.
- Required validation passes or is explicitly waived with evidence.

## Scope / Non-goals
- Scope:
  - `plugins/coding-agent-orchestration-harness/scripts/validate_harness_package.py`
  - `plugins/coding-agent-orchestration-harness/scripts/run_validation_smoke_tests.py`
  - `plugins/coding-agent-orchestration-harness/skills/wave-integration/scripts/validate_closeout.py`
  - `plugins/coding-agent-orchestration-harness/tests/fixtures/valid-closeout-plan.md`
  - `plugins/coding-agent-orchestration-harness/tests/fixtures/valid-closeout-summary.yaml`
  - `plugins/coding-agent-orchestration-harness/tests/fixtures/valid-closeout-summary-with-governance.yaml`
  - `plugins/coding-agent-orchestration-harness/tests/fixtures/invalid-closeout-governance-shape.yaml`
- Non-goals:
  - Do not edit packet, snippet, or integration prose directly; those belong to the operational routing plan.
  - Do not make governance required in closeout validation yet.
  - Do not add broad prose-quality validation beyond objective routing tokens.

## Context (workspace)
- Related files/areas:
  - `plugins/coding-agent-orchestration-harness/skills/wave-integration/references/reviewer-packet-template.md`
  - `plugins/coding-agent-orchestration-harness/skills/subagent-strategy/references/prompt-snippets.md`
  - `plugins/coding-agent-orchestration-harness/skills/wave-integration/references/integration-checklist.md`
  - `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/completion-closeout.md`
  - `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/final-response-contract.md`
- Existing patterns or references:
  - Package validation should protect structural decisions, not editable style.
  - Closeout currently models plan status, reviewer, tasks, validations, and blockers; governance is a next optional shape.
- Repo reference docs consulted:
  - `docs/coding-agent/rules/index.md`
  - `docs/coding-agent/rules/common.md`
  - `docs/coding-agent/rules/orchestrator.md`
  - `docs/coding-agent/rules/worker.md`

## Open Questions (max 3)
- Q1: None.

## Assumptions
- A1: Validator additions should be exact enough to catch stale routing surfaces but flexible about prose.
- A2: Optional governance support is the correct first hardening step; required governance can be added later when report-to-closeout propagation is implemented.
- A3: No existing closeout fixtures are present; add fixture files instead of embedding ad hoc validation samples inline.
- A4: Do not reuse `valid-plan.md` for closeout validation because closeout requires both summary `plan_status` and plan header status to be `done`.

## Tasks

### Task_1: Guard Reviewer Packet Template Routing
- type: test
- owns:
  - `plugins/coding-agent-orchestration-harness/scripts/validate_harness_package.py`
- depends_on: []
- description: |
  Add structure-only package validation requiring `reviewer-packet-template.md` to mention the four newer latent-risk reference files.
- acceptance:
  - Validator checks `review-latent-risk-public-api.md`.
  - Validator checks `review-latent-risk-entrypoints-admission.md`.
  - Validator checks `review-latent-risk-diagnostics.md`.
  - Validator checks `review-latent-risk-build-ci.md`.
  - Error messages identify `reviewer-packet-template.md` as the failing surface.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "python scripts/validate_harness_package.py"
  - kind: review
    required: true
    owner: reviewer
    detail: "Confirm checks are structural token checks and do not lock exact section wording."

### Task_2: Guard Reviewer Prompt Snippet Vocabulary
- type: test
- owns:
  - `plugins/coding-agent-orchestration-harness/scripts/validate_harness_package.py`
- depends_on: []
- description: |
  Add package validation requiring the Reviewer latent-risk snippet to mention public API, diagnostics, build cfg/features or strict-CI, entrypoint intent/admission, collection semantics, and runtime model compatibility.
- acceptance:
  - Validator checks for public API vocabulary.
  - Validator checks for diagnostics vocabulary.
  - Validator accepts build cfg/features or strict-CI vocabulary.
  - Validator checks for entrypoint intent/admission vocabulary.
  - Validator checks for collection semantics and runtime model compatibility.
  - Error messages identify `prompt-snippets.md` and the Reviewer latent-risk snippet context.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "python scripts/validate_harness_package.py"
  - kind: review
    required: true
    owner: reviewer
    detail: "Confirm vocabulary checks do not require the full snippet to match exact text."

### Task_3: Guard Wave Integration HMC Aggregation
- type: test
- owns:
  - `plugins/coding-agent-orchestration-harness/scripts/validate_harness_package.py`
- depends_on: []
- description: |
  Add package validation requiring `integration-checklist.md` to mention `harness_migration_candidates`.
- acceptance:
  - Validator checks `integration-checklist.md` for `harness_migration_candidates`.
  - Error message points to wave integration checklist routing.
  - Check complements existing Worker report schema validation rather than duplicating it.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "python scripts/validate_harness_package.py"
  - kind: review
    required: true
    owner: reviewer
    detail: "Confirm this catches dropped wave-integration routing without over-constraining prose."

### Task_4: Add Optional Governance To Closeout Validation
- type: test
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/wave-integration/scripts/validate_closeout.py`
  - `plugins/coding-agent-orchestration-harness/tests/fixtures/valid-closeout-plan.md`
  - `plugins/coding-agent-orchestration-harness/tests/fixtures/valid-closeout-summary.yaml`
  - `plugins/coding-agent-orchestration-harness/tests/fixtures/valid-closeout-summary-with-governance.yaml`
  - `plugins/coding-agent-orchestration-harness/tests/fixtures/invalid-closeout-governance-shape.yaml`
  - `plugins/coding-agent-orchestration-harness/scripts/run_validation_smoke_tests.py`
- depends_on:
  - Task_1
  - Task_2
  - Task_3
- description: |
  Extend the structured closeout validator to accept an optional `governance` object with lessons, repo rule updates, harness migration candidates, and waivers.
- acceptance:
  - `governance.lessons_recorded` is accepted as a boolean when present.
  - `governance.repo_rule_updates` is accepted as a list when present.
  - `governance.harness_migration_candidates` is accepted as a list when present.
  - `governance.waivers` is accepted as a list when present.
  - Existing closeout summaries without `governance` remain valid.
  - Invalid governance field types are rejected when present.
  - New closeout fixtures are added under `tests/fixtures/` rather than embedded inline in scripts.
  - `valid-closeout-plan.md` has plan header `status: done`.
  - Smoke tests run `validate_closeout.py` for base valid and governance-valid summaries.
  - Smoke tests run `validate_closeout.py` for invalid governance shape and expect exit code `3`.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "python skills/wave-integration/scripts/validate_closeout.py --plan tests/fixtures/valid-closeout-plan.md --summary tests/fixtures/valid-closeout-summary.yaml"
  - kind: command
    required: true
    owner: worker
    detail: "python skills/wave-integration/scripts/validate_closeout.py --plan tests/fixtures/valid-closeout-plan.md --summary tests/fixtures/valid-closeout-summary-with-governance.yaml"
  - kind: command
    required: true
    owner: worker
    detail: "python skills/wave-integration/scripts/validate_closeout.py --plan tests/fixtures/valid-closeout-plan.md --summary tests/fixtures/invalid-closeout-governance-shape.yaml must fail with exit code 3"
  - kind: command
    required: true
    owner: worker
    detail: "python scripts/run_validation_smoke_tests.py"
  - kind: command
    required: true
    owner: worker
    detail: "python scripts/validate_harness_package.py"
  - kind: review
    required: true
    owner: reviewer
    detail: "Confirm optional governance support aligns with completion closeout and final response contract without prematurely requiring governance."

## Task Waves (explicit parallel dispatch sets)

Interpretation:
- Tasks listed in the same wave are intended to be dispatched in parallel by default when `owns` are disjoint and dependencies are met.
- Waves are executed sequentially.

- Wave 1 (parallel): [Task_1, Task_2, Task_3]
- Wave 2 (parallel): [Task_4]

## E2E / Visual Validation Spec

- Not applicable; no UI or user flow is impacted.

## Rollback / Safety
- Revert validator changes as a unit if validation behavior becomes too broad.
- If closeout governance needs to become required based on implementation findings, pause and replan because that changes compatibility expectations.

## Progress Log (append-only)

- 2026-05-16 00:00 Plan drafted.
  - Summary: Created scoped implementation plan for package validation guards and optional closeout governance shape.
  - Validation evidence: Not run; draft plan only.
  - Notes: Research waived because the user supplied current-file findings and work is limited to plan creation.

## Decision Log (append-only; re-plans and major discoveries)

- 2026-05-16 00:00 Decision: Keep enforcement separate from prose updates.
  - Trigger / new insight: Validator checks should assert completed routing work, not drive placeholder prose.
  - Plan delta (what changed): This plan depends conceptually on operational routing updates being present but keeps its write scope to validators and tests.
  - Tradeoffs considered: Combining validators with prose edits would make review harder and risk overfitting implementation text.
  - User approval: yes, user requested actual plan files after reviewing the split.

- 2026-05-16 00:00 Decision: Add closeout fixtures and smoke-test coverage.
  - Trigger / new insight: User clarified there are no existing closeout fixtures and `run_validation_smoke_tests.py` only py-compiles `validate_closeout.py`.
  - Plan delta (what changed): Task_4 now owns explicit closeout fixtures and smoke-test updates, including expected exit code `3` for invalid governance.
  - Tradeoffs considered: Inline ad hoc samples would be faster but would not establish reusable fixture coverage.
  - User approval: yes, user provided the fixture and smoke-test direction.

## Notes
- Risks:
  - Validator checks can become too brittle if they assert exact prose.
  - Optional governance schema could accidentally become required if defaults are mishandled.
- Edge cases:
  - The invalid governance fixture should fail for governance shape, not because the plan is not done.
