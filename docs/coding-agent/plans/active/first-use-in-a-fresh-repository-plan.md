# Plan: First use in a fresh repository

- status: in_progress
- generated: 2026-10-07
- last_updated: 2026-10-07
- work_type: docs

## Goal
- The harness gives what the governing brief `docs/coding-agent/briefs/active/first-use-in-a-fresh-repository-brief.md` states: someone opening the plugin in a fresh repository with a Counsel session and an Orchestrator session reaches a ratified philosophy and a first stack without working around the harness, at the six places the report named.
- The brief is the requirement and is not restated here; where this plan and the brief differ, the brief governs and the difference is a plan defect.
- This is the first plan of the run recorded in `docs/coding-agent/plans/active/first-use-in-a-fresh-repository-run.md`.

## Definition of Done
- A philosophy is pure prose: no provenance tag on its statements and no ratification record inside it. Provenance and ratification live in a companion file beside it, named after it, with one record per ratified version (the ratifier's quoted words and the date); the forms say where it is, and the Orchestrator, the Auditor and setup look there.
- The plugin carries a philosophy reference stating what a philosophy holds, what is not in one and where that goes, the qualities Counsel checks, and one invented prose example naming no real project; Counsel reads it only after the discussion has produced a draft and lists gaps for the owner, never supplying wording; a gap left out is recorded in the companion so it is not raised again.
- The owner's acceptance of a stack by name, as his own statement in the Orchestrator session or Counsel's quoted relay, is enough for the Orchestrator to merge it; the text says so plainly and says the runtime's tool permission is the owner's to grant once, with no rule text standing in for it.
- Counsel takes a seat of its own on the peer channel before its first relay; the Counsel text names the convention. No acknowledgement rule is added for relays.
- Setup's report offers the standing approval that admits Counsel's relays; on the owner's yes it records the entry and writes the one line in the Repository Reference Documents section that records Counsel's seat and that relays are admitted; admission is recorded in the common rule file and nowhere else.
- The Counsel skill carries two lines for the one-time matters: at open, look in the section Counsel reads anyway for that line; if present, nothing more; if absent, read a first-session reference and follow it once (take the seat, offer setup if it has not run, have the standing approval recorded). The philosophy reference is read only when a draft is being checked. The skill's word count does not grow for the one-time procedure beyond the two lines.
- For the engineering discussion Counsel obtains a view from a model of another family by whatever route the environment provides, says which route, puts the question as the discussion put it, keeps the reply verbatim in the discussion notes with model and route named, and where no route exists says so and the owner decides.
- A Counsel session opened before setup has run says that setup has not run and offers it. Dates in value documents are the owner's local calendar date; channel timestamps are left alone.
- Where a statement changes what an accepted record decides, that record is revised (or a new one proposed) and accepted by the owner by name before harness text is built on it.
- Machine-specific user names and paths, and the names of the owner's other repositories, reach the remote in no file this work touches.
- Package validators and smoke tests pass; the branch has Reviewer `APPROVED`. Scenario 1 is shown on a fixture repository; of scenario 2 the part a fixture can carry is shown (a prose philosophy with its companion record is found by setup and read as ratified, with no missing-ratification flag), and the closeout says plainly that the discussion itself and the reference's effect on quality were not shown and are the owner's to judge.
- The plan closes and the run is reported ready as `completion-closeout.md` states: its branch published on the stack and a pull request opened under the standing approval, the note to Counsel sent, nothing merged; the run stays open until the owner's acceptance of its stack.

## Planner-added requirements
- The companion is named `<philosophy-stem>-companion.md` beside the philosophy and holds only provenance, the ratification records and the gaps left out; the audit's mandate names it as an input. It is not a notes file: discussion stays in notes files, which the Auditor never opens. Needed because: the brief sends the Orchestrator and the Auditor to the companion for the ratification, and the mandate keeps every notes file unread; a file that is an input to one reader and forbidden to another cannot be the same file.
- A philosophy ratified before this change, carrying its record and tags inside the document, is read as ratified until Counsel moves its record into a companion; readers accept either place. Needed because: two of the owner's philosophies were written with the plugin in the old form, and the brief does not ask that they be rewritten before the harness works on them.
- The engineering philosophy's discussion has no initiative and no brief, so its discussion notes (the outside view's verbatim reply included) live in a notes file beside that philosophy, `<philosophy-stem>-notes.md`, unread by the Auditor as every notes file is. Needed because: the brief says the reply is kept in the discussion notes, and today notes exist only beside a brief.
- The plugin version rises to 0.31.0 in the three manifests. Needed because: the owner's fresh repository ran the plugin at 0.30.0 from the runtime's plugin cache, which installs by version; the changed text reaches a repository only under a new version.

## Scope / Non-goals
- Scope: `skills/value-documents/SKILL.md`; `skills/counsel/SKILL.md` and a new `skills/counsel/references/` (the philosophy reference, the first-session reference); the Counsel adapters and the tool-capability matrix where they restate what Counsel may consult; `skills/orchestration-harness/references/{value-level-operation,value-audit-mandate,completion-closeout,status-model}.md` and the Orchestrator adapters where they state the run's close and the merge; `skills/rulebook/references/{bootstrap-lifecycle,rules-files,rule-suite-templates}.md`; `skills/git-workflow/references/stacked-prs.md` where it states merge authorization; the three manifests (version); this repository's `rules/common.md` and `rules/orchestrator.md`; decision records ADR-D-0035 and ADR-D-0038, and one proposed record on the merge.
- Non-goals: a relay acknowledgement contract; a named route for the outside view; any change to trivial work (the brief leaves all three out); the fixed dispatch template; the Auditor's grades; goal mode; rewriting existing philosophies of other repositories.

## Design
- Chosen: the companion is a file beside each philosophy, `<stem>-companion.md`, holding provenance, ratification records and the gaps left out and nothing of the discussion, named as an input in the mandate; the engineering discussion's notes are a notes file beside the philosophy, unread by the Auditor; the philosophy reference and the first-session reference are references of the counsel skill, read only at the moments the brief names; the setup report offers the relay approval and writes one line `Counsel: <identity>; relays admitted` in Repository Reference Documents beside the Standing Approvals entry that carries the owner's quoted words; the merge rests on the owner's acceptance of a stack by name, stated in the run's closeout text and this repository's rule, with a record of its own proposed for it; ADR-D-0035's permission to ask another model becomes the brief's duty with its no-route escape, route-neutral; the seat is claimed by Counsel following the first-session reference in every runtime, and no hook is built.
- Alternative A: keep the ratification record inside the philosophy as a short footer and move only the tags to the companion.
- Alternative B: build the session-start hook the brief's means names for the Claude runtime, the adapter claiming Counsel's seat.
- Lenses. structure: chosen gives the companion one home and one reader rule, and keeps every notes file on one side of the Auditor's boundary; A leaves the ratification in a document the owner wants as pure prose; B adds the plugin's first hook, bound to one channel tool the plugin never names. evolution: chosen lets any channel serve; A keeps two places for ratification over time; B ties the plugin to one runtime and one channel. verification: chosen is shown by scenario 1 on a fixture and by the mandate reading the companion; A the same; B needs a running Claude session to show. operation: chosen costs two lines at every Counsel open and a seat claim once per repository; B saves the claim's tokens once. human: chosen matches "pure prose" and "look for one line"; A does not give pure prose; B is invisible when it works and opaque when it fails. safety: chosen admits relays only through the common rule file the owner accepts; B fires in every session of the runtime, the Orchestrator's included.
- Why chosen: it gives every statement of the brief; the hook is a means, and departing from it changes nothing the owner experiences beyond one claim per repository (recorded as a finding).

## Compatibility stance (required if a contract/interface/persisted format is touched)
- surface: the philosophy's form (tags and ratification record inside it) and where a ratification is read; the common rule file's Repository Reference Documents section (a Counsel line); merge authorization.
- stance: migrate
- justification: the locatable consumers are the owner's repositories whose philosophies carry the old form; readers accept either place until Counsel moves a record (planner-added requirement 2), so nothing breaks on the day the text lands.

