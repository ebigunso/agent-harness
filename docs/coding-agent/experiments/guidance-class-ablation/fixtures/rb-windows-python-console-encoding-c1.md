---
id: rb-windows-python-console-encoding-c1
section: rb-windows-python-console-encoding
type: clean
---
Task framing: Diagnose the failed command and give the smallest safe remediation and confirmation.

Synthetic diagnostic scenario; the profile and transcript are scenario data, not a claim of live reproduction.

Environment: Windows 11 23H2 build 22631; PowerShell 7.4.6; CPython 3.12.7. cwd: C:/work/py-report. stdout is captured through a pipe, not an interactive Windows console.

Command: `python read_input.py`

Exit code: 1

stdout:
```text
(empty)
```

stderr:
```text
Traceback (most recent call last):
  File "C:\work\py-report\read_input.py", line 9, in <module>
    text = Path('input.txt').read_text(encoding='utf-8')
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte
```

Diagnostic observations:

- In the same captured-stream environment: sys.stdout.encoding = utf-8; sys.flags.utf8_mode = 0.
- The input file begins FF FE and is declared UTF-16LE with a BOM by its producer. The reader explicitly selected UTF-8. No output call has executed and no files were modified.
