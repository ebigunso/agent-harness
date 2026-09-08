# Plan: Plan Gate waiver boundary (no self-waived approval of non-trivial work)

- status: draft
- generated: 2026-09-09
- last_updated: 2026-09-09
- work_type: mixed

## Goal
- Close the blocker recorded by the live loader check on 2026-09-08 (`docs/coding-agent/experiments/frontier-guard-probes/results-2026-09-live-loader.md`): the Plan Gate in `orchestration-harness/SKILL.md` lets the Orchestrator waive plan approval "with a recorded reason and evidence", and a headless Codex session used that clause to implement a non-trivial change with no human seeing the plan. Decide where the waiver boundary lies, land it as a decision record if it passes the admission test, apply it to the skill and the replicated adapter blocks, and show cell (ii) passing.

## Definition of Done
- The Plan Gate wording no longer permits the Orchestrator to waive user approval of a plan for non-trivial work on its own authority; what the Orchestrator may still do alone (reclassify work as trivial under the existing tripwires, or stop and wait when no user is present) is stated in the same section.
- If the admission test in `durable-docs-authoring/references/adr.md` passes, one decision record states the boundary and is accepted by ebigunso on its own; if it fails, the Decision Log records why and the boundary lives in skill text only.
- The three runtime adapter copies of the role contract that mention the Plan Gate, if any, are updated together and diffed for sync per `runtime-adapter-contract`.
- A rerun of loader cell (ii) (same ephemeral method, same prompt, a fresh session on a checkout carrying the change) loads the harness, presents a plan, and stops without implementing; the Reviewer judges the transcript read-only and records PASS.
- No other Plan Gate behavior changes: the trivial/non-trivial classification, the draft-plan review, and the goal-mode substitution stay as written.

## Scope / Non-goals
- Scope: `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/SKILL.md` (Plan Gate section), `references/lifecycle-gates.md` if it restates the waiver, the three Worker/Orchestrator adapter files only where they replicate the waiver wording, `docs/coding-agent-orchestration-harness/decisions/` for the record, `docs/coding-agent/experiments/frontier-guard-probes/` for the rerun.
- Non-goals: the headless-runtime subagent spawn failure (a Codex limitation, recorded in the live loader results; not a harness fault); goal mode's envelope ratification; any change to ADR-D-0017 or ADR-D-0020, both supported by the live check.

## Compatibility stance
- surface: the Plan Gate text every Orchestrator session follows, and the replicated adapter blocks.
- stance: migrate
- justification: the only consumers are the skill's readers and the three adapters, all in this repository; installed copies are refreshed by the user after merge (same procedure as Refresh 1 and 2 in `frontier-guidance-follow-ups-plan.md`).

## Context (workspace)
- Related files/areas: `skills/orchestration-harness/SKILL.md` Plan Gate ("requires a plan plus user approval unless explicitly waived by the user or Orchestrator with a recorded reason and evidence"; the draft-plan review clause extends the waiver); `references/lifecycle-gates.md`; `agents/Orchestrator.md`, `claude/agents/harness-orchestrator.md`, `codex/agent-templates/harness_*.toml`; the live loader transcript `frontier-guard-probes/live-loader/transcript-ii.txt` (self-waiver at lines 3245-3247).
- Existing patterns or references: ADR-D-0020 (loader-routed sessions assume the Orchestrator role; supported by the check), ADR-D-0017 (harness text holds no user authority), ADR-D-0027 (goal mode: the envelope is ratified by the user and immutable during the run, the analogous boundary for goal mode), the frontier-guard-probes README on the guard class.
- Design record consulted and deviations from its acceptance: ADR-D-0027 is the nearest precedent (a loop may never widen its own permissions); this plan applies the same shape to plan mode.
- Prior evidence: cell (ii) of the live loader check, Reviewer verdict 2026-09-08: the self-waiver "is permitted by the Plan Gate as written".

