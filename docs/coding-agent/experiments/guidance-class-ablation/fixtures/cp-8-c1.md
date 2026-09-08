---
id: cp-8-c1
section: cp-8
type: clean
---
Task framing: Share numeric formatting across active exporters.

```diff
--- a/Export.cs
+++ b/Export.cs
@@ -0,0 +1,6 @@
+using System.Globalization;
+public static class Export {
+    static string Amount(decimal amount) => amount.ToString("0.00", CultureInfo.InvariantCulture);
+    public static string Csv(decimal amount) => "amount\n" + Amount(amount);
+    public static string Text(decimal amount) => "Total: " + Amount(amount);
+}
```
Commit message: "share numeric formatting across active exporters"

Reviewer notes: Both CSV numeric column and plain-text invoice exporter are currently used. Only decimal amount formatting is shared; CSV header and text wording remain format-specific. Invariant culture prevents localized delimiters.
