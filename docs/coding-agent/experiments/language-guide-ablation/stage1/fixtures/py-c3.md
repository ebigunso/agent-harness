---
id: py-c3
language: python
type: clean
---
Task framing: Pass shipment details from intake through pricing to the label printer.

```diff
--- a/shipping/intake.py
+++ b/shipping/intake.py
@@ def intake(form: dict[str, str]) -> Quote:
+    shipment = Shipment(
+        weight_kg=float(form["weight"]),
+        service=ServiceLevel(form["service"]),
+        destination=Address.parse(form["destination"]),
+    )
+    return pricing.quote(shipment)
--- a/shipping/pricing.py
+++ b/shipping/pricing.py
@@
+def quote(shipment: Shipment) -> Quote:
+    base = RATES[shipment.service] * shipment.weight_kg
+    return Quote(amount=base + zone_fee(shipment.destination))
```
