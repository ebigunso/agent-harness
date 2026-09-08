---
id: cp-9-c4
section: cp-9
type: clean
---
Task framing: Retry transient read failures at most three times while preserving permanent and final failures.

```diff
--- a/src/CatalogClient.java
+++ b/src/CatalogClient.java
@@ -1,3 +1,11 @@
 Response fetch(Client client) throws ClientFailure {
-    return client.read();
+    for (int attempt = 1; ; attempt++) {
+        try {
+            return client.read();
+        } catch (ClientFailure failure) {
+            if (!failure.retryable() || attempt == 3) {
+                throw failure;
+            }
+        }
+    }
 }
```
Commit message: "bound catalog retries"

Reviewer notes: Method belongs to an existing class. Client.read is a read-only local IPC call with an enforced 100 ms timeout. ClientFailure.retryable is false for validation/auth errors. Three immediate attempts (no delay) are explicitly accepted for this local use. The exact final exception including cause is rethrown; a permanent failure stops on the first attempt. No framework is required.
