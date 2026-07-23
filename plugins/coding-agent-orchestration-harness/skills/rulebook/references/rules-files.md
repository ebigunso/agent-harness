# Repository Rules Files: Required Structure

Rules live under:
- docs/coding-agent/rules/index.md
- docs/coding-agent/rules/common.md
- docs/coding-agent/rules/worker.md
- docs/coding-agent/rules/orchestrator.md
- docs/coding-agent/rules/reviewer.md
- docs/coding-agent/rules/_lifecycle.json

The rule suite is considered installed only when:
- `index.md` exists;
- all required role rule files exist;
- `_lifecycle.json` exists;
- `index.md` and all role rule files share the same `suite_id`;
- the schema version matches the plugin-required schema.

`index.md` is a low-token routing file and bootstrap success marker.

`_lifecycle.json` is the machine-oriented lifecycle sidecar and is read only for bootstrap, repair, schema migration, targeted refresh, source-drift diagnosis, or contradiction handling.

Required sections:

1) index.md must include:
- rule schema version
- suite ID
- lifecycle manifest path
- required role rule files
- role-to-file routing
- short rule freshness guidance

2) common.md must include:
- Repository Reference Documents
- Repository-Specific Validation Commands
- Repo Safety / Boundaries
- Repo Naming / Structure

common.md may additionally include one optional Decision Records line recording the repository's ADR convention, in exactly one of two forms:

- `Decision records: follow <path>; match the existing ADRs' numbering and sections.`
- `Decision records: no repo convention — harness default template applies (durable-docs-authoring references/adr.md).`

Set and update this line only through the detection/placement procedure in `references/bootstrap-lifecycle.md`; never record or change it without user confirmation.

3) worker.md must include:
- Repo-Specific Worker Notes
- Repo CI / Checks Mapping
- Mechanical Gate Candidates

4) orchestrator.md must include:
- Repo-Specific Orchestrator Policies
- Repo-Specific Integration / Git Policy
- Rule Suite Refresh Notes

5) reviewer.md must include:
- Repo-Specific Reviewer Notes
- Review Risk Hotspots
- Required Reviewer-Owned Evidence
- Review Heuristics
- Recurring Misses And Prevention
- Mechanical Gate Candidates

Applying rule_candidates:
- Route by `rule_candidates[].audience` to the file (common/worker/orchestrator/reviewer).
- `rule_candidates` are always repo-specific. Apply them to active repo rule sections or repo-local candidate sections such as Mechanical Gate Candidates.
- Harness-global ideas must be emitted as `harness_migration_candidates` or lesson candidates with `promotion_target: harness_migration`.

Harness migration staging:
- `docs/coding-agent/skill-candidates.md` is the canonical backlog for cross-repo harness improvements discovered during target-repository work.
- `docs/coding-agent/skill-drafts/*.md` holds fuller drafts when a candidate is too large or ambiguous for one backlog entry.
- Use `references/skill-candidates-file.md` for the required `HMC-*` format.
