---
id: cp-4-c4
section: cp-4
type: clean
---
Task framing: Format selected names with explicit locale.

```diff
--- a/names.ts
+++ b/names.ts
@@ -1 +1,6 @@
-export function names(input: readonly string[]): string[] { return input.map(x => x.toUpperCase()); }
+type Formatter = (name: string, locale: string) => string;
+// Calls format synchronously in input order, once per name.
+export function names(input: readonly string[], locale: string, format: Formatter): string[] {
+  return input.map(name => format(name, locale));
+}
+export function upper(name: string, locale: string) { return name.toLocaleUpperCase(locale); }
```
Commit message: "format selected names with explicit locale"

Reviewer notes: Callback runs synchronously once per item in input order. It receives locale explicitly and returns a value; no ambient state or mutation. Locale is a validated supported locale from startup.
