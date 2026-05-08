# Plan: Multi-Runtime Harness Plugin Integration

- status: done
- generated: 2026-05-08
- last_updated: 2026-05-08
- work_type: mixed

## Goal
- Update `plugins/coding-agent-orchestration-harness` so GitHub Copilot, Claude Code, and Codex share one canonical `skills/` tree while each runtime gets only the adapter files it needs.
- Preserve locally verified behavior over stale hand-off assumptions, especially around Copilot agent filenames and Codex inert template storage.

## Definition of Done
- `plugins/coding-agent-orchestration-harness/skills/` remains the only canonical shared skills tree.
- `skills/orchestration-harness/SKILL.md` is explicitly documented as the workflow source of truth.
- Copilot agents remain directly under `agents/` with their current filenames and Copilot-specific frontmatter.
- `.github/plugin/plugin.json` points to `./agents/` and `./skills/`.
- Claude agents live under `claude/agents/`, and `.claude-plugin/plugin.json` points to `./claude/agents/` and `./skills/`.
- Claude has `harness-orchestrator`, `harness-researcher`, `harness-worker`, and `harness-reviewer` adapters based closely on the Copilot definitions with only runtime-required changes.
- `.codex-plugin/plugin.json` exists, points to `./skills/`, and uses loader/source-of-truth wording instead of workflow mechanics.
- `.agents/plugins/marketplace.json` remains valid for the local Codex plugin marketplace.
- Codex TOML profiles remain inert templates under `codex/agent-templates/`, omit `model`, and are installed into user or repo scope only by bootstrap.
- Codex app connector policies remain split by role under `references/` and are copied next to installed Codex agents.
- Codex bootstrap has a canonical `install_codex_harness.py` entrypoint and preserves existing user/repo scope behavior.
- Codex managed `AGENTS.md` content is loader-only and does not duplicate harness workflow mechanics or role names.
- README/runtime docs match the final merged design.
- Static validation and bootstrap smoke checks pass.

## Scope / Non-goals
- Scope:
  - Update plugin manifests where current paths/prompts do not match the merged design.
  - Add or update Claude runtime adapters.
  - Refine the shared orchestration skill metadata and source-of-truth preamble.
  - Refine Codex bootstrap script naming, flags, snippets, and docs.
  - Update README runtime support documentation.
- Non-goals:
  - Do not rename Copilot agent files to `*.agent.md`.
  - Do not move Copilot agents out of root `agents/`.
  - Do not move Codex templates to `codex/agents/`.
  - Do not duplicate shared skill bodies into runtime-specific directories.
  - Do not pin a Codex model in TOML templates.
  - Do not automatically install repo-scoped `AGENTS.md` instructions by default.
  - Do not introduce a build step.

## Context (workspace)
- Related files/areas:
  - `plugins/coding-agent-orchestration-harness/.github/plugin/plugin.json`
  - `plugins/coding-agent-orchestration-harness/.claude-plugin/plugin.json`
  - `plugins/coding-agent-orchestration-harness/.codex-plugin/plugin.json`
  - `plugins/coding-agent-orchestration-harness/agents/`
  - `plugins/coding-agent-orchestration-harness/claude/agents/`
  - `plugins/coding-agent-orchestration-harness/codex/agent-templates/`
  - `plugins/coding-agent-orchestration-harness/codex/snippets/`
  - `plugins/coding-agent-orchestration-harness/references/`
  - `plugins/coding-agent-orchestration-harness/skills/`
  - `.agents/plugins/marketplace.json`
  - `README.md`
- Existing patterns or references:
  - Copilot root agents are currently discoverable with `*.md` filenames.
  - Codex templates are intentionally stored under `codex/agent-templates/` to avoid active discovery ambiguity.
  - Current bootstrap already supports user/repo scope, safe user `AGENTS.md` prompts, and role-specific connector reference copying.
  - Current Claude adapters under `agents/claude/` are too thin compared to the Copilot source.
