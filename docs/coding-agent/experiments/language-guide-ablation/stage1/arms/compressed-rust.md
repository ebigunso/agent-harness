# Rust review checklist (compressed)

- No `unwrap()`/`expect()` on production paths fed by external/config/manifest data; return `Result`.
- No lossy `as` casts; use `try_from` where truncation is possible.
- Exhaustive `match` on enums for state logic — no `if let` chains that lose compiler exhaustiveness.
- Newtypes/enums over primitives (`String` ids, raw amounts) at module boundaries.
- Structured error enums with caller-actionable variants; never flatten to `String`.
- Clones are intentional, not borrowck workarounds.
- Domain rules stay out of transport handlers.
- Deserialization/transport/persistence inputs are untrusted.
