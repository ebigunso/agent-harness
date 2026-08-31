---
name: engineering-quality-baselines
description: Trigger for non-trivial implementation, PR/code review, and bug fix/refactor work; routes validation depth and evidence expectations, including required checks, through progressive disclosure across architecture, stack, language/tech, validation, and security.
---

# Engineering Quality Baselines

## Quick Start

### Intent and Scope

- Intent: provide a minimum-sufficient, repository-agnostic quality baseline for non-trivial changes and reviews.
- Scope: implementation, review, refactor, and validation-depth selection.
- Boundary: this skill guides decisions and evidence quality; repository-local docs remain canonical for required commands and policy precedence.

### Risk Triage (first pass)

Classify risk before loading deeper references:
- Security impact
- Data integrity impact
- Migration/schema impact
- Concurrency/ordering impact
- External dependency/integration impact
- Contract/API/schema compatibility impact
- Performance/latency/resource impact

If all are low and local, use the default targeted validation depth. If any are medium/high or uncertain, escalate to a deeper validation tier.

### Routing Decision

Load only the reference categories relevant to the change; explicitly note major categories left out and why. Escalate to broader coverage on unresolved high-risk findings, unclear boundary ownership, failing validation evidence, or reviewer-identified uncertainty.

Per-language baseline references (Rust/TS/Python/Go idiom and anti-pattern guides) were removed after ablation testing showed current frontier models apply that content reliably without them — see ADR-I-0004 (implements ADR-D-0015). Do not reintroduce per-language baseline docs without new ablation evidence.

Load only relevant categories:
- Core principles: `references/core-principles.md` (read for every non-trivial implementation or review; also when intent/scope or tradeoffs are unclear)
- Architecture gates: `references/architecture-gates.md` (when boundaries, layering, or contracts change)
- Stack concerns (backend/frontend): `references/stack-backend-frontend.md` (when execution path spans backend/frontend concerns)
- Validation and evidence model: `references/testing-validation.md` (when selecting required checks and evidence depth)
- Test authoring: `references/test-authoring.md` (when writing, modifying, or reviewing tests)
- Security boundaries: `references/security-boundaries.md` (when auth, secrets, trust boundaries, or data sensitivity are touched)
- Review scoring summary: `references/review-rubric.md` (when performing PR/code review or final quality scoring)
- Latent-risk review routing: `references/review-latent-risk.md` (when PR/code review or final Reviewer approval may involve state drift, derived data, fallbacks, contract divergence, merge semantics, scope leakage, hot-path cost, public API compatibility, diagnostics, build/CI hygiene, entrypoint admission, future-edit brittleness, validation-boundary issues, risk-specific tests, or information conservation across serialization, conversion, aggregation, and fallback boundaries)

Then, when a web framework is meaningfully touched:
- Web frameworks: `references/tech-web-frameworks.md`

### Drift Tripwires (always active)

- Trip when about to optimize, extend, or test something whose consumer or necessity cannot be named.
- Trip when adding a process step, validation, or automation justified mainly by "in case".
- Trip when repeatedly working around the same component, process step, or rule.
- Trip when the fix goes around a type, schema, boundary, or constraint this task could change.

If tripped: stop and surface the observation through existing channels (report questions/blockers, lesson candidates, or the user) together with the cleaner alternative and its cost delta — never act on it or suppress it silently, and do not proceed on the workaround without a ruling — and read `references/long-horizon-audit.md` when the pattern looks systemic.

### Required Evidence Note (template)

Use this note in task output:

```
Quality routing note
- In-scope docs: [...]
- Out-of-scope docs: [...] (reason)
- Top risks: [security|data-integrity|migration|concurrency|external-deps|contract|performance]
- Risk profile: [low|medium|high] with rationale
- Validation depth: [targeted|extended|full-sweep]
- Required checks: [{name: ..., status: pass|fail|waived, evidence: ...}]
- Optional recommended checks: [{name: ..., status: pass|fail|skipped, evidence: ...}]
- At Risk items: [{item: ..., owner: ..., target_date: ...}] or []
- Residual risk / follow-up: [...]
```

Stop condition: stop only when acceptance is fully met, all required validations are `pass` or explicitly `waived` with rationale and evidence, no remaining `Fail` gates exist at the selected validation depth, and every `At Risk` item has an owner and target date recorded.

## Precedence

- This skill guides engineering decisions, checks, and evidence expectations.
- Repository-local documents define canonical required commands, mandatory validations, and policy precedence.
- If there is any conflict, follow repository-local required validation mappings and governance docs.
