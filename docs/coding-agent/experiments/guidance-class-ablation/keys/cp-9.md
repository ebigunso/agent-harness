# Answer key — cp-9

Hit requires the named mechanism/location and fix direction; partial names the area without the mechanism. Clean-fixture rework findings are false positives unless a real authoring error is confirmed across arms.

## Planted

| id | primary check | planted defect | a hit must state |
|---|---|---|---|
| cp-9-01 | “Avoid swallowing failures or converting them into ambiguous states.” | Go database timeout becomes a successful empty account list. | Name timeout-to-success conversion and require useful failure or explicitly modeled bounded stale result. |
| cp-9-02 | “Avoid swallowing failures or converting them into ambiguous states.” | Python import loop catches Exception and continues without recording failed row or count, presenting partial import as complete. | Name swallowed row failures and expose failed rows/count or stop with actionable context. |
| cp-9-03 | “Do fallbacks preserve safety and correctness expectations?” | Java payment client falls back to marking charge paid after gateway timeout, despite unknown remote result. | Name unknown payment outcome misrepresented as paid; keep pending/unknown or reconcile through safe idempotent contract. |
| cp-9-04 | “Design fallback behavior to be safe, observable, and bounded.” | Node inventory client retries rejected promise recursively with no delay/budget, continuing forever on permanent validation error. | Name unbounded retry and permanent-error loop; classify errors and bound attempts/time with visible final failure. |
| cp-9-05 | “Handle errors at appropriate boundaries with useful context.” | Rust worker replaces all parse/storage errors with string 'job failed' without job ID, operation, or cause even though boundary has that context. | Preserve useful operation/job context and cause at worker boundary instead of erasing diagnosis. |
| cp-9-06 | “Design fallback behavior to be safe, observable, and bounded.” | C# optional cache fallback has no age limit and serves stale authorization decisions after permission revocation. | Name unsafe unbounded-age authorization fallback; fail safely or use explicitly valid bounded authorization semantics. |
| cp-9-07 | “Are failure paths visible and diagnosable?” | Go background goroutine returns an error to a discarded channel; supervisor reports job success when goroutine launch succeeds. | Name unobserved asynchronous failure and require completion/error propagation to supervisor. |
| cp-9-08 | “Avoid swallowing failures or converting them into ambiguous states.” | Ruby rescue returns nil for both genuine not-found and database outage; caller interprets nil as permission to create another record. | Distinguish not-found from unavailable; do not initiate creation based on outage masquerading as absence. |
| cp-9-09 | “Do fallbacks preserve safety and correctness expectations?” | PHP file export writes directly to destination, catches mid-write disk error, and leaves truncated file advertised as ready. | Name partial file published as success; use safe atomic completion/error signaling and preserve prior valid artifact where applicable. |
| cp-9-10 | “Avoid swallowing failures or converting them into ambiguous states.” | Kotlin HTTP boundary logs timeout at debug then returns success:true with missing payload, indistinguishable from legitimate empty success. | Surface timeout as explicit failed/unknown result with actionable context rather than ambiguous success. |
| cp-9-11 | “Design fallback behavior to be safe, observable, and bounded.” | C++ service catches a resource-allocation failure and retries in tight loop on the same input, blocking all work indefinitely. | Name endless retry of nonrecovering resource failure; bound/terminate safely with visible cause. |
| cp-9-12 | “Handle errors at appropriate boundaries with useful context.” | Scala optional enrichment failure aborts the whole durable order workflow after payment, despite existing contract allowing an explicitly missing enrichment. | Contain optional enrichment failure at its boundary and return explicit degraded status without undoing unrelated completed core work. |

## Clean decoys

- **cp-9-c1**: Go timeout maps to typed failure with useful context and no secrets. Known acceptable optional nitpick: More verbose logging.
- **cp-9-c2**: Python read-only fallback exposes bounded cache age under an explicit stale-data contract. Known acceptable optional nitpick: Removing an intentional safe fallback.
- **cp-9-c3**: Rust optional thumbnail failure is visible while the core operation succeeds. Known acceptable optional nitpick: Failing the entire operation.
- **cp-9-c4**: Java bounded retries stop on permanent failure and preserve final cause. Known acceptable optional nitpick: New retry framework.
