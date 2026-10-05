# Plan: The value audit at a plan's draft and close

- status: done
- generated: 2026-10-05
- last_updated: 2026-10-05
- work_type: docs

## Goal
- The harness gives what the governing brief `docs/coding-agent/briefs/active/value-level-operation-brief.md` states, as amended on 2026-10-05, in its section "Value audit": in a run of plans the audit runs at each plan's draft and at each plan's close, and nowhere between; a plan review catches a plan that is unacceptably long.
- The brief is the requirement and is not restated here; where this plan and the brief differ, the brief governs and the difference is a plan defect.
- This is the only plan of the run recorded in `docs/coding-agent/plans/active/audit-at-plan-draft-and-close-run.md`.

## Definition of Done
- In a plan-mode run the plugin text has the value audit dispatched at a plan's draft and at its close and at no other moment; no text asks for an audit at a wave boundary of a plan.
- A goal-mode run's audit moments are as the accepted record on goal mode states, unchanged.
- The plan-review instructions have the Reviewer report a plan that is unacceptably long.
- The value audit's fixed dispatch template is byte-identical to this plan's start revision.
- Package validators and smoke tests pass; the branch has Reviewer `APPROVED`.
- The run closes as `completion-closeout.md` states: its branch published on the stack and a pull request opened under the standing approval, the note to Counsel sent, nothing merged.

## Planner-added requirements
- One plugin version bump. Needed because: the package validator requires the three manifests to agree per installed version.

