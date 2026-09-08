---
id: ag-2-c3
section: ag-2
type: clean
---
Task framing: Wire application storage at composition root.

```diff
--- a/app.ts
+++ b/app.ts
@@ -0,0 +1,2 @@
+export interface Accounts { active(id: string): boolean; }
+export function eligible(accounts: Accounts, id: string) { return accounts.active(id); }
--- a/store.ts
+++ b/store.ts
@@ -0,0 +1,2 @@
+import type {Accounts} from "./app";
+export class Store implements Accounts { active(id: string) { return id === "demo"; } }
--- a/root.ts
+++ b/root.ts
@@ -0,0 +1,3 @@
+import {eligible} from "./app";
+import {Store} from "./store";
+export function check() { return eligible(new Store(), "demo"); }
```
Commit message: "wire application storage at composition root"

Reviewer notes: All modules shown; in-memory adapter is the current store. App imports no concrete persistence type. Dependencies go from root and adapter inward.
