# ag-5 grading key

Author-only; exclude from reviewer input. A full hit names mechanism/location and required repair. Secondary overlaps are admitted by the frozen primary-mapping protocol.

| ID | Primary check | Planted defect | A hit must state |
|---|---|---|---|
| ag-5-01 | “Invariants are protected at authoritative boundaries.” | Rails admin update bypasses inventory guard present only in normal controller. | Name optional-path enforcement; restore shared authoritative mutation guard. |
| ag-5-02 | “Concurrent or repeated execution behavior is considered where relevant.” | Java booking service checks available seats then inserts reservation outside a transaction, allowing two concurrent calls to claim final seat. | Name check/write race and require authoritative atomic capacity enforcement with concurrent-case evidence. |
| ag-5-03 | “State transitions that allow invalid intermediate states.” | Go account deletion marks row deleted before cancelling its recurring jobs; cancellation failure leaves deleted account with active billing work. | Name invalid deleted-but-billable intermediate state and require a consistent transactional/staged lifecycle transition. |
| ag-5-04 | “For classification or attribution features, derive the full truth table before selecting the data model.” | Python classifier stores exclusive owner A or B even though task truth table permits both owners or neither; code arbitrarily picks A when both signals are true. | Enumerate neither/A-only/B-only/both, and choose representation preserving valid attribution combinations rather than arbitrary priority. |
| ag-5-05 | “Conflicting write paths without ownership clarity.” | TypeScript API and batch importer each update customer balance with different rounding rules, with no authoritative writer or invariant boundary. | Name divergent write ownership and centralize consistent balance transition/enforcement. |
| ag-5-06 | “Concurrent or repeated execution behavior is considered where relevant.” | C# event consumer applies an increment each time a delivery arrives and has no dedupe despite documented at-least-once transport. | Name replay-induced double increment; enforce idempotent event application at authoritative state boundary. |
| ag-5-07 | “State transitions that allow invalid intermediate states.” | Ruby object is persisted as Approved before required approver identity is attached by a second save, exposing invalid state to observers. | Save approval status and required identity atomically or model an explicit non-approved pending transition. |
| ag-5-08 | “Data ownership, lifecycle, and state transitions are consistent and enforceable.” | Rust removal path frees a shared resource while owner registry still advertises it; cleanup failure prevents registry update. | Name registry/resource lifecycle inconsistency and order/coordinate transition so advertised ownership remains valid. |
| ag-5-09 | “Conflicting write paths without ownership clarity.” | PHP admin adjustment directly writes stored total while regular order update recomputes total from lines; two authoritative-looking writers can overwrite each other. | Define authoritative total derivation/write owner and make admin adjustment part of that consistent model. |
| ag-5-10 | “For classification or attribution features, derive the full truth table before selecting the data model.” | Kotlin classifier data model uses Boolean isInternal although inputs can be trusted-internal, trusted-external, unknown, or conflicting, and mapping silently collapses latter two to external. | Name lost unknown/conflict states; derive complete evidence-to-classification table before choosing representation. |
| ag-5-11 | “Review verifies invariant checks remain at reliable enforcement points.” | C++ queue moves a job to Completed before durable result write, so crash/retry sees completed job with no retrievable result. | Protect completed-implies-durable-result at transition boundary with atomic/staged publication. |
| ag-5-12 | “Plan identifies impacted invariants and lifecycle transitions.” | Scala expiry cleanup deletes session owner record while child capabilities remain valid without checking owner, contrary to defined revocation lifecycle. | Identify ownership deletion/revocation invariant and update capability validity/cleanup in the same lifecycle design. |

## Clean decoys

No blocking target defect. Listed nitpicks are neutral only when optional; unnecessary blocking/rework requests are false positives.

| ID | Correct behavior | Known acceptable optional nitpick |
|---|---|---|
| ag-5-c1 | Rails shared model/transaction enforces invariant for admin and normal writes. | More UI checks. |
| ag-5-c2 | Go explicit transition table rejects invalid moves atomically. | FSM dependency. |
| ag-5-c3 | Java classification truth table includes mixed/unknown cases before data model. | Another diagram. |
| ag-5-c4 | Python event application has one writer and concurrent duplicate evidence. | Second lock layer. |
