# Rule Suite Bootstrap Lifecycle

## Full Suite

Bootstrap always creates all five rule files plus `_lifecycle.json`:

- `docs/coding-agent/rules/index.md`
- `docs/coding-agent/rules/common.md`
- `docs/coding-agent/rules/worker.md`
- `docs/coding-agent/rules/orchestrator.md`
- `docs/coding-agent/rules/reviewer.md`
- `docs/coding-agent/rules/_lifecycle.json`

## Write Order

1. `common.md`
2. `worker.md`
3. `orchestrator.md`
4. `reviewer.md`
5. `_lifecycle.json`
6. `index.md`

`index.md` is written last and acts as the success marker.

## Derived Validity

Do not rely on a stored status flag alone.

A rule suite is valid when:

- `index.md` exists;
- required files exist;
- role rule files share `suite_id`;
- `_lifecycle.json` exists;
- schema version matches the plugin-required schema;
- no relevant source drift or contradiction is known.

## Full Bootstrap Triggers

Run full bootstrap when:

- no valid `index.md` exists;
- required files are missing;
- `_lifecycle.json` is missing;
- suite IDs do not match;
- old skeleton-only files are present;
- manifest integrity cannot be established.

## Schema Migration Triggers

Run schema migration when:

- rule files exist, but schema version is older than plugin-required schema.

Schema migration should be targeted. For schema v2, add or refresh `reviewer.md` and lifecycle metadata without rediscovering the whole repository unless existing rules are also invalid.

## Targeted Refresh Triggers

Run targeted refresh when:

- the current task edits lifecycle refresh-source paths;
- source drift is detected through the sidecar;
- Worker, Reviewer, Researcher, CI, or user feedback contradicts existing rules.

## Repair Triggers

Run repair when:

- required files or front matter are missing;
- role rule files disagree on `suite_id`;
- `index.md` points to missing required files;
- `_lifecycle.json` cannot be parsed or does not name the required files.

Repair should restore suite integrity with the least repository rediscovery needed.

## Runtime Fast Path

Do not run bootstrap as a per-task ritual.

For trivial tasks, skip rule-readiness checks unless the task directly edits rule files, CI, validation sources, build manifests, or agent instruction files.

For non-trivial tasks, read `index.md` only when repo rules are needed for planning, validation, review, or repository-specific constraints.

Read `_lifecycle.json` only for bootstrap, repair, schema migration, targeted refresh, source-drift diagnosis, or contradiction handling.
