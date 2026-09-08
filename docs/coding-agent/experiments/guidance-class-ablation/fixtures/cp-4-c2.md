---
id: cp-4-c2
section: cp-4
type: clean
---
Task framing: Format report names consistently.

```diff
--- a/report.py
+++ b/report.py
@@ -1,2 +1,11 @@
+def display_name(name):
+    return name.strip().title()
+
 def report(names):
-    return ", ".join(names)
+    return ", ".join(display_name(name) for name in names)
+
+def check():
+    names = [" ada ", "LIN"]
+    assert report(names) == "Ada, Lin"
+    assert names == [" ada ", "LIN"]
+    assert report([]) == ""
```
Commit message: "format report names consistently"

Reviewer notes: Display-only transformation; empty names intentionally remain empty. Helpers are pure and do not change the input list.
