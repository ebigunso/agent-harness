# Go Best Practices (Repository-Agnostic)

Use this reference when implementing or reviewing Go code. Apply these checks with repository-local rules for required commands and validation gates.

## Scope and applicability

Apply this guide to:
- Go feature work, bug fixes, and behavior-preserving refactors
- Review decisions around correctness, maintainability, and operational reliability

Out of scope:
- Repository-specific required commands and CI ownership

## Core quality gates

- Define interfaces at consumer boundaries and keep them minimal and capability-focused.
- Treat errors as values, wrap with context (`%w`), and classify with `errors.Is`/`errors.As`.
- Use goroutines only where concurrency adds clear value, and provide explicit lifecycle ownership.
- Pass `context.Context` through cancellable work and enforce timeout/deadline expectations.
- Keep package APIs small, cohesive, and dependency direction acyclic.
- Keep transport/storage concerns separated from core domain behavior.

## Safety/failure boundaries

- Treat network/storage/IPC boundaries as failure-amplifying points requiring explicit error translation.
- Ensure every goroutine has a guaranteed termination path.
- Protect shared mutable state with a single, consistent coordination model.
- Keep channel close/send ownership explicit and single-owner where possible.
- Sanitize user-facing failures while preserving actionable internal diagnostics.

## Validation expectations (conceptual)

- Validate interface necessity and size against actual consumer substitution needs.
- Validate error identity and wrapping behavior across boundary hops.
- Validate concurrency paths for cancellation compliance, leak risk, and synchronization correctness.
- Validate package boundaries for cohesion, export discipline, and dependency direction.
- Capture evidence in focused tests and review notes; use repository-local docs for canonical command-level validation requirements.

## Review prompts

- Does each interface represent a stable capability rather than a provider detail?
- Do error paths preserve causal context and support `errors.Is`/`errors.As` classification?
- Can every goroutine terminate under success, failure, and cancellation scenarios?
- Is shared state protected consistently, with clear ownership for channel lifecycle?
- Are package exports minimal and aligned to cohesive responsibilities?

## Common anti-patterns

- Creating interfaces for every struct by default.
- Dropping original error causes or matching on `err.Error()` strings.
- Using panic/recover as routine error control flow.
- Launching unbounded goroutines without backpressure or cancellation.
- Unsynchronized shared map/slice access across goroutines.
- Dumping unrelated behavior into broad utility packages or package-level globals.
