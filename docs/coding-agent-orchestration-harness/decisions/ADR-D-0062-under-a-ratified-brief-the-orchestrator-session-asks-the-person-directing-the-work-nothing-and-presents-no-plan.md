---
status: proposed
adr_type: design
date: 2026-10-29
deciders: ["ebigunso"]
consulted: ["Claude Opus 5.5"]
informed: []
supersedes: []
superseded_by: null
depends_on: ["ADR-D-0038-the-word-of-the-person-directing-the-work-reaches-an-orchestrator-session-directly-or-by-quoted-relay.md", "ADR-D-0064-non-trivial-work-is-authorized-only-by-the-person-directing-the-work-or-by-that-persons-ratified-brief.md", "ADR-D-0065-a-ratified-brief-authorizes-a-plan-only-through-a-closed-plan-review-and-a-value-audit-that-holds-nothing-above-the-run.md", "ADR-D-0043-counsel-speaks-to-the-orchestrator-only-in-the-words-of-the-person-directing-the-work-and-its-advice-goes-to-that-person.md", "ADR-D-0051-work-under-a-brief-is-a-run-of-one-or-more-units-that-closes-once.md"]
---

# ADR-D-0062: While a ratified brief governs a run, the Orchestrator session puts no question to the person directing the work: whatever needs that person, of any kind, reaches that person through Counsel or ends the turn blocked, and a plan is never presented for approval, in that session or through Counsel

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session the person directing the work opens for value discussion, separate from any Orchestrator session. The Orchestrator session is a session that holds the Orchestrator role (ADR-D-0020) and plans, dispatches and reports the work.

A person who hands over a ratified brief talks with Counsel and judges the result; the run goes on without that person (ADR-D-0051). Questions at the level of direction already travel through Counsel, but the route was written as an exception for that kind of question and for a list of consent gates. Every other kind fell back to the Orchestrator session: the questions slot of a final response, a confirmation at a replan, and the approval of a plan the brief route did not authorize. Before 2026-10-28 an Orchestrator session under a ratified brief asked for plan approval in its own session, so the person who had handed the work over had to watch that session after all. The fork is whether the route through Counsel is an exception for some kinds of question or the default for every question while a brief governs, and what becomes of plan approval under a brief.

## Decision

- While a ratified brief governs a run, every question that needs the person directing the work, whatever its kind, travels through Counsel: a decision at the level of direction, an act that person reserved, and what only that person can give (an act, a permission or an input no statement of that person's covers and no one else can supply). The answer returns as ADR-D-0038 states. The Orchestrator session puts no question to that person.
- An instruction elsewhere that asks the user reads, under a brief, as sending the question through Counsel or, where the turn cannot go on without the answer, as ending the turn blocked and naming what it waits on. The final response names what is with Counsel and what the turn ended blocked on, in place of questions.
- A brief, a hand-over or a dispatch arriving as a message in the Orchestrator session does not make the person directing the work present there for questions. Anyone may still talk to that session directly, and a question is answered where it was asked.
- Under a brief a plan is never presented for approval, in the Orchestrator session or through Counsel: it is authorized by the brief route (ADR-D-0065) or it does not run. When the route does not authorize it, the Orchestrator has three moves: correct its own input and have the plan audited again, carry the verdict's value question through Counsel, or end the turn blocked naming the condition that failed.
- The agreement to a goal-mode envelope is one of these questions: under a brief it reaches the person directing the work through Counsel, and that person's relayed answer agreeing to it starts the loop (ADR-D-0063, ADR-D-0064).
- Each consent gate keeps its own terms; only the carrier is added. The runtime's own permission for the merge tool, which no relay carries, is not asked for either: a merge waiting for it ends the turn blocked, naming it.
- Work no brief governs, a run on a philosophy alone included, is unchanged: its plan is presented and its user asked in the Orchestrator session.

## Why

While a run under a ratified brief is in progress, the person directing the work should never need to look at the Orchestrator session, yet a session under a brief asked that person for plan approval in its own session. The route through Counsel was written as an exception for one kind of question, so every other kind fell back to the session; stated as the default for every kind while a brief governs, it leaves the session nothing to ask, and a new instruction that asks the user is right under a brief with no edit. A plan under a brief is authorized by the brief route or is not yet a plan that can run, so there is no approval left to ask for, in the session or through Counsel.

## Rejected Alternatives

- Carrying plan approval through Counsel when the brief route does not authorize the plan: it lost because a plan the route does not authorize is not yet a plan that can run, so there is nothing for an approval to add; reopen if runs under a brief are found unable to end with nothing asked of the person directing the work in the Orchestrator session without it.
- Adding a clause that sends the question through Counsel to each instruction that asks the user: it lost because the route stays an exception written line by line, and a line without the clause sends its question back to the session; reopen if a run under a brief is found asking in the Orchestrator session through an instruction the default was meant to cover.
- Leaving the agreement to a goal envelope as the one question asked in the Orchestrator session: rejected outright; the person directing the work would have to look at that session for that case.
- A hand-over or a dispatch arriving as a message counts as the person directing the work being present for questions: rejected outright; it is the reading under which a session handed its work by a message goes on to ask in that session, which the statement on message arrival in the governing brief excludes.

## Decision Boundary

Invariant: while a ratified brief governs a run, the Orchestrator session puts no question to the person directing the work; every question that needs that person travels through Counsel or ends the turn blocked naming it; no plan is presented for approval, in that session or through Counsel; work no brief governs is unchanged; the Decision list states the rest.

Not covered: how a relay is admitted and what counts as the answer (ADR-D-0038); the sources of authorization (ADR-D-0064), the conditions of the brief route (ADR-D-0065) and of a small change built without a plan (ADR-D-0055); what Counsel does with what it receives (ADR-D-0043); what the value audit grades (ADR-D-0052); the grant of the runtime's merge-tool permission itself, which stays that person's to give in the session; how a goal envelope is graded (ADR-D-0063); the wording of the instructions that ask the user.

## Validation

- Under a brief, no Orchestrator session presents a plan for approval or phrases a question to the person directing the work; a plan the brief route did not authorize shows one of the three moves in its Progress Log.
- Under a brief, a final response names what is with Counsel and what the turn ended blocked on, and phrases nothing as a question to its reader.
- A run with no brief presents its plan and asks in the Orchestrator session.

## Revisit When

- On 2026-10-29 no run under a brief had yet ended with nothing asked of the person directing the work in the Orchestrator session; a run under a brief that asks that person anything there reopens this record.
- A run without Counsel is found to need its questions kept out of the Orchestrator session as a run under a brief has them.

## More Information

Source of intent: the brief "A quiet Orchestrator session under a brief" (`quiet-orchestrator-session-brief.md`), "Who it is for and why", "What the plugin states", "Directed during the run" and "Limits". The brief states as means that the lines asking the user are read through the default rather than each edited, and that a message's arrival does not make the person present; the three moves and the removal of plan approval are its gives-statements. Related: ADR-D-0038 (the word of the person directing the work), ADR-D-0064 and ADR-D-0065 (authorization), ADR-D-0043 (Counsel speaks only in that person's words), ADR-D-0051 (the run), ADR-D-0063 (a goal-mode run and its envelope).
