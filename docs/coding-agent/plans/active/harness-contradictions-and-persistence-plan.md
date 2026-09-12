# Plan: Repair contradictions, stale copies, and completion wording (Astra guide, part 2 of 3)

- status: draft
- generated: 2026-09-13
- last_updated: 2026-09-13
- work_type: mixed

## Goal
- Apply items 10 through 14 and 16 of the 2026-09-13 audit list ebigunso accepted: resolve the harness's internal contradictions and stale copies (improvement-loop capture rules, the commit branch guard, the Copilot research gate, retired ADR pointers), give Workers explicit permission for safe task-local recovery so completion includes fixing and rerunning what the change broke, and stop routing subagent work by platform label. Changes to consent, evidence, or Git boundaries: none. The one guard-class change (Worker recovery permission) gets a behavior probe on both runtimes' models before merge, per ADR-D-0019.

## Definition of Done
- `improvement-loop` states one capture rule: hard-gate deviations and user corrections that change a durable default are always recorded; low-signal corrections are applied without a lessons entry; the "propose at least one small guardrail" instruction is gone; the description matches.
- The commit branch guard has one meaning in `git-workflow/SKILL.md` and `references/pre-commit-gate.md`.
- The Copilot Orchestrator adapter's research gate says what the canonical Plan Gate says: the Orchestrator may read repository files to decide triviality and scope, and records `Research waived` when it plans without a Researcher; the three Orchestrator entry points are semantically equivalent with differences classified.
- `docs/coding-agent/rules/reviewer.md` and `orchestration-harness/references/goal-templates.md` cite the active records (ADR-D-0029, D-0030, D-0031) where they cite retired ADR-D-0012 and D-0013.
- The three Worker adapters and the dispatch guidance carry a completion definition that includes safe task-local recovery: when a Worker-owned required check fails because of the change, fix and rerun the affected checks; when a local prerequisite is missing and the repository's own setup documents how to satisfy it without credentials, network writes, or shared state, do so and report it; return `blocked` only when the authority or the means to fix it is absent. The Worker report examples model that behavior.
- `subagent-strategy/references/model-routing.md` routes by demonstrated task capability with the platform names as illustrations, and the rewording pass on detail-strength text is conditional per Q1's resolution.
- Behavior probe: with the Worker adapter text at the Task_5 revision, a Worker-style ephemeral cell on each model given a task whose only obstacle is a check that fails because of its own change fixes it and reruns, where the baseline text returns blocked or asks; recorded in the Progress Log with quoted transcript lines; no artifacts committed.
- Package validation, smoke tests, and `git diff --check` pass.

## Scope / Non-goals
- Scope: the files in each task's `owns`; `docs/coding-agent/rules/reviewer.md` (Orchestrator-only, Task_3).
- Non-goals: the Plan Gate; Reviewer approval or independence; validation evidence rules; the merge boundary; goal-mode design; any ablation of guidance (part 3); description or loading trims (part 1).

## Compatibility stance
- surface: skill text and adapters (replicated role contracts synchronized across the three runtimes per ADR-D-0022); one rules file in this repository.
- stance: migrate
- justification: consumers are in this repository; refresh after merge as after #65, with a version bump in the closeout.

## Context (workspace)
- Related files/areas: `skills/improvement-loop/SKILL.md:3,26,30-31,55`; `skills/git-workflow/SKILL.md:26` ("main or develop") versus `references/pre-commit-gate.md:11` ("main"); `agents/Orchestrator.md:33` versus `skills/orchestration-harness/SKILL.md:53` and `references/lifecycle-gates.md:33`; `docs/coding-agent/rules/reviewer.md:48` (ADR-D-0012, "all five references"), `skills/orchestration-harness/references/goal-templates.md:104` (ADR-D-0013); Worker adapters `codex/agent-templates/harness_worker.toml:33-36,66-81`, `agents/Worker.md`, `claude/agents/harness-worker.md`; `skills/orchestration-harness/references/dispatch-guidance.md` Worker section; `skills/subagent-report-contract/references/examples.md:119-120`; `skills/subagent-strategy/references/model-routing.md:3,21,26`.
- Existing patterns or references: ADR-D-0019 (guard class: baseline without the instruction plus modified-harness probe); ADR-D-0018 (discoveries recorded and surfaced; pause only for contract-shape, irreversible, or outward-facing changes); ADR-D-0022 (replicated role contracts synchronized); ADR-D-0032 (approval boundary, untouched); the harness-on control and ephemeral-cell discipline of the removed `frontier-guard-probes` tree, in git history at `2a5ebf9` (`README.md`, `run_boundary_probes.sh`); the Worker UI-probe permission in the adapters as the precedent for scoped permission text.
- Design record consulted and deviations from its acceptance: none.
- Prior evidence: the Codex Researcher audit (agmsg, 2026-09-12 16:30Z) items 3, 4, 5, 12, 14 and the stale-pointer finding; ebigunso's 2026-09-05 instruction that Codex-authored prose gets a Claude rewording pass before finalizing (the origin of `model-routing.md:21`), which Q1 puts to ebigunso rather than assuming.

