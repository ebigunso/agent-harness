"""Validate the manifest's sections against --frozen; no model calls or dependencies."""
from pathlib import Path
import argparse
import re
import subprocess

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[3]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--frozen", required=True)
    args = parser.parse_args()
    manifest = dict(re.findall(r"^  ([\w-]+): \[(.*?)\]$", (BASE / "manifest.yaml").read_text(encoding="utf-8"), re.M))
    assert manifest, "manifest has no sections"
    registered = {(section, arm): text for section, arm, text in re.findall(r"^### (tv-\d+) ([ABC])\n\n```text\n(.*?)\n```", (BASE / "protocol.md").read_text(encoding="utf-8"), re.M | re.S)}
    counts = {"planted": 0, "clean": 0}
    expected_counts = {"planted": 0, "clean": 0}
    owned = [Path(__file__)]
    if (BASE / "authoring-notes.md").exists():
        owned.append(BASE / "authoring-notes.md")
    # Read the registered revision because the working copy is edited as outcomes land.
    def frozen(path):
        return subprocess.run(["git", "-C", str(ROOT), "show", f"{args.frozen}:{path}"], capture_output=True, check=True).stdout.replace(b"\r\n", b"\n")
    validation = frozen("plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/testing-validation.md")
    skip = next(line for line in validation.splitlines() if line.startswith(b"- Skip-capable tests"))
    baseline = next(line for line in validation.splitlines() if line.startswith(b"- When validation fails in tests"))
    sources = dict(zip(("tv-1", "tv-2"), skip.split(b", and ", 1)))
    sources["tv-3"] = baseline
    for section in manifest:
        ids = [item.strip() for item in manifest[section].split(",")]
        assert ids and len(ids) == len(set(ids)), section
        section_counts = {kind: sum(ident.startswith(section + "-c") == (kind == "clean") for ident in ids) for kind in counts}
        for kind in counts:
            expected_counts[kind] += section_counts[kind]
        key = BASE / "keys" / f"{section}.md"
        key_text = key.read_text(encoding="utf-8")
        owned.append(key)
        for ident in ids:
            path = BASE / "fixtures" / f"{ident}.md"
            text = path.read_text(encoding="utf-8")
            header = re.match(r"---\n(.*?)\n---\n", text, re.S)
            assert header, f"missing frontmatter: {ident}"
            fields = dict(line.split(": ", 1) for line in header[1].splitlines())
            kind = "clean" if ident.startswith(section + "-c") else "planted"
            assert fields == {"id": ident, "section": section, "type": kind}, ident
            assert ident in key_text and "Task framing:" in text, ident
            counts[kind] += 1
            if section.startswith("tv-"):
                diff = re.search(r"```diff\n(.*?)```", text, re.S)
                assert diff and "Commit message:" in text and "Reviewer notes:" in text, ident
                subprocess.run(["git", "apply", "--numstat", "-"], input=diff[1].encode(), cwd=ROOT, check=True, capture_output=True)
            else:
                assert all(word in text.lower() for word in ("command", "exit code", "stdout", "stderr", "cwd", "windows")), ident
            owned.append(path)
        b_path = BASE / "arms" / f"{section}-B.md"
        c_path = BASE / "arms" / f"{section}-C.md"
        a_path = BASE / "arms" / f"{section}-A.md"
        a = a_path.read_text(encoding="utf-8").rstrip("\n")
        b, c = b_path.read_bytes(), c_path.read_bytes()
        source = sources[section]
        assert b.replace(b"\r\n", b"\n").strip() == source.strip(), f"B differs from source: {section}"
        for arm, path in (("A", a_path), ("B", b_path), ("C", c_path)):
            assert path.read_text(encoding="utf-8").rstrip("\n") == registered[(section, arm)], f"unregistered arm: {section}-{arm}"
        assert registered[(section, "C")].startswith(a + " If that evidence is absent, "), f"C lacks its obligation and conditional hint: {section}"
        # Character counts are diagnostic only; the protocol registers the complete C text.
        b_chars, c_chars = len(b.decode().replace("\r\n", "\n")), len(c.decode().replace("\r\n", "\n"))
        owned.extend((a_path, b_path, c_path))
        print(f"{section}: {section_counts['planted']} planted + {section_counts['clean']} clean; B={b_chars}, C={c_chars} characters")
    for path in owned:
        assert all(line == line.rstrip() for line in path.read_text(encoding="utf-8").splitlines()), f"trailing whitespace: {path.name}"
    assert counts == expected_counts, counts
    print(f"PASS: {sum(counts.values())} matching fixtures; {len(manifest)} keys; {3 * len(manifest)} registered arms; C retains obligation plus conditional hint")


if __name__ == "__main__":
    main()
