# Rule Suite Fast Path

Use this reference when performing the Repository Rule Entry load in detail, or when tempted toward rule lifecycle work (bootstrap, repair, schema migration, targeted refresh) to decide whether it is actually needed.

## Repository Rule Entry (full procedure)

For repository coding tasks, perform the minimal repository rule load before planning, editing, dispatching subagents, or selecting validation/review policy:

1. Check for `docs/coding-agent/rules/index.md`.
2. If the repository rule suite is present, read the relevant rule files for the current main-thread role:
   - `docs/coding-agent/rules/common.md`
   - `docs/coding-agent/rules/orchestrator.md`
3. Treat this as rule instruction loading, not as full rule-suite readiness work.
4. Do not read `_lifecycle.json`, bootstrap rules, refresh rules, or run `rulebook` unless the fast path below or the task itself requires lifecycle work.
5. If the repository rule files are absent or unreadable, continue under the `orchestration-harness` skill and record the missing rule context when it materially affects planning or validation.

## Fast Path Rules

Do not run repository rule bootstrap as a per-task ritual.

The Repository Rule Entry minimal load is not a full rule-readiness check. The fast path still skips lifecycle/bootstrap/refresh checks for clearly trivial work unless the task touches rule-relevant paths or otherwise needs rule lifecycle work.

For trivial work, skip rule-readiness checks unless the task directly touches:

- `docs/coding-agent/rules/**`;
- CI or validation sources;
- build/package manifests;
- agent instruction files;
- known refresh-source paths from lifecycle metadata that was already read for prior lifecycle work.

Do not read `_lifecycle.json` solely to decide whether trivial work can stay on the fast path. If refresh-source matching is unknown and no other trigger applies, keep the trivial fast path.

For non-trivial work, use repo rules when they are needed for planning, validation, review policy, or repository-specific constraints.

Fast path:

1. Read `docs/coding-agent/rules/index.md` only when repo rules are relevant.
2. If `index.md` exists, schema matches, required files exist, and no current task signal invalidates the rules, use the relevant role rule files.
3. Do not read `_lifecycle.json` unless lifecycle work is needed.

## When To Use `rulebook`

Use `rulebook` for:

- full bootstrap when the suite is missing or corrupt;
- schema migration when schema is outdated;
- targeted refresh when rule-source files changed or contradictions are found;
- repair when required files or suite IDs do not match.

If required validation cannot be selected confidently because rules are missing or stale, bootstrap or refresh the rule suite before dispatching Worker tasks, unless explicitly waived with rationale.
