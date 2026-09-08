---
id: cp-5-c3
section: cp-5
type: clean
---
Task framing: Normalize timestamps during ingestion.

```diff
--- a/time_input.py
+++ b/time_input.py
@@ -0,0 +1,18 @@
+from datetime import datetime, timezone
+import re
+def ingest(raw):
+    try:
+        if not isinstance(raw, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,6})?(?:Z|[+-](?:[01]\d|2[0-3]):[0-5]\d)", raw):
+            raise ValueError("timestamp shape")
+        if raw.endswith("-00:00"):
+            raise ValueError("unknown offset")
+        value = datetime.fromisoformat(raw)
+        return value.astimezone(timezone.utc)
+    except (ValueError, OverflowError) as exc:
+        raise ValueError("timestamp: explicit known ISO offset required") from exc
+def check():
+    assert ingest("2026-01-01T01:00:00+01:00") == ingest("2026-01-01T00:00:00Z")
+    for value in ["2026-01-01T00:00:00", "2026-01-01T00:00:00-00:00", "2026-01-01T00:00:00-00:00:00", "bad", None]:
+        try: ingest(value)
+        except ValueError as exc: assert "timestamp" in str(exc)
+        else: raise AssertionError(value)
```
Commit message: "normalize timestamps during ingestion"

Reviewer notes: Python 3.12. Wire shape is YYYY-MM-DDTHH:MM:SS, optional 1..6 fractional digits, followed by Z or an explicit ±HH:MM offset. Unknown -00:00 is rejected. Naive, malformed, or out-of-range timestamps receive a field-specific error. Internal callers get aware UTC datetime.
