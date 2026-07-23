# PR Authoring

Use this reference when creating or updating pull requests, or when driving an external review loop to closure.

## PR body input

- Pass PR bodies literally via stdin or a file: `gh pr create --body-file - <<'EOF'`. A double-quoted `--body` argument lets the shell execute backticks and expand variables inside the markdown.

## Template discovery

- Search hidden locations under `.github/**` (e.g. `.github/pull_request_template.md`) before assuming no PR template exists; ignore-default file listings miss hidden directories unless told otherwise (e.g. `rg --files --hidden`).

## PR description content

- Describe the final state of the branch for reviewers, not the work history. Reviewers need what the change is now, not the sequence of attempts that produced it.

## Review-thread closeout

- When waiting on PR review rounds or arming review monitoring, read `pr-review-monitoring.md`.

- After addressing a review comment (fix pushed, reply posted), mark its thread resolved: GraphQL `resolveReviewThread` with the thread id from `reviewThreads`. Replying alone does not resolve the thread.
- Before claiming all review comments are resolved, extract every `"isResolved": false` thread from the COMPLETE thread payload (re-fetch if needed); never rely on a partial or line-range read of a large saved payload.
- Before declaring the review loop finished, apply the stopping rubric in `pr-review-monitoring.md`.

## Copilot re-review

- After Copilot has already reviewed a PR, `gh pr edit --add-reviewer` can be a no-op for re-review even when it exits successfully.
- Fallback: GraphQL `requestReviewsByLogin` with `userLogins: ["copilot-pull-request-reviewer"]` and `union: true` (using `botLogins` fails server-side).
- Verify via GraphQL: treat the re-review request as unverified until `reviewRequests` shows a queued entry or `latestReviews` shows a new review on the current head SHA — never trust the exit code.
- If neither signal appears after polling, report that no fresh review was observed instead of claiming one happened.
