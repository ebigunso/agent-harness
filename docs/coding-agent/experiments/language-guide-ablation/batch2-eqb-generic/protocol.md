# Ablation batch 2 — eqb generic references (pre-registered 2026-09-01, before any cell ran)

Target docs (arm B loads the fixture's home doc): tech-web-frameworks.md (twf-*),
stack-backend-frontend.md (sbf-*), security-boundaries.md (sec-*),
review-latent-risk-performance.md (perf-*).
Arms: A = core-principles.md only; B = A + home doc. (Arm C/D dead per ADR-I-0004 result.)
Models: Fable 5, Sol 5.6, Luna 5.6. Seeds: 2 (deviation from batch 1's 3, pre-registered:
batch 1 observed zero cross-seed variance at 216/216).
Fixtures: 12 planted (from the docs' own concern lists) + 4 clean decoys.
Decision rule per doc, worst model: B-A < 10pp on that doc's fixtures -> obsolete, delete.
FP guard: arm B FP rate on decoys > arm A + 10pp -> regression, cannot delete.
Grading: independent grader agents per (model, arm) against keys.md.
