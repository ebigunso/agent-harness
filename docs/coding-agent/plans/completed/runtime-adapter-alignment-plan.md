# Plan: Runtime Adapter Alignment

- status: done
- generated: 2026-05-09
- last_updated: 2026-05-09
- work_type: mixed

## Goal
- Align Copilot, Claude, and Codex runtime adapters with the shared orchestration skill while preserving runtime-specific behavior and prompt budgets.

## Definition of Done
- Copilot Orchestrator is a medium kernel and remains explicitly user-invocable.
- Claude `harness-orchestrator` is a first-class short kernel with the right skills and role map.
- Codex remains loader-only plus installed templates.
- Runtime adapter maintenance is governed by a dedicated skill.

## Scope / Non-goals
- Scope:
  - Update Copilot Orchestrator adapter.
  - Update Claude Orchestrator adapter.
  - Add `runtime-adapter-contract` skill and references.
  - Add routing from `skills-maintenance`.
  - Verify manifests still use directory discovery.
- Non-goals:
  - Do not rename existing Copilot public agent names.
  - Do not add a large Codex `AGENTS.md` block.
  - Do not duplicate the full workflow in runtime adapters.

## Context (workspace)
- Related files/areas:
  - `plugins/coding-agent-orchestration-harness/agents/Orchestrator.md`
  - `plugins/coding-agent-orchestration-harness/claude/agents/harness-orchestrator.md`
  - `plugins/coding-agent-orchestration-harness/codex/snippets/AGENTS.md`
  - `plugins/coding-agent-orchestration-harness/skills/runtime-adapter-contract/`
  - `plugins/coding-agent-orchestration-harness/skills/skills-maintenance/SKILL.md`
  - `plugins/coding-agent-orchestration-harness/.github/plugin/plugin.json`
  - `plugins/coding-agent-orchestration-harness/.claude-plugin/plugin.json`
  - `plugins/coding-agent-orchestration-harness/.codex-plugin/plugin.json`
- Existing patterns or references:
  - `docs/coding-agent-orchestration-harness/decisions/ADR-I-0001-runtime-adapter-layout.md`
  - `docs/coding-agent-orchestration-harness/decisions/ADR-I-0002-codex-bootstrap-and-loader-strategy.md`
  - `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/runtime-role-map.md`
- Repo reference docs consulted:
  - `docs/coding-agent/rules/index.md`
  - `docs/coding-agent/rules/common.md`
  - `docs/coding-agent/rules/orchestrator.md`

## Open Questions (max 3)
- Q1: resolved. Keep Claude frontmatter minimal unless existing Claude plugin behavior confirms `tools` is valid and useful.

## Assumptions
- A1: Copilot adapter frontmatter should preserve existing tools and `agents`.
- A2: Claude should use `model: inherit`.
- A3: Codex plugin manifest continues to expose only shared skills.
- A4: Claude adapter goals are short prompt budget and runtime compatibility; avoid adding schema surface unless it is known-good.

## Tasks

### Task_1: Compress Copilot Orchestrator Adapter
- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/agents/Orchestrator.md`
- depends_on: []
- description: |
  Replace the copied full workflow with a medium-length Copilot kernel that routes to `orchestration-harness`.
- acceptance:
  - Frontmatter preserves `user-invocable: true`, `disable-model-invocation: true`, tools, and existing Copilot agent names unless a concrete issue is found.
  - Body states the Orchestrator is explicitly selected.
  - Body names the five hard gates, runtime role map, Worker UI probe boundary, and final response summary.
  - Body does not restate every detailed gate procedure.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Review Copilot adapter for explicit entrypoint semantics and no full workflow duplication."

### Task_2: Update Claude Orchestrator Adapter
- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/claude/agents/harness-orchestrator.md`
- depends_on: []
- description: |
  Update the existing Claude Orchestrator into a short Claude-specific kernel with role mapping and relevant skills.
- acceptance:
  - Agent name remains `harness-orchestrator`.
  - Body is materially shorter than Copilot Orchestrator.
  - Skills include orchestration, plan, strategy, report contract, UI probe policy, wave integration guidance, E2E evidence, quality baselines, git, rulebook, improvement, troubleshooting, and skills maintenance.
  - Physical subagents are listed as `harness-researcher`, `harness-worker`, and `harness-reviewer`.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Review Claude adapter for concise kernel and correct role names."

### Task_3: Add Runtime Adapter Contract Skill
- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/runtime-adapter-contract/SKILL.md`
  - `plugins/coding-agent-orchestration-harness/skills/runtime-adapter-contract/references/adapter-maintenance-checklist.md`
  - `plugins/coding-agent-orchestration-harness/skills/runtime-adapter-contract/references/prompt-budgeting.md`
  - `plugins/coding-agent-orchestration-harness/skills/runtime-adapter-contract/references/tool-capability-matrix.md`
- depends_on: [Task_1, Task_2]
- description: |
  Add a maintenance skill governing runtime-specific adapter definitions, role names, prompt budget, and tool permissions.
- acceptance:
  - Skill states shared semantics live in skills/references.
  - Skill states runtime mechanics may diverge.
  - Skill warns against copying full workflow into adapters.
  - Skill preserves Codex loader-only architecture.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Review runtime-adapter-contract for clear trigger scope and no ordinary coding-task overreach."

### Task_4: Route Skills Maintenance To Adapter Contract
- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/skills-maintenance/SKILL.md`
- depends_on: [Task_3]
- description: |
  Add routing language from skills-maintenance to runtime-adapter-contract for adapter-specific changes.