## Open Questions (max 3)
- Q1: Does the boundary admit a "no user present" branch (a headless session stops and reports the plan) or must a headless session refuse non-trivial work outright? Proposed: stop and report; the plan is the deliverable, and a later human turn approves it.
- Q2: Does the change reach the goal-mode Plan Gate position (mode selection test) or only plan mode? Proposed: plan mode only; goal mode already has ADR-D-0027.
- Q3: Is the cell (ii) rerun enough evidence, or should the guard class also get a probe with the user-turn instruction "waive approval" to show the user can still waive? Proposed: add that second probe; it is one more ephemeral cell.

## Assumptions
- A1: The waiver clause lives in one place in `SKILL.md` and is restated in `lifecycle-gates.md` at most once; the adapters route to the skill and do not quote the clause — source: grep for "waived" across the plugin on 2026-09-09 (to be confirmed by Task_1).
- A2: The ephemeral method from `frontier-guidance-follow-ups-plan.md` (Decision Log 2026-09-08) reproduces the failure and can show the fix — source: transcript-ii.txt.
- A3: Installed copies are refreshed by ebigunso after merge before any live session relies on the change — source: Refresh 1 and 2 pattern.

## Tasks

### Task_1: Inventory the waiver wording and its consumers
- type: research
- owns: []
- depends_on: []
- description: |
  Researcher, read-only: every place in the plugin and the rules that states, restates, or depends on the Orchestrator's ability to waive plan approval or draft-plan review (skill, references, adapters, validators, rule templates, lessons). For each, quote the line and say whether it must change, stay, or is only a pointer. Also list what the Orchestrator does today when no user can answer (headless, or an unanswered approval ask) and where that is written. Return the inventory and a one-paragraph statement of the fork for the decision record.
- acceptance:
  - Every hit for "waive" and "waiver" in `plugins/` and `docs/coding-agent/rules/` is classified with a file:line.
  - The fork is stated in one paragraph a first-time reader could act on.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Spot-check the inventory against a fresh grep; confirm no consumer of the waiver clause is missing."

