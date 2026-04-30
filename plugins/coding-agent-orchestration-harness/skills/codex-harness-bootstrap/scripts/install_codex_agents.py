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
REFERENCE_FILENAMES = [
    "codex-app-connector-policy-researcher.md",
    "codex-app-connector-policy-worker.md",
    "codex-app-connector-policy-reviewer.md",
]

SCOPES = ("user", "repo")
INSTRUCTIONS_ACTIONS = ("ask", "add", "skip")
INSTRUCTIONS_START = "<!-- coding-agent-orchestration-harness:start -->"
INSTRUCTIONS_END = "<!-- coding-agent-orchestration-harness:end -->"
INSTRUCTIONS_BLOCK = f"""{INSTRUCTIONS_START}
## Coding Agent Orchestration Harness

For non-trivial coding tasks that benefit from planning, delegation, implementation, and review, use the coding-agent orchestration harness.

- Prefer the installed harness subagents when delegating: `harness_researcher`, `harness_worker`, and `harness_reviewer`.
- Load and follow the `orchestration-harness` skill when the task needs the full harness workflow.
- Do not apply the harness to simple questions, small mechanical edits, or non-coding tasks unless the user explicitly asks for it.
{INSTRUCTIONS_END}
"""


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


def ask_scope() -> str:
    print("Install Codex harness agents where?")
    print("  1) user scope: available in all Codex sessions for this user")
    print("  2) repository scope: available only from this repository")

    while True:
        choice = input("Choose user or repository scope [user/repo]: ").strip().lower()
        if choice in {"user", "u", "1"}:
            return "user"
        if choice in {"repo", "repository", "r", "2"}:
            return "repo"
        print("Please enter 'user' or 'repo'.")


def ask_yes_no(prompt: str, default: bool = False) -> bool:
    suffix = " [Y/n]: " if default else " [y/N]: "
    while True:
        answer = input(prompt + suffix).strip().lower()
        if not answer:
            return default
        if answer in {"y", "yes"}:
            return True
        if answer in {"n", "no"}:
            return False
        print("Please enter 'yes' or 'no'.")


def resolve_target_dir(
    scope: str,
    repo_root: pathlib.Path | None,
    codex_home: pathlib.Path,
) -> pathlib.Path:
    if scope == "user":
        return codex_home / "agents"

    assert repo_root is not None
    return repo_root / ".codex" / "agents"


def replace_managed_block(existing: str) -> tuple[str, bool]:
    start = existing.find(INSTRUCTIONS_START)
    end = existing.find(INSTRUCTIONS_END)
    if start == -1 or end == -1 or end < start:
        separator = "\n\n" if existing and not existing.endswith("\n\n") else ""
        return existing + separator + INSTRUCTIONS_BLOCK + "\n", False

    end += len(INSTRUCTIONS_END)
    replacement = INSTRUCTIONS_BLOCK.rstrip()
    return existing[:start] + replacement + existing[end:], True


def install_user_instructions(codex_home: pathlib.Path, action: str) -> str:
    agents_md = codex_home / "AGENTS.md"
    existing = agents_md.read_text(encoding="utf-8") if agents_md.exists() else ""
    has_managed_block = INSTRUCTIONS_START in existing and INSTRUCTIONS_END in existing

    if action == "skip":
        return "skipped"

    if action == "ask":
        if has_managed_block:
            print(f"Existing harness instruction block found in {agents_md}.")
            should_write = ask_yes_no("Replace it with the current recommended block?", default=True)
        elif existing.strip():
            print(f"Existing user instructions found in {agents_md}:")
            print("--- existing AGENTS.md preview ---")
            preview = existing if len(existing) <= 2000 else existing[:2000] + "\n... <truncated>"
            print(preview)
            print("--- end preview ---")
            should_write = ask_yes_no(
                "Append the harness instruction block without changing existing content?",
                default=False,
            )
        else:
            should_write = ask_yes_no(
                f"Add a small harness routing rule to {agents_md}?",
                default=True,
            )

        if not should_write:
            return "skipped"

    updated, replaced = replace_managed_block(existing)
    agents_md.parent.mkdir(parents=True, exist_ok=True)
    agents_md.write_text(updated, encoding="utf-8")
    return "updated" if replaced else "added"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Install Codex custom-agent profiles for the coding-agent orchestration harness."
    )
    parser.add_argument(
        "--scope",
        choices=SCOPES,
        default=None,
        help="Install scope. If omitted, the script asks interactively.",
    )
    parser.add_argument(
        "--repo-root",
        type=pathlib.Path,
        default=None,
        help="Target repository root for --scope repo. Defaults to the nearest parent containing .git, or the current directory.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing harness profiles in the selected target agents directory.",
    )
    parser.add_argument(
        "--user-instructions",
        choices=INSTRUCTIONS_ACTIONS,
        default="ask",
        help="Manage a small harness routing block in ~/.codex/AGENTS.md. Defaults to ask.",
    )
    parser.add_argument(
        "--codex-home",
        type=pathlib.Path,
        default=pathlib.Path.home() / ".codex",
        help=argparse.SUPPRESS,
    )
    args = parser.parse_args()

    script_path = pathlib.Path(__file__)
    plugin_root = find_plugin_root(script_path)
    source_dir = plugin_root / "codex" / "agent-templates"
    reference_source_dir = plugin_root / "references"

    if not source_dir.exists():
        print(f"Missing source directory: {source_dir}", file=sys.stderr)
        return 1

    if not reference_source_dir.exists():
        print(f"Missing reference source directory: {reference_source_dir}", file=sys.stderr)
        return 1

    scope = args.scope or ask_scope()
    repo_root = None
    if scope == "repo":
        repo_root = args.repo_root.resolve() if args.repo_root else find_repo_root(pathlib.Path.cwd())

    codex_home = args.codex_home.resolve()
    target_dir = resolve_target_dir(scope, repo_root, codex_home)
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

    reference_target_dir = target_dir / "references"
    reference_target_dir.mkdir(parents=True, exist_ok=True)

    for filename in REFERENCE_FILENAMES:
        source = reference_source_dir / filename
        target = reference_target_dir / filename

        if not source.exists():
            print(f"Missing reference file: {source}", file=sys.stderr)
            return 1

        if target.exists() and not args.overwrite:
            skipped.append(target)
            continue

        shutil.copyfile(source, target)
        installed.append(target)

    print(f"Scope: {scope}")
    print(f"Target directory: {target_dir}")

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

    instructions_status = "not-applicable"
    if scope == "user":
        instructions_status = install_user_instructions(codex_home, args.user_instructions)
        print(f"User instructions: {instructions_status}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