- acceptance:
  - `skills-maintenance` points adapter work to `runtime-adapter-contract`.
  - Routing does not imply adapter-contract should trigger for ordinary coding tasks.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Review routing language for scope clarity."

### Task_5: Verify Manifests And Codex Loader
- type: test
- owns:
  - `plugins/coding-agent-orchestration-harness/.github/plugin/plugin.json`
  - `plugins/coding-agent-orchestration-harness/.claude-plugin/plugin.json`
  - `plugins/coding-agent-orchestration-harness/.codex-plugin/plugin.json`
  - `plugins/coding-agent-orchestration-harness/codex/snippets/AGENTS.md`
- depends_on: [Task_4]
- description: |
  Verify runtime manifests still point to directories and Codex loader remains small.
- acceptance:
  - GitHub manifest points to `./agents/` and `./skills/`.
  - Claude manifest points to `./claude/agents/` and `./skills/`.
  - Codex manifest points to `./skills/`.
  - Codex `AGENTS.md` snippet remains loader-only.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "python plugins/coding-agent-orchestration-harness/scripts/validate_harness_package.py, after package validator exists; until then run JSON parse/path review manually."
  - kind: review
    required: true
    owner: reviewer
    detail: "Review runtime adapter changes against ADR-I-0001 and ADR-I-0002."

## Task Waves (explicit parallel dispatch sets)

- Wave 1 (parallel): [Task_1, Task_2]
- Wave 2 (parallel): [Task_3]
- Wave 3 (parallel): [Task_4]
- Wave 4 (parallel): [Task_5]

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
- Revert adapter files and remove `runtime-adapter-contract` if runtime schema issues appear.

## Progress Log (append-only)

- 2026-05-09 00:00 Plan drafted: [Task_1, Task_2, Task_3, Task_4, Task_5]
  - Summary: Initial implementation plan created.
  - Validation evidence: Plan format self-check.
  - Notes: Awaiting approval before execution.
- 2026-05-09 00:00 Plan approved and started: [Task_1, Task_2, Task_3, Task_4, Task_5]
  - Summary: User accepted the open-question recommendation and requested implementation.
  - Validation evidence: User approval in conversation.
  - Notes: Dedicated branch `codex-runtime-adapter-alignment`, stacked on `codex-orchestration-skill-kernel-refactor`.
- 2026-05-09 00:00 Wave 1 completed: [Task_1, Task_2]
  - Summary: Replaced Copilot Orchestrator duplicated workflow with a medium kernel and updated Claude Orchestrator to a short explicit kernel.
  - Validation evidence: Copilot kernel 72 lines; Claude kernel 55 lines; `rg` confirmed canonical policy routing and UI evidence boundary wording.
  - Notes: Claude frontmatter kept minimal per resolved decision.
- 2026-05-09 00:00 Wave 2 completed: [Task_3]
  - Summary: Added `runtime-adapter-contract` skill and maintenance references.
  - Validation evidence: Manual review of skill frontmatter, checklist, prompt budgeting, and tool matrix.
  - Notes: Skill scopes adapter work only, not ordinary coding tasks.
- 2026-05-09 00:00 Wave 3 completed: [Task_4]
  - Summary: Routed `skills-maintenance` to `runtime-adapter-contract` for runtime-specific adapter changes.
  - Validation evidence: Manual review of added routing language.
  - Notes: Routing explicitly excludes ordinary coding tasks unless adapter maintenance is in scope.
- 2026-05-09 00:00 Wave 4 completed: [Task_5]
  - Summary: Verified manifests parse and Codex loader remains loader-only.
  - Validation evidence: `ConvertFrom-Json` passed for all plugin manifests; `Get-Content` reviewed Codex `AGENTS.md` snippet.
  - Notes: No manifest structure changes were needed.

## Decision Log (append-only; re-plans and major discoveries)

- 2026-05-09 00:00 Decision:
  - Trigger / new insight: Current Copilot adapter duplicates canonical workflow and Claude adapter needs a stronger short kernel.
  - Plan delta (what changed): Adapter alignment work separated from canonical skill refactor.
  - Tradeoffs considered: Preserve runtime-specific metadata while consolidating semantics.
  - User approval: yes

## Notes
- Risks:
  - Claude frontmatter compatibility should be checked carefully before adding unsupported keys.
- Edge cases:
  - New skills under shared `skills/` should be discovered through existing manifest paths.
