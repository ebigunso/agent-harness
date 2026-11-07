# Plan: A goal run under a brief, authorized and graded on the brief

- status: in progress
- generated: 2026-11-07
- last_updated: 2026-11-07
- work_type: docs

## Goal
- The harness gives what the governing brief `docs/coding-agent/briefs/active/quiet-orchestrator-session-brief.md` states in its entries of 2026-11-07 under Directed during the run:
  - under a brief, a goal-mode run starts without the owner's agreement, through Counsel or anywhere;
  - its envelope is authorized as a plan under a brief is;
  - the value audit grades the whole goal run under a brief against the brief;
  - a finding the run can remediate without any further decision is handled by the run, without stopping the loop or reaching the owner;
  - every record names the thing it means and not its position ("the second source");
  - wording is chosen so that its meaning does not change when something else changes.
- The brief is the requirement and is not restated here. Where this plan and the brief differ, the brief governs and the difference is a plan defect.
- This is the third unit of the run recorded in `docs/coding-agent/plans/active/quiet-orchestrator-session-run.md`, on top of pull request 93's branch.

## Definition of Done
- Under a brief, a goal envelope is authorized by the brief route on a plan's conditions, and no one is asked:
  - the Reviewer's pass covers the goal condition and every clause of the recorded envelope, and is closed with no finding open;
  - a plan-draft value audit dispatched after that pass grades the envelope against the brief and holds nothing;
  - the three moves apply when the route does not authorize;
  - a changed envelope goes back through the route, as a changed plan does.
