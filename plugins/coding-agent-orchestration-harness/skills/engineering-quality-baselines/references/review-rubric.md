# Lightweight Review Rubric

Use this rubric as a quick summary aid after detailed checks.
It does **not** replace required validation, tests, or policy gates.

## 30-Second Pass

- Scope is clear and change size is proportional to the problem.
- Behavior and contracts are preserved or intentionally versioned.
- Risks, assumptions, and follow-up items are visible.

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
