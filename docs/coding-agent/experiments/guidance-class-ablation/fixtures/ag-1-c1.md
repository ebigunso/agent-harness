---
id: ag-1-c1
section: ag-1
type: clean
---
Task framing: Supply stored facts to pricing policy.

```diff
--- a/Pricing.java
+++ b/Pricing.java
@@ -0,0 +1,14 @@
+import java.sql.*;
+record AccountFacts(int years) {}
+final class Pricing { static int discount(AccountFacts facts) { return facts.years() >= 2 ? 10 : 0; } }
+final class Accounts {
+ static AccountFacts read(Connection db, long id) throws SQLException {
+  try(var q=db.prepareStatement("SELECT years FROM accounts WHERE id=?")) {
+   q.setLong(1,id); try(var r=q.executeQuery()) { if(!r.next()) throw new SQLException("account missing"); return new AccountFacts(r.getInt(1)); }
+  }
+ }
+}
+final class Application { static int quote(AccountFacts facts) { return Pricing.discount(facts); } }
+final class Controller {
+ static int quote(Connection db,long id) throws SQLException { return Application.quote(Accounts.read(db,id)); }
+}
```
Commit message: "supply stored facts to pricing policy"

Reviewer notes: Java 17. Repository only reads facts; application calls policy on facts. Outer controller owns JDBC wiring/errors; domain/application import no SQL types in their signatures. Required row is explicit; SQL contains no pricing policy.
