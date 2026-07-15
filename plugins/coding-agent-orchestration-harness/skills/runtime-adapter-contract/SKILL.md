---
name: runtime-adapter-contract
description: Maintains runtime-specific adapter files for the harness. Use when editing Copilot, Claude, or Codex agent definitions, manifests, role names, tool permissions, prompt length, or bootstrap behavior.
---

# Runtime Adapter Contract

Use this skill when maintaining runtime-specific harness adapter files.
Paths in this skill are relative to the plugin root unless explicitly labeled repo-relative.

Runtime adapters include:

- Copilot agent definitions under `agents/`;
- Claude agent definitions under `claude/agents/`;
- Codex loader snippets and inert agent templates under `codex/`;
- runtime plugin manifests.

## Core rules (always apply)

- Shared policy remains canonical in shared skills and references.
- Enforcement-critical role workflow and output contracts are intentionally replicated across Copilot agent instructions, Claude subagent system prompts, and Codex `developer_instructions`.
- This replication is deliberate because runtime instruction blocks enforce role boundaries more reliably than thread-level skill reads alone.
- When shared replicated text changes in one adapter, update all three runtime copies and diff their instruction bodies to confirm sync outside intentional runtime-specific blocks.
- Runtime mechanics, tool names, connector policy, and platform-specific loading details may diverge.
- Keep role physical names mapped in `skills/orchestration-harness/references/runtime-role-map.md`.
- Keep Codex `AGENTS.md` loaders and snippets loader-only; inert role-template `developer_instructions` may carry the replicated role contract.
- Tool permissions should match role boundaries but may vary by runtime.

## Progressive disclosure (read only what you need)

- Use `references/adapter-maintenance-checklist.md` before finishing adapter edits.
- Use `references/prompt-budgeting.md` when changing prompt length or kernel shape.
- Use `references/tool-capability-matrix.md` when changing tool permissions or role capabilities.
