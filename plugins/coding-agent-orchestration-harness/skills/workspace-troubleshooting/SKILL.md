---
name: workspace-troubleshooting
description: Triage runbook for workspace failures, with references for stale view or branch mismatch, GitHub CLI auth failures, and unexpected external file changes, and the home of the record of what the machine the work runs on is known to do. Use when an Orchestrator session starts or a seat is dispatched (the machine's record), when an obstacle of the machine has been got past, when the user's view of the repository differs from yours, gh auth fails mid-task, files change without your edits, or a command fails or behaves unexpectedly and needs systematic triage before remediation.
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

If you see “external changes” (formatter/user/tool edits) and need to decide whether to pause:
- Read references/external-changes-triage.md

If the user reports missing changes or your view doesn’t match theirs:
- Read references/stale-view-or-branch-mismatch.md

If gh CLI auth fails mid-task or a session assigned real-GitHub validation reports an invalid stored token:
- Read references/github-cli-auth-failures.md

---

## What this machine is known to do

What is known about the obstacles of the machine the work runs on (a command that fails here, a tool that is missing, a check that stops a session) reaches every new seat and every new Orchestrator session when it starts, so that an obstacle one seat has got past is not paid for again by the next. Instinct goes wrong by keeping the way past in the context of the session that found it, where it ends with that session, or by writing it into a lesson or a note the repository tracks.

- Where: one file, `harness-machine-obstacles.md`, in the directory `git rev-parse --git-common-dir` names. Why there: every working tree of the repository reads the same file, and it is never pushed.
- The line: nothing particular to a machine goes into a tracked file. What would hold on any machine is troubleshooting knowledge and goes as the next section states; only what is particular to this machine goes into the record.
- An Orchestrator session reads the record when it starts. A dispatch names it, and carries the entries that apply to the work where the seat cannot read that directory (a sandbox may keep it out). An Auditor is the one seat a dispatch cannot carry entries to, its dispatch being a fixed template: it reads the record itself, and where that read fails the record has not reached that seat, the auditor says so in what it returns, and the session that dispatched it records that as a limit of that dispatch in the plan's or run's log and does not count the record as delivered there.
- Each entry states four things: what was met; where it applies (the system, shell, tool and version, or kind of session); when it was last seen; how it was got past.
- The session that met the obstacle writes the entry. A seat that cannot write there tells of it in its report, and the session that integrates the report writes it.
- An entry is true as of its date and is not trusted for ever. Work that comes to where an entry applies checks it again: it renews the date where the obstacle is still there, and corrects or removes the entry where it is not or the way past no longer works.

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
