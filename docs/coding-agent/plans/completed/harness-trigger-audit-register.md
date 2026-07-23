# Existing-Harness Trigger-Chain Audit — Findings Register

Date: 2026-07-23. Consolidated by agent-harness-orchestrator from two parallel Codex audits (researcher: skills side, 16 skills; reviewer: adapter side, 3 runtimes × 4 roles). Both read-only; package validator green. (Correction to earlier inventory: the plugin has **16** skills, not 17.)

**Answer to the question asked:** yes — the existing harness has the same symptom classes the promotion audit predicted. 24 findings total: 17 skills-side, 7 adapter-side. Goal mode is the clean counter-example: every cadence rule is imperatively bound (its references literally embed "read the mandate" in the fixed dispatch text). Seven skills got a clean bill: codex-harness-bootstrap, durable-docs-authoring, plan-format, playwright-cli, playwright-e2e-evidence, runtime-adapter-contract, workspace-troubleshooting.

## Gap-class counts

| Class | Count | Meaning |
|---|---|---|
| optional-phrasing | 8 | MUST-apply rule behind "If you want/need…" routing |
| routing-only | 3 | reference named in a routing table but never imperatively read at its event |
| description mismatch | 3 | skill/route description doesn't cover a situation the skill's own content claims |
| binding-moment | 1 | rule lives in a skill that normally loads after the moment it binds |
| orphan | 2 | reference file no routing line reaches |
| adapter hard-route gaps | 3 | role/runtime lacks any hard route to a skill whose rules bind on it (blocking) |
| adapter parity issues | 4 | Claude-only preloads with no binding role action; Orchestrator child-route divergence (non-blocking) |

## Blocking findings (fix before or with the promotion PR)

1. **Worker × engineering-quality-baselines** (adapter #1 + skills F2; = promotion fix A). Copilot/Codex Workers reach the skill with its "always active" Drift Tripwires only by semantic matching; Claude preloads it. Fix: one synchronized load-and-apply line in all three Worker bodies (and keep Reviewer conditional routing after an always-load line, per promotion fix A).
2. **Worker × git-workflow on delegated commits** (adapter #2). When the Orchestrator delegates a commit-affecting mutation, Copilot/Codex Workers have no route to the skill that owns the safety gates. Fix: conditional line in the synchronized git-boundary paragraph — "if delegated a commit-affecting mutation, load git-workflow before acting."
3. **Reviewer × playwright-e2e-evidence** (adapter #3). The skill contains a required Reviewer artifact-existence gate, but Copilot/Codex Reviewers never hard-load it for UI acceptance. Fix: exact conditional route in the synchronized Reviewer UI section; then drop the Claude-only unconditional preload for symmetry.
4. **Per-commit gate optionalized** (skills F3). `pre-commit-gate.md` says "use before ANY commit-affecting mutation"; the router says "If you need the ordered gate…". Fix: imperative wording.
5. **Post-correction micro-checklist optionalized** (skills F6). improvement-loop's own SKILL.md mandates the checklist "whenever active", then routes it behind "If you need…". Fix: "whenever this skill is active, read and complete it before ending the turn."
6. **Improvement-loop's non-user triggers unrouted** (skills F5). Missed hard gates and review misses are claimed triggers, but orchestration-harness routes only "correction events". Fix: extend the Governance line to missed-gate/review-miss discovery.

## Non-blocking findings

- **Optional-phrasing on mandatory paths** (skills F1, F7, F11, F12, F13, F14): EQB core-principles ("start with this for every non-trivial impl/review" vs "when unclear"), repeat-twice promotion rule, rule-writing-style (= promotion H), HMC staging format, skills-maintenance final QA pass, dispatch-checklists (= promotion B hardening). All same fix shape: imperative event-bound wording.
- **Routing-only references** (skills F9, F15): completion-closeout (= part of promotion E fix) and wave-integration's two references listed without "read/run" (supports promotion D hook). Fix: event-bound imperatives.
- **Description mismatches** (skills F4 = promotion G git-workflow PR coverage; F10 rulebook reference-document maintenance).
- **Binding-moment** (skills F8): the "skim lessons.md before non-trivial work" startup rule lives in improvement-loop, which normally loads only after a correction. Fix: move the startup read into orchestration-harness's non-trivial start gate.
- **Orphans** (skills F16, F17): `subagent-report-contract/references/examples.md` and `schema.yaml` have zero inbound routes; the validator doesn't consume schema.yaml (consistent with the promotion P5c finding). Fix: route them or make schema.yaml the validator's canonical input — decide during P5c work.
- **Adapter parity** (adapter #4–7): Orchestrator child-route sets diverge across runtimes (functionally safe — orchestration-harness hard-routes every binding event — but contract drift); Claude Researcher preloads REPORT/STRAT/RULE with no binding role action; Claude Worker and Reviewer preload RULE (and Reviewer REPORT) similarly. Fix: normalize to OH-as-single-router for the main thread, prune non-binding Claude preloads.

## Overlap with the promotion plan (Rev 3)

Seven findings are the same fixes already in promotion scope: adapter #1/skills F2 = fix A; F14 = B; F9 = E(3); F15 = D hook; F4 = G; F11 = H; F17 = P5c schema decision. The remaining ~17 are new existing-content debt.

## Remediation constraints (from the adapter audit)

- Codex `AGENTS.md` snippet stays loader-only — subrole hard routes go in TOML `developer_instructions`; main-thread event routes go in orchestration-harness.
- Researcher/Worker/Reviewer bodies are byte-synchronized across runtimes: edit all three together, body-diff after.
- Claude enforcement-critical role text may not be shortened for budget; Copilot keeps its medium kernel with the five gates visible.

## Proposed sequencing

**PR 1 — wiring remediation (no new content):** all imperative-wording, routing, description, orphan, and adapter-route fixes above. Small, mechanical, independently reviewable; validators + body-diff as gates. **PR 2 — the promotion PR (Rev 3 scope)** then lands its content on already-correct wiring, with only its genuinely new wiring (conservation risk shape, escalation-ruling hook, value-audit triggers, design_alerts validation). This avoids entangling content review with wiring review and makes both diffs honest.
