---
id: ag-1-c3
section: ag-1
type: clean
---
Task framing: Parse order requests at HTTP boundary.

```diff
--- a/order.py
+++ b/order.py
@@ -0,0 +1,15 @@
+def place(quantity, orders):
+    if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity <= 0:
+        raise ValueError("quantity must be positive integer")
+    orders.append(quantity)
+def post(body, orders):
+    raw = body.get("quantity")
+    if not isinstance(raw, str) or not raw.isascii() or not raw.isdecimal():
+        return 400
+    try: place(int(raw), orders)
+    except ValueError: return 400
+    return 201
+def check():
+    orders=[]
+    assert post({"quantity":"2"},orders)==201 and orders==[2]
+    assert post({"quantity":"0"},orders)==400 and orders==[2]
```
Commit message: "parse order requests at http boundary"

Reviewer notes: Framework supplies a JSON object. Application owns positive quantity invariant and append. Handler converts transport string and returns explicit 400 on invalid quantity; direct application callers get the same guard.
