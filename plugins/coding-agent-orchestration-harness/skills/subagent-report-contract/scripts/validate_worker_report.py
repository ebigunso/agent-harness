#!/usr/bin/env python3
"""
Validate a Worker YAML report against the subagent-report-contract schema.

Usage:
  python3 scripts/validate_worker_report.py --file path/to/report.yaml
  python3 scripts/validate_worker_report.py --stdin

Exit codes:
  0 = valid
  2 = missing dependency (PyYAML)
  3 = invalid schema
"""

from __future__ import annotations

import argparse
import re
import sys
from typing import Any, Dict, List

try:
    import yaml  # type: ignore
except Exception:
    print(
        "ERROR: PyYAML is required to run this validator.\n"
        "Install with: pip install pyyaml\n",
        file=sys.stderr,
    )
    sys.exit(2)

ALLOWED_STATUS = {"done", "blocked", "failed"}
ALLOWED_FILE_CHANGE = {"modified", "created", "deleted"}
ALLOWED_CMD_RESULT = {"pass", "fail", "skipped"}
ALLOWED_UI_PROBE_RESULT = {"pass", "fail", "skipped"}
ALLOWED_VALIDATION_KIND = {"command", "manual", "e2e", "review"}
ALLOWED_OWNER = {"worker", "reviewer", "orchestrator", "user"}
ALLOWED_AUDIENCE = {"common", "worker", "orchestrator"}
ALLOWED_INTENDED_HOME = {"repo_specific", "global_candidate"}
ALLOWED_LESSON_CATEGORY = {"planning", "delegation", "validation", "environment", "review", "docs", "other"}
TASK_ID_RE = re.compile(r"^Task_[1-9][0-9]*$")
YAML_BLOCK_RE = re.compile(r"```(?:yaml|yml)\s*\r?\n(.*?)(?:\r?\n)?```", re.DOTALL | re.IGNORECASE)


def err(msg: str) -> None:
    print(f"SCHEMA ERROR: {msg}", file=sys.stderr)


def is_str(x: Any) -> bool:
    return isinstance(x, str)


def is_bool(x: Any) -> bool:
    return isinstance(x, bool)


def is_list(x: Any) -> bool:
    return isinstance(x, list)


def is_dict(x: Any) -> bool:
    return isinstance(x, dict)


def require_keys(obj: Dict[str, Any], keys: List[str], ctx: str) -> bool:
    ok = True
    for k in keys:
        if k not in obj:
            err(f"{ctx}: missing required key '{k}'")
            ok = False
    return ok


def validate_enum(value: Any, allowed: set[str], ctx: str) -> bool:
    if not is_str(value):
        err(f"{ctx} must be a string")
        return False
    if value not in allowed:
        err(f"{ctx} must be one of {sorted(allowed)}")
        return False
    return True


def validate_files_changed(v: Any) -> bool:
    if not is_list(v):
        err("files_changed must be a list")
        return False
    ok = True
    for i, item in enumerate(v):
        ctx = f"files_changed[{i}]"
        if not is_dict(item):
            err(f"{ctx} must be a dict")
            ok = False
            continue
        ok &= require_keys(item, ["path", "change", "intent"], ctx)
        if "path" in item and not is_str(item["path"]):
            err(f"{ctx}.path must be a string")
            ok = False
        if "change" in item:
            ok &= validate_enum(item["change"], ALLOWED_FILE_CHANGE, f"{ctx}.change")
        if "intent" in item and not is_str(item["intent"]):
            err(f"{ctx}.intent must be a string")
            ok = False
    return ok


