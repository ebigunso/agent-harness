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
- `index.md` and role rule files share `suite_id`;
- `_lifecycle.json` exists;
- schema version matches the plugin-required schema;
- no relevant source drift or contradiction is known.

## Decision Records Detection And Placement

During full bootstrap, detect candidate decision-record conventions: `docs/decisions/`, `docs/adr/`, and `ADR-*` file globs — scoped to tracked paths only (`git ls-files`), since gitignored trees such as review worktrees or vendored sibling checkouts can carry another repository's ADRs and must never count as this repository's convention.

Record the resulting Decision Records line in `common.md` and always report what was recorded in the bootstrap output; a detected convention (outcome 1) is recorded without a confirmation step. Three outcomes:

1. Convention detected: point at it — `Decision records: follow <path>; match the existing ADRs' numbering and sections.`
2. No convention, placement approved: the Orchestrator copies the two drop-ins from `skills/durable-docs-authoring/references/` — `adr-template.md` to `docs/decisions/template.md` and `adr-repo-readme.md` to `docs/decisions/README.md` (track directories are created on the first ADR). The pointer then reads as outcome 1, at `docs/decisions/`.
3. No convention, placement declined: record the harness-default form — `Decision records: no repo convention — harness default template applies (durable-docs-authoring references/adr.md).` Re-offer placement only at rule-suite refresh, never per task.

Placement is a repository mutation and is gated on explicit user approval at bootstrap time.

At targeted refresh, verify the Decision Records line against tracked paths only (`git ls-files`, the same scope as bootstrap detection) and flag any contradiction (pointer to a missing convention, or an unrecorded tracked convention present) to the user.

## Philosophy Lines

At full bootstrap and at every targeted refresh, the Repository Reference Documents section of `common.md` holds exactly one line for each of the two philosophies, product and engineering, in one of the four forms `references/rules-files.md` gives. For each philosophy:

- An existing pointer line is left as it is. At refresh, a pointer whose file is gone or moved is flagged to the user and the line left unchanged; removing or repointing it is on the owner's word (`skills/value-documents/SKILL.md`).
- An existing awaiting line is left as it is, except that a file it names that is gone drops from it: the files that remain, even one alone, still await the person's word, and with none left it becomes the none-yet line.
- With neither a pointer line nor an awaiting line, look among tracked paths only (`git ls-files`, the same scope as decision-record detection) for a document that states, in whatever words, that it is this repository's product philosophy or its engineering philosophy and that carries a ratification record, the owner's quoted words with a date, as `skills/value-documents/SKILL.md` requires of every philosophy. This is how setup looks, not a form a philosophy must take. A file a none-yet line names as not the philosophy is never recorded or brought to the person again.
  - Exactly one such document, plainly this repository's own: record its pointer line without asking.
  - Exactly one, but it looks as if it may belong to something else in the repository: write the awaiting line naming it, not its pointer line and not the none-yet line, and bring it to the person in the report. Judge this from where the file sits and what the files around it are: a file inside a vendored project, an example or a test fixture may state what it is for that project rather than for this repository.
  - More than one, wherever each sits: record none and write the awaiting line naming every one, not the none-yet line, and bring them to the person in the report to pick.
  - None: write the none-yet line.
  - A none-yet line keeps naming any file the line it replaces named as not the philosophy.
- The person's objection to a pointer setup recorded replaces the line with the none-yet line naming that file. The person's word on an awaiting line replaces it: yes to one of its files, with that file's pointer line, and nothing is written about the others; no to all of them, with the none-yet line naming each.

Report, in the bootstrap or refresh output, line by line and only for a line this run wrote: a pointer line recorded, with its file; an awaiting line written, with each file it names, for a single file why it may belong to something else, and that the person's word decides: yes to one file records its pointer, no to all leaves the philosophy none yet and none of them is recorded or brought again; a none-yet line written, with what the philosophy gives and that it starts by opening a Counsel session. A none-yet or awaiting line that was already there is not reported again, so each is told once, when its line is first written. A pointer whose file is gone or moved is flagged in every refresh that finds it so, whether or not any line changed. Nothing else is reported as missing.

Setup never writes, drafts, starts, templates or offers a form for a philosophy's content, and infers none from the repository's code or documents: a philosophy comes only from discussion with the person entitled to state it.

## Full Bootstrap Triggers

Run full bootstrap when:

- no valid `index.md` exists;
- required files are missing;
- `_lifecycle.json` is missing;
- `index.md` and role rule file suite IDs do not match;
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
- `index.md` and role rule files disagree on `suite_id`;
- `index.md` points to missing required files;
- `_lifecycle.json` cannot be parsed or does not name the required files.

Repair should restore suite integrity with the least repository rediscovery needed.

## Runtime Fast Path

Do not run bootstrap as a per-task ritual.

For trivial tasks, skip rule-readiness checks unless the task directly edits rule files, CI, validation sources, build manifests, or agent instruction files.

For non-trivial tasks, read `index.md` only when repo rules are needed for planning, validation, review, or repository-specific constraints.

Read `_lifecycle.json` only for bootstrap, repair, schema migration, targeted refresh, source-drift diagnosis, or contradiction handling.
