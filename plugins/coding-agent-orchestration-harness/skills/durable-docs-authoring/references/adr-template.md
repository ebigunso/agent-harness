---
status: accepted
adr_type: {design | implementation}
date: YYYY-MM-DD
deciders: []
consulted: []   # durable identities: model or person names, never roles or platforms
informed: []
warrant: ""     # signal letters plus mishandling mode, e.g. "a, b — violate"; signals: (a) cross-boundary contract/authority/evidence-ownership shape; (b) rejected alternative likely to be re-proposed; (c) costly migration/reversal; (d) cross-repository obligation; (e) user ruling setting a durable governance default; (f) premises likely to expire; (g) deliberately bounded scope; modes: violate / wrongly preserve / wrongly extend
supersedes: []        # current relative paths; update when an archive move renames the target file
superseded_by: null   # current relative path; update when an archive move renames the target file
supersession_scope: null   # full | partial; set on both sides of a supersession
# Optional keys, include only when applicable — depends_on: [] (ADRs this decision builds on); implements: [] (ADRs this decision implements); both carry current relative paths
---

# ADR-{D|I}-XXXX: {Decision title}

<!-- Two tracks (design D / implementation I) with per-track numbering are the default; a repository may collapse to a single track. IDs are never reused. -->

## Context and Problem Statement
{What problem, risk, or design pressure makes this decision necessary? Keep this concrete.}

## Decision Drivers
- {driver 1}
- {driver 2}

## Decision
{State the decision directly.}

## Product / Philosophy Relevance
{Optional. Use when the decision protects the project's core philosophy or product intent. Omit or shorten for purely implementation-level ADRs.}

## Implementation Impact
{Optional. Use when the decision affects API shape, storage, tests, migrations, performance, or operational behavior. Omit or shorten for high-level design ADRs.}

## Considered Options
1. {Option A}
2. {Option B — mark the rejected option likely to be re-proposed, and state the evidence or condition that would reopen it.}

## Decision Outcome
Chosen option: **{Option X}**. {Explain why this option best satisfies the decision drivers.}

## Consequences
- Positive: {positive consequence}
- Negative / tradeoffs: {tradeoff}

## Decision Boundary
{Optional. Separate the invariant (changing it requires a superseding ADR) from calibrated defaults that may change through measured configuration or a plan record. Also the home for a deliberately bounded scope and its rationale — the guard against wrongly extending the decision.}

## Measurement Basis
{Optional. For empirically grounded decisions: the corpus, configuration, and provenance behind the numbers; scope limits; a reproducibility pointer. Evidence alone does not warrant an ADR.}

## Validation
{How will implementation or review prove this decision is being followed? Examples: schema checks, compile-time types, integration tests, migration tests, documentation review.}

## Revisit When
{State the premise whose expiry reopens the decision — this section is what makes legitimate reversal safe instead of wrongly preserving the decision.}

## Consultation impact
{Optional, one line: question asked, ruling adopted or rejected, unresolved dissent.}

## More Information
{Optional links to related ADRs, issues, experiments, or evidence.}
