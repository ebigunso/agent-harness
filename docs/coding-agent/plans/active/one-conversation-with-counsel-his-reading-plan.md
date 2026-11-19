# Plan: One conversation with Counsel, his reading of the nineteen

- status: in progress (authorized by the ratified brief 2026-11-19: plan review closed with no finding open; second plan-draft audit holds nothing)
- generated: 2026-11-19
- last_updated: 2026-11-19
- work_type: docs

## Goal
- Build what the governing brief `docs/coding-agent/briefs/active/one-conversation-with-counsel-brief.md` now says after the owner's reading of the nineteen proposed records: its group of entries under Directed during the run dated 2026-11-19, and the statements those entries corrected in place (One conversation, Runs side by side, Dispatch, What reaches him, Limits, core scenarios 4 and 5, Pass conditions).
- The brief is the requirement and is not restated here; where this plan and the brief differ, the brief governs and the difference is a plan defect.
- This is a later unit of the same run and lands in the same pull request (109). The plan that built the brief as first ratified is closed under `completed/`.

## Definition of Done
- The plugin's text states, each once and at the place a session that needs it reads it: what reaches the owner and when (record 18's entry); that one Orchestrator session carries several briefs by default and when another is started (record 15's entry); what Counsel may say to an Orchestrator session and the guard on what is asked of it (record 8's entry); the dispatcher's freedom of relay and that it looks after whatever it sent the work to (the Dispatch section); a view from any other model (record 16's entry).
- The proposed records numbered 4 and 14 on the list fixed at commit 5e3528a are gone from the branch, with nothing in their place; the one line of record 4 stays in the plugin's text where a peer channel is handled, with its reason.
- The proposed records numbered 8, 15, 16 and 18 state the decisions their entries give. Every remaining proposed record has a problem statement that says what was wanted and why and what failed to serve it, with no account of what was observed or happened that does not bear on the decision; no remaining record rests on the account that a brief waited for the run in progress.
- `docs/coding-agent/rules/common.md` carries the third standing rule as changed: the dispatcher may use any relay the environment offers.
- Added 2026-11-19 before the plan-draft audit, on his word relayed 08:43Z: the plugin version is 1.8.0, and the plugin's README, where someone who updates reads what changed, states plainly that a session with no role chosen is now Counsel and that the block in the Codex home no longer routes coding requests to the Orchestrator (brief, Directed during the run, the entry on the version).
- The text of pull request 109 states the same two things plainly. This is the Orchestrator's own obligation at publication, after the final review and the closeout audit: it reads the published text for both statements before it reports the terms of the version step met.
- Added 2026-11-19 on the first plan-draft audit: scenarios 1, 2, 3, 5 and 8 are shown where one can be made, against the brief's wording as changed 2026-11-19, and where one cannot the closeout says so plainly, scenario by scenario (brief, pass condition).
- The package validators pass. Nothing is marked accepted, nothing is retired, no number is taken.
- The branch is reviewed `APPROVED`, value audits at plan draft and closeout are logged, and a new numbered list of the remaining proposed records is fixed at the closing commit.

## Planner-added requirements
- The Orchestrator session at work answers a further hand-over by taking it or by saying it cannot take more. Needed because: the brief has another session started "where none is at work or the one at work cannot take more" and leaves that call to the harness; under the design chosen below the session at work is the part of the harness that makes it, and without its answer Counsel has nothing to start another on but a guess.

## Scope / Non-goals
- Scope: plugin text under `plugins/coding-agent-orchestration-harness/` on Counsel's conduct, on the Orchestrator under a brief, and on dispatch; the runtime adapter files that restate any of it; the nineteen proposed records; `docs/coding-agent/rules/common.md`; the run's records.
- Non-goals: the sentence for the record standard (`durable-docs-authoring/references/adr.md`), which the run "Decision records at intent altitude" owns and builds on its own branch. Marking a record accepted, numbering one, retiring an accepted record or repairing references to one. Editing either philosophy or its companion. The peer-messaging tool itself. Any permission setting.

## Design
- Fixed by the brief and not compared: every decision the entries of 2026-11-19 state.
- The choice left is how Counsel learns whether an Orchestrator session at work can take a further brief.
- Chosen: Counsel hands the brief to the Orchestrator session at work, and that session answers that it takes it or that it cannot take more; on the second answer, or where none is at work, Counsel starts one by the means the workspace records. Alternative: Counsel judges from outside, by what it knows of the session's load, and starts another without asking.
- structure: the chosen design keeps the call with the one session that knows its own state; the alternative gives Counsel a second, staler copy of that state.
- evolution: the chosen design adds no concept, since a hand-over and its answer already exist; the alternative adds a measure of load that some text would have to define.
- verification: the chosen design is shown by one hand-over and its answer; the alternative has nothing to observe but Counsel's guess.
- operation: the chosen design costs one message for each brief; a session that does not answer is already covered by the text on a stopped run.
- human: under both the owner is asked nothing, and neither adds anything to what reaches him.
- safety: neither changes what a session may do.
- Why chosen wins: the brief makes the call the harness's, and the session at work is the only part of the harness that can make it from knowledge and not from a guess.
- The work is one unit and not seven small changes, because the change to record 15 touches the problem statements of several records and the entry on record 8 is held by text on both Counsel's and the Orchestrator's side.

## Compatibility stance
- surface: the plugin reference `subagent-strategy/references/seats.md` and the pointers to it; the names of the proposed records.
- stance: break. The consumers are the plugin's own files, which this plan changes together, and the pull request's reader, who gets a new list. No released version carries the text changed here: it is on this unmerged branch only.

