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
- Setup (`skills/rulebook`) resolves the reasons against the lineup the runtime offers, fills the workspace record in `common.md` with the date, and holds it for the owner's confirmation before anything is dispatched on it; the record's form is in the rule-suite templates; the budget allowance is the owner's, stated in the record, and the plugin states no price and no cheap-or-expensive line (brief, items 5 and 6). Setup also records what the environment runs on (a subscription plan or a pay-as-you-go budget) and shows it with the record; when the owner confirms without naming an allowance, a cost-bounded role's option is found by walking down the fit ranking, taking the best-fitting option whose cost is acceptable against that budget, and otherwise the next, judged the same way (brief, "Directed during the run").
- Every other plugin text that uses the old strength names (`model-routing.md` Prose quality and Tiers and fallback; `durable-docs-authoring/references/adr.md`:54) reads in the new reasons; no plugin rule names a model, family alias, provider, seat or price (`runtime-adapter-contract/references/prompt-budgeting.md`:5 "GPT-Oriented" heading included); the seed names providers only, as dated observations.
- This repository's `common.md` "Models And Peers In This Workspace" holds the record in the reason form with the owner's resolutions of 2026-10-28 and the FrontierCode 2.0 citation for the Orchestrator's reason (brief, "This repository, as the first application"); the Orchestrator-on-Opus trial closes into it. These rule-file changes are this repository's and do not ship.
- Scenarios 1, 3 and 5 are shown on a fixture, outcomes in the Progress Log; scenarios 2 and 4 are shown by reading where a fixture adds nothing; the human-only pass condition stays pending and the closeout says so.
- The plugin's version is the next minor version over the base branch at the time it is made, in every file that states it, made as the last change before the run is reported ready.
- Package validators and smoke tests pass; the branch has Reviewer `APPROVED`; value audits at plan draft and closeout are logged; the plan closes and the run is reported ready: branch published, pull request opened under the standing approval, note to Counsel, nothing merged.

## Planner-added requirements
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
- Ruling R1 (budget at setup): setup fills every line it can resolve, records what the environment runs on, and shows the record; the record is not dispatched on until confirmed. When the owner confirms without naming an allowance, the walk down the fit ranking with a cost check against what the environment runs on decides the Worker's option, and the Reviewer's, which the brief puts on the Worker's grounds (brief, "Directed during the run"; item 1, Reviewer). The Researcher's cost setting is the brief's, stated by the plugin: research goes to the stronger option for its work type, cost notwithstanding (brief, item 1); the Auditor has no cost ceiling.
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
  - Each role's reason has the brief's three parts and, for each work type, the preferred tendency, the detrimental tendency and why; the Reviewer's reason chooses by the kind of finding the work wants at its stage and takes a different family only when that kind is its strength; no ordering of models is implied. The Worker's reason states, once, the walk for a record confirmed without an allowance (brief, "Directed during the run"), and the Reviewer's points to it.
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
  Add setup's step for the models record: resolve each role's reason against the lineup the runtime offers and the seed, write the record into common.md with the date from a template section, and hold it for the owner's confirmation before anything is dispatched on it, as the philosophy step holds an unsettled pointer (Ruling R1 for the budget line and the walk).
- acceptance:
  - Setup writes the record with its date and what the environment runs on, shows it, and no dispatch goes by it before the owner confirms; the budget allowance is his to state there; re-running setup redates the record.
  - Setup's step points to the walk for a confirmation without an allowance, which Task_1 states with the Worker's reason; setup does not restate it.
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

- 2026-10-28 17:17 Plan review round 2 at fe28441 (and the log-order commit 12aa28e): APPROVED, MPR-F1 closed, no new findings. The plan review is closed with no finding open.
- 2026-10-28 17:20 Plan-draft value audit dispatched (Claude subagent `harness-auditor` on Fable, a new dispatch), text verbatim (the worktree path shortened):
  You are the value auditor. Read references/value-audit-mandate.md of the orchestration-harness skill and follow it exactly. Position: plan draft. Plan: <worktree>/docs/coding-agent/plans/active/model-defaults-by-reason-plan.md. Governing brief: <worktree>/docs/coding-agent/briefs/active/model-defaults-by-reason-brief.md. Changes since: none.
