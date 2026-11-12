# Mechanisms: what each runtime really does

Findings of Task_1 of the plan `one-conversation-with-counsel-plan.md`.

Every fact in this file was seen on 2026-11-12, and each section heading repeats that date.

Each fact is marked one of three ways: **observed** (a trial was run and its result is stated), **documented** (the runtime's or tool's own documentation says so, with the page; no trial), or **unknown** (neither).

Versions the trials ran on: Claude Code 2.1.322 (terminal CLI, Windows), Codex CLI 0.167.2, the peer-messaging tool agmsg 1.5.0.

## Answers to the plan's assumptions (2026-11-12)

- A1 (Claude Code runs a plugin's named agent as the main session when the plugin's root `settings.json` sets it, on the surfaces people use): **held for the terminal CLI, observed**, in a non-interactive run and in a full terminal session started in the background. For the desktop app's Code tab and the IDE extensions it is **documented** as loading plugin `settings`, and was not tried. It is **not held** for cloud sessions and for claude.ai chat and Cowork, by documentation. Whom it reaches is listed under Claude Code below.
- A2 (Copilot offers a documented way for installed text to make the built-in agent hold a role when none is chosen, other than a skill's description matching): **not held**. No page read documents a default custom agent or a plugin-supplied always-on instruction. Two undocumented candidates are named under Copilot below and were not tried.
- A3 (a session can be started in the Orchestrator role with a first message, without a person, by at least one means): **held, observed**, by the Claude CLI's background-session option with the Orchestrator agent, in a directory whose workspace trust had already been given. A second means was observed in Codex (a non-interactive run whose first message invokes the Orchestrator skill by name), which ends when its one turn ends.
- A5 (a stopped session, and one that has something ready, can come to another session's attention without the owner saying anything, while that session stays free to answer him): **held for a watching session that is in the middle of a turn, observed**; **unknown by trial for a watching session that sits idle waiting for its user**, which the runtime's own tool description says is re-invoked the same way. The trial is under Watching a started session below.

## Claude Code (2026-11-12)

### What makes a session with no role chosen hold a named role

- Tried: a throwaway copy of the harness plugin with one added file at its root, `settings.json` holding `{"agent": "harness-counsel"}`, loaded for one session with the CLI's `--plugin-dir` option; first message asking only for the name of the role held; no agent flag.
- Observed: the session replied `Counsel`. The same copy without the added file replied `none`. (**observed**)
- Observed: the same holds in a terminal session started with the background option and no agent flag: its start-up header showed `@coding-agent-orchestration-harness:harness-counsel`, its transcript recorded that agent as the session's agent setting, and it replied `Counsel`. (**observed**)
- Observed: the bare agent name in the plugin's `settings.json` resolved to the plugin's own agent; the plugin-scoped name was not needed there. (**observed**)
- Observed: a plugin loaded for one session with `--plugin-dir` took the place of the installed plugin of the same name for that session. (**observed**)
- Observed: the runtime warns that the plugin's root `agents/` folder is ignored because the manifest sets `agents`; the six agents the manifest lists were the ones loaded. (**observed**)
- Documented: a `settings.json` at the plugin root, or the manifest's `settings` key, applies while the plugin is enabled; only `agent` and `subagentStatusLine` take effect; `agent` runs the main thread as one of the plugin's own agents. (**documented**: https://code.claude.com/docs/en/plugins/components, Default settings; https://code.claude.com/docs/en/plugins-reference, `settings`)
- Documented: plugin defaults are the lowest settings layer, so a person's own `agent` in a user, project or local settings file overrides the plugin's. (**documented**: same page, Default settings)

### What lets the opener choose either role

- Tried: the launch flag `--agent` with the plugin-scoped agent name, once for each role, with and without the plugin default present.
- Observed: `--agent` with the Orchestrator agent gave `Orchestrator` although the plugin default named Counsel; `--agent` with the Counsel agent gave `Counsel` where no default existed. (**observed**)
- Observed: an `agent` value passed for one session through the CLI's `--settings` option also overrode the plugin default (`Orchestrator`). (**observed**)
- Documented: `agent` in a project's `.claude/settings.json` makes that agent the default for every session in the project, and the launch flag overrides the setting. (**documented**: https://code.claude.com/docs/en/sub-agents, Invoke subagents explicitly)
- Unknown: whether the desktop app's Code tab and the IDE extensions offer the opener a way to name the session's agent other than a settings file. No page read says. (**unknown**)
- Not tried: invoking a role's skill by name as the first message in Claude Code.

### Whether a session's role can change while it lives

- Documented: the agent is chosen at launch, persists when the session is resumed, and no page read gives a way to switch the main session's agent in a running session. (**documented**: https://code.claude.com/docs/en/sub-agents, Invoke subagents explicitly)
- Tried: resuming a stopped background session that had been started as the Orchestrator, passing `--agent` with the Counsel agent.
- Observed: the runtime did not change the session; it said the session keeps its own saved options and started a copy under a new id. The copy's transcript still recorded the Orchestrator agent and it replied `Orchestrator`. The reply may follow the conversation history as well as the agent, so the recorded agent setting is the firmer evidence. (**observed**)
- Unknown: whether text loaded later in a session (a skill, a message) can make the model act under another role; the runtime has no mechanism that forbids it, and it was not tried. (**unknown**)

### Whom a plugin default would reach, and whom it would not

- Reached, observed: a person using the terminal CLI with the plugin enabled, in interactive terminal sessions, background sessions and non-interactive runs, who has set no `agent` of their own and passes no `--agent`.
- Reached, documented and not tried: the desktop app's Code tab in local and SSH sessions and the VS Code extension, which read the same settings files as the terminal and load plugin `settings`; JetBrains IDEs, which run the CLI in the IDE's terminal. (**documented**: https://code.claude.com/docs/en/plugins/install; https://claude.com/docs/plugins/platform-support, Compare component support by app)
- Not reached, documented: cloud sessions, including the browser, which do not load plugins installed on the person's machine or turned on by the repository's settings. (**documented**: https://code.claude.com/docs/en/plugins/install, Cloud session tab)
- Not reached, documented: claude.ai chat and Cowork, which ignore a plugin's `settings`; chat also ignores its agents. (**documented**: https://claude.com/docs/plugins/platform-support)
- Not reached: a person whose own user, project or local settings set `agent`, a person who launches with `--agent`, and a person who has the plugin disabled. The first is documented, the second observed.
- By way of installing: user, project and local scope all enable the same plugin, so the default follows the plugin at any scope; a project-scope entry turns the plugin on for collaborators but each still installs it once per clone. (**documented**: https://code.claude.com/docs/en/plugins/install, Choose an install scope)
- Unknown: the oldest Claude Code version that honours a plugin's `agent` setting. (**unknown**)
- Could not be tested here: the desktop app, the IDE extensions, cloud sessions, and an interactive terminal session opened by a person.

## Codex (2026-11-12)

### What makes a session with no role chosen hold a named role

- Read: the bootstrap skill and its script. The managed loader block is written only to the `AGENTS.md` in the Codex home, only in a user-scope install, and only when the person answers yes or passes `--user-instructions add`; a repository-scope install writes no block. The block's present text routes coding tasks to the Orchestrator skill and names no role for other sessions.
- Tried: a non-interactive Codex run (`codex exec`, read-only sandbox, not persisted) in a scratch directory with the harness plugin installed and the loader block present, first message asking only for the role held.
- Observed: it replied `primary agent`, which is no harness role. (**observed**)
- Tried: the same run in a scratch directory holding an `AGENTS.md` that says a session with no role chosen holds a role with a made-up name, and that a first message naming another role gives that role.
- Observed: with no role named the session replied with the default role's name; with the other role named in the first message it replied with that one. Instruction-file text can therefore give a default role and leave the choice to the opener. (**observed**)
- Documented: Codex reads one `AGENTS.md` from the Codex home and one per directory from the project root down to the working directory, and builds that chain once per run, which for the terminal UI is once per launched session. (**documented**: https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- The plugin manifest's default prompt: the page on building plugins shows `defaultPrompt` only inside an example of interface metadata, as short starter prompts, and says nothing of it as an instruction. (**documented**: https://developers.openai.com/codex/plugins/build, Add OpenAI-specific metadata) In the first trial above the plugin with its default prompt was installed and the session held no harness role. (**observed**, for a non-interactive run, which has no composer in which a starter prompt could be shown)
- Whether a plugin install alone can give a default: no page read lets a plugin add instruction-file text or name a default agent. A plugin can bundle hooks, and a `SessionStart` hook's output is added to the model's context, but a hook that is not managed by policy must be reviewed and trusted by the person before it runs, and the plugin page says lifecycle hooks are supported for plugins installed manually in the desktop app. So by documentation a plugin install alone gives no default without a further act by the person. (**documented**: https://developers.openai.com/codex/plugins/build; https://learn.chatgpt.com/docs/hooks) Not tried.

### What lets the opener choose either role

- Tried: a non-interactive run whose first message invokes the Orchestrator skill by name and says the session is opened as the Orchestrator.
- Observed: it replied `Orchestrator`. (**observed**)
- Observed in the CLI's help output: no option names an agent or role for the main session. (**observed**)
- Not tried: the same for the Counsel skill; an interactive session.

### Whether a session's role can change while it lives

- Documented: the instruction chain is fixed for the run once built. (**documented**: https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- Unknown: the role is held by instruction text and the conversation only; nothing in the runtime fixes it, and whether a later message changes it was not tried. (**unknown**)

### Whom a default carried by the loader block would reach, and whom it would not

- Reached: a person who ran the bootstrap at user scope and added the block, in runs that read the Codex home's `AGENTS.md`. Observed for the CLI's non-interactive run only.
- Not reached: a person who installed the plugin and did not run the bootstrap; one who ran it at repository scope; one who ran it at user scope and declined the block. (read from the script)
- Not reached until they run the bootstrap again: a person whose block was written by an earlier version, since the block is replaced only when the bootstrap is run and told to. (read from the script)
- Unknown: whether the IDE extension, the desktop app and cloud tasks load the Codex home's `AGENTS.md`; the page speaks only of the command-line tool and its terminal UI. (**unknown**)
- A repository's own `AGENTS.md` would reach everyone who runs Codex in that repository (observed in a scratch directory), but it is a file of the repository, not something a plugin install writes.

## GitHub Copilot in VS Code (2026-11-12)

No trial was made: every way in needs a person at the editor.

### What makes a session with no role chosen hold a named role

- Documented: a custom agent is chosen per chat from the Agent dropdown; the page names no setting or file that makes a custom agent the default for new chats. (**documented**: https://code.visualstudio.com/docs/copilot/customization/custom-agents)
- Documented: an agent plugin can contribute skills, custom agents, rules, hooks, MCP servers and slash commands; the page does not say a plugin can set a default agent, and describes plugin rules only as reusable guidance, not as always applied. Agent plugins need the `chat.plugins.enabled` setting turned on. (**documented**: https://code.visualstudio.com/docs/copilot/customization/agent-plugins)
- Documented: the project instruction files the Copilot harness includes are `.github/copilot-instructions.md` or `AGENTS.md`, which are files of the workspace; the page says instructions can be distributed as rule components in a plugin and that support depends on the harness and plugin format. (**documented**: https://code.visualstudio.com/docs/copilot/customization/custom-instructions)
- Documented: hooks are in preview; a `sessionStart` hook exists "to add context when a session starts or resumes", and a plugin can bundle hooks; the page does not show the form in which a `sessionStart` hook returns context. (**documented**: https://code.visualstudio.com/docs/copilot/customization/hooks)
- So: **no mechanism is documented** by which installed plugin text makes the built-in agent hold a role when none is chosen. Two candidates exist that the documentation does not carry that far, a plugin rule and a plugin `sessionStart` hook; neither was tried, and whether either is applied to every chat is **unknown**.

### What lets the opener choose either role

- Documented: plugin agents that allow user invocation are selectable in the Agent dropdown; `user-invocable: false` hides one. (**documented**: custom-agents page) The package's Copilot agent files for the Orchestrator and Counsel set `user-invocable: true`. (read from the package)

### Whether a session's role can change while it lives

- Documented: "The custom agent remains selected until you switch agents"; the person can switch the agent in the same chat, and a handoff button switches it too in the Local harness. So the runtime lets the person change the agent of a living chat. (**documented**: custom-agents page)

### Whom a default would reach

- Nobody, by any documented mechanism. A workspace instruction file would reach those who open that workspace, and is not written by installing the plugin.

## Starting a session in the Orchestrator role without a person (2026-11-12)

### The Claude CLI's background-session option

- Tried: `claude --bg --agent <the plugin-scoped Orchestrator agent> --name <name> "<first message>"`, run from a shell with no terminal attached, the first message asking only for the role held.
- Observed: the command returned at once and printed a short id; the session ran as a full terminal session with the Orchestrator agent in its header, and replied `Orchestrator`. (**observed**)
- Observed: in a directory whose workspace trust had never been given, the same command created no session and exited with `Workspace not trusted`, telling the person to run the CLI there once and accept the prompt. (**observed**; **documented**: https://code.claude.com/docs/en/agent-view) Nothing was done to get past it.
- Documented: the option cannot be combined with the non-interactive print option; the first message is the positional argument. (**documented**: same page; the trials used the positional form)
- Documented: a separate supervisor process runs background sessions, so they outlive the shell that started them; a restart of the machine stops them; a session that has finished or waits for its next message and has had nobody attached for about an hour has its process stopped and resumes on the next reply. (**documented**: same page) The supervisor was seen to start on demand with the first background session.

### Codex

- Tried: `codex exec` with a first message, as above.
- Observed: it runs one turn without a person and exits; it is not a session that stays alive, and it can be continued with `codex exec resume <id>` unless it was run as not persisted, as these were. (**observed** for the run and exit; resume is **documented**: https://learn.chatgpt.com/docs/non-interactive-mode)

### The peer-messaging tool's spawn

- Not tried, because it registers the new agent as a member of the project's existing team before launching it.
- Documented: `spawn <type> <name>` joins the name to the team and launches that runtime's CLI with the tool's identity command as its first prompt; `--boot-prompt <text>` adds a first task to that same first turn; it opens a pane in a terminal multiplexer, or else a new terminal window, and errors where neither is available; by default it waits until the new agent is listening. It has no option that names an agent or role for the launched session, other than extra CLI flags set per agent type in the tool's spawn-options file. (**documented**: the tool's README, Spawn a new agent)
- Documented: its `despawn <name>` ends a spawned member, gracefully by a control message or with `--force` from the placement recorded at spawn. (**documented**: the tool's README, Tear down a spawned agent)

## Watching a started session from outside (2026-11-12)

### Liveness and state

- Tried: `claude agents --json`, and the same with `--all`, polled from a shell while the background sessions ran and after they were stopped.
- Observed: a running background session is listed with a process id, `status` and `state`. While it worked: `status: busy`, `state: working`. After it finished its turn and waited for the next message: `status: idle`, `state: done`. (**observed**)
- Observed: a session that met a permission prompt was listed with `status: waiting`, `waitingFor: permission prompt`, `state: blocked`. (**observed**)
- Observed: after `claude stop`, the session has no process id and no `status`, is absent from the plain listing and present under `--all`; its `state` was `done` where it had finished its turn before the stop and `stopped` where it was stopped while blocked. (**observed**)
- Documented: the states are `working`, `blocked`, `done`, `failed` and `stopped`; `waitingFor` is one of `permission prompt`, `input needed`, `sandbox request`, `worker request`, `dialog open`; `blocked` always means the session needs something from the person, and `done` means it finished its turn; a session whose process was ended from outside or that ended while the supervisor was off shows as `stopped`, and one cut off by a shutdown shows as `failed`; the files under the runtime's jobs directory are not a stable interface. (**documented**: https://code.claude.com/docs/en/agent-view)
- Observed: `claude logs <id>` prints the session's recent terminal screen, which showed the first message, the reply and, when blocked, the text of the prompt. The session's transcript file also holds the messages. (**observed**)
- So working, waiting and stopped can be told apart from outside. What a waiting session waits for is given as a kind, not as the thing it named; the thing itself has to be read from its screen or transcript. (**observed**)
- Unknown: nothing observed tells a session that is working long from one that is stuck while its process lives; both read `working`. (**unknown**)

### Bringing a stopped or reporting session to another session's attention

- Tried: from the watching session, a shell command run in the background that polls `claude agents --json --all` and exits when the watched session's `state` is no longer `working`.
- Observed: the watching session went on with other work, and was notified by the runtime when the command exited, at the moment the watched session became `blocked`. No person said anything. (**observed**) The watching session was a subagent in the middle of a turn.
- Unknown by trial: the same for a top-level session that is idle and waiting for its user. The runtime's description of its own background-command tool says such a command keeps running across turns and re-invokes the session when it exits. (**unknown** by trial)
- Documented: while the agent view is open, the runtime sends a terminal notification and fires the `Notification` hook when a background session starts needing input, finishes or fails. (**documented**: https://code.claude.com/docs/en/agent-view) This reaches a person or a hook, not another session, and was not tried.
- Documented: with the peer-messaging tool in monitor delivery, a message sent to a Claude Code session reaches it as an event within seconds without its user, once that session has taken one turn; a Codex session receives messages only between turns unless it was launched through the tool's bridge. (**documented**: the tool's README, Delivery modes) A started session that sends a message when it has something ready would reach the other session this way; not tried here.

### Sending a further message, and ending the session

- Observed: `claude --bg --resume <session id> "<message>"` with other flags started a copy; the runtime's note says that without flags the same command continues the original session under the same id. (**observed** for the copy; the flagless continuation is stated by the runtime and was not tried)
- Documented: a person can reply to a background session from the agent view; a reply does not answer a permission prompt. (**documented**: agent-view page)
- Observed: `claude stop <id>` ended each session's process and kept its conversation. (**observed**)
- Documented and not tried: `claude rm <id>` removes a session from the list, with a worktree the runtime created for it when that is safe. (**documented**: agent-view page; the CLI's help)

## Permission checks (2026-11-12)

### What a started session does when it meets one

- Tried: a background Claude Code session started with `--permission-mode manual` and asked to write one file in a scratch directory outside its working directory and outside any repository.
- Observed: it stopped at the prompt and stayed there, listed as `blocked` with `waitingFor: permission prompt`; nothing was written; it was stopped unanswered. A background session does not decide a prompt for itself and does not fail: it waits. (**observed**)
- Documented: a prompt in a background session is answered only by a person who attaches to it. (**documented**: agent-view page)
- Observed: a background session started without a permission-mode flag ran in the permission mode the owner's settings name. (**observed**)
- Documented and not tried: in a non-interactive run the option `--permission-prompts none` makes anything that would prompt be denied automatically. (the CLI's help)
- Tried in Codex: a non-interactive run under the read-only sandbox asked to create one file in a scratch directory.
- Observed: the file was not created, no approval prompt appeared, and the session reported the failure and ended. (**observed**)

### What the owner's own settings can settle beforehand

- Claude Code, documented: `permissions.allow`, `permissions.ask`, `permissions.deny`, `permissions.defaultMode` and `permissions.additionalDirectories` can be set in the user settings file, the project's `.claude/settings.json`, the project's local `.claude/settings.local.json` and managed settings; allow rules approve the listed tool uses without a prompt. (**documented**: https://code.claude.com/docs/en/settings-reference) The rule syntax was not read.
- Claude Code, observed: workspace trust for a directory is a separate check that only a person's one-time acceptance in an interactive run settles; no setting was found that gives it. (**observed** for the refusal; **documented**: agent-view page)
- Codex, observed in the CLI's help and documented: the approval policy and sandbox mode are set in the Codex home's `config.toml`, per run by `--sandbox`, and by rule files; a non-interactive run defaults to the read-only sandbox. (**documented**: https://learn.chatgpt.com/docs/non-interactive-mode)
- No setting was created or changed for these trials, and no mode that skips a runtime's checks was used.

## A repository where no setup has yet run (2026-11-12)

### What means to start a session exist there

- The Claude CLI's background option exists wherever the CLI is installed and needs no setup of the harness. It needs the directory's workspace trust, which a person gives once in an interactive run there, and it needs the harness plugin enabled for the Orchestrator agent's name to resolve. (**observed**: both conditions were met in the directory where the start succeeded, and the untrusted directory refused)
- Documented: if the agent name matches nothing, the launch prints a warning, still reports the session as backgrounded, and the session exits at once with an error. (**documented**: agent-view page)
- `codex exec` exists wherever the Codex CLI is installed; the Orchestrator role by naming the skill needs the plugin installed in Codex. (**observed** where it was installed)
- The peer-messaging tool's spawn needs that tool installed, a team for the project and a terminal it can open. (**documented**: the tool's README)
- Unknown: whether a session opened by a person in a directory through the desktop app or an IDE extension leaves that directory trusted for the CLI's background option. (**unknown**)

### How a workspace's record of such means could be filled without the person opening an Orchestrator session

- Observed: the facts such a record needs were all established here by commands that need no person and no particular role: the CLIs' version and help output, `claude agents --json`, and a start of one background session with a harmless first message followed by `claude stop`. A session of any role that has a shell can run them. (**observed**)
- So nothing in the runtimes requires an Orchestrator session to find or record the means. Which role may write the record into the workspace's rule files is a question of the harness's own rules, not a fact about the runtimes.
- Unknown: whether a Counsel session on every surface has a shell with which to run them; it has in the terminal CLI. (**unknown** for other surfaces)

## Sessions started for these trials (2026-11-12)

Each got one harmless first message, changed no file in any repository, and none is left running.

- Claude Code, non-interactive, plugin copy with the default agent, no agent flag: ended by itself after its one reply.
- Claude Code, non-interactive, plugin copy without the default: ended by itself after its one reply.
- Claude Code, non-interactive, default present and `--agent` naming the Orchestrator: ended by itself after its one reply.
- Claude Code, non-interactive, no default and `--agent` naming Counsel: ended by itself after its one reply.
- Claude Code, non-interactive, default present and `agent` given by `--settings`: ended by itself after its one reply.
- Claude Code, background, in an untrusted scratch directory: no session was created.
- Claude Code, background, `--agent` naming the Orchestrator: ended with `claude stop` after its reply.
- Claude Code, background, the copy made by resuming the one above with another agent flag: ended with `claude stop` after its reply.
- Claude Code, background, manual permission mode, asked to write one scratch file: ended with `claude stop` while blocked at the prompt; the file was not written.
- Claude Code, background, plugin copy with the default agent and no agent flag: ended with `claude stop` after its reply.
- Codex, non-interactive, no role named: ended by itself when its turn ended.
- Codex, non-interactive, scratch directory with a default role in `AGENTS.md`, no role named: ended by itself when its turn ended.
- Codex, non-interactive, same directory, another role named in the first message: ended by itself when its turn ended.
- Codex, non-interactive, first message invoking the Orchestrator skill: ended by itself when its turn ended.
- Codex, non-interactive, read-only sandbox, asked to create one scratch file: ended by itself when its turn ended; the file was not created.
- The four stopped background sessions were not removed with `claude rm`; they remain as ended entries in the runtime's list of past sessions.
