# Plan: One conversation with Counsel, his reading of the nineteen

- status: draft
- generated: 2026-11-19
- last_updated: 2026-11-19
- work_type: docs

## Goal
- Build what the governing brief `docs/coding-agent/briefs/active/one-conversation-with-counsel-brief.md` now says after the owner's reading of the nineteen proposed records: its group of entries under Directed during the run dated 2026-11-19, and the statements those entries corrected in place (Sessions and roles, Runs side by side, Dispatch, What reaches him, Limits, core scenarios 4 and 5, Pass conditions).
- The brief is the requirement and is not restated here; where this plan and the brief differ, the brief governs and the difference is a plan defect.
- This is a later unit of the same run and lands in the same pull request (109). The plan that built the brief as first ratified is closed under `completed/`.

## Definition of Done
- The plugin's text states, each once and at the place a session that needs it reads it: what reaches the owner and when (record 18's entry); that one Orchestrator session carries several briefs by default and when another is started (record 15's entry); what Counsel may say to an Orchestrator session and the guard on what is asked of it (record 8's entry); the dispatcher's freedom of relay and that it looks after whatever it sent the work to (the Dispatch section); a view from any other model (record 16's entry).
- The proposed records numbered 4 and 14 on the list fixed at commit 5e3528a are gone from the branch, with nothing in their place; the one line of record 4 stays in the plugin's text where a peer channel is handled, with its reason.
- The proposed records numbered 8, 15, 16 and 18 state the decisions their entries give. Every remaining proposed record has a problem statement that says what was wanted and why and what failed to serve it, with no account of what was observed or happened that does not bear on the decision; no remaining record rests on the account that a brief waited for the run in progress.
- `docs/coding-agent/rules/common.md` carries the third standing rule as changed: the dispatcher may use any relay the environment offers.
- The package validators pass. Nothing is marked accepted, nothing is retired, no number is taken.
- The branch is reviewed `APPROVED`, value audits at plan draft and closeout are logged, and a new numbered list of the remaining proposed records is fixed at the closing commit.

## Planner-added requirements
- None

## Scope / Non-goals
- Scope: plugin text under `plugins/coding-agent-orchestration-harness/` on Counsel's conduct, on the Orchestrator under a brief, and on dispatch; the runtime adapter files that restate any of it; the nineteen proposed records; `docs/coding-agent/rules/common.md`; the run's records.
- Non-goals: the sentence for the record standard (`durable-docs-authoring/references/adr.md`), which the run "Decision records at intent altitude" owns and builds on its own branch. Marking a record accepted, numbering one, retiring an accepted record or repairing references to one. Editing either philosophy or its companion. Trying any scenario in practice: none can be made by this unit's work that the earlier unit did not already try, and the closeout says so. The peer-messaging tool itself. Any permission setting.

## Design
- Fixed by the brief and not compared: every decision the entries of 2026-11-19 state.
- The choice left is how Counsel learns whether an Orchestrator session at work can take a further brief.
- Chosen: Counsel hands the brief to the Orchestrator session at work, and that session answers that it takes it or that it cannot take more; on the second answer, or where none is at work, Counsel starts one by the means the workspace records. Alternative: Counsel judges from outside, by what it knows of the session's load, and starts another without asking.
- structure: the chosen design keeps the call with the one session that knows its own state; the alternative gives Counsel a second, staler copy of that state.
- evolution: the chosen design adds no concept, since a hand-over and its answer already exist; the alternative adds a measure of load that some text would have to define.
- verification: the chosen design is shown by one hand-over and its answer; the alternative has nothing to observe but Counsel's guess.
- operation: the chosen design costs one message for each brief; a session that does not answer is already covered by the text on a stopped run.
- human: under both the owner is asked nothing; under the chosen design the line he gets says which session carries the brief.
- safety: neither changes what a session may do.
- Why chosen wins: the brief makes the call the harness's, and the session at work is the only part of the harness that can make it from knowledge and not from a guess.
- The work is one unit and not seven small changes, because the change to record 15 touches the problem statements of several records and the entry on record 8 is held by text on both Counsel's and the Orchestrator's side.

## Compatibility stance
- surface: the plugin reference `subagent-strategy/references/seats.md` and the pointers to it; the names of the proposed records.
- stance: break. The consumers are the plugin's own files, which this plan changes together, and the pull request's reader, who gets a new list. No released version carries the text changed here: plugin 2.0.0 is this unmerged branch.

