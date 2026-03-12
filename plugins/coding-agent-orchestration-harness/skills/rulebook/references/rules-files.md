# Repository Rules Files: Required Structure

Rules live under:
- docs/coding-agent/rules/common.md
- docs/coding-agent/rules/worker.md
- docs/coding-agent/rules/orchestrator.md
- docs/coding-agent/rules/index.md

Required sections:

1) common.md must include:
- Repository Reference Documents
- Repository-Specific Validation Commands
- Repo Safety / Boundaries
- Repo Naming / Structure
- Global Migration Candidates (Placeholder)

2) worker.md must include:
- Repo-Specific Worker Notes
- Repo CI / Checks Mapping
- Global Migration Candidates (Placeholder)

3) orchestrator.md must include:
- Repo-Specific Orchestrator Policies
- Repo-Specific Integration / Git Policy
- Global Migration Candidates (Placeholder)

Applying rule_candidates:
- Route by `rule_candidates[].audience` to the file (common/worker/orchestrator).
- Route by `rule_candidates[].intended_home`:
  - repo_specific → normal sections
  - global_candidate → placeholder section
