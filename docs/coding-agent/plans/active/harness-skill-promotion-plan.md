# Plan: Harness Skill Promotion — CharacterMemory/CharacterMemoryEvals Candidates (PR 2 of 2)

- status: draft
- generated: 2026-07-23
- last_updated: 2026-07-23
- work_type: docs

## Goal
- Promote the eight consolidated improvement themes (P1–P8) plus verified singles from the CharacterMemory / CharacterMemoryEvals staging surfaces into first-party harness skills, at the homes and with the wiring verified by the three-layer triage (categorization → reference homes → trigger chains), on top of the v0.8.1 corrected wiring.

## Definition of Done
- All P1–P8 themes and in-scope singles landed at their Rev 3 verified homes with their required wiring (companion doc: `harness-skill-promotion-triage.md`, same folder — the normative content spec).
- Every newly added always-applied or event-triggered rule satisfies the acceptance bar: an explicit mandatory route at its binding moment, never semantic-selection reliance (triage doc, Trigger-chain verification table items A–H).
- `design_alerts` is a validated, consumed report field (contract prose + schema sample + validator + fixtures + smoke entries + wave-integration collection step) — not a documentation-only key.
- Role-body edits stay byte-synchronized across the three runtimes; Codex AGENTS loader unchanged.
- Version 0.9.0 in all three manifests; full validator set green; Codex Reviewer APPROVED.

## Scope / Non-goals
- Scope: new/extended reference content and wiring in `plugins/coding-agent-orchestration-harness/` per the companion triage doc; the four 2026-07-23 lessons folded in (see Lessons folded in); drain of the harness repo's own promotable lessons.
- Non-goals: target-repo follow-ups (marking HMC entries promoted, draining CM/CME lessons, slimming their now-duplicated rules) — separate post-merge work in those repos; Orchestrator child-route normalization (still deferred); repo-local items listed KEEP REPO-LOCAL in the triage.

