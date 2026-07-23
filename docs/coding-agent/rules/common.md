---
rule_schema_version: 2
suite_id: "rules-20260513-b80f05e"
rule_file: "common"
last_updated: "2026-07-24"
---

# Common Repository Rules

## Repository Reference Documents

- `plugins/coding-agent-orchestration-harness/README.md`: plugin layout, runtime paths, validators, Codex bootstrap commands, and ADR location.
- Decision records: follow `docs/coding-agent-orchestration-harness/decisions/`; match the existing ADRs' ADR-D/ADR-I numbering and sections (durable architecture and implementation decisions for the harness).
- `docs/coding-agent/plans/completed/`: completed implementation plans and validation history.
- `docs/coding-agent/lessons.md`: recurring mistakes and local prevention rules.

## Repository-Specific Validation Commands

Run plugin validators from `plugins/coding-agent-orchestration-harness/` unless noted:

- `python scripts/validate_harness_package.py`
- `python scripts/run_validation_smoke_tests.py`
- `python skills/plan-format/scripts/validate_plan.py --file tests/fixtures/valid-plan.md --mode balanced`
- `python skills/subagent-report-contract/scripts/validate_worker_report.py --file tests/fixtures/valid-worker-report.yaml`
- `python skills/subagent-report-contract/scripts/validate_worker_report.py --file tests/fixtures/valid-worker-report-reviewer-candidate.yaml` when reviewer rule-candidate audience support is in scope.
- From repository root: `git diff --check` before committing or publishing.

## Repo Safety / Boundaries

- Preserve role boundaries in the orchestration harness unless a task explicitly requires changing them.
- Only the Orchestrator edits `docs/coding-agent/rules/*.md`.
- Keep shared workflow semantics in skills/references; runtime adapters should route to shared skills rather than inline full checklists, with one deliberate exception: role workflow/output contracts are replicated into each runtime's instruction block per `runtime-adapter-contract` (edit all three copies together and confirm sync).
- Do not add a universal repository quality-gate runner that assumes arbitrary target repositories use a specific language or task runner.
- Do not treat untracked files as baseline or stage them silently.

## Repo Naming / Structure

- First-party orchestration skills live under `plugins/coding-agent-orchestration-harness/skills/<skill-name>/`.
- Keep first-party skill content version agnostic; track rollout phase and evolution plans outside the skill unless the version is part of a public compatibility contract.
- Store runtime payload templates as inert plugin files unless the task intentionally installs them into a runtime discovery path.
- Design and implementation decisions live under `docs/coding-agent-orchestration-harness/decisions/`.

## Global Migration Candidates

- When adding package validation for enum/schema changes, check the exact enum owner or contract field rather than a broad substring.
