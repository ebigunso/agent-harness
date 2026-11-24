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

# ADR-D-XXXX: A rule suite's validity conditions and refresh triggers are rulebook skill text

## Context and Problem Statement

A repository rule suite's validity is derived from what the repository contains, and its refresh is triggered by observed facts about the repository and the work. Which conditions make a suite valid, and which facts trigger a refresh, have to be stated somewhere for agents to apply them. The fork is whether they are stated in the decision records that decide how validity and refresh work, or are the `rulebook` skill's text.

## Decision

The validity conditions and the refresh triggers of a rule suite themselves are `rulebook` skill text.

## Why

ADR-D-0025, from which this record is carried, gives this decision no reason, and none is supplied here.

## Decision Boundary

Not covered: that validity is derived from what the repository contains and never trusted from stored state (`ADR-D-from-0025-rule-suite-validity-is-derived-from-what-the-repository-contains-never-from-stored-state.md`); that refresh is triggered by observed facts and never by elapsed time or a stored flag (`ADR-D-from-0025-rule-suite-refresh-is-triggered-by-observed-facts-never-by-elapsed-time-or-a-stored-flag.md`); which sections a refresh touches and the drift heuristics, which live in the `rulebook` skill and the sidecar schema; the wording of the `rulebook` skill's text.

## Validation

The decision is broken where the validity conditions or the refresh triggers of a rule suite are not in the `rulebook` skill's text.

## Revisit When

- ADR-D-0025 names no premise for this decision, and none is supplied here.

## More Information

With `ADR-D-from-0025-rule-suite-validity-is-derived-from-what-the-repository-contains-never-from-stored-state.md`, `ADR-D-from-0025-a-git-commit-sha-is-not-a-rule-suite-freshness-baseline.md`, `ADR-D-from-0025-rule-suite-refresh-is-targeted.md`, `ADR-D-from-0025-rule-suite-refresh-is-triggered-by-observed-facts-never-by-elapsed-time-or-a-stored-flag.md` and `ADR-D-from-0025-rule-suite-bootstrap-is-never-a-per-task-ritual.md`, replaces ADR-D-0025 in full; the decision carried here is the same. Carried here from it: its Decision's sentence that the validity conditions and the refresh triggers themselves are `rulebook` skill text, as it stands there. It is a record of its own because it binds with any of the others retired: whatever conditions made a suite valid and whatever triggered a refresh, they would still be `rulebook` skill text.
