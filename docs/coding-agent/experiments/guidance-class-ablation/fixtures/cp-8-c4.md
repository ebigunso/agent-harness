---
id: cp-8-c4
section: cp-8
type: clean
---
Task framing: Name both dispatch outcomes locally.

```diff
--- a/lib.rs
+++ b/lib.rs
@@ -0,0 +1,9 @@
+pub enum Outcome { Retry, Stop }
+pub fn label(outcome: Outcome) -> &'static str {
+    match outcome { Outcome::Retry => "Retry", Outcome::Stop => "Stop" }
+}
+#[test]
+fn labels() {
+    assert_eq!(label(Outcome::Retry), "Retry");
+    assert_eq!(label(Outcome::Stop), "Stop");
+}
```
Commit message: "name both dispatch outcomes locally"

Reviewer notes: Two real variants; no global registry or macros. Pure exhaustive match keeps the internal dispatch explicit.
