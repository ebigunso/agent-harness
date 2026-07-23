# Harness Promotion Triage — CharacterMemory + CharacterMemoryEvals

Date: 2026-07-23. Prepared by agent-harness-orchestrator.
**Rev 4 (2026-07-23): Tier A value audit applied.** A user-directed bloat audit (Claude Tier A subagent) issued per-item EARNS-ITS-PLACE/OVERSIZED/DELETE verdicts. The authoritative post-audit scope is the plan's Normative scope section (`harness-skill-promotion-plan.md`); where this document and the plan conflict, the plan wins. Headline cuts: P3 deleted (already covered nearly verbatim by existing shards); P5c validator machinery deleted (convention approach); P5d adapter text deleted (absorbed into one strengthened tripwire sentence); P7 halved (only third-bounce and pre-merge-after-churn triggers survive); single h folded into adapter-maintenance-checklist; P5a/P2/P1 trimmed to stated line budgets. Audit meta-lesson: promotion triage must include a per-item existing-text diff before scheduling — three items survived two triage revisions while restating text already present in their exact target files.
**Rev 2 (2026-07-23): proposed homes re-verified against real loading patterns** — orchestrator altitude pass (disclosure layer: always-read vs reference, which role loads what, when) + Codex researcher detail verification with file:line citations (agmsg report 2026-07-23T07:23Z). Home lines below are the verified map; changes from Rev 1 are marked **[revised]**. Governing principle from the verification: guidance must be in context at the moment its failure mode occurs — a rule living only in a reference that is never re-entered at that moment is dormant.
Inputs: Codex forensic scans of both repos (332 items total), Claude inventory of the harness (17 skills, v0.8.0), and the harness's own promotion criteria (`improvement-loop/references/promotion-guidelines.md`, `rulebook/references/skill-candidates-file.md`, ADR-D-0007).

## What was scanned

| Source | Items |
|---|---|
| CharacterMemory `skill-candidates.md` | 13 staged HMC candidates |
| CharacterMemory `lessons.md` | 54 lessons |
| CharacterMemory `rules/*.md` | 43 rules |
| CharacterMemory `FOLLOWUP-SEED.md` / `HANDOFF.md` | 72 follow-up notes |
| CharacterMemoryEvals `lessons.md` | 55 lessons |
| CharacterMemoryEvals `rules/*.md` | 95 rules |

Raw per-item inventories with assessments: `scan-CharacterMemory.md`, `scan-CharacterMemoryEvals.md` (scratchpad).

Promotion criteria applied (from the harness itself): reusable across repos with a durable skill/reference owner → promote; behavior constraint tied to repo facts → repo rule; **repeats twice → promotion required, not optional**. Promotion precedent (v0.7.1): smallest durable unit — append a line to an existing reference where possible; new reference file only for a full symptom→cause→steps body; drain promoted staging entries afterward.

## PROMOTE — 8 consolidated work items

Many staged items are the same failure class observed repeatedly across both repos; they promote as themes, not one-to-one. Every item below has multi-incident evidence and no existing harness coverage (grep-verified).

