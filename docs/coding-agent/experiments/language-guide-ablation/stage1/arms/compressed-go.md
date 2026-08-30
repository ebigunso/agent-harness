# Go review checklist (compressed)

- Wrap errors with `%w`; classify with `errors.Is`/`errors.As` — never match `err.Error()` strings.
- Every goroutine has a guaranteed termination path (ctx, timeout, or bound); no unbounded spawning.
- Shared mutable state (maps, slices) is synchronized under one consistent scheme.
- `context.Context` flows through all cancellable work; never swap in `context.Background()` mid-chain.
- No panic/recover as routine control flow.
- Interfaces live at consumer boundaries, minimal; no interface-per-struct.
- Transport/storage concerns stay out of domain logic.
- Channel close/send ownership is explicit and single-owner.
