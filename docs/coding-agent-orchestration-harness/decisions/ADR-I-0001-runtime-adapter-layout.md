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

# ADR-I-0001: Use Runtime-Specific Adapter Paths With Shared Skills

## Context and Problem Statement

GitHub Copilot, Claude Code, and Codex use different agent definition formats and discovery conventions. Copilot agents are discoverable directly under the plugin root `agents/` directory with the `*.md` filenames used by the Copilot agent files. Claude plugin agents require Claude-specific frontmatter and should not inherit Copilot model labels or tool names. Codex custom agents are TOML files installed into Codex agent directories, not plugin-discovered Markdown agents.

Combining all runtime agent definitions in one discovery path risks duplicate or invalid registrations.

## Decision Drivers

- Preserve locally verified Copilot discovery behavior.
- Keep runtime-specific frontmatter and model/tool labels isolated.
- Avoid duplicate visible agent definitions in runtimes that scan multiple formats.
- Keep shared workflow and supporting skills in one canonical `skills/` tree.

## Decision

Runtime adapter files are separated by runtime while all shared skills remain under `plugins/coding-agent-orchestration-harness/skills/`.

- Copilot agents remain directly under `plugins/coding-agent-orchestration-harness/agents/` with their root `*.md` filenames.
- Claude agents live under `plugins/coding-agent-orchestration-harness/claude/agents/*.md`.
- Codex TOML files are stored as inert templates under `plugins/coding-agent-orchestration-harness/codex/agent-templates/` and are installed by bootstrap.

## Implementation Impact

- `.github/plugin/plugin.json` points to `./agents/` and `./skills/`.
- `.claude-plugin/plugin.json` lists the Claude agent Markdown files under `./claude/agents/` and points to `./skills/`.
- `.codex-plugin/plugin.json` points to `./skills/`; Codex agent installation is handled by bootstrap.

## Considered Options

1. Put every runtime's agent definitions under `agents/`.
2. Move Copilot agents into a nested Copilot directory.
3. Keep Copilot at root and put non-Copilot adapters in runtime-specific paths.

## Decision Outcome

Chosen option: **Option 3**.

This preserves known Copilot discovery behavior, gives Claude a clean plugin agent path, and keeps Codex templates out of source paths that look like active agent discovery locations.

## Consequences

### Positive

- Runtime metadata stays isolated.
- Copilot discovery behavior remains stable.
- Codex templates are clearly bootstrap payloads, not live plugin agents.

### Negative / Tradeoffs

- The plugin has several runtime-specific directories to document.
- Claude and Codex adapter changes must be checked against their runtime conventions separately.

## Validation

- Parse all plugin manifests as JSON.
- Verify each manifest's referenced paths exist.
- Search for Copilot model labels outside root Copilot agent files.
- Verify no `codex/agents/` source-template directory exists.

## Revisit When

- Copilot reliably discovers nested agent directories in this plugin.
- Claude or Codex plugin packaging gains a different recommended component layout.
- A runtime begins registering duplicate agents from the selected paths.

## More Information

- `plugins/coding-agent-orchestration-harness/.github/plugin/plugin.json`
- `plugins/coding-agent-orchestration-harness/.claude-plugin/plugin.json`
- `plugins/coding-agent-orchestration-harness/.codex-plugin/plugin.json`
