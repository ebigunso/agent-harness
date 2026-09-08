---
id: cp-2-c4
section: cp-2
type: clean
---
Task framing: Accept the two uppercase boolean literals emitted by the pinned vendor device SDK.

```diff
--- a/src/vendor_adapter.rs
+++ b/src/vendor_adapter.rs
@@ -1,3 +1,8 @@
 fn read_vendor_flag(raw: &str) -> Result<bool, VendorError> {
-    vendor::parse_bool(raw)
+    // Vendor 2.1 emits uppercase booleans but its parser accepts lowercase only.
+    match raw {
+        "TRUE" => vendor::parse_bool("true"),
+        "FALSE" => vendor::parse_bool("false"),
+        _ => vendor::parse_bool(raw),
+    }
 }
```
Commit message: "adapt pinned vendor uppercase booleans at the shared boundary"

Reviewer notes: vendor::parse_bool returns Result<bool, VendorError>; lowercase literals work and other strings remain errors. SDK is external and binary-only; repository cannot patch it. This adapter is the only SDK boolean entry point. Owner: integrations team. Remove workaround when vendor 2.2 with issue V-184 fixed is qualified, or re-evaluate by 2026-10-01. Tests cover TRUE/FALSE, true/false, invalid input and unchanged error propagation. No case folding is applied to arbitrary data.
