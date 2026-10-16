---
status: accepted
adr_type: design
date: 2026-10-02
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1"]
informed: []
supersedes: []
superseded_by: null
depends_on: ["ADR-D-0052-the-orchestrator-never-grades-its-own-run-and-its-reading-is-compared-only-after-the-grades-are-fixed.md", "ADR-D-0044-counsel-pauses-the-affected-part-of-the-work-where-continuing-without-a-decision-would-be-severe.md"]
---

# ADR-D-0045: During a run Counsel hears from the value audit only of an item the audit lets through that rests on a statement marked provisional, and a brief carries no watch list

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session the person directing the work opens for value discussion, separate from any Orchestrator session. The Orchestrator session is a session that holds the Orchestrator role (ADR-D-0020) and plans, dispatches and reports the work.

Counsel may pause the affected part of a run where continuing without the decision of the person directing the work would be severe (ADR-D-0044), but between the hand-over and the closeout it sees only the questions the Orchestrator escalates. It reads no plan and no diff (ADR-D-0035), and what the value audit lets through reaches that person at closeout (ADR-D-0042). So a matter Counsel would have raised can pass unseen until the work on it is done. Reporting everything to Counsel during the run would put it back to monitoring the run, which the separation of the two sessions exists to avoid. This record first answered with two sources of reports, a watch list written into the brief and an item let through on a statement marked provisional. Across the audits of two plans the watch list's entries fired on lines the brief itself states and caught nothing, its entries were worded and then reworded, and one entry was overtaken by a later decision of that person. The fork is whether a brief carries a watch list at all, and what still reaches Counsel from the audit during a run.

## Decision

- A brief carries no watch list, and the value audit checks no item against one.
- During a run Counsel hears from the value audit of one thing only: an item the audit lets through, graded as covered or as a cheap-to-undo extension, that rests on a statement the documents mark provisional.
- In a run under a brief the Orchestrator sends each such item to Counsel at once, as the verdict states it and with nothing added, and the work proceeds; a line already sent is not sent again while it is unchanged.
- A report adds no gate and removes none: the item's grade and the gates of the audit's position apply as they stand (ADR-D-0052), so an item free to go ahead stops only if Counsel judges continuing severe and pauses it (ADR-D-0044). A report is not itself a stop, and it is not a grade.
- Everything else the audit marks reaches that person at closeout as ADR-D-0042 states, and Counsel's first read of a result is formed without it. Reporting an extension that rests on a provisional statement during the run is a limited exception to extensions being shown at closeout, which ADR-D-0042 chose over showing them as they are made: it goes to Counsel, not to that person, and reaches that person during the run only if Counsel raises it.
- The Orchestrator neither selects what is reported nor decides that an item is too small to send: the finding is the audit's.

## Why

A watch list is wrong in kind: what can be foreseen is a constraint written a second time with a weaker consequence, what cannot be foreseen cannot be listed, and what remains is being told of things that are fine, and rewording a poorly worded list is churn. A statement marked provisional is different: it is the one mark already in the documents that says a statement is not yet settled, and Counsel can pause in time only what it sees. The audit finds such items because it already reads every item at fixed positions and is the party the Orchestrator cannot frame (ADR-D-0052); the Orchestrator choosing what Counsel hears would be an account of its own work.

## Rejected Alternatives

- The brief keeps a watch list that the audit checks every item against, as this record first decided: it lost because what can be foreseen is a constraint written a second time with a weaker consequence, what cannot be foreseen cannot be listed, and what remains is being told of things that are fine; reopen if matters the person directing the work would have wanted to hear of at once are found to have reached that person only at closeout, with no constraint that could have named them.
- Counsel receives every verdict, or every item the audit marks, as the run goes: it lost because Counsel would be monitoring the run and its first read of the result would no longer be independent; reopen if matters Counsel would have paused are found to have passed without reaching it.
- Nothing reaches Counsel during a run beyond escalated questions: it lost because the pause then depends on chance; reopen if reports of items let through on a provisional statement are found never to have led Counsel to raise anything with that person.
- The Orchestrator reports to Counsel what it judges Counsel would want to know: rejected outright; the party whose work may be paused would choose what the pausing party sees.

## Decision Boundary

Invariant: a brief carries no watch list; during a run Counsel is sent from the audit only the items the audit lets through on a statement marked provisional, as the verdict states them, at once; a report changes no gate, and work free to proceed does so unless Counsel pauses; the Orchestrator selects nothing; the Decision list states the rest.

Not covered: what replaces the watch list in the brief, which the brief states and the workflow text carries: the question Counsel asks at the closing pass, whose answers go into the brief as constraints the audit holds on, and the hold on a change that loosens a stop, a pass condition or who decides; the pause itself and its severities (ADR-D-0044); what Counsel may say to the Orchestrator (ADR-D-0043); the audit's grades, positions and dispatch (ADR-D-0052); what is shown at closeout (ADR-D-0042); questions the Orchestrator escalates, which are unchanged; how a statement is marked provisional and how the verdict shows it; how a report travels between sessions.

## Validation

- No brief form, Counsel text, audit mandate, verdict record form or run-side text of the plugin states a watch list, a watch hit or a watch field.
- The Orchestrator's run-side text sends each item let through on a provisional statement to Counsel at once, as the verdict states it, and says the work proceeds.
- A report to Counsel recorded in a plan shows the verdict line it carried and nothing of the Orchestrator's.

## Revisit When

- A matter Counsel would have paused is found to have passed without reaching it.
- Matters the person directing the work would have wanted to hear of at once are found to have reached that person only at closeout, with no constraint that could have named them.
- An item let through on a provisional statement is found not sent by the Orchestrator, or sent with an account of its own added.

## More Information

Amended on 2026-10-05, before merge. As first accepted on 2026-10-02 this record had reports reach Counsel from two sources, a watch list written into the brief and an item let through on a statement marked provisional. The amendment removes the watch list and the audit's check of items against it; everything the record decided about an item let through on a provisional statement stands, with how it is sent, that a report adds no gate, and that the Orchestrator neither selects nor withholds. Its earlier rejected alternatives on a long watch list or one the audit extends, and on a hit stopping the affected work, no longer have anything to apply to. Source of intent: `docs/coding-agent/briefs/active/design-led-long-runs-brief.md`, "Watch list" and "What reaches you, and what does not", whose statements this record fixes are all marked as what the work must give, none as a means; for the provisional item, `docs/coding-agent/briefs/active/value-level-operation-brief.md`, "Roles and sessions". Related: ADR-D-0044 (the pause this serves), ADR-D-0052 (the value audit), ADR-D-0042 (what the audit marks for closeout), ADR-D-0043 (what Counsel says to the Orchestrator), ADR-D-0035 (Counsel's reach).
