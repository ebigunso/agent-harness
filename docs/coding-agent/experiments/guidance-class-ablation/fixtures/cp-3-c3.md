---
id: cp-3-c3
section: cp-3
type: clean
---
Task framing: Accept upper-case yes answers.

```diff
--- a/Answers.java
+++ b/Answers.java
@@ -1,4 +1,4 @@
 final class Answers {
-    static boolean parse(String text) { return "yes".equals(text); }
+    static boolean parse(String text) { return "yes".equalsIgnoreCase(text); }
     static boolean submit(String text) { return parse(text); }
 }
```
Commit message: "accept upper-case yes answers"

Reviewer notes: Review target is commit 2 only. Commit 1 separately extracted this parse method without behavior change and can be independently reverted by inlining; no module or external API changed. Before/after examples: yes true, YES false→true, no false, null false.
