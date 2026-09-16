---
name: engineering-quality-baselines
description: Routes validation depth and evidence expectations, including required checks, through progressive disclosure across architecture gates, testing and validation, test authoring, review rubric, latent-risk routing, and long-horizon audit. Use when doing non-trivial implementation, PR/code review, or bug fix/refactor work.
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

Escalate to broader coverage on unresolved high-risk findings, unclear boundary ownership, failing validation evidence, or reviewer-identified uncertainty.

Load only relevant categories:
- Core principles: `references/core-principles.md` (read for every non-trivial implementation or review; also when intent/scope or tradeoffs are unclear)
- Architecture gates: `references/architecture-gates.md` (when boundaries, layering, or contracts change)
- Validation and evidence model: `references/testing-validation.md` (when selecting required checks and evidence depth)
- Test authoring: `references/test-authoring.md` (when writing, modifying, or reviewing tests)
- Review checks: `references/review-rubric.md` (when performing PR/code review or final Reviewer approval; symmetric checks and gate-fail precedence)
- Plan review: `references/core-principles.md` and the Symmetric checks section of `references/review-rubric.md` only (when reviewing a draft plan before approval; no latent-risk routing)
- Latent-risk review routing: `references/review-latent-risk.md` (when PR/code review or final Reviewer approval may involve state drift, derived data, fallbacks, contract divergence, merge semantics, scope leakage, hot-path cost, public API compatibility, diagnostics, build/CI hygiene, entrypoint admission, future-edit brittleness, validation-boundary issues, risk-specific tests, or information conservation across serialization, conversion, aggregation, and fallback boundaries)

### Drift Tripwires (always active)

- Trip when about to optimize, extend, or test something whose consumer or necessity cannot be named.
- Trip when adding a process step, validation, or automation justified mainly by "in case".
- Trip when repeatedly working around the same component, process step, or rule.
- Trip when the fix goes around a type, schema, boundary, or constraint that this task could change, or that sits outside `owns` and the plan could change on request (a shared type lacking a field is the usual case).
- Trip when adding a compatibility shim, wrapper, or dual code path for a consumer you cannot locate.

If tripped: surface the observation in the report (questions/blockers or lesson candidates) with the cleaner alternative and its cost delta, then classify it against the acceptance criteria and any packet pre-ruling: a workaround in your own edit whose remedy the criteria already decided is corrected to the decided shape and the check rerun; every other finding waits for the Orchestrator's ruling before any action. Read `references/long-horizon-audit.md` when the pattern looks systemic.

### Required Evidence Note (fallback template)

Two fields already have a home: a Worker report supplies required and optional checks as `validation_results` entries (`subagent-report-contract/references/schema.yaml`: `required`, `status: pass|fail|skipped`, `evidence`; a waived required check is `skipped` with the waiver evidence in `evidence`). No other field has an equivalent in the plan template or the report schema.

Include the note in the task output whenever the output does not already supply a field under a surviving obligation, and it adds no key to any schema. In a standalone Reviewer or Orchestrator output the note appears as the block below. In a Worker report, whose final message is exactly one YAML block, every field the report schema lacks is carried in an existing free-text key, each prefixed with the field name: risk profile with rationale, validation depth, and top risks as lines in `summary`; in-scope docs, out-of-scope docs with their reason, At Risk items, and residual risk as `assumptions` entries:

```
Quality routing note
- In-scope docs: [...]
- Out-of-scope docs: [...] (reason)
- Top risks: [security|data-integrity|migration|concurrency|external-deps|contract|performance]
- Risk profile: [low|medium|high] with rationale
- Validation depth: [targeted|extended|full-sweep]
- Required checks: `validation_results` entries with `required: true` when the output is a Worker report; otherwise [{name: ..., status: pass|fail|waived, evidence: ...}]
- Optional recommended checks: `validation_results` entries with `required: false` when the output is a Worker report; otherwise [{name: ..., status: pass|fail|skipped, evidence: ...}]
- At Risk items: [{item: ..., owner: ..., target_date: ...}] or []
- Residual risk / follow-up: [...]
```

Stop condition: stop only when acceptance is fully met, all required validations are `pass` or explicitly `waived` with rationale and evidence, no remaining `Fail` gates exist at the selected validation depth, and every `At Risk` item has an owner and target date recorded.

## Precedence

- This skill guides engineering decisions, checks, and evidence expectations.
- Repository-local documents define canonical required commands, mandatory validations, and policy precedence.
- If there is any conflict, follow repository-local required validation mappings and governance docs.
