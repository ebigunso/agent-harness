# Plan: Package Validation Guards For Clean Split

- status: done
- generated: 2026-05-14
- last_updated: 2026-05-14
- work_type: test

## Goal

- Add package validation guards that prevent regression back to conflating repo rule candidates with harness/global migration candidates.

## Definition of Done

- Package validation fails on stale `intended_home` report contract usage.
- Package validation fails if `validate_worker_report.py` defines `ALLOWED_INTENDED_HOME`.
- Package validation fails if lesson-producing adapters contain old lesson targets `global-skill` or `references/*`.
- Package validation fails if Orchestrator adapters or post-correction guidance allow ordinary target-repository work to edit bundled harness content directly.
- Package validation fails if rulebook templates or references reintroduce `Global Migration Candidates` or `global_candidate` routing.
- Package validation checks that promotion guidelines contain harness migration candidate guidance.
- Existing smoke tests cover the new guards.

## Scope / Non-goals

- Scope:
  - Update `validate_harness_package.py` and related smoke-test expectations.
  - Add deterministic text guards for the clean split.
- Non-goals:
  - Do not validate exact prose beyond deterministic forbidden/required tokens.
  - Do not add runtime behavior.
  - Do not add these guards before the dependent docs and schemas have been updated.

## Context (workspace)

- Related files/areas:
  - `plugins/coding-agent-orchestration-harness/scripts/validate_harness_package.py`
  - `plugins/coding-agent-orchestration-harness/scripts/run_validation_smoke_tests.py`
  - `plugins/coding-agent-orchestration-harness/skills/subagent-report-contract/SKILL.md`
  - `plugins/coding-agent-orchestration-harness/skills/subagent-report-contract/scripts/validate_worker_report.py`
  - `plugins/coding-agent-orchestration-harness/agents/Reviewer.md`
  - `plugins/coding-agent-orchestration-harness/claude/agents/harness-reviewer.md`
  - `plugins/coding-agent-orchestration-harness/codex/agent-templates/harness_reviewer.toml`
  - `plugins/coding-agent-orchestration-harness/skills/improvement-loop/SKILL.md`
  - `plugins/coding-agent-orchestration-harness/skills/improvement-loop/references/promotion-guidelines.md`
  - `plugins/coding-agent-orchestration-harness/skills/rulebook/references/rule-suite-templates.md`
  - `plugins/coding-agent-orchestration-harness/skills/rulebook/references/rules-files.md`
- Existing patterns or references:
  - Existing package validator already performs deterministic structural and content checks.
  - Existing smoke runner compiles validators and executes package validation.
- Repo reference docs consulted:
  - `docs/coding-agent/plans/completed/contract-first-validators-and-fixtures-plan.md`

## Open Questions (max 3)

- Q1: resolved. Guards should scan only authoritative current surfaces, not completed plans, historical docs, hand-off artifacts, or unrelated documentation.

## Assumptions

- A1: This plan runs last after the five design/documentation/schema plans have landed.
- A2: Guards should fail only on deterministic tokens or missing required anchor phrases.
- A3: Historical completed plans may mention old terms and should not be scanned.

## Tasks

### Task_1: Define Guard Surface And Failure Messages

- type: design
- owns:
  - `plugins/coding-agent-orchestration-harness/scripts/validate_harness_package.py`
- depends_on: []
- description: |
  Add helper structure for deterministic forbidden-token and required-token checks with actionable error messages.
- acceptance:
  - Guard implementation names the file being checked and the stale or missing concept.
  - Checks are limited to current authoritative harness docs/scripts/adapters.
  - Failure messages explain the new destination or expected replacement.
  - The implementation avoids scanning `docs/coding-agent/plans/completed`.
- validation:
  - kind: review
    required: true
    owner: worker
    detail: "Review guard list for deterministic behavior and low brittleness before adding all checks."

### Task_2: Add Report Contract And Validator Guards

- type: test
- owns:
  - `plugins/coding-agent-orchestration-harness/scripts/validate_harness_package.py`
- depends_on: [Task_1]
- description: |
  Guard the report contract and Worker report validator against old rule candidate routing.
- acceptance:
  - Package validator fails if `subagent-report-contract/SKILL.md` contains `intended_home`.
  - Package validator fails if `validate_worker_report.py` contains `ALLOWED_INTENDED_HOME`.
  - Package validator optionally checks that report contract mentions `harness_migration_candidates`.
  - Failure messages point to `harness_migration_candidates` and repo-local `rule_candidates`.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "Run `python -m py_compile plugins/coding-agent-orchestration-harness/scripts/validate_harness_package.py`."

### Task_3: Add Runtime Adapter Guards

- type: test
- owns:
  - `plugins/coding-agent-orchestration-harness/scripts/validate_harness_package.py`
- depends_on: [Task_1]
- description: |
  Guard lesson-producing runtime surfaces against old lesson promotion targets.
- acceptance:
  - Package validator fails if Researcher or Reviewer authoritative surfaces contain `global-skill`.
  - Package validator fails if Researcher or Reviewer authoritative surfaces contain `references/*` as a lesson promotion target.
  - Guard covers Copilot, Claude, and Codex Researcher/Reviewer adapters.
  - Guard covers Copilot and Claude Orchestrator staging-boundary wording.
  - Guard does not reject legitimate path references to plugin references outside the old lesson target context unless implementation intentionally chooses strict token scanning for those files.