- Repo reference docs consulted:
  - `docs/coding-agent/lessons.md`
  - `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/SKILL.md`
  - `plugins/coding-agent-orchestration-harness/skills/plan-format/SKILL.md`
  - `plugins/coding-agent-orchestration-harness/skills/codex-harness-bootstrap/SKILL.md`

## Open Questions (max 3)
- None.

## Assumptions
- A1: The hand-off document is guidance, not a strict implementation spec, when it conflicts with locally verified runtime behavior.
- A2: Copilot root agent filenames should remain as currently tested and working.
- A3: Codex templates should remain inert until the bootstrap installs them into `~/.codex/agents/` or `<repo>/.codex/agents/`.
- A4: Runtime-specific agent definitions should stay as close to the Copilot source bodies as each runtime allows.

## Tasks

### Task_1: Lock Copilot manifest and root agent layout
- type: review
- owns:
  - `plugins/coding-agent-orchestration-harness/.github/plugin/plugin.json`
  - `plugins/coding-agent-orchestration-harness/agents/`
- depends_on: []
- description: |
  Verify and preserve the Copilot-facing layout. The hand-off's `*.agent.md` filename convention is not required because the current filenames are already discoverable.
- acceptance:
  - Copilot agents remain directly under `agents/`.
  - Current Copilot agent filenames are preserved.
  - `.github/plugin/plugin.json` continues to use `agents: "./agents/"` and `skills: "./skills/"`.
  - Copilot-specific model labels remain confined to root Copilot agents.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "Parse `.github/plugin/plugin.json` as JSON and verify referenced `agents` and `skills` paths exist."
  - kind: command
    required: true
    owner: worker
    detail: "Search for `GPT-5.*(copilot)` and verify matches are confined to `plugins/coding-agent-orchestration-harness/agents/` root files."

