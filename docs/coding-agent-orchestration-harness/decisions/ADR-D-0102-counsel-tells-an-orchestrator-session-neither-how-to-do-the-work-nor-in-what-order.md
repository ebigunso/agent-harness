---
status: accepted
adr_type: design
date: 2026-11-19
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1", "Claude Fable 5.2", "GPT-6 Astra"]
informed: []
supersedes: ["superseded/ADR-D-0043-counsel-speaks-to-the-orchestrator-only-in-the-words-of-the-person-directing-the-work--superseded-by-ADR-D-0097.md"]
superseded_by: null
depends_on: ["ADR-D-0034-counsel-is-a-separate-session-at-the-level-of-behaviour-and-decisions.md"]
---

# ADR-D-0102: Counsel tells an Orchestrator session neither how to do the work nor in what order

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session role that person talks with about what the product does or should do. The Orchestrator session is a session that holds the Orchestrator role and plans, dispatches and reports the work.

The session the person directing the work talks with is to stay at the level of what is wanted, so that that person is never drawn into how the work is made (ADR-D-0034). Counsel is in contact with Orchestrator sessions all the same: it sees a run's questions and what is being decided, and it answers them in that person's words or with a reading of its own. Each such message is an occasion to say what should be done next, how, or which thing first, and Counsel holds none of that person's authority to say it. The fork is whether anything Counsel says to an Orchestrator session may direct how the work is done.

## Decision

- Counsel tells an Orchestrator session neither how to do the work nor in what order.
- The one exception is a stop of part of the work, which Counsel issues only as its own record provides (ADR-D-0044).

## Why

Anything Counsel tells an Orchestrator session about how the work is done is an instruction with no authority behind it, and a Counsel that settles how tasks are done is directing the work; the person who talks with it is then one step from judging implementation, where the product philosophy's "Who it is for" asks of them only what they want and whether what they got is it.

## Rejected Alternatives

- Counsel gives an Orchestrator session its opinion on how the work is done, marked as not binding: it lost because the session that person talks with would then be working at the level of plans, and an Orchestrator session cannot tell how much weight the opinion of the session nearest that person is meant to carry; reopen if runs are found to have gone wrong in a way that a word from Counsel on how or in what order would have prevented and nothing else would.

## Decision Boundary

Not covered: what Counsel may say of what that person wants (ADR-D-0100, ADR-D-0097); whether and when Counsel may stop work (ADR-D-0044); how far Counsel reaches into the work (ADR-D-0099); when a ratified brief is handed over (ADR-D-0115); what Counsel sends in its own words that says nothing of what the work is to be or how it is done, and decides nothing in it; what Counsel is responsible for (ADR-D-0034).

## Validation

The decision is broken where Counsel told an Orchestrator session how to do the work or in what order.

## Revisit When

- The premise that Counsel can answer an Orchestrator session about what is wanted without saying how the work is done fails: Counsel's answers are found to have set how tasks were done or which came first.

## More Information

With ADR-D-0100, ADR-D-0097 and ADR-D-0103, replaces ADR-D-0043 in full. Carried here from it, unchanged: that Counsel gives no instruction on how the work is done or in what order, and the exception for a stop. Source of intent: `docs/coding-agent/briefs/completed/value-level-operation-brief.md`, "Roles and sessions"; the brief "One conversation with Counsel", "Directed during the run".
