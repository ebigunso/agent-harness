---
id: rb-powershell-json-array-cardinality-c4
section: rb-powershell-json-array-cardinality
type: clean
---
Task framing: Diagnose the failed command and give the smallest safe remediation and confirmation.

Synthetic workspace/profile; parse/assertion behavior and stream text checked on installed runtimes.

Environment: Windows 11 23H2 build 22631; PowerShell 7.4.6; cwd C:/work/json-shape. Script execution is permitted in this scenario.

Command: `pwsh -NoProfile -File probes/unique.ps1`

Source, probes/unique.ps1:
```powershell
$ErrorActionPreference = 'Stop'
$ErrorView = 'NormalView'
$raw = '[1,1]'
$parsed = $raw | ConvertFrom-Json -NoEnumerate
Write-Output ('raw=' + $raw)
Write-Output ('parsed type=' + $parsed.GetType().FullName)
if ($parsed -isnot [array]) { throw 'Expected JSON array' }
$seen = [System.Collections.Generic.HashSet[long]]::new()
foreach ($item in $parsed) {
    if (-not $seen.Add($item)) { throw "Duplicate item $item" }
}
```

Exit code: 1

stdout:
```text
raw=[1,1]
parsed type=System.Object[]
```

stderr:
```text
Duplicate item 1
At C:\work\json-shape\probes\unique.ps1:10 char:34
+     if (-not $seen.Add($item)) { throw "Duplicate item $item" }
+                                  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
+ CategoryInfo          : OperationStopped: (Duplicate item 1:String) [], RuntimeException
+ FullyQualifiedErrorId : Duplicate item 1
```

Diagnostic observations: Contract requires unique integer IDs. Shape and element types are correct; value 1 is repeated. No files are modified.
