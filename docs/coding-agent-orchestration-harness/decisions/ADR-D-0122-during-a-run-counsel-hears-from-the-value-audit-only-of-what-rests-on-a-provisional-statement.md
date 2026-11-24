---
status: proposed
adr_type: design
date: 2026-11-24
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1", "Claude Fable 5.2"]
informed: []
supersedes: ["ADR-D-0045-during-a-run-counsel-hears-from-the-audit-only-of-an-item-let-through-on-a-provisional-statement.md"]
superseded_by: null
---

# ADR-D-0122: During a run Counsel hears from the value audit only of an item the audit lets through that rests on a statement marked provisional

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session role that person talks with about what the product does or should do. The Orchestrator session is a session that holds the Orchestrator role and plans, dispatches and reports the work. A run is the work done under one ratified brief. The value audit is the independent grading of a run's plan and result against the value documents, which are the brief and the philosophies. A statement marked provisional is one those documents mark as not yet settled.

Counsel may pause part of a run where continuing without that person's decision would be severe (ADR-D-0121), and it can pause in time only what it sees. It is also kept from following the run: it reads no plan and no diff (ADR-D-0099), so that the session that person talks with is not drawn into the work and its read of the result is its own. Between the hand-over of a brief and the closeout it therefore sees only the questions the Orchestrator session escalates, and what the value audit lets through reaches that person at closeout (ADR-D-0042). Work that rests on a statement not yet settled can then be built on, unseen by Counsel, until it is done; and reporting everything to Counsel as the run goes would have Counsel monitoring the run. The fork is what reaches Counsel from the audit during a run, and who chooses it.

## Decision

- During a run Counsel hears from the value audit of one thing only: an item the audit lets go ahead that rests on a statement marked provisional. Nothing else of a verdict reaches Counsel before closeout.
- Each such item reaches Counsel at once, as the audit stated it and with nothing of the Orchestrator's added, and once for as long as it is unchanged. The Orchestrator session neither selects among such items nor judges one too small to send: the finding is the audit's.
- A report is neither a stop nor a grade. It adds no gate and removes none: the work proceeds as the audit's verdict leaves it, and an item free to go ahead stops only where Counsel pauses it (ADR-D-0121).
- A report goes to Counsel and not to the person directing the work. It reaches that person during the run only if Counsel raises it. Everything else the audit marks reaches that person at closeout, as ADR-D-0042 states, and a report is a limited exception to that.

## Why

A statement marked provisional is the one mark already in the value documents that says a statement is not yet settled, so work resting on one is where the failure the product philosophy's "What goes wrong, in order" names "The wrong thing, built confidently" is likeliest to start, and Counsel can pause in time only what it sees. The audit is the one to find such items because it already reads every item and is the party the Orchestrator cannot frame (ADR-D-0052); the Orchestrator choosing what Counsel hears would be an account of its own work.

## Rejected Alternatives

- Counsel receives every verdict, or every item the audit marks, as the run goes: it lost because Counsel would be monitoring the run and its first read of the result would no longer be independent; reopen if matters Counsel would have paused are found to have passed without reaching it.
- Nothing reaches Counsel during a run beyond escalated questions: it lost because the pause then depends on chance; reopen if reports of items let through on a provisional statement are found never to have led Counsel to raise anything with that person.
- The Orchestrator session reports to Counsel what it judges Counsel would want to know: rejected outright; the party whose work may be paused would choose what the pausing party sees.

## Decision Boundary

Not covered: whether a brief carries a list of things to watch for (ADR-D-0123); that Counsel's first read of a result is formed without what the audit marks, apart from what reached Counsel during the run (ADR-D-0126); the pause itself (ADR-D-0121); what Counsel may say to an Orchestrator session (ADR-D-0097, ADR-D-0100, ADR-D-0102); the audit's grades, positions and dispatch (ADR-D-0052); what is shown at closeout (ADR-D-0042); the questions the Orchestrator session escalates, and a finding that bears on the design (ADR-D-0053); how a statement is marked provisional, how a verdict shows the mark, how a report travels between sessions and where it is written down, all of which the plugin's text states.

## Validation

The decision is broken where:

- an item the audit let go ahead on a statement marked provisional did not reach Counsel during the run, reached it late, or reached it with an account of the Orchestrator's added;
- anything else of a verdict reached Counsel before closeout;
- an Orchestrator session chose which such items to send;
- a report was treated as a stop or as a grade: work free to go ahead waited on a report that Counsel had not answered with a pause, or a held item went ahead because it had been reported.

## Revisit When

- A matter Counsel would have paused is found to have passed without reaching it.
- An item let through on a provisional statement is found not sent by the Orchestrator session, or sent with an account of its own added.
- Reports of items let through on a provisional statement are found never to have led Counsel to raise anything with the person directing the work.

## More Information

With ADR-D-0123 and ADR-D-0126, replaces ADR-D-0045 in full. Related: ADR-D-0121 (the pause this serves), ADR-D-0052 (the value audit), ADR-D-0042 (what the audit marks for closeout), ADR-D-0099 (Counsel's reach). Source of intent: `docs/coding-agent/briefs/completed/value-level-operation-brief.md`, "Roles and sessions".
