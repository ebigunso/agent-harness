# Rust Implementation and Review Baselines

Use this reference for repository-agnostic Rust quality checks during implementation and code review.

## Scope and applicability

Apply this guide to:
- New Rust features and bug fixes
- Refactors that should preserve behavior
- Review pass/fail decisions for correctness and maintainability

Out of scope:
- Repository-specific command requirements and CI policy

## Core quality gates

- Model domain concepts with newtypes and enums instead of loosely typed primitives.
- Prefer exhaustive `match` on enums for state transitions.
- Keep invalid states unrepresentable in type definitions.
- Use trait bounds to express capabilities, not speculative abstractions.
- Return `Result<T, E>` from fallible boundaries; reserve panics for unrecoverable invariants.
- Use structured error types and translate boundary errors into domain-meaningful categories.
- Minimize cloning; prefer borrowing when ownership transfer is unnecessary.
- Keep pure/domain logic separated from I/O boundaries to support deterministic testing.

## Safety/failure boundaries

- Treat deserialization, transport, and persistence boundaries as untrusted input points.
- Avoid hidden panics in production paths (`unwrap`/`expect`) unless guarding hard invariants.
- Ensure error propagation preserves cause and caller-actionable meaning.
- Keep interior mutability and shared-state synchronization scoped and explicit.
- Avoid unchecked casts and untyped payload flow in core business logic.

## Validation expectations (conceptual)

- Validate that type modeling prevents invalid states and reduces runtime ambiguity.
- Validate that failures are explicit, categorized, and translated at subsystem boundaries.
- Validate that ownership and mutability decisions avoid unnecessary cloning and contention.
- Validate behavior through deterministic tests at the right level (unit for domain logic, targeted integration for boundary contracts).
- Capture evidence as reviewer notes and test outcomes; use repository-local validation docs for canonical command requirements.

## Review prompts

- Are key domain fields represented by concrete types rather than primitive catch-alls?
- Do `Option<T>` and `Result<T, E>` represent real optionality/fallibility instead of modeling gaps?
- Are error variants meaningful to callers and mapped appropriately at boundaries?
- Are clones, locks, and mutable borrows intentional and narrowly scoped?
- Can critical behavior be validated deterministically without coupling tests to unstable details?

## Common anti-patterns

- Primitive obsession across module boundaries (`String` IDs, raw timestamps, magic numbers).
- Broad untyped value usage in core logic where typed structs should exist.
- `as` casts that can truncate or reinterpret values without checks.
- Non-exhaustive state logic implemented with ad-hoc `if` chains.
- Widespread `unwrap()`/`expect()` in non-test production paths.
- Clone-heavy code used to bypass ownership design issues.
- Business logic embedded in transport handlers with hardcoded I/O.