- 2026-10-28 17:24 Verdict as returned (machine paths shortened; the two comparison lines are in the readings file):
  Position: plan draft
  Documents read: docs/coding-agent/plans/active/model-defaults-by-reason-plan.md; docs/coding-agent/briefs/active/model-defaults-by-reason-brief.md; docs/coding-agent/rules/common.md (pointer lines :12-13, Models And Peers :48-59, Standing Approvals :61-67); plugins/coding-agent-orchestration-harness/skills/value-documents/SKILL.md; for understanding only: skills/subagent-strategy/references/model-routing.md, durable-docs-authoring/references/adr.md:50-57, runtime-adapter-contract/references/prompt-budgeting.md:1-12, counsel/SKILL.md:20, rulebook/references/bootstrap-lifecycle.md (grep). Not opened before grading: docs/coding-agent/briefs/active/model-defaults-by-reason-notes.md (never opened); docs/coding-agent/plans/active/model-defaults-by-reason-readings.md (opened once after the grades were fixed).
  Product basis: brief in the product owner's words (brief line 6: "the product owner's own words in this brief. ebigunso owns the harness"); ratification record present (status line, 2026-10-29, "I ratify both briefs, hand them over now.").
  Not audited: engineering side, no engineering philosophy (common.md:13 "Engineering philosophy: none yet"); product philosophy likewise none (common.md:12), so the product side is graded on the brief alone.
  Missing inputs: none
  Value documents changed in range: none (Changes since: none; no range)
  Items:
  - DoD 1 (five reasons once in model-routing.md, three parts, own words, no quotation, no ordering; strength keys replaced; "Choosing where research goes" keeps its rule, resolves by the Researcher's reason) | maps to the brief | cited | brief "What the plugin states" item 1 "For each role, a reason in three parts" (gives); item 2 "no single best model and no total ordering" (constraint); item 3 "written as reasoning, in the plugin's own words ... neither quoted in the plugin text nor taken literally" (constraint); pass condition "stated once in the plugin at the place where routing is decided" | -
  - DoD 2 (seed in a reference of its own, dated, provider level, Claude and GPT only, tendencies, replaced by a workspace observation, no sources) | maps to the brief | cited | brief item 4 "ships a seed observation, dated and at the provider level ... written as tendencies, never as what a family can or cannot do. A workspace's own dated observation replaces it. The first version covers only the Claude and GPT families" (gives); Limits "the seed carries the observation and its date, not the sources" (constraint) | -
  - DoD 3 (setup resolves, fills the record with the date, holds for confirmation; record form in templates; budget allowance the owner's; no price) | maps to the brief | cited | brief item 5 "Setup resolves the reasons against the lineup the runtime offers, fills the workspace record from them with the date, and shows the result for confirmation before anything is dispatched on it" (gives); item 6 "The budget allowance is the workspace's, stated by its owner in the record; the plugin states no price and no cheap-or-expensive line" (constraint) | -
  - DoD 4 (other plugin texts read in the new reasons; no plugin rule names a model, family alias, provider, seat or price, the "GPT-Oriented" heading included; seed names providers only as dated observations) | maps to the brief | cited | brief Limits "No model name, family alias, provider, seat or price in the plugin's rules; the seed names providers only, as observations with dates" (constraint); pass condition "no plugin rule names a model, alias, provider, seat or price" | -
  - DoD 5 (this repository's common.md record in the reason form with the owner's resolutions of 2026-10-28 and the FrontierCode 2.0 citation; the Opus trial closes into it; does not ship) | maps to the brief | cited | brief "This repository" "The record in `common.md` is rewritten in the reason form, with the current resolutions as the owner's words of 2026-10-28" (gives); "the record cites FrontierCode 2.0 ... with its date" (means); Limits "The rule-file changes are this repository's and do not ship in the plugin" (constraint) | -
  - DoD 6 (scenarios 1, 3, 5 on a fixture, 2 and 4 by reading; human-only condition stays pending) | maps to the brief | cited | brief pass conditions "scenarios 1, 3 and 5 are shown where one can be made, and where one cannot the closeout says so plainly"; human-only "setup in another repository of his yields a usable record" (pending by its kind) | -
  - DoD 7 (plugin version next minor over base, in every file, last) | internal mechanics (packaging convention; orchestrator.md:29 presumes versions move in manifests) | not audited | - | -
  - DoD 8 (validators pass, Reviewer APPROVED, audits logged, plan closes, branch published, PR opened, note to Counsel, nothing merged) | maps to the brief | cited | step 1 passed on the standing approval, common.md:65 "A finished, reviewed run may publish its branch and open pull requests in this repository without asking first. Merges are not covered and wait for the owner ... Given and accepted by the repository's owner, ebigunso, on 2026-09-30, relayed by Counsel: 'The common rule proposed, accepted.'" (the record is there and says what it must; a file cannot show the words were said); brief pass condition "the package validators pass". The note to Counsel is the harness's reporting to the owner's channel, not a write to an external system; nothing acts on it. | -
  - Planner-added: fixtures and probe outputs in the scratchpad, not the repository | internal mechanics | not audited | - | -
  - Planner-added: the seed in a file of its own | internal mechanics (structure of the plugin's files; behaviour unchanged either way) | not audited | - | -
  - Planner-added: version next minor, last | internal mechanics | not audited | - | -
  - Non-goal: adapters' `model: inherit` and Codex templates stay without a model value; choice made at dispatch from the record | maps to the brief | cited | brief "Who it is for" "not as a model, a family alias or a tier" (constraint); Left out "Any model name or family alias as the default" | -
  - Non-goal: runtime and platform identities and named external skills stay (Claude, Codex, Copilot adapters and paths, the skill-creator skill) | maps to the brief | inferred | extends Limits "No model name, family alias, provider ... in the plugin's rules" (constraint) read with the gives "when a new model or model class ships, nothing in the plugin needs editing": a runtime adapter name identifies a platform and does not change when a model ships; cheap to undo (text) | -
  - Non-goal: the research test run's two observations | maps to the brief | cited | brief Left out "Recording in this repository the two observations from the research test run ... 'not worth keeping so can be kept out'" | -
  - Non-goal: porting the owner's stance beyond the seed | maps to the brief | cited | brief Left out "Porting the owner's own stance between repositories beyond the dated seed" | -
  - Design chosen (reasons in model-routing.md where routing is decided; seed beside it; setup step resolving against lineup and seed, record from a template section, held with the philosophy step's hold-and-confirm) | maps to the brief | cited | pass condition "stated once in the plugin at the place where routing is decided"; item 5 "the same hold-and-confirm the owner chose for philosophy detection" (gives); item 4 (gives) | -
  - Ruling R1 (budget left for the owner to state at confirmation; nothing dispatched before; "Research's 'cost notwithstanding' is the owner's standing setting in this repository only; the plugin states no default allowance") | maps to the brief | ask-now | the first half is covered by item 6 (constraint) and item 5 (gives). The second half departs from a gives: brief item 1 lists under "What the plugin states", as the Researcher's third part (its cost setting), "cost notwithstanding, as the standing setting of 2026-10-22", beside the Auditor's "no cost ceiling"; while "This repository" lists "cost notwithstanding for research" among this repository's resolutions. The statements bearing on it read both ways, and R1 resolves it by dropping the Researcher's cost setting from the plugin, which DoD 1 ("the cost setting" for each role) contradicts inside the plan. | Reason 1: conflict between item 1 (the plugin's Researcher reason carries a cost setting, stated as cost notwithstanding) and R1 as written. Value question: in a fresh repository, does research go to the stronger option for its work type regardless of cost by default, with no cost ceiling as the Auditor has none, or does each repository's owner state research's cost setting as he states the budget allowance? Reason 2: the plan does not say what setup does when the owner confirms the record without stating a budget allowance, which the "says nothing about models, and dispatches go to fitting models at once" gives and the Worker's "best model whose cost is within the budget allowance" both bear on. Value question: when the owner confirms the record without naming an allowance, does the Worker go to the best fitting option regardless of cost, or does setup keep holding until an allowance is stated? | -
  - Ruling R2 (the Orchestrator's model is the session's; its reason is recorded so setup can say which option fits and the owner opens the session on it) | maps to the brief | cited | brief item 1 Orchestrator bullet "judgement that keeps the bigger picture ... at a cost that allows long sessions"; "This repository" "Orchestrator on Opus 5.5" (gives) | -
  - Compatibility stance: migrate; another workspace's old-form record is rewritten in the new form when setup next runs there; nothing promised before then | maps to the brief | inferred | extends item 5 "Setup ... fills the workspace record" (gives) and scenario 2 "setup re-run in a repository redates the record"; the brief says nothing of a workspace that updates the plugin before re-running setup; cheap to undo (text) | -
  - Context: a decision record proposed for ADR-D-0061's rule resolving by the Researcher's reason, if the admission test passes | internal mechanics (repository decision records, not the plugin; acceptance stays the owner's by adr.md step 3) | not audited | - | -
  - Assumption A1 (the no-model constraint covers model choice; runtime and platform identities and the named external skill stay) | maps to the brief | inferred | as the runtime-identities non-goal above: extends Limits (constraint) with the gives "nothing in the plugin needs editing" when a model ships; cheap to undo | -
  - Assumption A2 (the seed names a family beside its provider, no model or version) | maps to the brief | cited | brief item 4 "The first version covers only the Claude and GPT families" (gives); Limits "the seed names providers only, as observations with dates" | -
  - Task_1 (reasons, seed, pointers brought to the new terms; name search; decision record if admitted) | maps to the brief | cited | as DoD 1, 2, 4; item 1 Reviewer bullet "chosen by the kind of finding the work wants at its stage ... chosen when the wanted kind of finding is its strength, not for the difference itself" | -
  - Task_2 (setup's record step, template section, rules-files description; redates on re-run; no model, provider or price) | maps to the brief | cited | as DoD 3; scenario 2 "setup re-run in a repository redates the record"; item 7 "The record is re-observed and redated when a model changes" (means) | -
  - Task_3 (this repository's record rewritten by the Orchestrator; owner's resolutions; FrontierCode citation; lines that stay) | maps to the brief | cited | as DoD 5 | -
  - Task_4 (scenarios 1, 3, 5 shown on fixtures by fresh agents; outcomes in the Progress Log) | maps to the brief | cited | pass condition "scenarios 1, 3 and 5 are shown where one can be made"; probes are local measurement instruments, which common.md:59 allows ("Ephemeral headless ... sessions are allowed only as measurement instruments"); not outward-facing | -
  - Task_5 (version) | internal mechanics | not audited | - | -
  - Decision Log: no entries.
  Human-only conditions pending: "setup in another repository of his yields a usable record without his stating a model"
  Scenarios: none
  Note outside the grades: the Progress Log records the researcher seat reading files outside the dispatch's evidence scope for R1; the plan says none of its findings rests on them. Not an item at plan draft; stated so the Orchestrator sees the auditor saw it.
- Acting on the verdict: Ruling R1 `ask-now`. Reason 1 rests on a line the Orchestrator added ("Research's 'cost notwithstanding' is the owner's standing setting in this repository only"), which departs from the brief's item 1 (the Researcher's cost setting, cost notwithstanding, is stated by the plugin): the line is redone to follow the brief, and no question goes to the owner for it. Reason 2 (a confirmation without an allowance) survives: the brief does not say, and it is sent to Counsel as the verdict's value question. Inferred calls, as the item lines state them: the runtime-identities non-goal and Assumption A1 ("extends Limits ... read with the gives 'nothing in the plugin needs editing' when a model ships"); the Compatibility stance ("extends item 5 ... and scenario 2"); cheap to undo. No statement marked provisional. `Reading compared:` divergences: R1 corrected as above; the fixtures' place, as in the other run, kept only as Task_4's `owns` and dropped from Planner-added requirements; the Compatibility stance's reading corrected to inferred, its text unchanged; the version and the seed's own file stay as listed, the reviewer having asked for them to be listed (MPR-F1), the reading of them as internal mechanics accepted. The revision goes back through plan review and a new plan-draft audit once the owner's answer is in the brief.

## Decision Log (append-only; re-plans and major discoveries)

- D1, 2026-10-28: the plan-draft audit held Ruling R1. Its research-cost half was the Orchestrator's own line departing from the brief's item 1, redone to follow it; its other half (a confirmation without an allowance) is sent to Counsel as the verdict's value question, and the plan waits for the answer in the brief. The fixtures' place is dropped from Planner-added requirements (internal mechanics), kept as Task_4's `owns`.

- D2, 2026-10-29: the owner's answer to D1 and to the plan-draft audit's ask-now on Ruling R1, relayed by Counsel at 2026-10-28T17:37:20Z (admitted by the standing approval of 2026-10-01), quoting him on 2026-10-29: "I'd lean towards your proposal, but only if the best option would be considered expensive by what budget the environment runs on. Today that is mostly true for any setup since the best models are expensive even on the biggest budget plan available, but this may change, so it should be checked against how expensive a model is compared to whatever subscription plan or pay as you go budget." and "the fall back should be the second best model, also judged for its cost, and so on until it lands on something acceptable." Counsel wrote it into the brief under "Directed during the run"; committed with this revision. The plan is revised for it (DoD 3, Ruling R1, Task_2). The revision goes through plan review and a new plan-draft audit before anything is built. D1's hold is ended.

## Notes (Risks / Edge cases)
- A fixture shows what a fresh agent does with the text, not what setup does in his next repository; the human-only pass condition covers that.
- Task_3 edits a rule file and is the Orchestrator's own (`common.md`, Repo Safety); it is dispatched to no Worker.
