---
id: ag-1-c2
section: ag-1
type: clean
---
Task framing: Render authoritative checkout quote.

```diff
--- a/Checkout.tsx
+++ b/Checkout.tsx
@@ -0,0 +1,5 @@
+import * as React from "react";
+export function Checkout({quantity, quote, onSubmit}: {quantity: number; quote: number; onSubmit: (q: number) => void}) {
+ const valid = Number.isSafeInteger(quantity) && quantity > 0;
+ return <><output>{quote}</output><button disabled={!valid} onClick={() => { if(valid) onSubmit(quantity); }}>Order</button></>;
+}
```
Commit message: "render authoritative checkout quote"

Reviewer notes: React installed. Server result is authoritative display data; onSubmit is the application API adapter, which repeats quantity validation and recomputes policy server-side. UI validation is UX only.
