---
status: proposed
adr_type: design
date: 2026-11-14
deciders: ["ebigunso"]
consulted: ["GPT-6 Astra", "Claude Fable 5.2"]
informed: []
supersedes: []
superseded_by: null
---

# ADR-D (not yet numbered): A run found stopped either recovers within a stated limit or reaches the person directing the work as a report

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session role that person talks with about what the product does or should do. A run is the work done under one ratified brief.

A run that has stopped making progress is found without the person directing the work (`ADR-D-a-stopped-run-is-found-without-the-person.md`). That person's attention is to go to a stop only where they are needed to settle it, and no stop is to be kept from them. Reporting every stop at once spends their attention on what one further attempt would have cleared. Restarting a stopped run until it goes spends the machine's limit on a cause a restart does not remove, with nothing said. The fork is what is done about a stopped run before that person hears of it.

## Decision

- A stopped run either recovers within a stated limit or reaches the person directing the work through Counsel as a clear report.
- A run is never restarted over and over.

## Why

Recovery is bounded because each attempt spends the machine's limit and hides the stop from the one person who could settle it; past the limit a report is the stated doubt the product philosophy's "What goes wrong, in order" calls the remedy.

## Rejected Alternatives

- A stopped run is restarted until it goes: it lost because a run that stops for a cause a restart does not remove is restarted without end, at the cost of the machine's limit and with nothing said; rejected outright.
- Every stop is reported to that person at once, with no attempt to recover: it lost because a stop that one further attempt clears would spend that person's attention on what could have been settled; reopen if recovered runs are found to have repeated acts or lost work that a report first would have saved.

## Decision Boundary

Not covered: how a stop is found and told apart from a run working long or rightly waiting (`ADR-D-a-stopped-run-is-found-without-the-person.md`); the limit itself, how many attempts and of what kind, and what counts as the same stop, which the Counsel text states; an attempt that would repeat an act that cannot be undone, which is not made; what the report to that person holds; what happens when the machine's limit for a period is reached; what a session does about something it dispatched work to that has stopped (ADR-D-0021).

## Validation

The decision is broken where a stopped run is tried again past the stated limit, or no limit is stated; or where a run that did not recover within the limit has not reached the person directing the work as a report.

## Revisit When

- The premise that a bounded number of attempts recovers most stops fails. No run under a brief had been recovered this way on 2026-11-14; stops that regularly reach that person after the limit, with a cause a further attempt would have cleared, or attempts that regularly fail, reopen the limit, not the decision.

## More Information

Source of intent: the brief "One conversation with Counsel", "What reaches him" and "Core scenarios". Related: ADR-D-0051 (the run), ADR-D-0062 (everything that needs that person reaches them through Counsel).
