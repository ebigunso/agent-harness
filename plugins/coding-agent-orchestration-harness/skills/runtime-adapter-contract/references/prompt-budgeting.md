# Prompt Budgeting

Runtime adapters should preserve shared semantics while fitting each runtime's prompt behavior.

## Copilot / GPT-Oriented Adapters

- May carry a medium-length Orchestrator kernel.
- Keep the five hard gates visible.
- Avoid copying detailed procedures that already live in `orchestration-harness` references.

## Claude Code Adapters

- Prefer short kernels plus skills/references.
- Include only the minimum hard gates needed to orient the explicitly selected agent.
- Avoid long repeated lists when the shared skill can be loaded.

## Codex

- Keep `AGENTS.md` loader-only.
- Install role templates through bootstrap.
- Do not put a full Orchestrator workflow in Codex loader snippets.

## Review Heuristic

Adapter prompt divergence is acceptable when:

- runtime mechanics require it;
- the adapter still points to shared policy;
- logical roles and hard gates remain aligned;
- wording differences do not create semantic differences.
