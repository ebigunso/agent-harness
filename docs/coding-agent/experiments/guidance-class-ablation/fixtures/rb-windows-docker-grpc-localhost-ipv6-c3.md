---
id: rb-windows-docker-grpc-localhost-ipv6-c3
section: rb-windows-docker-grpc-localhost-ipv6
type: clean
---
Task framing: Diagnose the failed command and give the smallest safe remediation and confirmation.

Synthetic diagnostic scenario; Docker address asymmetry and timing are constructed observations, not a claim of live reproduction.

Environment: Windows 11 23H2 build 22631; PowerShell 7.4.6; Docker Desktop 4.35.1, WSL2 backend; Java 21.0.5; grpc-java 1.68.1; cwd C:/work/grpc-local. Service port 50051 is plaintext h2c gRPC, sibling port 50080 is HTTP/1.1 health. There is no TLS/certificate-name check. Project probe files and dependencies exist, are validated, and built/cached.

Probe contract: The project probe accepts --target, --timeout (seconds; Go accepts a duration), and where shown --method. It prints response values to stdout only after a successful call. It explicitly maps deadline status to process exit 2 and stderr "DEADLINE_EXCEEDED: deadline expired after 2s"; UNAVAILABLE maps to 2, PERMISSION_DENIED and UNIMPLEMENTED to 3. These are probe-defined normalized messages, not claims about each library's default CLI formatting. It does not override localhost resolution or retry with a different address.

Command: `java -jar probes/grpc-probe.jar --target localhost:50051 --method Private --timeout 2`

Exit code: 3

stdout:
```text
(empty)
```

stderr:
```text
PERMISSION_DENIED: role required
```

Address-only comparison:

Command: `java -jar probes/grpc-probe.jar --target 127.0.0.1:50051 --method Private --timeout 2`

Exit code: 3

stdout:
```text
(empty)
```

stderr:
```text
PERMISSION_DENIED: role required
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

Diagnostic observations: The response arrives in 15 ms. The server policy interceptor records both requests, then rejects the missing required role. Port publishing and HTTP/2 transport both work; no credential values are included.

Service/port evidence:
```text
method=Private invoked=true policy=role-required status=PERMISSION_DENIED
```
