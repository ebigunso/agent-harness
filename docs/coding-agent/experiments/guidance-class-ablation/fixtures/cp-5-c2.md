---
id: cp-5-c2
section: cp-5
type: clean
---
Task framing: Introduce validated nonempty account IDs.

```diff
--- a/lib.rs
+++ b/lib.rs
@@ -0,0 +1,12 @@
+pub struct AccountId(String);
+impl AccountId {
+    pub fn new(raw: String) -> Result<Self, &'static str> {
+        if raw.is_empty() { Err("account id must be nonempty") } else { Ok(Self(raw)) }
+    }
+    pub fn len(&self) -> usize { self.0.len() }
+}
+#[test]
+fn boundary() {
+    assert!(AccountId::new(String::new()).is_err());
+    assert_eq!(AccountId::new("a".into()).ok().unwrap().len(), 1);
+}
```
Commit message: "introduce validated nonempty account ids"

Reviewer notes: Contract requires nonempty bytes, not nonblank human names. Private field prevents arbitrary construction outside this module. Internal length needs no repeat validation.
