---
id: cp-7-c4
section: cp-7
type: clean
---
Task framing: Clarify submit button label.

```diff
--- a/Submit.tsx
+++ b/Submit.tsx
@@ -1,2 +1,2 @@
 import * as React from "react";
-export function Submit() { return <button type="submit">Go</button>; }
+export function Submit() { return <button type="submit">Submit report</button>; }
--- a/Submit.check.tsx
+++ b/Submit.check.tsx
@@ -0,0 +1,6 @@
+import * as React from "react";
+import {renderToStaticMarkup} from "react-dom/server";
+import {Submit} from "./Submit";
+export function check() {
+  if (renderToStaticMarkup(<Submit />) !== '<button type="submit">Submit report</button>') throw new Error("label");
+}
```
Commit message: "clarify submit button label"

Reviewer notes: Label-only edit; no state, role or event changes. Targeted check renders actual component and asserts button text; broader E2E is unchanged. React and react-dom are already installed.
