# Plan: An option is a model at the setting it runs at

- status: authorized 2026-11-11 by the brief route (plan review closed, plan-draft audit holds nothing); in execution
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

## Decision Log (append-only; re-plans and major discoveries)
- 2026-11-11 Plan review (Codex seat `agent-harness-reviewer`, pinned at 7f3481f): CHANGES_REQUESTED, four minor findings, all accepted. OPT-P1: the wave line repeated its task IDs in a note, failing the plan validator; the note is a line of its own. OPT-P2: the version task had one acceptance bullet; it has its two checks. OPT-P3: the Design compared the brief's own requirement against not meeting it; it now holds the option's identity fixed and compares how the definition and the unavailable-option rule are carried through the texts. OPT-P4: the fixture for scenario 3 could pass on one branch of the rule; it now shows both, the passing over of a cost-rejected option included. The review's inventory finds no requirement unlisted under Planner-added requirements, and confirms the owns, the compatibility stance and the handling of a decision record.

## Notes (Risks / Edge cases)
- The research rule's step 5 (no recorded option fits) and the new unavailable-option rule answer different questions; the risk is a reader taking them for one rule stated twice. Task_1's acceptance asks that they not contradict, and the review checks that they are told apart.
- ADR-D-0068 defines an option without a setting. The definition is not contradicted by adding what a model runs at, but whether its wording must follow is the kind of change that returns to the owner; Task_1 reports, and nothing in an accepted record is changed by this plan.
