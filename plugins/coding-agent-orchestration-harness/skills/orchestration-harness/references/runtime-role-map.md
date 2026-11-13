# Runtime Role Map

Logical roles are stable. Physical agent names may vary by runtime.

| Logical role | GitHub/Copilot physical name | Claude Code physical name | Codex physical name |
|---|---|---|---|
| Orchestrator | Orchestrator | harness-orchestrator | main Codex thread following `$orchestration-harness` |
| Researcher | Researcher | harness-researcher | harness_researcher |
| Worker | Worker | harness-worker | harness_worker |
| Reviewer | Reviewer | harness-reviewer | harness_reviewer |
| Auditor | Auditor | harness-auditor | harness_auditor |
| Counsel | Counsel | harness-counsel | main Codex thread following `$counsel` |

## How A Session Gets Its Role

A session's role is set when it is opened, by the opener's choice or by default, and does not change while the session lives: another role is another session.
A skill loaded because its description matched gives a session no role, and neither does an incidental reference to a role's skill.
A session that holds no role takes one when the person opening it invokes the role's skill by name; a session that already holds a role does not.
What each runtime does below was seen on 2026-11-12, except where a line gives its own date.

- Claude Code, no agent chosen: the session is Counsel, because the plugin's root `settings.json` names `harness-counsel` as the plugin's default agent. The default holds wherever Claude Code loads a plugin's settings; cloud sessions, claude.ai chat and Cowork do not load them, and it does not reach those.
- Claude Code, by choice: launch the session as the role's agent (`claude --agent coding-agent-orchestration-harness:harness-orchestrator` or `claude --agent coding-agent-orchestration-harness:harness-counsel`), or set `agent` in the person's own user, project or local settings. Either overrides the plugin's default. A resumed session keeps the agent it was saved with.
- GitHub Copilot, by choice: select the `Orchestrator` or `Counsel` agent in the Agent dropdown when starting a chat. Copilot also lets the person switch the agent of a living chat in that dropdown; the harness cannot forbid what the runtime allows, and no harness text asks for it: for another role, start a new chat.
- Codex, by choice: invoke the role's skill by name in the first message, `$orchestration-harness` for the Orchestrator or `$counsel` for Counsel. The Codex CLI has no option that names an agent for the main session, so the role is held by the skill's text and the conversation, and nothing in the runtime fixes it.
- Codex and GitHub Copilot, no role chosen: neither runtime lets a plugin install give a session a role, so there the default is carried by the repository's own instructions. The harness's setup writes a marked block into them (`rulebook/references/bootstrap-lifecycle.md`, Default Role Block): a session opened in that repository with no role chosen is Counsel and says so in its first reply, with how the Orchestrator is opened, and the Orchestrator stays the opener's choice. A repository where setup has not written the block has no default in these two runtimes, and a session opened there with no role chosen holds none. No text the harness installs makes a session the Orchestrator without its opener's choice: the block the Codex bootstrap offers for the Codex home gives no role.
- Codex, the default as seen on 2026-11-13: in non-interactive runs with the plugin installed, the block in the repository's `AGENTS.md` gave Counsel in five of five runs that named no role, three of them coding requests made while the Codex home held the earlier block that routed coding tasks to the Orchestrator, and a first message invoking `$orchestration-harness` gave the Orchestrator. Untried: an interactive session, the IDE extension, the desktop app, cloud tasks, a person who has not installed the plugin, and the block as setup itself writes it (the trial's was written by hand). The role is held by instruction text only, so the runs are no guarantee. A Codex home that still holds the earlier block sends a coding request to the Orchestrator skill in a repository without the default (seen in one run), until the bootstrap is run again and replaces it.
- GitHub Copilot, the default untried as of 2026-11-13: setup writes the block to `.github/copilot-instructions.md`, which the runtime documents as a repository instruction file it includes. No chat was opened to see it followed, so the default is not counted as delivered there. The other documented way is a start-of-chat hook carried by the plugin; the owner has left open whether it is tried, and nothing installs one.

## Home Of Each Session Role

A session holds one role and takes its mechanics from that role's home. It never loads another role's home; what the roles share is in a home of its own that names no role's procedure.

- Orchestrator, and the Researcher, Worker, Reviewer and Auditor it dispatches: the `orchestration-harness` skill and its references. The Auditor's value audit and goal assessor mandates live in those references.
- Counsel: the `counsel` skill and its references.
- The forms of the value documents have a home of their own, the `value-documents` skill, which both role homes point to and which points to neither.

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
- Codex physical names should correspond to templates under `plugins/coding-agent-orchestration-harness/codex/agent-templates/`.
- The Orchestrator and Counsel have no Codex template: each is its skill under `plugins/coding-agent-orchestration-harness/skills/`.
