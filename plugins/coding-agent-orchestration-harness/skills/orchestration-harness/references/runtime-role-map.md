# Runtime Role Map

Logical roles are stable. Physical agent names may vary by runtime.

| Logical role | GitHub/Copilot physical name | Claude Code physical name | Codex physical name |
|---|---|---|---|
| Orchestrator | Orchestrator | harness-orchestrator | main Codex thread + `$orchestration-harness` loader |
| Researcher | Researcher | harness-researcher | harness_researcher |
| Worker | Worker | harness-worker | harness_worker |
| Reviewer | Reviewer | harness-reviewer | harness_reviewer |
| Counsel | Counsel | harness-counsel | main Codex thread + the `$counsel` skill invoked explicitly by the person directing the work |

## Home Of Each Session Role

A session holds one role and takes its mechanics from that role's home. It never loads another role's home as its own; it reads a reference kept in another home only where its own home points it to that file.

- Orchestrator, and the Researcher, Worker and Reviewer it dispatches: the `orchestration-harness` skill and its references.
- Counsel: the `counsel` skill and its references.

## Rules

- Counsel is a separate session the person directing the work opens, never a subagent: no role dispatches it, and it dispatches only the Researcher. Its policy is the `counsel` skill; a Counsel session never loads `orchestration-harness`.
- Plans and shared skills use logical role names.
- Runtime adapters invoke physical names.
- Preserve existing Copilot physical names unless a migration plan is explicitly added.
- Prefer namespaced physical names for newly added runtime agents, except where a runtime's agents already use bare role names (Copilot).
- Do not rely on generic names such as `worker` in runtimes where collisions with platform-provided agents are plausible.

## Maintenance Checks

- GitHub/Copilot physical names should correspond to files under `plugins/coding-agent-orchestration-harness/agents/`.
- Claude Code physical names should correspond to files under `plugins/coding-agent-orchestration-harness/claude/agents/`.
- Codex physical names should correspond to templates under `plugins/coding-agent-orchestration-harness/codex/agent-templates/` or loader behavior documented in `plugins/coding-agent-orchestration-harness/codex/snippets/AGENTS.md`.
- Counsel has no Codex template and no loader line; its Codex entry is the `counsel` skill under `plugins/coding-agent-orchestration-harness/skills/counsel/`.
