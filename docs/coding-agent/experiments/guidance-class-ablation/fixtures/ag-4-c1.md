---
id: ag-4-c1
section: ag-4
type: clean
---
Task framing: Migrate both ends of internal account rename.

```diff
--- a/api.py
+++ b/api.py
@@ -1 +1 @@
-def response(): return {"user_id":"a"}
+def response(): return {"account_id":"a"}
--- a/client.ts
+++ b/client.ts
@@ -1 +1,2 @@
-export function id(row: {user_id: string}) { return row.user_id; }
+export function id(row: {account_id: string}) { return row.account_id; }
+export function check() { if(id({account_id:"a"})!=="a") throw new Error("rename"); }
```
Commit message: "migrate both ends of internal account rename"

Reviewer notes: Breaking internal field rename is deliberate; every locatable consumer migrated in the same change. No persisted data or external clients. Required account_id shape is validated before consumption.
