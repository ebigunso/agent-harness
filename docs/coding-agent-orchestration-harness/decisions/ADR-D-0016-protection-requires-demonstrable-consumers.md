---
status: accepted
adr_type: design
date: 2026-09-01
deciders: ["ebigunso"]
consulted: ["Claude Fable 5"]
informed: []
warrant:
  warranted_by: "without this record, future edits to harness guidance would likely soften the evidence requirement for protective artifacts back toward industry defaults, reading the strict formulation as an oversight to fix rather than a decision to keep"
  detected_signals: "a decider's ruling setting a durable governance default; rejected alternatives likely to be re-proposed (both the softer industry-default wording and the stronger per-report enforcement)"
  cost_of_violation: "protective artifacts re-accumulate without owners — compatibility surfaces nobody consumes and assertions nobody depends on — each individually defensible, collectively freezing designs against change; the erosion arrives as one justified-looking edit at a time and is invisible in any single diff"
  cost_of_over_extension: "read as a license to strip protection wherever evidence is not already in hand, the decision would silently break surfaces whose consumers are real but unverifiable; the routing clause exists precisely to prevent that reading"
supersedes: []
superseded_by: null
supersession_scope: null
---

# ADR-D-0016: Protection requires demonstrable consumers

## Context and Problem Statement

Agents default to two protective behaviors nobody asked for: preserving existing interfaces via compatibility layers, and pinning behavior with test assertions beyond what the change requires. Both create artifacts that constrain future work — a surface that must keep working, an assertion that must keep passing — while the thing they protect may not exist. Left ungoverned, the harness rewards these defaults, because "more compatibility" and "more tests" each read as diligence.

## Decision Drivers

- A protective artifact is a standing obligation on all future work; obligations without beneficiaries are pure cost.
- Industry framing ("compatibility is first-class", coverage-maximizing testing) is the attractor state any unguarded wording drifts back to.
- Weak formulations of a consumer requirement are gameable and therefore no requirement at all.

## Decision

Protection — a compatibility layer or a test assertion — must be justified by evidence of a demonstrable consumer or contract: something that exists and can be shown, not merely conceived of. Two constraints make the requirement non-gameable: the justification may not be self-referential (an artifact never counts as its own consumer — a test is not justified by the suite it lives in, a shim not by its own documentation), and hypothetical or categorical consumers ("downstream users might") are not evidence. When consumer existence genuinely cannot be verified, the question routes to the user; neither preserving nor breaking is a permitted silent default.

## Considered Options

1. Industry default: treat compatibility preservation and added test assertions as inherently virtuous.
2. Soft requirement: ask for a "named" consumer without evidentiary or self-reference constraints.
3. Evidence requirement with user routing for the unverifiable case (chosen).
4. Enforcement via per-test justification fields in the Worker report contract.

## Decision Outcome

Chosen option: **Option 3**. It is the weakest formulation that survives adversarial compliance: option 2 collapses into option 1, because an agent can always name a categorical consumer or let the artifact vouch for itself, and a requirement satisfiable by restating the default enforces nothing.

### Rejected Alternatives

Option 1 is the failure mode itself, not a candidate — and any future edit softening this decision's guidance back toward it is a reversal of this decision, not a cleanup, however reasonable the wording change looks locally. Option 2 is rejected as gameable per above. Option 4 (structured per-test justification in the Worker report contract) is deliberately held back, not rejected outright: it is the strongest forcing function but adds ceremony to a load-bearing schema. Adopt it only if the guidance-and-review approach demonstrably fails to hold the line.

## Validation

Review of guidance edits in this area checks direction of drift: a change that weakens the evidence requirement, readmits categorical consumers, or removes the user-routing clause requires a superseding ADR, not a prose fix.

## Revisit When

- Agents' default behavior no longer over-produces unrequested protection, making the guard redundant.
- Evidence accumulates that guidance plus review cannot prevent the drift — the condition for adopting the held-back report-contract enforcement.

## More Information

Non-authoritative side note: as of this writing the intent is implemented in the engineering-quality-baselines and plan-format skill prose; the implementation may be reworded or relocated freely so long as the intent above is preserved.
