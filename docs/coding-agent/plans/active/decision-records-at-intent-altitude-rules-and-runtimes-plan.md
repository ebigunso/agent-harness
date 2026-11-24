# Plan: Decision records at intent altitude: rule suites, runtimes and validators

- status: draft
- generated: 2026-11-24
- last_updated: 2026-11-24
- work_type: docs

## Goal
- Four active records of the area "Roles, routing, runtimes and rules" (ADR-D-0024, ADR-D-0025, ADR-I-0006, ADR-I-0007), the ones on rule-suite lifecycle data, rule-suite validity, runtime discovery and what validators may block, are checked against the record standard as it stands, and each decision that fails the check has a new complete record proposed for it. No decision changes.

## Definition of Done
- Each of the four records has its check's result ready for the run record's table: meets, rewritten (to which), split (into which), retired (material where), or raised.
- Each new record is in the template's present form, states one decision by the owner's test, and names in `consulted` the old record's entries and the model that wrote it.
- Every Decision clause of an old record has one of three fates, listed clause by clause: carried by a new record; held by a named accepted record, or by a proposed record of the pull requests this unit is stacked on, whose line that states it is quoted and whose scope reaches as far as the old clause; or, only for what the brief lists as mechanics (routes, moves, file names, admission of a relay, template fill-ins) and for exact strings, left to the plugin's text, quoted by file and line, with which of those it is named. A clause that says when, who, which or whether is not mechanics, and a list the decision closes ("only", "no other", "every") stays as written.
- These reach the owner by name: a record split in two or more; a record the run cannot show to keep its decision; a record whose revisit condition says something the old record's reason does not. Every other rewrite waits for the closeout audit's confirmation, record by record, that its decision is unchanged, and he is given the list afterwards.
- The package validator and the smoke tests pass.

## Planner-added requirements
- `consulted` carries the old record's entries as well as the model that wrote the new record. Needed because: the brief asks for the models talked with, and the old record's entries are the only record of who was consulted when the decision was made.
- Each task's report lists every Decision clause of the old record and where it went, quotes a holder's line, and also lists each old Validation line not carried with where its content lives, each term the new record defines that the old did not, and anything a new Decision holds that the old record had in another section. Needed because: the brief's rule on a clause not carried cannot be reviewed without the list, and earlier units' reviews found scopes narrowed by added definitions, allowances lost with Validation lines, and sentences moved into a Decision unnamed (`docs/coding-agent/lessons.md`, the entries of 2026-11-24).
- A new record's file name, once numbered, is at most 109 characters. Needed because: a retired record's name gains 26 characters and names beyond 135 have failed the smoke test's copy of the tree (`docs/coding-agent/lessons.md`, the entry on file-name length).

## Scope / Non-goals
- Scope: new proposed records under `docs/coding-agent-orchestration-harness/decisions/`.
- Non-goals:
  - Changing any decision's outcome; a decision found stale or contradicted is brought to the owner through Counsel and not rewritten.
  - The plugin's text, the record standard and its template. The possible mismatch between the plugin's relaxed validation mode and ADR-I-0007's blocking of missing evidence is a matter for later, about the plugin's text, noted to Counsel (Decision Log).
  - Marking any record accepted, retiring any old record, and repairing references to it: these follow acceptance, as a small change of the run.
  - The area's other records (ADR-D-0004, 0019, 0021, 0048, 0050, 0068, 0069, 0070), the later units of this area; ADR-D-0026, left to the run under the brief "Lessons keep their purpose"; the records of pull requests 113, 114 and 116; ADR-D-0057 and ADR-D-0062, held for the owner's answer.

## Design
- Chosen: one task per old record or closely tied pair, each writing the new records for it; no alternative required. The change touches no responsibility, contract, persisted state, new component, trust boundary or hot path.

