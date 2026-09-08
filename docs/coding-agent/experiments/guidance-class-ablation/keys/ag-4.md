# ag-4 grading key

Author-only; exclude from reviewer input. A full hit names mechanism/location and required repair. Secondary overlaps are admitted by the frozen primary-mapping protocol.

| ID | Primary check | Planted defect | A hit must state |
|---|---|---|---|
| ag-4-01 | “Review verifies contract updates are synchronized across producers/consumers.” | Python producer renames user_id to account_id while named TypeScript consumer still reads user_id. | Name field mismatch and synchronize named consumer and migration. |
| ag-4-02 | “Returning ambiguous success/failure signals.” | Go RPC changes successful empty collection to nil and uses same nil for transport failure; named caller treats both as no work. | Distinguish legitimate empty result from failed RPC with explicit modeled failure. |
| ag-4-03 | “Implicit contracts communicated only by call-site assumptions.” | Java inventory adapter assumes caller passes UTC timestamps, but public input type accepts any LocalDateTime and no docs/validation encode that assumption. | Make timestamp semantics explicit in input representation/conversion rather than rely on one caller. |
| ag-4-04 | “Breaking contract changes shipped without migration or compatibility notes.” | Python package changes return from tuple to dict while known CLI and service callers still unpack positional fields; no migration note exists. | Identify changed return contract and migrate documented callers with explicit impact, not silent shape change. |
| ag-4-05 | “Boundaries between components are explicit, minimal, and stable.” | TypeScript service adds untyped options bag used to pass internal database connection and browser UI object across boundary for one query. | Name leaking unrelated internal dependencies; define minimal explicit query input/result at boundary. |
| ag-4-06 | “Failure modes are explicit and not silently swallowed.” | C# API returns HTTP 204 after queue rejects enqueue, erasing failure even though client contract treats 204 as accepted. | Propagate/model enqueue rejection rather than report accepted work. |
| ag-4-07 | “Inputs, outputs, and failure semantics are intentionally modeled.” | Rust adapter assumes byte offsets while downstream interface documents Unicode scalar indices; tests cover ASCII only. | State index unit at interface and translate/align explicitly, including non-ASCII evidence. |
| ag-4-08 | “Plan states contract-impact scope (none/additive/breaking).” | Ruby service adds mandatory field to its response struct but notes classify impact as none and serializer/client schema remain unchanged. | Name incorrect impact declaration and update producer/consumer contract with correct additive/breaking rationale. |
| ag-4-09 | “Review verifies contract updates are synchronized across producers/consumers.” | Kotlin network result exposes a vendor-specific exception type to all callers while declared app contract lists stable domain failure categories. | Translate vendor exceptions to declared categories or deliberately synchronize contract/callers. |
| ag-4-10 | “Returning ambiguous success/failure signals.” | PHP repository returns false both when record is absent and when update was rejected; application cannot choose retry versus create. | Model absence and rejection distinctly so caller behavior is actionable. |
| ag-4-11 | “Inputs, outputs, and failure semantics are intentionally modeled.” | C++ public parser documents caller-owned output but new code caches pointer and reads it after return with no ownership/lifetime change in interface. | Name unmodeled lifetime assumption and retain/copy with an explicit ownership contract rather than hidden borrowed retention. |
| ag-4-12 | “Review verifies contract updates are synchronized across producers/consumers.” | Scala service endpoint changes documented sort stability as part of storage refactor, but downstream pagination still relies on ties retaining prior order. | Identify stability contract drift and preserve ordering or migrate pagination contract and consumers deliberately. |

## Clean decoys

No blocking target defect. Listed nitpicks are neutral only when optional; unnecessary blocking/rework requests are false positives.

| ID | Correct behavior | Known acceptable optional nitpick |
|---|---|---|
| ag-4-c1 | Python/TypeScript rename updates both ends and migration notes. | Legacy alias for migrated internal callers. |
| ag-4-c2 | Go typed success/error outcomes are exhaustively handled. | Error library. |
| ag-4-c3 | Java additive field preserves documented reader tolerance and states scope. | Automatic major-version bump. |
| ag-4-c4 | Rust explicit minimal input/output structs avoid call-site assumptions. | More generic contract. |