def validate_commands_run(v: Any) -> bool:
    if not is_list(v):
        err("commands_run must be a list")
        return False
    ok = True
    for i, item in enumerate(v):
        ctx = f"commands_run[{i}]"
        if not is_dict(item):
            err(f"{ctx} must be a dict")
            ok = False
            continue
        ok &= require_keys(item, ["command", "result", "notes"], ctx)
        if "command" in item and not is_str(item["command"]):
            err(f"{ctx}.command must be a string")
            ok = False
        if "result" in item:
            ok &= validate_enum(item["result"], ALLOWED_CMD_RESULT, f"{ctx}.result")
        if "notes" in item and not is_str(item["notes"]):
            err(f"{ctx}.notes must be a string")
            ok = False
    return ok


def validate_validation_results(v: Any, status: str) -> bool:
    if not is_list(v):
        err("validation_results must be a list")
        return False
    ok = True
    for i, item in enumerate(v):
        ctx = f"validation_results[{i}]"
        if not is_dict(item):
            err(f"{ctx} must be a dict")
            ok = False
            continue
        ok &= require_keys(item, ["kind", "required", "owner", "detail", "status", "evidence"], ctx)
        if "kind" in item and item["kind"] not in ALLOWED_VALIDATION_KIND:
            err(f"{ctx}.kind must be one of {sorted(ALLOWED_VALIDATION_KIND)}")
            ok = False
        if "required" in item and not is_bool(item["required"]):
            err(f"{ctx}.required must be boolean")
            ok = False
        if "owner" in item and item["owner"] not in ALLOWED_OWNER:
            err(f"{ctx}.owner must be one of {sorted(ALLOWED_OWNER)}")
            ok = False
        if "detail" in item and not is_str(item["detail"]):
            err(f"{ctx}.detail must be a string")
            ok = False
        if "status" in item and item["status"] not in {"pass", "fail", "skipped"}:
            err(f"{ctx}.status must be one of ['pass','fail','skipped']")
            ok = False
        if "evidence" in item and not is_str(item["evidence"]):
            err(f"{ctx}.evidence must be a string")
            ok = False

        # Enforce: worker-owned required validations cannot be skipped unless evidence indicates waiver
        if (
            item.get("required") is True
            and item.get("owner") == "worker"
            and item.get("status") == "skipped"
        ):
            ev = item.get("evidence", "")
            if not re.search(r"\bwaiv(ed|er)\b", ev, flags=re.IGNORECASE):
                err(
                    f"{ctx}: required worker validation cannot be skipped without explicit waiver evidence"
                )
                ok = False

        # Enforce: status=done implies no required worker validations failed
        if status == "done" and item.get("required") is True and item.get("owner") == "worker":
            if item.get("status") == "fail":
                err(f"{ctx}: status=done but required worker validation failed")
                ok = False
            if item.get("status") == "skipped":
                # allowed only if evidence has waiver (checked above)
                pass

    return ok


def validate_ui_probes(v: Any) -> bool:
    if not is_list(v):
        err("ui_probes must be a list")
        return False
    ok = True
    for i, item in enumerate(v):
        ctx = f"ui_probes[{i}]"
        if not is_dict(item):
            err(f"{ctx} must be a dict")
            ok = False
            continue
        ok &= require_keys(item, ["base_url", "flow", "result", "evidence", "notes"], ctx)
        if "base_url" in item and not is_str(item["base_url"]):
            err(f"{ctx}.base_url must be a string")
            ok = False
        if "flow" in item and not is_str(item["flow"]):
            err(f"{ctx}.flow must be a string")
            ok = False
        if "result" in item:
            ok &= validate_enum(item["result"], ALLOWED_UI_PROBE_RESULT, f"{ctx}.result")
        if "evidence" in item and not is_str(item["evidence"]):
            err(f"{ctx}.evidence must be a string")
            ok = False
        if "notes" in item and not is_str(item["notes"]):
            err(f"{ctx}.notes must be a string")
            ok = False
    return ok


