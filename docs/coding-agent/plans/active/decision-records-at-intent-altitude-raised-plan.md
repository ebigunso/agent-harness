# Plan: Decision records at intent altitude, the three raised decisions

- status: authorized 2026-11-11 by the brief route (plan review closed, plan-draft audit holds nothing); in execution
- generated: 2026-11-11
- last_updated: 2026-11-11
- work_type: mixed

## Goal
- Carry out the owner's answers of 2026-11-11 on the three decisions the census raised, under the governing brief `docs/coding-agent/briefs/active/decision-records-at-intent-altitude-brief.md` (section "The three raised decisions, answered 2026-11-11"): ADR-D-0016 is brought to what the plugin's text says, ADR-D-0020 is corrected where a later record and the text overtook it, and the package checker is brought in line with ADR-I-0007.
- The brief is the requirement and is not restated here; where this plan and the brief differ, the brief governs and the difference is a plan defect.
- This is the first plan of the run recorded in `docs/coding-agent/plans/active/decision-records-at-intent-altitude-run.md`. The batches of about ten records follow it, each a unit of its own.

## Definition of Done
- A proposed record replaces ADR-D-0016 and states the decision as the owner confirmed it: a protection needs a demonstrable consumer; where a consumer cannot be verified, the question goes to the person directing the work only for a surface that crosses the repository's boundary, and inside the repository the change goes ahead and is reported. It meets the record standard and reaches him by name (brief, the answers' section, its inferred sentence on these two records).
- A proposed record replaces ADR-D-0020 and states its decision without the sentence the later record and the text overtook: a session takes the Orchestrator role by the deliberate routes ADR-D-0037 and the plugin's text name, and a load by description match or an incidental reference does not make one. Whatever of ADR-D-0020 is only procedure (which rule files are loaded, in what order) is not covered by the record and is confirmed present in the plugin's text. It meets the record standard and reaches him by name.
- The package checker no longer fails on the wording of the Reviewer's latent-risk prompt snippet, its heading included: it warns at most, and a reviewer judges whether the risks are covered (brief, the third answer). ADR-I-0007 is not changed by this plan.
- The decisions themselves do not change beyond what his three answers state; nothing else in any record, and no other checker behaviour, is changed.
- No accepted record is retired by this plan: ADR-D-0016 and ADR-D-0020 are retired, with their inbound references repaired, only when he accepts their replacements by name.
- Package validators and smoke tests pass; the branch has Reviewer `APPROVED`; value audits at plan draft and closeout are logged; the unit is reported: branch published, pull request opened under the standing approval, note to Counsel, nothing merged.

## Planner-added requirements
- Whatever of ADR-D-0020 is only procedure is confirmed present in the plugin's text before the replacement leaves it out. Needed because: the brief has a record's operational material placed in the rule or skill text that already states it, or added there, and a replacement that silently dropped the rule-entry step would lose it.
- The checker's change keeps a warning in place of the failure. His answer sets an upper bound ("it warns at most") and does not require a warning, so keeping one is the plan's choice. Needed because: someone rewording the snippet is then told which risks a reviewer will look for, at the moment of the edit, where a silent pass tells them nothing (Design).
- The version is the next version over `main` when made, last. Needed because: an installed plugin is refreshed only when its version changes, and this plan changes a shipped script.

## Scope / Non-goals
- Scope: two new proposed records under `docs/coding-agent-orchestration-harness/decisions/`; `plugins/coding-agent-orchestration-harness/scripts/validate_harness_package.py` (the latent-risk snippet check) and the smoke tests that exercise it; the version files.
- Non-goals: every other record the census classed (the batches); ADR-I-0007's own wording; the record standard and its template (the census's two observations on the template go to the owner as a question with the first batch); retiring ADR-D-0016 or ADR-D-0020 before acceptance.

