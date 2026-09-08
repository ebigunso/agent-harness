"""Validate the authored seven-section pilot; no model calls or dependencies."""
from pathlib import Path
import re
import subprocess

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[3]
PILOT = (
    "cp-2", "cp-9", "cp-3", "cp-4", "cp-5", "cp-6", "cp-7", "cp-8", "cp-10",
    "ag-1", "ag-2", "ag-3", "ag-4", "ag-5", "ag-6", "ag-7", "rb-windows-npm-eperm-locks",
    "rb-windows-docker-grpc-localhost-ipv6",
    "rb-windows-python-console-encoding",
    "rb-powershell-json-array-cardinality",
    "rb-persistent-shell-cwd-normalization",
)


def main():
    manifest = dict(re.findall(r"^  ([\w-]+): \[(.*?)\]$", (BASE / "manifest.yaml").read_text(encoding="utf-8"), re.M))
    counts = {"planted": 0, "clean": 0}
    owned = [Path(__file__), BASE / "authoring-notes.md"]
    # Sources are read from the frozen revision (main 2710486), because the working copy is edited as outcomes land.
    def frozen(path):
        return subprocess.run(["git", "-C", str(ROOT), "show", f"2710486:{path}"], capture_output=True, check=True).stdout.replace(b"\r\n", b"\n")
    core = frozen("plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/core-principles.md")
    gates = frozen("plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/architecture-gates.md")
    for section in PILOT:
        ids = [item.strip() for item in manifest[section].split(",")]
        expected = {f"{section}-{n:02}" for n in range(1, 13)} | {f"{section}-c{n}" for n in range(1, 5)}
        assert len(ids) == 16 and set(ids) == expected, section
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
            if section.startswith(("cp-", "ag-")):
                diff = re.search(r"```diff\n(.*?)```", text, re.S)
                assert diff and "Commit message:" in text and "Reviewer notes:" in text, ident
                subprocess.run(["git", "apply", "--numstat", "-"], input=diff[1].encode(), cwd=ROOT, check=True, capture_output=True)
            else:
                assert all(word in text.lower() for word in ("command", "exit code", "stdout", "stderr", "cwd", "windows")), ident
            owned.append(path)
        b_path = BASE / "arms" / f"{section}-B.md"
        c_path = BASE / "arms" / f"{section}-C.md"
        b, c = b_path.read_bytes(), c_path.read_bytes()
        if section.startswith("cp-"):
            source = re.search(rb"(?ms)^### " + section[3:].encode() + rb"\).*?(?=^### |^## |\Z)", core)[0]
        elif section.startswith("ag-"):
            source = re.search(rb"(?ms)^### Gate " + section[3:].encode() + rb":.*?(?=^### |^## |\Z)", gates)[0]
        else:
            source = frozen("plugins/coding-agent-orchestration-harness/skills/workspace-troubleshooting/references/" + section[3:] + ".md")
        assert b.replace(b"\r\n", b"\n").strip() == source.strip(), f"B differs from source: {section}"
        # Check LF-normalized character counts too, so Git newline conversion cannot break the cap.
        b_chars, c_chars = len(b.decode().replace("\r\n", "\n")), len(c.decode().replace("\r\n", "\n"))
        assert c_chars * 3 <= b_chars, (section, b_chars, c_chars)
        owned.extend((b_path, c_path))
        print(f"{section}: 12 planted + 4 clean; B={b_chars}, C={c_chars} characters")
    for path in owned:
        assert all(line == line.rstrip() for line in path.read_text(encoding="utf-8").splitlines()), f"trailing whitespace: {path.name}"
    assert counts == {"planted": 12 * len(PILOT), "clean": 4 * len(PILOT)}, counts
    print(f"PASS: {16 * len(PILOT)} matching fixtures; {len(PILOT)} keys; {2 * len(PILOT)} arms; all C <= B/3")


if __name__ == "__main__":
    main()
