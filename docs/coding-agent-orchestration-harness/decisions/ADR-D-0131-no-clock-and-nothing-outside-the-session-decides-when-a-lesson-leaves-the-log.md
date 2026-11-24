---
status: proposed
adr_type: design
date: 2026-11-24
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.2"]
informed: []
supersedes: []
superseded_by: null
---

# ADR-D-0131: No clock and nothing outside the session decides when a lesson leaves the log

## Context and Problem Statement

Terms used here: a lesson is what a session records of a mistake so that the same mistake is not made twice. The log is where a repository's lessons are kept while they wait. A lesson leaves the log when it is deleted, moves into the repository's rules, or moves somewhere in the person's own scope.

The log is to keep its purpose in every repository the harness is used in, whatever kind of work is done there, and a log whose entries leave only in occasional clean-ups on no trigger loses that purpose without anyone noticing. Something has to decide when a lesson leaves. The fork is whether that is a pace or a mechanism outside the session, or moments in the session's own work.

## Decision

- A lesson's leaving is decided at moments that occur in the work of any repository.
- No clock decides it, and nothing outside the session does: not a fixed pace, not a schedule of runs, not a job in a repository's automation.

## Why

A fixed pace does not give a good experience and runs do not occur at a fixed cadence, and a job in a repository's automation depends on the repository and can be out of reach where the repository is not wholly the person's; the handling is for every repository the harness is used in, and not for one kind.

## Rejected Alternatives

- A clock, a count of runs, or a job in the repository's automation clears the log: it lost because runs occur at no fixed cadence, and the automation depends on the repository and may be out of the person's reach; reopen if something outside the session is shown to be there, and the person's to change, in every repository the harness is used in.

## Decision Boundary

Not covered: which moments decide a lesson's leaving; which of the ways of leaving a lesson takes; what is asked of the person and what is done unasked, of which the part on new obligations has its own record (ADR-D-0129); what happens when a log has grown too large; where what leaves the log is kept; a log several people share; what a repository does to its own log by its own means.

## Validation

The decision is broken where a lesson's leaving is done by, or waits on, a fixed pace, a run's schedule, a job in the repository's automation, or anything else outside the session that is not the person; or where the handling of lessons works only in repositories of one kind of work or with automation the person controls.

## Revisit When

- The premise that runs occur at no fixed cadence and that a repository's automation may be out of the person's reach fails for the repositories the harness is used in: something outside the session is shown to be there, and the person's to change, in every one of them.

## More Information

Source of intent: the brief "Lessons keep their purpose", "Who it is for and why", "A lesson waits, and then leaves", "When it is decided" and "Left out on purpose".
