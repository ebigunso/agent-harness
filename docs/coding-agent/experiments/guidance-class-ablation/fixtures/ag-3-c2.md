---
id: ag-3-c2
section: ag-3
type: clean
---
Task framing: Increase request timeout to two seconds.

```diff
--- a/client.go
+++ b/client.go
@@ -1,3 +1,3 @@
 package client
 import ("net/http"; "time")
-func New() *http.Client { return &http.Client{Timeout:time.Second} }
+func New() *http.Client { return &http.Client{Timeout:2*time.Second} }
```
Commit message: "increase request timeout to two seconds"

Reviewer notes: Review target is timeout commit only. Unrelated earlier log naming cleanup is a separate commit with independent revert evidence; it changes no dependency or lifetime needed here.
