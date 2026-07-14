# Plan: Promote Cross-Repo Lessons Into Harness Skill Updates

- status: done (Reviewer APPROVED 2026-07-14)
- generated: 2026-07-15
- last_updated: 2026-07-15
- work_type: docs

## Goal
- Promote the qualifying lessons from the 2026-07-15 cross-repo triage (SleepTracker, CharacterMemory, CharacterMemoryEvals, agent-harness) into the first-party harness skills, so future coding-agent runs benefit from the confirmed prevention rules.

## Definition of Done
- All triage items marked "qualifies" are represented in the target skills, each placed per the progressive-disclosure design rule below.
- Persistent-multi-agent dispatch guidance lives in a gated reference read only when the runtime uses long-lived agents over an external channel.
- Package validators and smoke tests pass; Reviewer APPROVED.

## Scope / Non-goals
- Scope: first-party skill content under `plugins/coding-agent-orchestration-harness/skills/` (SKILL.md routing lines and references).
- Non-goals: editing target repositories' lesson logs or repo rules; re-promoting CME review lessons already covered by the `review-latent-risk-*` reference family (spot-check only); runtime adapter changes; agmsg tooling changes.

## Design Rules (user-directed, apply to every task)
- Progressive disclosure for anything not always relevant: new guidance goes into `references/*` files with a one-line routing condition in SKILL.md; always-read text gains at most a pointer.
- Keep prompts thin: minimize added tokens in SKILL.md and always-read references; no duplicated checklists; prefer amending an existing reference over creating a new one when the topic matches.
- Environment-conditional guidance must state its routing condition explicitly (per lesson 2026-07-15, Gate Environment-Dependent Guidance Behind Progressive Disclosure).

## Context (workspace)
- Source triage: conversation report of 2026-07-15; source lesson logs in the four sibling repos' `docs/coding-agent/lessons.md`.
- Repo reference docs consulted: `docs/coding-agent/rules/{index,common,orchestrator}.md`, `plugins/coding-agent-orchestration-harness/skills/*` (coverage greps confirmed the listed themes are absent today).
- Research waived: triage research completed inline over lesson logs and targeted skill-tree coverage greps; content to promote is fully enumerated in this plan.

## Open Questions (max 3)
- Q1 (resolved 2026-07-14): Durable-docs authoring cluster becomes its own skill `durable-docs-authoring` (user decision via agmsg).

## Follow-Up After Merge (out of this plan's scope)
- After these skill updates merge in agent-harness, remove the now-redundant original lesson entries from the source repos' `docs/coding-agent/lessons.md` (SleepTracker, CharacterMemory, CharacterMemoryEvals). Plain removal, no promotion-traceability pointers: once the rules are fully encoded in harness skills, pointers add nothing for agents (user decision, 2026-07-14). Track as a separate task per repo.

## Assumptions
- A1: Plugin version bump and CHANGELOG handling follow the repo's existing convention and are done in the closeout task.
- A2: Workers are dispatched as harness-worker subagents (no live external worker team is registered for this repo session).

## Tasks