## Context (workspace)
- Governing brief: `docs/coding-agent/briefs/active/decision-records-at-intent-altitude-brief.md`. Ratification as it reached this session: Counsel's relay over the peer channel, 2026-11-24T09:42:31Z, handing over the part of the open run that is not begun and quoting the owner's words from the run record's hand-over line: "Nothing to add, I ratify the brief, hand it over." (2026-11-02). Relays are admitted by the Standing Approvals entry "Relays from Counsel" in `docs/coding-agent/rules/common.md`, accepted 2026-11-20.
- Run record: `docs/coding-agent/plans/active/decision-records-at-intent-altitude-run.md`. Readings file: `docs/coding-agent/plans/active/decision-records-at-intent-altitude-readings.md`.
- Branch: `feature/2026-11-24/decision-records-roles-area`, stacked on the branch of pull request 116 (ae26bce0).
- Models: by the owner's lineup relayed by Counsel at 2026-11-24T11:00Z ("Yes, that lineup is fine."): the Orchestrator, writing Workers and design Reviewers on Opus 5.5 at high reasoning effort; the Auditor and insight research on Fable 5.2 at high; rigorous research and rigorous review to the Codex seats as the record of models in `common.md` has it.
- Research: the researcher seat `agent-harness-researcher` (Codex), 2026-11-24, eight parts over the peer channel, on the area's twelve records at ae26bce0. Its classifications for these four, which each task checks again: ADR-D-0024 two or three decisions (lifecycle facts stay outside the rules read during normal work; agents read lifecycle facts only on six named occasions, a closed list; the index only routes and role rules carry operating policy only); ADR-D-0025 three or four (validity is established anew from repository facts whenever needed; refresh answers only an observed need and is limited to what needs it; bootstrap is never a per-task ritual; possibly, the rulebook owns validity conditions and refresh triggers); ADR-I-0006 three (each runtime discovers only its own adapters; Codex agents become live only on explicit installation; every runtime loads skills from the same tree); ADR-I-0007 one, arguably two (validators block failures of contract, required evidence or completion, and judgement of wording and strategy belongs to reviewers). None is operational only, none fully meets the present form, and none is found stale or contradicted. No accepted record holds any of their clauses; each is carried. The seat names, for ADR-D-0024, an internal discrepancy between the Decision's closed six occasions and a Not covered line that leaves "read triggers" out; and, for ADR-I-0007, the plugin's relaxed validation mode beside the record's categorical gates.
- What earlier units leave to this one: how the owner's test is read (a clause is part of another decision when no way of retiring that decision leaves it anything to constrain), which three closeout audits have marked as a matter of direction; it was put to the owner through Counsel on 2026-11-24, with two readings as he would experience them (Open Questions).
- Numbers: another run proposes records at the same time, so a draft is named by its subject and takes its number when the work lands. A draft's working name here is `ADR-D-from-<old number>-<slug>.md` or `ADR-I-from-<old number>-<slug>.md`.

## Open Questions (max 3)
- With the owner, through Counsel (sent 2026-11-24): which reading of his one-decision test the rest of the run writes to. This unit is written to the reading the run has used; if he chooses the plainer reading, records of this unit that it would join are merged before acceptance, which is cheap while they are proposed.

## Assumptions
- A1: the researcher seat's counts hold. source: unverified: each task applies the test again in both directions and writes to the count it gives, reporting a count that differs from the one expected as a judgement call; every split reaches the owner by name and the review checks the count.
- A2: no Decision clause of the four is stale or contradicted. source: the researcher seat's comparison of 2026-11-24 with the plugin's present text and the newer accepted records. A task that finds one writes no record for that decision and reports it, and it goes to the owner through Counsel as raised; the Orchestrator then rules, before anything of the unit is published, what the unit's other records do.
- A3: the owner's answer on the reading of the test may arrive during the unit. source: the question is open. If it does, the records are brought to it before the closeout audit, through the plan's gate for a revision.

## Tasks