## Design
- Proportional form does not apply: the checker's behaviour on a shipped contract changes.
- Fixed by the record standard and the brief, and not compared: each of the two records is replaced by a new complete record, the old one retired on acceptance.
- The remaining choice is what the checker does with the snippet.
- Chosen: the checker keeps its list of the topics the snippet should cover and looks for the snippet without depending on its heading's exact words; a topic it does not find, or a snippet it cannot find, is reported as a warning that never fails the run.
- Alternative: the snippet check is removed, and whether the snippet covers the risks is left wholly to review.
- structure: the chosen design keeps a second place that knows the topics (the checker beside the snippet), which must be kept in step; the alternative has one (the snippet).
- evolution: under the chosen design a new topic is two edits and a stale list gives a false warning; under the alternative it is one edit and nothing can go stale. The alternative has the shorter deletion path, being the deletion.
- verification: the chosen design adds one smoke case (a reworded snippet passes with a warning); the alternative adds none, and the review rubric carries the whole check.
- operation: no runtime cost under either.
- human: the chosen design tells whoever rewords the snippet, when they do it, which risks a reviewer will look for; the alternative tells them nothing until review.
- safety: neither changes a trust boundary.
- Why chosen wins: the snippet is copied and adapted by people who have not read the review rubric, and a warning at the edit costs less than a review round; the price is a list kept in step, which the warning itself exposes when it is stale.

## Compatibility stance
- break, for one checker behaviour: a package whose latent-risk snippet lacks one of the listed topics no longer fails validation. The locatable consumers are this repository's package checks and smoke tests, which are changed with it; no consumer relies on the failure. The records' filenames change only at acceptance, when references are repaired.

## Context (workspace)
- The census of 2026-11-10 by the Researcher seat (49 accepted records) raised three decisions; the owner answered all three through Counsel on 2026-11-11, taking Counsel's advice on each.
- ADR-D-0037 holds that a session role is entered by an explicit act; `orchestration-harness/SKILL.md` states the three routes for the Orchestrator role.
- `engineering-quality-baselines/references/core-principles.md` and `plan-format/SKILL.md` state the surface split for an unverifiable consumer.
- Readings file: `docs/coding-agent/plans/active/decision-records-at-intent-altitude-readings.md`.
- Research: the census is this plan's research; the Orchestrator checked the three cited conflicts against the files before they went to the owner.

## Open Questions (max 3)
- None.

## Assumptions
- The latent-risk snippet check is the only place the package checker fails on prompt wording; Task_2 reports any other it finds and changes none.

## Tasks

### Task_1: The two replacement records
- type: docs
- owns:
  - docs/coding-agent-orchestration-harness/decisions/ (two new proposed records only)
- depends_on: []
- description: |
  Write the two proposed records that replace ADR-D-0016 and ADR-D-0020, from the old records, the brief's section "The three raised decisions, answered 2026-11-11" and the plugin's text they are brought to. The record standard is `durable-docs-authoring/references/adr.md` with its template; quote it where the report relies on it.
- acceptance:
  - Each record holds one decision, tested with every neighbouring decision held fixed, and states it so that any rewording of the plugin's text that preserves it stays valid; no exact mechanics.
  - The record replacing ADR-D-0016 states the surface split as the owner confirmed it and keeps everything else ADR-D-0016 decided; the record replacing ADR-D-0020 leaves out the overtaken sentence, agrees with ADR-D-0037, and leaves the rule-entry procedure to the plugin's text, which the report shows already states it.
  - Each Why is prose, present tense, a sentence or two, the fork and the reason one branch won; it cites no brief, plan or person's ruling as its authority; every rejected alternative carries its reopen condition or is rejected outright with its reason; no wording names a thing by its position or order.
  - Status proposed; `supersedes` names the old record; numbers follow the directory's next free numbers; filenames at most 109 characters, so that the retirement suffix keeps them within 135.
  - Nothing is decided that the old record, the owner's answer and the plugin's text do not decide; where a reason is not written down anywhere, the report says so and none is invented.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: every record filename cited in the two records' front matter exists; from `plugins/coding-agent-orchestration-harness/`, `py -I scripts/validate_harness_package.py`; from the repository root, `git diff --check`.
  - kind: review
    required: true
    owner: reviewer
    detail: each record against the standard and against the old record, clause by clause: what is kept, what moved to the plugin's text and where it is stated there, what the owner's answer changed.

### Task_2: The checker warns and does not fail on the snippet's wording
- type: impl
- owns:
  - plugins/coding-agent-orchestration-harness/scripts/validate_harness_package.py
  - plugins/coding-agent-orchestration-harness/scripts/run_validation_smoke_tests.py
  - tests/coding-agent-orchestration-harness/ (a fixture only if the smoke runner cannot make the reworded case inline)
