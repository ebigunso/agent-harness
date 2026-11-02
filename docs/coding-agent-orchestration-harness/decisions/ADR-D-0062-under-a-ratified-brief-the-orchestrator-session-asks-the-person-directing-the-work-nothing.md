---
status: proposed
adr_type: design
date: 2026-10-29
deciders: ["ebigunso"]
consulted: ["Claude Opus 5.5"]
informed: []
supersedes: []
superseded_by: null
depends_on: ["ADR-D-0038-the-word-of-the-person-directing-the-work-reaches-an-orchestrator-session-directly-or-by-quoted-relay.md", "ADR-D-0043-counsel-speaks-to-the-orchestrator-only-in-the-words-of-the-person-directing-the-work-and-its-advice-goes-to-that-person.md", "ADR-D-0051-work-under-a-brief-is-a-run-of-one-or-more-units-that-closes-once.md"]
---

# ADR-D-0062: Under a ratified brief the Orchestrator session asks the person directing the work nothing

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session the person directing the work opens for value discussion, separate from any Orchestrator session. The Orchestrator session is a session that holds the Orchestrator role (ADR-D-0020) and plans, dispatches and reports the work.

A person who hands over a ratified brief talks with Counsel and judges the result; the run goes on without that person (ADR-D-0051). Questions at the level of direction travelled through Counsel, but as an exception for that kind of question and for a list of consent gates, and every other kind fell back to the Orchestrator session. Before 2026-10-28 an Orchestrator session under a ratified brief asked for plan approval in its own session, so the person who had handed the work over had to watch that session after all. The fork is whether Counsel is the way to that person for some kinds of question or for every kind while a brief governs.

## Decision

- While a ratified brief governs a run, the Orchestrator session puts no question to the person directing the work. Whatever needs that person, of any kind, reaches that person through Counsel.
- In place of questions, what the Orchestrator reports names what is with Counsel and what the work waits on.
- Nothing that needs the person directing the work is settled without that person because it cannot be asked in the Orchestrator session: each consent keeps its own terms, and only where it is asked changes.
- A brief, a hand-over or an instruction arriving as a message in the Orchestrator session does not make the person directing the work present there for questions. Anyone may talk to that session directly, and a question is answered where it was asked.
- Work no brief governs, a run on a philosophy alone included, is unchanged: its user is asked in the Orchestrator session.

## Why

While a run under a ratified brief is in progress, the person directing the work should never need to look at the Orchestrator session ("A quiet Orchestrator session under a brief", "Who it is for and why"). Counsel carrying only some kinds of question left every other kind, plan approval among them, to fall back to that session, so while a brief governs Counsel is the way to that person for every kind.

## Rejected Alternatives

- Counsel carries some kinds of question (those at the level of direction and the named consent gates), and every other kind, the agreement to a goal envelope included, is asked in the Orchestrator session: rejected outright; the person directing the work would have to watch that session for every kind left off the list.
- A hand-over or an instruction arriving as a message counts as the person directing the work being present for questions: rejected outright; it is the reading under which a session handed its work by a message goes on to ask in that session.

## Decision Boundary

Invariant: while a ratified brief governs a run, the Orchestrator session puts no question to the person directing the work; whatever needs that person reaches that person through Counsel, and the Orchestrator's report names what is with Counsel and what the work waits on in place of questions; no consent is loosened by it; a message's arrival does not make that person present; work no brief governs is unchanged.

Not covered: how a question reaches Counsel and what the Orchestrator does while the work waits on an answer, which the harness text states; how the answer is admitted and what counts as it (ADR-D-0038); what Counsel does with what it receives (ADR-D-0043); what authorizes a unit of work under a brief, and that no plan is put to that person for approval (ADR-D-0064, ADR-D-0065); an act only that person can perform in the session itself, such as granting a runtime permission; the wording of the instructions that ask the user and of the Orchestrator's report.

## Validation

- Under a brief, no Orchestrator session phrases a question to the person directing the work, and its report names what is with Counsel and what the work waits on.
- A run with no brief asks its user in the Orchestrator session.
- Review of any change to the harness text asks: under a brief, does any line put a question to the person directing the work in the Orchestrator session?

## Revisit When

- On 2026-10-29 no run under a brief had yet ended with nothing asked of the person directing the work in the Orchestrator session; a run under a brief that asks that person anything there reopens this record.
- A run without Counsel is found to need its questions kept out of the Orchestrator session as a run under a brief has them.

## More Information

Source of intent: the brief "A quiet Orchestrator session under a brief" (`docs/coding-agent/briefs/active/quiet-orchestrator-session-brief.md`), "Who it is for and why", "What the plugin states", "Directed during the run" and "Limits". How a question travels, how the harness text's instructions that ask the user read under a brief, and what the Orchestrator does when the work cannot go on without an answer are the harness text's and change without this record. Related: ADR-D-0038 (the word of the person directing the work), ADR-D-0043 (Counsel speaks only in that person's words), ADR-D-0051 (the run), ADR-D-0064 (the sources of authorization), ADR-D-0065 (when a ratified brief authorizes a plan).
