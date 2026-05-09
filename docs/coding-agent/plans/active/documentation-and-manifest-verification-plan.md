# Plan: Documentation And Manifest Verification

- status: in_progress
- generated: 2026-05-09
- last_updated: 2026-05-09
- work_type: docs

## Goal
- Update user-facing and plugin-local documentation to describe explicit Orchestrator invocation, role mapping, UI validation tiers, and balanced validation philosophy.

## Definition of Done
- Root README accurately describes runtime operation model.
- Plugin-local README exists and concisely documents runtime paths, role map, key skills, validators, and bootstrap commands.
- Docs link to ADRs and the canonical runtime role map.
- Manifests parse and require no structural changes unless validation finds one.

## Scope / Non-goals
- Scope:
  - Update `README.md`.
  - Add `plugins/coding-agent-orchestration-harness/README.md`.
  - Verify manifests and directory discovery.
- Non-goals:
  - Do not imply auto skill discovery is primary activation for Copilot/Claude.
  - Do not duplicate full orchestration workflow in README.
  - Do not list individual skills in manifests unless required by runtime validation.

## Context (workspace)
- Related files/areas:
  - `README.md`
  - `plugins/coding-agent-orchestration-harness/README.md`
  - `plugins/coding-agent-orchestration-harness/.github/plugin/plugin.json`
  - `plugins/coding-agent-orchestration-harness/.claude-plugin/plugin.json`
  - `plugins/coding-agent-orchestration-harness/.codex-plugin/plugin.json`
  - `docs/coding-agent-orchestration-harness/decisions/`
  - `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/runtime-role-map.md`
- Existing patterns or references:
  - Existing root README runtime support section.
  - Existing ADRs for runtime adapter layout and Codex bootstrap.
- Repo reference docs consulted:
  - `docs/coding-agent/rules/index.md`
  - `docs/coding-agent/rules/common.md`
  - `docs/coding-agent/rules/orchestrator.md`

## Open Questions (max 3)
- Q1: resolved. Optimize the root README for users; optimize the plugin-local README for maintainers while keeping enough user-facing runtime paths to orient both audiences.

## Assumptions
- A1: Root README should stay high-level and avoid detailed workflow mechanics.
- A2: Plugin-local README can include more plugin-specific paths and validator commands.
- A3: Manifest structure probably does not need changes because shared skill directories are already configured.
- A4: Plugin-local docs should be concise but more operational than the root README.

## Tasks

### Task_1: Update Root README Runtime Model
- type: docs
- owns:
  - `README.md`
- depends_on: []
- description: |
  Add concise documentation for explicit Orchestrator invocation, Codex loader behavior, shared skills, role names, UI validation, and validation philosophy.
- acceptance:
  - README says Copilot/Claude users explicitly invoke/select the Orchestrator.
  - README says Codex uses loader instructions and installed templates.
  - README says skills are shared capability modules.
  - README includes role map table and points to canonical role-map reference.
  - README explains Worker UI probes, Researcher UI research, and Reviewer independent evidence.
  - README explains strict contracts/evidence and flexible prose/strategy.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Review README for accuracy and no implication that auto discovery is the main Copilot/Claude activation path."

### Task_2: Add Plugin-Local README
- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/README.md`
- depends_on: []
- description: |
  Add concise plugin-local documentation for runtime paths, role map, key skills, validators, and bootstrap commands.
- acceptance:
  - README identifies Copilot, Claude, and Codex adapter paths.
  - README links to canonical role map and ADRs.
  - README lists key skills without restating full behavior.
  - README lists validator commands and bootstrap freshness commands.
  - README stays concise.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Review plugin README for maintainability and no duplicated workflow policy."

### Task_3: Verify Manifest Structure
- type: test
- owns:
  - `plugins/coding-agent-orchestration-harness/.github/plugin/plugin.json`
  - `plugins/coding-agent-orchestration-harness/.claude-plugin/plugin.json`
  - `plugins/coding-agent-orchestration-harness/.codex-plugin/plugin.json`
- depends_on: [Task_1, Task_2]
- description: |
  Confirm manifests parse and still point to existing runtime directories.
- acceptance:
  - GitHub/Copilot manifest points to `./agents/` and `./skills/`.
  - Claude manifest points to `./claude/agents/` and `./skills/`.
  - Codex manifest points to `./skills/`.
  - No manifest lists individual skills unless a runtime requirement is discovered.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "python plugins/coding-agent-orchestration-harness/scripts/validate_harness_package.py"
  - kind: review
    required: true
    owner: reviewer
    detail: "Review manifest validation results and docs references."

## Task Waves (explicit parallel dispatch sets)

- Wave 1 (parallel): [Task_1, Task_2]
- Wave 2 (parallel): [Task_3]

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
- Revert README changes and remove plugin-local README if docs prove misleading.

## Progress Log (append-only)

- 2026-05-09 00:00 Plan drafted: [Task_1, Task_2, Task_3]
  - Summary: Initial implementation plan created.
  - Validation evidence: Plan format self-check.
  - Notes: Awaiting approval before execution.
- 2026-05-09 00:00 Plan approved and started: [Task_1, Task_2, Task_3]
  - Summary: User accepted the open-question recommendation and requested implementation.
  - Validation evidence: User approval in conversation.
  - Notes: Dedicated branch `codex-docs-manifest-verification`, stacked on `codex-bootstrap-freshness`.

## Decision Log (append-only; re-plans and major discoveries)

- 2026-05-09 00:00 Decision:
  - Trigger / new insight: Runtime operation and validation philosophy need user-facing documentation after structural changes.
  - Plan delta (what changed): Documentation work separated into a final plan.
  - Tradeoffs considered: Keep README concise and link to canonical references.
  - User approval: yes

## Notes
- Risks:
  - Docs may lag implementation if written too early. Execute this after core skill/validator changes.
- Edge cases:
  - If package validator finds manifest changes are necessary, update docs and manifests together.
