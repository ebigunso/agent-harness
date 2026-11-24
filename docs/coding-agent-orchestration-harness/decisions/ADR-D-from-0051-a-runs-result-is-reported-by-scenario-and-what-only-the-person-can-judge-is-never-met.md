---
status: proposed
adr_type: design
date: 2026-11-24
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1", "Claude Opus 5.5"]
informed: []
supersedes: ["ADR-D-0051-work-under-a-brief-is-a-run-of-one-or-more-units-that-closes-once.md"]
superseded_by: null
depends_on: ["ADR-D-from-0051-work-under-a-ratified-brief-is-a-run-of-units-that-goes-from-unit-to-unit-without-the-person.md"]
---

# ADR-D-XXXX: A run's result is reported as ready as behaviour, scenario by scenario, and a scenario only the person directing the work can judge is never reported as met

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. A run is what a ratified brief governs: one or more units of work, whose result is reported as ready for that person's judgement (ADR-D-from-0051-work-under-a-ratified-brief-is-a-run-of-units-that-goes-from-unit-to-unit-without-the-person).

The person directing the work judges what is built from its behaviour, and a design held in a brief by its scenarios, which only the whole shows. The report of a run as ready is what that judgement starts from. Some scenarios only that person can judge, so the run cannot establish by itself that such a scenario is met. The fork is in what terms a run's result is put to that person, and how a scenario only that person can judge is reported.

## Decision

- A run's report as ready leads with behaviour, one scenario of the brief at a time, with how to observe each.
- A scenario only the person directing the work can judge is reported as ready for that person's judgement and never as met.

## Why

The person directing the work judges what is built from its behaviour and a design by scenarios that only the whole shows, so the result is put to that person in those terms, as the product philosophy's "What goes wrong, in order" asks: "What is meant is established in terms the person can judge." A scenario only that person can judge is not met before that person has judged it, and the same section has "confidence is never taken on the builder's word: what was not done or not checked is said outright".

## Decision Boundary

Not covered: when a run's result is reported as ready, and that the close of a unit is no such report (ADR-D-from-0051-work-under-a-ratified-brief-is-a-run-of-units-that-goes-from-unit-to-unit-without-the-person); what follows a report as ready (ADR-D-from-0051-a-run-reported-ready-stays-open-takes-the-persons-changes-and-closes-once-on-acceptance); which of the extensions and judgement calls of the run the report shows, and how (ADR-D-0042, which the proposed ADR-D-0133 takes over for this); where a scenario's state comes from (the run record, ADR-D-from-0051-work-under-a-ratified-brief-is-a-run-of-units-that-goes-from-unit-to-unit-without-the-person); the form of the report and the rest of what it carries; goal mode; work with no brief.

## Validation

The decision is broken where a run's report as ready does not lead with behaviour, does not name each scenario of the brief with its state and how to observe it, or reports as met a scenario only the person directing the work can judge.

## Revisit When

- The premise that the person directing the work judges what is built from its behaviour, and a design by scenarios that only the whole shows, no longer holds.

## More Information

With ADR-D-from-0051-work-under-a-ratified-brief-is-a-run-of-units-that-goes-from-unit-to-unit-without-the-person and ADR-D-from-0051-a-run-reported-ready-stays-open-takes-the-persons-changes-and-closes-once-on-acceptance, replaces ADR-D-0051 in full; the decision carried here is the same. Carried here from it: the clause on how a run's report as ready presents its result and reports a scenario only the person directing the work can judge. ADR-D-0051 stated no revisit condition for this clause; the one here is worded from what ADR-D-0051 states of that person and of the design. Source of intent: `docs/coding-agent/briefs/completed/design-led-long-runs-brief.md`, "Closeout" and "The run". Of what this record fixes, that brief states one thing as a means: that a scenario only the person directing the work can judge ends as ready for that person's judgement; this record fixes that means as a rule. Related: ADR-D-0133 (what the person directing the work is shown of what a run decided without them).
