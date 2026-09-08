---
id: rb-windows-docker-grpc-localhost-ipv6-c4
section: rb-windows-docker-grpc-localhost-ipv6
type: clean
---
Task framing: Diagnose the failed command and give the smallest safe remediation and confirmation.

Synthetic diagnostic scenario; Docker address asymmetry and timing are constructed observations, not a claim of live reproduction.

Environment: Windows 11 23H2 build 22631; PowerShell 7.4.6; Docker Desktop 4.35.1, WSL2 backend; .NET SDK 8.0.404; Grpc.Net.Client 2.67.0; cwd C:/work/grpc-local. Service port 50051 is plaintext h2c gRPC, sibling port 50080 is HTTP/1.1 health. There is no TLS/certificate-name check. Project probe files and dependencies exist, are validated, and built/cached.

Probe contract: The project probe accepts --target, --timeout (seconds; Go accepts a duration), and where shown --method. It prints response values to stdout only after a successful call. It explicitly maps deadline status to process exit 2 and stderr "DEADLINE_EXCEEDED: deadline expired after 2s"; UNAVAILABLE maps to 2, PERMISSION_DENIED and UNIMPLEMENTED to 3. These are probe-defined normalized messages, not claims about each library's default CLI formatting. It does not override localhost resolution or retry with a different address.

Command: `dotnet run --project probes/GrpcProbe -- --target 127.0.0.1:50051 --method Absent`

Exit code: 3

stdout:
```text
(empty)
```

stderr:
```text
UNIMPLEMENTED: unknown method Absent
```

Address-only comparison:

Command: `dotnet run --project probes/GrpcProbe -- --target localhost:50051 --method Absent`

Exit code: 3

stdout:
```text
(empty)
```

stderr:
```text
UNIMPLEMENTED: unknown method Absent
```

HTTP sibling comparison:

Command:
```powershell
curl.exe --silent --show-error --max-time 2 --write-out '\nhttp_code=%{http_code} total_seconds=%{time_total}\n' http://localhost:50080/health
```
Exit code: 0.

stdout:
```text
200 OK
http_code=200 total_seconds=0.012000
```

stderr: (empty).

Diagnostic observations: Both addresses return the same response promptly. Server access logs record the absent method; the deployed descriptor exposes Ping, not Absent. Probe has a default two-second deadline when --timeout is omitted. Transport succeeds.

Service/port evidence:
```text
method=Absent transport=h2c status=UNIMPLEMENTED
```
