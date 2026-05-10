#!/usr/bin/env python3
"""
Validate a structured closeout summary before reporting final done.

Usage:
  python skills/wave-integration/scripts/validate_closeout.py --plan path/to/plan.md --summary closeout.yaml

Exit codes:
  0 = valid closeout
  2 = missing dependency for YAML summaries
  3 = invalid closeout or parse error

The summary file may be JSON or YAML and should use this shape:

  plan_status: done
  non_trivial: true
  reviewer:
    status: APPROVED
    waiver: ""
  tasks:
    - id: Task_1
      status: done
      waiver: ""
  validations:
    - detail: "npm test"
      required: true
      status: pass
      waiver: ""
  blockers: []

When a waiver is used, provide waiver evidence as a mapping:

  waiver:
    authority: "user or Orchestrator"
    reason: "why the required item is waived now"
    evidence: "link, transcript note, or other proof of approval"
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

try:
    import yaml  # type: ignore
except Exception:
    yaml = None  # type: ignore


class MissingDependencyError(RuntimeError):
    pass


def err(message: str) -> None:
    print(f"CLOSEOUT ERROR: {message}", file=sys.stderr)


def load_summary(path: Path) -> Any:
    raw = path.read_text(encoding="utf-8")
    suffix = path.suffix.lower()
    if suffix == ".json":
        return json.loads(raw)
    if suffix not in {".yaml", ".yml"}:
        raise ValueError("summary file must use .json, .yaml, or .yml extension")
    if yaml is None:
        raise MissingDependencyError("PyYAML is required for YAML summaries; use JSON or install pyyaml")
    return yaml.safe_load(raw)


def is_waived(value: Any) -> bool:
    if not isinstance(value, dict):
        return False
    required = ("authority", "reason", "evidence")
    return all(isinstance(value.get(key), str) and bool(value[key].strip()) for key in required)


def is_bool(value: Any) -> bool:
    return isinstance(value, bool)


def extract_plan_task_ids(plan_text: str) -> list[str]:
    return re.findall(r"^###\s+(Task_[0-9]+):", plan_text, flags=re.MULTILINE)


def validate(summary: Any, plan_text: str) -> bool:
    ok = True
    if not isinstance(summary, dict):
        err("summary must be a mapping/object")
        return False

    plan_status = summary.get("plan_status")
    if plan_status != "done":
        err("plan_status must be 'done' before final done report")
        ok = False

    if not re.search(r"^- status:\s*[\"']?done[\"']?\s*$", plan_text, flags=re.MULTILINE):
        err("plan file must have '- status: done' before final done report")
        ok = False

    tasks = summary.get("tasks")
    plan_task_ids = extract_plan_task_ids(plan_text)
    if not isinstance(tasks, list) or not tasks:
        err("tasks must be a non-empty list")
        ok = False
    else:
        summary_task_ids: list[str] = []
        for i, task in enumerate(tasks):
            ctx = f"tasks[{i}]"
            if not isinstance(task, dict):
                err(f"{ctx} must be a mapping")
                ok = False
                continue
            task_id = task.get("id")
            if not isinstance(task_id, str) or not re.match(r"^Task_[0-9]+$", task_id):
                err(f"{ctx}.id must match Task_<number>")
                ok = False
            else:
                summary_task_ids.append(task_id)
            status = task.get("status")
            if status not in {"done", "waived"}:
                err(f"{ctx}.status must be done or waived")
                ok = False
            elif status == "waived" and not is_waived(task.get("waiver")):
                err(f"{ctx} has status waived but lacks waiver authority, reason, and evidence")
                ok = False
        missing_tasks = sorted(set(plan_task_ids).difference(summary_task_ids))
        extra_tasks = sorted(set(summary_task_ids).difference(plan_task_ids))
        if missing_tasks:
            err(f"tasks summary missing plan tasks: {', '.join(missing_tasks)}")
            ok = False
        if extra_tasks:
            err(f"tasks summary includes tasks not present in plan: {', '.join(extra_tasks)}")
            ok = False
        if len(summary_task_ids) != len(set(summary_task_ids)):
            err("tasks summary contains duplicate task ids")
            ok = False

    validations = summary.get("validations", [])
    if not isinstance(validations, list):
        err("validations must be a list")
        ok = False
    else:
        for i, validation in enumerate(validations):
            ctx = f"validations[{i}]"
            if not isinstance(validation, dict):
                err(f"{ctx} must be a mapping")
                ok = False
                continue
            for key in ("detail", "required", "status"):
                if key not in validation:
                    err(f"{ctx}.{key} is required")
                    ok = False
            detail = validation.get("detail")
            if "detail" in validation and (not isinstance(detail, str) or not detail.strip()):
                err(f"{ctx}.detail must be a non-empty string")
                ok = False
            status = validation.get("status")
            if "status" in validation and status not in {"pass", "fail", "skipped", "waived"}:
                err(f"{ctx}.status must be pass, fail, skipped, or waived")
                ok = False
            required = validation.get("required")
            if not is_bool(required):
                err(f"{ctx}.required must be boolean")
                ok = False
                continue
            if required is True:
                if status == "waived":
                    if not is_waived(validation.get("waiver")):
                        err(f"{ctx} has status waived but lacks waiver authority, reason, and evidence")
                        ok = False
                elif status != "pass":
                    err(f"{ctx} required validation must pass or be waived")
                    ok = False

    blockers = summary.get("blockers", [])
    if not isinstance(blockers, list):
        err("blockers must be a list")
        ok = False
    elif blockers:
        err("unresolved blockers remain")
        ok = False

    non_trivial = summary.get("non_trivial", True)
    if not is_bool(non_trivial):
        err("non_trivial must be boolean")
        ok = False
    reviewer = summary.get("reviewer", {})
    if non_trivial is True:
        if not isinstance(reviewer, dict):
            err("reviewer must be a mapping for non-trivial closeout")
            ok = False
        elif reviewer.get("status") != "APPROVED" and not is_waived(reviewer.get("waiver")):
            err("non-trivial closeout requires Reviewer APPROVED or explicit waiver")
            ok = False

    return ok


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--plan", required=True, type=Path)
    parser.add_argument("--summary", required=True, type=Path)
    args = parser.parse_args()

    try:
        plan_text = args.plan.read_text(encoding="utf-8")
        summary = load_summary(args.summary)
    except MissingDependencyError as exc:
        err(str(exc))
        return 2
    except Exception as exc:
        err(str(exc))
        return 3

    return 0 if validate(summary, plan_text) else 3


if __name__ == "__main__":
    raise SystemExit(main())