## Context (workspace)
- Normative content spec: `docs/coding-agent/plans/active/harness-skill-promotion-triage.md` (Rev 3: homes + wiring fixes per item).
- Wiring-state baseline: v0.8.1 (PR #40) — the existing-content fixes in `harness-trigger-audit-register.md` are already landed; PR 2 adds only its own new wiring (conservation risk shape, escalation-ruling hook, value-audit triggers, design_alerts chain, model-routing route).
- Repo reference docs consulted: rules suite rules-20260513-b80f05e; `improvement-loop/references/promotion-guidelines.md`; ADR-D-0007.

## Lessons folded in (2026-07-23, PR 1 execution)
- Atomic ruling persistence → P6 escalation-ruling section text: delivering an escalation ruling and recording it in the plan Decision Log are one atomic action.
- Adapter-preload baseline verification → runtime-adapter-contract `adapter-maintenance-checklist.md`: verify frontmatter/preload baselines against actual files before encoding keep/remove lists in plans; distinguish removal authorization from descriptive audit context.
- Scope validation assertions to their owning surface → `engineering-quality-baselines/references/testing-validation.md` one line: frontmatter-trigger assertions check frontmatter, body-route assertions check their section; whole-file occurrence counts false-fail.
- Line-bounded adapter body-sync normalization → new `workspace-troubleshooting/references/adapter-body-sync.md` runbook + SKILL.md routing line (runbook precedent per v0.7.1).
- Also drained from harness lessons.md (2026-07-16): complete contract specs before parallel authoring → `subagent-strategy/references/dispatch-checklists.md` line. ("Verify catalog-provided skill paths" stays a repo lesson — weak cross-repo generalization; rationale recorded here.)

## Open Questions (max 3)
- None; content spec is the companion triage doc plus the exact-wording authority delegated to the drafting tasks below (Claude-authored, per model routing).

## Assumptions
- A1: v0.8.1 wiring is the baseline; no PR 1 regressions.
- A2: Version bump is minor (0.9.0): new content surface.

## Tasks

### Task_1: Engineering-quality-baselines cluster (P1–P4, P5a, P7 appendix, singles a/b/g)
- type: impl
- owns:
  - plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/**
- depends_on: []
- description: |
  Author and land, per the triage doc's verified homes: (P1) new `references/review-latent-risk-conservation.md`
  + router risk-shape and conditional-route wiring in `review-latent-risk.md` + SKILL.md routing-line addition
  ("information conservation across serialization, conversion, aggregation, and fallback boundaries");
  (P2) enforcement-evidence matrix in `review-latent-risk-validation-tests.md`, truth-table-before-data-model in
  `architecture-gates.md` (Gate 4/5), cross-link in `test-authoring.md`; (P3) exact-semantic-action-set +
  rejected-candidate regression in `review-latent-risk-entrypoints-admission.md`, metric-stage cardinality and
  disabled-path-no-work in `review-latent-risk-diagnostics.md`; (P4) predecessor-obligation inventory in
  `review-latent-risk-contract-scope.md`; (P5a) Workaround Tripwire as a fourth always-active Drift Tripwire in
  SKILL.md (boundary/constraint test + alert-and-wait response; immutable-boundary exception generalized, no
  named sealed-artifact rule); (P7) EARNS-ITS-PLACE/OVERSIZED/DELETE trigger/verdict appendix in
  `long-horizon-audit.md` mapped onto the existing five-step outcomes; singles: run-scoped dependency revision
  in `review-latent-risk-build-ci.md` (a), cross-repo mirror seam test in `review-latent-risk-contract-scope.md` (b),
  owning-surface validation-assertion line in `testing-validation.md` (g).
- acceptance:
  - All listed items present at the exact files named, with evidence-derived content per the triage doc entries
  - New conservation shard wired in BOTH router surfaces (risk-shape list and conditional-reference table) and the SKILL.md route line
  - No weakening of existing content; additions follow each file's existing format (checklist shards stay checklist-shaped)
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py && python scripts/run_validation_smoke_tests.py"

### Task_2: Orchestration cluster (P6, P7 triggers, P8, P5b, singles c/d/e/i)
- type: impl
- owns:
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/**
  - plugins/coding-agent-orchestration-harness/skills/subagent-strategy/**
  - plugins/coding-agent-orchestration-harness/skills/wave-integration/**
  - plugins/coding-agent-orchestration-harness/skills/rulebook/**
  - plugins/coding-agent-orchestration-harness/skills/git-workflow/**
- depends_on: []
- description: |
  Author and land: (P6) new "Escalation Ruling" section in `orchestration-harness/references/lifecycle-gates.md`
  (two-tier threshold, blast-radius obligation, researcher-before-ruling, atomic Decision-Log persistence per the
  folded lesson) + imperative MUST-read hook with direct section anchor in
  `wave-integration/references/integration-checklist.md` at blocker/question/design_alert aggregation + prompt-side
  consumer-obligation line in subagent-strategy; (P7 triggers) design-review/third-bounce/next-phase triggers in
  `lifecycle-gates.md`, third-bounce detector in `integration-checklist.md`, pre-merge-after-churn trigger in
  `completion-closeout.md`, explicit never-continuous non-trigger; (P8) new
  `subagent-strategy/references/model-routing.md` — capability-first table (detail scrutiny/forensic vs
  altitude/lateral design/writing), review-tier and research-type and ADR-authorship routing, the prose-quality
  rule (detail-model text gets a writing-model rewording pass), one-platform fallback, version-agnostic wording —
  + progressive-disclosure route in subagent-strategy SKILL.md; (P5b) dispatch-constraint escape hatch in
  `dispatch-checklists.md`; singles: evidenced-scope line in `rulebook/references/rule-writing-style.md` (c),
  forensic-deliverable refinement line in `dispatch-checklists.md` (d), external-review stopping rubric in
  `git-workflow/references/pr-authoring.md` + risk-gated internal delta-review path in `integration-checklist.md` (e),
  complete-contract-specs-before-parallel-authoring line in `dispatch-checklists.md` (i).
- acceptance:
  - All listed items present at the named files; escalation hook and third-bounce detector are imperative (MUST + direct reference), not routing-table nouns
  - model-routing.md reachable via a new explicit progressive-disclosure line; persistent-peer-dispatch.md untouched
  - No weakening of existing content; wave-integration/lifecycle-gates additions align with their v0.8.1 imperative style
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py && python scripts/run_validation_smoke_tests.py"

### Task_3: design_alerts chain + adapter and troubleshooting work (P5c/P5d, F wiring, singles f/h)
- type: impl
- owns:
  - plugins/coding-agent-orchestration-harness/skills/subagent-report-contract/**
  - plugins/coding-agent-orchestration-harness/skills/runtime-adapter-contract/**
  - plugins/coding-agent-orchestration-harness/skills/workspace-troubleshooting/**
  - plugins/coding-agent-orchestration-harness/skills/wave-integration/references/integration-checklist.md
  - plugins/coding-agent-orchestration-harness/agents/**
  - plugins/coding-agent-orchestration-harness/claude/**
  - plugins/coding-agent-orchestration-harness/codex/**
  - plugins/coding-agent-orchestration-harness/tests/**
- depends_on: [Task_1, Task_2]
- description: |
  (P5c) `design_alerts` as a first-class validated Worker-report field: contract prose in
  subagent-report-contract SKILL.md (what is worked around, cleaner alternative, cost delta; alert-and-wait),
  schema sample in `references/schema.yaml`, validation function wired into
  `scripts/validate_worker_report.py`, valid/invalid fixtures, smoke-test entries in
  `run_validation_smoke_tests.py`, collection/ruling step in `integration-checklist.md` (extending Task_2's
  escalation hook, sequenced after it). (P5d) synchronized Worker mid-task stop-alert-await text in all three
  Worker bodies; (F wiring) conservation risk shape added to the synchronized Reviewer trigger sentence in all
  three Reviewer bodies; (single f) preload-baseline verification item in
  `runtime-adapter-contract/references/adapter-maintenance-checklist.md`; (single h) new
  `workspace-troubleshooting/references/adapter-body-sync.md` runbook (line-bounded connector-block
  normalization, pairwise hashes before treating mismatch as content failure) + SKILL.md routing line.
  Codex AGENTS loader snippet unchanged.
- acceptance:
  - An unknown-shape design_alerts entry FAILS validation; a well-formed one passes; both proven by fixtures + smoke entries
  - Worker/Reviewer bodies remain byte-synchronized across runtimes (normalized comparison per adapter-body-sync runbook)
  - All named files changed; loader snippet blob-identical to branch point
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py && python scripts/run_validation_smoke_tests.py && python skills/subagent-report-contract/scripts/validate_worker_report.py --file tests/fixtures/valid-worker-report.yaml"
  - kind: manual
    required: true
    owner: worker
    detail: "Normalized three-runtime body-sync comparison evidence (pairwise hashes) for Worker and Reviewer bodies"

### Task_4: Claude prose-quality pass over Codex-authored text
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/**
- depends_on: [Task_3]
- description: |
  Orchestrator (Claude) reviews every sentence added or reworded by the Codex worker in Task_3 and rewords for
  quality where warranted; semantics, imperative force, and three-runtime sync preserved. (Task_1/Task_2 text is
  Claude-authored and needs no pass.)
- acceptance:
  - Every Task_3-added sentence reviewed; any rewording keeps validation fixtures passing and body sync intact
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
  Bump 0.8.1 → 0.9.0 in the three manifests. Drain promoted lessons from `docs/coding-agent/lessons.md`
  (v0.7.1 precedent): remove entries now landed in skills (spec-completeness, the three 2026-07-23 candidates,
  atomic-ruling), leaving repo-local ones with a promoted-note. Run the full common.md validator set.
- acceptance:
  - Manifests at 0.9.0; drained lessons match landed content 1:1; validator set green
- validation:
  - kind: command
    required: true
    owner: orchestrator
    detail: "All commands from docs/coding-agent/rules/common.md Repository-Specific Validation Commands"

### Task_6: Independent review (trigger-chain acceptance bar)
- type: review
- owns: []
- depends_on: [Task_5]
- description: |
  Codex Reviewer at pinned commit: (1) item-by-item content verification against the companion triage doc
  (P1–P8, singles a–i, folded lessons) with file:line citations; (2) trigger-chain verification of every newly
  added always-applied/event-triggered rule against the acceptance bar — explicit mandatory route at the binding
  moment, per triage table items A–H; (3) design_alerts negative/positive fixture behavior; (4) three-runtime
  body sync + loader immutability; (5) no weakened existing content; (6) independent validator rerun.
- acceptance:
  - Reviewer status APPROVED
  - Explicit per-item verdicts including the A–H wiring items
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Content + trigger-chain + schema-behavior review at pinned commit with independent validator rerun"

## Task Waves (explicit parallel dispatch sets)

- Wave 1: [Task_1, Task_2]
- Wave 2: [Task_3]
- Wave 3: [Task_4]
- Wave 4: [Task_5]
- Wave 5: [Task_6]

(Wave 1 runs Task_1 and Task_2 in parallel as Claude harness-worker subagents — disjoint owns, Claude-authored
prose per model routing. Wave 2 goes to the Codex worker via agmsg — validator/fixture/adapter mechanics.
Dispatch prompts must carry complete contract specs — the folded spec-completeness lesson.)

## Rollback / Safety
- All changes on `feature/2026-07-23/harness-skill-promotion`; revert = drop branch. Inert plugin content; no runtime installs.

## Progress Log (append-only)

- 2026-07-23 Plan drafted (post PR #40 merge, v0.8.1 baseline); awaiting user approval before Wave 1 dispatch.

## Decision Log (append-only; re-plans and major discoveries)

- 2026-07-23 Decision: "Verify catalog-provided skill paths" lesson stays repo-local (weak cross-repo generalization); all other open lesson candidates fold into PR 2 content.
- 2026-07-23 Decision: Wave 1 uses Claude harness-worker subagents (content authoring = writing-strength work); Wave 2 uses the Codex agmsg worker (validator/fixture/adapter mechanics = detail-strength work); Task_4 pass covers only Codex-authored text.

## Notes
- Risks: P5a Drift-Tripwire wording must stay compact (always-read budget); design_alerts validator changes must keep existing fixtures passing; parallel Wave 1 requires both dispatch prompts to be spec-complete to avoid divergent invention (known failure mode).
- Edge cases: integration-checklist.md is touched by Task_2 (Wave 1) and Task_3 (Wave 2) — sequential waves make that safe; Task_3 extends, never rewrites, Task_2's hook.
