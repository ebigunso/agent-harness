---
id: rs-c4
language: rust
type: clean
---
Task framing: Store sample offsets compactly in the telemetry ring buffer.

```diff
--- a/src/telemetry/ring.rs
+++ b/src/telemetry/ring.rs
@@ impl Ring {
     pub fn push(&mut self, offset: u64) {
-        self.slots[self.head] = offset;
+        self.slots[self.head] = u32::try_from(offset)
+            .unwrap_or_else(|_| panic!("offset {offset} exceeds u32 ring slot; segment size misconfigured"));
         self.head = (self.head + 1) % self.slots.len();
     }
```
Note: segment size is validated at startup to fit u32 offsets; the panic guards that invariant.
