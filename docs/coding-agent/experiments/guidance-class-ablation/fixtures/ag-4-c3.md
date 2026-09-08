---
id: ag-4-c3
section: ag-4
type: clean
---
Task framing: Add optional invoice label.

```diff
--- a/Invoice.java
+++ b/Invoice.java
@@ -1,3 +1,3 @@
 import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
-record Invoice(String id) {}
+record Invoice(String id, String label) {}
 @JsonIgnoreProperties(ignoreUnknown=true) record Reader(String id) {}
```
Commit message: "add optional invoice label"

Reviewer notes: Java 17/Jackson installed, unknown fields explicitly tolerated by reader. Impact is additive optional metadata; required id preserved. Reader is not required to use label.
