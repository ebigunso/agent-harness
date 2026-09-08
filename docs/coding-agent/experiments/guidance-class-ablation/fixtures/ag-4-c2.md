---
id: ag-4-c2
section: ag-4
type: clean
---
Task framing: Keep RPC success and failure distinct.

```diff
--- a/rpc.go
+++ b/rpc.go
@@ -0,0 +1,5 @@
+package rpc
+func Fetch(call func() ([]string,error)) ([]string,error) { return call() }
+func Next(call func() ([]string,error)) (string,error) {
+ rows,err:=Fetch(call); if err!=nil { return "",err }; if len(rows)==0 { return "idle",nil }; return "work",nil
+}
--- a/rpc_test.go
+++ b/rpc_test.go
@@ -0,0 +1,7 @@
+package rpc
+import ("testing"; "errors")
+func TestOutcomes(t *testing.T) {
+ if state,err:=Next(func()([]string,error){return nil,nil}); err!=nil || state!="idle" { t.Fatal(state,err) }
+ cause:=errors.New("unavailable")
+ if _,err:=Next(func()([]string,error){return nil,cause}); !errors.Is(err,cause) { t.Fatal(err) }
+}
```
Commit message: "keep rpc success and failure distinct"

Reviewer notes: Go normal error contract: nil error means successful empty or populated result. Non-nil error remains an actionable unavailable result; caller handles it before examining collection.
