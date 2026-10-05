# Plan: Setup names what is missing

- status: in_progress
- generated: 2026-10-05
- last_updated: 2026-10-05
- work_type: docs

## Goal
- The harness gives what the governing brief `docs/coding-agent/briefs/active/setup-names-what-is-missing-brief.md` states.
- The brief is the requirement and is not restated here; where this plan and the brief differ, the brief governs and the difference is a plan defect.
- This is the only plan of the run recorded in `docs/coding-agent/plans/active/setup-names-what-is-missing-run.md`.

## Definition of Done
- Every gives-statement and constraint of the brief is carried by the plugin text, each stated once in the file that owns that moment; its means are built from, and a departure from one is recorded as a finding.
- Scenarios 1 and 2 hold on a fixture repository: a fresh agent following the built setup text on each fixture produces the report and the common rule file the scenarios describe, and on the second fixture a later run, a small piece of work carried from its plan to its close by fresh agents under the built text, is graded at its plan's draft and at its close by fresh Auditor dispatches against the product philosophy the pointer names.
- No setup text drafts, templates or offers a form for a philosophy.
- A run in a repository whose philosophies are marked missing behaves exactly as a run does today in a repository without one: a line saying a philosophy is missing turns nothing on and nothing off (value-level operation is on under a governing brief as today, and off without one), and no run mentions what is missing.
- Any decision record this plan proposes is checked and accepted by the owner by name before text is built on it.
- Package validators and smoke tests pass; the branch has Reviewer `APPROVED`.
- The run closes as `completion-closeout.md` states: scenario by scenario, its branch published on the stack and a pull request opened under the standing approval, the note to Counsel sent, nothing merged.

## Planner-added requirements
- Setup looks among tracked files, as it does for decision records, and records a pointer for a document that states, in whatever words, that it is the repository's product philosophy or its engineering philosophy and that carries a ratification record; where more than one document fits one philosophy it records none, names them in the report and leaves that philosophy listed as missing. This is how setup looks, not a form a philosophy must take. Needed because: to record a pointer setup has to tell a philosophy from any other document and tell which of the two it is; the ratification record is the one thing the form asks of every philosophy, and the document's own statement of what it is is the only thing in it that says which. With two that fit, setup cannot know which the person means, and the brief lets a philosophy go unfound and be corrected by a sentence.
- The line that lists a philosophy as missing is worded so that it cannot be read as a pointer, and the texts that find philosophies through pointer lines say so. Needed because: a pointer turns value-level operation on, and the brief's constraint is that a run behaves as today while a philosophy is missing.
- When the person objects to a pointer setup recorded, the line that replaces it names the file that is not the philosophy, in a form that is not a pointer. Needed because: the lines are derived again at every refresh, and without that record the next refresh would find the same file and record it again, undoing his objection.
- The lines are derived again at every refresh, in a repository set up before this change as well. Needed because: the brief's "stays visible" is the common rule file, and an accepted record has no stored state decide what a rule file says.
- This repository's own rule file gets its two lines by a refresh under the built text. Needed because: it is the first repository the owner will see them in.
- The audit mandate opens with a first step that keeps an auditor from the readings file before grading (added 2026-10-05; see the Decision Log). Needed because: this run's own audits returned void without it.
- One plugin version bump. Needed because: the package validator requires the three manifests to agree per installed version.

## Scope / Non-goals
- Scope: `rulebook` (SKILL.md, `bootstrap-lifecycle.md`, `rules-files.md`, `rule-suite-templates.md`), `value-documents/SKILL.md`, `counsel/SKILL.md`, `orchestration-harness` (SKILL.md, `value-level-operation.md`, `value-audit-mandate.md`), the three manifests, two fixture repositories under `tests/coding-agent-orchestration-harness/fixtures/`, a decision record if the admission test passes, this repository's `docs/coding-agent/rules/common.md`.
- Non-goals: the brief's "Left out on purpose" (standing approvals and initiative briefs as missing items); a script that performs setup; a validator for the rule files' content; any change to how a philosophy is written or ratified; the fixed dispatch templates.

## Design
- Chosen: setup stays what it is, the rulebook's bootstrap and refresh, followed as text. It gains one step beside the one for decision records: look among tracked files for a philosophy that names itself and carries a ratification record; record a pointer line for one found, or a line saying there is none yet, what it gives and how to start; say in the report which it did. Counsel reads that section of the common rule file when it opens.
- Alternative: setup records no pointer by itself; it lists every philosophy as missing unless a pointer already exists, and the person names the file.
- Lenses. structure: chosen adds one detection rule to the rulebook; the alternative adds none. evolution: chosen changes who writes a pointer first, which the brief states as a rule in force that changes; the alternative leaves that rule alone. verification: both are checked by a fresh agent on a fixture; chosen needs the second fixture. operation: none. human: with the alternative a person who already has a philosophy is told it is missing every time, which the brief's "everything is in place" rules out. safety: chosen can record a wrong file, bounded by the self-naming and ratification test and corrected by his objection; the alternative cannot.
- Why chosen: the brief gives that an existing philosophy is found and its pointer recorded.

## Compatibility stance (required if a contract/interface/persisted format is touched)
- surface: the "Repository Reference Documents" section of `docs/coding-agent/rules/common.md` (two line forms added); who may add a philosophy pointer line.
- stance: preserve
- justification: the locatable consumers are this repository and Character Memory. An existing pointer line keeps its form and meaning. A repository set up earlier gains the lines at its next refresh and nothing in it stops working before that. A line that says a philosophy is missing is not a pointer, so value-level operation stays off where it was off.

## Context (workspace)
- Governing brief: `docs/coding-agent/briefs/active/setup-names-what-is-missing-brief.md`, ratified 2026-10-05 ("I ratify the brief, hand it over after the run closes."), handed over by Counsel's relay of 2026-10-05, taken up after the audit-positions change on his word.
- Run record: `docs/coding-agent/plans/active/setup-names-what-is-missing-run.md`. Readings file: `docs/coding-agent/plans/active/setup-names-what-is-missing-readings.md`. This plan starts from revision: 6935b2c3.
- Research: a Researcher report received in session on 2026-10-05; not on disk, so nothing here rests on it alone. Facts the plan relies on, each checkable in the tree: setup is the rulebook's full bootstrap, followed as text (`skills/rulebook/references/bootstrap-lifecycle.md`); it detects a decision-record convention among tracked files, records it without asking, reports what it recorded and flags a contradiction at refresh; the section "Repository Reference Documents" is required and its lines are free; the rule that a pointer line is added only on the owner's word is in `value-documents/SKILL.md` and `value-level-operation.md` and in no decision record; Counsel reads no rule file when it opens; no fixture repository exists.
- The audits of this run: this plan's draft and its close.
- Design record consulted and deviations from its acceptance: ADR-D-0036 (kept: setup states no value and infers none; it leaves forms and locations to the value-document form), ADR-D-0024 and ADR-D-0025 (kept: the lines sit in the common rule file and are derived again at refresh), ADR-D-0052 and ADR-D-0056 (kept).

