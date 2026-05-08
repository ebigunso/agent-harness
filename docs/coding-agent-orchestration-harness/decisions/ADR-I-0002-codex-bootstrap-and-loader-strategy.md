---
status: accepted
adr_type: implementation
date: 2026-05-09
deciders:
  - ebigunso
consulted:
  - GPT-5.5
informed: []
supersedes: []
superseded_by: null
---

# ADR-I-0002: Install Codex Agents From Inert Templates With Loader-Only Instructions

## Context and Problem Statement

Codex custom agents are usable only after they are installed into a Codex agent directory such as `~/.codex/agents/` or `<repo>/.codex/agents/`. Keeping TOML files directly in a plugin source path that resembles active agent discovery can confuse other runtimes or create duplicate visible agents.

Codex also uses `AGENTS.md` for persistent instructions. A repo-scoped `AGENTS.md` affects other coding-agent platforms, while user-scoped Codex instructions affect all Codex sessions for that user. The harness needs enough instruction to load the orchestration skill without duplicating workflow mechanics.

## Decision Drivers

- Make Codex harness agents available only after explicit bootstrap.
- Avoid active-discovery ambiguity in the plugin source tree.
- Keep `AGENTS.md` content loader-only.
- Preserve existing user instructions and avoid wholesale overwrites.
- Avoid compatibility wrappers unless a concrete compatibility contract exists.

## Decision

Codex agent TOML files live as inert templates under `plugins/coding-agent-orchestration-harness/codex/agent-templates/`.

The canonical bootstrap script is `plugins/coding-agent-orchestration-harness/skills/codex-harness-bootstrap/scripts/install_codex_harness.py`. It installs the templates into user or repository Codex agent scope, copies role-specific connector policy references, and optionally manages a marked loader block in user-scoped `~/.codex/AGENTS.md`.

The managed `AGENTS.md` block routes Codex to `$orchestration-harness` and does not duplicate plan gates, delegation rules, validation rules, role names, or reporting formats.

## Implementation Impact

- The bootstrap script supports `--scope user`, `--scope repo`, `--repo-root`, `--overwrite-agents`, and `--user-instructions`.
- The script reads the loader block from `codex/snippets/AGENTS.md`.
- The older wrapper script name is not retained because the canonical script is functionally sufficient.

## Considered Options

1. Put Codex TOML files under `codex/agents/` and rely on runtime behavior.
2. Install Codex agents manually and document the copy steps.
3. Store Codex TOML files as inert templates and install them through a bootstrap script.

## Decision Outcome

Chosen option: **Option 3**.

This keeps the plugin source tree clean, makes installation explicit, and lets the bootstrap script preserve user instructions while installing the correct agent and reference files.

## Consequences

### Positive

- Codex agents are installed only into the requested scope.
- Other runtimes are less likely to discover Codex TOML templates accidentally.
- Loader instructions can be updated through a marked block without overwriting unrelated user content.

### Negative / Tradeoffs

- Codex users must run a bootstrap step after installing or updating the plugin.
- Installed agents can become stale if the plugin changes and bootstrap is not rerun.

## Validation

- Run `python -m py_compile` on `install_codex_harness.py`.
- Run user-scope bootstrap smoke tests with a temporary `--codex-home`.
- Run repo-scope bootstrap smoke tests against a temporary repository.
- Verify generated `AGENTS.md` contains `$orchestration-harness` and omits harness role names.
- Verify no `install_codex_agents.py` wrapper remains.

## Revisit When

- Codex supports plugin-shipped custom agents directly.
- Codex adds scoped skill-loading policy that removes the need for an `AGENTS.md` loader.
- Users need a documented compatibility guarantee for an older bootstrap command name.

## More Information

- `plugins/coding-agent-orchestration-harness/skills/codex-harness-bootstrap/scripts/install_codex_harness.py`
- `plugins/coding-agent-orchestration-harness/codex/snippets/AGENTS.md`
- `plugins/coding-agent-orchestration-harness/codex/agent-templates/`
