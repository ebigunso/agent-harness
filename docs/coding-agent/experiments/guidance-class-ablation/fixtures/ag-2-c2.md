---
id: ag-2-c2
section: ag-2
type: clean
---
Task framing: Translate domain rejection at controller.

```diff
--- a/Controller.java
+++ b/Controller.java
@@ -0,0 +1,4 @@
+enum Outcome { ALLOWED, REJECTED }
+final class Rule { static Outcome apply(boolean active) { return active ? Outcome.ALLOWED : Outcome.REJECTED; } }
+record HttpResponse(int status) {}
+final class Controller { static HttpResponse handle(boolean active) { return new HttpResponse(Rule.apply(active) == Outcome.ALLOWED ? 200 : 403); } }
```
Commit message: "translate domain rejection at controller"

Reviewer notes: Java 17. HttpResponse is a complete outer transport DTO. Domain enum/function have no dependency on it; controller owns HTTP mapping.
