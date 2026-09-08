# cp-4 grading key

Author-only; exclude from review input. A full hit names the mechanism/location and repair direction. Secondary overlap is permitted by the frozen primary-mapping protocol.

| ID | Primary check | Planted defect | A hit must state |
|---|---|---|---|
| cp-4-01 | “Can a reader understand intent without reconstructing hidden context?” | Java isEligible() secretly mutates singleton discount state read later by price(). | Name the hidden predicate mutation and require explicit discount data flow. |
| cp-4-02 | “Reduce hidden coupling and surprising side effects.” | Python calculate_total() deletes entries from caller-owned list before returning sum; name/signature do not indicate mutation. | Identify concealed list mutation; compute purely or expose an explicitly named mutation contract. |
| cp-4-03 | “Can a reader understand intent without reconstructing hidden context?” | Go findUser() writes subscription tier while every caller treats it as a lookup. | Name subscription mutation hidden in lookup and separate/name the state-changing operation. |
| cp-4-04 | “Reduce hidden coupling and surprising side effects.” | TypeScript config import changes global locale; formatters depend on import order. | Name import-order locale coupling; use explicit startup configuration or locale parameter. |
| cp-4-05 | “Keep functions/components at a single level of abstraction.” | Java validate() interleaves parsing, SQL writes, email delivery, and boolean conversion at the same level. | Name mixed validation/workflow responsibilities; expose named steps and separate validation from effect orchestration. |
| cp-4-06 | “Favor clear names, explicit boundaries, and straightforward control flow.” | Rust helper returns (bool,bool,bool) for retry/reject/quarantine; meaning exists only in a distant comment and caller swaps last two. | Identify unlabeled tuple roles; use a named outcome making local bindings unambiguous. |
| cp-4-07 | “Can a reader understand intent without reconstructing hidden context?” | C# ProcessOrder uses numeric phase 0/1/2, advanced from a logging callback, to select side effects. | Name hidden phase mutation in logging and make workflow states/transitions explicit. |
| cp-4-08 | “Reduce hidden coupling and surprising side effects.” | Ruby query scope reads Thread.current tenant; unrelated presenter resets it, altering later query ownership. | Name presenter-controlled ambient tenant state; use an explicit request tenant boundary. |
| cp-4-09 | “Favor clear names, explicit boundaries, and straightforward control flow.” | PHP checkPermission both answers a predicate and registers a background job through global queue. | Name hidden enqueue effect and separate permission check from explicit job submission. |
| cp-4-10 | “Keep functions/components at a single level of abstraction.” | Kotlin nested takeIf/also/let expression with nonlocal returns interleaves address selection, cart mutation, and payment. | Identify mixed-level effects and implicit exits; use explicit sequential named steps with visible control flow. |
| cp-4-11 | “Reduce hidden coupling and surprising side effects.” | C++ formatting helper increments a shared counter consumed by ID generation; previewing text changes future IDs. | Name formatter/ID coupling; keep formatting pure and allocate IDs explicitly. |
| cp-4-12 | “Can a reader understand intent without reconstructing hidden context?” | Scala getOrElse fallback sends email while computing a value for read-only rendering. | Name fallback notification side effect and separate rendering from explicit notification workflow. |

## Clean decoys

No blocking target defect. Nitpicks are neutral only when optional; unnecessary blocking/rework requests are false positives.

| ID | Intended correct behavior | Known acceptable optional nitpick |
|---|---|---|
| cp-4-c1 | Java pure predicate returns eligibility; a named command applies the discount. | Using a record instead. |
| cp-4-c2 | Python straightforward formatter has one descriptive helper at a consistent abstraction level. | One more extraction. |
| cp-4-c3 | Rust local exhaustive match has no global effects. | Arm ordering. |
| cp-4-c4 | TypeScript callback receives all needed state explicitly and documents invocation order. | Inlining the callback. |
