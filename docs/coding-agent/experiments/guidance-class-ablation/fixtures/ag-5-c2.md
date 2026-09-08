---
id: ag-5-c2
section: ag-5
type: clean
---
Task framing: Apply account transitions atomically.

```diff
--- a/state.go
+++ b/state.go
@@ -0,0 +1,9 @@
+package state
+import ("sync"; "fmt")
+type State struct { mu sync.Mutex; value string }
+func (s *State) Move(next string) error {
+ s.mu.Lock(); defer s.mu.Unlock()
+ allowed:=(s.value=="" && next=="active") || (s.value=="active" && next=="closed")
+ if !allowed { return fmt.Errorf("invalid transition") }; s.value=next; return nil
+}
+func (s *State) Value() string { s.mu.Lock(); defer s.mu.Unlock(); return s.value }
--- a/state_test.go
+++ b/state_test.go
@@ -0,0 +1,6 @@
+package state
+import "testing"
+func TestMoves(t *testing.T) {
+ s:=&State{}; if s.Move("closed")==nil { t.Fatal("invalid accepted") }
+ if s.Move("active")!=nil || s.Move("closed")!=nil || s.Move("active")==nil || s.Value()!="closed" { t.Fatal("transitions") }
+}
```
Commit message: "apply account transitions atomically"

Reviewer notes: In-memory single-process state owns its mutex and private status. Zero-value state is new; all reads/writes route through methods. allowed transitions are new→active, active→closed, and no outgoing closed transition.