### Task_2: Decide the boundary and propose the record
- type: docs
- owns:
  - docs/coding-agent-orchestration-harness/decisions/**
- depends_on: [Task_1]
- description: |
  Orchestrator: run the admission test on the boundary decision (candidate statement: "The Orchestrator never waives user approval of a plan for non-trivial work; it may reclassify work as trivial under the existing tripwires, and with no user present it presents the plan and stops"). If it passes, draft one record to the template, present it to ebigunso on its own (title, decision, constraint, why), and land it only on an explicit yes; if it fails, record why in this plan's Decision Log and carry the boundary in skill text only. Resolve Q1 and Q2 here.
- acceptance:
  - The admission test result is recorded in the Decision Log with the criterion that decided it.
  - If a record is proposed, it has a standalone acceptance entry before any skill edit lands.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Admission questions per subagent-strategy's ADR review snippet; can a maintainer act on the Decision alone; no time-relative wording; one decision."

### Task_3: Apply the boundary to the skill and adapters
- type: impl
- owns:
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/lifecycle-gates.md
  - plugins/coding-agent-orchestration-harness/agents/Orchestrator.md
  - plugins/coding-agent-orchestration-harness/claude/agents/harness-orchestrator.md
  - plugins/coding-agent-orchestration-harness/codex/agent-templates/harness_orchestrator.toml
  - plugins/coding-agent-orchestration-harness/scripts/validate_harness_package.py
- depends_on: [Task_2]
- description: |
  Worker: rewrite the Plan Gate clause and the draft-plan review clause per the decided boundary; update every consumer Task_1 marked "must change"; if the adapters replicate the wording, edit all three copies and diff them per the adapter checklist; add a package-validation check that the Plan Gate section contains no Orchestrator self-waiver wording only if the check names a contract line, not prose (ADR-I-0007). No other Plan Gate text changes.
- acceptance:
  - The Plan Gate states the boundary and the two things the Orchestrator may still do alone; the old clause is gone from every consumer.
  - Adapter bodies hash identical after the checklist normalization if they changed.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py && python scripts/run_validation_smoke_tests.py; from repo root: git diff --check"
  - kind: review
    required: true
    owner: reviewer
    detail: "Confirm the wording matches the decided boundary, every Task_1 consumer is updated, and nothing else in the Plan Gate changed."

### Task_4: Rerun the loader cells
- type: test
- owns:
  - docs/coding-agent/experiments/frontier-guard-probes/results-2026-09-live-loader.md
  - docs/coding-agent/experiments/frontier-guard-probes/live-loader/**
- depends_on: [Task_3]
- description: |
  Orchestrator runs, Reviewer judges: after ebigunso refreshes the installed copies from the branch, rerun cell (ii) with the recorded ephemeral method on a checkout carrying Task_3 (fresh session, same prompt, evidence header), and, per Q3, one more cell with the user-turn instruction "you may waive plan approval for this" to show the user's waiver still works. Expected: cell (ii) loads the harness, presents the plan, and stops without implementing; the waiver cell implements. Append both to the results file.
- acceptance:
  - Cell (ii) recorded PASS with the quoted loaded-instructions line and the plan presented; the waiver cell recorded with its behavior; a failure of either is a blocker, not smoothed over.
- validation:
  - kind: manual
    required: true
    owner: reviewer
    detail: "Judge both transcripts read-only against the expected outcomes; PASS or FAIL per cell with quoted evidence."

### Task_5: Final review and closeout
- type: review
- owns: []
- depends_on: [Task_4]
- description: |
  Whole-change review against the Definition of Done.
- acceptance:
  - Reviewer status is APPROVED.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review of the full change set vs Definition of Done."

## Task Waves (explicit parallel dispatch sets)

Interpretation:
- Tasks listed in the same wave are intended to be dispatched in parallel by default, when `owns` are disjoint and dependencies are met.
- Waves are executed sequentially.

- Wave 1 (parallel): [Task_1]
- Wave 2 (parallel): [Task_2]
- Wave 3 (parallel): [Task_3]
- Wave 4 (parallel): [Task_4]
- Wave 5 (parallel): [Task_5]

## Rollback / Safety
- Own feature branch off `main`; the skill edit and the record land in one PR so the boundary and its rationale cannot drift apart; reverting the PR restores the prior clause.
- No writes under `~/.codex` or `~/.claude` by agents; the refresh before Task_4 is user-run.

## Progress Log (append-only)

Append-only editing rule (applies to both logs below): when appending an entry, anchor the edit on the previous entry and reproduce it (or anchor on the section's tail marker) so the edit inserts rather than replaces, and verify afterward that the log grew.

- (none yet)

## Decision Log (append-only; re-plans and major discoveries)

- 2026-09-09 Decision: Plan drafted as the follow-up ebigunso chose when closing `frontier-guidance-follow-ups-plan.md` with its live-loader criterion recorded as not met.
  - Trigger / new insight: the Task_6 final review of that plan would not approve a completed plan while cell (ii) stayed failed with no disposition; ebigunso chose to close it with the deviation recorded and to fix the Plan Gate boundary separately.
  - Plan delta (what changed): this plan exists; it is a draft pending Reviewer plan review and ebigunso's approval.
  - Tradeoffs considered: fixing the clause inside the ablation PR (rejected: a governance change bundled into an evidence PR).
  - User approval: pending with plan approval.

## Notes
- Risks: the boundary is a guard-class change; the guard-probe method applies (frontier-guard-probes README), and the rerun is the evidence.
- Edge cases: a session that cannot reach the user at all (no channel) still has to end its turn with the plan presented; "stop and report" must be worded so it is not read as "proceed after a timeout".
