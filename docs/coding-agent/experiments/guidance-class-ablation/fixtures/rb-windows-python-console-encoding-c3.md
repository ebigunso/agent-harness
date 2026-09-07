---
id: rb-windows-python-console-encoding-c3
section: rb-windows-python-console-encoding
type: clean
---
Task framing: Diagnose the failed command and give the smallest safe remediation and confirmation.

Synthetic diagnostic scenario; the profile and transcript are scenario data, not a claim of live reproduction.

Environment: Windows 11 23H2 build 22631; PowerShell 7.4.6; CPython 3.12.7. cwd: C:/work/py-report. stdout is captured through a pipe, not an interactive Windows console.

Command: `python json_report.py`

Exit code: 1

stdout:
```text
(empty)
```

stderr:
```text
Traceback (most recent call last):
  File "C:\work\py-report\json_report.py", line 22, in <module>
    print(json.dumps(data, ensure_ascii=False))
  File "C:\Python312\Lib\json\__init__.py", line 238, in dumps
    **kw).encode(obj)
  File "C:\Python312\Lib\json\encoder.py", line 200, in encode
    chunks = self.iterencode(o, _one_shot=True)
  File "C:\Python312\Lib\json\encoder.py", line 258, in iterencode
    return _iterencode(o, 0)
  File "C:\Python312\Lib\json\encoder.py", line 180, in default
    raise TypeError(f'Object of type {o.__class__.__name__} '
TypeError: Object of type Decimal is not JSON serializable
```

Diagnostic observations:

- In the same captured-stream environment: sys.stdout.encoding = utf-8; sys.flags.utf8_mode = 0.
- data includes Decimal("1.25"), whose intended wire representation is an exact decimal string. No custom JSON encoder is configured. Serialization fails before print writes anything.
