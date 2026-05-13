---
status: accepted
adr_type: design
date: 2026-05-12
deciders:
  - ebigunso
consulted:
  - GPT-5.5 Pro
informed: []
supersedes: []
superseded_by: null
---

# ADR-D-0006: Use a Full Repository Rule Suite With a Low-Token Index and Lifecycle Sidecar

## Context and Problem Statement

The coding-agent orchestration harness is designed to run across many repositories and multiple coding-agent runtimes. Runtime adapters route to shared skills, while repository-specific operating constraints live under `docs/coding-agent/rules/*.md`.

The existing rulebook structure defines repository rule files for common, worker, orchestrator, and index rules. In practice, the harness also needs review-specific repository policy, especially for recurring review findings such as public API compatibility, diagnostic fidelity, build-configuration parity, and entrypoint/admission semantics.

The harness also needs a way to bootstrap repository rules with useful content instead of creating placeholder skeletons. However, bootstrap and freshness checks must not add expensive context-token overhead to every task. The frequently read index file should not contain long source snapshots, fingerprint lists, or full lifecycle state.

## Decision Drivers

- Create useful repo-specific rules on first meaningful harness use.
- Include Reviewer-specific repository policy as part of the standard rule suite.
- Avoid per-task full bootstrap checks or repository-wide scans.
- Keep frequently read rule files small, especially `index.md`.
- Preserve progressive disclosure and prompt-budget discipline.
- Keep lifecycle data available for repair, schema migration, targeted refresh, and contradiction handling.
- Avoid generic repository quality scripts that assume arbitrary languages or frameworks.
- Make staleness a derived property of manifest integrity, changed paths, and contradiction signals rather than a durable status flag that can itself become stale.

## Decision

The harness will use a full repository rule suite:

- `docs/coding-agent/rules/index.md`
- `docs/coding-agent/rules/common.md`
- `docs/coding-agent/rules/worker.md`
- `docs/coding-agent/rules/orchestrator.md`
- `docs/coding-agent/rules/reviewer.md`
- `docs/coding-agent/rules/_lifecycle.json`

Bootstrap always creates the full suite. `reviewer.md` is not optional.

`index.md` is a low-token routing file and bootstrap success marker. It contains the schema version, suite ID, required role rule files, and pointer to `_lifecycle.json`. It should be safe to read often.

`_lifecycle.json` is the machine-oriented lifecycle sidecar. It contains required file paths, baseline metadata, refresh groups, source evidence, and source-to-rule-section mappings. Agents read it only when lifecycle work is needed.

The bootstrap write order is:

1. `common.md`
2. `worker.md`
3. `orchestrator.md`
4. `reviewer.md`
5. `_lifecycle.json`
6. `index.md`

Writing `index.md` last makes it the success marker. If bootstrap is interrupted before `index.md` is written, the suite is not considered installed.

Rule-suite validity is derived, not trusted from a durable status flag. A suite is valid when:

- `index.md` exists;
- `_lifecycle.json` exists;
- required role rule files exist;
- all rule files share the same suite ID;
- schema version matches the plugin-required schema;
- no relevant source drift or contradiction is known.

The harness does not run full bootstrap as a per-task ritual.

For trivial work, agents skip rule-readiness checks unless the task directly touches rule files, CI/validation sources, build manifests, or agent instruction files.

For non-trivial work, the Orchestrator reads `index.md` only when repo rules are needed for planning, validation, review policy, or repository-specific constraints. It reads `_lifecycle.json` only for bootstrap, repair, schema migration, targeted refresh, source-drift diagnosis, or contradiction handling.

Staleness is handled through targeted refresh. Refresh is triggered by:

- current-task changes to rule-source paths;
- source drift detected through lifecycle metadata;
- contradictions discovered by Researcher, Worker, Reviewer, CI, or user feedback;
- schema migration needs;
- repeated review misses that reveal missing repo-specific policy.

## Considered Options

### Option 1: Store all lifecycle metadata in `index.md`

This makes the index self-contained, but increases context-token cost because agents read `index.md` often.

Rejected because the index would become too heavy for normal planning and review.

