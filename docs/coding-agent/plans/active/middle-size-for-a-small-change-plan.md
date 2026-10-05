# Plan: A middle size for a small change

- status: in_progress
- generated: 2026-10-06
- last_updated: 2026-10-06
- work_type: docs

## Goal
- The harness gives what the governing brief `docs/coding-agent/briefs/active/small-change-from-his-word-brief.md` states: a small change that comes from the owner's word is built without a plan, a plan review or a plan-draft audit, keeps the review of the change and one closing value audit, and while its stack is unmerged goes on top of the last branch with no pull request of its own.
- The brief is the requirement and is not restated here; where this plan and the brief differ, the brief governs and the difference is a plan defect.
- This is the only plan of the run recorded in `docs/coding-agent/plans/active/middle-size-for-a-small-change-run.md`. This work is itself of full size: it loosens a gate and proposes a decision record.

## Definition of Done
- The harness text states a third size between trivial and full: under a governing brief, a small change the owner stated in that brief is built with no plan document, no plan review and no plan-draft audit; the review of the change and one closing value audit are kept, and the closing audit holds the change where it went beyond the owner's statement.
- Whether a change is small is stated as the Orchestrator's call, with the closing audit as its guard.
- While the stack the change belongs to is unmerged, the text has it go on top of the stack's last branch with no branch and no pull request of its own.
- Trivial work and work of full size read as at this plan's start revision.
- The accepted records that state the gate (ADR-D-0041, and ADR-D-0040 where its decision or a rejected alternative says otherwise) are revised to carry the small change, and each revised record is accepted by the owner by its own name before any harness text is built on it.
- The value audit's fixed dispatch template is byte-identical to this plan's start revision.
- Package validators and smoke tests pass; the branch has Reviewer `APPROVED`.
- The run closes as `completion-closeout.md` states: its branch published on the stack and a pull request opened under the standing approval, the note to Counsel sent, nothing merged.

## Planner-added requirements
- A small change keeps a short record file of its own: where the owner's statement is, the revision it starts from, the review's result, and the closing audit's dispatch text and verdict. Needed because: the verdict and the review must be logged somewhere a later reader finds them, and the audit's fixed template names a file after `Plan:`; with no plan there is no other home, and changing the template is outside this work. The record carries no tasks, design or definition of done, so it is not a plan.
- The middle size applies only under a governing brief whose ratification reached the session, to a change the owner stated in that brief or an amendment to it. Needed because: the closing audit that guards the size grades against the owner's statement, and without a brief there is no statement on disk for it to grade against.

## Scope / Non-goals
- Scope: `orchestration-harness/SKILL.md` Plan Gate and its references (`lifecycle-gates.md`, `value-level-operation.md`, `value-audit-mandate.md` outside its template block, `completion-closeout.md`, `final-response-contract.md`, `status-model.md`) where each states what a non-trivial change needs; `plan-format` where it states when a plan is required; the two Orchestrator adapters, which restate the gate; the accepted records ADR-D-0040 and ADR-D-0041.
- Non-goals: trivial work; work of full size; goal mode; the two sources of authorization, which stay two; the conditions under which a plan of full size is authorized; the fixed dispatch templates; a rule on test artifacts (the brief leaves it out); running the full suite on small changes to exercise the guards (the brief leaves it out); a version bump (nothing of this stack is released).

## Design
- Chosen: a small change is a third unit of work beside the plan and the goal envelope, authorized by the second source ADR-D-0040 names. Today ADR-D-0041 has that source authorize in plan mode only a plan reviewed and audited before it is built, and ADR-D-0040 rejects a brief that authorizes with no audit judging the fit before the work. The small change alters that: the owner's statement in the brief authorizes the build, and the audit judges the fit once, at the close, before anything is published or reported as done. So the accepted records are revised to say so, in place (neither is merged to `main`), and return to the owner by name; ADR-D-0041 carries the conditions for the small change beside those for a plan, as one decision on when a ratified brief authorizes work in plan mode. The closing audit is dispatched by the unchanged template, whose `Plan:` names the change's short record.
- Alternative A: keep a plan document for a small change, in a one-page proportional form, and drop only its review and draft audit.
- Alternative B: a new record for the small change, with ADR-D-0040 and ADR-D-0041 left as accepted.
- Lenses. structure: chosen keeps one record for when a brief authorizes work in plan mode and adds one short file per small change; A keeps a plan whose content repeats the owner's sentence; B leaves two live records that contradict each other on whether an audit precedes the build. evolution: chosen keeps every rule about plans of full size true as written; A needs each rule about plans to say which form it means; B leaves a later reader to work out which record wins. verification: all three are checked by the same reading of the text and by the next small change the owner gives. operation: chosen and B drop two dispatches and a document per small change; A drops the dispatches only. human: chosen matches the brief's "his statement in the brief is the plan" and its "the accepted record that states it returns to him"; A does not give "no plan document"; B returns no accepted record. safety: in all three nothing is published before the closing audit, and a change beyond the statement is held; the direction this fits is the brief's, the only value document this repository has.
- Why chosen: it gives every statement of the brief and leaves no accepted record saying the opposite.

