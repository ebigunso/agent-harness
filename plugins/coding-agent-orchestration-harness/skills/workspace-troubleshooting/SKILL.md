---
name: workspace-troubleshooting
description: Centralized troubleshooting runbook for recurring workspace/tool failures (npm install/test errors, Windows file locks, branch/state mismatches, unexpected external file changes, CI/validation confusion, flaky local E2E). Use when commands fail, installs break, permissions/EPERM/EBUSY errors occur, behavior differs from expectation, or a systematic triage process is needed.
---

# Skill: workspace-troubleshooting

This skill is the centralized location for cross-repo troubleshooting knowledge.

Goal:
- reduce repeated “rediscovery” of the same environment/tool failures
- standardize triage evidence collection and safe remediation steps
- make troubleshooting tips reusable across projects

---

## Core rules (always apply)

1) Capture minimal reproducible evidence first
Record:
- the exact command
- exit code
- relevant stdout/stderr
- working directory
- OS and runtime versions (node/npm, etc.) if relevant
- `git status --porcelain` and `git diff --name-only` if changes are involved

2) Prefer the smallest safe remediation
- avoid “shotgun” fixes that destroy context unless explicitly justified
- use reversible steps when possible

3) Never claim “done” when validation is required but missing
- if required validation can’t be run, the correct state is “blocked” or “needs revision” unless the user explicitly waives

4) Keep SKILL.md as routing guidance; put detailed runbooks in references
- Keep core rules high-level and stable.
- Put command-level recovery steps (including shell/cwd procedures) in `references/*` and link them from this file.

5) Use short recovery checklists for repeated failure patterns
- Prefer explicit, ordered mini-checklists (symptom → checks → safe remediation → validation rerun).
- Keep checklist steps minimal and reversible; avoid mixing multiple failure classes in one checklist.

---

## Progressive disclosure (read only what you need)

If npm install/ci fails on Windows with EPERM/EBUSY and locked native modules:
- Read references/windows-npm-eperm-locks.md

If you see “external changes” (formatter/user/tool edits) and need to decide whether to pause:
- Read references/external-changes-triage.md

If the user reports missing changes or your view doesn’t match theirs:
- Read references/stale-view-or-branch-mismatch.md

If failures might be caused by persistent shell cwd drift:
- Read references/persistent-shell-cwd-normalization.md

If a gRPC client hangs against a Docker Desktop published port on Windows while REST on a sibling port responds fast:
- Read references/windows-docker-grpc-localhost-ipv6.md

If PowerShell JSON array checks behave inconsistently for one-element arrays (cardinality validation after ConvertFrom-Json):
- Read references/powershell-json-array-cardinality.md

---

## How to contribute new troubleshooting knowledge

When you discover a reusable troubleshooting tip, propose it in this format (staged repo-locally):
- Title:
- Symptoms:
- Likely causes:
- Safe steps (ordered):
- Evidence to capture:
- Caveats / rollback:
- Scope (OS/toolchain/repo type):
