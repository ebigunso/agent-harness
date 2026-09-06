# Codex App Connector Policy

Use this reference only when the assignment involves external services, Apps/connectors, MCP tools, GitHub issues/PRs, email, calendar, chat, or other account-scoped data. Apply the rules for your assigned role.

## Role Boundaries

| Role | Context and access | Remote mutations |
|---|---|---|
| Researcher | Prefer local repository evidence. Use connectors only when they materially improve research or plan-fill inputs. | Never. |
| Worker | Do not use connectors or external-service MCP tools by default. Prefer Orchestrator-supplied context. Access requires explicit assignment for the Task_X; otherwise report the need in the Worker YAML instead of independently browsing account data. | Only when the Orchestrator explicitly assigns that exact action. |
| Reviewer | Prefer local diffs, files, diagnostics, and validation evidence. Use connectors only when they materially improve review correctness or evidence verification. | Never. |

Do not access account-scoped data speculatively. If sensitive or unrelated data is encountered, summarize only what the assignment needs.

## GitHub App Connector

Keep context gathering read-only and limited to the assignment:

| Role | Permitted context |
|---|---|
| Researcher | Installed-account or installation checks; issue and PR discovery; PR comments, review submissions, and review context; repository metadata needed to plan work. |
| Worker | GitHub context gathering only when explicitly assigned by the Orchestrator, limited to the Task_X. |
| Reviewer | PR diffs and changed-file context; review comments and submissions; issue/PR acceptance context; validation evidence already attached to GitHub. |

Creating PRs, changing PR state, requesting reviewers, resolving threads, dismissing reviews, editing issues, and other remote GitHub changes are subject to the role's mutation boundary above.

## Other Connectors

Use Gmail, calendar, chat, drive, or similar connectors only under these conditions:

- Researcher: the user request or Orchestrator assignment explicitly points to that service.
- Worker: the assigned Task_X explicitly names that service and the needed action.
- Reviewer: the Orchestrator assignment explicitly points to that service as review evidence.

Prefer read-only inspection. Do not archive, delete, label, move, send, or modify account data; the only role exception is a Worker explicitly assigned that exact action by the Orchestrator.

## Tool Discovery

If connector tools are not initially visible, use tool discovery only when the role's access conditions above are met.
