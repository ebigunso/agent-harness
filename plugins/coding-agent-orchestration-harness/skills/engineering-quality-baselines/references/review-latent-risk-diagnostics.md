# Latent-Risk Review: Diagnostics and Telemetry

Read when the change emits or modifies errors, health state, metrics, traces, telemetry, validation failures, rejection diagnostics, or debug details.

## Checks

1. Diagnostic fidelity
- Ensure errors and warnings preserve the actionable cause, affected object, operation, and safe remediation detail.
- Avoid collapsing distinct failure modes into one misleading message.

2. Observability parity
- Check that metrics, traces, health state, and logs reflect the actual accepted/rejected/degraded state.
- Verify success, partial success, fallback, retry exhaustion, and rejection paths are visible where operators need them.

3. Safety and stability
- Do not expose secrets, credentials, personal data, or attacker-controlled raw payloads in diagnostics.
- Keep metric labels and telemetry dimensions bounded.

Verify diagnostic metadata points to the actual failing source:
- field name
- column index
- path
- object id
- operation
- backend/store
- scope
- request/user/tenant/config
- candidate vs accepted/rejected status

Watch for loop diagnostics that accidentally use a constant, default, or outer value instead of the current failing item.

## Output

Report diagnostics that mislead operators, hide material failure, leak sensitive data, or create unbounded telemetry.
