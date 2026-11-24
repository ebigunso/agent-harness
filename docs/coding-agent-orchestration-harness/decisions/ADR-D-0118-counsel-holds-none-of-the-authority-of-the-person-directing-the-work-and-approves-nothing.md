---
status: proposed
adr_type: design
date: 2026-11-24
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1", "Claude Fable 5.2"]
informed: []
supersedes: ["ADR-D-0034-counsel-is-a-separate-session-at-the-level-of-behaviour-and-decisions.md"]
superseded_by: null
depends_on: ["ADR-D-0105-harness-text-holds-none-of-the-users-authority.md"]
---

# ADR-D-0118: Counsel holds none of the authority of the person directing the work and approves nothing

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session role that person talks with about what the product does or should do and about how the project should look.

What is ratified or approved in a piece of work is to be the decision of the person directing it. Counsel is the session that person talks with: it hears what they want, words it, and writes the documents the work is built from. A session that close to that person's wishes can always say what they would probably ratify or approve, and letting it do so would spare them the act. What then stands as ratified or approved is Counsel's decision under that person's name. The fork is whether the session that holds the discussion may ratify or approve anything for that person.

## Decision

- Counsel holds none of the authority of the person directing the work. It drafts and restates, and only that person's own act ratifies anything.
- Counsel approves nothing, a plan, a decision record and a merge included.

## Why

An agent that ratified or approved for the person directing the work would hold that person's authority, against ADR-D-0105. The statement served is the product philosophy's "What it aspires to", which has "saying what they want, and judging what they got" as "the two things only they can do": what Counsel ratified or approved for that person would be Counsel's saying and Counsel's judging.

## Rejected Alternatives

- Counsel approving plans, decision records or merges on that person's behalf: rejected outright; an agent would hold that person's authority, against ADR-D-0105.

## Decision Boundary

Not covered: where value discussion and ratification are held, and the level Counsel works at (ADR-D-0117); how that person's word reaches an Orchestrator session, and what admits Counsel's relays of it (ADR-D-0112, ADR-D-0111); what Counsel gives an Orchestrator session as that person's and what it gives as its own (ADR-D-0100, ADR-D-0097); Counsel's stop of part of the work, which decides nothing for that person (ADR-D-0121); which questions Counsel settles without bringing them to that person (ADR-D-0125); when a ratified brief is handed over (ADR-D-0115); what authorizes work, and whether a plan is put to anyone for approval (ADR-D-0064, ADR-D-0065); who states a product's values (ADR-D-0119); the form an act of ratification takes and how it is recorded, which the harness text states.

## Validation

The decision is broken where something stands as ratified that rests on Counsel's act and not on an act of the person directing the work, or where Counsel approved anything, a plan, a decision record or a merge included.

## Revisit When

- The premise that ratifying and approving are acts of the person directing the work, which no agent performs for them, no longer holds.

## More Information

With ADR-D-0117, replaces ADR-D-0034 in full; the decision carried here is the same. Carried here from it: that Counsel holds none of that person's authority, that only that person's own act ratifies, and that Counsel approves nothing. It is a record of its own because it would still bind if value discussion were held in a session that also did the work. Source of intent: `docs/coding-agent/briefs/completed/value-level-operation-brief.md`, "What Counsel is" and "Roles and sessions". Related: ADR-D-0103 (Counsel's advice goes to that person).
