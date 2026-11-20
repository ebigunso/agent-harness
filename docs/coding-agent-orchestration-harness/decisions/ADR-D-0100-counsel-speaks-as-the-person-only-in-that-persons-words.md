---
status: accepted
adr_type: design
date: 2026-11-19
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1", "Claude Fable 5.2", "GPT-6 Astra"]
informed: []
supersedes: ["superseded/ADR-D-0043-counsel-speaks-to-the-orchestrator-only-in-the-words-of-the-person-directing-the-work--superseded-by-ADR-D-0097.md"]
superseded_by: null
depends_on: ["ADR-D-0034-counsel-is-a-separate-session-at-the-level-of-behaviour-and-decisions.md", "ADR-D-0112-the-persons-word-reaches-an-orchestrator-session-in-it-or-by-counsels-quoted-relay.md"]
---

# ADR-D-0100: Counsel speaks as the person directing the work only in that person's words

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session role that person talks with about what the product does or should do. The Orchestrator session is a session that holds the Orchestrator role and plans, dispatches and reports the work.

The direction of the work is to stay with the person directing it, and Counsel holds none of that person's authority (ADR-D-0034). Counsel carries that person's decisions to an Orchestrator session (ADR-D-0112), and it heard the discussion those decisions came from, so on a point the words left open it can always say what that person would probably have said. An answer given so, as that person's, is acted on as their decision. The fork is whether what Counsel gives as that person's may go beyond what that person said.

## Decision

- Counsel speaks as the person directing the work only in that person's words, given for the matter at hand or standing from earlier.
- An answer given as that person's rests on a statement that explicitly covers the question; Counsel extends none.

## Why

An answer given as that person's is acted on with that person's authority, and one that extends their words is Counsel's decision under that person's name, with nothing to show that it happened. The statement served is the product philosophy's "The line": what waits for the person's yes waits for the person.

## Rejected Alternatives

- Counsel gives its own reading of what that person would want as what that person said: rejected outright; it would claim an authority Counsel does not hold (ADR-D-0034).

## Decision Boundary

Not covered: what Counsel may say to an Orchestrator session in its own name (ADR-D-0097, ADR-D-0102); when a quoted relay counts as that person's decision and what admits relays (ADR-D-0112); what Counsel is responsible for (ADR-D-0034); how a message travels between sessions.

## Validation

The decision is broken where Counsel gave something as that person's that no statement of that person's explicitly covers.

## Revisit When

- The premise that Counsel can tell a statement that explicitly covers a question from one it would be extending fails: Counsel is found answering as that person from a standing statement that did not explicitly cover the question.

## More Information

With ADR-D-0097, ADR-D-0102 and ADR-D-0103, replaces ADR-D-0043 in full. Carried here from it, unchanged: that Counsel speaks as that person only in that person's words and extends no statement. Moved out: the ways Counsel answers what an Orchestrator session sends, which Counsel's text states. Source of intent: `docs/coding-agent/briefs/completed/value-level-operation-brief.md`, "Roles and sessions"; the brief "One conversation with Counsel", "Directed during the run".
