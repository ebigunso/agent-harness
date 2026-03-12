# Parallel Research Splits (Patterns)

Parallel Researcher calls are appropriate when:
- the area is unfamiliar
- changes are cross-cutting
- validation/CI mapping is unclear
- UI behavior needs baseline confirmation
- performance/security risk needs a dedicated pass

## Recommended split patterns

### Pattern A: Code map + Validation map (most common)
- Researcher A objective: "Code map"
  - identify relevant files, symbols, conventions, similar implementations
  - propose Task_X candidates and owns boundaries
- Researcher B objective: "Validation map"
  - identify relevant tests, local commands, CI workflows by touched paths
  - propose validation items (kind/required/owner/detail) for the plan

### Pattern B: Add UI baseline (UI or UX-critical work)
- Researcher C objective: "UI baseline via browser exploration"
  - use the selected browser automation provider to confirm current behavior and identify stable interaction refs
  - propose E2E/visual spec fields (flows, viewports, evidence screenshots)
  - save evidence screenshots under the provider-defined artifact root

### Pattern C: Risk / edge-case pass (risky changes)
- Researcher D objective: "Risk pass"
  - enumerate edge cases, data correctness risks, security/perf concerns
  - propose mitigations and plan validation adjustments

## Reducing duplication across parallel Researcher calls

When running multiple Researcher calls:
- Tell each Researcher explicitly which outputs matter most.
Examples:
- "Focus on Validation / CI Notes + validation items; skip broad code mapping."
- "Focus on UI baseline and E2E spec; keep plan-fill tasks limited to the review/e2e task."

The Orchestrator should merge:
- Code map + validation map + UI baseline into one plan with explicit validation ownership.
