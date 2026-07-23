---
name: subagent-strategy
description: Delegation and parallel-subagent strategy for Orchestrator. Use when you are deciding how to split work across Researcher/Worker/Reviewer, writing or refining subagent prompts, running parallel research/review, consolidating multiple subagent outputs, or when subagent calls are drifting in scope or getting bloated.
---

# Skill: subagent-strategy

This skill standardizes how the Orchestrator uses subagents to:
- keep the Orchestrator context window clean
- increase coverage by parallel analysis
- keep each subagent invocation single-scope and high-signal
- prevent delegation drift (research vs execution vs review)

---

## Core rules (always apply)

1) Prefer subagents to preserve Orchestrator context
- Use Workers for implementation tasks.
- Use Researcher for read-only exploration and plan-fill inputs.
- Use Reviewer for read-only review + E2E/visual evidence when required.

2) Prefer semantic discovery with an explicit fallback
- When exploring a codebase or framing Researcher work, prefer semantic, symbol-aware, and diagnostics capabilities when they are available.
- If those capabilities are unavailable or do not answer the question cleanly, fall back to targeted text search and file reads.

3) One objective per subagent invocation
- Every subagent call should have one objective and one deliverable shape.
- If a call would require multiple independent objectives, split into multiple invocations.
- Prefer Worker tasks completable in one short feedback loop — one module, one validation failure, one review slice — over whole-component assignments.

4) Parallelize analysis for complex problems
- For complex or high-ambiguity work, run multiple Researcher calls in parallel.
- Each Researcher call must have a narrow focus (e.g., validation/CI mapping only).

5) Keep prompts bounded AND properly framed (short rationale is allowed)
Subagents benefit from “why” when it changes decisions, but long narratives are usually harmful.

- Include the following prompt sections (short, explicit):
  - Objective
  - Deliverables (exact output sections expected)
  - Scope boundaries (what to include / what to ignore)
  - Constraints (must-follow rules)
  - Evidence requirements (validation artifacts / screenshots)
  - Sources to consult (file paths)

- Context / Rationale:
  - Include ONLY if it materially steers decisions (constraints, tradeoffs, risk, why scope is bounded).
  - Keep it to 2–5 bullets.
  - For deeper background, reference file paths (plan/rules/docs) instead of pasting narrative.

6) Consolidate results deterministically
- The Orchestrator must reconcile parallel Researcher outputs into one coherent plan.
- Prefer concrete file-based evidence (paths, symbols, workflows) over speculation.

---

## Progressive disclosure (read only what you need)

If the runtime launches subagents asynchronously or as background processes:
- Read references/async-dispatch-lifecycle.md

If the runtime setup uses multiple long-lived agents that stay alive across dispatches and communicate over an external channel (team messaging, shared inbox):
- Read references/persistent-peer-dispatch.md

If you want patterns for splitting research in parallel:
- Read references/research-splits.md

Before each Researcher/Worker/Reviewer dispatch, read and apply `references/dispatch-checklists.md`.

If you want concise prompt snippets to copy/adapt:
- Read references/prompt-snippets.md
