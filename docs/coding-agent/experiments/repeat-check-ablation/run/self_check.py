"""Exercise the registered pipeline with local stubs only; never calls a model CLI."""
import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

import yaml

BASE = Path(__file__).resolve().parents[1]


def run(args, cwd, expected=0, env=None):
    result = subprocess.run(args, cwd=cwd, env=env, text=True, encoding="utf-8", capture_output=True)
    print(result.stdout.strip())
    if result.returncode != expected:
        print(result.stderr)
    assert result.returncode == expected, (args, result.returncode)
    return result.stdout


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--frozen", required=True)
    parser.add_argument("--bash", default="bash")
    args = parser.parse_args()
    # The temporary tree and its automatic cleanup are confined to the assigned run directory.
    with tempfile.TemporaryDirectory(prefix="stub-", dir=BASE / "run") as directory:
        stub = Path(directory).resolve()
        assert stub.is_relative_to((BASE / "run").resolve())
        for name in ("protocol.md", "validate_pilot.py", "score.py"):
            shutil.copyfile(BASE / name, stub / name)
        shutil.copytree(BASE / "arms", stub / "arms")
        (stub / "run").mkdir()
        for name in ("gen_prompts.py", "run_fable.sh", "blind.py", "unblind.py"):
            shutil.copyfile(BASE / "run" / name, stub / "run" / name)
        manifest = yaml.safe_load((BASE / "manifest.yaml").read_text(encoding="utf-8"))
        manifest["sections"] = {section: [f"{section}-01", f"{section}-c1"] for section in manifest["sections"]}
        manifest_text = "models: [claude-fable-5-1, gpt-6-astra]\nseeds: 1\nsections:\n"
        for section, ids in manifest["sections"].items():
            manifest_text += f"  {section}: [{', '.join(ids)}]\n"
        (stub / "manifest.yaml").write_text(manifest_text, encoding="utf-8")
        for folder in ("fixtures", "keys"):
            (stub / folder).mkdir()
        for section, ids in manifest["sections"].items():
            (stub / "keys" / f"{section}.md").write_text("\n".join(ids), encoding="utf-8")
            for ident in ids:
                kind = "clean" if ident.endswith("-c1") else "planted"
                text = (f"---\nid: {ident}\nsection: {section}\ntype: {kind}\n---\n"
                        f"Task framing: fixture {ident}; synthetic pipeline check only.\n"
                        "Commit message: Change a value\nReviewer notes: Stub validation summary.\n"
                        "```diff\ndiff --git a/value.txt b/value.txt\n--- a/value.txt\n+++ b/value.txt\n@@ -1 +1 @@\n-old\n+new\n```\n")
                (stub / "fixtures" / f"{ident}.md").write_text(text, encoding="utf-8")
        run([sys.executable, "run/gen_prompts.py"], stub)
        prompts = sorted((stub / "work/prompts").glob("*.txt"))
        assert len(prompts) == 18
        for prompt in prompts:
            arm, rest = prompt.stem.split("-", 1)
            fixture = rest.rsplit("-s", 1)[0]
            section = re.sub(r"-(?:c\d|\d{2})$", "", fixture)
            text = prompt.read_text(encoding="utf-8")
            context = text.split("\n\n", 1)[1].split("\n\n---\n\n", 1)[0]
            registered = (stub / "arms" / f"{section}-{arm}.md").read_text(encoding="utf-8").strip()
            assert context == registered, prompt.name
            assert "type: planted" not in text and "type: clean" not in text
        print("PASS: 18 prompts each contain exactly their registered A/B/C context; fixture types stripped")
        run([sys.executable, "validate_pilot.py", "--frozen", args.frozen], stub)

        # A function named claude intercepts the runner's CLI call; the real CLI is never invoked.
        cli = stub / "fake_cli.py"
        cli.write_text('''import json, os, sys
from pathlib import Path
text = sys.stdin.read()
assert sys.argv[sys.argv.index("--setting-sources") + 1] == ""
context = text.split("\\n\\n", 1)[1].split("\\n\\n---\\n\\n", 1)[0]
a = (Path(os.environ["STUB_ROOT"]) / "arms/tv-1-A.md").read_text().strip()
bad = context == a and "fixture tv-1-c1;" in text
mode = os.environ.get("STUB_FAILURE", "error")
with open(Path(os.environ["STUB_ROOT"]) / "calls.txt", "a") as calls:
    calls.write("call\\n")
print(json.dumps({"is_error": bad and mode == "error", "result": "" if bad and mode == "empty" else "synthetic result"}))
''', encoding="utf-8")
        failed_cell = "A-tv-1-c1-s1"
        (stub / "work/fable").mkdir()
        (stub / "work/fable-json").mkdir()
        (stub / "work/fable" / f"{failed_cell}.txt").write_text("stale\n__ABLATION_DONE__ exit=0\n")
        (stub / "work/fable-json" / f"{failed_cell}.json").write_text('{"is_error":true,"result":"not success"}')
        env = dict(os.environ, STUB_ROOT=stub.as_posix(), STUB_CLI=cli.as_posix(), STUB_PYTHON=Path(sys.executable).as_posix())
        shell = ('python() { "$STUB_PYTHON" "$@"; }; '
                 'claude() { python "$STUB_CLI" "$@"; }; '
                 'timeout() { shift; "$@"; }; '
                 'export -f python claude timeout; bash "$1" "$2" 1')
        runner = [args.bash, "-c", shell, "_", (stub / "run/run_fable.sh").as_posix(), stub.as_posix()]
        run(runner, stub, expected=3, env=env)
        assert len((stub / "calls.txt").read_text().splitlines()) == 18, "done-only cell was incorrectly skipped"
        assert json.loads((stub / "work/fable-json" / f"{failed_cell}.json").read_text())["is_error"] is True
        assert "__ABLATION_DONE__" not in (stub / "work/fable" / f"{failed_cell}.txt").read_text()
        print("PASS: is_error result rejected; stale done marker did not skip execution or count completion")
        run(runner, stub, expected=3, env=dict(env, STUB_FAILURE="empty"))
        assert len((stub / "calls.txt").read_text().splitlines()) == 19, "successful cells should be reused"
        assert "__ABLATION_DONE__" not in (stub / "work/fable" / f"{failed_cell}.txt").read_text()
        print("PASS: empty result rejected; only failed cell retried")

        (stub / "work/astra").mkdir()
        for prompt in prompts:
            (stub / "work/astra" / prompt.name).write_text("synthetic result\n__ABLATION_DONE__ exit=0\n")
        for model, count in (("fable", 17), ("astra", 18)):
            run([sys.executable, "run/blind.py", model], stub)
            mapping = json.loads((stub / "work/blind" / model / "mapping.json").read_text())
            assert len(mapping) == count
            assert all(row["cell"] != failed_cell for row in mapping.values()) if model == "fable" else True
            grades = stub / "work/grades" / model
            grades.mkdir(parents=True)
            rows = [{"id": bid, "fixture": row["fixture"], "score": 1, "false_positives": 0} for bid, row in mapping.items()]
            (grades / "stub.yaml").write_text(yaml.safe_dump({"records": rows}), encoding="utf-8")
            run([sys.executable, "run/unblind.py", model], stub)
            results = yaml.safe_load((stub / "work" / f"results-{model}.yaml").read_text())
            assert results["run_date"] == datetime.now(timezone.utc).date().isoformat()
        output = run([sys.executable, "score.py", "--manifest", "manifest.yaml", "--seeds", "1", "work/results-fable.yaml", "work/results-astra.yaml"], stub)
        assert "tv-1: INCOMPLETE" in output and "tv-2: DELETE" in output and "tv-3: DELETE" in output
        print("PASS: unsuccessful cell excluded from grading; score remains INCOMPLETE; zero model calls")


if __name__ == "__main__":
    main()
