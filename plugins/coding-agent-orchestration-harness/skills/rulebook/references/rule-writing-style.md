# Rule Writing Style

Goal: rules should be *checkable* and reduce rework.

Prefer:
- One sentence per rule.
- Clear scope and trigger.
- Concrete “must/must not” language.
- Promote at the evidenced scope, not the broadest phrasing the incident could support.

Examples:

Good:
- “If you touch paths mapped to CI checks, you must run those checks before reporting done, unless explicitly waived by the user.”
- “Workers must not edit files outside owns; if unavoidable, they must explain why in the report.”

Bad:
- “Try to run tests when possible.”
- “Be careful with changes.”

Deduplication:
- If a new rule overlaps an old rule, merge them rather than adding a near-duplicate.

Migration staging:
- If a rule is cross-repo and procedural, stage it in `docs/coding-agent/skill-candidates.md` or `docs/coding-agent/skill-drafts/*.md`.
- If it is repo-specific (commands, paths, CI mapping), keep it in normal sections.
