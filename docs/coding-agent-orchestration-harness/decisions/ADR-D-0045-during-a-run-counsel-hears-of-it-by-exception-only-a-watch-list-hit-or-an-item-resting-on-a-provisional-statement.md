---
status: accepted
adr_type: design
date: 2026-10-02
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1"]
informed: []
supersedes: []
superseded_by: null
depends_on: ["ADR-D-0039-the-orchestrator-never-grades-its-own-run-against-the-value-documents.md", "ADR-D-0044-counsel-pauses-the-affected-part-of-the-work-where-continuing-without-a-decision-would-be-severe.md"]
---

# ADR-D-0045: During a run Counsel hears of it by exception only, from the value audit: an item that hits the brief's watch list, or an item let through that rests on a statement marked provisional

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. The product owner is whoever is entitled to state the product's values and to answer product-level questions for that work; when the person directing the work owns the product, both are that person. Counsel is the session the person directing the work opens for value discussion, separate from any Orchestrator session. The Orchestrator session is a session that holds the Orchestrator role (ADR-D-0020) and plans, dispatches and reports the work.

Counsel may pause the affected part of a run where continuing without the decision of the person directing the work would be severe (ADR-D-0044), but between the hand-over and the closeout it sees only the questions the Orchestrator escalates. It reads no plan and no diff (ADR-D-0035), and what the value audit lets through reaches that person at closeout (ADR-D-0042). So a matter Counsel would have raised can pass unseen until the work on it is done. Reporting everything to Counsel during the run would put it back to monitoring the run, which the separation of the two sessions exists to avoid. The fork is what, if anything, reaches Counsel while a run is under way, and who selects it.

## Decision

- During a run, reports reach Counsel by exception only, from two sources, both found by the value audit at the positions the workflow fixes.
- The first source is the brief's watch list: a short list, a handful of entries for a brief, of the things the person directing the work would want to hear about at once if they came up. It is written by that person with Counsel at the closing pass of the discussion and ratified with the brief. A brief may have none.
- The audit checks each item it grades against the watch list and names each hit, with the entry it hit, in its verdict.
- The second source is an item the audit lets through, graded as covered or as a cheap-to-undo extension, that rests on a statement the documents mark provisional.
- In a run under a brief the Orchestrator sends each such item to Counsel at once, as the verdict states it and with nothing added, and the work proceeds; a line already sent is not sent again while it is unchanged.
- A report adds no gate and removes none: the item's grade and the gates of the audit's position apply as they stand (ADR-D-0039), so an item held for a decision above the run still waits, and an item free to go ahead stops only if Counsel judges continuing severe and pauses it (ADR-D-0044). A hit is not itself a stop, and it is not a grade.
- Everything else the audit marks reaches that person at closeout as ADR-D-0042 states, and Counsel's first read of a result is formed without it. Reporting an extension that rests on a provisional statement during the run is a limited exception to extensions being shown at closeout, which ADR-D-0042 chose over showing them as they are made: it goes to Counsel, not to that person, and reaches that person during the run only if Counsel raises it.
- The Orchestrator neither selects what is reported nor decides that a hit is too small to send: the list is that person's, and the finding is the audit's.

## Why

A pause is only as good as Counsel's chance to notice in time, and Counsel cannot notice what it never sees. What it should see is decided before the run by the person whose attention is being spared, in a list short enough that a hit means something, and by the one mark already in the documents that says a statement is not yet settled. The audit finds the hits because it already reads every item at fixed positions and is the party the Orchestrator cannot frame (ADR-D-0039); the Orchestrator choosing what Counsel hears would be an account of its own work.

## Rejected Alternatives

- Counsel receives every verdict, or every item the audit marks, as the run goes: it lost because Counsel would be monitoring the run and its first read of the result would no longer be independent; reopen if matters Counsel would have paused are found to have passed outside both sources.
- Nothing reaches Counsel during a run beyond escalated questions: it lost because the pause then depends on chance; reopen if exception reports are found never to have led Counsel to raise anything with that person.
- The Orchestrator reports to Counsel what it judges Counsel would want to know: rejected outright; the party whose work may be paused would choose what the pausing party sees.
- A long watch list, or one the audit extends by its own judgement: it lost because a list that hits often is monitoring by another name, and an entry that person did not write is not that person's wish; reopen if a brief's list is found to hit at most positions of a run.
- A hit stops the affected work until Counsel answers: it lost because most hits will be matters that person only wanted to hear of, and a stop on each returns the run to waiting; reopen if work continued past a hit is found to have needed undoing at a cost a stop would have saved.

## Decision Boundary

Invariant: during a run Counsel is sent only the items the value audit names as watch-list hits or as let through on a provisional statement, as the verdict states them, at once; a report changes no gate, and work free to proceed does so unless Counsel pauses; the watch list is short, written by the person directing the work with Counsel and ratified with the brief; the Orchestrator selects nothing; the Decision list states the rest.

Not covered: the pause itself and its severities (ADR-D-0044); what Counsel may say to the Orchestrator (ADR-D-0043); the audit's grades, positions and dispatch (ADR-D-0039); what is shown at closeout (ADR-D-0042); questions the Orchestrator escalates, which are unchanged; the form of the watch list in the brief and of the hit in the verdict record; how many entries a handful is; how a report travels between sessions.

## Validation

- The brief form has a place for the watch list and says who writes it, when, and that it is short.
- The audit's mandate checks each graded item against the watch list and its verdict record names each hit with its entry.
- The Orchestrator's run-side text sends each hit and each item let through on a provisional statement to Counsel at once, as the verdict states it, and says the work proceeds.
- A report to Counsel recorded in a plan shows the verdict line it carried and nothing of the Orchestrator's.

## Revisit When

- A matter Counsel would have paused is found to have passed outside both sources.
- A watch list is found to hit at most positions of a run.
- On 2026-10-02 no brief carried a watch list and no exception report had been sent on any runtime; a hit the Orchestrator did not send, or one sent with its own account added, reopens this record.

## More Information

Source of intent: `docs/coding-agent/briefs/active/value-level-operation-brief.md`, "Roles and sessions". Related: ADR-D-0044 (the pause this serves), ADR-D-0039 (the value audit), ADR-D-0042 (what the audit marks for closeout), ADR-D-0043 (what Counsel says to the Orchestrator), ADR-D-0035 (Counsel's reach).
