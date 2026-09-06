# Latent-Risk Review Router

Purpose: route reviewers to deeper risk checks only when the change shape warrants them.

Core review question:

> What future condition would make this code lie, drift, scale poorly, silently degrade, or admit an invalid state?

## Conditional References

During PR/code review or final Reviewer approval, identify applicable triggers and read only the matching references.

| Trigger | Reference or check |
|---|---|
| Persisted/lifecycle state, invariants, cached/derived/denormalized data, counters, indexes, IDs, ordering, merge/update/upsert logic. | `review-latent-risk-state.md` |
| Fallible operations, retries, timeouts, fallback, partial success, stale/corrupt data, unavailable/external dependencies, suppressed errors, or degraded behavior. | `review-latent-risk-failure.md` |
| Multiple implementations of one contract (fake/production, client/server validation, batch/single, sync/async), or request/user/tenant/root/config/cache scoped decisions. | `review-latent-risk-contract-scope.md` |
| Hot paths, loops over growing data, locks, repeated scans/sorts/allocations/I/O, or iterative network/database/API calls. | Assess hot-path cost directly and report the criterion. |
| Enum/list/caller expansion brittleness, dead code, speculative APIs, public/internal API surface, abstractions, positional lists, switch/default logic, test-only production surface/hooks, or speculative extension points. | `review-latent-risk-future-surface.md` |
| Domain/config construction, constructible invalid values, delayed validation, validation boundaries, or any risky behavior lacking targeted regression coverage (including fallback/merge/lifecycle/corrupt-data/duplicate/race behavior). | `review-latent-risk-validation-tests.md` |
| Public/semi-public APIs, exports/re-exports, prelude/crate-root visibility, docs/examples, feature-gated public items, or downstream-facing DTOs. | `review-latent-risk-public-api.md` |
| Multiple entrypoints, explicit/inferred intent, admission/filtering, candidate/accepted sets, or data filtered, admitted, rejected, hydrated, recorded, cached, counted, emitted, or enqueued; side effects after selection. | `review-latent-risk-entrypoints-admission.md` |
| Errors, warnings, diagnostics, health, metrics, traces, telemetry, validation failures, rejection diagnostics, or debug metadata/details. | `review-latent-risk-diagnostics.md` |
| Build cfg, feature flags, test-only/platform-specific code, imports, strict lints, warnings-as-errors, docs warnings, docs/examples, or CI-sensitive hygiene. | `review-latent-risk-build-ci.md` |
| Information conservation across serialization, conversion, aggregation, wrapping, or fallback boundaries carrying structured data. | `review-latent-risk-conservation.md` |

## Reporting Rule

Only report applicable criteria.

Do not print the full checklist when most criteria are irrelevant. Report latent-risk issues under the normal review findings. For each applicable latent-risk issue, include:

- criterion:
- status: PASS | AT_RISK | FAIL
- evidence:
- issue, if any:
- required regression test, if applicable:

Approval is blocked when an applicable latent-risk item is FAIL and no waiver or accepted residual-risk note exists.