- depends_on: []
- description: |
  Bring the latent-risk snippet check in line with ADR-I-0007: the checker does not fail on the snippet's wording, the wording of its heading included. A topic it does not find, or a snippet it cannot find because the heading was reworded or the section moved, is reported as a warning. A check of the package's files and structure that is not a match on prompt prose is left as it is.
- acceptance:
  - With the snippet unchanged the checker passes with no warning; with one topic phrase reworded to an equivalent, it passes and prints a warning that names the topic; with only the snippet's heading reworded and its body unchanged, it passes, with a warning at most.
  - No other check changes; any other place the checker fails on prompt wording is reported and left.
  - One smoke case covers a reworded topic and one a reworded heading, made inline by the runner where it can.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: from `plugins/coding-agent-orchestration-harness/`, `py -I scripts/validate_harness_package.py` and `py -I scripts/run_validation_smoke_tests.py`; the three cases of the first acceptance bullet shown with their output and exit codes; from the repository root, `git diff --check`.
  - kind: review
    required: true
    owner: reviewer
    detail: the diff against ADR-I-0007's decision and invariant; that a warning cannot become a failure through an exit code or a count.

### Task_3: Version
- type: chore
- owns:
  - .claude-plugin/marketplace.json
  - .github/plugin/marketplace.json
  - plugins/coding-agent-orchestration-harness/.claude-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.codex-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.github/plugin/plugin.json
- depends_on: [Task_1, Task_2]
- description: |
  The Orchestrator's own task: the next version over `main` at the time it is made, in every file that states it.
- acceptance:
  - The version is the next version over `main` at the time it is made.
  - Every file that states the plugin's version states that version, and no file states another.
- validation:
  - kind: command
    required: true
    owner: orchestrator
    detail: a search for the old and the new version outside `docs/`; `py -I scripts/validate_harness_package.py` and `py -I scripts/run_validation_smoke_tests.py`.

## Task Waves (explicit parallel dispatch sets)
- Wave 1: Task_1, Task_2
- Wave 2: Task_3

## Rollback / Safety
- Records, one script and its tests, on a branch; a revert restores them. Nothing is retired before acceptance and nothing merges without the owner's acceptance naming the pull request.

## Progress Log (append-only)
- 2026-11-10T21:41Z Value audit dispatched (Claude subagent `harness-auditor` on Fable, a new dispatch), text verbatim:
  You are the value auditor. Read references/value-audit-mandate.md of the orchestration-harness skill and follow it exactly. Position: plan draft. Plan: <worktree>/docs/coding-agent/plans/active/decision-records-at-intent-altitude-raised-plan.md. Governing brief: <worktree>/docs/coding-agent/briefs/active/decision-records-at-intent-altitude-brief.md. Changes since: none.
