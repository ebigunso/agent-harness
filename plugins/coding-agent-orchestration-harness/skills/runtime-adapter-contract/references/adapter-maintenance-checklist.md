# Adapter Maintenance Checklist

Use this checklist before completing runtime adapter changes.

## Scope

- Identify which runtime is affected: Copilot, Claude, Codex, or manifest packaging.
- Confirm whether the change is runtime mechanics, shared semantics, or both.
- Move shared semantics to shared skills/references instead of copying them into adapters.

## Role Names

- Check `orchestration-harness/references/runtime-role-map.md`.
- Preserve existing public physical names unless a migration plan exists.
- Prefer namespaced names for new physical agents where collisions are plausible.

## Prompt Shape

- Keep Copilot/GPT adapters to a medium kernel when explicit selection benefits from local reminders.
- Keep Claude adapters short and reference-driven.
- Keep Codex `AGENTS.md` snippets loader-only.

## Tool Permissions

- Match tools to role boundaries.
- Researcher and Reviewer remain read/review oriented.
- Worker may edit within `owns` and run assigned validation.
- Shared-state Git mutations remain Orchestrator-controlled unless explicitly delegated.

## Final Checks

- Manifest paths still point to the intended runtime directories.
- Adapter bodies route to `orchestration-harness`.
- No adapter contains a full duplicate of the canonical workflow.
- New skills live under shared `skills/` unless runtime-specific by design.
