# agent-harness

Repository for agent plugins, reusable templates, and useful hooks or scripts intended to enhance an agent harness.

## Quick Start

This repository currently publishes one plugin:

- Marketplace: `agent-harness`
- Plugin: `coding-agent-orchestration-harness`

## GitHub Copilot in VS Code

1. Enable agent plugins in VS Code:

```json
// settings.json
"chat.plugins.enabled": true
```

2. Register this marketplace in `settings.json`.

For GitHub:

```json
// settings.json
"chat.plugins.marketplaces": [
	"ebigunso/agent-harness"
]
```

For a local clone:

```json
// settings.json
"chat.plugins.marketplaces": [
	"file:///path/to/agent-harness"
]
```

3. Open the Extensions view with `Ctrl+Shift+X`, search for `@agentPlugins`, then install `coding-agent-orchestration-harness` from the `agent-harness` marketplace.

4. After installation, the plugin's agents and skills appear in chat alongside your local customizations.

If you want to register the plugin directly from a local checkout instead of through a marketplace, use `chat.plugins.paths`:

```json
// settings.json
"chat.plugins.paths": {
	"/path/to/agent-harness/plugins/coding-agent-orchestration-harness": true
}
```

## Claude Code

1. Add this marketplace:

```text
/plugin marketplace add ebigunso/agent-harness
```

If you already cloned the repo locally, you can add it from disk instead:

```text
/plugin marketplace add ./agent-harness
```

2. Install the plugin from the marketplace:

```text
/plugin install coding-agent-orchestration-harness@agent-harness
```

3. Run the plugin manager with `/plugin` to browse installed plugins, enable or disable them, and inspect any marketplace or loading errors.

4. If you install or update plugins during an active session, run `/reload-plugins` to apply changes that do not require a full restart.

## Notes

- Claude Code plugin support requires Claude Code `1.0.33` or later.
- Plugin marketplaces and plugins are highly trusted. Only install from sources you trust.
- This repository includes both `.claude-plugin` and `.github/plugin` metadata so the same plugin bundle can be consumed by supported clients.

## Runtime support

This plugin supports GitHub Copilot, Claude Code, and Codex.

Unless otherwise noted, paths in this section are relative to the plugin root:

`plugins/coding-agent-orchestration-harness/`

### Skills

All runtimes use the same canonical `skills/` directory.

The shared orchestration workflow source of truth is:

`skills/orchestration-harness/SKILL.md`

Runtime-specific files should route to that skill instead of duplicating the harness workflow.

Design decisions for this plugin are recorded in `docs/coding-agent-orchestration-harness/decisions/`.

### Agents

Agent definitions are runtime-specific because model names, tool names, and frontmatter schemas differ:

- Copilot agents: `agents/*.md`
- Claude agents: `claude/agents/`
- Codex agent templates: `codex/agent-templates/`

### Codex bootstrap

From the repository where the Codex profiles should be installed, run the bootstrap script from the installed plugin location:

```bash
python /path/to/coding-agent-orchestration-harness/skills/codex-harness-bootstrap/scripts/install_codex_harness.py
```

The script asks whether to install in user scope or repository scope.

Use `--scope user` to install into `~/.codex/agents/`.

Use `--scope repo` to install into `.codex/agents/` under the nearest repository root.

Use `--repo-root /path/to/repo` with `--scope repo` when installing into a repository other than the current working directory's nearest `.git` parent.

Use `--overwrite-agents` to replace existing profiles. `--overwrite` is also accepted.

Use `--dry-run` to preview planned writes/skips without writing files.

Use `--check` to compare installed Codex profiles against the plugin templates and report stale, missing, modified, or matching files.

Use `--verify` to assert required installed files and the managed install manifest exist.

Normal installs write `.coding-agent-orchestration-harness-install.json` in the target agents directory by default. Use `--no-write-manifest` only when manifest creation is intentionally unwanted.

For user-scope installs, the script also asks whether to add a small managed routing rule to `~/.codex/AGENTS.md` so Codex knows when to load `$orchestration-harness`. Existing user instructions are not overwritten. If the file already has content, the script shows a preview and asks whether to append the managed block; if the managed block already exists, it asks whether to replace only that block.

Use `--user-instructions add` to add or update that managed block non-interactively, or `--user-instructions skip` to leave `~/.codex/AGENTS.md` untouched.

The managed Codex `AGENTS.md` block is loader-only. It routes coding-related tasks to `$orchestration-harness`; workflow mechanics stay in the skill.

### Model behavior

Copilot agents may pin Copilot-specific model names such as `GPT-5.5 (copilot)`.

Claude agents should use `model: inherit`, omit `model`, or use Claude-supported aliases/model IDs.

Codex agent templates currently omit `model`, so they inherit the main Codex session model.

Unsupported model names are not assumed to fall back safely.
