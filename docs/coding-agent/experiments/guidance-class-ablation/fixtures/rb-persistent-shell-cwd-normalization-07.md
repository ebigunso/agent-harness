---
id: rb-persistent-shell-cwd-normalization-07
section: rb-persistent-shell-cwd-normalization
type: planted
---
Task framing: Diagnose the failed command and give the smallest safe remediation and confirmation.

Synthetic diagnostic scenario; recorded paths and retry results are constructed for this example.

Environment: Windows 11 23H2 build 22631; PowerShell 7.4.6; Go 1.23.3. Intended execution base: C:/work/go-service.

Prior command in this same persistent shell: `Set-Location -LiteralPath 'C:/work/assets'` (exit/status 0, stdout/stderr empty).

State captured before any repair:

Command: `pwd`; exit/status 0; stderr empty. Path output: `C:/work/assets`.

Command: `Get-ChildItem -Name`; exit/status 0; stderr empty. stdout:
```text
logo.svg
```

Failing command: `go test ./...`

Exit code / shell status: 1

stdout:
```text
FAIL	./... [setup failed]
FAIL
```

stderr:
```text
pattern ./...: directory prefix . does not contain main module or its selected dependencies
```

Read-only absolute-path inspection confirms these existing entries under the intended base:
```text
C:/work/go-service/go.mod
C:/work/go-service/service_test.go
```

Captured comparison:

1. `Set-Location -LiteralPath 'C:/work/go-service'` — exit/status 0; stdout/stderr empty.
2. `pwd` — normalized cwd C:/work/go-service; exit/status 0.
3. `go test ./...` — exit/status 0.

stdout:
```text
ok  	example.test/go-service	0.015s
```

stderr:
```text
(empty)
```

Final `pwd`: C:/work/go-service; exit/status 0.

Diagnostic observations: The tool UI still displays C:/work/go-service as its remembered workspace root; the persistent shell has its own cwd, shown above. No code, branch, PATH, dependency, configuration or permission change occurred between attempts. All referenced files are accessible. The original command is repeated unchanged; only the explicit navigation differs.
