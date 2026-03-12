# Architecture Gates

## Contents

- [Purpose](#purpose)
- [How to Use in Planning](#how-to-use-in-planning)
- [How to Use in Review](#how-to-use-in-review)
- [Architecture Gates](#architecture-gates)
- [Decision Guidance](#decision-guidance)
- [Output Template for Plans and Reviews](#output-template-for-plans-and-reviews)
- [Non-Goals](#non-goals)

## Purpose

Use these architecture gates to evaluate change design quality before implementation and during review. They are cross-stack and repository-agnostic, and they focus on boundaries, dependency direction, and operational safety rather than language-specific style details.

## How to Use in Planning

Apply these gates while writing or reviewing an execution plan:

1. Map the target behavior and identify which boundaries are crossed (UI, service/application, domain, data, integration, infra).
2. For each affected boundary, state the intended dependency direction and ownership.
3. Record risks and define the minimum evidence needed to demonstrate the gate is satisfied.
4. Reject or split tasks that violate gates unless an explicit exception and mitigation are documented.

## How to Use in Review

For each gate below, classify the result as one of:
- **Pass**: gate satisfied with clear evidence.
- **At Risk**: partially satisfied; issue is non-blocking but requires follow-up.
- **Fail**: gate not satisfied; must be fixed or explicitly waived.

A change should not be approved when any gate is **Fail** unless explicitly waived using the canonical required-check waiver template in [testing-validation.md](testing-validation.md#canonical-required-check-waiver-template).

## Architecture Gates

### Gate 1: Clear Responsibility Boundaries

**Expectation**
- Each layer/module has a clear responsibility and does not absorb unrelated concerns.
- Business rules remain in domain/application logic, not scattered into presentation or persistence details.

**Evidence expectations**
- Planning notes identify impacted boundaries and owned responsibilities.
- Review confirms behavior changes are implemented in the correct layer.
- No unexplained cross-layer logic movement.

**Anti-patterns**
- UI or transport handlers embedding business invariants.
- Data access layer deciding domain policy.
- “Utility” modules accumulating unrelated logic as a shortcut.

### Gate 2: Correct Dependency Direction

**Expectation**
- Dependencies point from outer layers toward stable inner abstractions.
- Core behavior does not depend directly on volatile delivery or storage details.

**Evidence expectations**
- Plan documents dependency direction for touched components.
- Review verifies new imports/calls do not invert boundaries.
- Abstraction seams are explicit where external systems are involved.

**Anti-patterns**
- Domain logic directly calling framework, transport, or vendor clients.
- Circular dependencies between modules.
- Feature code bypassing interfaces to reach lower-level internals.

### Gate 3: Cohesive Change Surface

**Expectation**
- The change set is cohesive and aligned to one architectural intent.
- Cross-cutting updates are deliberate and traceable.

**Evidence expectations**
- Plan links each touched area to the same architectural objective.
- Review confirms no unrelated edits are bundled.
- Refactor-only changes are separated from behavior changes when risk warrants.

**Anti-patterns**
- Mixing feature work, refactors, and incidental cleanup without rationale.
- Large “drive-by” edits across modules with weak coupling to the objective.
- Hidden behavior changes inside nominally mechanical diffs.

### Gate 4: Explicit Interface Contracts

**Expectation**
- Boundaries between components are explicit, minimal, and stable.
- Inputs, outputs, and failure semantics are intentionally modeled.

**Evidence expectations**
- Plan states contract-impact scope (none/additive/breaking).
- Review verifies contract updates are synchronized across producers/consumers.
- Failure modes are explicit and not silently swallowed.

**Anti-patterns**
- Implicit contracts communicated only by call-site assumptions.
- Breaking contract changes shipped without migration or compatibility notes.
- Returning ambiguous success/failure signals.

### Gate 5: Data and State Integrity

**Expectation**
- Data ownership, lifecycle, and state transitions are consistent and enforceable.
- Invariants are protected at authoritative boundaries.

**Evidence expectations**
- Plan identifies impacted invariants and lifecycle transitions.
- Review verifies invariant checks remain at reliable enforcement points.
- Concurrent or repeated execution behavior is considered where relevant.

**Anti-patterns**
- Invariants enforced only in optional caller paths.
- Conflicting write paths without ownership clarity.
- State transitions that allow invalid intermediate states.

### Gate 6: Operational and Failure Containment

**Expectation**
- Failures are contained to the smallest practical scope.
- Timeouts, retries, idempotency, and degradation paths are intentional when integrating external dependencies.

**Evidence expectations**
- Plan lists likely failure modes for touched integrations.
- Review verifies error propagation and fallback behavior are deliberate.
- Risky operations include containment strategy notes.

**Anti-patterns**
- Unbounded retries or blocking operations in critical paths.
- Broad exception/error suppression that obscures root causes.
- Cascading failure paths without isolation boundaries.

### Gate 7: Observability of Architectural Behavior

**Expectation**
- Meaningful signals exist to understand critical behavior and failures at boundaries.
- Observability supports diagnosis without exposing sensitive internals.

**Evidence expectations**
- Plan identifies what success/failure signals are needed for changed flows.
- Review confirms key boundary events and failures are inspectable.
- Sensitive data exposure risk in logs/telemetry is assessed.

**Anti-patterns**
- Silent failure paths with no diagnosable signal.
- Overly noisy instrumentation that hides actionable indicators.
- Logging sensitive payloads as a convenience.

## Decision Guidance

Use the gates with proportional rigor:
- **Low-risk localized change**: verify relevant gates for touched boundary; concise evidence is acceptable.
- **Cross-module or behavior-sensitive change**: evaluate all relevant gates and require explicit risk notes.
- **High-risk architectural change**: require comprehensive gate evidence and clear rollback/mitigation framing.

## Output Template for Plans and Reviews

Use this compact structure in planning or review artifacts:

- **Boundary map**: impacted layers/modules and dependency direction.
- **Gate status**: pass/at-risk/fail for each relevant gate.
- **Evidence**: what demonstrates each status.
- **Risks**: unresolved concerns and impact.
- **Mitigation**: follow-up actions, owner, and target date.

## Non-Goals

These gates do not:
- Prescribe repository-specific commands, CI jobs, or mandatory checks.
- Replace language-level correctness, security, or style guidance.
- Override repository-local governance for required validation and approvals.
