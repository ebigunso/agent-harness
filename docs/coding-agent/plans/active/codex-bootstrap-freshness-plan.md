# Plan: Codex Bootstrap Freshness

- status: in_progress
- generated: 2026-05-09
- last_updated: 2026-05-09
- work_type: code

## Goal
- Add lightweight dry-run, check, verify, and manifest support to Codex bootstrap so installed templates can be detected as stale without changing the loader-only Codex architecture.

## Definition of Done
- Existing bootstrap behavior remains compatible.
- `--dry-run` prints planned writes/skips without writing files.
- `--check` compares installed files against source templates and reports stale/missing/modified state.
- `--verify` asserts required installed files and optional AGENTS block presence.
- Managed install manifest can be written and includes SHA-256 hashes.
- Temporary user-scope and repo-scope smoke tests pass without touching real `~/.codex`.

## Scope / Non-goals
- Scope:
  - Update `install_codex_harness.py`.
  - Add manifest read/write/hash helpers.
  - Add temporary-dir smoke coverage through the validation smoke runner or dedicated bootstrap checks.
  - Update bootstrap documentation.
- Non-goals:
  - Do not write to the developer's real `~/.codex` during tests.
  - Do not change Codex loader-only `AGENTS.md` design.
  - Do not add active Codex agents directly under plugin discovery paths.

## Context (workspace)
- Related files/areas:
  - `plugins/coding-agent-orchestration-harness/skills/codex-harness-bootstrap/scripts/install_codex_harness.py`
  - `plugins/coding-agent-orchestration-harness/codex/agent-templates/`
  - `plugins/coding-agent-orchestration-harness/codex/snippets/AGENTS.md`
  - `plugins/coding-agent-orchestration-harness/references/codex-app-connector-policy-*.md`
  - `plugins/coding-agent-orchestration-harness/scripts/run_validation_smoke_tests.py`
- Existing patterns or references:
  - `docs/coding-agent-orchestration-harness/decisions/ADR-I-0002-codex-bootstrap-and-loader-strategy.md`
- Repo reference docs consulted:
  - `docs/coding-agent/rules/index.md`
  - `docs/coding-agent/rules/common.md`
  - `docs/coding-agent/rules/orchestrator.md`

## Open Questions (max 3)
- Q1: resolved. Manifest writing should be default-on for normal installs, with a `--no-write-manifest` escape hatch.

## Assumptions
- A1: Default install remains copy-based and compatible with existing flags.
- A2: `--check` should not mutate files.
- A3: Hash comparisons use source templates as the source of truth.
- A4: Freshness checks are most useful when normal installs leave a managed manifest by default.

## Tasks

### Task_1: Refactor Bootstrap Into Testable Operations
- type: impl
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/codex-harness-bootstrap/scripts/install_codex_harness.py`
- depends_on: []
- description: |
  Separate planning, copying, instructions management, manifest generation, check, and verify logic enough to support new flags.
- acceptance:
  - Existing flags still parse.
  - Install planning can be reused by install, dry-run, check, and verify paths.
  - No behavior change for default install unless manifest writing is intentionally enabled.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "python -m py_compile plugins/coding-agent-orchestration-harness/skills/codex-harness-bootstrap/scripts/install_codex_harness.py"
  - kind: review
    required: true
    owner: reviewer
    detail: "Review refactor for behavior preservation."

### Task_2: Add Dry Run And Check Modes
- type: impl
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/codex-harness-bootstrap/scripts/install_codex_harness.py`
- depends_on: [Task_1]
- description: |
  Add `--dry-run` and `--check` modes.
- acceptance:
  - `--dry-run` prints planned target files and whether each would write or skip.
  - `--dry-run` does not create directories, copy files, or write AGENTS.md.
  - `--check` reports missing, stale, matching, and locally modified installed files.
  - `--check` exits non-zero when required files are missing/stale/modified.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "Run bootstrap --dry-run against a temporary --codex-home and verify no files are created."
  - kind: command
    required: true
    owner: worker
    detail: "Run bootstrap --check against a temporary stale install and verify stale files are reported."
  - kind: review
    required: true
    owner: reviewer
    detail: "Review mode behavior for non-mutating guarantees."

