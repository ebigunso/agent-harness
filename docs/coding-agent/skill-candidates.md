# Harness Migration Candidates

Purpose:
- Stage cross-repository improvements discovered during target-repository work.
- These are not active repo rules.
- These should be picked up by a later harness-maintenance PR/issue.

## Candidates

### HMC-20260908-validator-check-exact-enum-owner

- Status: staged
- Category: validator
- Proposed home: `plugins/coding-agent-orchestration-harness/skills/skills-maintenance/SKILL.md` (validator authoring guidance) or the relevant check in `plugins/coding-agent-orchestration-harness/scripts/validate_harness_package.py`
- Generalized rule:
  When adding package validation for an enum or schema change, check the exact enum owner or contract field rather than a broad substring.
- Trigger:
  A validator check is added or changed for an enum value, schema key, or contract field.
- Evidence from this repo:
  Carried over from the legacy "Global Migration Candidates" section of `docs/coding-agent/rules/common.md`, removed on 2026-09-08 under the boundary ADR-D-0026 carries (rule files carry active policy only).
- Why this generalizes:
  Substring checks fire on unrelated text and miss the owning field; the mistake recurs in any repository that grows validators.
- Suggested change:
  Add the rule to validator authoring guidance and audit existing substring checks.
