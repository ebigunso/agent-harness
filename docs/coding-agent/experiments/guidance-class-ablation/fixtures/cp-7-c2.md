---
id: cp-7-c2
section: cp-7
type: clean
---
Task framing: Retry payment once with stable dedupe key.

```diff
--- a/payment.go
+++ b/payment.go
@@ -0,0 +1,6 @@
+package payment
+func Pay(key string, charge func(string) error) error {
+ err:=charge(key)
+ if err!=nil { return charge(key) }
+ return nil
+}
--- a/payment_test.go
+++ b/payment_test.go
@@ -0,0 +1,10 @@
+package payment
+import ("testing"; "errors")
+func TestLostResponse(t *testing.T) {
+ seen:=map[string]bool{}; calls:=0; charges:=0
+ err:=Pay("order-1",func(key string) error {
+  calls++; if !seen[key] { seen[key]=true; charges++ }
+  if calls==1 { return errors.New("lost response") }; return nil
+ })
+ if err!=nil || calls!=2 || charges!=1 || !seen["order-1"] { t.Fatal(err,calls,charges) }
+}
```
Commit message: "retry payment once with stable dedupe key"

Reviewer notes: Authoritative charge callback owns persistent idempotency. Test simulates first response lost after charge, then successful repeat; it asserts one charge and two calls using the same key. Service supports serial retry only; no load behavior changed.
