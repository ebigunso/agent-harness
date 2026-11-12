# Plan: One conversation with Counsel

- status: draft
- generated: 2026-11-12
- last_updated: 2026-11-12 (revised after the plan review's findings OC-P1 to OC-P6)
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
- A1: Claude Code runs a plugin's named agent as the main session when the plugin's root `settings.json` sets it, on the surfaces people use. source: unverified: the documentation states the mechanism and not which surfaces honour it; needs evidence from Task_1. Tasks 2 and 3 use the mechanism where it is shown and say plainly where it is not.
- A2: Copilot offers a documented way for installed text to make the built-in agent hold a role when none is chosen, other than a skill's description matching. source: unverified: research found none; needs evidence from Task_1. If none exists, Copilot's default is not written and the matter goes to the owner through Counsel as two experiences (the brief says every runtime; the runtime may not allow it).
- A3: On this machine a session can be started in the Orchestrator role with a first message, without a person, by at least one means. source: unverified: the installed tools document two candidates; needs evidence from Task_1. If neither works, the start of a run on ratification is not written as achieved: the requirement is held and what he would experience either way goes to the owner through Counsel, as for A2.
- A5: A stopped session, and one that has something ready, can come to Counsel's attention without the owner saying anything, while Counsel stays free to answer him. source: unverified: nothing in the package or the installed tools' documentation settles it; needs evidence from Task_1. If it does not hold, the statements on a stopped run and on not being kept waiting are not written as achieved: they are held and go to the owner through Counsel as what he would experience either way.
- A4: Starting a session to observe what a runtime does is measurement, which `common.md` already allows for headless sessions. source: `docs/coding-agent/rules/common.md`, Models And Peers In This Workspace.

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
  Sessions started for this are measurement only: each is given a harmless first message, is ended when observed, and changes no file in any repository. No permission setting is created or changed, no mode that skips a runtime's safety checks is used, and nothing is sent to the peer channel's registered seats.
- acceptance:
  - The file states, per runtime and per question above, what was tried, what was observed, and whether the fact is observed, documented (with the page) or unknown.
  - Each of assumptions A1, A2, A3 and A5 is answered as held, not held or unknown.
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
  Where Task_1 found no mechanism for a runtime, write nothing that pretends to one: say in the README what that runtime does and stop there for that runtime.
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

## Notes
- Risks: a runtime may offer no way to make a default role (A2), no way to start a session without a person on this machine (A3), or no way to bring a stopped session to Counsel's attention (A5); each is answered by Task_1 before any text is written on them. The four writing tasks share one working tree, so a validator run by one sees the others' edits.
- Edge cases: a person who installed the plugin for Codex without the loader gets no default role from the package; the README says so.
