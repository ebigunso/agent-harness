---
id: rb-persistent-shell-cwd-normalization-c2
section: rb-persistent-shell-cwd-normalization
type: clean
---
Task framing: Diagnose the failed command and give the smallest safe remediation and confirmation.

Synthetic diagnostic scenario.

Environment: Windows 11 23H2 build 22631; PowerShell 7.4.6; CPython 3.12.7; cwd and intended root both C:/work/reports. Tool UI workspace root is also C:/work/reports.

Prior command: `Set-Location -LiteralPath "C:/work/reports"` — status 0.

Before retry/repair: `pwd` reports C:/work/reports; `Get-Item -Force -LiteralPath 'scripts/check.py','README.md' | Select-Object -ExpandProperty FullName` exits 0, stderr empty, stdout:
```text
C:/work/reports/scripts/check.py
C:/work/reports/README.md
```

Failing command: `python scripts/removed.py`

Exit code: 2

stdout:
```text
(empty)
```

stderr:
```text
C:\Python312\python.exe: can't open file 'C:\\work\\reports\\scripts\\removed.py': [Errno 2] No such file or directory
```

Diagnostic observations: Read-only git log and git ls-files show scripts/removed.py was intentionally renamed to scripts/check.py in the current committed tree; no uncommitted deletion exists. Current README names python scripts/check.py. The issued command came from an old terminal history entry.

Final `pwd` remains C:/work/reports. No navigation, file or environment change occurred.
