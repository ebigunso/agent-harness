# Prompt Snippets (Concise)

These are text snippets to adapt into your agent/runSubagent wrapper.
Keep them single-scope.

## Researcher snippet (validation mapping focus)

Objective:
- Map required validation and CI checks for the likely touched paths.

Context / Rationale (optional; only what steers decisions):
- <why validation mapping matters for this task>
- <any constraints/tradeoffs>

Deliverables:
- Validation / CI Notes (commands + workflows)
- Plan-Fill Inputs: validation items for each Task_X (kind/required/owner/detail)
- If uncertain, list up to 5 open questions.

Rules:
- Read docs/coding-agent/rules/common.md and orchestrator.md if present.
- Do not edit workspace files.
- If you do browser exploration, name the selected provider and save evidence under that provider's artifact root.

## Researcher snippet: rule-suite bootstrap or refresh

Objective:
Discover repository facts needed to bootstrap, migrate, repair, or refresh `docs/coding-agent/rules/*`.

Scope:
Read-only. Do not edit rule files.

Deliverables:
- existing rule-suite status
- source files inspected
- validation / CI command mapping
- agent instruction files found
- repo reference docs
- safety boundaries
- review hotspots
- rule/source contradictions
- suggested operation: full_bootstrap | schema_migration | targeted_refresh | repair | none
- confidence

## Researcher snippet (UI baseline focus)

Objective:
- Establish current UI behavior baseline and propose E2E/visual spec fields.

Context / Rationale (optional; only what steers decisions):
- <what UI risks matter and why>
- <what flows are critical>

Deliverables:
- E2E/Visual Findings: flows, viewports, screenshots under the selected provider artifact root, console/network notes
- Plan-Fill Inputs: Reviewer-owned E2E validation item + draft spec fields

Rules:
- Use the selected browser automation provider for browser automation.
- Localhost/127.0.0.1 only unless explicitly configured.

## Reviewer snippet (plan review)

Scope:
- Review the draft plan at <plan> before user approval. The artifact is the plan file, not a diff.
- Inputs: the plan; Researcher output at <path or "none">.

Procedure:
- Run `python <plugin root>/skills/plan-format/scripts/validate_plan.py --file <plan> --mode balanced` first. Its pass output is the required validation evidence; do not re-check by hand what it checks.
- Read `<plugin root>/skills/plan-format/SKILL.md`; apply `<plugin root>/skills/engineering-quality-baselines/SKILL.md` per its plan-review routing entry.
- Open every source an Assumption or Context claim names and confirm it says what the plan says.

Deliverables:
- Each finding names the fact, record, or reference it contradicts.
- Your verdict is advisory to the Orchestrator. Question the decomposition given; do not propose another.

## Reviewer snippet (ADR review)

Review <record> against `durable-docs-authoring/references/adr.md`:
- What future design or implementation does the decision constrain?
- What would ignoring it cost to detect or undo?
- Can its reasoning be reconstructed from the artifact, git history, or a plan?
- Can its why be stated for a first-time reader in a sentence or two?
- Does it contain stale, superseded, or wrong content?
- Is its only constraint "do not re-add these files"?
- Does it concern the repository's product domain?
- Does it ratify an existing exception without considering remediation?
- Can a maintainer act on the Decision alone?
- Which section is re-derivable?
- Is implementation wording mirrored?
- Is any wording time-relative?
- Is more than one decision present?

## Reviewer snippet (E2E/visual gate)

Scope:
- Review this wave only. Validate acceptance criteria and REQUIRED validation evidence.

Context / Rationale (optional; only what steers decisions):
- <why certain issues are high-risk>
- <what to focus on>

If E2E/visual is required:
- Execute the E2E spec using the selected browser automation provider.
- Save evidence screenshots under the provider-defined artifact root and reference them.
- If required evidence is missing, Status must be NEEDS_REVISION.

## Reviewer snippet (latent-risk routing)

Use only when the changed code may involve:
- state, invariants, authority, derived data, or collection semantics
- fallible operations, fallback behavior, or degradation
- contract divergence or scope-sensitive decisions
- hot-path cost or runtime model compatibility
- brittle future edits, dead surface, or low-value abstraction
- validation boundaries or risk-specific test gaps
- public API compatibility or public surface completeness
- diagnostics, telemetry, or observability metadata
- build cfg/features, strict-CI hygiene, or test-production parity
- entrypoint intent, admission semantics, or candidate-vs-accepted sets

Scope:
- Review this wave only.
- Use the plugin's `engineering-quality-baselines` skill.
- First follow `engineering-quality-baselines/references/review-latent-risk.md`.
- Then read only matching conditional references.

Deliverables:
- Applicable latent-risk findings only.
- File:line evidence for each finding.
- Missing regression test shape for each risky behavior, when applicable.

Rules:
- Do not print the full checklist.
- Do not report irrelevant `N/A` criteria.
- Do not approve if an applicable latent-risk item is FAIL without waiver or accepted residual risk.

## Reviewer snippet (repo review policy)

Use when review-specific repository policy matters.

Rules:
- Include `docs/coding-agent/rules/reviewer.md` in the packet if present and relevant.
- Name relevant review hotspots from that file.
- Do not read `_lifecycle.json` unless lifecycle work is part of the review.
