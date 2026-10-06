# Plan: Setup holds and asks when several documents fit

- status: done
- generated: 2026-10-06
- last_updated: 2026-10-06
- work_type: docs

## Goal
- The harness gives what the governing brief `docs/coding-agent/briefs/active/setup-names-what-is-missing-brief.md` states in the statement added on 2026-10-06 under "A philosophy that already exists": where more than one document fits, setup records nothing by itself and does not write the philosophy down as simply missing; it holds, shows the person the candidates, and the person picks.
- The brief is the requirement and is not restated here; where this plan and the brief differ, the brief governs and the difference is a plan defect.
- This is the only plan of the run recorded in `docs/coding-agent/plans/active/setup-holds-when-several-fit-run.md`. It follows the run that closed on 2026-10-06 (`docs/coding-agent/plans/completed/setup-names-what-is-missing-plan.md`), whose closed plan is not reopened.

## Definition of Done
- Where more than one tracked document fits one philosophy, the setup text has setup record no pointer, write a line that names the candidates as awaiting the person's word and not the none-yet line, and bring the candidates to the person in its report; the person's pick records that document's pointer, which ends the looking.
- The rest of setup's philosophy step behaves as it does at this plan's start revision.
- On a fixture repository that holds two fitting documents, a fresh agent following the setup text records no pointer, writes the awaiting line naming both, and brings both for the person to pick.
- The value audit's fixed dispatch template is byte-identical to this plan's start revision.
- Package validators and smoke tests pass; the branch has Reviewer `APPROVED`.
- The run closes as `completion-closeout.md` states: its branch published on the stack and a pull request opened under the standing approval, the note to Counsel sent, nothing merged.

## Planner-added requirements
- When the person answers that none of the candidates is the philosophy, the line that replaces the awaiting line names each as not it, as a file is named after an objection. Needed because: the lines are derived again at every refresh, and without that record the next refresh would find the same documents and ask again. A pick needs no such record: the pointer it writes ends the looking.

## Scope / Non-goals
- Scope: `rulebook/references/bootstrap-lifecycle.md` and `rules-files.md`, `counsel/SKILL.md` where it speaks of an awaiting line, one fixture under `tests/coding-agent-orchestration-harness/fixtures/setup-philosophy/`.
- Non-goals: any other branch of setup's philosophy step; the texts on what is not a pointer, which already cover every line that is not settled; the fixed dispatch templates; a decision record (none states setup's step).

## Design
- Chosen: the awaiting line form carries one or more paths, and the several-fit branch writes it with every candidate; the report lists the candidates and asks the person to pick; a pick is the person's word for that pointer, and the candidates not picked are named in the pointer's place only if no pick is made.
- Alternative: a separate fifth line form for several candidates.
- Lenses. structure: chosen keeps four line forms and one branch for "held"; the alternative adds a form that differs only in number. evolution: chosen leaves one sentence on what is not a pointer true as written; the alternative would need each text that lists forms checked again. verification: both are shown by the same fixture. operation: none. human: the person reads the same kind of line whether one document or several are held. safety: neither records a pointer without the person's word.
- Why chosen: the brief says "likewise"; the same held state serves both cases.

## Compatibility stance (required if a contract/interface/persisted format is touched)
- surface: the awaiting line of the "Repository Reference Documents" section (it may name more than one file); what setup does when several documents fit.
- stance: break
- justification: the several-fit behaviour changes on the owner's word. The locatable consumers are this repository and Character Memory; neither holds a line written by the several-fit branch, since the text that wrote it has not been released.

