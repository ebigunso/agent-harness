# Latent-Risk Review: Entrypoints and Admission

Read when the same domain action enters through multiple APIs, or candidate data is filtered, admitted, rejected, hydrated, recorded, cached, counted, emitted, or enqueued.

## Checks

1. Entrypoint parity
- Identify all entrypoints for the same domain action.
- Check whether authorization, validation, defaults, idempotency, side effects, telemetry, and error behavior match intentionally.

2. Candidate vs accepted sets
- Distinguish discovered candidates from admitted records.
- Verify that rejected candidates are not counted, cached, emitted, enqueued, or persisted as accepted state.

3. Side effects after selection
- Check that hydration, persistence, metrics, event emission, notifications, and downstream jobs happen only after the intended admission decision.
- Flag inferred intent when explicit user or caller intent is available but ignored.

## Output

Report mismatches between entrypoints or side effects that happen before admission is proven.
