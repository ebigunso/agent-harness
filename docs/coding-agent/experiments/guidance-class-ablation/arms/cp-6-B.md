### 6) Maintain Contract Fidelity Across Layers

- Keep data models, service contracts, and adapters aligned.
- Avoid silent field loss, implicit coercions, or shape drift.
- Version and migrate interfaces deliberately when needed.

Review checks:
- Do upstream/downstream boundaries agree on schema and semantics?
- Is contract drift prevented or merely tolerated?
