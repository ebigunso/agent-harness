---
id: ag-5-c4
section: ag-5
type: clean
---
Task framing: Apply duplicate counter deliveries once.

```diff
--- a/counter.py
+++ b/counter.py
@@ -0,0 +1,18 @@
+from threading import Lock
+from concurrent.futures import ThreadPoolExecutor
+class Counter:
+    def __init__(self):
+        self._lock=Lock(); self._seen=set(); self._value=0
+    def apply(self, ident, delta):
+        with self._lock:
+            if ident not in self._seen:
+                self._value += delta
+                self._seen.add(ident)
+            return self._value
+    def value(self):
+        with self._lock: return self._value
+def check():
+    counter=Counter()
+    with ThreadPoolExecutor(max_workers=8) as pool:
+        values=list(pool.map(lambda _:counter.apply("e1",1),range(32)))
+    assert values==[1]*32 and counter.value()==1
```
Commit message: "apply duplicate counter deliveries once"

Reviewer notes: Single-process in-memory authoritative store. Lock and dedupe set protect the same transition. Identical event ID always carries same immutable delta; process persistence/restart is outside this bounded store contract. Concurrent duplicate check exercises 32 deliveries.
