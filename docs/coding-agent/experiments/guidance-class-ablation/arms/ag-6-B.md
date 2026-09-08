### Gate 6: Operational and Failure Containment

**Expectation**
- Failures are contained to the smallest practical scope.
- Timeouts, retries, idempotency, and degradation paths are intentional when integrating external dependencies.

**Evidence expectations**
- Plan lists likely failure modes for touched integrations.
- Review verifies error propagation and fallback behavior are deliberate.
- Risky operations include containment strategy notes.

**Anti-patterns**
- Unbounded retries or blocking operations in critical paths.
- Broad exception/error suppression that obscures root causes.
- Cascading failure paths without isolation boundaries.
