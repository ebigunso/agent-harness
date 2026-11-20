# Coding Agent Orchestration Harness

This plugin provides a shared orchestration harness for GitHub Copilot, Claude Code, and Codex.

## Updating To 1.8.0

Two behaviours differ from versions before 1.8.0:

- A session with no role chosen is Counsel: in Claude Code wherever the plugin's settings load, and in Codex and GitHub Copilot in a repository where the harness's setup has written that default. For the Orchestrator, open the session as the Orchestrator: in Claude Code launch it with `claude --agent coding-agent-orchestration-harness:harness-orchestrator` or set `agent` in your own settings, either of which overrides the plugin's default; in GitHub Copilot select the `Orchestrator` agent in the Agent dropdown; in Codex invoke `$orchestration-harness` by name in the first message.
- The managed block in the Codex home (`~/.codex/AGENTS.md`) does not route coding requests to the Orchestrator: it gives a session no role and says how each role is chosen. A block written by an earlier version keeps routing them until it is replaced; run the Codex bootstrap again with `--user-instructions add` to replace it. For the Orchestrator in Codex, invoke `$orchestration-harness` by name in the first message.

A repository set up by an earlier version keeps its means to start and watch a session in `docs/coding-agent/rules/common.md`; the next refresh of its rule suite moves them to `docs/coding-agent/rules/sessions.md`, which only Counsel and the Orchestrator read.

## Runtime Paths

- Copilot agents: `agents/*.md`
- Claude agents: `claude/agents/*.md`
- Claude Code default agent: `settings.json`
- Codex inert templates: `codex/agent-templates/*.toml`
- Codex home instructions snippet: `codex/snippets/AGENTS.md`
- Default-role block that setup writes into a repository: `skills/rulebook/references/rule-suite-templates.md`
- Shared skills: `skills/`

Runtime adapters route to `skills/orchestration-harness/SKILL.md`, the canonical runtime workflow policy. The Counsel agents route to `skills/counsel/SKILL.md` instead and never load `orchestration-harness`.

## Role Map

Logical roles are stable; physical names vary by runtime.

| Logical role | Copilot | Claude | Codex |
|---|---|---|---|
| Orchestrator | Orchestrator | harness-orchestrator | main Codex thread following `$orchestration-harness` |
| Researcher | Researcher | harness-researcher | harness_researcher |
| Worker | Worker | harness-worker | harness_worker |
| Reviewer | Reviewer | harness-reviewer | harness_reviewer |
| Auditor | Auditor | harness-auditor | harness_auditor |
| Counsel | Counsel | harness-counsel | main Codex thread following `$counsel` |

Canonical reference: `skills/orchestration-harness/references/runtime-role-map.md`.

## Counsel Session

Counsel is a separate session from the Orchestrator: the owner opens it to discuss what the product does or should do, at the level of behaviour and decisions. It is never dispatched as a subagent, dispatches only the read-only Researcher, and does not read plans or diffs. It may do quick reads of code in service of the discussion; grounding that needs bulk code reading, and every check-up on the project's state, goes to a Researcher.

In Claude Code a session opened with no agent chosen is Counsel; in Codex and GitHub Copilot that default exists only in a repository where the harness's setup has written it. How a session gets either role in each runtime, and the limits of each way, is in `skills/orchestration-harness/references/runtime-role-map.md`, How A Session Gets Its Role. The Codex bootstrap installs no Counsel template.

## Key Skills

- `orchestration-harness`: canonical Orchestrator policy and hard gates.
- `counsel`: canonical Counsel session policy.
- `value-documents`: forms, locations and ownership of the value documents; the home of no role.
- `plan-format`: Task_X plan structure and waves.
- `subagent-strategy`: dispatch strategy and prompt checklists.
- `subagent-report-contract`: Worker YAML report contract.
- `wave-integration`: Orchestrator-owned Worker wave integration checklist.
- `runtime-adapter-contract`: runtime adapter maintenance rules.
- `playwright-e2e-evidence`: UI/E2E evidence shape.
- `git-workflow`: safe Git workflow.
- `rulebook`: repository rule updates.
- `improvement-loop`: post-correction handling.
- `workspace-troubleshooting`: systematic failure triage.
- `skills-maintenance`: first-party skill maintenance.

## Validators

Run these commands from this plugin directory (`plugins/coding-agent-orchestration-harness/` in the repository checkout). Test fixtures and the watcher self-check live outside the distributed plugin, under the repository's `tests/coding-agent-orchestration-harness/`:

```bash
python scripts/validate_harness_package.py
python scripts/run_validation_smoke_tests.py
python skills/plan-format/scripts/validate_plan.py --file ../../tests/coding-agent-orchestration-harness/fixtures/valid-plan.md --mode balanced
python skills/subagent-report-contract/scripts/validate_worker_report.py --file ../../tests/coding-agent-orchestration-harness/fixtures/valid-worker-report.yaml
```

Validation is contract-first: hard for structure and required evidence, flexible for exact prose and strategy.

## Codex Bootstrap

Codex agent templates are installed by:

```bash
python skills/codex-harness-bootstrap/scripts/install_codex_harness.py
```

Useful flags:

- `--scope user` installs into `~/.codex/agents/`.
- `--scope repo` installs into `.codex/agents/` under the selected repository.
- `--repo-root <path>` selects the target repository for repo scope.
- `--dry-run` previews writes/skips without writing files.
- `--check` compares installed files against source templates and requires the managed manifest for a successful check.
- `--verify` checks required installed files and the managed install manifest.
- `--overwrite-agents` replaces existing installed templates.
- `--user-instructions add|skip|ask` controls the user-scope `AGENTS.md` block.

Normal installs write `.coding-agent-orchestration-harness-install.json` in the target agents directory by default. Use `--no-write-manifest` only when manifest creation is intentionally unwanted.
