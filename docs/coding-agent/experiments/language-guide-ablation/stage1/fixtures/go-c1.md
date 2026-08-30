---
id: go-c1
language: go
type: clean
---
Task framing: Wrap storage errors with operation context before returning to callers.

```diff
--- a/store/orders.go
+++ b/store/orders.go
@@ func (s *OrderStore) Get(ctx context.Context, id OrderID) (*Order, error) {
 	row, err := s.db.QueryRowContext(ctx, getOrderSQL, id)
 	if err != nil {
-		return nil, err
+		return nil, fmt.Errorf("order store: get %s: %w", id, err)
 	}
 	return scanOrder(row)
 }
```
