# PowerShell one-element JSON arrays appear scalar after ConvertFrom-Json

PowerShell pipelines unroll JSON arrays; post-pipeline -is [array] cannot prove wire framing. Check trimmed raw JSON starts [ and ends ] (not a syntax validator). On pwsh 7+, ConvertFrom-Json -NoEnumerate preserves arrays unless re-piped; Windows PowerShell 5.1 lacks it, so use raw framing. Record raw JSON, element count and exact parse/assertion.
