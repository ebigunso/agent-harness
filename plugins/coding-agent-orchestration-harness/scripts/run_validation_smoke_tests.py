#!/usr/bin/env python3
"""Run lightweight validation smoke tests for harness validators."""

from __future__ import annotations

import subprocess
import sys
import tempfile
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


def run_bootstrap_smoke() -> bool:
    script = ROOT / "skills" / "codex-harness-bootstrap" / "scripts" / "install_codex_harness.py"
    ok = True
    with tempfile.TemporaryDirectory() as tmp:
        codex_home = Path(tmp) / "codex-home"
        ok &= run([PY, str(script), "--scope", "user", "--codex-home", str(codex_home), "--user-instructions", "skip", "--dry-run"], 0)
        if (codex_home / "agents").exists():
            print("dry-run unexpectedly created agents directory", file=sys.stderr)
            ok = False
        ok &= run([PY, str(script), "--scope", "user", "--codex-home", str(codex_home), "--user-instructions", "skip"], 0)
        ok &= run([PY, str(script), "--scope", "user", "--codex-home", str(codex_home), "--user-instructions", "skip", "--check"], 0)
        ok &= run([PY, str(script), "--scope", "user", "--codex-home", str(codex_home), "--user-instructions", "skip", "--verify"], 0)
        worker = codex_home / "agents" / "harness_worker.toml"
        worker.write_text(worker.read_text(encoding="utf-8") + "\n# stale\n", encoding="utf-8")
        ok &= run([PY, str(script), "--scope", "user", "--codex-home", str(codex_home), "--user-instructions", "skip", "--check"], 3)
    with tempfile.TemporaryDirectory() as tmp:
        repo = Path(tmp) / "repo"
        (repo / ".git").mkdir(parents=True)
        ok &= run([PY, str(script), "--scope", "repo", "--repo-root", str(repo), "--user-instructions", "skip"], 0)
        ok &= run([PY, str(script), "--scope", "repo", "--repo-root", str(repo), "--user-instructions", "skip", "--verify"], 0)
    return ok


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
        ([PY, str(ROOT / "skills" / "plan-format" / "scripts" / "validate_plan.py"), "--file", str(fixtures / "invalid-plan-unrelated-canonical-waiver.md"), "--mode", "balanced"], 3),
        ([PY, str(ROOT / "skills" / "subagent-report-contract" / "scripts" / "validate_worker_report.py"), "--file", str(fixtures / "valid-worker-report.yaml")], 0),
        ([PY, str(ROOT / "skills" / "subagent-report-contract" / "scripts" / "validate_worker_report.py"), "--message-file", str(fixtures / "valid-worker-message.md")], 0),
        ([PY, str(ROOT / "skills" / "subagent-report-contract" / "scripts" / "validate_worker_report.py"), "--file", str(fixtures / "valid-ui-worker-report-with-probes.yaml")], 0),
        ([PY, str(ROOT / "skills" / "subagent-report-contract" / "scripts" / "validate_worker_report.py"), "--file", str(fixtures / "invalid-worker-report-missing-validation.yaml"), "--task-contract", str(fixtures / "task-contract-required-worker-validation.yaml")], 3),
        ([PY, str(ROOT / "skills" / "subagent-report-contract" / "scripts" / "validate_worker_report.py"), "--file", str(fixtures / "invalid-worker-report-done-with-failed-required-validation.yaml")], 3),
    ]
    ok = True
    for cmd, expected in checks:
        ok &= run(cmd, expected)
    ok &= run_bootstrap_smoke()
    return 0 if ok else 3


if __name__ == "__main__":
    raise SystemExit(main())
