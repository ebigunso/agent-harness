Task framing: Make checkout resilient to flaky network by retrying the charge request.

```diff
--- a/web/src/checkout.ts
+++ b/web/src/checkout.ts
@@
+export async function submitCharge(order: Order) {
+  for (let attempt = 0; attempt < 3; attempt++) {
+    try {
+      return await api.post("/v1/charges", { orderId: order.id, amount: order.total });
+    } catch (err) {
+      if (attempt === 2) throw err;
+      await sleep(1000 * (attempt + 1));
+    }
+  }
+}
```
Note: `api.post` throws on timeout; `/v1/charges` creates a new charge per request.