def validate_rule_candidates(v: Any) -> bool:
    if not is_list(v):
        err("rule_candidates must be a list")
        return False
    ok = True
    for i, item in enumerate(v):
        ctx = f"rule_candidates[{i}]"
        if not is_dict(item):
            err(f"{ctx} must be a dict")
            ok = False
            continue
        ok &= require_keys(item, ["audience", "intended_home", "id", "rule", "rationale", "scope", "example"], ctx)
        if item.get("audience") not in ALLOWED_AUDIENCE:
            err(f"{ctx}.audience must be one of {sorted(ALLOWED_AUDIENCE)}")
            ok = False
        if item.get("intended_home") not in ALLOWED_INTENDED_HOME:
            err(f"{ctx}.intended_home must be one of {sorted(ALLOWED_INTENDED_HOME)}")
            ok = False
        for k in ["id", "rule", "rationale", "scope", "example"]:
            if k in item and not is_str(item[k]):
                err(f"{ctx}.{k} must be a string")
                ok = False
    return ok


def validate_lesson_candidates(v: Any) -> bool:
    if not is_list(v):
        err("lesson_candidates must be a list")
        return False
    ok = True
    for i, item in enumerate(v):
        ctx = f"lesson_candidates[{i}]"
        if not is_dict(item):
            err(f"{ctx} must be a dict")
            ok = False
            continue
        ok &= require_keys(
            item,
            [
                "id",
                "category",
                "deviation",
                "root_cause",
                "prevention",
                "promotion_target",
            ],
            ctx,
        )
        if item.get("category") not in ALLOWED_LESSON_CATEGORY:
            err(f"{ctx}.category must be one of {sorted(ALLOWED_LESSON_CATEGORY)}")
            ok = False
        for k in ["id", "deviation", "root_cause", "prevention", "promotion_target"]:
            if k in item and not is_str(item[k]):
                err(f"{ctx}.{k} must be a string")
                ok = False
    return ok


def validate_root(doc: Any) -> bool:
    if not is_dict(doc):
        err("Top-level YAML must be a mapping/dict")
        return False

    required = [
        "task_id",
        "status",
        "summary",
        "files_changed",
        "commands_run",
        "validation_results",
        "tests",
        "blockers",
        "questions_for_orchestrator",
        "assumptions",
        "rule_candidates",
    ]
    ok = require_keys(doc, required, "root")

    if "skill_candidates" in doc:
        err("skill_candidates is not part of the contract; use lesson_candidates for deviations")
        ok = False

    if "task_id" in doc and not is_str(doc["task_id"]):
        err("task_id must be a string")
        ok = False
    elif "task_id" in doc and not TASK_ID_RE.match(doc["task_id"]):
        err("task_id must match ^Task_[1-9][0-9]*$")
        ok = False

    status = doc.get("status")
    if status not in ALLOWED_STATUS:
        err(f"status must be one of {sorted(ALLOWED_STATUS)}")
        ok = False
        status = "failed"  # safe fallback for downstream checks

    if "summary" in doc and not is_str(doc["summary"]):
        err("summary must be a string (use |- for multiline)")
        ok = False

    ok &= validate_files_changed(doc.get("files_changed", []))
    ok &= validate_commands_run(doc.get("commands_run", []))
    ok &= validate_validation_results(doc.get("validation_results", []), status)

    tests = doc.get("tests")
    if not is_dict(tests):
        err("tests must be a dict")
        ok = False
    else:
        ok &= require_keys(tests, ["ran", "notes"], "tests")
        if "ran" in tests and not is_bool(tests["ran"]):
            err("tests.ran must be boolean")
            ok = False
        if "notes" in tests and not is_str(tests["notes"]):
            err("tests.notes must be a string")
            ok = False

    for k in ["blockers", "questions_for_orchestrator", "assumptions"]:
        if k in doc and not is_list(doc[k]):
            err(f"{k} must be a list")
            ok = False

    if status in {"blocked", "failed"} and is_list(doc.get("blockers")) and len(doc.get("blockers", [])) == 0:
        err("status blocked/failed requires non-empty blockers")
        ok = False

    ok &= validate_rule_candidates(doc.get("rule_candidates", []))
    if "ui_probes" in doc:
        ok &= validate_ui_probes(doc.get("ui_probes", []))
    if "lesson_candidates" in doc:
        ok &= validate_lesson_candidates(doc.get("lesson_candidates", []))

    return ok


