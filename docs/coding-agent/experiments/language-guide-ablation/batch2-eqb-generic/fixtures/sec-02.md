Task framing: Make startup failures easier to debug in production.

```diff
--- a/server/boot.py
+++ b/server/boot.py
@@ def start():
     try:
         svc = build_services(config)
     except Exception as e:
-        log.error("startup failed: %s", e)
+        log.error("startup failed: %s\nconfig=%r", e, config)
         raise
```
Note: `config` holds `stripe_api_key`, `db_url` (with password), and `jwt_secret` alongside feature flags.
