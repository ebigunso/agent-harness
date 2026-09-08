---
id: rb-powershell-json-array-cardinality-10
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
$raw = '[{"state":"ok"}]'
$wireCount = '1'
$raw = (Invoke-WebRequest http://127.0.0.1:5080/items).Content; $parsed = $raw | ConvertFrom-Json
Write-Output ('raw=' + $raw)
Write-Output ('wire elements=' + $wireCount)
$kind = if ($null -eq $parsed) { '<null>' } else { $parsed.GetType().FullName }
Write-Output ('parsed type=' + $kind)
if ($parsed -isnot [array]) { throw 'Expected JSON array' }
```

Exit code: 1

stdout:
```text
raw=[{"state":"ok"}]
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

Diagnostic observations: Raw JSON is valid; checker writes no files. Contract accepts empty, singleton and multiple-element arrays, and rejects scalar wire values. Node 20.18.0 tiny HTTP producer returns HTTP 200 and Content-Type application/json with exact body [{"state":"ok"}]; independently captured raw response matches. No transport/authentication error. Scenario port is 5080.
