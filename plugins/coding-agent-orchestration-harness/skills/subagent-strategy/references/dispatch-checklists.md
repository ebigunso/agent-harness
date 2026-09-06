# Dispatch Checklists (Subagent Calls)

Use these checklists to prevent vague or over-broad subagent prompts.

## Researcher dispatch checklist
Include:
- Objective (one per invocation; split otherwise)
- Scope (what area/modules to inspect; what to ignore)
- Required deliverables (which sections must be filled)
- Sources to consult (repo rules + reference docs paths)
- Browser artifact rule: if browser exploration is used, name the selected provider and save evidence under the provider-defined artifact root
- Local-only browser rule (localhost/127.0.0.1 unless explicitly configured)
- For rule-suite bootstrap or refresh research, require read-only deliverables: existing suite status, inspected sources, validation mapping, agent instruction files, repo reference docs, safety boundaries, review hotspots, contradictions, suggested operation, and confidence.
- For forensic research (census or inventory work), require an auditable deliverable: complete census, file:line evidence for every claim, and explicit zero-hit reporting for anything searched but absent.

Optional (only if it materially steers decisions):
- Context / Rationale
  - why constraints exist
  - what risks/tradeoffs matter
  - what to ignore and why

## Worker dispatch checklist
Include:
- Task_X id, title, type
- owns (paths/globs)
  - For retire/delete tasks: run a repo-wide search for the retired name at plan time and put every referencing file — including scripts, validators, and manifests — into owns, or sequence against the task owning them
- depends_on
- acceptance criteria
- validation items (kind/required/owner/detail)
- Consumer obligations: instruct the subagent to name the known consumer obligations of any contract it touches and escalate rather than assume — its view is the local patch; the Orchestrator owns the blast radius.
- Escape hatch for surface-minimizing constraints: any constraint like "smallest possible diff" must state that preserving existing types, schemas, and boundaries outranks it — a workaround-shaped fix is surfaced, not forced through.
- When dispatching from a triage or audit table, re-baseline each listed item against the current file state first and mark pre-landed items verify-only — derived artifacts go stale the moment other work merges.
- For parallel authoring waves: confirm each dispatch prompt is spec-complete on its own — a Worker must not need a sibling task's output or an unstated convention to satisfy acceptance.
- Hard requirement:
  - "If you cannot run required worker-owned validation, return status=blocked with the reason."
- Output contract:
  - "Final message MUST be exactly one YAML code block matching subagent-report-contract."

Optional (only if it materially steers decisions):
- Context / Rationale
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
- When review-specific repository policy matters, include `docs/coding-agent/rules/reviewer.md` in the packet and name any relevant review hotspots from that file.
- For plan review, the packet is the plan path, the Researcher output path, and the plugin root; no changed-files list.

Optional (only if it materially steers decisions):
- Context / Rationale
  - why certain checks are required
  - risk areas to pay extra attention to
- Latent-risk routing hints:
  - relevant latent-risk category
  - plugin skill and conditional reference to use
  - one sentence explaining why the category applies
