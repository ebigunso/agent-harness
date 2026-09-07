---
id: cp-2-c1
section: cp-2
type: clean
---
Task framing: Make the shared line parser accept LF and CRLF identically.

```diff
--- a/app/lines.py
+++ b/app/lines.py
@@ -1,8 +1,14 @@
 def parse(text):
-    return text.split("\n")
+    return text.replace("\r\n", "\n").split("\n")

 def cli(text):
     return parse(text)

 def scheduled(text):
     return parse(text)
+
+def test_newlines():
+    for caller in (cli, scheduled):
+        assert caller("a\r\nb\r\n") == ["a", "b", ""]
+        assert caller("a\nb\n") == ["a", "b", ""]
+        assert caller("") == [""]
```
Commit message: "normalize CRLF at parser entry"

Reviewer notes: Contract: preserve trailing empty records and standalone CR characters; do not trim whitespace or support other newline conventions. Both callers use this parser. Examples execute under pytest or by calling test_newlines.
