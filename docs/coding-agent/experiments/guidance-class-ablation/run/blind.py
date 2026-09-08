"""Blind model outputs for grading: work/<model>/<cell>.txt -> work/blind/<model>/<section>/<fixture>__<uuid>.txt (the fixture id is needed to apply the key; the arm and seed stay hidden)

Keeps only the model's final response (strips the echoed prompt and banner), assigns a random id per
cell, and writes work/blind/<model>/mapping.json (private to the Orchestrator; graders never read it).
Usage: python run/blind.py astra|fable
"""
import json, re, sys, uuid
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
model = sys.argv[1]
src = HERE / "work" / model
out = HERE / "work" / "blind" / model
mapping = {}
for p in sorted(src.glob("*.txt")):
    cell = p.stem
    arm, rest = cell.split("-", 1)
    fixture, seed = rest.rsplit("-s", 1)
    section = re.sub(r"-(?:c\d|\d{2})$", "", fixture)
    t = p.read_text(encoding="utf-8", errors="replace")
    if model == "astra":
        blocks = t.split("\ncodex\n")
        body = blocks[-1] if len(blocks) > 1 else t
        body = re.sub(r"\ntokens used\n.*$", "", body, flags=re.DOTALL)
        body = re.sub(r"\n__ABLATION_DONE__.*$", "", body, flags=re.DOTALL)
    else:
        body = t
    bid = uuid.uuid4().hex[:12]
    (out / section).mkdir(parents=True, exist_ok=True)
    (out / section / f"{fixture}__{bid}.txt").write_text(body.strip() + "\n", encoding="utf-8", newline="\n")
    mapping[bid] = {"cell": cell, "arm": arm, "fixture": fixture, "seed": int(seed), "section": section}
(out / "mapping.json").write_text(json.dumps(mapping, indent=1), encoding="utf-8")
print(f"{model}: {len(mapping)} blinded into {out}")
