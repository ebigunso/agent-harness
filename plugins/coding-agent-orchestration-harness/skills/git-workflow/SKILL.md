---
name: git-workflow
description: Standardizes safe Git workflow decisions for branch safety, logical commit chunking, commit hygiene, and explicit non-interactive or non-destructive defaults. Use when planning or executing commit-affecting work, checking whether a commit should proceed, deciding how to split changes into coherent commits, or routing shared-state Git mutations through the Orchestrator.
---

# Skill: git-workflow

This skill is the cross-repo home for safe Git workflow procedure.

It defines how to:
- keep each commit scoped to one coherent intent
- gate commits on branch safety before mutating shared state
- keep Git usage non-interactive and non-destructive by default
- preserve the Orchestrator as the default owner for shared-state Git mutations

---

## Core rules (always apply)

1) One coherent intent per commit
- Default to one logical change per commit unless the user explicitly requests a different grouping.
- Do not mix unrelated behavior changes, refactors, formatting churn, or follow-up fixes into the same commit when they can be separated cleanly.

2) Pre-commit branch gate
- Before creating a commit, verify the current branch.
- If the branch is `main` or `develop`, stop and do not commit unless the user explicitly waives that gate.
- This skill defines the safety check, not repo-specific branch naming or release policy.

3) Shared-state Git mutations stay Orchestrator-controlled by default
- Commits, branch creation or switching, rebases, merges, resets, pushes, pulls that update shared state, and similar Git mutations remain Orchestrator-controlled unless explicitly delegated.
- Worker and other subagents should not assume they may mutate shared Git state just because this skill is active.

4) Prefer non-interactive Git usage
- Use explicit command flags and messages rather than opening editors or interactive consoles.
- Prefer deterministic commands that are easy to audit in logs and easy for the user to review afterward.
- If separating changes would require interactive staging or risky history editing, pause and escalate instead of improvising.

5) Prefer non-destructive defaults
- Prefer inspection commands first (`git status`, `git diff`, `git log`, `git show`) before any mutation.
- Do not use destructive commands such as hard resets, checkout-style reverts, or aggressive cleans unless the user explicitly requests or approves them.
- Route failure recovery and branch-state troubleshooting to `workspace-troubleshooting` instead of expanding this skill into a troubleshooting runbook.

6) Keep the skill cross-repo
- Keep branch protection, naming conventions, review policy, and release flow in repo-specific rules when needed.
- This skill should define reusable procedure and safety gates, not repository policy.

---

## Progressive disclosure (read only what you need)

If you need the ordered gate before a commit-affecting mutation:
- Read `references/pre-commit-gate.md`

If you need guidance on splitting work into logical commits and writing clean commit messages:
- Read `references/logical-commit-chunking.md`

If you need explicit defaults for safe Git command selection:
- Read `references/safe-git-defaults.md`

If you are creating or updating a PR, or driving an external review loop (e.g. Copilot re-review, thread closeout):
- Read `references/pr-authoring.md`

If Git behavior is failing, branch state looks wrong, or the workspace appears out of sync:
- Use `workspace-troubleshooting` rather than adding troubleshooting steps here.
