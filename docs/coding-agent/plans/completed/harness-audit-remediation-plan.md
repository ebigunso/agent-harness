# Plan: Harness Audit Remediation (Iterating)

- status: done (Reviewer APPROVED 2026-07-15)
- generated: 2026-07-15
- last_updated: 2026-07-15
- work_type: mixed

## Goal
- Act on the 2026-07-15 long-horizon audit of the harness: resolve the step-1 requirement challenges with the user, then execute the surviving deletions, simplifications, and accelerations in dependency order.

## Definition of Done
- Every audit finding has a user-ratified disposition (implemented, deferred, or rejected with reason); implemented items pass validators and independent review; plan iterated to done.

## Scope / Non-goals
- Scope: `plugins/coding-agent-orchestration-harness/**`; the uncommitted 2026-07-15 lessons entry rides with this plan's first commit.
- Non-goals: new capabilities; changes to target repositories; automating anything whose step-1 question is unresolved (explicitly: no manifest-bump automation before Q2 is answered).

## Decision Topics (iterating — one per audit finding)

| # | Finding | Step | Proposed disposition | Status |
|---|---|---|---|---|
| 1 | Research Dispatch Gate always waived for harness-repo governance/docs work | 1 | Keep unchanged, no edits: cross-repo evidence shows the gate exercised productively in all three coding repos (zero waivers there; CM lesson 2026-05-10 shows docs tasks are not a safe carve-out class); the recorded waiver is the working lightweight path; clarifying line rejected as too specific | resolved 2026-07-15 (no task) |
| 2 | Triple manifest versions bumped in lockstep | 1 | Keep three files (runtime discovery surfaces, legitimately different); add cross-manifest consistency check to validate_harness_package.py for version + shared identity fields (name, repository, license) | agreed 2026-07-15 (Task_8) |
| 3 | skill-creator route implies bundled path | 1 | Keep route (bounds skills-maintenance scope); reword pointer as Anthropic-official, environment-provided, surface-if-unavailable | agreed 2026-07-15 (Task_1) |
| 4 | worker-ui-probes standalone skill (28 lines, 0 refs) | 2 | Retire entirely: ~90% verbatim duplication of ui-validation-policy.md (policy) and subagent-report-contract (ui_probes schema); merge the one unique line (fix obvious issues within owns) into ui-validation-policy.md; update the two routes (Claude orchestrator agent frontmatter, README) | agreed 2026-07-15 (Task_3) |
| 5 | codex-harness-bootstrap vs runtime-adapter-contract overlap | 2 | Merge hypothesis withdrawn after inspection: nominal overlap only — installer skill (setup-time CLI docs, bootstrap-triggered, no always-read cost) vs maintainer governance; merging would worsen setup discoverability to save one index slot. Keep both unchanged | resolved 2026-07-15 (no task) |
| 6 | Waiver/required semantics split across validation-strictness.md and testing-validation.md | 2 | No consolidation (different layers; modes are validate_plan.py CLI args). One cross-pointer line in validation-strictness.md directing waiver evidence to the canonical template in testing-validation.md (prevented failure: improvised waiver prose failing canonical-waiver validators) | agreed 2026-07-15 (Task_4) |
| 7 | orchestration-harness SKILL.md 209 always-read lines; gates restated in lifecycle-gates.md | 3 | Slim to ~130 lines under the retention criterion (always-read = blocking decision rules + routing index only). Deletions (duplicates): UI three-tier table, route-restating Governance lines. Moves (routable read-moments): gate procedure to lifecycle-gates.md, fast-path detail to a reference (3-line core stays), rule-entry and role-description compression. Replan triggers and Dispatch Integrity field list stay whole | agreed 2026-07-15 (Task_2) |
| 8 | playwright-cli largest skill (280 lines + 7 refs) | 3 | Keep/defer, no task: live consumer exists (SleepTracker UI E2E); zero always-read cost — loads only when browser work is selected, so slimming has no per-task payoff | resolved 2026-07-15 (no task) |
| 9 | subagent-report-contract inlines full YAML schema (144 lines) | 3 | Keep unless prompt budgets tighten | keep (weak candidate) |
| 10 | Codex agmsg delivery required 3 manual nudges this session | 4 | No skill change: the channel earns its keep (strength-split review value) and persistent-peer-dispatch.md already mandates delivery verification; the method is tool-specific and operational (enable codex-side monitor mode) | resolved 2026-07-15 (no task) |
| 11 | gh-auth preflight lesson candidate unpromoted | 4 | Promote to workspace-troubleshooting entry (consumer: anyone assigning real-GitHub validation; prevented failure occurred 2026-07-15) | agreed 2026-07-15 (Task_5) |
| 13 | Role adapters maintained in triplicate: workflow + output contracts 89-94% line-identical across Copilot, Claude, and Codex adapter files | 2 | Keep the triplication — verified as deliberate instruction-block compilation (Codex developer_instructions, Copilot instructions, Claude system prompt; stronger role enforcement than thread-level reads; revisable if evidence changes). New task: one-time drift reconciliation across the 9 files (classify each differing line as intentional vs accidental) + update runtime-adapter-contract rules/checklist to codify replicate-and-sync and resolve the Claude-shorter tension. No drift validator (repo rule against overfitting validators to prose; checklist + Reviewer guard it) | agreed 2026-07-15 (Task_9) |
| 12 | Nothing new to automate | 5 | Keep as-is | agreed |