### P1. Lossless-boundary conservation review
- Evidence: HMC 2026-07-22 lossless-boundary (~15 Copilot findings across CM #63–65, CME #15); CME lessons on reconstruction context, duplicate-contract joins; "compare full observable contract" recurred independently in BOTH repos (CM lesson 2026-07-21, CME LESSON-55).
- Content: per-boundary conservation audit — every consumed field reaches output or has recorded intentional drop; classifications retain their discriminant; breakdowns reconstruct their totals; multi-failure paths capture all causes order-independently; fallback arms carry no less data than primary.
- Home (verified): new `engineering-quality-baselines/references/review-latent-risk-conservation.md`, wired into BOTH the router's risk-shape list and conditional-reference table (`review-latent-risk.md`) — an unwired shard is unreachable; the package validator checks shard existence but not routing. Also add a conservation hint to `wave-integration/references/reviewer-packet-template.md`'s latent-risk menu. Content: concrete conservation method only — `core-principles.md` already owns the general no-silent-field-loss principle; don't restate it.

### P2. Enforcement-claim negative evidence + attribution truth tables
- Evidence: 6 of the 13 HMC entries (truth-table testing, data-model-after-truth-table, labels-are-not-invariants, positive+zero rows per category, negative evidence for enforcement claims) plus CME lessons (public readers as admission boundaries, exact-set both directions, per-branch tamper coverage). Largest single evidence pool.
- Content: every enforcement claim ("strict", "fail-closed", "exhaustive", "canary") ships rejection tests per level including nested; comparisons use independent sources; exhaustiveness is compiler-enforced or generated; canaries bind to the real producer; for attribution/classification features, derive the full truth table (positive, forbidden, permutation, side-branch rows) BEFORE choosing the data model.
- Home **[revised — split]**: enforcement-claim negative evidence (rejection per level, independent sources, compiler-enforced exhaustiveness, real-producer canaries) → compact enforcement matrix in `review-latent-risk-validation-tests.md`. But "derive the truth table BEFORE choosing the data model" → `architecture-gates.md` (Gate 4/5, explicit contracts/invariants): test-authoring is loaded while writing tests — too late for a design-time rule. `test-authoring.md` gets only a cross-link/assertion-level rows.

### P3. Producer/consumer set reconciliation for diagnostics
- Evidence: HMC rounds 6, 7, 10 (producer-set vs final-eligible-set, cost-gate table + staged cardinality binding, semantic action set / phase-dependent depth).
- Content: telemetry computed before filtering/admission must be reconciled against the final eligible set; optional diagnostics prove the disabled path does no work; every metric binds to exactly one named stage in a chained-limiter cardinality table.
- Home **[revised — split]**: primary is `review-latent-risk-entrypoints-admission.md` — it already owns candidate-vs-accepted set distinctions and is routed whenever data is filtered/admitted/counted/emitted; extend it with "exact semantic action set" and the rejected-candidate regression. `review-latent-risk-diagnostics.md` keeps only the metric-specific parts (named-stage cardinality binding, disabled-path-does-no-work); hot-path cost routes to the performance shard when material.

### P4. Consolidation completeness contract
- Evidence: HMC 2026-07-22 (4 Copilot findings — lost timeout, deleted test suite, lost export format, unextended mock).
- Content: consolidation acceptance requires a predecessor-obligation inventory (behaviors, config values, validation, formats, tests, mirror surfaces), each item carried or intentionally-dropped-with-reason; reviewers verify against each deleted implementation.
- Home **[revised]**: the reviewer-side inventory goes in `review-latent-risk-contract-scope.md` (already compares fake/prod, old/new, fallback/primary implementations of one contract) — NOT review-rubric, whose format contract explicitly forbids expanding it with full checklists. Confirmed: one dispatch line in `subagent-strategy/references/dispatch-checklists.md` requiring the predecessor-obligation inventory as acceptance for consolidation tasks (in context at prompt-construction time).

### P5. Workaround Tripwire (three-part)
- Evidence: HMC 2026-07-21 + user-directed rules already applied in BOTH repos' common/worker/orchestrator files; highest-conviction candidate.
- Content: (a) shared definition at failure-mode altitude — escalate when the fix goes around what it could change, symptoms as non-exhaustive examples; (b) dispatch constraint framing with explicit escape hatch (surface-minimizing constraints must state that preserving existing structure outranks them) → `subagent-strategy`; (c) first-class `design_alerts` field → `subagent-report-contract` schema. Alert-then-wait escalation contract; sealed-artifact exception.
- Home **[revised — four-part]**:
  (a) Detection: a fourth always-active trip condition inside `engineering-quality-baselines/SKILL.md` "Drift Tripwires (always active)" — the failure fires mid-implementation, when only the always-read layer is guaranteed in context; the section already trips on repeated workarounds, so add the sharper boundary/constraint test + response, nothing more (core-principles already owns root-cause-over-symptom).
  (b) Dispatch escape hatch: confirmed in `subagent-strategy/references/dispatch-checklists.md`.
  (c) `design_alerts`: schema.yaml alone is INSUFFICIENT — it is an unversioned example shape; real validation is hard-coded in `validate_worker_report.py` and unknown keys aren't rejected, so a YAML-only addition would be accepted but never validated or consumed. A real field needs: contract prose + schema sample + validator function + valid/invalid fixtures + smoke-test entries + a collection/ruling step in `wave-integration/references/integration-checklist.md`.
  (d) Mid-task stop-alert-await behavior is enforcement-critical role text, not a report field — it needs synchronized Worker workflow text across all three runtime adapters (Copilot/Claude/Codex) per `runtime-adapter-contract`, or the alert arrives only at final report, too late.
  Contradiction fix: do NOT promote a named "sealed-artifact exception" (the triage classifies sealed-artifact policy as repo-local); generalize to "owning boundary genuinely immutable/out of scope — report the constraint and cost".

### P6. Escalation rulings: blast-radius obligation + design-consult threshold
- Evidence: HMC 2026-07-22 asymmetric coordination/advice split (every defective orchestrator ruling of the phase was a contract-shape question answered at coordination tempo); orchestrator rules already applied in both repos.
- Content: escalation rulings carry a blast-radius obligation (all consumers in all repos, serialization surfaces, deferred scopes, owned contracts), researcher dispatch before ruling when self-verification can't cover it; two-tier threshold — contract-shape escalations require a pre-decision design consult (Tier A altitude); workers/reviewers state known consumer obligations and escalate rather than assume.
- Home **[revised]**: orchestration-harness does NOT currently own general escalation rulings (it routes escalation only inside goal mode). Authoritative two-tier ruling procedure + blast-radius obligation → new "Escalation Ruling" section in `orchestration-harness/references/lifecycle-gates.md` (extending the existing replan procedure), with an invocation hook from `wave-integration/references/integration-checklist.md` — the exact moment Worker questions/blockers/design alerts are aggregated. subagent-strategy keeps only the prompt-side line (Workers/Reviewers name known consumer obligations; their view is the local patch, orchestrator owns the radius).

### P7. Design-value audit triggers
- Evidence: HMC 2026-07-23 (Tier A value audit found two OVERSIZED structures + precedent drift; four-round fix chain with no proportionality checkpoint); orchestrator value-audit rules in both repos.
- Content: scheduled EARNS-ITS-PLACE / OVERSIZED / DELETE audits at four points — design review (every structure names a consumer), third fix bounce on one seam, pre-merge after fix churn, next-phase planning (no-inheritor structures become deletion candidates). Explicit non-trigger: never continuously.
- Home **[confirmed with hard constraint]**: audit body extends `long-horizon-audit.md` as a compact trigger/verdict appendix mapped onto the existing challenge/delete/simplify outcomes (not a parallel runbook). The triggers MUST live where they're loaded at the event: long-horizon-audit.md is explicitly "never load in standard task flow", so design-review/third-bounce/next-phase triggers → `lifecycle-gates.md`; pre-merge-after-churn → `completion-closeout.md` (or the wave-integration pre-Reviewer decision). Preserve the explicit non-trigger (never continuously).

### P8. Model-strength routing (Claude vs Codex)
- Evidence: orchestrator rules in BOTH repos (route detail-sensitive → Codex, altitude/lateral-judgment → Claude; forensic inventories → Codex, exploratory design research → Claude; Tier D correctness → Codex, Tier A design → Claude; ADRs authored by Orchestrator/Claude, never dispatched to implementation workers). Zero harness coverage today despite being applied and user-corrected repeatedly (e.g., ADR authorship correction 2026-07-18).
- Content: routing table by failure mode with graceful degradation when only one platform exists. Include the prose-quality rule (user-directed 2026-07-23): text authored by a detail-strength model (Codex) gets a rewording pass by a writing-strength model (Claude) before finalizing, without semantic change.
- Home **[confirmed, narrowed]**: new `subagent-strategy/references/model-routing.md` + a progressive-disclosure line in SKILL.md ("when multiple model platforms are available for delegation"). Do NOT extend `persistent-peer-dispatch.md` — it applies only to long-lived external-channel peers, so routing there would be dormant for ordinary spawned subagents. Write capability-first (forensic/detail scrutiny vs altitude/lateral design judgment) with Claude/Codex as current examples and a one-platform fallback, keeping the prose version-agnostic.

### Small singles (fold into the same PR) — homes verified
- Resolve a moving external dependency once before CI fan-out; one immutable SHA everywhere (CME LESSON-12) → confirmed: `review-latent-risk-build-ci.md`, one run-scoped-revision check.
- Cross-repo mirrored policies need a production-reachable seam test failing on either side's drift (CME LESSON-43) → **[revised]** `review-latent-risk-contract-scope.md` (two implementations of one contract), not the P1 conservation shard.
- "Promote rules at the evidenced scope, not the broadest phrasing" (CM lesson, Tier A) → confirmed: one declarative line in `rulebook/references/rule-writing-style.md`.
- Forensic researchers are read-only (CM FOLLOWUP-065) → confirmed but slimmed: the role boundary already exists in `orchestration-harness/references/dispatch-guidance.md`; add only the forensic-deliverable refinement (auditable census, file:line evidence, explicit zero-hits) as a dispatch-checklist line — no duplicate role-boundary block.
- Terminal review exit rubric + light delta-review path (CM FOLLOWUP-067/069) → **[revised — split]** external-review stopping rubric → `git-workflow/references/pr-authoring.md` / `pr-review-monitoring.md` (where external review loops are routed); low-risk internal delta path → `wave-integration/references/integration-checklist.md`, gated by explicit risk criteria (not unconditional). If Reviewer decision text changes, it must stay synchronized across runtime Reviewer adapters.

## KEEP REPO-LOCAL

- **All 72 FOLLOWUP product-backlog items** (typed-error refactors, Qdrant operational hardening, DTO/port redesigns, v0.2 roadmap inheritance) — product work for those repos, not process guidance. Two exceptions promoted above (FOLLOWUP-065/067/069) and one process seed (FOLLOWUP-060 re-confirm deferrals) which is absorbed by P7's next-phase-planning trigger.
- **Validation command mappings and evidence gates**: per-crate cargo test mappings, continuity two-run reproducibility, fixture byte-identity, live adapter evidence, sibling-revision provenance — repo CI facts.
- **Product policies**: benchmark live-by-default / mock opt-in, gold-label isolation, schema 2.0.0 fail-closed, sealed-artifact exception, no-backcompat (depends on the "no external consumers" repo fact), crate ownership/layout rules, branch naming convention.
- **Environment/tooling specifics**: Qdrant builder `.timeout()` semantics, local gRPC idle-stall + reboot remedy, config-crate `usize`→`i64` casts, Rust module layout preference — correct as repo lessons/rules. (The Qdrant timeout lesson is genuinely reusable knowledge but has no harness home; workspace-troubleshooting could take a Qdrant note if it ever recurs elsewhere — not required now.)
- **agmsg operational quirks** (send.sh four positionals — recurred 5×; Git-Bash PATH prepend): these belong to the **agmsg skill**, not the orchestration harness. Flag to the agmsg skill's maintenance loop as a separate small change if desired.

## ALREADY COVERED — no action, candidates for repo-rule slimming later

Zero-test-count evidence, worker owns-scope discipline, reviewer pinned isolated worktrees, parallelize-approved-work, replan-before-direction-change, research-dispatch gate, PR monitor arming (pr-comment-watch, v0.6.1), mid-plan formal task records (plan-format), shared-state git orchestrator ownership (git-workflow), artifact placement/disposition (largely covered; verify during implementation).

## Trigger-chain verification (Rev 3, 2026-07-23)

For every rule expected to be always applied or always read when its situation arises, the full load chain was audited: role's always-loaded surface (runtime adapter / repo-rule bootstrap) → skill load (explicit mandatory route vs semantic trigger match) → section/reference load. **Acceptance bar: an always-applied rule may not depend on runtime semantic skill selection — it needs an explicit mandatory route.** (Repo-rule bootstrap is not a substitute: the rules index routes role rule files only, never plugin references.) Verdicts and required wiring fixes, now part of the promotion scope:

| Item | Verdict | Required wiring fix |
|---|---|---|
| A. Workaround Tripwire (P5a) | **GAP** | Claude Worker/Reviewer adapters preload `engineering-quality-baselines`; Copilot and Codex Worker templates never load it, and Copilot/Codex Reviewers load it only on listed risk shapes. Fix: one synchronized line in all three Worker AND Reviewer role bodies — "Before implementation/code review, load `engineering-quality-baselines`; apply its Drift Tripwires throughout." |
| B. Dispatch escape hatch (P5b) | OK, harden | Reached via the Dispatch Integrity Gate's imperative "use subagent-strategy". Harden the local "If you want a dispatch checklist" phrasing to "Before every Worker dispatch, read `references/dispatch-checklists.md`." |
| C. `design_alerts` availability (P5c) | OK | All three Worker runtimes explicitly mandate `subagent-report-contract` — the field is guaranteed by report time. Mid-task stop-alert-await still requires the P5d adapter text; C only guarantees final-report shape. |
| D. Escalation Ruling (P6) | OK **iff hook is imperative** | wave-integration is guaranteed after each wave (Gate 5), but lifecycle-gates is only a details pointer. The integration-checklist hook must read: on any contract-shape/design ruling item, MUST read and apply `lifecycle-gates.md#escalation-ruling` before answering or dispatching, and record the ruling. Without MUST + direct anchor: GAP. |
| E. Value-audit triggers (P7) | **GAP** | Three missing event links: (1) Plan Gate can be satisfied from SKILL.md inline text without opening lifecycle-gates — change the lead-in to "MUST read lifecycle-gates before planning non-trivial plan-mode work; reread on replan"; (2) third-bounce needs a detector in `integration-checklist.md` (the only surface re-entered every wave), not just lifecycle-gates; (3) Completion Closeout Gate needs an explicit "MUST read completion-closeout.md before final done", whose fix-churn trigger then routes to the value-audit appendix. |
| F. Conservation shard routing (P1) | **GAP** (P2–P4 OK) | Reviewer adapters' replicated risk-shape lists and the e-q-b latent-risk route line don't name information conservation — a pure wrapper/conversion/aggregate change can miss all named shapes. Fix: add "information conservation across serialization, conversion, aggregation, and fallback boundaries" to `engineering-quality-baselines/SKILL.md` routing AND the synchronized risk-shape sentence in all three Reviewer adapters. P2 (validation), P3 (admission/diagnostics), P4 (multiple implementations) are already named in adapters and the reviewer packet. |
| G. PR review rubric homes (single e) | **GAP** at skill entry | git-workflow's description and orchestration-harness's routing label cover commit-affecting work only; a pure review-monitoring follow-up (read-only) can miss semantic selection on Copilot/Codex. Fix: extend git-workflow's frontmatter description with "creating/updating PRs and driving/monitoring external review loops" and the routing label to match. Internal chain (SKILL→pr-authoring→pr-review-monitoring) is already mandatory. |
| H. Evidenced-scope rule (single c) | **GAP** at reference boundary | rulebook's always-on bullets let an Orchestrator curate rules without ever opening style guidance ("If you need style guidance"). Fix: make it mandatory — "Before writing, merging, or curating any repository rule, MUST read `references/rule-writing-style.md`." |

## Implementation risk register (from home verification)

1. **Unwired shard**: a new review-latent-risk shard that isn't added to BOTH the router's risk-shape list and its conditional-reference table is unreachable; the package validator checks file existence, not routing.
2. **Unvalidated `design_alerts`**: schema.yaml is an example, not an executable schema; without a validator function, fixtures, smoke entries, and a wave-integration consumption step, the field would be silently inert.
3. **Reference-only event rules**: escalation-ruling and value-audit rules placed only in files not re-entered at the triggering moment (long-horizon-audit, persistent-peer-dispatch) are dormant — every event-triggered rule needs a trigger line in the file that IS loaded at that moment (SKILL.md always-read layer, lifecycle-gates, integration-checklist).
4. **Adapter synchronization**: mid-task Worker stop-alert-await behavior and any Reviewer decision-text changes must land in all three runtime adapters per runtime-adapter-contract, or runtimes diverge.
5. **Semantic-trigger reliance (Rev 3)**: an always-applied rule whose skill loads only by description matching is not guaranteed — Copilot/Codex Workers currently load NO quality-baseline skill at all, and Copilot/Codex Reviewers load it only on listed risk shapes. Every always-applied promotion carries its explicit-route wiring fix (table above) as part of its acceptance criteria; a promotion PR that lands content without the wiring is incomplete.

## Execution shape (proposed, not started)

1. Harness-maintenance plan in `agent-harness` (plan-format), target ~v0.9.0. One PR, waves by skill touched: P1–P4+singles (engineering-quality-baselines), P5–P6 (subagent-strategy + subagent-report-contract + orchestration-harness), P7 (long-horizon-audit + lifecycle-gates), P8 (subagent-strategy).
2. Role split per model strengths: Claude drafts reference prose (altitude/writing); Codex reviewer verifies each promoted line against its cited evidence and dedups against existing shard content (scrutiny); validators (`validate_harness_package.py`, smoke tests) green throughout.
3. Post-merge follow-ups in both target repos: mark promoted HMC entries, drain promoted lessons (v0.7.1 precedent), slim the now-duplicated generic rules from `rules/*.md` per rulebook dedup policy.
4. Separate small item: harness's own `docs/coding-agent/lessons.md` still holds 2 unpromoted lessons from 2026-07-16 — fold into the same PR.