### Task_2: Refine shared orchestration skill as source of truth
- type: impl
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/SKILL.md`
- depends_on: [Task_1]
- description: |
  Add the source-of-truth preamble and refine frontmatter without rewriting the workflow body.
- acceptance:
  - Frontmatter description identifies the skill as the workflow source of truth for harness behavior.
  - Body begins with a short source-of-truth preamble.
  - Existing Orchestrator workflow semantics remain intact.
  - The skill does not contain Copilot model labels or runtime setup instructions.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "Search the skill for Copilot model labels and runtime setup leakage."
  - kind: review
    required: true
    owner: reviewer
    detail: "Review the skill diff for source-of-truth clarity and preservation of workflow semantics."

### Task_3: Move and expand Claude adapters
- type: impl
- owns:
  - `plugins/coding-agent-orchestration-harness/.claude-plugin/plugin.json`
  - `plugins/coding-agent-orchestration-harness/agents/claude/`
  - `plugins/coding-agent-orchestration-harness/claude/agents/`
- depends_on: [Task_2]
- description: |
  Move Claude adapters to a Claude-specific component path and base their bodies closely on the Copilot agent definitions with minimal Claude frontmatter/tool changes.
- acceptance:
  - `.claude-plugin/plugin.json` points to `./claude/agents/` and `./skills/`.
  - `claude/agents/harness-orchestrator.md` exists and references `orchestration-harness` as source of truth.
  - `claude/agents/harness-researcher.md`, `harness-worker.md`, and `harness-reviewer.md` exist.
  - Claude role bodies preserve the substantive Copilot role instructions where runtime-compatible.
  - Old `agents/claude/` adapter files are removed after replacement.
  - Claude files do not contain Copilot-only model labels.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "Parse `.claude-plugin/plugin.json` as JSON and verify referenced `agents` and `skills` paths exist."
  - kind: command
    required: true
    owner: worker
    detail: "Verify the four expected Claude agent files exist under `claude/agents/` and `agents/claude/` no longer exists."
  - kind: command
    required: true
    owner: worker
    detail: "Search `claude/` for Copilot-only model labels."

### Task_4: Refine Codex plugin metadata, templates, and loader snippet
- type: impl
- owns:
  - `.agents/plugins/marketplace.json`
  - `plugins/coding-agent-orchestration-harness/.codex-plugin/plugin.json`
  - `plugins/coding-agent-orchestration-harness/codex/agent-templates/`
  - `plugins/coding-agent-orchestration-harness/codex/snippets/`
  - `plugins/coding-agent-orchestration-harness/references/`
- depends_on: [Task_2]
- description: |
  Preserve the current inert Codex template design while adding a loader-only snippet and cleaning plugin default prompt wording.
- acceptance:
  - `.codex-plugin/plugin.json` points to `./skills/`.
  - Codex plugin `defaultPrompt` tells Codex to load and follow `orchestration-harness` as source of truth.
  - Codex templates remain under `codex/agent-templates/`.
  - Codex templates omit `model`.
  - No `codex/agents/` source-template directory is introduced.
  - `codex/snippets/AGENTS.md` exists and is loader-only.
  - Loader snippet mentions `$orchestration-harness` and does not mention `harness_researcher`, `harness_worker`, or `harness_reviewer`.
  - Split connector policy references remain under `references/`.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "Parse `.codex-plugin/plugin.json` and `.agents/plugins/marketplace.json` as JSON."
  - kind: command
    required: true
    owner: worker
    detail: "Search `codex/agent-templates/*.toml` for `^model\\s*=` and verify no matches."
  - kind: command
    required: true
    owner: worker
    detail: "Verify `codex/snippets/AGENTS.md` contains `$orchestration-harness` and omits role agent names."

### Task_5: Update Codex bootstrap interface without losing safety behavior
- type: impl
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/codex-harness-bootstrap/SKILL.md`
  - `plugins/coding-agent-orchestration-harness/skills/codex-harness-bootstrap/scripts/`
- depends_on: [Task_4]
- description: |
  Merge the hand-off's cleaner bootstrap naming with the current script's safer user/repo scope behavior.
- acceptance:
  - `install_codex_harness.py` is the canonical implementation entrypoint.
  - `--overwrite-agents` is supported as an alias for the existing overwrite behavior.
  - User and repo install scopes continue to work.
  - Source templates are loaded from `codex/agent-templates/`.
  - Role-specific connector references are copied into an installed `references/` folder.
  - User `AGENTS.md` management preserves unrelated content and replaces only the marked block.
  - Managed `AGENTS.md` content uses the loader-only snippet.
  - Repo `AGENTS.md` installation is not automatic by default.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "Run `python -m py_compile` on the bootstrap scripts."
  - kind: command
    required: true
    owner: worker
    detail: "Run user-scope bootstrap smoke test with a temporary `--codex-home`; verify agents, references, and loader-only `AGENTS.md` behavior."
  - kind: command
    required: true
    owner: worker
    detail: "Run repo-scope bootstrap smoke test against a temporary repo; verify `.codex/agents/` output and skip/overwrite behavior."

### Task_6: Update runtime documentation
- type: docs
- owns:
  - `README.md`
- depends_on: [Task_3, Task_5]
- description: |
  Update README runtime support docs to reflect the merged design, not the literal hand-off tree.
- acceptance:
  - README states the plugin supports GitHub Copilot, Claude Code, and Codex.
  - README states canonical shared skills live under `skills/`.
  - README identifies `skills/orchestration-harness/SKILL.md` as workflow source of truth.
  - README lists Copilot agents as `agents/*.md`.
  - README lists Claude agents as `claude/agents/`.
  - README lists Codex templates as `codex/agent-templates/`.
  - README documents the canonical `install_codex_harness.py` command.
  - README explains that Codex `AGENTS.md` content is loader-only.
- validation:
  - kind: review
    required: true
    owner: worker
    detail: "Review README diff against final paths and behavior."

### Task_7: Final integration validation and review
- type: review
- owns: []
- depends_on: [Task_6]
- description: |
  Run static validation and review the final diff against the merged acceptance criteria.
- acceptance:
  - JSON manifests parse successfully.
  - Expected Copilot, Claude, Codex, skill, reference, and snippet paths exist.
  - Copilot model labels do not leak into Claude, Codex, or shared skills.
  - Codex templates omit `model`.
  - Bootstrap smoke checks pass.
  - Final review finds no must-fix issues, or all must-fix issues are remediated.
- validation:
  - kind: command
    required: true
    owner: orchestrator
    detail: "Run manifest JSON parse checks."
  - kind: command
    required: true
    owner: orchestrator
    detail: "Run grep/path checks for runtime leakage, missing paths, Codex model omission, and loader-only snippet contents."
  - kind: command
    required: true
    owner: orchestrator
    detail: "Run bootstrap smoke checks for user and repo scopes using temporary directories."
  - kind: review
    required: true
    owner: reviewer
    detail: "Review final diff against this plan."

## Task Waves (explicit parallel dispatch sets)

Interpretation:
- Tasks listed in the same wave are intended to be dispatched in parallel by default when `owns` are disjoint and dependencies are met.
- Waves are executed sequentially.

- Wave 1 (parallel): [Task_1]
- Wave 2 (parallel): [Task_2]
- Wave 3 (parallel): [Task_3, Task_4]
- Wave 4 (parallel): [Task_5]
- Wave 5 (parallel): [Task_6]
- Wave 6 (parallel): [Task_7]

## E2E / Visual Validation Spec

- Not applicable. This change affects plugin manifests, agent definitions, skills, scripts, and documentation, with no UI/browser behavior.

## Rollback / Safety
- Revert changes to `.claude-plugin/plugin.json`, `.codex-plugin/plugin.json`, `.agents/plugins/marketplace.json`, runtime agent directories, Codex snippets, bootstrap scripts, and README.
- If Claude adapter migration fails, restore the previous `agents/claude/` files and point `.claude-plugin/plugin.json` back to that path.
- Bootstrap smoke tests must use temporary directories or explicit test paths, not real user repositories.
- User-scoped Codex install tests must use temporary `--codex-home` unless the user explicitly asks to update the real machine.

## Progress Log (append-only)

- 2026-05-08 Draft rewritten: [Task_1, Task_2, Task_3, Task_4, Task_5, Task_6, Task_7]
  - Summary: Replaced stale literal hand-off plan with a merged plan based on current repo state and locally verified runtime behavior.
  - Validation evidence: Current manifests, agent paths, orchestration skill, Codex templates, connector references, bootstrap script, and README were inspected.
  - Notes: Awaiting user approval before implementation.
- 2026-05-08 Implementation started: [Task_1]
  - Summary: User approved the plan and requested implementation.
  - Validation evidence: Pending Task_1 baseline checks.
  - Notes: Execution status set to in_progress.
- 2026-05-08 Wave 1 completed: [Task_1]
  - Summary: Preserved Copilot root agent layout and current filenames.
  - Validation evidence: Parsed `.github/plugin/plugin.json`; verified `agents/` and `skills/` paths exist; confirmed Copilot model labels appear only in root Copilot role agents.
  - Notes: No Copilot file moves or renames were needed.
- 2026-05-08 Wave 2 completed: [Task_2]
  - Summary: Updated `orchestration-harness` frontmatter and added the source-of-truth preamble without changing the workflow body.
  - Validation evidence: Grep checks found no Copilot model labels, `.agent.md`, plugin installation wording, or stale runtime paths in the shared skill.
  - Notes: The shared skill remains the canonical workflow owner.
- 2026-05-08 Wave 3 completed: [Task_3, Task_4]
  - Summary: Moved Claude adapters to `claude/agents/`, added `harness-orchestrator`, preserved Copilot role bodies with Claude frontmatter, updated Codex default prompt, and added loader-only `codex/snippets/AGENTS.md`.
  - Validation evidence: JSON parsing passed; expected Claude and Codex paths exist; `agents/claude/` is absent; no Copilot model labels appear in Claude, Codex, or shared skill paths; Codex templates omit `model`; no `codex/agents/` source path exists; the snippet contains `$orchestration-harness` and omits role agent names.
  - Notes: `.agents/plugins/marketplace.json` required no changes.
- 2026-05-08 Wave 4 completed: [Task_5]
  - Summary: Added canonical `install_codex_harness.py`, added `--overwrite-agents`, and switched managed instructions to the loader-only snippet.
  - Validation evidence: `python -m py_compile` passed for the bootstrap script; user-scope smoke test installed agents, copied references, and wrote loader-only `AGENTS.md`; repo-scope smoke test installed, skipped existing files, overwrote with `--overwrite-agents`, and did not create repo `AGENTS.md`.
  - Notes: Initial smoke attempt under `C:\tmp` hit a Windows access denial, so validation was rerun under workspace temporary directories and passed.
- 2026-05-08 Wave 5 completed: [Task_6]
  - Summary: Updated README runtime support docs for canonical skills, `claude/agents/`, `codex/agent-templates/`, canonical bootstrap command, and loader-only Codex instructions.
  - Validation evidence: README diff reviewed against final paths and behavior.
  - Notes: Bootstrap docs use only the canonical `install_codex_harness.py` entrypoint.
- 2026-05-08 Wave 6 completed: [Task_7]
  - Summary: Ran final static validation and diff review.
  - Validation evidence: Manifest JSON parse checks passed; path checks passed; runtime leakage checks passed; Codex model omission check passed; loader-only snippet check passed; bootstrap smoke checks passed; `git diff --check` reported no whitespace errors.
  - Notes: No subagent Reviewer was spawned because this execution did not receive an explicit delegation request beyond using the approved plan; Orchestrator performed the final diff review.

## Decision Log (append-only; re-plans and major discoveries)

- 2026-05-08 Decision:
  - Trigger / new insight: User confirmed Copilot agent definitions can keep current filenames and do not need `*.agent.md` to be discoverable.
  - Plan delta (what changed): Removed Copilot rename/restructure work; preserve root `agents/*.md`.
  - Tradeoffs considered: Keeping tested filenames avoids unnecessary churn and preserves local discovery behavior.
  - User approval: yes.
- 2026-05-08 Decision:
  - Trigger / new insight: Current bootstrap is safer than the hand-off's minimal script because it supports user/repo scope, preserves existing user instructions, and copies role-specific connector references.
  - Plan delta (what changed): Keep current bootstrap behavior, add canonical script naming and aliases, and replace only the managed instruction block with a loader-only version.
  - Tradeoffs considered: This preserves the hand-off intent without regressing user-safety behavior.
  - User approval: yes.
- 2026-05-08 Decision:
  - Trigger / new insight: Codex source templates under `codex/agent-templates/` better communicate inert bootstrap payloads than the hand-off's `codex/agents/`.
  - Plan delta (what changed): Preserve `codex/agent-templates/` and explicitly disallow introducing `codex/agents/` as a source-template path.
  - Tradeoffs considered: This diverges from the hand-off tree but avoids discovery ambiguity and matches prior local testing.
  - User approval: yes.

## Notes
- Risks:
  - Claude plugin agent frontmatter may need runtime verification in Claude Code after static validation.
  - Keeping multiple runtime adapter formats close to the Copilot source requires disciplined minimal edits to avoid drift.
  - Bootstrap changes must not touch real `~/.codex/AGENTS.md` during smoke tests unless explicitly requested.
- Edge cases:
  - Existing installed Codex agents may have older managed blocks that mention role names; the updated bootstrap should safely replace only the marked block.
  - If a user has unrelated `~/.codex/AGENTS.md` content, bootstrap must keep preview-and-confirm behavior before appending.
