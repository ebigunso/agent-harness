---
id: rb-persistent-shell-cwd-normalization-05
section: rb-persistent-shell-cwd-normalization
type: planted
---
Task framing: Diagnose the failed command and give the smallest safe remediation and confirmation.

Synthetic diagnostic scenario; recorded paths and retry results are constructed for this example.

Environment: Windows 11 23H2 build 22631; PowerShell 7.4.6; .NET SDK 8.0.404. Intended execution base: C:/work/inventory.

Prior command in this same persistent shell: `Set-Location -LiteralPath 'C:/work/inventory/src'` (exit/status 0, stdout/stderr empty).

State captured before any repair:

Command: `pwd`; exit/status 0; stderr empty. Path output: `C:/work/inventory/src`.

Command: `Get-ChildItem -Name`; exit/status 0; stderr empty. stdout:
```text
Inventory.csproj
```

Failing command: `dotnet test Tests/Tests.csproj`

Exit code / shell status: 1

stdout:
```text
MSBUILD : error MSB1009: Project file does not exist.
Switch: Tests/Tests.csproj
```

stderr:
```text
(empty)
```

Read-only absolute-path inspection confirms these existing entries under the intended base:
```text
C:/work/inventory/Tests/Tests.csproj
C:/work/inventory/src/Inventory.csproj
```

Captured comparison:

1. `Set-Location -LiteralPath 'C:/work/inventory'` — exit/status 0; stdout/stderr empty.
2. `pwd` — normalized cwd C:/work/inventory; exit/status 0.
3. `dotnet test Tests/Tests.csproj` — exit/status 0.

stdout:
```text
Passed!  - Failed:     0, Passed:     1, Skipped:     0, Total:     1, Duration: 12 ms - Tests.dll (net8.0)
```

stderr:
```text
(empty)
```

Final `pwd`: C:/work/inventory; exit/status 0.

Diagnostic observations: The tool UI still displays C:/work/inventory as its remembered workspace root; the persistent shell has its own cwd, shown above. No code, branch, PATH, dependency, configuration or permission change occurred between attempts. All referenced files are accessible. The original command is repeated unchanged; only the explicit navigation differs.
