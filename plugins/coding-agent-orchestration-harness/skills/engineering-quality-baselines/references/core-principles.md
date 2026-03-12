# Core Principles

## Contents

- [How to Use](#how-to-use)
- [Core Implementation and Review Principles](#core-implementation-and-review-principles)
- [Common Anti-Patterns](#common-anti-patterns)
- [Quick Review Pass (Minimal)](#quick-review-pass-minimal)
- [Non-Goals](#non-goals)

Universal baseline principles for implementation and review that preserve behavior, reduce risk, and improve long-term maintainability.

These principles are intentionally repository-agnostic and language-neutral.

## How to Use

1. Start with this document for every non-trivial implementation or review.
2. Select only applicable companion references (architecture, stack, language, validation, security).
3. Apply each principle as both a build-time and review-time check.
4. Prefer the smallest change that satisfies correctness, clarity, and evidence requirements.
5. If trade-offs are required, document the chosen trade-off and residual risk.

## Core Implementation and Review Principles

### 1) Preserve Intended Behavior

- Keep externally observable behavior stable unless a behavior change is explicitly intended.
- For intended behavior changes, make scope and impact explicit.
- Treat compatibility (API contracts, data shape, persistence semantics) as first-class.

Review checks:
- Are behavior changes intentional and clearly bounded?
- Are interface and contract impacts explicit?

### 2) Prefer Root-Cause Fixes Over Symptom Patches

- Address the source of the issue instead of adding repeated local workarounds.
- Avoid duplicating fragile logic across modules.
- Strengthen invariants where failures originate.

Review checks:
- Does the change remove the cause or only suppress outcomes?
- Is duplicated or compensating logic being introduced?

### 3) Keep Changes Small, Cohesive, and Reversible

- Group related edits into a single coherent unit.
- Avoid coupling unrelated refactors with functional changes.
- Make rollback straightforward by limiting blast radius.

Review checks:
- Is the diff focused on one clear goal?
- Can this change be safely reverted without collateral edits?

### 4) Optimize for Readability and Local Reasoning

- Favor clear names, explicit boundaries, and straightforward control flow.
- Keep functions/components at a single level of abstraction.
- Reduce hidden coupling and surprising side effects.

Review checks:
- Can a reader understand intent without reconstructing hidden context?
- Are responsibilities and boundaries obvious?

### 5) Define and Protect Invariants

- Make assumptions explicit at module boundaries.
- Validate inputs at trust boundaries and normalize internal state early.
- Fail early with actionable errors when invariants are violated.

Review checks:
- Which invariants are introduced or relied upon?
- Are boundary checks and failure modes explicit?

### 6) Maintain Contract Fidelity Across Layers

- Keep data models, service contracts, and adapters aligned.
- Avoid silent field loss, implicit coercions, or shape drift.
- Version and migrate interfaces deliberately when needed.

Review checks:
- Do upstream/downstream boundaries agree on schema and semantics?
- Is contract drift prevented or merely tolerated?

### 7) Build for Testability and Verifiability

- Structure logic so important decisions are easy to test.
- Prefer deterministic seams over hidden global state.
- Match validation depth to risk and change surface.

Review checks:
- Can critical behavior be validated without fragile setup?
- Is evidence proportional to risk?

### 8) Control Complexity and Duplication

- Remove accidental complexity before introducing abstraction.
- Abstract only when multiple concrete uses justify it.
- Keep dependency direction intentional and acyclic where practical.

Review checks:
- Does abstraction reduce or increase cognitive load?
- Is new complexity justified by measurable maintenance benefit?

### 9) Make Failure Modes Explicit and Safe

- Handle errors at appropriate boundaries with useful context.
- Avoid swallowing failures or converting them into ambiguous states.
- Design fallback behavior to be safe, observable, and bounded.

Review checks:
- Are failure paths visible and diagnosable?
- Do fallbacks preserve safety and correctness expectations?

### 10) Leave the System Easier to Change

- Improve clarity, boundaries, or diagnostics when touching code.
- Avoid debt amplification in the name of short-term speed.
- Prefer incremental improvement aligned with existing architecture.

Review checks:
- Is maintainability improved, neutral, or degraded?
- Did the change reduce future risk at reasonable cost?

## Common Anti-Patterns

- Mixed-purpose diffs: combining behavior changes, refactors, and formatting into one opaque change.
- Implicit behavior shifts: changing defaults or contracts without explicit acknowledgment.
- Validation theater: broad but low-signal checks that do not cover the risky paths.
- Defensive duplication: copy-pasted guards instead of restoring boundary invariants.
- Abstraction-first design: introducing generic layers before concrete needs exist.
- Silent failure handling: catching and suppressing errors without observability or correction path.
- Hidden coupling: introducing cross-module dependencies that obscure ownership and change impact.
- Review by surface area: approving based on file count or size instead of risk and semantics.

## Quick Review Pass (Minimal)

Use this short pass when time is limited:
- Intent: Is the goal explicit and scope-bounded?
- Behavior: Are observable changes intentional and compatible?
- Invariants: Are boundary assumptions and checks explicit?
- Complexity: Did the diff reduce, hold, or increase complexity?
- Evidence: Is validation targeted at the highest-risk paths?
- Maintainability: Is the codebase easier to evolve after this change?

## Non-Goals

- This document does not define repository-specific commands, CI gates, or policy precedence.
- This document does not replace architecture, language, security, or validation references.
- This document does not prescribe framework-specific implementation patterns.
