# Plan: Trim skill loading, descriptions, and duplicated procedure (Astra guide, part 1 of 3)

- status: in_progress
- generated: 2026-09-13
- last_updated: 2026-09-15
- work_type: docs

## Goal
- Apply the structural findings of the 2026-09-13 audit of the harness against OpenAI's "Rethinking skills and prompts for GPT-6 Astra" (items 1 through 9 of the audit list ebigunso accepted on 2026-09-13): skills load on relevance instead of on presence, descriptions say when to use a skill and nothing else, and each retained rule has one surviving copy. Every change here is the redundancy class of ADR-D-0019: for a duplicated passage, a consumer check and a named surviving canonical copy; for a description trigger nothing in the skill serves, a recorded retirement; no behavior change, no guard relaxed. The harness serves Claude Fable 5.1 and GPT-6 Astra alike; nothing here is model-specific tuning.

## Definition of Done
- Claude adapter frontmatter preloads only the skills a role needs on every task; every other skill the role may need is reachable through the routing table or a conditional route in the body, and the adapter maintenance checklist confirms the three runtimes still agree on role semantics.
- At the start of a non-trivial task the Orchestrator reads the three rule files (`index.md`, `common.md`, `orchestrator.md`, per ADR-D-0020) and nothing else unconditionally; lessons, plans, and the repository reference documents listed in `common.md` are named with the condition under which each is read, in the "use X for Y" form; the create-missing-rules instruction in `lifecycle-gates.md` and the continue-and-record fallback in the skill root say the same thing; `rule-suite-fast-path.md` no longer contradicts itself about when `index.md` is read. The Researcher adapters carry the same conditional form.
- The dispatch checklist is read on first use per role in a session, not before every dispatch; `wave-integration` has one integration procedure, and its Reviewer-packet instruction distinguishes post-Worker packets from draft-plan review.
- Descriptions of `git-workflow`, `durable-docs-authoring`, `playwright-cli`, `playwright-e2e-evidence`, `workspace-troubleshooting`, and `subagent-report-contract` name the scenarios that need the skill and contain no execution mechanics, taxonomy, or promises the references do not keep. Each phrase removed from a description is classified in the Worker report as one of: execution mechanics moved (the body or a reference carries the obligation, quoted); a scenario cue retained in the frontmatter in shorter form; or a trigger retired on purpose because nothing in the skill serves it (the audit's stale troubleshooting families and the provider skill's generic web-interaction list). Retired triggers need no surviving home; obligations do.
- `subagent-report-contract/SKILL.md` carries the schema once and each rule once, with the sample and examples in references; the example that has a Worker editing a rules file is corrected.
- `engineering-quality-baselines` states the core-principles read once; the "explicitly note major categories left out and why" instruction is removed as consumer-less ceremony (no reviewer, validator, or template reads that list; the Reviewer confirms by search); the Required Evidence Note keeps every field whose obligation has no other home (risk profile and rationale, At Risk items with owner and target date, validation depth, residual risk) and points at the plan template or the Worker report for the fields those already require, each such field named with its surviving location. No required evidence is relaxed.
- For every merged or deleted passage that carried an obligation, the Reviewer can name the surviving canonical copy and confirm no consumer pointed only at the deleted text; retired description triggers are listed in the Task_1 report and need no surviving copy.
- Package validation, smoke tests, and `git diff --check` pass; no validator, schema, consent gate, output contract, or evidence requirement changes.

## Scope / Non-goals
- Scope: the files in each task's `owns`.
- Non-goals: any guidance ablation (part 3), any contradiction or stale-copy repair not listed here (part 2), any change to the Plan Gate, Reviewer approval, validation evidence, or Git boundaries; renaming skills; touching `docs/coding-agent/rules/`.

## Compatibility stance
- surface: skill descriptions (discovery text every runtime reads), skill roots and references, Claude adapter frontmatter, Researcher adapter bodies.
- stance: migrate
- justification: all consumers are in this repository; installed copies are refreshed by ebigunso after merge through the plugin update, as after #65; a version bump ships with the change.

