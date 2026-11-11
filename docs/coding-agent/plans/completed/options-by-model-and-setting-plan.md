# Plan: An option is a model at the setting it runs at

- status: done 2026-11-11 (final review APPROVED; closeout audit holds nothing; scenario 2 not yet, and one finding with the owner through Counsel)
- generated: 2026-11-11
- last_updated: 2026-11-11
- work_type: docs

## Goal
- The harness gives what the governing brief `docs/coding-agent/briefs/active/options-by-model-and-setting-brief.md` states: the plugin's text speaks of an option as a seat or a subagent, on a model, at a setting; names reasoning effort as the setting it means; has setup record the settings worth telling apart; has a resolution name its option's setting and a dispatch run at it; and says where a role goes when the option it resolves to is unavailable.
- The brief is the requirement and is not restated here; where this plan and the brief differ, the brief governs and the difference is a plan defect.
- This is the first plan of the run recorded in `docs/coding-agent/plans/active/options-by-model-and-setting-run.md`.

## Definition of Done
- `skills/subagent-strategy/references/model-routing.md` defines an option and a setting as the brief does, names reasoning effort as the setting it means and says the same holds of any other setting a runtime offers, without naming one; everything it says of options (the capability finding, the cost judgement, the fit ranking, the cost-bounded walk) reads of options so understood (brief, "What the plugin states", first to third statements).
- The same reference states, for every role, where a role goes when the option it resolves to is unavailable when a dispatch is due, and that the dispatcher says which option it used and why (brief, fifth statement). What it says today for research where no recorded option fits stays true.
- Setup (`skills/rulebook`: `references/bootstrap-lifecycle.md` Models Record, `references/rule-suite-templates.md`, `references/rules-files.md`) records an option's reasoning effort with its model, records the settings worth telling apart and not every setting a model offers, makes the capability finding and the cost judgement per option, names the setting in each resolution, and states the setting an option runs at where the runtime gives the dispatch no choice or a seat's setting was fixed by whoever set it up (brief, third and fourth statements).
- Every other plugin text that tells a dispatcher which option a role runs on speaks of the setting where it speaks of the model, or points to the reference that does.
- No plugin rule names a model, a family alias, a provider, a seat, a price or a level of reasoning effort; the seed names providers only, as dated observations; the owner's words are not quoted in the plugin's text (brief, Limits).
- The reasons by role are unchanged, and no resolution in this repository's `common.md` changes (brief, Limits). Whether that record's own form needs a pointer or a line brought into the new form is Task_3's to find.
- ADR-D-0068, ADR-D-0069 and ADR-D-0070 are not contradicted. A decision record is proposed only if the admission test passes, and then waits for the owner's acceptance by name (brief, Limits).
- Scenarios 1 and 3 are shown on a fixture and scenario 2 by reading this repository's record against the text, outcomes in the Progress Log; the human-only pass condition stays pending and the closeout says so.
- The plugin's version is the next minor version over `main` at the time it is made, in every file that states it.
- Package validators and smoke tests pass; the branch has Reviewer `APPROVED`; value audits at plan draft and closeout are logged; the run is reported ready: branch published, pull request opened under the standing approval, note to Counsel, nothing merged.

## Planner-added requirements
- Every other plugin text that tells a dispatcher which option a role runs on speaks of the setting where it speaks of the model, or points to the reference that does. Needed because: the brief's second scenario has each dispatch run at the setting its resolution names, and a dispatcher reads its dispatch rules in `subagent-strategy/SKILL.md`, the dispatch checklists, the dispatch guidance and the `counsel` skill before it reads the routing reference; a line there that says "on which model" and stops would leave the setting out of the dispatch.
- The version is the next minor over `main` when made, last. Needed because: an installed plugin is refreshed only when its version changes, and a later fix must not ship under a version already published.
- Scenarios 1 and 3 are shown on a fixture. Needed because: the brief's agent-checkable conditions are about the text, and a text can say all of it and still not lead a setup to two options for one model; a fresh agent following the text on a made-up lineup is the cheapest way to see that it does.
- Added at integration, each with its reason in the Decision Log: a setting setup cannot read is recorded as not known (D2); the record's form has a place for the option a resolution names for the unavailable case (D3); the sentence that an unavailable option still fits the work (D5).

## Scope / Non-goals
- Scope: `skills/subagent-strategy/references/model-routing.md`; `skills/subagent-strategy/SKILL.md` and its dispatch references where they say which option a role runs on; `skills/orchestration-harness/references/dispatch-guidance.md` and `skills/counsel/SKILL.md` for the same; `skills/rulebook/references/bootstrap-lifecycle.md` (Models Record), `rule-suite-templates.md`, `rules-files.md`; this repository's `docs/coding-agent/rules/common.md` only if its record's form needs it; the version files.
- Non-goals: the reasons by role; any resolution in this repository's record; the seed's entries; recording every setting of every model (brief, "Left out on purpose"); how a runtime adapter passes a setting to a dispatch, beyond the plugin's text saying the dispatch runs at it wherever the runtime lets the dispatch choose.

## Design
- Fixed by the brief and not compared: an option is a seat or a subagent, on a model, at a setting, and everything said of options holds of options so understood.
- The remaining choice is how that definition, and the rule for an unavailable option, are carried through the texts that use them.
- Chosen: both are stated once, in `model-routing.md` (the definition in The record of options, the unavailable-option rule in Tiers and fallback, for all roles). Setup's texts, the dispatch texts and the `counsel` skill use the terms and point there. The research rule's step for "no recorded option fits" stays as it is, as the Researcher's case of a different question (nothing fits, as against the fitting option being unavailable).
- Alternative: each text that acts on an option carries what it needs in full: setup's Models Record restates what a setting is and which settings to record, each dispatch text restates that a dispatch runs at the resolution's setting, and each role's reason carries its own unavailable-option line.
- structure: chosen has one owner for the definition and one for the rule, and the other texts depend on that stable place; the alternative duplicates both across four or five files, with a conversion to keep in step at every edit.
- evolution: a runtime that adds a kind of setting, or a change to the unavailable-option rule, is one edit under the chosen design and one per file under the alternative; the alternative's blast radius is every text that restates. Concept count is the same; the chosen design has the shorter deletion path.
- verification: both are checked by reading and by the fixture. Under the chosen design the review checks one statement and the pointers to it; under the alternative it checks that every restatement agrees.
- operation: no runtime cost under either. A dispatcher under the chosen design reads one more reference where it did not already; the routing reference is already read whenever more than one model is available.
- human: the alternative lets a reader of one file act without following a pointer; the chosen design asks for the pointer and in return cannot disagree with itself.
- safety: neither changes a trust boundary or what a dispatch may reach.
- Why chosen wins: the record of options already has one home in the plugin, `model-routing.md`, which the other texts point to, and the brief's limits (no model, no level of reasoning effort in the rules) are checked most surely against one statement.

## Compatibility stance
- preserve. The record of options in a workspace's `common.md` is a persisted form with locatable consumers: this repository's record, and any workspace set up since version 1.3.0. A record that names no setting stays valid and in force; a refresh brings it into the form with settings, as a refresh already rewrites an older form (`bootstrap-lifecycle.md`, Models Record, last paragraph). No record is invalidated by the change.

## Context (workspace)
- The text this changes entered `main` with pull request 94 (version 1.3.0): `model-routing.md`, the seed, `bootstrap-lifecycle.md` Models Record, the record's form in `rule-suite-templates.md`.
- This repository's record has named settings in its resolutions since 2026-11-11 (`docs/coding-agent/rules/common.md`, Models And Peers In This Workspace).
- ADR-D-0068 defines an option as "a way a workspace has to run a role: an in-session subagent or a peer seat, each on some model". ADR-D-0069 holds the Researcher that the dispatcher can always run where no recorded option fits.
- Research waived: the scope is the plugin text the previous run of this session wrote and the Orchestrator read in full before drafting (`model-routing.md`, the seed, `bootstrap-lifecycle.md` Models Record, the record template, `rules-files.md` line on the section, and a search of the plugin for the places that say which option a role runs on).

## Open Questions (max 3)
- None for the owner. Whether a decision record is needed is Task_1's to test and report.

## Assumptions
- "Reasoning effort" may be named in the plugin's rules as a kind of setting; no level of it may be (brief, Limits).
- Validators hold no assertion on the sentences this changes; Task_1 and Task_2 confirm by running them.

## Tasks

### Task_1: The option, the setting and the unavailable option
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/subagent-strategy/references/model-routing.md
  - plugins/coding-agent-orchestration-harness/skills/subagent-strategy/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/subagent-strategy/references/dispatch-checklists.md
  - plugins/coding-agent-orchestration-harness/skills/subagent-strategy/references/prompt-snippets.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/dispatch-guidance.md
  - plugins/coding-agent-orchestration-harness/skills/counsel/SKILL.md
  - docs/coding-agent-orchestration-harness/decisions/ (a new proposed record only, if the admission test passes)