- 2026-11-10T21:47Z Verdict as returned (machine paths shortened; the two comparison lines are in the readings file):
  Value audit verdict: plan draft, no `ask-now`, nothing `ungraded`.
  Two things to know before the record:
  - **Order of reading.** I opened the plan and the brief in the same step in which I located the mandate, so before I had read the mandate to its end. That departs from its First Step. Neither is a notes or readings file, the notes file was never opened, and the readings file was opened once, after the grades were fixed. The mandate voids an audit only for a readings file opened early; whether this departure warrants a fresh dispatch is yours to decide.
  - **Dispatch.** It matches the fixed template with nothing added.
  Repository root for every path below: the worktree (HEAD de999fb, working tree clean).
  ## Verdict record
  Position: plan draft
  Documents read:
  - Value documents and artifact: `docs/coding-agent/briefs/active/decision-records-at-intent-altitude-brief.md`; `docs/coding-agent/plans/active/decision-records-at-intent-altitude-raised-plan.md` (all of it, as claims); `docs/coding-agent/rules/common.md` (sections "Repository Reference Documents" and "Standing Approvals", unchanged against HEAD).
  - Instructions: `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/value-audit-mandate.md`; `plugins/coding-agent-orchestration-harness/skills/value-documents/SKILL.md`.
  - Read to understand, never as support: `docs/coding-agent/plans/active/decision-records-at-intent-altitude-run.md`; ADR-D-0016, ADR-D-0020, ADR-D-0037 and ADR-I-0007 under `docs/coding-agent-orchestration-harness/decisions/`; `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/SKILL.md` (lines 8-37); `plugins/coding-agent-orchestration-harness/scripts/validate_harness_package.py` (lines 216-415); name-only searches of `engineering-quality-baselines/references/core-principles.md` and `plan-format/SKILL.md`.
  - After the grades were fixed, once: `docs/coding-agent/plans/active/decision-records-at-intent-altitude-readings.md`.
  - Not opened: `docs/coding-agent/briefs/active/decision-records-at-intent-altitude-notes.md`, and every `*-notes.md` and `*-readings.md` under `completed/`.
  Product basis: brief in the product owner's words ("product basis: the product owner's own words in this brief. ebigunso owns the harness; no product philosophy and no engineering philosophy exist for this repository.")
  Not audited: engineering side; it has no document (`common.md` reads "Engineering philosophy: none yet", which is not a pointer line). The product philosophy is also "none yet"; the product side is graded on the brief.
  Missing inputs: none. The brief is under `active/`, carries its ratification record ("Nothing to add, I ratify the brief, hand it over.", 2026-11-02) and its product basis; its amendments of 2026-11-11 carry quoted words with the date.
  Value documents changed in range: none (plan draft; no range).
  Items:
  - DoD: a proposed record replaces ADR-D-0016, states the surface split, meets the standard and reaches him by name | maps to the brief | cited | Brief: "ADR-D-0016 (protection requires demonstrable consumers): his decision is what the plugin's text says. Where nobody can show who uses something, a run asks him only when the thing is visible outside the repository; inside the repository it goes ahead and says what it did. The record is behind the text and is rewritten to say this." Brief: "A record that fails the check is rewritten to meet it, under the standard's own lifecycle: a new complete record, the old one retired, accepted by name." Brief, Limits: "Acceptance is by name, as the standard says; one statement may accept several records when it names each." | - (The plan names the answers' section's sentence tagged inferred as its source for "by name". That sentence has no ratification record of its own and is no support. The item does not depend on it: the Limits constraint covers acceptance by name, and the told exception, "A rewrite that does not materially change what its decision is about goes in without his reading it", does not reach a record whose decision wording changes.)
  - DoD: a proposed record replaces ADR-D-0020 without the overtaken sentence; its procedure is left to the plugin's text and confirmed there; it reaches him by name | maps to the brief | cited | Brief: "ADR-D-0020 (loader-routed sessions assume the Orchestrator role): the record was overtaken by ADR-D-0037 and the plugin's text. A session becomes the Orchestrator only by the deliberate routes they name, not because the skill was loaded on a description match. The old sentence is corrected in the rewrite." Brief: "exact mechanics (routes, moves, file names, admission of a relay, template fill-ins) not covered". Brief, Limits: "Acceptance is by name, as the standard says" | -
  - DoD: the checker no longer fails on the wording of the Reviewer's latent-risk snippet, heading included; it warns at most; ADR-I-0007 unchanged | maps to the brief | cited | Brief: "ADR-I-0007 (validators never fail on exact prose): the record stands and the checker is brought in line with it. The check that requires exact phrases in the Reviewer's prompt snippet warns at most, and whether the snippet covers those risks is a reviewer's judgement." | - (The heading is one of the exact phrases that check requires; the file-exists failure is left as it is.)
  - DoD: the decisions do not change beyond his three answers; nothing else in any record and no other checker behaviour changes | maps to the brief | cited | Brief: "The decisions themselves do not change. The work moves altitude, not outcome; where a check finds a decision itself wrong, stale or contradicted, that is a value question for the owner through Counsel, not a rewrite." | -
  - DoD: no accepted record is retired by this plan; ADR-D-0016 and ADR-D-0020 are retired, references repaired, only on his acceptance by name | maps to the brief | cited | Brief: "a new complete record, the old one retired, accepted by name"; Limits: "Acceptance is by name, as the standard says" | -
  - DoD: validators and smoke tests pass; Reviewer APPROVED; audits logged; branch published, pull request opened, note to Counsel, nothing merged | internal mechanics | not audited | Step 1 was run. Publishing the branch and opening the pull request are outward-facing and covered by `common.md` Standing Approvals: "A finished, reviewed run may publish its branch and open pull requests in this repository without asking first. Merges are not covered and wait for the owner. ... Given and accepted by the repository's owner, ebigunso, on 2026-09-30, relayed by Counsel: \"The common rule proposed, accepted.\"" The entry records its giver and his acceptance with the date and is committed at HEAD; whether the words were said is not something the file can show. | - (The note to Counsel is read as not outward-facing: it goes to the run's own carrier on the local peer channel, which `common.md` names, and reaches nobody outside the repository's work. No merge is planned.)
  - Planner-added: ADR-D-0020's procedure is confirmed present in the plugin's text before the replacement leaves it out | maps to the brief | cited | Brief: "a record found to carry only operational material is retired and its material placed in the rule or skill text that already states it, or added there"; scenario 3: "its material confirmed present in the rule or skill text, or placed there" | -
  - Planner-added: the checker keeps a warning in place of the failure | maps to the brief | cited | Brief: "The check that requires exact phrases in the Reviewer's prompt snippet warns at most, and whether the snippet covers those risks is a reviewer's judgement." | - (The statement bounds from above; a warning sits inside the bound.)
  - Planner-added: the version is the next over `main`, made last | maps to the brief (the third answer, by extension) | inferred | Extends the brief's "the checker is brought in line with it": a shipped script changes, and the version is how that change reaches an installed plugin. No statement names a version. Cheap to undo: a revert restores the files; nothing is released by this plan. | -
  - Non-goal: every other record the census classed (the batches) | maps to the brief | cited | Brief: "The records whose decision the check finds stale or contradicted reach him first, as value questions through Counsel, before the rest is rewritten"; "The rest reaches him in batches by area, each batch its own pull request and its own acceptance, of about ten records." | -
  - Non-goal: ADR-I-0007's own wording | maps to the brief | cited | Brief: "the record stands and the checker is brought in line with it" | -
  - Non-goal: the record standard and its template; the census's two observations on the template go to the owner as a question with the first batch | maps to the brief | cited | Brief: "Where the check finds that the standard's own form invites the detail (a section that asks for enumeration, a template that mirrors procedure), that is reported to the owner through Counsel as a value question; the standard is not changed by this work without his word." | - (The brief fixes no time for that report; "with the first batch" is the plan's timing and changes nothing in the standard.)
  - Non-goal: retiring ADR-D-0016 or ADR-D-0020 before acceptance | maps to the brief | cited | Brief: "a new complete record, the old one retired, accepted by name" | -
  - Assumption: the latent-risk snippet check is the only place the checker fails on prompt wording; Task_2 reports any other and changes none | maps to the brief | inferred | Extends the third answer, which names one check ("The check that requires exact phrases in the Reviewer's prompt snippet"), and the constraint that what a check finds contradicted is "a value question for the owner through Counsel, not a rewrite". Cheap to undo: nothing is changed. | - (See the first observation below: the file contradicts the assumption as a fact.)
  - Task_1: the two replacement records | maps to the brief | cited | Brief: "one decision per record; the constraint stated so that any rewording of the plugin text that preserves it stays valid; the why in prose at intent altitude; exact mechanics ... not covered"; "The check also asks whether a record's wording names the thing it means rather than its position, order or relation to something else"; "The decisions themselves do not change." | -
  - Task_2: the checker warns and does not fail on the snippet's wording | maps to the brief | cited | Brief: the third answer, quoted above | - (Fixture placement and the smoke cases are internal mechanics, not audited.)
  - Task_3: version | maps to the brief (by extension) | inferred | As the planner-added version item | -
  - Decision Log 2026-11-11, RAI-P1: the heading's wording no longer fails either | maps to the brief | cited | Brief: the third answer, quoted above | -
  - Decision Log 2026-11-11, RAI-P2: the new-record lifecycle held fixed; the warning stated as the plan's choice | maps to the brief | cited | Brief: "under the standard's own lifecycle: a new complete record, the old one retired, accepted by name"; "warns at most" | -
  - Decision Log 2026-11-11, RAI-P3: a fixture, if needed, goes under `tests/coding-agent-orchestration-harness/` | internal mechanics | not audited | - | -
  - Decision Log 2026-11-11, note: the loader obligation is not assumed gone; if no decision of ADR-D-0020's own survives, the replacement is not written and the item waits on the owner | maps to the brief | cited | Brief: "where a check finds a decision itself wrong, stale or contradicted, that is a value question for the owner through Counsel, not a rewrite"; scenario 4: "A record whose decision the check finds no longer true: not rewritten; brought to the owner through Counsel." | - (This tightens who decides.)
  - Decision Log 2026-11-11, note: an area's output is counted again after its splits and the area subdivided before its batch is presented | maps to the brief | cited | Brief: "batches by area, each batch its own pull request and its own acceptance, of about ten records" | -
  Human-only conditions pending: none marked. The brief's two pass conditions carry neither an agent-checkable nor a human-only mark, though `value-documents/SKILL.md` asks for one on each.
  Scenarios: none
  ## Observations outside the grades
  - **The assumption is contradicted by the file as a fact.** `validate_harness_package.py` line 387 fails an Orchestrator adapter that lacks text matching `do not edit bundled.*harness`, which is a match on prompt prose. Lines 392-398 fail on two exact phrases in `improvement-loop/SKILL.md`. The plan's handling still holds (Task_2 reports and changes none), but it does not say where that report goes after the Worker. Under the brief, a checker at odds with ADR-I-0007 elsewhere is a question for the owner through Counsel. Until then the Goal's sentence "the package checker is brought in line with ADR-I-0007" is true of the named check only.
  - **Pass condition on recording the check's result.** The plan has no step that records the result for these three records ("rewritten (to which)" or "raised"), which the brief's pass condition asks for every record. The run record's unit table is the likely place at closeout.
  - **The readings file is not named in the plan's Context.** The run record names it, and the plan's Goal names the run record. The mandate has the auditor take it from the plan's Context section.