## Context (workspace)
- Related files/areas: `claude/agents/harness-orchestrator.md:5-17` (twelve preloaded skills, about 7,000 root words), `harness-worker.md:5-8`, `harness-reviewer.md:6-8`; `skills/orchestration-harness/SKILL.md:14` ("also skim lessons and any active plans"), `references/lifecycle-gates.md:7-17` (seven-entry start-of-work read list; create-missing-rules at :17), `references/rule-suite-fast-path.md:7-12` and :37; Researcher adapters `codex/agent-templates/harness_researcher.toml:35-38`, `agents/Researcher.md:36-39`, `claude/agents/harness-researcher.md:34-37`; `skills/subagent-strategy/SKILL.md:61`; `skills/wave-integration/SKILL.md:12-28` and `references/integration-checklist.md`; the six descriptions at each `SKILL.md:3`; `skills/subagent-report-contract/SKILL.md` (951 words; the Reviewer-evidence rule at :81, :99, :112, :151; `references/examples.md:144`); `skills/engineering-quality-baselines/SKILL.md:31,34,52` and `references/core-principles.md:18`.
- Existing patterns or references: ADR-D-0019 (redundancy class: consumer check plus surviving copy); ADR-D-0020 (the three-file rule entry is the minimum load); ADR-D-0022 (one home for workflow mechanics; replicated role contracts in adapters are the one exception and stay synchronized); `runtime-adapter-contract/references/adapter-maintenance-checklist.md`; `skills-maintenance/references/final-ambiguity-pass.md`.
- Design record consulted and deviations from its acceptance: none; every edit stays inside ADR-D-0019's redundancy class and ADR-D-0022's exception.
- Prior evidence: the Codex Researcher audit delivered over agmsg on 2026-09-12 16:30Z (four parts) and the Orchestrator's own reads of the router skill, the three largest roots, two adapters, and the rules; the article's points are the rubric recorded in the Decision Log.

## Open Questions (max 3)
- Q1: resolved 2026-09-13 by ebigunso as proposed: the Claude Orchestrator preloads `orchestration-harness`, `plan-format`, `subagent-strategy`; Worker keeps `subagent-report-contract` and `engineering-quality-baselines` with `git-workflow` loading only on delegated Git work; Reviewer keeps `engineering-quality-baselines` with `playwright-e2e-evidence` loading only for UI acceptance.

## Assumptions
- A1: Claude loads a skill named in adapter frontmatter at agent start regardless of task; removing a name from the list only changes when the skill loads, since the body's routes still name it — source: Claude Code plugin agent frontmatter semantics; the Reviewer confirms the routes exist for every removed name.
- A2: The package validator's adapter checks look at duplication markers and role sections, not at frontmatter skill lists — source: `scripts/validate_harness_package.py` adapter section; confirmed by running it after Task_6.

## Tasks

### Task_1: Descriptions say when, not how
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/git-workflow/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/durable-docs-authoring/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/playwright-cli/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/playwright-e2e-evidence/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/workspace-troubleshooting/SKILL.md
- depends_on: []
- description: |
  Worker: rewrite the frontmatter description of each owned skill to the article's form ("<what it does>. Use when <scenarios>."), scenario-targeted and as short as the triggers allow. git-workflow: drop the watcher-arming instruction and the stack sentence from the description (both live in the body). durable-docs-authoring: drop the document taxonomy and the admission mechanics (body and `references/adr.md` carry them). playwright-cli: trigger on "a browser automation provider has been selected and it is playwright-cli", not on any web interaction. playwright-e2e-evidence: trigger on UI/E2E acceptance evidence, not on the bare word screenshots. workspace-troubleshooting: name only the failure families the three surviving references cover (stale view or branch mismatch, GitHub CLI auth, unexpected external changes) plus the generic triage entry; drop npm, Windows file locks, and flaky E2E. Bodies change only where a description trigger moved into them and was not already there.
- acceptance:
  - Each owned description names scenarios and contains no imperative execution step; shorter is the editing target, completeness of triggers and obligations the constraint.
  - The Worker report classifies every removed phrase as moved (with the quoted surviving line), retained cue, or retired trigger, and lists the retired triggers explicitly; scenario cues a first-time reader needs to select the skill stay in the frontmatter, never body-only (skills-maintenance final-ambiguity pass).
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py && python scripts/run_validation_smoke_tests.py; from repo root: git diff --check"
  - kind: review
    required: true
    owner: reviewer
    detail: "For each description: scenario-targeted, no mechanics; every moved obligation located in the body or a reference; every retired trigger genuinely served by nothing in the skill; selection cues still in frontmatter; the final-ambiguity pass applied."

