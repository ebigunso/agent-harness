# Lifecycle Sidecar

`docs/coding-agent/rules/_lifecycle.json` is compact, machine-readable lifecycle data for the repository rule suite.

It should stay out of normal task context. Read it only for bootstrap, repair, schema migration, targeted refresh, source-drift diagnosis, or contradiction handling.

## Minimum Shape

```json
{
  "rule_schema_version": 2,
  "suite_id": "rules-<timestamp-or-id>",
  "bootstrapped_at": "<iso8601>",
  "baseline": {
    "kind": "worktree",
    "description": "Initial repository rule-suite bootstrap."
  },
  "required_files": {
    "index": "docs/coding-agent/rules/index.md",
    "common": "docs/coding-agent/rules/common.md",
    "worker": "docs/coding-agent/rules/worker.md",
    "orchestrator": "docs/coding-agent/rules/orchestrator.md",
    "reviewer": "docs/coding-agent/rules/reviewer.md"
  },
  "refresh_groups": {
    "validation": {
      "patterns": [
        ".github/workflows/**",
        ".gitlab-ci.yml",
        "package.json",
        "Cargo.toml",
        "pyproject.toml",
        "go.mod",
        "Makefile",
        "Justfile",
        "Taskfile.yml"
      ],
      "affects": [
        "common.validation_commands",
        "worker.check_mapping",
        "reviewer.required_evidence"
      ]
    },
    "agent_instructions": {
      "patterns": [
        "AGENTS.md",
        "CLAUDE.md",
        "GEMINI.md",
        ".github/copilot-instructions.md",
        ".github/instructions/**"
      ],
      "affects": [
        "common.reference_documents",
        "orchestrator.repo_policies"
      ]
    },
    "review_policy": {
      "patterns": [
        "CONTRIBUTING.md",
        "docs/testing/**",
        "docs/development/**",
        "docs/coding-agent/lessons/**"
      ],
      "affects": [
        "reviewer.review_risk_hotspots",
        "reviewer.copilot_finding_prevention"
      ]
    }
  },
  "source_evidence": []
}
```

## Guidance

- Keep the sidecar small enough for lifecycle work, but do not optimize it for normal prompt reads.
- Store refresh-source path patterns and the rule sections they affect.
- Store source evidence as compact records that explain where a rule fact came from.
- Do not use Git commit SHAs as the standard baseline. Squash and rebase merges can remove PR-local commits from target-branch history, so freshness should be derived from source paths, schema, suite integrity, and contradiction signals instead.
- Do not store durable `stale`, `partial`, or `skeletal` flags as the main lifecycle mechanism.
- Derive validity from required files, suite IDs, schema version, source drift, and contradiction reports.
