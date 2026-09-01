# Plan: Compatibility-Stance and Test-Scope Guidance

- status: done
- generated: 2026-09-01
- last_updated: 2026-09-01
- work_type: docs

## Goal

- Shipped harness guidance stops rewarding two default behaviors: unrequested backwards-compatibility preservation, and over-constraining test suites (especially narrow mid-task regression tests).
- Both are corrected by one shared, operationalized rule — protection (a compat layer or a test assertion) is justified only by a locatable consumer/contract — enforced at scope-formation, implementation, and review checkpoints rather than by slogan alone.

## Definition of Done

- Core principles no longer read as "compatibility is always virtuous"; speculative compatibility is a named anti-pattern.
- The locatable-consumer test (locatable + within/out of reach + surface classification, unknown routes to the user) is defined once in shipped prose and referenced where needed, not restated divergently.
- Plan format requires a compatibility stance (`break | preserve | migrate | ask-user`) for work touching contracts/interfaces, justified by locatable consumers.
- test-authoring.md contains positive selection criteria (what earns a test), a necessity gate, placement guidance, and regression-generalization discipline, alongside the existing low-signal list.
- Reviewer rubric has both symmetric two-directional checks: unintended breakage vs. unrequested compat preservation; over-constrained tests vs. unguarded changed contracts.
- Package validators pass; plugin version bumped per release convention.

## Scope / Non-goals

- Scope: shipped plugin skill prose (`engineering-quality-baselines`, `plan-format`), one slim ADR for the maintenance invariant (not the policy norm), package validation, version bump.
- Non-goals:
  - No change to `subagent-report-contract` (per-test contract justification in Worker reports). Deliberately held back; revisit only if the reference + rubric changes prove insufficient.
  - No new reference documents; edits reshape existing files (guidance-volume creep is itself a drift risk).
  - No runtime-adapter edits (shared skill references are runtime-agnostic; role workflow/output contracts are not touched).
  - No repo-local rules (`docs/coding-agent/rules/*.md`) changes; this plan targets shipped guidance for consumer repos.

## Context (workspace)