### Task_2: Rule entry loads on relevance
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/lifecycle-gates.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/rule-suite-fast-path.md
- depends_on: []
- description: |
  Worker: keep the three-file rule entry (ADR-D-0020) and rewrite everything else in the Repository Rule Entry section, the lifecycle reference's "At the start of non-trivial work, read:" list, and the fast-path reference so each additional source carries its condition: lessons when starting non-trivial work in a repository with a lessons file (recent or relevant entries), active plans when one covers the same area, the repository reference documents listed in `common.md` each for the purpose `common.md` states, project files after the Research Dispatch Gate. Remove the duplicate mandated three-file load from the fast-path reference (state it once, point to the root) and its self-contradiction about when `index.md` is read. Make `lifecycle-gates.md` say what the root says when rule files are absent: continue under the skill and record the missing context; creating rules is `rulebook` work triggered separately. No Plan Gate text changes.
- acceptance:
  - The only unconditional reads at task start are the three rule files; every other source in the three owned files has a stated condition.
  - The absent-rules behavior is stated once and identically in the root and the lifecycle reference; the fast-path reference names index.md's read condition once.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py && python scripts/run_validation_smoke_tests.py; from repo root: git diff --check"
  - kind: review
    required: true
    owner: reviewer
    detail: "Every source load in the three files has a condition; the three-file entry is intact (ADR-D-0020); the two absent-rules statements agree; nothing else in the Plan Gate or the five gates changed."

