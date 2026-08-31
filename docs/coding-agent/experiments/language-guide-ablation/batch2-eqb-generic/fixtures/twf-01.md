Task framing: Show a "last synced" banner on the dashboard, rendered on the server for fast first paint.

```diff
--- a/app/dashboard/SyncBanner.tsx
+++ b/app/dashboard/SyncBanner.tsx
@@
+export function SyncBanner({ lastSync }: { lastSync: string }) {
+  const ago = Date.now() - new Date(lastSync).getTime();
+  return (
+    <aside className="sync-banner">
+      Synced {Math.round(ago / 60000)} min ago at{" "}
+      {new Date(lastSync).toLocaleTimeString()}
+    </aside>
+  );
+}
```
Note: rendered by the server component tree; no "use client" directive anywhere in this subtree.