## Context (workspace)
- Governing brief: `docs/coding-agent/briefs/active/one-conversation-with-counsel-brief.md`, ratified 2026-11-12; its entries of 2026-11-19 reached this session as Counsel's relay of 2026-11-19 08:34Z quoting the owner, admitted by the standing approval in `docs/coding-agent/rules/common.md`.
- Philosophies, by the pointer lines in `common.md`: `docs/product-philosophy.md` and `docs/engineering-philosophy.md`, each with its companion.
- Run record: `docs/coding-agent/plans/active/one-conversation-with-counsel-run.md`. Readings file: `docs/coding-agent/plans/active/one-conversation-with-counsel-readings.md`.
- Start revision of this unit: fe43aae (the brief and Counsel's notes as changed 2026-11-19). The brief's entry on the version came in after it, by Counsel's relay of 2026-11-19 08:43Z, and is part of this unit's requirement.
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
  handing a ratified brief to an Orchestrator session at work and starting one only where none is at work or it answers that it cannot take more (One conversation, Runs side by side, the entry on record 15, and this plan's Design);
  what Counsel may say to an Orchestrator session, and the guard (the entry on record 8);
  a view from any other model the environment offers (the entry on record 16).
  Each sentence of those entries is held once; text that states the earlier decision is rewritten, not added to. Adapter files restate only what they already restate.
- acceptance:
  - Each sentence of the brief's statement under What reaches him and of its entries on records 8, 15, 16 and 18 that binds Counsel is held by a sentence in the owned files, once; the report maps each to its place.
  - No line in the owned files still states: that each brief gets its own Orchestrator session; that Counsel speaks to an Orchestrator only in the owner's words with no reading of its own; that the consulted model is of another family or serves the engineering discussion only; that each ready thing reaches him as a line when it is ready.
  - The text on taking a view from another model names no model family and assumes nothing about which model Counsel runs on, and no sentence this task writes fixes how many roles there are. The names a runtime's adapter file has to carry, and the roles that exist, stay named.
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
  The record standard as it stands on this branch, and its admission test, govern; a restated record that no longer passes the admission test is reported, not kept, and the Orchestrator tells the owner of any such further withdrawal through Counsel.
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
  The Orchestrator's own task (only it edits rule files). In Models And Peers In This Workspace, change the rule that dispatch goes only to the registered peer seats or Claude subagents and that a command-line call to another runtime is allowed only as a measurement instrument: the dispatcher may use any relay the environment offers and looks after what it sent the work to; Counsel hands a ratified brief to the Orchestrator session at work. The registered seats stay recorded as options. The lines of that section which state what the brief's Dispatch statement stands in place of (a first dispatch to a seat and a silent seat as rules of their own, nothing depending on a seat surviving, two peer seats never shared) go with it; that the session which dispatches looks after what it sent to, and that he is not the one to notice or repair, stays. Pointers follow Task_2's result. `last_updated` is set.
- acceptance:
  - The rule reads as the brief's Limits names it changed, with the date and the brief as its source.
  - Nothing in the file still limits dispatch to particular kinds of relay; no session is licensed to use a mode that skips a runtime's safety checks.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "The changed lines against the brief's Limits and Dispatch"

### Task_5: Version 1.8.0
- type: chore
- owns:
  - plugins/coding-agent-orchestration-harness/.claude-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.codex-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.github/plugin/plugin.json
  - .claude-plugin/marketplace.json
  - .github/plugin/marketplace.json
  - plugins/coding-agent-orchestration-harness/README.md
  - README.md
- depends_on: []
- description: |
  The brief's entry of 2026-11-19 on the version: the step is minor, 1.8.0, in place of 2.0.0, on its terms. Set the version wherever the current one is carried. Where someone who updates reads what changed, state plainly the two things the entry names; if neither README has such a place, add the shortest one that serves, in the plugin's README.
- acceptance:
  - No file carries 2.0.0 as the plugin's version; every place that carried it reads 1.8.0.
  - A reader updating from an earlier version finds, in the plugin's README, that a session with no role chosen is now Counsel and that the Codex home block no longer routes coding requests to the Orchestrator.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "py -I scripts/validate_harness_package.py and py -I scripts/run_validation_smoke_tests.py from the plugin root; git diff --check; a search for 2.0.0"
  - kind: review
    required: true
    owner: reviewer
    detail: "The README text against the entry's terms"

### Task_6: The scenarios shown
- type: research
- owns:
  - docs/coding-agent/plans/active/one-conversation-with-counsel-scenarios.md
  - docs/coding-agent/plans/active/one-conversation-with-counsel-mechanisms.md
- depends_on: [Task_1, Task_2, Task_4]
- description: |
  Try in practice what this unit changes, with this branch's plugin text and by the means the workspace's Sessions record names: a ratified stand-in brief handed to an Orchestrator session already at work, and its answer (scenario 3 as the brief now gives the arrangement); work sent to a sub-agent that is lost part-way and replaced by the session that sent it (scenario 5 as reworded 2026-11-19). For scenarios 1, 2 and 8, say whether the earlier unit's trial still shows the scenario under the text as changed, and try again where it does not and one can be made. Record for each scenario what was tried, what happened, and where none can be made why not.
  Limits on a trial: stand-in briefs and throwaway working trees only; no session uses a mode that skips a runtime's safety checks; a refused check is recorded and not retried or worked around; no permission setting is changed; nothing is pushed, merged or sent outside the machine; every session started is ephemeral and ended by the task.
- acceptance:
  - For each of scenarios 1, 2, 3, 5 and 8 the scenarios file says, against the brief's present wording, what was shown and how to observe it, or plainly that none could be made and why.
  - Nothing is written as shown that was not observed in this task or cited from a recorded earlier trial that the changed text leaves valid.
- validation:
  - kind: manual
    required: true
    owner: worker
    detail: "For each trial: the command or act, the session's own output quoted, and the revision of the plugin text it ran on"
  - kind: review
    required: true
    owner: reviewer
    detail: "Each claim in the scenarios file against its recorded evidence"

### Task_7: Final review
- type: review
- owns: []
- depends_on: [Task_1, Task_2, Task_3, Task_4, Task_5, Task_6]
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

- Wave 1 (parallel): [Task_1, Task_2, Task_3, Task_5]
- Wave 2: [Task_4]
- Wave 3: [Task_6]
- Wave 4: [Task_7]

## Rollback / Safety
- Everything is on one branch and reverts as one. Nothing is merged, accepted, numbered or retired by this plan. Outside the repository two things happen: the branch and the text of pull request 109 are published after the final review and the closeout audit, on the standing approval for a finished, reviewed run; and Task_6's trials start ephemeral sessions on this machine within the limits that task states.

## Progress Log (append-only)

- 2026-11-19 08:36Z Draft plan sent to the Codex seat `agent-harness-reviewer` for plan review (a698257). 08:42Z CHANGES REQUESTED: HR-PLAN-F1 (the hand-over answer is a planner-added requirement and was not listed), HR-PLAN-F2 (Task_1's third acceptance bullet banned names the adapter files have to carry). Both applied (7bd100d); 08:44Z APPROVED on the delta.
- 2026-11-19 08:43Z Counsel's relay of the owner's word on the version (1.8.0 in place of 2.0.0, on terms); the brief's entry brought in by name (5ec43ee) and the plan extended with a Definition of Done line and Task_5 (46cd6aa). 08:46Z CHANGES REQUESTED: HR-PLAN-F3 (the pull request's half of the terms had no check). Applied as the Orchestrator's own obligation at publication (20c1f56); 08:47Z APPROVED, no finding open.
- 2026-11-19 08:47Z The reading is written in the readings file before the plan-draft audit is dispatched.
- 2026-11-19 08:47Z Value audit dispatched (Claude subagent `harness-auditor` on Fable, a new dispatch), text verbatim:
  You are the value auditor. Read references/value-audit-mandate.md of the orchestration-harness skill and follow it exactly. Position: plan draft. Plan: <worktree>/docs/coding-agent/plans/active/one-conversation-with-counsel-his-reading-plan.md. Governing brief: <worktree>/docs/coding-agent/briefs/active/one-conversation-with-counsel-brief.md. Changes since: none.
- 2026-11-19 08:55Z Verdict as returned (machine paths shortened; the two comparison lines are in the readings file):
  Value audit verdict, plan draft. Two items are `ask-now` (the Design clause on what the line to him says, and the non-goal of trying no scenario); both can be cured by revising the plan. Everything else is `cited` or `inferred`.
  The dispatch matched the fixed template. I followed the installed mandate (plugin 1.5.0). The branch's own copy differs from it by two added lines, which I did not read or follow. No notes file was opened; the readings file was opened only after the grades were fixed.
  Position: plan draft
  Documents read:
  - `docs/coding-agent/plans/active/one-conversation-with-counsel-his-reading-plan.md`
  - `docs/coding-agent/briefs/active/one-conversation-with-counsel-brief.md` (and its first-ratified version at a295f45, for the wording on machine obstacles and scenario 5)
  - `docs/coding-agent/rules/common.md` (pointer lines; Standing Approvals, same as HEAD 8ce2367, tree clean)
  - `docs/product-philosophy.md` and `product-philosophy-companion.md`
  - `docs/engineering-philosophy.md` and `engineering-philosophy-companion.md`
  - Read to understand, never as support: the `Scenarios` section of `docs/coding-agent/plans/active/one-conversation-with-counsel-run.md`; lines 64-68 of `plugins/coding-agent-orchestration-harness/skills/counsel/SKILL.md`; the file names of the nineteen proposed records.
  Product basis: philosophy (the brief traces to the product philosophy; ebigunso is owner and product owner)
  Not audited: none
  Missing inputs: none
  Value documents changed in range: none (no range at plan draft). The brief's amendments of 2026-11-19 (commits fe43aae and 5ec43ee) each carry his quoted words with the date beside them.
  Items:
  - DoD 1, the plugin's text states the five matters, each once where its reader reads it | maps to the brief | cited | brief, What reaches him: "Only what needs him reaches him, and it arrives ready to decide."; Runs side by side: "One Orchestrator session carries several briefs at once by default."; entry on record 8: "Counsel may give the Orchestrator its own reading of what he wants, marked as its own"; Dispatch: "free to send it to a sub-agent by any relay the environment offers, and it looks after whatever it sent the work to"; entry on record 16: "Counsel may take a view from any other model the environment offers"; engineering philosophy §5: "Each thing is written once, in the place whose pace matches its reason" | -
  - DoD 2, records 4 and 14 gone with nothing in their place; record 4's line stays in the plugin's text | maps to the brief | cited | brief: "Record 14 ... is withdrawn, with nothing in its place"; "Record 4 ... is withdrawn. Its one line stays in the plugin's text where a peer channel is handled, with its reason." | -
  - DoD 3, records 8, 15, 16, 18 restated; every remaining problem statement read against his sentence; no record rests on a brief having waited | maps to the brief | cited | brief, entry on record 17: "The problem statement of a record says what was wanted and why, and what failed to serve it; everything in it bears on the decision, and an account of what was observed or of what happened, which does not, is left out."; entry on record 15: "Its account that a brief used to wait for the run in progress is not so and goes."; "the change to record 15 touches the context of several of them"; engineering philosophy §2: "Contents that say what is so." Not graded as a conflict: the brief's own line under Who it is for still reads "a brief handed over while another run is in progress waits for that run", which is Counsel's to square with the entry on record 15. | -
  - DoD 4, `common.md` carries the third standing rule as changed | maps to the brief | cited | brief, Limits: "On his word of 2026-11-19 it changes a third ... the dispatcher may use any relay the environment offers." | -
  - DoD 5, version 1.8.0 and the README states the two things | maps to the brief | cited | brief: "The version step is minor, 1.8.0, on these terms: the pull request, and wherever someone who updates reads what changed, state plainly that a session with no role chosen is now Counsel and that the block in the Codex home no longer routes coding requests to the Orchestrator." | -
  - DoD 6, pull request 109's text states the same, at publication after the final review and the closeout audit; the unit lands in pull request 109 | maps to the brief | cited | outward-facing, passed on the standing approval in `common.md`: "A finished, reviewed run may publish its branch and open pull requests in this repository without asking first. Merges are not covered and wait for the owner." (record: "Given and accepted by the repository's owner, ebigunso, on 2026-09-30, relayed by Counsel: \"The common rule proposed, accepted.\""; whether those words were said a file cannot show). I read it as covering the text of the run's own pull request once the run is finished and reviewed, which is where the plan puts the act. Brief, the version entry, as above. The plan's Rollback line "nothing outside the repository is written" does not hold beside this entry. | -
  - DoD 7, validators pass; nothing accepted, retired or numbered | maps to the brief | cited | brief, Pass conditions: "the package validators pass"; Limits: "What waits for him today still waits for him: ... accepting a decision record by name"; "A number that must be unique across runs is taken when the work lands, not while it is drafted."; "He has accepted none of the nineteen." | -
  - DoD 8a, the branch is reviewed `APPROVED` and the value audits are logged | maps to the brief (how its result is checked) | cited | product philosophy §2: "confidence is never taken on the builder's word: what was not done or not checked is said outright"; §6: "Not its own judge." | -
  - DoD 8b, a new numbered list of the remaining proposed records fixed at the closing commit | maps to the brief | inferred | extends brief: "he read the nineteen proposed records against the list fixed at commit 5e3528a and spoke to six of them by its numbers"; "hold his acceptance by number until the changed records are rebuilt"; cheap to undo | -
  - Planner-added: the Orchestrator session at work answers a further hand-over by taking it or saying it cannot take more | maps to the brief | inferred | extends brief: "Counsel hands the brief to an Orchestrator session already at work in the repository, and starts one where none is at work or the one at work cannot take more."; "that is the harness's to decide and no question to him"; "Each Orchestrator states when it takes a brief what its run will touch."; cheap to undo; follows the means | -
  - Design, human bullet: "under the chosen design the line he gets says which session carries the brief" (Tasks 1 and 2 build from "this plan's Design") | scope expansion | ask-now | no statement covers it; against it, brief, What reaches him: "Only what needs him reaches him ... no account of what was done or is going on is written out for him"; product philosophy §1: "A design that works only if the person understands a role, a model or a step of the process is wrong"; beside it, brief: "the line that tells him the run has started says what it runs on" | Reasons: it adds to what reaches him with no support, and the statements that bear on it pull apart. Value question: when a brief he has ratified goes to a session already carrying other work, is he told which session carries it, or only that its work has started, hearing more only if he asks where the brief stands? Struck from the plan, this item is gone and nothing is owed to him.
  - Non-goal: the sentence for the record standard is the other run's | maps to the brief | cited | brief, entry on record 17: "The same goes into the record standard, in the run that owns it." | -
  - Non-goal: marking a record accepted, numbering one, retiring an accepted record or repairing references to one | maps to the brief | cited | brief, Limits: "accepting a decision record by name" waits for him; "three decision records, which are replaced by records he accepts by name" | -
  - Non-goal: editing either philosophy or its companion | maps to the brief | cited | brief, Limits: "a change to a philosophy" waits for him | -
  - Non-goal: trying any scenario in practice ("none can be made by this unit's work that the earlier unit did not already try") | maps to the brief (changes how a pass condition is checked) | ask-now | brief, Pass conditions: "Agent-checkable: ... scenarios 1, 2, 3, 5 and 8 are shown where one can be made, and where one cannot the closeout says so plainly."; "Scenarios 4 and 5 were changed again on his words of 2026-11-19." | Reason: it loosens a pass condition. The plan settles ahead of the work, on its own word, that nothing can be shown, while this unit changes the default way a brief reaches a run (handed to the session at work, which answers) and scenario 5's wording changed on 2026-11-19. The plan's own Design says the chosen design "is shown by one hand-over and its answer". Value question: after the way a ratified brief reaches a run was changed on 2026-11-19, is the result called ready on the earlier trials of the earlier arrangement, or is the changed way tried once in practice first, with scenario 5 stated against its new wording? A plan that tries what can be made, and says per scenario why not where it cannot, meets the condition as the brief words it and needs no answer from him.
  - Non-goal: the peer-messaging tool itself | internal mechanics | cited | engineering philosophy §7: "the burden of proof is on what is added or kept, and absence needs no defence" | -
  - Non-goal: any permission setting | maps to the brief | cited | brief: "an allow rule for the merge tool in his own settings, which is his to make and which nothing in the work makes for him"; "No check a runtime makes for safety is defeated to avoid it." | -
  - Compatibility stance: break, for the reference on seats and the names of the proposed records | internal mechanics | cited | engineering philosophy §7: "What already exists has no claim."; brief: "The plugin's reference on seats shrinks to what a dispatcher must know when the relay happens to be a peer channel." | -
  - A1: one Orchestrator session has carried two briefs side by side | maps to the brief | cited | brief, entry on record 15: "with the grounds that one session had carried this run and the run on decision records side by side for a week and that one session for each brief had never been done; told 2026-11-19: \"Yes I agree with those takes.\"" | -
  - A2: record 4's line belongs in what remains of the reference on seats | internal mechanics | cited | brief: "Its one line stays in the plugin's text where a peer channel is handled"; "shrinks to what a dispatcher must know when the relay happens to be a peer channel"; engineering philosophy §5: "where the reader who needs it will be reading when the decision comes" | -
  - Task_1, Counsel's conduct | maps to the brief | cited | brief, What reaches him and the entries on records 8, 15, 16, 18 as quoted above; entry on record 16: "no family is named and nothing assumes which model Counsel runs on"; "The plugin's text goes on naming the roles that exist."; engineering philosophy §4: "A model's name, a price, a count ... these go where changing them costs one line"; §5 as above. The hand-over answer is graded under Planner-added. | -
  - Task_2, the Orchestrator under a brief, and dispatch | maps to the brief | cited | brief, Dispatch as quoted; entry on record 8: "A question reaches Counsel only when its options differ in what he would experience ... where they do not, the call is the Orchestrator's own"; "The reading carries none of his authority; the Orchestrator weighs it as it weighs its own inferences"; entry on record 15 as quoted; "What is known about the obstacles of the machine the work runs on reaches whatever starts work on it" (its kind on 2026-11-19 is tagged inferred, but its content was ratified with the brief on 2026-11-12 and the task keeps what is built); "Both Auditor mandates go on reading the record of the machine's obstacles before grading, as built." Any line changed in either mandate is graded at closeout from the diff. | -
  - Task_3, the proposed records: delete 4 and 14, restate 8, 15, 16, 18, rename where the subject no longer says the decision, read the rest against the entry on record 17 | maps to the brief | cited | brief, the entries on records 4, 14, 15 and 17 as quoted; engineering philosophy §7: "someone who knows what the harness is for can predict where a thing is and what it is called before they look" | -
  - Task_3, a restated record that fails the admission test is reported and not kept ("or fewer with each further withdrawal reported") | maps to the brief | inferred | extends brief: "Counsel then held it against the record standard's admission test and recommended withdrawing it; told 2026-11-19: \"Yes, withdraw record 4.\""; product philosophy §2: "If a decision can be undone and stays inside the work, it is made and reported, and not asked."; §3: "The telling is not optional"; cheap to undo. Both withdrawals so far were his by name, so the support holds only if a further withdrawal is told to him. | direction
  - Task_4, this repository's rule on dispatch | maps to the brief | cited | brief, Limits, the third rule as quoted; "It changes two standing rules of his, and only as far as this brief says"; "No check a runtime makes for safety is defeated to avoid it." | -
  - Task_5, version 1.8.0 | maps to the brief | cited | brief: "The change takes a minor version step, to 1.8.0."; the version entry as quoted | -
  - Task_6, final review over the unit's range | maps to the brief (how its result is checked) | cited | product philosophy §2: "a result is judged by an agent other than the one that built it"; §6: "Not its own judge." | -
  - Decision Log | - | no entries | - | -
  Human-only conditions pending: "the next two briefs he hands over close together both start without him opening a session; over those two runs he opens no Orchestrator session, starts or repairs no seat, and is not the one who notices a stop."
  Scenarios: none
- Acting on the verdict: two items are ask-now and the verdict says each is cured by revising the plan, so the plan is revised and nothing goes to him. The Design's clause that the line he gets says which session carries the brief is struck: nothing in the brief has him told that. The non-goal of trying no scenario is withdrawn and a task added that tries what this unit changes (a hand-over to a session at work and its answer; a sub-agent lost part-way and replaced by the session that sent it the work) and states scenario by scenario, against the brief's present wording, what was shown and why not where one cannot be made. The item marked direction: a further withdrawal of a proposed record on the admission test is told to him through Counsel, and Task_3 now says so. Rollback said nothing outside the repository is written; the pull request's text is, at publication, and the line is corrected. The brief's line under Who it is for still says a brief handed over while another run is in progress waits for that run; that is Counsel's sentence and is told to Counsel. The revised plan goes back to the review seat for the delta and to a second plan-draft audit before any Worker starts.
- 2026-11-19 08:57Z Delta review of the revised plan by the Codex seat `agent-harness-reviewer`: APPROVED at c84305b, no finding open. The reading for the revised plan was written in the readings file at c84305b, before the second plan-draft audit is dispatched.
- 2026-11-19 08:58Z Value audit dispatched (Claude subagent `harness-auditor` on Fable, a new dispatch), text verbatim:
  You are the value auditor. Read references/value-audit-mandate.md of the orchestration-harness skill and follow it exactly. Position: plan draft. Plan: <worktree>/docs/coding-agent/plans/active/one-conversation-with-counsel-his-reading-plan.md. Governing brief: <worktree>/docs/coding-agent/briefs/active/one-conversation-with-counsel-brief.md. Changes since: none.
- 2026-11-19 09:04Z Verdict as returned (machine paths shortened; the two comparison lines are in the readings file):
  Value audit verdict, plan draft (second audit of this plan, graded on the whole plan as it stands at 66508df, tree clean). No item is `ask-now` and none is `ungraded`. Three items are `inferred`, one of them marked `direction`; the rest are `cited`.
  The dispatch matched the fixed template. I followed the installed mandate (plugin 1.5.0, identical to the copy on `main`); the branch's own copy differs and I did not read it. No notes file was opened. The readings file was opened once, after the grades were fixed, for its sections on this plan and its Findings only. The earlier verdict logged in the plan was not used as support.
  Position: plan draft
  Documents read:
  - `docs/coding-agent/plans/active/one-conversation-with-counsel-his-reading-plan.md`
  - `docs/coding-agent/briefs/active/one-conversation-with-counsel-brief.md` (and, at a295f45, its first-ratified lines on machine obstacles and scenario 5)
  - `docs/coding-agent/rules/common.md` (pointer lines; Standing Approvals, as at HEAD 66508df)
  - `docs/product-philosophy.md` and `docs/product-philosophy-companion.md`
  - `docs/engineering-philosophy.md` and `docs/engineering-philosophy-companion.md`
  - Read to understand, never as support: file names only of the nineteen proposed records, of the files carrying `2.0.0`, and of changelog-like files (none exists).
  Product basis: philosophy (the brief states it traces to the product philosophy; ebigunso is owner and product owner)
  Not audited: none
  Missing inputs: none
  Value documents changed in range: none (no range at plan draft). The brief's entries of 2026-11-19 each carry his quoted words with the date.
  Items:
  - DoD 1, the plugin's text states the five matters, each once where its reader reads it | maps to the brief | cited | brief, What reaches him: "Only what needs him reaches him, and it arrives ready to decide."; Runs side by side: "One Orchestrator session carries several briefs at once by default."; entry on record 8: "Counsel may give the Orchestrator its own reading of what he wants, marked as its own"; Dispatch: "free to send it to a sub-agent by any relay the environment offers, and it looks after whatever it sent the work to"; entry on record 16: "Counsel may take a view from any other model the environment offers"; engineering philosophy §5: "Each thing is written once, in the place whose pace matches its reason, where the reader who needs it will be reading when the decision comes." | -
  - DoD 2, records 4 and 14 gone with nothing in their place; record 4's line stays in the plugin's text | maps to the brief | cited | brief: "Record 14 ... It is withdrawn, with nothing in its place"; "Record 4 ... It is withdrawn. Its one line stays in the plugin's text where a peer channel is handled, with its reason." | -
  - DoD 3, records 8, 15, 16, 18 restated; every remaining problem statement read against his sentence; no record rests on a brief having waited | maps to the brief | cited | brief, entry on record 17: "The problem statement of a record says what was wanted and why, and what failed to serve it; everything in it bears on the decision, and an account of what was observed or of what happened that does not bear on the decision is left out."; entry on record 15: "Its account that a brief used to wait for the run in progress is not so and goes." with his words "The base assumption is probably wrong."; engineering philosophy §2: "A guess is not written as a finding." Not graded as a conflict: the brief's line under Who it is for still reads "a brief handed over while another run is in progress waits for that run"; the entry on record 15 itself says that assumption was Counsel's, so the line is Counsel's to square. | -
  - DoD 4, `common.md` carries the third standing rule as changed | maps to the brief | cited | brief, Limits: "On his word of 2026-11-19 it changes a third: this workspace's rule that dispatch goes only to the registered peer seats or to Claude subagents, and that a command-line call to another runtime is allowed only as a measurement instrument; the dispatcher may use any relay the environment offers." | -
  - DoD 5, version 1.8.0 and the plugin's README states the two things | maps to the brief | cited | brief: "The version step is minor, 1.8.0, on these terms: the pull request, and wherever someone who updates reads what changed, state plainly that a session with no role chosen is now Counsel and that the block in the Codex home no longer routes coding requests to the Orchestrator." The repository has no changelog file, so the README is that place. | -
  - DoD 6, pull request 109's text states the same, read by the Orchestrator at publication after the final review and the closeout audit; the unit lands in pull request 109 | maps to the brief | cited | outward-facing, passed on the standing approval in `common.md`: "A finished, reviewed run may publish its branch and open pull requests in this repository without asking first. Merges are not covered and wait for the owner." (its record: "Given and accepted by the repository's owner, ebigunso, on 2026-09-30, relayed by Counsel: \"The common rule proposed, accepted.\""; whether those words were said a file cannot show). I read it as covering the text of the run's own pull request when the finished, reviewed run publishes, which is where the plan puts the act. Brief, the version entry as quoted. | -
  - DoD 7, scenarios 1, 2, 3, 5 and 8 shown where one can be made, against the wording as changed, and said plainly scenario by scenario where one cannot | maps to the brief | cited | brief, Pass conditions: "scenarios 1, 2, 3, 5 and 8 are shown where one can be made, and where one cannot the closeout says so plainly."; "Scenarios 4 and 5 were changed again on his words of 2026-11-19." | -
  - DoD 8, the package validators pass; nothing accepted, retired or numbered | maps to the brief | cited | brief, Pass conditions: "the package validators pass"; Limits: "What waits for him today still waits for him: ratifying a brief, accepting a decision record by name"; "A number that must be unique across runs is taken when the work lands, not while it is drafted."; "He has accepted none of the nineteen." | -
  - DoD 9a, the branch reviewed `APPROVED` and the value audits logged | maps to the brief (how its result is checked) | cited | product philosophy §2: "confidence is never taken on the builder's word: what was not done or not checked is said outright"; §6: "Not its own judge." | -
  - DoD 9b, a new numbered list of the remaining proposed records fixed at the closing commit | maps to the brief | inferred | extends brief: "he read the nineteen proposed records against the list fixed at commit 5e3528a and spoke to six of them by its numbers"; "hold his acceptance by number until the changed records are rebuilt"; cheap to undo | -
  - Planner-added requirement and the Design's choice: the Orchestrator session at work answers a further hand-over by taking it or saying it cannot take more, against Counsel judging from outside | maps to the brief | inferred | extends brief: "Counsel hands the brief to an Orchestrator session already at work in the repository, and starts one where none is at work or the one at work cannot take more."; "that is the harness's to decide and no question to him"; cheap to undo; it follows the means. The answer must not become a wait: "A brief ratified while other runs are in progress does not wait for them." | -
  - Non-goal: the sentence for the record standard is the other run's | maps to the brief | cited | brief, entry on record 17: "The same goes into the record standard, in the run that owns it." | -
  - Non-goal: marking a record accepted, numbering one, retiring an accepted record or repairing references to one | maps to the brief | cited | brief, Limits: "accepting a decision record by name" waits for him; "three decision records, which are replaced by records he accepts by name". The brief's revision of the four accepted records (his word of 2026-11-17, "Which run does it he did not say") is not in this unit and stays owed by the run. | -
  - Non-goal: editing either philosophy or its companion | maps to the brief | cited | brief, Limits: "a change to a philosophy" waits for him | -
  - Non-goal: the peer-messaging tool itself | internal mechanics | cited | engineering philosophy §7: "the burden of proof is on what is added or kept, and absence needs no defence" | -
  - Non-goal: any permission setting | maps to the brief | cited | brief: "an allow rule for the merge tool in his own settings, which is his to make and which nothing in the work makes for him"; "It works within what he has already allowed for the repository" | -
  - Compatibility stance: break, for the reference on seats and the names of the proposed records | internal mechanics | cited | engineering philosophy §7: "What already exists has no claim."; brief: "The plugin's reference on seats shrinks to what a dispatcher must know when the relay happens to be a peer channel." (`seats.md` is not on `main`.) | -
  - A1: one Orchestrator session has carried two briefs side by side | maps to the brief | cited | brief, entry on record 15: "with the grounds that one session had carried this run and the run on decision records side by side for a week and that one session for each brief had never been done; told 2026-11-19: \"Yes I agree with those takes.\"" | -
  - A2: record 4's line belongs in what remains of the reference on seats | internal mechanics | cited | brief: "Its one line stays in the plugin's text where a peer channel is handled, with its reason."; "shrinks to what a dispatcher must know when the relay happens to be a peer channel"; engineering philosophy §5 as quoted | -
  - Task_1, Counsel's conduct | maps to the brief | cited | brief, What reaches him and the entries on records 8, 15, 16 and 18 as quoted; entry on record 16: "no family is named and nothing assumes which model Counsel runs on"; "The plugin's text goes on naming the roles that exist."; engineering philosophy §4: "A model's name, a price, a count, a date-bound fact: these go where changing them costs one line." The hand-over answer is graded under Planner-added. | -
  - Task_2, the Orchestrator under a brief, and dispatch | maps to the brief | cited | brief, Dispatch as quoted, with "A relay that lets the sub-agent message the dispatcher in the middle of the work is preferred and not required."; entry on record 8: "A question reaches Counsel only when its options differ in what he would experience"; "The reading carries none of his authority; the Orchestrator weighs it as it weighs its own inferences, and he is told, in Counsel's read at closeout and not at the time."; "What is known about the obstacles of the machine the work runs on reaches whatever starts work on it" (reworded 2026-11-19 on Counsel's reading, tagged inferred; its content was ratified with the brief on 2026-11-12, checked at a295f45); "Both Auditor mandates go on reading the record of the machine's obstacles before grading, as built." Any line actually changed in either mandate is graded at closeout from the diff; one that loosens a stop would be held there. | -
  - Task_3, the proposed records: delete 4 and 14, restate 8, 15, 16 and 18, rename where the subject no longer says the decision, read the rest against the entry on record 17 | maps to the brief | cited | brief, the entries on records 4, 14, 15, 17 as quoted; "Record 18, what reaches him. It is restated as the statement under What reaches him now reads."; engineering philosophy §7: "someone who knows what the harness is for can predict where a thing is and what it is called before they look" | -
  - Task_3, a restated record that no longer passes the admission test is reported, not kept, and told to him through Counsel | maps to the brief | inferred | extends brief: "Counsel then held it against the record standard's admission test and recommended withdrawing it; told 2026-11-19: \"Yes, withdraw record 4.\""; product philosophy §2: "If a decision can be undone and stays inside the work, it is made and reported, and not asked."; §3: "The telling is not optional"; cheap to undo. Both withdrawals so far were his by name, and the brief says of records 8, 15, 16 and 18 that each is restated, so a withdrawal of one of those leaves a gives-statement unmet and is graded against it at closeout. | direction
  - Task_4, this repository's rule on dispatch, edited by the Orchestrator | maps to the brief | cited | brief, Limits, the third rule as quoted; "Counsel hands the brief to an Orchestrator session already at work in the repository"; "No check a runtime makes for safety is defeated to avoid it." Standing Approvals is not touched by the task. | -
  - Task_5, version 1.8.0 | maps to the brief | cited | brief: "The change takes a minor version step, to 1.8.0."; the version entry as quoted | -
  - Task_6, the scenarios shown, with its limits on a trial | maps to the brief | cited | brief, Pass conditions as quoted; core scenarios 3 and 5 as changed; "No check a runtime makes for safety is defeated to avoid it."; his words of 2026-11-13: "test them out so that it doesn't say something that turns out impossible in practice." Not outward-facing as the plan bounds it: sessions are ephemeral and on this machine, nothing is pushed, merged or sent, no setting is changed. The limits tighten and are not held. | -
  - Task_7, final review of the range by the review seat | maps to the brief (how its result is checked) | cited | product philosophy §2: "a result is judged by an agent other than the one that built it"; §6: "Not its own judge." | -
  - Decision Log | - | no entries | - | -
  Human-only conditions pending: "the next two briefs he hands over close together both start without him opening a session; over those two runs he opens no Orchestrator session, starts or repairs no seat, and is not the one who notices a stop."
  Scenarios: none
  Observations outside the grades, for the Orchestrator:
  - The plan's Goal and Task_1 point to a brief section "Sessions and roles". The brief on disk has no such heading; those statements are under "One conversation".
  - Task_4 names only the rule on kinds of relay. `common.md` also carries, in Models And Peers, the first-dispatch and silent-seat line and "nothing depends on a seat surviving, and two peer seats are never shared between two Orchestrators", which the brief's Dispatch statement says it stands in place of. The plan does not say whether those lines go; the closeout audit grades whatever the diff does.
  - The brief's Pass conditions dropped the condition on a seat having seen an earlier unit, with no quote of its own; it rests on his "Yes, that's the core and those consequences are right." in the entry on record 14. No plan item depends on it.
- Acting on the verdict: no item is ask-now or ungraded, and the plan review closed with no finding open, so the ratified brief authorizes execution and wave 1 is dispatched. The item marked direction (a further withdrawal on the admission test): any such withdrawal is told to him through Counsel, and one of records 8, 15, 16 or 18 is not withdrawn by a Worker's report alone; it comes back to the Orchestrator first. From outside the grades: the plan's two pointers to a brief section "Sessions and roles" are corrected to the brief's heading "One conversation"; Task_4 is read as also taking out of the rule file the lines the brief's Dispatch statement stands in place of (a first dispatch to a seat and a silent seat as rules of their own, nothing depending on a seat surviving, two seats never shared), and its description now says so; the hand-over answer must not become a wait, which Tasks 1 and 2 are told. The brief's line under Who it is for and the pass condition dropped without a quote of its own are Counsel's and are told to Counsel.
- 2026-11-19 about 09:05Z (first written as 09:10Z without reading the clock; the dispatch preceded the review seat's message of 09:06:55Z) Wave 1 dispatched in parallel, each to a Claude subagent `harness-worker` on Fable 5.2 at low reasoning effort: Task_1, Task_2, Task_3, Task_5. Each is told that a hand-over answer is not a wait where it bears on its task, and that one of records 8, 15, 16 or 18 is not withdrawn on a Worker's judgement.
- 2026-11-19 09:15Z Wave 1 integrated: Task_1, Task_2, Task_3 and Task_5 report done, each inside its owns; the package validator, the smoke tests and `git diff --check` pass on the whole tree and were rerun by the Orchestrator. Task_4 done by the Orchestrator in the same pass.
  - Task_1 (Counsel's conduct): `counsel/SKILL.md`, `counsel/references/first-session.md`, the two Counsel adapter files, the capability matrix. What reaches him and the entry on record 18 are held in Contacts with a run; the hand-over and its answer in Hand-over and relay; what Counsel may say and the guard in Contacts with a run; a view from any other model in Limits and, as before, in the adapter files and the matrix.
    - Judgement calls (the Worker's): an unanswered or unreachable hand-over is handled as a run that has stopped making progress, by the text already there, with no new time limit; a hand-over that cannot reach the session until its turn ends counts as not waiting; record 8's reopen condition is written as conduct (on finding itself answering about tasks or in effect directing, Counsel tells the owner); the earlier option of handing back a question "below the level the owner wants to see" is replaced by the experience test; each reading Counsel gives is added to the short list in its notes that the closeout read includes; his ground (Counsel cannot know whether he is watching, so the session is taken as unattended) and scenario 4's "at a pause he is told what waits" are in the entry though the statement has neither; "told in a line" is kept where it only means brief; "the owner decides whether to go on without it" removed for "says so and goes on"; the Researcher's option names no fixed kinds of relay.
  - Task_2 (the Orchestrator's side, dispatch): twelve files. The Dispatch statements are Core rule 6 of `subagent-strategy/SKILL.md`; `seats.md` keeps its name and holds delivery on a peer channel and the one line on identity with its reason; one session for several briefs, its answer to a hand-over and runs kept apart are in `value-level-operation.md`, Runs Side By Side; the guard on questions and Counsel's own reading are two bullets of The Carrier, with one clause in the note to Counsel at closeout. No line of either Auditor mandate changed.
    - Judgement calls (the Worker's): "looks after" is spelled as starts, sees the work arrived, notices loss or silence, replaces, ends; Core rule 6 adds that no relay is used in a mode that skips a runtime's safety checks; the six-point part-way hand-off stays as ordinary dispatch discipline, and the rule that every follow-up carries it goes with the statement it rested on; the identity bullet is held once, in `seats.md`, without "given when it is created and not changed after"; the definition of an option is widened by "any other relay the environment offers" in three places; the Orchestrator records each reading of Counsel's it acts on and names it in the note to Counsel; the guard is written for questions of judgement only; record 8's reopen condition is not written on the Orchestrator's side; the hand-over is answered by the way it arrived, from what the session knows of its own state, with no measure of load.
  - Task_3 (the proposed records): records 4 and 14 deleted; records 8, 15, 16 and 18 restated and renamed; the problem statement of each of the other thirteen changed to say what was wanted and why and what failed to serve it. Seventeen remain, none accepted or numbered.
    - Judgement calls (the Worker's): record 15's Decision has exactly two bullets, "which run lands first does not settle it" inside the second; the four new subjects are the Worker's; record 8 keeps from ADR-D-0043 what the entry did not withdraw (an answer given as the person's rests on a statement that explicitly covers the question; the exception for a stop; Counsel's advice on direction goes to the person) and cites ADR-D-0059 for the experience test; rejected alternatives and reopen conditions beyond the entries in records 8, 16 and 18 are drafted from the entries' reasoning; Revisit When in records 8 and 18 says nothing had exercised it on 2026-11-19; record 1 no longer says "a session of its own"; record 7 cites ADR-D-0021 where it cited record 14; record 12 loses the account of the earlier loader, and records 3, 5 and 17 keep naming the record each replaces; for the eleven records the owner did not name the change is the smallest that makes the problem statement say what was wanted.
  - Task_5 (version): 1.8.0 in the three manifests and both marketplace files; a section "Updating To 1.8.0" at the head of the plugin's README with the two statements and how the Orchestrator role is opened in each runtime; the root README needed no change.
    - Judgement calls (the Worker's): no time-relative wording, so "differ from versions before 1.8.0" where his terms say "now" and "no longer"; the first statement carries the scope the plugin's text gives the default for each runtime; no way to restore the old routing is offered, since the plugin states none.
  - Task_4 (the Orchestrator's): in `docs/coding-agent/rules/common.md`, Models And Peers, the two entries on a first dispatch to a seat and on creating seats are replaced by one on dispatch by any relay, with the dispatcher looking after what it sent to and no mode that skips a safety check, and one on Counsel handing a ratified brief to the session at work; `last_updated` 2026-11-19.
  - Rulings (the Orchestrator's):
    - Record 15 holding two things stays one record: the brief's entry says "The record then holds two things". The Worker's doubt, that the two could be retired apart and that the first is close to what the product philosophy already yields, is told to Counsel.
    - Record 18 keeps the entry's wording on the short list; the wording and length of the list are under Not covered. Told to Counsel as a question of altitude.
    - Three statements the brief gives have no proposed record after the entries narrowed records 15 and 18 (a ratified brief does not wait; how many runs go at once is the harness's call; Counsel can say where every brief stands). No record is added: the plugin's text holds each and none was asked for. Told to Counsel.
    - Withdrawn before commit, two rulings of the Orchestrator's own. First it had both Workers let a session that Counsel did not start receive the owner's answer on the admitting entry by relay; the Counsel-side Worker's question showed that this widens what a relay can do on a message's own claim, and both files were restored to their committed text. In its place: a session takes a brief by hand-over only where Counsel's relays are admitted in it (The Carrier), and Counsel treats one where they are not as a session that cannot take more. Second it named "Counsel started the session" as a ground for taking a hand-over; the Orchestrator-side Worker pointed out that this admits only the first relay on the entry, and the sentence names no cases and points to The Carrier.
    - On Counsel's correction of the brief (825caac: no line for every start; he is told only where a run could not be started on what his record names) the line on every start is removed from `counsel/SKILL.md` and the limit reworded.
    - Left as they are: "a session Counsel started for the brief does not stop to ask" (the brief words it so); the mandates' and the template's uses of "seat"; the entry "The owner gives a decision once" on Counsel's side, which states when a relay counts and predates this unit.
- 2026-11-19 09:16Z The built range fe1e53f..cb23b8e sent to the Codex seat `agent-harness-reviewer` for review, and Task_6 dispatched to a Claude subagent `harness-worker` on Fable 5.2 at low reasoning effort (wave 3), with the plan's limits on a trial and this workspace's standing rules on sessions restated in its dispatch.

## Decision Log (append-only; re-plans and major discoveries)

- 2026-11-19 09:04Z After the second plan-draft audit, three corrections that change no requirement: the brief section pointed to is "One conversation" (the plan said "Sessions and roles", a heading the brief does not have); Task_4 says which further lines of the rule file go with the changed rule; a hand-over answer is not a wait (told to Tasks 1 and 2 in their dispatch, on the brief's "A brief ratified while other runs are in progress does not wait for them.").

## Notes
