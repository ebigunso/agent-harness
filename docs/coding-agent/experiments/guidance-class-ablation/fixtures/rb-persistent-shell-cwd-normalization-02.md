---
id: rb-persistent-shell-cwd-normalization-02
section: rb-persistent-shell-cwd-normalization
type: planted
---
Task framing: Diagnose the failed command and give the smallest safe remediation and confirmation.

Synthetic diagnostic scenario; recorded paths and retry results are constructed for this example.

Environment: Windows 11 23H2 build 22631; PowerShell 7.4.6; CPython 3.12.7. Intended execution base: C:/work/reports.

Prior command in this same persistent shell: `Set-Location -LiteralPath 'C:/work/reports/tools'` (exit/status 0, stdout/stderr empty).

State captured before any repair:

Command: `pwd`; exit/status 0; stderr empty. Path output: `C:/work/reports/tools`.

Command: `Get-ChildItem -Name`; exit/status 0; stderr empty. stdout:
```text
inspect.py
```

Failing command: `python scripts/check.py`

Exit code / shell status: 2

stdout:
```text
(empty)
```

stderr:
```text
C:\Python312\python.exe: can't open file 'C:\\work\\reports\\tools\\scripts\\check.py': [Errno 2] No such file or directory
```

Read-only absolute-path inspection confirms these existing entries under the intended base:
```text
C:/work/reports/scripts/check.py
C:/work/reports/tools/inspect.py
```

Captured comparison:

1. `Set-Location -LiteralPath 'C:/work/reports'` — exit/status 0; stdout/stderr empty.
2. `pwd` — normalized cwd C:/work/reports; exit/status 0.
3. `python scripts/check.py` — exit/status 0.

stdout:
```text
checks passed
```

stderr:
```text
(empty)
```

Final `pwd`: C:/work/reports; exit/status 0.

Diagnostic observations: The tool UI still displays C:/work/reports as its remembered workspace root; the persistent shell has its own cwd, shown above. No code, branch, PATH, dependency, configuration or permission change occurred between attempts. All referenced files are accessible. The original command is repeated unchanged; only the explicit navigation differs.
