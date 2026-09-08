---
id: cp-3-c4
section: cp-3
type: clean
---
Task framing: Rename internal user label to displayName.

```diff
--- a/user.ts
+++ b/user.ts
@@ -1,3 +1,3 @@
-export function user() { return {label: "Ada"}; }
-export function view() { return user().label; }
-export function check() { if (view() !== "Ada") throw new Error("label"); }
+export function user() { return {displayName: "Ada"}; }
+export function view() { return user().displayName; }
+export function check() { if (view() !== "Ada") throw new Error("displayName"); }
```
Commit message: "rename internal user label to displayname"

Reviewer notes: Entire internal API and both consumers are shown. This field is neither persisted nor published. One rename is the only requirement; accompanying adapter and check keep it atomic.
