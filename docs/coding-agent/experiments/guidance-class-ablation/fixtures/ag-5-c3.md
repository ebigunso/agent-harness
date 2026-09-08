---
id: ag-5-c3
section: ag-5
type: clean
---
Task framing: Model all source attribution cases.

```diff
--- a/Source.java
+++ b/Source.java
@@ -0,0 +1,11 @@
+enum Source { UNKNOWN, INTERNAL, EXTERNAL, CONFLICT;
+ static Source classify(boolean internal,boolean external) {
+  if(internal && external) return CONFLICT;
+  if(internal) return INTERNAL;
+  if(external) return EXTERNAL;
+  return UNKNOWN;
+ }
+ static void check() {
+  if(classify(false,false)!=UNKNOWN || classify(true,false)!=INTERNAL || classify(false,true)!=EXTERNAL || classify(true,true)!=CONFLICT) throw new AssertionError();
+ }
+}
```
Commit message: "model all source attribution cases"

Reviewer notes: Java 17. Truth table is neither→UNKNOWN, internal only→INTERNAL, external only→EXTERNAL, both→CONFLICT. Every state is distinct in model and executable checks.