## Context (workspace)
- Governing brief: `docs/coding-agent/briefs/active/setup-names-what-is-missing-brief.md`, ratified 2026-10-05; the statement of 2026-10-06 on several fitting documents carries the owner's quoted words: "Yes, hold and ask when several fit."
- Run record: `docs/coding-agent/plans/completed/setup-holds-when-several-fit-run.md`. Readings file: `docs/coding-agent/plans/completed/setup-holds-when-several-fit-readings.md` (both under `active/` until the run closed). This plan starts from revision: 34cb534.
- Where the behaviour is stated today: `bootstrap-lifecycle.md`, Philosophy Lines ("More than one, wherever each sits: record none and write the none-yet line."; the report's clause on "the files found where more than one fitted"); `rules-files.md`, the awaiting form with one path.
- Research waived: the change is confined to the section this run's predecessor wrote, read in full before drafting.
- The audits of this run: this plan's draft and its close.
- Design record consulted: none states setup's philosophy step; ADR-D-0024 and ADR-D-0025 (the lines are derived at refresh; kept).

## Open Questions (max 3)
- None.

## Assumptions
- A1: when the person picks one of several, the picked document's pointer is recorded on that word and the awaiting line is replaced by it; nothing is written about the others, since a pointer line ends the looking. source: `bootstrap-lifecycle.md`, "An existing pointer line is left as it is"; a reading.
- A2: when the person says none of them is it, the line becomes the none-yet line naming each as not it. source: the same section's rule for a no to an awaiting line.

## Tasks

### Task_1: Several fitting documents are held for the person to pick
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/rulebook/references/bootstrap-lifecycle.md
  - plugins/coding-agent-orchestration-harness/skills/rulebook/references/rules-files.md
  - plugins/coding-agent-orchestration-harness/skills/counsel/SKILL.md
  - tests/coding-agent-orchestration-harness/fixtures/setup-philosophy/**
- depends_on: []
- description: |
  The several-fit branch of setup's philosophy step writes the awaiting line with every candidate and brings them to the person to pick; the awaiting line form allows more than one path; the report and Counsel's opening mention follow. A fourth fixture holds two fitting documents: the repository's own product philosophy and a vendored project's.
- acceptance:
  - More than one fitting document: no pointer recorded, the awaiting line names each candidate, the report lists them and says the person's pick decides; the none-yet line is not written for that philosophy.
  - The person's pick replaces the awaiting line with that document's pointer; "none of them" replaces it with the none-yet line naming each as not it; a later refresh that changes nothing does not ask again.
  - Every other branch of the step, the fixed dispatch template, the mandate and the manifests read as at this plan's start revision.
  - The fourth fixture is a file set whose ratification lines are kept apart, as the other fixtures' are, so that nothing in this repository is itself a ratified philosophy.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "python scripts/validate_harness_package.py; python scripts/run_validation_smoke_tests.py; git diff --check"
  - kind: manual
    required: true
    owner: orchestrator
    detail: "After the Worker's report and before the review: a fresh agent's setup on the fourth fixture in a temporary repository, its whole reply stored with the fixtures' records"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review against the brief's statement; independent reading of the stored fixture reply against this task's acceptance"

### Task_2: Close the plan and the run
- type: review
- owns:
  - docs/coding-agent/plans/**
- depends_on: [Task_1]
- description: |
  The Orchestrator closes the plan (closeout audit with its reading; the review of Task_1, which covers the stored fixture reply, is the branch's final review) and the run: the branch pushed on the stack, a pull request opened under the standing approval, the note to Counsel, `candidate ready`.
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
- 2026-10-06 Plan review (Codex reviewer): NEEDS_REVISION with three minor findings, applied (see the Decision Log); re-review APPROVED with no finding open. Plan validator passes.
- 2026-10-06 Plan-draft audit, dispatch text (to a fresh Auditor dispatch on Fable):

  ```text
  You are the value auditor. Read references/value-audit-mandate.md of the orchestration-harness skill and follow it exactly. Position: plan draft. Plan: docs/coding-agent/plans/active/setup-holds-when-several-fit-plan.md. Governing brief: docs/coding-agent/briefs/active/setup-names-what-is-missing-brief.md. Changes since: none.
  ```

- 2026-10-06 Plan-draft audit, verdict as returned (machine paths redacted; the two comparison lines are logged in the readings file, not here):

  ## Value audit verdict: plan draft, setup-holds-when-several-fit

  No item is `ask-now` and none is `ungraded`. Two procedural points are yours to rule on before logging:

  - **Reading order.** The mandate says to read it alone and to its end before opening any other file. My first lookup for the mandate missed (it is not in the plugin cache, only in the repository), and the plan and the brief were opened in that same step, before the mandate was read. Both are inputs of this position. No notes file was opened, and the readings file was opened once, after the grades were fixed. The mandate voids an audit only for a readings file opened early, so I graded; re-dispatch if you read the first step more strictly.
  - **Dispatch content.** The dispatch text matches the fixed template exactly. The context also carried harness-injected skill text (engineering-quality-baselines, a ponytail hook). Neither contains any account of the work, so I did not treat it as text beyond the template.

  ### Verdict record

  `Position: plan draft`

  `Documents read: docs/coding-agent/plans/active/setup-holds-when-several-fit-plan.md; docs/coding-agent/briefs/active/setup-names-what-is-missing-brief.md; docs/coding-agent/rules/common.md (Repository Reference Documents for pointer lines, Standing Approvals); docs/coding-agent/plans/active/setup-holds-when-several-fit-run.md. Read to understand, not as support: plugins/coding-agent-orchestration-harness/skills/rulebook/references/bootstrap-lifecycle.md (Philosophy Lines), rules-files.md (line forms), counsel/SKILL.md line 33, orchestration-harness/references/completion-closeout.md (Closeout Under Value-Level Operation). Instructions: value-audit-mandate.md, value-documents/SKILL.md.`

  `Product basis: brief in the product owner's words` (the brief: "product basis: the product owner's own words in this ratified brief. ebigunso owns the harness; no product philosophy and no engineering philosophy exist for this repository."; ratification record present: "I ratify the brief, hand it over after the run closes.", 2026-10-05; the several-fit statement carries its own record: "Yes, hold and ask when several fit.", 2026-10-06)

  `Not audited: engineering side; common.md reads "Engineering philosophy: none yet", which is not a pointer line, so that side has no document. The product philosophy line is also none yet; the product side is graded against the brief.`

  `Missing inputs: none`

  `Value documents changed in range: none` (plan draft; no range)

  Item lines:

  - DoD 1: several fitting documents: no pointer, an awaiting line naming the candidates and not the none-yet line, candidates brought in the report, the person's pick records the pointer | maps to the brief | cited | brief: "Where more than one document fits, setup likewise records nothing by itself and does not write the philosophy down as simply missing: it holds, shows the person the candidates, and the person picks." | -
  - DoD 2: the rest of the philosophy step behaves as at the start revision | maps to the brief | cited | brief: "Where the repository already has a philosophy document, setup finds it, records the pointer to it, and says in its report that it did"; "Where the only document that fits looks as if it may belong to something else in the repository ... it holds the decision and brings what it found to the person for confirmation." | -
  - DoD 3: shown on a fixture with two fitting documents by a fresh agent | internal mechanics | not audited | none; step 1 passed: reverting restores the prior state and nothing leaves the repository. It adds a check and changes none of the brief's pass conditions, and settles no human-only condition. | -
  - DoD 4: the value audit's fixed dispatch template byte-identical | internal mechanics | not audited | none; step 1 passed | -
  - DoD 5: package validators and smoke tests pass; Reviewer APPROVED | maps to the brief | cited | brief, Pass conditions: "Agent-checkable: the package validators pass" | -
  - DoD 6: the run closes as completion-closeout.md states: branch published, pull request opened, note to Counsel, nothing merged | internal mechanics | not audited | Publishing and the pull request are outward-facing and covered by the standing approval in common.md: "A finished, reviewed run may publish its branch and open pull requests in this repository without asking first. Merges are not covered and wait for the owner." Its record: "Given and accepted by the repository's owner, ebigunso, on 2026-09-30, relayed by Counsel: \"The common rule proposed, accepted.\"" The entry is committed at HEAD and no merge is planned. Whether the quoted words were said is not something the file can show. The note to Counsel I read as not outward-facing: it passes between the owner's own sessions working in this repository and reaches no person or system beyond them. No standing approval covers it, so if you read "a message sent" as catching it, that part is ask-now. | -
  - Planner-added: on "none of them", the line that replaces the awaiting line names each candidate as not it | maps to the brief | inferred | extends brief: "it holds, shows the person the candidates, and the person picks."; "Nothing nags. Work runs as it does today while a philosophy is missing, and no run reminds the person of it." Cheap to undo: a text revert. | -
  - Non-goal: any other branch of the philosophy step | maps to the brief | cited | the two statements quoted at DoD 2 | -
  - Non-goal: the texts on what is not a pointer | internal mechanics | not audited | none; step 1 passed | -
  - Non-goal: the fixed dispatch templates | internal mechanics | not audited | none; step 1 passed | -
  - Non-goal: a decision record | internal mechanics | not audited | none; step 1 passed | -
  - A1: a pick records that document's pointer, replaces the awaiting line, and nothing is written about the others | maps to the brief | inferred | The pick recording the pointer is the brief's "the person picks"; writing nothing about the unpicked candidates extends that statement and "Nothing nags." Cheap to undo. | -
  - A2: "none of them" leaves the none-yet line naming each as not it | maps to the brief | inferred | extends brief: "the person picks"; "Nothing nags." Cheap to undo. | -
  - Task_1: several fitting documents are held for the person to pick (setup text, line form, report, Counsel's opening mention, fourth fixture) | maps to the brief | cited | brief: "Where more than one document fits, setup likewise records nothing by itself and does not write the philosophy down as simply missing: it holds, shows the person the candidates, and the person picks."; for Counsel's mention, the means "A Counsel session sees those lines when it opens and may offer to start on one." Its "none of them" clause is the planner-added requirement, graded on its own line. | -
  - Task_2: close the plan and the run | internal mechanics | not audited | the standing approval quoted at DoD 6, with the same reading of the note to Counsel | -
  - Decision Log 1: no new line form, no record, no change to the texts on what is not a pointer | maps to the brief | inferred | extends brief: "setup likewise records nothing by itself ... it holds" (the same held state for one doubtful document and for several). Cheap to undo. | -
  - Decision Log 2a: the record of rejected candidates is kept only for an explicit "none of them" | maps to the brief | inferred | as A1 and A2 | -
  - Decision Log 2b: the fresh agent's fixture run moved into Task_1, before the review | internal mechanics | not audited | none; step 1 passed | -
  - Decision Log 2c: the version bump dropped | internal mechanics | not audited | none; step 1 passed: nothing is released by this item | -

  `Human-only conditions pending: "his first setup on a repository of his own, judged by whether what he was shown as missing was clear and whether anything pushed him."`

  `Scenarios: none`

  ### Files

  - [machine path redacted]\docs\coding-agent\plans\active\setup-holds-when-several-fit-plan.md
  - [machine path redacted]\docs\coding-agent\briefs\active\setup-names-what-is-missing-brief.md
  - [machine path redacted]\docs\coding-agent\rules\common.md
  - [machine path redacted]\docs\coding-agent\plans\active\setup-holds-when-several-fit-readings.md
  - [machine path redacted]\plugins\coding-agent-orchestration-harness\skills\orchestration-harness\references\value-audit-mandate.md

  How the Orchestrator applied it: no item is `ask-now` and none is `ungraded`. With the brief's ratification relayed by Counsel under the standing approval, the plan review closed with no finding open, and this verdict, the plan is authorized under the ratified brief; this records no approval by the owner. No item rests on a provisional statement. On the auditor's two procedural points the Orchestrator rules as in the earlier run that the verdict counts: the readings file was opened once, after the grades; the plan and brief were opened in the same step as the lookup for the mandate. The note to Counsel at closeout is the harness's own carrier between the owner's sessions, as every earlier audit of these runs read it. The comparison set readings apart from grades in class only, corrected in the readings file.
- 2026-10-06 Wave 1, Task_1: Worker report `done`, one YAML block, every changed file inside the task's `owns`. With more than one fitting document setup writes the awaiting line naming every candidate and brings them to the person to pick; a pick records that document's pointer; "none of them" leaves the none-yet line naming each as not it; a file gone at refresh drops from an awaiting line. The awaiting form reads `<Product | Engineering> philosophy: not settled. <path>[ or <path> ...] may be it and awaits the owner's word.` Counsel's opening sentence covers one or several awaiting documents. A fourth fixture, `with-two-philosophies`, holds the repository's own philosophy and a vendored project's. Worker validation: package validator pass, smoke tests pass, `git diff --check` clean. The Orchestrator's item, a fresh agent's setup on the fourth fixture, follows; then the review.
  - Judgement calls (Task_1): the wording for several paths keeps the one-file case as it was ("A or B may be it"; "A is not it, nor is B"); the report says why a file may belong to something else only where the line names a single file.
- 2026-10-06 Task_1, the Orchestrator's validation item: the fourth fixture was copied into a temporary git repository with its two ratification lines in place, and a fresh agent was given the same setup dispatch as the other fixtures. It recorded no pointer, wrote `Product philosophy: not settled. docs/product/what-tally-is-for.md or vendor/wordlist/docs/what-wordlist-is-for.md may be it and awaits the owner's word.`, did not write the none-yet line for the product philosophy, and brought both files with the person's word deciding. Its whole reply is stored in `tests/coding-agent-orchestration-harness/fixtures/setup-philosophy/RUN-2026-10-05-records/setup-reports.md`, and the run write-up has a section for it. Status: pass. Review: dispatched next.
- 2026-10-06 Review of Task_1, also the branch's final review (Codex reviewer, range from this plan's start revision): APPROVED, no finding. It read the stored fixture reply against the acceptance independently; validators and smoke tests pass; the mandate's template block and First Step and the manifests unchanged; privacy clean over the range. Task_1 is done.
- 2026-10-06 Closeout audit, dispatch text (to a fresh Auditor dispatch on Fable):

  ```text
  You are the value auditor. Read references/value-audit-mandate.md of the orchestration-harness skill and follow it exactly. Position: closeout. Plan: docs/coding-agent/plans/active/setup-holds-when-several-fit-plan.md. Governing brief: docs/coding-agent/briefs/active/setup-names-what-is-missing-brief.md. Changes since: 34cb534.
  ```

- 2026-10-06 Closeout audit, verdict as returned (machine paths redacted; the two comparison lines are logged in the readings file, not here):

  ## Value audit verdict: closeout, setup-holds-when-several-fit

  No item is `ask-now` and none is `ungraded`. No judgement call is marked `direction`.

  Procedural points for you to rule on before logging:

  - **Reading order.** The mandate is not in the plugin cache, so my first lookup missed. The plan, the brief and a `git diff --stat` were opened in that same step, before the mandate was read. All three are inputs of this position. No notes file was opened. The readings file was opened once, after the grades were fixed. The mandate voids an audit only for a readings file opened early, so I graded; re-dispatch if you read the First Step more strictly.
  - **Dispatch content.** The dispatch text matches the fixed template exactly. The context also carried harness-injected text (a reviewer role prompt, the engineering-quality-baselines skill, a ponytail hook). None contains an account of the work, so I did not treat it as text beyond the template.
  - **Untracked files.** `.claude/pr67body.tmp` (dated Sep 15) and `.claude/settings.local.json` (dated Jul 23) predate the range and were not opened; the first is pull request text by its name.
  - **Checks I ran myself.** `validate_harness_package.py` passed, `run_validation_smoke_tests.py` exited 0, and `git diff --check` over the range was clean.

  ### Verdict record

  `Position: closeout`

  `Documents read: docs/coding-agent/plans/active/setup-holds-when-several-fit-plan.md; docs/coding-agent/briefs/active/setup-names-what-is-missing-brief.md; docs/coding-agent/rules/common.md (Repository Reference Documents for pointer lines; Standing Approvals); docs/coding-agent/plans/active/setup-holds-when-several-fit-run.md; the range 34cb534..working tree by git diff with the two exclude pathspecs (counsel/SKILL.md, rulebook/references/bootstrap-lifecycle.md, rulebook/references/rules-files.md, tests/.../fixtures/setup-philosophy/**). Read to understand, not as support: docs/coding-agent/plans/completed/setup-names-what-is-missing-run.md; the Counsel lines of orchestration-harness/references/completion-closeout.md; the headings of tests/.../setup-philosophy/RUN-2026-10-05.md. Instructions: value-audit-mandate.md, value-documents/SKILL.md.`

  `Product basis: brief in the product owner's words` (the brief: "product basis: the product owner's own words in this ratified brief. ebigunso owns the harness; no product philosophy and no engineering philosophy exist for this repository."; ratification record present: "I ratify the brief, hand it over after the run closes.", 2026-10-05; the several-fit statement carries its own record: "Yes, hold and ask when several fit.", 2026-10-06)

  `Not audited: engineering side; common.md reads "Engineering philosophy: none yet", which is not a pointer line, so that side has no document. The product philosophy line is also none yet; the product side is graded against the brief.`

  `Missing inputs: none`

  `Value documents changed in range: none` (no brief, philosophy, pointer line or decision record changed between 34cb534 and the working tree; common.md is unchanged in the range)

  Item lines, the plan:

  - DoD 1: several fitting documents: no pointer, an awaiting line naming the candidates and not the none-yet line, candidates brought in the report, the person's pick records the pointer | maps to the brief | cited | brief: "Where more than one document fits, setup likewise records nothing by itself and does not write the philosophy down as simply missing: it holds, shows the person the candidates, and the person picks." | -
  - DoD 2: the rest of the philosophy step behaves as at the start revision | maps to the brief | cited | brief: "Where the repository already has a philosophy document, setup finds it, records the pointer to it, and says in its report that it did"; "Where the only document that fits looks as if it may belong to something else in the repository ... it holds the decision and brings what it found to the person for confirmation." The diff leaves the one-document, doubtful-document and no-document branches as they were. | -
  - DoD 3: shown on a fixture with two fitting documents by a fresh agent | internal mechanics | not audited | none; step 1 passed: it stays in the repository, adds a check and changes none of the brief's pass conditions, and settles no human-only condition | -
  - DoD 4: the value audit's fixed dispatch template byte-identical | internal mechanics | not audited | none; step 1 passed. The range changes no file under the orchestration-harness skill. | -
  - DoD 5: package validators and smoke tests pass; Reviewer APPROVED | maps to the brief | cited | brief, Pass conditions: "Agent-checkable: the package validators pass" | -
  - DoD 6: the run closes as completion-closeout.md states: branch published, pull request opened, note to Counsel, nothing merged | internal mechanics | not audited | Publishing and the pull request are outward-facing and covered by the standing approval in common.md: "A finished, reviewed run may publish its branch and open pull requests in this repository without asking first. Merges are not covered and wait for the owner." Its record: "Given and accepted by the repository's owner, ebigunso, on 2026-09-30, relayed by Counsel: \"The common rule proposed, accepted.\"" The entry is committed at HEAD and unchanged in the range; no merge is planned. Whether the quoted words were said is not something the file can show. The note to Counsel is graded on the ruling's own line below. | -
  - Planner-added: on "none of them", the line that replaces the awaiting line names each candidate as not it | maps to the brief | inferred | extends brief: "it holds, shows the person the candidates, and the person picks."; "Nothing nags. Work runs as it does today while a philosophy is missing, and no run reminds the person of it." Cheap to undo: a text revert. | -
  - Non-goal: any other branch of the philosophy step | maps to the brief | cited | the two statements quoted at DoD 2 | -
  - Non-goal: the texts on what is not a pointer | internal mechanics | not audited | none; step 1 passed | -
  - Non-goal: the fixed dispatch templates | internal mechanics | not audited | none; step 1 passed | -
  - Non-goal: a decision record | internal mechanics | not audited | none; step 1 passed | -
  - A1: a pick records that document's pointer, replaces the awaiting line, and nothing is written about the others | maps to the brief | inferred | the pick recording the pointer is the brief's "the person picks"; writing nothing about the others extends that statement and "Nothing nags." Cheap to undo. | -
  - A2: "none of them" leaves the none-yet line naming each as not it | maps to the brief | inferred | extends brief: "the person picks"; "Nothing nags." Cheap to undo. | -
  - Task_1: several fitting documents are held for the person to pick | maps to the brief | cited | brief: the several-fit statement quoted at DoD 1. Its parts that go beyond that statement are graded on the change lines below. | -
  - Task_2: close the plan and the run | internal mechanics | not audited | the standing approval quoted at DoD 6 | -
  - Decision Log 1: no new line form, no record, no change to the texts on what is not a pointer | maps to the brief | inferred | extends brief: "setup likewise records nothing by itself ... it holds" (one held state for a doubtful single document and for several). Cheap to undo. | -
  - Decision Log 2a: the record of rejected candidates is kept only for an explicit "none of them" | maps to the brief | inferred | as A1 and A2 | -
  - Decision Log 2b: the fresh agent's fixture run moved into Task_1, before the review | internal mechanics | not audited | none; step 1 passed | -
  - Decision Log 2c: the version bump dropped | internal mechanics | not audited | none; step 1 passed: nothing is released by this item | -

  Item lines, the changes:

  - bootstrap-lifecycle.md: with more than one fitting document, setup records none, writes the awaiting line naming every one and not the none-yet line, and brings them in the report to pick | maps to the brief | cited | brief: the several-fit statement quoted at DoD 1 | -
  - bootstrap-lifecycle.md: the person's word on an awaiting line: yes to one file writes its pointer line and nothing about the others; no to all writes the none-yet line naming each | maps to the brief | inferred | the yes is the brief's "the person picks"; the rest extends it and "Nothing nags." Cheap to undo. | -
  - bootstrap-lifecycle.md: at refresh, a file that is gone drops from an awaiting line; the files that remain, even one alone, still await the person's word; with none left the line becomes the none-yet line | maps to the brief | inferred | extends brief: "it holds, shows the person the candidates, and the person picks."; "At refresh, a pointer to a file that is gone or moved is flagged, as it is for decision records." (means). A remaining single candidate is kept held, not recorded by setup, which tightens who decides and loosens nothing. Cheap to undo. The plan's Definition of Done and Task_1 acceptance do not state this behaviour; only the Progress Log's Worker entry does. | -
  - bootstrap-lifecycle.md: the report for an awaiting line gives each file it names and that the person's word decides; the none-yet report no longer lists the files found where more than one fitted | maps to the brief | cited | brief: "shows the person the candidates, and the person picks." | -
  - rules-files.md: the awaiting form names one or more paths ("<path>[ or <path> ...] may be it and awaits the owner's word"); four forms as before (the persisted line format; the plan's compatibility stance is break) | maps to the brief | inferred | extends brief: "does not write the philosophy down as simply missing: it holds"; "the common rule file carries a line for each missing philosophy" (means). Cheap to undo: a text revert; no line written by this branch exists outside the fixtures' records. | -
  - rules-files.md: the none-yet-after-objection form names one or more paths ("<path> is not it[, nor is <path> ...]") | maps to the brief | inferred | as A2 | -
  - counsel/SKILL.md: Counsel's opening mention covers one or more documents awaiting the owner's word on which, if any, is the philosophy; mentioned once | maps to the brief | inferred | extends brief: "A Counsel session sees those lines when it opens and may offer to start on one." (means); "Nothing nags." Cheap to undo. | -
  - tests/.../setup-philosophy: the fourth fixture `with-two-philosophies`, its ratification lines kept apart, the stored setup reply and the write-up section | internal mechanics | not audited | none; step 1 passed. No file in the fixture carries a ratification record in place, so nothing here is a ratified philosophy in this repository. | -

  Item lines, the judgement calls:

  - Worker: the wording for several paths keeps the one-file case as it was ("A or B may be it"; "A is not it, nor is B") | maps to the brief | inferred | extends brief: "shows the person the candidates"; the line is what the person reads in common.md. Cheap to undo. | -
  - Worker: the report says why a file may belong to something else only where the line names a single file | maps to the brief | inferred | extends brief: "shows the person the candidates, and the person picks." With several candidates nothing is recorded, so the single-document statement's "Nothing obviously awkward passes quietly" is not loosened. Cheap to undo. In the stored fixture reply the person is shown two paths and no word that one sits in a vendored project. | -
  - Orchestrator ruling: the plan-draft verdict counts despite the auditor's order of reading | internal mechanics | not audited | none; step 1 passed: nothing irreversible or outward-facing | -
  - Orchestrator ruling: the note to Counsel at closeout is the harness's own carrier between the owner's sessions, not an outward-facing message | internal mechanics | not audited | none. Step 1 as I read it: the note goes to the owner's own Counsel session for this repository, which is how a result reaches the owner, and it reaches no person or system beyond the owner. No standing approval covers it: the second entry in common.md covers relays from Counsel to an Orchestrator session, not the reverse. If you read the mandate's "a message sent" as catching it, this item is `ask-now`, with the question whether a finished run may tell the owner's Counsel session that it has closed without asking first. | -
  - Orchestrator ruling: the plan is authorized under the ratified brief | internal mechanics | not audited | none; that decision is the Plan Gate's and a verdict approves nothing | -

  `Human-only conditions pending: "his first setup on a repository of his own, judged by whether what he was shown as missing was clear and whether anything pushed him."`

  `Scenarios: 1. A repository with no philosophy: demonstrated; observe in tests/coding-agent-orchestration-harness/fixtures/setup-philosophy/RUN-2026-10-05.md, section "Scenario 1, no-philosophy", and RUN-2026-10-05-records/setup-reports.md. 2. A repository that already has a product philosophy: demonstrated; observe in the same write-up, section "Scenario 2, with-product-philosophy". 3. A Counsel session mentions what is missing and offers to start; an Orchestrator session does not: not yet. Prior states: by the mandate every scenario is "not yet" before this run's first plan closes; the run record instead carries 1 and 2 as demonstrated and 3 as not yet from the run that closed on 2026-10-06. Against either prior, neither demonstration of 1 and 2 was made in this range, the branches they exercise are unchanged by the diff, and nothing in the range bears on 3. Getting closer: yes. At the start revision the setup text contradicted the brief's several-fit statement ("record none and write the none-yet line"); the text now gives it, and the stored reply on the fourth fixture shows no pointer, the awaiting line naming both files and no none-yet line for the product philosophy. Not shown anywhere: a pick or a "none of them" being applied, and a later refresh leaving the line alone. That the stored reply is a fresh agent's whole reply is the record's claim, which I could not check.`

  ### Files

  - [machine path redacted]\docs\coding-agent\plans\active\setup-holds-when-several-fit-plan.md
  - [machine path redacted]\docs\coding-agent\briefs\active\setup-names-what-is-missing-brief.md
  - [machine path redacted]\docs\coding-agent\rules\common.md
  - [machine path redacted]\docs\coding-agent\plans\active\setup-holds-when-several-fit-run.md
  - [machine path redacted]\docs\coding-agent\plans\active\setup-holds-when-several-fit-readings.md
  - [machine path redacted]\plugins\coding-agent-orchestration-harness\skills\orchestration-harness\references\value-audit-mandate.md
  - [machine path redacted]\plugins\coding-agent-orchestration-harness\skills\rulebook\references\bootstrap-lifecycle.md
  - [machine path redacted]\plugins\coding-agent-orchestration-harness\skills\rulebook\references\rules-files.md
  - [machine path redacted]\plugins\coding-agent-orchestration-harness\skills\counsel\SKILL.md
  - [machine path redacted]\tests\coding-agent-orchestration-harness\fixtures\setup-philosophy\RUN-2026-10-05.md

  How the Orchestrator applied it: no item is `ask-now` or `ungraded`, none is marked `direction`, and no record was reworded in the range, so nothing is held. The audit judges the run is getting closer: the text now gives the brief's several-fit statement and the fourth fixture shows it; the plan closes and with it the run. No item rests on a provisional statement. On the auditor's procedural points the Orchestrator rules as before that the verdict counts (the readings file was opened once, after the grades), and keeps its reading of the note to Counsel as the harness's own carrier between the owner's sessions, which is how a result reaches him; both rulings are the audited party's own and are named in the closeout. The comparison set two readings apart from their grades in class only, corrected in the readings file with nothing to redo. One thing the auditor noticed is carried to the closeout as an observation for the owner: with several candidates the report shows the paths and does not say that one of them sits in a vendored project.
- 2026-10-06 Plan closed: Task_1 done; Task_2's closeout audit done, and the publication of the branch with its pull request and the note to Counsel follow this commit. Required validation: package validator and smoke tests pass; review APPROVED.

## Decision Log (append-only; re-plans and major discoveries)
- 2026-10-06 Decision: requirement challenge before decomposition.
  - Trigger / new insight: the statement is one sentence and asks for one branch to change.
  - Plan delta (what changed): no new line form, no record, no change to the texts on what is not a pointer.
  - Tradeoffs considered: see Design.
  - User approval: not applicable at draft
  - Record proposed: none
- 2026-10-06 Decision: draft-plan review (Codex reviewer): NEEDS_REVISION, three minor findings, all applied.
  - Trigger / new insight: the planner-added line recorded every candidate not picked, against A1 and for a reason that does not hold once a pointer exists; the fixture evidence Task_1 needs was placed in Task_2; the version bump's stated reason was not true of the validator.
  - Plan delta (what changed): the record of rejected candidates is kept only for an explicit "none of them"; the fresh agent's setup on the fourth fixture is the Orchestrator's validation item inside Task_1, before the review, which reads the stored reply; the version bump is dropped, no rule or check asking for one.
  - Tradeoffs considered: none further.
  - User approval: not applicable at draft
  - Record proposed: none

## Notes
- The audits of this run: this plan's draft and its close.