### Task_3: Add Verify And Manifest Support
- type: impl
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/codex-harness-bootstrap/scripts/install_codex_harness.py`
- depends_on: [Task_1]
- description: |
  Add `--verify` and optional manifest writing for installed files.
- acceptance:
  - Manifest path is `.coding-agent-orchestration-harness-install.json` in the target agents directory.
  - Manifest includes plugin name, version, installed_at, scope, and file hashes.
  - `--verify` asserts required installed files exist.
  - `--verify` can verify optional user AGENTS block when user-scope instructions are expected.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "Run bootstrap install with manifest in temporary user scope and verify manifest hashes."
  - kind: command
    required: true
    owner: worker
    detail: "Run bootstrap --verify in temporary user and repo scopes."
  - kind: review
    required: true
    owner: reviewer
    detail: "Review manifest schema and verify behavior."

### Task_4: Add Bootstrap Smoke Tests
- type: test
- owns:
  - `plugins/coding-agent-orchestration-harness/scripts/run_validation_smoke_tests.py`
  - `plugins/coding-agent-orchestration-harness/tests/fixtures/`
- depends_on: [Task_2, Task_3]
- description: |
  Add temporary-directory bootstrap checks to the smoke test runner or a helper invoked by it.
- acceptance:
  - Tests use temporary `--codex-home`.
  - Tests use temporary repo root for repo scope.
  - Tests do not write to real home or real repo `.codex`.
  - Tests cover dry-run, normal install, check, stale detection, and verify.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "python plugins/coding-agent-orchestration-harness/scripts/run_validation_smoke_tests.py"
  - kind: review
    required: true
    owner: reviewer
    detail: "Review tests for isolation from real user Codex state."

### Task_5: Update Bootstrap Documentation
- type: docs
- owns:
  - `README.md`
  - `plugins/coding-agent-orchestration-harness/README.md`
  - `plugins/coding-agent-orchestration-harness/skills/codex-harness-bootstrap/SKILL.md`
- depends_on: [Task_2, Task_3]
- description: |
  Document new bootstrap flags and freshness workflow.
- acceptance:
  - Docs mention `--dry-run`, `--check`, `--verify`, and manifest behavior.
  - Docs preserve existing default install commands.
  - Docs warn tests/checks should use temporary locations when appropriate.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Review docs for accurate bootstrap behavior and no loader design drift."

## Task Waves (explicit parallel dispatch sets)

- Wave 1 (parallel): [Task_1]
- Wave 2 (parallel): [Task_2, Task_3]
- Wave 3 (parallel): [Task_4, Task_5]

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
- Revert bootstrap script changes and docs. Existing installed Codex templates are not modified by tests because temporary directories are required.

## Progress Log (append-only)

- 2026-05-09 00:00 Plan drafted: [Task_1, Task_2, Task_3, Task_4, Task_5]
  - Summary: Initial implementation plan created.
  - Validation evidence: Plan format self-check.
  - Notes: Awaiting approval before execution.
- 2026-05-09 00:00 Plan approved and started: [Task_1, Task_2, Task_3, Task_4, Task_5]
  - Summary: User accepted the open-question recommendation and requested implementation.
  - Validation evidence: User approval in conversation.
  - Notes: Dedicated branch `codex-bootstrap-freshness`, stacked on `codex-contract-validators-fixtures`.

## Decision Log (append-only; re-plans and major discoveries)

- 2026-05-09 00:00 Decision:
  - Trigger / new insight: ADR-I-0002 notes stale installed Codex agents as a tradeoff.
  - Plan delta (what changed): Added freshness checks without changing loader architecture.
  - Tradeoffs considered: Keep default compatible; add non-mutating modes for safety.
  - User approval: yes

## Notes
- Risks:
  - Interactive prompts can complicate smoke tests. Prefer non-interactive flags in tests.
- Edge cases:
  - `--dry-run` must avoid creating the target directory as well as avoiding file writes.
