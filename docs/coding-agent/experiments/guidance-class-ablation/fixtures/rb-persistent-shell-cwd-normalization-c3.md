---
id: rb-persistent-shell-cwd-normalization-c3
section: rb-persistent-shell-cwd-normalization
type: clean
---
Task framing: Diagnose the failed command and give the smallest safe remediation and confirmation.

Synthetic diagnostic scenario.

Environment: Windows 11 23H2 build 22631; PowerShell 7.4.6; Git 2.47.0; cwd and intended root both C:/work/repo. Tool UI workspace root is also C:/work/repo.

Prior command: `Set-Location -LiteralPath "C:/work/repo"` — status 0.

Before retry/repair: `pwd` reports C:/work/repo; `Get-Item -Force -LiteralPath '.git','README.md' | Select-Object -ExpandProperty FullName` exits 0, stderr empty, stdout:
```text
C:/work/repo/.git
C:/work/repo/README.md
```

Failing command: `git rev-parse --verify missing-branch`

Exit code: 128

stdout:
```text
(empty)
```

stderr:
```text
fatal: Needed a single revision
```

Diagnostic observations: git rev-parse --show-toplevel exits 0 and prints C:/work/repo. git branch --list prints main; git show-ref has no missing-branch ref. No repository/cwd error occurs.

Final `pwd` remains C:/work/repo. No navigation, file or environment change occurred.
