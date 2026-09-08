# cp-8 grading key

Author-only; exclude from review input. A full hit names the mechanism/location and repair direction. Secondary overlap is permitted by the frozen primary-mapping protocol.

| ID | Primary check | Planted defect | A hit must state |
|---|---|---|---|
| cp-8-01 | “Abstract only when multiple concrete uses justify it.” | C# one CSV exporter gains reflection, provider registry, and six unused configuration knobs. | Name unused registry/knobs and keep the existing direct exporter until a second concrete need. |
| cp-8-02 | “Abstract only when multiple concrete uses justify it.” | Python one command handler adds a plugin registry, importlib discovery, and provider configuration although the sole handler is locally called once. | Name speculative discovery/registry and use the existing direct call until another concrete handler needs it. |
| cp-8-03 | “Keep dependency direction intentional and acyclic where practical.” | Go two packages import each other through a new common facade solely to avoid moving a shared value type; current build needs an import-cycle workaround. | Identify the dependency cycle and place stable shared type in existing inward package rather than add facade workarounds. |
| cp-8-04 | “Is new complexity justified by measurable maintenance benefit?” | Java single fixed retry delay gets a strategy interface, reflective factory, and per-service YAML class name despite no alternative policy. | Name unsupported retry extensibility cost and keep direct installed retry configuration. |
| cp-8-05 | “Remove accidental complexity before introducing abstraction.” | TypeScript UI renders one fixed label via a generic expression interpreter with operator registry and serialization instead of ordinary conditional code. | Identify expression machinery for fixed behavior; use direct native conditional rendering. |
| cp-8-06 | “Does abstraction reduce or increase cognitive load?” | Rust small two-variant dispatch introduces code-generation build script and proc macro solely to emit a match already present nearby. | Name generated indirection without concrete benefit; retain explicit local match. |
| cp-8-07 | “Abstract only when multiple concrete uses justify it.” | C# one local JSON file read adds repository/unit-of-work abstractions plus transaction API though no transaction or alternate store exists. | Name speculative persistence layers and use existing direct file read/parse path. |
| cp-8-08 | “Remove accidental complexity before introducing abstraction.” | Ruby new string-format helper duplicates installed standard formatter behind three adapters and a custom token parser for the same fixed template. | Reuse the existing formatter; identify unnecessary parser/adapters rather than polish them. |
| cp-8-09 | “Is new complexity justified by measurable maintenance benefit?” | PHP a seven-line mapping duplicates an existing same-semantics shared mapper in each of six request handlers. | Identify concrete duplicate transformations and reuse the already-present mapper with the same boundary contract. |
| cp-8-10 | “Is new complexity justified by measurable maintenance benefit?” | Kotlin notification module adds an event bus for one synchronous producer and one consumer, losing simple return/error flow with no asynchronous need. | Name unnecessary bus and restore direct call/result flow absent a measured multi-consumer need. |
| cp-8-11 | “Does abstraction reduce or increase cognitive load?” | C++ a bounded three-item lookup gains template metaprogramming with custom typelists instead of existing array lookup, without performance evidence. | Identify opaque compile-time machinery and use existing small lookup unless an evidenced constraint justifies it. |
| cp-8-12 | “Is new complexity justified by measurable maintenance benefit?” | Scala feature adds a second parallel dependency-injection container for one adapter while the composition root already supports direct constructor wiring. | Name redundant container/lifetime graph and wire adapter through existing composition root. |

## Clean decoys

No blocking target defect. Nitpicks are neutral only when optional; unnecessary blocking/rework requests are false positives.

| ID | Intended correct behavior | Known acceptable optional nitpick |
|---|---|---|
| cp-8-c1 | C# two live exporters share a small formatter with explicit format-specific logic. | A third implementation. |
| cp-8-c2 | Python removes a one-use registry in favor of existing direct call with equivalent behavior. | Future plugin hook. |
| cp-8-c3 | Go acyclic dependencies use an existing narrow interface for two current stores. | Removing the justified interface. |
| cp-8-c4 | Rust local match covers two actual variants. | Generic dispatch macro. |
