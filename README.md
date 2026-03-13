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
