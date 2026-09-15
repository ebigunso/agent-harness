# Model Routing (Multi-Model Delegation)

Use this reference when more than one model is available for delegation. Route each role by the strength the model behind it has demonstrated on that kind of work, not by the name of its platform.

## Strengths routed on

- Writing: altitude and lateral design judgment, and general prose — framing tradeoffs, spotting cross-cutting design risk, producing clear text.
- Detail scrutiny: forensic inventories and mechanical-precision work — exhaustive census passes, spec-conformance checking, line-level correctness.
- Long-context reading: holding a large corpus (many files, long transcripts, whole record sets) in one pass without losing what an early part said.

A model shows a strength through its results on this kind of work in this workspace; that observation is the routing key. A model that has shown a strength is called a writing-strength, detail-strength, or long-context model below.

Illustration, dated 2026-09-15: in this workspace the Claude models have shown the writing strength and the Codex models the detail-scrutiny strength. No illustration is recorded for long-context reading; route on it only after observing it. Re-observe when a model changes and replace this illustration with a newly dated one.

## Routing by work type

Give each role to the model that has shown the strength the work needs:

- Forensic research (inventories, audits, evidence census): detail-strength.
- Exploratory or design research (option framing, architecture surveys): writing-strength.
- Research over a large corpus (whole-repo reads, long transcripts): a long-context model, chosen among those showing the strength the research type above needs.
- Review, correctness tier (line-level defects, spec conformance, validation evidence): detail-strength.
- Review, design tier (boundaries, contracts, proportionality, long-horizon cost): writing-strength.
- Implementation: either — prefer detail-strength when acceptance is mechanical precision, writing-strength when acceptance is judgment or prose.
- Decision records (ADRs, plan decisions, design rulings): authored by the coordinating, writing-strength side — never dispatched to implementation workers.

## Prose quality

- User-facing prose (records, lessons, skill text, PR bodies) authored by a detail-strength model receives a rewording pass by a writing-strength model before finalizing, without semantic change.
- Machine-consumed or contract text (YAML reports, fixtures, scripts) authored by a detail-strength model receives that pass only when its prose needs it — a summary, message, or comment that misleads or reads poorly; otherwise it finalizes as authored.

## Tiers and fallback

- Keep the tiers (correctness vs design review, forensic vs design research) as separate dispatches when the tiers differ in the strengths the task needs. When they call on the same strength, one dispatch may cover both, with the packet naming each tier's acceptance.
- When only one model is available, it covers every role; the tier rule above still decides whether the tiers are dispatched separately.
