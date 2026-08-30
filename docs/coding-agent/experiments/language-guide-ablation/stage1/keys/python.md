# Answer key — Python fixtures

Grading rule: hit = planted mechanism at planted location; partial = area without mechanism.
Findings on clean fixtures are false positives unless they expose a real authoring error.

## Planted

| id | bullet | planted defect | a hit must state |
|---|---|---|---|
| py-01 | P11 | `event: MetricEvent` widened to `Any` + `hasattr` probe to silence mypy | type deleted instead of fixed; the real issue (tags optionality) belongs in the type model |
| py-02 | P13 | `except Exception: return Standing.UNKNOWN` in business logic | broad mid-layer handler converts every failure (incl. bugs) into a silent ambiguous state |
| py-03 | P9 | `from err` dropped on re-raise | causal chain lost; hiding internals does not require discarding `__cause__` |
| py-04 | P10 | module-level `load_settings()` + `httpx.Client` construction | import-time side effects (env/config read, socket pool) break test isolation and import order |
| py-05 | P12 | `Shipment` dataclass replaced by a raw dict flowing through layers, mutated in `quote` | unstructured dict crossing layer boundaries, no stable contract, in-place mutation |
| py-06 | P14 | `time.sleep(1.2)` wall-clock test of TTL expiry | nondeterministic timing-dependent test; inject/patch the clock |
| py-07 | P8 | `try` widened over lookup + audit + computation | audit's `InvalidOperation` is misclassified as RateUnavailable; scope must cover only the lookup/parse |
| py-08 | P1 | new public API `reconcile(ledger, statement, tolerance=None)` untyped | public boundary must be annotated; also `tolerance or DEFAULT` mishandles 0 |

## Clean decoys

py-c1 (correct translate-and-chain), py-c2 (fake clock test), py-c3 (typed models across
layers), py-c4 (lazy cached client, no import-time effects).

Known acceptable nitpicks on decoys: py-c4 lru_cache never closes the client (accept, do
not count).
