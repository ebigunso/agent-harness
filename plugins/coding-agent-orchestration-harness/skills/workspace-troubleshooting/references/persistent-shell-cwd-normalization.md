# Persistent Shell CWD Normalization

Use this guide when command failures may be caused by running from the wrong current working directory (cwd), especially in persistent terminal sessions.

## When to read this

Read this reference when any of the following appear:
- repeated `cd <dir> && ...` command chains fail unexpectedly
- errors like “path not found”, “no such file or directory”, or missing script/package from a directory where it should exist
- command behavior changes between retries without code changes
- you are using a persistent shell where cwd state is carried across commands

## Quick triage checklist

1) Capture current state before changing anything
- run `pwd`
- run `ls` (or `dir`) to confirm you are where you think you are
- record failing command + error output

2) Confirm intended run location
- identify the intended directory for the command (repo root vs subdirectory)
- if needed, verify script location from project files

3) Normalize cwd minimally
- use explicit navigation to intended path (single `cd` to the target)
- avoid stacking duplicated `cd <same-dir> && ...` patterns in persistent sessions
- rerun the original command unchanged after cwd normalization

4) Validate and record
- if fixed, record that cwd drift was root cause
- capture both pre-normalization cwd and normalized cwd in troubleshooting evidence
- if not fixed, continue with another runbook to avoid overfitting on cwd

## Safe command pattern examples

- Pattern A (normalize then run):
  - `pwd`
  - `cd <intended-path>`
  - `<original-command>`

- Pattern B (single explicit execution path):
  - from repo root, use one explicit `cd <target> && <command>`
  - avoid repeating nested `cd` assumptions across retries

## Evidence expectations

When cwd drift contributed to failure, include:
- failing command and error text
- pre-normalization cwd
- normalized cwd
- rerun command result
- final status (`resolved` / `still failing`)