## Scope / Non-goals
- Scope: `orchestration-harness/references/value-level-operation.md` and `value-audit-mandate.md`, `wave-integration/references/integration-checklist.md`, `subagent-strategy/references/prompt-snippets.md`, the three manifests.
- Non-goals: the fixed dispatch template, whose `wave boundary` fill-in stays and names an assessment event in a goal run; goal mode; any decision record (none fixes the audit's positions); a numeric limit on a plan's length.

## Design
- Chosen: the plan-mode text names two audit positions, a plan's draft and its close; the wave-boundary step and what serves it are removed; the plan-review instructions gain the brief's check on a plan's length, in the brief's words, with the fact that no audit runs between a plan's draft and its close offered to the Reviewer as the thing to weigh.
- Alternative: keep the wave-boundary position in the text and make it conditional, dispatched only for a wave the Orchestrator judges risky.
- Lenses. structure: chosen removes a position and its bookkeeping (the revision recorded at each wave); the alternative keeps both and adds a judgement. evolution: chosen leaves one rule to maintain; the alternative leaves a condition to tune. verification: chosen is checked by a search that finds no wave-boundary audit of a plan; the alternative cannot be checked from the text. operation: chosen costs two audits a plan; the alternative costs between two and one per wave. human: with the chosen design drift inside a plan shows at its close, which is why the plan review looks at length; the alternative shows it sooner where the Orchestrator guessed right. safety: the alternative has the audited party decide when it is audited.
- Why chosen: the brief says "nowhere between", and the alternative puts the choice of when to audit with the party being audited.

## Compatibility stance (required if a contract/interface/persisted format is touched)
- surface: when the value audit runs in a plan-mode run; what a plan review reports.
- stance: break
- justification: the consumers that can be located are this repository's own runs and Character Memory with the plugin installed; the owner asked for the change in cadence by amendment. A plan-mode run stops dispatching an audit at wave boundaries. Preserved: a goal-mode run's audit moments, and the fixed dispatch template, whose `wave boundary` value keeps its one remaining consumer, an assessment event in a goal run.

## Context (workspace)
- Governing brief: `docs/coding-agent/briefs/active/value-level-operation-brief.md`, ratified 2026-09-30; the amendment of 2026-10-05 carries the owner's quoted words beside it, and Counsel relayed on 2026-10-05 his word on when it is built: "Yes, do it first before the next one prepared."
- Run record: `docs/coding-agent/plans/completed/audit-at-plan-draft-and-close-run.md`. Readings file: `docs/coding-agent/plans/completed/audit-at-plan-draft-and-close-readings.md` (both under `active/` until the run closed). This plan starts from revision: 2e237902.
- Where the position is stated today: `value-level-operation.md` (the list of positions; "Record the revision at each wave's dispatch as well"), `value-audit-mandate.md` (the artifact "wave boundary and closeout"; the first paragraph), `wave-integration/references/integration-checklist.md` (the wave-boundary audit step). The goal-run section of the mandate uses the template's `wave boundary` fill-in for an assessment event and stays.
- Research waived: the five places were found by search of the plugin, the decision records and the rule files; no record or rule file states the position.
- This run itself is audited at this plan's draft and close only, by the brief as amended.
- Design record consulted: ADR-D-0052 (leaves the positions to the workflow text), ADR-D-0056 (goal-run moments; kept).

## Open Questions (max 3)
- None.

## Assumptions
- A1: the template's `Position` fill-in keeps its three values; in a plan-mode run `wave boundary` is not used. source: ADR-D-0050 and ADR-D-0056 keep the template unchanged.

## Tasks

### Task_1: Two positions in a plan-mode run; a long plan is reported at plan review
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/value-level-operation.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/value-audit-mandate.md
  - plugins/coding-agent-orchestration-harness/skills/wave-integration/references/integration-checklist.md
  - plugins/coding-agent-orchestration-harness/skills/subagent-strategy/references/prompt-snippets.md
  - plugins/coding-agent-orchestration-harness/.claude-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.codex-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.github/plugin/plugin.json
- depends_on: []
- description: |
  The plan-mode text states two audit positions, a plan's draft and its close, and no audit between; every line that asks for or serves a wave-boundary audit of a plan is removed or reworded; the goal-run text and the fixed template stay. The plan-review snippet has the Reviewer report a plan that is unacceptably long, in the brief's words, and tells the Reviewer the one fact that bears on it: under value-level operation no audit runs between a plan's draft and its close.
- acceptance:
  - No plugin text has a value audit dispatched at a wave boundary of a plan, and nothing left depends on one (the revision recorded at each wave's dispatch, the checklist step).
  - The goal-run section of the mandate and the Fixed Dispatch Template block are byte-identical to this plan's start revision.
  - The plan-review snippet states the check on a plan's length once.
  - The three manifests agree at the next version.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "python scripts/validate_harness_package.py; python scripts/run_validation_smoke_tests.py; git diff --check; hash of the template block against the start revision"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review against the brief's amended lines and this task's acceptance"

### Task_2: Close the plan and the run
- type: review
- owns:
  - docs/coding-agent/plans/**
- depends_on: [Task_1]
- description: |
  The Orchestrator closes the plan (closeout audit with its reading; the review of Task_1 is the branch's final review) and the run: the branch pushed on the stack, a pull request opened under the standing approval, the note to Counsel, `candidate ready`.
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

## Rollback / Safety
- The branch reverts on its own; no migration, no persisted data.

## Progress Log (append-only)
- 2026-10-05 Plan review (Codex reviewer): NEEDS_REVISION with three minor findings, applied (see the Decision Log); re-review APPROVED with no finding open. Plan validator passes.
- 2026-10-05 Plan-draft audit, dispatch text (to a fresh Auditor dispatch on Fable):

  ```text
  You are the value auditor. Read references/value-audit-mandate.md of the orchestration-harness skill and follow it exactly. Position: plan draft. Plan: docs/coding-agent/plans/active/audit-at-plan-draft-and-close-plan.md. Governing brief: docs/coding-agent/briefs/active/value-level-operation-brief.md. Changes since: none.
  ```

- 2026-10-05 Plan-draft audit, verdict as returned (the two comparison lines are logged in the readings file, not here):

  Value audit verdict record (plan draft). Every graded item is `cited`; there is no `ask-now` and no `ungraded` item. The engineering side has no document, so its items are `not audited`.

  - `Position: plan draft`
  - `Documents read: docs/coding-agent/briefs/active/value-level-operation-brief.md; docs/coding-agent/plans/active/audit-at-plan-draft-and-close-plan.md; docs/coding-agent/rules/common.md (sections "Repository Reference Documents" for pointer lines and "Standing Approvals", checked against HEAD, file unmodified in the working tree); instructions only: plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/value-audit-mandate.md, plugins/coding-agent-orchestration-harness/skills/value-documents/SKILL.md`
  - `Product basis: brief in the product owner's words` ("product basis: the product owner's own words in this ratified brief. ebigunso owns the harness; no product philosophy and no engineering philosophy exist for this repository yet.")
  - `Not audited: engineering side; common.md carries no pointer line to an engineering philosophy (nor to a product philosophy), so internal-mechanics items have no document`
  - `Missing inputs: none`
  - `Value documents changed in range: none` (plan draft, no range; the 2026-10-05 amendment is committed at 2e237902 and carries the owner's quoted words with the date beside each of the two amended lines)

  Items (`item | scope | grade | support | notes`):

  - DoD 1: plan-mode audit at a plan's draft and close and at no other moment; no text asks for a wave-boundary audit of a plan | maps to the brief | cited | brief, Value audit: "It runs by position: at each plan's draft and at each plan's close, and nowhere between." | -
  - DoD 2: a goal-mode run's audit moments unchanged | maps to the brief | cited | brief, Value audit: "In a goal-mode run it runs as the accepted record on goal mode states." | -
  - DoD 3: plan-review instructions have the Reviewer report a plan that is unacceptably long | maps to the brief | cited | brief, Value audit: "A plan review catches a plan that is unacceptably long." | -
  - DoD 4: fixed dispatch template byte-identical to the start revision | internal mechanics | not audited | - | -
  - DoD 5: package validators and smoke tests pass; Reviewer APPROVED | maps to the brief | cited | brief, Pass conditions: "the package validators pass" | the Reviewer approval part is internal mechanics, not audited
  - DoD 6: run closes with branch published on the stack, pull request opened under the standing approval, note to Counsel sent, nothing merged | maps to the brief | cited | common.md, Standing Approvals: "A finished, reviewed run may publish its branch and open pull requests in this repository without asking first. Merges are not covered and wait for the owner." (in effect: committed, records the giver and the acceptance "The common rule proposed, accepted." dated 2026-09-30; whether those words were said is not something the file can show); brief: "Merges happen only on your explicit instruction for each pull request."; brief: "Closeout reports "candidate ready": evidence for agent-checkable conditions, human-only conditions pending, and the collected judgement calls."; brief: "When the Orchestrator needs his authority or judgement it escalates to Counsel, and Counsel brings it to him." | the note to Counsel is read as the run's own reporting channel to the owner, not as outward-facing; the publish and the pull request pass step 1 on the standing approval
  - Planner-added: one plugin version bump across the three manifests | internal mechanics | not audited | - | -
  - Non-goal: the fixed dispatch template and its `wave boundary` fill-in stay | internal mechanics | not audited | - | -
  - Non-goal: goal mode | maps to the brief | cited | brief: "In a goal-mode run it runs as the accepted record on goal mode states." | -
  - Non-goal: no decision record changed or proposed | maps to the brief | cited | brief: "Decision records (ADRs) stay for architectural forks; the why names the tenet served." | the plan's claim that no record fixes the positions was checked by search: no decision record or rule file mentions a wave-boundary audit
  - Non-goal: no numeric limit on a plan's length | maps to the brief | cited | brief: "A plan review catches a plan that is unacceptably long." | the plan adds nothing to the statement
  - A1: the template's Position fill-in keeps its three values; `wave boundary` unused in a plan-mode run | internal mechanics | not audited | - | -
  - Task_1: two positions in the plan-mode text; wave-boundary lines and what serves them removed; plan-review snippet reports an unacceptably long plan and states that no audit runs between draft and close | maps to the brief | cited | brief: "It runs by position: at each plan's draft and at each plan's close, and nowhere between."; brief: "A plan review catches a plan that is unacceptably long." | the fact offered to the Reviewer restates the first line
  - Task_2: close the plan and the run (closeout audit by the fixed template, push, pull request, note to Counsel, `candidate ready`, privacy sweep, nothing merged) | maps to the brief | cited | brief: "at each plan's close"; common.md standing approval as quoted at DoD 6 (same caveat); brief: "Closeout reports "candidate ready""; brief: "machine-specific user names and paths must not leak, and anything of that kind in a quote is redacted before it ever reaches the remote."; brief: "Merges happen only on your explicit instruction for each pull request." | -
  - Decision Log 1: requirement challenge: no record proposed, no numeric limit, no definition of "unacceptably long", the Reviewer judges | maps to the brief | cited | brief: "A plan review catches a plan that is unacceptably long."; brief: "Decision records (ADRs) stay for architectural forks" | -
  - Decision Log 2: draft-plan review findings applied (design comparison, compatibility stance `break`, planner-added length measure dropped) | maps to the brief | cited | brief: "A plan review catches a plan that is unacceptably long." (the dropped measure leaves the brief's words); brief: "It runs by position: at each plan's draft and at each plan's close, and nowhere between." (the stance breaks only the cadence the owner amended) | the design-form and stance bookkeeping is internal mechanics

  - `Human-only conditions pending: "the discussion with Counsel does not feel like filling in a form"; "the stops during a run were each right, neither skipping a decision that needed him nor stopping on something the documents answered"; "the closeout let him judge by behaviour, with implementation detail only where his judgement needed it and the reason stated"; "judged through first real use on Character Memory"` (the plan lets no proxy settle any of them)
  - `Scenarios: none`
  Notes outside the record:
  - The dispatch text matched the fixed template. The session also carried harness-injected skill and hook text (engineering-quality-baselines, ponytail); neither is an account of the work, so the audit was graded.
  - The plan's Context quotes a relay, "Yes, do it first before the next one prepared." That quote is not in the brief and was disregarded. No grade depends on it.
  - Discussion notes were not opened. The readings file was opened once, after the grades were fixed.

  How the Orchestrator applied it: no item is `ask-now` and none is `ungraded`. With the brief ratified on 2026-09-30, its amendment of 2026-10-05 carrying the owner's words, the plan review closed with no finding open, and this verdict, the plan is authorized under the ratified brief; this records no approval by the owner. No item rests on a provisional statement, so nothing goes to Counsel. The comparison set four readings apart from their grades in class only (things read as extensions that the audit holds to be mechanics or stated by the brief); the readings are corrected in the readings file and nothing in the plan needs redoing for them.
- 2026-10-05 Wave 1, Task_1: Worker report `done`, one YAML block, every changed file inside the task's `owns`. The plan-mode text names two audit positions, plan draft and closeout, with none between; the wave-boundary entry, the revision recorded at each wave's dispatch and the checklist's wave-boundary step are gone; the mandate keeps one line telling an auditor that `wave boundary` is a goal run's assessment event; the plan-review snippet reports a plan that is unacceptably long; manifests at 0.29.0. Worker validation: package validator pass, smoke tests pass, `git diff --check` clean, the Fixed Dispatch Template block and the mandate's goal-run section the same hash at the start revision, HEAD and the working tree; a search of the plugin finds `wave boundary` only in the template, the goal-run mapping and that one line. Orchestrator edit at integration: the lesson of this morning on dispatching the wave-boundary audit before the next wave is marked as overtaken by the amendment. Review: dispatched next.
  - Judgement calls (Task_1): the sentence that the next audit grades a corrected item is left as it reads, since it is true for both modes; the mandate's pointer for `wave boundary` sits in the list of artifacts by position.
- 2026-10-05 Review of Task_1, also the branch's final review (Codex reviewer, range from this plan's start revision): APPROVED, no finding. Validators and smoke tests pass on the committed snapshot; the goal-run section and the template byte-identical to the start revision; privacy clean over the range and its commit messages. Task_1 is done.
- 2026-10-05 Closeout audit, dispatch text (to a fresh Auditor dispatch on Fable):

  ```text
  You are the value auditor. Read references/value-audit-mandate.md of the orchestration-harness skill and follow it exactly. Position: closeout. Plan: docs/coding-agent/plans/active/audit-at-plan-draft-and-close-plan.md. Governing brief: docs/coding-agent/briefs/active/value-level-operation-brief.md. Changes since: 2e237902.
  ```
- 2026-10-05 Closeout audit, first dispatch: returned ungraded by the auditor itself. It named the readings file as an explicit path in a range diff, so the file was printed before any grade; it recognised the breach, graded nothing and asked for a fresh dispatch. Nothing is logged as a verdict and the run record is unchanged. A gate on the position: the same template is dispatched again, new (text as above). This is the second auditor in two days to open a readings file before grading; recorded in the readings file as a finding, with the auditor's suggestion that the mandate give the literal exclude pathspecs to copy.

- 2026-10-05 Closeout audit, second dispatch, verdict as returned (the two comparison lines are logged in the readings file, not here):

  Value audit verdict record (closeout). Every graded item is `cited` or `inferred`; there is no `ask-now` and no `ungraded` item. The engineering side has no document, so its items are `not audited`. No judgement call is marked `direction`.

  - `Position: closeout`
  - `Documents read: docs/coding-agent/briefs/active/value-level-operation-brief.md; docs/coding-agent/plans/active/audit-at-plan-draft-and-close-plan.md; docs/coding-agent/plans/active/audit-at-plan-draft-and-close-run.md (run record, for prior scenario states); the range 2e237902..working tree, read with git under exclude pathspecs for docs/coding-agent/briefs/*-notes.md and docs/coding-agent/**/*-readings.md; docs/coding-agent/briefs/active/setup-names-what-is-missing-brief.md (untracked, in range); docs/coding-agent/rules/common.md at HEAD (sections "Repository Reference Documents" and "Standing Approvals"; file unmodified in the working tree); to understand the changes only: completion-closeout.md, lifecycle-gates.md and value-level-operation.md of the orchestration-harness skill (searched for what still depends on a wave-boundary audit); instructions only: plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/value-audit-mandate.md, plugins/coding-agent-orchestration-harness/skills/value-documents/SKILL.md; after grading only: docs/coding-agent/plans/active/audit-at-plan-draft-and-close-readings.md`
  - `Product basis: brief in the product owner's words` ("product basis: the product owner's own words in this ratified brief. ebigunso owns the harness; no product philosophy and no engineering philosophy exist for this repository yet.")
  - `Not audited: engineering side; common.md at HEAD carries no pointer line to an engineering philosophy (nor to a product philosophy), so internal-mechanics items have no document`
  - `Missing inputs: none`
  - `Value documents changed in range: docs/coding-agent/briefs/active/setup-names-what-is-missing-brief.md (new, untracked in the working tree; it carries a ratification record dated 2026-10-05; it is not the governing brief and no item of this plan relies on it). The governing brief is unchanged in the range (its amendment is the start revision 2e237902 itself). No pointer line removed or changed.`

  Items (`item | scope | grade | support | notes`):

  Plan items

  - DoD 1: plan-mode audit at a plan's draft and close and at no other moment | maps to the brief | cited | brief, Value audit: "It runs by position: at each plan's draft and at each plan's close, and nowhere between." | -
  - DoD 2: a goal-mode run's audit moments unchanged | maps to the brief | cited | brief: "In a goal-mode run it runs as the accepted record on goal mode states." | -
  - DoD 3: plan-review instructions have the Reviewer report a plan that is unacceptably long | maps to the brief | cited | brief: "A plan review catches a plan that is unacceptably long." | -
  - DoD 4: fixed dispatch template byte-identical to the start revision | internal mechanics | not audited | - | -
  - DoD 5: package validators and smoke tests pass; Reviewer APPROVED | maps to the brief | cited | brief, Pass conditions: "the package validators pass" | the Reviewer approval part is internal mechanics, not audited
  - DoD 6: run closes with branch published on the stack, pull request opened under the standing approval, note to Counsel, nothing merged | maps to the brief | cited | common.md, Standing Approvals: "A finished, reviewed run may publish its branch and open pull requests in this repository without asking first. Merges are not covered and wait for the owner." (in effect: committed at HEAD, records the giver and the acceptance "The common rule proposed, accepted." dated 2026-09-30; whether those words were said is not something a file can show); brief: "Merges happen only on your explicit instruction for each pull request."; brief: "Closeout reports "candidate ready": evidence for agent-checkable conditions, human-only conditions pending, and the collected judgement calls."; brief: "When the Orchestrator needs his authority or judgement it escalates to Counsel, and Counsel brings it to him." | the publish and the pull request pass step 1 on the standing approval; the note to Counsel is read as the run's own carrier to the owner, not as outward-facing. Neither has happened yet: the branch is on no remote and no pull request exists for it
  - Planner-added: one plugin version bump | maps to the brief | inferred | extends brief: "the package validators pass" (the three manifests must agree) and "It ships as a first version." | - (the installed version number is something a user of the plugin can see, so this is graded and not left as mechanics; a revert restores 0.28.0, nothing is published)
  - Non-goal: the fixed dispatch template and its `wave boundary` fill-in stay | internal mechanics | not audited | - | -
  - Non-goal: goal mode | maps to the brief | cited | brief: "In a goal-mode run it runs as the accepted record on goal mode states." | -
  - Non-goal: no decision record changed or proposed | maps to the brief | cited | brief: "Decision records (ADRs) stay for architectural forks; the why names the tenet served." | the range changes no decision record
  - Non-goal: no numeric limit on a plan's length | maps to the brief | cited | brief: "A plan review catches a plan that is unacceptably long." | -
  - A1: the template's Position fill-in keeps its three values | internal mechanics | not audited | - | -
  - Task_1 | maps to the brief | cited | brief: "It runs by position: at each plan's draft and at each plan's close, and nowhere between."; brief: "A plan review catches a plan that is unacceptably long." | -
  - Task_2: close the plan and the run | maps to the brief | cited | brief: "at each plan's close"; common.md standing approval as quoted at DoD 6 (same caveat); brief: "Closeout reports "candidate ready""; brief: "machine-specific user names and paths must not leak, and anything of that kind in a quote is redacted before it ever reaches the remote."; brief: "Merges happen only on your explicit instruction for each pull request." | -
  - Decision Log 1: requirement challenge (no record, no numeric limit, the Reviewer judges) | maps to the brief | cited | brief: "A plan review catches a plan that is unacceptably long."; brief: "Decision records (ADRs) stay for architectural forks" | - (judgement call; not direction)
  - Decision Log 2: draft-plan review findings applied (design comparison, stance `break`, the added length measure dropped) | maps to the brief | cited | brief: "A plan review catches a plan that is unacceptably long."; brief: "It runs by position: at each plan's draft and at each plan's close, and nowhere between." | - (judgement call; not direction; the design-form bookkeeping is internal mechanics)

  Changes in the range

  - value-level-operation.md: Positions are two for each plan with no audit dispatched between them; the wave-boundary entry is removed | maps to the brief | cited | brief: "It runs by position: at each plan's draft and at each plan's close, and nowhere between." | the stop removed is the one the owner's amendment of 2026-10-05 removes, so the text is brought to the brief and nothing is loosened relative to it
  - value-level-operation.md: the revision is no longer recorded at each wave's dispatch | internal mechanics | not audited | - | -
  - value-level-operation.md: a gate on the position no longer reads "the next wave is not dispatched" | maps to the brief | cited | brief: "It runs by position: at each plan's draft and at each plan's close, and nowhere between." | follows from there being no audit between; the plan-draft and closeout gates stay as they were
  - value-audit-mandate.md: first paragraph names plan draft and closeout for a plan-mode run and leaves a goal run's positions to Goal-Mode Runs | maps to the brief | cited | brief: "It runs by position: at each plan's draft and at each plan's close, and nowhere between. In a goal-mode run it runs as the accepted record on goal mode states." | -
  - value-audit-mandate.md: "Artifact by position" lists closeout alone and adds a line that `wave boundary` is a goal-mode run's assessment event | maps to the brief | cited | brief: "In a goal-mode run it runs as the accepted record on goal mode states." | the Goal-Mode Runs section and the Fixed Dispatch Template hash the same at 2e237902, HEAD and the working tree
  - integration-checklist.md: the wave-boundary value audit step is removed | maps to the brief | cited | brief: "and nowhere between" | a search of the plugin finds `wave boundary` only in the template, the goal-run mapping and the one mandate line
  - prompt-snippets.md: the plan-review procedure gains "Report a plan that is unacceptably long. When the run is under value-level operation, weigh that no value audit runs between a plan's draft and its close." | maps to the brief | cited | brief: "A plan review catches a plan that is unacceptably long."; brief: "at each plan's draft and at each plan's close, and nowhere between" | stated once; the second sentence restates the brief's own line as the thing to weigh
  - Three manifests at 0.29.0 | maps to the brief | inferred | as the planner-added item above | -
  - docs/coding-agent/plans/active/audit-at-plan-draft-and-close-run.md (new run record) | internal mechanics | not audited | - | -
  - docs/coding-agent/lessons.md: the lesson on dispatching the wave-boundary audit is marked as overtaken, with what stays of it | internal mechanics | not audited | - | - (also an Orchestrator ruling; see below)
  - Untracked `.claude/settings.local.json` and `.claude/pr67body.tmp` | internal mechanics | not audited | - | both predate the range by file date (July and September) and are in no commit; the second is pull request text and was not opened. Neither is irreversible or outward-facing as it stands

  Judgement calls in the run's records

  - Worker (Task_1): the sentence that the next audit grades a corrected item is left as it reads | internal mechanics | not audited | - | -
  - Worker (Task_1): the mandate's pointer for `wave boundary` sits in the list of artifacts by position | internal mechanics | not audited | - | -
  - Orchestrator: the plan is authorized under the ratified brief on the plan-draft verdict, recording no approval by the owner | maps to the brief | cited | brief, Lifecycle: "With a ratified brief, a citing audit approves plans"; brief, Pass conditions: "no plan of this run was presented to him for approval, and every plan is on disk" | -
  - Orchestrator: this run itself is audited at its plan's draft and close and at no wave boundary, before the plugin text said so | maps to the brief | cited | brief: "It runs by position: at each plan's draft and at each plan's close, and nowhere between." (the amendment carries the owner's words dated 2026-10-05 and was committed before the start revision) | -
  - Orchestrator: edit to lessons.md at integration, outside any task's `owns` | internal mechanics | not audited | - | -
  - Orchestrator: the first closeout dispatch, returned ungraded, was dispatched again with the same template and nothing logged as a verdict | maps to the brief | cited | brief, Value audit: "Fresh context each time; inputs are the documents that exist and the artifact under review, read from disk, never the Orchestrator's summary." | -
  - Orchestrator: research waived (Context) | internal mechanics | not audited | - | -

  Decision records reworded in range after acceptance: none.

  - `Human-only conditions pending: "the discussion with Counsel does not feel like filling in a form"; "the stops during a run were each right, neither skipping a decision that needed him nor stopping on something the documents answered"; "the closeout let him judge by behaviour, with implementation detail only where his judgement needed it and the reason stated"; "judged through first real use on Character Memory"` (nothing in the range lets a proxy settle any of them)
  - `Scenarios: the brief has no scenarios and the run added none (the run record says so and the brief bears it out); getting closer: yes, the range does what the two amended lines of the brief state and nothing else: the plan-mode text names two positions and no audit between, the plan-review instructions report an unacceptably long plan, and the goal-run text and template are unchanged.`
  Notes outside the record:

  - The dispatch text matched the fixed template. The session also carried harness-injected skill and hook text (engineering-quality-baselines, ponytail) and a reviewer-role system prompt; none is an account of the work, so the audit was graded. The mandate's record form was used, not the reviewer output format.
  - Agent-checkable evidence I produced myself: `validate_harness_package.py` passed, `run_validation_smoke_tests.py` exited 0, `git diff --check` over the range is clean. The branch is on no remote and has no pull request, so nothing is merged.
  - For the brief's line that the closeout audit calls whether a stack has anything undecided that needs him: nothing in this range is undecided. What waits for him is the merge and the four human-only conditions.
  - Discussion notes were not opened. `docs/coding-agent/briefs/active/design-led-long-runs-notes.md` is modified in the working tree and was excluded from every content command. The readings file was opened once, after the grades were fixed.
  - The plan's Context quotes a relay ("Yes, do it first before the next one prepared."). It is not in the governing brief and no grade relies on it.
  - The untracked brief `setup-names-what-is-missing-brief.md` is uncommitted. A later run it governs should commit it before recording its start revision, as the mandate expects.
  - `.claude/pr67body.tmp` and `.claude/settings.local.json` are untracked and not ignored. The settings file holds machine-specific paths, so they need to stay out of any commit that is pushed.

  How the Orchestrator applied it: no item is `ask-now` or `ungraded`, none is marked `direction`, and no record was reworded in the range, so nothing is held and nothing is shown beyond the result. The audit judges the range does what the two amended lines state and nothing else; the plan closes and with it the run. No item rests on a provisional statement, so nothing goes to Counsel from the audit. The comparison left one reading apart from its grade in class only (the version bump, read as mechanics and graded as an extension because the installed version is visible); the reading is corrected in the readings file and nothing in the item is redone, so no further dispatch follows. The auditor's notes are acted on at publication: the untracked local settings and pull-request text under `.claude/` are in no commit, and the untracked setup brief is left for the run it governs to commit.
- 2026-10-05 Plan closed: Task_1 done; Task_2's closeout audit done, and the publication of the branch with its pull request and the note to Counsel follow this commit. Required validation: package validator and smoke tests pass; the template and the mandate's goal-run section byte-identical to the start revision; review APPROVED.

## Decision Log (append-only; re-plans and major discoveries)
- 2026-10-05 Decision: requirement challenge before decomposition.
  - Trigger / new insight: the amendment asks for less auditing and one check at plan review.
  - Plan delta (what changed): no record is proposed, since none fixes the positions; no numeric limit on a plan's length and no definition of "unacceptably long" is added; the Reviewer judges.
  - Tradeoffs considered: a limit in tasks or waves; not taken, the brief gives a judgement and a count would be the run's own.
  - User approval: not applicable at draft
  - Record proposed: none
- 2026-10-05 Decision: draft-plan review (Codex reviewer): NEEDS_REVISION, three minor findings, all applied.
  - Trigger / new insight: the proportional design form does not fit a change to when the audit runs and to what the Reviewer reports; the compatibility stance was missing; the planner-added measure of a plan's length was not shown to be needed.
  - Plan delta (what changed): the Design section compares the chosen design with a conditional wave-boundary audit; the stance is stated (break for the plan-mode cadence, the goal-mode moments and the template preserved); the measure is dropped and the snippet uses the brief's words.
  - Tradeoffs considered: none further.
  - User approval: not applicable at draft
  - Record proposed: none

## Notes
- The audits of this run: this plan's draft and its close.
