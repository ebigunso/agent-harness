---
id: rb-windows-docker-grpc-localhost-ipv6-05
section: rb-windows-docker-grpc-localhost-ipv6
type: planted
---
Task framing: Diagnose the failed command and give the smallest safe remediation and confirmation.

Synthetic diagnostic scenario; Docker address asymmetry and timing are constructed observations, not a claim of live reproduction.

Environment: Windows 11 23H2 build 22631; PowerShell 7.4.6; Docker Desktop 4.35.1, WSL2 backend; .NET SDK 8.0.404; Grpc.Net.Client 2.67.0; cwd C:/work/grpc-local. Service port 50051 is plaintext h2c gRPC, sibling port 50080 is HTTP/1.1 health. There is no TLS/certificate-name check. Project probe files and dependencies exist, are validated, and built/cached.

Probe contract: The project probe accepts --target, --timeout (seconds; Go accepts a duration), and where shown --method. It prints response values to stdout only after a successful call. It explicitly maps deadline status to process exit 2 and stderr "DEADLINE_EXCEEDED: deadline expired after 2s"; UNAVAILABLE maps to 2, PERMISSION_DENIED and UNIMPLEMENTED to 3. These are probe-defined normalized messages, not claims about each library's default CLI formatting. It does not override localhost resolution or retry with a different address.

Failed unary Echo call:

Command: `dotnet run --project probes/GrpcProbe -- --target localhost:50051 --timeout 2`

Exit code: 2

stdout:
```text
(empty)
```

stderr:
```text
DEADLINE_EXCEEDED: deadline expired after 2s
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

Diagnostic observations:

- Name-resolution trace orders localhost as ::1 then 127.0.0.1; the failed channel uses [::1]:50051. A TCP connect to that endpoint succeeds, but no HTTP/2 response headers arrive before the deadline.
- The service is running; published mappings are host 50051 -> service 50051 and host 50080 -> service 50080. No invocation for the failed call appears in the service interceptor log.

Captured address-only comparison (same method, payload, deadline, server, container and configuration except target):

Command: `dotnet run --project probes/GrpcProbe -- --target 127.0.0.1:50051 --timeout 2`

Exit code: 0

stdout:
```text
pong
```

stderr:
```text
(empty)
```

Service log for the comparison call:
```text
probe method="unary Echo" transport=h2c invoked=true completed=true
```
