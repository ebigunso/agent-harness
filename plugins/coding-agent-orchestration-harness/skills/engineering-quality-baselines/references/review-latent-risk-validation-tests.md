# Latent-Risk Review: Validation Boundaries and Risk-Based Tests

Read when invalid values may be constructible, validation is delayed until use, or the change has fallback/merge/lifecycle/corrupt-data/duplicate/race behavior that needs targeted regression coverage.

## Checks

1. Validation boundary correctness
- Check whether invalid values can be constructed at all.
- Prefer validation at boundaries where domain/config objects are created.
- Do not rely only on validation at distant use sites when invalid state can leak elsewhere.

2. Test coverage of risk, not lines
For each risky behavior, require a regression test that would fail for the exact class of bug discussed.

Common risk tests:
- persistence across reopen/reload
- fallback path
- duplicate merge
- corrupt data
- lifecycle edge
- disabled tracing
- no production caller
- production-reachable behavior, not only direct helper calls
- stale cache
- retry after partial failure
- fake vs production parity

3. Flag tests that assert developer-convenience surfaces (log text, error prose, incidental formatting, uncontracted mock interactions) outside a stated contract; see `test-authoring.md`.

4. Enforcement-claim negative evidence
Every claim of "strict", "fail-closed", "exhaustive", or "validated" behavior needs proof it rejects:
- rejection tests at every nesting level the claim covers, including absent-field cases
- comparisons against an independent source, not the code under test's own output
- exhaustiveness enforced by the compiler or generated from the authoritative list, never hand-maintained
- paired surfaces (fake/production, client/server, batch/single) proven to reject the same inputs

## Output

For each serious issue, name the missing regression test shape.
