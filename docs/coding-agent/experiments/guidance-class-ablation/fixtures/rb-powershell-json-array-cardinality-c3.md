---
id: rb-powershell-json-array-cardinality-c3
section: rb-powershell-json-array-cardinality
type: clean
---
Task framing: Diagnose the failed command and give the smallest safe remediation and confirmation.

Synthetic workspace/profile; parse/assertion behavior and stream text checked on installed runtimes.

Environment: Windows 11 23H2 build 22631; Windows PowerShell 5.1.22621.4391; cwd C:/work/json-shape. Script execution is permitted in this scenario.

Command: `powershell.exe -NoProfile -File probes/parse.ps1`

Source, probes/parse.ps1:
```powershell
$ErrorActionPreference = 'Stop'
$ErrorView = 'NormalView'
$raw = '[1,'
Write-Output ('raw=' + $raw)
$parsed = $raw | ConvertFrom-Json
```

Exit code: 1

stdout:
```text
raw=[1,
```

stderr:
```text
ConvertFrom-Json : Invalid array passed in, extra trailing ','. (3): [1,
At C:\work\json-shape\probes\parse.ps1:5 char:18
+ $parsed = $raw | ConvertFrom-Json
+                  ~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (:) [ConvertFrom-Json], ArgumentException
    + FullyQualifiedErrorId : System.ArgumentException,Microsoft.PowerShell.Commands.ConvertFromJsonCommand
```

Diagnostic observations: Payload ends after the comma; no closing bracket or second value. Syntax fails before any array-type assertion. No files are modified.
