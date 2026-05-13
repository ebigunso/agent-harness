---
rule_schema_version: 2
suite_id: "rules-20260513-b80f05e"
rule_file: "reviewer"
last_updated: "2026-05-13"
---

# Reviewer Repository Rules

## Repo-Specific Reviewer Notes

- Review plugin changes against shared-skill centralization: adapters should stay compact and route to skills/references.
- Treat validation evidence as contract-first: structure and required evidence can be mechanically checked; prose quality and prompt-budget discipline need reviewer judgment.
- For rule-suite lifecycle work, verify `index.md` stays small and `_lifecycle.json` is not required for normal task reads.

## Review Risk Hotspots

- Public API compatibility: runtime agent names, plugin manifests, Codex bootstrap entrypoints, validator CLI flags, Worker report schema keys, and rule file names are compatibility surfaces.
- Derived/cached data: Codex bootstrap install manifests and rule-suite `_lifecycle.json` contain derived state that must not be treated as the sole source of truth.
- Build configuration / feature parity: Copilot, Claude, and Codex adapters should preserve shared semantics even when wording diverges for prompt budget.
- Diagnostics / telemetry: validator error messages should identify the exact missing field, enum, file, or evidence requirement.
- Entrypoint intent and admission: prefer one canonical script or entrypoint unless a concrete compatibility contract requires a wrapper.
- Async/runtime model: no repo-specific async runtime policy is recorded yet.
- Collection semantics: role maps, expected install file lists, manifest file arrays, rule-suite required files, and latent-risk reference lists should be kept complete and intentionally ordered when order affects validation or review.

## Required Reviewer-Owned Evidence

| Trigger | Evidence Required | Source |
|---|---|---|
| Runtime adapter changes | Confirm all affected Copilot, Claude, and Codex adapters preserve shared semantics without inlining full shared checklists. | `plugins/coding-agent-orchestration-harness/agents/`, `claude/agents/`, `codex/agent-templates/` |
| Package validator changes | Confirm checks remain structure-oriented and do not overfit exact skill prose. | `plugins/coding-agent-orchestration-harness/scripts/validate_harness_package.py` |
| Worker report contract changes | Confirm validator, schema reference, contract prose, and fixtures all agree on required keys and enum values. | `skills/subagent-report-contract/` |
| Rule-suite lifecycle changes | Confirm full-suite validity is derived from required files, shared `suite_id`, schema version, sidecar presence, and contradiction/source-drift signals. | `skills/rulebook/references/` |
| Plan lifecycle closeout | Confirm completed plans are moved under `docs/coding-agent/plans/completed/` and status is `done`. | `docs/coding-agent/plans/` |

## Copilot Finding Prevention

- After moving a plan from `active` to `completed`, update any durable lesson or ADR references to the completed path.
- When fast-path guidance says not to read a sidecar in normal work, do not add adjacent wording that implicitly requires reading the sidecar to decide triviality.
- For enum/schema package checks, verify the exact enum owner or contract field rather than broad token presence.

## Mechanical Gate Candidates

- Add or preserve package validation for required rulebook lifecycle references, Reviewer adapter `reviewer.md` references, Worker report reviewer-audience support, and latent-risk reference existence.
- Consider future validation for the repository rule suite itself once schema v2 settles enough to validate front matter and sidecar shape mechanically.

## Global Migration Candidates

- None.
