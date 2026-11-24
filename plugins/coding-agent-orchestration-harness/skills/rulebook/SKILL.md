---
name: rulebook
description: Maintains repository rule files under docs/coding-agent/rules/*.md. Use when bootstrapping, repairing, migrating, refreshing, updating repo rules, applying repo-local rule_candidates, or adding repo reference documents.
---

# Skill: rulebook

This skill defines how the Orchestrator maintains repository rule files as the source of truth for repo-specific constraints and operating rules.

This skill is for RULES.

---

## Core rules (always apply)

- Only the Orchestrator edits docs/coding-agent/rules/*.md (single-writer).
- Worker proposes repo-local rule_candidates; Orchestrator curates them.
- A rule that adds an obligation from a lesson is written only after the person's yes, and carries that yes, quoted with its date, where the rule is written. A rule candidate that is the prevention of a mistake is handled as a lesson and waits for that yes (`improvement-loop/references/settling-lessons.md`); one that records a fact of the repository (a command, a path) and adds no obligation is rule upkeep and is applied.
- A change that reverses or removes a rule takes the lessons about that rule out of the lessons log in the same change (`improvement-loop/references/settling-lessons.md`).
- New rules must be short, declarative, unambiguous.
- Deduplicate aggressively; avoid rule proliferation.
- Rule files hold the rules of the repository being worked on; work in a target repository never edits bundled harness files.
- Update last_updated when editing a rules file.
- Treat `docs/coding-agent/rules/index.md` as the low-token routing file and bootstrap success marker.
- Treat `docs/coding-agent/rules/_lifecycle.json` as the machine-oriented lifecycle sidecar. Read it only for bootstrap, repair, schema migration, targeted refresh, source-drift diagnosis, or contradiction handling.
- Do not run full rule-suite bootstrap as a per-task ritual.

---

## Progressive disclosure (read only what you need)

If you need the required structure and sections of each rules file:
- Read references/rules-files.md

When adding or updating a repository reference document, read `references/rules-files.md` (the common.md entry under Required sections).

If you need to decide whether to bootstrap, repair, migrate, or refresh the rule suite:
- Read references/bootstrap-lifecycle.md

When filling or refreshing the workspace's models record in `common.md`, read `references/bootstrap-lifecycle.md` (Models Record); for its record of sessions in `sessions.md`, the same reference (Sessions Record).

If you need template content for a new or repaired rule suite:
- Read references/rule-suite-templates.md

If you need lifecycle sidecar shape or refresh-source guidance:
- Read references/lifecycle-sidecar.md

Before writing, merging, or materially revising any repository rule, read `references/rule-writing-style.md`.

If you want an optional helper to update last_updated reliably:
- Run scripts/update_last_updated.py