def extract_message_yaml(raw: str) -> str | None:
    matches = YAML_BLOCK_RE.findall(raw)
    if len(matches) != 1:
        err(f"--message-file requires exactly one YAML code block; found {len(matches)}")
        return None
    parts = YAML_BLOCK_RE.split(raw, maxsplit=1)
    before, after = parts[0], parts[-1]
    if before.strip() or after.strip():
        err("--message-file must contain one YAML code block and no extra prose")
        return None
    return matches[0]


def load_task_contract(path: str) -> Any:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f.read())


def validate_against_task_contract(doc: Dict[str, Any], contract: Any) -> bool:
    if not is_dict(contract):
        err("task contract must be a mapping")
        return False
    ok = True
    contract_task_id = contract.get("task_id")
    if contract_task_id and doc.get("task_id") != contract_task_id:
        err(f"task_id does not match task contract: {doc.get('task_id')} != {contract_task_id}")
        ok = False
    validation_contract = contract.get("validation", [])
    if validation_contract is None:
        validation_contract = []
    if not is_list(validation_contract):
        err("task contract validation must be a list")
        return False

    required_worker = []
    for i, item in enumerate(validation_contract):
        ctx = f"task contract validation[{i}]"
        if not is_dict(item):
            err(f"{ctx} must be a mapping")
            ok = False
            continue
        if item.get("required") is True and item.get("owner") == "worker":
            detail = item.get("detail")
            if not is_str(detail) or not detail.strip():
                err(f"{ctx}.detail must be a non-empty string for required worker validation")
                ok = False
                continue
            required_worker.append(item)
    report_results = doc.get("validation_results", [])
    for item in required_worker:
        detail = item.get("detail")
        match = next(
            (
                result
                for result in report_results
                if is_dict(result)
                and result.get("required") is True
                and result.get("owner") == "worker"
                and result.get("detail") == detail
            ),
            None,
        )
        if match is None:
            err(f"missing report validation result for required worker validation: {detail}")
            ok = False
        elif match.get("status") == "skipped":
            evidence = match.get("evidence", "")
            if not isinstance(evidence, str) or not re.search(r"\bwaiv(ed|er)\b", evidence, flags=re.IGNORECASE):
                err(f"required worker validation skipped without waiver evidence: {detail}")
                ok = False
    return ok


def main() -> int:
    ap = argparse.ArgumentParser()
    input_group = ap.add_mutually_exclusive_group(required=True)
    input_group.add_argument("--file", type=str, default="")
    input_group.add_argument("--message-file", type=str, default="")
    input_group.add_argument("--stdin", action="store_true")
    ap.add_argument("--task-contract", type=str, default="")
    args = ap.parse_args()

    if args.stdin:
        raw = sys.stdin.read()
    elif args.message_file:
        with open(args.message_file, "r", encoding="utf-8") as f:
            message = f.read()
        extracted = extract_message_yaml(message)
        if extracted is None:
            return 3
        raw = extracted
    elif args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            raw = f.read()
    else:
        err("Specify exactly one input source: --file <path>, --message-file <path>, or --stdin")
        return 3

    try:
        doc = yaml.safe_load(raw)
    except Exception as e:
        err(f"YAML parse failed: {e}")
        return 3

    ok = validate_root(doc)
    if ok and args.task_contract and is_dict(doc):
        try:
            contract_ok = validate_against_task_contract(doc, load_task_contract(args.task_contract))
            ok = ok and contract_ok
        except Exception as e:
            err(f"task contract parse failed: {e}")
            ok = False

    if not ok:
        return 3

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
