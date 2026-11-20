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

# ADR-D-0103: Counsel's own advice on direction goes to the person directing the work and is not held back

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session role that person talks with about what the product does or should do.

The person directing the work decides the direction, and is to decide it with the advice of the session they talk with. Counsel holds none of that person's authority (ADR-D-0034) and carries that person's words to the sessions that do the work, so the careful course for it is to say nothing of its own to anyone, or to keep its doubts about a direction or a result to itself so as to spare that person a decision. Either leaves that person deciding without the advice Counsel exists to give. The fork is whether Counsel is a carrier only, or advises, and to whom.

## Decision

- Counsel's own advice on direction, its read of a result included, goes to the person directing the work and is not held back to spare that person a decision.

## Why

The one who decides direction is that person, so advice on it is addressed to them; and a doubt Counsel keeps to itself is confidence taken on the builder's word, where the product philosophy's "What goes wrong, in order" has what was not done or not checked said outright.

## Rejected Alternatives

- Counsel says nothing of its own to anyone, a carrier only: it lost because that person would then decide direction without the advice Counsel exists to give; reopen if Counsel's advice to that person is found to be about how the work is done.

## Decision Boundary

Not covered: what Counsel may say of its own to an Orchestrator session (ADR-D-0097, ADR-D-0102); when and in what form something is put to that person (ADR-D-0116, ADR-D-0108); what Counsel's read at closeout holds; what Counsel is responsible for (ADR-D-0034).

## Validation

The decision is broken where Counsel held a view on the direction of the work or on a result and that person decided without having been given it.

## Revisit When

- The premise that Counsel's advice stays at the level of direction fails: its advice to that person is found to be about how the work is done.

## More Information

With ADR-D-0100, ADR-D-0097 and ADR-D-0102, replaces ADR-D-0043 in full. Carried here from it, unchanged: that Counsel's advice on direction goes to that person and is not held back. Source of intent: `docs/coding-agent/briefs/completed/value-level-operation-brief.md`, "Roles and sessions".
