# Prompt Snippets (Concise)

These are text snippets to adapt into your agent/runSubagent wrapper.
Keep them single-scope.

## Researcher snippet (validation mapping focus)

Objective:
- Map required validation and CI checks for the likely touched paths.

Context / Rationale (optional; 2–5 bullets):
- <why validation mapping matters for this task>
- <any constraints/tradeoffs>

Deliverables:
- Validation / CI Notes (commands + workflows)
- Plan-Fill Inputs: validation items for each Task_X (kind/required/owner/detail)
- If uncertain, list up to 5 open questions.

Rules:
- Read docs/coding-agent/rules/common.md and orchestrator.md if present.
- Prefer semantic, symbol-aware, and diagnostics capabilities when available; otherwise fall back to targeted text search and file reads.
- Do not edit workspace files.
- If you do browser exploration, name the selected provider and save evidence under that provider's artifact root.

## Researcher snippet (UI baseline focus)

Objective:
- Establish current UI behavior baseline and propose E2E/visual spec fields.

Context / Rationale (optional; 2–5 bullets):
- <what UI risks matter and why>
- <what flows are critical>

Deliverables:
- E2E/Visual Findings: flows, viewports, screenshots under the selected provider artifact root, console/network notes
- Plan-Fill Inputs: Reviewer-owned E2E validation item + draft spec fields

Rules:
- Prefer semantic, symbol-aware, and diagnostics capabilities for repo exploration when available; otherwise fall back to targeted text search and file reads.
- Use the selected browser automation provider for browser automation.
- Localhost/127.0.0.1 only unless explicitly configured.

## Reviewer snippet (E2E/visual gate)

Scope:
- Review this wave only. Validate acceptance criteria and REQUIRED validation evidence.

Context / Rationale (optional; 2–5 bullets):
- <why certain issues are high-risk>
- <what to focus on>

If E2E/visual is required:
- Prefer semantic and diagnostics tooling for non-browser review evidence when available; otherwise fall back to targeted search/read inspection.
- Execute the E2E spec using the selected browser automation provider.
- Save evidence screenshots under the provider-defined artifact root and reference them.
- If required evidence is missing, Status must be NEEDS_REVISION.
