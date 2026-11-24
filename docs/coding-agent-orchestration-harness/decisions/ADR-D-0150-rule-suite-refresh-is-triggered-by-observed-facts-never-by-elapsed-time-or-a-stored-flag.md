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

# ADR-D-0150: Rule-suite refresh is triggered by observed facts about the repository and the work, never by elapsed time or a stored flag

## Context and Problem Statement

A repository rule suite goes stale when the sources it was written from change: validation commands, build manifests, agent instruction files, review policy. Something has to decide when a refresh is due. A stored flag does not serve this: it is one more thing that can be stale, and it says "fresh" precisely when nobody has looked. Nor does elapsed time, which is not a change to any source. The fork is whether a refresh is triggered by what is observed of the repository and the work, or by elapsed time or a stored flag.

## Decision

Refresh of a rule suite is triggered by observed facts about the repository and the work, never by elapsed time or a stored flag.

## Why

A rule suite goes stale when the sources it was written from change, so what shows that a refresh is due is a fact observed about them or about the work; and a stored flag is one more thing that can be stale, and it fails in the worst direction: it says "fresh" precisely when nobody has looked. This serves the engineering philosophy's "Contents that say what is so": "A later worker can rely only on what is honest about its own standing."

## Rejected Alternatives

- A durable status flag in the index: rejected outright; it reintroduces the staleness it is meant to detect.

## Decision Boundary

Not covered: the exact refresh triggers and the drift heuristics, which live in the `rulebook` skill and the sidecar schema; that the refresh triggers themselves are `rulebook` skill text (ADR-D-0153); that refresh is targeted (ADR-D-0151); that bootstrap is never a per-task ritual (ADR-D-0152).

## Validation

The decision is broken where a refresh of a rule suite was triggered by elapsed time or a stored flag, or by something other than observed facts about the repository and the work.

## Revisit When

- Runtimes gain lifecycle hooks that observe source changes directly and can maintain freshness without stored state or prompt cost (none on 2026-09-07).
- Repeated refresh misses show the derivation needs a stricter sidecar schema; that is a schema change, not a return to stored status.

## More Information

With ADR-D-0148, ADR-D-0149, ADR-D-0151, ADR-D-0152 and ADR-D-0153, replaces ADR-D-0025 in full; the decision carried here is the same. Carried here from it: what triggers a refresh and what never does, with the rejected alternative of a durable status flag, which ADR-D-0148 carries as well for its own decision, and the revisit conditions that bear on it. It is a record of its own because it binds with any of the others retired: were validity allowed to be stored, or refresh to reach the whole suite, a refresh would still be triggered by observed facts and never by elapsed time or a stored flag.
