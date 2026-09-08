### 5) Define and Protect Invariants

- Make assumptions explicit at module boundaries.
- Validate inputs at trust boundaries and normalize internal state early.
- Fail early with actionable errors when invariants are violated.

Review checks:
- Which invariants are introduced or relied upon?
- Are boundary checks and failure modes explicit?
