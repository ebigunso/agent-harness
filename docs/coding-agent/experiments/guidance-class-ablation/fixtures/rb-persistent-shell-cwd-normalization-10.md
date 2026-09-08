---
id: rb-persistent-shell-cwd-normalization-10
section: rb-persistent-shell-cwd-normalization
type: planted
---
Task framing: Diagnose the failed command and give the smallest safe remediation and confirmation.

Synthetic diagnostic scenario; recorded paths and retry results are constructed for this example.

Environment: Windows 11 23H2 build 22631; PowerShell 7.4.6; Git 2.47.0. Intended execution base: C:/work/repo.

Prior command in this same persistent shell: `Set-Location -LiteralPath 'C:/work/notes'` (exit/status 0, stdout/stderr empty).

State captured before any repair:

Command: `pwd`; exit/status 0; stderr empty. Path output: `C:/work/notes`.

Command: `Get-ChildItem -Name`; exit/status 0; stderr empty. stdout:
```text
today.txt
```

Failing command: `git status --porcelain`

Exit code / shell status: 128

stdout:
```text
(empty)
```

stderr:
```text
fatal: not a git repository (or any of the parent directories): .git
```

Read-only absolute-path inspection confirms these existing entries under the intended base:
```text
C:/work/repo/.git
C:/work/repo/README.md
```

Captured comparison:

1. `Set-Location -LiteralPath 'C:/work/repo'` — exit/status 0; stdout/stderr empty.
2. `pwd` — normalized cwd C:/work/repo; exit/status 0.
3. `git status --porcelain` — exit/status 0.

stdout:
```text
(empty)
```

stderr:
```text
(empty)
```

Final `pwd`: C:/work/repo; exit/status 0.

Diagnostic observations: The tool UI still displays C:/work/repo as its remembered workspace root; the persistent shell has its own cwd, shown above. No code, branch, PATH, dependency, configuration or permission change occurred between attempts. All referenced files are accessible. The original command is repeated unchanged; only the explicit navigation differs.
