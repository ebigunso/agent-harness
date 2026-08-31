Task framing: Add customer names to the monthly orders report.

```diff
--- a/server/reports/orders.py
+++ b/server/reports/orders.py
@@ def monthly_report(month):
     orders = db.query("SELECT * FROM orders WHERE month = %s", month)
     rows = []
     for o in orders:
-        rows.append([o.id, o.total])
+        customer = db.query_one("SELECT name FROM customers WHERE id = %s", o.customer_id)
+        rows.append([o.id, o.total, customer.name])
     return rows
```
Note: a month typically has 50k-200k orders.
