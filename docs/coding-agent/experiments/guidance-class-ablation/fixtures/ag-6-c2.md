---
id: ag-6-c2
section: ag-6
type: clean
---
Task framing: Bound optional recommendation failures.

```diff
--- a/optional.go
+++ b/optional.go
@@ -0,0 +1,6 @@
+package optional
+import ("context"; "time")
+func Recommendation(parent context.Context, call func(context.Context)(string,error), signal func(string)) string {
+ ctx,cancel:=context.WithTimeout(parent,100*time.Millisecond); defer cancel()
+ value,err:=call(ctx); if err!=nil { signal("recommendation_unavailable"); return "" }; return value
+}
```
Commit message: "bound optional recommendation failures"

Reviewer notes: Downstream implementation must honor context cancellation. Optional recommendation is independent of required checkout; failure is signaled safely and degrades to empty recommendation. It has its own 100ms child deadline; no shared worker pool.
