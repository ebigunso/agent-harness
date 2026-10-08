# Plan: Process principles in the plugin

- status: in_progress
- generated: 2026-10-08
- last_updated: 2026-10-08
- work_type: docs

## Goal
- The harness gives what the governing brief `docs/coding-agent/briefs/active/process-principles-in-the-plugin-brief.md` states: five process principles present once each in the plugin text at the place where it acts, as what the agent does and not what code must be; the record on discoveries brought in line with the second principle.
- The brief is the requirement and is not restated here; where this plan and the brief differ, the brief governs and the difference is a plan defect.
- This is the first plan of the run recorded in `docs/coding-agent/plans/active/process-principles-in-the-plugin-run.md`.

## Definition of Done
- Plan review asks, of each piece of a design, what it is for (the thing in the goal it serves; for a piece that prevents something, the situation and how likely it is in everyday use) and what it costs (debt, operational complexity, effect on future change, blast radius relative to the task); a preventive piece that does not make its case is a finding, and so is a smaller design the questions point to. Stated once, where the plan-review check lives; the Plan Gate points to it.
- A discovered issue is read by the Orchestrator as one of three: within the task as given, fixed in place; a change to the design, which revises or extends the plan; a matter for later, noted for its own task. It is never absorbed into the current change. A plan revised or extended mid-run goes back through the gate that admitted it, for what changed, before any of it is built: the plan review, and the value audit on the plan as it now stands (under a brief), or the user's approval of the revision (without one); the audit's scope test applies to the revision; the two questions apply to each added piece. Stated once, in the replan procedure; the triggers and the wave checklist point to it.
- Reports say what was left out and why, what was not verified, and where the work scoped down, out loud; the final response states it once and the Worker report's summary feeds it with no new key.
- The closing review names any evidence artifact (test output, probe results, captured samples and the like) left in the change or lying in the working tree once its claim is recorded; it stays only where the change makes the case that future work rests on it; regression tests are not evidence. Stated once, in the Reviewer's final check.
- A guard, a limit or a compromise states where it is added what it is for and when it could go. Stated once, in the core principles, widening the existing line on suppressions and scaffolding.
- No new text states a code norm; the existing code norms in the plugin are left as they are and named to the owner.
- The record on discoveries (ADR-D-0033, accepted and merged to `main`) is replaced by a new complete record carrying the second principle, accepted by the owner by name before harness text is built on it, and ADR-D-0033 is then retired atomically with its inbound references repaired; ADR-D-0041 (not on `main`) is revised where its decision on changes after the verdict tightens, and ADR-D-0051 where a reason becomes false, each returning by name.
- Where a repository's engineering philosophy or rules say otherwise on any of the five principles, the repository's text wins; stated once, in the engineering-quality-baselines Precedence section every non-trivial implementation and review loads, the five places pointing to it.
- Package validators and smoke tests pass; the branch has Reviewer `APPROVED`.
- The plan closes and the run is reported ready: branch published on the stack, pull request opened under the standing approval, note to Counsel, nothing merged.

