# Tool Capability Matrix

Tool names vary by runtime. This reference describes capability boundaries rather than exact tool strings.

| Logical role | Expected capabilities | Default restrictions |
|---|---|---|
| Orchestrator | read, search, ask user, edit plan/rules/docs, dispatch subagents, run validation commands, git coordination | owns shared-state Git mutations and plan lifecycle state |
| Researcher | read, search, diagnostics, bounded UI research when assigned | no implementation edits; no plan-file writes |
| Worker | read, search, edit within `owns`, run assigned validation, bounded UI probes for assigned UI/frontend work | no nested subagents; no shared-state Git mutations unless delegated |
| Reviewer | read, search, diagnostics, run review/evidence checks, bounded UI/E2E evidence when required | no implementation edits |

## Runtime Notes

- Copilot tool labels are defined in plugin-root-relative `agents/*.md` frontmatter.
- Claude tool support should be kept minimal unless the plugin schema and runtime behavior are confirmed.
- Codex templates should use sandbox/tool settings appropriate to each role and rely on bootstrap for installation.
