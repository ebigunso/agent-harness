# Dispatch Checklists (Subagent Calls)

Use these checklists to prevent vague or over-broad subagent prompts.

## Researcher dispatch checklist
Include:
- Objective (single sentence)
- Scope (what area/modules to inspect; what to ignore)
- Required deliverables (which sections must be filled)
- Sources to consult (repo rules + reference docs paths)
- Tooling preference: prefer semantic, symbol-aware, and diagnostics capabilities when available; otherwise fall back to targeted text search and file reads
- Browser artifact rule: if browser exploration is used, name the selected provider and save evidence under the provider-defined artifact root
- Local-only browser rule (localhost/127.0.0.1 unless explicitly configured)

Optional (only if it materially steers decisions):
- Context / Rationale (2–5 bullets)
  - why constraints exist
  - what risks/tradeoffs matter
  - what to ignore and why

## Worker dispatch checklist
Include:
- Task_X id, title, type
- owns (paths/globs)
- depends_on
- acceptance criteria
- validation items (kind/required/owner/detail)
- Hard requirement:
  - "If you cannot run required worker-owned validation, return status=blocked with the reason."
- Output contract:
  - "Final message MUST be exactly one YAML code block matching subagent-report-contract."

Optional (only if it materially steers decisions):
- Context / Rationale (2–5 bullets)
  - why this task is framed this way
  - compatibility constraints
  - why scope must remain narrow

## Reviewer dispatch checklist
Include:
- Review scope (one wave/phase)
- Objective + acceptance criteria
- List of changed files
- Required validation checklist (what is REQUIRED vs optional, and who owns it)
- If E2E/visual is required:
  - include the E2E spec (shape per playwright-e2e-evidence)
  - require evidence screenshots under the provider-defined artifact root
  - require console/network notes if specified

Optional (only if it materially steers decisions):
- Context / Rationale (2–5 bullets)
  - why certain checks are required
  - risk areas to pay extra attention to
