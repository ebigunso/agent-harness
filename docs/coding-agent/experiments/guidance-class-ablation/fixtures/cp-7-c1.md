---
id: cp-7-c1
section: cp-7
type: clean
---
Task framing: Expire tokens exactly at deadline.

```diff
--- a/expiry.py
+++ b/expiry.py
@@ -0,0 +1,8 @@
+from datetime import datetime, timedelta, timezone
+def expired(deadline, now):
+    return now >= deadline
+def check():
+    deadline = datetime(2026, 1, 1, tzinfo=timezone.utc)
+    assert not expired(deadline, deadline - timedelta(microseconds=1))
+    assert expired(deadline, deadline)
+    assert expired(deadline, deadline + timedelta(microseconds=1))
```
Commit message: "expire tokens exactly at deadline"

Reviewer notes: Deterministic input-time seam; all values are aware UTC datetimes. Assertions run by calling check without sleeping or changing system timezone.
