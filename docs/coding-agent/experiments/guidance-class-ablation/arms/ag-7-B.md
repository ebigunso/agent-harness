### Gate 7: Observability of Architectural Behavior

**Expectation**
- Meaningful signals exist to understand critical behavior and failures at boundaries.
- Observability supports diagnosis without exposing sensitive internals.

**Evidence expectations**
- Plan identifies what success/failure signals are needed for changed flows.
- Review confirms key boundary events and failures are inspectable.
- Sensitive data exposure risk in logs/telemetry is assessed.

**Anti-patterns**
- Silent failure paths with no diagnosable signal.
- Overly noisy instrumentation that hides actionable indicators.
- Logging sensitive payloads as a convenience.
