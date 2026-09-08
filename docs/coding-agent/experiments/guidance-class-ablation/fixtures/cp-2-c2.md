---
id: cp-2-c2
section: cp-2
type: clean
---
Task framing: Fix the shared retry policy so maxAttempts includes the first attempt.

```diff
--- a/retry/retry.go
+++ b/retry/retry.go
@@ -1,12 +1,12 @@
 package retry

 func Run(maxAttempts int, operation func() error) error {
     var last error
-    for attempt := 1; attempt < maxAttempts; attempt++ {
+    for attempt := 0; attempt < maxAttempts; attempt++ {
         last = operation()
         if last == nil { return nil }
     }
     return last
 }
 func CLI(operation func() error) error { return Run(3, operation) }
 func Service(operation func() error) error { return Run(3, operation) }
```
Commit message: "honor the configured attempt count"

Reviewer notes: Internal API requires maxAttempts >= 1, validated in both configuration loaders. operation is an idempotent local read and returns only retryable errors; this short bounded policy deliberately needs no delay. Verified: max=1 invokes once and returns its error; max=3 failing operation invokes three times; early success stops immediately. No caller supplies zero or negative budgets.
