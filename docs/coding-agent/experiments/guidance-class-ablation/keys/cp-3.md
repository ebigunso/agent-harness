# cp-3 grading key

Author-only; exclude from review input. A full hit names the mechanism/location and repair direction. Secondary overlap is permitted by the frozen primary-mapping protocol.

| ID | Primary check | Planted defect | A hit must state |
|---|---|---|---|
| cp-3-01 | “Is the diff focused on one clear goal?” | Go authentication fix also replaces an unrelated metrics dependency and rewrites its imports. | Name unrelated metrics replacement and split it for independent revert. |
| cp-3-02 | “Is the diff focused on one clear goal?” | Python CLI error-message task also changes scheduler interval from 60 to 5 seconds without a shared requirement. | Name unrelated scheduler behavior and split/remove it from message change. |
| cp-3-03 | “Avoid coupling unrelated refactors with functional changes.” | Java payment endpoint diff mass-reformats unrelated ORM entities despite an urgent independent endpoint rollback requirement. | Separate incidental formatting/refactor so functional review and rollback stay focused. |
| cp-3-04 | “Can this change be safely reverted without collateral edits?” | Rust parser fix and unrelated module rename share one commit; reverting parser also undoes renames already consumed by another change. | Name coupled parser rollback/module migration and separate independent changes. |
| cp-3-05 | “Group related edits into a single coherent unit.” | TypeScript CSS spacing diff changes analytics consent default in settings under a cleanup label. | Name unrelated consent behavior; isolate it with explicit task rationale. |
| cp-3-06 | “Make rollback straightforward by limiting blast radius.” | Go one-line TTL fix bundles complete logging-backend replacement; rollback instructions undo both. | Split unrelated logging replacement so TTL behavior can be reverted alone. |
| cp-3-07 | “Avoid coupling unrelated refactors with functional changes.” | C# obsolete invoice-field removal also migrates auth storage because dependency injection file was already open. | Identify independent auth migration and split it. |
| cp-3-08 | “Can this change be safely reverted without collateral edits?” | Ruby reversible data backfill shares migration with unrelated irreversible column drops; rollback cannot restore those columns. | Separate destructive drops and their decision from the reversible backfill. |
| cp-3-09 | “Is the diff focused on one clear goal?” | PHP paginator fix upgrades unrelated monorepo admin UI packages by major versions with separate release requirements. | Limit upgrades to actual paginator dependencies or move unrelated upgrades to a separate change. |
| cp-3-10 | “Is the diff focused on one clear goal?” | Kotlin one-screen empty-state fix migrates all routes to a new router although the fix requires no route change. | Separate navigation migration from empty-state repair. |
| cp-3-11 | “Is the diff focused on one clear goal?” | C++ parser-option patch deletes benchmarks and introduces SIMD in an unrelated compressor in the same commit. | Identify benchmark deletion/compressor optimization as independent objectives and split them. |
| cp-3-12 | “Avoid coupling unrelated refactors with functional changes.” | Django import-exception fix also changes migrations and locale files for an unrelated currency feature. | Separate currency schema/UI scope from the import fix. |

## Clean decoys

No blocking target defect. Nitpicks are neutral only when optional; unnecessary blocking/rework requests are false positives.

| ID | Intended correct behavior | Known acceptable optional nitpick |
|---|---|---|
| cp-3-c1 | Go atomic field/caller changes fix one auth requirement. | Fewer files. |
| cp-3-c2 | Python schema migration and matching rollback form one bounded unit. | Splitting an atomic unit. |
| cp-3-c3 | Java separate preceding refactor commit has unchanged behavior and independent revert evidence. | Commit-title wording. |
| cp-3-c4 | TypeScript producer/adapter/tests all change for one documented internal API rename. | Reducing mechanical line count. |
