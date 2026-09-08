### Gate 1: Clear Responsibility Boundaries

**Expectation**
- Each layer/module has a clear responsibility and does not absorb unrelated concerns.
- Business rules remain in domain/application logic, not scattered into presentation or persistence details.

**Evidence expectations**
- Planning notes identify impacted boundaries and owned responsibilities.
- Review confirms behavior changes are implemented in the correct layer.
- No unexplained cross-layer logic movement.

**Anti-patterns**
- UI or transport handlers embedding business invariants.
- Data access layer deciding domain policy.
- “Utility” modules accumulating unrelated logic as a shortcut.
