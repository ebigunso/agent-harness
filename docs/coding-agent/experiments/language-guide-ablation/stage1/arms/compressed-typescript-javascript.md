# TypeScript/JavaScript review checklist (compressed)

- No `any` or bare `as` casts at boundaries; model the real type.
- Untrusted payloads (HTTP, webhook, queue, env) runtime-validated at first entry — a TS cast is not validation.
- Validate before side effects; fail closed.
- Every critical promise is awaited or explicitly supervised; no fire-and-forget.
- No catch blocks that swallow errors without logging/observability.
- Discriminated unions over all-optional object shapes for multi-state results.
- Contracts derived from one executable source (schema package); no hand-copied duplicates.
- Transport (`req`/`res`, headers, status) stays out of domain services.
