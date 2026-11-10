# Plan: Decision records at intent altitude, the three raised decisions

- status: draft
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

## Decision Log (append-only; re-plans and major discoveries)
- 2026-11-11 Plan review (Codex seat `agent-harness-reviewer`, pinned at 4a9cc30): CHANGES_REQUESTED, three minor findings, all accepted. RAI-P1: keeping a missing snippet section as a failure kept an exact-heading match, which is the same failure on prose; the checker no longer fails on the heading's wording either, and the acceptance shows a reworded heading. RAI-P2: the Design set a compliant design against one the lifecycle forbids, and read "warns at most" as requiring a warning; it now holds the new-record lifecycle fixed, compares keeping a warning with removing the check, and the planner-added requirement says the warning is the plan's choice. RAI-P3: the checker task's owns let fixtures into the shipped plugin's scripts directory; a fixture, if one is needed at all, goes under `tests/coding-agent-orchestration-harness/`. The review's inventory finds no other unlisted addition. Its notes, taken: ADR-D-0037 delegates the loader route to ADR-D-0020, so the loader obligation is not assumed gone; if no decision of ADR-D-0020's own survives, the replacement is not written and the Definition of Done item waits on the owner; an area's output is counted again after its splits and the area subdivided before its batch is presented.

## Notes (Risks / Edge cases)
- Pull request 95 is open on another branch and also sets the version; whichever lands second takes the next one.
- The record replacing ADR-D-0020 sits beside ADR-D-0037; the risk is two records holding one decision. Task_1's first acceptance bullet tests each with the other held fixed, and if nothing of ADR-D-0020 is left as a decision of its own, the report says so and the record is not written: ADR-D-0020 would then be retired as overtaken, which returns to the owner.
