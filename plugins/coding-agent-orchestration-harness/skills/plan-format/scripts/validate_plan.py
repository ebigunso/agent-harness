#!/usr/bin/env python3
"""Validate Task_X execution plans."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


TASK_RE = re.compile(r"^### (Task_[0-9]+):", re.MULTILINE)
REQUIRED_SECTIONS = [
    "Goal",
    "Definition of Done",
    "Scope / Non-goals",
    "Tasks",
    "Task Waves",
    "Progress Log",
    "Decision Log",
]
VALIDATION_FIELDS = {"kind", "required", "owner", "detail"}


def error(errors: list[str], msg: str) -> None:
    errors.append(msg)


def warn(warnings: list[str], msg: str) -> None:
    warnings.append(msg)


def section_for_task(text: str, match: re.Match[str], next_start: int) -> str:
    return text[match.start() : next_start]


def parse_list_value(block: str, field: str) -> list[str]:
    match = re.search(rf"^- {re.escape(field)}:\s*\[(.*?)\]\s*$", block, flags=re.MULTILINE)
    if not match:
        return []
    raw = match.group(1).strip()
    if not raw:
        return []
    return [item.strip() for item in raw.split(",") if item.strip()]


def has_field(block: str, field: str) -> bool:
    return bool(re.search(rf"^- {re.escape(field)}:", block, flags=re.MULTILINE))


def parse_validation_blocks(task_block: str) -> list[dict[str, str]]:
    validations: list[dict[str, str]] = []
    current: dict[str, str] | None = None
    in_validation = False
    for line in task_block.splitlines():
        if line.startswith("- validation:"):
            in_validation = True
            continue
        if in_validation and re.match(r"^### |^## ", line):
            break
        item = re.match(r"\s+- kind:\s*(.+?)\s*$", line)
        if item:
            current = {"kind": item.group(1).strip().strip('"')}
            validations.append(current)
            continue
        field = re.match(r"\s+(required|owner|detail):\s*(.+?)\s*$", line)
        if field and current is not None:
            current[field.group(1)] = field.group(2).strip().strip('"')
    return validations


def has_heading(text: str, heading: str) -> bool:
    return bool(re.search(rf"^##\s+{re.escape(heading)}(?:\s|\(|$)", text, flags=re.MULTILINE))


def section_body(text: str, heading: str) -> str:
    match = re.search(rf"^##\s+{re.escape(heading)}(?:\s|\(|$).*?$", text, flags=re.MULTILINE)
    if not match:
        return ""
    body = text[match.end() :]
    next_section = re.search(r"^##\s+", body, flags=re.MULTILINE)
    if next_section:
        return body[: next_section.start()]
    return body


def validate(text: str, mode: str) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    for section in REQUIRED_SECTIONS:
        if not has_heading(text, section):
            error(errors, f"missing required section: ## {section}")

    matches = list(TASK_RE.finditer(text))
    if not matches:
        error(errors, "no Task_X sections found")
        return errors, warnings

    task_ids = [m.group(1) for m in matches]
    expected = [f"Task_{i}" for i in range(1, len(task_ids) + 1)]
    if task_ids != expected:
        error(errors, f"task ids must be sequential: expected {expected}, found {task_ids}")

    deps: dict[str, list[str]] = {}
    all_validation_items: list[dict[str, str]] = []
    for index, match in enumerate(matches):
        next_start = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        block = section_for_task(text, match, next_start)
        task_id = match.group(1)
        for field in ("type", "owns", "depends_on", "acceptance", "validation"):
            if not has_field(block, field):
                error(errors, f"{task_id}: missing field {field}")
        deps[task_id] = parse_list_value(block, "depends_on")
        validations = parse_validation_blocks(block)
        if not validations:
            error(errors, f"{task_id}: no validation items found")
        for item in validations:
            missing = VALIDATION_FIELDS.difference(item)
            if missing:
                error(errors, f"{task_id}: validation item missing fields {sorted(missing)}")
            if item.get("required") not in {"true", "false"}:
                error(errors, f"{task_id}: validation.required must be true or false")
            if item.get("owner") not in {"worker", "reviewer", "orchestrator", "user"}:
                error(errors, f"{task_id}: validation.owner is invalid or missing")
            all_validation_items.append(item)

    for task_id, task_deps in deps.items():
        for dep in task_deps:
            if dep not in task_ids:
                error(errors, f"{task_id}: dependency does not exist: {dep}")

    visited: set[str] = set()
    stack: set[str] = set()

    def visit(task_id: str) -> None:
        if task_id in stack:
            error(errors, f"dependency cycle detected at {task_id}")
            return
        if task_id in visited:
            return
        stack.add(task_id)
        for dep in deps.get(task_id, []):
            if dep in deps:
                visit(dep)
        stack.remove(task_id)
        visited.add(task_id)

    for task_id in task_ids:
        visit(task_id)

    wave_section = section_body(text, "Task Waves")
    wave_lines = [line for line in wave_section.splitlines() if re.match(r"^\s*-\s*Wave\b", line)]
    wave_tasks = [task for line in wave_lines for task in re.findall(r"Task_[0-9]+", line)]
    if sorted(wave_tasks) != sorted(task_ids) or len(wave_tasks) != len(task_ids):
        error(errors, "Task Waves must include all tasks exactly once")

    tasks_section = section_body(text, "Tasks")
    ui_impact = re.search(r"\b(UI|frontend|visual|user flows?)\b", tasks_section, flags=re.IGNORECASE)
    has_reviewer_e2e = any(
        item.get("owner") == "reviewer" and item.get("required") == "true" and item.get("kind") in {"e2e", "manual"}
        for item in all_validation_items
    )
    has_waiver = re.search(r"\bwaiv(ed|er)\b", text, flags=re.IGNORECASE)
    if ui_impact and not has_reviewer_e2e and not has_waiver:
        error(errors, "UI-impact plan requires Reviewer-owned E2E/visual validation or explicit waiver")

    if mode == "strict" and len(task_ids) > 8:
        warn(warnings, "strict mode: large task count; consider reviewing decomposition manually")
    elif mode == "balanced" and len(task_ids) > 8:
        warn(warnings, "balanced mode: large task count may need decomposition review")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True, type=Path)
    parser.add_argument("--mode", choices=["strict", "balanced", "relaxed"], default="balanced")
    args = parser.parse_args()
    text = args.file.read_text(encoding="utf-8")
    errors, warnings = validate(text, args.mode)
    for message in warnings:
        print(f"WARNING: {message}", file=sys.stderr)
    for message in errors:
        print(f"PLAN ERROR: {message}", file=sys.stderr)
    if errors and args.mode != "relaxed":
        return 3
    print("Plan validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
