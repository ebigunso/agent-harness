#!/usr/bin/env python3
"""Validate harness package structure without validating exact prose."""

from __future__ import annotations

import json
import py_compile
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def warn(warnings: list[str], message: str) -> None:
    warnings.append(message)


def has_frontmatter(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    return text.startswith("---\n") and "\n---\n" in text[4:]


def load_json(path: Path, errors: list[str]) -> dict:
    if not path.exists():
        fail(errors, f"{path}: missing manifest")
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(errors, f"{path}: JSON parse failed: {exc}")
        return {}
    if not isinstance(data, dict):
        fail(errors, f"{path}: manifest root must be a JSON object")
        return {}
    return data


def is_relative_to(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
        return True
    except ValueError:
        return False


def check_manifests(errors: list[str]) -> None:
    manifests = [
        ROOT / ".github" / "plugin" / "plugin.json",
        ROOT / ".claude-plugin" / "plugin.json",
        ROOT / ".codex-plugin" / "plugin.json",
    ]
    for manifest in manifests:
        data = load_json(manifest, errors)
        for key in ("agents", "skills"):
            value = data.get(key)
            if value is None:
                continue
            values: list[str]
            if isinstance(value, str):
                values = [value]
            elif isinstance(value, list) and all(isinstance(item, str) for item in value):
                values = value
            else:
                fail(errors, f"{manifest}: {key} must be a string path or list of string paths")
                continue
            for item in values:
                target = (ROOT / item).resolve()
                if not is_relative_to(target, ROOT):
                    fail(errors, f"{manifest}: referenced {key} path escapes plugin root: {item}")
                    continue
                if not target.exists():
                    fail(errors, f"{manifest}: referenced {key} path does not exist: {item}")


def check_skills(errors: list[str]) -> None:
    skills_dir = ROOT / "skills"
    if not skills_dir.is_dir():
        fail(errors, f"missing skills directory: {skills_dir}")
        return
    required = [
        "orchestration-harness",
        "plan-format",
        "subagent-report-contract",
        "worker-ui-probes",
        "wave-integration",
        "runtime-adapter-contract",
        "rulebook",
    ]
    for name in required:
        path = skills_dir / name / "SKILL.md"
        if not path.exists():
            fail(errors, f"missing required skill: {path}")
    for skill in skills_dir.iterdir():
        if skill.is_dir():
            path = skill / "SKILL.md"
            if not path.exists():
                fail(errors, f"skill directory missing SKILL.md: {skill}")
            elif not has_frontmatter(path):
                fail(errors, f"skill missing frontmatter: {path}")


def check_role_map(errors: list[str]) -> None:
    role_map = ROOT / "skills" / "orchestration-harness" / "references" / "runtime-role-map.md"
    if not role_map.exists():
        fail(errors, f"missing runtime role map: {role_map}")
        return
    text = role_map.read_text(encoding="utf-8")
    expected_paths = [
        ROOT / "agents" / "Orchestrator.md",
        ROOT / "agents" / "Researcher.md",
        ROOT / "agents" / "Worker.md",
        ROOT / "agents" / "Reviewer.md",
        ROOT / "claude" / "agents" / "harness-orchestrator.md",
        ROOT / "claude" / "agents" / "harness-researcher.md",
        ROOT / "claude" / "agents" / "harness-worker.md",
        ROOT / "claude" / "agents" / "harness-reviewer.md",
        ROOT / "codex" / "agent-templates" / "harness_researcher.toml",
        ROOT / "codex" / "agent-templates" / "harness_worker.toml",
        ROOT / "codex" / "agent-templates" / "harness_reviewer.toml",
    ]
    for path in expected_paths:
        if not path.exists():
            fail(errors, f"role map expected file does not exist: {path}")
    role_map_tokens = (
        "Orchestrator",
        "Researcher",
        "Worker",
        "Reviewer",
        "harness-orchestrator",
        "harness-researcher",
        "harness-worker",
        "harness-reviewer",
        "harness_researcher",
        "harness_worker",
        "harness_reviewer",
    )
    for token in role_map_tokens:
        if token not in text:
            fail(errors, f"runtime role map missing token: {token}")


def check_codex(errors: list[str]) -> None:
    bootstrap = ROOT / "skills" / "codex-harness-bootstrap" / "scripts" / "install_codex_harness.py"
    try:
        py_compile.compile(str(bootstrap), doraise=True)
    except Exception as exc:
        fail(errors, f"Codex bootstrap compile failed: {exc}")
    for name in ("harness_researcher.toml", "harness_worker.toml", "harness_reviewer.toml"):
        if not (ROOT / "codex" / "agent-templates" / name).exists():
            fail(errors, f"missing Codex template: {name}")


def check_adapter_duplication(warnings: list[str]) -> None:
    marker_patterns = [
        r"## Plan Gate",
        r"## Research Dispatch Gate",
        r"## Validation Gate",
        r"## Completion criteria",
        r"## Final user-facing response format",
    ]
    for path in [ROOT / "agents" / "Orchestrator.md", ROOT / "claude" / "agents" / "harness-orchestrator.md"]:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        hits = sum(1 for pattern in marker_patterns if re.search(pattern, text))
        if hits >= 3:
            warn(warnings, f"{path}: possible copied orchestration workflow sections ({hits} markers)")


def check_rulebook_lifecycle(errors: list[str]) -> None:
    rulebook = ROOT / "skills" / "rulebook"
    refs = rulebook / "references"
    for name in ("bootstrap-lifecycle.md", "rule-suite-templates.md", "lifecycle-sidecar.md"):
        path = refs / name
        if not path.exists():
            fail(errors, f"missing rulebook lifecycle reference: {path}")

    rules_files = refs / "rules-files.md"
    if not rules_files.exists():
        fail(errors, f"missing rules-files reference: {rules_files}")
        return
    text = rules_files.read_text(encoding="utf-8")
    for token in ("index.md", "common.md", "worker.md", "orchestrator.md", "reviewer.md", "_lifecycle.json"):
        if token not in text:
            fail(errors, f"{rules_files}: missing required rule-suite token: {token}")


def check_reviewer_adapters(errors: list[str]) -> None:
    expected = "docs/coding-agent/rules/reviewer.md"
    paths = [
        ROOT / "agents" / "Reviewer.md",
        ROOT / "claude" / "agents" / "harness-reviewer.md",
        ROOT / "codex" / "agent-templates" / "harness_reviewer.toml",
    ]
    for path in paths:
        if not path.exists():
            fail(errors, f"missing Reviewer adapter: {path}")
            continue
        if expected not in path.read_text(encoding="utf-8"):
            fail(errors, f"{path}: Reviewer adapter must mention {expected}")


def check_worker_report_reviewer_audience(errors: list[str]) -> None:
    validator = ROOT / "skills" / "subagent-report-contract" / "scripts" / "validate_worker_report.py"
    schema = ROOT / "skills" / "subagent-report-contract" / "references" / "schema.yaml"
    contract = ROOT / "skills" / "subagent-report-contract" / "SKILL.md"
    for path in (validator, schema, contract):
        if not path.exists():
            fail(errors, f"missing Worker report contract file: {path}")

    if validator.exists():
        validator_text = validator.read_text(encoding="utf-8")
        match = re.search(r"ALLOWED_AUDIENCE\s*=\s*\{([^}]+)\}", validator_text)
        if not match:
            fail(errors, f"{validator}: missing ALLOWED_AUDIENCE set")
        else:
            audience_values = set(re.findall(r'"([^"]+)"|\'([^\']+)\'', match.group(1)))
            flattened = {left or right for left, right in audience_values}
            if flattened != {"common", "worker", "orchestrator", "reviewer"}:
                fail(errors, f"{validator}: ALLOWED_AUDIENCE must be common/worker/orchestrator/reviewer")

    expected = {"common", "worker", "orchestrator", "reviewer"}
    for path in (schema, contract):
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        match = re.search(r"audience:\s*(?:\"([^\"]+)\"|([^\n]+))", text)
        if not match:
            fail(errors, f"{path}: missing rule_candidates audience line")
            continue
        audience_text = (match.group(1) or match.group(2)).strip()
        values = {part.strip() for part in audience_text.split("|")}
        if values != expected:
            fail(errors, f"{path}: Worker report audience line must allow common/worker/orchestrator/reviewer")


def check_latent_risk_references(errors: list[str]) -> None:
    refs = ROOT / "skills" / "engineering-quality-baselines" / "references"
    router = refs / "review-latent-risk.md"
    if not router.exists():
        fail(errors, f"missing latent-risk router: {router}")
        return
    router_text = router.read_text(encoding="utf-8")
    required = [
        "review-latent-risk-public-api.md",
        "review-latent-risk-entrypoints-admission.md",
        "review-latent-risk-diagnostics.md",
        "review-latent-risk-build-ci.md",
    ]
    for name in required:
        if name not in router_text:
            fail(errors, f"{router}: missing conditional reference: {name}")
        if not (refs / name).exists():
            fail(errors, f"missing conditional latent-risk reference: {refs / name}")

    for match in re.findall(r"`(review-latent-risk-[^`]+\.md)`", router_text):
        if not (refs / match).exists():
            fail(errors, f"{router}: referenced latent-risk file does not exist: {match}")


def check_clean_split_guards(errors: list[str]) -> None:
    contract = ROOT / "skills" / "subagent-report-contract" / "SKILL.md"
    worker_validator = ROOT / "skills" / "subagent-report-contract" / "scripts" / "validate_worker_report.py"
    promotion_guidelines = ROOT / "skills" / "improvement-loop" / "references" / "promotion-guidelines.md"
    improvement_loop = ROOT / "skills" / "improvement-loop" / "SKILL.md"
    rule_templates = ROOT / "skills" / "rulebook" / "references" / "rule-suite-templates.md"
    rules_files = ROOT / "skills" / "rulebook" / "references" / "rules-files.md"

    if contract.exists():
        text = contract.read_text(encoding="utf-8")
        if "intended_home" in text:
            fail(errors, f"{contract}: must not document rule_candidates[].intended_home; use repo-local rule_candidates plus harness_migration_candidates")
        if "harness_migration_candidates" not in text:
            fail(errors, f"{contract}: must document harness_migration_candidates")

    if worker_validator.exists():
        text = worker_validator.read_text(encoding="utf-8")
        if "ALLOWED_INTENDED_HOME" in text:
            fail(errors, f"{worker_validator}: must not define ALLOWED_INTENDED_HOME")

    reviewer_paths = [
        ROOT / "agents" / "Reviewer.md",
        ROOT / "claude" / "agents" / "harness-reviewer.md",
        ROOT / "codex" / "agent-templates" / "harness_reviewer.toml",
    ]
    for path in reviewer_paths:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        if "global-skill" in text:
            fail(errors, f"{path}: Reviewer adapter must not use old lesson target global-skill")
        if re.search(r"promotion_target\s*:\s*.*\b(?:rules|references)/\*", text):
            fail(errors, f"{path}: Reviewer adapter must use repo_rule | harness_migration | troubleshooting | residual_risk lesson targets")

    if improvement_loop.exists():
        text = improvement_loop.read_text(encoding="utf-8")
        stale_phrases = [
            "first-party skills and references (update the owning skill directly",
            "an update to a first-party skill or reference when that skill is the durable owner",
        ]
        for phrase in stale_phrases:
            if phrase in text:
                fail(errors, f"{improvement_loop}: ordinary runtime guidance must stage harness migration candidates, not direct first-party skill/reference edits")

    if promotion_guidelines.exists():
        text = promotion_guidelines.read_text(encoding="utf-8").lower()
        if "harness migration candidate" not in text:
            fail(errors, f"{promotion_guidelines}: must include harness migration candidate guidance")

    if rule_templates.exists() and "Global Migration Candidates" in rule_templates.read_text(encoding="utf-8"):
        fail(errors, f"{rule_templates}: role rule templates must not contain Global Migration Candidates sections")

    if rules_files.exists():
        text = rules_files.read_text(encoding="utf-8")
        if "global_candidate" in text:
            fail(errors, f"{rules_files}: must not route rule_candidates by global_candidate")
        if "intended_home" in text:
            fail(errors, f"{rules_files}: must not route rule_candidates by intended_home")


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    check_manifests(errors)
    check_skills(errors)
    check_role_map(errors)
    check_codex(errors)
    check_adapter_duplication(warnings)
    check_rulebook_lifecycle(errors)
    check_reviewer_adapters(errors)
    check_worker_report_reviewer_audience(errors)
    check_latent_risk_references(errors)
    check_clean_split_guards(errors)

    for message in warnings:
        print(f"WARNING: {message}", file=sys.stderr)
    for message in errors:
        print(f"ERROR: {message}", file=sys.stderr)
    if errors:
        return 3
    print("Harness package validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