## Open Questions (max 3)
- Q1 (resolved 2026-07-15): keep the Research Dispatch Gate unchanged; no clarifying line (too specific).
- Q2 (resolved 2026-07-15): three manifests stay; drift detection added to the validator (Task_8).
- Q3: How often is browser validation actually exercised across current target repos? (Gates any playwright-cli simplification.)

## Follow-Up After Merge (agreed 2026-07-15)
- One small batch promoting the session's lessons: one line each in long-horizon-audit.md Step 2 (relevance-over-usability deletion judgment) and its Output/Step-2 area (proposed additions must name the concrete consumer or prevented failure); one Evidence Integrity line in testing-validation.md (hash-verify exact restoration of temporary test edits); a workspace-troubleshooting runbook entry for PYTHONIOENCODING on Windows consoles; one dispatch-checklists.md line in subagent-strategy (retire/delete tasks run the repo-wide name search at plan time and own every referencing file — supersedes the orchestrator.md repo-rule staging from Task_3's candidate, since the rule is not repo-specific).

## Assumptions
- A1: Tasks execute only after their Decision Topic reads "agreed"; the plan is expected to be edited across several discussion rounds before dispatch.
- A2: Version bump size decided at closeout based on what actually lands.

Required-check waiver
- What is waived: Reviewer-owned UI/E2E evidence for this plan.
- Why waived now: The plan changes documentation, skill content, and a validator script only; no UI, user flow, or layout surface is modified.
- Risk accepted and impact: None to UI behavior; the UI keywords in this plan are discussion text about skill routing.
- Mitigation and follow-up: Task_7 Reviewer performed full-diff review; any future UI-affecting work uses real Reviewer-owned E2E evidence.
- Owner and expiration: Orchestrator ; this plan only.

## Tasks

### Task_1: Reword the skill-creator route (agreed)
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/skills-maintenance/SKILL.md
- depends_on: []
- description: |
  Reword rule 6's pointer: skill-creator is Anthropic-official and environment-provided, not bundled with this plugin; if unavailable, surface that to the user instead of following a dead path. One-to-two lines; no change to the rule's scope boundary.
- acceptance:
  - No wording implies a bundled path; unavailable-case behavior stated.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py"
  - kind: review
    required: true
    owner: reviewer
    detail: "Wording review vs agreed disposition"

