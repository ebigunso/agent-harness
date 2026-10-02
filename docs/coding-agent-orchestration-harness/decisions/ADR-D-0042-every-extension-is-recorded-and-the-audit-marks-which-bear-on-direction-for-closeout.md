---
status: accepted
adr_type: design
date: 2026-10-01
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1"]
informed: []
supersedes: []
superseded_by: null
depends_on: ["ADR-D-0039-the-orchestrator-never-grades-its-own-run-against-the-value-documents.md", "ADR-D-0041-a-ratified-brief-authorizes-a-plan-only-through-a-closed-plan-review-and-a-value-audit-that-holds-nothing-above-the-run.md"]
---

# ADR-D-0042: Every extension the value audit lets through and every judgement call of a run is recorded in the run's records, and at closeout the person directing the work is shown only those the audit marked as bearing on the product's direction

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. The product owner is whoever is entitled to state the product's values and to answer product-level questions for that work; when the person directing the work owns the product, both are that person. Counsel is the session the person directing the work opens for value discussion, separate from any Orchestrator session. The Orchestrator session is a session that holds the Orchestrator role (ADR-D-0020) and plans, dispatches and reports the work.

Under ADR-D-0041 a plan may start with items that no value document states, when the value audit judges each a cheap-to-undo extension of statements it names; the audit grades a result on the same terms (ADR-D-0039). A run also makes judgement calls of its own: the choices Workers report and the rulings the Orchestrator makes. All of these are decisions made below the level at which the person directing the work was consulted, and that person has to be able to see them afterwards without reading every plan. The fork is how much of this reaches that person at closeout, and who chooses it.

## Decision

- Every item the value audit grades as an extension is recorded in the run's records, with the statements the verdict named as the ones it extends.
- At closeout the person directing the work is shown the extensions that bear on the product's direction, and not every one. Direction is the level of either philosophy, product or engineering: a marked extension on either side is shown.
- Which extensions bear on direction is marked by the value audit in its verdict, not chosen by the Orchestrator.
- The same holds for the run's judgement calls, the choices Workers reported and the rulings the Orchestrator made: they are kept in the run's records in full, the closeout audit marks from those records which bear on direction, and the person directing the work is shown the marked ones and no others.
- The closeout carries each marked item, extension or judgement call, as the audit stated it, with its grade and the statements the verdict names for it; the Orchestrator adds no account of why it was made.
- An item not marked stays in the run's records, where the person directing the work can read it.

## Why

The person directing the work shapes direction at product level and should see what was decided for the product in that person's absence, not every structural choice a run made; shown everything, that person is back to reading plans. The party that made the extensions and the rulings cannot be the one that decides which of them that person sees, for the same reason it does not grade its own run (ADR-D-0039): any account it gives chooses what the judge sees. The unmarked ones are still written down, so nothing is lost, only not pushed.

## Rejected Alternatives

- Every extension is shown at closeout: it returns the person directing the work to reading each run's structural choices, which the brief exists to end; reopen if an unmarked extension turns out to be one that person would have stopped.
- The Orchestrator chooses which of its own rulings and its Workers' choices to show, the audit marking only the extensions it graded: it lost because the rulings are the Orchestrator's own work as much as the extensions are, and its choice of which to show is an account of that work; reopen if the audit, reading the run's records, is found unable to tell a ruling that bears on direction from one that does not.
- The Orchestrator chooses which extensions to show: rejected outright; it is the party that made them, and its choice of what to show is an account of its own work.
- No extension is shown, all stay in the records: it leaves direction-bearing decisions for that person to find; reopen if the marked set is found to be empty across runs that did make such decisions.
- Extensions are shown as they are made, during the run: it interrupts the person directing the work with items the audit has already let through; reopen if closeout proves too late to undo a marked extension cheaply.

## Decision Boundary

Invariant: every extension and every judgement call is in the run's records; the closeout shows the person directing the work only those the value audit marked as bearing on the product's direction, as the audit stated them; the Orchestrator neither chooses nor annotates them; the Decision list states the rest.

Not covered: what an extension is and when it lets a plan start (ADR-D-0041); the grade names and their definitions, which no record states and the audit's mandate owns (ADR-D-0039 leaves them uncovered); the audit's procedure and the dispatch wording (ADR-D-0039); the form of the closeout note and the rest of what it carries; where in the run's records the extensions and the judgement calls are written.

## Validation

- A run's records list every item graded as an extension, each with the statements the verdict named, and every Worker choice and Orchestrator ruling.
- The closeout shows only the extensions and judgement calls the verdict marked as bearing on direction, in the audit's words, and the Orchestrator's own text adds none and reasons for none.
- The verdict record has a field or marking for direction-bearing items, so that an unmarked verdict shows nothing at closeout rather than leaving the choice to the Orchestrator.

## Revisit When

- An unmarked extension or judgement call turns out, when the person directing the work reads the records afterwards, to be one that person would have stopped: it reopens how the audit marks direction, and this record if the marking is not the cause.
- The marked set is empty across runs that did make direction-bearing decisions.
- A marked item is one the person directing the work would not have wanted shown: it reopens how the audit marks direction.
- On 2026-10-03 no closeout audit had marked a run's judgement calls on any runtime; an audit found unable to tell, from the run's records, a ruling that bears on direction from one that does not reopens this record.

## More Information

Source of intent: `docs/coding-agent/briefs/active/value-level-operation-brief.md`, "Stops during a run" and "Lifecycle". Related records: ADR-D-0039 (the value audit), ADR-D-0041 (extensions as a condition of authorization), ADR-D-0040 (the sources of authorization).
