### 3) Keep Changes Small, Cohesive, and Reversible

- Group related edits into a single coherent unit.
- Avoid coupling unrelated refactors with functional changes.
- Make rollback straightforward by limiting blast radius.

Review checks:
- Is the diff focused on one clear goal?
- Can this change be safely reverted without collateral edits?
