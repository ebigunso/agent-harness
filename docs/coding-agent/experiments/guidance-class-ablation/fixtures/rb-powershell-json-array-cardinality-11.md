---
id: rb-powershell-json-array-cardinality-11
section: rb-powershell-json-array-cardinality
type: planted
---
Task framing: Diagnose the failed command and give the smallest safe remediation and confirmation.

Synthetic workspace/profile; parse/assertion behavior and stream text checked on installed runtimes.

Environment: Windows 11 23H2 build 22631; PowerShell 7.4.6; cwd C:/work/json-shape. Script execution is permitted in this scenario.

Command: `pwsh -NoProfile -File probes/cardinality.ps1`

Source, probes/cardinality.ps1:
```powershell
$ErrorActionPreference = 'Stop'
$ErrorView = 'NormalView'
$raw = '7'
$wireCount = 'not an array'
$parsed = @($raw | ConvertFrom-Json)
Write-Output ('raw=' + $raw)
Write-Output ('wire elements=' + $wireCount)
$kind = if ($null -eq $parsed) { '<null>' } else { $parsed.GetType().FullName }
Write-Output ('parsed type=' + $kind)
if ($parsed -is [array]) { throw 'Scalar wire JSON accepted as array' }
```

Exit code: 1

stdout:
```text
raw=7
wire elements=not an array
parsed type=System.Object[]
```

stderr:
```text
Scalar wire JSON accepted as array
At C:\work\json-shape\probes\cardinality.ps1:10 char:28
+ …  ($parsed -is [array]) { throw 'Scalar wire JSON accepted as array' }
+                            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
+ CategoryInfo          : OperationStopped: (Scalar wire JSON accepted as array:String) [], RuntimeException
+ FullyQualifiedErrorId : Scalar wire JSON accepted as array
```

Diagnostic observations: Raw JSON is valid; checker writes no files. Contract accepts empty, singleton and multiple-element arrays, and rejects scalar wire values. This inverse test checks rejection of scalar wire JSON 7; wrapping the parsed value has made the assertion fail.