- The goal-mode texts say so: `goal-mode.md` Authority Envelope and Value Audit, `value-level-operation.md` (opening paragraph, Goal-Mode Runs, The Carrier's list of consent gates), `lifecycle-gates.md` Plan Gate Details, `SKILL.md` (Repository Rule Entry and Plan Gate), `goal-condition-checklist.md`, `goal-templates.md`. A stop of the loop under a brief still goes by the Carrier.
- Under a brief, the value audit grades the whole goal run against the brief, in a repository with no philosophy as well: the envelope before the loop starts, the run at each assessment event, and the completion report. The mandate's goal-run fill-ins name the governing brief under a brief (`value-audit-mandate.md`). With a philosophy and no brief, the audit reads as before.
- Under a brief, an item the audit holds in a goal run that the run can remediate without any further decision is remediated by the run: the loop does not stop, the owner is not reached, and the audit is dispatched again new on what the remediation changed (D4). Only an item that needs a decision above the run stops the loop and goes by the Carrier.
- A goal run without a brief reads exactly as before: the user ratifies the envelope in the session, and the audit runs only where a philosophy exists.
- No plugin line touched by this unit points at a source, a step or a section by its position or order where it can name the thing (brief, the 2026-11-07 constraint). `SKILL.md` Plan Gate's "Second source" and `lifecycle-gates.md`'s "the second source" are among them.
- `durable-docs-authoring` states the wording rule for every document the harness writes (planner-added).
- The proposed records are rewritten for the direction, at intent altitude, one decision each, naming things rather than positions:
  - ADR-D-0064: under a brief, the ratification is the only authority for every unit, a goal envelope included.
  - ADR-D-0065: the brief route's conditions for a plan and for a goal envelope.
  - ADR-D-0063: a goal run under a brief or in a repository with a philosophy is graded by the audit beside the assessor, over the whole run; under a brief, an item the run can remediate without a further decision does not stop the loop.
  - ADR-D-0062: its rejected alternative no longer names an agreement to an envelope.
  - A new record replaces the accepted ADR-D-0027. It keeps what ADR-D-0027 decides (the forbidden set is a criterion; the envelope is fixed before the loop and never changed by it) and leaves who authorizes it to ADR-D-0064. It is numbered ADR-D-0068 while pull requests 93 and 94 are both open, and renumbered at merge.
  - All stay proposed for the owner's acceptance by name; nothing is retired before it.
- Package validators and smoke tests pass; the change has Reviewer `APPROVED`; value audits at plan draft and closeout are logged. The branch is pushed and pull request 93's text brought up to date, the run is reported ready again with the note to Counsel, and nothing is merged.

## Planner-added requirements
- `durable-docs-authoring` states the wording rule. Needed because the brief's constraint covers "every document the harness writes" and the owner said "in general". Writing it into this run's text alone would leave every later document the harness writes outside it.
- A new record replaces ADR-D-0027. Needed because its accepted invariant has the envelope ratified by the user before the loop starts, and the brief's 2026-11-07 gives removes that under a brief. ADR-D-0064 as it stands already names a goal-mode record superseding ADR-D-0027 as the place this would be decided.
- The Reviewer's pass covers every clause of the recorded envelope, and `goal-condition-checklist.md` says so. Needed because the route's condition is a review closed on the unit it authorizes. Today's checklist reviews the goal condition, and of the envelope only its exclusion of the irreversible class (`goal-condition-checklist.md`:7-18). It leaves the decision scope, the progress and stall obligations and the backstops (`goal-mode.md`:40-46) unreviewed. It stays one Reviewer pass, not a second dispatch.

## Scope / Non-goals
- Scope: the plugin texts named in the Definition of Done; `skills/durable-docs-authoring/` (the wording rule); ADR-D-0062 to ADR-D-0065 and the new record.
- Non-goals:
  - what authorizes a plan under a brief, which is unchanged;
  - the assessor and its mandate, the stall and completion rules;
  - runs without a brief, a goal run on a philosophy alone included;
  - accepted records other than ADR-D-0027, which run "decision records at intent altitude" checks (told that ADR-D-0027 is now this run's);
  - a sweep of all plugin text for positional wording beyond the lines this unit touches. The rule in `durable-docs-authoring` governs later writing, and run "decision records at intent altitude" checks the records.

## Design
- Chosen: a goal envelope under a brief goes through the route a plan under a brief already has, stated once in `lifecycle-gates.md` Plan Gate Details for both units, and goal-mode texts point there. The audit's goal-run attachment widens from "a repository with a philosophy" to "under a brief or in a repository with a philosophy", at the positions it already has. A held item passes one test first, the brief's: is its remedy already determined within the run's authority, leaving no additional decision? If so, the run carries it out with the procedure `value-level-operation.md` Acting On A Verdict already has (drop the unsupported line, correct the input, dispatch the audit again, new), without stopping the loop.
  - structure: one route, one owner of its conditions, and one correction procedure shared by both modes, entered only through the brief's test. The envelope stands where the plan stands, and the Reviewer's pass on the condition and the envelope stands where the plan review stands.
  - evolution: a later change to the route or to the corrections changes both modes at once. Deletion path: the envelope lines in Plan Gate Details and the brief clause in the audit's goal-run attachment.
  - verification: by reading and search. No probe (see below).
  - operation: an Auditor dispatch at each assessment event and at completion, growing with the run, in a repository with no philosophy where none ran before. A remediable item costs a new audit instead of a stop.
  - human: the owner is asked nothing to start a goal run, and only an item needing his decision reaches him.
  - safety: the irreversibility class stays outside every envelope, and an irreversible action still waits for its moment. An item that needs a decision still stops the whole loop.
- Alternative: the run gets its own catalogue of self-remediable findings for goal mode, separate from the plan-mode procedure.
  - structure: two catalogues of what the run may correct by itself.
  - evolution: the catalogues drift apart.
  - verification: two places to check.
  - operation: the same.
  - human: a reader meets two answers to one question.
  - safety: a catalogue can admit a remedy that makes a decision; a test cannot be outgrown that way.
- Why chosen: the owner's words, "if a finding can be remediated without any additional decisions", are a test, not a list. The existing procedure carries out a remedy once the test holds. A redo that needs a new choice fails the test and keeps its route: review and the brief route, or a stop of the loop and the Carrier.
- Ruling D1: the plan route's conditions apply to the envelope as written. Its review is the Reviewer's pass, widened to cover every clause of the envelope (planner-added).
- Ruling D2: under a brief the audit runs at the goal-run positions it already has (envelope, each assessment event, completion), graded against the brief, and the mandate's goal-run fill-ins name the brief.
- Ruling D4: in a goal run under a brief, a held item is remediated by the run only when its remedy is already determined within the run's authority (the brief's 2026-11-07 test). The goal contract stays as `goal-mode.md` states it: tightening is free, loosening escalates, and a changed envelope goes back through the route. So no remediation widens or changes the envelope. The journal records the remediation as it records any decision of the loop, and no grade or other part of a verdict.
- Ruling D3: no fixture probe. The brief's scenarios do not cover goal mode, and the change is a route reused, not a new behaviour. The Reviewer's search for any line under a brief that still has the owner agree to an envelope is the check.

## Compatibility stance
- surface: what starts a goal-mode run under a brief, and the audit's goal-run positions.
- stance: break
- justification: the consumers are Orchestrator sessions reading the plugin, and the owner, for whom the brief changes it. No goal run under a brief has yet run, so no recorded goal depends on the old start.

## Context (workspace)
- Governing brief: as above. Ratification as it reached this session: Counsel's relay of 2026-10-28 (16:17Z), quoting the owner on 2026-10-29: "I ratify both briefs, hand them over now." The entries of 2026-11-07 reached this session by Counsel's relay of 2026-11-07 09:08Z, quoting the owner's words given beside each entry; his check of the inferred entry and the self-remediation entry by Counsel's relay of 2026-11-07 10:02Z, quoting "Go with the whole run reading. And, if a finding can be remediated without any additional decisions, I'd like it automatically handled as well." Relays are admitted by the Standing Approvals entry of 2026-10-01 in `common.md`.
- Run record and readings file: `docs/coding-agent/plans/active/quiet-orchestrator-session-run.md`, `docs/coding-agent/plans/active/quiet-orchestrator-session-readings.md`.
- Research waived: the affected lines were found by search of `plugins/` for envelope, ratification and source wording on 2026-11-07. The area is the run's own text of 2026-10-28.

## Open Questions (max 3)
- None. The owner's check of the inferred entry reached the brief on 2026-11-07 (234ea83), in the whole-run form, with the self-remediation entry beside it.

## Assumptions
- None.

## Tasks

### Task_1: The goal envelope under a brief in the plugin text
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/lifecycle-gates.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/goal-mode.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/value-level-operation.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/value-audit-mandate.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/goal-condition-checklist.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/goal-templates.md
  - plugins/coding-agent-orchestration-harness/skills/durable-docs-authoring/
  - plugins/coding-agent-orchestration-harness/agents/Orchestrator.md and claude/agents/harness-orchestrator.md, only if they restate a changed line
- depends_on: []
- description: |
    Make the plugin say what the Definition of Done says for the plugin text. Wording is the Worker's, within the brief's words.
- acceptance:
  - Under a brief, the envelope is authorized by the brief route on a plan's conditions (D1), with nothing anywhere having the owner agree to it or relaying his answer to start the loop. The conditions are stated once, in Plan Gate Details. A changed envelope goes back through the route.
  - `goal-condition-checklist.md` has the Reviewer's pass cover every clause of the recorded envelope as well as the goal condition.
  - Under a brief, the audit grades the whole goal run against the brief at its envelope, assessment events and completion, philosophy or not, and the mandate's goal-run fill-ins name the brief (D2). Without a brief, everything reads as before.
  - Under a brief, a held item whose remedy is already determined within the run's authority is remediated with Acting On A Verdict's procedure and the audit dispatched again new, without stopping the loop or reaching the owner (D4). The text states the test, not a list of eligible findings. An item needing a decision stops the loop and goes by the Carrier.
  - No line touched names a source, step or section by its position or order where it can name the thing.
  - `durable-docs-authoring` states, once, that wording names the thing meant rather than its position, order or relation to something that can change.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: py scripts/validate_harness_package.py and py scripts/run_validation_smoke_tests.py pass; git diff --check clean on owned paths"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review against the brief's 2026-11-07 entries; a search of plugins/ for envelope ratification, relayed agreement and 'second source' finds no line under a brief that has the owner agree to an envelope or names a source by position"

### Task_2: The records rewritten for the direction
- type: docs
- owns:
  - docs/coding-agent-orchestration-harness/decisions/ADR-D-0062-*.md, ADR-D-0063-*.md, ADR-D-0064-*.md, ADR-D-0065-*.md (renamed where the title changes)
  - docs/coding-agent-orchestration-harness/decisions/ADR-D-0068-*.md (new)
- depends_on: []
- description: |
    Rewrite the records as the Definition of Done states, at the altitude `durable-docs-authoring/references/adr.md` states and the brief's 2026-11-02 entry asks for: one decision each, mechanism out, names and not positions.
- acceptance:
  - Each record states one decision that holds through any rewording of the plugin text preserving it, and no record has the owner agree to a goal envelope under a brief.
  - No record points at a source, condition or record by its position or order ("the first source", "the second source", "the third condition") where it can name the thing.
  - The new record carries ADR-D-0027's decisions and supersedes it; ADR-D-0064's Not covered no longer defers to a goal-mode record. Supersession lists and related-record lines agree across the five records. Nothing accepted is edited or retired.
  - Filenames at or under 135 characters, each heading matching its filename.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "py scripts/validate_harness_package.py passes; filename lengths printed; a search of the five records for 'first source|second source|third condition' finds none"
  - kind: review
    required: true
    owner: reviewer
    detail: "Each record against adr.md Form and the one-decision test; nothing ADR-D-0027, ADR-D-0040, ADR-D-0041 or ADR-D-0056 decides is lost except what the brief's 2026-11-07 entries change"

## Task Waves (explicit parallel dispatch sets)
- Wave 1: Task_1, Task_2 (disjoint owns)

## Rollback / Safety
- Each task's commits are its own, and reverting them restores the prior text. Nothing reaches the remote before review and the closeout audit. Nothing is merged without the owner's acceptance naming the pull request.

## Progress Log (append-only)
- Unit starts from revision: 4c2008d (the owner's reading of 2026-11-07 in the brief and Counsel's notes, committed on the run's branch).
- 2026-11-07 09:10 The conflict between the brief's constraint of 2026-10-29 and its inferred entry of 2026-11-07 put to Counsel, with the plan's reading. Counsel revised the constraint (3664419): its second half stands until the owner checks the inferred entry.
- 2026-11-07 09:12 Plan review dispatched to the reviewer seat `agent-harness-reviewer` with the plan-review snippet, at d8d4bc2. 09:19 NEEDS_REVISION, two findings:
  - GE-F1 (major): the audit's widening to the assessment events and completion goes beyond the brief, which narrows its Limits only for the envelope, and it was missing from Planner-added requirements.
  - GE-F2 (minor): the checklist pass reviews the goal condition and only the forbidden-class clause of the envelope, so it is not a closed review of the envelope as a unit.
  - Triage: GE-F1 fix (narrowed to the envelope; the widening became the Design's alternative, with Counsel for the owner's check). GE-F2 fix (the pass covers every clause of the envelope, listed as planner-added).
  - The finding also made plain that items resting on the inferred entry are `ask-now`, so the plan-draft audit waits for the owner's check (Open Questions). Validator: pass.
- 2026-11-07 09:23 Plan review round 2 at c2c15cf (delta d8d4bc2..c2c15cf): APPROVED, GE-F1 and GE-F2 closed, no new findings. The plan review is closed with no finding open. The plan-draft audit waits for the owner's check of the inferred entry.
- 2026-11-07 10:02 Counsel's relay: the owner checked the inferred entry in the whole-run form and added that a finding remediable without a further decision is handled by the run. Brief and notes committed (234ea83, b22859f). The plan revised for both: the audit grades the whole goal run under a brief (D2), and remediable held items do not stop the loop (D4, on the corrections Acting On A Verdict lists). The Design's alternative is now a separate goal-mode list of corrections.
- 2026-11-07 10:04 Plan review round 3 dispatched at 279fa00 (delta f533f99..279fa00). 10:07 NEEDS_REVISION, GE-F1 and GE-F2 still closed, two new findings:
  - GE3-F1 (minor): Acting On A Verdict is not a list of corrections that make no decision, since a redo or a re-derivation can choose.
  - GE3-F2 (minor): D4's ban on any change to the goal condition or an invariant overreached the tighten-free contract and was an unlisted addition.
  - Triage: both fixed. D4 is now the brief's test (remedy already determined within the run's authority), carried out with the existing procedure, and the goal contract is left as `goal-mode.md` states it.
- 2026-11-07 10:08 Plan review round 4 dispatched at 1145da8 (delta 279fa00..1145da8). 10:10 APPROVED: GE3-F1 and GE3-F2 closed, GE-F1 and GE-F2 still closed, no new findings. The plan review is closed with no finding open.
- 2026-11-07 10:11 Value audit dispatched (Claude subagent `harness-auditor` on Fable, a new dispatch), text verbatim:
  You are the value auditor. Read references/value-audit-mandate.md of the orchestration-harness skill and follow it exactly. Position: plan draft. Plan: docs/coding-agent/plans/active/quiet-orchestrator-session-goal-envelope-plan.md. Governing brief: docs/coding-agent/briefs/active/quiet-orchestrator-session-brief.md. Changes since: none.
- 2026-11-07 10:15 Verdict as returned (machine paths shortened; the two comparison lines are in the readings file):
  Procedural note first: in one tool batch I opened the mandate, the plan and the brief together before taking the names-only listing. The mandate asks for the listing between the mandate and any other file. No notes file and no readings file was opened before the grades were fixed, so the audit is not voided; the deviation is recorded here so the Orchestrator can weigh it.
  - Position: plan draft
  - Documents read: docs\coding-agent\plans\active\quiet-orchestrator-session-goal-envelope-plan.md (artifact); docs\coding-agent\briefs\active\quiet-orchestrator-session-brief.md (governing brief, HEAD dbd49ed); docs\coding-agent\rules\common.md (pointer lines 12-13 and Standing Approvals 61-67, at HEAD); plugins\coding-agent-orchestration-harness\skills\value-documents\SKILL.md (instructions); plugins\coding-agent-orchestration-harness\skills\orchestration-harness\references\goal-condition-checklist.md and a search of goal-mode.md (to understand what the plan changes, not as support). Readings file opened after grading: docs\coding-agent\plans\active\quiet-orchestrator-session-readings.md.
  - Product basis: brief in the product owner's words (brief line 6: "the product owner's own words in this brief. ebigunso owns the harness"; owner and product owner are one person, so `inferred` is available).
  - Not audited: engineering side, no engineering philosophy (common.md line 13: "Engineering philosophy: none yet", not a pointer line). Product philosophy likewise none (line 12); the product side is graded on the brief alone.
  - Missing inputs: none. Brief is under active/, committed (git status shows only `.claude/` untracked), carries its ratification (line 3) and product basis (line 6). Brief line 34 (tagged inferred, added 2026-11-07 after ratification) carries no quoted words of its own ("Checked by him the same day, in the wider form below"), so it is not relied on below; the told entries at lines 33, 35, 36, 37, 38 each carry the owner's quoted words with the date and are relied on.
  - Value documents changed in range: none (plan draft, no range). Two wording notes for Counsel, not grades: brief line 28 ("his relayed answer agreeing to them is what starts the loop") and line 43 ("Nothing here changes what the audit grades") are left standing beside the later told entries at lines 33 and 35 that retire them; line 30 records its own retirement, lines 28 and 43 do not. The later told entries govern, so no item is held on the apparent conflict.
  Items (item | mapping | grade | support | ask-now reasons / direction):
  - DoD: under a brief the envelope is authorized by the brief route on a plan's conditions, no one asked (D1) | maps to the brief | cited | brief line 33 "Under a brief, the owner's agreement is not required to start a goal-mode run, through Counsel or anywhere"; line 35 "a changed envelope goes back through the route as a changed plan does"; line 20 "It is authorized by the brief route or it is not yet a plan that can run" | -
  - DoD 1a / planner-added: the Reviewer's one pass covers the goal condition and every clause of the recorded envelope | maps to the brief | inferred | extends line 35 "the envelope reviewed ... goes back through the route as a changed plan does" and line 20 (the route's review condition); today's checklist (goal-condition-checklist.md lines 7-18) covers the condition and only the forbidden-class clause, as the plan says; cheap to undo | -
  - DoD 1b: a plan-draft audit after the pass grades the envelope against the brief and holds nothing | maps to the brief | cited | line 35 "the envelope before the loop starts" graded against the brief | -
  - DoD 1c: the three moves apply to the envelope when the route does not authorize | maps to the brief | inferred | extends line 20 "three moves and no fourth" (stated for a plan) with line 35 "as a changed plan does"; cheap to undo | -
  - DoD 1d: a changed envelope goes back through the route | maps to the brief | cited | line 35 "a changed envelope goes back through the route as a changed plan does" | -
  - DoD: the named goal-mode texts say so; a stop of the loop under a brief still goes by the Carrier | maps to the brief | cited | line 21 "every question that needs the owner, whatever its kind, travels by the Carrier"; line 35 "An item the audit holds stops the loop and its question travels through Counsel" | -
  - DoD: the audit grades the whole goal run against the brief, no philosophy too, at envelope, each assessment event, completion; mandate fill-ins name the brief (D2) | maps to the brief | cited | line 35 "the value audit grades the whole goal run against the brief, in a repository with no philosophy too: the envelope before the loop starts, the run at each point the assessor runs, and the completion report"; line 30 "the second half is retired by his choice of the whole-run reading" | -
  - DoD: with a philosophy and no brief the audit reads as before | maps to the brief | cited | line 24 "A run without Counsel, on a philosophy alone or with no brief, is unchanged" | -
  - DoD: a held item the run can remediate without a further decision is remediated by the run, no stop, owner not reached, audit dispatched again new (D4) | maps to the brief | cited | line 36 "A finding of the audit during a goal run that can be remediated without any additional decision is handled by the run itself and does not stop the loop or reach him; only a finding that needs a decision above the run stops the loop and travels through Counsel"; the re-dispatch from line 20 "correct its own input and dispatch the audit again". Not a loosening beyond the brief: the narrowing of line 35's stop is the owner's own told entry. D4's test wording ("remedy already determined within the run's authority") restates line 36 | -
  - D4 detail: no remediation widens or changes the envelope; the journal records the remediation as a decision of the loop | maps to the brief | inferred | extends line 36 and line 35 "a changed envelope goes back through the route"; cheap to undo | -
  - DoD: a goal run without a brief reads exactly as before | maps to the brief | cited | line 24 (constraint, quoted above) | -
  - DoD: no touched plugin line names a source, step or section by position; "Second source" lines included | maps to the brief | cited | line 37 "the wording names the thing itself ... so the statement holds when the order changes"; line 38 "Choose wording that would be less likely to change meaning when something else changes" | -
  - DoD / planner-added: `durable-docs-authoring` states the wording rule | maps to the brief | cited | line 38 "Across every document the harness writes, wording is chosen so that its meaning is unlikely to change when something else changes" (constraint). Note: the skill governs durable documents; "every document the harness writes" is wider (plans, reports, journals), which the Reviewer may want to check the placement against | -
  - DoD: ADR-D-0064 rewritten so that under a brief the ratification is the only authority for every unit, envelope included | maps to the brief | cited | line 33 "ADR-D-0064 as rewritten does not stand"; line 32 "one decision per record, stated so that any rewording of the plugin text that preserves it stays valid" | -
  - DoD: ADR-D-0065 states the brief route's conditions for a plan and an envelope, naming things | maps to the brief | cited | line 37 "In ADR-D-0065 ... the wording names the thing itself (the ratified brief carried by the value audit)"; line 32 | -
  - DoD: ADR-D-0063 rewritten: whole-run grading beside the assessor; remediable item does not stop the loop | maps to the brief | cited | lines 35 and 36 (quoted above); line 32 | -
  - DoD: ADR-D-0062's rejected alternative no longer names an agreement to an envelope | maps to the brief | cited | line 33; line 32 | -
  - DoD / planner-added: a new proposed record (ADR-D-0068) replaces accepted ADR-D-0027, keeping its decisions and leaving who authorizes to ADR-D-0064; nothing accepted edited or retired before the owner's acceptance by name | maps to the brief | inferred | extends line 33 (no agreement starts a goal run under a brief; "the earlier record ... is revised accordingly" at line 28) and line 32 "merged where the standard's one-decision test allows"; a proposed file, cheap to undo; acceptance of a decision record keeps its own gate | direction: which accepted record is superseded is on the owner's reading surface and sets who authorizes autonomous runs
  - DoD: numbered ADR-D-0068 while pull requests 93 and 94 are open, renumbered at merge | maps to the brief | inferred | extends line 32 (the records rewritten and held); cheap to undo | -
  - DoD: all records stay proposed for the owner's acceptance by name | maps to the brief | cited | line 32 "are held, not accepted" | -
  - DoD: validators and smoke tests pass; Reviewer APPROVED; value audits at plan draft and closeout logged | maps to the brief | cited | line 57 "the package validators pass" (agent-checkable pass condition) | -
  - DoD: the branch is pushed and pull request 93's text brought up to date | maps to the brief | cited | outward-facing; standing approval, common.md line 65: "A finished, reviewed run may publish its branch and open pull requests in this repository without asking first. ... Given and accepted by the repository's owner, ebigunso, on 2026-09-30, relayed by Counsel: 'The common rule proposed, accepted.'" The entry records the giver, the acceptance and the date; that the words were said is not something a file can show | -
  - DoD: the run is reported ready again with the note to Counsel | maps to the brief | cited | line 14 "Whatever needs him, of any kind, reaches him through Counsel"; line 53 "it names what is with Counsel". Read as the brief's own channel, not an external system | -
  - DoD / Rollback: nothing is merged; merges wait for the owner naming the pull request | maps to the brief | cited | standing approval line 65 "Merges are not covered and wait for the owner" | -
  - Non-goal: what authorizes a plan under a brief is unchanged | maps to the brief | cited | line 43 "Nothing here changes ... what authorizes a plan under a brief" | -
  - Non-goal: the assessor and its mandate, stall and completion rules unchanged | maps to the brief | inferred | extends line 35 "the run at each point the assessor runs" (the audit beside the assessor, not in its place); cheap to undo | -
  - Non-goal: runs without a brief, a goal run on a philosophy alone included | maps to the brief | cited | line 24 | -
  - Non-goal: accepted records other than ADR-D-0027 left to run "decision records at intent altitude" | maps to the brief | cited | line 32's gives is scoped to "ADR-D-0062 to ADR-D-0065"; the owner's wider remark "not limited to the ones proposed" is in his quoted words, not the gives, and the plan routes it to the run that holds it | -
  - Non-goal: no sweep of all plugin text for positional wording beyond touched lines | maps to the brief | inferred | extends line 38 (a constraint on writing: "Choose wording ... when writing documents in general") and line 37 (records); cheap to undo | -
  - Design D3: no fixture probe; verification by reading and the Reviewer's search | maps to the brief | cited | line 57 "scenarios 1, 2 and 5 are shown where one can be made, and where one cannot the closeout says so plainly"; the brief's scenarios do not reach goal mode, and the pass condition is not loosened so long as the closeout says so | -
  - Compatibility stance: break, for what starts a goal run under a brief | maps to the brief | cited | line 33 | -
  - Task_1 | maps to the brief | cited | as the DoD entries above (lines 20, 21, 24, 33, 35, 36, 37, 38) | -
  - Task_2 | maps to the brief | cited | lines 32, 33, 37; the ADR-D-0027 replacement within it is inferred as graded above | -
  - Assumptions: none; Decision Log: no entries.
  No item is `ask-now`. No scope expansion found: every planner-added requirement traces to a brief statement named above.
  - Human-only conditions pending: "his next run under a brief in this repository ends with nothing asked of him in the Orchestrator's session."
  - Scenarios: none
