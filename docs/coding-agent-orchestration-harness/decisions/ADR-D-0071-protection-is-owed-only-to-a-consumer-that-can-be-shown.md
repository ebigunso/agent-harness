---
status: proposed
adr_type: design
date: 2026-11-11
deciders: ["ebigunso"]
consulted: []
informed: []
supersedes: ["ADR-D-0016-protection-requires-demonstrable-consumers.md"]
superseded_by: null
---

# ADR-D-0071: Protection is owed only to a consumer that can be shown

## Context and Problem Statement

Terms used here: protection is anything a change adds or keeps so that existing behaviour stays as it is, a compatibility layer or a test assertion. A consumer is whoever or whatever relies on that behaviour.

Agents add two kinds of protection nobody asked for: they keep existing interfaces alive through compatibility layers, and they pin behaviour with test assertions beyond what the change requires. Each reads as diligence, and each is a standing obligation on all later work: a surface that must keep working, an assertion that must keep passing. The fork is whether protection is good in itself or must be owed to someone. What happens where it cannot be established whether a consumer exists is decided in ADR-D-0073.

## Decision

- Protection is justified only by a consumer or contract that exists and can be shown.
- Protection never counts as its own consumer, and a consumer that is only conceivable, or named only as a category, is not evidence.

## Why

Protection with nobody behind it costs every later change and benefits no one, and a requirement that a categorical consumer or the protection itself can satisfy enforces nothing, because an agent can always supply one of those.

## Rejected Alternatives

- Compatibility and added test assertions treated as good in themselves: it lost because it is the behaviour this record exists to stop; rejected outright.
- A consumer that need only be named, with no demand that it be shown and no bar on protection vouching for itself: it lost because naming a category or pointing at the protection always satisfies it, which leaves the default in place; rejected outright.
- A justification field for each test in the Worker's report: it lost because it adds ceremony to a report format every task depends on; reopen if guidance and review are shown not to hold the requirement.

## Decision Boundary

Invariant: protection needs a consumer or contract that can be shown, never itself and never a hypothetical one.

Not covered: what counts as showing a consumer; what is done about a consumer that is found; whether the person directing the work is asked where it cannot be established that a consumer exists (ADR-D-0073); the wording and location of the guidance.

## Validation

- Review of a change asks: does each compatibility layer and each added assertion map to a consumer that can be shown, other than itself?
- Review of an edit to the guidance in this area checks the direction of drift: an edit that weakens the demand that a consumer be shown, or readmits categorical consumers, needs a record replacing this one, not a prose fix.

## Revisit When

- The premise that agents, without this requirement, add protection nobody asked for no longer holds. It was held when the decision was first taken on 2026-09-01; the record of that date names no models checked.

## More Information

With ADR-D-0073, replaces ADR-D-0016 in full. This record carries its requirement that protection have a consumer that can be shown. What it decided for the case in which a consumer cannot be verified is ADR-D-0073's, and is changed there.
