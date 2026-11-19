---
status: proposed
adr_type: design
date: 2026-11-17
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1", "Claude Fable 5.2"]
informed: []
supersedes: ["ADR-D-0049-each-session-roles-workflow-mechanics-have-one-home-and-every-runtime-surface-routes-to-it.md"]
superseded_by: null
---

# ADR-D (not yet numbered): What session roles share is stated once, in a home that is no role's

## Context and Problem Statement

Terms used here: a session role is a role a session itself holds. A role's home is the one place its workflow is stated (`ADR-D-each-session-roles-workflow-is-stated-in-one-home-and-no-runtime-surface-restates-it.md`).

Each session is to stay at its role's level, so a session never loads another role's home (`ADR-D-a-session-takes-its-workflow-only-from-its-own-roles-home.md`). The roles also read some of the same things, the documents that pass between them for one, and every role is to be able to read those. Stated in one role's home, what roles share reaches the other roles only by their loading that home, with that role's workflow in it. The fork is where what roles share is stated.

## Decision

- What roles share is stated once, in a home of its own that is no role's: the role homes point to it, and it points to none of them and states no role's procedure.

## Why

A shared home that is no role's lets every role read what the roles share without any reading another's home, and a shared home that stated a role's procedure would put that role's workflow in front of every session that reads it, and a session drawn to another role's level stops speaking in terms a person can judge, which the product philosophy's "What goes wrong, in order" has what is meant established in.

## Rejected Alternatives

- What roles share is stated in the home of one of the roles: it lost because every other role would load that role's workflow in order to read it; reopen if sessions are allowed to load another role's home.

## Decision Boundary

Not covered: which home is the home of what roles share, which the role map states (ADR-D-0048); what the roles share; that a session never loads another role's home, and what each home states of an exchange more than one role has a part in (`ADR-D-a-session-takes-its-workflow-only-from-its-own-roles-home.md`); that a home is the only statement of its role's workflow (`ADR-D-each-session-roles-workflow-is-stated-in-one-home-and-no-runtime-surface-restates-it.md`).

## Validation

The decision is broken where something roles share is stated in a role's home and not in the shared one; where the shared home points to a role's home; or where the shared home states what a role does.

## Revisit When

- The premise that what roles share can be stated without stating what any role does fails: the shared home is found stating a role's procedure because what is shared could not be said without it.

## More Information

With `ADR-D-each-session-roles-workflow-is-stated-in-one-home-and-no-runtime-surface-restates-it.md` and `ADR-D-a-session-takes-its-workflow-only-from-its-own-roles-home.md`, replaces ADR-D-0049 in full; the decision carried here is the same. Related: ADR-D-0034 (Counsel is a separate session at its own level).
