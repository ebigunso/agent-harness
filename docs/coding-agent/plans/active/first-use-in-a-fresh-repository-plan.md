# Plan: First use in a fresh repository

- status: draft
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

## Decision Log
- 2026-10-07 The hook means is not taken: the plugin has no hook mechanism and names no channel tool, so an adapter hook would bind it to one channel and fire in every session of that runtime; Counsel claims its seat following the first-session reference, once per repository. Recorded as a finding in the readings file (trivial: it changes nothing the owner experiences beyond one claim).
- 2026-10-07 The companion is named `<philosophy-stem>-companion.md`, metadata only, an input to the audit; discussion stays in notes files the Auditor never opens, the engineering philosophy's beside it as `<philosophy-stem>-notes.md`; old-form philosophies are read as ratified until Counsel moves their record. (First drafted as a `-notes.md` companion carved out of the exclusion; the plan review found that one file cannot be an input to one reader and forbidden to another.)
- 2026-10-07 Plan review applied: Task_2's acceptance scoped to the forms and Counsel's side, the readers being Task_3's; the readings file's post-grading comparison kept; the fixture carries the part of scenario 2 it can (a prose philosophy with a companion record found and read as ratified); the merge record's acceptance states the admission path, not the record's contents; the version bump listed as planner-added with its reason; the run is reported ready, not closed.
