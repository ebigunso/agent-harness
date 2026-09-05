---
rule_schema_version: 2
suite_id: "rules-20260513-b80f05e"
rule_file: "worker"
last_updated: "2026-09-05"
---

# Worker Repository Rules

## Repo-Specific Worker Notes

- Keep Worker edits within assigned `owns` scope.
- Do not perform shared-state Git mutations unless the Orchestrator explicitly assigns them.
- Do not edit `docs/coding-agent/rules/*.md`; return `rule_candidates` for Orchestrator curation instead.
- Keep runtime adapter changes compact and route shared behavior through plugin skills/references.
- When authoring a reference that encodes a contract (enum, path scheme, fixed template, vocabulary) whose authoritative source is not yet ratified, mark the field TBD and report it — never invent values.

## Repo CI / Checks Mapping

| Change Type | Required Checks | Notes |
|---|---|---|
| Harness package structure, manifests, runtime role map, adapter references, rulebook lifecycle references, or latent-risk reference links | `python scripts/validate_harness_package.py` | Run from `plugins/coding-agent-orchestration-harness/`. |
| Cross-harness validation plumbing or Codex bootstrap behavior | `python scripts/run_validation_smoke_tests.py` | Run from `plugins/coding-agent-orchestration-harness/`; includes package validation and bootstrap smoke checks. |
| Plan-format skill or plan fixture changes | `python skills/plan-format/scripts/validate_plan.py --file tests/fixtures/valid-plan.md --mode balanced` | Add targeted plan fixture validation when a specific fixture is changed. |
| Worker report contract, schema, validator, or fixtures | `python skills/subagent-report-contract/scripts/validate_worker_report.py --file tests/fixtures/valid-worker-report.yaml` | Also validate any new or changed report fixture. |
| Reviewer rule-candidate audience support | `python skills/subagent-report-contract/scripts/validate_worker_report.py --file tests/fixtures/valid-worker-report-reviewer-candidate.yaml` | Required when `rule_candidates[].audience: reviewer` behavior is touched. |
| Documentation-only ADR, lessons, or rulebook prose changes | `git diff --check` plus Reviewer-owned diff review | Pair with package validators when docs affect validated structure. |
| `skills/git-workflow/scripts/**` (PR watcher or its self-check) | `bash skills/git-workflow/scripts/pr-comment-watch-selfcheck.sh` plus `bash -n` on both scripts | Run from `plugins/coding-agent-orchestration-harness/`; add a self-check case for every new output line, exit path, or member lifecycle transition (add, change, remove). Live `gh` smoke is read-only and supplementary. |

## Global Migration Candidates

- None.
