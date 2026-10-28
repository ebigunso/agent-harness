# Plan: Model defaults by reason

- status: draft
- generated: 2026-10-28
- last_updated: 2026-10-28
- work_type: docs

## Goal
- The harness gives what the governing brief `docs/coding-agent/briefs/active/model-defaults-by-reason-brief.md` states: each role's model is chosen by a stated reason that resolves against whatever lineup the workspace has, a dated seed of observed tendencies fills the gap until the workspace observes its own, setup fills the record and shows it for confirmation, and this repository's record takes the reason form with the owner's current resolutions.
- The brief is the requirement and is not restated here; where this plan and the brief differ, the brief governs and the difference is a plan defect.
- This is the first plan of the run recorded in `docs/coding-agent/plans/active/model-defaults-by-reason-run.md`.

## Definition of Done
- `skills/subagent-strategy/references/model-routing.md` states, once, the reason for each role (Orchestrator, Auditor, Researcher, Worker, Reviewer) in the brief's three parts: the kind of capability, the split by work type where the owner's reasons split, and the cost setting; each written in the plugin's own words as the tendency preferred for that kind of work, the tendency detrimental to it, and why each is so; no quotation of the owner; no total ordering (brief, "What the plugin states", items 1 to 3). It replaces the strength keys ("Strengths routed on", "Routing by work type"); "Choosing where research goes" (ADR-D-0061) keeps its rule and resolves the Researcher by the new reason.
- The plugin ships a seed observation in a reference of its own, dated and at the provider level, for the Claude and GPT families only, written as tendencies and never as what a family can or cannot do; a workspace's own dated observation replaces it for that family; the seed carries the observation and its date and no sources (brief, items 4 and Limits).
- Setup (`skills/rulebook`) resolves the reasons against the lineup the runtime offers, fills the workspace record in `common.md` with the date, and holds it for the owner's confirmation before anything is dispatched on it; the record's form is in the rule-suite templates; the budget allowance is the owner's, stated in the record, and the plugin states no price and no cheap-or-expensive line (brief, items 5 and 6).
- Every other plugin text that uses the old strength names (`model-routing.md` Prose quality and Tiers and fallback; `durable-docs-authoring/references/adr.md`:54) reads in the new reasons; no plugin rule names a model, family alias, provider, seat or price (`runtime-adapter-contract/references/prompt-budgeting.md`:5 "GPT-Oriented" heading included); the seed names providers only, as dated observations.
- This repository's `common.md` "Models And Peers In This Workspace" holds the record in the reason form with the owner's resolutions of 2026-10-28 and the FrontierCode 2.0 citation for the Orchestrator's reason (brief, "This repository, as the first application"); the Orchestrator-on-Opus trial closes into it. These rule-file changes are this repository's and do not ship.
- Scenarios 1, 3 and 5 are shown on a fixture, outcomes in the Progress Log; scenarios 2 and 4 are shown by reading where a fixture adds nothing; the human-only pass condition stays pending and the closeout says so.
- The plugin's version is the next minor version over the base branch at the time it is made, in every file that states it, made as the last change before the run is reported ready.
- Package validators and smoke tests pass; the branch has Reviewer `APPROVED`; value audits at plan draft and closeout are logged; the plan closes and the run is reported ready: branch published, pull request opened under the standing approval, note to Counsel, nothing merged.

## Planner-added requirements
- The fixtures and probe outputs live in the Orchestrator's scratchpad, not in the repository. Needed because: they are one-off measurements of how a fresh agent reads the text, not checks a validator runs again (`common.md`, validation commands).
- The seed is a reference file of its own, not a section of `model-routing.md`. Needed because: the brief keeps the routing rules free of provider names while the seed names providers as dated observations; a file boundary is where a search and a reader can see that line without excluding a section (Design).
- The version is the next minor over the base branch when made, last. Needed because: an installed plugin is refreshed only when its version changes; another run (a quiet Orchestrator session under a brief) also changes the version, so the number is fixed when this change is made; last, so a later fix does not ship under a version already published.

