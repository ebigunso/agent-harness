# TypeScript/JavaScript Baselines

Use this reference when implementing or reviewing TypeScript/JavaScript changes after loading core principles and architecture gates.

## Scope and applicability

Apply this guide to:
- TypeScript and JavaScript feature delivery, bug fixes, and behavior-preserving refactors
- Review decisions around correctness, maintainability, and contract safety

Out of scope:
- Repository-specific command policy and CI gate ownership

## Core quality gates

- Define explicit input/output types at boundary modules.
- Model domain constraints with narrow types and discriminated unions instead of broad optional object shapes.
- Keep `any` and unchecked `unknown` out of boundary interfaces.
- Validate untrusted runtime inputs at first entry and map validated data into domain types.
- Standardize async error taxonomy and map each class to stable caller-facing behavior.
- Keep API contracts versioned and executable (schema-driven or strongly typed) to prevent drift.

## Safety/failure boundaries

- Treat external payloads (HTTP, queue, file, environment, third-party responses) as untrusted until validated.
- Fail closed on invalid shape/value combinations before side effects occur.
- Avoid hidden async failures by assigning ownership for promise lifecycle, cancellation, and retry behavior.
- Prevent transport concerns from leaking into domain services.
- Use compatibility-safe API evolution by default and explicitly manage breaking changes.

## Validation expectations (conceptual)

- Validate boundary contract strictness and trust-zone transitions.
- Validate that runtime schema checks run before business execution for untrusted inputs.
- Validate that async failure handling is observable, categorized, and deterministic under timeout/retry conditions.
- Validate API contract alignment across providers and consumers with executable checks.
- Capture evidence as focused tests and review notes; rely on repository-local validation docs for canonical required commands.

## Review prompts

- Does each external boundary narrow untrusted input before domain use?
- Are domain contracts encoded in types rather than implied by conventions or comments?
- Are async paths explicit about timeout, cancellation, retries, and fallback behavior?
- Are error classes and mapping rules stable and caller-actionable?
- Is contract drift actively prevented through versioned schemas or contract tests?

## Common anti-patterns

- Trusting inferred payload types from external systems without runtime narrowing.
- Using `any` or permissive passthrough objects across trust boundaries.
- Parsing/validation deep inside business logic after side effects begin.
- Catch-all async error handling that swallows failures or continues with partial state.
- Fire-and-forget critical promises without supervision or failure reporting.
- Manual copy-paste contract definitions that drift between producers and consumers.
