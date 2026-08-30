---
id: ts-c4
language: typescript-javascript
type: clean
---
Task framing: The nightly importer should keep going when a single feed fails.

```diff
--- a/src/import/nightly.ts
+++ b/src/import/nightly.ts
@@ export async function runNightly(feeds: Feed[]): Promise<ImportSummary> {
   const summary = new ImportSummary();
   for (const feed of feeds) {
-    const rows = await fetchFeed(feed);
-    summary.add(feed.id, await upsert(rows));
+    try {
+      const rows = await fetchFeed(feed);
+      summary.add(feed.id, await upsert(rows));
+    } catch (err) {
+      logger.error("feed import failed", { feed: feed.id, err });
+      summary.markFailed(feed.id, err);
+    }
   }
   return summary;
 }
```
Note: `ImportSummary.markFailed` surfaces failed feeds in the ops dashboard and pages when >20% fail.