## Scope / Non-goals
- Scope: `skills/subagent-strategy/references/model-routing.md` and a new seed reference beside it; `skills/subagent-strategy/SKILL.md` where it routes to them; `skills/rulebook/SKILL.md`, `references/bootstrap-lifecycle.md`, `references/rule-suite-templates.md`, `references/rules-files.md` (setup's record step and the record's form); `skills/durable-docs-authoring/references/adr.md`:54; `skills/runtime-adapter-contract/references/prompt-budgeting.md`:5; `skills/counsel/SKILL.md` where it reads the record or chooses a family to consult; this repository's `docs/coding-agent/rules/common.md`; the version files; a decision record if the admission test passes.
- Non-goals: adapters' `model: inherit` and the Codex templates, which stay without a model value (the choice is made at dispatch from the record, R1 B); runtime and physical identities and named external skills (R1 A, parts 2 and 3), which identify a platform or tool and choose no model; the research test run's two observations (brief, Left out); porting the owner's stance beyond the seed (brief, Left out).

## Design
- Chosen: the five reasons replace the strength keys inside `model-routing.md`, where routing is decided and both sessions already read; the seed lives in a reference of its own beside it (`skills/subagent-strategy/references/model-tendencies-seed.md` or a name the Worker picks), so the routing rules name no provider while the seed names providers as dated observations; setup gains one step in `bootstrap-lifecycle.md` that resolves the reasons against the lineup and the seed, writes the record into `common.md` from a template section, and holds it with the hold-and-confirm the philosophy step uses.
  - structure: one owner for the reasons, one for the seed, one for the record; the record depends on both, the rules on neither's content. evolution: a new model or family changes the workspace record or adds a seed entry, never a rule (brief, scenario 2); deletion path: the seed file. verification: a search for model, provider and price names in the rules; fixture probes. operation: none at runtime beyond reading one more reference at setup. human: a reader finds why a role goes where it goes in one place. safety: nothing dispatched on an unconfirmed record.
- Alternative: the seed written inside `model-routing.md` under a dated heading.
  - structure: one file, but the routing rules and a provider-naming observation share it. evolution: a seed update edits the rules file. verification: the no-provider search must exclude a section. operation: none. human: one file to read. safety: the same.
