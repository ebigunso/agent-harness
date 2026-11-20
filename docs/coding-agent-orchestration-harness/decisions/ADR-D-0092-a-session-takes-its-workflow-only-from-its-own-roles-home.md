---
status: accepted
adr_type: design
date: 2026-11-17
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1", "Claude Fable 5.2"]
informed: []
supersedes: ["superseded/ADR-D-0049-each-session-roles-workflow-mechanics-have-one-home-and-every-runtime-surface-routes-to-it--superseded-by-ADR-D-0092.md"]
superseded_by: null
---

# ADR-D-0092: A session takes its workflow only from the home of the role it holds

## Context and Problem Statement

Terms used here: a session role is a role a session itself holds. A role's home is the one place its workflow is stated (ADR-D-0104).

A session holds one role, and there is more than one session role, each working at a level of its own (ADR-D-0034). Each session is to stay at its role's level, and the session a person talks with above all, because that person can judge only what is said at theirs. One home for everything would be the simplest to keep, and a session would then have another role's workflow in front of it together with its own. The fork is whether a session may read another role's home.

## Decision

- A session takes its workflow from the home of the role it holds and never loads another role's home.
- Where more than one role has a part in one exchange, each home states only its own role's part.

## Why

A session that reads another role's workflow is drawn to that role's level of work, and the session a person talks with then stops speaking in terms that person can judge, which the product philosophy's "What goes wrong, in order" has what is meant established in.

## Rejected Alternatives

- One home for every session role: it lost because a session would load another role's workflow with its own; reopen if two homes are found restating each other's rules.

## Decision Boundary

Not covered: where what roles share is stated (ADR-D-0114); which session roles exist and which skill is the home of each, which the role map states (ADR-D-0048); that a home is the only statement of its role's workflow (ADR-D-0104); what each role is responsible for (ADR-D-0034); how a session comes to hold a role (ADR-D-0090); what a role is told of another role's part where it needs to know what to expect.

## Validation

The decision is broken where a session holding one role loaded another role's home; or where one role's home states another role's part of an exchange as procedure.

## Revisit When

- The premise that the roles' workflows can be kept apart fails: two homes are found restating each other's rules.

## More Information

With ADR-D-0104 and ADR-D-0114, replaces ADR-D-0049 in full; the decision carried here is the same. It is a record of its own because it would still bind if runtime surfaces were allowed to restate a workflow. Related: ADR-D-0034 (Counsel is a separate session at its own level).
