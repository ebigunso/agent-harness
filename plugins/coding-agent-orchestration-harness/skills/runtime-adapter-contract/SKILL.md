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

- Shared semantics live in shared skills and references.
- Runtime mechanics may diverge.
- Do not copy the full canonical workflow into adapters.
- Keep role physical names mapped in `skills/orchestration-harness/references/runtime-role-map.md`.
- Claude adapters should be shorter than GPT/Copilot adapters.
- Codex loader remains loader-only.
- Tool permissions should match role boundaries but may vary by runtime.

## Progressive disclosure (read only what you need)

- Use `references/adapter-maintenance-checklist.md` before finishing adapter edits.
- Use `references/prompt-budgeting.md` when changing prompt length or kernel shape.
- Use `references/tool-capability-matrix.md` when changing tool permissions or role capabilities.
