# Prompt Budgeting

Runtime adapters should preserve shared semantics while fitting each runtime's prompt behavior.

## Copilot / GPT-Oriented Adapters

- May carry a medium-length Orchestrator kernel.
- Keep the five hard gates visible.
- Keep replicated role workflow and output-contract text synchronized with Claude and Codex instruction bodies.
- Avoid copying detailed procedures that already live in `orchestration-harness` references.

## Claude Code Adapters

- Preserve the same enforcement-critical role workflow and output contract used by Copilot and Codex adapters.
- Keep Claude-specific mechanics concise and reference-driven.
- Do not shorten shared replicated contract text merely to make the Claude adapter smaller.

## Codex

- Keep `AGENTS.md` loaders and snippets loader-only.
- Install inert role templates through bootstrap; their `developer_instructions` may carry replicated role workflow and output contracts.
- Keep Codex-specific connector and platform mechanics concise and local to Codex templates.

## Review Heuristic

Adapter prompt divergence is acceptable when:

- runtime mechanics require it;
- it is outside the synchronized role workflow/output contract;
- the adapter still points to shared policy;
- logical roles and hard gates remain aligned;
- wording differences do not create semantic differences.