## Context (workspace)
- Governing brief: `docs/coding-agent/briefs/active/one-conversation-with-counsel-brief.md`, ratified 2026-11-12; its entries of 2026-11-19 reached this session as Counsel's relay of 2026-11-19 08:34Z quoting the owner, admitted by the standing approval in `docs/coding-agent/rules/common.md`.
- Philosophies, by the pointer lines in `common.md`: `docs/product-philosophy.md` and `docs/engineering-philosophy.md`, each with its companion.
- Run record: `docs/coding-agent/plans/active/one-conversation-with-counsel-run.md`. Readings file: `docs/coding-agent/plans/active/one-conversation-with-counsel-readings.md`.
- Start revision of this unit: fe43aae (the brief and Counsel's notes as changed 2026-11-19).
- Research waived: the Orchestrator read the brief's change in full and located the affected text itself (`counsel/SKILL.md` and its references, the two Counsel adapter files, `orchestration-harness/references/value-level-operation.md`, `subagent-strategy/references/seats.md` and the four files that point to it, `runtime-adapter-contract/references/tool-capability-matrix.md`, lines of `common.md`); a Worker's own search of its owned files completes it.
- The list of the nineteen fixed at commit 5e3528a is in the pull request's text and in the changes file; numbers in this plan are that list's.
- Design record consulted: ADR-D-0021 (the dispatching session owns the life of what it dispatched to), which the brief names as already deciding what record 14 said.

## Open Questions (max 3)
- None for the owner at plan draft.

## Assumptions
- A1: One Orchestrator session carrying two briefs side by side has been done (this session, this run and the run on decision records, since 2026-11-12). source: the brief's entry on record 15 states it as Counsel's grounds, and the two run records show it.
- A2: The line of record 4 kept in the plugin's text belongs in what remains of the reference on seats. source: the brief's entry on record 4 ("where a peer channel is handled") and on record 14 ("what a dispatcher must know when the relay happens to be a peer channel").

## Tasks

### Task_1: Counsel's conduct
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/counsel/**
  - plugins/coding-agent-orchestration-harness/agents/Counsel.md
  - plugins/coding-agent-orchestration-harness/claude/agents/harness-counsel.md
  - plugins/coding-agent-orchestration-harness/codex/**
  - plugins/coding-agent-orchestration-harness/skills/runtime-adapter-contract/**
  - plugins/coding-agent-orchestration-harness/skills/value-documents/**
- depends_on: []
- description: |
  Bring the text on Counsel's conduct to the brief as changed 2026-11-19, on four matters:
  what reaches the owner and when (the statement under What reaches him and the entry on record 18);
  handing a ratified brief to an Orchestrator session at work and starting one only where none is at work or it answers that it cannot take more (Sessions and roles, Runs side by side, the entry on record 15, and this plan's Design);
  what Counsel may say to an Orchestrator session, and the guard (the entry on record 8);
  a view from any other model the environment offers (the entry on record 16).
  Each sentence of those entries is held once; text that states the earlier decision is rewritten, not added to. Adapter files restate only what they already restate.
- acceptance:
  - Each sentence of the brief's statement under What reaches him and of its entries on records 8, 15, 16 and 18 that binds Counsel is held by a sentence in the owned files, once; the report maps each to its place.
  - No line in the owned files still states: that each brief gets its own Orchestrator session; that Counsel speaks to an Orchestrator only in the owner's words with no reading of its own; that the consulted model is of another family or serves the engineering discussion only; that each ready thing reaches him as a line when it is ready.
  - Nothing names a model family, a tool or a count of roles where the brief names none.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "py -I scripts/validate_harness_package.py and py -I scripts/run_validation_smoke_tests.py from the plugin root; git diff --check"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff against the brief's entries of 2026-11-19 on records 8, 15, 16, 18"

### Task_2: The Orchestrator under a brief, and dispatch
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/**
  - plugins/coding-agent-orchestration-harness/skills/subagent-strategy/**
  - plugins/coding-agent-orchestration-harness/agents/Orchestrator.md
  - plugins/coding-agent-orchestration-harness/claude/agents/harness-orchestrator.md
  - plugins/coding-agent-orchestration-harness/skills/workspace-troubleshooting/**
  - plugins/coding-agent-orchestration-harness/skills/rulebook/**
- depends_on: []
- description: |
  Bring the Orchestrator's side and the text on dispatch to the brief as changed 2026-11-19:
  one Orchestrator session carries several briefs, and answers a further hand-over by taking it or saying it cannot take more (the entry on record 15, this plan's Design);
  a question goes to Counsel only when its options differ in what the owner would experience, and otherwise the call is the Orchestrator's own; a reading Counsel marks as its own carries none of his authority, is weighed as the Orchestrator weighs its own inferences, and is told to him at closeout (the entry on record 8);
  the brief's section Dispatch in place of what the text says on seats: the dispatcher is free to use any relay the environment offers and looks after whatever it sent the work to; a relay that lets the sub-agent message the dispatcher mid-work is preferred, not required. What is known of the machine's obstacles still reaches whatever starts work.
  The reference on seats shrinks to what a dispatcher must know when the relay happens to be a peer channel, and keeps the one line of record 4 with its reason (a session holds one identity on a peer channel and reads another's messages without taking its identity). The value-audit mandate and the goal-assessor mandate are changed only where a line of theirs states something the brief withdrew.
- acceptance:
  - Each sentence of the brief's section Dispatch and of its entries on records 8, 14 and 15 that binds the Orchestrator or a dispatcher is held by a sentence in the owned files, once; the report maps each to its place.
  - No line in the owned files still states: that each run has its own Orchestrator session; that nothing depends on a seat surviving, with its conditions on a first dispatch and a take-over, as a rule of its own; that two Orchestrators never share a peer seat; that dispatch is limited to particular kinds of relay.
  - No pointer in the plugin leads to a heading or file this task removed or renamed.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "py -I scripts/validate_harness_package.py and py -I scripts/run_validation_smoke_tests.py from the plugin root; git diff --check; a search of the whole plugin for pointers to any heading or file removed"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff against the brief's section Dispatch and its entries on records 8, 14, 15"

### Task_3: The proposed records
- type: docs
- owns:
  - docs/coding-agent-orchestration-harness/decisions/**
- depends_on: []
- description: |
  Only the nineteen proposed records of this run (files named ADR-D-<subject>.md, listed in the changes file at commit 5e3528a) are touched; no numbered record is.
  Delete records 4 and 14. Restate records 8, 15, 16 and 18 as their entries of 2026-11-19 give them, renaming a file where its subject no longer says its decision. Read every remaining record against the entry on record 17: its problem statement says what was wanted and why and what failed to serve it, and holds nothing that does not bear on the decision; record 17 and record 1 are named by the owner. Remove from every record the account that a brief waited for the run in progress, and every citation of a deleted record.
  The record standard as it stands on this branch, and its admission test, govern; a restated record that no longer passes the admission test is reported, not kept.
- acceptance:
  - Seventeen proposed records remain, or fewer with each further withdrawal reported with the admission-test reason; none is marked accepted or numbered.
  - Records 8, 15, 16 and 18 state every sentence of their entries that is a decision, a boundary or a reopen condition, and nothing the entry withdrew.
  - The report lists, for each remaining record, whether its problem statement changed and why.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "py -I scripts/validate_harness_package.py from the plugin root; git diff --check; a search of the repository for the file names of deleted or renamed records"
  - kind: review
    required: true
    owner: reviewer
    detail: "Each changed record against its entry and against the record standard"

### Task_4: This repository's rule on dispatch
- type: docs
- owns:
  - docs/coding-agent/rules/common.md
- depends_on: [Task_2]
- description: |
  The Orchestrator's own task (only it edits rule files). In Models And Peers In This Workspace, change the rule that dispatch goes only to the registered peer seats or Claude subagents and that a command-line call to another runtime is allowed only as a measurement instrument: the dispatcher may use any relay the environment offers and looks after what it sent the work to; Counsel hands a ratified brief to the Orchestrator session at work. The registered seats stay recorded as options. Pointers follow Task_2's result. `last_updated` is set.
- acceptance:
  - The rule reads as the brief's Limits names it changed, with the date and the brief as its source.
  - Nothing in the file still limits dispatch to particular kinds of relay; no session is licensed to use a mode that skips a runtime's safety checks.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "The changed lines against the brief's Limits and Dispatch"

### Task_5: Final review
- type: review
- owns: []
- depends_on: [Task_1, Task_2, Task_3, Task_4]
- description: |
  The Codex review seat reads the whole range from the start revision: each task's diff against the brief's entries, the plugin's text and the records saying the same thing, pointers, validators.
- acceptance:
  - `APPROVED` with no finding open.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Range fe43aae..HEAD"

## Task Waves (explicit parallel dispatch sets)

- Wave 1 (parallel): [Task_1, Task_2, Task_3]
- Wave 2: [Task_4]
- Wave 3: [Task_5]

## Rollback / Safety
- Everything is on one branch and reverts as one. Nothing is merged, accepted, numbered or retired by this plan, and nothing outside the repository is written.

## Progress Log (append-only)

## Decision Log (append-only; re-plans and major discoveries)

## Notes
