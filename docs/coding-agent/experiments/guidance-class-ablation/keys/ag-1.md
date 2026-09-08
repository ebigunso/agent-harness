# ag-1 grading key

Author-only; exclude from reviewer input. A full hit names mechanism/location and required repair. Secondary overlaps are admitted by the frozen primary-mapping protocol.

| ID | Primary check | Planted defect | A hit must state |
|---|---|---|---|
| ag-1-01 | “Business rules remain in domain/application logic, not scattered into presentation or persistence details.” | Java SQL repository selects discount tier instead of returning facts to existing domain pricing policy. | Name pricing-policy leakage into storage and return it to domain/application logic. |
| ag-1-02 | “UI or transport handlers embedding business invariants.” | React checkout component computes loyalty eligibility and final discount from account age, duplicating application policy absent from API and mobile callers. | Name loyalty rule ownership in presentation; keep authoritative eligibility in application/domain used by all callers. |
| ag-1-03 | “Review confirms behavior changes are implemented in the correct layer.” | Go HTTP handler implements full subscription transition table inline while application method simply saves passed status. | Move authoritative transition policy to application/domain; handler should parse input and invoke it. |
| ag-1-04 | “Data access layer deciding domain policy.” | Python SQL repository decides whether account qualifies for refund based on purchase age instead of retrieving facts for refund service. | Name refund eligibility in storage and relocate policy to existing domain/application service. |
| ag-1-05 | ““Utility” modules accumulating unrelated logic as a shortcut.” | C# Utilities class accumulates JWT parsing, invoice tax rules, SMTP dispatch, and CSS color mapping to avoid adding to their existing owners. | Identify unrelated responsibility aggregation; place each concern with its existing owner rather than enlarge catch-all utility. |
| ag-1-06 | “Business rules remain in domain/application logic, not scattered into presentation or persistence details.” | Rust transport decoder both validates protobuf framing and chooses fraud-review policy by customer score. | Keep wire decoding at transport; pass decoded facts to authoritative fraud policy. |
| ag-1-07 | “Each layer/module has a clear responsibility and does not absorb unrelated concerns.” | Ruby ActiveRecord serializer triggers fulfillment on every paid order it renders, so listing endpoint executes business workflow. | Name workflow side effect in serialization and invoke fulfillment explicitly through application use case. |
| ag-1-08 | “Data access layer deciding domain policy.” | PHP cache adapter selects free-shipping threshold per customer segment instead of simply caching application result. | Remove shipping policy from cache adapter and call existing shipping domain policy before cache access. |
| ag-1-09 | “UI or transport handlers embedding business invariants.” | Kotlin Compose screen contains account-closure grace-period and balance policy; background closure worker has no shared owner for same rules. | Name closure invariants in UI and place them in domain/application closure command. |
| ag-1-10 | “No unexplained cross-layer logic movement.” | Java change moves invoice due-date calculation from billing domain into JSON response mapper with no explanation, leaving batch exports with old behavior. | Identify due-date policy migration into presentation and keep a shared domain policy for both consumers. |
| ag-1-11 | “Each layer/module has a clear responsibility and does not absorb unrelated concerns.” | Scala DAO logs audit business events based on application status decisions, even when transaction is later rolled back; event ownership is not part of persistence contract. | Name audit policy/event timing in DAO; application transaction/use-case should own committed business event emission. |
| ag-1-12 | “Review confirms behavior changes are implemented in the correct layer.” | C++ database row converter decides customer suspension when decoding a debt field, so merely loading a record applies domain policy. | Name suspension rule in data mapping and make it an explicit application/domain operation. |

## Clean decoys

No blocking target defect. Listed nitpicks are neutral only when optional; unnecessary blocking/rework requests are false positives.

| ID | Correct behavior | Known acceptable optional nitpick |
|---|---|---|
| ag-1-c1 | Java repository supplies facts to existing pricing policy. | Another repository interface. |
| ag-1-c2 | React renders server policy result and validates input only for UX. | Duplicating domain policy in UI. |
| ag-1-c3 | Python HTTP handler parses transport data then invokes application command. | A handler class. |
| ag-1-c4 | Rust storage translates SQL-specific transient errors without deciding business eligibility. | Moving SQL translation into domain. |
