---
id: cp-4-c1
section: cp-4
type: clean
---
Task framing: Apply member discounts explicitly.

```diff
--- a/Pricing.java
+++ b/Pricing.java
@@ -1,4 +1,7 @@
 final class Pricing {
     static final class Order { int cents; Order(int cents) { this.cents = cents; } }
     static boolean eligible(boolean member) { return member; }
+    static void applyDiscount(Order order, boolean member) {
+        if (eligible(member)) order.cents -= 10;
+    }
 }
```
Commit message: "apply member discounts explicitly"

Reviewer notes: Integer cents >= 10. Predicate has no effects; named command updates only its supplied order. One command per order: members lose 10 cents, nonmembers stay unchanged; no singleton state.
