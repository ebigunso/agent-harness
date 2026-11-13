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

# ADR-D (not yet numbered): A run that has stopped making progress is found without the person directing the work, and either recovers within a stated limit or reaches that person as a report

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session role that person talks with about what the product does or should do. A run is the work done under one ratified brief.

A run goes on in a session the person directing the work does not watch (`ADR-D-a-ratified-briefs-run-starts-without-the-person-opening-anything.md`). When that session stops, nothing in it tells anyone: a stopped run, a run that is working long and a run that is rightly waiting for an answer are all quiet. On 2026-11-12 that person twice had to say that something had stopped. The fork is who notices a stop, and what is done about it before that person hears of it.

## Decision

- The person directing the work does not have to notice that a run or a seat has stopped. A run that has stopped making progress is found without that person.
- A stopped run is told apart from one that is working long and from one that is rightly waiting.
- A stopped run either recovers within a stated limit or reaches that person through Counsel as a clear report.
- A run is never restarted over and over.

## Why

A stop that only the person directing the work can notice makes that person the monitor of the machinery, which the product philosophy's "Who it is for" says is never asked of them, and a run that sits stopped is a wait nobody chose. Recovery is bounded because each attempt spends the machine's limit and hides the stop from the one person who could settle it; past the limit a report is the stated doubt the philosophy's "What goes wrong, in order" calls the remedy.

## Rejected Alternatives

- That person looks in on the runs, or is told only when they ask: it lost because that person would be watching sessions to learn whether the work is going; rejected outright.
- A stopped run is restarted until it goes: it lost because a run that stops for a cause a restart does not remove is restarted without end, at the cost of the machine's limit and with nothing said; rejected outright.
- Every stop is reported to that person at once, with no attempt to recover: it lost because a stop that one further attempt clears would spend that person's attention on what could have been settled; reopen if recovered runs are found to have repeated acts or lost work that a report first would have saved.
- A quiet run is treated as stopped after a fixed time: it lost because a run working long and a run rightly waiting are quiet too, and stopping or restarting either undoes sound work; reopen if a supported runtime is found to give no way at all to tell them apart.

## Decision Boundary

Not covered: by what means a run is watched and how its state is read, which the workspace's record states; what a run's own reports say of where it stands; the limit itself, how many attempts and of what kind, and what counts as the same stop, which the Counsel text states; an attempt that would repeat an act that cannot be undone, which is not made; what the report to that person holds; a run that stops because it has stopped getting closer to its goal and says so, which the workflow text states; what happens when the machine's limit for a period is reached; how a seat that stops under an Orchestrator session is replaced (`ADR-D-nothing-depends-on-a-seat-surviving.md`).

## Validation

The decision is broken where a run has stopped making progress and the first to notice is the person directing the work; where a run that was working or rightly waiting is stopped or restarted as if it had stopped; where a stopped run is tried again past the stated limit, or no limit is stated; or where a run that did not recover within the limit has not reached that person as a report.

## Revisit When

- What can be read of a session from outside changes. On 2026-11-12, in Claude Code, a started session's state could be read from outside as working, waiting with the kind of thing waited for, finished its turn, or stopped; nothing seen told a session working long from one that was stuck while its process lived, so that case rested on a judgement from the run's last report. A stuck run that went unnoticed under that judgement, or a working run treated as stopped, reopens how a stop is told apart.
- The premise that a bounded number of attempts recovers most stops fails. No run under a brief had been recovered this way on 2026-11-14; stops that regularly reach that person after the limit, with a cause a further attempt would have cleared, or attempts that regularly fail, reopen the limit, not the decision.

## More Information

Source of intent: the brief "One conversation with Counsel", "What reaches him" and "Core scenarios"; the limit on recovery is the advice of the model consulted for that brief. Related: ADR-D-0044 (Counsel's pause, which is a stop Counsel issues and not one it finds), ADR-D-0051 (the run), ADR-D-0062 (everything that needs that person reaches them through Counsel).
