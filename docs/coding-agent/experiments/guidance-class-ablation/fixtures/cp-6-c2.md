---
id: cp-6-c2
section: cp-6
type: clean
---
Task framing: Map required invoice fields losslessly.

```diff
--- a/invoice.py
+++ b/invoice.py
@@ -0,0 +1,13 @@
+from dataclasses import dataclass
+@dataclass(frozen=True)
+class InvoiceProto:
+    id: str
+    amount: int
+    tax_amount: int
+def to_view(proto):
+    return {"id": proto.id, "amount": proto.amount, "taxAmount": proto.tax_amount}
+def to_proto(view):
+    return InvoiceProto(view["id"], view["amount"], view["taxAmount"])
+def check():
+    for proto in [InvoiceProto("a", 100, 20), InvoiceProto("b", 0, 0)]:
+        assert to_proto(to_view(proto)) == proto
```
Commit message: "map required invoice fields losslessly"

Reviewer notes: Dataclass is the complete local facade for required protobuf fields; all three are required by the upstream schema. Optional/unknown protobuf fields are outside this client view contract. Round-trip check below exercises every required field, including zero tax.
