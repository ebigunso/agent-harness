---
id: ag-7-c4
section: ag-7
type: clean
---
Task framing: Sample routine polling debug signals.

```diff
--- a/poll.ts
+++ b/poll.ts
@@ -0,0 +1,16 @@
+export function poller(outcome: (kind: "success"|"failure", trace: string) => void, debug: (trace: string) => void) {
+ let polls=0;
+ return async (trace: string, read: () => Promise<string>) => {
+  polls=(polls+1)%100;
+  if(polls===0) debug(trace);
+  try { const value=await read(); outcome("success",trace); return value; }
+  catch(error) { outcome("failure",trace); throw error; }
+ };
+}
+export async function check() {
+ let successes=0,failures=0,samples=0;
+ const poll=poller(kind=>{if(kind==="success")successes++;else failures++;},()=>{samples++;});
+ for(let i=0;i<100;i++) await poll("r",async()=>"ok");
+ try { await poll("r2",async()=>{throw new Error("offline");}); } catch {}
+ if(successes!==100 || failures!==1 || samples!==1) throw new Error("signals");
+}
```
Commit message: "sample routine polling debug signals"

Reviewer notes: TypeScript. Outcome sink increments counters/records failures and remains unsampled. Debug sink emits only every hundred polls, no payload. Correlation is safe ID; signal functions are bounded nonthrowing adapters. Counter cycles to avoid integer growth.
