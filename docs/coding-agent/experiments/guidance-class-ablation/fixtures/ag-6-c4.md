---
id: ag-6-c4
section: ag-6
type: clean
---
Task framing: Use recent cached display count during outage.

```diff
--- a/display.py
+++ b/display.py
@@ -0,0 +1,17 @@
+def read(fetch, cache, clock, signal):
+    try: return fetch()
+    except OSError:
+        now=clock()
+        if cache is not None and 0 <= now-cache[0] <= 30:
+            signal("display_cache_fallback")
+            return cache[1]
+        raise
+def check():
+    signals=[]
+    def fail(): raise OSError("offline")
+    assert read(fail,(10,7),lambda:40,signals.append)==7
+    assert signals==["display_cache_fallback"]
+    for cache in [None,(9,7),(41,7)]:
+        try: read(fail,cache,lambda:40,signals.append)
+        except OSError: pass
+        else: raise AssertionError("invalid fallback")
```
Commit message: "use recent cached display count during outage"

Reviewer notes: Noncritical display count permits stale data <= 30 monotonic seconds old. Cache is immutable (timestamp,value), clock finite and sampled after failed fetch. Only OSError qualifies; fallback emits safe signal. Expired/future/missing cache rethrows original failure.
