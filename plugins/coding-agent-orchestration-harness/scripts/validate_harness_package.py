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


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    check_manifests(errors)
    check_skills(errors)
    check_role_map(errors)
    check_codex(errors)
    check_adapter_duplication(warnings)

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
