# Lightweight Review Rubric

Use this rubric as a quick summary aid after detailed checks.
It does **not** replace required validation, tests, or policy gates.

## 30-Second Pass

- Scope is clear and change size is proportional to the problem.
- Every contract change is intentional; nothing is broken or preserved by accident.
- Risks, assumptions, and follow-up items are visible.

## Symmetric Checks (0 findings requires checking both directions)

Each pair below has two failure directions. Checking only the familiar direction and passing the other by default is an incomplete review, not a pass.

Compatibility:
- Flag consumer-visible behavior or contracts broken without stated intent.
- Flag compatibility layers (shims, wrappers, dual code paths, deprecation layers) that do not map to a locatable consumer beyond the change's reach — the operational definition is in [core-principles.md](core-principles.md). Speculative preservation is scope creep to flag, exactly as an unintended break is.

Tests:
- Flag over-constrained tests: would a legitimate refactor fail them? Do they pin implementation details instead of a depended-on contract?
- Flag unguarded changed contracts: for each contract this change touches, name the test that fails if it breaks; if none exists, that is a finding.

## Scorecard (0-2 each)

- Correctness: handles expected paths and key edge cases.
- Maintainability: clear structure, naming, and ownership boundaries.
- Security: trust boundaries and sensitive data handling are addressed.
- Validation: required checks were run and evidence is attached.

Scoring guide:
- 0 = missing or high risk
- 1 = partially addressed
- 2 = adequately addressed

## Outcome Bands

- 7-8: Approve (or approve with minor follow-ups).
- 5-6: Needs revision before approval.
- 0-4: Reject for rework; risks are not controlled.

## Gate-Fail Precedence (Blocking)

Scorecard bands are advisory summaries.

If any relevant architecture, language, framework, or repository-required validation gate is **Fail**, the change is blocking regardless of total score and cannot be approved unless explicitly waived.

## Required Companion Check

Before final approval, confirm:
- Required validation gates were actually executed.
- Evidence is concrete (commands, outputs, artifacts, or review notes).
- Any explicitly waived checks reference the canonical required-check waiver template in [testing-validation.md](testing-validation.md#canonical-required-check-waiver-template).

## Latent-Risk Companion Check

Before final approval, if the change shape matches a trigger in `review-latent-risk.md`, read that router and only the applicable conditional latent-risk references.

Do not expand this rubric with the full latent-risk checklist.

A relevant latent-risk FAIL blocks approval unless waived or recorded as accepted residual risk.
