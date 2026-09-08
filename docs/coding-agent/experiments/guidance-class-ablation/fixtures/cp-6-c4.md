---
id: cp-6-c4
section: cp-6
type: clean
---
Task framing: Rename persisted owner label to client.

```diff
--- a/lib.rs
+++ b/lib.rs
@@ -1 +1,15 @@
-pub fn owner(record: &(String, String)) -> &str { &record.1 }
+pub fn migrate(records: &[(String, String)]) -> Result<Vec<(String, String)>, &'static str> {
+    records.iter().map(|(key, value)| {
+        if key == "customer" { Ok(("client".into(), value.clone())) } else { Err("unexpected old field") }
+    }).collect()
+}
+pub fn client(record: &(String, String)) -> &str { &record.1 }
+pub fn display(record: &(String, String)) -> String { client(record).to_owned() }
+#[test]
+fn migration() {
+    let old = vec![("customer".into(), "Ada".into())];
+    let new = migrate(&old).unwrap();
+    assert_eq!(new[0].0, "client");
+    assert_eq!(display(&new[0]), "Ada");
+    assert_eq!(old[0].0, "customer");
+}
```
Commit message: "rename persisted owner label to client"

Reviewer notes: Offline exclusive migration of the entire bounded in-memory document store before new reader activation. This example uses explicit key/value tuples as persisted records; there are no other consumers, writers or optional fields. Startup takes ownership and returns migrated data atomically; immutable original is retained by caller until success.
