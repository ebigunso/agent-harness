# Latent-Risk Review: Failure Modes and Degradation

Read when the change includes fallible operations, retries, fallback, timeout handling, partial success, stale data, corrupt data, external dependencies, suppressed errors, or degraded behavior.

## Checks

1. Failure mode completeness
- For each fallible operation, check partial success, retry, timeout, unavailable dependency, stale data, corrupt data, and fallback.
- Confirm failures are safely rolled back, visibly degraded, or explicitly recoverable.

2. Observability of degradation
- If the code falls back, skips work, approximates, suppresses an error, or uses stale data, verify this is observable.
- Acceptable observability may include logs, health state, metrics, return values, diagnostics, structured warnings, or surfaced status.

## Output

For each degradation path, state:
- what degraded
- who can observe it
- what recovery or mitigation exists
