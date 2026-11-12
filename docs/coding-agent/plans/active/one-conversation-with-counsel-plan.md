# Plan: One conversation with Counsel

- status: draft
- generated: 2026-11-12
- last_updated: 2026-11-12 (revised after the plan review's findings and after the first plan-draft audit)
- work_type: mixed

## Goal
- Build what the governing brief `docs/coding-agent/briefs/active/one-conversation-with-counsel-brief.md` asks for: a session opened with no role chosen is Counsel; a ratified brief starts a run without the owner opening anything; runs go side by side; nothing depends on a seat surviving; what is ready for him reaches him as a line and waits; a stopped run is found without him.
- The brief is the requirement and is not restated here; where this plan and the brief differ, the brief governs and the difference is a plan defect.
- The whole brief is built as one unit and published as one pull request, because the brief has the default role and the start of a run on ratification ship together as one change, and the rest of its statements are what makes that start safe to rely on.

## Definition of Done
- Every gives-statement and constraint of the brief is stated by plugin text, by a runtime adapter file or by this repository's rule files, each once, at the place a session that needs it reads it; the closeout maps each statement to where it is held.
- In each supported runtime the way a session with no role chosen becomes Counsel, and the way into each role by choice, is one the runtime documents or that Task_1 showed working; where a runtime offers none, the closeout says so plainly and the matter goes to the owner through Counsel before text for that runtime is written.
- No line of the plugin's text makes a result depend on a seat having seen an earlier unit of work (brief, pass condition).
- Scenarios 1, 2, 3, 5 and 8 are shown where one can be made, and where one cannot the closeout says so plainly (brief, pass condition).
- The package validators pass (brief, pass condition).
- Decision records replacing ADR-D-0037 and ADR-D-0020 are proposed, with any other record the admission test admits; none is marked accepted and nothing is retired by this plan.
- The two standing rules the brief changes are changed only as far as it says, in `docs/coding-agent/rules/common.md`, and every standing-approval entry this plan writes is recorded as proposed and not in effect until the owner accepts it.
- The closeout lists, for the owner, every case where a runtime's own permission check still needs input in a session's window and what he has to do for each.
- The branch is reviewed `APPROVED` and value audits at plan draft and closeout are logged.

## Planner-added requirements
- A findings file from Task_1 recording, per runtime, what was tried and what happened. Needed because: the brief's statements on the default role and on starting a run rest on what each runtime really does, the documentation leaves several points open, and text written on an unverified mechanism would be a guess written as a finding.
- Counsel names itself and the way into the Orchestrator role in the first reply of every Counsel session, not only one that holds the role by default. Needed because: in at least one runtime the default and the chosen Counsel are the same agent file and cannot be told apart, and the brief's statement holds if every Counsel session says it.
- The record of what is known about the machine's obstacles lives in the repository's shared git directory. Needed because: the brief requires it to reach every new seat and session and never the remote, and runs side by side work in separate working trees.
- A census of the plugin text for lines that rely on a seat's memory, run at closeout. Needed because: it is the only way to show the brief's third agent-checkable pass condition.

## Scope / Non-goals
- Scope: plugin text under `plugins/coding-agent-orchestration-harness/`; the runtime adapter files, manifests and the Codex loader; the two READMEs; `docs/coding-agent/rules/common.md` and `orchestrator.md`; proposed decision records; the run's records.
- Non-goals: more than one Counsel session at a time; how money is handled in a goal run; holding back part of the machine's limit; measuring how long a new seat takes to find its way (all four: brief, Left out on purpose). Marking a record accepted, retiring ADR-D-0037 or ADR-D-0020, or repairing the references to them. Editing either philosophy or its companion. Changing anyone's permission settings on any machine: what the owner has allowed is his to set. The peer-messaging tool itself.

## Design
- Fixed by the brief and not compared: Counsel is the default; both roles stay choosable; the default and the start of a run ship together; one Counsel at a time; the acts that wait for him still wait.
- The choice is where the knowledge of how a session is started, watched and ended lives.
- Chosen: the plugin text states what must happen and names no tool; each workspace records, in its rule files beside its record of models and peers, the means it has to start a session in a role with a first message, to see whether a session is alive, and to end one. Counsel and the Orchestrator read that record. This repository's record names the means Task_1 showed working here.
- Alternative: the plugin text names the means itself, per runtime (a background-session command for one runtime, the peer-messaging tool's spawn for another).
- structure: the chosen design keeps one owner for each fact (the plugin for the obligation, the workspace for the means) and adds one entry to an existing record; the alternative couples the plugin to two tools' command surfaces and duplicates what those tools document.
- evolution: under the chosen design a tool that changes its commands changes one workspace's record; under the alternative it changes the plugin for everyone, including workspaces that do not have the tool. The chosen design adds one concept, the record of means; its deletion path is the entry.
- verification: both are shown the same way, by starting a session here; the chosen design can also be checked by reading that the plugin's policy on starting, watching and ending a session rests on no particular installed tool.
- operation: the same sessions run under either. The brief leaves how many runs go at once to the harness, unbounded by default; neither design says anything on what the work may cost in money, which the product philosophy governs and the brief leaves out.
- human: under the chosen design someone who installs the harness has a record of means before Counsel can start a run, which setup fills as it fills the record of models. Under the alternative a run starts without that entry only where the named tool is installed. Under neither is a start by the person's own hand written as a way the harness works: where no means to start a session without a person can be established, the brief's statement is not met there, and that goes to the owner through Counsel (A3).
- safety: under both, a started session works within what the owner has allowed and no safety check is defeated; the chosen design keeps the permission basis in the workspace's own record, where the owner accepts it by name.
- Why chosen wins: it holds the brief for every runtime and tool without the plugin taking on knowledge that goes stale at another project's pace. Its price is one more entry for setup to fill.
- A second choice, where the obstacles record lives. Chosen: one file in the repository's shared git directory, read by every working tree and never pushed. Alternative: an ignored path in the working tree, which is per tree, is lost with the tree, and needs an ignore entry in every repository. The chosen place serves runs side by side; its limit is a seat whose sandbox cannot read the git directory, for which the dispatch carries the relevant entries.

## Compatibility stance
- surface: how a session takes a role in each runtime (the Claude Code plugin's default agent, the managed Codex loader block and the Codex manifest's default prompt, the adapter descriptions), and the names of plugin reference files that other files point to.
- stance: break, for the default role: a session opened with no role chosen stops being role-less (or, in Codex with the loader, the Orchestrator for a coding task) and becomes Counsel. This is the change the brief ratifies; the consumers are the people who open sessions, and the first reply tells each of them how to open the other role. Preserve, for the published agent names (ADR-D-0048) and the loader block's markers, which the bootstrap script reads.

## Context (workspace)
- Governing brief: `docs/coding-agent/briefs/active/one-conversation-with-counsel-brief.md`. Its ratification reached this session on 2026-11-12 as Counsel's relay quoting the owner: "I ratify the "One conversation with Counsel" brief." Relays from Counsel's identity are admitted by the standing approval in `docs/coding-agent/rules/common.md`, Standing Approvals.
- Philosophies, by the pointer lines in `common.md`: `docs/product-philosophy.md` and `docs/engineering-philosophy.md`, each with its companion.
- Run record: `docs/coding-agent/plans/active/one-conversation-with-counsel-run.md`. Readings file: `docs/coding-agent/plans/active/one-conversation-with-counsel-readings.md`.
- Research waived for nothing: three Researchers read the present state on 2026-11-12 (how a session gets its role; Counsel's conduct and the means to start and watch a session; seats, dispatch continuity and what runs share). What they found that the plan builds on:
  - No role is the default in any runtime today. Claude Code documents a plugin-level default agent the package does not use. In Codex the only package-controlled lever is the managed loader block, which reaches only those who ran the bootstrap. Copilot documents no default-agent mechanism.
  - `skills/counsel/SKILL.md` gives the Counsel role on any load of the skill; `skills/orchestration-harness/SKILL.md` already denies the role to a load by description match.
  - Every start of a session is the owner's act today, and two passages (`references/value-level-operation.md`, The Carrier; `docs/coding-agent/rules/orchestrator.md`) have him grant the merge tool's permission inside the Orchestrator session.
  - Nothing covers a session that goes quiet; the only stall rule is the goal loop's.
  - `skills/subagent-strategy/references/persistent-peer-dispatch.md` is premised on agents that stay alive across dispatches; delta re-review and follow-up dispatch name no packet that carries what an earlier seat knew.
  - `skills/durable-docs-authoring/references/adr.md` already takes a record's number at merge; nothing says how the plugin version or the files every run edits are shared between runs.
- Another run is in progress on other branches (the decision-records cleanup, waiting on the owner). It has ADR-D-0037 in an area it has not started and left ADR-D-0020 to another initiative; this run replaces both, and takes no record number until its work lands.
- Design record consulted: ADR-D-0017, 0020, 0021, 0034, 0035, 0037, 0038, 0043, 0048, 0051, 0062, 0064, 0068. Deviations: ADR-D-0037 and ADR-D-0020, which the brief names as replaced.

## Open Questions (max 3)
- None for the owner at plan draft. What Task_1 may raise is named under Assumptions.

## Assumptions
- A1: Claude Code runs a plugin's named agent as the main session when the plugin's root `settings.json` sets it, on the surfaces people use. source: unverified: the documentation states the mechanism and not which surfaces honour it; needs evidence from Task_1. Tasks 2 and 3 use the mechanism where it is shown. Where it is shown to reach only some of the surfaces people use, the default is not written as delivered for the others: what a person there would experience either way goes to the owner through Counsel, as under A2.
- A2: Copilot offers a documented way for installed text to make the built-in agent hold a role when none is chosen, other than a skill's description matching. source: unverified: research found none; needs evidence from Task_1. If none exists, Copilot's default is not written and the matter goes to the owner through Counsel as two experiences (the brief says every runtime; the runtime may not allow it).
- A3: On this machine a session can be started in the Orchestrator role with a first message, without a person, by at least one means. source: unverified: the installed tools document two candidates; needs evidence from Task_1. If neither works, the start of a run on ratification is not written as achieved: the requirement is held and what he would experience either way goes to the owner through Counsel, as for A2.
- A5: A stopped session, and one that has something ready, can come to Counsel's attention without the owner saying anything, while Counsel stays free to answer him. source: unverified: nothing in the package or the installed tools' documentation settles it; needs evidence from Task_1. If it does not hold, the statements on a stopped run and on not being kept waiting are not written as achieved: they are held and go to the owner through Counsel as what he would experience either way.
- A4: Starting a session to observe what a runtime does is within what the brief asks. source: the brief's pass condition that scenarios are shown where one can be made, and its statement that seats are created and ended by the session that uses them. The rule file allows headless sessions only as two named kinds of measurement and does not name this one; Task_6 changes that rule as far as the brief says. The sessions are ended when observed and change no file.

## Where each statement is held

One task writes the sentence that holds each statement of the brief; a mirror is a pointer or a matching line another task's file needs, and it restates nothing. Each statement is named by its section and its opening words in the brief.

| Brief statement | Held by | Mirror |
| --- | --- | --- |
| One conversation: "A session opened with no role chosen is Counsel"; "Whoever opens a session can still choose either role" (with the sentence on a skill loaded by description match) | Task_2 | Task_3: the Counsel skill's own sentence on when a session is Counsel |
| One conversation: "A session that holds the default role says so in its first reply" (with the sentence that the role does not change) | Task_3 | Task_2: the two Counsel adapters |
| One conversation: "When he ratifies a brief, the run starts"; "Counsel starts an Orchestrator session for the brief"; "He is not kept waiting by Counsel's own work" | Task_3 | none |
| One conversation: "One Counsel session at a time per repository" | Task_3 | none |
| Runs side by side: "A brief ratified while other runs are in progress does not wait"; "Each run has its own Orchestrator session"; "How many runs go at once"; "The harness may hold part of a run back"; "Runs side by side do not need him to untangle them" | Task_4 | none |
| Runs side by side: "He can ratify a brief at any moment" (Counsel holds a brief and tells him) | Task_3 | none |
| Runs side by side: "A number that must be unique across runs" (with the sentence that each Orchestrator states what its run will touch) | Task_4 | none |
| Runs side by side: "He can ask Counsel at any moment where every brief stands" | Task_3 | Task_4: each report states where the run stands and what it waits for |
| Seats: "Seats are created and destroyed as the work needs"; "Nothing depends on a seat surviving" with its three sub-statements ("The first dispatch of a unit of work stands alone"; "A seat that takes over a unit of work part-way"; "What is known about the obstacles of the machine"); "What is known about a machine's obstacles is kept where it does not reach the remote"; "Two peer seats are never shared" | Task_5 | Task_4: the delta re-review packet in the two files it owns |
| Seats: "A session holds one identity on the peer channel" | Task_3 | none |
| What reaches him: "When something becomes ready for him he is told"; "A decision of his is given once" | Task_3 | none |
| What reaches him: "A session started by Counsel does not stop to ask him for permission"; "Where a runtime's own permission check can be satisfied only by input in that session's window" | Task_4 | Task_6: this repository's merge rule |
| What reaches him: "He does not have to notice that a run or a seat has stopped" | Task_3 | Task_4: the report line above |
| Limits: "What waits for him today still waits for him" | no task changes it; the review checks that none does | none |
| Limits: "This changes two decision records" | Task_7 | none |
| Limits: "It changes two standing rules of his" | Task_6 | none |
| Limits: "When the machine's limit for a period is reached" | Task_3 | none |

## Tasks

### Task_1: What each runtime really does
- type: research
- owns:
  - docs/coding-agent/plans/active/one-conversation-with-counsel-mechanisms.md
- depends_on: []
- description: |
  Establish by trial on this machine, and by each runtime's own documentation where a trial cannot be made, the facts the later tasks build on, and record them in the owned file with no machine path, user name or credential in it.
  For each of Claude Code, Codex and Copilot: what makes a session with no role chosen hold a named role; what lets the opener choose either role; whether a session's role can change while it lives.
  For this machine: by what means a session can be started in the Orchestrator role with a first message and without a person; how that session's liveness can be read from outside it; how it can be seen from outside whether it is working, waiting on something it has named, or stopped; what brings a stopped or reporting session to Counsel's attention without the owner saying anything, and whether Counsel can go on answering him meanwhile; how it is ended; what it does when it meets a permission check; and which permission checks can be settled for a repository beforehand by the owner's own settings.
  A setup step that may prompt (a fresh Codex home, for one) is probed once on its own, not found inside a batch.
  Also establish, per runtime, which of the people who install the harness the default would reach (every surface of the runtime, every way of installing), and what means to start a session exist in a repository where no setup has yet run.
  The owned file holds what the runtimes and tools do. An obstacle particular to this machine that the trials meet is told to the Orchestrator in the report and is not written in the file.
  Sessions started for this are measurement only: each is given a harmless first message, is ended when observed, and changes no file in any repository. No permission setting is created or changed, no mode that skips a runtime's safety checks is used, and nothing is sent to the peer channel's registered seats.
- acceptance:
  - The file states, per runtime and per question above, what was tried, what was observed, and whether the fact is observed, documented (with the page) or unknown.
  - Each of assumptions A1, A2, A3 and A5 is answered as held, not held or unknown, and for each runtime the file says whom the default would reach and whom it would not.
  - Every session started is listed with how it was ended.
- validation:
  - kind: review
    required: true
    owner: orchestrator
    detail: "Findings read against assumptions A1, A2, A3 and A5; privacy sweep of the file"
  - kind: review
    required: true
    owner: reviewer
    detail: "Each fact marked observed has its trial stated; nothing marked observed rests on documentation alone"

### Task_2: The default role and the way into each role
- type: impl
- owns:
  - plugins/coding-agent-orchestration-harness/settings.json
  - plugins/coding-agent-orchestration-harness/.claude-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.codex-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.github/plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/agents/Orchestrator.md
  - plugins/coding-agent-orchestration-harness/agents/Counsel.md
  - plugins/coding-agent-orchestration-harness/claude/agents/harness-orchestrator.md
  - plugins/coding-agent-orchestration-harness/claude/agents/harness-counsel.md
  - plugins/coding-agent-orchestration-harness/codex/**
  - plugins/coding-agent-orchestration-harness/skills/codex-harness-bootstrap/**
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/runtime-role-map.md
  - plugins/coding-agent-orchestration-harness/skills/runtime-adapter-contract/**
  - plugins/coding-agent-orchestration-harness/README.md
  - README.md
  - plugins/coding-agent-orchestration-harness/scripts/validate_harness_package.py
  - plugins/coding-agent-orchestration-harness/scripts/run_validation_smoke_tests.py
- depends_on: [Task_1]
- description: |
  Make a session opened with no role chosen Counsel in every supported runtime, by the mechanism Task_1 found for each, and keep a way into both roles by the opener's choice (brief, One conversation, first two statements).
  A skill loaded because its description matched gives no role. The role a session holds does not change while it lives; where a runtime lets its user switch agents in a session, the text says what that is and does not pretend the runtime forbids it.
  Where Task_1 found no mechanism for a runtime, or one that reaches only some of the people who install, write nothing for that runtime or for those people until the owner's answer is recorded in the Decision Log; the rest of the task goes ahead.
  An Orchestrator session may now be one Counsel started; text that says the owner opened it is brought in line.
  The validators check package integrity only: add a check only for a new file the package cannot work without.
- acceptance:
  - For each runtime, the files that make the default and the files that describe the two ways in agree with each other and with Task_1's findings.
  - No sentence in the owned files says a role is entered only by the opener's explicit act, or that a loader-routed session is the Orchestrator.
  - Adapter text that is the same role's text in two runtimes says the same thing in both.
  - The Codex loader block keeps its markers, and the bootstrap's verify mode still passes.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "py -I scripts/validate_harness_package.py and py -I scripts/run_validation_smoke_tests.py from the plugin root; git diff --check"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff against the brief's One conversation section and Task_1's findings"

### Task_3: Counsel's conduct
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/counsel/**
  - plugins/coding-agent-orchestration-harness/skills/value-documents/**
- depends_on: [Task_1]
- description: |
  Bring Counsel's own text to what the brief gives.
  A session is Counsel because it was opened so, by choice or by default, and never because the skill's description matched. Every Counsel session says in its first reply that it is Counsel and how to open the other role.
  When the owner ratifies a brief, Counsel starts the run without him opening anything, by the means the workspace records; the first message to a started session stands alone, names the brief's path, and claims no authority of the owner's (the ratification follows as a relay, as today).
  When a brief is handed over is Counsel's to settle: one that builds on a change another run has not finished is held, and he is told that it is held and what it waits for.
  He is not kept waiting by Counsel's own work: starting, watching and reading reports do not hold up his conversation.
  When something becomes ready for him he is told in a line what it is and what it holds up; it then waits. Counsel can tell him at any moment everything that waits on him, which item holds up the most work, and where every brief stands, without him looking at another session.
  A run that has stopped making progress is found without him, told apart from one working long or rightly waiting, and either recovers within a stated limit or reaches him as a clear report; it is never restarted over and over. State the limit.
  A decision of his is given once, to Counsel. A session holds one identity on the peer channel, given when it is created; reading another seat's messages never requires holding that seat's identity.
  When the machine's limit for a period is reached everything stops until it resets, his conversation with Counsel included; nothing is held back against that, and the text says so (brief, Limits, last statement).
  What still waits for him is unchanged (brief, Limits, first statement). Counsel still approves nothing and gives an Orchestrator no instruction of its own on how the work is done.
- acceptance:
  - Each statement the table under Where each statement is held gives this task is held by a sentence in the owned files, once.
  - No sentence in the owned files has a session take, move or change a seat's identity after it is created.
  - What the owned files say about starting, watching and ending a session rests on no particular installed tool; it points to the workspace's record of means.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "py -I scripts/validate_harness_package.py and py -I scripts/run_validation_smoke_tests.py from the plugin root; git diff --check"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff against the brief's statements this task holds; the text that tells a stopped run from one working long or rightly waiting, read against Task_1's findings on what can be observed"

### Task_4: The Orchestrator session that Counsel started
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/value-level-operation.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/completion-closeout.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/lifecycle-gates.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/final-response-contract.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/dispatch-guidance.md
  - plugins/coding-agent-orchestration-harness/skills/git-workflow/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/git-workflow/references/**
  - plugins/coding-agent-orchestration-harness/skills/durable-docs-authoring/**
- depends_on: [Task_1]
- description: |
  Bring the Orchestrator's text under a brief to what the brief gives.
  A session Counsel started does not stop to ask the owner for permission in its own window: it works within what he has already allowed for the repository, and anything outside that reaches him as a question through Counsel. Where a runtime's check can be satisfied only by input in the window, that is the backup: it carries his word and nothing else, such cases are kept as few as the runtime allows, and the closeout says which remain and what he has to do for each. No safety check is defeated. The passages that have him grant the merge tool's permission in the session are brought in line with this.
  On taking a brief the session tells Counsel what its run will touch. Each report to Counsel states where the run stands and, when it waits, what it waits for, so that a quiet run that is waiting can be told from one that has stopped.
  Runs go side by side: each keeps the other's work intact, validates the revision it delivers, and makes no other run's finished result wrong without saying so. A number that must be unique across runs is taken when the work lands. What every run edits (the rule files, the lessons file, the manifests' version) is settled without him by the run that lands later. Where two briefs ask for things that cannot both hold, that goes to him through Counsel before both results are called ready. The harness may hold part of a run back where running it now would collide with another run; that is its decision and no question to him.
  A re-review scoped to a delta gives its reviewer what the earlier review covered and found, so that a reviewer who saw nothing can judge it.
- acceptance:
  - Each statement the table under Where each statement is held gives this task is held by a sentence in the owned files, once.
  - No sentence in the owned files has the owner grant a permission in the Orchestrator session as the ordinary way.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "py -I scripts/validate_harness_package.py and py -I scripts/run_validation_smoke_tests.py from the plugin root; git diff --check"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff against the brief's statements named in the acceptance"

### Task_5: Seats that need not survive
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/subagent-strategy/**
  - plugins/coding-agent-orchestration-harness/skills/wave-integration/**
  - plugins/coding-agent-orchestration-harness/skills/workspace-troubleshooting/**
  - plugins/coding-agent-orchestration-harness/skills/rulebook/**
  - plugins/coding-agent-orchestration-harness/skills/improvement-loop/**
- depends_on: [Task_1]
- description: |
  Bring the text on seats and dispatch to what the brief gives under Seats.
  Seats are created and ended as the work needs, by the session that uses them; a session may keep one while it is useful and may end one at any time, and nothing depends on a seat surviving.
  The first dispatch of a unit of work stands alone. A seat that takes over a unit part-way is handed where it stands: what it is for, what is decided and on whose word, what is done and at which revision, what remains, what is still open, and what may already have been done outside the repository; it neither repeats an act already performed nor undoes a decision already made.
  What is known about the obstacles of the machine reaches every new seat and every new Orchestrator session when it starts. It is kept in one file in the repository's shared git directory, so that every working tree reads it and it never reaches the remote; each entry says where it applies and when it was last seen, and an entry is checked again and not trusted for ever. Where a seat cannot read that place, its dispatch carries the entries that apply.
  The workspace's record gains the means it has to start a session in a role with a first message, to see whether one is alive and whether it is working or waiting, and to end one; setup fills it as it fills the record of models. The policy rests on no particular installed tool.
  Remove or rewrite every line that relies on a seat's memory of earlier work, including the premise of the reference on long-lived peers; move its inbound pointers with it.
- acceptance:
  - Each statement the table under Where each statement is held gives this task is held by a sentence in the owned files, once.
  - A search of the owned files finds no line that makes a result depend on a seat having seen an earlier unit of work; the report lists each line changed for this reason.
  - No pointer in the plugin leads to a file this task renamed or removed.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "py -I scripts/validate_harness_package.py and py -I scripts/run_validation_smoke_tests.py from the plugin root; git diff --check; a search for pointers to any renamed file"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff against the brief's Seats section; the census of lines relying on a seat's memory"

### Task_6: This repository's rules
- type: docs
- owns:
  - docs/coding-agent/rules/common.md
  - docs/coding-agent/rules/orchestrator.md
  - docs/coding-agent/rules/_lifecycle.json
- depends_on: [Task_2, Task_3, Task_4, Task_5]
- description: |
  The Orchestrator's own task, since only the Orchestrator edits the rule files.
  Change the two standing rules only as far as the brief says: Counsel may start an Orchestrator session for a ratified brief, and a session may create and end the seats its work needs. Record the means this workspace has to start, watch and end a session, as Task_1 showed them.
  Bring the merge rule in line with Task_4. Write as proposed, and not in effect until the owner accepts each by name, any standing-approval entry the started sessions need.
- acceptance:
  - The rule against starting seats and the rule on a silent seat say what the brief allows and no more.
  - Each proposed standing-approval entry is marked as awaiting the owner's acceptance.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff against the brief's Limits section"

### Task_7: The decision records
- type: docs
- owns:
  - docs/coding-agent-orchestration-harness/decisions/**
- depends_on: [Task_2, Task_3, Task_4, Task_5]
- description: |
  For what this plan decides, propose a decision record wherever the admission test of `durable-docs-authoring/references/adr.md` passes, each holding one decision by the owner's test recorded in the cleanup brief, in the template's present form. Two of them replace ADR-D-0037 and ADR-D-0020.
  Name in the report every accepted record a clause of which no longer holds once these are accepted, with the clause quoted; change no accepted record.
  A record's number is a working number until the work lands.
- acceptance:
  - Each proposed record states one decision, its reasons and what would let it go, and names what it replaces.
  - No accepted record is edited, retired or moved.
  - File names stay within the length the smoke test allows on this platform.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "py -I scripts/validate_harness_package.py and py -I scripts/run_validation_smoke_tests.py from the plugin root; git diff --check"
  - kind: review
    required: true
    owner: reviewer
    detail: "Each record against the standard and the brief; the list of accepted records touched"

### Task_8: The scenarios shown
- type: test
- owns:
  - docs/coding-agent/plans/active/one-conversation-with-counsel-scenarios.md
- depends_on: [Task_6, Task_7]
- description: |
  Show scenarios 1, 2, 3, 5 and 8 of the brief where one can be made on this machine, with the plugin as this branch has it, and record in the owned file what was done and seen for each, or plainly that it could not be made and why. Run the census of the whole plugin text for lines relying on a seat's memory and record its result there. The run record is not this task's: it holds only what the audits state, copied by the Orchestrator.
  Sessions started for this are ended when observed; none changes a tracked file or reaches outside the machine.
- acceptance:
  - Each of the five scenarios has a line: shown (how to observe it) or not makeable (why).
  - The census result is recorded with the search used.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "The record of each scenario against the brief's wording of it"

## Task Waves (explicit parallel dispatch sets)

- Wave 1: [Task_1]
- Wave 2 (parallel): [Task_2, Task_3, Task_4, Task_5]
- Wave 3 (parallel): [Task_6, Task_7]
- Wave 4: [Task_8]

## Rollback / Safety
- Everything is on one branch and reverts as one. Nothing is merged, accepted or retired by this plan.
- No session started under this plan uses a mode that skips a runtime's safety checks, changes a permission setting, or acts outside the machine.

## Progress Log (append-only)

- 2026-11-12 The brief and Counsel's notes were committed by name at a295f45, the revision this plan starts from.
- 2026-11-12 12:41Z Plan review (Codex review seat) at 4f48cf7: CHANGES REQUESTED, OC-P1 to OC-P6. Revised at 87a9ff3. 12:44Z re-review: five closed, OC-R1 open (the table's numbering). Corrected at d6abf16. 12:46Z re-review: APPROVED, no open finding; the reviewer notes that A1, A2, A3 and A5 remain questions for Task_1.
- 2026-11-12 12:48Z The reading is written in the readings file before the plan-draft audit is dispatched.
- 2026-11-12T12:49Z Value audit dispatched (Claude subagent `harness-auditor` on Fable, a new dispatch), text verbatim:
  You are the value auditor. Read references/value-audit-mandate.md of the orchestration-harness skill and follow it exactly. Position: plan draft. Plan: <worktree>/docs/coding-agent/plans/active/one-conversation-with-counsel-plan.md. Governing brief: <worktree>/docs/coding-agent/briefs/active/one-conversation-with-counsel-brief.md. Changes since: none.
- 2026-11-12T12:56Z Verdict as returned (machine paths shortened; the two comparison lines are in the readings file):
  Value audit verdict, plan draft. One item is `ask-now`; every other item is `cited` or `inferred`; nothing is `ungraded`.
  The dispatch matched the fixed template. The mandate was read from the worktree copy, `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/value-audit-mandate.md`. No notes file was opened, and the readings file was opened once, after the grades were fixed.
  Position: plan draft
  Documents read: `docs/coding-agent/briefs/active/one-conversation-with-counsel-brief.md`; `docs/coding-agent/plans/active/one-conversation-with-counsel-plan.md`; `docs/product-philosophy.md` and `docs/product-philosophy-companion.md`; `docs/engineering-philosophy.md` and `docs/engineering-philosophy-companion.md`; `docs/coding-agent/rules/common.md` (pointer lines and Standing Approvals, same as HEAD). All are in the run's worktree. Read to understand only, never as support: `docs/coding-agent/rules/orchestrator.md`, the plugin `README.md`, and The Carrier in `references/value-level-operation.md`.
  Product basis: philosophy (the brief traces to the product philosophy; ebigunso is owner and product owner)
  Not audited: none
  Missing inputs: none
  Value documents changed in range: none (no range at plan draft)
  Items:
  - Goal: the whole brief built as one unit and published as one pull request | maps to the brief | cited | brief: "The default role and this ship together, as one change."; the outward-facing publish passes on `common.md` Standing Approvals: "A finished, reviewed run may publish its branch and open pull requests in this repository without asking first. Merges are not covered and wait for the owner." (the entry records "Given and accepted by the repository's owner, ebigunso, on 2026-09-30, relayed by Counsel: 'The common rule proposed, accepted.'" and is committed; a file cannot show that the words were said) | -
  - DoD 1: every gives-statement and constraint stated once, where the session that needs it reads it; the closeout maps each | maps to the brief | cited | brief: "This brief is the grounds for the work."; engineering philosophy §5: "Each thing is written once, in the place whose pace matches its reason, where the reader who needs it will be reading when the decision comes." | -
  - DoD 2: the default and the way into each role rest on what the runtime documents or Task_1 showed; a runtime with none goes to the owner before text is written | maps to the brief | cited | brief: "A session opened with no role chosen is Counsel, in every runtime the harness supports and for everyone who installs it."; brief: "every supported runtime offers a way into both"; engineering philosophy §2: "A guess is not written as a finding." | -
  - DoD 3: no line makes a result depend on a seat having seen earlier work | maps to the brief | cited | brief, Pass conditions: "no line of the plugin's text makes a result depend on a seat having seen an earlier unit of work" | -
  - DoD 4: scenarios 1, 2, 3, 5 and 8 shown where one can be made | maps to the brief | cited | brief, Pass conditions: "scenarios 1, 2, 3, 5 and 8 are shown where one can be made, and where one cannot the closeout says so plainly" | -
  - DoD 5: the package validators pass | maps to the brief | cited | brief, Pass conditions: "the package validators pass" | -
  - DoD 6: records replacing ADR-D-0037 and ADR-D-0020 proposed, none accepted, nothing retired | maps to the brief | cited | brief, Limits: "This changes two decision records, which are replaced by records he accepts by name"; "What waits for him today still waits for him: ... accepting a decision record by name" | -
  - DoD 7: the two standing rules changed only as far as the brief says; standing-approval entries written as proposed | maps to the brief | cited | brief, Limits: "It changes two standing rules of his, and only as far as this brief says: that Counsel starts and prompts no peer, and that no new seat is started for a dispatch."; "What waits for him today still waits for him: ... a standing approval" | -
  - DoD 8: the closeout lists every case still needing input in a session's window | maps to the brief | cited | brief: "the closeout says plainly which remain and what he has to do for each" | -
  - DoD 9: the branch reviewed APPROVED; value audits at plan draft and closeout logged | internal mechanics | cited | product philosophy §6: "Not its own judge. A builder's confidence in its own work is not evidence"; the engineering philosophy is silent on it | -
  - Planner-added: Task_1 findings file | internal mechanics | cited | engineering philosophy §2: "A guess is not written as a finding. A fact that may change carries the date it was seen." | -
  - Planner-added: every Counsel session, not only a default one, names itself and the way into the Orchestrator role in its first reply | maps to the brief | inferred | brief: "A session that holds the default role says so in its first reply, with how to open the other role." | -
  - Planner-added and Design, second choice: the obstacles record lives in the repository's shared git directory | internal mechanics | inferred | brief: "What is known about a machine's obstacles is kept where it does not reach the remote."; brief: "What is known about the obstacles of the machine the work runs on reaches every new seat and every new Orchestrator session when it starts"; engineering philosophy §5: "A workspace's dated record holds what is true today." | -
  - Planner-added: a census of the plugin text at closeout | maps to the brief | cited | brief, Pass conditions: "no line of the plugin's text makes a result depend on a seat having seen an earlier unit of work" (agent-checkable) | -
  - Non-goal: the four things the brief leaves out | maps to the brief | cited | brief, Left out on purpose: "More than one Counsel session at a time."; "How money is handled in a goal run."; "Holding back part of the machine's limit so that his conversation survives when runs reach it."; "How long a new seat takes to find its way in an area, and what that costs in money." | -
  - Non-goal: marking a record accepted, retiring ADR-D-0037 or ADR-D-0020, repairing references to them | maps to the brief | cited | brief, Limits: "replaced by records he accepts by name" | -
  - Non-goal: editing either philosophy or its companion | maps to the brief | cited | brief, Limits: "What waits for him today still waits for him: ... a change to a philosophy" | -
  - Non-goal: changing anyone's permission settings | maps to the brief | cited | brief: "It works within what he has already allowed for the repository"; "No check a runtime makes for safety is defeated to avoid it." | -
  - Non-goal: the peer-messaging tool itself | internal mechanics | cited | engineering philosophy §7: "the burden of proof is on what is added or kept, and absence needs no defence" | -
  - Design, first choice: the plugin states what must happen and names no tool; each workspace records its means to start, watch and end a session; setup fills the record | internal mechanics | cited | engineering philosophy §5: "The harness's text holds how decisions are carried out. A workspace's dated record holds what is true today."; §4: "What changes faster than the place it would be written." The plan does not say how that record gets filled in a repository where no Orchestrator session has yet run; if the person has to open one, the brief's "such a person does not choose a role, open a second session, start a seat or repair one" is touched. That is for the closeout to look at; it is not held here. | -
  - Compatibility stance: break for the default role; preserve the published agent names and the loader markers | maps to the brief | cited | brief: "A session opened with no role chosen is Counsel, in every runtime the harness supports and for everyone who installs it." | -
  - A1: Claude Code runs the plugin's named agent as the main session; unverified, Task_1 tests it | internal mechanics | cited | engineering philosophy §2: "A guess is not written as a finding." Its fallback, "say plainly where it is not", is graded in the partial-reach item below. | -
  - A2: Copilot offers a documented default; if none, not written and it goes to the owner | maps to the brief | cited | brief: "in every runtime the harness supports"; product philosophy §2: "If a question would prevent the wrong thing, it is asked, whatever it interrupts." | -
  - A3: a session can be started in the Orchestrator role without a person; if not, the requirement is held and goes to the owner | maps to the brief | cited | brief: "When he ratifies a brief, the run starts without him opening anything."; product philosophy §2, as for A2 | -
  - A5: a stopped or ready session reaches Counsel without the owner speaking; if not, held and goes to the owner | maps to the brief | cited | brief: "He does not have to notice that a run or a seat has stopped."; "He is not kept waiting by Counsel's own work"; product philosophy §2, as for A2 | -
  - A4: starting a session to observe a runtime is measurement the rule file already allows | internal mechanics | inferred | brief, Pass conditions: "scenarios 1, 2, 3, 5 and 8 are shown where one can be made"; brief: "Seats are created and destroyed as the work needs, by the session that uses them."; product philosophy §2: "What the harness can find out, it finds out." The rule's own words do not cover it: `common.md` allows "Ephemeral headless `codex exec` and `claude -p` sessions ... only as measurement instruments: ablation probes and the Auditor comparison's replays", so the plan's "already allows" is wider than the rule. The support is the brief; it is cheap to undo (sessions ended, no file changed). | -
  - Task_1: what each runtime really does | internal mechanics | cited | product philosophy §2: "What the harness can find out, it finds out. It asks only what only the person can answer."; engineering philosophy §2: "A guess is not written as a finding." The owned file is tracked and records facts "for this machine". The brief's constraint "What is known about a machine's obstacles is kept where it does not reach the remote" is wider than the task's "no machine path, user name or credential"; the closeout diff will show which it was. | -
  - Task_2: the default role and the way into each role | maps to the brief | cited | brief: "A session opened with no role chosen is Counsel, in every runtime the harness supports and for everyone who installs it."; "Whoever opens a session can still choose either role by what the runtime offers ... A skill loaded because its description matched never gives a session a role."; "The role a session holds does not change while it lives."; engineering philosophy §2: "A limit is written as a limit and not dressed as the behaviour that was wanted." | -
  - Partial reach of the default (Notes, Edge cases: "a person who installed the plugin for Codex without the loader gets no default role from the package; the README says so"; A1's fallback "say plainly where it is not") | maps to the brief | ask-now | brief: "A session opened with no role chosen is Counsel, in every runtime the harness supports and for everyone who installs it." (gives, told: "ship it for everyone") | No support. A binding gives-statement is left unmet for some of the people who install, and the plan settles that itself with a README line; for a runtime with no default at all (A2) the same plan takes it to the owner. Value question: where a runtime can give the default role only to some of the people who install the harness (in Codex, only those whose setup added the loader; in Claude Code, perhaps only some of its apps), is it acceptable that the others open a session that holds no role and learn why from the README, or must the default hold for them too before this is called delivered?
  - Task_3: Counsel's conduct | maps to the brief | cited | brief: "When he ratifies a brief, the run starts without him opening anything."; "When it is handed over is Counsel's to settle, and he is not asked"; "He is not kept waiting by Counsel's own work"; "When something becomes ready for him he is told that it is there: what it is and what it holds up, briefly"; "either recovers within a stated limit or reaches him through Counsel as a clear report. It is never restarted over and over."; "A decision of his is given once."; "A session holds one identity on the peer channel"; "When the machine's limit for a period is reached, everything stops until it resets, his conversation with Counsel included."; "One Counsel session at a time per repository." | -
  - Task_4: the Orchestrator session that Counsel started | maps to the brief | cited | brief: "A session started by Counsel does not stop to ask him for permission in its own window. It works within what he has already allowed for the repository, and anything outside that reaches him as a question through Counsel."; "that input is the backup and not the default"; scenario 7: "He accepts a pull request by name in his conversation with Counsel. It merges, and he is asked nowhere else."; "What two runs share (numbers, the files every run edits, the stack of pull requests) is settled without him."; "The harness may hold part of a run back where running it now would collide with another run"; "Each Orchestrator states when it takes a brief what its run will touch." The merge-permission passages change on these statements. That is a third rule's wording beside the two the brief's Limits names; the gives-statement and scenario 7 answer it, so it is not held. | -
  - Task_5: seats that need not survive | maps to the brief | cited | brief: "Nothing depends on a seat surviving. How long a seat lives is not fixed: a session may keep one while it is useful and may end one at any time."; "The first dispatch of a unit of work stands alone"; "A seat that takes over a unit of work part-way is handed where that unit stands"; "Each such thing says where it applies and when it was last seen, so that it is checked again and not trusted for ever."; "Two peer seats are never shared between two Orchestrators in the middle of a run." | -
  - Task_6: this repository's rules | maps to the brief | cited | brief, Limits: "It changes two standing rules of his, and only as far as this brief says: that Counsel starts and prompts no peer, and that no new seat is started for a dispatch."; "What waits for him today still waits for him: ... a standing approval"; for the silent-seat rule: "He does not have to notice that a run or a seat has stopped." | -
  - Task_7: the decision records | maps to the brief | cited | brief, Limits: "This changes two decision records, which are replaced by records he accepts by name"; brief means: "A number that must be unique across runs is taken when the work lands, not while it is drafted."; engineering philosophy §5: "A decision record holds one decision at the level of intent" | -
  - Task_8: the scenarios shown and the census | maps to the brief | cited | brief, Pass conditions: "scenarios 1, 2, 3, 5 and 8 are shown where one can be made, and where one cannot the closeout says so plainly; no line of the plugin's text makes a result depend on a seat having seen an earlier unit of work" | -
  - Decision Log 12:45Z: draft revised on review findings OC-P1 to OC-P6 | maps to the brief | cited | brief: "When he ratifies a brief, the run starts without him opening anything." (P1); "He does not have to notice that a run or a seat has stopped." (P5); "it is not a bound on what the work may cost" (P6); engineering philosophy §5: "Each thing is written once" (P2 to P4) | -
  - Decision Log 12:47Z: the table names each statement by its section and opening words | internal mechanics | cited | brief: "It is passed verbatim; do not paraphrase it into a plan as if the paraphrase were the requirement." | -
  Human-only conditions pending: "the next two briefs he hands over close together both start without him opening a session; over those two runs he opens no Orchestrator session, starts or repairs no seat, and is not the one who notices a stop."
  Scenarios: none
- Acting on the verdict: one item is held (ask-now): the plan settled by itself, with a README line, that a default role reaching only some of the people who install is acceptable. The line is the Orchestrator's own and has no support, so it is redone and not sent to the owner as it stands: where Task_1 finds a runtime can give the default to only some who install, nothing is written as delivered for them and what they would experience either way goes to him through Counsel, as for a runtime with no default at all. Also taken from the verdict: A4 no longer says the rule file already allows the trial sessions; Task_1's tracked file holds what the runtimes do and no obstacle of this machine; how the record of means is filled where no Orchestrator session has yet run is named as a question for Task_1. The plan is revised, reviewed again and audited again at plan draft, new. Nothing is built meanwhile.
- 2026-11-12 13:00Z Re-review of the revised plan (Codex review seat) at 59bd4e5: APPROVED, no open finding. The reviewer reads Task_2's hold as partial progress and not completion: its acceptance bullets stay mandatory, and an answer of the owner's that changes the experience follows the ordinary gates. The reading for the revised plan is in the readings file. 13:02Z second plan-draft audit dispatched, new.

## Decision Log (append-only; re-plans and major discoveries)

- 2026-11-12 12:45Z Decision: the draft is revised on the plan review's six findings, before any audit.
  - Trigger: review CHANGES REQUESTED at 4f48cf7 (OC-P1 to OC-P6).
  - Plan delta: a start by the owner's own hand is no longer written as a backup, and a missing means goes to him through Counsel (P1); the scenario trials get a file of their own and the run record stays the audits' (P2); the ban on naming tools is narrowed to the policy on starting, watching and ending a session (P3); a table gives each statement of the brief one task, and the machine's limit is assigned (P4); Task_1 also establishes how a stopped session comes to Counsel's attention, as assumption A5 (P5); the Design no longer reads the brief's unbounded number of runs as a word on cost (P6).
  - User approval: not applicable; under the ratified brief no plan is presented.
  - Record proposed: none.

- 2026-11-12 12:47Z Decision: the table of statements is corrected on the re-review's finding OC-R1.
  - Trigger: re-review CHANGES REQUESTED at 87a9ff3: the table's numbering did not match the brief's statements.
  - Plan delta: each statement is named by its section and opening words; the assignments are as the descriptions had them. Task_1's validation names the four assumptions.
  - User approval: not applicable.
  - Record proposed: none.

- 2026-11-12 12:58Z Decision: the plan is revised on the first plan-draft audit, which held one item.
  - Trigger: the audit's ask-now on the partial reach of the default role (a README line settling that some who install get no default).
  - Plan delta: the line is dropped; who the default reaches is established by Task_1, and where it does not reach everyone the default is not written as delivered and the question goes to the owner through Counsel (A1, Task_1, Task_2, Notes). A4 is reworded so that it claims no allowance the rule file does not give. Task_1's file holds no obstacle of this machine. How the record of means is filled before any Orchestrator session has run is named as a question.
  - Tradeoffs considered: sending the audit's value question to the owner now, before Task_1. Not done: the line was the Orchestrator's own, and after Task_1 the question, if it remains, can say which people in which runtime.
  - User approval: not applicable.
  - Record proposed: none.

## Notes
- Risks: a runtime may offer no way to make a default role (A2), no way to start a session without a person on this machine (A3), or no way to bring a stopped session to Counsel's attention (A5); each is answered by Task_1 before any text is written on them. The four writing tasks share one working tree, so a validator run by one sees the others' edits.
- Edge cases: the default role may reach only some of the people who install (in Codex, the package's only lever is the loader block, which a person's setup may not have added). The plan does not settle that with a line of documentation: Task_1 establishes who is reached in each runtime, and where some are not, the default is not called delivered for them and the question goes to the owner through Counsel before text for that runtime is written.
- A question for Task_1 and the tasks after it: how a workspace's record of means gets filled where no Orchestrator session has yet run, without the person opening one. If it cannot be done without him, that too goes to him through Counsel.
