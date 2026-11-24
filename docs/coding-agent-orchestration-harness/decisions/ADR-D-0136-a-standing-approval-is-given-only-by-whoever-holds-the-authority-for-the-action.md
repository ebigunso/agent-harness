---
status: proposed
adr_type: design
date: 2026-11-24
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1", "Claude Fable 5.2"]
informed: []
supersedes: ["ADR-D-0052-the-orchestrator-never-grades-its-own-run-and-its-reading-is-compared-only-after-the-grades-are-fixed.md"]
superseded_by: null
---

# ADR-D-0136: A standing approval is given only by whoever holds the authority for the action, counts only once its giver has accepted the written entry, and never stands in for an act that keeps its own acceptance

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. The product owner is whoever is entitled to state the product's values and to answer product-level questions for that work; when the person directing the work owns the product, both are that person. The Orchestrator session is a session that holds the Orchestrator role and plans, dispatches and reports the work. A repository's rule files are the files that hold the rules its runs work under, which the Orchestrator writes.

An action of a run can wait for the decision of whoever holds the authority for it; one that cannot be undone or that reaches outside the work waits for that decision at its moment (ADR-D-0065). What the holder of the authority for an action has approved for all future runs is to hold, so that a run does not stop on something already answered. Such an approval is kept in the repository's rule files, and two things fail to serve it: the Orchestrator writes those files, so an entry there is by itself no more than the Orchestrator's word, and the person directing the work does not hold the authority for every action in every repository. The fork is who can give an approval for all future runs, when an entry that states one counts, and which acts one can stand in for.

## Decision

- A standing approval is an approval for all future runs given by whoever holds the authority for that action in that repository, recorded in that repository's rule files.
- The entry records who gave it.
- The person directing the work may grant one only within that person's own authority.
- The Orchestrator writes the entry, and the entry counts only once the giver has accepted it and it records that acceptance, so a file the Orchestrator can write never becomes a source the Orchestrator decides.
- A standing approval never discharges acceptance of a decision record, a change to a philosophy, plan approval, or acceptance of another standing approval.
- A standing approval may cover a merge only where that repository's rule files allow it and only when given by the product owner of that repository.

## Why

An approval reaches no further than the authority of the one who gives it, and an entry the Orchestrator wrote is that person's approval only when that person has accepted the entry itself. A standing approval given within its giver's authority and accepted as written is a yes given once beforehand by the one entitled to give it; one thing such a yes answers beforehand is what the product philosophy's "The line" has wait: "What cannot be undone, and what reaches outside the work, waits for the person's yes".

## Rejected Alternatives

- A standing approval given by the person directing the work for any action, authority or not: rejected outright; an approval reaches no further than the authority of the one who gives it.

## Decision Boundary

Not covered: how a standing approval is recorded and brought to its giver; under which heading and in which rule file an entry is kept, and when an accepted entry takes effect; who holds the authority for each action in a repository, which that repository's rules state; whether a repository's rules allow a merge to be covered; which actions wait for a decision at their moment, and what a plan that contains one must state (ADR-D-0065); what a standing approval in effect does for an irreversible or outward-facing action in a unit being authorized (ADR-D-0065); that a grade of the value audit may be supported by an accepted standing approval (ADR-D-0134); what else the value audit does with an action a standing approval covers, which the audit's own text states; the rules that acceptance of a decision record, a change to a philosophy and plan approval each keep, which their own records and texts state; the entry that admits Counsel's relays and how the answer to it travels (ADR-D-0111, ADR-D-0112).

## Validation

The decision is broken where:

- an action went ahead on a standing approval given by someone who does not hold the authority for that action in that repository;
- an entry counted that does not record who gave it and that person's acceptance of it, or counted before that acceptance;
- acceptance of a decision record, a change to a philosophy, plan approval or acceptance of another standing approval was taken as given by a standing approval;
- a merge went ahead on a standing approval in a repository whose rule files do not allow it, or on one the product owner of that repository did not give.

## Revisit When

- The premise that an approval reaches no further than the authority of the one who gives it no longer holds.
- The premise that the Orchestrator can write the file in which an entry is kept, so that an entry without its giver's recorded acceptance is the Orchestrator's word alone, no longer holds.

## More Information

With ADR-D-0134 and ADR-D-0135, replaces ADR-D-0052 in full; the decision carried here is the same. Carried here from it: every clause on standing approvals. It is a record of its own because it binds whether or not a value audit grades the run. ADR-D-0052 excluded goal mode as a whole and stated no mode for standing approvals; this record states none. Source of intent: `docs/coding-agent/briefs/completed/value-level-operation-brief.md`, "Stops during a run" (who gives a standing approval; a merge approval in a repository the person directing the work does not own is the product owner's to give; merge looseness is a per-repository matter for that repository's rule files). Related: ADR-D-0065 (an action no standing approval covers, in a plan authorized by a ratified brief), ADR-D-0112 and ADR-D-0111 (the standing approval that admits Counsel's relays), ADR-D-0051 (publication where a standing approval covers it).
