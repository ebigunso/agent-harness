### Gate 5: Data and State Integrity

**Expectation**
- Data ownership, lifecycle, and state transitions are consistent and enforceable.
- Invariants are protected at authoritative boundaries.
- For classification or attribution features, derive the full truth table before selecting the data model.

**Evidence expectations**
- Plan identifies impacted invariants and lifecycle transitions.
- Review verifies invariant checks remain at reliable enforcement points.
- Concurrent or repeated execution behavior is considered where relevant.

**Anti-patterns**
- Invariants enforced only in optional caller paths.
- Conflicting write paths without ownership clarity.
- State transitions that allow invalid intermediate states.
