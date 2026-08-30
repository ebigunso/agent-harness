---
id: py-c2
language: python
type: clean
---
Task framing: Add a test covering token expiry in the session manager.

```diff
--- a/tests/test_sessions.py
+++ b/tests/test_sessions.py
@@
+def test_session_expires_after_ttl(monkeypatch):
+    clock = FakeClock(start=1_000_000.0)
+    monkeypatch.setattr(sessions, "now", clock.now)
+    mgr = SessionManager(ttl_seconds=60)
+    token = mgr.create(user_id=7)
+    assert mgr.validate(token)
+    clock.advance(61)
+    assert not mgr.validate(token)
```
