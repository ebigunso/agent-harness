---
id: cp-6-c3
section: cp-6
type: clean
---
Task framing: Include optional invoice memo.

```diff
--- a/Invoice.cs
+++ b/Invoice.cs
@@ -1,4 +1,4 @@
 using System.Text.Json;
-public record Wire(string Id, int Total);
+public record Wire(string Id, int Total, string? Memo = null);
 public record Client(string Id, int Total);
 public static class Adapter { public static Client? Parse(string json) => JsonSerializer.Deserialize<Client>(json); }
```
Commit message: "include optional invoice memo"

Reviewer notes: System.Text.Json default unknown-property tolerance is the documented consumer policy. memo is optional informational metadata; consumer only needs Id and Total. Existing required JSON property names stay unchanged.
