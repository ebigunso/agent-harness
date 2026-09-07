---
status: proposed
adr_type: design
date: 2026-09-07
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1"]
informed: []
supersedes: ["ADR-D-0006-repository-rule-suite-bootstrap-lifecycle.md"]
superseded_by: null
---

# ADR-D-0025: Rule-suite freshness is derived from repository facts, never from a stored status

## Context and Problem Statement

A repository rule suite goes stale when the sources it was written from change: validation commands, build manifests, agent instruction files, review policy. Something has to decide whether the suite is still valid and when a targeted refresh is due. The fork is whether that judgment is stored (a status flag, a "last verified" commit) or derived each time from what the repository contains.

## Decision

Rule-suite validity is derived, never trusted from stored state. A suite is valid when its required files exist, the index and every role file share one suite ID, the schema version matches what the plugin requires, and no relevant source drift or contradiction is known. Git commit SHAs are not a freshness baseline. Refresh is targeted and triggered by facts: changes to rule-source paths in the current task, drift detected through lifecycle metadata, contradictions reported by any role or the user, schema migration, or repeated review misses that expose missing policy. Bootstrap is never a per-task ritual.

## Why

A stored status is one more thing that can be stale, and it fails in the worst direction: it says "fresh" precisely when nobody has looked, while squash and rebase merges erase the commits a SHA baseline would compare against.

## Rejected Alternatives

- A durable status flag in the index: rejected outright; it reintroduces the staleness it is meant to detect.
- A commit SHA baseline: reopen if the repository's merge policy guarantees linear history with preserved commits.
- Full bootstrap or a repository-wide scan on every task: rejected outright; the cost lands on every task to catch a rare event.

## Decision Boundary

Invariant: no stored "fresh" or "verified" state and no commit baseline decides validity; every validity check derives from files, suite ID, schema version, and known drift or contradictions.

Not covered: the exact refresh triggers, which sections a refresh touches, and the drift heuristics, which live in the `rulebook` skill and the sidecar schema.

## Validation

- Package validation checks that rulebook lifecycle references exist and that the index template carries no status flag.
- Review of any rulebook change asks whether a new field stores a judgment that should be derived.

## Revisit When

- Runtimes gain lifecycle hooks that observe source changes directly and can maintain freshness without stored state or prompt cost (none on 2026-09-07).
- Repeated refresh misses show the derivation needs a stricter sidecar schema; that is a schema change, not a return to stored status.

## More Information

Replaces ADR-D-0006 together with ADR-D-0024. Sidecar placement: ADR-D-0024.
