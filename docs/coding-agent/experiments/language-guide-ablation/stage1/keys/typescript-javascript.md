# Answer key — TypeScript/JavaScript fixtures

Grading rule: hit = planted mechanism at planted location; partial = area without mechanism.
Findings on clean fixtures are false positives unless they expose a real authoring error.

## Planted

| id | bullet | planted defect | a hit must state |
|---|---|---|---|
| ts-01 | T3 | `as any` cast at the SDK boundary | type check disabled at exactly the boundary that changed; model the v9 return type instead |
| ts-02 | T11/T4 | `req.body as SignupEvent` — compile-time cast, no runtime validation | untrusted webhook payload reaches the DB unvalidated; `.toLowerCase()` throws on missing email |
| ts-03 | T14 | unawaited `metering.recordUsage` promise feeding billing | fire-and-forget critical promise; rejection is unhandled, usage silently lost |
| ts-04 | T13 | bare `catch { continue }` in the feed loop | failures swallowed with no logging/observability; partial import indistinguishable from success |
| ts-05 | T12 | `CouponSchema.parse` throws after `orders.create` + `inventory.reserve` wrote | validation after side effects; invalid coupon leaves an orphaned order and reserved stock |
| ts-06 | T15 | hand-copied `OrderStatus` interface with a "keep in sync" comment | manual contract duplicate will drift; derive from the published `@acme/contracts` zod schema |
| ts-07 | T2 | all-optional flat object for a 4-state result | invalid combinations representable (done without resultUrl, etc.); use a discriminated union |
| ts-08 | T10 | domain service method takes `Response`, sets headers/status | transport leaked into domain layer; return a value, let `src/http/` own the response |

## Clean decoys

ts-c1 (zod-validated webhook), ts-c2 (awaited metering with retry queue), ts-c3
(discriminated union), ts-c4 (caught, logged, surfaced failures).

Known acceptable nitpicks on decoys: none expected.
