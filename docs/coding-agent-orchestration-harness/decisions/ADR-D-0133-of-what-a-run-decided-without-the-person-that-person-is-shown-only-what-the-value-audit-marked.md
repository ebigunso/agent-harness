---
status: proposed
adr_type: design
date: 2026-11-24
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1", "Claude Fable 5.2"]
informed: []
supersedes: ["ADR-D-0042-every-extension-is-recorded-and-the-audit-marks-which-bear-on-direction-for-closeout.md"]
superseded_by: null
depends_on: ["ADR-D-0134-the-orchestrator-never-grades-its-own-run-against-the-value-documents.md", "ADR-D-0065-a-ratified-brief-authorizes-a-plan-or-a-goal-envelope-only-on-a-closed-review-and-a-value-audit-that-holds-nothing.md"]
---

# ADR-D-0133: Of what a run decided without the person directing the work, that person is shown only what the value audit marked as bearing on the product's direction, as the audit stated it

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. The Orchestrator session is a session that holds the Orchestrator role and plans, dispatches and reports the work. Counsel is the session role that person talks with about what the product does or should do. The value audit is the independent grading of a run's plan and result against the value documents (ADR-D-0134). The product philosophy and the engineering philosophy are the standing value documents: the one states what is wanted of the product, the other what is wanted of how it is built. An extension is an item that no value document states and that the audit lets through as a cheap-to-undo extension of statements it names (ADR-D-0065). A judgement call is a choice a run makes without the person directing the work: a choice made in the course of the work and reported, or a ruling of the Orchestrator's.

A run starts and goes on without the person directing the work reading its plan, extensions included (ADR-D-0065), and it makes judgement calls of its own as it goes. All of these are decisions made below the level at which that person was consulted. That person shapes the product's direction and has to be able to see what was decided for the product in their absence, without reading every plan. Showing all of it returns that person to reading plans. Leaving the choice of what to show to the Orchestrator has the party that made the decisions choose what their judge sees. The fork is how much of what a run decided reaches that person, when, and who chooses it.

## Decision

- Of the extensions the value audit let through and the judgement calls a run made without the person directing the work, that person is shown those that bear on the product's direction, and no others.
- An item bears on direction when it is a decision at the level of the product philosophy or of the engineering philosophy. An item marked on the engineering side is shown as one on the product side is.
- Which items bear on direction is the value audit's to mark, in its verdict. The Orchestrator chooses none of them. A judgement call is marked by the audit that grades the work it was made in, which reads it from the run's records.
- The marked items are shown when the work is reported to that person as ready for their judgement, and not as each is made. For a run under a ratified brief that is the report of the run as ready, as ADR-D-0051 states; a unit's close is no such report.
- Each marked item reaches that person as the audit stated it, with the audit's grade of it and the statements the audit's verdict names for it. The Orchestrator adds no account of why the item was made.

## Why

The product philosophy's "What goes wrong, in order" has "Attention is the scarce thing, and people rightly will not spend it on what they did not need to know": the person directing the work should see what was decided for the product in their absence, not every structural choice a run made, and shown everything, that person is back to reading plans. The party that made the extensions and the rulings cannot be the one that decides which of them that person sees, for the same reason it does not grade its own run (ADR-D-0134), which the product philosophy's "What it must not be" states as "Not its own judge": any account it gives chooses what the judge sees.

## Rejected Alternatives

- Every extension is shown when the work is reported as ready: it returns the person directing the work to reading each run's structural choices, which the brief exists to end; reopen if an unmarked extension turns out to be one that person would have stopped.
- The Orchestrator chooses which of the run's judgement calls to show, its own rulings and the choices reported to it, the audit marking only the extensions it graded: it lost because the rulings are the Orchestrator's own work as much as the extensions are, and its choice of which to show is an account of that work; reopen if the audit, reading the run's records, is found unable to tell a ruling that bears on direction from one that does not.
- The Orchestrator chooses which extensions to show: rejected outright; it is the party that made them, and its choice of what to show is an account of its own work.
- No extension is shown, all stay in the records: it leaves direction-bearing decisions for that person to find; reopen if the marked set is found to be empty across runs that did make such decisions.
- Extensions are shown as they are made, during the run: it interrupts the person directing the work with items the audit has already let through; reopen if the report of the work as ready proves too late to undo a marked extension cheaply.

## Decision Boundary

Not covered: that every extension and every judgement call is kept in the run's records and stays there, shown or not (ADR-D-0132); what an extension is and when it lets a plan start (ADR-D-0065); when a run under a ratified brief is reported as ready, and that the close of a unit of such a run is no such report (ADR-D-0051); what Counsel hears from the value audit during a run, which is a limited exception to this record (ADR-D-0045, which the proposed ADR-D-0122 takes over); the grade names and their definitions, which no record states and the audit's mandate owns (ADR-D-0134 leaves them uncovered); the audit's procedure, which the plugin's text states and no record; the dispatch wording (ADR-D-0050); how a verdict carries the mark; the form of the report that shows the marked items and the rest of what it carries.

## Validation

The decision is broken where:

- the person directing the work was shown, of what a run decided without them, an item the audit's verdict did not mark, or was not shown one it marked;
- which items were shown fell to the Orchestrator's choice, a verdict that marked nothing included: such a verdict shows nothing;
- a marked item reached that person in words other than the audit's, without the audit's grade of it or the statements the verdict names for it, or with the Orchestrator's account of why it was made;
- the Orchestrator session put a decision the run had already made without that person to them as it was made, on the ground that it bears on direction, and not when the work was reported as ready.

## Revisit When

- An unmarked extension or judgement call turns out, when the person directing the work reads the records afterwards, to be one that person would have stopped: it reopens how the audit marks direction, and this record if the marking is not the cause.
- The marked set is empty across runs that did make direction-bearing decisions.
- A marked item is one the person directing the work would not have wanted shown: it reopens how the audit marks direction.
- On 2026-10-03 no closeout audit had marked a run's judgement calls on any runtime; an audit found unable to tell, from the run's records, a ruling that bears on direction from one that does not reopens this record.

## More Information

With ADR-D-0132, replaces ADR-D-0042 in full. ADR-D-0042 named the judgement calls as the choices Workers reported and the rulings the Orchestrator made, and the moment as closeout; this record names the first by what they are, choices a run makes without the person directing the work, and the second as the work being reported to that person as ready for their judgement. Source of intent: `docs/coding-agent/briefs/completed/value-level-operation-brief.md`, "Stops during a run" and "Lifecycle". Related: ADR-D-0134 (the value audit), ADR-D-0065 (extensions as a condition of authorization), ADR-D-0064 (the sources of authorization), ADR-D-0051 (the run and its report as ready).