- depends_on: []
- description: |
  Bring the routing reference to the brief's "What the plugin states", first, second, third and fifth statements, and bring the other texts a dispatcher reads to agree. The brief is the content; the wording is the Worker's, and the owner's words are not quoted in the plugin's text.
- acceptance:
  - The reference defines an option and a setting as the brief does and names reasoning effort as the setting it means; it says the same statements hold of any other setting a runtime offers that changes what a model can do or what it costs, naming none; no level of reasoning effort, model, family alias, provider, seat or price appears in any plugin rule.
  - Everything the reference says of options reads of options so understood, with no statement left that ties the capability finding, the cost judgement, the fit ranking or the walk to a model alone.
  - A resolution names its option's setting and a dispatch on it runs at that setting wherever the runtime lets the dispatch choose; where it does not, or a seat's setting was fixed by whoever set it up, the record states the setting the option runs at and the reference's best-effort statement applies.
  - For every role: where the option a role resolves to is unavailable when a dispatch is due, the role goes to what its resolution names for that case, and where it names nothing, to the next option in the fit ranking for that work that the role's cost setting accepts; the dispatcher says which option it used and why. The research rule's own step for the case where no recorded option fits still holds and the two do not contradict.
  - Each other owned text that says which option a role runs on speaks of the setting where it speaks of the model, or points to the reference; nothing else in those texts changes.
  - Propose an ADR if the admission test passes, per `durable-docs-authoring/references/adr.md`; if it fails, the report says why. ADR-D-0068, 0069 and 0070 are not contradicted, and if one would have to be reworded the report says so and nothing in it is changed.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: from `plugins/coding-agent-orchestration-harness/`, `py -I scripts/validate_harness_package.py` and `py -I scripts/run_validation_smoke_tests.py`; from the repository root, `git diff --check`.
  - kind: review
    required: true
    owner: reviewer
    detail: the acceptance bullets against the brief, read with the Limits; a search of the plugin's rules for any model, family alias, provider, seat, price or level of reasoning effort.

### Task_2: Setup records the settings worth telling apart
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/rulebook/references/bootstrap-lifecycle.md
  - plugins/coding-agent-orchestration-harness/skills/rulebook/references/rule-suite-templates.md
  - plugins/coding-agent-orchestration-harness/skills/rulebook/references/rules-files.md
  - plugins/coding-agent-orchestration-harness/skills/rulebook/SKILL.md
- depends_on: []
- description: |
  Bring setup's Models Record step, the record's form and the line that describes the section to the brief's first, third and fourth statements. The definition of an option and a setting is Task_1's, in `model-routing.md`; these texts use it and do not restate it.
- acceptance:
  - Setup's options are read with the settings the runtime offers for each model and each seat's fixed setting; it records as options of their own the settings that differ for some role's work or in cost, and not every setting a model offers; the capability finding and the cost judgement are made per option; the record is shown for confirmation with these options in it.
  - Each resolution line in the record's form names its option's setting; where the runtime gives the dispatch no choice, or a seat's setting was fixed by whoever set it up, the record states the setting the option runs at.
  - A record that names no setting stays valid and in force, and a refresh brings it into the form with settings as a refresh rewrites an older form.
  - The texts speak of an option's reasoning effort as well as its model, name no level of it, and name no model, family alias, provider, seat or price.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: from `plugins/coding-agent-orchestration-harness/`, `py -I scripts/validate_harness_package.py` and `py -I scripts/run_validation_smoke_tests.py`; from the repository root, `git diff --check`.
  - kind: review
    required: true
    owner: reviewer
    detail: the acceptance bullets against the brief; agreement with Task_1's text on what an option and a setting are.

### Task_3: This repository's record and the scenarios
- type: test
- owns:
  - docs/coding-agent/rules/common.md
  - docs/coding-agent/plans/active/options-by-model-and-setting-plan.md (Progress Log)
- depends_on: [Task_1, Task_2]
- description: |
  The Orchestrator's own task; only the Orchestrator edits rule files. Read this repository's record against the changed text, and show the scenarios.
- acceptance:
  - This repository's record is read against the new form: no resolution changes; any line whose form the changed text now asks for differently (the options this workspace has, say) is brought into it, and what was changed is logged with the reason.
  - Scenario 1: a fresh agent given only the plugin's text and a made-up lineup with one model at more than one setting fills a record that lists the differing settings as options of their own, each with its finding and cost, and resolves a cost-bounded role to the stronger model's lower setting where that is the fit its cost setting accepts. The prompt and the outcome are in the Progress Log.
  - Scenario 3, both branches on one made-up record: a fresh agent given only the plugin's text, the record and the statement that a Worker's resolved option is unavailable (a) takes the option the resolution names for that case, where it names one; and (b) where the resolution names nothing, takes the next option in the fit ranking that the role's cost setting accepts, passing over a higher-ranked option the cost setting rejects. In each it reports which option ran the task and why. The prompts and the outcomes are in the Progress Log.
  - Scenario 2 is shown by reading: each resolution in this repository's record names a setting, and the changed text has a dispatch run at it.
- validation:
  - kind: manual
    required: true
    owner: orchestrator
    detail: the two fixture runs and the reading, logged with their prompts and outcomes; a fixture whose outcome does not show the scenario is a finding against Task_1 or Task_2, not a waiver.

### Task_4: Version
- type: chore
- owns:
  - .claude-plugin/marketplace.json
  - .github/plugin/marketplace.json
  - plugins/coding-agent-orchestration-harness/.claude-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.codex-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.github/plugin/plugin.json
- depends_on: [Task_3]
- description: |
  The Orchestrator's own task: the next minor version over `main` at the time it is made, in every file that states it.
- acceptance:
  - The version is the next minor version over `main` at the time it is made.
  - Every file that states the plugin's version states that version, and no file states another.
- validation:
  - kind: command
    required: true
    owner: orchestrator
    detail: a search for the old and the new version across the repository outside `docs/`; `py -I scripts/validate_harness_package.py` and `py -I scripts/run_validation_smoke_tests.py`.

## Task Waves (explicit parallel dispatch sets)
- Wave 1: Task_1, Task_2
- The first wave's two tasks have disjoint owns; the setup task uses the routing task's definition by name and is reconciled with it at integration.
- Wave 2: Task_3
- Wave 3: Task_4

## Rollback / Safety
- Text and rule-file changes only, on a branch; a revert restores them. Nothing is published before the run is reported ready, and nothing merges without the owner's acceptance naming the pull request.

## Progress Log (append-only)
- 2026-11-10T18:55Z Value audit dispatched (Claude subagent `harness-auditor` on Fable, a new dispatch), text verbatim:
  You are the value auditor. Read references/value-audit-mandate.md of the orchestration-harness skill and follow it exactly. Position: plan draft. Plan: <main checkout>/docs/coding-agent/plans/active/options-by-model-and-setting-plan.md. Governing brief: <main checkout>/docs/coding-agent/briefs/active/options-by-model-and-setting-brief.md. Changes since: none.
