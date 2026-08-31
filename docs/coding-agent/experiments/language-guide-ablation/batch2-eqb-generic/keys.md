# Keys — batch 2. hit = states the planted mechanism at the planted location.

| id | doc | planted defect | a hit must state |
|---|---|---|---|
| twf-01 | tech-web-frameworks | server-rendered component embeds Date.now()/locale formatting | nondeterministic server render diverges from client render (hydration mismatch); move to client-only or pass stable value |
| twf-02 | tech-web-frameworks | mutation succeeds but cached route/list data never revalidated | stale cache after mutation; invalidate/revalidate the affected query or route data |
| twf-03 | tech-web-frameworks | async route section fetch failure unhandled, no error boundary/fallback | fetch rejection escapes: needs error boundary or explicit error/fallback state at the route/section level |
| sbf-01 | stack-backend-frontend | API returns timeout_seconds, client passes it to setTimeout as ms | unit mismatch seconds vs milliseconds across the contract boundary |
| sbf-02 | stack-backend-frontend | client auto-retries a charge POST on timeout, no idempotency key | retry of non-idempotent mutation can double-charge; needs idempotency key or server dedupe |
| sbf-03 | stack-backend-frontend | quantity/price limits enforced only in the form; handler trusts payload | server must enforce validation; client-side checks are bypassable UX only |
| sec-01 | security-boundaries | new admin/export endpoint checks session (authn) but no role/permission (authz) | any authenticated user reaches admin data; add authorization check at the endpoint |
| sec-02 | security-boundaries | startup failure logs entire config object including api_key/db password | secrets written to logs; redact or log field allowlist |
| sec-03 | security-boundaries | account-deletion triggered via GET link | state-changing GET: CSRF-able and prefetchable; must be POST/DELETE with CSRF protection |
| sec-04 | security-boundaries | CI adds dependency at "latest" and pipes remote install script to sh | unpinned dependency + remote script execution; pin versions/hashes |
| perf-01 | review-latent-risk-performance | per-order customer lookup inside loop over all orders | N+1 query; batch fetch or join before the loop |
| perf-02 | review-latent-risk-performance | regex compiled and catalog re-sorted inside per-item hot loop | invariant work (regex compile, sort) hoisted out of the loop |

Clean decoys (findings are FPs unless they expose a real authoring error):
c1: endpoint with correct authn+authz and parameterized query. c2: typed Duration used
end-to-end (no unit ambiguity). c3: mutation followed by explicit cache invalidation.
c4: single batched query with prepared statement. Known acceptable nitpicks (count as
neither hit nor FP): c1 missing rate limiting; c3 missing optimistic-update rollback;
generic "add tests/logging" suggestions on any decoy.
