# Coding Agent Orchestration Harness

This plugin provides a shared orchestration harness for GitHub Copilot, Claude Code, and Codex.

## Runtime Paths

- Copilot agents: `agents/*.md`
- Claude agents: `claude/agents/*.md`
- Codex inert templates: `codex/agent-templates/*.toml`
- Codex loader snippet: `codex/snippets/AGENTS.md`
- Shared skills: `skills/`

Runtime adapters route to `skills/orchestration-harness/SKILL.md`, the canonical runtime workflow policy.

## Role Map

Logical roles are stable; physical names vary by runtime.

| Logical role | Copilot | Claude | Codex |
|---|---|---|---|
| Orchestrator | Orchestrator | harness-orchestrator | main Codex thread + `$orchestration-harness` loader |
| Researcher | Researcher | harness-researcher | harness_researcher |
| Worker | Worker | harness-worker | harness_worker |
| Reviewer | Reviewer | harness-reviewer | harness_reviewer |

Canonical reference: `skills/orchestration-harness/references/runtime-role-map.md`.

## Key Skills

- `orchestration-harness`: canonical Orchestrator policy and hard gates.
- `plan-format`: Task_X plan structure and waves.
- `subagent-strategy`: dispatch strategy and prompt checklists.
- `subagent-report-contract`: Worker YAML report contract.
- `worker-ui-probes`: bounded Worker UI probe policy.
- `wave-integration`: Orchestrator-owned Worker wave integration checklist.
- `runtime-adapter-contract`: runtime adapter maintenance rules.
- `playwright-e2e-evidence`: UI/E2E evidence shape.
- `git-workflow`: safe Git workflow.
- `rulebook`: repository rule updates.
- `improvement-loop`: post-correction handling.
- `workspace-troubleshooting`: systematic failure triage.
- `skills-maintenance`: first-party skill maintenance.

## Validators

```bash
python scripts/validate_harness_package.py
python scripts/run_validation_smoke_tests.py
python skills/plan-format/scripts/validate_plan.py --file tests/fixtures/valid-plan.md --mode balanced
python skills/subagent-report-contract/scripts/validate_worker_report.py --file tests/fixtures/valid-worker-report.yaml
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
