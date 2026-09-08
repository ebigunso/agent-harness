### Gate 4: Explicit Interface Contracts

**Expectation**
- Boundaries between components are explicit, minimal, and stable.
- Inputs, outputs, and failure semantics are intentionally modeled.

**Evidence expectations**
- Plan states contract-impact scope (none/additive/breaking).
- Review verifies contract updates are synchronized across producers/consumers.
- Failure modes are explicit and not silently swallowed.

**Anti-patterns**
- Implicit contracts communicated only by call-site assumptions.
- Breaking contract changes shipped without migration or compatibility notes.
- Returning ambiguous success/failure signals.
