# ag-6 grading key

Author-only; exclude from reviewer input. A full hit names mechanism/location and required repair. Secondary overlaps are admitted by the frozen primary-mapping protocol.

| ID | Primary check | Planted defect | A hit must state |
|---|---|---|---|
| ag-6-01 | “Timeouts, retries, idempotency, and degradation paths are intentional when integrating external dependencies.” | Node charge client retries timeout forever with a new request ID on each attempt. | Name duplicate-charge risk/unbounded retry; require stable idempotency and bounded attempts/time. |
| ag-6-02 | “Unbounded retries or blocking operations in critical paths.” | Java external recommendation call runs without timeout on checkout thread; slow optional service can stall all checkout requests. | Name unbounded optional dependency wait; apply deadline and deliberate isolated degradation so checkout is bounded. |
| ag-6-03 | “Cascading failure paths without isolation boundaries.” | Go fan-out enrichment shares one blocking worker pool with payment processing; enrichment outage exhausts the pool and stops payments. | Identify shared-resource cascade and isolate/bound optional work so failure stays local. |
| ag-6-04 | “Unbounded retries or blocking operations in critical paths.” | Python retries all HTTP responses including permanent 400 forever; each loop immediately reuses same invalid request. | Classify transient/permanent failures, cap retries/time, and propagate final actionable cause. |
| ag-6-05 | “Timeouts, retries, idempotency, and degradation paths are intentional when integrating external dependencies.” | C# upload timeout restarts a non-idempotent storage create with new object key each attempt, leaking multiple completed uploads. | Name duplicate-create risk on unknown outcome; use stable operation identity/dedupe and bounded reconciliation. |
| ag-6-06 | “Broad exception/error suppression that obscures root causes.” | Ruby critical workflow rescues every vendor exception and continues as if shipment booked, hiding missing fulfillment. | Preserve failure cause and explicit unbooked state; do not pretend critical integration succeeded. |
| ag-6-07 | “Failures are contained to the smallest practical scope.” | TypeScript client cancellation does not propagate to downstream expensive query; abandoned requests continue consuming all available connection slots. | Name orphaned work after cancellation; propagate cancellation/deadline and release scoped resources. |
| ag-6-08 | “Review verifies error propagation and fallback behavior are deliberate.” | Rust service retries each of five nested layers three times independently, multiplying remote attempts far beyond the documented request budget. | Identify retry amplification across layers; centralize/share an overall bounded budget and preserve error propagation. |
| ag-6-09 | “Failures are contained to the smallest practical scope.” | Kotlin per-user sync failure cancels entire tenant batch, though jobs and correctness contracts are independent per user. | Contain failed user job and expose per-user outcome; retain independent work instead of global cancellation. |
| ag-6-10 | “Unbounded retries or blocking operations in critical paths.” | PHP endpoint downloads a partner response with no size/time limit before returning, letting a stalled stream hold critical workers indefinitely. | Bound stream duration/size and define failure cleanup/outcome at partner boundary. |
| ag-6-11 | “Risky operations include containment strategy notes.” | C++ service holds global state mutex while calling optional metrics exporter over network; exporter hang blocks all state updates. | Identify external call under global lock and move/bound export outside critical state path with explicit containment. |
| ag-6-12 | “Plan lists likely failure modes for touched integrations.” | Scala circuit-open fallback launches parallel calls to three same-failure-domain mirrors without overall limit, increasing load during outage. | Name correlated fallback amplification; use deliberate bounded degradation/isolation rather than uncontrolled mirror fan-out. |

## Clean decoys

No blocking target defect. Listed nitpicks are neutral only when optional; unnecessary blocking/rework requests are false positives.

| ID | Correct behavior | Known acceptable optional nitpick |
|---|---|---|
| ag-6-c1 | Node charge client reuses server-supported idempotency key with bounded budget. | Retry dependency. |
| ag-6-c2 | Go optional downstream calls have deadlines and isolated failures. | Service mesh. |
| ag-6-c3 | Java poison message is isolated with visible bounded dead-letter handling. | Process per message. |
| ag-6-c4 | Python noncritical read fallback has bounded age, signal, and explicit correctness contract. | Rejecting all fallback behavior. |
