---
id: cp-8-c3
section: cp-8
type: clean
---
Task framing: Use current stores through existing reader port.

```diff
--- a/store.go
+++ b/store.go
@@ -1,7 +1,8 @@
 package store
+import "strings"
 type Reader interface { Name() string }
 type Memory struct { Value string }
 func (m Memory) Name() string { return m.Value }
 type Config struct { Value string }
 func (c Config) Name() string { return c.Value }
-func Label(reader Reader) string { return reader.Name() }
+func Label(reader Reader) string { return strings.TrimSpace(reader.Name()) }
```
Commit message: "use current stores through existing reader port"

Reviewer notes: Dependencies are acyclic: service depends on narrow Reader and strings only; both current stores implement it. The fixture shows one package to avoid omitted imports. Network or database I/O is not needed by either current store.
