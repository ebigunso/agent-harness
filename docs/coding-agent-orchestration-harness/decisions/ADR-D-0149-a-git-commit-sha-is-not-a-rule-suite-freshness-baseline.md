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

# ADR-D-0149: A Git commit SHA is not a rule-suite freshness baseline

## Context and Problem Statement

A repository rule suite goes stale when the sources it was written from change, and whether it is still fresh could be judged by comparing the repository against a "last verified" commit recorded as a baseline. That comparison needs the commit to remain in the history, and squash and rebase merges erase the commits a SHA baseline would compare against. The fork is whether a Git commit SHA may serve as the baseline for a rule suite's freshness.

## Decision

A Git commit SHA is not a freshness baseline for a rule suite.

## Why

Squash and rebase merges erase the commits a SHA baseline would compare against.

## Rejected Alternatives

- A commit SHA baseline: reopen if the repository's merge policy guarantees linear history with preserved commits.

## Decision Boundary

Not covered: that validity is derived from what the repository contains and never trusted from stored state (ADR-D-0148); the drift heuristics, which live in the `rulebook` skill and the sidecar schema.

## Validation

The decision is broken where a Git commit SHA served as the baseline against which a rule suite's freshness was judged, or a commit baseline decided whether a rule suite is valid.

## Revisit When

- The repository's merge policy guarantees linear history with preserved commits.

## More Information

With ADR-D-0148, ADR-D-0151, ADR-D-0150, ADR-D-0152 and ADR-D-0153, replaces ADR-D-0025 in full; the decision carried here is the same. Carried here from it: that a Git commit SHA is not a freshness baseline, with its own reason and its own reopen condition. It is a record of its own because it binds with any of the others retired: were a stored status allowed to decide validity, a baseline taken as a commit SHA would still be ruled out, and it reopens on a premise, the repository's merge policy, that none of the others rests on.
