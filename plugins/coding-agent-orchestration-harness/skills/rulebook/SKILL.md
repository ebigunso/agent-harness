---
name: rulebook
description: Maintains repository rule files under docs/coding-agent/rules/*.md. Use when bootstrapping, repairing, migrating, refreshing, updating repo rules, applying rule_candidates, adding repo reference documents, or staging global migration candidates.
---

# Skill: rulebook

This skill defines how the Orchestrator maintains repository rule files as:
1) the source of truth for repo-specific constraints, and
2) a staging area for rules that should later be migrated into global settings.

This skill is for RULES. Skill creation/update is staged separately in docs/coding-agent/skill-candidates.md and drafts under docs/coding-agent/skill-drafts/.

---

## Core rules (always apply)

- Only the Orchestrator edits docs/coding-agent/rules/*.md (single-writer).
- Worker proposes rule_candidates; Orchestrator curates and applies them.
- New rules must be short, declarative, unambiguous.
- Deduplicate aggressively; avoid rule proliferation.
- Update last_updated when editing a rules file.
- Treat `docs/coding-agent/rules/index.md` as the low-token routing file and bootstrap success marker.
- Treat `docs/coding-agent/rules/_lifecycle.json` as the machine-oriented lifecycle sidecar. Read it only for bootstrap, repair, schema migration, targeted refresh, source-drift diagnosis, or contradiction handling.
- Do not run full rule-suite bootstrap as a per-task ritual.

---

## Progressive disclosure (read only what you need)

If you need the required structure and sections of each rules file:
- Read references/rules-files.md

If you need to decide whether to bootstrap, repair, migrate, or refresh the rule suite:
- Read references/bootstrap-lifecycle.md

If you need template content for a new or repaired rule suite:
- Read references/rule-suite-templates.md

If you need lifecycle sidecar shape or refresh-source guidance:
- Read references/lifecycle-sidecar.md

If you need style guidance for writing high-quality rules:
- Read references/rule-writing-style.md

If you need the required format for harness migration candidates:
- Read references/skill-candidates-file.md

If you want an optional helper to update last_updated reliably:
- Run scripts/update_last_updated.py
