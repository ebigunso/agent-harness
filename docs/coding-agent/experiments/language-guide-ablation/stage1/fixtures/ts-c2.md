---
id: ts-c2
language: typescript-javascript
type: clean
---
Task framing: Record a usage metric when a report is generated.

```diff
--- a/src/reports/generate.ts
+++ b/src/reports/generate.ts
@@ export async function generateReport(spec: ReportSpec): Promise<Report> {
   const data = await warehouse.query(spec.query);
   const report = render(spec.template, data);
   await store.save(report);
+  try {
+    await metering.recordUsage({ kind: "report", tenant: spec.tenantId, bytes: report.size });
+  } catch (err) {
+    logger.error("usage metering failed; queued for retry", { tenant: spec.tenantId, err });
+    await meteringRetryQueue.enqueue(spec.tenantId, report.size);
+  }
   return report;
 }
```
