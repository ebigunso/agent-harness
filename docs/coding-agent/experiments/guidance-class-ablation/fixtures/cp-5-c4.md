---
id: cp-5-c4
section: cp-5
type: clean
---
Task framing: Validate upload configuration at startup.

```diff
--- a/buffer.go
+++ b/buffer.go
@@ -0,0 +1,8 @@
+package buffer
+import "fmt"
+type Buffer struct { size int }
+func New(size int) (*Buffer, error) {
+ if size < 1 || size > 8*1024*1024 { return nil, fmt.Errorf("buffer size must be 1..8388608") }
+ return &Buffer{size:size}, nil
+}
+func (b *Buffer) Allocate() []byte { return make([]byte,b.size) }
--- a/buffer_test.go
+++ b/buffer_test.go
@@ -0,0 +1,6 @@
+package buffer
+import "testing"
+func TestConfig(t *testing.T) {
+ for _, n := range []int{-1,0,8388609} { if _,err:=New(n); err==nil { t.Fatal(n) } }
+ b,err:=New(1); if err!=nil || len(b.Allocate())!=1 { t.Fatal("valid") }
+}
```
Commit message: "validate upload configuration at startup"

Reviewer notes: Go package exposes only constructor and method; immutable private field is used by a validated value object. Zero-value Buffer intentionally returns empty bytes and is not a configured instance; New rejects all invalid config.