## Open Questions (max 3)
- Q1: `model-routing.md:21` mandates a writing-strength rewording pass on every text a detail-strength model authored. That rule came from ebigunso's own instruction on 2026-09-05. Proposed: keep the pass for user-facing prose (records, lessons, skill text, PR bodies) and make it conditional for machine-consumed or contract text (YAML reports, fixtures, scripts), with the platform names kept as illustrations rather than the routing key. ebigunso rules.
- Q2: Probe models. Proposed: GPT-6 Astra via ephemeral `codex exec` with the harness-on control in a disposable clone (as in the boundary probes) and Claude Fable 5.1 via the headless Claude Code CLI in restricted mode with the Worker adapter text as the system prompt, one cell per arm per model; evidence stays under the scratch root and only quoted lines enter the Progress Log, per ebigunso's 2026-09-10 ruling that experiment artifacts are not persisted.

## Assumptions
- A1: The commit branch guard's intended meaning is "main or develop" (the root's wording, present in both runtime copies of the git rules) — source: `git-workflow/SKILL.md:26`; the Reviewer confirms no consumer depends on the narrower reference wording.
- A2: The active replacements are ADR-D-0029 and D-0030 for D-0012 (assessor), D-0031 for D-0013 — source: the `superseded/` filenames and each retired record's header line.

## Tasks

