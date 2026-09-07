"""Merge grader YAML files with the private mapping into results-<model>.yaml for score.py.
Usage: python run/unblind.py astra|fable
"""
import json, sys
from pathlib import Path
import yaml

HERE = Path(__file__).resolve().parents[1]
model = sys.argv[1]
mapping = json.load(open(HERE / "work" / "blind" / model / "mapping.json", encoding="utf-8"))
records, seen, problems = [], set(), []
for g in sorted((HERE / "work" / "grades" / model).glob("*.yaml")):
    doc = yaml.safe_load(g.read_text(encoding="utf-8")) or {}
    for r in doc.get("records") or []:
        bid = str(r.get("id", "")).strip()
        m = mapping.get(bid)
        if not m:
            problems.append(f"{g.name}: unknown id {bid}"); continue
        if bid in seen:
            problems.append(f"{g.name}: duplicate id {bid}"); continue
        seen.add(bid)
        if m["fixture"] != r.get("fixture"):
            problems.append(f"{g.name}: id {bid} fixture {r.get('fixture')} != {m['fixture']}")
        clean = m["fixture"].rsplit("-", 1)[-1].startswith("c")
        rec = {"arm": m["arm"], "section": m["section"], "fixture": m["fixture"], "seed": m["seed"]}
        if clean:
            rec["false_positives"] = r.get("false_positives")
        else:
            rec["score"] = r.get("score")
        records.append(rec)
missing = [bid for bid in mapping if bid not in seen]
name = {"astra": "gpt-6-astra", "fable": "claude-fable-5-1"}[model]
out = HERE / "work" / f"results-{model}.yaml"
out.write_text(yaml.safe_dump({"model": name, "run_date": "2026-09-08", "records": records}, sort_keys=False), encoding="utf-8")
print(f"{model}: {len(records)} records, {len(missing)} ungraded, {len(problems)} problems -> {out}")
for p in problems[:20]: print("  ", p)
for b in missing[:10]: print("   missing", b, mapping[b]["cell"])
