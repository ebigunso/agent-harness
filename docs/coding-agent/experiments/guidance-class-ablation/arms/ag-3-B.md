### Gate 3: Cohesive Change Surface

**Expectation**
- The change set is cohesive and aligned to one architectural intent.
- Cross-cutting updates are deliberate and traceable.

**Evidence expectations**
- Plan links each touched area to the same architectural objective.
- Review confirms no unrelated edits are bundled.
- Refactor-only changes are separated from behavior changes when risk warrants.

**Anti-patterns**
- Mixing feature work, refactors, and incidental cleanup without rationale.
- Large “drive-by” edits across modules with weak coupling to the objective.
- Hidden behavior changes inside nominally mechanical diffs.
