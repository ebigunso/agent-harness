---
status: proposed
adr_type: design
date: 2026-11-24
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1", "Claude Opus 5.5"]
informed: []
supersedes: ["ADR-D-0051-work-under-a-brief-is-a-run-of-one-or-more-units-that-closes-once.md"]
superseded_by: null
depends_on: ["ADR-D-0139-non-trivial-work-is-authorized-only-by-the-person-directing-the-work.md", "ADR-D-0141-a-brief-authorizes-a-plan-or-goal-envelope-only-on-a-closed-review-and-an-audit-holding-nothing.md", "ADR-D-0147-a-small-change-stated-in-a-brief-may-skip-the-plan-and-stands-once-its-audit-holds-nothing.md"]
---

# ADR-D-0144: Work under a ratified brief is a run of one or more units, which goes from unit to unit without the person directing the work

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour.

Someone who hands over a design in a ratified brief wants to come back to it built. A ratified brief can authorize a unit of work without the person directing the work reading it: a plan (ADR-D-0141), or a small change that person stated in the brief (ADR-D-0147). A design held in a brief is often larger than one unit can carry, and its shape is found as the work goes. When the unit is what a brief governs and what is reported as ready, the work ends after a single unit and that person is called to judge a part, or has to hand the rest over again. The fork is what a brief governs, and whether the result is reported as ready at the close of each unit or once the work the brief asked for is done.

## Decision

- What a ratified brief governs is a run: one or more units of work, taken one after another as the work shows what the next has to be.
- Each unit of a run is a plan-mode plan or a small change as ADR-D-0147 states; a goal-mode run is not a unit of a run.
- Each unit of a run is authorized on its own, as its kind is: a plan as ADR-D-0139 and ADR-D-0141 state, a small change as ADR-D-0147 states. Being in a run authorizes no unit.
- A unit of a run closes with its own checks and is not reported as ready for judgement; the run continues into its next unit without the person directing the work.
- When every unit of the run has closed and no further unit is to follow, the result is reported as ready for that person's judgement, and the run's reviewed branches are published where a standing approval covers that. The close of a unit is no such report.
- What a brief gives does not depend on how many units the work takes: a run of a single unit is a run.
- A run keeps a run record beside its units: each scenario of the brief and each the run added, with the state the latest audit gave it, and each unit, those built for a change directed while the run is open included, with what its closing audit found. The run record holds only what audits stated.
- Between units the person directing the work is reached only by what already reaches that person during a unit.

## Why

Someone who hands over a design wants to come back to it built, not to a part of it and a request to continue: being called at each unit boundary would have that person steering the work unit by unit, which the brief exists to end, and which the product philosophy's "What it must not be" refuses: "Not a permission-seeker." The check that lets a unit start without that person is made per unit and stays per unit, so a longer run adds no authority; it only moves the moment of judgement to where there is a whole to judge.

## Rejected Alternatives

- Each plan closes as ready for judgement, as a single plan does: it lost because the person directing the work would be asked to judge parts and to restart the work after each, when the design is judged by scenarios that only the whole shows; reopen if runs are found to reach their report as ready with results that person would have stopped at a plan the run had already closed.
- One plan extended by replans until the design is carried: it lost because the plan every audit re-reads would grow without bound; reopen if drafting a new plan for each step is found to cost more than the bounded, separately reviewed unit it buys (a revision also receives its own review, so the review alone is not what a new plan buys).
- The run authorized once, when it starts, and its units built on that authorization: rejected outright; a verdict covers the unit it graded (ADR-D-0141, ADR-D-0147), and a unit built after it decides things no audit has seen.
- Extending goal mode to designs a person judges: it lost because it gives one loop two kinds of end and changes how goal mode admits work; reopen if runs under a brief are found to need goal mode's per-iteration checks.

## Decision Boundary

Not covered: the conditions for authorizing a plan (ADR-D-0139, ADR-D-0141) and a small change (ADR-D-0147); what follows once the run is reported as ready, and when it closes (ADR-D-0145); in what terms the result is reported (ADR-D-0146); what the report shows of the extensions the value audit let through and of the run's judgement calls (ADR-D-0042, which the proposed ADR-D-0132 and ADR-D-0133 take over); the note to Counsel when the run is reported as ready and what it carries, which the workflow text states; what a standing approval is and who may give one (ADR-D-0052, which the proposed ADR-D-0136 takes over for this); when a run stops without finishing because it has stopped getting closer, which the workflow text states; what the Orchestrator writes for the audit to compare, and where (ADR-D-0052, which the proposed ADR-D-0135 takes over for this); design-level findings during a run (ADR-D-0053, which the proposed ADR-D-0137 takes over); the form of the run record; goal mode itself; work with no brief.

## Validation

The decision is broken where:

- a run's result was reported as ready while a unit of the run had not closed or a further unit was to follow, or a unit was reported as ready for judgement on its own close;
- a unit of a run started on another unit's authorization or on its place in the run, without the authorization its own kind requires;
- a goal-mode run was taken as a unit of a run;
- the person directing the work was reached between units by something that would not have reached that person during a unit;
- the run record holds something no audit stated, or lacks a scenario's audited state or a unit's closing audit.

## Revisit When

- Runs are found to reach their report as ready with results the person directing the work would have stopped at a plan the run had already closed.
- Units inside a run are found starting without the checks their kind requires.
- On 2026-10-04 one run had been carried over more than one plan, by hand, before ADR-D-0051's text existed; a run in which the person directing the work had to be called between units for something that would not reach that person during a unit reopens this record.

## More Information

With ADR-D-0145 and ADR-D-0146, replaces ADR-D-0051 in full; the decision carried here is the same. Carried here from it: what a brief governs, the kinds of unit and their order, the per-unit authorization, the unit's close without a report, when the result is reported as ready and its branches published, the run of a single unit, the run record, and what reaches the person directing the work between units. ADR-D-0051 listed what reaches that person between units as an item the audit holds, a question the Orchestrator escalates and Counsel's pause; this record states the criterion that list followed. The run record is the run's own addition. Source of intent: `docs/coding-agent/briefs/completed/design-led-long-runs-brief.md`, "The run"; `docs/coding-agent/briefs/completed/small-change-from-his-word-brief.md`, "A small change and the run". Related: ADR-D-0139 and ADR-D-0141 (authorization), ADR-D-0147 (a small change), ADR-D-0132 (what a run records of what it decided without the person directing the work), ADR-D-0133 (what that person is shown of it), ADR-D-0044 (Counsel's pause).
