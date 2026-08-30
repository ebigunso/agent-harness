---
id: ts-c3
language: typescript-javascript
type: clean
---
Task framing: Model the result of a document-conversion job for the status endpoint.

```diff
--- /dev/null
+++ b/src/convert/status.ts
@@
+export type ConversionStatus =
+  | { state: "queued" }
+  | { state: "running"; progress: number }
+  | { state: "done"; resultUrl: string }
+  | { state: "failed"; error: string; retryAfter?: number };
+
+export function isRetryable(s: ConversionStatus): boolean {
+  return s.state === "failed" && s.retryAfter !== undefined;
+}
```
