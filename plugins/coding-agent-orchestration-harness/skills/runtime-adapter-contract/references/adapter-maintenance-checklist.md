# Adapter Maintenance Checklist

Use this checklist before completing runtime adapter changes.

## Scope

- Identify which runtime is affected: Copilot, Claude, Codex, or manifest packaging.
- Classify the change as detailed shared policy, an enforcement-critical role workflow/output contract, runtime mechanics, or a combination.
- Keep detailed shared policy and procedures canonical in shared skills/references.
- Replicate enforcement-critical role workflow/output contracts in each runtime's instruction block.

## Role Names

- Check `skills/orchestration-harness/references/runtime-role-map.md`.
- Preserve existing public physical names unless a migration plan exists.
- Prefer namespaced names for new physical agents where collisions are plausible.

## Instruction Bodies

- Treat the Copilot agent body, Claude subagent body, and Codex role-template `developer_instructions` as runtime instruction blocks.
- Keep shared role workflow and output-contract text synchronized across all three instruction blocks.
- Keep runtime-specific additions local to the runtime that needs them, such as tool names, connector policy references, and platform mechanics.
- Keep Codex `AGENTS.md` loaders and snippets loader-only; do not confuse them with role-template `developer_instructions`.

## Replicated Contract Sync

When editing shared role workflow or output-contract text:

1. Update the Copilot, Claude, and Codex instruction bodies for that role.
2. Compare bodies only: exclude YAML frontmatter and TOML configuration fields.
3. Diff all three body pairs after the edit.
4. Classify every remaining differing line as intentional runtime-specific behavior; reconcile any unexplained drift.

- Verify frontmatter and preload baselines against the actual adapter files before encoding keep/remove lists in plans; distinguish removal authorization from descriptive context.
- Use line-bounded connector-block normalization when comparing bodies; never use dot-all greedy matching.
- Print pairwise body hashes before treating a synchronization mismatch as content drift.

## Tool Permissions

- Match tools to role boundaries.
- Researcher and Reviewer remain read/review oriented.
- Worker may edit within `owns` and run assigned validation.
- Shared-state Git mutations remain Orchestrator-controlled unless explicitly delegated.

## Final Checks

- Manifest paths still point to the intended runtime directories.
- Adapter bodies route to `orchestration-harness`.
- Pairwise body diffs contain only classified runtime-specific differences.
- Adapters do not duplicate detailed canonical procedures beyond the enforcement-critical role workflow/output contract.
- New skills live under shared `skills/` unless runtime-specific by design.
