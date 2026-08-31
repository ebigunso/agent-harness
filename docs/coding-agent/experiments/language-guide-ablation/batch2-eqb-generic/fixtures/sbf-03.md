Task framing: Enforce the 10-items-per-order limit and minimum price in the order form.

```diff
--- a/web/src/OrderForm.tsx
+++ b/web/src/OrderForm.tsx
@@
+  const canSubmit = qty >= 1 && qty <= 10 && price >= MIN_PRICE;
+  <button disabled={!canSubmit} onClick={() => submit({ qty, price })}>Order</button>
--- a/server/orders/handler.py
+++ b/server/orders/handler.py
@@ def create_order(req):
-    order = Order(qty=req.json["qty"], price=req.json["price"])
+    # limits enforced by the form
+    order = Order(qty=req.json["qty"], price=req.json["price"])
     db.save(order)
```
