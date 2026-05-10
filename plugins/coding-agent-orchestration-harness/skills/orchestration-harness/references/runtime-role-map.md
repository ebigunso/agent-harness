# Runtime Role Map

Logical roles are stable. Physical agent names may vary by runtime.

| Logical role | GitHub/Copilot physical name | Claude Code physical name | Codex physical name |
|---|---|---|---|
| Orchestrator | Orchestrator | harness-orchestrator | main Codex thread + `$orchestration-harness` loader |
| Researcher | Researcher | harness-researcher | harness_researcher |
| Worker | Worker | harness-worker | harness_worker |
| Reviewer | Reviewer | harness-reviewer | harness_reviewer |

## Rules

- Plans and shared skills use logical role names.
- Runtime adapters invoke physical names.
- Preserve existing Copilot physical names unless a migration plan is explicitly added.
- Prefer namespaced physical names for newly added runtime agents.
- Do not rely on generic names such as `worker` in runtimes where collisions with platform-provided agents are plausible.

## Maintenance Checks

- GitHub/Copilot physical names should correspond to files under `plugins/coding-agent-orchestration-harness/agents/`.
- Claude Code physical names should correspond to files under `plugins/coding-agent-orchestration-harness/claude/agents/`.
- Codex physical names should correspond to templates under `plugins/coding-agent-orchestration-harness/codex/agent-templates/` or loader behavior documented in `plugins/coding-agent-orchestration-harness/codex/snippets/AGENTS.md`.
