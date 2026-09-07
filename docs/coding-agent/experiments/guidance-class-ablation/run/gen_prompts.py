"""Generate one prompt file per cell for the pilot: work/prompts/<arm>-<fixture>-s<seed>.txt.

Usage: python run/gen_prompts.py [section ...]   (default: the seven pilot sections)
Prompt = arm context (none for A; arms/<section>-B.md or -C.md) + the protocol prompt + the fixture
body with its frontmatter stripped. Identical across models; seeds are separate calls of the same prompt.
"""

import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parents[1]
PILOT = ["rb-windows-npm-eperm-locks", "rb-windows-docker-grpc-localhost-ipv6", "rb-windows-python-console-encoding",
         "rb-powershell-json-array-cardinality", "rb-persistent-shell-cwd-normalization", "cp-2", "cp-9"]
REVIEW = ("You are reviewing a proposed change. The task the author was given is stated at the top of the fixture, "
          "followed by the diff. Report every defect you would block or flag in review, as a list. For each finding give: "
          "file/location, what is wrong, why it matters, and what you would require instead. If the change is acceptable "
          "as-is, say so explicitly. Do not pad the list; report only findings you would actually raise.")
RUNBOOK = ("A command failed in the workspace described below. State the cause, the smallest safe remediation, and how "
           "you would confirm it worked. If the failure is not a workspace problem, say so.")


def main(sections):
    manifest = yaml.safe_load((HERE / "manifest.yaml").read_text(encoding="utf-8"))
    out = HERE / "work" / "prompts"
    out.mkdir(parents=True, exist_ok=True)
    n = 0
    for section in sections:
        prompt = RUNBOOK if section.startswith("rb-") else REVIEW
        arms = {"A": "", "B": (HERE / "arms" / f"{section}-B.md").read_text(encoding="utf-8"),
                "C": (HERE / "arms" / f"{section}-C.md").read_text(encoding="utf-8")}
        for fixture in manifest["sections"][section]:
            body = (HERE / "fixtures" / f"{fixture}.md").read_text(encoding="utf-8")
            body = re.sub(r"\A---\n.*?\n---\n", "", body, count=1, flags=re.DOTALL).strip()
            for arm, ctx in arms.items():
                head = f"Reference material loaded for this review:\n\n{ctx.strip()}\n\n---\n\n" if ctx else ""
                text = f"{head}{prompt}\n\n{body}\n"
                for seed in range(1, manifest["seeds"] + 1):
                    (out / f"{arm}-{fixture}-s{seed}.txt").write_text(text, encoding="utf-8", newline="\n")
                    n += 1
    print(f"wrote {n} prompts to {out}")


if __name__ == "__main__":
    main(sys.argv[1:] or PILOT)
