---
id: cp-9-c2
section: cp-9
type: clean
---
Task framing: Allow bounded stale catalog reads during source outages.

```diff
--- a/catalog/read.py
+++ b/catalog/read.py
@@ -1,2 +1,11 @@
 def read_catalog(source, cache, clock):
-    return {"items": source.read(), "stale": False, "age_seconds": 0}
+    try:
+        return {"items": source.read(), "stale": False, "age_seconds": 0}
+    except SourceUnavailable:
+        cached = cache.get()
+        if cached is None:
+            raise
+        age = clock() - cached.saved_at
+        if not 0 <= age <= 60:
+            raise
+        return {"items": cached.items, "stale": True, "age_seconds": age}
```
Commit message: "expose bounded catalog fallback"

Reviewer notes: Contract explicitly permits stale product descriptions up to 60 seconds; catalog contains no price, stock or authorization decisions. clock is the injected monotonic clock, sampled after the failed read immediately before returning the fallback; cache timestamps use the same clock and restart clears cache. SourceUnavailable is the existing source exception. Negative and expired ages are rejected. Result envelope exposes degradation; both callers show it. Cache/source errors beyond SourceUnavailable propagate.
