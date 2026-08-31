# Testing & Validation Model (Required vs Recommended)

## Purpose

This document defines a repository-agnostic model for selecting and reporting validation.

It distinguishes:
- **Required validation**: mandatory checks that must pass (or be explicitly waived) before claiming completion.
- **Recommended validation**: additional checks that increase confidence but are not blocking by default.

---

## Validation Classes

### Class 1) Required Checks (Blocking)

Use for checks that protect correctness, safety, compatibility, or policy compliance.

Typical examples:
- Required unit/integration tests for changed runtime paths.
- Required type-check/build gates for changed compile targets.
- Required migration/runtime checks for changed data or environment contracts.
- Required manual review checkpoints when documentation or operational guidance changes.

Rules:
- If required validation is missing or failing, status cannot be marked done.
- Required checks may be skipped only with explicit waiver from the governing authority for that repository/workflow.
- Any waiver must record risk and what remains unvalidated.

### Class 2) Optional Recommended Checks (Non-Blocking)

Use for confidence amplification, regression prevention, and quality signal improvement.

Typical examples:
- Wider test suites beyond touched scope.
- Performance, load, or exploratory checks for low-risk edits.
- Additional static analysis not designated mandatory by local policy.

Rules:
- Recommended checks should be executed when cost-effective and risk-appropriate.
- Skipping recommended checks does not block completion if all required checks are satisfied.

---

## Evidence Expectations

Validation evidence should be explicit, reproducible, and reviewable.

Minimum evidence set:
- Risk profile (`low|medium|high`) and chosen validation depth with concise rationale.
- What was run/reviewed (command or manual checklist item).
- Result (`pass`, `fail`, `waived`, or `skipped`) with concise reason for non-pass outcomes.
- Scope linkage (what changed and why the check applies).
- Remaining risk for any skipped/failed required item.

For manual validations (including doc-review):
- Record the exact review criterion used.
- Record outcome and any discrepancies found.
- Confirm command/reference consistency where instructions are documented.

For automated validations:
- Capture exact command and outcome.
- Capture targeted mode/range if not running full suite.
- Include artifact paths where applicable (logs, reports, screenshots).

---

## Evidence Integrity

Rules that keep validation evidence trustworthy, not just present:

- Absence claims ("no X remains") require an evidence search matching the broadest syntactic form of X — encode the class, not the expected spelling — scoped to the repo root with only documented historical/generated paths excluded.
- Never infer file/asset absence from ignore-aware search (`rg`/`fd` honor `.gitignore`); require direct filesystem checks or `--no-ignore`.
- Skip-capable tests can report green with unexecuted bodies: when specific-test evidence matters, rerun it targeted and confirm no skip message, and verify gated live tests once with the service deliberately down.
- Scripted bulk text mutations assert their postconditions before commit — replaced count, required text present and absent, and placement (the mutated content sits inside its owning section, not merely somewhere in the file); in documents with non-uniform structure, prefer anchored single-target edits over regex segment surgery.
- Targeted-test evidence requires a positive executed-test count, never exit code alone — filters can match zero tests and still exit 0.
- When validation fails in tests the change did not touch, rerun against baseline HEAD (stash/worktree) to classify pre-existing vs regression before remediating.
- Evidence claims must state scenario scope, config identity, and dependency provenance at the point of claim; label scoped evidence as scoped.
- Temporary test mutations that must restore exactly (verify-fail-restore sequences, planted mismatches): record a pre-edit hash and verify it after restoration — patch tooling can silently change line endings on edited lines, which content comparison cannot see.
- Assert on the surface that owns the validated behavior, not a mirror or derived copy — a mirror assertion stays green while the owning surface drifts.

---

## Risk Profile → Validation Depth and Check Selection

Use this quick mapping to choose proportional validation depth and check selection.

| Change risk profile | Validation depth guidance | Minimum required checks | Optional recommended checks |
|---|---|---|---|
| Low (localized, non-sensitive, reversible) | `targeted` (default) | Targeted required checks for touched surface + concise evidence | One nearby regression-focused check |
| Medium (cross-module behavior or contract-adjacent) | `extended`, when boundaries expand or uncertainty remains | All applicable required checks across affected boundaries + explicit residual-risk note | Wider integration coverage and focused manual scenario review |
| High (security/data integrity/critical path/breaking contract) | `full-sweep`, when change impact is systemic or hard to bound | Full applicable required checks, explicit failure-mode review, and clear rollback/mitigation notes | E2E/operational validation and before/after evidence artifacts |

Escalate to the next depth tier when uncertainty is high or impact is hard to bound.

---

## Canonical Required-Check Waiver Template

Use this template whenever a required validation check is waived.

```text
Required-check waiver
- What is waived: <specific required check(s) or gate(s)>
- Why waived now: <constraint or reason>
- Risk accepted and impact: <what could fail, who/what is affected>
- Mitigation and follow-up: <short-term controls + concrete next action>
- Owner and expiration: <responsible owner> ; <waiver expiry date/condition>
```

Notes:
- Keep waivers time-bounded and specific; avoid blanket waivers.
- If expiration is reached before closure, re-approval is required.

---

## Precedence Model (Canonical Source for Required Checks)

This model is intentionally repo-agnostic. It does not define repository-canonical commands.

Precedence rule:
1. Repository-local validation mapping is canonical for **required** checks.
2. Repository-local governance/rules can add mandatory constraints.
3. This global baseline defines selection and evidence behavior when local docs are silent.

Fallback when repository-local required-validation mapping is missing or ambiguous:
1. Inspect repository CI/build/test scripts and pipeline definitions to infer candidate required checks.
2. Treat the ambiguity as an escalation condition; do not silently downgrade inferred required checks.
3. Record assumptions explicitly in validation evidence (sources inspected, inferred required checks, and escalation target/owner).

If sources disagree:
- Treat local required-validation mapping as authoritative for blocking checks.
- Escalate ambiguity rather than silently downgrading required checks.

---

## Practical Decision Flow

1. Identify changed surface (code paths, tests, docs, ops/runbooks).
2. Load repository-local required-validation mapping.
3. If mapping is missing/ambiguous, apply fallback inference from CI/build/test scripts and escalate.
4. Mark each applicable check as required or optional recommended.
5. Select validation depth (`targeted`, `extended`, or `full-sweep`) based on risk and uncertainty.
6. Execute all required checks first.
7. Execute optional recommended checks based on risk/time budget.
8. Report evidence with explicit pass/fail/waived/skipped status, assumptions, and residual risk.

---

## Completion Criteria

Completion is valid when:
- All applicable required checks passed, or
- A required-check waiver is explicitly granted and risk is documented.

Completion is not valid when:
- Required checks are missing without waiver.
- Evidence is insufficient to verify what was validated.
