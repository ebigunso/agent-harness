Task framing: Add a "recent activity" section to the account page.

```diff
--- a/app/account/page.tsx
+++ b/app/account/page.tsx
@@
+async function RecentActivity({ userId }: { userId: string }) {
+  const events = await fetchActivity(userId);
+  return (
+    <section>
+      <h2>Recent activity</h2>
+      <ul>{events.map(e => <li key={e.id}>{e.summary}</li>)}</ul>
+    </section>
+  );
+}
@@
   return (
     <main>
       <ProfileCard user={user} />
+      <RecentActivity userId={user.id} />
     </main>
   );
```
Note: `fetchActivity` calls the activity service, which has a 99.5% SLA. No Suspense or error boundary exists on this route.