## Context (workspace)
- Governing brief: `docs/coding-agent/briefs/active/first-use-in-a-fresh-repository-brief.md`. Its ratification reached this session on 2026-10-07 as a relay from Counsel quoting the owner: "Yes, go work on it." Relays from Counsel are admitted by the Standing Approvals entry of 2026-10-01 in `docs/coding-agent/rules/common.md`.
- Run record: `docs/coding-agent/plans/active/first-use-in-a-fresh-repository-run.md`. Readings file: `docs/coding-agent/plans/active/first-use-in-a-fresh-repository-readings.md`. This plan starts from revision: 8b36645.
- Research: a Researcher mapped each statement to the text it changes (file and line) and the records it touches; its report is the basis of the Scope and Tasks. Counsel's skill is 3304 words at the start revision.
- Records touched: ADR-D-0035 (Counsel may ask another model: becomes the brief's duty with its escape; returns by name); ADR-D-0038 (its example "naming the pull request" gains the stack; its Revisit When names a failed relayed merge, and the report's failure was the runtime's permission layer, not the relay, so the record is not reopened; wording only, confirmed by the audit); ADR-D-0051 leaves merge authorization uncovered, so a record is proposed for it if the admission test passes.
- The audits of this run: this plan's draft and its close.
- Lessons applied: a changed form is traced through producer (Counsel), consumers (the Orchestrator, the Auditor, setup) and validation; a new line in the common rule file is traced through the templates, setup's writer and Counsel's reader.

## Open Questions (max 3)
- None.

## Assumptions
- A1: "a stack by name" is the owner naming the stack or its pull requests as he sees them; his acceptance covers each pull request in it. source: the brief, Merging a stack; a reading.
- A2: "recorded in the common rule file and nowhere else" excludes the Orchestrator's runtime memory and any other file; the owner's direct statement in the session still admits relays for that session, as ADR-D-0038 decides, and is recorded in the rule file to outlast it. source: the brief, Relay admission before setup; ADR-D-0038.
- A3: the setup report offers the approval naming Counsel's identity by the convention the Counsel text states, `<repository>-counsel` on the channel, and the owner's yes may correct the name. source: the brief, The peer channel; a reading.

## Tasks

### Task_1: The records carry the brief
- type: docs
- owns:
  - docs/coding-agent-orchestration-harness/decisions/**
- depends_on: []
- description: |
  Revise ADR-D-0035 (the outside view as the brief states it) and ADR-D-0038 where its wording names the pull request alone; run the admission test on a record that the owner's acceptance of a stack by name authorizes its merge, and draft it as proposed if it passes. Write only what the brief and this plan state.
- acceptance:
  - ADR-D-0035 states the brief's duty, its route neutrality and its no-route escape; everything else it decides is unchanged.
  - ADR-D-0038 keeps its decision; only the wording that names the pull request as the example changes, and its Revisit When is left as it is.
  - The admission test's result on the merge record is reported; if admitted, the draft meets adr.md's form and lifecycle, says what the brief's Merging a stack states and nothing more, and takes the lowest free number.
  - Each record whose decision, boundary, reasons or reopen conditions changed is named in the report, so each returns to the owner by name.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "python scripts/validate_harness_package.py; python scripts/run_validation_smoke_tests.py; git diff --check"
  - kind: review
    required: true
    owner: reviewer
    detail: "The records against adr.md and the brief; which return by name"
  - kind: manual
    required: true
    owner: user
    detail: "The owner accepts each proposed or revised record by its own name, carried by Counsel's relay; Wave 2 is not dispatched before that"

### Task_2: Counsel's side: the forms, the two references, the skill
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/value-documents/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/counsel/**
  - plugins/coding-agent-orchestration-harness/agents/Counsel.md
  - plugins/coding-agent-orchestration-harness/claude/agents/harness-counsel.md
  - plugins/coding-agent-orchestration-harness/skills/runtime-adapter-contract/references/tool-capability-matrix.md
- depends_on: [Task_1]
- description: |
  The value-documents forms (a philosophy as pure prose; the companion; dates; readers accept the old form until moved); the philosophy reference and the first-session reference as counsel references; the Counsel skill's two open-time lines, its drafting and ratification text, the outside view, the before-setup case, the seat convention; the Counsel adapters and capability matrix where they must allow the consulting route.
- acceptance:
  - The forms, Counsel's text, the two references and the Counsel adapters state the philosophy as prose with its companion and its notes file, the reference and when it is read, the seat and its convention, the two open-time lines and the first-session procedure, the outside view, the before-setup case and the dates, so that each statement of the brief's sections on them can be pointed to in these files; what the Orchestrator, the Auditor and setup do with the companion is Task_3's.
  - The philosophy reference states what the brief's means lists, in that order, what is not in a philosophy and where it goes, the qualities checked, and one invented example naming no real project; the Counsel text reads it only after a draft exists and never during the discussion.
  - The Counsel skill's word count, measured against 3304, grows for the one-time procedure by the two lines only; other additions are reported with their counts.
  - No value-documents text asks for a tag or a ratification record inside a philosophy; the brief's forms are unchanged.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "python scripts/validate_harness_package.py; python scripts/run_validation_smoke_tests.py; git diff --check; wc -w on counsel/SKILL.md before and after, reported"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review against the brief and the accepted records; the reference against ADR-D-0047's question (does it bind the document to the discussion's terms)"

### Task_3: The Orchestrator's side: setup, the run's close and the merge, the audit's inputs
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/**
  - plugins/coding-agent-orchestration-harness/skills/rulebook/**
  - plugins/coding-agent-orchestration-harness/skills/git-workflow/references/stacked-prs.md
  - plugins/coding-agent-orchestration-harness/agents/Orchestrator.md
  - plugins/coding-agent-orchestration-harness/claude/agents/harness-orchestrator.md
  - plugins/coding-agent-orchestration-harness/.claude-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.codex-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.github/plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/README.md
- depends_on: [Task_1]
- description: |
  Setup detects a philosophy by its companion's record (or the old form), offers the relay approval in its report and writes the Counsel line and the Standing Approvals entry on the owner's yes; the common-rule templates carry the line's form; the Orchestrator and the Auditor read the companion for a ratification, the mandate naming it as an input apart from the discussion notes; the owner's acceptance of a stack by name authorizes the merge, stated at run closeout, in the carrier, in the status model and the adapters, with the runtime permission as the owner's; the version bumps to 0.31.0.
- acceptance:
  - Every Definition of Done item on setup, admission, the merge and the readers of a ratification holds, and each statement of the brief's sections on them can be pointed to.
  - The fixed dispatch template is byte-identical; the mandate reads the companion as an input, still never opens a notes file, and opens the readings file only after the grades are fixed, as today.
  - The two Orchestrator adapters agree with each other and with the skill text.
  - No text says a relay acknowledgement is needed or names a channel tool.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "python scripts/validate_harness_package.py; python scripts/run_validation_smoke_tests.py; git diff --check"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review against the brief and the accepted records, with the adapter parity check"

### Task_4: This repository's rules, and scenarios 1 and 2 on a fixture
- type: chore
- owns:
  - docs/coding-agent/rules/common.md
  - docs/coding-agent/rules/orchestrator.md
  - docs/coding-agent/plans/**
- depends_on: [Task_2, Task_3]
- description: |
  The Orchestrator writes this repository's Counsel line in `common.md` and the merge rule in `orchestrator.md` as the new text has them; then runs the fixture in a temporary directory: scenario 1, a fresh agent given the setup dispatch offers the relay approval and writes the line on a yes, and a fresh agent given the Counsel skill opens, finds the line and does nothing more; the fixture part of scenario 2, the fixture holding an invented prose philosophy with a companion carrying a synthetic ratification record, setup finds it and records the pointer, a fresh agent following the Orchestrator's Documents step reads it as ratified with no missing-ratification flag, and a fresh Auditor dispatch by the fixed template on the fixture (a plan under its brief, both invented) reads the companion and returns no missing-ratification entry. The fixture's file contents (or the recipe that recreates them), the dispatch texts and the agents' replies are kept in this plan's Progress Log; no fixture is committed.
- acceptance:
  - `common.md` carries the Counsel line beside its Standing Approvals entry; `orchestrator.md` has the owner's acceptance of a stack by name cover each pull request in it.
  - The agents' replies show scenario 1 and the fixture part of scenario 2 (the Orchestrator's and the Auditor's lookup both) as the brief states them, or the plan records where they did not and what was corrected; the discussion itself and the reference's effect on quality are left to the owner and said so.
- validation:
  - kind: manual
    required: true
    owner: orchestrator
    detail: "Scenario 1 and the fixture part of scenario 2 (setup, the Orchestrator's Documents step, one Auditor dispatch) on the fixture; the fixture's contents, the dispatch texts and the replies logged verbatim in the Progress Log; this is also the branch's final review's input"
  - kind: review
    required: true
    owner: reviewer
    detail: "Final review of the branch: the rule files and the logged replies against the brief"

### Task_5: Close the plan and report the run ready
- type: review
- owns:
  - docs/coding-agent/plans/**
- depends_on: [Task_4]
- description: |
  The Orchestrator closes the plan (closeout audit with its reading) and reports the run ready, which stays open until the owner's acceptance of its stack: the branch pushed on the stack, a pull request opened under the standing approval, the note to Counsel.
- acceptance:
  - The closeout audit is dispatched by the fixed template and logged; the closeout says plainly which part of scenario 2 was shown on the fixture and that the discussion and the reference's effect on quality were not.
  - Every outgoing commit, message and pull request text is swept for machine-specific names and paths and for the names of the owner's other repositories before it is pushed; nothing is merged.
- validation:
  - kind: command
    required: true
    owner: orchestrator
    detail: "package validator and smoke tests; privacy sweep over every commit to be pushed"

## Task Waves (explicit parallel dispatch sets)
- Wave 1: Task_1
- Wave 2: Task_2, Task_3
- Wave 3: Task_4
- Wave 4: Task_5

## Rollback / Safety
- The branch reverts on its own; no migration, no persisted data; existing philosophies elsewhere keep working under planner-added requirement 2.

## Progress Log (append-only)
- 2026-10-07 Brief committed on the run's branch; the plan starts from revision 8b36645.
- 2026-10-07 Plan review (Codex reviewer): NEEDS_REVISION with four MAJOR and three MINOR findings, applied (see the Decision Log); a second round on one remaining MAJOR (the Auditor's companion lookup not exercised), applied; re-review at 9b506b4 APPROVED with no finding open. Plan validator passes.
- 2026-10-07 Plan-draft audit, dispatch text (to a fresh Auditor dispatch on Fable):

  ```text
  You are the value auditor. Read references/value-audit-mandate.md of the orchestration-harness skill and follow it exactly. Position: plan draft. Plan: docs/coding-agent/plans/active/first-use-in-a-fresh-repository-plan.md. Governing brief: docs/coding-agent/briefs/active/first-use-in-a-fresh-repository-brief.md. Changes since: none.
  ```

- 2026-10-07 Plan-draft audit, verdict as returned (machine paths redacted; the two comparison lines are logged in the readings file, not here):

  ## Value Audit: First use in a fresh repository (plan draft)

  Procedural disclosure: the plan and the brief were opened in the same tool call that located the mandate, before the mandate had been read. Both are sanctioned inputs; no notes file or readings file was opened before the grades were fixed, and the dispatch carried only the fixed template, so neither voiding condition is met. Noted here so the Orchestrator can judge it.

  - `Position: plan draft`
  - `Documents read: plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/value-audit-mandate.md (instructions); docs/coding-agent/plans/active/first-use-in-a-fresh-repository-plan.md (artifact); docs/coding-agent/briefs/active/first-use-in-a-fresh-repository-brief.md (governing brief); plugins/coding-agent-orchestration-harness/skills/value-documents/SKILL.md (instructions, to locate philosophies); docs/coding-agent/rules/common.md (pointer lines, Standing Approvals at HEAD; unmodified in the working tree); docs/coding-agent/rules/orchestrator.md, ADR-D-0035, ADR-D-0038, ADR-D-0051 (grep), skills/orchestration-harness/references/completion-closeout.md (grep), plugin.json version, counsel/SKILL.md word count (to understand what the plan changes; never as support); docs/coding-agent/plans/active/first-use-in-a-fresh-repository-readings.md (after grading, once)`
  - `Product basis: brief in the product owner's words (brief line 6: "ebigunso owns the harness; no product philosophy and no engineering philosophy exist for this repository"; ratified line 3: "Yes, go work on it." 2026-10-07)`
  - `Not audited: engineering side, no engineering philosophy (common.md pointer line "Engineering philosophy: none yet"). No item in this plan is internal mechanics only, so no item carries the record value.`
  - `Missing inputs: none` (brief under `briefs/active/`, carries ratification record and product basis; run record and readings file exist at the paths the plan names)
  - `Value documents changed in range: none` (position is plan draft; no range)

  Standing approvals relied on (common.md, Standing Approvals, at HEAD, committed): (SA-1) "A finished, reviewed run may publish its branch and open pull requests in this repository without asking first. Merges are not covered and wait for the owner. ... Given and accepted by the repository's owner, ebigunso, on 2026-09-30, relayed by Counsel: 'The common rule proposed, accepted.'" (SA-2) "a relay from the agmsg identity `agent-harness-counsel` that quotes the person directing the work carries that person's decisions to an Orchestrator session ... plan approval and its waiver are not carried ... Given and accepted by the repository's owner, ebigunso ... on 2026-10-01, relayed by Counsel: 'I accept ADR-D-0038 and the standing approval entry.'" Both entries record giver, acceptance of the entry, and date; whether the quoted words were said is not something a file can show.

  Items (item | mapping | grade | support | ask-now reasons / direction):

  - DoD 1 (philosophy pure prose; provenance and ratification in a companion beside it, one record per ratified version; Orchestrator, Auditor and setup look there) | maps to the brief | cited | brief 18 "A philosophy is pure prose. No provenance tag on its statements and no ratification record inside it."; 19 "Provenance and ratification live in a companion notes file beside each philosophy, named after it, with one ratification record per ratified version ... The Orchestrator and the Auditor look there for the ratification" | -
  - DoD 2 (philosophy reference: contents, read only after a draft, gaps listed, no wording supplied, gaps left out recorded in the companion) | maps | cited | brief 24 "The plugin carries a reference for what a philosophy states"; 25 "Counsel reads the reference only after the discussion has produced a draft ... a gap left out is recorded in the companion notes ... The reference never supplies wording"; 26 (means) "It carries one short example in prose, invented" | -
  - DoD 3 (acceptance of a stack by name, own statement or Counsel's quoted relay, is enough to merge; runtime permission the owner's once) | maps | cited | brief 30 "The owner's acceptance of a stack by name ... is enough for the Orchestrator to merge it ... The runtime's own tool permission for merging is the owner's to grant in that session once ... no rule text stands in for it." The item loosens this repository's per-pull-request merge rule (orchestrator.md line 40) exactly as the gives-statement asks; the owner also accepts the merge record by name under Task_1, so no stop is owed here. | -
  - DoD 4 (Counsel's own seat before first relay, convention named; no acknowledgement rule) | maps | cited | brief 35 "Counsel takes a seat of its own on the peer channel ... before its first relay; the Counsel text says so and names the convention."; 34 "No acknowledgement rule is added for relays." | -
  - DoD 5 (setup report offers the relay approval; on yes records the entry and the Counsel line; admission in the common rule file only) | maps | cited | brief 39 "Setup's report offers the standing approval that admits Counsel's relays ... Admission is recorded in the common rule file and nowhere else"; 43 "Setup writes that line in the same section when it records the approval." | -
  - DoD 6 (two open-time lines; first-session reference; philosophy reference only at a draft check; word count) | maps | cited | brief 43 "The skill carries two lines: at open, read the Repository Reference Documents section ... if it is absent, read a first-session reference and follow it once ... The philosophy reference is read only when a draft is being checked"; 72 "the Counsel skill's word count does not grow for the one-time procedure beyond the two lines" | -
  - DoD 7 (outside view, route named, question as put, verbatim reply, no-route escape) | maps | cited | brief 48 "Counsel obtains a view from a model of a different family ... Counsel says which route it used ... the reply is kept verbatim in the discussion notes with the model and the route named. Where the environment provides no such route, Counsel says so and the owner decides" | -
  - DoD 8 (before setup: say so and offer it; dates local) | maps | cited | brief 52 "say that setup has not run, and offer it"; 53 "Dates in value documents are the owner's local calendar date ... the channel's timestamps ... are left alone." | -
  - DoD 9 (changed records revised or proposed and accepted by name first) | maps | cited | brief 58 "Where it changes what an accepted decision record decides, that record returns to him for acceptance by name." | -
  - DoD 10 (no machine-specific names, paths or other-repository names reach the remote) | maps | cited | brief 59 "Machine-specific user names and paths, and the names of his other repositories, do not reach the remote in any file this work touches." | -
  - DoD 11 (validators and smoke tests pass; Reviewer APPROVED; scenario 1 on a fixture; scenario 2's checkable part; closeout says the rest is the owner's) | maps | cited | brief 72 "scenarios 1 and 2 are shown on a fixture repository where one can be made, and where one cannot the closeout says so plainly"; 73 human-only "scenarios 2 and 3 in his next real use; whether the reference improved a philosophy's quality without shaping the discussion". Showing only the checkable part does not loosen the pass condition: the discussion and the reference's effect are already human-only. | -
  - DoD 12 (plan closes; run reported ready: branch published, PR opened under the standing approval, note to Counsel, nothing merged; run stays open until acceptance of its stack) | maps | cited | SA-1 quoted above covers publish and pull request (step 1 passed on it); SA-1 "Merges are not covered and wait for the owner" and brief 30 cover nothing merged; brief 10 "How is the Orchestrator's" covers the closeout procedure. The note to Counsel is a message to a session of this repository's own work, not outside it, so it is not outward-facing. | -
  - Planner-added 1 (companion `<stem>-companion.md`, metadata only, an audit input; discussion in notes files the Auditor never opens) | maps | cited | brief 19 as quoted; 25 "recorded in the companion notes so it is not raised again". The brief's word "notes" is not carried into the filename, so the mandate's notes exclusion does not catch a file the brief makes the Auditor's input; the substance of the gives-statement is given whole. | -
  - Planner-added 2 (old-form philosophies read as ratified until Counsel moves their record) | maps (compatibility for the gives) | inferred | extends brief 18-19 and 26 ("three philosophies of his, two of them written with this plugin"); cheap to undo; no statement covers it | -
  - Planner-added 3 (engineering discussion's notes in `<stem>-notes.md` beside the philosophy, unread by the Auditor) | maps | inferred | extends brief 48 "the reply is kept verbatim in the discussion notes", where the engineering philosophy has no brief to sit beside; cheap to undo | -
  - Planner-added 4 (version 0.31.0 in three manifests) | maps (the text reaches a fresh repository, brief 14, only under a new version) | inferred | extends brief 14 "Someone opens the plugin in a repository that has never seen it ... without working around the harness"; manifests show 0.30.0 today; cheap to undo | -
  - Non-goal: relay acknowledgement contract | maps | cited | brief 77 "A relay acknowledgement contract, as the report suggested." | -
  - Non-goal: a named route for the outside view | maps | cited | brief 78 "A named route for the outside-model view." | -
  - Non-goal: any change to trivial work | maps | cited | brief 79 "Any change to what counts as trivial work." | -
  - Non-goal: the fixed dispatch template | maps | cited | brief 58 "This brief changes the forms in the value-documents skill, the Counsel skill, the setup procedure and the Orchestrator's run-side text." (the template is not among them) | -
  - Non-goal: the Auditor's grades | maps | cited | brief 58 as quoted | -
  - Non-goal: goal mode | maps | cited | brief 58 as quoted | -
  - Non-goal: rewriting existing philosophies of other repositories | maps | cited | brief 58 as quoted; brief 18-19 change forms, not any document, and only the owner changes a philosophy (value-documents, Changed by) | -
  - A1 (a stack by name = the owner naming the stack or its pull requests; covers each PR in it) | maps | cited | brief 30 "The owner's acceptance of a stack by name" | -
  - A2 ("nowhere else" excludes runtime memory and other files; a direct in-session statement still admits for that session and is recorded in the rule file to outlast it) | maps | inferred | extends brief 39 "a note the Orchestrator keeps for itself is not a place the harness reads"; cheap to undo. Caution for the Orchestrator (not a grade): a rule-file entry written on a session statement is in effect only when the quoted words accept the entry as it stands (mandate, Standing approval); a bare "accept Counsel's relays" said in session may not. | -
  - A3 (identity convention `<repository>-counsel`; the owner's yes may correct the name) | maps | inferred | extends brief 35 "names the convention" and 39; cheap to undo | -
  - Task_1 (revise ADR-D-0035 and -0038 wording; admission test and proposed merge record; each returns by name; Wave 2 waits) | maps | cited | brief 58 as quoted; 48 (outside view); 30 (merge). Not outward-facing; record acceptance is the owner's by name and is carried by relay under SA-2 (records are carried; plan approval is not). | -
  - Task_2 (forms, two references, Counsel skill, Counsel adapters, matrix) | maps | cited | brief 18-19, 24-26, 34-35, 43, 48, 52-53 as quoted | -
  - Task_3 (setup, templates, companion as audit input, merge at closeout, adapters, version) | maps | cited | brief 19, 30, 39, 43 as quoted; the version part is graded under Planner-added 4 | -
  - Task_4 (this repository's Counsel line and merge rule; scenarios 1 and part of 2 on a fixture, logged) | maps | cited | brief 30, 39, 43, 65-66 (scenarios 1 and 2), 72 as quoted. The merge rule in orchestrator.md is loosened from per-pull-request to per-stack exactly as brief 30 asks; the owner accepts the merge record by name before Wave 2. | -
  - Task_5 (closeout audit; reported ready; privacy sweep; nothing merged) | maps | cited | SA-1 quoted; brief 59, 72 | -
  - Decision Log 1 (no hook; Counsel claims the seat following the first-session reference once per repository) | maps | cited | brief 43 "The first-session reference holds the one-time procedure: take the seat, offer setup if it has not run, have the standing approval recorded." Departure from the means at brief 44 ("Where a runtime offers a session-start hook, the plugin's adapter for that runtime claims Counsel's seat from the hook, at no token cost"): the seat is claimed by Counsel in every runtime; graded on the gives-statement it serves. | -
  - Decision Log 2 (companion named and metadata-only; notes beside the engineering philosophy; old form accepted) | maps | cited | brief 19, 25 as quoted (the extensions it bundles are graded under Planner-added 2 and 3) | -
  - Decision Log 3 (plan review applied: Task_2 scoped; readings comparison kept; partial scenario 2 on fixture; merge record's acceptance states the admission path; version bump planner-added; reported ready not closed) | maps | cited | brief 72 and 58 as quoted; brief 30 and SA-1 for reported ready without a merge | -

  - `Human-only conditions pending: "scenarios 2 and 3 in his next real use; whether the reference improved a philosophy's quality without shaping the discussion."`
  - `Scenarios: none`
  Notes for the Orchestrator (not grades):
  1. Planner-added 3 puts a notes file beside a philosophy, which has no fixed path. The mandate's exclusion mechanics are path-globbed to `docs/coding-agent/briefs/**/*-notes.md`; a philosophy-adjacent `-notes.md` elsewhere is excluded by the mandate's rule ("when ... a philosophy links to them") but not by the pathspec. Task_3's acceptance "still never opens a notes file" should be checked against that gap.
  2. Plan Context line 53 says ADR-D-0038's wording-only change is "confirmed by the audit". An audit grades; it confirms nothing. At closeout the changed-record test runs on the diff itself.
  3. A2's "recorded in the rule file to outlast it": see the caution on the item line.

  How the Orchestrator applied it: no item is `ask-now` and none is `ungraded`; nothing is marked `direction`. With the brief's ratification relayed by Counsel under the standing approval, the plan review closed with no finding open, and this verdict, the plan is authorized under the ratified brief; this records no approval by the owner. No item rests on a provisional statement. Inferred calls, as the verdict states them: Planner-added 2 (old-form philosophies read as ratified until moved), Planner-added 3 (the engineering discussion's notes beside the philosophy), Planner-added 4 (version 0.31.0), A2 (what "nowhere else" excludes), A3 (the identity convention). On the auditor's procedural disclosure the Orchestrator rules as in the earlier runs that the verdict counts: the plan and brief were opened in the same step as the lookup for the mandate, no notes or readings file before the grades. The comparison set two readings apart from grades in class only (Planner-added 1 and A1, cited where the Orchestrator read extends), corrected in the readings file with nothing to redo. The auditor's three notes are taken: the pathspec gap for a philosophy-adjacent notes file goes into Task_3's packet (the mandate's exclusion must catch `<stem>-notes.md` wherever a philosophy sits); the Context line's "confirmed by the audit" reads as `adr.md` has it, the closeout confirms a wording-only call; A2's caution on a session statement's entry is carried to Task_3's packet.

- 2026-10-07 Wave 1, Task_1: Worker report `done`, one YAML block, three files inside the task's `owns`. ADR-D-0035 revised in place (title, context, a Decision bullet with the brief's four terms, Why, two rejected alternatives, invariant, Not covered, Validation; file not renamed, slug still true): returns by name. ADR-D-0038 wording only: the merge example reads "the pull request or the stack" in Context and Decision bullet 4; everything else byte-identical. ADR-D-0057 proposed, admission test passed on all five conditions: the owner's acceptance of a stack by name authorizes the merge of the stack and each pull request in it, as his own statement or Counsel's admitted relay; the runtime's permission is his to grant once and no rule text stands in for it; a standing approval covers a merge only as ADR-D-0052 allows. Worker validation: package validator pass, smoke tests pass, `git diff --check` clean.
  - Orchestrator rulings on the Worker's questions: (1) the reason in ADR-D-0035's Why and its second rejected alternative (an engineering philosophy written by one model family alone carries that family's defaults unexamined) is the Orchestrator's wording from the packet, not the brief's; it goes to the owner marked as such with the record, for him to accept or replace. (2) Who accepts a stack where the owner is not the product owner is left as the record leaves it, in the records' term "the person directing the work", consistent with ADR-D-0051. (3) ADR-D-0040 and ADR-D-0051 keep "merge authorization" as not covered until ADR-D-0057 is accepted; a pointer is then a wording-only repair the Orchestrator makes.
- 2026-10-07 Delta re-review of Task_1 (Codex reviewer, at ccf615e): APPROVED, no finding open. ADR-D-0035 (revised) and ADR-D-0057 (proposed) go to the owner through Counsel for acceptance, each by its own name, with the Orchestrator's reason in ADR-D-0035 marked as such; ADR-D-0038 does not return. Wave 2 waits on his answer.
- 2026-10-07 Wave 2, Task_3: Worker report `done`, one YAML block, thirteen files inside the task's `owns`. The Orchestrator reads each pointed philosophy with its companion; the mandate names the companion an input, keeps every notes file unread wherever it sits (the exclude pathspec is now `**/*-notes.md`), and lists a philosophy without a ratification record under Missing inputs; setup detects a philosophy by its companion's record or the old form, and a new section has its report offer the relay-admission entry, written with the Counsel line on the owner's yes in the session, in `common.md` and nowhere else; the Counsel line's form and the template stub; the owner's acceptance of a stack by name authorizes the merge of each pull request in it, the runtime's permission his to grant once, stated in the carrier, at run closeout, in the status model, both adapters and stacked-prs; manifests at 0.31.0; README unchanged. Worker validation: package validator pass, smoke tests pass, `git diff --check` clean, template block byte-identical, adapter parity, the new pathspec tried in a scratch repository.
  - Judgement calls (Task_3): the Standing Approvals stub's wording in the template (the carrier's terms, plan approval excluded, the impersonation risk named); the offer made at bootstrap and at a targeted refresh when no Counsel line exists; the owner's yes as his own statement in the session unless relays are already admitted; the repository-wide notes exclusion.
  - Orchestrator rulings: the wide `**/*-notes.md` exclusion stays, since a philosophy may sit anywhere and the mandate's First Step has the auditor list names before reading, so a file that merely matches (a release-notes file, say) can be read by name as the mandate's rules on inputs allow; `pr-review-monitoring.md` reads consistently and is left; the stub's wording is confirmed, Task_4 writes this repository's line in that form.
- 2026-10-07 Wave 2, Task_2: Worker report `done`, one YAML block, seven files inside the task's `owns`. A philosophy is plain prose; the companion `<philosophy-stem>-companion.md` (provenance, one ratification record per version, gaps left out; not a notes file; read by Counsel, the Orchestrator and the auditor) and a philosophy's notes file beside it; the old form read as ratified until moved; dates the owner's local date; briefs unchanged. Counsel's skill: the two open-time lines and the before-setup clause; drafting without tags, ratification in the companion; the philosophy reference read only after a draft, as gaps, supplying no wording; the outside view as ADR-D-0035; the seat convention. New references `philosophy-reference.md` (479 words, a gap check with the brief's nine elements, the exclusions, the qualities, an invented example of an unnamed tool) and `first-session.md` (289 words). Counsel adapters and the capability matrix allow consulting a model of another family as consulting, not dispatch. Word count 3304 to 3482 at the Worker's hand-back, 3518 after the Orchestrator's one sentence below: the one-time procedure +3 net (two lines +40, the moved admission text -37); other additions +211 (outside view, reference pointer, companion and dates, before-setup, seat, the channel-history sentence). Worker validation: package validator pass, smoke tests pass, `git diff --check` clean, no text asks for a tag or record inside a philosophy, the example names no real project.
  - Judgement calls (Task_2): the notes file applies to either philosophy's discussion; `provisional` kept as a status, not a tag; the two lines placed after the open-time bullet; "Dispatch only the read-only Researcher" became "For facts, dispatch only…".
  - Orchestrator rulings: the Copilot adapter's agent list is left as it is, the no-route case covering a runtime so configured (Counsel says so and the owner decides); the notes file for either philosophy's discussion confirmed; the brief's constraint that Counsel reads the channel's history rather than trusting its inbox, and that no acknowledgement is asked, is added as one sentence to the peer-channel bullet by the Orchestrator (counted with the other additions).
- 2026-10-07 Wave 2 review (Codex reviewer, 28244ad..eb363d1): NEEDS_REVISION, one MAJOR (bootstrap-lifecycle.md read as forbidding any relay to start setup, where the brief restricts only the first request before relays are admitted; scoped to that) and one MINOR (the word-count entry omitted the Orchestrator's sentence; corrected above). Everything else passed: both sides agree on the companion, the Counsel line, the seat, the audit's inputs; the reference does not bind the document to the discussion's terms; adapter parity; privacy.- 2026-10-07 Wave 3, Task_4 (the Orchestrator's own): this repository's rule files written (d441db9): the Counsel line in `common.md` in the form `rules-files.md` gives, naming the identity the Standing Approvals entry of 2026-10-01 names; `orchestrator.md`'s merge rule reads as the new text has it. Then the fixture, in a temporary directory outside the repository, nothing of it committed.
- 2026-10-07 Fixture recipe (invented, naming no real project): a git repository `fresh-repo` holding `README.md`, `src/ledgerling.py` (a 25-line expense splitter), `docs/product/what-ledgerling-is-for.md` (the prose philosophy below) and `docs/product/what-ledgerling-is-for-companion.md` (the companion below); no rule files. The philosophy, verbatim:

  # What Ledgerling is for

  Ledgerling exists so that people who share a home never have to have the conversation about money twice. One of them types what was spent as it happens, and at the end of the month everyone sees one number each and nobody argues about the arithmetic.

  The person it serves is the housemate who hates asking. They would rather pay more than bring it up. Ledgerling succeeds when that person opens it, sees the balance, and the balance is simply right, with nothing to discuss. It fails when anyone has to reconstruct a month from memory, however pretty the output.

  Two principles carry it. Plain text wins over any database, because a ledger people can read without the tool is a ledger they trust; when speed and legibility conflict, legibility wins. One number per person wins over itemised fairness, because the point is to end the conversation, not to extend it; when exactness and simplicity conflict, the tool rounds and says so.

  It behaves like a quiet flatmate who writes everything on the fridge: never reminds, never nags, never hides a line. It aspires to settle a shared holiday as easily as a week of groceries, and until it can, it says plainly that it handles one household and one currency.

  It must not become a budgeting app, a bank connection, or a chat. It refuses notifications, because a reminder is the conversation it exists to avoid. It refuses categories beyond a free word, because taxonomy is where arguments start.

  You can see it working when a month closes with no message between housemates about money. The question every change is held to: does this make the money conversation shorter? When in doubt, leave it out.

  Left out on purpose: multiple currencies and recurring expenses, because both reintroduce the arithmetic the tool exists to hide.

  The companion, verbatim:

  # Companion: What Ledgerling is for

  ## Provenance

  The scene and the measure, the two principles and the refusals are the owner's own. The analogy to a quiet flatmate and the north-star question were proposed by Counsel and accepted.

  ## Ratification

  - Version 1, ratified by the owner on 2026-10-07: "Yes, this is what Ledgerling is for. Ratified."

  ## Gaps left out

  - The reference's "what it aspires to" beyond one household: left out on purpose; the owner said the tool stays at one household for now.

- 2026-10-07 Scenario 1 and the fixture part of scenario 2, step 1: setup. Dispatch (a fresh Claude Worker-type agent on Opus; the fixture's path and the plugin's path given as machine paths, redacted here): "You are the Orchestrator session of a fresh repository, asked by its owner directly: 'Run setup for this repository.' The repository is at [machine path redacted] (a git repository; work only inside it; commit nothing). The harness you follow is the plugin at [machine path redacted] (read its skills by path; this is the version installed for this repository). Run the rulebook's full bootstrap as `skills/rulebook/SKILL.md` and its `references/bootstrap-lifecycle.md`, `rules-files.md` and `rule-suite-templates.md` state, with `skills/value-documents/SKILL.md` for how a philosophy is found; the peer channel this repository uses names seats `<repository>-counsel` by convention. Write the rule files the bootstrap writes under the fresh repository's `docs/coding-agent/rules/`. Then give the owner the setup report the text asks for, exactly as the text has you give it, and stop there: do not assume any answer from the owner. Your final message is the setup report (the text you would show the owner), followed by one short section 'Files written' listing the paths relative to the fresh repository and the full text of its `common.md`. Use no path of the machine in the report itself." Reply, verbatim:

  ## Setup report

  Setup is done. I wrote the repository's rules under `docs/coding-agent/rules/` and committed nothing.

  **Product philosophy:** recorded as `docs/product/what-ledgerling-is-for.md`. It is the only document in the repository that says what Ledgerling is for. Its companion beside it records your ratification on 2026-10-07, so I recorded it without asking. From now on, work here is held to it. If it isn't your product philosophy, say so and I'll remove the line.

  **Engineering philosophy:** none yet. Once one exists, work here is held to how you want the project to look. To start one, open a Counsel session.

  **Decision records:** the repository has no convention for them yet, and I haven't written a line for this. Two options:
  - **Yes:** I add the harness's ADR template and README under `docs/decisions/`, and `common.md` points there.
  - **No:** `common.md` records that there's no repository convention and the harness's default template applies.

  Do you want them placed?

  **Admitting Counsel's relays (an offer, nothing is missing):** you can let Counsel bring your decisions to this session, so you don't have to type them here yourself. The seat is named by convention; tell me if you want a different name. If you accept, I'll add this under a new Standing Approvals section in `common.md`:

  > - Relays from Counsel: a relay from `fresh-repo-counsel` on the peer channel that quotes the owner carries the owner's decisions to an Orchestrator session in this repository, on the terms of the `orchestration-harness` value-level operation reference (The Carrier); plan approval and its waiver are not carried. A message's sender cannot be verified, and the owner accepts that risk with this entry. Given and accepted by <you> on <date>: "<your words>".

  In the same change I'd add this line under Repository Reference Documents:

  > - Counsel: fresh-repo-counsel on the peer channel; relays admitted (Standing Approvals).

  Do you accept this entry as written, with this seat name? Until you say yes, neither line is written.

  ## Files written

  - `docs/coding-agent/rules/common.md`
  - `docs/coding-agent/rules/worker.md`
  - `docs/coding-agent/rules/orchestrator.md`
  - `docs/coding-agent/rules/reviewer.md`
  - `docs/coding-agent/rules/_lifecycle.json`
  - `docs/coding-agent/rules/index.md` (written last, as the marker that setup succeeded)

  Full text of `common.md`:

  ```md
  ---
  rule_schema_version: 2
  suite_id: "rules-20261007-1"
  rule_file: "common"
  last_updated: "2026-10-07"
  ---

  # Common Repository Rules

  ## Repository Reference Documents

  - Product philosophy: docs/product/what-ledgerling-is-for.md
  - Engineering philosophy: none yet. Once it exists, work here is held to how the owner wants the project to look. To start one, open a Counsel session.

  ## Repository-Specific Validation Commands

  - None recorded yet.

  ## Repo Safety / Boundaries

  - None recorded yet.

  ## Repo Naming / Structure

  - None recorded yet.
  ```

  Notes for the Orchestrator (not part of the owner report):
  - **No Decision Records line yet:** each of the three allowed outcomes needs either a detected convention or the owner's yes or no on placement, so I left it out until he answers.
  - **Seat name:** the repository has no git remote, so I took `<repository>` from its folder name, `fresh-repo`.
  - **Report format:** I followed your requested final-message format instead of the Worker YAML contract.

- 2026-10-07 Step 2: the owner's answers, sent to the same agent as the fixture's owner: "The owner, in this session, 2026-10-07: 'No, don't place the ADR template; record that the harness default applies. And yes, I accept the Standing Approvals entry as written, with the seat name fresh-repo-counsel.' Act on both as the text has you act, then reply with the full text of common.md as it now stands and one line on what you wrote where. Commit nothing." Reply, verbatim:

  I've made both changes in `docs/coding-agent/rules/common.md` and committed nothing. Under Repository Reference Documents I added the harness-default Decision records line, since you declined the template, and the Counsel line. I also added a new Standing Approvals section with the entry, quoting your acceptance and dated 2026-10-07. Finally, in `docs/coding-agent/rules/_lifecycle.json` I updated the evidence note so it says ADR placement was declined.

  The entry doesn't admit Counsel's relays until it is committed. Until then, I won't act on any relay from `fresh-repo-counsel`.

  Two things to check in the entry:
  - **Who accepted:** I wrote "the owner" because I don't know your name. Tell me your name if you want it there instead.
  - **Your quote:** I quoted only the part of your message that accepts the entry, starting at "yes".

  `common.md` as it now stands:

  ```md
  ---
  rule_schema_version: 2
  suite_id: "rules-20261007-1"
  rule_file: "common"
  last_updated: "2026-10-07"
  ---

  # Common Repository Rules

  ## Repository Reference Documents

  - Product philosophy: docs/product/what-ledgerling-is-for.md
  - Engineering philosophy: none yet. Once it exists, work here is held to how the owner wants the project to look. To start one, open a Counsel session.
  - Decision records: no repo convention — harness default template applies (durable-docs-authoring references/adr.md).
  - Counsel: fresh-repo-counsel on the peer channel; relays admitted (Standing Approvals).

  ## Repository-Specific Validation Commands

  - None recorded yet.

  ## Repo Safety / Boundaries

  - None recorded yet.

  ## Repo Naming / Structure

  - None recorded yet.

  ## Standing Approvals

  - Relays from Counsel: a relay from `fresh-repo-counsel` on the peer channel that quotes the owner carries the owner's decisions to an Orchestrator session in this repository, on the terms of the `orchestration-harness` value-level operation reference (The Carrier); plan approval and its waiver are not carried. A message's sender cannot be verified, and the owner accepts that risk with this entry. Given and accepted by the owner on 2026-10-07: "yes, I accept the Standing Approvals entry as written, with the seat name fresh-repo-counsel."
  ```

  The fixture's rule files were then committed in the fixture repository so that the entry is in effect.
- 2026-10-07 Step 3: a fresh Counsel session opens. Dispatch (a fresh agent on Opus): "You are a Counsel session that the owner has just opened in the repository at [machine path redacted] (work only inside it; write nothing; the owner has said nothing yet beyond opening the session). Your skill is [machine path redacted]/skills/counsel/SKILL.md and its references (read the skill by path; follow only what it has you do at open). Do exactly what the skill's open-time steps say for this repository and nothing more; the peer channel of this repository is assumed present with seats named by the convention the skill states, and you need not actually take a seat, only say whether the skill sends you to do so. Your final message: (1) the files you read, in order, with the reason the skill gave for each; (2) what you found in the Repository Reference Documents section and what the skill then had you do; (3) whether you read `references/first-session.md` or `references/philosophy-reference.md` at open, and why or why not; (4) the greeting or opening words you would say to the owner, if the skill has you say anything. Use no machine path in the message." Reply, verbatim:

  task_id: Task_counsel_open_fresh_repo
  status: done
  summary: |
    I followed the counsel skill's open-time steps in the fresh repository. I read two files and wrote nothing.
    The Repository Reference Documents section exists, so setup has run. It lists a product philosophy, says the engineering philosophy is "none yet", and has the Counsel line ("fresh-repo-counsel on the peer channel; relays admitted").
    Because the Counsel line is there, the skill says "nothing more": I did not read first-session.md, and I read philosophy-reference.md only after a draft exists.
    The skill says the owner speaks first, so I say nothing at open. My first reply will mention once that there is no engineering philosophy yet and offer to start one.
    Risk profile: low (a read-only role check). Validation depth: targeted.
  files_changed: []
  commands_run:
    - command: "list files in the fresh repository (excluding .git)"
      result: pass
      note: "Found the rules files, the product philosophy and its companion, README, src/ledgerling.py. Used only to find files; not a skill step."
  validation_results:
    - name: "open-time steps of the counsel skill followed exactly, nothing written"
      kind: manual
      required: true
      owner: worker
      status: pass
      evidence: "I read only the skill and common.md, edited nothing, took no seat and sent no message."
  tests: "None; read-only behavioural check."
  answers:
    q1_files_read_in_order:
      - file: "the counsel skill's SKILL.md"
        reason: "The task assigned it as my skill; it defines Counsel's conduct and what to do at open."
      - file: "docs/coding-agent/rules/common.md"
        reason: "The skill says: 'When the session opens, read the \"Repository Reference Documents\" section of docs/coding-agent/rules/common.md; reading it is not editing it.'"
    q2_reference_documents_section:
      found:
        - "Product philosophy: docs/product/what-ledgerling-is-for.md"
        - "Engineering philosophy: none yet. To start one, open a Counsel session."
        - "Decision records: no repo convention; the harness default template applies."
        - "Counsel: fresh-repo-counsel on the peer channel; relays admitted (Standing Approvals). This matches a Standing Approvals entry the owner accepted on 2026-10-07."
      what_the_skill_had_me_do:
        - "The section exists, so setup has run. I do not say setup is missing and do not offer it."
        - "The engineering philosophy is listed as none yet. The skill says to mention it once, in my first reply, and offer to start on one, then not raise it again this session if the owner does not take it up. No document is listed as waiting for the owner to say whether it is the philosophy, so I mention nothing about that."
        - "The Counsel line is there, so the skill says 'nothing more'. No first-session step runs."
        - "Peer seat: no open-time step sends me to take a seat. The skill only says messages travel with Counsel on its own seat, named <repository>-counsel by convention (here fresh-repo-counsel), and that I read the channel's history instead of trusting my inbox only while the channel is broken. Reading the discussion notes at open applies only when there is no peer channel, and this repository has one, so I did not read them."
        - "I did not open the product philosophy, its companion, or the value-documents skill. The skill sends me to value-documents only before I draft, change, locate or hand over a value document, and none of that happens at open."
    q3_first_session_and_philosophy_reference:
      first_session_md: "Not read. The skill sends me to it only when the Counsel line is missing from the section, and here it is present."
      philosophy_reference_md: "Not read. The skill allows it only after a discussion has produced a philosophy draft ('never during it'). No draft exists at open."
    q4_opening_words:
      at_open: "Nothing. 'The owner speaks first, and Counsel restates it so the owner can check it.' The owner has not spoken yet, so I make no greeting and wait."
      first_reply_once_owner_speaks: |
        [A restatement of what the owner said, for the owner to check, put as person -> does -> experiences -> gains.]
        One thing to mention once: this project has a product philosophy ("what ledgerling is for") but no engineering philosophy yet. An engineering philosophy would set how you want the project to look to whoever works on it later, and work here would be held to it. If you'd like, we can work one out in conversation, for as long as that takes. If not, I won't bring it up again.
  blockers: []
  questions_for_orchestrator: []
  assumptions:
    - "Out-of-scope docs: the product philosophy, its companion, the value-documents skill and both counsel references. The skill gives no reason to open any of them at open."
    - "'Seats named by the convention the skill states' means fresh-repo-counsel, which matches the Counsel line in common.md."
    - "Residual risk: the skill gives no explicit open-time step for taking the peer seat, so whether Counsel should take its seat when the session opens is unspecified."
  rule_candidates: []
  ```

- 2026-10-07 Step 4: the Orchestrator reads the value documents. Dispatch (a fresh agent on Opus): "You are the Orchestrator session of the repository at [machine path redacted] (work only inside it; write nothing). The owner has asked for a small piece of work and no brief governs it. Before planning, do what [machine path redacted]/skills/orchestration-harness/SKILL.md Repository Rule Entry and `references/value-level-operation.md` (Documents) have you do about value documents in this repository, reading `skills/value-documents/SKILL.md` where the reference sends you; stop before any planning. Your final message: (1) whether value-level operation is on for this run and why; (2) each value document you read, where you found its ratification, and whether it is ratified (quote the record you relied on); (3) whether anything would be escalated or flagged as a missing ratification, and why or why not; (4) the files you read, in order. Use no machine path in the message." Reply, verbatim:

  task_id: Task_value_docs_entry
  status: done
  summary: >
    I ran Repository Rule Entry and the Documents step of the value-level operation reference for the fresh repository, and stopped before any planning. Value-level operation is on because common.md has a pointer to a product philosophy.
    I read that philosophy and its companion. It is ratified, and nothing needs escalating or flagging. Nothing was written.
    Risk profile: low (read-only). Validation depth: targeted.
  files_changed: []
  commands_run:
    - command: "list the files in the fresh repository, excluding .git"
      status: pass
      note: "Found the rule suite, docs/product/what-ledgerling-is-for.md with its companion, README.md and src/ledgerling.py. There is no briefs directory."
  validation_results:
    - kind: manual
      required: true
      owner: worker
      status: pass
      evidence: "I followed the reads in SKILL.md Repository Rule Entry and in value-level-operation.md Documents (plus value-documents/SKILL.md, where it sends you). The answers below come from the files quoted."
  tests: "None. The task only reads documents."
  blockers: []
  questions_for_orchestrator: []
  assumptions:
    - "This is a plan-mode run: the owner asked for a small piece of work and no goal envelope was mentioned."
    - "The owner directing this work is also Ledgerling's product owner. No file says otherwise, and the companion records the ratification as 'the owner'."
  findings:
    1_value_level_operation: >
      ON. common.md, under "Repository Reference Documents", has the pointer line
      "Product philosophy: docs/product/what-ledgerling-is-for.md". In plan mode, a pointer to a product or engineering
      philosophy turns value-level operation on even when no brief was handed over, and no brief was.
      The engineering line, "Engineering philosophy: none yet. ...", is not a pointer. It turns nothing on or off and
      is not mentioned to the person. With no brief, the run is audited against the product philosophy alone, so there is no Counsel carrier
      for value questions and the user is asked in this session (The Carrier, last paragraph). The Counsel line and the Standing
      Approvals relay entry in common.md are on record, but this run does not use them.
    2_value_documents_read:
      - document: "Product philosophy, docs/product/what-ledgerling-is-for.md"
        ratification_found_in: "its companion beside it, docs/product/what-ledgerling-is-for-companion.md, section Ratification"
        ratified: true
        record_relied_on: "Version 1, ratified by the owner on 2026-10-07: \"Yes, this is what Ledgerling is for. Ratified.\""
        note: >
          The philosophy itself carries no ratification record, which is the form the value-documents skill expects. The companion's
          Provenance says the flatmate analogy and the north-star question came from Counsel and were accepted. Ratification
          covers the whole philosophy, so those parts count on the Version 1 record.
      - document: "Engineering philosophy"
        ratification_found_in: "not applicable: there is no pointer ('none yet'), so I read no file and probed no path"
        ratified: "n/a"
    3_escalation_or_missing_ratification: >
      Nothing to escalate and no missing ratification. The one pointer names a file that exists and can be read, and its
      companion holds a ratification record quoting the owner with a date. No brief was handed over, so no brief ratification needs to
      reach the session, and nothing calls for asking for one. The engineering "none yet" line is not a pointer and the run
      does not raise it. One thing I noticed, which needs no action: the philosophy's line "It aspires to settle a shared holiday ..."
      sits slightly awkwardly beside the companion's "Gaps left out" entry, which leaves out any aspiration beyond one household. But
      Version 1 was ratified with that text, the philosophy also says it "handles one household and one currency", and the run never
      edits a philosophy or its companion. So I am not raising it as a question; at most it is a reading note for Counsel.
    4_files_read_in_order:
      - "orchestration-harness SKILL.md (Repository Rule Entry)"
      - "orchestration-harness references/value-level-operation.md"
      - "fresh repository: docs/coding-agent/rules/index.md"
      - "fresh repository: docs/coding-agent/rules/common.md"
      - "fresh repository: docs/coding-agent/rules/orchestrator.md"
      - "value-documents SKILL.md"
      - "fresh repository: docs/product/what-ledgerling-is-for.md"
      - "fresh repository: docs/product/what-ledgerling-is-for-companion.md"
    ordering_note: >
      The reference ended up being read before the repository's common.md, because the task told me to read both up front. By the rule's order,
      common.md decides whether the reference is read at all. It does turn value-level operation on here, so the outcome is the same.
  rule_candidates: []
  ```

- 2026-10-07 Step 5: one Auditor dispatch by the fixed template. The mandate reads `docs/coding-agent/rules/common.md` of the repository it runs in, so the fixture's philosophy and companion were copied into this repository's working tree under `docs/product/`, an invented brief (`ledgerling-fixture-brief.md`, ratified "Yes, do it.", product basis the philosophy) and plan (`ledgerling-fixture-plan.md`, one task on `src/ledgerling.py`) placed under `briefs/active/` and `plans/active/` untracked, with a readings file, and the product-philosophy pointer line of `common.md` set to `docs/product/what-ledgerling-is-for.md` in the working tree only; all of it removed and the pointer restored after the verdict, nothing committed. Dispatch text, verbatim: "You are the value auditor. Read references/value-audit-mandate.md of the orchestration-harness skill and follow it exactly. Position: plan draft. Plan: docs/coding-agent/plans/active/ledgerling-fixture-plan.md. Governing brief: docs/coding-agent/briefs/active/ledgerling-fixture-brief.md. Changes since: none." Verdict as returned (machine paths redacted):

  ## Value Audit: Settle rounds to whole units (plan draft)

  - Position: plan draft
  - Documents read: [machine path redacted] [machine path redacted] [machine path redacted] [machine path redacted] (claims under review); docs/coding-agent/rules/common.md at HEAD (Standing Approvals section and pointer lines) and its working-tree diff
  - Product basis: product philosophy (`docs/product/what-ledgerling-is-for.md`; ratification record in its companion: Version 1, owner, 2026-10-07, "Yes, this is what Ledgerling is for. Ratified.")
  - Not audited: engineering side, which has no document (pointer line reads "none yet")
  - Missing inputs: none
  - Value documents changed in range: none (no range at plan draft). Noted for the record: the product-philosophy pointer line in common.md is changed in the uncommitted working tree from "none yet" to `docs/product/what-ledgerling-is-for.md`; the philosophy, its companion and the governing brief are untracked, not yet committed. The brief carries its ratification record ("Yes, do it.", owner, 2026-10-07) and states its product basis.
  - DoD: `settle` prints whole numbers and one line saying the amounts are rounded | maps to the brief | cited | brief, gives: "When the month settles, each housemate sees one whole number, never cents." (told 2026-10-07: "Round to whole units and say so; nobody wants to owe 13.37."); philosophy: "when exactness and simplicity conflict, the tool rounds and says so." | -
  - DoD: the ledger file's format is unchanged | maps to the brief | cited | philosophy: "Plain text wins over any database, because a ledger people can read without the tool is a ledger they trust"; "When in doubt, leave it out." | -
  - Non-goal: add | maps to the brief | cited | brief, gives: "When the month settles, each housemate sees one whole number, never cents." (the brief asks for settle alone); philosophy: "When in doubt, leave it out." | -
  - Non-goal: the ledger format | maps to the brief | cited | philosophy: "Plain text wins over any database, because a ledger people can read without the tool is a ledger they trust"; "When in doubt, leave it out." | -
  - Non-goal: currencies | maps to the brief | cited | philosophy: "it says plainly that it handles one household and one currency"; "Left out on purpose: multiple currencies and recurring expenses, because both reintroduce the arithmetic the tool exists to hide." | -
  - A1: rounding is to the nearest whole unit, half up | maps to the brief | inferred | extends brief "Round to whole units and say so" and philosophy "the tool rounds and says so"; no statement names a rounding rule; cheap to undo | -
  - Task_1: Round the settle output | maps to the brief | cited | brief, gives: "When the month settles, each housemate sees one whole number, never cents."; philosophy: "the tool rounds and says so." | -
  - Decision Log: no entries, no items.
  - Human-only conditions pending: "Human-only: the owner's next month-end."
  - Scenarios: none
  - Reading compared: DoD 1: agrees (covered / cited). DoD 2 (ledger format unchanged): unread. Non-goal add: unread. Non-goal ledger format: unread. Non-goal currencies: unread. A1: agrees (extends / inferred). Task_1: unread.
  - Findings compared: none found (readings file records "None yet")

  No `ask-now` items: the brief and the philosophy decide every item on the audited side. No item is irreversible or outward-facing; no standing approval was relied on.

  Remark outside the record (not a grade): the plan's owns path `src/ledgerling.py` does not exist in this repository (no `ledgerling*` file outside docs/). If this is intended as a fixture exercise that is fine; otherwise the Plan Gate's own checks should catch it.

- 2026-10-07 Task_4 outcome, the Orchestrator's reading: scenario 1 shown (setup found the companion's record and recorded the pointer without asking; offered the relay-admission entry as an offer with the seat `fresh-repo-counsel` by convention; wrote nothing until the yes; on the yes wrote the entry with the quoted words and date and the Counsel line in one change; a fresh Counsel session found the line and did nothing more, reading neither reference). The fixture part of scenario 2 shown (the Orchestrator's Documents step and the Auditor each read the companion's record as the ratification, with no missing-ratification flag; the Auditor's `Missing inputs: none`). Not shown and the owner's to judge: the discussion itself and whether the reference improves a philosophy without shaping the discussion (scenario 2's human-only part), scenario 3 (a real merge on his acceptance), scenario 4. Two things noticed, carried to the owner as observations: with the Counsel line present the skill has no open-time step for sitting on the seat in a later session (the brief's "nothing more"); setup took `<repository>` from the folder name where the repository has no remote. The review of the branch follows.
- 2026-10-07 Final review of the branch (Codex reviewer, 8b36645..2a5ff5d): NEEDS_REVISION, one MAJOR: the Auditor fixture step's invented brief and plan were described but not retained, so the case that returned `Missing inputs: none` could not be inspected. Recovered exactly from the session's own record of the command that wrote them (not reconstructed from the verdict) and retained here as fixture inputs. Everything else passed: the rule files, the logged replies, the records, validators, template block, adapter parity, the privacy sweep over all fourteen commits with no other repository's name found.
- 2026-10-07 Fixture inputs for step 5, verbatim as written to the working tree. Seed tracking state: in the fixture repository of steps 1 to 4, `README.md`, `src/ledgerling.py`, the philosophy and the companion were committed (tracked) before setup ran, and setup discovered the philosophy among tracked paths; in this repository's working tree for step 5 the philosophy, the companion, the brief, the plan and the readings file were untracked and the pointer line was changed in the working tree only, which the Auditor noted in its record. The brief, `docs/coding-agent/briefs/active/ledgerling-fixture-brief.md`:

  ```md
    # Brief: Settle rounds to whole units

    - status: ratified by the owner on 2026-10-07 ("Yes, do it.")
    - drafted by: Counsel, from discussion with the owner on 2026-10-07
    - handed to: the Orchestrator on 2026-10-07
    - product basis: the product philosophy, `docs/product/what-ledgerling-is-for.md`
    - kind marks: **gives** (binds), **constraint** (fixed), **means** (does not bind).

    ## Who it is for and why

    - When the month settles, each housemate sees one whole number, never cents. **gives** *(told 2026-10-07: "Round to whole units and say so; nobody wants to owe 13.37.")*

    ## Core scenario

    1. A housemate runs settle and sees whole numbers with a line saying the amounts are rounded.

    ## Pass conditions

    - Agent-checkable: settle prints whole numbers and a rounding line.
    - Human-only: the owner's next month-end.
  ```

  The plan, `docs/coding-agent/plans/active/ledgerling-fixture-plan.md`:

  ```md
    # Plan: Settle rounds to whole units

    - status: draft
    - generated: 2026-10-07
    - last_updated: 2026-10-07
    - work_type: impl

    ## Goal
    - Settle prints each balance as a whole number and says the amounts are rounded, as `docs/coding-agent/briefs/active/ledgerling-fixture-brief.md` states.

    ## Definition of Done
    - `settle` prints whole numbers and one line saying the amounts are rounded.
    - The ledger file's format is unchanged.

    ## Planner-added requirements
    - None

    ## Scope / Non-goals
    - Scope: `src/ledgerling.py`, settle only.
    - Non-goals: add; the ledger format; currencies.

    ## Design
    - Proportional form: one function changes its output format; no responsibility, contract or state is touched.

    ## Compatibility stance (required if a contract/interface/persisted format is touched)
    - surface: none touched
    - stance: preserve
    - justification: the ledger file is unchanged.

    ## Context (workspace)
    - Governing brief: `docs/coding-agent/briefs/active/ledgerling-fixture-brief.md`, ratified 2026-10-07 ("Yes, do it.").
    - Run record: none yet. Readings file: `docs/coding-agent/plans/active/ledgerling-fixture-readings.md`.

    ## Open Questions (max 3)
    - None.

    ## Assumptions
    - A1: rounding is to the nearest whole unit, half up. source: a reading of "whole units".

    ## Tasks

    ### Task_1: Round the settle output
    - type: impl
    - owns:
      - src/ledgerling.py
    - depends_on: []
    - description: |
      Settle rounds each balance to a whole number and prints one line saying so.
    - acceptance:
      - Balances print as whole numbers.
      - One line says the amounts are rounded.
    - validation:
      - kind: command
        required: true
        owner: worker
        detail: "python src/ledgerling.py settle on a sample ledger"
      - kind: review
        required: true
        owner: reviewer
        detail: "Diff review against the brief"

    ## Task Waves (explicit parallel dispatch sets)
    - Wave 1: Task_1

    ## Rollback / Safety
    - Revert the commit.

    ## Progress Log (append-only)
    - 2026-10-07 Drafted.

    ## Decision Log
    - None.
  ```

  The readings file, `docs/coding-agent/plans/active/ledgerling-fixture-readings.md`, held two reading lines for the audit to compare after grading (DoD 1 covered by the brief's whole-numbers statement; A1 extending "whole units") and a `Findings` section reading "None yet."; it is not reproduced here so that no readings text sits in a plan. The philosophy and the companion are those logged above.

## Decision Log
- 2026-10-07 The hook means is not taken: the plugin has no hook mechanism and names no channel tool, so an adapter hook would bind it to one channel and fire in every session of that runtime; Counsel claims its seat following the first-session reference, once per repository. Recorded as a finding in the readings file (trivial: it changes nothing the owner experiences beyond one claim).
- 2026-10-07 The companion is named `<philosophy-stem>-companion.md`, metadata only, an input to the audit; discussion stays in notes files the Auditor never opens, the engineering philosophy's beside it as `<philosophy-stem>-notes.md`; old-form philosophies are read as ratified until Counsel moves their record. (First drafted as a `-notes.md` companion carved out of the exclusion; the plan review found that one file cannot be an input to one reader and forbidden to another.)
- 2026-10-07 Plan review applied: Task_2's acceptance scoped to the forms and Counsel's side, the readers being Task_3's; the readings file's post-grading comparison kept; the fixture carries the part of scenario 2 it can (a prose philosophy with a companion record found and read as ratified); the merge record's acceptance states the admission path, not the record's contents; the version bump listed as planner-added with its reason; the run is reported ready, not closed.
- 2026-10-07 Proposal, ADR-D-0057 (proposed, awaiting the owner's acceptance by name): "Acceptance of a stack by name authorizes the Orchestrator to merge it." Decision: the owner's acceptance of a stack by name, as his own statement or Counsel's admitted relay, authorizes the merge of that stack and each pull request in it; the runtime's merge permission is his to grant once in the session and no rule text stands in for it. Constraint on future work: no rule asks a merge instruction per pull request, and none claims to grant the runtime's permission. Why: the stack is the unit he judges, so his acceptance by name is the merge decision, and the permission layer is the runtime's.
- 2026-10-07 Proposal, ADR-D-0035 revised (accepted record, revision awaiting acceptance by name): for the engineering discussion Counsel obtains a view from a model of another family by whatever route the environment provides, says the route, puts the question as the discussion put it, keeps the reply verbatim with model and route named, and where no route exists says so and the owner decides. Constraint: the harness names no route. Why: the brief's; the harness must serve many environments and model families. The second reason the record gives (one family's defaults unexamined) is the Orchestrator's wording, marked for the owner.
- 2026-10-07 Review of Task_1 (Codex reviewer): NEEDS_REVISION, one MAJOR (ADR-D-0035 read as already accepted in its new terms; a header now says the revision awaits acceptance by name and the terms of 2026-10-01 stand until then) and one MINOR (the two proposals were not in the Decision Log; the entries above). The reviewer's ruling on the Orchestrator's reason: go to the owner as marked.
- 2026-10-07 The owner's answers, relayed by Counsel (admitted by the standing approval of 2026-10-01). On ADR-D-0035, quoted in full: "I accept the revision to ADR-D-0035." The text before him was the file at be9a03e, the Orchestrator's reason included, offered for cutting and accepted as it stands; the pending header is removed and the record stands accepted in its revised terms. On ADR-D-0057, not accepted, his words quoted in full: "For the new ADR, I want to ask this question: 'What does this decision affect in how the harness is built?' because I kind of feel that this doesn't carry enough weight." The Orchestrator's answer: it constrains only the workflow text on merging (that the Orchestrator asks no instruction per pull request once a stack is accepted by name, and that no rule claims the runtime's permission), a miss a reviewer would catch on the next diff; the reasoning that the stack is the unit he judges is already ADR-D-0051's, and that a relay carries his word is ADR-D-0038's. So the draft fails the admission test's first two conditions on his question and is withdrawn (a dropped draft frees its number); the behaviour lives in the text Task_3 and Task_4 write, and ADR-D-0051 keeps merge authorization as not covered by a record. The first ADR-D-0057 of this stack was withdrawn on the same ground; the number is twice unused.