### Task_1: ADR-D-0024 and ADR-D-0025
- type: docs
- owns:
  - docs/coding-agent-orchestration-harness/decisions/ADR-D-from-0024-*.md
  - docs/coding-agent-orchestration-harness/decisions/ADR-D-from-0025-*.md
- depends_on: []
- description: |
  Check ADR-D-0024 and ADR-D-0025 against the record standard and the owner's test (the brief: a clause belongs to the same decision only if it could not stand once the first is retired; read here as: a clause is part of another decision when no way of retiring that decision leaves the clause anything to constrain), applied in both directions for each pair of clauses, and write a new complete proposed record for each decision each holds; two or three are expected from ADR-D-0024 and three or four from ADR-D-0025. ADR-D-0024's list of the occasions on which lifecycle facts are read is closed by the decision and stays as written; the file the facts live in is a file name. Its Not covered line that leaves "read triggers" out is read beside the closed list: the list of occasions is decision content and the exact conditions that make an occasion arise are not; a task that cannot reconcile the two reports both lines and writes the list as the Decision has it. ADR-D-0025's assignment of validity conditions and refresh triggers to the rulebook is carried as who owns them; the reference path and file names are mechanics; whether it is a decision of its own is decided by the test. "A Git commit SHA is not a freshness baseline" is carried as its criterion (stored state is never a freshness baseline), the example kept only if a first-time reader needs it.
- acceptance:
  - Each new record states one decision by the owner's test, in the template's present form, with nothing that merely happens to be so, wording that names a thing by what it is and not by its position, order or count, a problem statement that says what was wanted, why, and what failed to serve it, and no term defined so that it narrows what the old record reached.
  - The report holds what Planner-added requirements lists; a clause that is decision content is never left to the plugin's text, a clause left to it is named as which of the brief's mechanics or which exact string it is, and a list the decision closes stays as written.
  - The Why names the philosophy statement the decision serves where one does, quoted from the philosophy, and invents none; where the old record gives no reason for a clause, the gap is reported and nothing is written for it.
  - Rejected alternatives, their reasons and reopen conditions, and revisit conditions are the old record's, restated and not replaced or narrowed; the dated fact of a dated revisit line stays as written; an act stays an act, a limit stays a limit, a conditional keeps its condition in the old record's order; no qualifier is added that the old record does not have; a pointer to another record is checked against that record's scope and Not covered.
  - `status: proposed`; `supersedes` names the old record; `consulted` as Planner-added requirements states; the file name, once numbered, is at most 109 characters; the old record itself is unchanged.
  - A count by the owner's test that differs from the one expected is written to and reported as a judgement call.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness: python scripts/validate_harness_package.py and python scripts/run_validation_smoke_tests.py; from the root: git diff --check, and git diff --no-index --check /dev/null <each new file>"
  - kind: review
    required: true
    owner: reviewer
    detail: "Each new record against the record standard, the owner's test and the old record, clause by clause; the decision is unchanged"

### Task_2: ADR-I-0006
- type: docs
- owns:
  - docs/coding-agent-orchestration-harness/decisions/ADR-I-from-0006-*.md
- depends_on: []
- description: |
  As Task_1, for ADR-I-0006; three records are expected: each runtime discovers only its own adapters; agents of the runtime that needs an explicit installation become live only on that installation, nothing in the plugin's source tree being one of its live agents; every runtime loads skills from one shared tree. The runtime the old record names as needing explicit installation is the subject of that decision, not an incidental example, and is named. The paths, manifests and validator checks are mechanics; that each runtime's discovery path is one no other runtime scans for agents is the criterion and is carried. The old record's dated or unverified statement on nested discovery stays as written where it is a revisit premise. The Validation is restated as what would show each decision broken, not as the validator and smoke test that check it.
- acceptance:
  - As Task_1's first six bullets, for ADR-I-0006.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "As Task_1"
  - kind: review
    required: true
    owner: reviewer
    detail: "As Task_1"

### Task_3: ADR-I-0007
- type: docs
- owns:
  - docs/coding-agent-orchestration-harness/decisions/ADR-I-from-0007-*.md
