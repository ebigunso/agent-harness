---
id: py-c4
language: python
type: clean
---
Task framing: The notifier needs a shared client; construct it once instead of per-call.

```diff
--- a/notify/client.py
+++ b/notify/client.py
@@
 import httpx
+from functools import lru_cache
+
+
+@lru_cache(maxsize=1)
+def _client() -> httpx.Client:
+    settings = load_settings()
+    return httpx.Client(base_url=settings.webhook_url, timeout=5.0)
 
 def send(alert: Alert) -> None:
-    settings = load_settings()
-    with httpx.Client(base_url=settings.webhook_url, timeout=5.0) as client:
-        client.post("/notify", json=alert.as_dict())
+    _client().post("/notify", json=alert.as_dict())
```
