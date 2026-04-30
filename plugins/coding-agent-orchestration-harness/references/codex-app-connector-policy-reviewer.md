# Codex App Connector Policy: Reviewer

Use this reference only when the review involves external services, Apps/connectors, MCP tools, GitHub issues/PRs, email, calendar, chat, or other account-scoped data.

## Boundaries

- Prefer local diff, files, diagnostics, and validation evidence first.
- Use connector tools only when they materially improve review correctness or evidence verification.
- Do not access account-scoped data speculatively.
- Do not perform remote mutations.
- If connector access reveals sensitive or unrelated data, summarize only what is needed for the review.

## GitHub App Connector

You may use read-only GitHub connector tools for:
- PR diffs and changed-file context
- review comments and review submissions
- issue/PR acceptance context
- validation evidence already attached to GitHub

Do not create PRs, change PR state, request reviewers, resolve threads, dismiss reviews, edit issues, or otherwise mutate remote GitHub state.

## Other Connectors

Use Gmail, calendar, chat, drive, or similar connectors only when the Orchestrator assignment explicitly points to that service as review evidence.

Prefer read-only inspection. Do not archive, delete, label, move, send, or modify account data.

## Tool Discovery

If connector tools are not initially visible, use tool discovery only when this reference says connector access is relevant to the review.
