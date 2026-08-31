Task framing: Let users archive a project from the project list page.

```diff
--- a/app/projects/actions.ts
+++ b/app/projects/actions.ts
@@
+export async function archiveProject(id: string) {
+  await api.post(`/projects/${id}/archive`);
+  toast.success("Project archived");
+}
--- a/app/projects/ProjectRow.tsx
+++ b/app/projects/ProjectRow.tsx
@@
+      <button onClick={() => archiveProject(project.id)}>Archive</button>
```
Note: the project list is served from the route-level query cache (staleTime: 5 minutes).