## Compatibility stance (required if a contract/interface/persisted format is touched)
- surface: the Plan Gate (what a non-trivial change needs before and after it is built).
- stance: break
- justification: the gate is loosened on the owner's word for one class of change. The locatable consumers are sessions in this repository and in Character Memory; neither holds state written under the gate that the change invalidates, and plans in progress are of full size and unaffected.

## Context (workspace)
- Governing brief: `docs/coding-agent/briefs/active/small-change-from-his-word-brief.md`. Its ratification reached this session on 2026-10-06 as a relay from Counsel quoting the owner in full: "Your proposal seems like a good way to handle things. I'll take it." Relays from Counsel are admitted by the Standing Approvals entry of 2026-10-01 in `docs/coding-agent/rules/common.md`.
- Run record: `docs/coding-agent/plans/active/middle-size-for-a-small-change-run.md`. Readings file: `docs/coding-agent/plans/active/middle-size-for-a-small-change-readings.md`. This plan starts from revision: 12b1892.
- Where the gate is stated today: `orchestration-harness/SKILL.md` Plan Gate; `references/lifecycle-gates.md` Plan Gate Details; `references/value-level-operation.md` The Value Audit ("two for each plan"); `references/completion-closeout.md` Closeout Under Value-Level Operation; ADR-D-0040 and ADR-D-0041.
- Research waived: the Orchestrator read those texts and both records in full before drafting.
- The audits of this run: this plan's draft and its close.
- Lessons applied (`docs/coding-agent/lessons.md`): a new branch of a rule is traced through every text that states the rule, its special cases and its stops.

## Open Questions (max 3)
- None.

## Assumptions
- A1: the owner's word for a small change arrives as the several-fit statement did: Counsel writes it into a governing brief with his quoted words, and it reaches the session as a relay. source: the brief, "For a change this small his statement in the brief is the plan."
- A2: once the stack is merged, a small change takes a branch and a pull request as any change does. source: the brief, "While the stack it belongs to is unmerged"; a reading.
- A3: what the brief does not drop stays: the Worker builds, the change closes with the note to Counsel and `candidate ready`, and nothing reaches the remote before the review and the closing audit. source: the brief, "keeps two checks" and "he is told when it is done"; a reading.

## Tasks