### Option 2: Keep only skeleton rule files and let agents rediscover repository truth each task

This keeps rule files simple but wastes repeated agent effort and makes validation/review behavior inconsistent.

Rejected because it does not provide a durable repository operating contract.

### Option 3: Add a generic quality-gate script that detects and runs checks for arbitrary repositories

This could catch some mechanical issues, but arbitrary repositories have different languages, frameworks, task runners, services, and validation conventions.

Rejected as the default approach. Scripts remain appropriate for plugin self-validation, adapter/bootstrap plumbing, and repository-specific workflows after explicit bootstrap, but not as universal quality gates.

### Option 4: Use a low-token index plus a sidecar lifecycle manifest

Chosen. It preserves fast normal operation while keeping enough lifecycle metadata for repair, migration, targeted refresh, and contradiction handling.

## Decision Outcome

Chosen option: **Option 4**.

The harness will create a full rule suite and use `index.md` as a compact routing/success marker. Heavier lifecycle data will live in `_lifecycle.json`.

## Consequences

### Positive

- First meaningful harness use can create useful repo-specific operating rules.
- Reviewer-specific repository policy has a durable home.
- Normal tasks avoid expensive bootstrap or freshness checks.
- The frequently read index stays small.
- Lifecycle maintenance remains possible without polluting agent context.
- Staleness is derived from repository facts instead of a potentially stale status flag.
- Rule refresh can be targeted to validation, agent-instruction, review-policy, or other affected sections.

### Negative / Tradeoffs

- The rule suite now has one additional role file and one lifecycle sidecar.
- Orchestrator logic must distinguish full bootstrap, schema migration, targeted refresh, and repair.
- Some lifecycle checks require comparing changed paths or reading `_lifecycle.json`.
- Repositories without git or with unusual source-control workflows may need lower-confidence lifecycle handling.

## Implementation Impact

- `rulebook` must define full-suite bootstrap, schema migration, targeted refresh, and repair.
- `rules-files.md` must require `reviewer.md` and `_lifecycle.json`.
- Orchestrator must add a Rule Suite Fast Path.
- Reviewer adapters must consult `docs/coding-agent/rules/reviewer.md`.
- Researcher output should support rule-suite bootstrap/freshness observations when requested.
- Worker report `rule_candidates[].audience` should allow `reviewer`.
- Package validation should check structure and references, not exact prose.
- Reviewer packets should include sparse repo-rule context when relevant.

## Validation

Validate the harness package with:

```bash
python scripts/validate_harness_package.py
python scripts/run_validation_smoke_tests.py
python skills/plan-format/scripts/validate_plan.py --file tests/fixtures/valid-plan.md --mode balanced
python skills/subagent-report-contract/scripts/validate_worker_report.py --file tests/fixtures/valid-worker-report.yaml
```

Additional validation:

- Verify package validation checks that rulebook lifecycle references exist.
- Verify package validation checks that Reviewer adapters mention `reviewer.md`.
- Verify Worker report validation accepts `rule_candidates[].audience: reviewer`.
- Verify no runtime adapter inlines the full bootstrap lifecycle or full latent-risk checklist.
- Verify the index template remains compact and points to `_lifecycle.json`.

## Revisit When

- Agent runtimes gain portable, repo-independent lifecycle hooks that can maintain rule freshness without prompt-token overhead.
- The harness introduces generated runtime adapters or generated rule templates.
- Repeated rule-refresh misses show that `_lifecycle.json` needs a stricter schema.
- Repository bootstrap becomes automated through a dedicated, explicitly invoked repo setup workflow.

## More Information

- `plugins/coding-agent-orchestration-harness/skills/rulebook/SKILL.md`
- `plugins/coding-agent-orchestration-harness/skills/rulebook/references/rules-files.md`
- `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/SKILL.md`
- `plugins/coding-agent-orchestration-harness/agents/Reviewer.md`
- `docs/coding-agent-orchestration-harness/decisions/ADR-D-0005-runtime-prompt-budgeting.md`
- `docs/coding-agent-orchestration-harness/decisions/ADR-I-0003-contract-first-validation-strategy.md`
