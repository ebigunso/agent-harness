Task framing: Respect the server-configured session timeout in the web client.

```diff
--- a/web/src/session.ts
+++ b/web/src/session.ts
@@
+export async function scheduleSessionExpiry() {
+  const cfg = await api.get("/v1/config"); // { session: { timeout_seconds: 1800 } }
+  setTimeout(() => {
+    store.dispatch(sessionExpired());
+  }, cfg.session.timeout_seconds);
+}
```
