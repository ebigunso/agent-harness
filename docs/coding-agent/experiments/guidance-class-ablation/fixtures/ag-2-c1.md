---
id: ag-2-c1
section: ag-2
type: clean
---
Task framing: Wire quotes into domain through existing port.

```diff
--- a/go.mod
+++ b/go.mod
@@ -0,0 +1,2 @@
+module example.test/app
+go 1.22
--- a/domain/price.go
+++ b/domain/price.go
@@ -0,0 +1,3 @@
+package domain
+type Quote interface { Quote() int }
+func Price(q Quote) int { return q.Quote()+10 }
--- a/adapter/quote.go
+++ b/adapter/quote.go
@@ -0,0 +1,5 @@
+package adapter
+import "example.test/app/domain"
+type Fixed struct{}
+func (Fixed) Quote() int { return 100 }
+func Price() int { return domain.Price(Fixed{}) }
```
Commit message: "wire quotes into domain through existing port"

Reviewer notes: Outer adapter implements domain-owned port; no reverse import. Complete Go packages shown. Arithmetic operates on bounded cents.
