#!/usr/bin/env python3
"""Run lightweight validation smoke tests for harness validators."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PY = sys.executable


def run(cmd: list[str], expect: int = 0) -> bool:
    print("+ " + " ".join(cmd))
    result = subprocess.run(cmd, cwd=ROOT.parent.parent)
    if result.returncode != expect:
        print(f"Expected exit {expect}, got {result.returncode}", file=sys.stderr)
        return False
    return True


def main() -> int:
    fixtures = ROOT / "tests" / "fixtures"
    checks: list[tuple[list[str], int]] = [
        ([PY, "-m", "py_compile", str(ROOT / "scripts" / "validate_harness_package.py")], 0),
        ([PY, "-m", "py_compile", str(ROOT / "scripts" / "run_validation_smoke_tests.py")], 0),
        ([PY, "-m", "py_compile", str(ROOT / "skills" / "plan-format" / "scripts" / "validate_plan.py")], 0),
        ([PY, "-m", "py_compile", str(ROOT / "skills" / "subagent-report-contract" / "scripts" / "validate_worker_report.py")], 0),
        ([PY, "-m", "py_compile", str(ROOT / "skills" / "wave-integration" / "scripts" / "validate_closeout.py")], 0),
        ([PY, str(ROOT / "scripts" / "validate_harness_package.py")], 0),
        ([PY, str(ROOT / "skills" / "plan-format" / "scripts" / "validate_plan.py"), "--file", str(fixtures / "valid-plan.md"), "--mode", "balanced"], 0),
        ([PY, str(ROOT / "skills" / "plan-format" / "scripts" / "validate_plan.py"), "--file", str(fixtures / "valid-plan-canonical-ui-waiver.md"), "--mode", "balanced"], 0),
        ([PY, str(ROOT / "skills" / "plan-format" / "scripts" / "validate_plan.py"), "--file", str(fixtures / "invalid-plan-missing-validation-owner.md"), "--mode", "balanced"], 3),
        ([PY, str(ROOT / "skills" / "plan-format" / "scripts" / "validate_plan.py"), "--file", str(fixtures / "invalid-plan-ui-waiver-prose.md"), "--mode", "balanced"], 3),
        ([PY, str(ROOT / "skills" / "subagent-report-contract" / "scripts" / "validate_worker_report.py"), "--file", str(fixtures / "valid-worker-report.yaml")], 0),
        ([PY, str(ROOT / "skills" / "subagent-report-contract" / "scripts" / "validate_worker_report.py"), "--message-file", str(fixtures / "valid-worker-message.md")], 0),
        ([PY, str(ROOT / "skills" / "subagent-report-contract" / "scripts" / "validate_worker_report.py"), "--file", str(fixtures / "valid-ui-worker-report-with-probes.yaml")], 0),
        ([PY, str(ROOT / "skills" / "subagent-report-contract" / "scripts" / "validate_worker_report.py"), "--file", str(fixtures / "invalid-worker-report-missing-validation.yaml"), "--task-contract", str(fixtures / "task-contract-required-worker-validation.yaml")], 3),
        ([PY, str(ROOT / "skills" / "subagent-report-contract" / "scripts" / "validate_worker_report.py"), "--file", str(fixtures / "invalid-worker-report-done-with-failed-required-validation.yaml")], 3),
    ]
    ok = True
    for cmd, expected in checks:
        ok &= run(cmd, expected)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
