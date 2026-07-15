# Python Unicode output fails on Windows consoles (CP932/legacy code pages)

## Symptoms

- a Python command fails with `UnicodeEncodeError` while printing output that contains em-dashes, smart quotes, or other non-ASCII characters
- diff/report scripts crash on Windows but run fine on Linux/macOS or in UTF-8 terminals
- the failure happens at print time, after the actual work succeeded

## Likely cause

Python inherits the console code page for stdout on Windows; legacy code pages (CP932, CP1252) cannot encode characters that commonly appear in prose-bearing files, so `print` raises even though the computation succeeded.

## Safe, ordered steps

1) Rerun with the encoding override
- set `PYTHONIOENCODING=utf-8` for the command (e.g. `PYTHONIOENCODING=utf-8 python ...` in Git Bash, or `$env:PYTHONIOENCODING = 'utf-8'; python ...` in PowerShell)

2) Confirm no partial side effects from the failed attempt
- print-time failures normally leave files untouched, but verify if the script writes as well as prints

3) For scripts you own, prefer explicit encoding at the write/print site
- pass `encoding="utf-8"` on file handles rather than relying on console defaults

## Evidence to capture

- the `UnicodeEncodeError` message and the offending character
- the rerun command with the override and its success

## Scope

Windows consoles with legacy code pages; any Python command that prints content from prose-bearing files (adapter bodies, markdown, JSON with typographic characters).
