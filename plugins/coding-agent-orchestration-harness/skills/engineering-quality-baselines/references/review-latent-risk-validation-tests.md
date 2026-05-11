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
- stale cache
- retry after partial failure
- fake vs production parity

## Output

For each serious issue, name the missing regression test shape.