- 2026-11-10T19:00Z Verdict as returned (machine paths shortened; the two comparison lines are in the readings file):
  Value audit verdict, plan draft. No item is `ask-now`. All grades were fixed before the readings file was opened.
  Procedure, disclosed: I opened the plan and the brief in the same step in which I located the mandate, so before I had read the mandate to its end. Both are inputs. No notes file was opened at any point, and the readings file was opened once, after the grades were fixed. One git command printed content without the exclude pathspecs: `git show a204548 -- docs/coding-agent/rules/common.md`, a single commit on one named path, filtered to the standing-approval line. The dispatch carried nothing beyond the fixed template.
  Paths written down as not to be opened before grading: every `docs/coding-agent/briefs/completed/*-notes.md` (five files, among them `model-defaults-by-reason-notes.md`, which the brief points to) and every `docs/coding-agent/plans/**/*-readings.md`, among them `docs/coding-agent/plans/active/options-by-model-and-setting-readings.md`.
  ## Verdict record
  Position: plan draft
  Documents read:
  - Instructions: `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/value-audit-mandate.md` and `plugins/coding-agent-orchestration-harness/skills/value-documents/SKILL.md`.
  - Inputs: `docs/coding-agent/briefs/active/options-by-model-and-setting-brief.md`, `docs/coding-agent/plans/active/options-by-model-and-setting-plan.md`, and `docs/coding-agent/rules/common.md` (pointer lines and Standing Approvals, at HEAD 00ab329, working tree clean apart from untracked `.claude/`).
  - Read to understand what the plan changes, never as support: that same `common.md`'s Models And Peers section; `plugins/coding-agent-orchestration-harness/skills/subagent-strategy/references/model-routing.md`; `.../subagent-strategy/references/model-tendencies-seed.md`; `.../rulebook/references/bootstrap-lifecycle.md` (Models Record); ADR-D-0068 and ADR-D-0069 under `docs/coding-agent-orchestration-harness/decisions/`. ADR-D-0070 was not opened.
  - After grading: `docs/coding-agent/plans/active/options-by-model-and-setting-readings.md`. The plan's Context section does not name it; the run record the plan names does (`options-by-model-and-setting-run.md`, line 6).
  Product basis: brief in the product owner's words. The brief says so ("the product owner's own words in this brief once ratified. ebigunso owns the harness; no product philosophy and no engineering philosophy exist for this repository") and carries its ratification record ("I ratify it.", 2026-11-11).
  Not audited: the engineering side. `common.md` reads "Engineering philosophy: none yet", so there is no document. The product philosophy line also reads "none yet"; the product side is graded on the brief.
  Missing inputs: none
  Value documents changed in range: none (plan draft, no range)
  Items ("brief" is the governing brief):
  - DoD 1, the routing reference defines an option and a setting, names reasoning effort, names no other setting, and everything said of options reads of options so understood | maps to the brief | cited | brief: "The plugin's text names reasoning effort as the setting it means."; "The same statements hold of any other setting a runtime offers that changes what a model can do or what it costs; the text says so without naming one."; "An option is a way to run a role: a seat or a subagent, on a model, at a setting."; "Everything the plugin already says of options holds of options so understood" | -
  - DoD 2, the unavailable-option rule for every role, the dispatcher says which option and why, and the research step for no fitting option stays true | maps to the brief | cited | brief: "Where the option a role resolves to is unavailable when a dispatch is due, the role goes to what its resolution names for that case; where the resolution names nothing, to the next option in the fit ranking for that work that the role's cost setting accepts. The dispatcher says which option it used and why."; "The decision records ADR-D-0068, ADR-D-0069 and ADR-D-0070, accepted 2026-11-11, are not contradicted by this." | -
  - DoD 3, setup records an option's reasoning effort with its model, the settings worth telling apart, finding and cost per option, and the setting in each resolution | maps to the brief | cited | brief: "Two settings of one model that differ for some role's work, or in cost, are two options in the workspace's record."; "the capability finding is made for the option, its cost is judged for the option"; "A resolution names its option's setting ... Where the runtime gives no such choice, or a seat's setting was fixed by whoever set it up, the record states the setting the option runs at"; the means "Setup records the settings worth telling apart, not every setting a model offers, and shows them for confirmation with the rest of the record.", which the plan follows | -
  - DoD 4, every other plugin text that tells a dispatcher which option a role runs on speaks of the setting or points to the reference | maps to the brief | cited | brief: "Everything the plugin already says of options holds of options so understood"; "a dispatch on that resolution runs at it wherever the runtime lets the dispatch choose"; scenario 2, "Each dispatch runs at the setting its resolution names" | -
  - DoD 5, no plugin rule names a model, alias, provider, seat, price or level of reasoning effort; the seed names providers only; the owner's words are not quoted | maps to the brief | cited | brief: "No model name, family alias, provider, seat or price enters the plugin's rules; the seed names providers only, as observations with dates."; "Reasoning effort is named as a kind of setting; no level of it is named"; "His words are not carried into the plugin's text as quotations, and are not read to the letter." | -
  - DoD 6, reasons by role unchanged and no resolution in this repository's record changes; whether the record's form needs a line brought into the new form is Task_3's to find | maps to the brief | inferred | covered for the first sentence by the brief: "The reasons by role do not change, and no resolution in this repository's record changes; that record has named settings since 2026-11-11." A change of form to this repository's record is covered by no statement. It extends "Two settings of one model that differ for some role's work, or in cost, are two options in the workspace's record." and "Someone who sets up the harness in a repository, or refreshes its record when a model changes, gets a record that tells apart the settings a model can run at". It is cheap to undo. The grade covers form only (note 1). | -
  - DoD 7, ADR-D-0068 to ADR-D-0070 not contradicted; a decision record proposed only if the admission test passes, then waits for the owner's acceptance by name | maps to the brief | cited | brief: "The decision records ADR-D-0068, ADR-D-0069 and ADR-D-0070, accepted 2026-11-11, are not contradicted by this. If the run finds that a decision record is needed or that an accepted one must be reworded, that record returns to him for acceptance by name." | -
  - DoD 8, scenarios 1 and 3 shown on a fixture, scenario 2 by reading; the human-only condition stays pending and the closeout says so | maps to the brief | inferred | the way each scenario is shown is covered by no statement; it extends the brief's Core scenarios 1, 2 and 3. Keeping the human-only condition pending is covered: "Human-only: the next time a model arrives with more than one setting, he judges whether the refreshed record found the fitting setting for each role without his naming it." No proxy settles it. Cheap to undo. | -
  - DoD 9, the plugin's version is the next minor over `main`, in every file that states it | maps to the brief (a version is observable to whoever installs the plugin, and it is how the changed text reaches them) | inferred | no statement covers it; it extends the brief: "Someone who sets up the harness in a repository, or refreshes its record when a model changes, gets a record that tells apart the settings a model can run at". Cheap to undo; the version change publishes nothing by itself. | -
  - DoD 10, validators and smoke tests pass, Reviewer `APPROVED`, value audits logged, run reported ready with the branch published and a pull request opened, note to Counsel, nothing merged | maps to the brief | cited | brief, Pass conditions: "the package validators pass". Publishing the branch and opening the pull request are outward-facing and pass step 1 on the standing approval in `common.md`, Standing Approvals: "A finished, reviewed run may publish its branch and open pull requests in this repository without asking first. Merges are not covered and wait for the owner. ... Given and accepted by the repository's owner, ebigunso, on 2026-09-30, relayed by Counsel: \"The common rule proposed, accepted.\"" The entry is committed at HEAD and records giver, acceptance and date; whether the quoted words were said is not something the file can show. The note to Counsel I did not treat as outward-facing: it goes to the owner's own Counsel session on the workspace's peer channel, as the final report goes to the owner. | -
  - Planner-added 1, the other dispatch texts speak of the setting or point to the reference | maps to the brief | cited | as DoD 4 | -
  - Planner-added 2, the version is the next minor over `main` when made, last | maps to the brief | inferred | as DoD 9 | -
  - Planner-added 3, scenarios 1 and 3 shown on a fixture | maps to the brief | inferred | extends Core scenarios 1 and 3; it adds a check and loosens none. Cheap to undo. | -
  - Non-goal 1, the reasons by role | maps to the brief | cited | brief: "The reasons by role do not change" | -
  - Non-goal 2, any resolution in this repository's record | maps to the brief | cited | brief: "no resolution in this repository's record changes" | -
  - Non-goal 3, the seed's entries | maps to the brief | cited | brief: "the seed names providers only, as observations with dates"; "no level of it is named, since levels belong to a workspace's record like the models they are set on" | -
  - Non-goal 4, recording every setting of every model | maps to the brief | cited | brief, Left out on purpose: "Recording every setting of every model at setup." | -
  - Non-goal 5, how a runtime adapter passes a setting to a dispatch, beyond the text saying the dispatch runs at it where the runtime lets it choose | maps to the brief | inferred | no statement covers leaving the adapters alone; it extends the brief: "a dispatch on that resolution runs at it wherever the runtime lets the dispatch choose. Where the runtime gives no such choice ... what the plugin says of best effort applies." Cheap to undo. A search of the plugin found no adapter file that fixes a reasoning effort. | -
  - Assumption 1, "reasoning effort" may be named as a kind of setting, no level of it | maps to the brief | cited | brief: "Reasoning effort is named as a kind of setting; no level of it is named" | -
  - Assumption 2, validators hold no assertion on the sentences this changes | internal mechanics | not audited | no engineering philosophy; not irreversible or outward-facing | -
  - Task_1, the option, the setting and the unavailable option | maps to the brief | cited | brief, "What the plugin states", first, second, third and fifth statements as quoted under DoD 1, 2 and 4; Limits as quoted under DoD 5 and 7 | -
  - Task_2, setup records the settings worth telling apart | maps to the brief | inferred | covered for its first, second and fourth acceptance bullets by the statements quoted under DoD 3 and DoD 5. Its third bullet, that a record naming no setting stays valid and in force until a refresh brings it into the form, is covered by no statement; it extends "or refreshes its record when a model changes, gets a record that tells apart the settings". Cheap to undo. | -
  - Task_3, this repository's record and the scenarios | maps to the brief | inferred | as DoD 6 for the record's form and DoD 8 for the scenarios; the constraint "no resolution in this repository's record changes" is kept in its acceptance. Notes 1 and 2. | -
  - Task_4, version | maps to the brief | inferred | as DoD 9 | -
  - Decision Log 2026-11-11, OPT-P1, the wave note moved to its own line | internal mechanics | not audited | no engineering philosophy | -
  - Decision Log 2026-11-11, OPT-P2, the version task given two acceptance bullets | internal mechanics | not audited | no engineering philosophy; what the bullets ask is graded under Task_4 | -
  - Decision Log 2026-11-11, OPT-P3, the Design holds the option's identity fixed and compares only how it is carried through the texts | maps to the brief | cited | brief: "An option is a way to run a role: a seat or a subagent, on a model, at a setting."; "It states what and why. How is the Orchestrator's, except where a means is stated". The comparison that remains, one home against restating in each text, is how the text is organised and has no engineering document. | -
  - Decision Log 2026-11-11, OPT-P4, the scenario 3 fixture shows both branches of the rule | maps to the brief | inferred | extends Core scenario 3 and the fifth statement, "where the resolution names nothing, to the next option in the fit ranking for that work that the role's cost setting accepts"; it adds a check. Cheap to undo. | -
  Human-only conditions pending: "the next time a model arrives with more than one setting, he judges whether the refreshed record found the fitting setting for each role without his naming it."
  Scenarios: none
  ## Notes beside the record (no grade rests on them)
  1. Three seat resolutions in this repository's record name no setting at HEAD: the Researcher's rigor work, the Worker's logic-oriented coding and the Reviewer's rigorous review (`common.md`, lines 59 to 61). Task_3's reading for scenario 2, "each resolution in this repository's record names a setting", therefore does not hold of the record as written. The brief's scenario 2 names only the Auditor and a design-writing Worker, and both of those do name one. Stating a seat's setting would be new content in the owner's confirmed record, not a change of form: an observation of the seat, or his to state. The `inferred` grade on DoD 6 and Task_3 covers a line that says nothing the record does not already say.
  2. Scenario 2 shown by reading shows what the text says, not that a dispatch ran at the recorded setting. Which state that earns is the closeout audit's to judge on the evidence then.
  3. The standing-approval line entered the repository whole in commit a204548 (2026-10-15, pull request 72). I found no later change to it, so nothing shows its terms moved after the acceptance it records.
