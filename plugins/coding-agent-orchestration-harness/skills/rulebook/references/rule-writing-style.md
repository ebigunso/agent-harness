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
- “Workers must not edit files outside owns, except a minimal touch their own edit needs to meet the acceptance criteria or a change a packet pre-ruling names, reported either way; anything else is surfaced and waits for a ruling.”

Bad:
- “Try to run tests when possible.”
- “Be careful with changes.”

Deduplication:
- If a new rule overlaps an old rule, merge them rather than adding a near-duplicate.

Placement:
- If it is repo-specific (commands, paths, CI mapping), keep it in normal sections.

From a lesson:
- A rule written from a lesson takes the wording `improvement-loop/references/settling-lessons.md` asks for.
