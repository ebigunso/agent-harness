---
id: rs-c3
language: rust
type: clean
---
Task framing: Add transfer between wallets to the payments module.

```diff
--- a/src/payments/transfer.rs
+++ b/src/payments/transfer.rs
@@
+pub fn transfer(
+    ledger: &mut Ledger,
+    from: &WalletId,
+    to: &WalletId,
+    amount: Money,
+) -> Result<TxId, TransferError> {
+    ledger.debit(from, &amount)?;
+    ledger.credit(to, &amount)?;
+    Ok(TxId::new(from, to))
+}
```
