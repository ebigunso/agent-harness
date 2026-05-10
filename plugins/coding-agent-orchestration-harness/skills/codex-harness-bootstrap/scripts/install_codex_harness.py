#!/usr/bin/env python3

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import pathlib
import shutil
import sys


PLUGIN_NAME = "coding-agent-orchestration-harness"
MANIFEST_FILENAME = ".coding-agent-orchestration-harness-install.json"
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


def find_plugin_root(script_path: pathlib.Path) -> pathlib.Path:
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


def resolve_target_dir(scope: str, repo_root: pathlib.Path | None, codex_home: pathlib.Path) -> pathlib.Path:
    if scope == "user":
        return codex_home / "agents"
    if repo_root is None:
        raise ValueError("repo_root is required when scope is 'repo'")
    return repo_root / ".codex" / "agents"


def load_plugin_version(plugin_root: pathlib.Path) -> str:
    manifest = plugin_root / ".codex-plugin" / "plugin.json"
    try:
        return json.loads(manifest.read_text(encoding="utf-8")).get("version", "unknown")
    except Exception:
        return "unknown"


def sha256(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_instructions_block(plugin_root: pathlib.Path) -> str:
    snippet = plugin_root / "codex" / "snippets" / "AGENTS.md"
    if not snippet.exists():
        raise FileNotFoundError(f"Missing AGENTS.md snippet: {snippet}")

    block = snippet.read_text(encoding="utf-8").strip()
    if INSTRUCTIONS_START not in block or INSTRUCTIONS_END not in block:
        raise ValueError(f"AGENTS.md snippet is missing required markers: {snippet}")

    return block + "\n"


def replace_managed_block(existing: str, instructions_block: str) -> tuple[str, bool]:
    start = existing.find(INSTRUCTIONS_START)
    end = existing.find(INSTRUCTIONS_END)
    if start == -1 or end == -1 or end < start:
        separator = "\n\n" if existing and not existing.endswith("\n\n") else ""
        return existing + separator + instructions_block + "\n", False

    end += len(INSTRUCTIONS_END)
    replacement = instructions_block.rstrip()
    return existing[:start] + replacement + existing[end:], True


def install_user_instructions(codex_home: pathlib.Path, action: str, instructions_block: str) -> str:
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

    updated, replaced = replace_managed_block(existing, instructions_block)
    agents_md.parent.mkdir(parents=True, exist_ok=True)
    agents_md.write_text(updated, encoding="utf-8")
    return "updated" if replaced else "added"


def source_target_pairs(plugin_root: pathlib.Path, target_dir: pathlib.Path) -> list[tuple[pathlib.Path, pathlib.Path, str]]:
    source_dir = plugin_root / "codex" / "agent-templates"
    reference_source_dir = plugin_root / "references"
    pairs: list[tuple[pathlib.Path, pathlib.Path, str]] = []
    for filename in AGENT_FILENAMES:
        pairs.append((source_dir / filename, target_dir / filename, filename))
    for filename in REFERENCE_FILENAMES:
        rel = f"references/{filename}"
        pairs.append((reference_source_dir / filename, target_dir / rel, rel))
    return pairs


def validate_sources(pairs: list[tuple[pathlib.Path, pathlib.Path, str]]) -> bool:
    ok = True
    for source, _, _ in pairs:
        if not source.is_file():
            print(f"Missing source file: {source}", file=sys.stderr)
            ok = False
    return ok


def write_manifest(target_dir: pathlib.Path, plugin_version: str, scope: str, pairs: list[tuple[pathlib.Path, pathlib.Path, str]]) -> None:
    files = []
    for _, target, rel in pairs:
        if target.exists():
            files.append({"path": rel, "sha256": sha256(target)})
    manifest = {
        "plugin_name": PLUGIN_NAME,
        "plugin_version": plugin_version,
        "installed_at": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat(),
        "scope": scope,
        "files": files,
    }
    (target_dir / MANIFEST_FILENAME).write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def dry_run(scope: str, target_dir: pathlib.Path, pairs: list[tuple[pathlib.Path, pathlib.Path, str]], overwrite: bool) -> int:
    print(f"Scope: {scope}")
    print(f"Target directory: {target_dir}")
    print("Planned files:")
    for source, target, rel in pairs:
        if not source.is_file():
            status = "missing-source"
        elif target.exists() and not overwrite:
            status = "skip-existing"
        elif target.exists() and overwrite:
            status = "overwrite"
        else:
            status = "write"
        print(f"  {rel}: {status} -> {target}")
    print("Dry run only; no files written.")
    return 0


def check_install(target_dir: pathlib.Path, pairs: list[tuple[pathlib.Path, pathlib.Path, str]]) -> int:
    ok = True
    for source, target, rel in pairs:
        if not source.is_file():
            print(f"MISSING_SOURCE: {rel}")
            ok = False
            continue
        if not target.exists():
            print(f"MISSING: {rel}")
            ok = False
        elif not target.is_file():
            print(f"INVALID: {rel} is not a file")
            ok = False
        elif sha256(source) != sha256(target):
            print(f"STALE_OR_MODIFIED: {rel}")
            ok = False
        else:
            print(f"MATCH: {rel}")
    manifest = target_dir / MANIFEST_FILENAME
    if manifest.is_file():
        print(f"MANIFEST: {manifest}")
    elif manifest.exists():
        print(f"INVALID: {MANIFEST_FILENAME} is not a file")
        ok = False
    else:
        print(f"MISSING: {MANIFEST_FILENAME}")
        ok = False
    return 0 if ok else 3


def verify_install(
    scope: str,
    codex_home: pathlib.Path,
    target_dir: pathlib.Path,
    pairs: list[tuple[pathlib.Path, pathlib.Path, str]],
    require_user_instructions: bool,
) -> int:
    ok = True
    for _, target, rel in pairs:
        if not target.exists():
            print(f"VERIFY MISSING: {rel}", file=sys.stderr)
            ok = False
        elif not target.is_file():
            print(f"VERIFY INVALID: {rel} is not a file", file=sys.stderr)
            ok = False
    manifest = target_dir / MANIFEST_FILENAME
    if not manifest.exists():
        print(f"VERIFY MISSING: {MANIFEST_FILENAME}", file=sys.stderr)
        ok = False
    elif not manifest.is_file():
        print(f"VERIFY INVALID: {MANIFEST_FILENAME} is not a file", file=sys.stderr)
        ok = False
    if scope == "user" and require_user_instructions:
        agents_md = codex_home / "AGENTS.md"
        text = agents_md.read_text(encoding="utf-8") if agents_md.exists() else ""
        if INSTRUCTIONS_START not in text or INSTRUCTIONS_END not in text:
            print(f"VERIFY MISSING: managed AGENTS.md block in {agents_md}", file=sys.stderr)
            ok = False
    return 0 if ok else 3


def install_files(
    target_dir: pathlib.Path,
    pairs: list[tuple[pathlib.Path, pathlib.Path, str]],
    overwrite: bool,
) -> tuple[list[pathlib.Path], list[pathlib.Path]]:
    target_dir.mkdir(parents=True, exist_ok=True)
    installed: list[pathlib.Path] = []
    skipped: list[pathlib.Path] = []
    for source, target, _ in pairs:
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists() and not overwrite:
            skipped.append(target)
            continue
        shutil.copyfile(source, target)
        installed.append(target)
    return installed, skipped


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Install Codex custom-agent profiles for the coding-agent orchestration harness."
    )
    parser.add_argument("--scope", choices=SCOPES, default=None, help="Install scope. Omit to be prompted.")
    parser.add_argument("--repo-root", type=pathlib.Path, default=None, help="Repository root for --scope repo. Defaults to nearest .git parent, otherwise the current working directory.")
    parser.add_argument("--overwrite", "--overwrite-agents", action="store_true", dest="overwrite_agents", help="Replace existing installed agent profiles and references.")
    parser.add_argument("--user-instructions", choices=INSTRUCTIONS_ACTIONS, default="ask", help="For user scope, ask/add/skip the managed AGENTS.md loader block.")
    mode_group = parser.add_mutually_exclusive_group()
    mode_group.add_argument("--dry-run", action="store_true", help="Print planned writes/skips without writing files.")
    mode_group.add_argument("--check", action="store_true", help="Compare installed files against source templates.")
    mode_group.add_argument("--verify", action="store_true", help="Verify required installed files and optional loader block.")
    parser.add_argument("--no-write-manifest", dest="write_manifest", action="store_false", default=True, help="Do not write the managed install freshness manifest.")
    parser.add_argument("--codex-home", type=pathlib.Path, default=pathlib.Path.home() / ".codex", help=argparse.SUPPRESS)
    args = parser.parse_args()

    script_path = pathlib.Path(__file__)
    plugin_root = find_plugin_root(script_path)
    plugin_version = load_plugin_version(plugin_root)
    try:
        instructions_block = load_instructions_block(plugin_root)
    except (FileNotFoundError, ValueError) as error:
        print(str(error), file=sys.stderr)
        return 1

    scope = args.scope or ask_scope()
    repo_root = None
    if scope == "repo":
        repo_root = args.repo_root.resolve() if args.repo_root else find_repo_root(pathlib.Path.cwd())

    codex_home = args.codex_home.resolve()
    target_dir = resolve_target_dir(scope, repo_root, codex_home)
    pairs = source_target_pairs(plugin_root, target_dir)
    if not validate_sources(pairs):
        return 1

    if args.dry_run:
        return dry_run(scope, target_dir, pairs, args.overwrite_agents)
    if args.check:
        return check_install(target_dir, pairs)
    if args.verify:
        return verify_install(scope, codex_home, target_dir, pairs, args.user_instructions == "add")

    installed, skipped = install_files(target_dir, pairs, args.overwrite_agents)

    if args.write_manifest:
        write_manifest(target_dir, plugin_version, scope, pairs)

    print(f"Scope: {scope}")
    print(f"Target directory: {target_dir}")

    if installed:
        print("Installed:")
        for path in installed:
            print(f"  {path}")

    if skipped:
        print("Skipped existing files; pass --overwrite-agents to replace:")
        for path in skipped:
            print(f"  {path}")

    if not installed and not skipped:
        print("No agent profiles were installed.")

    if args.write_manifest:
        print(f"Manifest: {target_dir / MANIFEST_FILENAME}")

    instructions_status = "not-applicable"
    if scope == "user":
        instructions_status = install_user_instructions(codex_home, args.user_instructions, instructions_block)
        print(f"User instructions: {instructions_status}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
