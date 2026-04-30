---
name: codex-harness-bootstrap
description: Install or refresh Codex custom-agent TOML profiles for the coding-agent orchestration harness in user or repository scope.
---

# Codex harness bootstrap

Use this skill when setting up the coding-agent orchestration harness for Codex.

Run the bootstrap script from the installed plugin location:

```bash
python /path/to/coding-agent-orchestration-harness/skills/codex-harness-bootstrap/scripts/install_codex_agents.py
```

The script asks whether to install the agents in user scope or repository scope.

Use `--scope user` to install into `~/.codex/agents/`.

Use `--scope repo` to install into `.codex/agents/` under the nearest repository root.

Use `--repo-root` with `--scope repo` when installing into a repository other than the current working directory's nearest `.git` parent.

Use `--overwrite` to replace existing profiles.

When installing in user scope, the script also asks whether to add a small managed harness routing block to `~/.codex/AGENTS.md`.

- Existing content is never overwritten wholesale.
- If `AGENTS.md` already has other content, review the preview and choose whether to append the managed block.
- If the managed block already exists, choose whether to replace only that block.
- Use `--user-instructions add` for non-interactive add/update, or `--user-instructions skip` to leave `AGENTS.md` untouched.