### Task_1: The accepted records carry the small change
- type: docs
- owns:
  - docs/coding-agent-orchestration-harness/decisions/**
- depends_on: []
- description: |
  Revise ADR-D-0041, and ADR-D-0040 where its decision, boundary, reasons or a rejected alternative says otherwise, so that the records state when the second source authorizes a small change and what the closing audit holds. Write only what the brief and this plan state. A new record is drafted only if the one-decision test of `durable-docs-authoring/references/adr.md` requires it.
- acceptance:
  - The records state the conditions under which a small change stated by the person directing the work in a ratified brief is built without a plan and stands, and that the closing audit holds it where it went beyond the statement.
  - What the records decide for a plan of full size, for goal mode and for the two sources is unchanged; no live record contradicts another.
  - Each record whose decision, boundary, reasons or reopen conditions changed is named in the Worker's report, so that each returns to the owner by name; inbound references and titles stay consistent.
  - A reason the brief and this plan do not state is reported as a question, not written.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "python scripts/validate_harness_package.py; python scripts/run_validation_smoke_tests.py; git diff --check"
  - kind: review
    required: true
    owner: reviewer
    detail: "The revised records against the form and lifecycle rules of adr.md, against each other and against the brief"
  - kind: manual
    required: true
    owner: user
    detail: "The owner accepts each revised record by its own name, carried by Counsel's relay; Task_2 is not dispatched before that"

### Task_2: The harness text states the middle size
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/**
  - plugins/coding-agent-orchestration-harness/skills/plan-format/**
  - plugins/coding-agent-orchestration-harness/skills/counsel/SKILL.md
  - plugins/coding-agent-orchestration-harness/agents/Orchestrator.md
  - plugins/coding-agent-orchestration-harness/claude/agents/harness-orchestrator.md
  - plugins/coding-agent-orchestration-harness/README.md
- depends_on: [Task_1]
- description: |
  Every text of the plugin that states what a non-trivial change needs states the middle size the brief gives and the accepted record decides, and the closing audit's mandate says what it grades and holds for a small change.
- acceptance:
  - Each Definition of Done item on the text holds, and each statement under the brief's "The middle size" can be pointed to in the text.
  - The middle size is traced through every text that states the Plan Gate, the audit's positions, closeout, publication and the final response, the two Orchestrator adapters included (edited together per `runtime-adapter-contract`), so that none still requires a plan, a plan review or a plan-draft audit of a small change, and none lets a small change skip the review or the closing audit.
  - The closing audit's mandate has a small change graded against the owner's statement and held where it went beyond it; the template block is byte-identical.
  - Trivial work, full-size work and goal mode read as at this plan's start revision.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "python scripts/validate_harness_package.py; python scripts/run_validation_smoke_tests.py; git diff --check"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review against the brief and the accepted records, with the adapter parity check; this is also the branch's final review"

### Task_3: Close the plan and the run
- type: review
- owns:
  - docs/coding-agent/plans/**
- depends_on: [Task_2]
- description: |
  The Orchestrator closes the plan (closeout audit with its reading) and the run: the branch pushed on the stack, a pull request opened under the standing approval, the note to Counsel, `candidate ready`.
- acceptance:
  - The closeout audit is dispatched by the fixed template and logged.
  - Every outgoing commit, message and pull request text is swept for machine-specific names and paths before it is pushed; nothing is merged.
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
- 2026-10-06 Brief committed on the run's branch; the plan starts from revision 12b1892.
- 2026-10-06 Plan review (Codex reviewer): NEEDS_REVISION with two MAJOR findings, applied (see the Decision Log); re-review at f7e676a APPROVED with no finding open. Plan validator passes.
- 2026-10-06 Plan-draft audit, dispatch text (to a fresh Auditor dispatch on Fable):

  ```text
  You are the value auditor. Read references/value-audit-mandate.md of the orchestration-harness skill and follow it exactly. Position: plan draft. Plan: docs/coding-agent/plans/active/middle-size-for-a-small-change-plan.md. Governing brief: docs/coding-agent/briefs/active/small-change-from-his-word-brief.md. Changes since: none.
  ```

- 2026-10-06 Plan-draft audit, verdict as returned (machine paths redacted; the two comparison lines are logged in the readings file, not here):

  ## Value audit verdict: middle-size-for-a-small-change-plan.md, plan draft

  Every item on the audited side is graded; none is `ask-now` and none is `ungraded`. Three items are `inferred` with the `direction` mark.

  Two procedure disclosures, for the Orchestrator to rule on:
  - **First Step order.** I opened the plan and the brief in the same step in which I located the mandate, so before reading the mandate to its end. No notes file was opened, and the readings file was opened only after the grades were fixed, so the mandate's stated void condition did not occur. If you hold the order lapse to void the audit, dispatch again.
  - **Dispatch text.** The dispatch was the fixed template verbatim. The runtime appended the `engineering-quality-baselines` skill text and a hook's mode text to it; neither is an account of the work, so I did not return the audit ungraded for extra text.

  ### Verdict record

  Position: plan draft

  Documents read: `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/value-audit-mandate.md` and `plugins/coding-agent-orchestration-harness/skills/value-documents/SKILL.md` (instructions); `docs/coding-agent/briefs/active/small-change-from-his-word-brief.md`; `docs/coding-agent/plans/active/middle-size-for-a-small-change-plan.md`; `docs/coding-agent/rules/common.md` (pointer lines and Standing Approvals, at HEAD, unmodified); ADR-D-0040 and ADR-D-0041 under `docs/coding-agent-orchestration-harness/decisions/` and four `Counsel` / `candidate ready` lines of `completion-closeout.md` (all to understand, not as support); `docs/coding-agent/plans/active/middle-size-for-a-small-change-readings.md` (after grading only).

  Product basis: brief in the product owner's words ("ebigunso owns the harness; no product philosophy and no engineering philosophy exist for this repository"; ratified 2026-10-06: "Your proposal seems like a good way to handle things. I'll take it.")

  Not audited: engineering side; it has no document (`common.md`: "Engineering philosophy: none yet", which is not a pointer line).

  Missing inputs: none

  Value documents changed in range: none (plan draft; no range)

  Items:

  - DoD 1: a third size with no plan, plan review or plan-draft audit; the review and one closing audit kept; the audit holds what went beyond the statement | maps to the brief | cited | brief: "A small change that comes from his word keeps two checks: the review of the change, and one closing value audit, which checks that what was built is what he said and nothing more."; "It drops the separate plan, the plan's review and the plan-draft audit. For a change this small his statement in the brief is the plan."; "This loosens a gate, and he was told so before he took it." | -
  - DoD 2: smallness is the Orchestrator's call, guarded by the closing audit | maps to the brief | cited | brief: "Whether a change is small is the Orchestrator's call. The guard on that call is the closing audit: where the change went beyond his statement, the audit holds it." | -
  - DoD 3: on top of the stack's last branch, no branch or pull request of its own, while the stack is unmerged | maps to the brief | cited | brief: "While the stack it belongs to is unmerged, it takes no branch and no pull request of its own; it goes on top of the last one." | -
  - DoD 4: trivial and full-size work read as at the start revision | maps to the brief | cited | brief: "Trivial work and work of full size are handled as they are today." | -
  - DoD 5: ADR-D-0041, and ADR-D-0040 where it says otherwise, revised, and each accepted by the owner by name before harness text is built on it | maps to the brief | cited | brief: "It changes the Plan Gate, so the accepted record that states it returns to him for acceptance by name."; pass condition "the record that states the Plan Gate is accepted by him by name before the change lands". The plan's "before any harness text is built on it" tightens the pass condition. The acceptance stays the owner's own act, and no standing approval is relied on for it. | -
  - DoD 6: the fixed dispatch template byte-identical | maps to the brief | inferred | extends brief: "keeps two checks: the review of the change, and one closing value audit"; "Trivial work and work of full size are handled as they are today."; cheap to undo | -
  - DoD 7: validators and smoke tests pass; Reviewer `APPROVED` | maps to the brief | cited | brief, pass conditions: "the package validators pass". The Reviewer approval is the run's own mechanics and tightens. | -
  - DoD 8: the run closes with its branch published on the stack, a pull request opened, the note to Counsel sent, nothing merged | maps to the brief | cited | Standing approval, `common.md`: "A finished, reviewed run may publish its branch and open pull requests in this repository without asking first. Merges are not covered and wait for the owner. ... Given and accepted by the repository's owner, ebigunso, on 2026-09-30, relayed by Counsel: \"The common rule proposed, accepted.\"" The entry carries its record and is committed; whether the quoted words were said a file cannot show. I read the note to Counsel as the run's report to the owner's own session, not as an outward-facing message. If that reading is wrong, no standing approval covers the note. | -
  - Planner-added 1: a small change keeps a short record file of its own, named after `Plan:` in the template | maps to the brief | inferred | extends brief: "one closing value audit, which checks that what was built is what he said and nothing more"; "It drops the separate plan"; core scenario "with no plan document". As described the file holds no tasks, design or definition of done. Cheap to undo. | direction: every small change still leaves a document of its own, where the owner asked for less ceremony
  - Planner-added 2: the middle size applies only under a governing brief whose ratification reached the session, to a change stated in that brief or an amendment | maps to the brief | inferred | extends brief: "For a change this small his statement in the brief is the plan."; "A small change that comes from his word". The brief does not say "only": a one-sentence change he states directly to the Orchestrator outside a brief is excluded by the plan, not by the brief. Tightens; cheap to undo. | direction: whether his word must pass through Counsel and a brief to get the middle size
  - Non-goal: trivial work | maps to the brief | cited | brief: "Trivial work and work of full size are handled as they are today." | -
  - Non-goal: work of full size | maps to the brief | cited | same statement | -
  - Non-goal: the conditions under which a plan of full size is authorized | maps to the brief | cited | same statement | -
  - Non-goal: goal mode | maps to the brief | inferred | extends the same statement; the brief speaks only of the plan, its review and its audits; cheap to undo | -
  - Non-goal: the two sources of authorization stay two | maps to the brief | inferred | extends brief: "For a change this small his statement in the brief is the plan." (the ratified brief stays the source); cheap to undo | -
  - Non-goal: the fixed dispatch templates | maps to the brief | inferred | as DoD 6 | -
  - Non-goal: a rule on test artifacts | maps to the brief | cited | brief, Left out on purpose: "A rule on test artifacts. *(told 2026-10-06: \"No recorded rule required yet.\")*" | -
  - Non-goal: running the full suite on small changes to exercise the guards | maps to the brief | cited | brief, Left out on purpose: "Running the full suite on small changes to exercise the guards." | -
  - Non-goal: no version bump | maps to the brief | inferred | extends brief: "While the stack it belongs to is unmerged"; nothing changes; cheap to undo | -
  - A1: his word for a small change arrives as a statement Counsel writes into a governing brief with his quoted words, relayed | maps to the brief | inferred | extends brief: "For a change this small his statement in the brief is the plan."; cheap to undo | direction: the same decision as Planner-added 2
  - A2: once the stack is merged a small change takes a branch and a pull request as any change does | maps to the brief | inferred | extends brief: "While the stack it belongs to is unmerged, it takes no branch and no pull request of its own"; cheap to undo | -
  - A3: what the brief does not drop stays (the Worker builds, the note to Counsel and `candidate ready`, nothing reaches the remote before the review and the closing audit) | maps to the brief | cited | brief: "keeps two checks: the review of the change, and one closing value audit"; core scenario "It is built on top of the stack, reviewed and audited once at its close, with no plan document and no new pull request, and he is told when it is done." | -
  - Task_1: the accepted records carry the small change; the owner accepts each by name before Task_2 is dispatched | maps to the brief | cited | brief: "It changes the Plan Gate, so the accepted record that states it returns to him for acceptance by name."; "Trivial work and work of full size are handled as they are today." | -
  - Task_2: the harness text states the middle size; the closing audit's mandate grades a small change against the owner's statement | maps to the brief | cited | brief, "The middle size", all four statements as quoted under DoD 1 to 3; "where the change went beyond his statement, the audit holds it."; "Trivial work and work of full size are handled as they are today." The gate is loosened only as far as the brief gives. | -
  - Task_3: close the plan and the run (closeout audit, push on the stack, pull request, note to Counsel, `candidate ready`, privacy sweep, nothing merged) | maps to the brief | cited | Standing approval as quoted under DoD 8, with the same note on the message to Counsel. The privacy sweep tightens. | -
  - Decision Log 1: the accepted records are revised in place and return by name, not a new record beside them | maps to the brief | cited | brief: "the accepted record that states it returns to him for acceptance by name" | -
  - Decision Log 2: Task_2 owns the two Orchestrator adapters and names its skill paths | internal mechanics | not audited | the engineering side has no document; the irreversible-or-outward-facing test was run and does not catch it | -

  Human-only conditions pending: "the next small change he gives, judged by whether it felt proportionate." Nothing in the plan lets a proxy settle it.

  Scenarios: none

  ### Observations outside the grades

  - Task_2 `owns` lists `skills/counsel/SKILL.md` and the plugin `README.md`, which the plan's Scope section does not name. If the build changes how Counsel writes a small change into a brief, that change is user-facing and will be graded at closeout against the brief.
  - Planner-added 1 exists only because the template is held fixed (a non-goal the brief does not ask for). The alternative of no per-change file was not weighed in the Design section. That is the reason for the `direction` mark.

  How the Orchestrator applied it: no item is `ask-now` and none is `ungraded`. With the brief's ratification relayed by Counsel under the standing approval, the plan review closed with no finding open, and this verdict, the plan is authorized under the ratified brief; this records no approval by the owner. No item rests on a provisional statement. Inferred calls, as the verdict states them: DoD 6, the non-goals on goal mode, the two sources, the templates and the version bump, A2, and three marked `direction`: Planner-added 1 (every small change still leaves a document of its own), Planner-added 2 and A1 (whether his word must pass through Counsel and a brief to get the middle size). The marked items go ahead and are shown to the owner at closeout as the closeout verdict states them. On the auditor's two procedural points the Orchestrator rules as in the earlier runs that the verdict counts: the readings file was opened only after the grades. The note to Counsel is the harness's own carrier between the owner's sessions. The comparison set readings apart from grades in class only (DoD 6, DoD 8, four non-goals, A3), corrected in the readings file with nothing to redo. The auditor's observation that Task_2 owns two files the Scope does not name is taken: they are owned so that a consumer found there can be traced, and a change to either is graded at closeout.

## Decision Log
- 2026-10-06 Which record: the first draft proposed a new record and left ADR-D-0040 and ADR-D-0041 as accepted. The plan review found that wrong: ADR-D-0041 has a plan reviewed and audited before it is built, ADR-D-0040 rejects a brief authorizing with no audit judging the fit first, and the brief says the accepted record returns to the owner. The accepted records are revised in place and return by name.
- 2026-10-06 Plan review, second finding applied: Task_2 owns the two Orchestrator adapters and names its skill paths.