## Open Questions (max 3)
- None for the owner.

## Assumptions
- A1: a pointer whose file is gone or moved is flagged at refresh and the line is left as it is; removing or repointing it stays on the owner's word. source: the brief's means on refresh; `value-level-operation.md` on a pointer that names an absent file.
- A2: a Counsel session mentions what is missing once, when it opens, and offers to start; it does not raise it again in that session. source: the brief, "may offer to start" and "Nothing nags"; a reading.
- A3: the later run of scenario 2 is a whole run on the fixture, kept small: one plan for the small request the fixture carries, its audit at plan draft, the change made, its audit at close. The agents that plan and build it are fresh and follow the built text; the Orchestrator of this run dispatches them and the two audits, since a subagent cannot dispatch another. source: the brief, scenario 2 and its pass condition; the runtime's limit on nested dispatch.

## Tasks

### Task_1: Draft the record
- type: docs
- owns:
  - docs/coding-agent-orchestration-harness/decisions/**
- depends_on: []
- description: |
  A Worker runs the admission test on one decision: setup may record a philosophy's pointer line itself for a document that names itself and carries a ratification record, the person hearing of it in the report and removing it by objecting; no philosophy is drafted, templated or inferred by setup. The brief already states the changed rule, so a record that only repeats it does not pass: the Worker has to find a decision that binds later work and cannot be read back from the brief or this plan, or return that the test failed. If the test passes it drafts the record as proposed, writing only what the brief and this plan's log state and reporting gaps. The Orchestrator checks it says what was decided, a Reviewer checks it against the record standard, and it goes to the owner by name. If the test fails, no record is written, the content stays in the plugin text, and Task_2 starts with nothing asked of the owner.
- acceptance:
  - The admission test's result is reported with its reasons.
  - A record, if drafted, states only what the brief or this plan's log states; every gap is reported, none filled.
  - No text of Task_2 is written before the owner has accepted the record by name, or before the test has failed.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "python scripts/validate_harness_package.py from the plugin root; git diff --check"
  - kind: review
    required: true
    owner: reviewer
    detail: "ADR review per the subagent-strategy ADR-review snippet"

### Task_2: Setup, the pointer rule, Counsel's opening
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/rulebook/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/rulebook/references/bootstrap-lifecycle.md
  - plugins/coding-agent-orchestration-harness/skills/rulebook/references/rules-files.md
  - plugins/coding-agent-orchestration-harness/skills/rulebook/references/rule-suite-templates.md
  - plugins/coding-agent-orchestration-harness/skills/value-documents/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/counsel/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/value-level-operation.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/value-audit-mandate.md
  - plugins/coding-agent-orchestration-harness/.claude-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.codex-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.github/plugin/plugin.json
- depends_on: [Task_1]
- description: |
  The rulebook's bootstrap and refresh gain the philosophy step and its two line forms; the report says which philosophies were found and recorded and which are missing, with what each gives and how to start; the pointer rule in the value-document form and the run-side reference follows the brief; a line saying a philosophy is missing is not a pointer for any text that finds philosophies through pointer lines; Counsel reads that section when it opens and may offer once; an Orchestrator session and a run say nothing of what is missing.
- acceptance:
  - At bootstrap and at refresh the common rule file's "Repository Reference Documents" section has, for each of the two philosophies, either a pointer line or one line saying there is none yet, what it gives once it exists, and that it starts by opening a Counsel session; the report says the same and lists nothing else as missing.
  - A pointer is recorded by setup only as the planner-added requirement states, and the report names the file; the person's objection removes it, and the line that replaces it says which file is not the philosophy, so that a later refresh does not record that file again; a pointer whose file is gone or moved is flagged at refresh and left as it is.
  - Setup writes, drafts, templates and offers nothing for a philosophy's content, and no text has it infer one.
  - A line saying a philosophy is missing is not a pointer: it turns value-level operation neither on nor off, so a run under a governing brief is audited as today and a run with no value documents has no audit as today; outside the setup report itself, which is where the person is told, no Orchestrator text mentions what is missing to the person; a Counsel session mentions it once when it opens and offers to start.
  - The value audit's fixed dispatch template is byte-identical to this plan's start revision; the three manifests agree at the next version.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "python scripts/validate_harness_package.py; python scripts/run_validation_smoke_tests.py; git diff --check; hash of the template block against the start revision"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review against the brief and this task's acceptance; a trace of scenario 3 through Counsel's and the Orchestrator's text"

### Task_3: Two fixture repositories and the scenarios on them
- type: test
- owns:
  - tests/coding-agent-orchestration-harness/fixtures/setup-philosophy/**
- depends_on: [Task_2]
- description: |
  Two small fixture repositories are added as file sets: one with no philosophy, one with a ratified product philosophy under a path and name of its own. A fresh agent that has read nothing of this run copies each into a temporary git repository and follows the built rulebook text from the working tree to set it up; its report and the resulting common rule file are returned as evidence for scenarios 1 and 2. On the second fixture, after setup, a later run is made: a second fresh agent takes the small request the fixture carries and, following the built orchestration text from the working tree, drafts a plan for it; a fresh Auditor grades the plan by the fixed template; a fresh agent makes the change the plan asks for; a fresh Auditor grades the result at the plan's close. The Orchestrator of this run dispatches each of them in the fixture and adds nothing to the fixed template; the built text's own gates apply in the fixture, so the fixture's plan is reviewed, and, the fixture run being on a philosophy alone, approved by the Orchestrator of this run standing in for the fixture's user, which is said in the evidence. Each dispatch text and whatever else the runtime put in the agent's context is kept with the returned artifacts.
- acceptance:
  - On the first fixture the report and the common rule file each name both philosophies as missing, with what each gives and how to start, and list nothing else as missing.
  - On the second the pointer to the product philosophy is recorded and the report says so, and only the engineering philosophy is listed as missing.
  - Neither setup wrote, drafted or templated a philosophy.
  - On the second fixture the later run's two audit verdicts, at its plan's draft and at its close, each name the product philosophy, found through the pointer setup recorded, as their product basis and grade the plan's items and the change against it, and nothing they hold is left open at the close.
- validation:
  - kind: manual
    required: true
    owner: reviewer
    detail: "A fresh agent's setup on each fixture in a temporary repository (the report text and the common rule file's section are the evidence); on the second, the later run's plan, its change and its two audit verdicts"

### Task_4: Land the record; refresh this repository's rule file; close
- type: review
- owns:
  - docs/coding-agent-orchestration-harness/decisions/**
  - docs/coding-agent/rules/common.md
  - docs/coding-agent/plans/**
- depends_on: [Task_1, Task_2, Task_3]
- description: |
  On the owner's acceptance naming the record the Orchestrator sets it accepted and logs the quoted words. After Task_3 it refreshes this repository's own common rule file under the built text, which lists both philosophies as missing here. It then closes the plan (closeout audit with its reading; final review) and the run: the branch pushed on the stack, a pull request opened under the standing approval, the note to Counsel, `candidate ready`.
- acceptance:
  - No record is set accepted without the owner's acceptance naming it, logged with the quoted words.
  - This repository's common rule file names both philosophies as missing in the built form and carries no pointer for either.
  - Every outgoing commit, message and pull request text is swept for machine-specific names and paths before it is pushed; nothing is merged.
- validation:
  - kind: command
    required: true
    owner: orchestrator
    detail: "package validator and smoke tests; privacy sweep over every commit to be pushed"
  - kind: review
    required: true
    owner: reviewer
    detail: "Final review of the branch vs this plan's Definition of Done"

## Task Waves (explicit parallel dispatch sets)
- Wave 1: Task_1
- Wave 2: Task_2
- Wave 3: Task_3
- Wave 4: Task_4

Task_2 waits for the owner's acceptance of the record, or for the admission test to fail.

## Rollback / Safety
- The branch reverts on its own; no migration, no persisted data. A repository refreshed under the new text and then under the old one keeps two free lines the old text ignores.

## Progress Log (append-only)
- 2026-10-05 Plan review (Codex reviewer): NEEDS_REVISION with two major and one minor finding, applied (see the Decision Log); re-review APPROVED with no finding open. Plan validator passes.
- 2026-10-05 Plan-draft audit, dispatch text (to a fresh Auditor dispatch on Fable):

  ```text
  You are the value auditor. Read references/value-audit-mandate.md of the orchestration-harness skill and follow it exactly. Position: plan draft. Plan: docs/coding-agent/plans/active/setup-names-what-is-missing-plan.md. Governing brief: docs/coding-agent/briefs/active/setup-names-what-is-missing-brief.md. Changes since: none.
  ```

- 2026-10-05 Plan-draft audit, first dispatch, verdict as returned (the two comparison lines are logged in the readings file, not here):

  Value audit verdict, plan draft. Four items are `ask-now`, all on one question: scenario 2's "a later run there is kept to that product philosophy" is checked by a plan draft and its audit only, which narrows an agent-checkable pass condition of the brief. Everything else is `cited`, `inferred` or `not audited`.

  The dispatch matched the fixed template with nothing added. Discussion notes were not opened; the readings file was opened once, after the grades were fixed.

  Position: plan draft

  Documents read: `docs/coding-agent/briefs/active/setup-names-what-is-missing-brief.md`; `docs/coding-agent/plans/active/setup-names-what-is-missing-plan.md` (artifact); `docs/coding-agent/rules/common.md` at HEAD (pointer lines and "Standing Approvals" only); after grading, `docs/coding-agent/plans/active/setup-names-what-is-missing-readings.md`

  Product basis: brief in the product owner's words (the brief says "ebigunso owns the harness; no product philosophy and no engineering philosophy exist for this repository"; ratification record present, dated 2026-10-05)

  Not audited: engineering side, it has no document (no pointer line for an engineering philosophy in `common.md`)

  Missing inputs: none

  Value documents changed in range: none

  Items (`item | maps | grade | support | reasons / mark`):

  - DoD 1: every gives-statement and constraint carried by the plugin text, means built from, departures recorded | maps to the brief | cited | brief: "This brief is the grounds for the work. It is passed verbatim"; "a means does not bind" | -
  - DoD 2: scenarios 1 and 2 hold on a fixture; scenario 2's later run shown by a plan draft and a plan-draft audit | maps to the brief | ask-now | brief, Pass conditions: "scenarios 1 and 2 hold on a fixture repository"; scenario 2: "a later run there is kept to that product philosophy" | Loosens a pass condition: the scenario says a later run is kept to the philosophy, and the plan counts it as holding on the start of a run only (see A3). The setup half (report and rule file on both fixtures) would be `cited` on its own. Value question: for a repository that already has a product philosophy, is it enough to see that later work there is planned and graded against that philosophy at its start, or must a piece of work be carried through to its end and shown kept to it before the scenario counts as holding?
  - DoD 3: no setup text drafts, templates or offers a form for a philosophy | maps to the brief | cited | brief, Limits: "Setup never writes, drafts, starts or offers a form to fill in for a philosophy, and infers none from the repository's code or documents." | -
  - DoD 4: a run with philosophies marked missing behaves as today; a missing line turns nothing on or off; no run mentions it | maps to the brief | cited | brief, Limits: "A run in a repository whose philosophies are marked missing behaves exactly as a run does today in a repository without one."; "Nothing nags. Work runs as it does today while a philosophy is missing, and no run reminds the person of it." | -
  - DoD 5: a proposed decision record is accepted by the owner by name before text is built on it | internal mechanics | not audited | - | - (tightens who decides; not irreversible, not outward-facing)
  - DoD 6: package validators and smoke tests pass; Reviewer `APPROVED` | maps to the brief | cited | brief, Pass conditions: "the package validators pass" | -
  - DoD 7: the run closes with its branch published, a pull request opened, the note to Counsel sent, nothing merged | maps to the brief | cited | standing approval, `common.md` "Standing Approvals": "A finished, reviewed run may publish its branch and open pull requests in this repository without asking first. Merges are not covered and wait for the owner." Its record: "Given and accepted by the repository's owner, ebigunso, on 2026-09-30, relayed by Counsel: "The common rule proposed, accepted."" The entry is committed at HEAD; whether the quoted words were said is not something a file can show. | - (the note to Counsel is read as the harness's own carrier between two sessions on this repository, not as reaching anyone outside it)
  - Planner-added 1: setup looks among tracked files for a document that names itself a philosophy and carries a ratification record; with more than one fitting it records none and names them | maps to the brief | inferred | brief: "Where the repository already has a philosophy document, setup finds it, records the pointer to it, and says in its report that it did; the person objects only if it picked the wrong file."; "A philosophy has no fixed path or name, so setup will sometimes list one as missing when it exists. A sentence from the person corrects it."; "A philosophy comes only from discussion with the person entitled to state it." | direction (it decides which of a person's existing documents the harness treats as their philosophy)
  - Planner-added 2: the missing line cannot be read as a pointer | maps to the brief | cited | brief, Limits: "A run in a repository whose philosophies are marked missing behaves exactly as a run does today in a repository without one." | -
  - Planner-added 3: the lines are derived again at every refresh, in repositories set up earlier too | maps to the brief | inferred | brief: "What is missing stays visible after the setup report is gone: the common rule file carries a line for each missing philosophy."; "At refresh, a pointer to a file that is gone or moved is flagged, as it is for decision records." | -
  - Planner-added 4: this repository's own rule file gets its two lines by a refresh under the built text | maps to the brief | inferred | brief, scenario 1: "the report and the common rule file each name both philosophies as missing"; product basis line: "no product philosophy and no engineering philosophy exist for this repository" | - (does not settle the human-only condition, and the plan does not claim it does)
  - Planner-added 5: one plugin version bump | internal mechanics | not audited | - | -
  - Non-goal: the brief's "Left out on purpose" | maps to the brief | cited | brief: "Standing approvals as missing items."; "Initiative briefs: they belong to a piece of work, not to the repository." | -
  - Non-goal: no script that performs setup | internal mechanics | not audited | - | -
  - Non-goal: no validator for the rule files' content | internal mechanics | not audited | - | -
  - Non-goal: no change to how a philosophy is written or ratified | maps to the brief | cited | brief, Limits: "A philosophy comes only from discussion with the person entitled to state it." | -
  - Non-goal: the fixed dispatch templates untouched | internal mechanics | not audited | - | -
  - A1: a pointer whose file is gone or moved is flagged at refresh and left; removal or repointing stays on the owner's word | maps to the brief | cited | brief: "At refresh, a pointer to a file that is gone or moved is flagged, as it is for decision records." | -
  - A2: a Counsel session mentions what is missing once when it opens, offers to start, and does not raise it again | maps to the brief | inferred | brief: "A Counsel session sees those lines when it opens and may offer to start on one."; "Nothing nags."; scenario 3: "mentions what is missing and offers to start" | -
  - A3: scenario 2's later run shown by the start of a run, not a whole one | maps to the brief | ask-now | brief, scenario 2: "a later run there is kept to that product philosophy"; Pass conditions: "scenarios 1 and 2 hold on a fixture repository" | Loosens a pass condition: it changes how an agent-checkable condition is checked to less than the scenario's words. Value question: as at DoD 2.
  - Task_1: admission test and, if it passes, a proposed record to the owner by name | internal mechanics | not audited | - | -
  - Task_2: setup text, the pointer rule, Counsel's opening, Orchestrator silence | maps to the brief | cited | brief: "setup says what the person gains once it exists and how to start: open a Counsel session"; "After this work, setup's report is where he hears of it, and his objection removes it."; "Only the two philosophy documents ... are marked as missing by setup."; Limits, both statements; scenario 3: "A Counsel session opened in the repository of scenario 1 mentions what is missing and offers to start; an Orchestrator session there does not." | -
  - Task_3: two fixtures and the scenarios on them | maps to the brief | ask-now | brief, Pass conditions and scenarios 1 and 2 as quoted above | Only the fourth acceptance entry is held ("this shows the start of a run kept to it, and is not claimed as a whole run"), for the reason and value question at DoD 2. The first three entries would be `cited` on "scenarios 1 and 2 hold on a fixture repository".
  - Task_4: set the record accepted on the owner's word, refresh this repository's rule file, close and publish | maps to the brief | cited | the standing approval quoted at DoD 7, with the same caveat; the refresh as Planner-added 4 | - (record acceptance waits for the owner by name, which no standing approval discharges and the plan does not ask it to; nothing is merged)
  - Decision Log 1: requirement challenge (no script, no validator; two candidates recorded as neither; earlier repositories at refresh; gone pointer flagged and left; Counsel once per session) | maps to the brief | inferred | the statements quoted at Planner-added 1 and 3, A1 and A2 | - (the direction mark is on Planner-added 1)
  - Decision Log 2: draft review applied (a missing line turns nothing on or off; a plan draft and its audit on the second fixture, a whole run not taken; detection rule restated) | maps to the brief | ask-now | brief, Limits and scenario 2 as quoted above | The tradeoff "a whole run on the fixture; not taken" is the loosening at DoD 2, same value question. The other two deltas would be `cited` and `inferred`.

  Human-only conditions pending: "his first setup on a repository of his own, judged by whether what he was shown as missing was clear and whether anything pushed him."

  Scenarios: none

  Observations outside the record, with no effect on any grade:
  - Planner-added 3 has the lines derived again at every refresh, and the brief has the person's objection remove a pointer. The plan does not say what stops the next refresh from recording the same file again after an objection. This is a plan-review matter.
  - Task_2 says "no Orchestrator text mentions what is missing to the person", while the setup report, which does mention it, may be produced in an Orchestrator session. The built text needs to keep those two apart.
  - The mandate read is the working-tree copy at `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/value-audit-mandate.md`; no installed copy was found at the 0.21.0 cache path to compare it with.

  How the Orchestrator applied it: four items are `ask-now`, all on one line the Orchestrator added to its own plan: that scenario 2's later run is shown by the start of a run only, which loosens a pass condition of the brief. The plan is not authorized on this verdict. By the brief's section on what reaches the owner, an unsupported line of the Orchestrator's own plan is the Orchestrator's to drop or redo, and nothing is asked of him while that settles it: the line is redone so that the fixture carries a small piece of work through to its end, the audit is dispatched again, new, and the next entry records it. No item rests on a provisional statement, so nothing goes to Counsel. The auditor's two observations are taken into the plan as well.
- 2026-10-05 The Orchestrator's own line redone after the first plan-draft verdict: A3 and the lines built on it showed scenario 2's later run by its start only. The brief's scenario says a later run is kept to the philosophy and its pass condition says the scenario holds on a fixture, so the line is redone to a whole small run on the fixture, audited at its plan's draft and at its close. From the auditor's observations: an objection is kept in the line that replaces the pointer, so a refresh does not record the same file again; the setup report is named as the one place an Orchestrator session tells the person what is missing. The changed plan goes to the Reviewer, a second reading is written, and the plan-draft audit is dispatched again, new (text as above).

- 2026-10-05 Plan review delta (Codex reviewer) after the redone line: one minor finding applied, then APPROVED with no finding open. Plan-draft audit, second dispatch (same template text), verdict as returned (machine paths redacted; the two comparison lines are logged in the readings file, not here):

  Value audit verdict, plan draft (second dispatch). No item is `ask-now`. Every item is `cited`, `inferred` or `not audited`; one `inferred` item carries the `direction` mark (Planner-added 1).

  The dispatch matched the fixed template with nothing added. The session also carried runtime context (a reviewer role prompt, a quality-baselines skill text, a hook note); none of it is an account of this work, so the audit was graded. Discussion notes were not opened. The readings file was opened once, after the grades were fixed.

  Position: plan draft

  Documents read: `docs/coding-agent/briefs/active/setup-names-what-is-missing-brief.md`; `docs/coding-agent/plans/active/setup-names-what-is-missing-plan.md` (artifact); `docs/coding-agent/rules/common.md` at HEAD ("Repository Reference Documents" and "Standing Approvals" only); after grading, `docs/coding-agent/plans/active/setup-names-what-is-missing-readings.md`

  Product basis: brief in the product owner's words (the brief says "ebigunso owns the harness; no product philosophy and no engineering philosophy exist for this repository"; ratification record present, dated 2026-10-05: "I ratify the brief, hand it over after the run closes.")

  Not audited: engineering side, it has no document (`common.md` at HEAD carries no pointer line for either philosophy)

  Missing inputs: none

  Value documents changed in range: none

  Items (`item | maps | grade | support | reasons / mark`):

  - DoD 1: every gives-statement and constraint carried by the plugin text, means built from, a departure recorded as a finding | maps to the brief | cited | brief: "This brief is the grounds for the work. It is passed verbatim"; "a means does not bind" | -
  - DoD 2: scenarios 1 and 2 hold on a fixture; on the second a later small run is carried from plan to close and graded by fresh Auditors at draft and close against the philosophy the pointer names | maps to the brief | cited | brief, Pass conditions: "scenarios 1 and 2 hold on a fixture repository"; scenario 2: "a later run there is kept to that product philosophy" | -
  - DoD 3: no setup text drafts, templates or offers a form for a philosophy | maps to the brief | cited | brief, Limits: "Setup never writes, drafts, starts or offers a form to fill in for a philosophy, and infers none from the repository's code or documents." | -
  - DoD 4: a run with philosophies marked missing behaves as today; a missing line turns nothing on or off; no run mentions it | maps to the brief | cited | brief, Limits: "A run in a repository whose philosophies are marked missing behaves exactly as a run does today in a repository without one."; "Nothing nags. Work runs as it does today while a philosophy is missing, and no run reminds the person of it." | -
  - DoD 5: a proposed decision record is accepted by the owner by name before text is built on it | internal mechanics | not audited | - | - (tightens who decides; not irreversible, not outward-facing)
  - DoD 6: package validators and smoke tests pass; Reviewer `APPROVED` | maps to the brief | cited | brief, Pass conditions: "the package validators pass" | -
  - DoD 7: the run closes with its branch published, a pull request opened, the note to Counsel sent, nothing merged | maps to the brief | cited | standing approval, `common.md` "Standing Approvals": "A finished, reviewed run may publish its branch and open pull requests in this repository without asking first. Merges are not covered and wait for the owner." Its record: "Given and accepted by the repository's owner, ebigunso, on 2026-09-30, relayed by Counsel: "The common rule proposed, accepted."" The entry is committed at HEAD; whether the quoted words were said is not something a file can show. | - (the note to Counsel is read as the harness's own carrier between two sessions on this repository, not as reaching anyone outside it)
  - Planner-added 1: setup looks among tracked files for a document that says it is the product or the engineering philosophy and carries a ratification record; with more than one fitting it records none, names them and lists that philosophy as missing | maps to the brief | inferred | brief: "Where the repository already has a philosophy document, setup finds it, records the pointer to it, and says in its report that it did; the person objects only if it picked the wrong file."; "A philosophy has no fixed path or name, so setup will sometimes list one as missing when it exists. A sentence from the person corrects it."; Limits: "infers none from the repository's code or documents" | direction (it decides which of a person's existing documents the harness treats as their philosophy)
  - Planner-added 2: the missing line cannot be read as a pointer, and the texts that find philosophies through pointer lines say so | maps to the brief | cited | brief, Limits: "A run in a repository whose philosophies are marked missing behaves exactly as a run does today in a repository without one." | -
  - Planner-added 3: after an objection, the line that replaces the pointer names the file that is not the philosophy, in a form that is not a pointer | maps to the brief | inferred | brief: "the person objects only if it picked the wrong file"; "After this work, setup's report is where he hears of it, and his objection removes it." | -
  - Planner-added 4: the lines are derived again at every refresh, in repositories set up earlier too | maps to the brief | inferred | brief: "What is missing stays visible after the setup report is gone: the common rule file carries a line for each missing philosophy."; "At refresh, a pointer to a file that is gone or moved is flagged, as it is for decision records." | - (the plan's own reason, about accepted records and stored state, was not taken as support)
  - Planner-added 5: this repository's own rule file gets its two lines by a refresh under the built text | maps to the brief | inferred | brief, scenario 1: "the report and the common rule file each name both philosophies as missing"; product basis line: "no product philosophy and no engineering philosophy exist for this repository" | - (does not settle the human-only condition, and the plan does not claim it does)
  - Planner-added 6: one plugin version bump | internal mechanics | not audited | - | - (a version number in the manifests is not a release)
  - Non-goal: the brief's "Left out on purpose" | maps to the brief | cited | brief: "Standing approvals as missing items."; "Initiative briefs: they belong to a piece of work, not to the repository." | -
  - Non-goal: no script that performs setup | internal mechanics | not audited | - | -
  - Non-goal: no validator for the rule files' content | internal mechanics | not audited | - | -
  - Non-goal: no change to how a philosophy is written or ratified | maps to the brief | cited | brief, Limits: "A philosophy comes only from discussion with the person entitled to state it." | -
  - Non-goal: the fixed dispatch templates untouched | internal mechanics | not audited | - | -
  - A1: a pointer whose file is gone or moved is flagged at refresh and left; removal or repointing stays on the owner's word | maps to the brief | cited | brief: "At refresh, a pointer to a file that is gone or moved is flagged, as it is for decision records." | -
  - A2: a Counsel session mentions what is missing once when it opens, offers to start, and does not raise it again | maps to the brief | inferred | brief: "A Counsel session sees those lines when it opens and may offer to start on one."; "Nothing nags."; scenario 3: "mentions what is missing and offers to start" | -
  - A3: scenario 2's later run is a whole small run on the fixture (one plan, its draft audit, the change, its closing audit), its agents fresh and dispatched by this run's Orchestrator | maps to the brief | inferred | brief, scenario 2: "a later run there is kept to that product philosophy"; Pass conditions: "Agent-checkable: ... scenarios 1 and 2 hold on a fixture repository" | - (the brief does not say how large the run is or who dispatches it; the scenario's words are met by a run carried to its close, so no pass condition is loosened)
  - Task_1: admission test and, if it passes, a proposed record to the owner by name | internal mechanics | not audited | - | - (record acceptance waits for the owner by name)
  - Task_2: setup text, the two line forms, the pointer rule, Counsel's opening, Orchestrator silence outside the setup report | maps to the brief | cited | brief: "For each one that is missing, setup says what the person gains once it exists and how to start: open a Counsel session."; "After this work, setup's report is where he hears of it, and his objection removes it."; "Only the two philosophy documents ... are marked as missing by setup."; Limits, both statements; scenario 3: "A Counsel session opened in the repository of scenario 1 mentions what is missing and offers to start; an Orchestrator session there does not." | - (the manifests and the template hash are mechanics inside the task)
  - Task_3: two fixtures; a fresh agent's setup on each; on the second, the later run through the built text's gates, this run's Orchestrator standing in for the fixture's user | maps to the brief | inferred | brief, Pass conditions: "Agent-checkable: the package validators pass; scenarios 1 and 2 hold on a fixture repository"; scenarios 1 and 2 as quoted above | - (the first three acceptance entries would be `cited` alone. The stand-in is an extension: the brief marks the scenario agent-checkable, so a fixture user played by an agent takes no decision from a real person; who decides is not loosened)
  - Task_4: set the record accepted on the owner's word, refresh this repository's rule file, close and publish | maps to the brief | cited | the standing approval quoted at DoD 7, with the same caveat; the refresh as Planner-added 5 | - (record acceptance waits for the owner by name, which no standing approval discharges and the plan does not ask it to; nothing is merged)
  - Decision Log 1: requirement challenge (no script, no validator; two candidates recorded as neither; earlier repositories at refresh; gone pointer flagged and left; Counsel once per session) | maps to the brief | inferred | the statements quoted at Planner-added 1 and 4, A1 and A2 | - (the direction mark is on Planner-added 1)
  - Decision Log 2: draft review applied (a missing line turns nothing on or off; a plan draft and its audit on the second fixture; detection rule restated) | maps to the brief | inferred | brief, Limits and scenario 2 as quoted above; the statements at Planner-added 1 | - (its tradeoff "a whole run on the fixture; not taken" is no longer what the plan does: Decision Log 3, A3, DoD 2 and Task_3 replace it, so nothing in the plan as it stands loosens the pass condition)
  - Decision Log 3: the later run of scenario 2 is a whole run on the fixture; nothing asked of the owner | maps to the brief | cited | brief, scenario 2: "a later run there is kept to that product philosophy"; Pass conditions: "scenarios 1 and 2 hold on a fixture repository" | - (the entry's own source, "the brief makes an unsupported line of the Orchestrator's own plan the Orchestrator's to redo", is not in this brief and was not taken as support; the grade rests on the scenario the line now follows)
  - Decision Log 4: delta review applied (the objection line listed as planner-added; the fixture run passes the built gates with a stand-in user) | maps to the brief | inferred | as Planner-added 3 and Task_3 | -

  Human-only conditions pending: "his first setup on a repository of his own, judged by whether what he was shown as missing was clear and whether anything pushed him."

  Scenarios: none

  Observations outside the record, with no effect on any grade:
  - The Progress Log says "By the brief's section on what reaches the owner" and Decision Log 3 says "the brief makes an unsupported line ... the Orchestrator's to redo". This brief has no such section or statement. The rule is in `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/value-level-operation.md` (line 41) and, by the readings file, in an earlier brief's amendment. The plan's wording should name the right source.
  - Task_2 has the setup report say what is missing at every refresh. The brief makes the report the place he hears of it, so this is graded as covered, but the built text should keep a refresh report from reading as a reminder ("Nothing nags").
  - The mandate read is the working-tree copy at `[machine path redacted]\plugins\coding-agent-orchestration-harness\skills\orchestration-harness\references\value-audit-mandate.md`.
  - Two notes files show as modified in the working tree (`design-led-long-runs-notes.md`, `value-level-operation-notes.md`); neither was opened.

  How the Orchestrator applied it: no item is `ask-now` and none is `ungraded`. With the brief's ratification relayed by Counsel under the standing approval, the plan review closed with no finding open, and this verdict, the plan is authorized under the ratified brief; this records no approval by the owner. One item is marked `direction` (which of a person's existing documents setup treats as their philosophy) and is shown at closeout if the closeout audit marks it. No item rests on a provisional statement, so nothing goes to Counsel. The comparison set readings apart from grades in class only; they are corrected in the readings file. The auditor's observations are taken: the rule that an unsupported line of the Orchestrator's own plan is the Orchestrator's to redo is in the run-side reference (`value-level-operation.md`) and in the earlier brief's amendment, not in this brief, and the entries above that name this brief for it are read so; Task_2's Worker is told that a refresh report must not read as a reminder.
- 2026-10-05 Wave 1, Task_1: Worker report `done`, one YAML block, the one file inside `owns`. The admission test failed for the candidate as a whole and passed for a narrower decision, which is drafted as proposed ADR-D-0057: setup records a philosophy's pointer line itself, only for one tracked document that states which philosophy it is and carries a ratification record; the person hears of it in the report and removes it by objecting, the objection holding at every refresh. That setup drafts, templates and infers no philosophy failed the test and stays in the rulebook text. The Worker wrote only what the brief and this plan state and reported the gaps (no reopen conditions, no Revisit When), which the Decision Log settles; the Orchestrator applied them and read the record against what was decided. Worker validation: package validator pass, `git diff --check` clean. The Worker disclosed that it marked the new file intent-to-add for a moment to run the check and reset it at once; the index is as it was. Review: dispatched next.
- 2026-10-05 Task_1 closed: the admission test failed on review and the proposed record was withdrawn (see the Decision Log); nothing was asked of the owner.
- 2026-10-05 Wave 2, Task_2: Worker report `done`, one YAML block, every changed file inside the task's `owns`. The rulebook's bootstrap and refresh gain a step for the two philosophies, with three line forms for the common rule file's "Repository Reference Documents" section: a pointer (`<Product | Engineering> philosophy: <path>`), none yet with what it gives and how to start, and none yet naming a file that is not it. Setup looks among tracked files for a document that states which philosophy it is and carries a ratification record, records one, names several without recording, and reports what it did; a refresh that changes none of the lines says nothing of them. The value-document form states setup's recording as the one exception to a pointer changing only on the owner's word; the run-side reference, the skill's rule entry and the mandate say a none-yet line is not a pointer; Counsel reads the section when a session opens and offers once, in its first reply. Manifests at 0.30.0. Worker validation: package validator pass, smoke tests pass, `git diff --check` clean, the Fixed Dispatch Template block the same hash at HEAD and in the working tree. Left as they are, on the Orchestrator's ruling: the hand-over sentence in Counsel's skill that has the owner name a philosophy; the mandate's rule that a pointer removed inside an audited range is named in the verdict, which also covers a pointer replaced by an objection line. Review: dispatched next.
  - Judgement calls (Task_2): Counsel's mention comes in its first reply, since the owner speaks first; several fitting documents are named only when the line is first written; a none-yet line keeps naming a file an earlier objection named; an existing pointer in other wording stays a pointer; the step runs at bootstrap and at every targeted refresh, with no new refresh trigger.
- 2026-10-05 Review of Task_2 (Codex reviewer): NEEDS_REVISION with two minor findings, both applied by the Orchestrator. (1) Counsel's hand-over still had the owner name a philosophy's path whenever one exists, which a pointer setup recorded makes unnecessary; it now asks for that only where the philosophy has no pointer line yet. (2) The rulebook's reporting rule read two ways at refresh; it now reports line by line, only for a line the run wrote, never repeats a none-yet line that was already there, and flags a gone or moved pointer in every refresh that finds it. Everything else traced clean, scenario 3 included. Re-review requested.
- 2026-10-05 Wave 3, Task_3, first part: the Codex worker created the two fixture file sets (report `done`; the package validator and smoke suite were reassigned to the Orchestrator and pass). Each fixture was copied into a temporary git repository and committed, and a fresh agent was told only to run a first-time setup there by following the rulebook skill from the working tree, with no word about philosophies. Scenario 1: the report and the common rule file each list both philosophies as none yet, with what each gives and that it starts by opening a Counsel session; no philosophy drafted. Scenario 2, setup half: the pointer `Product philosophy: docs/product/what-tally-is-for.md` recorded, the report naming the file and how to object; only the engineering philosophy listed as none yet. Both reports also state the decision-record line setup already wrote before this change.
- 2026-10-05 Task_3, the later run on the second fixture, so far: a fresh agent acting as that repository's Orchestrator under the built text found value-level operation on through the pointer, found that the fixture's request contradicts two statements of the philosophy, and stopped to ask before planning; the Orchestrator of this run, standing in for the fixture's user, answered to keep to the philosophy and asked for a smaller change. The agent drafted a plan and its reading; a fresh Reviewer approved the plan; a fresh Auditor at plan draft (fixed template, the plan's full path, `Governing brief: none`) named the product philosophy found through the pointer as its product basis, graded every item against it, held nothing, and recorded the engineering side as having no document; the stand-in approved the plan; a fresh Worker made the one-line change and its checks pass; a fresh Reviewer approved it. The closeout audit was then dispatched twice and returned void both times by the auditor itself, each having printed the fixture's readings file in a batch of files before grading.
- 2026-10-05 A blocker met and the plan widened by one line of text: four Auditor dispatches in two days have opened a readings file before grading (two in earlier runs, two here in a row), each working from a file listing, and the mandate's sentence telling the auditor to settle its inputs first has not held. The position cannot be cleared by dispatching again on the same text. The mandate gains a First Step section: read the mandate alone first, write down the paths not to open, open files one named path at a time, and copy the exact exclude pathspecs, which were tested against this repository's history. This tightens the audit's boundary and loosens nothing. It is outside Task_2's stated acceptance and is recorded in the Decision Log as added; it goes to the Reviewer, and the fixture's closeout audit is dispatched again under it.
- 2026-10-05 Task_3 done: under the mandate's First Step the fixture's closeout audit returned a verdict on its third dispatch, the readings file opened once after grading: product basis the philosophy located by the pointer line, every product-side item graded, no `ask-now`, nothing `ungraded`, three items marked `direction`. So on the second fixture a later run was carried from its plan to its close and graded at both ends against the philosophy setup pointed to. The run, its dispatch text, what the runtime added to each agent's context and what the run does not show are written up in `tests/coding-agent-orchestration-harness/fixtures/setup-philosophy/RUN-2026-10-05.md`. Validation owner for this item is the reviewer; the final review reads that file.
- 2026-10-05 Found while refreshing this repository: the second fixture's philosophy, tracked here with its ratification line, is exactly what setup looks for, so a refresh of this repository would have recorded a pointer to a test fixture as its product philosophy. The fixture now keeps its ratification line in a file of its own, joined when the fixture is copied, and the fixtures' README says so. The general case, a repository that holds another project's ratified philosophy, is a wrong pick the brief leaves to one objection; recorded as a finding.
- 2026-10-05 Task_4, the refresh: this repository's `docs/coding-agent/rules/common.md` lists both philosophies as none yet in the built form; no tracked document here states that it is this repository's philosophy and carries a ratification record. Setup report for this refresh, to the owner through the closeout: Product philosophy: none yet; once it exists, work here is held to the behaviour the product owner wants from the product. Engineering philosophy: none yet; once it exists, work here is held to how the owner wants the project to look. To start either, open a Counsel session.

## Decision Log (append-only; re-plans and major discoveries)
- 2026-10-05 Decision: requirement challenge before decomposition.
  - Trigger / new insight: the brief, read for what need not exist, and the questions research left open.
  - Plan delta (what changed): no setup script and no rule-file validator are added, since setup is text a model follows and the brief asks for no more. Settled from the brief without asking: with two candidate files for one philosophy setup records neither and names both; a repository set up earlier gains the lines at its next refresh; a pointer whose file is gone is flagged and left; Counsel offers once per session.
  - Tradeoffs considered: detecting a philosophy by file name alone; not taken, it would record documents nobody ratified.
  - User approval: not applicable at draft
  - Record proposed: one, at Task_1, if the admission test passes
- 2026-10-05 Decision: draft-plan review (Codex reviewer): NEEDS_REVISION, two major and one minor finding, all applied.
  - Trigger / new insight: (1) the plan said value-level operation is off while philosophies are missing, which would have switched off the audit of a run under a brief, this one included; (2) scenario 2's later run had only a trace behind it though the plan promised it on a fixture; (3) the reason given for the detection rule leaned on a record that does not say it, and the tracked-files limit was not listed as added.
  - Plan delta (what changed): a missing line turns nothing on and nothing off. Task_3 adds, on the second fixture, a plan drafted by a fresh agent and a fresh Auditor's verdict on it. The detection rule is restated as how setup looks, with its own reason, and names tracked files. Task_1 says a record that only repeats the brief fails the test, and that a failed test starts Task_2 with nothing asked.
  - Tradeoffs considered: a whole run on the fixture; not taken, the plan draft and its audit are where being kept to a philosophy first shows.
  - User approval: not applicable at draft
  - Record proposed: unchanged
- 2026-10-05 Decision: the later run of scenario 2 is a whole run on the fixture.
  - Trigger / new insight: the first plan-draft audit held four items on one planner-added line, for loosening a pass condition of the brief.
  - Plan delta (what changed): A3, the Definition of Done line and Task_3 now carry a small piece of work on the second fixture from its plan to its close, with a fresh Auditor at each end. Nothing is asked of the owner: the brief makes an unsupported line of the Orchestrator's own plan the Orchestrator's to redo.
  - Tradeoffs considered: asking him whether the start of a run is enough; not taken, his brief already says what the scenario is and the question does not survive redoing the line. Cost: two more Auditor dispatches and two Worker dispatches on a fixture.
  - User approval: not applicable
  - Record proposed: unchanged
- 2026-10-05 Decision: delta review after the first plan-draft verdict (Codex reviewer): NEEDS_REVISION, one minor finding, applied.
  - Trigger / new insight: keeping the rejected file's name in the line that replaces a pointer is an addition of the plan's and was not listed as one.
  - Plan delta (what changed): it is listed under planner-added requirements with its reason. Task_3 also says that the fixture's later run passes the built text's own gates: its plan is reviewed, and approved by this run's Orchestrator standing in for the fixture's user, since a run on a philosophy alone is not authorized by an audit.
  - Tradeoffs considered: none.
  - User approval: not applicable at draft
  - Record proposed: unchanged
- 2026-10-05 Decision: a record is proposed for the narrow decision; its gaps are settled here.
  - Trigger / new insight: the Task_1 Worker's admission test passed for one part of the candidate: that setup records a pointer line without asking first, and for which document. The rule it reverses is in no record, an accepted record says a line in a file is never the consent of the person directing the work, and a later maintainer restoring "only on the owner's word" would look like tightening.
  - Plan delta (what changed): ADR-D-0057 is proposed, numbered after the withdrawn ADR-D-0055 and ADR-D-0056 so that no number names two things. Reopen conditions: setup recording nothing by itself reopens if setup is found recording documents the person did not mean as a philosophy, objection after objection; detection by file name alone is rejected outright; an objection that leaves no line behind reopens if refresh stops deriving the lines from the repository. Revisit When takes those, and that philosophies which exist are found listed as missing again and again because they do not say which philosophy they are, and the dated fact that on 2026-10-05 setup had recorded a pointer only on fixtures. The reason for keeping the objection line is the planner-added requirement's, which is part of this plan's log.
  - Tradeoffs considered: no record, the brief standing as the only statement; not taken, a brief is moved away when its work is accepted and the plugin text will state the rule without its reason.
  - User approval: not applicable; the record goes to the owner by name
  - Record proposed: ADR-D-0057
- 2026-10-05 Decision: no record; ADR-D-0057 is withdrawn before it went to the owner.
  - Trigger / new insight: the Reviewer's ADR review judged that the narrower decision does not pass the admission test: it is load-bearing, but the decision and its reasons can be read back from the brief and this plan, which the record standard excludes. The Orchestrator had passed it on the Worker's judgement call and had asked the Reviewer to say plainly if it fails.
  - Plan delta (what changed): the proposed record is deleted and its number freed. The decided behaviour is built in the plugin text, which states the rule and, where the text owns it, the reason in a clause. Task_1 is done with the test failed; nothing is asked of the owner; Task_2 starts.
  - Tradeoffs considered: keeping the record on the ground that the brief moves to `completed/`; not taken, a completed brief is still on disk and still the source.
  - User approval: not applicable
  - Record proposed: none
- 2026-10-05 Decision: the audit mandate gains a First Step section, in this plan.
  - Trigger / new insight: the fixture's closeout audit returned void twice running because the auditor printed the readings file with other files before grading; it is the third and fourth such return in two days.
  - Plan delta (what changed): one planner-added requirement, built at once: the mandate tells the auditor to read it alone first, list the paths it will not open, open one named path at a time and copy the exact exclude pathspecs. Needed because: this run's own closeout audits, on the fixture and at the plan's close, cannot be relied on to return a verdict without it, and a further dispatch on unchanged text is not a remedy. The brief does not ask for it; it is the Orchestrator's addition and the closeout audit grades it.
  - Tradeoffs considered: a hook that denies the read; not taken, the text change is smaller and is tried first. Leaving it for a later run; not taken, this run cannot close its fixture evidence without a verdict.
  - User approval: not applicable; it tightens the audit's boundary
  - Record proposed: none

## Notes
- A record is checked by the owner before anything is built on it; the audits of this run are at this plan's draft and close.
