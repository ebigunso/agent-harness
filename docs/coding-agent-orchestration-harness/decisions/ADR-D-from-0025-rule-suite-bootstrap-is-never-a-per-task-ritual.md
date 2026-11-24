---
status: proposed
adr_type: design
date: 2026-11-24
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1", "Claude Opus 5.5"]
informed: []
supersedes: ["ADR-D-0025-rule-suite-freshness-is-derived-from-repository-facts.md"]
superseded_by: null
---

# ADR-D-XXXX: Rule-suite bootstrap is never a per-task ritual

## Context and Problem Statement

A repository rule suite goes stale when the sources it was written from change, and a stale suite has to be caught. Running a full bootstrap, or a repository-wide scan, as part of every task would catch it, but staleness is a rare event and the cost of catching it that way lands on every task. The fork is whether bootstrap of the suite runs as a ritual of every task.

## Decision

Bootstrap of a rule suite is never a per-task ritual.

## Why

A full bootstrap or a repository-wide scan on every task makes the cost land on every task to catch a rare event. This serves the product philosophy's "What it must not be": "Not heavier than the request. A small ask gets a small process."

## Rejected Alternatives

- Full bootstrap or a repository-wide scan on every task: rejected outright; the cost lands on every task to catch a rare event.

## Decision Boundary

Not covered: when a bootstrap is run and what it does, which the `rulebook` skill states; that refresh is targeted (`ADR-D-from-0025-rule-suite-refresh-is-targeted.md`) and what triggers it (`ADR-D-from-0025-rule-suite-refresh-is-triggered-by-observed-facts-never-by-elapsed-time-or-a-stored-flag.md`).

## Validation

The decision is broken where bootstrap of a rule suite was run as a ritual of every task.

## Revisit When

- Runtimes gain lifecycle hooks that observe source changes directly and can maintain freshness without stored state or prompt cost (none on 2026-09-07).

## More Information

With `ADR-D-from-0025-rule-suite-validity-is-derived-from-what-the-repository-contains-never-from-stored-state.md`, `ADR-D-from-0025-a-git-commit-sha-is-not-a-rule-suite-freshness-baseline.md`, `ADR-D-from-0025-rule-suite-refresh-is-targeted.md`, `ADR-D-from-0025-rule-suite-refresh-is-triggered-by-observed-facts-never-by-elapsed-time-or-a-stored-flag.md` and `ADR-D-from-0025-a-rule-suites-validity-conditions-and-refresh-triggers-are-rulebook-skill-text.md`, replaces ADR-D-0025 in full; the decision carried here is the same. Carried here from it: that bootstrap is never a per-task ritual, with the rejected alternative of a full bootstrap or a repository-wide scan on every task, which `ADR-D-from-0025-rule-suite-refresh-is-targeted.md` carries as well for its own decision, and the revisit condition that bears on it. It is a record of its own because it binds with any of the others retired: whatever decided validity or triggered a refresh, bootstrap would still not run as a ritual of every task.
