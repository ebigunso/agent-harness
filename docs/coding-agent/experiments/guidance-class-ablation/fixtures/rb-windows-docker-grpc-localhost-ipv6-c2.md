---
id: rb-windows-docker-grpc-localhost-ipv6-c2
section: rb-windows-docker-grpc-localhost-ipv6
type: clean
---
Task framing: Diagnose the failed command and give the smallest safe remediation and confirmation.

Synthetic diagnostic scenario; Docker address asymmetry and timing are constructed observations, not a claim of live reproduction.

Environment: Windows 11 23H2 build 22631; PowerShell 7.4.6; Docker Desktop 4.35.1, WSL2 backend; Node 20.18.0; @grpc/grpc-js 1.12.2; cwd C:/work/grpc-local. Service port 50051 is plaintext h2c gRPC, sibling port 50080 is HTTP/1.1 health. There is no TLS/certificate-name check. Project probe files and dependencies exist, are validated, and built/cached.

Probe contract: The project probe accepts --target, --timeout (seconds; Go accepts a duration), and where shown --method. It prints response values to stdout only after a successful call. It explicitly maps deadline status to process exit 2 and stderr "DEADLINE_EXCEEDED: deadline expired after 2s"; UNAVAILABLE maps to 2, PERMISSION_DENIED and UNIMPLEMENTED to 3. These are probe-defined normalized messages, not claims about each library's default CLI formatting. It does not override localhost resolution or retry with a different address.

Command: `node probes/unary.mjs --target localhost:50052 --timeout 2`

Exit code: 2

stdout:
```text
(empty)
```

stderr:
```text
UNAVAILABLE: connection refused
```

Address-only comparison:

Command: `node probes/unary.mjs --target 127.0.0.1:50052 --timeout 2`

Exit code: 2

stdout:
```text
(empty)
```

stderr:
```text
UNAVAILABLE: connection refused
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

Diagnostic observations: Docker port inspection shows only host 50051 for gRPC and 50080 for health. No listener or mapping exists on 50052. Both refused calls are absent from the server invocation log. Correctly targeted 50051 probes are healthy.

Service/port evidence:
```text
published=50051/tcp,50080/tcp; requested=50052/tcp; no invocation
```
