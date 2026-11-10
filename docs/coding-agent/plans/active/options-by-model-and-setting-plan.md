# Plan: An option is a model at the setting it runs at

- status: draft
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

## Decision Log (append-only; re-plans and major discoveries)
- 2026-11-11 Plan review (Codex seat `agent-harness-reviewer`, pinned at 7f3481f): CHANGES_REQUESTED, four minor findings, all accepted. OPT-P1: the wave line repeated its task IDs in a note, failing the plan validator; the note is a line of its own. OPT-P2: the version task had one acceptance bullet; it has its two checks. OPT-P3: the Design compared the brief's own requirement against not meeting it; it now holds the option's identity fixed and compares how the definition and the unavailable-option rule are carried through the texts. OPT-P4: the fixture for scenario 3 could pass on one branch of the rule; it now shows both, the passing over of a cost-rejected option included. The review's inventory finds no requirement unlisted under Planner-added requirements, and confirms the owns, the compatibility stance and the handling of a decision record.

## Notes (Risks / Edge cases)
- The research rule's step 5 (no recorded option fits) and the new unavailable-option rule answer different questions; the risk is a reader taking them for one rule stated twice. Task_1's acceptance asks that they not contradict, and the review checks that they are told apart.
- ADR-D-0068 defines an option without a setting. The definition is not contradicted by adding what a model runs at, but whether its wording must follow is the kind of change that returns to the owner; Task_1 reports, and nothing in an accepted record is changed by this plan.
