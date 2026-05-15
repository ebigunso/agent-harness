---
status: accepted
adr_type: design
date: 2026-05-16
deciders:
  - ebigunso
consulted:
  - GPT-5.5 Pro
informed: []
supersedes: []
superseded_by: null
---

# ADR-D-0007: Separate Repository Rules From Harness Migration Candidates

## Context and Problem Statement

The harness now maintains a full repository rule suite under `docs/coding-agent/rules/*.md` and supports Worker report fields for both repo-local rules and staged cross-repository harness improvements.

Without a durable boundary, runtime agents can blur two different kinds of findings:

- active operating rules for the target repository; and
- reusable harness-global improvements that need later harness-maintenance work.

That blur makes ordinary target-repository runs look like they are allowed to mutate bundled harness skills, references, adapters, validators, or plugin package validation. It also risks reintroducing old schema shapes such as `global_candidate`, `global-skill`, or role-file "Global Migration Candidates" sections.

## Decision Drivers

- Preserve the target repository rule suite as live repo-local operating policy.
- Keep cross-repository harness improvements out of role rule files.
- Give runtime agents a safe staging path for reusable harness improvements discovered during ordinary target-repository work.
- Prevent old global-candidate shapes from returning through plans, adapters, validators, or rule templates.
- Keep bundled harness maintenance explicit and intentional.

## Decision

Runtime agents maintain target-repository operating rules under:

- `docs/coding-agent/rules/index.md`
- `docs/coding-agent/rules/common.md`
- `docs/coding-agent/rules/worker.md`
- `docs/coding-agent/rules/orchestrator.md`
- `docs/coding-agent/rules/reviewer.md`
- `docs/coding-agent/rules/_lifecycle.json`

`rule_candidates` are always repo-local. They route by audience to active target-repository rule files and repo-local candidate sections.

Cross-repository harness improvements discovered during target-repository work are not written directly into bundled skills, references, agents, validators, or plugin files. They are staged for later harness-maintenance work as `harness_migration_candidates` and recorded under:

- `docs/coding-agent/skill-candidates.md`
- `docs/coding-agent/skill-drafts/*.md`, when a fuller draft is useful

This is a runtime boundary, not only a schema cleanup. Ordinary target-repository agents stage global improvements locally; later harness-maintenance work migrates accepted candidates into plugin code.

Bundled harness skills, references, adapters, and validators may be edited directly only during an explicit harness-maintenance task, or when the target repository is the harness repository and the requested task is to modify the plugin.

## Rejected Legacy Shapes

The following shapes are rejected:

- `rule_candidates[].intended_home: global_candidate`
- `lesson_candidates[].promotion_target: global-skill`
- `lesson_candidates[].promotion_target: references/*`
- `Global Migration Candidates` sections inside role rule files such as:
  - `common.md`
  - `worker.md`
  - `orchestrator.md`
  - `reviewer.md`

These shapes blur the boundary between active target-repository rules and proposed harness-global changes.

`rule_candidates` are now repo-local only.

Cross-repository harness improvements must be staged as `harness_migration_candidates` and recorded under:

- `docs/coding-agent/skill-candidates.md`
- `docs/coding-agent/skill-drafts/*.md`, when a fuller draft is useful

## Considered Options

### Option 1: Keep role-file "Global Migration Candidates" sections

This keeps all repo-discovered findings in the rule suite, but makes role rule files carry inactive harness-maintenance proposals beside active target-repository policy.

Rejected because it makes rule files ambiguous and encourages ordinary target-repository agents to treat harness-global proposals as live repo rules.

### Option 2: Keep `rule_candidates[].intended_home: global_candidate`

This preserves the old report shape, but keeps global migration routing inside the repo-rule candidate field.

Rejected because `rule_candidates` need a single meaning: repo-local rule updates.

### Option 3: Use lesson promotion targets such as `global-skill` or `references/*`

This routes reusable improvements through lesson candidates, but points runtime agents toward direct bundled skill/reference edits.

Rejected because ordinary target-repository work should stage harness-global ideas, not mutate bundled harness files.

### Option 4: Split repo-local rules from harness migration candidates

Chosen. Repo-local rules remain active operating policy. Harness-global proposals are staged separately as migration candidates for explicit harness-maintenance work.

## Decision Outcome

Chosen option: **Option 4**.

The harness keeps `rule_candidates` repo-local and uses `harness_migration_candidates` plus `docs/coding-agent/skill-candidates.md` or `docs/coding-agent/skill-drafts/*.md` for staged cross-repo improvements.

## Consequences

### Positive

- Role rule files remain focused on active target-repository policy.
- Runtime agents have a clear path for reusable harness improvements without editing bundled harness files.
- Validators can reject old global-candidate schema and promotion targets.
- Harness-maintenance work can review staged candidates with explicit intent and provenance.

### Negative / Tradeoffs

- Orchestrator integration must collect and route an additional candidate list.
- Some useful cross-repo ideas remain staged until explicit harness-maintenance work migrates them.
- Historical completed plans or ADRs may still mention rejected legacy shapes as context; current runtime surfaces must not reintroduce them as accepted routes.

## Implementation Impact

- Worker report contract keeps `rule_candidates` repo-local and validates `harness_migration_candidates`.
- Rulebook applies `rule_candidates` by audience to repo rule files and stages harness migrations separately.
- Runtime adapters must avoid `global-skill`, `references/*`, and direct bundled harness edit guidance during ordinary target-repository work.
- Wave integration and closeout should aggregate `harness_migration_candidates` for Orchestrator curation.
- Package validation should guard against reintroducing rejected legacy shapes in current authoritative surfaces.

## Validation

Validate the split with:

```bash
python scripts/validate_harness_package.py
python scripts/run_validation_smoke_tests.py
python skills/subagent-report-contract/scripts/validate_worker_report.py --file tests/fixtures/valid-worker-report.yaml
python skills/subagent-report-contract/scripts/validate_worker_report.py --file tests/fixtures/invalid-worker-report-intended-home.yaml
python skills/subagent-report-contract/scripts/validate_worker_report.py --file tests/fixtures/invalid-worker-report-lesson-target.yaml
```

Additional validation:

- Verify current role rule templates do not include "Global Migration Candidates" sections.
- Verify current rulebook references do not route `rule_candidates` by `global_candidate` or `intended_home`.
- Verify current runtime adapters stage harness-global ideas in `docs/coding-agent/skill-candidates.md` or `docs/coding-agent/skill-drafts/*.md`.

## Revisit When

- The harness introduces a dedicated migration workflow that consumes `docs/coding-agent/skill-candidates.md`.
- Runtime environments gain a first-class, audited mechanism for proposing plugin updates without editing bundled files during target-repository work.
- Repo rule suites gain a machine-readable candidate sidecar that can distinguish active rules from staged suggestions without prompt bloat.

## More Information

- `plugins/coding-agent-orchestration-harness/skills/rulebook/SKILL.md`
- `plugins/coding-agent-orchestration-harness/skills/rulebook/references/rules-files.md`
- `plugins/coding-agent-orchestration-harness/skills/rulebook/references/skill-candidates-file.md`
- `plugins/coding-agent-orchestration-harness/skills/subagent-report-contract/SKILL.md`
- `plugins/coding-agent-orchestration-harness/skills/subagent-report-contract/scripts/validate_worker_report.py`
- `docs/coding-agent-orchestration-harness/decisions/ADR-D-0006-repository-rule-suite-bootstrap-lifecycle.md`
