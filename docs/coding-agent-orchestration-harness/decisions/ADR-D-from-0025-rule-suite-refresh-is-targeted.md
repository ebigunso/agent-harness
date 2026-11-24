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

# ADR-D-XXXX: Rule-suite refresh is targeted

## Context and Problem Statement

A repository rule suite goes stale when the sources it was written from change: validation commands, build manifests, agent instruction files, review policy. When it has, a refresh brings it back. Bringing it back by a full bootstrap or a repository-wide scan on every task makes the cost land on every task to catch a rare event. The fork is whether a refresh of the suite is targeted, or reaches as far as a full bootstrap or a scan of the whole repository.

## Decision

Refresh of a rule suite is targeted.

## Why

A rule suite goes stale when the sources it was written from change, so what a refresh has to bring back is what was written from the sources that changed.

## Rejected Alternatives

- Full bootstrap or a repository-wide scan on every task: rejected outright; the cost lands on every task to catch a rare event.

## Decision Boundary

Not covered: which sections a refresh touches, which lives in the `rulebook` skill and the sidecar schema; what triggers a refresh (`ADR-D-from-0025-rule-suite-refresh-is-triggered-by-observed-facts-never-by-elapsed-time-or-a-stored-flag.md`), and the exact refresh triggers, which are `rulebook` skill text (`ADR-D-from-0025-a-rule-suites-validity-conditions-and-refresh-triggers-are-rulebook-skill-text.md`); that bootstrap is never a per-task ritual (`ADR-D-from-0025-rule-suite-bootstrap-is-never-a-per-task-ritual.md`).

## Validation

The decision is broken where a refresh of a rule suite was not targeted; a full bootstrap or a repository-wide scan run where a refresh was due is one such case.

## Revisit When

- Runtimes gain lifecycle hooks that observe source changes directly and can maintain freshness without stored state or prompt cost (none on 2026-09-07).
- Repeated refresh misses show the derivation needs a stricter sidecar schema; that is a schema change, not a return to stored status.

## More Information

With `ADR-D-from-0025-rule-suite-validity-is-derived-from-what-the-repository-contains-never-from-stored-state.md`, `ADR-D-from-0025-a-git-commit-sha-is-not-a-rule-suite-freshness-baseline.md`, `ADR-D-from-0025-rule-suite-refresh-is-triggered-by-observed-facts-never-by-elapsed-time-or-a-stored-flag.md`, `ADR-D-from-0025-rule-suite-bootstrap-is-never-a-per-task-ritual.md` and `ADR-D-from-0025-a-rule-suites-validity-conditions-and-refresh-triggers-are-rulebook-skill-text.md`, replaces ADR-D-0025 in full; the decision carried here is the same. Carried here from it: that refresh is targeted, with the rejected alternative of a full bootstrap or a repository-wide scan on every task, which `ADR-D-from-0025-rule-suite-bootstrap-is-never-a-per-task-ritual.md` carries as well for its own decision, and the revisit conditions that bear on it. It is a record of its own because it binds with any of the others retired: a refresh triggered by anything at all would still have to be targeted.
