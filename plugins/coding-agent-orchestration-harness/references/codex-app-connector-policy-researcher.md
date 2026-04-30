# Codex App Connector Policy: Researcher

Use this reference only when the assignment involves external services, Apps/connectors, MCP tools, GitHub issues/PRs, email, calendar, chat, or other account-scoped data.

## Boundaries

- Prefer local repository evidence first.
- Use connector tools only when they materially improve research or plan-fill inputs.
- Do not access account-scoped data speculatively.
- Do not perform remote mutations.
- If connector access reveals sensitive or unrelated data, summarize only what is needed for the assignment.

## GitHub App Connector

You may use read-only GitHub connector tools for:
- installed-account or installation checks
- issue and PR discovery
- PR comments, review submissions, and review context
- repository metadata needed to plan work

Do not create PRs, change PR state, request reviewers, resolve threads, dismiss reviews, edit issues, or otherwise mutate remote GitHub state.

## Other Connectors

Use Gmail, calendar, chat, drive, or similar connectors only when the user request or Orchestrator assignment explicitly points to that service.

Prefer read-only inspection. Do not archive, delete, label, move, send, or modify account data.

## Tool Discovery

If connector tools are not initially visible, use tool discovery only when this reference says connector access is relevant to the assignment.
