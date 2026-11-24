---
status: proposed
adr_type: design
date: 2026-11-24
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1", "Claude Opus 5.5"]
informed: []
supersedes: ["ADR-D-0051-work-under-a-brief-is-a-run-of-one-or-more-units-that-closes-once.md"]
superseded_by: null
depends_on: ["ADR-D-0144-work-under-a-ratified-brief-is-a-run-of-units-that-goes-from-unit-to-unit-without-the-person.md"]
---

# ADR-D-0145: A run reported as ready stays open for the judgement of the person directing the work, takes the changes that person directs against its brief as its own work, and closes once, on that person's acceptance

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. The Orchestrator session is a session that holds the Orchestrator role (ADR-D-0090) and plans, dispatches and reports the work. A run is what a ratified brief governs: one or more units of work (ADR-D-0144). A run's stack is the run's pull requests.

Someone who hands over a design wants to come back to it built and to judge what was built. Once a run's result is reported as ready, that person, judging it, may direct a change against the same brief before accepting it. A run that closed when it was reported as ready would leave that change apart from the work it corrects, and the brief would govern something other than its run. The fork is what closes a run, and whether a change directed while that person judges it belongs to it.

## Decision

- A run reported as ready stays open for the judgement of the person directing the work.
- A change that person directs against the run's brief while the run is open is work of the run: built on the run's stack as a small change, or as a plan where the Orchestrator chooses one, authorized as its kind is, reviewed and audited at its close, and kept in the run record. When it is done, the run is reported as ready again.
- The run closes once: when that person's acceptance of its stack reaches the Orchestrator session.
- A small change stated against a brief whose run has already been accepted and merged is not work of that run: it starts a run of its own, of that change alone, which closes once as any run does.

## Why

A change the person directing the work directs on judging the whole corrects the work the run did, under the same brief, so it is done as part of the run and on its stack, and the run is finished only when that person accepts what it built; the product philosophy's "What it aspires to" leaves that person "saying what they want, and judging what they got".

## Rejected Alternatives

- The run closes when it is reported as ready, and a change directed after that, or a small change, is a new run or stands outside any run: it lost because the brief would then govern something other than its run, and the change would be parted from the work it corrects; reopen if changes directed while a run is open are found not to correct the work the run did but to start work its brief did not ask for.

## Decision Boundary

Not covered: what a run is, its units, and when its result is reported as ready once its units are done (ADR-D-0144); in what terms the result is reported (ADR-D-0146); the conditions for authorizing each kind of unit (ADR-D-0139, ADR-D-0141, ADR-D-0147); how the word of the person directing the work reaches the Orchestrator session (ADR-D-0112); merge authorization; a change directed against a brief whose run is accepted and not yet merged; which brief governs the run a small change starts once the run it was stated against is accepted and merged, which the workflow text states; the form in which a change is kept in the run record; goal mode; work with no brief.

## Validation

The decision is broken where:

- a change the person directing the work directed against the run's brief while the run was open was built apart from the run's stack, authorized, reviewed or audited otherwise than a unit of its kind is, or left out of the run record;
- a run was not reported as ready again once such a change was done;
- a run was treated as closed before that person's acceptance of its stack reached the Orchestrator session, or a closed run was opened again;
- a small change stated against a brief whose run had been accepted and merged was built as work of that run, or as work of no run.

## Revisit When

- Changes directed while a run is open are found not to correct the work the run did but to start work its brief did not ask for.

## More Information

With ADR-D-0144 and ADR-D-0146, replaces ADR-D-0051 in full; the decision carried here is the same. Carried here from it: that a run reported as ready stays open, that a change directed against its brief while it is open is work of the run, that the run closes once on the acceptance of the person directing the work, and that a small change stated against a brief whose run is accepted and merged starts a run of its own. Source of intent: `docs/coding-agent/briefs/completed/small-change-from-his-word-brief.md`, "A small change and the run". Related: ADR-D-0112 (the word of the person directing the work), ADR-D-0096 (two briefs that cannot both hold).
