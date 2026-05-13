# Rule Suite Templates

Use these templates for full bootstrap, schema migration, or repair. Replace `<suite-id>` and dates during creation.

## Shared Front Matter

Each role rule file uses this minimum front matter:

```yaml
---
rule_schema_version: 2
suite_id: "<suite-id>"
rule_file: "worker"
last_updated: "YYYY-MM-DD"
---
```

Use the appropriate `rule_file` value: `common`, `worker`, `orchestrator`, or `reviewer`.

## index.md

```md
---
rule_schema_version: 2
suite_id: "<suite-id>"
lifecycle_manifest: "docs/coding-agent/rules/_lifecycle.json"
required_files:
  - "common.md"
  - "worker.md"
  - "orchestrator.md"
  - "reviewer.md"
---

# Coding Agent Rules Index

Read these files by role:

- `common.md`: shared repository facts, validation contract, safety boundaries.
- `worker.md`: Worker execution and validation mapping.
- `orchestrator.md`: planning, dispatch, integration, git, and rule maintenance.
- `reviewer.md`: review-specific repository policy and recurring risk hotspots.

## Rule Freshness

Do not read `_lifecycle.json` during normal work.

Use `_lifecycle.json` only when:
- required rule files are missing or suite IDs do not match;
- schema migration or rule-suite repair is needed;
- the task changes CI, validation, build, agent-instruction, or rule-source files;
- repository facts contradict the rules;
- targeted rule refresh is needed.
```

## common.md

```md
---
rule_schema_version: 2
suite_id: "<suite-id>"
rule_file: "common"
last_updated: "YYYY-MM-DD"
---

# Common Repository Rules

## Repository Reference Documents

- None recorded yet.

## Repository-Specific Validation Commands

- None recorded yet.

## Repo Safety / Boundaries

- None recorded yet.

## Repo Naming / Structure

- None recorded yet.
```

## worker.md

```md
---
rule_schema_version: 2
suite_id: "<suite-id>"
rule_file: "worker"
last_updated: "YYYY-MM-DD"
---

# Worker Repository Rules

## Repo-Specific Worker Notes

- None recorded yet.

## Repo CI / Checks Mapping

| Change Type | Required Checks | Notes |
|---|---|---|

## Mechanical Gate Candidates

- None.
```

## orchestrator.md

```md
---
rule_schema_version: 2
suite_id: "<suite-id>"
rule_file: "orchestrator"
last_updated: "YYYY-MM-DD"
---

# Orchestrator Repository Rules

## Repo-Specific Orchestrator Policies

- None recorded yet.

## Repo-Specific Integration / Git Policy

- None recorded yet.

## Rule Suite Refresh Notes

- None.
```

## reviewer.md

```md
---
rule_schema_version: 2
suite_id: "<suite-id>"
rule_file: "reviewer"
last_updated: "YYYY-MM-DD"
---

# Reviewer Repository Rules

## Repo-Specific Reviewer Notes

## Review Risk Hotspots

Suggested durable review categories:
- public_api_compatibility
- public_surface_completeness
- diagnostic_fidelity
- build_config_parity
- strict_ci_hygiene
- entrypoint_intent
- admission_before_side_effect
- collection_semantics
- runtime_model_compatibility
- abstraction_value_searchability
- canonical_policy_path
- authority_vs_derived_data
- failure_mode_completeness
- semantic_consistency
- validation_boundary_correctness
- risk_based_test_coverage

## Required Reviewer-Owned Evidence

| Trigger | Evidence Required | Source |
|---|---|---|

## Review Heuristics

Repository-specific review checks that are not mechanical gates and not tied to one tool.

## Recurring Misses And Prevention

Durable patterns learned from prior review misses, phrased as reusable prevention rules.

## Mechanical Gate Candidates

Checks that should eventually move into scripts, validators, CI, or package validation.
```
