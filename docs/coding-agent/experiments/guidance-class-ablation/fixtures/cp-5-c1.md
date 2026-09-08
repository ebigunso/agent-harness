---
id: cp-5-c1
section: cp-5
type: clean
---
Task framing: Validate inventory quantities at POST boundary.

```diff
--- a/inventory.ts
+++ b/inventory.ts
@@ -0,0 +1,15 @@
+const inventory: number[] = [];
+export function formValid(q: unknown): q is number {
+  return typeof q === "number" && Number.isSafeInteger(q) && q > 0;
+}
+export function post(body: {quantity?: unknown}) {
+  if (!formValid(body.quantity)) return {status: 400};
+  inventory.push(body.quantity);
+  return {status: 201};
+}
+export function check() {
+  for (const q of [-1, 0, 1.5, NaN, Infinity, "1", null]) {
+    if (post({quantity: q}).status !== 400) throw new Error("invalid accepted");
+  }
+  if (post({quantity: 1}).status !== 201) throw new Error("valid rejected");
+}
```
Commit message: "validate inventory quantities at post boundary"

Reviewer notes: JSON middleware supplies an object. Positive safe integers are the domain; form repeats the rule for feedback. Storage append happens only after server validation.
