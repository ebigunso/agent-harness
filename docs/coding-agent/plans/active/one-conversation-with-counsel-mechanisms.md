# Mechanisms: what each runtime really does

Findings of Task_1 of the plan `one-conversation-with-counsel-plan.md`.

Every fact in this file was seen on 2026-11-12, and each section heading repeats that date.

Each fact is marked one of three ways: **observed** (a trial was run and its result is stated), **documented** (the runtime's or tool's own documentation says so, with the page; no trial), or **unknown** (neither).

Versions the trials ran on: Claude Code 2.1.322 (terminal CLI, Windows), Codex CLI 0.167.2, the peer-messaging tool agmsg 1.5.0.

## Answers to the plan's assumptions (2026-11-12)

- A1 (Claude Code runs a plugin's named agent as the main session when the plugin's root `settings.json` sets it, on the surfaces people use): **held for the terminal CLI, observed**, in a non-interactive run and in a full terminal session started in the background. For the desktop app's Code tab and the IDE extensions it is **documented** as loading plugin `settings`, and was not tried. It is **not held** for cloud sessions and for claude.ai chat and Cowork, by documentation. Whom it reaches is listed under Claude Code below.
- A2 (Copilot offers a documented way for installed text to make the built-in agent hold a role when none is chosen, other than a skill's description matching): **unknown**. No page read documents a default custom agent. A plugin can carry a `sessionStart` hook whose output adds context to the session, which is documented; whether that gives every chat with no agent picked the default role, on every surface and for every way of installing, was not tried and is not documented. The facts are under Copilot below.
- A3 (a session can be started in the Orchestrator role with a first message, without a person, by at least one means): **held, observed**, by the Claude CLI's background-session option with the Orchestrator agent, in a directory whose workspace trust had already been given. A second means was observed in Codex (a non-interactive run whose first message invokes the Orchestrator skill by name), which ends when its one turn ends.
- A5 (a stopped session, and one that has something ready, can come to another session's attention without the owner saying anything, while that session stays free to answer him): **unknown as a whole by Task_1's trials**. One part was observed: a watching session that was a subagent in the middle of a turn was notified when its background poll saw the watched session become blocked. A second part was observed afterwards by the Orchestrator session itself, and is recorded under Watching a started session below: a top-level session that sat idle was woken by a finished background command with no input from its user. Not observed: that the watching session goes on answering its user while it handles such an event, and anything that tells a session working long from one that is stuck.

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

- Reached, observed: a person using the terminal CLI with the plugin enabled, in background terminal sessions and non-interactive runs, who has set no `agent` of their own and passes no `--agent`. An interactive terminal session opened by a person was not tried; that it behaves as the background terminal session did is an inference.
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

- Would be reached, by inference: a person who ran the bootstrap at user scope and added the block, in runs that read the Codex home's `AGENTS.md`, if the block carried a default. No trial put a default into a Codex home's block: the trial that showed instruction text giving a default used an `AGENTS.md` in a scratch directory, and the trial with the present home block returned no harness role.
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
- Documented: hooks are in preview; a `sessionStart` hook exists "to add context when a session starts or resumes", a plugin can bundle hooks, and the shared hooks reference gives the hook's output form, with an `additionalContext` field added to the session's context. (**documented**: https://code.visualstudio.com/docs/copilot/customization/hooks; https://code.visualstudio.com/docs/agents/reference/agent-plugin-reference, Supported hook events; https://docs.github.com/en/copilot/reference/hooks-reference, sessionStart)
- So: no setting or file is documented that makes a custom agent the default. Context added at the start of a session by a plugin's hook is documented; that it makes the built-in agent hold a role in every chat is **unknown**: it was not tried, a hook may need the person's trust before it runs, and the hooks are in preview. A plugin rule is a second candidate, described only as reusable guidance; whether it is applied to every chat is **unknown**.

### What lets the opener choose either role

- Documented: plugin agents that allow user invocation are selectable in the Agent dropdown; `user-invocable: false` hides one. (**documented**: custom-agents page) The package's Copilot agent files for the Orchestrator and Counsel set `user-invocable: true`. (read from the package)

### Whether a session's role can change while it lives

- Documented: "The custom agent remains selected until you switch agents"; the person can switch the agent in the same chat, and a handoff button switches it too in the Local harness. So the runtime lets the person change the agent of a living chat. (**documented**: custom-agents page)

### Whom a default would reach

- **Unknown**. By a default-agent setting, nobody: none is documented. By context a plugin's `sessionStart` hook adds: untried, so whom it would reach is not known. A workspace instruction file would reach those who open that workspace, and is not written by installing the plugin.

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
- Observed by the Orchestrator session on 2026-11-12, after Task_1: a top-level session that had ended its turn and was waiting for its user was re-invoked by the runtime when a background shell command it had started exited, 45 seconds later, with no input from the user. (**observed**) Not observed: what the user experiences if he writes while that re-invoked turn is running; the runtime handles one turn at a time, so by inference his message waits for that turn to end. (**unknown** by trial)
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

## The two answers tried in practice (2026-11-13)

Findings of Task_9 of the same plan, on the two ways the owner accepted on 2026-11-13 (brief, Directed during the run). Every fact under this heading and the headings below that repeat its date was seen on 2026-11-13, and is marked observed, documented or unknown as above.

Versions the trials ran on: Claude Code 2.1.323 (terminal CLI, Windows), Codex CLI 0.167.2. The harness plugin installed for Codex was the released 1.5.0, whose text is older than this branch's: its Counsel skill does not yet tell a Counsel session to say so in its first reply. The Claude Code session of the second way loaded this branch's plugin for that one session with `--plugin-dir`.

The acceptance carried in these trials was a stand-in. It was worded as a trial, named the throwaway repository and its proposed test entry, quoted made-up words marked as said by no real person, and went only to the trial's own sessions. It is nobody's authorization and put nothing in effect; the repositories it named are removed.

## The default in a set-up repository: Codex (2026-11-13)

### What was tried

- A throwaway git repository holding one small source file and an `AGENTS.md` at its root with this block and nothing else:

```md
<!-- coding-agent-orchestration-harness:default-role:start -->
## Coding Agent Orchestration Harness: the role of a session opened here

- A session opened in this repository with no role chosen is Counsel: load and follow `$counsel`, and say in the first reply that the session is Counsel and how a session is opened as the Orchestrator (a new session whose first message invokes `$orchestration-harness` by name).
- A session whose first message chooses the Orchestrator, by invoking `$orchestration-harness` by name or by saying it is opened as the Orchestrator, is the Orchestrator: load and follow `$orchestration-harness` and not `$counsel`.
- A skill loaded because its description matched gives a session no role.
<!-- coding-agent-orchestration-harness:default-role:end -->
```

- The Codex home's `AGENTS.md` held the present loader block throughout, which routes coding tasks to the Orchestrator skill. It was read and not changed.
- Non-interactive runs (`codex exec`, read-only sandbox, not persisted) in that repository: two with a first message that only opens a talk about what the project should do; one whose first message invokes the Orchestrator skill by name and says the session is opened as the Orchestrator; three with a first message that is a plain coding request and names no role. One control run with the same coding request in a second throwaway repository that has no `AGENTS.md`.

### What was observed

- No role chosen, a talk opened (2 of 2 runs): the session's first message of the turn said it is Counsel and that implementation is handled in a new session whose first message invokes the Orchestrator skill by name. It then loaded the Counsel skill and not the Orchestrator skill, looked for the rule files, said setup had not run, and asked for the idea. (**observed**)
- The statement that the session is Counsel was in the first message of the turn, written before the skill was loaded, and was not repeated in the message that ended the turn. A non-interactive run's "last message" output therefore does not hold it; the run's full output does. (**observed**) Whether the terminal UI shows a person both messages was not tried. (**unknown**)
- The announcement came from the repository's block: the installed Counsel skill has no such sentence. (**observed**, by reading the installed skill)
- The Orchestrator chosen in the first message (1 run): it replied that it holds the Orchestrator role and had loaded the Orchestrator skill only. (**observed**)
- A coding request with no role chosen (3 of 3 runs): the session said it is Counsel, loaded the Counsel skill (two of the three also read the Orchestrator skill's file), changed no file, and told the person to open a new session whose first message invokes the Orchestrator skill, quoting the Counsel skill for why. None took the Orchestrator role. (**observed**)
- The control run, with the Codex home's loader block and no repository file: it loaded the Orchestrator skill and made the change. So the home block alone sends a coding request to the Orchestrator skill, and with both texts present the repository's block won in every run. (**observed**)
- Why the repository's text wins: Codex joins the Codex home's file and then the project's files from the root down, and "files closer to your current directory override earlier guidance because they appear later in the combined prompt". (**documented**: https://learn.chatgpt.com/docs/agent-configuration/agents-md) The replies also quoted the Counsel skill, which tells a Counsel session not to take the Orchestrator role when a loader instruction routes coding tasks there. The runs printed no reasoning, so which of the two decided it in the model is **unknown**.
- The role is held by instruction text and the conversation only, as on 2026-11-12: six runs agreeing is not a guarantee, and another model or a longer instruction chain may read it differently.
- Every run printed that a start-of-session hook ran and completed. The harness plugin carries no hook, so it was not the harness's; a start hook does therefore run in non-interactive runs on a machine where one is installed and allowed. Whose it was and how it came to be allowed were not established. (**observed** for the run of a hook; the rest **unknown**)
- In the control run the header named the read-only sandbox and the change to the file was nevertheless made, by a script passed to an interpreter. A write through the shell was refused under the same sandbox on 2026-11-12. So the read-only sandbox was not seen to stop every way of writing. (**observed**, one run)

### What could not be tried

- An interactive Codex session opened by a person, the IDE extension, the desktop app and cloud tasks.
- A person who opens the repository in Codex without the harness plugin installed: the block names skills that would not be there.
- The block written by setup itself: it was written by hand, as setup would write it.

## The default in a set-up repository: Copilot, untried (2026-11-13)

No trial was made: both ways need a person at the editor. What follows is what a person would put in place and look for, from the documentation as read on 2026-11-13. Both are **untried**, and the file names and forms are **documented**, not observed.

### (a) The repository instruction file

Documented: the Copilot harness includes the project instruction file `.github/copilot-instructions.md` or `AGENTS.md`, at the repository root; the page says not to rely on a universal order of precedence between instruction sources. (https://code.visualstudio.com/docs/copilot/customization/custom-instructions)

1. In a throwaway folder that is a git repository, create `.github/copilot-instructions.md` holding the block above, with its second sentence reworded for Copilot: a chat in which the `Orchestrator` agent is selected in the Agent dropdown is the Orchestrator, and for the other role a new chat is started with that agent selected.
2. Have the harness plugin installed and agent plugins turned on in VS Code, then open the folder.
3. Run "Chat: Open Customizations", select Instructions, and check that the file is listed. This shows it was found, not that it is followed.
4. Start a new chat with no agent selected and type one sentence that asks for no code. Look for: the first reply says the chat is Counsel and how the Orchestrator is opened; the reply's References list names the instruction file; the Counsel skill was loaded.
5. Start another new chat with no agent selected and ask for a small code change. Look for: it stays Counsel, changes nothing, and points to the Orchestrator agent.
6. Start a new chat with the `Orchestrator` agent selected and ask the same. Look for: it acts as the Orchestrator and does not say it is Counsel.
7. Note the VS Code version and which of the six results held.

### (b) The plugin's start-of-chat hook

Documented: hooks are in preview; a `sessionStart` hook returns an object whose `additionalContext` text is added to the session; for the Copilot plugin format the hook file is `hooks.json` at the plugin root and `${PLUGIN_ROOT}` names that root; a local plugin folder is registered with the `chat.pluginLocations` setting, marked experimental. (https://code.visualstudio.com/docs/copilot/customization/hooks; https://code.visualstudio.com/docs/agents/reference/agent-plugin-reference; https://docs.github.com/en/copilot/reference/hooks-reference) The hooks reference names the Copilot CLI and the cloud agent as where the events run and does not name VS Code. The package carries no hook today.

1. Copy the plugin to a throwaway folder and add `hooks.json` at its root: `"version": 1`, and under `hooks` a `sessionStart` list with one command entry (`"type": "command"`, a `bash` and a `powershell` command, a timeout) whose script prints one JSON object, `{"additionalContext": "<the block's three sentences>"}`.
2. Word the first sentence so that it applies only when no agent is selected: the hook's input does not say which agent the chat has, so the same text reaches a chat opened as the Orchestrator.
3. Turn off the installed copy of the plugin and register the throwaway copy with `chat.pluginLocations`. This is a change to the person's own editor settings; undo it afterwards.
4. Open a folder that has no instruction file, start a new chat with no agent selected, and type one sentence that asks for no code. Look for: whether the editor asks to review or trust the hook before it runs; the first reply says the chat is Counsel and how the Orchestrator is opened; the agent debug log shows the hook ran.
5. Repeat with a small code change asked for, and again with the `Orchestrator` agent selected. Look for the same results as in (a) 5 and 6, above all that the Orchestrator chat does not call itself Counsel.
6. Note the VS Code version, whether the hook ran at all in the editor, and whether it ran again when an old chat was reopened.

## The first time in a repository: where a session can be started (2026-11-13)

- Tried: the Claude CLI's background-session option with a harmless first message in three throwaway places no session had ever been opened in: a new git repository in a scratch directory; a new git repository placed beside working trees that are trusted; and a new worktree of a throwaway repository, placed beside those working trees.
- Observed: all three refused with `Workspace not trusted` and created no session. Trust is given per folder: it does not carry to a folder beside a trusted one, and being a git worktree gives none. (**observed**) Nothing was done to get past it.
- Not tried: a new folder inside a trusted folder. Every trusted folder on hand is a repository these trials may not write into.
- So no throwaway repository could have a session started in it. The rest of this way was run with what does start: a background session started in a working tree already trusted, and told to set up the throwaway repository by its path. What that leaves untried: a setup session whose working directory is the repository it sets up, and so the permission checks on writes inside its own working directory.
- In the brief's scenario the owner has already opened a Counsel session in the repository. In the terminal CLI that is where the trust prompt is accepted, so a session started there afterwards would meet the condition by his having opened the first conversation: an inference, not observed. For a first conversation opened from the desktop app or an IDE extension it stays **unknown** (as on 2026-11-12).
- Codex: non-interactive runs started in throwaway folders never used before without any refusal. (**observed**) The one run that was persisted and given the workspace-write sandbox left that folder recorded as trusted in the Codex home's configuration file, written by the runtime with no act of a person; the runs that were not persisted and ran read-only left no such record. Which of the two differences caused it was not separated. (**observed**, one run)

## The first time in a repository: the setup session (2026-11-13)

### What was tried

- `claude --bg --agent <the plugin-scoped Orchestrator agent> --plugin-dir <this branch's plugin> --name <name> "<first message>"`, run from a trusted working tree with no terminal attached.
- The first message stood alone. It said that it is a trial in a throwaway repository and that nobody's authority stands behind it; named the throwaway repository's path as the repository to set up and forbade writing anywhere else; asked for the full bootstrap of the rulebook skill, with the entry that admits Counsel's relays written into `common.md` as proposed and awaiting acceptance; asked the session to end its turn saying what it waits for and from whom; and set the trial's conditions: start no session, dispatch no subagent, use no peer-messaging tool, and stop at any permission check.

### What was observed

- State from outside: `busy`, `working` for under two minutes, then `idle`, `done`. It was never listed as waiting for a permission prompt. (**observed**)
- Permission checks: the session ran in the runtime's automatic permission mode, which the settings in force named. It made seven file writes, all outside its working directory, and the runtime marked each as allowed by the automatic mode; nothing was asked. (**observed**) Under a mode that asks, a background session stopped at the prompt and waited (2026-11-12). So whether a started session stops in its own window depends on the permission mode the person's settings name, not on anything the harness's text does.
- What it wrote, all inside the throwaway repository and nothing elsewhere: the five rule files and the lifecycle file in the order the reference gives, and, unasked, the file that stages candidates for the harness. It made no commit. (**observed**)
- The entry: under Standing Approvals, the template's sentence naming `<repository>-counsel`, marked "proposed 2026-11-13; awaits the owner's acceptance; not in effect", with "Given and accepted by: awaiting". The Counsel line under Repository Reference Documents was not written. (**observed**)
- It found the plugin's text disagreeing with itself and said so: the rulebook's template and Counsel Relay Admission write the entry only on the owner's yes ("Before acceptance, neither is written"), while Standing Approvals in the value-level operation reference says to "write the entry and send it to the owner by the carrier with the path to the file". It followed the first message and Standing Approvals, and staged the disagreement as a candidate. (**observed**)
- The end of its turn: its reply was headed blocked, named every file written, and said what it waits for and from whom: "the repository owner, speaking directly in this session. No relay counts yet, because none has been admitted." It asked for the owner's own words accepting the entry as it stands with the identity it names, and said the commit that puts the entry in effect is on his word too. (**observed**)
- It waits for more than the entry: the same reply holds setup's own questions for the owner (what the work runs on, a budget allowance, whether decision records get a folder), and the models record stays unconfirmed until he answers. A first setup therefore has several things to carry to him and back, not one. (**observed**)
- From outside, the listing said only `done`. What the session waits for had to be read from its screen or transcript, as on 2026-11-12. (**observed**)
- The record's line on the means to start, watch and end a session was written as none found, because the trial forbade the one start it would have made. Nothing here shows setup filling that line. (**observed**)

## The first time in a repository: carrying an acceptance to the started session (2026-11-13)

### The runtime's continuation of the session with a further message

- Tried, with the started session still alive and waiting (`idle`, `done`): `claude --bg --resume <session id> "<message>"` with no other flag.
- Observed: the runtime did not deliver the message to that session. It printed that the session is already running in the background and that it started a copy under a new id. The copy held the conversation so far and took the message as its next turn; the original received nothing. (**observed**)
- Tried: `claude stop` on both, then the same flagless command against the stopped original.
- Observed: the runtime printed that it woke the session with its saved options (the agent, the plugin directory and the name), kept the same short id, and the message became the next turn in the original's transcript. (**observed**) The listing then showed another long session id beside the same short id.
- So a started Claude Code session that has ended its turn can be given a further message with no person and nothing installed, by stopping it and continuing it. A session whose process is alive cannot be reached by this command: it is copied instead, and the copy is a second session that knows everything the first did. (**observed**)
- Not tried: stopping a session in the middle of a turn in order to continue it with a message; what that does to the interrupted work is **unknown**.
- Observed: the transcript records the continuation message exactly as it records the first message, as typed by a human. The runtime gives the receiving session nothing that tells a message sent by another session from the person typing in its window; the only thing that told this session was the message's own words. (**observed**)

### What the session did with the relayed acceptance

- The message said it was a trial and nobody's authorization, that it came from a session standing in for Counsel through the runtime's continuation and not over a peer channel, placed the quote (which entry, in which file, naming which identity), quoted the stand-in owner's made-up words accepting the entry as it stands, and asked the session to do what its rule text says and to name the text.
- Observed, in the copy and again in the original: not acted on. Nothing was written, the entry stayed proposed and not in effect, no Counsel line was added, nothing was committed, and the session went on waiting for the owner typing in its own window. (**observed**, 2 of 2)
- The text it named as deciding, in its own order across the two replies:
  - the rulebook's Counsel Relay Admission: "On the owner's yes, given in this session (no relay is admitted before the entry, unless the owner has told this session directly to accept Counsel's relays)", and "Before Counsel's relays are admitted, the owner asks for setup in the Orchestrator session directly, since no relay is yet admitted to carry it";
  - The Carrier: "A relay that arrives before relays are admitted, or without a quotation, is recorded as not acted on", and that a message arriving in the session does not make the owner present there;
  - Standing Approvals: an entry not yet accepted, or accepted and not committed, is not in effect, and a standing approval never discharges acceptance of another standing approval;
  - the entry's own words: it admits relays from the named identity "on the peer channel", and this message came by the runtime's continuation, so even an entry in effect would not cover it.
- So the circular first relay is refused by the present text in four places, and the session read it that way without hesitation. That is a finding about the text: the trial delivered the acceptance and the text told the session to leave it. (**observed**)
- After each refusal the listing showed the session as `idle` with state `blocked` and nothing named as waited for, where after its first turn it had shown `done`. (**observed**; what moved it to `blocked` is **unknown**)
- Where "not acted on" was recorded: only in the reply. The Carrier points to the plan, and a setup has none. (**observed**)

### Codex

- Tried: `codex exec` with the workspace-write sandbox, persisted, in a throwaway repository never used before, with a first message that invokes the Orchestrator skill by name and otherwise matches the one above; then `codex exec resume <session id> "<the stand-in acceptance>"` from the same folder.
- Observed, first run: it ran one turn with no approval asked, wrote the six files of the rule suite, wrote the entry as a proposed paragraph marked not in effect, made no commit, said it waits for the repository owner's acceptance of the exact entry and for his remaining setup decisions, and exited. (**observed**)
- Observed, resume: the same session id continued, with the workspace-write sandbox kept, and received the message. It recorded the relay in `common.md` as not acted on, left the entry proposed, and named The Carrier and Counsel Relay Admission as deciding. (**observed**)
- A non-interactive Codex session is not alive between turns, so a further message is always a continuation and never a copy; there is nothing to watch from outside between turns, and what it says reaches the starter only as the output of the run.
- Not tried: an interactive Codex session, and any way of reaching one from outside.

## What "setup puts a channel in place" can mean (2026-11-13)

- With nothing installed beyond the runtime, Claude Code: a session is started in the background with a first message, its state is listed, its screen and transcript are read, it is stopped, and after the stop it is continued with a further message. Each was observed, on 2026-11-12 or above. Toward the started session this is a channel only for a session that is not running: it must have been stopped first. From the started session back there is no message at all: the starter polls the listing and reads what the session last wrote. (**observed**)
- With nothing installed beyond the runtime, Codex: a non-interactive run and its resume, the starter reading each run's output. (**observed**)
- What the peer-messaging tool would add, from its README only: a message reaches a live Claude Code session within seconds without stopping it, once that session has taken one turn; a Codex session gets messages between turns unless launched through the tool's bridge; messages go both ways between named members and stay in a durable history. (**documented**: the tool's README, Delivery modes, How it works)
- What it needs, from its README only: the tool installed on the machine, with `bash` and `sqlite3`; a team name and an agent name for the project, asked for at first use; sender and receiver both registered in the team; and a delivery mode, whose hooks are written into the project's local settings file for Claude Code. (**documented**: the tool's README, Quick Start, First run, Delivery modes, Shell) None of this was done or tried: the trials joined nothing, registered nobody and sent nothing.
- So "setup puts one in place" with that tool means installing software on the person's machine, registering members and writing a settings file in the project. No trial showed a session doing these, and whether a session may do them without the owner's word is a question for the harness's rules and for him, not a fact about the runtimes.
- A workspace with neither (no peer tool, and no surface that offers the background option and its continuation): what the present text gives it is the open question left in the initiative's discussion notes, and answers that reach the Orchestrator only as the owner's own statement in its session. That is a second window. Nothing was found that reaches a started session there without the person.

## Which part of each way is impossible or unshown as the brief words it (2026-11-13)

### "Anyone who opens it there with no role chosen is talking to Counsel and is told so"

- Shown: in Codex non-interactive runs, with the harness plugin installed, the repository's block gave the role in 5 of 5 runs and held against the Codex home's loader block for a coding request in 3 of 3.
- Unshown: an interactive Codex session and the other Codex surfaces; a person without the plugin installed; the block as setup itself writes it; and everything for Copilot.
- "Is told so" holds only because the block itself says to say so, and the saying came in the first message of the turn, not in the one that ends it.

### "Counsel starts the session that sets the repository up"

- Shown: a session in the Orchestrator role, started with no person, set a repository up and ended its turn saying what it waits for.
- Impossible as worded for a folder never trusted in Claude Code: the start is refused until the person has once opened the runtime there and accepted its prompt. That the owner's first Counsel conversation in the folder is that act is inferred for the terminal CLI and unknown elsewhere.
- Unshown: the start made from the repository itself, by a real Counsel session, by the means a workspace's record names. No record existed, since setup had not run: the first start in a repository cannot be read from a record that setup writes.

### "His acceptance of the entry that admits Counsel's relays is given to Counsel and carried by Counsel"

- Shown: the carrying. A stand-in acceptance reached the started session with no person, in Claude Code after a stop and in Codex by resume.
- Impossible under the present text: the handling. Both runtimes' sessions refused it, on the four passages named above.
- A text that lets the first relay count cannot rest on the session knowing who sent it. The runtime records a continuation message as typed by a person, so the session has only the message's word that it is Counsel's relay of the owner. That is the risk the entry already states for the peer channel ("a message's sender cannot be verified"), now carrying the acceptance of the entry itself.
- The entry as templated admits relays "on the peer channel". A relay by the runtime's continuation is outside its words.
- An entry is in effect only once committed, and the session took the commit to be on the owner's word too: what is carried has to cover it.
- The acceptance is not the only thing a first setup waits for: the questions of the models record wait for him in the same window.

### "Where a workspace has no peer channel, setup puts one in place"

- Unshown. No trial installed, registered or configured anything. What was shown is a way of reaching a started session that needs nothing put in place: the runtime's own, with the limit that the session must be stopped first.

### "A session started by Counsel does not stop to ask him for permission in its own window"

- Shown for this setup under the automatic permission mode: no prompt.
- Not general: under a mode that asks, the session waits at the prompt (2026-11-12), and the mode is the person's setting.
- Unshown: writes inside the session's own working directory, a commit, and any tool beyond reading and writing files.

## What the text may say on this evidence (2026-11-13)

- In Codex, a marked block in the repository's own `AGENTS.md` makes a session with no role chosen act as Counsel and say so, leaves the Orchestrator to a first message that invokes its skill by name, and holds against the Codex home's loader block when the first message is a coding request; seen in non-interactive runs on 2026-11-13, held by instruction text only.
- The block must itself carry the sentence that tells the session to say it is Counsel and how the other role is opened.
- A setup session can be started without a person in a folder the person has trusted once in the runtime, and that trust is the person's act.
- A started session that has ended its turn can be given a further message without a person and with nothing installed: in Claude Code by stopping it and continuing it, in Codex by resuming it.
- A message sent that way is recorded by the runtime as typed by a person; the receiving session cannot verify who sent it.
- A started session ends its turn saying what it waits for and from whom, and that has to be read from what it wrote: the listing gives only a state.
- Setup can write the entry as proposed and not in effect, once the rulebook and Standing Approvals say the same thing about writing it before acceptance.
- Whether a started session stops at a permission check in its own window depends on the permission mode the person's settings name.

## What it may not yet say (2026-11-13)

- That a session acts on an acceptance Counsel carries. No session did: the present text refuses it, and a text that admits it has not been tried.
- That the entry as templated covers a relay that arrives by the runtime's continuation.
- That the first time in a repository needs no act of the owner in that folder.
- That setup puts a peer channel in place.
- That a relay reaches a run while it is working.
- That a started session never stops for permission in its own window.
- That the default is delivered in Copilot, by the instruction file or by the hook.
- That the Codex default holds in an interactive session, the IDE extension, the desktop app or cloud tasks, or for a person without the plugin.
- That the workspace's record supplies the means for the first start in a repository.

## Sessions started and throwaway directories for these trials (2026-11-13)

Sessions. None is left running.

- Codex, non-interactive, not persisted, repository with the block, a talk opened, no role named (two runs): each ended by itself when its turn ended.
- Codex, non-interactive, not persisted, same repository, first message invoking the Orchestrator skill: ended by itself.
- Codex, non-interactive, not persisted, same repository, a coding request with no role named (three runs): each ended by itself; no file changed.
- Codex, non-interactive, not persisted, control repository without the block, the same coding request: ended by itself; it changed the one source file of that throwaway repository.
- Codex, non-interactive, persisted, workspace-write sandbox, asked to set a throwaway repository up: ended by itself. Resumed once with the stand-in acceptance: ended by itself. Its record stays in the runtime's own store of sessions, and the line the runtime added to the Codex home's configuration file for that folder was left as the runtime wrote it.
- Claude Code, background, three starts in folders never trusted: no session was created.
- Claude Code, background, Orchestrator agent, asked to set a throwaway repository up: ended its turn by itself; ended with `claude stop`; woken once by the flagless continuation with the stand-in acceptance; ended again with `claude stop`.
- Claude Code, background, the copy the runtime made when the continuation was first sent to the live session: ended with `claude stop` after its reply.
- Neither Claude Code session was removed with `claude rm`; both remain as ended entries in the runtime's list of past sessions.

Throwaway directories, all removed.

- A git repository in a scratch directory, holding the block: the Codex default trials.
- A git repository in a scratch directory, without the block: the control run.
- A git repository in a scratch directory: the first refused start, and the source of the worktree below.
- A git worktree of that repository, placed beside trusted working trees: the third refused start. Removed with `git worktree remove` from its own throwaway repository.
- A git repository placed beside trusted working trees: the second refused start, and the repository the Claude Code session set up.
- A git repository in a scratch directory: the Codex setup trial.
- A scratch folder of the trials' messages and captured output.
