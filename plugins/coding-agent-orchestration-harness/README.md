# Coding Agent Orchestration Harness

This plugin provides shared harness skills plus runtime-specific adapters for GitHub Copilot, Claude Code, and Codex.

## Codex Bootstrap

Codex agent templates live under `codex/agent-templates/` and are installed by:

```bash
python skills/codex-harness-bootstrap/scripts/install_codex_harness.py
```

Useful flags:

- `--scope user` installs into `~/.codex/agents/`.
- `--scope repo` installs into `.codex/agents/` under the selected repository.
- `--repo-root <path>` selects the target repository for repo scope.
- `--dry-run` previews writes/skips without writing files.
- `--check` compares installed files against source templates and requires the managed manifest for a successful check.
- `--verify` checks required installed files and the managed install manifest.
- `--overwrite-agents` replaces existing installed templates.
- `--user-instructions add|skip|ask` controls the user-scope loader block.

Normal installs write `.coding-agent-orchestration-harness-install.json` in the target agents directory by default. Use `--no-write-manifest` only when manifest creation is intentionally unwanted.
