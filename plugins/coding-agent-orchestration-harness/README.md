# Coding Agent Orchestration Harness

This plugin provides a shared orchestration harness for GitHub Copilot, Claude Code, and Codex.

## Runtime Paths

- Copilot agents: `agents/*.md`
- Claude agents: `claude/agents/*.md`
- Codex inert templates: `codex/agent-templates/*.toml`
- Codex loader snippet: `codex/snippets/AGENTS.md`
- Shared skills: `skills/`

Runtime adapters route to `skills/orchestration-harness/SKILL.md`, the canonical runtime workflow policy. The Counsel agents route to `skills/counsel/SKILL.md` instead and never load `orchestration-harness`.

## Role Map

Logical roles are stable; physical names vary by runtime.

| Logical role | Copilot | Claude | Codex |
|---|---|---|---|
| Orchestrator | Orchestrator | harness-orchestrator | main Codex thread + `$orchestration-harness` loader |
| Researcher | Researcher | harness-researcher | harness_researcher |
| Worker | Worker | harness-worker | harness_worker |
| Reviewer | Reviewer | harness-reviewer | harness_reviewer |
| Counsel | harness-counsel | harness-counsel | main Codex thread + the `$counsel` skill invoked explicitly by the owner |

Canonical reference: `skills/orchestration-harness/references/runtime-role-map.md`.

## Counsel Session

Counsel is a separate session from the Orchestrator: the owner opens it to discuss what the product does or should do, at the level of behaviour and decisions. It is never dispatched as a subagent, dispatches only the read-only Researcher, and does not read plans or diffs. It may do quick reads of code in service of the discussion; grounding that needs bulk code reading, and every check-up on the project's state, goes to a Researcher.

- Copilot and Claude Code: select the `harness-counsel` agent.
- Codex: open a session and invoke the `$counsel` skill explicitly. The managed `AGENTS.md` loader does not route to it, and the bootstrap installs no Counsel template.

## Key Skills

- `orchestration-harness`: canonical Orchestrator policy and hard gates.
- `counsel`: canonical Counsel session policy and the value-document forms.
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
- `--user-instructions add|skip|ask` controls the user-scope loader block.

Normal installs write `.coding-agent-orchestration-harness-install.json` in the target agents directory by default. Use `--no-write-manifest` only when manifest creation is intentionally unwanted.

## ADRs

Design and implementation decisions are recorded under:

`../../docs/coding-agent-orchestration-harness/decisions/`
