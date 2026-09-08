---
id: ag-2-c4
section: ag-2
type: clean
---
Task framing: Keep domain independent of outer adapter.

```diff
--- a/lib.rs
+++ b/lib.rs
@@ -0,0 +1,12 @@
+pub mod domain {
+ pub trait Quotes { fn cents(&self) -> u32; }
+ pub fn price(q: &impl Quotes) -> u32 { q.cents() + 10 }
+}
+pub mod outer {
+ use crate::domain::{self, Quotes};
+ struct Fixed;
+ impl Quotes for Fixed { fn cents(&self) -> u32 { 100 } }
+ pub fn price() -> u32 { domain::price(&Fixed) }
+}
+#[test]
+fn wired() { assert_eq!(outer::price(),110); }
```
Commit message: "keep domain independent of outer adapter"

Reviewer notes: Complete Rust module graph: outer depends on domain trait, domain depends on no outer type. Quote contract guarantees cents <= 1_000_000. One module per existing responsibility; no new crates needed.
