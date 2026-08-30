# Stage 0 — Regeneration Probe

## Protocol

Clean session. No harness skill loaded, no repo context, no prior turns. One probe per
session — do not batch languages into one conversation, or earlier answers will prime later
ones.

Run **3 samples per language** (12 sessions). Record verbatim output in `results.yaml`.

## Probe prompt (substitute `<LANGUAGE>`)

> List the quality gates, safety and failure boundaries, and common anti-patterns you would
> check when reviewing a non-trivial <LANGUAGE> change. Be specific and concise — bullets, no
> prose. Assume the reviewer is competent and does not need the basics explained.

Use exactly this wording for every sample. Do not mention the harness, the guide, or that an
evaluation is running.

## Scoring

For each key bullet below, mark the sample:

- `hit` — the sample states the same check, in any wording
- `partial` — the sample gestures at the area but misses the specific check
- `miss` — absent

Coverage = `(hits + 0.5 * partials) / total_bullets`, averaged across the 3 samples.

Score against the key mechanically. Do not credit a bullet because the model "would probably
have said it" — that is the exact bias this stage exists to avoid.

## Key bullets

Extracted verbatim-in-substance from each guide's Core quality gates / Safety boundaries /
Common anti-patterns sections.

### go (source: language-go.md)

- G1  interfaces defined at consumer boundaries, minimal and capability-focused
- G2  errors as values, wrapped with `%w`, classified via `errors.Is` / `errors.As`
- G3  goroutines only where concurrency adds value, explicit lifecycle ownership
- G4  `context.Context` threaded through cancellable work, timeouts/deadlines enforced
- G5  package APIs small and cohesive, dependency direction acyclic
- G6  transport/storage concerns separated from core domain behavior
- G7  every goroutine has a guaranteed termination path
- G8  shared mutable state protected by a single consistent coordination model
- G9  channel close/send ownership explicit and single-owner
- G10 user-facing failures sanitized, internal diagnostics preserved
- G11 anti-pattern: interface for every struct by default
- G12 anti-pattern: matching on `err.Error()` strings / dropping causes
- G13 anti-pattern: panic/recover as routine control flow
- G14 anti-pattern: unbounded goroutines without backpressure
- G15 anti-pattern: unsynchronized shared map/slice across goroutines
- G16 anti-pattern: broad utility packages / package-level globals

### python (source: language-python.md)

- P1  public function and method signatures type-annotated
- P2  type hints specific and intention-revealing
- P3  typed domain models (dataclass/TypedDict/protocol) over unstructured dicts
- P4  exception boundaries explicit, library exceptions translated at module edges
- P5  packages organized by cohesive responsibility, directional dependencies
- P6  tests deterministic — time, randomness, fs, network, env isolated
- P7  external input treated as untrusted until validated and normalized
- P8  narrow `try` scopes handling only expected failure modes
- P9  causal context preserved on re-raise (`raise ... from err`)
- P10 no import-time side effects or hidden process-global mutation
- P11 anti-pattern: `Any` added to silence the type checker
- P12 anti-pattern: loose dicts passed across layers without stable contracts
- P13 anti-pattern: broad exception handlers in mid-layer business logic
- P14 anti-pattern: mutable global fixtures or wall-clock sleeps in tests

### rust (source: language-rust.md)

- R1  domain modeled with newtypes and enums over loose primitives
- R2  exhaustive `match` on enums for state transitions
- R3  invalid states unrepresentable in the type definitions
- R4  trait bounds express real capabilities, not speculative abstraction
- R5  `Result<T, E>` at fallible boundaries; panic only for unrecoverable invariants
- R6  structured error types, boundary errors translated to domain categories
- R7  cloning minimized, borrowing preferred where ownership transfer is unnecessary
- R8  pure/domain logic separated from I/O for deterministic testing
- R9  deserialization/transport/persistence treated as untrusted input points
- R10 no hidden panics (`unwrap`/`expect`) in production paths
- R11 interior mutability and shared-state synchronization scoped and explicit
- R12 anti-pattern: primitive obsession across module boundaries
- R13 anti-pattern: `as` casts that truncate or reinterpret without checks
- R14 anti-pattern: non-exhaustive state logic via ad-hoc `if` chains
- R15 anti-pattern: clone-heavy code bypassing ownership design
- R16 anti-pattern: business logic embedded in transport handlers

### typescript-javascript (source: language-typescript-javascript.md)

- T1  explicit input/output types at boundary modules
- T2  narrow types and discriminated unions over broad optional object shapes
- T3  `any` and unchecked `unknown` kept out of boundary interfaces
- T4  untrusted runtime inputs validated at first entry, mapped into domain types
- T5  standardized async error taxonomy mapped to stable caller-facing behavior
- T6  API contracts versioned and executable (schema-driven or strongly typed)
- T7  external payloads (HTTP/queue/file/env/third-party) untrusted until validated
- T8  fail closed on invalid shapes before side effects occur
- T9  explicit ownership of promise lifecycle, cancellation, retry
- T10 transport concerns kept out of domain services
- T11 anti-pattern: trusting inferred payload types without runtime narrowing
- T12 anti-pattern: validation deep in business logic after side effects begin
- T13 anti-pattern: catch-all async handling that swallows or continues partial
- T14 anti-pattern: fire-and-forget critical promises
- T15 anti-pattern: hand-copied contract definitions that drift
