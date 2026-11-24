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

# ADR-D-0126: Counsel's first read of a result is formed without what the value audit marks, apart from what reached Counsel during the run

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session role that person talks with about what the product does or should do. A run is the work done under one ratified brief, and a result is what a run built. The value audit is the independent grading of a run's plan and result against the value documents, which are the brief and the philosophies, and a verdict is what it states of them. Counsel's read of a result is Counsel's own account of the result, given to that person.

Counsel's read of a result is to be independent of the audit's. The audit grades the same result and marks items for that person, so what it marks exists when Counsel comes to read the result, and a Counsel that had it in hand would form its read with it. The fork is whether Counsel's first read of a result is formed with what the audit marks or without it.

## Decision

- Counsel's first read of a result is formed without what the value audit marks, apart from what reached Counsel during the run (ADR-D-0122).

## Why

A read formed with what the audit marks in hand is no longer independent of the audit.

## Rejected Alternatives

- Counsel receives every verdict, or every item the audit marks, as the run goes: it lost because Counsel would be monitoring the run and its first read of the result would no longer be independent; reopen if matters Counsel would have paused are found to have passed without reaching it.

## Decision Boundary

Not covered: what Counsel hears from the audit during a run (ADR-D-0122); whether a brief carries a list of things to watch for (ADR-D-0123); what is shown to the person directing the work at closeout (ADR-D-0042); where Counsel's read of a result goes (ADR-D-0103); what Counsel reads of the work (ADR-D-0099); the audit's grades, positions and dispatch (ADR-D-0052); what Counsel's read holds, when it is given, and when what the audit marks reaches Counsel after that read, all of which the plugin's text states.

## Validation

The decision is broken where Counsel had anything of what the value audit marks, apart from what reached it during the run (ADR-D-0122), before its first read of the result was formed.

## Revisit When

- The premise that a read Counsel forms with what the audit marks in hand is no longer independent of the audit no longer holds.

## More Information

With ADR-D-0122 and ADR-D-0123, replaces ADR-D-0045 in full; the decision carried here is the same. Carried here from it: that Counsel's first read of a result is formed without what the audit marks, apart from what reached Counsel during the run. It is a record of its own because it would still bind if nothing reached Counsel from the audit during a run. ADR-D-0122 carries the same rejected alternative for its own decision. Related: ADR-D-0052 (the value audit), ADR-D-0042 (what the audit marks for closeout), ADR-D-0103 (where Counsel's read of a result goes).