### Task_2: Slim orchestration-harness SKILL.md (agreed scope)
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/lifecycle-gates.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/rule-suite-fast-path.md
- depends_on: []
- description: |
  Apply the ratified retention criterion: always-read lines are blocking decision rules or routing only. Keep: identity + loader-role clause (~6), rule entry compressed to ~4, role boundaries (~8, role descriptions compressed — they live in runtime-role-map.md and adapters), five gates at binding-essence (~45; Dispatch Integrity field list whole; procedure/edge cases into lifecycle-gates.md or a fast-path reference), routing table, replan triggers whole, governance essence (~4: improvement-loop on corrections, third-party read-only, durable changes stated back), final response as 1 line + existing final-response-contract.md route. Delete outright (verbatim duplicates): the UI three-tier table (1-2 trigger lines survive), Governance lines restating routing-table entries. Fast path: 3-line core stays, edge cases move to a reference with the routing condition "tempted toward lifecycle/bootstrap work". Every moved block gets a routing line.
- acceptance:
  - SKILL.md lands near ~130 lines; gates semantically unchanged (reviewer-verified against the pre-change text); every moved block reachable via a routing line naming its read-moment.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py && python scripts/run_validation_smoke_tests.py"
  - kind: review
    required: true
    owner: reviewer
    detail: "Semantic-equivalence review of moved gate text; thin-prompt check"

