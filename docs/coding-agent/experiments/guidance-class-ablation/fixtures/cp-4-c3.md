---
id: cp-4-c3
section: cp-4
type: clean
---
Task framing: Display all job states.

```diff
--- a/lib.rs
+++ b/lib.rs
@@ -1,4 +1,4 @@
 pub enum State { Ready, Running, Done }
 pub fn label(state: State) -> &'static str {
-    match state { State::Ready => "Ready", State::Running => "Busy", State::Done => "Done" }
+    match state { State::Ready => "Ready", State::Running => "Running", State::Done => "Done" }
 }
```
Commit message: "display all job states"

Reviewer notes: Closed internal enum with no external serialization; exhaustive match is the only formatter and has no global state.
