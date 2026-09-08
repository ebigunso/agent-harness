---
id: cp-6-c1
section: cp-6
type: clean
---
Task framing: Convert server seconds to timer milliseconds.

```diff
--- a/Timeout.java
+++ b/Timeout.java
@@ -0,0 +1 @@
+public record Timeout(int timeoutSeconds) {}
--- a/timeout.ts
+++ b/timeout.ts
@@ -0,0 +1,8 @@
+type Timeout = {timeoutSeconds: number};
+export function milliseconds(wire: Timeout) { return wire.timeoutSeconds * 1000; }
+export function schedule(wire: Timeout, timer: (ms: number) => void) { timer(milliseconds(wire)); }
+export function check() {
+  let received = -1;
+  schedule({timeoutSeconds: 3}, ms => { received = ms; });
+  if (received !== 3000 || milliseconds({timeoutSeconds: 0}) !== 0) throw new Error("units");
+}
```
Commit message: "convert server seconds to timer milliseconds"

Reviewer notes: Java record JSON field is timeoutSeconds. Validated range is 0..3600 inclusive. Small assertion exercises the exact adapter called by schedule; browser timer is injected to avoid waiting.