### Task_3: Dispatch checklist on first use; one wave-integration procedure
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/subagent-strategy/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/wave-integration/**
- depends_on: []
- description: |
  Worker: in `subagent-strategy/SKILL.md` change the per-dispatch reread of `references/dispatch-checklists.md` to a first-use read per role in a session, with the six required prompt sections remaining the always-on contract. In `wave-integration`, merge the root's ten-step Core Checklist and the reference's nine-section checklist into one procedure: the root keeps the trigger, the contract (parse reports, reconcile ownership, required evidence, no duplicate active work, async cleanup pointer to `subagent-strategy`), and routes; the reference keeps the branching (follow-up Worker versus Reviewer dispatch, escalation ruling). Qualify the Reviewer-packet instruction: the packet template is for post-Worker review; draft-plan review uses the plan-review snippet in `subagent-strategy`.
- acceptance:
  - No step appears in both the wave-integration root and its reference; the packet instruction names both review kinds and their inputs.
  - The dispatch checklist read is first-use per role; the six prompt sections are unchanged.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py && python scripts/run_validation_smoke_tests.py; from repo root: git diff --check"
  - kind: review
    required: true
    owner: reviewer
    detail: "Each merged step has exactly one home; contract items (ownership reconciliation, required evidence, independent Reviewer dispatch, async cleanup ownership per ADR-D-0021) all survive; the packet condition is correct."

### Task_4: One copy of the Worker report contract
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/subagent-report-contract/**
- depends_on: []
- description: |
  Worker: make `SKILL.md` the contract statement (absolute requirements, required keys with one-line meanings, the design-alert convention, when optional blocks apply) and move the full inline schema, the `ui_probes` and `lesson_candidates` schemas, and the filling notes into `references/schema.yaml` and `references/examples.md` where they are not already; state the "a Worker UI probe does not satisfy Reviewer-owned validation" rule once and the `base_url` rule once. Fix the description to trigger on producing, validating, or defining a Worker report. In `references/examples.md`, replace the example that has a Worker modifying `docs/coding-agent/rules/reviewer.md` with a rule candidate carrying `audience: reviewer` (only the Orchestrator edits rules), and make the test evidence in the done examples name what ran rather than "Exit code 0." alone. Keep every required key, every enum, and the exactly-one-YAML-block rule; the validator is not touched.
- acceptance:
  - `SKILL.md` carries the contract without the inline schema (shorter is the target, completeness the constraint); every required key and enum still appears in `references/schema.yaml`; each rule has one home.
  - `python skills/subagent-report-contract/scripts/validate_worker_report.py` passes on every fixture under `tests/coding-agent-orchestration-harness/fixtures/` that it passed on before; the corrected example validates.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/run_validation_smoke_tests.py (covers the report fixtures) && python scripts/validate_harness_package.py; from repo root: git diff --check"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff the contract before and after: no required key, enum, or evidence rule lost; each rule stated once; examples consistent with the single-writer rule for rules files; description scenario-targeted."

### Task_5: Quality-baselines scaffolding
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/core-principles.md
- depends_on: []
- description: |
  Worker: state the core-principles read once (in the root's routing list; delete the "Start with this document for every..." repeat inside the reference). Remove "explicitly note major categories left out and why" after confirming by search that no reference, template, validator, or Reviewer rule consumes that list. For the Required Evidence Note, build a field table first: for each of its nine fields, whether `plan-format/references/plan-template.md` or `subagent-report-contract/references/schema.yaml` requires an equivalent field under a surviving obligation (quote it) or not. The table decides: a field with an equivalent required elsewhere becomes a pointer to that home; every other field stays in the note. The note then applies as a fallback whenever the actual output does not already supply the field under a surviving obligation, for Worker reports and standalone Reviewer outputs alike; no new schema field is added anywhere. The Worker report is expected to show that risk profile with rationale, validation depth, and At Risk owner and target date have no equivalent in either contract and stay, and to decide in-scope and out-of-scope docs and the check lists from the table, not by assumption. Keep the risk triage, the routing list, the Drift Tripwires, the stop condition, and precedence unchanged.
- acceptance:
  - The core read is mandated in one place; the categories-left-out instruction is gone with the consumer search recorded; the field table is in the Worker report with a quoted equivalent for every field turned into a pointer; the note's fallback condition is stated in terms of the evidence the output supplies; the stop condition still references every field it needs.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py && python scripts/run_validation_smoke_tests.py; from repo root: git diff --check"
  - kind: review
    required: true
    owner: reviewer
    detail: "Tripwires, stop condition, routing conditions, and precedence unchanged; field table complete and correct against the plan template and the report schema; the consumer search for the categories-left-out list is reproduced; no required evidence relaxed."

### Task_6: Adapters load on relevance and stay in sync
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/claude/agents/**
  - plugins/coding-agent-orchestration-harness/agents/**
  - plugins/coding-agent-orchestration-harness/codex/agent-templates/**
- depends_on: [Task_2]
- description: |
  Worker: (1) Claude frontmatter `skills:` lists per Q1's resolution; add a body line in each Claude adapter naming where the removed skills are routed from. (2) In all three Researcher adapters, rewrite the "Consult repo docs if present" block to the conditional form Task_2 landed (the three rule files when present; reference documents each for the purpose `common.md` states). (3) Run `runtime-adapter-contract/references/adapter-maintenance-checklist.md`: the three Researcher bodies stay semantically equivalent, differences classified as runtime-specific. No other adapter text changes (the Copilot research gate and the Worker workflow are part 2).
- acceptance:
  - Claude adapters preload only the Q1 set; each removed skill is named by a route in the adapter body or the orchestration-harness routing table.
  - The three Researcher adapters carry the same conditional read block; the checklist's sync steps are reported with body hashes.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py && python scripts/run_validation_smoke_tests.py; from repo root: git diff --check"
  - kind: review
    required: true
    owner: reviewer
    detail: "A2 holds (validator passes); every removed preload has a live route; the Researcher block matches Task_2's wording; adapter sync evidence present; no other adapter lines changed."

### Task_7: Final review, version bump, and closeout
- type: review
- owns:
  - plugins/coding-agent-orchestration-harness/.claude-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.codex-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.github/plugin/plugin.json
- depends_on: [Task_1, Task_3, Task_4, Task_5, Task_6]
- description: |
  Orchestrator bumps the three plugin manifests together (patch version); Reviewer reviews the whole diff against the Definition of Done, with the ADR-D-0019 redundancy check applied to every deletion: surviving copy named, no consumer orphaned.
- acceptance:
  - Reviewer status is APPROVED; manifests agree.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review of the full change set vs Definition of Done; for each deleted or merged passage, the surviving canonical copy and a consumer search (grep for the old heading or phrase across plugins/ and docs/coding-agent/rules/)."

## Task Waves (explicit parallel dispatch sets)

Interpretation:
- Tasks listed in the same wave are intended to be dispatched in parallel by default, when `owns` are disjoint and dependencies are met.
- Waves are executed sequentially.

- Wave 1 (parallel): [Task_1, Task_2, Task_3, Task_4, Task_5]
- Wave 2 (parallel): [Task_6]
- Wave 3 (parallel): [Task_7]

## Rollback / Safety
- Own feature branch off `main`; one PR; reverting it restores every file. No installed copy changes before merge; ebigunso refreshes after merge.
- Parts 2 and 3 of the audit follow-up run after this plan merges, rebased on its result, because they touch some of the same skill files.

## Progress Log (append-only)

Append-only editing rule (applies to both logs below): when appending an entry, anchor the edit on the previous entry and reproduce it (or anchor on the section's tail marker) so the edit inserts rather than replaces, and verify afterward that the log grew.

- 2026-09-15 Wave 1 Task_1 through Task_5 implemented, review pending: [Task_1, Task_2, Task_3, Task_4, Task_5]
  - Summary: five Claude Worker subagents in parallel on disjoint owns. Task_1: five descriptions rewritten to "what. Use when scenarios."; removed phrases classified moved/retained/retired with quoted homes; retired: workspace-troubleshooting npm, Windows file locks, flaky E2E, installs break, EPERM/EBUSY, CI/validation confusion (no reference covers them); playwright-cli generic web list; bare "screenshots". Task_2: three-file rule entry kept; lessons, plans, common.md reference documents, and project files now load on stated conditions in the skill root with lifecycle-gates.md pointing at it; absent-rules sentence identical in both; fast-path reference no longer restates the load or contradicts itself; one duplicated create-plans sentence removed on ruling. Task_3: dispatch checklist read first-use per role; wave-integration root reduced to a five-item contract plus routes, reference to four branching sections; packet route names post-Worker packet versus draft-plan snippet; a new re-dispatch clause removed on ruling. Task_4: report contract root 951 to 637 words, full shape and enums in schema.yaml, probe rule and base_url rule one home each, rules-file-editing example replaced by an audience: reviewer candidate, evidence names what ran, description triggers on producing/validating/defining. Task_5: core read mandated once; categories-left-out clause removed with a consumer search; evidence note kept as fallback with two pointer fields (required and optional checks to validation_results) and seven retained fields; on ruling, a duplicate load sentence dropped and the stale companion list (stack, language, security references removed under ADR-I-0004/0005) replaced by the surviving set in core-principles.md and the description.
  - Validation evidence: each Worker: validate_harness_package.py pass, run_validation_smoke_tests.py exit 0, git diff --check clean (Task_5 saw one transient failure on Task_4's mid-edit file, rerun clean); Orchestrator reran all three on the integrated tree before commit. Reviewer review dispatched for the wave.
  - Notes: findings surfaced outside owns and left for later: dispatch-guidance.md:74-78 carries its own Reviewer packet field list without the draft-plan alternative (Task_3); the three Worker adapters restate the UI-probe rule as replicated role contract, kept (Task_4). Worker lesson candidates held for closeout: audience-line regex in the package validator; parallel-wave validator transients; Windows scratchpad path length; Bash heredoc and loop stalls.

## Decision Log (append-only; re-plans and major discoveries)

- 2026-09-13 Decision: Plan drafted as part 1 of the Astra-guide follow-up ebigunso requested ("Let's do all of them. Draft the plans needed.").
  - Trigger / new insight: the article's nine points (short scenario-targeted descriptions; root as minimal router; fewer recipes; model-specific guidance overconstrains; conditional file references; drop run-tests-and-ask handholding; explicit permission for safe workflows; reframe protective boundaries; define completion up front) were applied to the harness by the Codex Researcher (agmsg, 2026-09-12 16:30Z, four parts) and the Orchestrator. Items 1 through 9 of the accepted list are redundancy-class changes and form this plan; contradictions, stale copies, permission wording, and model assumptions (items 10 through 14 and 16) form part 2; the repeat-check ablation (item 15) forms part 3.
  - Plan delta (what changed): this plan exists; draft pending Reviewer plan review and ebigunso's approval. Research waived: the audit is the research; its findings are quoted in Context with line numbers.
  - Tradeoffs considered: one plan for all sixteen items (rejected: three evidence classes under ADR-D-0019 need three validation methods, and the ablation's cost should be approved on its own).
  - User approval: pending.
- 2026-09-13 Decision: Plan review round 1 (Codex Reviewer) findings applied.
  - Trigger / new insight: Task_1's acceptance required a surviving home for every removed description phrase, which would have reinstated the stale troubleshooting families and the generic browser list the DoD retires; Task_5 claimed the evidence note duplicates plan and report fields, but risk profile and At Risk owner/date have no other home and a Reviewer output is not a Worker report; the word ceilings were new constraints with no source.
  - Plan delta (what changed): removed phrases are classified as moved obligation, retained cue, or retired trigger, with surviving homes required only for obligations and selection cues kept in frontmatter; Task_5 builds a per-field table, keeps fields with no other home, and removes the categories-left-out instruction as consumer-less with the search recorded; the ceilings are editing targets subordinate to completeness.
  - Tradeoffs considered: keeping the ceilings as hard limits (rejected: no evidence behind the numbers).
  - User approval: pending with plan approval.
- 2026-09-13 Decision: Plan review round 2 (Codex Reviewer) findings applied.
  - Trigger / new insight: Task_5 still preclassified in-scope and out-of-scope docs as duplicated by the plan template and Worker report, which require no such fields, and tied the fallback to output type rather than to evidence present; the Goal and one DoD line still demanded a surviving copy for every deletion, contradicting the retired-trigger permission.
  - Plan delta (what changed): the field table decides pointers by quoted equivalents; the fallback applies whenever the output lacks the field; the surviving-copy requirement is limited to obligations and duplicated passages in the Goal and DoD.
  - Tradeoffs considered: none.
  - User approval: pending with plan approval.

- 2026-09-13 Decision: Q1 resolved by ebigunso as proposed.
  - Trigger / new insight: ebigunso: "All questions in the three plans are otherwise settled as accepting your given recommendations."
  - Plan delta (what changed): Q1 marked resolved; Task_6 applies the named preload sets.
  - Tradeoffs considered: none.
  - User approval: yes for Q1 (2026-09-13); plan approval pending.

- 2026-09-15 Decision: Plan approved by ebigunso.
  - Trigger / new insight: Codex Reviewer plan review APPROVED (a3d8908); ebigunso: "I accept all the plans as well as the ADR. Get to work."
  - Plan delta (what changed): status in_progress. Execution on feature/2026-09-15/astra-guide-part1, branched from the drafts branch so the accepted record and the approved parts 2 and 3 travel with it.
  - Tradeoffs considered: none.
  - User approval: yes (2026-09-15).

- 2026-09-15 Decision: Task_5 scope widened by one description on the Orchestrator's ruling.
  - Trigger / new insight: the Task_5 Worker surfaced that the engineering-quality-baselines description and core-principles.md How to Use still promised stack, language, and security references removed under ADR-I-0004 and ADR-I-0005.
  - Plan delta (what changed): the description and the companion list name the surviving references; the Goal's "no promises the references do not keep" covers it; redundancy class (a stale claim with no consumer).
  - Tradeoffs considered: deferring to part 2 (rejected: same class as Task_1's retirements, same owner, one line each).
  - User approval: not required (inside the approved Goal; recorded per ADR-D-0018's surfacing obligation).

## Notes
- Word counts in the audit are static whitespace counts of file text, not measured context; the plan does not claim a token saving, only that each rule has one home and each load a condition.

Required-check waiver
- What is waived: Reviewer-owned UI/E2E/visual validation for this plan.
- Why waived now: no UI, frontend, or user flow changes; the words UI, E2E, and visual appear only as the names of skills whose text or descriptions are edited.
- Risk accepted and impact: none; every edited file is Markdown or adapter frontmatter with no rendered surface.
- Mitigation and follow-up: package validation, smoke tests, and Reviewer diff review cover the edits; if a task turns out to touch a rendered surface, the Orchestrator replans.
- Owner and expiration: Orchestrator ; expires at plan closeout.