- Acting on the verdict: it holds nothing: no item ask-now or ungraded, no missing inputs. The plan review is closed (APPROVED at 00ab329) and the audit holds nothing, so the brief's ratification authorizes the plan and the first wave is dispatched; no one is asked. Inferred items, journaled as extensions for the closeout: a change of form to this repository's record; how the scenarios are shown; the version; leaving the runtime adapters alone; a record that names no setting staying in force until a refresh; the fixture showing both branches. Readings that diverge are under-claims or differences of side (the other dispatch texts read extends and graded cited; the version read as internal mechanics and graded inferred on the product side; the validators read not audited and graded cited), corrected in the reading. The audit's first note is taken as a ruling: three seat resolutions in this repository's record (the Researcher's rigor work, the Worker's logic-oriented coding, the Reviewer's rigorous review) name no setting, so Task_3's reading for scenario 2 is of the resolutions that name one, the Auditor's and the design-writing Worker's among them as the brief's scenario names; stating a seat's setting is new content in the owner's confirmed record, not a change of form, and goes to Counsel as a question, not into the record. The first-step deviation is one more occurrence of what the lesson of 2026-11-07 tracks.
- 2026-11-10T19:01Z Wave 1 dispatched: Task_1 and Task_2, each to a Claude subagent `harness-worker` on Fable 5.2 at low reasoning effort (the record's resolution for design and writing). Each dispatch: "Carry out <Task_X> of the plan `docs/coding-agent/plans/active/options-by-model-and-setting-plan.md` in <main checkout>, on the branch checked out. Read the governing brief `docs/coding-agent/briefs/active/options-by-model-and-setting-brief.md` first; it is the requirement and the plan does not restate it. The task's owns, acceptance and validation are in the plan; the plan's Design says where the definition and the unavailable-option rule live. The other first-wave task runs at the same time in the same checkout on disjoint files: do not touch its owns. Do not commit or push. Use `py -I` for Python. Open no `*-notes.md` or `*-readings.md` file. Report one YAML block per the subagent-report-contract skill, with questions and judgement calls under questions." Task_2's dispatch adds: "The definition of an option and a setting is Task_1's, in `model-routing.md` The record of options; use the terms option, setting and reasoning effort as the brief defines them and point there, without restating the definition."
- 2026-11-10T19:04Z Wave 1 integrated: Task_1 and Task_2 done, each after one follow-up on the Orchestrator's rulings; every edit inside owns as widened below; required Worker checks pass for both (`validate_harness_package.py`, `run_validation_smoke_tests.py`, `git diff --check`), rerun after the last edit with both tasks' changes in the tree.
  - Task_1: `model-routing.md` defines an option (a seat or a subagent, on a model, at a setting) and a setting in The record of options, names reasoning effort as the setting it means and says the same of any other setting, naming none; the capability finding, the fit ranking and the tendencies' tie read of the option; a resolution names its setting and a dispatch runs at it where the runtime lets it choose, otherwise the record states the setting and best effort applies; Tiers and fallback carries the unavailable-option rule for every role, and research step 5 says it is the other case. `subagent-strategy/SKILL.md` and `counsel/SKILL.md` speak of the setting where they spoke of the model. `dispatch-checklists.md`, `prompt-snippets.md` and `dispatch-guidance.md` needed nothing.
  - Task_2: `bootstrap-lifecycle.md` Models Record reads options with their settings, records as options of their own the settings that differ for a role's work or in cost, makes the finding and the cost per option, names the setting in each resolution and states a fixed or unchoosable one; a record naming no setting stays in force until a refresh. `rule-suite-templates.md` and `rules-files.md` carry the same in the record's form and its description. `rulebook/SKILL.md` needed nothing.
  - Judgement calls: Task_1 kept the Orchestrator's reason line as it is; says nothing of a fit ranking with no further acceptable option; reworded "only one model" to "only one option"; proposes no decision record, the admission test failing because the definition and the rule are stated in the reference itself and a miss shows on the next diff, with ADR-D-0068 to ADR-D-0070 not contradicted and unchanged. Task_2 makes the findings per setting first and then collapses the settings that differ in neither work nor cost; a freshly filled resolution line always carries the where-unavailable clause, as "none named" where none is. The Orchestrator ruled each of these kept (D2 to D5 below for the four that add something).
- 2026-11-10T19:12Z Wave 1 review (Codex seat `agent-harness-reviewer`, pinned at 8feb768): CHANGES_REQUESTED, one minor finding; both tasks' acceptance, the additions D2 to D5, the unchanged reasons by role, the name search and both validators check out, and it agrees no decision record is needed.
  - OPT-W1-F1 (minor): "When only one option is available, it covers every role" was unconditional beside the new rule, so a role left with one option its cost setting rejects was sent there by one line and past it by the next. Ruling: accepted. The line now speaks of a record that holds only one option, never of a role left with one because another is unavailable, and sets aside no reason or cost setting. No destination is invented for the case where no accepted option is left.
  - The review's process observation: the plan-draft audit opened the plan and the brief before reading its mandate alone. Recorded as a lesson occurrence at closeout.
- 2026-11-10T19:12Z Task_3, the Orchestrator's own. Fixtures run on Claude subagents on Fable 5.2 at low reasoning effort, each a fresh agent told to read only the plugin files its prompt names.
  - Scenario 1, prompt verbatim:
    > You are setting up the workspace's record of options for a repository, following a plugin's text and nothing else. Read only these four files, in the directory <main checkout>\plugins\coding-agent-orchestration-harness\skills, and follow them: subagent-strategy/references/model-routing.md; subagent-strategy/references/model-tendencies-seed.md; rulebook/references/bootstrap-lifecycle.md (the section "Models Record" only); rulebook/references/rule-suite-templates.md (the section "Models And Peers In This Workspace" only). Open no other file, edit nothing, run no command, and dispatch nothing: where the text would have you research, use the facts below as what the research returned.
    >
    > The made-up workspace. Everything here is invented; use the names as given.
    > - The runtime's subagent mechanism can dispatch on two models of one provider, Northwind. The session's own model is Alder.
    >   - Alder can be run at reasoning effort low, medium or high, chosen per dispatch.
    >   - Birch has no reasoning-effort setting.
    > - There are no peer seats.
    > - Northwind's own published statements, read today: Alder at high scores 62 on its capability index and costs 3.00 units per task; Alder at medium scores 61 and costs 2.90 units per task; Alder at low scores 54 and costs 1.00 unit per task; Birch scores 47 and costs 1.00 unit per task. On Northwind's writing and design evaluation the order is the same: Alder high, Alder medium, Alder low, Birch. On its coding-to-spec evaluation the order is also the same.
    > - The workspace has observed nothing of the Northwind family.
    > - The owner, asked at the hold, said: "Pay-as-you-go, 150 units a month. No allowance beyond that." He confirmed the record as you show it.
    > - The Worker role's writing work runs about 100 tasks a month in this workspace. The Orchestrator's session is long and takes about the usage of 40 tasks a month. The Auditor runs about 5 tasks a month.
    >
    > Your output: the filled "Models And Peers In This Workspace" section, in the form the template gives, as plain text. After it, in at most eight lines, say which options you recorded and why those and not others, and for the Worker's design and writing work which option it resolved to and how the cost decided. Do not ask anything.
  - Scenario 1, outcome: the record lists four options, the made-up stronger model at reasoning effort high, medium and low, and the second model, each with its score and cost; the setting whose effort the session itself runs at is recorded as not known. The Worker's design and writing work resolves to the stronger model at low, third in the fit ranking, the cost deciding by share of the stated budget (high 200 percent and medium 193 percent rejected, low 67 percent accepted); the Auditor and the Researcher, with no cost ceiling, resolve to the stronger model at high. Every resolution line carries "where unavailable: none named". The scenario is shown.
  - Scenario 3, prompt verbatim:
    > You are an Orchestrator about to dispatch one Worker task, following a plugin's text and nothing else. Read only this file and follow it: <main checkout>\plugins\coding-agent-orchestration-harness\skills\subagent-strategy\references\model-routing.md. Open no other file, edit nothing, run no command, and dispatch nothing.
    >
    > The made-up workspace's record of options. Everything here is invented; use the names as given.
    > - Options (all subagents of one provider, Northwind, a family the workspace has observed nothing of): Alder at reasoning effort high; Alder at reasoning effort low; Cedar at reasoning effort high; Birch (no reasoning-effort setting).
    > - Capability findings for design and human-readable writing, from Northwind's own statements, dated today: Alder at high is the most capable; then Alder at low; then Cedar at high; then Birch.
    > - Runs on: pay-as-you-go, 150 units a month, as the owner stated. Budget allowance: none stated.
    > - Cost per task: Alder at high 3.00 units; Alder at low 1.00 unit; Cedar at high 2.50 units; Birch 1.00 unit. The Worker's writing work runs about 100 tasks a month.
    >
    > The task due now: a Worker task of human-readable writing (a README section).
    >
    > Case A. The record's Worker line for design and writing reads: "Alder at reasoning effort low; where unavailable: Birch; rests on Northwind's statements of today." When the dispatch is due, Alder at reasoning effort low cannot be run (the runtime reports that setting unavailable).
    >
    > Case B. The same record, except that the Worker line reads: "Alder at reasoning effort low; where unavailable: none named; rests on Northwind's statements of today." Again Alder at reasoning effort low cannot be run when the dispatch is due.
    >
    > For each case, say which option the task goes to and give the reason in the terms of the text you read, naming every option you passed over and why. Then write, for each case, the one or two sentences you would put in your report about which option ran the task and why. Do not ask anything.
  - Scenario 3, first run (text at 8feb768): Case A goes to the option the resolution names, with no walk; Case B goes to the next option the cost setting accepts, passing over the higher-ranked option whose cost the setting rejects; each report says which option ran the task and why. The agent noted that "the next option in the fit ranking" did not say whether an option ranked above the unavailable one counts. That is a finding against Task_1; the rule now says the role goes down the ranking from the unavailable option and never up.
  - Scenario 3, second run (text after that change and OPT-W1-F1): the same destinations and reports in both cases; the agent cites "It never goes up the ranking" for the option above, and says the one-option line does not apply to a role left with one option. Both branches are shown.
  - Scenario 2, by reading: `model-routing.md` (The record of options) has a dispatch on a resolution run at the setting the resolution names wherever the runtime lets the dispatch choose. In this repository's record the Auditor's resolution names Fable 5.2 at high reasoning effort and the Worker's design, writing and interface resolution names Fable 5.2 at low reasoning effort, with Opus 5.5 at high reasoning effort for the unavailable case. This run's own dispatches were made that way (the audits at high, the Workers and fixtures at low). Per D1 the three Codex seat resolutions name no setting and are not part of this reading.
  - This repository's record read against the new form: no resolution changes. The line on what the workspace has gains one sentence: a Claude subagent's reasoning effort is chosen at each dispatch and each resolution names it, and the Codex seats' reasoning effort was fixed by whoever set them up and is not known to this record. "Not known" is what the changed text has setup write for a setting it cannot read (D2); it states nothing about the seats that the record did not already leave unsaid. The resolution lines keep their own wording and gain no where-unavailable clause where they name none; the clause is optional and a record without it stays in force.
  - A finding from scenario 1, recorded in the readings file: the fixture kept reasoning effort medium as an option of its own beside high, two settings that differ by one index point and a thirtieth of the cost and that no role resolved to.
- 2026-11-10T19:12Z Wave 1 re-review, pinned at db76bbc: APPROVED; OPT-W1-F1 closed, the downward walk confirmed as the unnamed-fallback branch only, no new finding. The review of wave 1 is closed.
- 2026-11-10T19:12Z Task_4, the Orchestrator's own: `main` states 1.3.0, so the version is 1.4.0 in the five files that state it (`.claude-plugin/marketplace.json`, `.github/plugin/marketplace.json`, and the plugin's `.claude-plugin/plugin.json`, `.codex-plugin/plugin.json`, `.github/plugin/plugin.json`); a search outside `docs/` finds 1.4.0 seven times in those five files and 1.3.0 nowhere; `validate_harness_package.py` and `run_validation_smoke_tests.py` pass. The final review covers Task_3's line in this repository's record and the version.
- 2026-11-10T19:17Z Final review, pinned at 54bd932: APPROVED, no new finding. It confirms this repository's record changed in one sentence with every resolution unchanged, the fixtures' logged routes and reasons for scenario 1 and both branches of scenario 3, the reading for scenario 2 within D1's limit, the version, and that no decision record is needed. It notes the limit of the fixture evidence: a named affordable fallback different from the next affordable option in the ranking was not exercised.
- 2026-11-10T19:17Z The reading for the closeout audit written in the readings file, before the dispatch. At this close the branch is published and a pull request opened under the standing approval; nothing is merged.
- 2026-11-10T19:18Z A second message from the review seat on the same final review, sent seconds after the approval and pinned at the same revision: CHANGES_REQUESTED, two minor findings. Both are sound, so the Orchestrator takes the review as open; the closeout audit dispatched on the approval at 19:17Z was stopped before it returned and nothing of it is used.
  - OPT-FINAL-F1 (minor): the sentence added to this repository's record said the three Codex seats' reasoning effort "was fixed by whoever set them up", a fact about those seats the record does not hold. Ruling: accepted. The clause is removed; the sentence says only that their reasoning effort is not known to this record.
  - OPT-FINAL-F2 (minor): in the scenario 3 fixture the named option of Case A and the walk's destination of Case B were the same option, so a dispatcher that ignored the named option would have passed both. Ruling: accepted. The record gains a fifth made-up option, ranked last and affordable, and Case A names it; rerun below.
  - Scenario 3, third run, prompt verbatim:
    > You are an Orchestrator about to dispatch one Worker task, following a plugin's text and nothing else. Read only this file and follow it: <main checkout>\plugins\coding-agent-orchestration-harness\skills\subagent-strategy\references\model-routing.md. Open no other file, edit nothing, run no command, and dispatch nothing.
    >
    > The made-up workspace's record of options. Everything here is invented; use the names as given.
    > - Options (all subagents of one provider, Northwind, a family the workspace has observed nothing of): Alder at reasoning effort high; Alder at reasoning effort low; Cedar at reasoning effort high; Birch (no reasoning-effort setting); Dogwood (no reasoning-effort setting).
    > - Capability findings for design and human-readable writing, from Northwind's own statements, dated today: Alder at high is the most capable; then Alder at low; then Cedar at high; then Birch; then Dogwood.
    > - Runs on: pay-as-you-go, 150 units a month, as the owner stated. Budget allowance: none stated.
    > - Cost per task: Alder at high 3.00 units; Alder at low 1.00 unit; Cedar at high 2.50 units; Birch 1.00 unit; Dogwood 0.80 units. The Worker's writing work runs about 100 tasks a month.
    >
    > The task due now: a Worker task of human-readable writing (a README section).
    >
    > Case A. The record's Worker line for design and writing reads: "Alder at reasoning effort low; where unavailable: Dogwood; rests on Northwind's statements of today." When the dispatch is due, Alder at reasoning effort low cannot be run (the runtime reports that setting unavailable).
    >
    > Case B. The same record, except that the Worker line reads: "Alder at reasoning effort low; where unavailable: none named; rests on Northwind's statements of today." Again Alder at reasoning effort low cannot be run when the dispatch is due.
    >
    > For each case, say which option the task goes to and give the reason in the terms of the text you read, naming every option you passed over and why. Then write, for each case, the one or two sentences you would put in your report about which option ran the task and why. Do not ask anything.
  - Scenario 3, third run, outcome: Case A goes to the option the resolution names, the last in the ranking, with no walk, though two options rank above it; Case B goes down the ranking from the unavailable option, passes over the next one because its cost takes more than the whole budget, and takes the first one the cost setting accepts, not reaching the named option of Case A. The two destinations differ, and each report says which option ran the task and why. Both branches are shown, and a dispatcher that ignored the named option would not have passed Case A.
- 2026-11-10T19:20Z Re-review of the final review, pinned at 627473c: APPROVED; OPT-FINAL-F1 and OPT-FINAL-F2 closed, no new finding. The seat states that its CHANGES_REQUESTED of 19:17Z supersedes its APPROVED of 19:16Z for the earlier revision. The review is closed. The reading written before the stopped audit stands for this dispatch: its line on this repository's record already says only that the Codex seats' reasoning effort is not known to the record.
- 2026-11-10T19:20Z Value audit dispatched (Claude subagent `harness-auditor` on Fable, a new dispatch), text verbatim:
  You are the value auditor. Read references/value-audit-mandate.md of the orchestration-harness skill and follow it exactly. Position: closeout. Plan: <main checkout>/docs/coding-agent/plans/active/options-by-model-and-setting-plan.md. Governing brief: <main checkout>/docs/coding-agent/briefs/active/options-by-model-and-setting-brief.md. Changes since: 39af158.
- 2026-11-10T19:27Z Verdict as returned (machine paths shortened; the two comparison lines are in the readings file):
  Value audit verdict, closeout. No item is `ask-now` and none is `ungraded`. All grades were fixed before the readings file was opened.
  Three things outside the grades need the Orchestrator's attention; details are in the notes at the end:
  - **Scenario 2 is `not yet`.** No run has opened after the change, and the one dispatch I can see from inside (this audit) does not confirm the Auditor's recorded setting.
  - **The scenario 1 finding bears on the design**, though the readings file reads it as trivial.
  - **The added sentence in `common.md` sits inside the owner's confirmed record** and has not been confirmed by him.
  Procedure, disclosed:
  - **First Step deviation:** I opened the plan and the brief in the same step in which I located the mandate, so before I had read the mandate. Both are inputs.
  - **Notes and readings:** no notes file was opened at any point. The readings file was opened once, after the grades were fixed.
  - **Git commands:** every command that printed content over the range named one path and carried both exclude pathspecs.
  - **Dispatch:** it carried nothing beyond the fixed template.
  - **Checks I ran myself:** `validate_harness_package.py` printed "Harness package validation passed."; `run_validation_smoke_tests.py` exited 0; `git diff --check` over the range was clean.
  Paths written down as not to be opened before grading:
  - The five `docs/coding-agent/briefs/completed/*-notes.md` files.
  - All thirteen `docs/coding-agent/plans/**/*-readings.md` files, among them `docs/coding-agent/plans/active/options-by-model-and-setting-readings.md`.
  - Untracked `.claude/pr67body.tmp` and `.claude/settings.local.json` were not opened. They are dated Sep 15 and Oct 27, before the range, and are not the run's changes.
  ## Verdict record
  Position: closeout
  Documents read:
  - Instructions: `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/value-audit-mandate.md` and `.../skills/value-documents/SKILL.md`.
  - Inputs:
    - `docs/coding-agent/briefs/active/options-by-model-and-setting-brief.md`
    - `docs/coding-agent/plans/active/options-by-model-and-setting-plan.md`
    - `docs/coding-agent/plans/active/options-by-model-and-setting-run.md` (Scenarios section, for prior states)
    - `docs/coding-agent/rules/common.md` (pointer lines and Standing Approvals at HEAD c17c4c1)
    - the range 39af158 to the working tree, one path at a time, for the seventeen changed files other than the readings file. The tree is clean apart from untracked `.claude/`.
  - Read to understand what the change does, never as support: `.../subagent-strategy/references/model-routing.md` in full; ADR-D-0068, ADR-D-0069 and ADR-D-0070 under `docs/coding-agent-orchestration-harness/decisions/`.
  - After grading: `docs/coding-agent/plans/active/options-by-model-and-setting-readings.md`. The plan's Context section does not name it; the run record does.
  Product basis: brief in the product owner's words. The brief says "the product owner's own words in this brief once ratified. ebigunso owns the harness; no product philosophy and no engineering philosophy exist for this repository", and carries its ratification record ("I ratify it.", 2026-11-11).
  Not audited: the engineering side. `common.md` reads "Engineering philosophy: none yet", so there is no document. The product philosophy line also reads "none yet"; the product side is graded on the brief.
  Missing inputs: none
  Value documents changed in range: none. The brief is not in the range; no pointer line was removed or changed.
  Statements of the brief, quoted once and referred to by letter in the item lines:
  - [A] "An option is a way to run a role: a seat or a subagent, on a model, at a setting. Two settings of one model that differ for some role's work, or in cost, are two options in the workspace's record."
  - [B] "The plugin's text names reasoning effort as the setting it means." and "The same statements hold of any other setting a runtime offers that changes what a model can do or what it costs; the text says so without naming one."
  - [C] "Everything the plugin already says of options holds of options so understood: the capability finding is made for the option, its cost is judged for the option, the fit ranking orders options, and the cost-bounded walk goes down that ranking."
  - [D] "A resolution names its option's setting, and a dispatch on that resolution runs at it wherever the runtime lets the dispatch choose. Where the runtime gives no such choice, or a seat's setting was fixed by whoever set it up, the record states the setting the option runs at, and what the plugin says of best effort applies."
  - [E] (a means) "Setup records the settings worth telling apart, not every setting a model offers, and shows them for confirmation with the rest of the record."
  - [F] "Where the option a role resolves to is unavailable when a dispatch is due, the role goes to what its resolution names for that case; where the resolution names nothing, to the next option in the fit ranking for that work that the role's cost setting accepts. The dispatcher says which option it used and why."
  - [G] "No model name, family alias, provider, seat or price enters the plugin's rules; the seed names providers only, as observations with dates." and "Reasoning effort is named as a kind of setting; no level of it is named".
  - [H] "His words are not carried into the plugin's text as quotations, and are not read to the letter."
  - [I] "The reasons by role do not change, and no resolution in this repository's record changes; that record has named settings since 2026-11-11."
  - [J] "The decision records ADR-D-0068, ADR-D-0069 and ADR-D-0070, accepted 2026-11-11, are not contradicted by this. If the run finds that a decision record is needed or that an accepted one must be reworded, that record returns to him for acceptance by name."
  - [K] "Someone who sets up the harness in a repository, or refreshes its record when a model changes, gets a record that tells apart the settings a model can run at wherever they differ in what the model can do for a role's work or in what it costs."
  - [L] "Agent-checkable: the package validators pass; the plugin's rules name no model and no level of reasoning effort; the text that defines the record of options, and the text setup follows to fill it, speak of an option's reasoning effort as well as its model."
  - [SA] `common.md`, Standing Approvals: "A finished, reviewed run may publish its branch and open pull requests in this repository without asking first. Merges are not covered and wait for the owner. ... Given and accepted by the repository's owner, ebigunso, on 2026-09-30, relayed by Counsel: \"The common rule proposed, accepted.\"" The entry is committed at HEAD, unchanged in the range, and records giver, acceptance and date. Whether the quoted words were said is not something the file can show.
  Items, the plan:
  - DoD 1, the routing reference defines an option and a setting, names reasoning effort, names no other setting, and everything said of options reads of options so understood | maps to the brief | cited | brief [A], [B], [C] | -
  - DoD 2, the unavailable-option rule for every role, the dispatcher says which option and why, the research step for no fitting option stays true | maps to the brief | cited | brief [F], [J] | -
  - DoD 3, setup records reasoning effort with the model, the settings worth telling apart, finding and cost per option, the setting in each resolution, and a fixed or unchoosable setting | maps to the brief | cited | brief [A], [C], [D], and the means [E], which the plan follows | -
  - DoD 4, every other plugin text that tells a dispatcher which option a role runs on speaks of the setting or points to the reference | maps to the brief | cited | brief [C], [D] | -
  - DoD 5, no plugin rule names a model, alias, provider, seat, price or level of reasoning effort; the seed names providers only; the owner's words are not quoted | maps to the brief | cited | brief [G], [H]. My own search of the plugin finds "reasoning effort" in five files and no level of it; the seed is unchanged in the range. | -
  - DoD 6, reasons by role unchanged and no resolution in this repository's record changes; a line of the record's form is Task_3's to find | maps to the brief | inferred | covered for the first sentence by [I]; the diff leaves Reasons by role and every resolution line untouched. A change of form to the record is covered by no statement; it extends [A] and [K]. Cheap to undo. See the changes item on `common.md`. | -
  - DoD 7, ADR-D-0068 to ADR-D-0070 not contradicted; a decision record proposed only if the admission test passes, then waits for the owner by name | maps to the brief | cited | brief [J]. No decision record is in the range. | -
  - DoD 8, scenarios 1 and 3 shown on a fixture, scenario 2 by reading; the human-only condition stays pending and the closeout says so | maps to the brief | inferred | how a scenario is shown is covered by no statement; it extends the brief's Core scenarios. Keeping the human-only condition pending is covered by the brief's Pass conditions. No proxy settles it. Cheap to undo. Which state each scenario earns is on the Scenarios line, and scenario 2 does not earn `demonstrated`. | -
  - DoD 9, the version is the next minor over `main` in every file that states it | maps to the brief (a version is observable to whoever installs the plugin) | inferred | no statement covers it; it extends [K]. Cheap to undo; the change publishes nothing by itself. | -
  - DoD 10, validators and smoke tests pass, Reviewer `APPROVED`, value audits logged, run reported ready with the branch published and a pull request opened, note to Counsel, nothing merged | maps to the brief | cited | brief [L] for the validators, which I ran. Publishing the branch and opening the pull request are outward-facing and pass step 1 on [SA]. At the time of this audit the branch has no upstream and no pull request exists for it, so nothing outward-facing has happened yet. The review verdicts are the plan's account; I cannot see the review seat's messages. The note to Counsel I did not treat as outward-facing: it goes to the owner's own Counsel session, as the final report goes to the owner. | -
  - Planner-added 1, the other dispatch texts speak of the setting or point to the reference | maps to the brief | cited | as DoD 4 | -
  - Planner-added 2, the version is the next minor over `main` when made, last | maps to the brief | inferred | as DoD 9 | -
  - Planner-added 3, scenarios 1 and 3 shown on a fixture | maps to the brief | inferred | extends Core scenarios 1 and 3; adds a check, loosens none. Cheap to undo. | -
  - Planner-added 4, the three added at integration (D2, D3, D5) | maps to the brief | inferred | each graded under its Decision Log entry below | -
  - Non-goal 1, the reasons by role | maps to the brief | cited | brief [I] | -
  - Non-goal 2, any resolution in this repository's record | maps to the brief | cited | brief [I] | -
  - Non-goal 3, the seed's entries | maps to the brief | cited | brief [G] | -
  - Non-goal 4, recording every setting of every model | maps to the brief | cited | brief, Left out on purpose: "Recording every setting of every model at setup." See note 2 on what the built text does here. | -
  - Non-goal 5, how a runtime adapter passes a setting to a dispatch | maps to the brief | inferred | no statement covers leaving the adapters alone; it extends [D]. Cheap to undo. | -
  - Assumption 1, "reasoning effort" may be named as a kind of setting, no level of it | maps to the brief | cited | brief [G] | -
  - Assumption 2, validators hold no assertion on the sentences this changes | internal mechanics | not audited | no engineering philosophy; not irreversible or outward-facing | -
  - Task_1, the option, the setting and the unavailable option | maps to the brief | cited | brief [A], [B], [C], [D], [F], [G], [J] | -
  - Task_2, setup records the settings worth telling apart | maps to the brief | inferred | covered by [A], [C], [D], [G] for its first, second and fourth bullets. The third, a record naming no setting stays valid until a refresh, is covered by no statement; it extends [K]. Cheap to undo. | -
  - Task_3, this repository's record and the scenarios | maps to the brief | inferred | as DoD 6 and DoD 8 | -
  - Task_4, version | maps to the brief | inferred | as DoD 9 | -
  - Decision Log, plan review, OPT-P1 and OPT-P2 (the wave note; the version task's two bullets) | internal mechanics | not audited | no engineering philosophy | -
  - Decision Log, plan review, OPT-P3 (the Design holds the option's identity fixed) | maps to the brief | cited | brief [A] and "It states what and why. How is the Orchestrator's, except where a means is stated" | -
  - Decision Log, plan review, OPT-P4 (the scenario 3 fixture shows both branches) | maps to the brief | inferred | extends Core scenario 3 and [F]; adds a check. Cheap to undo. | -
  - Decision Log D1, three seat resolutions name no setting; the reading for scenario 2 covers those that name one; stating a seat's setting goes to Counsel as a question and nothing is filled in | maps to the brief | cited | brief [I], "no resolution in this repository's record changes". Taking the question to the owner tightens who decides. See note 4. | -
  - Decision Log D2, a setting setup cannot read is recorded as not known, never inferred | maps to the brief | inferred | no statement covers a setting that cannot be read; it extends [D]. Cheap to undo. The record is shown at the hold, where the owner can state it. | -
  - Decision Log D3, the record's form gives each resolution a place for the option it names for the unavailable case, written only where the owner states it or the reason gives it | maps to the brief | cited | brief [F], "the role goes to what its resolution names for that case", which needs a place in the form. That setup never invents one is not in the brief; it extends [F] and tightens who decides. | -
  - Decision Log D4, owns widened to three more copies of the "(a subagent or a peer, on which model)" phrase | maps to the brief | cited | brief [C], [D]. The diff adds "at which setting" to each and nothing else; a search finds no fourth copy without it. | -
  - Decision Log D5, an unavailable option still fits the work and is used again once it can be run | maps to the brief | inferred | no statement says it; it extends [F] ("unavailable when a dispatch is due") and keeps [J]'s case apart. Cheap to undo. See note 5. | -
  Items, the changes in the range:
  - `model-routing.md`, the definition of an option and a setting, reasoning effort named, other settings unnamed; the finding, the tendencies' tie, the fit ranking and research step 2 read of the option | maps to the brief | cited | brief [A], [B], [C] | -
  - `model-routing.md`, a resolution names its setting, a dispatch runs at it where the runtime lets it choose, otherwise the record states it and best effort applies | maps to the brief | cited | brief [D] | -
  - `model-routing.md`, the unavailable-option rule for every role, the named option first, else the first option below that the cost setting accepts, the dispatcher saying which and why | maps to the brief | cited | brief [F] | -
  - `model-routing.md`, "more than one model" and "only one model" become "option" | maps to the brief | cited | brief [A], [C] | -
  - `bootstrap-lifecycle.md`, `rule-suite-templates.md`, `rules-files.md`: options read with their settings, differing settings as options of their own, finding and cost per option, the setting named in each resolution, a fixed or unchoosable setting stated | maps to the brief | cited | brief [A], [C], [D], [L]. Departure from the means [E] in effect, graded on the gives-statement [A] it serves: the text collapses only settings that differ in neither work nor cost, so any two settings whose cost differs are recorded. See note 2. | -
  - The record's form (a persisted format) gains the setting on the options line and on each resolution line, and a "where unavailable" clause; an older record stays in force | maps to the brief | inferred | the setting in the form is covered by [A], [D]; the clause by [F]; keeping older records in force until a refresh is covered by no statement and extends [K]. Cheap to undo. | -
  - `subagent-strategy/SKILL.md`, `counsel/SKILL.md`, `orchestration-harness/SKILL.md`, `agents/Orchestrator.md`, `claude/agents/harness-orchestrator.md` speak of the setting where they spoke of the model | maps to the brief | cited | brief [C], [D] | -
  - `docs/coding-agent/rules/common.md`, one sentence added to the line on what the workspace has: a Claude subagent's reasoning effort is chosen at each dispatch and each resolution names it; the three Codex seats' reasoning effort is not known to the record | maps to the brief | inferred | no statement covers a change to this record outside its resolutions; it extends [A] and [K]. No resolution line changed, which [I] requires. Cheap to undo. See note 3. | -
  - The version, 1.3.0 to 1.4.0, seven places in five files, no other version stated | maps to the brief | inferred | as DoD 9 | -
  - The plan, the run record and the readings file added under `docs/coding-agent/plans/active/` | internal mechanics | not audited | no engineering philosophy; nobody using the plugin observes them | -
  Items, the judgement calls and rulings:
  - Task_1: kept the Orchestrator's reason line as it is | maps to the brief | cited | brief [I], "The reasons by role do not change" | -
  - Task_1: says nothing of a fit ranking with no further acceptable option; the Orchestrator's ruling under OPT-W1-F1 that no destination is invented | maps to the brief | inferred | no statement covers the empty case; saying nothing extends [F] by adding nothing to it. Cheap to undo. See note 5. | -
  - Task_1: no decision record proposed; ADR-D-0068 to ADR-D-0070 not contradicted and unchanged | maps to the brief | cited | brief [J], which leaves the finding to the run. I read the three records: no decision bullet or invariant is contradicted. See note 6. | -
  - Task_2: findings made per setting first, then settings that differ in neither work nor cost collapsed | maps to the brief | cited | brief [A], [C]; the means [E] as noted on the changes line above | -
  - Task_2: a freshly filled resolution line always carries the where-unavailable clause, as "none named" where none is | maps to the brief | inferred | no statement covers it; extends [F]. Cheap to undo. | -
  - Orchestrator: the plan authorized by the brief route on a closed plan review and a plan-draft audit that holds nothing; no one asked | maps to the brief | cited | the brief's ratification record: "I ratify it." The logged plan-draft verdict shows no `ask-now` and no `ungraded` item. The review's approval is the plan's account. | -
  - Orchestrator: OPT-W1-F1, the one-option line speaks of a record with one option, never of a role left with one, and sets aside no reason or cost setting | maps to the brief | cited | brief [F], "that the role's cost setting accepts"; the old line would have sent a role past its cost setting | -
  - Orchestrator: after scenario 3's first run, a role goes down the ranking from the unavailable option and never up | maps to the brief | inferred | [F] says "the next option in the fit ranking" and does not say the direction outright; it extends [F] and [C], "the cost-bounded walk goes down that ranking". Cheap to undo. | -
  - Orchestrator: OPT-FINAL-F1, the record's sentence no longer says the Codex seats' setting was fixed by whoever set them up | maps to the brief | inferred | as the `common.md` change; the ruling narrows the sentence to what the record holds | -
  - Orchestrator: OPT-FINAL-F2, the scenario 3 fixture gains an option so the named option and the walk's destination differ | maps to the brief | inferred | extends Core scenario 3; tightens the check. Cheap to undo. | -
  - Orchestrator: the scenario 1 finding (a near-identical setting kept as an option of its own) read as trivial and not escalated | maps to the brief | cited | brief [A]; compared under Findings compared | -
  - Orchestrator: a second review message taken as reopening the review; the closeout audit already dispatched was stopped and nothing of it used | internal mechanics | not audited | no engineering philosophy; it tightens a stop | -
  - Orchestrator: research waived on its own reading of the text | internal mechanics | not audited | no engineering philosophy | -
  Human-only conditions pending: "the next time a model arrives with more than one setting, he judges whether the refreshed record found the fitting setting for each role without his naming it."
  Scenarios:
  - **Scenario 1: demonstrated, on a made-up lineup, not in a repository.** To observe it, give a fresh agent the four plugin files and the lineup in the plan's Progress Log (scenario 1 prompt) and read the record it fills. My own walk of the changed text on that lineup gives the same record: three settings of the stronger model and the second model as four options, and the Worker's writing resolved to the stronger model's lowest setting once the two above it are rejected on cost. It does not show setup reading settings from a real runtime or finding per-setting capability by research; that is the human-only condition, still pending.
  - **Scenario 2: not yet.** It asks for a run opened after the change, and none has. What exists is a reading: the text has a dispatch run at the setting its resolution names, and the record names one for the Auditor and for the design-writing Worker. The plan's statement that this run's own dispatches ran at the recorded settings is the Orchestrator's account. See note 1.
  - **Scenario 3: demonstrated, on a made-up record.** To observe it, give a fresh agent `model-routing.md` and the record in the Progress Log (scenario 3, third run). My own walk of the text gives the same: Case A goes to the named option, though it ranks last; Case B goes down from the unavailable option, passes over the one whose cost exceeds the budget, and takes the next. The rule has the dispatcher say which option and why. It does not show a real dispatch where an option was in fact unavailable.
  - **Getting closer: yes.** Every prior state was `not yet`. The text the three scenarios rest on is now in the range, and two of them can be observed by following it. Scenario 2 can only move in a later run.
  ## Notes beside the record (no grade rests on them)
  1. **This audit's own setting.** The only dispatch I can see from inside is this one. My context names the model as Fable 5.2, which matches the Auditor's resolution. It also carries a reasoning-effort value of 30, with no level name. I cannot map that number to the record's "high", so I cannot confirm this audit ran at the Auditor's recorded setting; on a scale where a larger number means more effort, 30 is not the top. The Orchestrator can check what it passed in the dispatch call. Until a run shows its dispatches' settings in a way someone other than the dispatcher can see, scenario 2 has nothing to be observed by.
  2. **Settings worth telling apart.** The brief's gives-statement [A] makes two options of any two settings that "differ ... in cost". Reasoning-effort settings nearly always differ in cost, so the built text will record nearly every setting a model offers. The brief's means [E] and its "Left out on purpose" both speak against that. The text follows the gives-statement to the letter, so the grade is cited. How far apart two settings must be before they are worth a line is something the brief does not say; it is the owner's to state if he wants fewer lines.
  3. **The sentence in this repository's record.** It sits in a section whose status line reads "confirmed by ebigunso". The plugin's own setup text has a confirmed record replaced only on his confirmation. The sentence says nothing the resolutions do not already show, plus that the seats' settings are not known, and it is labelled as added 2026-11-11 with the form. The grade is inferred on that footing. The closeout report should put the sentence in front of him by name, since the pull request is where he first sees it.
  4. **D1's question.** The brief's [D] has the record state the setting a fixed seat runs at, and its [I] says this record "has named settings since 2026-11-11". Three seat resolutions name none, and the record now says so. Nothing in the range shows the question reaching Counsel; the plan says it goes with the note at close. It should not be dropped.
  5. **Cases the unavailable-option rule leaves unstated**, for every role:
     - the named option is itself unavailable;
     - nothing below the unavailable option is accepted by the cost setting;
     - the unavailable option is last in the ranking.
     D5's sentence that an unavailable option "still fits the work" also keeps research step 5 from applying in the third case. No decision bullet of ADR-D-0069 is contradicted, but a Researcher whose only fitting option is unavailable has no stated destination.
  6. **The decision records' definition of an option.** ADR-D-0068, ADR-D-0069 and ADR-D-0070 each still define an option in their Context as "an in-session subagent or a peer seat, each on some model". The plugin now adds "at a setting". No decision, invariant or boundary is contradicted, and the brief leaves the finding to the run. The accepted records and the plugin now word the term differently; the owner may want to hear that in the closeout.
  7. **A date in the brief.** It calls the three records "accepted 2026-11-11"; their own headers carry 2026-10-29. No grade turns on it.
  8. **A slip in the Progress Log.** The wave 1 dispatch entry begins with a literal "%s" where its timestamp should be.
- Acting on the verdict: it holds nothing: no item ask-now or ungraded, no missing inputs, no value document changed, and no item marked direction. The plan closes on it, and the run is reported candidate ready, not ready, for what follows. Scenario 2 is not yet: it asks for a run opened after the change, and the reading the plan gave for it is a reading; the run record says so. The scenario 1 finding is compared as bearing on the design though read as trivial; it is escalated to Counsel as a value question (how far apart two settings must be before setup records them as options of their own), with the built text left as it follows the brief's statement, and its disposition is in the readings file. The audit could not confirm its own setting: its context named the model the record names for the Auditor and carried a reasoning-effort value it could not map to the record's level. The Orchestrator passed high reasoning effort in the dispatch call and cannot see from its side what the runtime applied; this goes to Counsel as a fact, since scenario 2 has nothing to be observed by until a dispatch's setting can be seen by someone other than the dispatcher. Also to Counsel with the report: the sentence added to this repository's confirmed record, put before the owner by name; D1's question on the three seat resolutions that name no setting; the cases the unavailable-option rule leaves unstated (the named option itself unavailable, nothing below accepted, the unavailable option last in the ranking); and that the three accepted records still word an option without a setting, uncontradicted. Inferred items are journaled as extensions and shown to him. Readings that diverge do so in part and as under-claims or over-claims of support on the same items (the one-option line and D3), corrected in the reading; the reading said the branch was published at this close, and it is published after this entry. The Progress Log's wave 1 entry carried a literal placeholder where its time belongs; corrected. The first-step deviation is recorded with the lesson of 2026-11-07.

## Decision Log (append-only; re-plans and major discoveries)
- 2026-11-11 Plan review (Codex seat `agent-harness-reviewer`, pinned at 7f3481f): CHANGES_REQUESTED, four minor findings, all accepted. OPT-P1: the wave line repeated its task IDs in a note, failing the plan validator; the note is a line of its own. OPT-P2: the version task had one acceptance bullet; it has its two checks. OPT-P3: the Design compared the brief's own requirement against not meeting it; it now holds the option's identity fixed and compares how the definition and the unavailable-option rule are carried through the texts. OPT-P4: the fixture for scenario 3 could pass on one branch of the rule; it now shows both, the passing over of a cost-rejected option included. The review's inventory finds no requirement unlisted under Planner-added requirements, and confirms the owns, the compatibility stance and the handling of a decision record.
- 2026-11-11 D1, from the plan-draft audit's first note: three seat resolutions in this repository's record name no setting. Task_3's reading for scenario 2 is of the resolutions that name one, the two the brief's scenario names among them. Stating a seat's setting is new content in the owner's confirmed record and goes to Counsel as a question; nothing is filled in.
- 2026-11-11 D2, planner-added at integration (Task_2's question): a setting setup cannot read is recorded as not known, never inferred. Needed because: the brief has the record state the setting a fixed seat runs at and does not say what happens when setup cannot observe it; without the line setup would guess, or ask a question the step forbids.
- 2026-11-11 D3, planner-added at integration (Task_2's design alert): the record's form gives each resolution line an optional place for the option it names for the case its own is unavailable, written by setup only where the owner states it or the reason gives it. Needed because: the brief's fifth statement sends a role first "to what its resolution names for that case", and a record form with no place for it leaves that branch unusable by any record setup fills.
- 2026-11-11 D4, owns widened at integration (Task_1's question): `agents/Orchestrator.md`, `claude/agents/harness-orchestrator.md` and `skills/orchestration-harness/SKILL.md` carried the phrase "(a subagent or a peer, on which model)"; each gains "at which setting", that phrase only, so the four copies agree. This is the plan's first planner-added requirement applied to copies the plan's owns had missed. No Codex copy carries the phrase.
- 2026-11-11 D5, planner-added at integration (Task_1's call): the reference says an unavailable option still fits the work and is used again once it can be run. Needed because: without it the unavailable case and research step 5 (no recorded option fits) read as one rule stated twice, the risk the plan's Notes name.

## Notes (Risks / Edge cases)
- The research rule's step 5 (no recorded option fits) and the new unavailable-option rule answer different questions; the risk is a reader taking them for one rule stated twice. Task_1's acceptance asks that they not contradict, and the review checks that they are told apart.
- ADR-D-0068 defines an option without a setting. The definition is not contradicted by adding what a model runs at, but whether its wording must follow is the kind of change that returns to the owner; Task_1 reports, and nothing in an accepted record is changed by this plan.
