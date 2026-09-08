---
id: ag-7-c3
section: ag-7
type: clean
---
Task framing: Count workflow outcomes with safe trace correlation.

```diff
--- a/workflow.py
+++ b/workflow.py
@@ -0,0 +1,17 @@
+def run(trace_id, work, signal):
+    try:
+        result=work()
+    except OSError:
+        signal("failure",trace_id)
+        raise
+    signal("success",trace_id)
+    return result
+def check():
+    events=[]
+    emit=lambda outcome,trace:events.append((outcome,trace))
+    assert run("r1",lambda:7,emit)==7
+    def fail(): raise OSError("offline")
+    try: run("r2",fail,emit)
+    except OSError: pass
+    else: raise AssertionError("swallowed")
+    assert events==[("success","r1"),("failure","r2")]
```
Commit message: "count workflow outcomes with safe trace correlation"

Reviewer notes: Trace ID is validated opaque server ID. Signals contain outcome and correlation only, no input payload. Work exposes only OSError as its operational failure; signal is bounded and nonthrowing. Failure is recorded before original OSError propagates; successful runs record success once.