### Task_1: git-workflow — worktree verification, shared-resource safety, privacy sweep, PR authoring
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/git-workflow/**
- depends_on: []
- description: |
  Fold into existing references (thin additions): pre-commit-gate.md gains (a) verify `git status` plus a targeted `git diff` of last-touched files before claiming a branch clean or opening a PR, and (b) a privacy sweep for machine-specific paths (`C:/Users`, `%USERPROFILE%`, `%APPDATA%`, MSYS forms) before pushing documentation-heavy changes. safe-git-defaults.md gains the frozen-target-list rule for destructive operations on shared mutable resources (enumerate once, act only on the frozen list, verify implementation matches any announced safety property). Add one new reference `pr-authoring.md`: literal PR bodies via `--body-file - <<'EOF'`; hidden `.github/**` template discovery; final-state PR descriptions; complete-payload unresolved-thread extraction before review closeout; Copilot re-review GraphQL fallback (`requestReviewsByLogin` with `userLogins: ["copilot-pull-request-reviewer"]`, verify via `reviewRequests`/`latestReviews`, never exit-code trust). SKILL.md gains one routing line for pr-authoring.md (condition: creating/updating PRs or driving external review loops).
- acceptance:
  - The four lesson themes are present in the named references with no duplication across files.
  - SKILL.md grows by at most a few routing lines; no checklist bodies inline.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review vs acceptance and Design Rules (thin prompts, no duplication)"

### Task_2: engineering-quality-baselines — evidence integrity and durable-code hygiene
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/**
- depends_on: []
- description: |
  Extend references/testing-validation.md with an "Evidence integrity" section (six rules): absence claims require the broadest syntactic form of the target (encode the class, not the expected spelling) and repo-root search scope; never infer file/asset absence from ignore-aware search (require filesystem checks or `--no-ignore`); skip-capable tests need targeted reruns with confirmed absence of skip output, and gated live tests need a deliberate service-down verification; targeted-test evidence requires a positive executed-test count, never exit code alone; failures in untouched tests are classified against baseline HEAD before remediation; evidence claims state scenario scope, config identity, and dependency provenance at the point of claim. Extend references/core-principles.md with durable-code hygiene: root-cause fixes over symptom patches/suppressions; temporary suppressions and scaffolding carry rationale plus removal conditions; roadmap/version labels stay out of durable code identifiers and comments.
- acceptance:
  - All six evidence-integrity rules and three hygiene rules present, each 1-2 lines, in the named references.
  - No changes to SKILL.md beyond routing wording if strictly needed.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review vs acceptance; confirm no overlap/contradiction with review-latent-risk-* references"

### Task_3: subagent-strategy — gated persistent-peer dispatch reference and task sizing
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/subagent-strategy/**
- depends_on: []
- description: |
  Create references/persistent-peer-dispatch.md, read only when the runtime setup uses multiple long-lived agents communicating over an external channel (not spawn-and-clean-up subagents): verify the peer's delivery path is live before dispatch (a successful send is not delivery); count live workers and spawn the shortfall before a parallel wave; verify critical report handoffs are visible in the registered store/channel before treating delivery as complete. Add the routing condition as one line in SKILL.md and one line in references/async-dispatch-lifecycle.md. In always-read guidance, strengthen task sizing (prefer tasks completable in one short feedback loop: one module, one validation failure, one review slice) and waiting patience (wait substantially longer before force-closing background agents; use checkpoint prompts to redirect, not as a prelude to termination) — patience guidance belongs in async-dispatch-lifecycle.md Waiting Behavior.
- acceptance:
  - persistent-peer-dispatch.md exists with the explicit routing condition at the top; always-read files gain only pointer lines plus the sizing/patience additions.
  - No agmsg-specific tool names in the reference; guidance stays channel-neutral.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review vs acceptance and gating condition wording"

### Task_4: plan gate and plan-format — approval signal, append-only editing, roadmap separation, prose formatting
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/plan-format/**
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/lifecycle-gates.md
- depends_on: []
- description: |
  lifecycle-gates.md Plan Gate wording: clarifications, follow-up requirements, and refinements are not plan approval; execution requires an explicit approval or direct execution instruction (one or two lines). plan-format: in plan-template.md's append-only log sections or SKILL.md core rules (whichever is thinner), add the append-only editing rule (anchor on the previous entry and reproduce it, or anchor on the tail marker; verify the log grew). Add to execution-plan-lifecycle.md: roadmaps stay at chunk granularity with concrete Task_X detail only for the next executable chunk; keep roadmaps and concrete plans in separate files; name plans by outcome, not ordinal. Add one line to plan authoring rules: never hard-wrap prose mid-sentence in committed plan/doc files.
- acceptance:
  - Approval-signal rule present in lifecycle-gates.md; the three plan-format additions present in the named files.
  - Always-read SKILL.md additions total at most ~4 lines.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python skills/plan-format/scripts/validate_plan.py --file tests/fixtures/valid-plan.md --mode balanced"
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review vs acceptance and Design Rules"

### Task_5: improvement-loop — lesson-writing standard
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/improvement-loop/**
- depends_on: []
- description: |
  Make the lesson-writing standard explicit in references/entry-template.md (and post-correction-micro-checklist.md only if a one-line pointer is needed): keep the incident record concrete and specific to what happened; generalize only the prevention rule, to the highest-value confirmed scope; if a broader scope is plausible but unconfirmed, ask instead of assuming.
- acceptance:
  - Standard present in entry-template.md next to the existing generalized_rule field; SKILL.md unchanged or pointer-only.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review vs acceptance"

### Task_6: workspace-troubleshooting — Windows loopback/gRPC and PowerShell JSON framing
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/workspace-troubleshooting/**
- depends_on: []
- description: |
  Add two entries to the existing Windows-oriented reference family (new references only if no existing file fits): (a) prefer `127.0.0.1` over `localhost` for gRPC clients targeting Docker Desktop published ports on Windows; when gRPC times out but REST on the sibling port is fast, test IPv4 vs IPv6 connect paths before suspecting the service; (b) when validating cardinality-stable JSON in PowerShell, assert raw `[`/`]` framing or parse with `ConvertFrom-Json -NoEnumerate`; never treat a post-pipeline `-is [array]` check as proof of JSON array framing.
- acceptance:
  - Both entries present and routed from the SKILL.md triage index with one line each.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review vs acceptance"

### Task_7: durable-docs authoring cluster (new skill)
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/durable-docs-authoring/**
- depends_on: []
- description: |
  Create the new skill `durable-docs-authoring` from the seven SleepTracker durable-docs lessons: freeze capability-class terminology before drafting; split philosophy / milestone sequencing / capability boundaries across document roles; explicit freshness metadata or date anchoring for time-relative language; lead with the governing claim and tier support material (no flat peer lists); fix misleading filenames/titles instead of disclaiming them; keep incident-triggered naming consistent between title, filename, and opening. Thin SKILL.md trigger, all content in one reference.
- acceptance:
  - New skill exists with a thin trigger-scoped SKILL.md and one content reference; single-repo evidence provenance noted in the reference.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review vs acceptance and trigger-description quality (skills-maintenance rules)"

### Task_8: integration, harmonization, and package closeout
- type: chore
- owns:
  - plugins/coding-agent-orchestration-harness/** (routing lines, manifest/version only)
- depends_on: [Task_1, Task_2, Task_3, Task_4, Task_5, Task_6, Task_7]
- description: |
  Orchestrator-owned harmonization pass: confirm no duplicated guidance across tasks' additions; confirm every new reference has exactly one routing condition; update the orchestration-harness routing table only if a new skill was added (Q1); spot-check that the CME 2026-07-12 review lessons are covered by review-latent-risk-* references and record the result in this plan; bump plugin version per repo convention; run full validators.
- acceptance:
  - No cross-file duplication; routing complete; version bumped; spot-check recorded in Progress Log.
- validation:
  - kind: command
    required: true
    owner: orchestrator
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py && python scripts/run_validation_smoke_tests.py"
  - kind: command
    required: true
    owner: orchestrator
    detail: "From repo root: git diff --check"

### Task_9: independent review
- type: review
- owns: []
- depends_on: [Task_8]
- description: |
  Reviewer verifies every triage item marked "qualifies" landed in its target, Design Rules were honored (thin always-read additions, gated references with explicit conditions), and validation evidence is complete.
- acceptance:
  - Reviewer status is APPROVED
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Full-diff review vs this plan's task acceptance criteria and Design Rules"

## Task Waves (explicit parallel dispatch sets)

- Wave 1 (parallel): [Task_1, Task_2, Task_3, Task_4, Task_5, Task_6, Task_7]
- Wave 2 (sequential): [Task_8]
- Wave 3 (sequential): [Task_9]


## Rollback / Safety
- All changes are docs/reference files on a feature branch (`feature/2026-07-15/lessons-triage-skill-updates`); revert by dropping the branch. No runtime installs or target-repo edits.

## Progress Log (append-only)

- 2026-07-15 Wave 1 completed: [Task_1, Task_2, Task_3, Task_4, Task_5, Task_6, Task_7]
  - Summary: all seven Workers reported done; 20 files touched (83 insertions), all within owns; new skill durable-docs-authoring created; no manifest edit needed (skills registered by directory, validator auto-discovers).
  - Validation evidence: validate_harness_package.py pass in all seven reports; validate_plan.py pass (Task_4). Reviewer-owned diff review deferred to Task_9 per plan.
  - Notes: Task_7 flagged the orchestration-harness routing table for Task_8; no blockers; no rule candidates; subagent cleanup is runtime-automatic (recorded as unavailable/no-op).

- 2026-07-15 Wave 2 completed: [Task_8]
  - Summary: full-diff harmonization pass found no duplicated guidance and every new reference carries exactly one routing condition; added `durable-docs-authoring` to the orchestration-harness routing table; bumped plugin version 0.4.0 → 0.5.0 in all three manifests (.claude-plugin, .codex-plugin, .github/plugin).
  - Validation evidence: validate_harness_package.py pass; run_validation_smoke_tests.py pass (error lines in output are expected negative fixtures); git diff --check clean.
  - Notes: CME review-lesson spot-check — the review-latent-risk-* family covers admission boundaries, closed-vocabulary/exhaustive checks, exact-class regression requirements, and duplicated-value state handling; two themes are only partially covered (durable-store inventory across lifecycle transitions; identity-deduplication/disjointness before aggregating counts into rates) and are noted as future candidates, out of this plan's scope.

- 2026-07-15 Wave 3 completed: [Task_9]
  - Summary: independent Reviewer (codex agent-harness-reviewer via agmsg) returned NEEDS_REVISION with two MEDIUM findings (PowerShell 5.1 `-NoEnumerate` incompatibility in the JSON-cardinality runbook; duplicated Core rules in durable-docs-authoring SKILL.md); both remediated by Orchestrator (see Decision Log) and re-review returned APPROVED.
  - Validation evidence: Reviewer independently reran validate_harness_package.py, run_validation_smoke_tests.py, validate_plan.py, and git diff --check (all pass); post-remediation validate_harness_package.py pass reconfirmed by Orchestrator and Reviewer.
  - Notes: Reviewer verified all Task_1..Task_8 acceptance criteria against the actual diff; no residual blockers. Targeted repo-rule refresh waived: no repository facts in docs/coding-agent/rules/*.md changed (validators, layout conventions, and boundaries are untouched; the new skill follows the recorded naming/structure rules).

## Decision Log (append-only; re-plans and major discoveries)

- 2026-07-15 Decision: Task_9 NEEDS_REVISION remediation applied directly by Orchestrator (Worker dispatch waived).
  - Trigger / new insight: Reviewer (codex, via agmsg) returned two MEDIUM findings — `-NoEnumerate` invalid for Windows PowerShell 5.1 scope in powershell-json-array-cardinality.md, and durable-docs-authoring SKILL.md duplicating reference content against the thin-SKILL.md design rule.
  - Plan delta (what changed): both fixes applied as reviewer-specified mechanical edits (version-gate -NoEnumerate to pwsh 7+ with the 5.1-safe framing path; strip duplicated Core rules from SKILL.md leaving trigger + pointer); package validator re-run pass.
  - Tradeoffs considered: dispatching a remediation Worker adds a round trip for two fully-specified few-line edits; direct application recorded as an explicit dispatch waiver.
  - User approval: not separately sought; covered by approved plan execution and reviewer-directed remediation.

- 2026-07-14 Decision: gate persistent-multi-agent dispatch guidance behind a progressive-disclosure reference.
  - Trigger / new insight: user correction — the guidance only applies when the runtime keeps agents alive across dispatches.
  - Plan delta (what changed): Task_3 creates a gated reference instead of extending always-read async-dispatch-lifecycle guidance.
  - Tradeoffs considered: always-read placement is simpler but adds noise for spawn-per-dispatch runtimes.
  - User approval: yes (agmsg, 2026-07-14).

- 2026-07-14 Decision: Q1 resolved — durable-docs cluster becomes its own skill; post-merge source-lesson cleanup added as tracked follow-up.
  - Trigger / new insight: user direction via agmsg (2026-07-14 19:49 UTC).
  - Plan delta (what changed): Task_7 unblocked and scoped to the new `durable-docs-authoring` skill; new "Follow-Up After Merge" section records the redundant-lesson removal in source repos.
  - Tradeoffs considered: reference under an existing skill would avoid a new trigger, but a dedicated thin-trigger skill routes better for doc-authoring work.
  - User approval: yes (agmsg, 2026-07-14).

## Notes
- Risks: guidance duplication across skills (mitigated by Task_8 harmonization); trigger-description bloat (mitigated by Design Rules).
- Edge cases: none outstanding.