- depends_on: []
- description: |
  As Task_1, for ADR-I-0007; one record is expected, arguably two (that validators block failures of contract, required evidence or completion; and that judgement of wording and strategy is a reviewer's and a validator warns at most). The positive classes are a closed list and stay as written; the kinds of thing given as contracts are examples and are restated as the criterion where the old record gives them as examples. The owner's answers of 2026-11-11 in the brief ("the record stands and the checker is brought in line with it"; a token a program reads stays failing where it is mentioned in a document only people and models read: "Leave them failing.") are the reading of the record's own criterion and are not new decisions; the record states the criterion so that both hold, and adds nothing beyond them. The possible mismatch with the plugin's relaxed validation mode is not this record's to settle and is not written into it.
- acceptance:
  - As Task_1's first six bullets, for ADR-I-0007.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "As Task_1"
  - kind: review
    required: true
    owner: reviewer
    detail: "As Task_1"

## Task Waves (explicit parallel dispatch sets)

- Wave 1 (parallel): [Task_1, Task_2, Task_3]

## Rollback / Safety
- New files only, all proposed; reverting the branch removes them. No record is accepted, retired or merged by this plan. The push and pull request go under the standing approval for a finished, reviewed run; acceptance of each record that reaches the owner by name, and the merge, wait for the owner.

## Progress Log (append-only)

Append-only editing rule (applies to both logs below): when appending an entry, anchor the edit on the previous entry and reproduce it (or anchor on the section's tail marker) so the edit inserts rather than replaces, and verify afterward that the log grew.

- 2026-11-24 Plan starts from revision ae26bce0 (the head of pull request 116's branch; the brief is unchanged since pull request 111).

## Decision Log (append-only; re-plans and major discoveries)

- 2026-11-24 Decision: the area "Roles, routing, runtimes and rules" is built in units of about ten records, this one first, as the group least changed by the open question on the reading of the test.
  - Trigger / new insight: the researcher seat counts about 35 to 40 new records for the area's twelve under the reading the run has used.
  - Tradeoffs considered: the brief has him receive batches "of about ten records"; the largest records (ADR-D-0019, ADR-D-0050) and the routing records change most with his answer, and wait for it.
  - User approval: no (Orchestrator ruling)
  - Record proposed: none
- 2026-11-24 Decision: no record of the area is raised. ADR-D-0021 is silent on subagents Counsel dispatches, not contradicted by the plugin text that lets Counsel dispatch Researchers; ADR-D-0050's "chosen per role by whoever configures the runtime" reads with ADR-D-0068's choice by a stated reason, the one who configures being the one who sets and confirms the record. Both are for their own units; neither is in this one.
  - Trigger / new insight: the researcher seat named both as possible tensions, not settled by the text.
  - Tradeoffs considered: a question goes to the owner only when its options differ in what he experiences; neither reading of either changes what he sees, and no closure word of either old record is broken.
  - User approval: no (Orchestrator ruling)
  - Record proposed: none
- 2026-11-24 Decision: the possible mismatch between the plugin's relaxed validation mode (`validation-strictness.md`: it reports "without blocking except for unsafe or clearly malformed critical contracts") and ADR-I-0007's blocking of missing required evidence and unresolved completion is a matter for later, noted to Counsel, and not part of this unit.
  - Trigger / new insight: the researcher seat named it; whether a mode changes a script's exit or a run's gate is not settled by the text.
  - Tradeoffs considered: the brief leaves the plugin's text out of this work; the record's rewrite keeps its decision whichever way the plugin text is read.
  - User approval: no (Orchestrator ruling)
  - Record proposed: none

## Notes
- Risks: ADR-I-0007 is pointed at by seventeen files, ADR-I-0006 by twelve; after acceptance each pointer is repaired by what it means. A Worker will be tempted to restate a closed list as its criterion, or to generalize a subject; both widen a decision.
