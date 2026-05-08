# Codex App Connector Policy: Worker

Use this reference only when the assigned Task_X explicitly requires external service context, Apps/connectors, MCP tools, GitHub issues/PRs, email, calendar, chat, or other account-scoped data.

## Default Boundary

- Do not use Apps/connectors or external-service MCP tools by default.
- Prefer context supplied by the Orchestrator prompt.
- If more remote context is needed, report the need in the Worker YAML instead of independently browsing account-scoped data.
- Do not perform remote mutations unless the Orchestrator explicitly assigns that authority.

## GitHub App Connector

Do not use GitHub connector tools by default.

If the Orchestrator explicitly assigns GitHub context gathering, keep it read-only and limited to the assigned Task_X.

You must not create PRs, change PR state, request reviewers, resolve threads, dismiss reviews, edit issues, or otherwise mutate remote GitHub state unless the Orchestrator explicitly assigns that exact action.

## Other Connectors

Use Gmail, calendar, chat, drive, or similar connectors only when the assigned Task_X explicitly names that service and the needed action.

Prefer read-only inspection. Do not archive, delete, label, move, send, or modify account data unless the Orchestrator explicitly assigns that exact action.

## Tool Discovery

If connector tools are not initially visible, use tool discovery only after confirming the assigned Task_X explicitly requires connector access.
