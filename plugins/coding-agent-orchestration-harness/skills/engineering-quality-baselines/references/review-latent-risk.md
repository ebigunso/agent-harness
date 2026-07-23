# Latent-Risk Review Router

Purpose: route reviewers to deeper risk checks only when the change shape warrants them.

Core review question:

> What future condition would make this code lie, drift, scale poorly, silently degrade, or admit an invalid state?

## Always Do This Short Pass

During PR/code review or final Reviewer approval, identify whether the change touches any of these risk shapes:

1. State, invariants, cached or derived data, counters, indexes, IDs, ordering, merge/update/upsert logic.
2. Fallible operations, retries, timeouts, fallback paths, stale/corrupt data, unavailable dependencies.
3. Multiple implementations of one contract, fake vs production paths, client/server validation, batch/single paths, sync/async paths.
4. Request/user/tenant/root/config/cache scoped decisions.
5. Hot paths, loops over growing data, locks, repeated scans/sorts/allocations/I/O.
6. Enum/list/caller expansion brittleness, dead code, speculative APIs, test-only production surface.
7. Domain/config construction, validation boundaries, risky behavior lacking targeted regression tests.
8. Public or semi-public API surface, exports, prelude/crate-root visibility, docs/examples, feature-gated public items, or downstream-facing DTOs.
9. Multiple entrypoints, explicit vs inferred intent, admission/filtering, candidate vs accepted sets, or side effects after selection.
10. Errors, warnings, diagnostics, health, metrics, traces, telemetry, or debug metadata.
11. Build cfg, feature flags, test-only code, strict lints, warnings-as-errors, docs warnings, or CI-sensitive hygiene.
12. Information conservation across serialization, conversion, aggregation, and fallback boundaries.

## Conditional References

Read `review-latent-risk-state.md` when:
- persisted state, lifecycle state, counters, indexes, cache, derived data, denormalized data, IDs, ordering, merge, update, or upsert behavior changes.

Read `review-latent-risk-failure.md` when:
- the change includes fallible operations, retries, fallback, timeout handling, partial success, stale data, corrupt data, external dependencies, suppressed errors, or degraded behavior.

Read `review-latent-risk-contract-scope.md` when:
- two or more paths claim to implement the same contract, or logic depends on user/request/tenant/root/config/cache scope.

Read `review-latent-risk-performance.md` when:
- loops touch potentially growing data, hot paths change, expensive work may repeat, locks are involved, or network/database/API calls appear in iterative code.

Read `review-latent-risk-future-surface.md` when:
- the change adds public/internal API surface, abstractions, enum handling, positional lists, switch/default logic, test-only hooks, or speculative extension points.

Read `review-latent-risk-validation-tests.md` when:
- invalid values may be constructible, validation is delayed until use, or the change has fallback/merge/lifecycle/corrupt-data/duplicate/race behavior that needs targeted regression coverage.

Read `review-latent-risk-public-api.md` when:
- public or semi-public API surface, exports, re-exports, prelude/crate-root visibility, docs/examples, feature-gated public items, or downstream-facing DTOs change.

Read `review-latent-risk-entrypoints-admission.md` when:
- the same domain action enters through multiple APIs, or candidate data is filtered, admitted, rejected, hydrated, recorded, cached, counted, emitted, or enqueued.

Read `review-latent-risk-diagnostics.md` when:
- the change emits or modifies errors, health state, metrics, traces, telemetry, validation failures, rejection diagnostics, or debug details.

Read `review-latent-risk-build-ci.md` when:
- the change touches cfgs, feature flags, test-only paths, platform-specific code, imports, lints, docs, examples, warning-sensitive code, or CI/build-sensitive behavior.

Read `review-latent-risk-conservation.md` when:
- the change serializes, converts, aggregates, wraps, or falls back across a boundary that carries structured data.

## Reporting Rule

Only report applicable criteria.

Do not print the full checklist when most criteria are irrelevant. Report latent-risk issues under the normal review findings. For each applicable latent-risk issue, include:

- criterion:
- status: PASS | AT_RISK | FAIL
- evidence:
- issue, if any:
- required regression test, if applicable:

Approval is blocked when an applicable latent-risk item is FAIL and no waiver or accepted residual-risk note exists.
