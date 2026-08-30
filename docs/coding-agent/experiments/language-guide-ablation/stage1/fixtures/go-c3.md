---
id: go-c3
language: go
type: clean
---
Task framing: Cache resolved feature flags per tenant to cut flag-service traffic.

```diff
--- a/flags/resolver.go
+++ b/flags/resolver.go
@@ type Resolver struct {
 	client *flagsvc.Client
+	mu     sync.RWMutex
+	cache  map[TenantID]map[string]bool
 }
@@ func (r *Resolver) Enabled(ctx context.Context, t TenantID, flag string) (bool, error) {
+	r.mu.RLock()
+	if v, ok := r.cache[t][flag]; ok {
+		r.mu.RUnlock()
+		return v, nil
+	}
+	r.mu.RUnlock()
 	v, err := r.client.Resolve(ctx, t, flag)
 	if err != nil {
 		return false, fmt.Errorf("resolve %s: %w", flag, err)
 	}
+	r.mu.Lock()
+	if r.cache[t] == nil {
+		r.cache[t] = make(map[string]bool)
+	}
+	r.cache[t][flag] = v
+	r.mu.Unlock()
 	return v, nil
 }
```
