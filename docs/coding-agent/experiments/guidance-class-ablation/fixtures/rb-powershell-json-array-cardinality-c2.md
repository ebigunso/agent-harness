---
id: rb-powershell-json-array-cardinality-c2
section: rb-powershell-json-array-cardinality
type: clean
---
Task framing: Diagnose the failed command and give the smallest safe remediation and confirmation.

Synthetic workspace/profile; parse/assertion behavior and stream text checked on installed runtimes.

Environment: Windows 11 23H2 build 22631; PowerShell 7.4.6; cwd C:/work/json-shape. Script execution is permitted in this scenario.

Command: `pwsh -NoProfile -File probes/check-items.ps1`

Source, probes/check-items.ps1:
```powershell
$ErrorActionPreference = 'Stop'
$ErrorView = 'NormalView'
$raw = '[{"id":7}]'
$parsed = $raw | ConvertFrom-Json -NoEnumerate
Write-Output ('raw=' + $raw)
Write-Output ('parsed type=' + $parsed.GetType().FullName)
if ($parsed -isnot [array]) { throw 'Expected JSON array' }
if (-not $parsed[0].PSObject.Properties['name']) { throw 'item[0].name is required' }
```

Exit code: 1

stdout:
```text
raw=[{"id":7}]
parsed type=System.Object[]
```

stderr:
```text
item[0].name is required
At C:\work\json-shape\probes\check-items.ps1:8 char:52
+ … [0].PSObject.Properties['name']) { throw 'item[0].name is required' }
+                                      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
+ CategoryInfo          : OperationStopped: (item[0].name is required:String) [], RuntimeException
+ FullyQualifiedErrorId : item[0].name is required
```

Diagnostic observations: Shape check passed. The schema requires both id and name; name is absent. Parsed result is never re-piped. No files are modified.
