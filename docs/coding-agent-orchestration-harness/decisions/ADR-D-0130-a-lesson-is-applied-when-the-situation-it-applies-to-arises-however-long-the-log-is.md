---
status: proposed
adr_type: design
date: 2026-11-24
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.2", "GPT-6 Astra"]
informed: []
supersedes: []
superseded_by: null
---

# ADR-D-0130: A lesson is applied when the situation it applies to arises, however long the log is

## Context and Problem Statement

Terms used here: a lesson is what a session records of a mistake so that the same mistake is not made twice. The log is where a repository's lessons are kept while they wait.

A lesson exists so that the same mistake is not made twice. Where lessons are read at the start of work, a lesson reaches only a situation that can be recognized then, and only while the log is short enough for that reading to reach every entry; a situation that first becomes recognizable halfway through the work is not reached. The fork is whether a lesson's reach is tied to the reading at the start of work, with the log kept short enough for it, or to the situation the lesson applies to, whenever in the work that situation arises.

## Decision

- A lesson's reach is not confined to the reading at the start of work and does not depend on the length of the log.
- A lesson is applied when the situation it applies to arises: at the start of work for what is known then, and partway through for what only becomes clear later.

## Why

The mistake a lesson prevents can sit at an action nobody foresaw when the work started, as when a task turns out to end in such an action, so a lesson that reaches only the start of work does not prevent it; and a reach that depends on the log staying short fails as the log grows. The product philosophy's "What goes wrong, in order" says "What the harness can find out, it finds out", and a lesson that waits in the log when its situation arises is something the harness can find out.

## Rejected Alternatives

- The log stays short enough for the reading at the start of work to reach every entry: it lost because the likeliest failure is a situation that first becomes recognizable halfway through the work, and because a reach that depends on the log staying short fails as the log grows; reopen if the situations lessons apply to are shown to be recognizable at the start of work.

## Decision Boundary

Not covered: how a session finds the lessons that bear on what it is about to do, and how it comes to look for one partway through work, which are left to the harness's text; what a waiting lesson requires of the session that applies it, which its own record states (ADR-D-0129); when a lesson leaves the log (ADR-D-0131); what happens when a log has grown too large; a log several people share; the form of an entry.

## Validation

The decision is broken where a lesson's application is confined to the start of work, or is made to depend on the log being short.

## Revisit When

- The premise that a situation a lesson applies to can first become recognizable partway through work fails: such situations are shown always to be recognizable at the start of work, so that a reading then would reach them.

## More Information

Source of intent: the brief "Lessons keep their purpose", "Who it is for and why", "A lesson waits, and then leaves", "Core scenarios" (1 and 4) and "Left out on purpose".