## Planner-added requirements
- Without a brief, "the same gate that admitted it" is the plan review and the user's explicit approval of the revision, or the user's explicit waiver naming the approval step (ADR-D-0040's first source as it stands); the record's two pause cases toward the user (contract-shape; irreversible or outward-facing) widen by this one. A fix within the task as given is not a revision and asks nothing. Needed because: the brief's guard names the gate that admitted the plan, and outside a brief that gate is the user's approval (ADR-D-0040); without this the principle would hold only under a brief.
- A mid-run revision is audited at position `plan draft` on the whole revised plan, dispatched by the fixed template with `Changes since: none`, after the plan review of the revision closes. Needed because: the mandate names positions and the template is fixed; the revision needs a position the auditor already knows how to grade.

## Scope / Non-goals
- Scope: `subagent-strategy/references/prompt-snippets.md` (plan-review check); `orchestration-harness/SKILL.md` (Plan Gate pointer; Replan Triggers' action line); `orchestration-harness/references/{lifecycle-gates,final-response-contract,value-audit-mandate (positions text only)}.md`; `wave-integration/references/integration-checklist.md`; `subagent-report-contract/SKILL.md` (the summary line) and its schema comment; `engineering-quality-baselines/references/{review-rubric,core-principles}.md`; records ADR-D-0041, ADR-D-0051, a new record replacing ADR-D-0033 and the retirement of ADR-D-0033 with its inbound references (`docs/coding-agent/lessons.md`, completed plans) repaired; `engineering-quality-baselines/SKILL.md` Precedence.
- Non-goals: any code norm, new or existing (compatibility stance, smallness as a target, refactoring, irreversibility: left as they are); a mechanism to carry a philosophy between repositories; the Reviewer adapters' output format; the fixed dispatch template; a fixture (the brief's pass conditions are agent-checkable on the text, and its scenarios are his next real run).

## Design
- Chosen: each principle tightens the one existing statement nearest to where it acts (the plan-review snippet; the replan procedure; the final-response contract with the Worker summary feeding it; the Reviewer's final check; the core principles' reason line), with the Plan Gate, the triggers and the wave checklist pointing rather than restating; the record on post-verdict changes is revised in place and returns by name; the record on discoveries, being on `main`, is replaced by a new complete record and retired, as adr.md's lifecycle has it; the repository's own text wins on every principle, stated once in the Precedence section.
- Alternative: one new reference, `process-principles.md`, holding the five statements, with a pointer at each of the five places.
- Lenses. structure: chosen keeps one statement per principle at its point of action; the alternative adds a file every role reads and five pointers. evolution: chosen edits text that already loads at those moments; the alternative adds a file to maintain and five pointer dependencies, and a reader at any of the five places must follow a pointer to learn what to do. verification: both checked by reading; chosen is checked by the brief's "present once at the place where it acts". operation: chosen adds no read. human: an agent meets the principle where it acts, not in a separate list. safety: neither adds a code norm; chosen widens core-principles line 69 (suppressions and scaffolding carry a rationale and removal conditions) and leaves line 68, the smallest-root-cause norm, untouched.
- Why chosen: the brief's means says tighten rather than add a second statement.

## Compatibility stance (required if a contract/interface/persisted format is touched)
- surface: the Worker report's `summary` meaning (no key added, old reports still valid); the replan procedure (what must happen before a revised decision is built); the plan-review check.
- stance: migrate
- justification: the report schema's keys and parse validity are preserved, so every existing report stays valid; what changes is the meaning producers and readers give the text (the Worker writing a summary; the Orchestrator integrating it and running the replan procedure; the Reviewer at plan review and final review; the Auditor grading a revision at plan draft; the Orchestrator adapters restating the replan action); each reader's text changes in this plan, so no layer carries the old meaning.

## Context (workspace)
- Governing brief: `docs/coding-agent/briefs/active/process-principles-in-the-plugin-brief.md`. Ratification reached this session on 2026-10-08 as Counsel's relay quoting the owner: "I ratify the brief, hand it over after the current run closes." Relays admitted by the Standing Approvals entry of 2026-10-01 in `common.md`. Hand-over condition unresolved at drafting: his words make the hand-over follow the close of the fresh-repository run, and under the text in the stack a run closes on his acceptance of its stack, which has not arrived; Counsel handed over at "reported ready" on its own reading. Asked of him through Counsel on 2026-10-08; nothing of this plan is executed until his answer makes the hand-over his.
- Run record: `docs/coding-agent/plans/active/process-principles-in-the-plugin-run.md`. Readings file: `docs/coding-agent/plans/active/process-principles-in-the-plugin-readings.md`. This plan starts from revision: 099d78f.
- Research: a Researcher mapped each principle to the text that states it in part (file and line) and found the record on discoveries: ADR-D-0033 (accepted 2026-09-13 and on `main`, so changed only by replacement), which agrees on the Worker's side and differs on the Orchestrator's (it lets a discovery be ruled into the current change, sorts nothing, re-runs no review, and caps the return to the user at two cases). ADR-D-0041 says a post-verdict change needs a later audit or the first source, with no plan review. ADR-D-0051's rejected alternative gives "no fresh plan review" as a reason, which the guard makes false.
- Existing code norms named to the owner, left as they are: plan-format rule 8 (compatibility stance); core-principles §1 and §2 (locatable consumer; small, cohesive, reversible changes; smallest root-cause fix); long-horizon-audit's deletion bias; ADR-D-0016.
- Research waived for dispatch: the Researcher's map is the basis of the Scope and Tasks.
- The audits of this run: this plan's draft and its close.

## Open Questions (max 3)
- None.

## Assumptions
- A1: "the smaller design wins" is the outcome of the two questions, not a size target; the text says so. source: the brief's constraint that no stance on smallness enters.
- A2: ADR-D-0053's test (a finding bears on the design when acting on it changes what someone experiences) stays the value question's test; the second principle's "change to the design" is the implementation design, read by the Orchestrator in the replan procedure; the two are reconciled in ADR-D-0033's revision. source: the brief's second principle; ADR-D-0053.

## Tasks

### Task_1: The records carry the second principle
- type: docs
- owns:
  - docs/coding-agent-orchestration-harness/decisions/**
  - docs/coding-agent/lessons.md
  - docs/coding-agent/plans/completed/**
- depends_on: []
- description: |
  Run the admission test on a record that replaces ADR-D-0033 with the brief's second principle and its guard (the Worker's side kept as ADR-D-0033 has it; the three-way reading; a design change revises or extends the plan and goes back through the admitting gate for what changed before any is built; never absorbed; reconciled with ADR-D-0053 per A2) and draft it as proposed if it passes; revise ADR-D-0041 in place where its decision on changes after the verdict gains the plan review; touch ADR-D-0051 only where a reason becomes false. On the owner's acceptance by name (the Orchestrator's step after review), the Orchestrator retires ADR-D-0033 atomically and repairs its inbound references in `lessons.md` and the completed plans. Write only what the brief and this plan state.
- acceptance:
  - The admission test's result is reported; if admitted, the replacement meets adr.md's form and lifecycle, says what the brief's second principle and this plan state and nothing more, and takes the lowest free number.
  - ADR-D-0041 says a change to what the plan decides after the verdict goes through the plan review and a new audit of the plan as it stands before the changed item is built.
  - ADR-D-0051 changed only if a reason it gives becomes false; the change named.
  - Each record whose decision, boundary, reasons or reopen conditions changed, and the proposed replacement, is named in the report, so each returns to the owner by name; the retirement of ADR-D-0033 waits for that acceptance and then repairs every inbound reference, proved by an absence search.
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
    detail: "The owner accepts each revised record by its own name, carried by Counsel's relay; Task_2 is not dispatched before that"

### Task_2: The five principles at the place where each acts
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/subagent-strategy/references/prompt-snippets.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/lifecycle-gates.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/final-response-contract.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/value-audit-mandate.md
  - plugins/coding-agent-orchestration-harness/skills/wave-integration/references/integration-checklist.md
  - plugins/coding-agent-orchestration-harness/skills/subagent-report-contract/**
  - plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/review-rubric.md
  - plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/core-principles.md
  - plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/SKILL.md
  - plugins/coding-agent-orchestration-harness/agents/Orchestrator.md
  - plugins/coding-agent-orchestration-harness/claude/agents/harness-orchestrator.md
- depends_on: [Task_1]
- description: |
  Each principle tightened into its one place as the Definition of Done states; the other places point to it; the mandate's positions text admits a revision audited at plan draft; the fixed template byte-identical; the Orchestrator adapters only where they restate the replan action.
- acceptance:
  - Each Definition of Done item on the five principles holds, and each statement of the brief's "The process principles" can be pointed to in exactly one place, the others pointing.
  - The brief's Limits hold: the repository's own text wins on every principle, stated once in `engineering-quality-baselines/SKILL.md` Precedence and pointed to from the five places; no mechanism carries a philosophy between repositories.
  - No new text states a code norm; the lines named in Context as existing code norms are unchanged.
  - The fixed dispatch template is byte-identical; the adapters agree with each other and with the skill text.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "python scripts/validate_harness_package.py; python scripts/run_validation_smoke_tests.py; python skills/subagent-report-contract/scripts/validate_worker_report.py --file ../../tests/coding-agent-orchestration-harness/fixtures/valid-worker-report.yaml; git diff --check"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review against the brief and the accepted records: each principle once at its place; no code norm; adapter parity. This is also the branch's final review."

### Task_3: Close the plan and report the run ready
- type: review
- owns:
  - docs/coding-agent/plans/**
- depends_on: [Task_2]
- description: |
  The Orchestrator closes the plan (closeout audit with its reading) and reports the run ready: branch pushed on the stack, pull request opened under the standing approval, note to Counsel; the run stays open until the owner's acceptance of its stack.
- acceptance:
  - The closeout audit is dispatched by the fixed template and logged; the closeout says plainly that no fixture was run and that the scenarios are his next real run.
  - Every outgoing commit, message and pull request text is swept for machine names and paths and for the names of his other repositories; nothing is merged.
- validation:
  - kind: command
    required: true
    owner: orchestrator
    detail: "package validator and smoke tests; privacy sweep over every commit to be pushed"

## Task Waves (explicit parallel dispatch sets)
- Wave 1: Task_1
- Wave 2: Task_2
- Wave 3: Task_3

## Rollback / Safety
- The branch reverts on its own; no migration, no persisted data.

## Progress Log (append-only)
- 2026-10-08 Brief committed on the run's branch; the plan starts from revision 099d78f.
- 2026-10-08 Plan review (Codex reviewer): NEEDS_REVISION with three MAJOR and three MINOR findings, applied (see the Decision Log); re-review at 3cc5750 APPROVED with no finding open. Plan validator passes. The plan-draft audit follows; execution waits on the owner's answer to the hand-over question.
- 2026-10-08 Plan-draft audit, dispatch text (to a fresh Auditor dispatch on Fable):

  ```text
  You are the value auditor. Read references/value-audit-mandate.md of the orchestration-harness skill and follow it exactly. Position: plan draft. Plan: docs/coding-agent/plans/active/process-principles-in-the-plugin-plan.md. Governing brief: docs/coding-agent/briefs/active/process-principles-in-the-plugin-brief.md. Changes since: none.
  ```

- 2026-10-08 Plan-draft audit, verdict as returned (machine paths redacted; the two comparison lines are logged in the readings file, not here):

  ## Value Audit: Process principles in the plugin (plan draft)

  Note on the dispatch: the user turn carried the fixed template verbatim plus the harness's auto-loaded `engineering-quality-baselines` skill text and the Reviewer role prompt. None of it is an account of the work, so the audit proceeded; recorded here so the Orchestrator can judge whether the skill auto-load should be suppressed on Auditor dispatches.

  - `Position: plan draft`
  - `Documents read:` [machine path redacted] (instructions); [machine path redacted] (instructions); [machine path redacted]\docs\coding-agent\rules\common.md (pointer lines, Standing Approvals; HEAD equals working tree); [machine path redacted]\docs\coding-agent\briefs\active\process-principles-in-the-plugin-brief.md; [machine path redacted]\docs\coding-agent\plans\active\process-principles-in-the-plugin-plan.md; for understanding only: [machine path redacted]\docs\coding-agent-orchestration-harness\decisions\ADR-D-0033-a-worker-acts-alone-only-within-the-acceptance-criteria.md, [machine path redacted]\plugins\coding-agent-orchestration-harness\skills\engineering-quality-baselines\references\core-principles.md (lines 55-79). Readings file opened after grading only. No notes file opened.
  - `Product basis: brief in the product owner's words` (brief line 6: "the product owner's own words in this ratified brief. ebigunso owns the harness"; ratification line 3: "I ratify the brief, hand it over after the current run closes.")
  - `Not audited: engineering side, no engineering philosophy (common.md line 13 reads "none yet", which is not a pointer line)`
  - `Missing inputs: none`
  - `Value documents changed in range: none` (no range at plan draft; the working-tree modification to `first-use-in-a-fresh-repository-brief.md` is another initiative's brief and outside this audit)

  Items (five fields, ` | `-separated):

  - DoD 1, two questions at plan review, once, Plan Gate pointing | maps to the brief | cited | brief principle 1 (gives): "Before a design is accepted, each piece of it is reassessed against the goal that was actually given"; "Where the plugin already asks part of this at plan review, the change is to ask all of it"; means (Limits): "the work tightens the existing text rather than adding a second statement of it" | -
  - DoD 2, three-way reading, never absorbed, guard (review + audit of revised plan before any is built), stated once in replan procedure | maps to the brief | cited | brief principle 2 (gives): "A discovered issue reopens the design; it does not slip in"; sub-statement (gives): "Revising or extending the plan is fine as long as the whole is still kept in line with every criterion set for the work"; means: "a plan revised or extended mid-run goes back through the same gate that admitted it, for what changed, before any of the change is built". The no-brief branch ("or the user's approval of the revision (without one)") is graded under Planner-added 1 | -
  - DoD 3, reports say left out / not verified / scoped down; final response once, Worker summary feeds it | maps to the brief | cited | brief principle 3 (gives): "say what was left out and why, say what was not verified, and scope down out loud rather than quietly building more to be safe"; "The plugin's report contracts are checked against this" | -
  - DoD 4, closing review names evidence artifacts; kept only with the case made; regression tests are not evidence | maps to the brief | cited | brief principle 4 (gives): "Evidence has served once its claim is recorded"; "Those are different from test code that catches regressions"; scenario 4: "A run's closing review names any evidence artifact left in the change" | -
  - DoD 5, guard/limit/compromise states what it is for and when it could go; widens core-principles line 69 | maps to the brief | cited | brief principle 5 (gives): "What is added carries its reason"; means: "tightens the existing text rather than adding a second statement" | -
  - DoD 6, no new code norm; existing code norms left as they are and named to the owner | maps to the brief | inferred | brief Limits constraint 1: "No stance on what code should be enters the plugin"; pass condition: "no new text states a code norm". The brief speaks of new text only; leaving the pre-existing code norms (plan-format rule 8, core-principles §1-2 and line 68, long-horizon-audit deletion bias, ADR-D-0016) in place while the brief's own constraint says "the plugin stays neutral on it" extends the brief; cheap to undo (a report line and an omission) | direction: whether the plugin keeps the code norms it already carries, against the stated neutrality, sets the harness's direction; the owner should see it at closeout
  - DoD 7, ADR-D-0033 replaced by a new record accepted by name, then retired with inbound references repaired; ADR-D-0041 and ADR-D-0051 revised where touched, each returning by name | maps to the brief | cited | brief pass condition: "the existing record on discoveries is consistent with the second principle, revised and returned to him by name where its decision changes"; principle 2 annotation: "The plugin's existing record on discoveries is checked against this and brought in line where it differs"; Limits constraint 3 supports following adr.md's lifecycle (replace, not revise, a record on `main`): "the repository's text is the legible authority and wins". Departure from the pass condition's word "revised" noted: replacement delivers the same return-by-name and is the repository's lifecycle rule. ADR-D-0041/0051 touches follow the guard means ("the plan review and the value audit on the plan as it now stands") | -
  - DoD 8, repository's text wins, stated once in engineering-quality-baselines Precedence, five places pointing | maps to the brief | cited | brief Limits constraint 3: "Where a repository's engineering philosophy or rules say otherwise on any of these, the repository's text is the legible authority and wins"; means: tighten rather than add | -
  - DoD 9, validators and smoke tests pass; Reviewer APPROVED | maps to the brief | cited | brief pass condition (agent-checkable): "the package validators pass". Reviewer approval is the harness's own run gate, not a brief decision | -
  - DoD 10, plan closes, branch published, pull request opened, note to Counsel, nothing merged | maps to the brief (reporting the run) | cited | step 1 passed on standing approval, common.md Standing Approvals: "A finished, reviewed run may publish its branch and open pull requests in this repository without asking first. Merges are not covered and wait for the owner. ... Given and accepted by the repository's owner, ebigunso, on 2026-09-30". The record is present and committed and says what it must; whether the words were said a file cannot show. The note to Counsel is the run's report to the owner by the admitted relay channel (Standing Approvals entry of 2026-10-01), not a publish | -
  - Planner-added 1, without a brief the admitting gate is the user's approval or waiver; the discoveries record's two pause cases widen by one | maps to the brief | inferred | brief means: "goes back through the same gate that admitted it"; brief gives (line 14): "Someone runs the harness in any repository, owned or not". Extends the means to the no-brief case; tightens a stop (adds a return to the user), does not loosen; cheap to undo | -
  - Planner-added 2, a mid-run revision is audited at `plan draft` on the whole revised plan, `Changes since: none`, after plan review | maps to the brief | cited | brief means: "the plan review and the value audit on the plan as it now stands, graded as a whole against the brief and the philosophies and not against the issue that prompted it". The position choice is how | -
  - Non-goal: any code norm, new or existing | maps to the brief | cited | Limits constraint 1 (quoted above); Left out on purpose: "The three principles of the document themselves ... a repository's own" | -
  - Non-goal: mechanism carrying a philosophy between repositories | maps to the brief | cited | Limits constraint 2: "No mechanism for carrying an owner's engineering philosophy between repositories is built" | -
  - Non-goal: Reviewer adapters' output format untouched | maps to the brief | cited | pass condition: "each principle is present once in the plugin text at the place where it acts"; means: tighten rather than add a second statement | -
  - Non-goal: fixed dispatch template unchanged | maps to the brief | inferred | extends the means "tightens the existing text rather than adding a second statement"; cheap to undo | -
  - Non-goal: no fixture; scenarios are his next real run | maps to the brief | cited | pass condition (human-only): "whether, in his next real run, the questions were asked without the harness pushing a stance of its own"; agent-checkable conditions are on the text. Observation, not a grade: the four core scenarios will stand `not yet` at this plan's closeout by design | -
  - Design: tighten one statement per principle at its point of action, pointers elsewhere; alternative (one `process-principles.md`) rejected | maps to the brief | cited | brief means: "the work tightens the existing text rather than adding a second statement of it"; pass condition: "present once in the plugin text at the place where it acts" | -
  - A1: "the smaller design wins" is the outcome of the two questions, not a size target | maps to the brief | cited | brief principle 1: "when the questions pull a draft toward a smaller design, the smaller design is the right one"; Limits constraint 1: "nothing on ... smallness of design as a target" | -
  - A2: ADR-D-0053's experience test stays the value question's test; "change to the design" read as the implementation design in the replan procedure; reconciled in the replacement record | maps to the brief | inferred | brief principle 2: "weighed against the task's scope, what it implies for the shape of the implementation and how it sits under the repository's philosophies". Extends the brief by fixing two readings of "design"; what reaches the owner under ADR-D-0053 is kept, so who decides is not loosened; cheap to undo (the record returns by name) | -
  - Task_1, records carry the second principle; admission test; owner accepts each by name before Task_2 | maps to the brief | cited | pass condition: "revised and returned to him by name where its decision changes"; Limits constraint 3 (repository's text wins) for adr.md's lifecycle; the manual gate tightens | -
  - Task_2, five principles at their places; mandate positions text admits a revision at plan draft; template byte-identical; adapters only where they restate replan | maps to the brief | cited | pass condition: "each principle is present once in the plugin text at the place where it acts; no new text states a code norm"; means: tighten rather than add; guard means for the mandate's positions text | -
  - Task_3, close the plan, report ready: push, pull request, Counsel note, privacy sweep, nothing merged | maps to the brief | cited | standing approval of 2026-09-30 (quoted under DoD 10); brief line 14: "project name redacted by Counsel under his standing privacy rule" supports the sweep for other repositories' names | -
  - Decision Log 1 (2026-10-08): outside a brief the gate is the user's approval or waiver; revision audited at plan draft | maps to the brief | inferred | as Planner-added 1 and 2: means "goes back through the same gate that admitted it"; cheap to undo | -
  - Decision Log 2a: ADR-D-0033 replaced and retired, not revised | maps to the brief | cited | Limits constraint 3 (repository's text wins; adr.md lifecycle); pass condition on the record on discoveries | -
  - Decision Log 2b: hand-over timing recorded as unresolved and asked of the owner; nothing executed until his answer | maps to the brief | cited | brief status line, the owner's words: "I ratify the brief, hand it over after the current run closes." Tightens a stop; who decides stays the owner | -
  - Decision Log 2c: repository-text-wins carried, Precedence section its home | maps to the brief | cited | Limits constraint 3 (quoted under DoD 8) | -
  - Decision Log 2d: compatibility stance `migrate`, readers named | maps to the brief (plugin text) | inferred | no brief statement; extends principle 3's "say what was left out and why" into naming each reader whose meaning changes; cheap to undo | -
  - Decision Log 2e: core-principles line 69 widened, line 68 untouched | maps to the brief | cited | principle 5: "What is added carries its reason"; Limits constraint 1 (line 68 is a code norm and stays) | -
  - Decision Log 2f: the Design's alternative compared as stated | maps to the brief | cited | principle 1: "each piece of it is reassessed against the goal ... what is it for ... what does it cost" | -

  - `Human-only conditions pending: "whether, in his next real run, the questions were asked without the harness pushing a stance of its own"`
  - `Scenarios: none` (plan draft; not a unit's closeout)
  No `ask-now` item. The documents decide every item on the audited side; the plan's authorization under the Plan Gate is decided where that gate states it, not by this verdict.

  How the Orchestrator applied it: no item is `ask-now` and none is `ungraded`. One item is marked `direction`: DoD 6, that the plugin keeps the code norms it already carries (plan-format rule 8, core-principles sections 1 and 2 and line 68, the long-horizon audit's deletion bias, ADR-D-0016) while the brief says the plugin stays neutral on code; it goes ahead as the brief's Limits have it and is shown to the owner at closeout. Inferred calls, as the verdict states them: DoD 6, Planner-added 1, the template non-goal, A2, Decision Log 1 and 2d. The plan review closed with no finding open and this verdict holds nothing; whether the plan is authorized under the ratified brief waits on one thing the verdict does not decide and the Plan Gate does: the brief's hand-over condition, "after the current run closes", asked of the owner through Counsel on 2026-10-08. Nothing is executed before his answer. On the auditor's note about the runtime's auto-loaded skill text in the dispatch, the Orchestrator rules as before that the verdict counts. The comparison set readings apart from grades in class only (DoD 6, DoD 10, Planner-added 2, the template non-goal, Decision Log 2d), corrected in the readings file with nothing to redo.

- 2026-10-08 The owner's answer on the hand-over condition, relayed by Counsel (admitted by the standing approval of 2026-10-01), quoted in full: "The timing was fine." The hand-over stands; with the brief's ratification relayed, the plan review closed with no finding open and the plan-draft verdict holding nothing, the plan is authorized under the ratified brief; this records no approval by the owner. Status set to in progress; Task_1 dispatched. This branch sits on #84's tip as it was when the brief was committed (9db5f13); #84 has since gained small changes 1 to 3, which do not touch this plan's files.
- 2026-10-08 Wave 1, Task_1: Worker report `done`, one YAML block, three files inside the task's `owns`. Admission test on the record replacing ADR-D-0033: passed on all five conditions, the Worker's line and the Orchestrator's handling kept in one record as one question (what happens to a discovery inside authorized work). ADR-D-0057 proposed: the Worker's side carried unchanged; the three-way reading (within the task, fixed in place; a design change, which revises or extends the plan; a matter for later, noted for its own task); never absorbed; a revised plan goes back through the admitting gate for what changed before any of it is built (under a brief the plan review and the value audit on the plan as it stands; without one the plan review and the user's explicit approval or waiver); the scope test and the two questions on the revision; nothing extended on the Orchestrator's judgement alone; reconciled with ADR-D-0053. ADR-D-0041 revised in place (post-verdict change: plan review and a new plan-draft audit before the changed item is built, or the first source), pending header added. ADR-D-0051: the stale reason replaced, pending header added. Worker validation: package validator pass, smoke tests pass, `git diff --check` clean; inbound references to ADR-D-0033 listed for the retirement: `plans/completed/harness-contradictions-and-persistence-plan.md` (two), this plan's quoted verdict (one), and the records ADR-D-0019, 0038, 0052, 0053, superseded 0018 and 0039.
  - Orchestrator rulings on the Worker's questions: "the person directing the work" stays (the term of ADR-D-0040 and 0041); the small change built without a plan stays under Not covered (the brief speaks of a plan revised or extended); ADR-D-0051's kept reopen condition is left for the review to judge.
## Decision Log
- 2026-10-08 Outside a brief the admitting gate is the user's approval or waiver, so a design change returns to the user with the plan review; the discoveries record's two pause cases widen by one (Planner-added 1). A revision is audited at plan draft on the whole revised plan (Planner-added 2).
- 2026-10-08 Plan review applied: ADR-D-0033 is on `main`, so it is replaced by a new complete record and retired, not revised; the hand-over's timing condition recorded as unresolved and asked of the owner; the repository-text-wins constraint carried, with the Precedence section as its home; the compatibility stance is `migrate` with the readers named; the reason line widened is core-principles 69, 68 untouched; the Design's alternative compared as stated.
- 2026-10-08 Proposal, ADR-D-0057 (proposed, awaiting the owner's acceptance by name): "A discovered issue reopens the design and never slips into the change." Decision: as the Progress Log entry above states. Constraint on future work: no text lets a discovery be ruled into the current change, or a revision be built, before the gate that admitted the plan has passed on what changed. Why: a change that grows unseen is the debt agents produce when nobody pushes back; the stack is judged by the whole plan, so what changes it goes back through its gate.
- 2026-10-08 Review of Task_1 (Codex reviewer, at 8d22380): NEEDS_REVISION, one MAJOR (ADR-D-0041 and ADR-D-0057 read as letting the first source's approval stand in for the revision's review; the review is now a prerequisite under either source, the audit or the approval following it) and two MINOR (the proposal moved here into the Decision Log; ADR-D-0051's replacement reason, which the Worker added beyond what the brief states, cut back to the bounded-size reason already accepted, its reopen condition made plain that a revision gets its own review too). The Worker's grouping in ADR-D-0057's Validation reworded the same way.