- Acting on the verdict: no item is ask-now, and the plan review closed with no finding open, so the brief route authorizes the plan as it stands at dbd49ed. Inferred calls, as the verdict's item lines state them: DoD 1a (the Reviewer's pass covers every envelope clause), DoD 1c (the three moves apply to the envelope), D4 detail (no remediation changes the envelope; the journal records it), the new record replacing ADR-D-0027 (direction: which accepted record is superseded sets who authorizes autonomous runs; for the owner's reading at acceptance), its interim number, the assessor non-goal, and the no-sweep non-goal. Missed step: the Orchestrator wrote no reading before this dispatch (value-level-operation.md Documents), so every item reads unread. The grades do not depend on the reading and stand; a reading written now, after the grades, would not be a reading, so none is added for this position. The closeout reading is written before the closeout dispatch. The procedural note (batch order) touched no notes or readings file before grading; the verdict is not void. The auditor's two wording notes on brief lines 28 and 43 go to Counsel as observations.
- 2026-11-07 10:17 The two observations went to Counsel. 10:18 Counsel marked both brief entries revised, in its own wording with no new word of the owner's (f7c963f).
- 2026-11-07 Wave 1 dispatched: Task_1 and Task_2 to Claude `harness-worker` subagents on Opus, in parallel (disjoint owns).
  - Task_1, done (e97c9a2): eight plugin files. Package validator and smoke tests pass, and git diff --check is clean. Adapters are unchanged, since they restate no changed line. Three questions, ruled in the Decision Log (D5 to D7); the follow-up edit to `value-audit-mandate.md` validated the same way.
  - Task_2, done (3bf43b8): ADR-D-0062 and ADR-D-0064 rewritten; ADR-D-0063 and ADR-D-0065 rewritten, retitled and renamed; ADR-D-0068 new, replacing ADR-D-0027. Validator pass; filename lengths 104, 132, 116, 128, 121; positional search clean; ADR-D-0068's admission test passes. The Worker reported one stray index write (`git add -N` on the new record), undone at once; the index was confirmed empty before the commit. Two questions, ruled in the Decision Log (D8, D9).
  - Wave integration: both reports map to one task each, every changed path is within owns, and every required Worker check passes. Reviewer dispatch next.

## Decision Log (append-only; re-plans and major discoveries)
- D5 (Task_1): the whole-envelope item in `goal-condition-checklist.md` applies under a brief only; runs without a brief keep the forbidden-set check alone (the brief's constraint that runs without a brief are unchanged).
- D6 (Task_1): under a brief, every clause of the recorded envelope is an item of the plan-draft audit, since the brief has the audit grade an envelope "as it grades a plan". Without a brief, the mandate's item list is unchanged.
- D7 (Task_1): an audit dispatched again after a correction or remediation names the same Changes since as the audit it repeats. Kept, so that the held changes are audited again.
- D8 (Task_2): ADR-D-0068 keeps ADR-D-0027's criterion and fixity as one decision, the boundary of the loop's autonomy set outside the loop. Splitting it would turn one accepted decision into two acceptance asks with nothing gained; the review checks it against the one-decision test.
- D9 (Task_2): ADR-D-0063 states no reason for the remediation exception applying only under a brief. Nothing written supplies one beyond the brief's own scope (runs without a brief unchanged), so the record stays silent rather than invent one.

## Notes (Risks / Edge cases)
- A remediation that quietly changes what the loop may do would bypass the route. The goal contract already keeps that out: a changed envelope goes back through the route, and loosening escalates.
