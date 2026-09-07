---
id: cp-9-c1
section: cp-9
type: clean
---
Task framing: Preserve typed timeout context when catalog fetch fails.

```diff
--- a/catalog/fetch.go
+++ b/catalog/fetch.go
@@ -1,3 +1,19 @@
+type FetchFailure struct {
+    Operation string
+    Timeout bool
+    Cause error
+}
+func (e *FetchFailure) Error() string { return e.Operation + " failed" }
+func (e *FetchFailure) Unwrap() error { return e.Cause }
+
 func Fetch(ctx context.Context, store Store) ([]Item, error) {
-    return store.Fetch(ctx)
+    items, err := store.Fetch(ctx)
+    if err != nil {
+        return nil, &FetchFailure{
+            Operation: "fetch catalog",
+            Timeout: errors.Is(err, context.DeadlineExceeded),
+            Cause: err,
+        }
+    }
+    return items, nil
 }
```
Commit message: "wrap catalog failures with operation and cause"

Reviewer notes: Existing imports include context and errors. Public message contains no request, credentials or raw database text. Internal callers can inspect Timeout and errors.Is/As through Unwrap; HTTP maps the typed failure to 503. Store errors are sanitized at their source. Success remains unchanged.
