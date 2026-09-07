# Python Unicode output fails on Windows consoles (CP932/legacy code pages)

## Symptoms

- a Python command fails with `UnicodeEncodeError` while printing output that contains em-dashes, smart quotes, or other non-ASCII characters
- diff/report scripts crash on Windows but run fine on Linux/macOS or in UTF-8 terminals
- the failure happens at print time, after the actual work succeeded

## Likely cause

Python inherits the console code page for stdout on Windows; non-UTF-8 legacy code pages (e.g. CP932) cannot encode characters that commonly appear in prose-bearing files, so `print` raises even though the computation succeeded. Which characters fail depends on the code page.

## Safe, ordered steps

1) Rerun with the encoding override
- set `PYTHONIOENCODING=utf-8` for the command (e.g. `PYTHONIOENCODING=utf-8 python ...` in Git Bash, or `$env:PYTHONIOENCODING = 'utf-8'; python ...` in PowerShell)

2) Confirm no partial side effects from the failed attempt
- print-time failures normally leave files untouched, but verify if the script writes as well as prints

3) For scripts you own, fix the output site explicitly
- console output: call `sys.stdout.reconfigure(encoding="utf-8")` at startup instead of relying on the console code page
- file output: pass `encoding="utf-8"` on file handles rather than relying on locale defaults

## Evidence to capture

- the `UnicodeEncodeError` message and the offending character
- the rerun command with the override and its success

## Scope

Windows consoles with legacy code pages; any Python command that prints content from prose-bearing files (adapter bodies, markdown, JSON with typographic characters).
