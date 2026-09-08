---
id: cp-7-c3
section: cp-7
type: clean
---
Task framing: Reject orders above remaining capacity.

```diff
--- a/lib.rs
+++ b/lib.rs
@@ -0,0 +1,13 @@
+pub fn accepts(capacity: u32, quantity: u32) -> bool { quantity <= capacity }
+pub fn from_text(capacity: u32, quantity: &str) -> Result<bool, std::num::ParseIntError> {
+    Ok(accepts(capacity, quantity.parse()?))
+}
+#[test]
+fn decisions() {
+    assert!(accepts(3,2)); assert!(accepts(3,3)); assert!(!accepts(3,4));
+}
+#[test]
+fn adapter() {
+    assert_eq!(from_text(3,"4").unwrap(), false);
+    assert!(from_text(3,"bad").is_err());
+}
```
Commit message: "reject orders above remaining capacity"

Reviewer notes: Pure decision has below/at/above checks. Adapter integration check exercises string parse through the same decision; parser errors remain visible. Capacity and quantity are u32 by contract, zero quantity allowed.
