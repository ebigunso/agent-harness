# PowerShell one-element JSON arrays appear scalar after ConvertFrom-Json

## Symptoms
- a JSON payload known to contain an array validates as "not an array" (or vice versa) in PowerShell when the array has exactly one element
- `-is [array]` checks give different results for the same JSON shape depending on element count
- cardinality assertions on JSON pass or fail nondeterministically as data volume changes

## Likely cause
PowerShell's pipeline unrolls collections: a one-element array emitted through the pipeline after `ConvertFrom-Json` arrives as the bare element, so a post-pipeline `-is [array]` check reports scalar even though the serialized JSON was framed with `[`/`]`.

## Safe, ordered steps

1) Never treat a post-pipeline `-is [array]` check as proof of JSON array framing
- the check reflects pipeline unrolling, not the wire format

2) Assert framing on the raw serialized value
- check that the trimmed raw JSON string starts with `[` and ends with `]` when validating cardinality-stable JSON

3) Or parse without enumeration (PowerShell 7+/pwsh only)
- use `ConvertFrom-Json -NoEnumerate` (and avoid re-piping the result) so one-element arrays stay arrays
- `-NoEnumerate` does not exist in Windows PowerShell 5.1; there, use step 2 (raw `[`/`]` framing) instead

## Evidence to capture
- the raw serialized JSON (or at least its first/last characters)
- element count of the array under test
- the exact parse + assertion expression used

## Scope
Windows/PowerShell (Windows PowerShell and pwsh); any JSON validation where array-vs-scalar framing matters.
