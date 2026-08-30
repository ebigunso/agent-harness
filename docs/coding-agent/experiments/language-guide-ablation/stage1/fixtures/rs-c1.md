---
id: rs-c1
language: rust
type: clean
---
Task framing: Handle the new `Suspended` variant added to `AccountState`.

```diff
--- a/src/accounts/transitions.rs
+++ b/src/accounts/transitions.rs
@@ pub fn can_withdraw(state: &AccountState) -> bool {
     match state {
         AccountState::Active => true,
         AccountState::Frozen => false,
         AccountState::Closed => false,
+        AccountState::Suspended => false,
     }
 }
```