- Why chosen: the brief separates the two ("No model name ... in the plugin's rules; the seed names providers only, as observations with dates"); a file boundary keeps that line where a search and a reader can see it.
- Ruling R1 (budget at setup): setup fills every line it can resolve and leaves the budget allowance as the owner's to state when he confirms the record; the record is not dispatched on until confirmed, so no dispatch is made on an allowance he has not stated. Research's "cost notwithstanding" is the owner's standing setting in this repository only; the plugin states no default allowance.
- Ruling R2 (the Orchestrator's reason): the Orchestrator's model is the session's, not dispatched; its reason is stated so setup can record which option fits it and the owner can open the session on it.

## Compatibility stance
- surface: the routing vocabulary other texts use (`writing-strength`, `detail-strength`, `long-context`) and the workspace record's form in `common.md`.
- stance: migrate
- justification: the consumers are locatable: `adr.md`:54 and `model-routing.md`'s own later sections (R1 B; the search above); this repository's record, rewritten in this run; another workspace's record in the old form is rewritten in the new form when setup is next run there (brief, scenario 2); nothing is promised for it before then.

## Context (workspace)
- Governing brief: `docs/coding-agent/briefs/active/model-defaults-by-reason-brief.md`. Ratification as it reached this session: Counsel's relay of 2026-10-28 (16:17Z), quoting the owner on 2026-10-29: "I ratify both briefs, hand them over now." Relays are admitted by the Standing Approvals entry of 2026-10-01 in `common.md`.
- Run record: `docs/coding-agent/plans/active/model-defaults-by-reason-run.md`. Readings file: `docs/coding-agent/plans/active/model-defaults-by-reason-readings.md`.
- Related files/areas: R1 census of 2026-10-28 by the researcher seat (agmsg history, 16:52Z to 16:58Z), path:line for the statements above.
- Existing patterns or references: the philosophy hold-and-confirm (`bootstrap-lifecycle.md`:58 to :66); the record standard (`model-routing.md`:24); ADR-D-0061.
- Design record consulted and deviations from its acceptance: ADR-D-0061's choice rule item 3 routes research by strength; this plan keeps the rule and changes what it resolves by, which a new record states if the admission test passes.

## Open Questions (max 3)
- None in this session.

## Assumptions
- A1: "no plugin rule names a model, alias, provider, seat or price" covers model choice; runtime and platform identities (Claude, Codex, Copilot adapters and paths) and the named external skill-creator skill identify a tool and stay — source: R1 parts 2, 3 and 7 F2; the brief's constraint concerns the default for a role.
- A2: "the seed names providers only" allows a family name beside its provider (the Claude and GPT families are named in the brief's seed statement) and no model or version — source: brief, "What the plugin states" item 4.

## Tasks

### Task_1: The reasons, the seed and the pointers
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/subagent-strategy/references/model-routing.md
  - plugins/coding-agent-orchestration-harness/skills/subagent-strategy/references/ (one new seed reference)
  - plugins/coding-agent-orchestration-harness/skills/subagent-strategy/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/durable-docs-authoring/references/adr.md
  - plugins/coding-agent-orchestration-harness/skills/runtime-adapter-contract/references/prompt-budgeting.md
  - plugins/coding-agent-orchestration-harness/skills/counsel/SKILL.md
  - docs/coding-agent-orchestration-harness/decisions/ (a new record only)
- depends_on: []
- description: |
  Write the five reasons in model-routing.md in place of the strength keys, the seed in its own reference, and bring the texts that use the old names to the new ones. The brief's "What the plugin states" is the content; wording is the Worker's and is not the owner's quoted.
- acceptance:
  - Each role's reason has the brief's three parts and, for each work type, the preferred tendency, the detrimental tendency and why; the Reviewer's reason chooses by the kind of finding the work wants at its stage and takes a different family only when that kind is its strength; no ordering of models is implied.
  - The seed is dated, at the provider level, Claude and GPT families only, tendencies only, no sources; it says a workspace's own dated observation replaces it for that family and the record is redated when a model changes.
  - "Choosing where research goes" keeps ADR-D-0061's rule and resolves by the Researcher's reason; Prose quality, Tiers and fallback, `adr.md`:54 and `prompt-budgeting.md`:5 read in the new terms; Counsel's text agrees where it reads the record.
  - A search of the plugin's rules for model names, family aliases, providers, seats and prices finds none outside the seed.
  - A decision record is proposed if the admission test in `durable-docs-authoring/references/adr.md` passes, filename at or under 135 characters.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: py scripts/validate_harness_package.py and py scripts/run_validation_smoke_tests.py pass; git diff --check clean on owned paths"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review against the brief's 'What the plugin states', Limits and pass conditions; the name search above"

### Task_2: Setup fills the record and holds it for confirmation
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/rulebook/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/rulebook/references/bootstrap-lifecycle.md
  - plugins/coding-agent-orchestration-harness/skills/rulebook/references/rule-suite-templates.md
  - plugins/coding-agent-orchestration-harness/skills/rulebook/references/rules-files.md
- depends_on: [Task_1]
- description: |
  Add setup's step for the models record: resolve each role's reason against the lineup the runtime offers and the seed, write the record into common.md with the date from a template section, and hold it for the owner's confirmation before anything is dispatched on it, as the philosophy step holds an unsettled pointer (Ruling R1 for the budget line).
- acceptance:
  - Setup writes the record with its date, shows it, and no dispatch goes by it before the owner confirms; the budget allowance is his to state there; re-running setup redates the record.
  - The common.md template carries the record's section; rules-files.md describes it.
  - Nothing names a model, provider or price.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "py scripts/validate_harness_package.py and py scripts/run_validation_smoke_tests.py pass; git diff --check clean"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review against the brief's setup statement and scenario 1"

### Task_3: This repository's record
- type: docs
- owns:
  - docs/coding-agent/rules/common.md
- depends_on: [Task_1]
- description: |
  Rewrite "Models And Peers In This Workspace" in the reason form with the owner's resolutions of 2026-10-28, the FrontierCode 2.0 citation with its date for the Orchestrator's reason, and the lines that stay (seats, liveness, dispatch restriction, the Auditor comparison).
- acceptance:
  - The record holds each role's resolution as the brief's "This repository" states, dated, with the budget setting as the owner stated it; nothing of his words is lost from the lines it replaces.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "The record against the brief's 'This repository, as the first application' and the replaced lines"

### Task_4: Scenarios on a fixture
- type: test
- owns:
  - the Orchestrator's scratchpad (fixtures and probe outputs)
- depends_on: [Task_1, Task_2, Task_3]
- description: |
  Show scenarios 1, 3 and 5 by giving a fresh agent the plugin text at the branch head and a fixture for each, and recording what it does.
- acceptance:
  - 1: a fresh agent running setup in a fixture repository whose runtime offers one provider fills the record from the reasons and the seed, shows it for confirmation, asks nothing about models, and its first dispatch after confirmation goes by the record.
  - 3: given a fixture record, a logic-oriented production coding task and its review, and a design still being worked out and its review, the agent routes each as the scenario states.
  - 5: given this repository's record, the agent routes an Orchestrator, Auditor, Researcher (both work types) and Worker (both work types) dispatch where the owner's words of 2026-10-28 put them.
  - The dispatch texts and outcomes are logged in the Progress Log; scenarios 2 and 4 are shown by reading, and any scenario a fixture cannot make is said so plainly.
- validation:
  - kind: manual
    required: true
    owner: orchestrator
    detail: "Each probe a new session with no context beyond the plugin text and the fixture; each outcome recorded in the Progress Log with the part of the response that shows it"

### Task_5: Version
- type: chore
- owns:
  - plugins/coding-agent-orchestration-harness/.claude-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.codex-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.github/plugin/plugin.json
  - .claude-plugin/marketplace.json
  - .github/plugin/marketplace.json
- depends_on: [Task_1, Task_2, Task_4]
- description: |
  Set the plugin's version to the next minor version over the base branch, everywhere it is stated, as the last change before the run is reported ready.
- acceptance:
  - Every file that states the version agrees on it.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "py scripts/validate_harness_package.py passes"

## Task Waves (explicit parallel dispatch sets)
- Wave 1: Task_1
- Wave 2: Task_2, Task_3
- Wave 3: Task_4
- Wave 4: Task_5

## Rollback / Safety
- Each task's commits are its own; reverting them restores the prior text. Nothing reaches the remote before review, and nothing is merged without the owner's acceptance naming the pull request.

## Progress Log (append-only)
- 2026-10-28 16:41 Research before drafting: R1, a forensic census, dispatched to the Researcher role on the researcher seat `agent-harness-researcher` (detail strength), its own dispatch and report over agmsg; no Worker task carried it. The seat disclosed reading files outside the dispatch's evidence scope (the other run's plan and run record, two rule files beyond the permitted section); none of its findings rests on them; no notes or readings file was opened for this task.
- Run starts from revision: f852cee.
- 2026-10-28 17:03 Plan review dispatched to the reviewer seat with the plan-review snippet, at 4ad1a7f. 17:15 NEEDS_REVISION, one finding: MPR-F1 (minor) two drafting constraints unlisted (the seed in a file of its own; old-form records keep routing until setup is re-run). Triage: fix; the first listed with the Design's reason, the second dropped as unrequested. Validator: pass.

## Decision Log (append-only; re-plans and major discoveries)

## Notes (Risks / Edge cases)
- A fixture shows what a fresh agent does with the text, not what setup does in his next repository; the human-only pass condition covers that.
- Task_3 edits a rule file and is the Orchestrator's own (`common.md`, Repo Safety); it is dispatched to no Worker.
