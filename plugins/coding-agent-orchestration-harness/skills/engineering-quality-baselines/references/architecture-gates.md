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

Keep layer responsibilities clear; business rules in domain/app. Map affected owners in plan; verify correct placement and explain moves. No UI policy, policy in data access, or catch-all utilities.

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
