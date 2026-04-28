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

### Skills

All runtimes use the same canonical `skills/` directory.

The shared orchestration instructions live in:

`skills/orchestration-harness/SKILL.md`

This skill should always be applied when using the harness in Codex or Claude Code.

### Agents

Agent definitions are runtime-specific because model names, tool names, and frontmatter schemas differ:

- Copilot agents: `agents/copilot/`
- Claude agents: `agents/claude/`
- Codex agent templates: `codex/agents/`

### Codex bootstrap

From the repository where the Codex profiles should be installed, run the bootstrap script from the installed plugin location:

```bash
python /path/to/coding-agent-orchestration-harness/skills/codex-harness-bootstrap/scripts/install_codex_agents.py
```

Use `--repo-root /path/to/repo` when installing into a repository other than the current working directory's nearest `.git` parent.

Use `--overwrite` to replace existing profiles.

### Model behavior

Copilot agents may pin Copilot-specific model names such as `GPT-5.5 (copilot)`.

Claude agents should use `model: inherit`, omit `model`, or use Claude-supported aliases/model IDs.

Codex agent templates currently omit `model`, so they inherit the main Codex session model.

Unsupported model names are not assumed to fall back safely.
