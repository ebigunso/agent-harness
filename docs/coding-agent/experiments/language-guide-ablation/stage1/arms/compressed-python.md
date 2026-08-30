# Python review checklist (compressed)

- Public signatures fully type-annotated; never widen to `Any` to silence the checker.
- Typed domain models (dataclass/TypedDict/protocol) instead of dicts crossing layers.
- `try` scopes narrow, handling only expected failures; no broad `except Exception` in business logic.
- Preserve cause on re-raise: `raise ... from err`.
- No import-time side effects (config reads, clients, connections) or process-global mutation.
- Tests deterministic: isolate time, randomness, filesystem, network, env; no wall-clock sleeps.
- External input untrusted until validated and normalized at the boundary.
- Library exceptions translated to domain exceptions at module edges.