### Task_3: Retire worker-ui-probes (agreed)
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/worker-ui-probes/**
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/ui-validation-policy.md
  - plugins/coding-agent-orchestration-harness/claude/agents/harness-orchestrator.md
  - plugins/coding-agent-orchestration-harness/README.md
- depends_on: []
- description: |
  Delete the worker-ui-probes skill directory. Merge its one non-duplicated rule (Workers fix obvious issues within owns during probes) into ui-validation-policy.md's Worker UI Probes section. Remove the skill from the Claude orchestrator agent frontmatter list and the README skill inventory. Verify no other route references it.
- acceptance:
  - Zero-match repo-root search for worker-ui-probes outside plans/lessons history; the fix-within-owns rule present in ui-validation-policy.md; probe semantics otherwise unchanged.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "Zero-match repo-root search for the retired skill name outside plans/lessons history; validate_harness_package.py pass"
  - kind: review
    required: true
    owner: reviewer
    detail: "Route-completeness and semantics review"

### Task_4: Waiver-evidence cross-pointer (agreed)
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/validation-strictness.md
- depends_on: []
- description: |
  Add one line to the hard-rules area of validation-strictness.md: waiver evidence follows the canonical Required-Check Waiver Template in engineering-quality-baselines/references/testing-validation.md. No other changes.
- acceptance:
  - Exactly one added line; the pointer names the canonical template's home; no semantics changed.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "validate_harness_package.py + smoke tests pass"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review vs agreed disposition"

### Task_5: gh-auth preflight troubleshooting entry (agreed)
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/workspace-troubleshooting/**
- depends_on: []
- description: |
  Promote the gh-auth preflight lesson into a workspace-troubleshooting entry in the skill's per-symptom runbook format: symptom (real-GitHub validation blocked mid-task; gh commands failing auth), safe ordered steps (run gh auth status before assigning real-GitHub validation to a session; assign such validation to a session with verified auth; never work around with token overrides), evidence, scope. One routing line in the SKILL.md triage index.
- acceptance:
  - Entry present in runbook format and routed from the index; no delivery-preflight content (topic 10 resolved no-change).
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "validate_harness_package.py pass"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review vs agreed dispositions"

### Task_6: Deferred/investigation items (findings 1, 2, 5, 8)
- type: research
- owns: []
- depends_on: []
- description: |
  Holds Q1/Q2/Q3 and the codex-harness-bootstrap merge investigation until their discussions resolve; converts into concrete tasks via plan iteration (Decision Log entries per resolution).
- acceptance:
  - Each held item resolved to a concrete task, an explicit deferral, or a rejection with reason.
- validation:
  - kind: review
    required: true
    owner: orchestrator
    detail: "Decision Log records each resolution"

### Task_7: Independent review and closeout
- type: review
- owns: []
- depends_on: [Task_1, Task_2, Task_3, Task_4, Task_5, Task_8, Task_9]
- description: |
  Reviewer verifies all landed changes against ratified dispositions; Orchestrator then bumps version (size per A2), runs full validators, commits in logical chunks including the pending 2026-07-15 lessons entry, opens the PR.
- acceptance:
  - Reviewer APPROVED; validators green; PR open.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Full-diff review vs plan dispositions"
  - kind: command
    required: true
    owner: orchestrator
    detail: "validate_harness_package.py && run_validation_smoke_tests.py; git diff --check"

### Task_8: Cross-manifest drift detection (agreed)
- type: impl
- owns:
  - plugins/coding-agent-orchestration-harness/scripts/validate_harness_package.py
- depends_on: []
- description: |
  Extend check_manifests (which already loads all three plugin.json files) to fail when version, name, repository, or license differ across them. Include the differing values in the error message. Verify behaviorally: current manifests pass; a deliberately mismatched version fails with a clear message (restore after). Dispatch note: Codex worker (script detail).
- acceptance:
  - Matching manifests pass; any mismatch in the four shared fields fails naming the field and values; smoke tests still pass.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "Behavioral check: pass on current manifests; fail on a temporarily mismatched version (restored afterward); python scripts/run_validation_smoke_tests.py pass"
  - kind: review
    required: true
    owner: reviewer
    detail: "Code review vs acceptance"

### Task_9: Adapter drift reconciliation and contract update (agreed)
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/agents/**
  - plugins/coding-agent-orchestration-harness/claude/agents/**
  - plugins/coding-agent-orchestration-harness/codex/agent-templates/**
  - plugins/coding-agent-orchestration-harness/skills/runtime-adapter-contract/**
- depends_on: [Task_3]
- description: |
  One-time reconciliation: diff each role's three adapter copies (Copilot agents/, Claude claude/agents/, Codex codex/agent-templates/), classify every differing body line as intentional runtime-specific or accidental drift, fix accidental drift toward the intended shared text, and report the classification. Then update runtime-adapter-contract SKILL.md core rules and adapter-maintenance-checklist.md: role workflow/output contracts are intentionally replicated as instruction blocks across runtimes (verified loading: Codex developer_instructions, Copilot instructions, Claude system prompt); editing shared contract text in one adapter requires updating all three and confirming sync; remove or scope the contradicted rules ('no full duplicate of the canonical workflow', 'Claude adapters shorter and reference-driven') to match. Depends on Task_3 (which edits claude/agents/harness-orchestrator.md frontmatter first).
- acceptance:
  - Per-role classification table reported (intentional vs fixed drift); the three copies of each role agree outside classified runtime-specific blocks; contract rules/checklist match the verified loading model with no self-contradiction.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "validate_harness_package.py + run_validation_smoke_tests.py pass; post-fix comm/diff evidence per role pair captured in the report"
  - kind: review
    required: true
    owner: reviewer
    detail: "Spot-verify the classification and the contract wording against the verified loading model"

## Task Waves (explicit parallel dispatch sets)

- Wave 0 (discussion, no dispatch): [Task_6]
- Wave 1 (parallel; disjoint owns; Claude workers plus the Codex worker for the validator change): [Task_1, Task_2, Task_3, Task_4, Task_5, Task_8]
- Wave 2 (Codex worker; after the retirement and validator tasks): [Task_9]
- Wave 3 (review + closeout): [Task_7]
- Task_6 resolved during discussion; all topics closed 2026-07-15.

## Rollback / Safety
- Docs/skill content only, on a feature branch created at first dispatch; revert by dropping the branch.

## Progress Log (append-only)

- 2026-07-16 Wave 1 completed: [Task_1, Task_2, Task_3, Task_4, Task_5, Task_8]
  - Summary: skill-creator reword landed; SKILL.md slimmed 209→139 (139 accepted — Routing Table + Replan Triggers kept whole per scope; lifecycle-gates.md needed no additions, every cut line already existed there or in a routed reference); worker-ui-probes retired with zero-match verification (one justified out-of-owns line: its entry in validate_harness_package.py's required-skills list, missed by the audit's route count); waiver pointer added (target heading verified); gh-auth runbook added; cross-manifest drift detection landed (Orchestrator independently verified fail-on-mismatch exit 3 and clean restore; Task_3/Task_8 concurrent edits to the validator coexist without clobbering).
  - Validation evidence: every Worker report green on its required items; Orchestrator reran package validator + smoke tests on the integrated worktree — pass.
  - Notes: Task_3 rule candidate staged for closeout (retire tasks enumerate every referencing file incl. validators into owns at plan time); Task_8 CRLF-restoration lesson recorded in lessons.md; Task_8 rule-refresh question assessed — no validation command or ownership changed, no rule-text update needed.

- 2026-07-16 Wave 2 completed: [Task_9]
  - Summary: adapter drift reconciliation confirmed topic 13's risk — Claude reviewer adapter had lost eight canonical latent-risk lines and compressed one more; five typography-drift lines in each of two Codex templates; one Copilot sentence aligned to the majority. Post-fix: Copilot=Claude bodies exact per role; Codex differs only by classified runtime mechanics (connector blocks, installed-plugin wording). runtime-adapter-contract SKILL.md/checklist/prompt-budgeting updated to the replicate-and-sync model; contradiction sweep clean.
  - Validation evidence: package validator + full smoke suite pass; post-fix pairwise diff tables in the Worker report; scoped git diff --check clean with CRLF conventions preserved.
  - Notes: targeted rule refresh REQUIRED and staged for closeout — common.md's "runtime adapters should route to shared skills rather than inline full checklists" needs scoping to the ratified exception (role workflow/output contracts deliberately replicated as instruction blocks). Windows PYTHONIOENCODING lesson recorded.

- 2026-07-16 Wave 3 completed: [Task_7]
  - Summary: Reviewer (codex) APPROVED with no blocking defects — gate semantics verified equivalent vs pre-change SKILL.md, retirement route-complete, drift detection code-reviewed, adapter reconciliation spot-verified (Copilot=Claude exact; Codex differs only by classified mechanics), small items confirmed, orphan-route sweep clean, all validators independently rerun. Closeout: targeted rule refresh applied (common.md adapters rule scoped to the replicated instruction-block exception); plan normalized to validator-clean (task ordering, Wave 0 for the discussion task, canonical UI waiver for keyword false-positive); version bumped to 0.7.0; full validators green.
  - Validation evidence: validate_plan.py balanced exit 0 on this plan; package validator + smoke tests pass post-bump; git diff --check clean.
  - Notes: post-merge follow-up batch recorded above (lesson promotions).

## Decision Log (append-only; re-plans and major discoveries)

- 2026-07-15 Decision: plan created as an iterating update plan rather than direct implementation, per user instruction; only finding 3 (skill-creator reword) and finding 12 (no new automation) are ratified so far.
  - Trigger / new insight: user direction after the audit report and the finding-3 disposition correction (relevance over current usability).
  - Plan delta (what changed): initial draft.
  - Tradeoffs considered: implementing trivial items directly (rejected — user wants plan-mediated iteration).
  - User approval: plan-as-vehicle yes; task dispatch pending per-topic agreement.

## Notes
- Risks: scope creep during iteration (mitigated: every topic tracked in the table with explicit status); Task_2 semantic drift while slimming (mitigated: reviewer equivalence check against pre-change text).
