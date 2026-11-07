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
  - the envelope's Reviewer pass on the goal-condition checklist is closed with no finding open;
  - a plan-draft value audit dispatched after that pass grades the envelope against the brief and holds nothing;
  - the three moves apply when the route does not authorize;
  - a changed envelope goes back through the route, as a changed plan does.
- The goal-mode texts say so: `goal-mode.md` Authority Envelope and Value Audit, `value-level-operation.md` (opening paragraph, Goal-Mode Runs, The Carrier's list of consent gates), `lifecycle-gates.md` Plan Gate Details, `SKILL.md` (Repository Rule Entry and Plan Gate), `goal-condition-checklist.md`, `goal-templates.md`. A stop of the loop under a brief still goes by the Carrier.
- Under a brief, the value audit grades a goal run against the brief wherever it now grades a goal run against a philosophy (the envelope, the assessment events, completion), in a repository with no philosophy as well (D2). The mandate's goal-run fill-ins name the governing brief under a brief (`value-audit-mandate.md`).
- A goal run without a brief reads exactly as before: the user ratifies the envelope in the session, and the audit runs only where a philosophy exists.
- No plugin line touched by this unit points at a source, a step or a section by its position or order where it can name the thing (brief, the 2026-11-07 constraint). `SKILL.md` Plan Gate's "Second source" and `lifecycle-gates.md`'s "the second source" are among them.
- `durable-docs-authoring` states the wording rule for every document the harness writes (planner-added).
- The proposed records are rewritten for the direction, at intent altitude, one decision each, naming things rather than positions:
  - ADR-D-0064: under a brief, the ratification is the only authority for every unit, a goal envelope included.
  - ADR-D-0065: the brief route's conditions for a plan and for a goal envelope.
  - ADR-D-0063: the audit grades a goal run under a brief or in a repository with a philosophy.
  - ADR-D-0062: its rejected alternative no longer names an agreement to an envelope.
  - A new record replaces the accepted ADR-D-0027. It keeps what ADR-D-0027 decides (the forbidden set is a criterion; the envelope is fixed before the loop and never changed by it) and leaves who authorizes it to ADR-D-0064. It is numbered ADR-D-0068 while pull requests 93 and 94 are both open, and renumbered at merge.
  - All stay proposed for the owner's acceptance by name; nothing is retired before it.
- Package validators and smoke tests pass; the change has Reviewer `APPROVED`; value audits at plan draft and closeout are logged. The branch is pushed and pull request 93's text brought up to date, the run is reported ready again with the note to Counsel, and nothing is merged.

## Planner-added requirements
- `durable-docs-authoring` states the wording rule. Needed because the brief's constraint covers "every document the harness writes" and the owner said "in general". Writing it into this run's text alone would leave every later document the harness writes outside it.
- A new record replaces ADR-D-0027. Needed because its accepted invariant has the envelope ratified by the user before the loop starts, and the brief's 2026-11-07 gives removes that under a brief. ADR-D-0064 as it stands already names a goal-mode record superseding ADR-D-0027 as the place this would be decided.

## Scope / Non-goals
- Scope: the plugin texts named in the Definition of Done; `skills/durable-docs-authoring/` (the wording rule); ADR-D-0062 to ADR-D-0065 and the new record.
- Non-goals:
  - what authorizes a plan under a brief, which is unchanged;
  - the assessor and its mandate, the stall and completion rules;
  - runs without a brief;
  - accepted records other than ADR-D-0027, which run "decision records at intent altitude" checks (told that ADR-D-0027 is now this run's);
  - a sweep of all plugin text for positional wording beyond the lines this unit touches. The rule in `durable-docs-authoring` governs later writing, and run "decision records at intent altitude" checks the records.

## Design
- Chosen: a goal envelope under a brief goes through the route a plan under a brief already has, stated once in `lifecycle-gates.md` Plan Gate Details for both units. Goal-mode texts point there. The audit's goal-run attachment widens from "a repository with a philosophy" to "under a brief or in a repository with a philosophy".
  - structure: one route, one owner of its conditions. The envelope stands where the plan stands, and the review pass on the checklist stands where the plan review stands.
  - evolution: a later change to the route changes both modes at once. Deletion path: the envelope lines in Plan Gate Details.
  - verification: by reading and search. No probe (see below).
  - operation: a goal run under a brief in a repository with no philosophy now costs audit dispatches at its assessment events, as a plan under a brief costs one per position.
  - human: the owner is asked nothing to start a goal run, so goal mode costs him no more than plan mode does.
  - safety: the irreversibility class stays outside every envelope, and an irreversible action still waits for its moment. A held item still stops the loop.
- Alternative: audit only the envelope under a brief, and leave the loop and completion ungraded where no philosophy exists.
  - structure: two attachments of the audit, one per document kind.
  - evolution: the loop's drift from the brief shows only when the work is built.
  - verification: the same.
  - operation: fewer dispatches.
  - human: the same at the start.
  - safety: nothing judges the loop against the brief after it starts, although the brief is now what authorized it.
- Why chosen: once the brief authorizes the loop, the brief is what the loop answers to. A plan under a brief is graded at closeout as well as at draft, and grading a goal run under a brief only at its envelope would leave it held to less than a plan. This is D2, Counsel's read of the inferred entry, put to Counsel on 2026-11-07 for the owner's check.
- Ruling D1: the plan route's conditions apply to the envelope as written, with the Reviewer's pass on the goal-condition checklist as its review.
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
- With Counsel since 2026-11-07: the brief's constraint of 2026-10-29 keeps "the audit mandate's dispatch wording for a goal run under a brief in a repository with a philosophy" as written (`Governing brief:` is `none`). The inferred entry of 2026-11-07 changes it, and that entry awaits the owner's check. This plan builds on the inferred entry.

## Assumptions
- A1: the Reviewer's pass on the goal-condition checklist is the envelope's review for the route's "review closed" condition. Source: `goal-mode.md` Value Audit already dispatches the envelope's audit after that pass.

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
  - Under a brief, the audit grades a goal run against the brief at its envelope, assessment events and completion, philosophy or not, and the mandate's goal-run fill-ins name the brief. Without a brief, everything reads as before.
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

## Decision Log (append-only; re-plans and major discoveries)

## Notes (Risks / Edge cases)
- The inferred entry may come back changed from the owner's check. If it does, the change goes back through this plan's gate before what it touches is built.
