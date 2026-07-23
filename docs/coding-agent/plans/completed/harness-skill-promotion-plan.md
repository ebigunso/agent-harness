# Plan: Harness Skill Promotion — CharacterMemory/CharacterMemoryEvals Candidates (PR 2 of 2)

- status: done
- generated: 2026-07-23
- last_updated: 2026-07-23
- work_type: docs

## Goal
- Promote the surviving high-value improvement themes from the CharacterMemory / CharacterMemoryEvals staging surfaces into first-party harness skills, at the homes and with the wiring verified by the three-layer triage, trimmed by the 2026-07-23 Tier A value audit (bloat-averse cut list applied).

## Definition of Done
- All post-audit surviving items (see Normative scope) landed at their verified homes with required wiring (companion docs: `harness-skill-promotion-triage.md` for content evidence + homes; the value-audit cut list in this plan's Decision Log is authoritative where they conflict).
- Every newly added always-applied or event-triggered rule has an explicit mandatory route at its binding moment (triage Trigger-chain table; item A verified as already landed in v0.8.1, not re-added).
- Role-body edits stay byte-synchronized across the three runtimes; Codex AGENTS loader unchanged.
- Version 0.9.0 in all three manifests; full validator set green; Codex Reviewer APPROVED.

## Scope / Non-goals
- Scope: trimmed content additions and wiring in `plugins/coding-agent-orchestration-harness/`; lessons drain.
- Non-goals (cut by value audit, residuals noted): P3 producer/consumer reconciliation (already covered nearly verbatim by existing shards; residual metric-stage table → CME repo rules); P5c validator/fixture/smoke machinery for `design_alerts` (convention approach instead; revisit only if machine-parsed ruling automation is ever wanted); P5d adapter-body stop-alert text (absorbed into the single strengthened tripwire response sentence); P7 design-review and next-phase triggers + Plan-Gate lead-in rewording (duplicate existing Plan Gate and long-horizon-audit text); single h as a new runbook (2 lines into adapter-maintenance-checklist instead); P2 test-authoring cross-link and canary-producer bullet (latter → repo rule). Also unchanged non-goals: target-repo follow-ups; Orchestrator child-route normalization; triage KEEP REPO-LOCAL items.

## Context (workspace)
- Companion docs: `harness-skill-promotion-triage.md` (Rev 3 homes/evidence), `harness-trigger-audit-register.md` (wiring baseline, landed in v0.8.1 / PR #40).
- Value audit: Claude Tier A subagent, 2026-07-23 — per-item EARNS-ITS-PLACE/OVERSIZED/DELETE verdicts; cut list in Decision Log. Expensive-layer budget after cuts: ~8–10 always-read/adapter lines, no new validator code, no new fixture files.
- Repo reference docs consulted: rules suite rules-20260513-b80f05e; `improvement-loop/references/promotion-guidelines.md`; ADR-D-0007.

## Lessons folded in (2026-07-23)
- Atomic ruling persistence → one clause inside the P6 Escalation Ruling section.
- Adapter-preload baseline verification → single f line in `adapter-maintenance-checklist.md`.
- Owning-surface validation assertions → single g line in `testing-validation.md`.
- Line-bounded body-sync normalization → 2 lines in `adapter-maintenance-checklist.md` (folded single h).
- Spec-completeness before parallel authoring → single i line in `dispatch-checklists.md`.
- Value-audit meta-lesson (promotion triage needs a per-item existing-text diff step) → staged in `docs/coding-agent/lessons.md` at Task_5; NOT promoted in this PR (bloat discipline: one incident).

## Open Questions (max 3)
- None. (Q1 resolved 2026-07-23: user ruled no automation now, per the automation-last discipline; convention approach stands.)

## Assumptions
- A1: v0.8.1 wiring is the baseline; triage table item A (Worker/Reviewer EQB routes) is already landed — verify, don't re-add.
- A2: Minor version bump (0.9.0).

## Normative scope (post-audit)

### Task_1 (EQB cluster; Claude-authored)
1. P1 conservation shard `references/review-latent-risk-conservation.md` (~20 lines; totals-reconstruction and multi-failure sub-cases as single bullets) + router wiring in BOTH `review-latent-risk.md` surfaces + SKILL.md route-line phrase ("information conservation across serialization, conversion, aggregation, and fallback boundaries").
2. P2-enforcement: 4–5 bullets appended to the existing Checks list in `review-latent-risk-validation-tests.md` (rejection tests per nesting level incl. absent-field; independent-source comparison; compiler-enforced/generated exhaustiveness; paired-surface parity). No canary bullet, no test-authoring cross-link, no "matrix" framing.
3. P2 truth-table: one sentence under `architecture-gates.md` Gate 5 (for classification/attribution features, derive the full truth table before selecting the data model).
4. P4 + single b in one `review-latent-risk-contract-scope.md` edit: predecessor-obligation inventory for consolidations (3–4 lines) + cross-repo mirror seam-test line.
5. P5a (absorbs P5d): ONE new tripwire line in SKILL.md Drift Tripwires (trip when the fix goes around a type/schema/boundary/constraint this task could change) + strengthen the existing response sentence to carry stop-and-alert semantics (surface with the cleaner alternative and cost delta; do not proceed on the workaround without a ruling). No exception clause.
6. P7 appendix: 3–4 lines in `long-horizon-audit.md` mapping EARNS-ITS-PLACE/OVERSIZED/DELETE onto the existing challenge/delete/simplify outcomes, with the never-continuously clause.
7. Single a: one run-scoped-dependency-revision line in `review-latent-risk-build-ci.md`.
8. Single g: one owning-surface assertion line in `testing-validation.md` Evidence Integrity list.

### Task_2 (orchestration cluster; Claude-authored)
1. P6: "Escalation Ruling" section (~12 lines) in `lifecycle-gates.md` — two-tier threshold (routine vs contract-shape), blast-radius obligation, researcher-before-ruling, atomic Decision-Log persistence clause; + ONE imperative MUST-read hook with direct section anchor in `integration-checklist.md` at blocker/question aggregation (design alerts arrive through those channels per the convention below); + one consumer-obligation prompt line in `dispatch-checklists.md`.
2. P7 triggers (trimmed): third-bounce detector line in `integration-checklist.md`; pre-merge-after-churn trigger line in `completion-closeout.md`. No Plan-Gate lead-in rewording.
3. P8: new `subagent-strategy/references/model-routing.md` (~25–30 lines; capability-first: detail scrutiny/forensic vs altitude/lateral design/writing; review-tier, research-type, ADR-authorship routing; prose-quality rule as one line; one-platform fallback; version-agnostic) + one progressive-disclosure route line in subagent-strategy SKILL.md.
4. P5b: one dispatch-constraint escape-hatch line in `dispatch-checklists.md`.
5. design_alerts convention (replaces P5c machinery): a short paragraph in `subagent-report-contract/SKILL.md` defining a design alert as a structured `blockers`/`questions_for_orchestrator` entry (what is worked around / cleaner alternative / cost delta) + one collection line in `integration-checklist.md` step 5. No schema/validator/fixture changes.
6. Singles: c (evidenced-scope line, `rule-writing-style.md`); d (forensic-deliverable line, `dispatch-checklists.md`); e-trimmed (stopping rubric 3–4 lines in `pr-authoring.md`/`pr-review-monitoring.md`; one internal delta-review line at integration-checklist step 8; git-workflow frontmatter G-extension is already landed in v0.8.1 — verify only); i (spec-completeness line, `dispatch-checklists.md`).

### Task_3 (adapter + maintenance mechanics; Codex worker)
1. F wiring: conservation phrase added to the synchronized Reviewer risk-shape sentence in all three Reviewer bodies.
2. Single f + folded h: three lines total in `runtime-adapter-contract/references/adapter-maintenance-checklist.md` (preload-baseline verification; line-bounded connector-block normalization; pairwise hashes before treating mismatch as drift).
3. Verify (no re-add): triage items A and G already landed in v0.8.1.

## Tasks

### Task_1: Engineering-quality-baselines cluster
- type: impl
- owns:
  - plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/**
- depends_on: []
- description: |
  Apply Normative scope Task_1 items 1–8 exactly. Follow each target file's existing format; additions stay
  at the stated line budgets; no other content changes.
- acceptance:
  - Items 1–8 present at the named files within stated budgets
  - Conservation shard wired in both router surfaces and the SKILL.md route line
  - Exactly one new Drift Tripwire line; response sentence strengthened in place; no exception clause
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py && python scripts/run_validation_smoke_tests.py"

### Task_2: Orchestration cluster
- type: impl
- owns:
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/**
  - plugins/coding-agent-orchestration-harness/skills/subagent-strategy/**
  - plugins/coding-agent-orchestration-harness/skills/wave-integration/**
  - plugins/coding-agent-orchestration-harness/skills/rulebook/**
  - plugins/coding-agent-orchestration-harness/skills/git-workflow/**
  - plugins/coding-agent-orchestration-harness/skills/subagent-report-contract/SKILL.md
- depends_on: []
- description: |
  Apply Normative scope Task_2 items 1–6 exactly. The integration-checklist escalation hook is imperative
  (MUST + direct section anchor). model-routing.md is a new self-gating reference; persistent-peer-dispatch.md
  untouched. The design_alerts convention paragraph adds no schema fields.
- acceptance:
  - Items 1–6 present at the named files within stated budgets
  - Escalation hook and third-bounce detector are imperative, not routing-table nouns
  - No schema/validator/fixture changes anywhere
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py && python scripts/run_validation_smoke_tests.py"

### Task_3: Adapter and maintenance mechanics
- type: impl
- owns:
  - plugins/coding-agent-orchestration-harness/agents/**
  - plugins/coding-agent-orchestration-harness/claude/**
  - plugins/coding-agent-orchestration-harness/codex/**
  - plugins/coding-agent-orchestration-harness/skills/runtime-adapter-contract/**
- depends_on: [Task_1, Task_2]
- description: |
  Apply Normative scope Task_3: conservation phrase in the synchronized Reviewer risk sentence (three runtime
  copies, byte-sync preserved); three checklist lines in adapter-maintenance-checklist.md; verify triage items
  A and G are already present from v0.8.1 and report the verification (do not re-add). Codex AGENTS loader
  snippet unchanged.
- acceptance:
  - Reviewer bodies remain byte-synchronized (normalized pairwise-hash evidence)
  - Checklist lines present; A/G verification reported with citations; loader blob unchanged
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py && python scripts/run_validation_smoke_tests.py"
  - kind: manual
    required: true
    owner: worker
    detail: "Normalized three-runtime Reviewer body-sync comparison (pairwise hashes)"

### Task_4: Claude prose-quality pass over Codex-authored text
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/**
- depends_on: [Task_3]
- description: |
  Orchestrator (Claude) reviews the sentences added by the Codex worker in Task_3 (small surface: one risk-shape
  phrase ×3, three checklist lines) and rewords where warranted; semantics and sync preserved.
- acceptance:
  - Every Task_3-added sentence reviewed; sync intact after any rewording
- validation:
  - kind: command
    required: true
    owner: orchestrator
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py && python scripts/run_validation_smoke_tests.py"

### Task_5: Version 0.9.0, lessons drain, full validation
- type: chore
- owns:
  - plugins/coding-agent-orchestration-harness/.claude-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.codex-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.github/plugin/plugin.json
  - docs/coding-agent/lessons.md
- depends_on: [Task_4]
- description: |
  Bump 0.8.1 → 0.9.0. Drain promoted lessons from docs/coding-agent/lessons.md (entries now landed in skills),
  leaving repo-local ones; append the value-audit meta-lesson (promotion triage requires a per-item
  existing-text diff) as a repo lesson. Run the full common.md validator set.
- acceptance:
  - Manifests at 0.9.0; drain matches landed content 1:1; meta-lesson recorded; validator set green
- validation:
  - kind: command
    required: true
    owner: orchestrator
    detail: "All commands from docs/coding-agent/rules/common.md Repository-Specific Validation Commands"

### Task_6: Independent review (trigger-chain + budget bar)
- type: review
- owns: []
- depends_on: [Task_5]
- description: |
  Codex Reviewer at pinned commit: (1) item-by-item verification against this plan's Normative scope (the
  authoritative post-audit list) with file:line citations; (2) trigger-chain check: every new always/event rule
  has an explicit mandatory route at its binding moment; (3) budget check: no addition exceeds its stated line
  budget; no cut item reappeared; (4) three-runtime Reviewer body sync + loader immutability; (5) no weakened
  existing content; (6) independent validator rerun.
- acceptance:
  - Reviewer status APPROVED with per-item verdicts including budget compliance
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Content + trigger-chain + budget review at pinned commit with independent validator rerun"

## Task Waves (explicit parallel dispatch sets)

- Wave 1: [Task_1, Task_2]
- Wave 2: [Task_3]
- Wave 3: [Task_4]
- Wave 4: [Task_5]
- Wave 5: [Task_6]

(Wave 1: two parallel Claude harness-worker subagents — disjoint owns, spec-complete dispatch prompts.
Wave 2: Codex agmsg worker. Task_4 scope is small after cuts but retained per the standing prose-pass rule.)

## Rollback / Safety
- All changes on `feature/2026-07-23/harness-skill-promotion`; revert = drop branch. Inert plugin content.

## Progress Log (append-only)

- 2026-07-23 Plan drafted (post PR #40 merge, v0.8.1 baseline).
- 2026-07-23 Tier A value audit applied (Claude subagent); plan re-scoped per cut list; awaiting user approval before Wave 1 dispatch.
- 2026-07-23 Wave 1 completed: [Task_1, Task_2]
  - Summary: two parallel Claude harness-worker subagents; all 14 items landed within budgets; two integration rulings recorded at ruling time; orchestrator added the packet-menu conservation entry. Commit fcc808b.
  - Validation evidence: both workers' validators exit 0; independent orchestrator rerun on the combined tree exit 0.
- 2026-07-23 Wave 2 completed: [Task_3]
  - Summary: Codex agmsg worker; conservation phrase ×3 Reviewer bodies (pairwise hashes identical), three maintenance-checklist lines, A/G verified pre-landed, loader unchanged. Commit 1356eeb.
  - Validation evidence: validators exit 0; body-sync hash 39a9a4a3…; loader SHA-256 unchanged.
- 2026-07-23 Wave 3 completed: [Task_4]
  - Summary: Claude prose pass over all six Task_3 sentences — reviewed, no rewording warranted. Validators rerun exit 0.
- 2026-07-23 Wave 4 completed: [Task_5]
  - Summary: manifests 0.9.0; three promoted lessons drained with drain note; two meta-lessons appended. Commit 578131d.
  - Validation evidence: full common.md validator set green (all exit 0).
- 2026-07-23 Wave 5 completed: [Task_6]
  - Summary: Codex Reviewer APPROVED at pin 578131d, findings none — item-by-item citations for all 17 scope items, trigger-chain bar PASS, budget/cut/no-regression bar PASS (no cut item reappeared; line budgets exact), Reviewer body parity hash b75f98dd…, loader blob unchanged, drain 1:1, independent validator rerun all green.
- 2026-07-23 User approved the re-scoped plan ("You are go for implementation"); Q1 resolved — no design_alerts automation, per the automation-last discipline. Wave 1 dispatched.
- 2026-07-23 Ruling (Task_1 question): the reviewer-packet-template conservation menu entry from Rev 3 survives — it is a cheap reference-layer line keeping the packet menu consistent with the router. Applied by the Orchestrator at Wave 1 integration (the file sat in Task_2's owns while that worker ran).
- 2026-07-23 Ruling (Task_2 question): the Plan-Gate lead-in rewording stays cut. The triage table's item-E GAP row is partially superseded by the value audit: its design-review and next-phase triggers were deleted as duplicates, and the surviving third-bounce/pre-merge triggers are wired through integration-checklist and completion-closeout, which need no Plan-Gate rewording. Task_6 review checks the surviving wiring only.
- 2026-07-23 Note for Task_5: stage Task_2's pre-landed-wiring lesson candidate (re-baseline triage tables against the current tree before dispatch) in lessons.md alongside the value-audit meta-lesson.

## Decision Log (append-only; re-plans and major discoveries)

- 2026-07-23 Decision: "Verify catalog-provided skill paths" lesson stays repo-local (weak cross-repo generalization).
- 2026-07-23 Decision: Wave 1 = Claude subagents (content authoring); Wave 2 = Codex agmsg worker (mechanics); Task_4 covers only Codex-authored text.
- 2026-07-23 Decision: value-audit cut list applied (user-directed bloat audit; Claude Tier A subagent report).
  - Trigger: user directive — verify additions earn their place; cut low-value items aggressively.
  - Plan delta — DELETED: P3 (near-verbatim duplicate of existing entrypoints-admission/diagnostics/validation-tests text; residual metric-stage table → CME repo rules); P5c validator/fixture/smoke/schema machinery (~150 code lines; existing blockers/questions channels already validated and aggregated — replaced by a convention paragraph + one collection line); P5d adapter stop-alert text (~9 adapter-body lines restating the preloaded tripwire response; absorbed into one strengthened SKILL.md sentence); P7 design-review and next-phase triggers + Plan-Gate lead-in rewording (duplicate lifecycle-gates Plan Gate and long-horizon-audit Steps 1–2); single h as a new file (2 lines into adapter-maintenance-checklist; workspace-troubleshooting was a misfile); P2 test-authoring cross-link and canary-producer bullet (canary → repo rule).
  - Plan delta — TRIMMED: P5a to one tripwire line + strengthened response sentence; P2 truth-table to one Gate-5 sentence; P7 appendix to 3–4 mapping lines; single e internal delta path to one line; P1 shard sub-cases to single bullets.
  - Result: expensive always-read/adapter lines ~20 → ~8–10; no new code; two planned new files avoided; ~200–250 lines total avoided. Ranking retained in the audit report (agent transcript, 2026-07-23).
  - Tradeoffs: convention-based design_alerts loses machine validation — accepted absent an automation consumer (open question Q1 records the revisit condition).
  - User approval: audit user-directed; revised plan awaits explicit approval before dispatch.

## Notes
- Risks: P5a single-line wording must carry the boundary test without bloating the always-read block; Wave 1 dispatch prompts must be spec-complete (known parallel-authoring failure mode).
- Edge cases: `integration-checklist.md` is touched only by Task_2 now; Task_3 no longer touches wave-integration.
- 2026-07-23 Post-closeout addition (user-directed): the two Task_5 meta-lessons qualified as promotion candidates on re-check — the stale-derived-artifact class occurred three times in this workstream (keep-list mismatch, pre-landed GAP verdicts, redundant promotion items), so repeats-twice made promotion required. Landed as one line each in promotion-guidelines.md (Existing-text check; mandatory route via the v0.8.1 F7 fix) and dispatch-checklists.md (re-baseline audit tables; mandatory route via the B fix). Both applied their own rule: target files quoted, no existing coverage found. Lessons drained with drain-note update.
