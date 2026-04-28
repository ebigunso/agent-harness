---
name: codex-harness-bootstrap
description: Install or refresh Codex custom-agent TOML profiles for the coding-agent orchestration harness in the current repository.
---

# Codex harness bootstrap

Use this skill when setting up the coding-agent orchestration harness for Codex.

From the repository where the Codex profiles should be installed, run the bootstrap script from the installed plugin location:

```bash
python /path/to/coding-agent-orchestration-harness/skills/codex-harness-bootstrap/scripts/install_codex_agents.py
```

Use `--repo-root` when installing into a repository other than the current working directory's nearest `.git` parent.

Use `--overwrite` to replace existing profiles.
