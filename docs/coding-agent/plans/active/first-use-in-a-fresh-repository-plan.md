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
- 2026-10-07 Wave 2, Task_2: Worker report `done`, one YAML block, seven files inside the task's `owns`. A philosophy is plain prose; the companion `<philosophy-stem>-companion.md` (provenance, one ratification record per version, gaps left out; not a notes file; read by Counsel, the Orchestrator and the auditor) and a philosophy's notes file beside it; the old form read as ratified until moved; dates the owner's local date; briefs unchanged. Counsel's skill: the two open-time lines and the before-setup clause; drafting without tags, ratification in the companion; the philosophy reference read only after a draft, as gaps, supplying no wording; the outside view as ADR-D-0035; the seat convention. New references `philosophy-reference.md` (479 words, a gap check with the brief's nine elements, the exclusions, the qualities, an invented example of an unnamed tool) and `first-session.md` (289 words). Counsel adapters and the capability matrix allow consulting a model of another family as consulting, not dispatch. Word count 3304 to 3482: the one-time procedure +3 net (two lines +40, the moved admission text -37); other additions +175 (outside view, reference pointer, companion and dates, before-setup, seat). Worker validation: package validator pass, smoke tests pass, `git diff --check` clean, no text asks for a tag or record inside a philosophy, the example names no real project.
  - Judgement calls (Task_2): the notes file applies to either philosophy's discussion; `provisional` kept as a status, not a tag; the two lines placed after the open-time bullet; "Dispatch only the read-only Researcher" became "For facts, dispatch only…".
  - Orchestrator rulings: the Copilot adapter's agent list is left as it is, the no-route case covering a runtime so configured (Counsel says so and the owner decides); the notes file for either philosophy's discussion confirmed; the brief's constraint that Counsel reads the channel's history rather than trusting its inbox, and that no acknowledgement is asked, is added as one sentence to the peer-channel bullet by the Orchestrator (counted with the other additions).
## Decision Log
- 2026-10-07 The hook means is not taken: the plugin has no hook mechanism and names no channel tool, so an adapter hook would bind it to one channel and fire in every session of that runtime; Counsel claims its seat following the first-session reference, once per repository. Recorded as a finding in the readings file (trivial: it changes nothing the owner experiences beyond one claim).
- 2026-10-07 The companion is named `<philosophy-stem>-companion.md`, metadata only, an input to the audit; discussion stays in notes files the Auditor never opens, the engineering philosophy's beside it as `<philosophy-stem>-notes.md`; old-form philosophies are read as ratified until Counsel moves their record. (First drafted as a `-notes.md` companion carved out of the exclusion; the plan review found that one file cannot be an input to one reader and forbidden to another.)
- 2026-10-07 Plan review applied: Task_2's acceptance scoped to the forms and Counsel's side, the readers being Task_3's; the readings file's post-grading comparison kept; the fixture carries the part of scenario 2 it can (a prose philosophy with a companion record found and read as ratified); the merge record's acceptance states the admission path, not the record's contents; the version bump listed as planner-added with its reason; the run is reported ready, not closed.
- 2026-10-07 Proposal, ADR-D-0057 (proposed, awaiting the owner's acceptance by name): "Acceptance of a stack by name authorizes the Orchestrator to merge it." Decision: the owner's acceptance of a stack by name, as his own statement or Counsel's admitted relay, authorizes the merge of that stack and each pull request in it; the runtime's merge permission is his to grant once in the session and no rule text stands in for it. Constraint on future work: no rule asks a merge instruction per pull request, and none claims to grant the runtime's permission. Why: the stack is the unit he judges, so his acceptance by name is the merge decision, and the permission layer is the runtime's.
- 2026-10-07 Proposal, ADR-D-0035 revised (accepted record, revision awaiting acceptance by name): for the engineering discussion Counsel obtains a view from a model of another family by whatever route the environment provides, says the route, puts the question as the discussion put it, keeps the reply verbatim with model and route named, and where no route exists says so and the owner decides. Constraint: the harness names no route. Why: the brief's; the harness must serve many environments and model families. The second reason the record gives (one family's defaults unexamined) is the Orchestrator's wording, marked for the owner.
- 2026-10-07 Review of Task_1 (Codex reviewer): NEEDS_REVISION, one MAJOR (ADR-D-0035 read as already accepted in its new terms; a header now says the revision awaits acceptance by name and the terms of 2026-10-01 stand until then) and one MINOR (the two proposals were not in the Decision Log; the entries above). The reviewer's ruling on the Orchestrator's reason: go to the owner as marked.
- 2026-10-07 The owner's answers, relayed by Counsel (admitted by the standing approval of 2026-10-01). On ADR-D-0035, quoted in full: "I accept the revision to ADR-D-0035." The text before him was the file at be9a03e, the Orchestrator's reason included, offered for cutting and accepted as it stands; the pending header is removed and the record stands accepted in its revised terms. On ADR-D-0057, not accepted, his words quoted in full: "For the new ADR, I want to ask this question: 'What does this decision affect in how the harness is built?' because I kind of feel that this doesn't carry enough weight." The Orchestrator's answer: it constrains only the workflow text on merging (that the Orchestrator asks no instruction per pull request once a stack is accepted by name, and that no rule claims the runtime's permission), a miss a reviewer would catch on the next diff; the reasoning that the stack is the unit he judges is already ADR-D-0051's, and that a relay carries his word is ADR-D-0038's. So the draft fails the admission test's first two conditions on his question and is withdrawn (a dropped draft frees its number); the behaviour lives in the text Task_3 and Task_4 write, and ADR-D-0051 keeps merge authorization as not covered by a record. The first ADR-D-0057 of this stack was withdrawn on the same ground; the number is twice unused.
