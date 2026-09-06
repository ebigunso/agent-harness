---
name: playwright-e2e-evidence
description: Defines standard browser E2E/visual validation specs and evidence reporting (flows, viewports, screenshots, console/network). Use when UI verification, E2E testing, visual inspection, responsive checks, screenshots, or browser-based validation is needed. Read the Playwright provider reference only when that concrete path is selected.
---

# Skill: playwright-e2e-evidence

This skill standardizes:
1) the E2E/visual validation SPEC that Orchestrator passes to Reviewer, and
2) the E2E/visual EVIDENCE that Researcher/Reviewer return after executing the spec.

Execution interface:
- Use the browser automation provider named in the plan or task to execute browser steps and collect artifacts.
- If the selected provider is `playwright-cli`, read `references/playwright-provider-path.md` and use the `playwright-cli` skill for commands.
- This skill does not re-document provider commands; it defines what to run and what evidence to produce.

Designed for local environments (localhost / 127.0.0.1) and minimal, targeted checks.

---

## Core rules (always apply)

- Specs must be explicit (base_url, readiness, flows, viewports, evidence requirements).
- Evidence must be concrete (screenshots + console/network notes).
- Keep runs bounded: collect required evidence, then stop.
- Every spec and evidence bundle must name its artifact root explicitly.
- Artifact paths must match the selected provider's output conventions.

Reviewer gate (required-evidence integrity):
- Reviewer must verify that every required artifact path referenced in evidence actually exists on disk.
- If any required artifact is missing/unreadable, Reviewer status must be `FAILED` or `NEEDS_REVISION`, not `APPROVED`.
- Missing optional artifacts may be noted as warnings, but cannot fail the run unless the spec marks them required.

---

## Progressive disclosure (read only what you need)

If you need a canonical spec template:
- Read references/spec-template.yaml

If you need a canonical evidence template:
- Read references/evidence-template.yaml


If the selected execution provider is `playwright-cli`:
- Read references/playwright-provider-path.md
