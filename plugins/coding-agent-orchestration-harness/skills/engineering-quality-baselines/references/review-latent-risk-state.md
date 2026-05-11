# Latent-Risk Review: State, Invariants, Authority, and Merge Semantics

Read when the change touches persisted state, lifecycle state, counters, indexes, cache, derived data, denormalized data, IDs, ordering, merge, update, or upsert behavior.

## Checks

1. Invariant preservation
- Identify what must always remain true after this change.
- Check write paths, update paths, fallback paths, repair paths, and merge paths.
- Look for counter/source mismatch, cache/authority drift, unstable IDs, nondeterministic ordering, loosened lifecycle/state, or bypassable security checks.

2. Authority vs derived data
- Classify each relevant value as authoritative, derived, cached, denormalized, materialized, summarized, or diagnostic.
- Verify how duplicated values are updated, invalidated, repaired, and observed when updates fail.

3. Monotonicity and merge semantics
- For every merge/upsert/update, decide whether each field should overwrite, min, max, union, intersect, append, dedupe, or conservatively combine.
- Flag implicit overwrite when the semantics are unclear.
- Check for timestamps regressing, permissions broadening, lifecycle becoming less restrictive, versions decreasing, or retries overwriting better data with worse data.

## Output

Report only findings with changed-path evidence.
