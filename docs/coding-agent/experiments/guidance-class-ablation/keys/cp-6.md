# cp-6 grading key

Author-only; exclude from review input. A full hit names the mechanism/location and repair direction. Secondary overlap is permitted by the frozen primary-mapping protocol.

| ID | Primary check | Planted defect | A hit must state |
|---|---|---|---|
| cp-6-01 | “Avoid silent field loss, implicit coercions, or shape drift.” | Java emits timeoutSeconds; TypeScript adapter passes that number directly to a millisecond timer. | Name the adapter unit mismatch and explicitly convert or align unit-bearing contracts. |
| cp-6-02 | “Avoid silent field loss, implicit coercions, or shape drift.” | Python service response includes taxAmount but hand-written JavaScript mapper drops it, causing downstream total display to exclude tax. | Identify mapper's dropped tax field and preserve it with consistent semantics in client model. |
| cp-6-03 | “Do upstream/downstream boundaries agree on schema and semantics?” | Go JSON API emits int64 IDs above 2^53; TypeScript parses them as Number and merges distinct IDs after precision loss. | Name numeric precision mismatch across wire/client and adopt shared lossless ID representation. |
| cp-6-04 | “Avoid silent field loss, implicit coercions, or shape drift.” | Java protobuf producer treats absent discount as unknown but C# adapter coerces it to numeric zero, changing unknown into no discount. | Preserve absence versus zero through adapter using the contract's optional representation. |
| cp-6-05 | “Is contract drift prevented or merely tolerated?” | Rust backend enum gains PendingReview; generated frontend schema is not regenerated and default mapper silently turns it into Approved. | Name missing variant/schema update and unsafe fallback; synchronize schemas/consumers and handle variant deliberately. |
| cp-6-06 | “Keep data models, service contracts, and adapters aligned.” | Rails serializer changes amount from cents to decimal major units but persisted audit consumer still multiplies by 0.01. | Name unit drift at audit adapter and migrate representation/consumers together. |
| cp-6-07 | “Do upstream/downstream boundaries agree on schema and semantics?” | C# REST producer emits createdAt without UTC offset while Python consumer treats naive strings as local time; documented contract promises UTC instant. | Require explicit UTC/offset-preserving serialization and aligned parsing. |
| cp-6-08 | “Avoid silent field loss, implicit coercions, or shape drift.” | TypeScript API replaces items array with a scalar for singleton results; Kotlin decoder still declares List<Item>. | Name cardinality-dependent wire shape and keep array framing or deliberately migrate both ends. |
| cp-6-09 | “Avoid silent field loss, implicit coercions, or shape drift.” | PHP adapter interprets response success='false' by truthiness as true, while upstream explicitly encodes textual boolean. | Name textual boolean coercion at adapter and parse declared values or align producer to real boolean schema. |
| cp-6-10 | “Version and migrate interfaces deliberately when needed.” | Go persisted document field customer is renamed client; Java reader still loads existing stored documents only through customer without migration path for new writes. | Name persisted reader/writer drift and define synchronized versioned migration/reader behavior. |
| cp-6-11 | “Keep data models, service contracts, and adapters aligned.” | Python gRPC adapter converts every error category into HTTP 200 with null, although TypeScript consumer differentiates not-found and unavailable statuses. | Preserve specified failure categories/status semantics through the adapter. |
| cp-6-12 | “Do upstream/downstream boundaries agree on schema and semantics?” | Java pagination contract defines cursor as opaque string, but React component parses it as page number and increments it. | Name opaque-cursor violation and pass server-provided cursor without numeric interpretation. |

## Clean decoys

No blocking target defect. Nitpicks are neutral only when optional; unnecessary blocking/rework requests are false positives.

| ID | Intended correct behavior | Known acceptable optional nitpick |
|---|---|---|
| cp-6-c1 | Java/TypeScript explicit seconds-to-ms adapter has a unit test. | Alternative naming. |
| cp-6-c2 | Python maps all required protobuf fields with round-trip evidence. | Automatic mapper library. |
| cp-6-c3 | C# additive optional field is ignored by a documented tolerant consumer. | Using that optional field now. |
| cp-6-c4 | Rust rename migrates persisted data and all named consumers together. | A shim for nonexistent callers. |
