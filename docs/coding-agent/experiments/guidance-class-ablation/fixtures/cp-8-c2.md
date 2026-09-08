---
id: cp-8-c2
section: cp-8
type: clean
---
Task framing: Replace sole command registry with direct call.

```diff
--- a/cli.py
+++ b/cli.py
@@ -1,5 +1,6 @@
 def status():
     return "ready"
-REGISTRY = {"status": status}
 def main():
-    return REGISTRY["status"]()
+    return status()
+def check():
+    assert main() == "ready"
```
Commit message: "replace sole command registry with direct call"

Reviewer notes: Only internal main calls the handler. Removed key and registry are not persisted or public. Equivalent output is asserted by executable check.
