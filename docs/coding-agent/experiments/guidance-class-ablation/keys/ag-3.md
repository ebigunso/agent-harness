# ag-3 grading key

Author-only; exclude from reviewer input. A full hit names mechanism/location and required repair. Secondary overlaps are admitted by the frozen primary-mapping protocol.

| ID | Primary check | Planted defect | A hit must state |
|---|---|---|---|
| ag-3-01 | “Review confirms no unrelated edits are bundled.” | Python billing fix bundles unrelated auth framework migration without common objective. | Name auth migration as independent and split from billing change. |
| ag-3-02 | “Plan links each touched area to the same architectural objective.” | Java task migrates metrics names but patch also changes password-expiry policy, with no trace to metrics objective. | Identify policy edit without architectural linkage and separate it from metrics migration. |
| ag-3-03 | “Hidden behavior changes inside nominally mechanical diffs.” | TypeScript mechanical import-sort diff changes a feature default from false to true inside a moved object literal. | Name hidden feature-default change and require explicit behavior scope/evidence in a separate or reclassified change. |
| ag-3-04 | “Large “drive-by” edits across modules with weak coupling to the objective.” | Rust storage backend feature also rewrites unrelated CLI parser and removes report columns as drive-by cleanup. | Name unrelated CLI/report edits and remove or split them. |
| ag-3-05 | “Refactor-only changes are separated from behavior changes when risk warrants.” | Go HTTP timeout feature bundles dependency graph refactor without rationale; refactor could ship independently and changes unrelated service lifetimes. | Separate risky lifetime refactor from timeout behavior and validate each objective independently. |
| ag-3-06 | “Cross-cutting updates are deliberate and traceable.” | Python logging key rename spans files but one unrelated database index migration is included merely because tests needed resetting. | Name untraceable index migration and split it or document a real necessary link before inclusion. |
| ag-3-07 | “Mixing feature work, refactors, and incidental cleanup without rationale.” | C# authentication endpoint fix includes widespread UI theming changes and new documentation generator dependency. | Identify separate theming/tooling purposes and isolate from auth fix. |
| ag-3-08 | “Hidden behavior changes inside nominally mechanical diffs.” | Ruby nominally behavior-preserving scope extraction moves a condition after a limit, changing which records can appear. | Name query-order behavior change; restore semantics or explicitly scope and evidence intended change. |
| ag-3-09 | “The change set is cohesive and aligned to one architectural intent.” | Kotlin database driver upgrade additionally renames domain models and changes navigation labels with no compatibility necessity. | Keep driver migration focused; separate unrelated domain/navigation edits. |
| ag-3-10 | “Review confirms no unrelated edits are bundled.” | PHP task fixes one cache key, but patch touches 80 templates to adopt an unrelated style preference without rationale. | Name template churn unrelated to cache key and split it. |
| ag-3-11 | “Hidden behavior changes inside nominally mechanical diffs.” | C++ compiler-warning cleanup changes floating-point rounding mode in shared math initialization, altering numeric behavior under a mechanical label. | Name rounding behavior change and separate/document/validate it instead of hiding in warnings cleanup. |
| ag-3-12 | “Plan links each touched area to the same architectural objective.” | Scala API pagination feature combines independent persistence partition redesign; touched-area notes justify only endpoint files and never partition migration. | Identify partition redesign missing objective linkage; split or supply actual dependency and risk rationale. |

## Clean decoys

No blocking target defect. Listed nitpicks are neutral only when optional; unnecessary blocking/rework requests are false positives.

| ID | Correct behavior | Known acceptable optional nitpick |
|---|---|---|
| ag-3-c1 | Python API/domain/persistence changes all trace to one billing requirement. | Fewer touched layers. |
| ag-3-c2 | Go unrelated cleanup is a different revertible change. | Combining changes. |
| ag-3-c3 | Java mechanical rename preserves conditions/defaults with evidence. | A different name. |
| ag-3-c4 | TypeScript risky refactor is separated from behavior addition with rationale. | Further splitting cohesive edits. |
