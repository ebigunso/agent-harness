#!/usr/bin/env python3

from __future__ import annotations

import argparse
import pathlib
import shutil
import sys


AGENT_FILENAMES = [
    "harness_researcher.toml",
    "harness_worker.toml",
    "harness_reviewer.toml",
]


def find_plugin_root(script_path: pathlib.Path) -> pathlib.Path:
    # scripts/install_codex_agents.py
    # -> codex-harness-bootstrap
    # -> skills
    # -> coding-agent-orchestration-harness
    return script_path.resolve().parents[3]


def find_repo_root(start: pathlib.Path) -> pathlib.Path:
    current = start.resolve()
    for candidate in [current, *current.parents]:
        if (candidate / ".git").exists():
            return candidate
    return current


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Install Codex custom-agent profiles for the coding-agent orchestration harness."
    )
    parser.add_argument(
        "--repo-root",
        type=pathlib.Path,
        default=None,
        help="Target repository root. Defaults to the nearest parent containing .git, or the current directory.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing .codex/agents harness profiles.",
    )
    args = parser.parse_args()

    script_path = pathlib.Path(__file__)
    plugin_root = find_plugin_root(script_path)
    source_dir = plugin_root / "codex" / "agents"

    if not source_dir.exists():
        print(f"Missing source directory: {source_dir}", file=sys.stderr)
        return 1

    repo_root = args.repo_root.resolve() if args.repo_root else find_repo_root(pathlib.Path.cwd())
    target_dir = repo_root / ".codex" / "agents"
    target_dir.mkdir(parents=True, exist_ok=True)

    installed: list[pathlib.Path] = []
    skipped: list[pathlib.Path] = []

    for filename in AGENT_FILENAMES:
        source = source_dir / filename
        target = target_dir / filename

        if not source.exists():
            print(f"Missing source file: {source}", file=sys.stderr)
            return 1

        if target.exists() and not args.overwrite:
            skipped.append(target)
            continue

        shutil.copyfile(source, target)
        installed.append(target)

    if installed:
        print("Installed:")
        for path in installed:
            print(f"  {path}")

    if skipped:
        print("Skipped existing files; pass --overwrite to replace:")
        for path in skipped:
            print(f"  {path}")

    if not installed and not skipped:
        print("No agent profiles were installed.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
