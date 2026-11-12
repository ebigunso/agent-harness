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
- With neither a pointer line nor an awaiting line, look among tracked paths only (`git ls-files`, the same scope as decision-record detection) for a document that states, in whatever words, that it is this repository's product philosophy or its engineering philosophy and whose ratification is recorded, the owner's quoted words with a date, as `skills/value-documents/SKILL.md` requires of every philosophy: in its companion beside it (`<philosophy-stem>-companion.md`). This is how setup looks, not a form a philosophy must take. A file a none-yet line names as not the philosophy is never recorded or brought to the person again.
  - Exactly one such document, plainly this repository's own: record its pointer line without asking.
  - Exactly one, but it looks as if it may belong to something else in the repository: write the awaiting line naming it, not its pointer line and not the none-yet line, and bring it to the person in the report. Judge this from where the file sits and what the files around it are: a file inside a vendored project, an example or a test fixture may state what it is for that project rather than for this repository.
  - More than one, wherever each sits: record none and write the awaiting line naming every one, not the none-yet line, and bring them to the person in the report to pick.
  - None: write the none-yet line.
  - A none-yet line keeps naming any file the line it replaces named as not the philosophy.
- The person's objection to a pointer setup recorded replaces the line with the none-yet line naming that file. The person's word on an awaiting line replaces it: yes to one of its files, with that file's pointer line, and nothing is written about the others; no to all of them, with the none-yet line naming each.

Report, in the bootstrap or refresh output, line by line and only for a line this run wrote: a pointer line recorded, with its file; an awaiting line written, with each file it names, for a single file why it may belong to something else, and that the person's word decides: yes to one file records its pointer, no to all leaves the philosophy none yet and none of them is recorded or brought again; a none-yet line written, with what the philosophy gives and that it starts by opening a Counsel session. A none-yet or awaiting line that was already there is not reported again, so each is told once, when its line is first written. A pointer whose file is gone or moved is flagged in every refresh that finds it so, whether or not any line changed. Nothing else is reported as missing.

Setup never writes, drafts, starts, templates or offers a form for a philosophy's content, and infers none from the repository's code or documents: a philosophy comes only from discussion with the person entitled to state it.

## Models Record

At full bootstrap and at every targeted refresh, setup fills the workspace's record of options (`subagent-strategy/references/model-routing.md`, The record of options) for the Models And Peers In This Workspace section of `common.md`, in the form `references/rule-suite-templates.md` gives, dated the day it is filled. When it is written into `common.md` is set by the hold below.

- Options: what the runtime offers: the session's own model, each model its subagent mechanism can be dispatched on, and each kind of peer seat a session can create here (Sessions, below), with the model it runs on and the role it can hold. A seat that happens to exist is not an option: seats are created and ended by the session that uses them. With each goes the setting it runs at, as `model-routing.md` (The record of options) defines a setting: the reasoning effort the runtime lets a dispatch choose for each model, and the reasoning effort a seat can be created at. Setup reads these from the runtime and the workspace.
  - Two settings of one model are two options where they differ in what the model can do for some role's work, or in cost; settings that differ in neither are one option. Setup makes the capability finding and the cost judgement for each of them, and writes into the record only the options some role resolves to or falls back to. It knows them by resolving each reason first (Resolutions, below) and then keeping, for each resolution, the option it resolves to and the option it names for the unavailable case, where it names one, and no others. An option no resolution keeps is not listed, though its setting differs.
  - Where the runtime gives neither the dispatch nor the creation of a seat a choice of setting, the record states the setting the option runs at. A setting setup cannot read is recorded as not known, never inferred.
- Sessions: the means the workspace has to start a session in a role with a first message and without a person, to see from outside whether one is alive and whether it is working or waiting, and to end one. A run's Orchestrator session is started by them and a session creates and ends its seats by them, so the harness's text names no tool, and a tool that changes its commands changes this line and nothing else. Setup finds them in the installed runtimes' and tools' own documentation and, where the workspace's rules allow a session to be started, by one trial that changes no file and is ended once seen. Each is written with what must already be so for it to work, its date, and whether it was observed or only documented; what setup cannot establish is recorded as none found, never inferred.
- Tendencies: for each family among the options, the workspace's own dated observation where the record holds one or the owner states one at the hold; it replaces the seed for that family. Otherwise the seed's entry (`subagent-strategy/references/model-tendencies-seed.md`) with the seed's date. A family neither covers is recorded as not yet observed.
- Capability for the work: before resolving the reasons, setup takes what each option can do for each role's work, a model at each setting it may run at taken as an option of its own, from what is readily available: the runtime's or the provider's own statements of its models, and the workspace's own observations. Where that is not readily available, setup researches it through the Researcher role. At a first setup, with no confirmed record, the research goes as `model-routing.md` (Choosing where research goes) sends it where no recorded option fits: a Researcher subagent on the session's own model, never by the unconfirmed record; at a refresh it goes by the confirmed record. The research asks nothing of the owner and is not one of the hold's questions, and it completes before the record is shown at the hold, so the record shown carries every line the research and the reasons resolve, the cost-bounded lines awaiting what the owner states there.
- Resolutions: each role's reason (`model-routing.md`, Reasons by role) resolved against the options, their tendencies and what each can do for the work, one option per work type where the reason splits. Each resolution line names its option whole, the setting with the seat or subagent and the model, and names, dated, the capability finding it rests on, which is that option's and not its model's at another setting; the record keeps no other list of capabilities. Cost is judged the same way, for the option at its setting and never once for its model. Each resolution also names one option the role goes to when its own is unavailable at the time a dispatch is due, its fallback. Setup names one for each role and work type wherever an option exists that is on a different model or seat from the option it backs, that is capable for that work and that the role's cost setting accepts, which does not bind a role with no cost ceiling: the next such option below the resolution in that work's fit ranking. Another setting of the same model is never named as its fallback, since when a model cannot be run its other settings usually cannot either. It writes that none is named only where no such option exists; the owner may change the line at the hold, as any other. The fallback is written with its setting and, in a few words, the capability finding it rests on, as a resolution's own option is. Where none is named, or the named option is itself unavailable, the rule in `model-routing.md` (Tiers and fallback) decides. A reason whose cost setting turns on what the environment runs on or on the allowance is resolved once the owner has stated them and any limits his statement leaves out are researched (the hold below).

