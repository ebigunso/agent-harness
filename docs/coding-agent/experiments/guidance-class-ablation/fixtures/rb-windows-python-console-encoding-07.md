---
id: rb-windows-python-console-encoding-07
section: rb-windows-python-console-encoding
type: planted
---
Task framing: Diagnose the failed command and give the smallest safe remediation and confirmation.

Synthetic diagnostic scenario; the profile and transcript are scenario data, not a claim of live reproduction.

Environment: Windows 11 23H2 build 22631; PowerShell 7.4.6; CPython 3.12.7. cwd: C:/work/py-report. stdout is captured through a pipe, not an interactive Windows console.

Command: `python templates.py`

Exit code: 1

stdout:
```text
(empty)
```

stderr:
```text
Traceback (most recent call last):
  File "C:\work\py-report\templates.py", line 27, in <module>
    print(rendered)
  File "C:\Python312\Lib\encodings\cp1252.py", line 19, in encode
    return codecs.charmap_encode(input,self.errors,encoding_table)[0]
UnicodeEncodeError: 'charmap' codec can't encode character '\u0416' in position 5: character maps to <undefined>
```

Diagnostic observations:

- In the same captured-stream environment: sys.stdout.encoding = cp1252; sys.flags.utf8_mode = 0.
- Jinja2 3.1.4 rendered "User Ж" successfully before print. No file writes or template loading errors.
