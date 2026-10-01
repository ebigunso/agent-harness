# Tool Capability Matrix

Tool names vary by runtime. This reference describes capability boundaries rather than exact tool strings.

| Logical role | Expected capabilities | Default restrictions |
|---|---|---|
| Orchestrator | read, search, ask user, edit plan/rules/docs, dispatch subagents, run validation commands, git coordination | owns shared-state Git mutations and plan lifecycle state |
| Researcher | read, search, diagnostics, bounded UI research when assigned | no implementation edits; no plan-file writes |
| Worker | read, search, edit within `owns`, run assigned validation, bounded UI probes for assigned UI/frontend work | no nested subagents; no shared-state Git mutations unless delegated |
| Reviewer | read, search, diagnostics, run review/evidence checks, bounded UI/E2E evidence when required | no implementation edits |
| Counsel | ask the owner, read and write value documents, quick reads of code in service of a discussion, search, dispatch Researchers, message the Orchestrator session over a peer channel (which may be shell-based, hence terminal tools) | separate session, never dispatched; dispatches no Worker or Reviewer; does not read plans or diffs; no bulk code reading, no check-up on the project's state, and no check on a run's work by reading code (those go to a Researcher); approves no plan, accepts no decision record, instructs no merge |

## Runtime Notes

- Copilot tool labels are defined in plugin-root-relative `agents/*.md` frontmatter.
- Claude tool support should be kept minimal unless the plugin schema and runtime behavior are confirmed.
- Codex templates should use sandbox/tool settings appropriate to each role and rely on bootstrap for installation.
- Counsel's dispatch limits are tool configuration in Copilot (`agents: ['Researcher']`, user-invocable only, absent from the Orchestrator's `agents` list) and a stated rule in Claude and Codex. Its reading limits are a stated rule in every runtime.
