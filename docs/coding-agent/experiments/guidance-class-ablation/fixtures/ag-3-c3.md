---
id: ag-3-c3
section: ag-3
type: clean
---
Task framing: Rename internal enabled field mechanically.

```diff
--- a/Config.java
+++ b/Config.java
@@ -1,2 +1,2 @@
-record Config(boolean enabled) {}
-final class App { static Config defaults() { return new Config(false); } static boolean show(Config c, boolean active) { return c.enabled() && active; } }
+record Config(boolean visible) {}
+final class App { static Config defaults() { return new Config(false); } static boolean show(Config c, boolean active) { return c.visible() && active; } }
```
Commit message: "rename internal enabled field mechanically"

Reviewer notes: Entire internal record/caller surface shown; no serialization or persistence. All four boolean combinations retain behavior; default remains false.
