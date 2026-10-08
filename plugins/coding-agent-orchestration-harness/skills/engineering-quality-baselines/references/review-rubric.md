# Lightweight Review Rubric

Use this rubric as a quick summary aid after detailed checks.
It does **not** replace required validation, tests, or policy gates.

## 30-Second Pass

- Scope is clear and change size is proportional to the problem.
- Every contract change is intentional; nothing is broken or preserved by accident.
- Risks, assumptions, and follow-up items are visible.

## Symmetric checks

Each pair below has two failure directions. Checking only the familiar direction and passing the other by default is an incomplete review, not a pass.

Compatibility:
- Flag consumer-visible behavior or contracts broken without stated intent.
- Flag compatibility layers (shims, wrappers, dual code paths, deprecation layers) that do not map to a locatable consumer beyond the change's reach — the operational definition is in [core-principles.md](core-principles.md). Speculative preservation is scope creep to flag, exactly as an unintended break is.

Tests:
- Flag over-constrained tests: would a legitimate refactor fail them? Do they pin implementation details instead of a depended-on contract?
- Flag unguarded changed contracts: for each contract this change touches, name the test that fails if it breaks; if none exists, that is a finding.

## Gate-fail precedence

If any relevant architecture, language, framework, or repository-required validation gate is **Fail**, the change is blocking and cannot be approved unless explicitly waived.

## Required Companion Check

Before final approval, confirm:
- Required validation gates were actually executed.
- Evidence is concrete (commands, outputs, artifacts, or review notes).
- No evidence artifact (a test output, a probe result, a captured sample, or the like) is left in the change or lying in the working tree, untracked files included, once its claim is recorded: each one found is a finding, unless the change makes the case that future work rests on it. Regression tests are not evidence artifacts. Where the repository's own text says otherwise, it wins ([SKILL.md](../SKILL.md#precedence)).
- Any explicitly waived checks reference the canonical required-check waiver template in [testing-validation.md](testing-validation.md#canonical-required-check-waiver-template).

## Latent-Risk Companion Check

Before final approval, if the change shape matches a trigger in `review-latent-risk.md`, read that router and only the applicable conditional latent-risk references.

Do not expand this rubric with the full latent-risk checklist.

A relevant latent-risk FAIL blocks approval unless waived or recorded as accepted residual risk.
