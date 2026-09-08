# Key errata

- 2026-09-08, `cp-9-c2` (clean decoy): the diff uses `SourceUnavailable` without importing it; reviewers in all six graded cells (both models, all arms) blocked on the missing import. Authoring error, decoy invalidated. Effect: cp-9 FP rates are inflated equally across arms (Fable A 1.12, B 0.75, C 0.75; Astra 0.00, 0.00, 0.12 including this decoy); cp-9 verdict (DELETE on dB = 0) unchanged. No regrade needed because detection is unaffected and the decoy is excluded from any adoption guard.
