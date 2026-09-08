---
id: rb-powershell-json-array-cardinality-c1
section: rb-powershell-json-array-cardinality
type: clean
---
Task framing: Diagnose the failed command and give the smallest safe remediation and confirmation.

Synthetic workspace/profile; parse/assertion behavior and stream text checked on installed runtimes.

Environment: Windows 11 23H2 build 22631; PowerShell 7.4.6; cwd C:/work/json-shape. Script execution is permitted in this scenario.

Command: `pwsh -NoProfile -File probes/require-array.ps1`

Source, probes/require-array.ps1:
```powershell
$ErrorActionPreference = 'Stop'
$ErrorView = 'NormalView'
$raw = '{"id":7}'
$null = $raw | ConvertFrom-Json
Write-Output ('raw=' + $raw)
$trimmed = $raw.Trim()
if (-not ($trimmed.StartsWith('[') -and $trimmed.EndsWith(']'))) {
    throw 'Expected array framing'
}
```

Exit code: 1

stdout:
```text
raw={"id":7}
```

stderr:
```text
Expected array framing
At C:\work\json-shape\probes\require-array.ps1:8 char:5
+     throw 'Expected array framing'
+     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
+ CategoryInfo          : OperationStopped: (Expected array framing:String) [], RuntimeException
+ FullyQualifiedErrorId : Expected array framing
```

Diagnostic observations: Input requires an array. The raw object is syntactically valid but lacks the required outer framing. No files are modified.
