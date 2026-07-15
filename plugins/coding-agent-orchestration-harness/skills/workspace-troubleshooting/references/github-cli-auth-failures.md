# GitHub CLI auth failures blocking assigned real-GitHub validation

## Symptoms
- `gh api` / `gh pr` commands fail authentication mid-task
- a session assigned real-GitHub validation reports the stored token invalid

## Likely cause
Expired or invalid stored `gh` token in that session's environment.

## Safe, ordered steps

1) Preflight before assignment or start
- run `gh auth status` BEFORE assigning or starting any real-GitHub validation

2) If auth is invalid, reassign or re-authenticate
- reassign that validation to a session with verified working auth, and record the reassignment
- or have the user re-run `gh auth login` in the affected terminal

3) Never work around auth
- do not work around with `GH_TOKEN`/`GITHUB_TOKEN` overrides or alternate credential stores

## Evidence to capture
- the `gh auth status` output
- the reassignment record

## Scope
Any multi-session/multi-agent setup where GitHub-validated work is dispatched.
