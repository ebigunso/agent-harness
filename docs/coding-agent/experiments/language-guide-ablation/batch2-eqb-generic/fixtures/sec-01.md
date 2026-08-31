Task framing: Add a CSV export of all user accounts for the admin console.

```diff
--- a/server/routes/admin.py
+++ b/server/routes/admin.py
@@
+@app.get("/admin/users/export")
+def export_users():
+    if not session.get("user_id"):
+        abort(401)
+    rows = db.query("SELECT email, name, plan, created_at FROM users")
+    return csv_response(rows, filename="users.csv")
```
Note: sessions are issued to every signed-in customer; the admin console UI is only linked from the staff navigation menu.