- validation:
  - kind: review
    required: true
    owner: worker
    detail: "Review adapter guard for avoiding false positives on legitimate reference paths."

### Task_4: Add Improvement Loop And Rulebook Guards

- type: test
- owns:
  - `plugins/coding-agent-orchestration-harness/scripts/validate_harness_package.py`
- depends_on: [Task_1]
- description: |
  Guard improvement-loop and rulebook docs against reintroducing direct first-party promotion and global migration sections in role rule files.
- acceptance:
  - Package validator fails if `promotion-guidelines.md` lacks `harness migration candidate`.
  - Package validator fails if improvement-loop ordinary runtime guidance instructs direct first-party skill/reference updates.
  - Package validator fails if the post-correction checklist instructs direct first-party skill/reference updates or old Global Migration Candidate rule placeholders.
  - Package validator fails if `rule-suite-templates.md` contains `Global Migration Candidates`.
  - Package validator fails if `rules-files.md` routes `global_candidate`.
  - Failure messages point to `docs/coding-agent/skill-candidates.md` and `docs/coding-agent/skill-drafts/*.md`.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "Run targeted package validator after checks are added."

### Task_5: Update Smoke Tests And Run Full Validation

- type: test
- owns:
  - `plugins/coding-agent-orchestration-harness/scripts/run_validation_smoke_tests.py`
  - possible `plugins/coding-agent-orchestration-harness/tests/fixtures/*`
- depends_on: [Task_2, Task_3, Task_4]
- description: |
  Ensure smoke tests execute the strengthened package validator and add targeted negative coverage only if the current smoke framework supports it without brittle temporary rewrites.
- acceptance:
  - Smoke runner executes package validation and fails if new guards fail.
  - Negative coverage is added only if it can be done safely with temporary copied fixture trees or unit-style helper tests.
  - Python compile checks pass.
  - Full smoke suite passes.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "Run `python -m py_compile plugins/coding-agent-orchestration-harness/scripts/validate_harness_package.py plugins/coding-agent-orchestration-harness/scripts/run_validation_smoke_tests.py`."
  - kind: command
    required: true
    owner: worker
    detail: "Run `python plugins/coding-agent-orchestration-harness/scripts/run_validation_smoke_tests.py`."

### Task_6: Final Guard Review

- type: review
- owns: []
- depends_on: [Task_2, Task_3, Task_4, Task_5]
- description: |
  Review the guard set for completeness, false-positive risk, and alignment with the clean split design.
- acceptance:
  - Guards cover every concrete protection listed in the hand-off document.
  - Guards avoid broad prose policing.
  - Existing validation passes.
  - Reviewer confirms this plan should run only after dependent clean-split changes land.
- validation:
  - kind: command
    required: true
    owner: reviewer
    detail: "Run `python plugins/coding-agent-orchestration-harness/scripts/run_validation_smoke_tests.py` or review equivalent Worker evidence."
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review against this plan and the hand-off guard list."

## Task Waves (explicit parallel dispatch sets)

- Wave 1 (parallel): [Task_1]
- Wave 2 (parallel): [Task_2, Task_3, Task_4]
- Wave 3 (parallel): [Task_5]
- Wave 4 (parallel): [Task_6]

## E2E / Visual Validation Spec

- Not applicable. This plan changes static validation scripts and smoke tests only.

## Rollback / Safety

- Revert package validator and smoke-test changes together if false positives block legitimate harness maintenance.
- Do not use broad repository-wide forbidden-token scans that would catch historical plans or external documents.

## Progress Log (append-only)

- 2026-05-14 Plan drafted.
  - Summary: Added implementation plan for final package validation guards that enforce the clean split.
  - Validation evidence: Plan-format self-check.
  - Notes: Awaiting approval before execution; should run after the other five plans.
- 2026-05-14 Waves 1-3 completed: [Task_1, Task_2, Task_3, Task_4, Task_5]
  - Summary: Stacked prerequisite clean-split work, resolved documentation conflicts, and added deterministic package guards for removed schema/routing targets.
  - Validation evidence: `python -m py_compile plugins\coding-agent-orchestration-harness\scripts\validate_harness_package.py plugins\coding-agent-orchestration-harness\scripts\run_validation_smoke_tests.py` passed; package validation passed; full smoke suite passed.
  - Notes: Guards scan authoritative current surfaces only, not historical plans.
- 2026-05-14 Wave 4 completed: [Task_6]
  - Summary: Strict guard review completed by Orchestrator.
  - Validation evidence: Conflict marker search returned no matches; smoke suite passed.
  - Notes: Reviewer subagent was not used in this desktop session; review was performed directly against the plan acceptance criteria.

## Decision Log (append-only; re-plans and major discoveries)

- 2026-05-14 Decision: Scan authoritative surfaces, not the entire repository.
  - Trigger / new insight: Historical completed plans and hand-off docs may legitimately mention removed shapes.
  - Plan delta (what changed): Guard surface is explicit and limited.
  - Tradeoffs considered: Repo-wide scans are simpler but too noisy for historical documentation.
  - User approval: yes.

## Notes

- Risks:
  - Required-token checks can become brittle if phrasing changes; keep them minimal.
  - Negative tests for package guards may require fixture-tree copying to avoid mutating real plugin files.
- Edge cases:
  - Legitimate plugin reference paths may include `references/`; the guard should target old lesson promotion target wording, especially in Reviewer adapters.
