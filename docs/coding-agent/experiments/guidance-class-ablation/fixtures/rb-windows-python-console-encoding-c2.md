---
id: rb-windows-python-console-encoding-c2
section: rb-windows-python-console-encoding
type: clean
---
Task framing: Diagnose the failed command and give the smallest safe remediation and confirmation.

Synthetic diagnostic scenario; the profile and transcript are scenario data, not a claim of live reproduction.

Environment: Windows 11 23H2 build 22631; PowerShell 7.4.6; CPython 3.12.7. cwd: C:/work/py-report. stdout is captured through a pipe, not an interactive Windows console.

Command: `python export_report.py`

Exit code: 1

stdout:
```text
(empty)
```

stderr:
```text
Traceback (most recent call last):
  File "C:\work\py-report\export_report.py", line 25, in <module>
    with open('report.txt', 'w', encoding='utf-8') as output:
PermissionError: [Errno 13] Permission denied: 'report.txt'
```

Diagnostic observations:

- In the same captured-stream environment: sys.stdout.encoding = utf-8; sys.flags.utf8_mode = 0.
- The report.txt ACL denies this user write access. The parent path and input data exist. The file open explicitly requested UTF-8; failure occurred before any write or truncation. No addon/process lock is reported.
