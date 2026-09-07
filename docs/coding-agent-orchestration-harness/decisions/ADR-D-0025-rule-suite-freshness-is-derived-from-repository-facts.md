---
status: accepted
adr_type: design
date: 2026-09-08
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1"]
informed: []
supersedes: ["superseded/ADR-D-0006-repository-rule-suite-bootstrap-lifecycle--superseded-by-ADR-D-0024.md"]
superseded_by: null
---

# ADR-D-0025: Rule-suite freshness is derived from repository facts, never from a stored status

## Context and Problem Statement

A repository rule suite goes stale when the sources it was written from change: validation commands, build manifests, agent instruction files, review policy. Something has to decide whether the suite is still valid and when a targeted refresh is due. The fork is whether that judgment is stored (a status flag, a "last verified" commit) or derived each time from what the repository contains.

## Decision

Rule-suite validity is derived from what the repository contains each time it is needed, never trusted from stored state, and a Git commit SHA is not a freshness baseline. Refresh is targeted and triggered by observed facts about the repository and the work, never by elapsed time or a stored flag; bootstrap is never a per-task ritual. The validity conditions and the refresh triggers themselves are `rulebook` skill text.

## Why

A stored status is one more thing that can be stale, and it fails in the worst direction: it says "fresh" precisely when nobody has looked, while squash and rebase merges erase the commits a SHA baseline would compare against.

## Rejected Alternatives

- A durable status flag in the index: rejected outright; it reintroduces the staleness it is meant to detect.
- A commit SHA baseline: reopen if the repository's merge policy guarantees linear history with preserved commits.
- Full bootstrap or a repository-wide scan on every task: rejected outright; the cost lands on every task to catch a rare event.

## Decision Boundary

Invariant: no stored "fresh" or "verified" state and no commit baseline decides validity; every validity check derives from current repository facts.

Not covered: the exact refresh triggers, which sections a refresh touches, and the drift heuristics, which live in the `rulebook` skill and the sidecar schema.

## Validation

- Package validation checks that rulebook lifecycle references exist and that the index template carries no status flag.
- Review of any rulebook change asks whether a new field stores a judgment that should be derived.

## Revisit When

- Runtimes gain lifecycle hooks that observe source changes directly and can maintain freshness without stored state or prompt cost (none on 2026-09-07).
- Repeated refresh misses show the derivation needs a stricter sidecar schema; that is a schema change, not a return to stored status.

## More Information

Replaces ADR-D-0006 together with ADR-D-0024. Sidecar placement: ADR-D-0024.
