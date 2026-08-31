Task framing: Let users delete their account from the settings email we send.

```diff
--- a/server/routes/account.py
+++ b/server/routes/account.py
@@
+@app.get("/account/delete")
+def delete_account():
+    user = require_login()
+    accounts.schedule_deletion(user.id)
+    return render("goodbye.html")
--- a/emails/settings_digest.html
+++ b/emails/settings_digest.html
@@
+<a href="{{base_url}}/account/delete">Delete my account</a>
```
Note: auth uses session cookies.