- Related files/areas:
  - `plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/SKILL.md` (drift tripwires)
  - `plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/core-principles.md` (principle #1, anti-patterns)
  - `plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/test-authoring.md`
  - `plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/review-rubric.md`
  - `plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/review-latent-risk-contract-scope.md` and `review-latent-risk-validation-tests.md` (alignment check only)
  - `plugins/coding-agent-orchestration-harness/skills/plan-format/SKILL.md` and `references/plan-template.md`
  - `docs/coding-agent-orchestration-harness/decisions/` (ADR home)
- Existing patterns or references:
  - `docs/coding-agent/lessons.md` 2026-05-09 "Avoid Compatibility Wrappers Without Clear Need" (the prevention rule this plan promotes into shipped guidance)
  - Drift tripwires in `engineering-quality-baselines/SKILL.md` already use the "cannot name the consumer" pattern; new content extends it, does not fork it.
- Repo reference docs consulted: `docs/coding-agent/rules/common.md`, `plugins/coding-agent-orchestration-harness/README.md`.

## Design summary (agreed in discussion)

Operational definition (replaces the bare "named consumer" phrase, which is gameable):

- A consumer counts only if **locatable** — you can point at a call site, dependent repo, documented contract, or persisted data. Conceivable/categorical consumers ("downstream users", "external scripts may call this") do not count.
- The artifact being justified cannot be its own consumer (a test is not justified by the test suite; a shim is not justified by its own docs).
- **Reach**: a locatable consumer within the change's reach (same repo/task scope) is migration work, not a compat obligation. Only out-of-reach locatable consumers justify compat layers.
- **Surface classification** for the unverifiable case: repo-internal surfaces — absence of found consumers is real evidence, default migrate/break; boundary-crossing surfaces (published packages, network APIs, persisted/wire formats, externally invoked CLIs) — consumers presumed possible, default is neither silently preserve nor silently break: route the question to the user in the plan.

Test selection principle: a test earns its place when it would detect a **plausible defect** in **behavior someone depends on**, at the **cheapest boundary that observes it**. Positive criteria: contract boundaries; decision logic and edge values (representatives per equivalence class); invariants and failure paths; fixed bugs generalized to the violated contract. Non-earners: branchless glue, framework/stdlib behavior, config plumbing, contracts already guarded at a higher-value boundary. Completeness inverted from line coverage: "which plausible defect would ship undetected?" — per changed contract, is there a test that fails if it breaks?

Reviewer symmetry (both areas, both directions): flag unintended breakage AND unrequested compat preservation; flag tests a legitimate refactor would fail AND changed contracts left unguarded.

## Open Questions (max 3)

- (none — Q1 and Q2 resolved; see Decision Log)

## Assumptions

- A1: The locatable-consumer definition lives in full in one place (core-principles compatibility section) and is referenced by tripwire/rubric/plan-format wording rather than duplicated.
- A2: Version bump is a minor release (behavioral guidance change, no schema/contract change), following the existing `vX.Y.Z` commit convention.
- A3: `review-latent-risk-*` files need at most alignment tweaks (no contradiction with the new symmetric checks), not restructuring.

## Tasks

### Task_1: Slim ADR — design intent of evidence-justified protection

- type: design
- owns:
  - docs/coding-agent-orchestration-harness/decisions/
- depends_on: []
- description: |
  Draft one slim ADR (target: ~half a page) recording the design intent of the compat/test guidance, self-contained at intent altitude and independent of where the guidance is implemented.
  Intent to record: protection (a compatibility layer or a test assertion) must be justified by evidence of a demonstrable consumer/contract; justification may not be self-referential; unverifiable cases route to the user rather than defaulting in either direction.
  Rationale to record: (a) the attractor risk — future edits will tend to soften this back toward industry defaults ("compatibility is first-class", coverage-maximizing tests), and such reversal is the failure mode being defended against, not a cleanup; (b) gameability of weaker formulations (categorical/hypothetical "named" consumers; artifacts justifying themselves); (c) rejected alternatives, including the held-back subagent-report-contract per-test justification with its revisit condition (adopt only if reference + rubric changes prove insufficient).
  Do NOT mirror the shipped implementation wording (operational bullets, phrasing, examples); implementation locations may appear at most as a non-authoritative side note. The record must read standalone and remain valid under any rewording of the shipped prose that preserves the intent.
  Follow durable-docs-authoring and existing ADR numbering/sections.
- acceptance:
  - ADR states the design intent completely and self-containedly; no clause depends on a reader having the shipped prose, and no implementation pointer is load-bearing.
  - ADR does not mirror implementation wording; it stays at intent altitude such that legitimate rewording of shipped prose does not invalidate it.
  - ADR records the attractor/gameability rationale, rejected alternatives, and the held-back report-contract option with its revisit condition.
  - ADR matches existing corpus conventions (numbering, sections) and stays near half a page.
- validation:
  - kind: review
    required: true
    owner: orchestrator
    detail: "Intent-altitude check: self-contained, implementation-independent, no mirrored wording; warrant criteria check per durable-docs-authoring."

### Task_2: Core principles + drift tripwire (compatibility)

- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/core-principles.md
- depends_on: []
- description: |
  Reword principle #1: stability is owed to consumers that exist; preserving surfaces with no locatable consumer is scope creep, not safety. House the full locatable-consumer definition here (per A1).
  Add "speculative compatibility" to Common Anti-Patterns (shims, wrappers, dual code paths, deprecation layers for unlocatable consumers).
  Add one drift tripwire to SKILL.md: trip when adding a compatibility shim/wrapper/dual path for a consumer you cannot locate.
- acceptance:
  - Principle #1 no longer reads as unconditional compat preservation; accidental-breakage protection is retained.
  - Definition appears once, in full, with reach + surface classification + self-reference exclusion.
  - New tripwire uses the existing tripwire voice and length; no other tripwires altered.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "python scripts/validate_harness_package.py (from plugins/coding-agent-orchestration-harness/)"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review vs acceptance; check no consumer-facing text references docs/ paths absent from the package."

### Task_3: Test-authoring reshape (positive criteria + necessity gate)

- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/test-authoring.md
- depends_on: []
- description: |
  Reshape into: selection principle (plausible defect x depended-on behavior x cheapest observing boundary) -> what earns a test (four positive criteria) -> non-earners -> necessity gate ("would anything other than this test observe the difference?") -> placement (one contract, one boundary) -> regression discipline (generalize to the violated contract; one test per contract, not per symptom) -> existing Low-Signal Surfaces and Contract Exception sections retained.
  Add the inverted completeness check: per changed contract, a test that fails if it breaks.
- acceptance:
  - All existing content (anchor heuristic, low-signal list, contract exception) survives, possibly repositioned.
  - Positive criteria and necessity gate use the locatable-consumer/contract framing consistent with Task_2 wording.
  - Document stays a single compact reference (no split, no new file).
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "python scripts/validate_harness_package.py (from plugins/coding-agent-orchestration-harness/)"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review vs acceptance; adversarial pass: can a model satisfy the gate with a self-referential or categorical justification?"

### Task_4: Reviewer rubric symmetric checks

- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/review-rubric.md
  - plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/review-latent-risk-contract-scope.md
  - plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/review-latent-risk-validation-tests.md
- depends_on: []
- description: |
  Add the two two-directional checks to the rubric: (a) unintended breakage vs. unrequested compat preservation (compat layers must map to locatable out-of-reach consumers); (b) over-constrained tests (legitimate refactor would fail them) vs. unguarded changed contracts.
  Latent-risk files: alignment-only pass per A3 — remove or reword anything that contradicts the symmetric checks; do not restructure.
- acceptance:
  - Rubric contains both symmetric checks, phrased so neither direction can be satisfied by defaulting.
  - Latent-risk references do not contradict the new checks; diffs there are minimal or empty.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "python scripts/validate_harness_package.py (from plugins/coding-agent-orchestration-harness/)"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review vs acceptance criteria."

### Task_5: Plan-format compatibility stance

- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/plan-format/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/plan-format/references/plan-template.md
  - plugins/coding-agent-orchestration-harness/skills/plan-format/references/examples.md
- depends_on: []
- description: |
  Add a core rule and template section: plans touching a contract/interface/persisted format declare a compatibility stance (break | preserve | migrate | ask-user) justified by locatable consumers; boundary-crossing surfaces with unverifiable consumers default to ask-user.
  Placement per Q1 resolution (proposed: plan-level section, per-task notes only when stances differ). Update one example to show a filled stance.
  No validator (validate_plan.py) changes unless Q1 resolves to per-task required field.
- acceptance:
  - Core rules and template carry the stance section with the four values and the justification requirement.
  - Wording defers to the definition owned by core-principles rather than restating it in full.
  - At least one example demonstrates a non-trivial stance (e.g., migrate with a locatable in-repo consumer).
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "python skills/plan-format/scripts/validate_plan.py --file tests/fixtures/valid-plan.md --mode balanced (from plugins/coding-agent-orchestration-harness/) — confirm existing fixtures still pass"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review vs acceptance criteria."

### Task_6: Integration review, package validation, version bump

- type: review
- owns:
  - plugins/coding-agent-orchestration-harness/.claude-plugin/
  - plugins/coding-agent-orchestration-harness/README.md
- depends_on: [Task_2, Task_3, Task_4, Task_5]
- description: |
  Cross-file coherence pass: the locatable-consumer definition appears in full exactly once; tripwire, rubric, plan-format wording reference it consistently; no shipped text references non-packaged docs/ paths.
  Run full package validators; bump plugin version (minor) per release convention; update README only if it enumerates the changed sections.
- acceptance:
  - Reviewer status is APPROVED on the combined diff.
  - All package validators pass.
  - Version bumped consistently with the existing release convention.
- validation:
  - kind: command
    required: true
    owner: reviewer
    detail: "python scripts/validate_harness_package.py && python scripts/run_validation_smoke_tests.py (from plugins/coding-agent-orchestration-harness/)"
  - kind: review
    required: true
    owner: reviewer
    detail: "Combined diff review: single-source definition, consistent cross-references, symmetric checks present, no consumer-facing maintainer notes."

## Task Waves (explicit parallel dispatch sets)

Interpretation:

- Tasks listed in the same wave are intended to be dispatched in parallel by default, when `owns` are disjoint and dependencies are met.
- Waves are executed sequentially.

- Wave 1 (parallel): [Task_1, Task_2, Task_3, Task_4, Task_5]
- Wave 2 (parallel): [Task_6]

## Rollback / Safety

- Docs-only change set; revert is a clean `git revert` of the release commit(s).
- No runtime schemas, validators, or adapters change (unless Q1 flips to per-task field, which would add validator scope to Task_5 and this section).

## Progress Log (append-only)

- 2026-09-01 Wave 1 completed: [Task_1, Task_2, Task_3, Task_4, Task_5]
  - Summary: ADR-D-0016 created (orchestrator review: pass — intent altitude, no mirrored wording, warrant with mode+cost). core-principles #1 reworded with full locatable-consumer definition + speculative-compatibility anti-pattern + one new drift tripwire. test-authoring reshaped (selection principle, positive criteria, necessity gate, placement, regression discipline, inverted completeness check; all prior content retained). review-rubric gained Symmetric Checks section; latent-risk files verified non-contradicting, unchanged. plan-format gained core rule 8 (compatibility stance), template section, and a filled migrate example; former rule 8 renumbered to 9.
  - Validation evidence: validate_harness_package.py pass (Tasks 2, 3, 4); validate_plan.py on valid-plan.md fixture pass (Task_5); orchestrator ADR review pass (Task_1).
  - Notes: definition single-sourced in core-principles (verified in integration diff read). For Task_6 reviewer: rubric additions hard-wrap mid-sentence vs one-line-per-sentence convention; confirm no stale references to renumbered plan-format rules.

- 2026-09-01 Wave 2 completed: [Task_6]
  - Summary: Reviewer verdict CHANGES_REQUIRED on two trivial items only, all substantive acceptance criteria met (single-source definition verified by grep; symmetric checks non-defaultable; no non-packaged docs/ references; latent-risk evidence clean in both routed categories, including the confident-breakage adversarial read). Orchestrator applied the fixes: review-rubric.md unwrapped to one sentence per line; version bumped 0.12.0 -> 0.13.0 across all three runtime manifests (.claude-plugin, .github/plugin, .codex-plugin — cross-manifest check caught the single-file bump). Review converts to APPROVED per reviewer's stated condition (no substantive re-review required).
  - Validation evidence: validate_harness_package.py pass post-fixes; run_validation_smoke_tests.py exit 0; git diff --check clean (reviewer run); README confirmed not to enumerate changed sections, no update needed.
  - Notes: test-authoring.md LF endings left for git autocrlf normalization at commit (reviewer: optional/harmless).

## Decision Log (append-only; re-plans and major discoveries)

- 2026-09-01 Decision: Hold back subagent-report-contract per-test justification.
  - Trigger / new insight: strongest forcing function, but adds ceremony to a load-bearing schema; reference + rubric changes may suffice.
  - Plan delta (what changed): recorded as non-goal with revisit condition.
  - Tradeoffs considered: enforcement strength vs. report-schema churn.
  - User approval: yes (discussion, 2026-09-01)

- 2026-09-01 Decision: Q1 resolved — compatibility stance is a plan-level section.
  - Trigger / new insight: user accepted the proposed lighter placement.
  - Plan delta (what changed): Task_5 keeps no-validator-change scope; per-task notes only when stances differ.
  - Tradeoffs considered: per-task required field is more validator-enforceable but adds schema churn.
  - User approval: yes (discussion, 2026-09-01)

- 2026-09-01 Decision: Q2 resolved — slim ADR scoped to the maintenance invariant, not the policy.
  - Trigger / new insight: user's bar — ADRs must have standing effect on future work, not serve as history. The policy norm's standing effect flows through shipped prose; the durable slice is the re-litigation risk (future edits softening defensive wording back toward industry defaults) plus the held-back report-contract option, and common.md bars maintainer rationale from plugins/, leaving decisions/ as its designated home.
  - Plan delta (what changed): Task_1 reshaped (invariant-scoped, ~half page, no policy restatement); Task_2–Task_5 dependencies on Task_1 dropped as artificial; waves flattened to two.
  - Tradeoffs considered: lessons.md entry (frames continuous pressure as a one-off mistake; corpus is what durable-docs-authoring routes editors to); full policy ADR (duplicates shipped prose — history log).
  - User approval: yes (discussion, 2026-09-01)

- 2026-09-01 Decision: ADR content principle — intent altitude, not norm deferral.
  - Trigger / new insight: user ruling — ADRs capture design intent, which holds regardless of implementation location; shipped normative prose is implementation (same as code) and never a substitute record for intent. Implementation pointers are at most non-authoritative side notes.
  - Plan delta (what changed): Task_1 re-anchored from "maintenance invariant with pointer to prose-owned norm" to "self-contained intent record"; acceptance criteria replaced (no load-bearing pointers, no mirrored wording, valid under intent-preserving rewording).
  - Tradeoffs considered: deferral-based minimality (rejected: makes a pointer load-bearing, creating referent-rot and standalone-readability costs; intent altitude achieves drift-resistance without them).
  - User approval: yes (discussion, 2026-09-01)

## Notes

- Risks:
  - Overcorrection: models reading "compat preservation is scope creep" may break boundary-crossing surfaces confidently; the surface classification and ask-user default are the mitigation — reviewer of Task_2 should adversarially read for this.
  - Definition drift across the five touched files if workers paraphrase instead of referencing; Task_6 exists to catch this.
- Edge cases:
  - Repos consuming the harness that ARE published libraries: nearly every surface is boundary-crossing; the guidance must not make ask-user so frequent it becomes noise. Task_2 wording should scope the classification to the surface actually being changed.