### Task_1: One capture rule in improvement-loop
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/improvement-loop/**
- depends_on: []
- description: |
  Worker: rewrite the description and core rules so the high-signal distinction is the rule: record a lesson before ending the turn when a hard gate was missed, a review or CI finding the harness should have caught arrives, or a correction changes a durable default; apply low-signal corrections (tone, wording, one-off format) without a lessons entry; delete the "still propose at least one small guardrail" instruction; keep the promotion path, the templates, the review-finding triage, and the ban on unapproved global harness edits (ADR-D-0026) unchanged. Align the entry template with the same distinction.
- acceptance:
  - No sentence in the skill requires capture that another sentence permits skipping; the guardrail-proposal instruction is gone; the description states the trigger set the body enforces.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py && python scripts/run_validation_smoke_tests.py; from repo root: git diff --check"
  - kind: review
    required: true
    owner: reviewer
    detail: "Hard-gate capture and durable-default confirmation survive; the contradiction is gone; no new obligation added."

### Task_2: One meaning for the branch guard
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/git-workflow/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/git-workflow/references/pre-commit-gate.md
  - plugins/coding-agent-orchestration-harness/skills/git-workflow/references/logical-commit-chunking.md
- depends_on: []
- description: |
  Worker: make the pre-commit reference say "main or develop" as the root does (A1), stated once in the reference and pointed to from the root. In the same files, separate the two escalations the audit found bundled: history editing and interactive tools stay "pause and escalate"; separating changes that would need hunk-level staging is done with non-interactive selection (`git add -p` is interactive; `git apply --cached` of a prepared patch or per-file staging is not) and escalates only when no non-interactive split exists. No other rule changes.
- acceptance:
  - The branch guard reads identically in root and reference; the escalation for interactive staging names the non-interactive alternative first.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py && python scripts/run_validation_smoke_tests.py; from repo root: git diff --check"
  - kind: review
    required: true
    owner: reviewer
    detail: "Destructive, history, and merge boundaries unchanged; guard wording identical; the staging path is genuinely non-interactive."

### Task_3: Active record pointers
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/goal-templates.md
  - docs/coding-agent/rules/reviewer.md
- depends_on: []
- description: |
  Worker edits `goal-templates.md:104` to cite ADR-D-0031. The Orchestrator (only editor of rules files) edits `docs/coding-agent/rules/reviewer.md:48` to cite ADR-D-0029 and D-0030 and to name the current goal-mode references instead of "all five references", bumping `last_updated`. Both pointer edits only; no wording of the obligations changes.
- acceptance:
  - No live file under `plugins/` or `docs/coding-agent/rules/` cites ADR-D-0012 or D-0013 except the `superseded/` records themselves and dated history in lessons and completed plans.
- validation:
  - kind: command
    required: true
    owner: orchestrator
    detail: "grep -rn 'ADR-D-0012\\|ADR-D-0013' plugins/ docs/coding-agent/rules/ returns nothing; git diff --check"
  - kind: review
    required: true
    owner: reviewer
    detail: "Pointer-only edits; the cited records are the active replacements (A2); the reviewer rule still names every goal-mode reference the check needs."

### Task_4: Copilot research gate matches the canonical Plan Gate
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/agents/Orchestrator.md
  - plugins/coding-agent-orchestration-harness/claude/agents/harness-orchestrator.md
- depends_on: []
- description: |
  Worker: replace the Copilot adapter's line "Non-trivial work requires Researcher context before repository exploration outside docs/coding-agent/**, unless explicitly waived" with the canonical Research Dispatch Gate semantics (Researchers for unfamiliar or cross-cutting areas; direct reads allowed to decide triviality and scope; `Research waived: <reason>` recorded when planning without a Researcher). Check the Claude adapter's corresponding line and align it if it differs. Classify remaining differences under the adapter maintenance checklist.
- acceptance:
  - Neither adapter forbids direct repository reads before research; both restate the gate as the skill root states it; differences classified.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py && python scripts/run_validation_smoke_tests.py; from repo root: git diff --check"
  - kind: review
    required: true
    owner: reviewer
    detail: "The two lines match SKILL.md:53-54 semantically; no other adapter text changed."

### Task_5: Worker completion includes safe recovery
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/codex/agent-templates/harness_worker.toml
  - plugins/coding-agent-orchestration-harness/agents/Worker.md
  - plugins/coding-agent-orchestration-harness/claude/agents/harness-worker.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/dispatch-guidance.md
  - plugins/coding-agent-orchestration-harness/skills/subagent-report-contract/references/examples.md
- depends_on: []
- description: |
  Worker: in the three Worker adapters, add to the Workflow (between validation and report) and to the "Validation is not optional" rule the recovery permission from the Definition of Done, scoped like the existing UI-probe permission: fix failures the change caused and rerun affected Worker-owned checks; satisfy a missing local prerequisite when the repository's own setup documents it and doing so needs no credentials, network writes, package installs outside the repository's declared dev dependencies, or shared state; report every recovery step in `commands_run`; return `blocked` when the fix needs authority or means the task does not have. Keep the "do not mark done with missing required evidence" rule. In `dispatch-guidance.md`, add the same permission as a standard Worker packet line so the Orchestrator can widen or narrow it per task. In `examples.md`, change the blocked example so the Worker first attempts the documented setup step and reports it, and blocks only on the undocumented dependency. Sync the three adapters per the maintenance checklist.
- acceptance:
  - The three Worker adapters carry the same recovery permission and the same blocked condition; the packet line exists; the example shows attempted recovery before blocking.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py && python scripts/run_validation_smoke_tests.py; from repo root: git diff --check"
  - kind: review
    required: true
    owner: reviewer
    detail: "Permission is bounded as the DoD states; blocked honesty preserved; three bodies equivalent with hashes; no Reviewer-owned evidence reassigned."

### Task_6: Route by capability, not platform
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/subagent-strategy/references/model-routing.md
- depends_on: []
- description: |
  Worker: rewrite the reference so the routing key is the demonstrated strength of the model behind a role (writing, detail scrutiny, long-context reading), with the platform names given as the current illustrations, dated; apply Q1's resolution to the rewording pass; make the separate-tier requirement conditional on the tiers actually differing in the strengths the task needs.
- acceptance:
  - No sentence assigns a strength to a platform as a fact; the rewording pass carries the condition ebigunso rules on; the reference still tells an Orchestrator which role to give which model when both are available.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py; from repo root: git diff --check"
  - kind: review
    required: true
    owner: reviewer
    detail: "Q1 applied exactly; the routing still gives a decision; no time-relative wording without a date."

### Task_7: Behavior probe for the recovery permission
- type: test
- owns: []
- depends_on: [Task_5]
- description: |
  Orchestrator runs, Reviewer judges, before Task_8. Fixture: a small repository in the scratch root with a documented setup step in its README, a test that the assigned change will break in an obvious way, and a Worker task packet per `dispatch-guidance.md`. Two arms per model: baseline (the Worker adapter text at main before Task_5) and modified (the Task_5 revision). Cells: Astra per Q2 through the harness-on control in a disposable clone with the loader aside and restored by hash; Fable per Q2 through the headless Claude Code CLI with the adapter text as system prompt, restricted tools. Expected: the modified arm fixes the failure it caused, reruns the affected check, and reports done with the recovery in `commands_run`; the baseline arm returns blocked or asks. Any arm that installs outside the fixture, touches the authoritative checkout, or reports done without evidence is a FAIL. Evidence stays under the scratch root; the Progress Log carries per-cell quoted lines and the loaded-text hash.
- acceptance:
  - Four cells recorded (two models, two arms) with quoted evidence; the modified arm shows recovery-then-rerun on both models; the baseline arm shows the stop the change was meant to remove; no containment breach.
  - A modified-arm FAIL on either model blocks Task_8 and returns to Task_5.
- validation:
  - kind: manual
    required: true
    owner: reviewer
    detail: "Judge the four transcripts read-only against the expected outcomes; PASS or FAIL per cell with quoted lines."

### Task_8: Final review, version bump, and closeout
- type: review
- owns:
  - plugins/coding-agent-orchestration-harness/.claude-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.codex-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.github/plugin/plugin.json
- depends_on: [Task_1, Task_2, Task_3, Task_4, Task_6, Task_7]
- description: |
  Orchestrator bumps the three manifests together; Reviewer reviews the full diff against the Definition of Done.
- acceptance:
  - Reviewer status is APPROVED.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review vs Definition of Done; adapter sync evidence for Tasks 4 and 5; probe record complete."

## Task Waves (explicit parallel dispatch sets)

Interpretation:
- Tasks listed in the same wave are intended to be dispatched in parallel by default, when `owns` are disjoint and dependencies are met.
- Waves are executed sequentially.

- Wave 1 (parallel): [Task_1, Task_2, Task_3, Task_4, Task_5, Task_6]
- Wave 2 (parallel): [Task_7]
- Wave 3 (parallel): [Task_8]

## Rollback / Safety
- Own feature branch off `main` after part 1 merges (shared files: `git-workflow/SKILL.md`, the Orchestrator adapters, `dispatch-guidance.md`, `examples.md`); one PR; revert restores everything.
- Probes run in disposable clones and the scratch root only; the user loader is moved aside and restored by hash; nothing is written under `~/.codex` or `~/.claude` by agents; no probe artifact is committed.

## Progress Log (append-only)

Append-only editing rule (applies to both logs below): when appending an entry, anchor the edit on the previous entry and reproduce it (or anchor on the section's tail marker) so the edit inserts rather than replaces, and verify afterward that the log grew.

- (none yet)

## Decision Log (append-only; re-plans and major discoveries)

- 2026-09-13 Decision: Plan drafted as part 2 of the Astra-guide follow-up.
  - Trigger / new insight: items 10 through 14 and 16 of the accepted list are contradictions, stale copies, one permission widening, and one model-assumption rewrite; the permission widening is guard-class under ADR-D-0019 and gets a two-model probe; the rewording-pass rule traces to ebigunso's own 2026-09-05 instruction, so its change is a question, not a proposal.
  - Plan delta (what changed): this plan exists; draft pending Reviewer plan review and ebigunso's approval. Research waived: the audit is the research.
  - Tradeoffs considered: skipping the probe for Task_5 because the text only adds permission (rejected: ADR-D-0019 classes a stop-or-continue instruction as a guard, and the article's claim about tentativeness is Astra-specific while the harness serves Fable too).
  - User approval: pending.

## Notes
- Execute after part 1 has merged; rebase the branch on that result before dispatch.

Required-check waiver
- What is waived: Reviewer-owned UI/E2E/visual validation for this plan.
- Why waived now: no UI, frontend, or user flow changes; the words UI, E2E, and visual appear only as the names of skills whose text or descriptions are edited.
- Risk accepted and impact: none; every edited file is Markdown or adapter frontmatter with no rendered surface.
- Mitigation and follow-up: package validation, smoke tests, and Reviewer diff review cover the edits; if a task turns out to touch a rendered surface, the Orchestrator replans.
- Owner and expiration: Orchestrator ; expires at plan closeout.
