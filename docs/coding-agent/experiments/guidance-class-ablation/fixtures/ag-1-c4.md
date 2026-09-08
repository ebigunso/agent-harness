---
id: ag-1-c4
section: ag-1
type: clean
---
Task framing: Translate storage retry categories at adapter boundary.

```diff
--- a/lib.rs
+++ b/lib.rs
@@ -0,0 +1,10 @@
+pub enum SqlError { SerializationFailure, Constraint }
+pub enum StoreError { Retryable, Rejected }
+pub fn translate(error: SqlError) -> StoreError {
+ match error { SqlError::SerializationFailure => StoreError::Retryable, SqlError::Constraint => StoreError::Rejected }
+}
+#[test]
+fn categories() {
+ assert!(matches!(translate(SqlError::SerializationFailure), StoreError::Retryable));
+ assert!(matches!(translate(SqlError::Constraint), StoreError::Rejected));
+}
```
Commit message: "translate storage retry categories at adapter boundary"

Reviewer notes: Closed driver errors modeled fully. Mapping only translates SQL error kinds to storage outcomes; it makes no business eligibility decision.
