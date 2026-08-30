---
id: go-c4
language: go
type: clean
---
Task framing: Add a small helper that formats invoice numbers.

```diff
--- /dev/null
+++ b/invoice/format.go
@@
+package invoice
+
+// FormatNumber renders an invoice number for display, e.g. "INV-00001234".
+func FormatNumber(prefix string, n Number) string {
+	return fmt.Sprintf("%s-%08d", prefix, n)
+}
```
