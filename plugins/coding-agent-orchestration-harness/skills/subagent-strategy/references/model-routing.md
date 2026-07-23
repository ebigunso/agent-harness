# Model Routing (Multi-Platform Delegation)

Use this reference when more than one model platform is available for delegation. Route by capability class, not platform name; Claude (writing-strength) and Codex (detail-strength) are the current examples of each class.

## Capability classes

- Detail-strength: detail scrutiny, forensic inventories, and mechanical-precision work — exhaustive census passes, spec-conformance checking, line-level correctness.
- Writing-strength: altitude and lateral design judgment, and general writing — framing tradeoffs, spotting cross-cutting design risk, producing clear prose.

## Routing by work type

- Forensic research (inventories, audits, evidence census): detail-strength.
- Exploratory or design research (option framing, architecture surveys): writing-strength.
- Review, correctness tier (line-level defects, spec conformance, validation evidence): detail-strength.
- Review, design tier (boundaries, contracts, proportionality, long-horizon cost): writing-strength.
- Implementation: either class — prefer detail-strength when acceptance is mechanical precision, writing-strength when acceptance is judgment or prose.
- Decision records (ADRs, plan decisions, design rulings): authored by the coordinating, writing-strength side — never dispatched to implementation workers.

## Prose quality

- Text authored by a detail-strength model receives a rewording pass by a writing-strength model before finalizing, without semantic change.

## One-platform fallback

- When only one platform exists, either class covers both roles.
- Keep the tier distinctions (correctness vs design review, forensic vs design research) as separate dispatches even on one platform.
