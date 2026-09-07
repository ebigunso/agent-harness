---
id: rb-powershell-json-array-cardinality-05
section: rb-powershell-json-array-cardinality
type: planted
---
Task framing: Diagnose the failed command and give the smallest safe remediation and confirmation.

Synthetic workspace/profile; parse/assertion behavior and stream text checked on installed runtimes.

Environment: Windows 11 23H2 build 22631; Windows PowerShell 5.1.22621.4391; cwd C:/work/json-shape. Script execution is permitted in this scenario.

Command: `powershell.exe -NoProfile -File probes/cardinality.ps1`

Source, probes/cardinality.ps1:
```powershell
$ErrorActionPreference = 'Stop'
$ErrorView = 'NormalView'
$raw = '[{"id":8}]'
$wireCount = '1'
$parsed = $raw | ConvertFrom-Json | Write-Output
Write-Output ('raw=' + $raw)
Write-Output ('wire elements=' + $wireCount)
$kind = if ($null -eq $parsed) { '<null>' } else { $parsed.GetType().FullName }
Write-Output ('parsed type=' + $kind)
if ($parsed -isnot [array]) { throw 'Expected JSON array' }
```

Exit code: 1

stdout:
```text
raw=[{"id":8}]
wire elements=1
parsed type=System.Management.Automation.PSCustomObject
```

stderr:
```text
Expected JSON array
At C:\work\json-shape\probes\cardinality.ps1:10 char:31
+ if ($parsed -isnot [array]) { throw 'Expected JSON array' }
+                               ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : OperationStopped: (Expected JSON array:String) [], RuntimeException
    + FullyQualifiedErrorId : Expected JSON array
```

Diagnostic observations: Raw JSON is valid; checker writes no files. Contract accepts empty, singleton and multiple-element arrays, and rejects scalar wire values.
