# Plan: A goal envelope under a brief authorized by the brief route

- status: draft
- generated: 2026-11-07
- last_updated: 2026-11-07
- work_type: docs

## Goal
- The harness gives what the governing brief `docs/coding-agent/briefs/active/quiet-orchestrator-session-brief.md` states in its entries of 2026-11-07 under Directed during the run:
  - under a brief, a goal-mode run starts without the owner's agreement, through Counsel or anywhere;
  - its envelope is authorized as a plan under a brief is;
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
- Under a brief, the value audit grades the envelope against the brief at its plan-draft position, in a repository with no philosophy as well, and the mandate's fill-in for that position names the governing brief (`value-audit-mandate.md`). The audit's other goal-run positions (the assessment events, completion) are unchanged: they run only where a philosophy exists, as written (D2).
- A goal run without a brief reads exactly as before: the user ratifies the envelope in the session, and the audit runs only where a philosophy exists.
- No plugin line touched by this unit points at a source, a step or a section by its position or order where it can name the thing (brief, the 2026-11-07 constraint). `SKILL.md` Plan Gate's "Second source" and `lifecycle-gates.md`'s "the second source" are among them.
- `durable-docs-authoring` states the wording rule for every document the harness writes (planner-added).
- The proposed records are rewritten for the direction, at intent altitude, one decision each, naming things rather than positions:
  - ADR-D-0064: under a brief, the ratification is the only authority for every unit, a goal envelope included.
  - ADR-D-0065: the brief route's conditions for a plan and for a goal envelope.
  - ADR-D-0063: a goal run in a repository with no philosophy is not graded by the audit, except that under a brief its envelope is, by the brief route.
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
  - runs without a brief;
  - accepted records other than ADR-D-0027, which run "decision records at intent altitude" checks (told that ADR-D-0027 is now this run's);
  - a sweep of all plugin text for positional wording beyond the lines this unit touches. The rule in `durable-docs-authoring` governs later writing, and run "decision records at intent altitude" checks the records.

## Design
- Chosen: a goal envelope under a brief goes through the route a plan under a brief already has, stated once in `lifecycle-gates.md` Plan Gate Details for both units. Goal-mode texts point there. The audit grades the envelope against the brief, and its other goal-run positions stay as written.
  - structure: one route, one owner of its conditions. The envelope stands where the plan stands, and the Reviewer's pass on the condition and the envelope stands where the plan review stands.
  - evolution: a later change to the route changes both modes at once. Deletion path: the envelope lines in Plan Gate Details.
  - verification: by reading and search. No probe (see below).
  - operation: one audit dispatch at the envelope where none ran before in a repository with no philosophy.
  - human: the owner is asked nothing to start a goal run, so goal mode costs him no more than plan mode does.
  - safety: the irreversibility class stays outside every envelope, and an irreversible action still waits for its moment.
- Alternative: the audit also grades a goal run under a brief against the brief at its assessment events and completion, in a repository with no philosophy as well.
  - structure: the audit's goal-run attachment widens from "a repository with a philosophy" to "under a brief or with a philosophy".
  - evolution: the loop's drift from the brief would show inside the loop, not only when the work is built.
  - verification: the same.
  - operation: an Auditor dispatch on every assessment event and at completion, growing with the run.
  - human: the same at the start.
  - safety: more stops of the whole loop.
- Why chosen: the brief's 2026-11-07 entry narrows its Limits only for the envelope ("the audit grades a goal envelope under a brief as it grades a plan"), and the Limits otherwise keep what the audit grades. The alternative was put to Counsel on 2026-11-07 for the owner's check. If he directs it, it comes back through this plan's gate.
- Ruling D1: the plan route's conditions apply to the envelope as written. Its review is the Reviewer's pass, widened to cover every clause of the envelope (planner-added).
- Ruling D2: the audit's assessment-event and completion positions are unchanged.
- Ruling D3: no fixture probe. The brief's scenarios do not cover goal mode, and the change is a route reused, not a new behaviour. The Reviewer's search for any line under a brief that still has the owner agree to an envelope is the check.

## Compatibility stance
- surface: what starts a goal-mode run under a brief, and the audit's goal-run positions.
- stance: break
- justification: the consumers are Orchestrator sessions reading the plugin, and the owner, for whom the brief changes it. No goal run under a brief has yet run, so no recorded goal depends on the old start.

## Context (workspace)
- Governing brief: as above. Ratification as it reached this session: Counsel's relay of 2026-10-28 (16:17Z), quoting the owner on 2026-10-29: "I ratify both briefs, hand them over now." The entries of 2026-11-07 reached this session by Counsel's relay of 2026-11-07 09:08Z, quoting the owner's words given beside each entry. Relays are admitted by the Standing Approvals entry of 2026-10-01 in `common.md`.
- Run record and readings file: `docs/coding-agent/plans/active/quiet-orchestrator-session-run.md`, `docs/coding-agent/plans/active/quiet-orchestrator-session-readings.md`.
- Research waived: the affected lines were found by search of `plugins/` for envelope, ratification and source wording on 2026-11-07. The area is the run's own text of 2026-10-28.

## Open Questions (max 3)
- With Counsel since 2026-11-07: the envelope's route rests on the brief's entry of 2026-11-07 tagged inferred, which awaits the owner's check. The brief's constraint of 2026-10-29, as revised that day, keeps the mandate's goal-run wording until he checks it. An item that depends on an inferred statement with no ratification record is `ask-now` (`value-audit-mandate.md`, Missing inputs and support). So the plan-draft audit is dispatched once his check is in the brief, and not before.

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
  - Under a brief, the audit grades the envelope against the brief, philosophy or not, and the mandate's plan-draft fill-in for a goal run names the brief. The assessment-event and completion positions read as before (D2). Without a brief, everything reads as before.
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

## Decision Log (append-only; re-plans and major discoveries)

## Notes (Risks / Edge cases)
- The inferred entry may come back changed from the owner's check. If it does, the plan is revised and reviewed again before the audit.
