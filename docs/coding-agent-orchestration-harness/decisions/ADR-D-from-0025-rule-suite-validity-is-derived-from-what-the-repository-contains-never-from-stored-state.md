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

# ADR-D-XXXX: Rule-suite validity is derived from what the repository contains each time it is needed, never trusted from stored state

## Context and Problem Statement

A repository rule suite goes stale when the sources it was written from change: validation commands, build manifests, agent instruction files, review policy. Something has to decide whether the suite is still valid. A judgment of validity that is stored, such as a status flag, does not serve this: it is one more thing that can be stale. The fork is whether the suite's validity is stored and trusted, or derived each time from what the repository contains.

## Decision

Rule-suite validity is derived from what the repository contains each time it is needed, never trusted from stored state.

## Why

A stored status is one more thing that can be stale, and it fails in the worst direction: it says "fresh" precisely when nobody has looked. This serves the engineering philosophy's "Contents that say what is so": "A later worker can rely only on what is honest about its own standing."

## Rejected Alternatives

- A durable status flag in the index: rejected outright; it reintroduces the staleness it is meant to detect.

## Decision Boundary

Not covered: the validity conditions themselves, which are `rulebook` skill text (`ADR-D-from-0025-a-rule-suites-validity-conditions-and-refresh-triggers-are-rulebook-skill-text.md`); that a Git commit SHA is not a freshness baseline (`ADR-D-from-0025-a-git-commit-sha-is-not-a-rule-suite-freshness-baseline.md`); the drift heuristics, which live in the `rulebook` skill and the sidecar schema; where the suite's lifecycle data is kept and when it is read (ADR-D-0024).

## Validation

The decision is broken where:

- a stored "fresh" or "verified" state, a status flag included, decided whether a rule suite is valid;
- a field of the rule suite stored a judgment of its validity, and that judgment was trusted in place of one derived from what the repository contains when the judgment is needed.

## Revisit When

- Runtimes gain lifecycle hooks that observe source changes directly and can maintain freshness without stored state or prompt cost (none on 2026-09-07).
- Repeated refresh misses show the derivation needs a stricter sidecar schema; that is a schema change, not a return to stored status.

## More Information

With `ADR-D-from-0025-a-git-commit-sha-is-not-a-rule-suite-freshness-baseline.md`, `ADR-D-from-0025-rule-suite-refresh-is-targeted.md`, `ADR-D-from-0025-rule-suite-refresh-is-triggered-by-observed-facts-never-by-elapsed-time-or-a-stored-flag.md`, `ADR-D-from-0025-rule-suite-bootstrap-is-never-a-per-task-ritual.md` and `ADR-D-from-0025-a-rule-suites-validity-conditions-and-refresh-triggers-are-rulebook-skill-text.md`, replaces ADR-D-0025 in full; the decision carried here is the same. Carried here from it: that validity is derived each time it is needed and never trusted from stored state, with its reason, its rejected alternative and its revisit conditions. It is a record of its own because it binds with any of the others retired: a suite whose refresh ran on a schedule, or whose freshness was judged against a commit, would still have to have its validity derived and not taken from a stored status. Sidecar placement: ADR-D-0024.
