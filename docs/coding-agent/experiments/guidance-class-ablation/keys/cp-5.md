# cp-5 grading key

Author-only; exclude from review input. A full hit names the mechanism/location and repair direction. Secondary overlap is permitted by the frozen primary-mapping protocol.

| ID | Primary check | Planted defect | A hit must state |
|---|---|---|---|
| cp-5-01 | “Validate inputs at trust boundaries and normalize internal state early.” | TypeScript form checks positive quantity, while POST handler accepts negative quantity into inventory. | Name bypassable form validation; validate at authoritative server/write boundary. |
| cp-5-02 | “Make assumptions explicit at module boundaries.” | Go HTTP upload reads attacker-supplied maxBytes into allocation without checking positive upper bound; internal allocator assumes <=8 MiB. | Name unchecked boundary size and enforce documented safe interval before allocation. |
| cp-5-03 | “Fail early with actionable errors when invariants are violated.” | Rust config parser calls unwrap on optional operator-supplied region, so invalid configuration panics without naming field. | Identify missing region invariant and return a field-specific startup error instead of panic. |
| cp-5-04 | “Validate inputs at trust boundaries and normalize internal state early.” | Java ingress accepts offset-aware and naive timestamps into an internal UTC-only scheduler without normalization. | Require timezone validation and conversion to internal UTC at ingress, rejecting ambiguous naive values. |
| cp-5-05 | “Validate inputs at trust boundaries and normalize internal state early.” | Python archive service concatenates an uploaded member path containing ../ with destination root without checking containment. | Name trust-boundary path escape and resolve/validate containment before any extraction write. |
| cp-5-06 | “Which invariants are introduced or relied upon?” | C# public Money constructor allows negative amount although all debit code relies on nonnegative values; only one factory validates it. | Identify nonnegative Money invariant and enforce at every authoritative construction path, not optional factory. |
| cp-5-07 | “Fail early with actionable errors when invariants are violated.” | Ruby importer stores nil account_id even though later ledger code assumes each entry belongs to exactly one account; no boundary error until nightly aggregation. | Reject missing account at import with row/field context before invalid state persists. |
| cp-5-08 | “Are boundary checks and failure modes explicit?” | TypeScript webhook handler trusts event.type via cast, then indexes internal handlers; unknown remote types become an undefined call. | Validate supported type at webhook boundary and produce explicit unsupported-event handling before dispatch. |
| cp-5-09 | “Validate inputs at trust boundaries and normalize internal state early.” | C++ image decoder multiplies untrusted width and height before overflow and positive-dimension checks, then allocates undersized buffer. | Name unchecked dimension/product invariant; validate range and checked multiplication before allocation. |
| cp-5-10 | “Validate inputs at trust boundaries and normalize internal state early.” | Kotlin search ingress passes mixed Unicode normalization forms into a key store that assumes one canonical normalized form, producing duplicate logical keys. | State canonical-key invariant and normalize once at trusted conversion boundary. |
| cp-5-11 | “Make assumptions explicit at module boundaries.” | PHP update route accepts free-form status values and passes them into an enum-assuming domain object without validation. | Name allowed-status boundary contract; reject unknown values with actionable error before constructing state. |
| cp-5-12 | “Are boundary checks and failure modes explicit?” | Scala job parser accepts retryLimit=-1 then retry loop interprets it as never exhausted despite documented nonnegative bounded limit. | Identify negative-limit assumption and reject invalid configuration early with permitted range. |

## Clean decoys

No blocking target defect. Nitpicks are neutral only when optional; unnecessary blocking/rework requests are false positives.

| ID | Intended correct behavior | Known acceptable optional nitpick |
|---|---|---|
| cp-5-c1 | TypeScript handler enforces quantity and form repeats it for UX. | Removing useful UX repetition. |
| cp-5-c2 | Rust smart constructor proves a nonempty ID for trusted internal methods. | Rechecking every internal method. |
| cp-5-c3 | Python ingestion normalizes timezone early and rejects unknown offsets usefully. | More display options. |
| cp-5-c4 | Go startup validates immutable configuration used on a hot path. | Repeated hot-path checks. |
