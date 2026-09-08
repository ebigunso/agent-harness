"""Merge grader YAML files with the private mapping into results-<model>.yaml for score.py.
Usage: python run/unblind.py astra|fable

Carry-forward: a section with no grade file in work/grades/<model>/ takes its rows verbatim from
work/results-<model>-v1.yaml (round-1 results), and the run prints which sections were carried.
Adjudications: work/adjudications.yaml lists {model, cell, score|false_positives, reason} overrides
applied after merging; the grader's original value stays in its grade file.
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
graded_sections = {mapping[b]["section"] for b in seen}
carried = []
v1 = HERE / "work" / f"results-{model}-v1.yaml"
if v1.exists():
    for r in (yaml.safe_load(v1.read_text(encoding="utf-8")) or {}).get("records") or []:
        if r["section"] not in graded_sections:
            records.append(dict(r)); carried.append(r["section"])
            for b, m in mapping.items():
                if (m["arm"], m["fixture"], m["seed"]) == (r["arm"], r["fixture"], r["seed"]): seen.add(b)
adj = HERE / "work" / "adjudications.yaml"
applied = 0
if adj.exists():
    for a in (yaml.safe_load(adj.read_text(encoding="utf-8")) or {}).get("adjudications") or []:
        if a["model"] != model: continue
        arm, rest = a["cell"].split("-", 1); fixture, seed = rest.rsplit("-s", 1)
        for r in records:
            if (r["arm"], r["fixture"], r["seed"]) == (arm, fixture, int(seed)):
                for k in ("score", "false_positives"):
                    if k in a: r[k] = a[k]
                applied += 1
missing = [bid for bid in mapping if bid not in seen]
name = {"astra": "gpt-6-astra", "fable": "claude-fable-5-1"}[model]
out = HERE / "work" / f"results-{model}.yaml"
out.write_text(yaml.safe_dump({"model": name, "run_date": "2026-09-08", "records": records}, sort_keys=False), encoding="utf-8")
print(f"{model}: {len(records)} records, {len(missing)} ungraded, {len(problems)} problems, carried from round 1: {sorted(set(carried))}, adjudications applied: {applied} -> {out}")
for p in problems[:20]: print("  ", p)
for b in missing[:10]: print("   missing", b, mapping[b]["cell"])
