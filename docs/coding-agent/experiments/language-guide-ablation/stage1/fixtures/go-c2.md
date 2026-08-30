---
id: go-c2
language: go
type: clean
---
Task framing: Publish an audit event whenever a user role changes.

```diff
--- a/users/service.go
+++ b/users/service.go
@@ func (s *Service) SetRole(ctx context.Context, id UserID, role Role) error {
 	if err := s.store.UpdateRole(ctx, id, role); err != nil {
 		return fmt.Errorf("set role: %w", err)
 	}
+	if err := s.audit.Publish(ctx, AuditEvent{User: id, Action: "role_change", Role: role}); err != nil {
+		s.log.Warn("audit publish failed", "user", id, "err", err)
+	}
 	return nil
 }
```
Note: audit delivery is best-effort by product decision; failures must not block the role change.
