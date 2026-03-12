# Backend/Frontend Cross-Language Concerns

## Contents

- [How to Apply](#how-to-apply)
- [1) Contract and Compatibility](#1-contract-and-compatibility)
- [2) Data Semantics and Normalization](#2-data-semantics-and-normalization)
- [3) Validation and Trust Boundaries](#3-validation-and-trust-boundaries)
- [4) State, Concurrency, and Idempotency](#4-state-concurrency-and-idempotency)
- [5) Performance and Resilience](#5-performance-and-resilience)
- [6) Security and Privacy Across Layers](#6-security-and-privacy-across-layers)
- [7) Observability and Debuggability](#7-observability-and-debuggability)
- [8) Delivery and Change Safety](#8-delivery-and-change-safety)
- [Review Checklist (Implementation + Review)](#review-checklist-implementation--review)
- [Scope Boundary](#scope-boundary)

Use this guide for implementation and review when changes span backend/frontend boundaries, regardless of specific languages or frameworks.

## How to Apply

- **Implementation usage**: before coding, identify the contract, data shape, failure modes, and observability expectations shared across backend/frontend.
- **Review usage**: verify each section below with evidence from code, tests, logs, and API/UI behavior rather than intent statements.

## 1) Contract and Compatibility

### Concerns

- Keep API contracts explicit, versioned when needed, and stable for existing clients.
- Treat schema, enum, and nullability changes as compatibility risks unless proven safe.
- Ensure error models are structured and machine-actionable (code + category + user-safe message).
- Define ownership for contract updates (producer and consumer both updated or protected by compatibility strategy).

### Anti-Patterns

- Silent contract drift (response shape changed without consumer updates).
- Ambiguous error payloads requiring brittle string parsing.
- Implicit defaults that differ across clients or environments.

## 2) Data Semantics and Normalization

### Concerns

- Align domain semantics across layers (time units, time zones, precision, currency, IDs, status lifecycles).
- Normalize at clear boundaries to avoid double conversion.
- Preserve server authority for canonical state while allowing client-local presentation transforms.
- Make unknown/optional fields explicit and safe.

### Anti-Patterns

- Mixed units (seconds vs milliseconds) without explicit typing or naming.
- Time/date interpretation split between backend/frontend with inconsistent assumptions.
- Frontend re-deriving business truth that should come from backend invariants.

## 3) Validation and Trust Boundaries

### Concerns

- Validate all externally supplied input at backend boundaries.
- Keep frontend validation for UX speed and clarity, not as sole enforcement.
- Centralize business invariants in backend domain logic.
- Return validation failures in a structured format that maps to UI field/global states.

### Anti-Patterns

- Trusting client constraints as authoritative security/business controls.
- Duplicating complex validation logic independently in multiple layers with drift.
- Returning opaque validation failures that block precise UI remediation.

## 4) State, Concurrency, and Idempotency

### Concerns

- Design mutating operations for retry safety where practical (idempotency keys, conflict detection, or safe replay semantics).
- Represent state transitions explicitly and reject illegal transitions deterministically.
- Define conflict behavior for concurrent edits (last-write-wins, optimistic locking, merge strategy).
- Make race-prone flows observable with clear correlation IDs and audit signals.

### Anti-Patterns

- Hidden side effects triggered by repeated requests.
- Non-deterministic conflict outcomes across identical inputs.
- UI assumptions of immediate consistency without loading/error reconciliation paths.

## 5) Performance and Resilience

### Concerns

- Set and enforce timeouts, retry policy, and backoff per dependency type.
- Bound payload size and query complexity to protect service and client performance.
- Use pagination/streaming patterns for large collections.
- Expose fallback behavior when dependencies degrade.

### Anti-Patterns

- Unbounded list endpoints consumed directly by UI views.
- Retry storms from naive frontend and backend retry stacking.
- Coupling critical UX paths to fragile, high-latency downstream calls without graceful degradation.

## 6) Security and Privacy Across Layers

### Concerns

- Enforce authentication/authorization server-side for every protected action.
- Minimize sensitive data exposure in payloads, logs, and client storage.
- Protect state-changing actions with appropriate anti-forgery/session controls.
- Ensure security-relevant events are auditable and attributable.

### Anti-Patterns

- Authorization implied by hidden UI controls instead of server checks.
- Sensitive fields returned "for convenience" without strict necessity.
- Logging secrets, tokens, or personal data in plaintext.

## 7) Observability and Debuggability

### Concerns

- Use correlation/request IDs that can be traced backend to frontend.
- Keep error taxonomy stable enough for alerting and dashboarding.
- Include actionable diagnostics for operators while preserving user safety.
- Ensure telemetry covers both success and failure paths for critical flows.

### Anti-Patterns

- UI-only or backend-only logging with no cross-layer join key.
- High-volume low-signal logs that obscure incident diagnosis.
- Error categories changing frequently and breaking operational baselines.

## 8) Delivery and Change Safety

### Concerns

- Prefer additive contract evolution before removals.
- Use staged rollout or compatibility windows for breaking-risk changes.
- Pair contract changes with consumer updates and validation evidence.
- Document migration expectations when behavior changes are unavoidable.

### Anti-Patterns

- Big-bang contract replacement without compatibility plan.
- Removing fields/endpoints before consumer adoption is confirmed.
- Shipping backend/frontend changes independently when coupling is mandatory.

## Review Checklist (Implementation + Review)

Use this checklist as a minimum evidence bar:

- Contract changes are explicit, compatibility risk classified, and consumer impact addressed.
- Validation/invariants are enforced at trust boundaries, with UI mapping for failures.
- Concurrency/idempotency behavior is documented and tested for mutating flows.
- Security/privacy controls are server-authoritative and data exposure is minimized.
- Observability allows end-to-end traceability and actionable incident response.
- Performance constraints and fallback behavior are defined for critical paths.

## Scope Boundary

- This document is stack-neutral and repository-agnostic by design.
- Repository-local rules define canonical required commands, CI gates, and policy precedence.