The record is held as Philosophy Lines holds an awaiting line: its status line says it awaits the owner's word, the bootstrap or refresh output brings it to him, and his word decides.

- Setup cannot observe what the environment runs on or the owner's budget allowance. What the environment runs on is asked for as enough to judge a model's cost against: which subscription plan, with its usage limits as he knows them, or how large a pay-as-you-go budget. It asks him for both at the hold, unless the record already holds what he stated, writes what he states, and infers neither. It then shows him the filled record, these lines included, and asks him to confirm it. These are the step's only questions: which model a role goes to is the reasons' to decide, and the owner may change any line at the hold.
- Where his answer names the kind of plan or budget without its limits or size, setup researches the named plan's limits by the same route as the capability research (Capability for the work, above) before it resolves the cost-bounded lines, and asks him nothing further for it. It writes what it found on the Runs on line with its source and date, kept apart from what he stated; where nothing can be found, the line says so and the walk's fallback for a budget whose limits are unknown (the Worker's reason, `model-routing.md`) applies. Once he has confirmed and the limits are researched, setup writes the cost-bounded lines resolved with their grounds, adds to the Options line the options those lines resolve to or fall back to, and reports them to him; no second confirmation is asked, since which model a role goes to is the reasons' to decide and he may change any line.
- A confirmation that names no allowance is valid: the record says none was stated, and the walk in the Worker's reason (`model-routing.md`) finds the cost-bounded options.
- Where `common.md` holds no confirmed record, setup writes the filled record there with its status line awaiting his word, and nothing is dispatched on it until he confirms.
- Where `common.md` holds a confirmed record (a record in an older form counts as confirmed), a refresh leaves that section untouched and in force, shows the filled record in the refresh output as proposed, and writes it into `common.md`, replacing the confirmed one, only on his confirmation.
- On his confirmation the status line records who confirmed and the date.

A refresh re-resolves the record against the options as they are then, redates it and holds it again; the lines the owner stated carry over as they are and are shown for him to keep or change, while limits setup researched are researched again. A record in an older form, routing by named strengths rather than by the reasons, is rewritten in this form: its dated observations and the lines the owner stated carry over into the lines that hold them, and a line this form has no place for is kept as it stands. A record that names no setting for its options is an older form in the same sense: it stays valid and in force as it stands, and a refresh brings it into the form with settings.

## Counsel Relay Admission

Before Counsel's relays are admitted, the owner asks for setup in the Orchestrator session directly, since no relay is yet admitted to carry it; once relays are admitted, a later refresh he directs reaches the session as any decision does. At full bootstrap, and again only at a targeted refresh, when Repository Reference Documents has no Counsel line, the report offers the standing approval that admits Counsel's relays: the entry `references/rule-suite-templates.md` gives, on the terms of `orchestration-harness/references/value-level-operation.md` (The Carrier, Standing Approvals), naming Counsel's identity on the peer channel by the convention `<repository>-counsel` or as the owner names it. It is an offer, not something reported missing.

- On the owner's yes, given in this session (no relay is admitted before the entry, unless the owner has told this session directly to accept Counsel's relays), write the entry under Standing Approvals in `common.md`, adding the section if it is absent, with who gave it and the owner's words quoted with the date, and write the Counsel line in Repository Reference Documents in the form `references/rules-files.md` gives. Both go in the same change.
- The entry is in effect only when the quoted words accept the entry as it stands, with the identity it names, and once it is committed; a yes to something else, or to accepting relays in general before the entry was shown, does not accept it. Show the entry and ask again.
- On a decline, nothing is written.
- The admission is recorded in `common.md` and nowhere else. A note the Orchestrator keeps for itself, in its runtime memory or any other file, is not a place the harness reads.

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
