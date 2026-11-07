# Brief: Decision records at intent altitude

- status: ratified by ebigunso on 2026-11-02 ("Nothing to add, I ratify the brief, hand it over."). Asked before ratifying whether there is anything the work must not do or must ask before doing, he added nothing.
- handed to: agent-harness-orchestrator on 2026-11-02
- drafted by: agent-harness-counsel, from discussion with ebigunso on 2026-11-02
- product basis: the product owner's own words in this brief. ebigunso owns the harness; no product philosophy and no engineering philosophy exist for this repository.
- provenance tags: *(told)* = ebigunso said it; *(inferred)* = Counsel read it from his words; *(agent-proposed)* = Counsel originated it and he accepted it. His quoted words with the date stand beside each.
- kind marks: **gives** (what the work must give him; it binds), **constraint** (fixed regardless), **means** (a way to get what a gives-statement asks for; the run builds from it and may better it).

This brief is the grounds for the work. It is passed verbatim; do not paraphrase it into a plan as if the paraphrase were the requirement. It states what and why. How is the Orchestrator's, except where a means is stated, and a means does not bind.

## Who it is for and why

- Someone who opens the decisions folder after the plugin has changed again finds, for each matter, one short record whose decision is still true, and can say what it decides from its title. Today the recent records restate the plugin's procedure, so a route change replaces them, and the reader gets the route of a given month. **gives** *(told 2026-11-02: "The ADRs are saying the right things, but I'm starting to feel that the recent suite of ADRs, not limited to the ones proposed, are slightly too much into the details to be a good decision that is expected to hold through subsequent changes.")*
- What Counsel found and he did not contest: ADR-D-0040 and 0041 (2026-09-30), 0056 (2026-10-05) and 0061 (2026-10-22) are superseded within weeks without any decision reversing; the folder holds 50 active and 23 retired records after two months; the standard (`durable-docs-authoring`, `references/adr.md`) already asks for intent altitude and one decision per record, and the records do not meet it. *(Counsel's read, 2026-11-02, mine)*

## What the work gives

- Every accepted record in `docs/coding-agent-orchestration-harness/decisions/` is checked against the standard the plugin already carries: one decision per record; the constraint stated so that any rewording of the plugin text that preserves it stays valid; the why in prose at intent altitude; exact mechanics (routes, moves, file names, admission of a relay, template fill-ins) not covered. **gives** *(told 2026-11-02: "checks and rewrites of older ADRs to meet those same standards should happen as a parallel task.")*
- The check also asks whether a record's wording names the thing it means rather than its position, order or relation to something else ("the second source"), so that the statement holds when that other thing changes. **gives** *(told 2026-11-07, reading a rewritten record of another run: "where it says 'the second source', I think should be reworded to point at what exactly it is, so that the statement holds even if it becomes the first or third or the likes. This is something to be wary of when writing documents in general. Choose wording that would be less likely to change meaning when something else changes.")*
- A record that fails the check is rewritten to meet it, under the standard's own lifecycle: a new complete record, the old one retired, accepted by name. A record found to be a bundle is split; a record found to carry only operational material is retired and its material placed in the rule or skill text that already states it, or added there. **gives** *(inferred 2026-11-02 from the above and the standard's lifecycle)*
- The decisions themselves do not change. The work moves altitude, not outcome; where a check finds a decision itself wrong, stale or contradicted, that is a value question for the owner through Counsel, not a rewrite. **constraint** *(inferred 2026-11-02; he asked for records that hold through changes, not for different decisions)*
- Records a run in progress proposes or supersedes are left to that run: on 2026-11-02 ADR-D-0040, 0041, 0056, 0061 to 0066. **constraint** *(agent-proposed 2026-11-02, so that two runs do not rewrite the same record)*
- Where the check finds that the standard's own form invites the detail (a section that asks for enumeration, a template that mirrors procedure), that is reported to the owner through Counsel as a value question; the standard is not changed by this work without his word. **constraint** *(agent-proposed 2026-11-02)*

## Limits

- The work runs beside the two runs in progress, as he asked, and lands by its own acceptance. **constraint** *(told 2026-11-02: "as a parallel task")*
- Acceptance is by name, as the standard says; one statement may accept several records when it names each. **constraint** *(the standard, Acceptance)*

## Core scenarios

Agent-proposed; ratified with the brief.

1. A record whose Decision lists the route a question travels and the moves when it fails: rewritten as one decision (who may be asked, by whom) with the route left to the plugin text; title short enough to state the decision.
2. A record deciding two things that could be retired separately: split into two, each accepted by name.
3. A record that is a rule with a status field (an exact string, a threshold, a dispatch template): retired; its material confirmed present in the rule or skill text, or placed there.
4. A record whose decision the check finds no longer true: not rewritten; brought to the owner through Counsel.

## Pass conditions

- For each active record, a reader can state what it decides in one sentence from its title, and no Decision section mirrors a passage of the plugin's procedure. *(agent-proposed)*
- The check's result for every record is recorded: meets, rewritten (to which), split (into which), retired (material where), or raised. *(agent-proposed)*

## Left out on purpose

- Changing any decision's outcome. Changing the record standard itself. Records belonging to runs in progress.