- Acting on the verdict: it holds nothing: no item ask-now or ungraded, no missing inputs. The plan review is closed (APPROVED at 769ab15) and the audit holds nothing, so the brief's ratification authorizes the plan and the first wave is dispatched; no one is asked. Inferred, journaled for the closeout: the version; the assumption that the snippet check is the only prose match. The audit finds that assumption false as a fact: the package checker also fails on prose where it matches an Orchestrator adapter's text and two phrases of the improvement-loop skill. Ruling: Task_2 changes the named check only, as planned, and reports every other prose match it finds; the Orchestrator takes that report to Counsel as a question for the owner, since his answer named one check. Readings that diverge are under-claims (read extends, graded cited), corrected in the reading. Two gaps the audit names, closed here: the check's result for these records is recorded in the run record's unit table at closeout, as the brief's pass condition asks; and the readings file is named in the plan's Context. The first-step deviation is one more occurrence of what the lesson of 2026-11-07 tracks.

## Decision Log (append-only; re-plans and major discoveries)
- 2026-11-11 Plan review (Codex seat `agent-harness-reviewer`, pinned at 4a9cc30): CHANGES_REQUESTED, three minor findings, all accepted. RAI-P1: keeping a missing snippet section as a failure kept an exact-heading match, which is the same failure on prose; the checker no longer fails on the heading's wording either, and the acceptance shows a reworded heading. RAI-P2: the Design set a compliant design against one the lifecycle forbids, and read "warns at most" as requiring a warning; it now holds the new-record lifecycle fixed, compares keeping a warning with removing the check, and the planner-added requirement says the warning is the plan's choice. RAI-P3: the checker task's owns let fixtures into the shipped plugin's scripts directory; a fixture, if one is needed at all, goes under `tests/coding-agent-orchestration-harness/`. The review's inventory finds no other unlisted addition. Its notes, taken: ADR-D-0037 delegates the loader route to ADR-D-0020, so the loader obligation is not assumed gone; if no decision of ADR-D-0020's own survives, the replacement is not written and the Definition of Done item waits on the owner; an area's output is counted again after its splits and the area subdivided before its batch is presented.

## Notes (Risks / Edge cases)
- Pull request 95 is open on another branch and also sets the version; whichever lands second takes the next one.
- The record replacing ADR-D-0020 sits beside ADR-D-0037; the risk is two records holding one decision. Task_1's first acceptance bullet tests each with the other held fixed, and if nothing of ADR-D-0020 is left as a decision of its own, the report says so and the record is not written: ADR-D-0020 would then be retired as overtaken, which returns to the owner.
