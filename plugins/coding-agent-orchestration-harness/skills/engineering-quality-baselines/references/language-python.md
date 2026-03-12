# Python Implementation and Review Baselines

Use this reference for repository-agnostic Python quality checks during implementation and code review.

## Scope and applicability

Apply this guide to:
- New Python features and bug fixes
- Refactors that should preserve behavior
- Review pass/fail decisions for correctness, readability, and maintainability

Out of scope:
- Repository-specific command execution policy and CI mapping

## Core quality gates

- Type annotate public function and method signatures.
- Keep type hints specific and intention-revealing.
- Use typed domain models (`dataclass`, `TypedDict`, or protocol-driven interfaces) instead of unstructured dictionaries for core data flow.
- Keep exception boundaries explicit and translate library exceptions at module edges.
- Organize packages by cohesive responsibility and enforce directional dependencies.
- Keep tests deterministic by isolating time, randomness, filesystem, network, and environment effects.

## Safety/failure boundaries

- Treat external input and adapter boundaries as untrusted until validated and normalized.
- Keep `try` scopes narrow and handle only expected failure modes.
- Preserve causal context when re-raising exceptions (`raise ... from err`).
- Avoid import-time side effects and hidden process-global mutation.
- Prevent flaky tests by eliminating wall-clock timing dependencies and shared mutable state.

## Validation expectations (conceptual)

- Validate that public APIs and critical boundaries are explicitly typed.
- Validate that exception translation preserves meaningful domain semantics.
- Validate that module/package structure supports testability and replacement.
- Validate that tests are order-independent, deterministic, and focused on contract behavior.
- Capture evidence in type-check outcomes, targeted test outcomes, and review notes; defer to repository-local docs for canonical command requirements.

## Review prompts

- Are module boundaries and public APIs fully annotated with intent-revealing types?
- Are wide types (`Any`, broad unions, loose dictionaries) minimized and justified?
- Are low-level exceptions translated before crossing business boundaries?
- Is package/module structure cohesive and free from avoidable dependency cycles?
- Can tests run independently and in parallel without hidden shared state?

## Common anti-patterns

- Adding `Any` only to silence type checker findings instead of improving type models.
- Passing loosely typed dictionaries across multiple layers without stable contracts.
- Using broad exception handlers in mid-layer business logic.
- Re-raising exceptions without preserving original cause.
- Import-time network/file/database actions and process-global side effects.
- Reusing mutable global fixtures or wall-clock sleeps in tests.

## Document-level review quick checks

- Guidance is repository-agnostic and avoids project-specific tools or paths.
- Each section includes implementation guidance, review prompts, anti-patterns, and concrete usage intent.
- Recommendations prioritize clarity, correctness, and maintainability over framework-specific preferences.
