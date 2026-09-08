---
id: ag-7-c1
section: ag-7
type: clean
---
Task framing: Log login event identifiers only.

```diff
--- a/Login.java
+++ b/Login.java
@@ -0,0 +1,6 @@
+import java.util.function.Consumer;
+record Credentials(String password,String bearerToken) {}
+record LoginEvent(String eventId,String requestId,String accountId) {}
+final class Login {
+ static void success(LoginEvent event, Credentials credentials, Consumer<LoginEvent> sink) { sink.accept(event); }
+}
```
Commit message: "log login event identifiers only"

Reviewer notes: Java 17. Telemetry schema intentionally allowlists event/request/account identifiers; credentials are separate and never passed to sink. All identifiers are safe server-generated opaque IDs.
