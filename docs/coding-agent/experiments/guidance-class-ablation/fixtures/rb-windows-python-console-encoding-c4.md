---
id: rb-windows-python-console-encoding-c4
section: rb-windows-python-console-encoding
type: clean
---
Task framing: Diagnose the failed command and give the smallest safe remediation and confirmation.

Synthetic diagnostic scenario; the profile and transcript are scenario data, not a claim of live reproduction.

Environment: Windows 11 23H2 build 22631; PowerShell 7.4.6; CPython 3.12.7. cwd: C:/work/py-report. stdout is captured through a pipe, not an interactive Windows console.

Command: `python compute.py`

Exit code: 1

stdout:
```text
(empty)
```

stderr:
```text
Traceback (most recent call last):
  File "C:\work\py-report\compute.py", line 8, in <module>
    ratio = numerator / denominator
ZeroDivisionError: division by zero
```

Diagnostic observations:

- In the same captured-stream environment: sys.stdout.encoding = cp932; sys.flags.utf8_mode = 0.
- numerator=3 and denominator=0. Computation fails before any print call. No files were written.
