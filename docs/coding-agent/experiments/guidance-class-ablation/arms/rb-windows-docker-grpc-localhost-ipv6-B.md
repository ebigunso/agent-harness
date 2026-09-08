# gRPC hangs against Docker Desktop published ports on Windows (REST sibling port fine)

## Symptoms
- a gRPC client targeting `localhost:<port>` on Docker Desktop for Windows hangs until client timeout
- a REST/HTTP endpoint on a sibling published port of the same service responds fast
- the service's own logs show no incoming request for the hanging gRPC calls

## Likely cause
`localhost` can resolve to IPv6 `::1` first. Docker Desktop's IPv6 port proxy accepts the TCP connect but stalls HTTP/2, so the gRPC channel hangs at the transport layer while plain HTTP/1.1 (REST) still works. The service itself is healthy.

## Safe, ordered steps

1) Test IPv4 vs IPv6 connect paths before suspecting the service
- retry the gRPC call with `127.0.0.1:<port>` instead of `localhost:<port>`
- if IPv4 works and `localhost` hangs, the asymmetry is the loopback resolution, not the service

2) Fix the connection string
- prefer `127.0.0.1` over `localhost` in local connection strings for gRPC clients targeting Docker Desktop published ports on Windows

3) Only if IPv4 also fails
- then investigate the service, port publishing, and container health as usual

## Evidence to capture
- exact target address used (`localhost` vs `127.0.0.1`) and port
- gRPC timeout/error output vs REST response timing on the sibling port
- result of the IPv4 retry

## Scope
Windows + Docker Desktop published ports; gRPC (HTTP/2) clients connecting to local containers.
