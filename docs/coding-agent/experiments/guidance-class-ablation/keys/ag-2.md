# ag-2 grading key

Author-only; exclude from reviewer input. A full hit names mechanism/location and required repair. Secondary overlaps are admitted by the frozen primary-mapping protocol.

| ID | Primary check | Planted defect | A hit must state |
|---|---|---|---|
| ag-2-01 | “Core behavior does not depend directly on volatile delivery or storage details.” | Go domain Price() imports a cloud-vendor client despite an existing quote port. | Name domain-to-vendor dependency and use stable quote seam with outer adapter. |
| ag-2-02 | “Domain logic directly calling framework, transport, or vendor clients.” | Java domain Order imports Spring HttpServletRequest to read tenant instead of receiving a stable tenant value. | Name domain-to-servlet coupling and pass a domain tenant through outer HTTP adapter. |
| ag-2-03 | “Core behavior does not depend directly on volatile delivery or storage details.” | Python domain pricing imports requests and contacts a vendor endpoint directly despite existing QuoteProvider seam. | Move vendor transport into outer provider adapter and depend on stable inward seam. |
| ag-2-04 | “Dependencies point from outer layers toward stable inner abstractions.” | TypeScript domain model imports PrismaClient and database generated types, so schema/client regeneration breaks core calculation compilation. | Name storage-generated type dependency from core and translate through an outer persistence adapter. |
| ag-2-05 | “Review verifies new imports/calls do not invert boundaries.” | Rust application core imports axum response/status types in rule outcomes rather than its existing domain error enum. | Keep core outcome/error transport-independent; HTTP layer translates domain errors to axum response. |
| ag-2-06 | “Feature code bypassing interfaces to reach lower-level internals.” | C# one feature accesses SqlRepository.InternalConnection directly instead of the existing public query interface. | Name bypass of repository seam and expose/use the needed operation through the owned interface. |
| ag-2-07 | “Core behavior does not depend directly on volatile delivery or storage details.” | Kotlin domain imports Android Context to access settings; command-line reuse now needs Android runtime for a pure rule. | Pass stable settings values/port into domain from Android outer layer. |
| ag-2-08 | “Circular dependencies between modules.” | Go cache package imports service for its key policy and service imports cache for access, creating a compile-time cycle. | Identify both dependency edges and move shared stable key policy/port to an inward owner without cycle. |
| ag-2-09 | “Abstraction seams are explicit where external systems are involved.” | Ruby application billing depends on Stripe-specific response objects all the way through its policy methods despite an existing payment-result abstraction. | Translate vendor result at integration boundary and use stable payment result inside application. |
| ag-2-10 | “Domain logic directly calling framework, transport, or vendor clients.” | PHP domain imports Laravel Facade DB for queries, replacing an injected account source. | Name framework/database dependence and restore inward-facing source seam with outer implementation. |
| ag-2-11 | “Dependencies point from outer layers toward stable inner abstractions.” | C++ inner geometry library imports UI widget to obtain current zoom; reusable geometry now links GUI platform libraries. | Supply stable numeric transform/input from UI rather than make geometry depend on widget. |
| ag-2-12 | “Feature code bypassing interfaces to reach lower-level internals.” | Scala orchestration bypasses VendorGateway and reflects into SDK private retry client because the needed operation is not yet exposed. | Name private-vendor bypass; extend owned gateway operation/adapter rather than couple feature to SDK internals. |

## Clean decoys

No blocking target defect. Listed nitpicks are neutral only when optional; unnecessary blocking/rework requests are false positives.

| ID | Correct behavior | Known acceptable optional nitpick |
|---|---|---|
| ag-2-c1 | Go domain accepts existing quote port implemented outside. | Extra adapter layer. |
| ag-2-c2 | Java domain values become HTTP responses only in controller. | DTO library. |
| ag-2-c3 | TypeScript composition root wires storage through application interface. | DI container. |
| ag-2-c4 | Rust domain crate and outer adapters form explicit acyclic graph. | A crate per file. |
