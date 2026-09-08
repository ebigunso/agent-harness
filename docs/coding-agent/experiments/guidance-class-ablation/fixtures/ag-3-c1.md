---
id: ag-3-c1
section: ag-3
type: clean
---
Task framing: Persist invoice tax in displayed total.

```diff
--- a/billing.py
+++ b/billing.py
@@ -1,5 +1,9 @@
-def total(net): return net
-def save(store, net): store.append({"net": net})
-def api(store, net):
-    save(store, net)
-    return {"total": total(net)}
+def total(net, tax): return net + tax
+def save(store, net, tax): store.append({"net": net, "tax": tax})
+def api(store, net, tax):
+    save(store, net, tax)
+    return {"total": total(net,tax)}
+def check():
+    store=[]
+    assert api(store,100,10)=={"total":110}
+    assert store==[{"net":100,"tax":10}]
```
Commit message: "persist invoice tax in displayed total"

Reviewer notes: One bounded requirement: retain tax in stored invoice and expose gross total. In-memory store has no old persisted records. API, domain and persistence all change together.
