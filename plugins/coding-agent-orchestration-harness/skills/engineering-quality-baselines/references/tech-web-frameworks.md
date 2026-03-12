# Web Framework Best Practices (Framework-Level)

## Contents

- [Purpose](#purpose)
- [Scope Boundary: Framework vs Language Concerns](#scope-boundary-framework-vs-language-concerns)
- [How to Use in Planning](#how-to-use-in-planning)
- [How to Use in Review](#how-to-use-in-review)
- [Framework Quality Areas](#framework-quality-areas)
- [Planning/Review Prompts](#planningreview-prompts)
- [Non-Goals](#non-goals)

## Purpose

Use this reference for framework-level implementation and review quality across common web stacks.
It applies to both:
- server-rendered flows (SSR/SSG/hybrid)
- SPA flows integrated with API/back-end services

This document is intentionally technology-focused and repository-agnostic.

## Scope Boundary: Framework vs Language Concerns

### Framework concerns (in scope)

- Routing, nested layouts, and route ownership.
- Data-loading lifecycle (server-side loaders, client fetch orchestration, prefetch/revalidation).
- Render lifecycle (SSR, hydration, client navigation, partial rendering).
- UI state placement (URL state, framework state stores, server state cache).
- Mutation flow semantics (optimistic update, rollback, invalidation, conflict UX).
- Framework middleware/hooks/interceptors for auth, errors, and request context.
- Framework-level code splitting, bundle boundaries, and lazy loading behavior.

### Language concerns (out of scope here)

- Static type-system discipline details.
- Language-specific error/exception idioms.
- Language-specific concurrency primitives and packaging structure.
- Language-level lint/format/build command policies.

Use language references for these concerns; do not duplicate them in framework reviews.

## How to Use in Planning

1. Identify application mode for each touched flow
- SSR-dominant, SPA-dominant, or mixed.
- Mark where the source of truth lives for each state transition.

2. Map boundary ownership
- Route owns composition and guard decisions.
- Loader owns data acquisition orchestration.
- Domain/API boundary owns business invariants.
- UI components own rendering and interaction presentation.

3. Choose rendering and data strategy intentionally
- Define what must render on first response vs after hydration/navigation.
- Define revalidation/invalidation triggers after mutations.
- Define fallback behavior for partial failure states.

4. Pre-register anti-pattern checks
- For each section below, list at least one likely failure mode to verify in review.

## How to Use in Review

For each section below, record:
- Pass / At Risk / Fail
- concrete evidence (code path, behavior trace, test/e2e artifact, or reproducible scenario)
- remediation owner when status is At Risk or Fail

If any relevant required gate/check is explicitly waived, reference the canonical required-check waiver template in [testing-validation.md](testing-validation.md#canonical-required-check-waiver-template) instead of restating waiver policy text.

Do not approve high-risk UX or data-flow changes without explicit evidence for loading, mutation, and error states.

## Framework Quality Areas

### 1) Route and Layout Composition

**Expectations**
- Route boundaries mirror feature boundaries and user navigation intent.
- Shared layout concerns remain in layout-level primitives, not duplicated in leaf routes.
- Route guards are centralized and deterministic.

**Anti-patterns**
- Copying layout logic into many pages/components.
- Guard logic split between unrelated UI components and route hooks.
- Route tree shaped by file convenience instead of feature ownership.

### 2) Data Loading and Revalidation Lifecycle

**Expectations**
- Data loading is colocated with the framework lifecycle that controls rendering.
- Cache/revalidation policy is explicit (stale strategy, trigger points, invalidation scope).
- Server and client data loaders cannot race into contradictory UI states.

**Anti-patterns**
- Duplicate fetching for the same resource in route loader and child components.
- Hidden refetch loops after navigation or mutation.
- Global invalidation causing avoidable refetch storms.

### 3) Server/Client Execution Boundary

**Expectations**
- Server-only logic stays server-only; browser bundles exclude privileged logic.
- Serialization boundaries are explicit and stable.
- Hydration does not rely on non-deterministic values that differ server vs client.

**Anti-patterns**
- Importing server-only modules into browser-executed components.
- Passing non-serializable values through framework data channels.
- Hydration mismatch ignored as a benign warning.

### 4) Mutation and Optimistic UX Semantics

**Expectations**
- Mutation path defines pending, success, conflict, and failure states.
- Optimistic updates include rollback or reconciliation behavior.
- User-visible state remains coherent during retries or out-of-order responses.

**Anti-patterns**
- Optimistic write without rollback path.
- Conflicts silently overwritten in UI state.
- Button disabling/spinner behavior that masks stuck requests without timeout UX.

### 5) Error Boundaries and Recovery

**Expectations**
- Error boundaries are placed at meaningful UX containment levels.
- Recoverable vs non-recoverable failures present different user actions.
- Framework error hooks/middleware preserve diagnostics while keeping user output safe.

**Anti-patterns**
- One global error page for all failures regardless of locality.
- Swallowing framework loader/action errors and returning generic success UI.
- Recovery requiring full page reload for local component-level failures.

### 6) Auth and Session Flow Integration

**Expectations**
- Protected routes and data loaders enforce auth consistently.
- Session expiration handling is predictable across tabs and navigations.
- Redirect-after-auth preserves user intent safely.

**Anti-patterns**
- Auth checks only in UI component visibility logic.
- Session refresh loops triggered by route transitions.
- Redirect chains losing original destination or mutating request context unexpectedly.

### 7) Performance and Delivery Mechanics

**Expectations**
- Route-level splitting matches user navigation patterns.
- Critical rendering path avoids avoidable blocking dependencies.
- Prefetch strategy is bounded and evidence-based.

**Anti-patterns**
- Eager loading large feature bundles on initial route.
- Broad prefetch for low-probability paths.
- Performance regressions accepted without before/after evidence.

### 8) Observability of User Flows

**Expectations**
- Key route transitions, loader failures, and mutation outcomes are observable.
- Correlation context is preserved between framework layer and backend/API traces.
- Instrumentation granularity supports diagnosis without exposing sensitive data.

**Anti-patterns**
- Logging only terminal errors without navigation/mutation context.
- No trace continuity across client navigation and API calls.
- Analytics events emitted without outcome or latency fields.

## Planning/Review Prompts

Use these prompts to keep framework analysis focused:
- Which framework lifecycle owns this behavior, and is ownership singular?
- Can SSR render, hydration, and client navigation all produce the same user truth?
- Are loading, mutation, conflict, and error states all explicit and testable?
- Does route/layout composition reduce duplication and enforce policy centrally?
- Is framework instrumentation sufficient to diagnose a failed user flow end-to-end?

## Non-Goals

This reference does not:
- define repository-specific commands or CI policies
- replace architecture gate checks for boundary direction and system coupling
- replace language-specific correctness/typing/error-handling guidance

Use this reference together with architecture and language references to avoid overlap and maintain progressive-disclosure clarity.
