# Answer key — Go fixtures

Grading rule: a finding counts as a **hit** only if it identifies the planted mechanism at
the planted location. Naming the general area without the mechanism is a **partial** (0.5).
Findings on clean fixtures count toward the false-positive rate unless they identify a real
defect the authors missed (log those for key revision).

## Planted

| id | bullet | planted defect | a hit must state |
|---|---|---|---|
| go-01 | G12 | retry decision via `strings.Contains(err.Error(), ...)` | matching on error strings is fragile; use a typed/sentinel error with `errors.Is`/`errors.As` |
| go-02 | G2 | wrapping with `%v` instead of `%w` | callers lose `errors.Is`/`As` classification because the cause chain is broken |
| go-03 | G7/G14 | audit goroutine polls `Ready()` forever if audit never becomes ready | goroutine has no termination path (no ctx, no timeout, no bound); leaks per call |
| go-04 | G15 | unsynchronized `map` read/write on shared `Resolver.cache` | concurrent map access from handlers is a data race / runtime fatal; needs sync |
| go-05 | G13 | `MustValidate` + `recover` replacing an error return | panic/recover used as routine control flow for an expected failure mode |
| go-06 | G4 | `context.Background()` replacing the request ctx in the fetch loop | breaks cancellation/deadline propagation; export can never be cancelled |
| go-07 | G11 | single-implementation, same-package `Formatter` interface | speculative interface; define interfaces at consumer boundaries or use a function |
| go-08 | G6 | promo pricing rules inline in the HTTP handler | domain/pricing logic embedded in transport; belongs in the billing domain package |

## Clean decoys

go-c1 (correct `%w` wrap), go-c2 (best-effort audit publish is a stated product decision),
go-c3 (correctly locked cache), go-c4 (plain function, no interface).

Known acceptable nitpicks on decoys (count as neither hit nor FP): go-c3 check-then-act
between RUnlock and Lock causing a duplicate resolve (benign, idempotent).

## Amendment (added with protocol-v2, before any Stage 1 cell ran)

| id | bullet | planted defect | a hit must state |
|---|---|---|---|
| go-09 | G5/G16 | pricing logic dropped into `internal/util` dumping ground, creating a util<->orders import cycle | domain logic belongs in a cohesive package (billing/orders); util grab-bags and the dependency cycle are the defect — reusability does not justify the placement |
