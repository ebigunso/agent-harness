# ag-7 grading key

Author-only; exclude from reviewer input. A full hit names mechanism/location and required repair. Secondary overlaps are admitted by the frozen primary-mapping protocol.

| ID | Primary check | Planted defect | A hit must state |
|---|---|---|---|
| ag-7-01 | “Observability supports diagnosis without exposing sensitive internals.” | Java successful-login event logs full credential DTO including password and bearer token. | Name credentials at telemetry site and require safe allowlist/redaction preserving useful event context. |
| ag-7-02 | “Meaningful signals exist to understand critical behavior and failures at boundaries.” | Go boundary wraps every downstream failure as 'request failed' and drops request/operation context; no trace IDs are propagated across the changed fan-out. | Name lost operation/correlation context; preserve safe correlation and actionable failure category at the fan-out boundary. |
| ag-7-03 | “Overly noisy instrumentation that hides actionable indicators.” | Python poller emits full DEBUG payload every 10 ms on the same sink as rare fatal job outcomes, flooding retention and burying actionable errors. | Identify high-frequency payload noise obscuring outcomes; sample/limit routine traffic and retain required failure signals. |
| ag-7-04 | “Logging sensitive payloads as a convenience.” | C# HTTP middleware logs all Authorization and Cookie headers on successful requests without redaction. | Name credential/session headers and replace wholesale capture with safe field allowlist/redaction. |
| ag-7-05 | “Review confirms key boundary events and failures are inspectable.” | Rust queue worker discards the result of background task and emits only 'spawned' counter, so crashes never appear as failed work. | Name launch-only signal gap; expose completion/failure for queued work, including safe job correlation. |
| ag-7-06 | “Plan identifies what success/failure signals are needed for changed flows.” | Ruby batch importer reports only accepted-row count; rejected rows are silently omitted from outcome telemetry despite new partial-success behavior. | Make rejected/failed outcomes inspectable with safe location/count information, not just accepted count. |
| ag-7-07 | “Meaningful signals exist to understand critical behavior and failures at boundaries.” | TypeScript frontend and backend generate unrelated trace IDs at a new gateway hop and neither records the mapping; one failing request cannot be followed through the boundary. | Name broken correlation across gateway; propagate or explicitly link safe trace/request identity. |
| ag-7-08 | “Silent failure paths with no diagnosable signal.” | Java retry loop logs every successful connect attempt but suppresses the final exhausted outcome, leaving operators seeing success while request fails. | Emit an actionable final exhaustion signal with relevant cause/attempt context instead of only intermediate connects. |
| ag-7-09 | “Sensitive data exposure risk in logs/telemetry is assessed.” | Kotlin mobile crash logger serializes full user profile including precise home address and private recovery answers for convenience. | Identify unnecessary sensitive fields and require assessment plus minimized/redacted diagnostic payload. |
| ag-7-10 | “Review confirms key boundary events and failures are inspectable.” | PHP service changed to asynchronous telemetry buffer but drops records on overflow with no loss counter or signal; incident bursts erase every failure indication. | Name unobservable telemetry loss on overflow; preserve critical signals and expose bounded dropped-event accounting. |
| ag-7-11 | “Overly noisy instrumentation that hides actionable indicators.” | C++ worker adds per-item INFO stack traces for routine successful allocations, exhausting log quota before boundary errors can be retained. | Identify noisy success stacks causing loss of useful boundary evidence; reduce/scope routine instrumentation while keeping actionable failures. |
| ag-7-12 | “Observability supports diagnosis without exposing sensitive internals.” | Scala database adapter logs SQL plus raw bound password-reset tokens on query failure. | Name secret bind values in failure logging; retain query/error category and safe correlation without sensitive parameter values. |

## Clean decoys

No blocking target defect. Listed nitpicks are neutral only when optional; unnecessary blocking/rework requests are false positives.

| ID | Correct behavior | Known acceptable optional nitpick |
|---|---|---|
| ag-7-c1 | Java login events include correlation/event IDs without credential fields. | Different log library. |
| ag-7-c2 | Go failure signals include category/duration with bounded labels. | Full request-body capture. |
| ag-7-c3 | Python success/failure counters and trace IDs expose changed workflow. | Per-item debug logs. |
| ag-7-c4 | TypeScript noisy polling telemetry is sampled while key outcomes/errors remain inspectable. | Unsampled debug traffic. |
