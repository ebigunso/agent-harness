---
name: codex-harness-bootstrap
description: Install or refresh Codex custom-agent TOML profiles and the minimal AGENTS.md loader block for the coding-agent orchestration harness.
---

# Codex harness bootstrap

Use this skill when setting up the coding-agent orchestration harness for Codex.

Run the canonical bootstrap script from the installed plugin location:

```bash
python /path/to/coding-agent-orchestration-harness/skills/codex-harness-bootstrap/scripts/install_codex_harness.py
```

The script asks whether to install the agents in user scope or repository scope.

Use `--scope user` to install into `~/.codex/agents/`.

Use `--scope repo` to install into `.codex/agents/` under the nearest repository root.

Use `--repo-root` with `--scope repo` when installing into a repository other than the current working directory's nearest `.git` parent.

Use `--overwrite-agents` to replace existing profiles. `--overwrite` is also accepted.

When installing in user scope, the script also asks whether to add a small managed harness routing block to `~/.codex/AGENTS.md`.

- Existing content is never overwritten wholesale.
- If `AGENTS.md` already has other content, review the preview and choose whether to append the managed block.
- If the managed block already exists, choose whether to replace only that block.
- Use `--user-instructions add` for non-interactive add/update, or `--user-instructions skip` to leave `AGENTS.md` untouched.

The managed `AGENTS.md` block is loader-only. It routes Codex to `$orchestration-harness`; workflow mechanics stay in the skill.
