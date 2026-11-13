<!-- coding-agent-orchestration-harness:start -->
## Coding Agent Orchestration Harness

This block gives a session no role; it says how a role of the coding-agent orchestration harness is chosen.

- A session whose first message invokes `$orchestration-harness` by name is the Orchestrator, and one whose first message invokes `$counsel` by name is Counsel: load and follow that skill and not the other. If the skill is unavailable, say so.
- Where the instructions of the repository the session is opened in say which role a session with no role chosen holds, they govern.
- Otherwise a session holds no role of the harness, and a skill loaded because its description matched gives it none.
<!-- coding-agent-orchestration-harness:end -->
