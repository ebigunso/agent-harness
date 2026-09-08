---
id: ag-7-c2
section: ag-7
type: clean
---
Task framing: Record bounded downstream failure metrics.

```diff
--- a/metrics.go
+++ b/metrics.go
@@ -0,0 +1,7 @@
+package metrics
+import ("context"; "errors"; "time")
+func Call(run func()error, observe func(string,time.Duration)) error {
+ start:=time.Now(); err:=run(); category:="success"
+ if errors.Is(err,context.DeadlineExceeded) { category="deadline" } else if err!=nil { category="other" }
+ observe(category,time.Since(start)); return err
+}
```
Commit message: "record bounded downstream failure metrics"

Reviewer notes: Go. Categories are fixed success/deadline/other; no request body, URL or error text labels. Duration and error propagation are preserved. Injected observe is a bounded nonthrowing sink.
