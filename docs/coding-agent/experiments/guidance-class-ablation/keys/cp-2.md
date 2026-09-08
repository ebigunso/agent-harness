# Answer key — cp-2

Hit requires the named mechanism/location and fix direction; partial names the area without the mechanism. Clean-fixture rework findings are false positives unless a real authoring error is confirmed across arms.

## Planted

| id | primary check | planted defect | a hit must state |
|---|---|---|---|
| cp-2-01 | “Does the change remove the cause or only suppress outcomes?” | Python importer duplicates IDs; a report-only dedupe hides duplicates while the CLI and scheduler still write them. | Name report-only suppression; enforce uniqueness once in shared import/write logic. |
| cp-2-02 | “Strengthen invariants where failures originate.” | Java LedgerService commits debit outside the transfer transaction; REST adds refund-on-error, while scheduled transfers still use the same service. | Name split transfer transaction as origin; make debit/credit atomic in shared service/store rather than add REST-only compensation. |
| cp-2-03 | “Address the source of the issue instead of adding repeated local workarounds.” | React view waits 200 ms before rendering stale responses; shared fetcher still lets an old request overwrite new selection used by sidebar too. | Name response-order race; gate/cancel obsolete responses in shared fetcher rather than delay a view. |
| cp-2-04 | “Does the change remove the cause or only suppress outcomes?” | Python exporter creates a relative folder on FileNotFoundError, although shared path builder drops configured absolute root for CLI and batch exports. | Repair shared destination mapping, not create the accidental relative folder. |
| cp-2-05 | “Strengthen invariants where failures originate.” | Go HTTP handler adds a local mutex around read-max-plus-one invoice IDs; background processes still race in shared allocator. | Name cross-process non-atomic allocation; fix authoritative allocation rather than per-handler locking. |
| cp-2-06 | “Does the change remove the cause or only suppress outcomes?” | Rust reader uses from_utf8_lossy after shared gzip loader skipped decompression; indexer still receives compressed bytes. | Name missing decompression and restore it before both consumers decode; lossy text is symptom suppression. |
| cp-2-07 | “Address the source of the issue instead of adding repeated local workarounds.” | C# controller returns 409 on duplicate-key error while common ID generator reseeds Random identically on each call; queue consumer uses it too. | Name generator reseeding and fix shared generation; controller-only conflict handling leaves collision source. |
| cp-2-08 | “Avoid duplicating fragile logic across modules.” | Ruby three presenters add amount / 100 after shared serializer labels integer cents as dollars; fourth report remains wrong. | Fix serializer unit representation once and remove compensating presenter conversions. |
| cp-2-09 | “Does the change remove the cause or only suppress outcomes?” | C++ preview clamps indices while shared mesh builder emits one extra index with <= loop bound; production renderer still sees bad index. | Name producer off-by-one; repair mesh generation rather than clamp one consumer. |
| cp-2-10 | “Strengthen invariants where failures originate.” | Java nightly sweep deletes duplicate reservations created by read-then-insert booking service; concurrent requests still overbook until sweep. | Enforce atomic capacity/uniqueness in allocation, not delayed repair. |
| cp-2-11 | “Avoid duplicating fragile logic across modules.” | PHP form copies a regex to reject invalid February dates after common validator regression; API/import keep faulty validator. | Repair calendar validation in the common entry point for every caller rather than fork a form check. |
| cp-2-12 | “Does the change remove the cause or only suppress outcomes?” | Kotlin screen restarts the app after logout; shared session cache still retains previous tenant keys used by background sync. | Name tenant-cache lifecycle defect and clear authoritative session-owned entries at logout for foreground and background paths. |

## Clean decoys

- **cp-2-c1**: Python shared parser normalizes CRLF once for both callers, with regression examples. Known acceptable optional nitpick: Extra caller-level tests.
- **cp-2-c2**: Go common retry policy fixes its attempt counter for CLI and service. Known acceptable optional nitpick: Renaming the counter.
- **cp-2-c3**: TypeScript shared URL builder is fixed and its compensating caller code removed. Known acceptable optional nitpick: A different URL helper.
- **cp-2-c4**: Rust scoped upstream workaround has an explicit constraint, owner, expiry, and coverage. Known acceptable optional nitpick: Immediate upstream repair beyond current scope.
