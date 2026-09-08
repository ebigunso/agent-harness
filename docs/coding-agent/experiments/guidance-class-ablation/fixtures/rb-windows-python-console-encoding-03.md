---
id: rb-windows-python-console-encoding-03
section: rb-windows-python-console-encoding
type: planted
---
Task framing: Diagnose the failed command and give the smallest safe remediation and confirmation.

Synthetic diagnostic scenario; the profile and transcript are scenario data, not a claim of live reproduction.

Environment: Windows 11 23H2 build 22631; PowerShell 7.4.6; CPython 3.12.7. cwd: C:/work/py-report. stdout is captured through a pipe, not an interactive Windows console.

Command: `python md_report.py`

Exit code: 1

stdout:
```text
(empty)
```

stderr:
```text
Traceback (most recent call last):
  File "C:\work\py-report\md_report.py", line 31, in <module>
    print(markdown)
  File "C:\Python312\Lib\encodings\cp1252.py", line 19, in encode
    return codecs.charmap_encode(input,self.errors,encoding_table)[0]
UnicodeEncodeError: 'charmap' codec can't encode character '\u2603' in position 10: character maps to <undefined>
```

Diagnostic observations:

- In the same captured-stream environment: sys.stdout.encoding = cp1252; sys.flags.utf8_mode = 0.
- Markdown rendering completed, yielding "# Weather ☃". No file writes.
