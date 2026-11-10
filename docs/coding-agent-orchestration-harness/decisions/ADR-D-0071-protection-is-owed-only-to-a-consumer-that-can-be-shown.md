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

# ADR-D-0071: Protection is owed only to a consumer that can be shown, and where none can be verified the person directing the work is asked only about a surface that crosses the repository's boundary

## Context and Problem Statement

Terms used here: protection is anything a change adds or keeps so that existing behaviour stays as it is, a compatibility layer or a test assertion. A consumer is whoever or whatever relies on that behaviour. The person directing the work is the one who says what the work should do and judges what is built from its behaviour.

Agents add two kinds of protection nobody asked for: they keep existing interfaces alive through compatibility layers, and they pin behaviour with test assertions beyond what the change requires. Each reads as diligence, and each is a standing obligation on all later work: a surface that must keep working, an assertion that must keep passing. The fork is whether protection is good in itself or must be owed to someone, and, where nobody can establish whether a consumer exists, who settles it.

## Decision

- Protection is justified only by a consumer or contract that exists and can be shown.
- Protection never counts as its own consumer, and a consumer that is only conceivable, or named only as a category, is not evidence.
- Where it cannot be verified whether a consumer exists:
  - for a surface that crosses the repository's boundary, the question goes to the person directing the work, and the surface is neither kept nor broken without an answer;
  - for a surface inside the repository, the change goes ahead without the protection and is reported.

## Why

Protection with nobody behind it costs every later change and benefits no one, and a requirement that a categorical consumer or the protection itself can satisfy enforces nothing, because an agent can always supply one of those. Inside the repository a search that finds no consumer is real evidence that there is none, so asking would spend the person's attention on a question the repository already answers; across its boundary consumers cannot be seen from inside, so only the person can say whether one exists.

## Rejected Alternatives

- Compatibility and added test assertions treated as good in themselves: it lost because it is the behaviour this record exists to stop; rejected outright.
- A consumer that need only be named, with no demand that it be shown and no bar on protection vouching for itself: it lost because naming a category or pointing at the protection always satisfies it, which leaves the default in place; rejected outright.
- A justification field for each test in the Worker's report: it lost because it adds ceremony to a report format every task depends on; reopen if guidance and review are shown not to hold the requirement.
- Asking the person directing the work in every unverifiable case, inside the repository as well: it lost because inside the repository the absence of a found consumer already answers the question; reopen if changes made on that evidence are found to break consumers inside a repository.

## Decision Boundary

Invariant: protection needs a consumer or contract that can be shown, never itself and never a hypothetical one; an unverifiable consumer is a question for the person directing the work only where the surface crosses the repository's boundary, and inside the repository the change goes ahead and is reported.

Not covered: what counts as showing a consumer; which kinds of surface cross the repository's boundary; what is done about a consumer that is found; how and where the question is put and the change is reported; the wording and location of the guidance.

## Validation

- Review of a change asks: does each compatibility layer and each added assertion map to a consumer that can be shown, other than itself?
- Review of a change to a boundary-crossing surface whose consumers could not be verified asks: was the person directing the work asked, and was a repository-internal change of the same kind reported?
- Review of an edit to the guidance in this area checks the direction of drift: an edit that weakens the demand that a consumer be shown, readmits categorical consumers, or changes who is asked in the unverifiable case needs a record replacing this one, not a prose fix.

## Revisit When

- The premise that agents, without this requirement, add protection nobody asked for no longer holds. It was held when the decision was first taken on 2026-09-01; the record of that date names no models checked.

## More Information

Replaces ADR-D-0016 in full. What it decided is carried, except the unverifiable case, which ADR-D-0016 sent to the person for every surface and this record sends only for a surface that crosses the repository's boundary.
