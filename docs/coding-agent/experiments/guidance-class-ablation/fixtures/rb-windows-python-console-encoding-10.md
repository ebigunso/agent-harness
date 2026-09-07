---
id: rb-windows-python-console-encoding-10
section: rb-windows-python-console-encoding
type: planted
---
Task framing: Diagnose the failed command and give the smallest safe remediation and confirmation.

Synthetic diagnostic scenario; the profile and transcript are scenario data, not a claim of live reproduction.

Environment: Windows 11 23H2 build 22631; PowerShell 7.4.6; CPython 3.12.7. cwd: C:/work/py-report. stdout is captured through a pipe, not an interactive Windows console.

Command: `python progress.py`

Exit code: 1

stdout:
```text
(empty)
```

stderr:
```text
Traceback (most recent call last):
  File "C:\work\py-report\progress.py", line 19, in <module>
    print(status, flush=True)
UnicodeEncodeError: 'cp932' codec can't encode character '\U0001f9ea' in position 8: illegal multibyte sequence
```

Diagnostic observations:

- In the same captured-stream environment: sys.stdout.encoding = cp932; sys.flags.utf8_mode = 0.
- status is "Working 🧪". The script scans files read-only; flush was added but the failure remains.
