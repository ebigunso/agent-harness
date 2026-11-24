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

# ADR-D-0151: Rule-suite refresh is targeted

## Context and Problem Statement

A repository rule suite goes stale when the sources it was written from change: validation commands, build manifests, agent instruction files, review policy. When it has, a refresh brings it back. Bringing it back by a full bootstrap or a repository-wide scan on every task makes the cost land on every task to catch a rare event. The fork is whether a refresh of the suite is targeted, or reaches as far as a full bootstrap or a scan of the whole repository.

## Decision

Refresh of a rule suite is targeted.

## Why

A rule suite goes stale when the sources it was written from change, so a refresh limits itself to what in the suite needs attention.

## Rejected Alternatives

- Full bootstrap or a repository-wide scan on every task: rejected outright; the cost lands on every task to catch a rare event.

## Decision Boundary

Not covered: which sections a refresh touches, which lives in the `rulebook` skill and the sidecar schema; what triggers a refresh (ADR-D-0150), and where the exact refresh triggers are stated (the accepted ADR-D-0025); that bootstrap is never a per-task ritual (ADR-D-0152).

## Validation

The decision is broken where a refresh rewrote the whole rule suite where only a part of it needed attention.

## Revisit When

- Runtimes gain lifecycle hooks that observe source changes directly and can maintain freshness without stored state or prompt cost (none on 2026-09-07).
- Repeated refresh misses show the derivation needs a stricter sidecar schema; that is a schema change, not a return to stored status.

## More Information

With ADR-D-0148, ADR-D-0149, ADR-D-0150 and ADR-D-0152, replaces ADR-D-0025; the decision carried here is the same. ADR-D-0025's sentence that the validity conditions and the refresh triggers are `rulebook` skill text is held for the owner's answer and not carried here; ADR-D-0025 is replaced in full only once that is settled. Carried here from it: that refresh is targeted, with the rejected alternative of a full bootstrap or a repository-wide scan on every task, which ADR-D-0152 carries as well for its own decision, and the revisit conditions that bear on it. It is a record of its own because it binds with any of the others retired: a refresh triggered by anything at all would still have to be targeted.
