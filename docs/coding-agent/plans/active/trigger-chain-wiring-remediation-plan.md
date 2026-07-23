# Plan: Trigger-Chain Wiring Remediation (PR 1 of 2)

- status: in_progress
- generated: 2026-07-23
- last_updated: 2026-07-23
- work_type: docs

## Goal
- Fix all existing trigger-chain gaps found by the 2026-07-23 harness audits so that every rule that claims mandatory/always application is reachable through an explicit imperative route at its binding moment, in every runtime. No new guidance content — wiring only. PR 2 (promotion of CharacterMemory/CharacterMemoryEvals candidates) lands on this corrected wiring.

## Definition of Done
- All 6 blocking and applicable non-blocking findings from the consolidated audit registers are fixed per the normative fix list below.
- Researcher/Worker/Reviewer instruction bodies remain byte-synchronized across Copilot/Claude/Codex (after documented runtime-mechanic deltas).
- All repo validators pass; plugin version bumped to 0.8.1 in all three manifests.
- Codex Reviewer APPROVED against the audit registers.

## Scope / Non-goals
- Scope: imperative-wording, routing, description, orphan-route, and adapter-route fixes in `plugins/coding-agent-orchestration-harness/` (skills + agents + claude + codex trees) and the three plugin manifests.
- Non-goals: (a) any new guidance content (PR 2); (b) `schema.yaml` canonical-validator integration (deferred to PR 2 / P5c — PR 1 only routes the file); (c) Orchestrator child-route normalization across adapters (adapter audit finding #4, MINOR, functionally safe — deferred; see Decision Log); (d) target-repo rule slimming.

## Context (workspace)
- Audit registers (normative evidence): scratchpad `existing-harness-trigger-audit.md` (consolidated), plus agmsg reports agent-harness-researcher 2026-07-23T08:42Z (skills side, findings F1–F17) and agent-harness-reviewer 2026-07-23T08:38Z (adapter side, findings 1–7 + matrix).
- Repo reference docs consulted: `docs/coding-agent/rules/*` (suite rules-20260513-b80f05e), `plugins/coding-agent-orchestration-harness/README.md`.
- Governing constraints: `docs/coding-agent/rules/common.md` (adapter copies edited together + sync confirmed; skills stay version-agnostic), runtime-adapter-contract (Codex AGENTS snippet stays loader-only).

## Open Questions (max 3)
- None. All wording decisions are fixed in the normative fix list below.

## Assumptions
- A1: Findings' file:line citations are accurate as of branch point (audits ran today against main = 4664741).
- A2: Version bump is patch (0.8.1): behavior-hardening of existing contracts, no new content surface.

## Normative fix list

### Task_1 scope (skills side)
1. (F1) `skills/engineering-quality-baselines/SKILL.md` core-principles route → "Core principles: `references/core-principles.md` (read for every non-trivial implementation or review; also when intent/scope or tradeoffs are unclear)".
2. (F2) `skills/orchestration-harness/SKILL.md` Dispatch Integrity Gate: append "Non-trivial implementation and review work loads `engineering-quality-baselines`; select routing depth per that skill before dispatch."
3. (F3) `skills/git-workflow/SKILL.md` pre-commit route → "Before any commit-affecting Git mutation: read and run `references/pre-commit-gate.md`."
4. (F4) `skills/git-workflow/SKILL.md` frontmatter description: append PR creation/update and external-review-loop driving/monitoring to the trigger description. `skills/orchestration-harness/SKILL.md` routing label → "Git safety, commit/PR workflow, and external review monitoring: `git-workflow`".
5. (F5) `skills/orchestration-harness/SKILL.md` Governance line → "Correction events, missed hard gates, and review/CI/human findings the harness should have caught require `improvement-loop` before ending the turn."
6. (F6) `skills/improvement-loop/SKILL.md` checklist route → "Whenever this skill is active, read and complete `references/post-correction-micro-checklist.md` before ending the turn."
7. (F7) `skills/improvement-loop/SKILL.md` promotion route → "When classifying a lesson or deciding promotion (mandatory on the second occurrence of the same lesson), read `references/promotion-guidelines.md`."
8. (F8) `skills/orchestration-harness/SKILL.md` Repository Rule Entry: append "Before starting non-trivial work, also skim `docs/coding-agent/lessons.md` and any active plans." (improvement-loop copy retained as reinforcement.)
9. (F9) `skills/orchestration-harness/SKILL.md` Completion Closeout Gate: prepend to "Before final done" list intro: "Read and apply `references/completion-closeout.md`, then confirm:".
10. (F10) `skills/rulebook/SKILL.md` add route: "If adding or updating a repository reference document: read `references/rules-files.md` (Repository Reference Documents section)."
11. (F11) `skills/rulebook/SKILL.md` style route → "Before writing, merging, or materially revising any repository rule, read `references/rule-writing-style.md`."
12. (F12) `skills/rulebook/SKILL.md` HMC route → "When staging or updating a harness migration candidate, read `references/skill-candidates-file.md`."
13. (F13) `skills/skills-maintenance/SKILL.md` QA route → "Before marking any skill change complete, read `references/final-ambiguity-pass.md` and run the pass."
14. (F14) `skills/subagent-strategy/SKILL.md` checklist route → "Before each Researcher/Worker/Reviewer dispatch, read and apply `references/dispatch-checklists.md`."
15. (F15) `skills/wave-integration/SKILL.md` reference list → two imperatives: "After every Worker wave: run `references/integration-checklist.md`." / "Before every Reviewer dispatch: read `references/reviewer-packet-template.md` and build the packet."
16. (F16) `skills/subagent-report-contract/SKILL.md` add route: "For worked report examples: `references/examples.md`."
17. (F17) `skills/subagent-report-contract/SKILL.md` add route: "For the canonical report shape sample: `references/schema.yaml`." (No validator change in PR 1.)

### Task_2 scope (adapter side; each edit applied to all three runtime copies together, byte-sync confirmed)
1. (Adapter #1 / F2) Worker bodies (`agents/Worker.md`, `claude/agents/harness-worker.md`, `codex/agent-templates/harness_worker.toml`): add Hard rule — "For non-trivial implementation, load and apply `engineering-quality-baselines` (routing depth per that skill); keep its Drift Tripwires active throughout."
2. (Adapter #2) Worker bodies, git-boundary paragraph: append "If the Orchestrator explicitly delegates a commit-affecting mutation, load and follow `git-workflow` before acting."
3. (Adapter #3) Reviewer bodies (`agents/Reviewer.md`, `claude/agents/harness-reviewer.md`, `codex/agent-templates/harness_reviewer.toml`), UI section: add "When reviewing UI/E2E acceptance, load `playwright-e2e-evidence` and enforce its evidence gates."
4. (Adapter #5) `claude/agents/harness-researcher.md`: remove non-binding frontmatter preloads `subagent-report-contract`, `subagent-strategy`, `rulebook`.
5. (Adapter #6) `claude/agents/harness-worker.md`: remove non-binding preload `rulebook`. Keep `engineering-quality-baselines` and `git-workflow` (binding-relevant belt-and-braces over the new body lines).
6. (Adapter #7) `claude/agents/harness-reviewer.md`: remove non-binding preloads `subagent-report-contract`, `rulebook`. Keep `engineering-quality-baselines`, `playwright-cli`, `playwright-e2e-evidence`.

## Tasks

### Task_1: Skills-side wiring fixes
- type: impl
- owns:
  - plugins/coding-agent-orchestration-harness/skills/**
- depends_on: []
- description: |
  Apply normative fix list items 1–17 (Task_1 scope) exactly as worded. No other content changes; do not reflow unrelated text; keep skill prose version-agnostic.
- acceptance:
  - Every fix-list item 1–17 applied with the exact routing/imperative semantics specified
  - No enforcement text weakened or removed; no new guidance content introduced
  - No unrelated diff hunks
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py && python scripts/run_validation_smoke_tests.py"
  - kind: command
    required: true
    owner: worker
    detail: "From repo root: git diff --check"

### Task_2: Adapter-side wiring fixes
- type: impl
- owns:
  - plugins/coding-agent-orchestration-harness/agents/**
  - plugins/coding-agent-orchestration-harness/claude/**
  - plugins/coding-agent-orchestration-harness/codex/**
- depends_on: [Task_1]
- description: |
  Apply normative fix list items 1–6 (Task_2 scope). Edit all three runtime copies of each role body together; Codex AGENTS snippet stays loader-only (no changes there). Confirm post-edit body synchronization (bodies byte-equivalent after frontmatter/TOML mechanics and the documented Codex connector-block delta).
- acceptance:
  - All six adapter fixes applied; the three copies of each edited role body remain synchronized
  - codex/snippets/AGENTS.md unchanged
  - Removed preloads limited to the three files and skills named
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py && python scripts/run_validation_smoke_tests.py"
  - kind: manual
    required: true
    owner: worker
    detail: "Body-diff evidence: normalized diff of Worker and Reviewer bodies across the three runtimes showing equivalence (documented deltas only)"

### Task_3: Claude prose-quality pass over Codex-authored text
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/**
  - plugins/coding-agent-orchestration-harness/agents/**
  - plugins/coding-agent-orchestration-harness/claude/**
  - plugins/coding-agent-orchestration-harness/codex/**
- depends_on: [Task_1, Task_2]
- description: |
  Orchestrator (Claude) reviews every sentence added or reworded by the Codex worker in
  Task_1/Task_2 diffs and rewords for clarity and quality where warranted, without changing
  routing semantics, imperative force, or enforcement meaning. Adapter role-body edits stay
  synchronized across the three runtime copies after rewording.
- acceptance:
  - Every Codex-authored/edited sentence in the wave diffs reviewed by Claude
  - No semantic or enforcement changes introduced by rewording
  - Three-runtime body sync preserved for any reworded adapter text
- validation:
  - kind: command
    required: true
    owner: orchestrator
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py && python scripts/run_validation_smoke_tests.py"

### Task_4: Version bump and full validation
- type: chore
- owns:
  - plugins/coding-agent-orchestration-harness/.claude-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.codex-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.github/plugin/plugin.json
- depends_on: [Task_3]
- description: |
  Bump version 0.8.0 → 0.8.1 in all three manifests; run the full repo validator set.
- acceptance:
  - All three manifests at 0.8.1
  - Full validator set green
- validation:
  - kind: command
    required: true
    owner: orchestrator
    detail: "All commands from docs/coding-agent/rules/common.md Repository-Specific Validation Commands"

### Task_5: Independent review
- type: review
- owns: []
- depends_on: [Task_4]
- description: |
  Codex Reviewer verifies, at the pinned commit: every audit finding's fix present and semantically correct vs the audit registers; three-way body sync; no weakened enforcement text; no content additions beyond wiring; validators green.
- acceptance:
  - Reviewer status APPROVED
  - Finding-by-finding verification against both audit registers
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Finding-by-finding wiring verification + sync diff + validator rerun at pinned commit"

## Task Waves (explicit parallel dispatch sets)

- Wave 1: [Task_1]
- Wave 2: [Task_2]
- Wave 3: [Task_3]
- Wave 4: [Task_4]
- Wave 5: [Task_5]

(Sequential waves: one shared checkout and a single Codex worker peer; Task_1/Task_2 owns are disjoint but serialization avoids mid-edit validator noise.)

## Rollback / Safety
- All changes on `feature/2026-07-23/trigger-chain-wiring-remediation`; revert = drop branch. No runtime installs touched; templates are inert plugin files.

## Progress Log (append-only)

- 2026-07-23 Plan drafted after user approval of the two-PR sequencing ("Yes, that looks like the right way to go. Start your work.").
- 2026-07-23 Wave 1 completed: [Task_1]
  - Summary: all 17 skills-side fixes applied across nine SKILL.md files by the Codex worker (agmsg report 09:22Z); orchestrator spot-verified the diff (23+/21-) against the normative list.
  - Validation evidence: validate_harness_package.py exit 0; run_validation_smoke_tests.py exit 0; git diff --check exit 0; worker's 17-item phrase/reference audit exit 0.
  - Notes: worker staged one lesson candidate (scope trigger assertions to their owning surface) — carried to closeout. Commit 3cffca0.
- 2026-07-23 Wave 2 completed: [Task_2]
  - Summary: six adapter fixes across seven files; three-runtime body sync verified by normalized SHA-256 (Worker 4E0EE980…, Reviewer EA403E3B…); loader snippet hash unchanged. One mid-task escalation ruled (see Decision Log). Commit 9a6e1bb.
  - Validation evidence: package validator exit 0; smoke tests exit 0; body-sync comparison exit 0; adapter checklist + git diff --check exit 0.
  - Notes: two lesson candidates staged (adapter-preload baseline verification; line-bounded connector-block normalization) — carried to closeout.
- 2026-07-23 Wave 3 completed: [Task_3]
  - Summary: Claude prose pass over both wave diffs; three rewordings, semantics preserved; adapter text unchanged. Commit ca19e00.
  - Validation evidence: package validator exit 0; smoke tests exit 0 (rerun cleanly after a piped-exit-code masking slip).
- 2026-07-23 Wave 4 completed: [Task_4]
  - Summary: version 0.8.1 in all three manifests. Commit d37e2c2.
  - Validation evidence: full common.md validator set green (pkg/smoke/plan/report×2/diff --check all exit 0).

## Decision Log (append-only; re-plans and major discoveries)

- 2026-07-23 Decision: defer Orchestrator child-route normalization (adapter audit finding #4).
  - Trigger: reviewer classified it MINOR contract divergence; orchestration-harness hard-routes every binding event, so functional risk is nil.
  - Plan delta: excluded from scope; recorded as follow-up candidate paired with a prompt-budget review.
  - Tradeoffs: leaves direct-route parity debt vs keeping PR 1 mechanical and low-risk.
  - User approval: covered by approval of the register's PR 1 scope, which listed this as the deferred alternative direction.
- 2026-07-23 Decision: PR 1 routes `schema.yaml`/`examples.md` orphans but defers canonical-schema validator integration to PR 2 (P5c), where `design_alerts` work must touch the validator anyway.
- 2026-07-23 Decision: Task_2 item 6 keep-list mismatch ruling (Worker escalation, agmsg 09:25Z).
  - Trigger / new insight: the item-6 keep-list named a `playwright-cli` preload in `claude/agents/harness-reviewer.md` that does not exist — the audit matrix's hard route for it comes from the reviewer body text (line 46), not frontmatter. "Keep" was imprecise descriptive context carried from the audit.
  - Plan delta: none to the diff — ruling was removals-only as authorized: remove `subagent-report-contract` and `rulebook` preloads, add nothing, preserve the existing `playwright-cli` body route. Fix-list item 6's keep-list is superseded by this entry.
  - Tradeoffs considered: adding a `playwright-cli` preload for symmetry was rejected — additions were unauthorized and the body route is the binding mechanism.
  - User approval: not required (within dispatched scope; recorded per reviewer requirement).
- 2026-07-23 Decision: added Task_5 (Claude prose-quality pass) between the Codex worker waves and the version bump.
  - Trigger: user directive — Claude models write higher-quality prose than the GPT-5.6 Codex models; any Codex-authored sentence gets a Claude rewording pass before finalizing.
  - Plan delta: new prose-pass task inserted as Task_3 (version bump and review renumbered to Task_4/Task_5); waves renumbered accordingly.
  - Tradeoffs: one extra pass per plan vs shipping lower-quality prose in durable skill/adapter text.
  - User approval: yes (user-directed, 2026-07-23). Also queued as content for PR 2's model-routing.md (P8).

## Notes
- Risks: wording drift between the three adapter copies (mitigated by Task_2 body-diff evidence + Reviewer sync check); audits cited line numbers that may shift after Task_1 (Task_2 dispatched with semantic anchors, not line numbers).
- Edge cases: Codex connector block and "installed plugin's" phrasing are documented allowed deltas in body-sync comparison.
