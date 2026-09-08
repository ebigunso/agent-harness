---
id: ag-6-c1
section: ag-6
type: clean
---
Task framing: Retry uncertain charge with stable identity and budget.

```diff
--- a/charge.js
+++ b/charge.js
@@ -0,0 +1,15 @@
+export class Timeout extends Error {}
+export async function charge(key, send) {
+ for(let attempt=0;attempt<3;attempt++) {
+  try { return await send(key,AbortSignal.timeout(1000)); }
+  catch(error) { if(!(error instanceof Timeout) || attempt===2) throw error; }
+ }
+}
+export async function check() {
+ const seen=new Set(); let calls=0;
+ const result=await charge("order-a",async key=>{seen.add(key); calls++; if(calls===1) throw new Timeout(); return "paid";});
+ if(result!=="paid" || seen.size!==1 || calls!==2) throw new Error("dedupe");
+ let failed=0;
+ try { await charge("b",async()=>{failed++;throw new Timeout();}); } catch(error) { if(!(error instanceof Timeout)) throw error; }
+ if(failed!==3) throw new Error("budget");
+}
```
Commit message: "retry uncertain charge with stable identity and budget"

Reviewer notes: Node 24. send is server adapter, honors its AbortSignal within 1s and deduplicates stable key; no retry on non-timeout errors. Exactly three attempts bound total adapter wait to 3s. Test models committed charge with lost first reply and verifies one charge.
