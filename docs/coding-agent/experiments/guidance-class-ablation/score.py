"""Score the guidance-class ablation and apply the pre-registered rule in protocol.md.

Usage: python score.py [--manifest manifest.yaml] [--seeds N] results-fable.yaml results-astra.yaml [...]
       python score.py --self-test

manifest.yaml registers the fleet, the seed count, and every fixture per section. Each
results file carries one model; every registered model must appear exactly once. Verdicts
are per section on the worst model (lowest arm-A detection); ties are evaluated on every
tied model and the most protective outcome stands. The FP guard is checked on every model.
A section missing any registered fixture, seed, arm, model, or grading value is INCOMPLETE.
Adapted from 47c409c:docs/coding-agent/experiments/language-guide-ablation/score_stage1.py.
"""

import collections
import sys

DELTA_LIFT = 0.10      # dB below this -> DELETE
DELTA_C_EQUIV = 0.05   # dC within this of dB -> COMPRESS
FP_REGRESSION = 0.10   # arm FP rate above that model's A by more than this -> cannot adopt
ARMS = "ABC"
PROTECTION = {"DELETE": 0, "COMPRESS": 1, "KEEP": 2}


def is_clean(fixture):
    return fixture.rsplit("-", 1)[-1].startswith("c")


def summarize(doc, manifest):
    """(section, arm) -> (detection, fp_rate); plus section -> incompleteness reasons."""
    seeds_required = manifest["seeds"]
    cells = {}  # (section, arm, fixture, seed) -> value
    problems = collections.defaultdict(list)
    for r in doc.get("records") or []:
        key = (r["section"], r["arm"], r["fixture"], r.get("seed"))
        value = r.get("false_positives") if is_clean(r["fixture"]) else r.get("score")
        if value is None:
            problems[r["section"]].append(f"{r['fixture']} arm {r['arm']} seed {r.get('seed')}: no grading value")
            continue
        cells[key] = float(value)
    summary = {}
    for section, fixtures in manifest["sections"].items():
        for arm in ARMS:
            scores, fps = [], []
            for fixture in fixtures:
                for seed in range(1, seeds_required + 1):
                    v = cells.get((section, arm, fixture, seed))
                    if v is None:
                        problems[section].append(f"{fixture} arm {arm} seed {seed}: missing")
                    elif is_clean(fixture):
                        fps.append(v)
                    else:
                        scores.append(v)
            if scores and fps:
                summary[(section, arm)] = (sum(scores) / len(scores), sum(fps) / len(fps))
    return summary, problems


def verdict_on(summary, section):
    a, b, c = (summary[(section, arm)] for arm in ARMS)
    d_b, d_c = b[0] - a[0], c[0] - a[0]
    if d_b < DELTA_LIFT:
        return "DELETE", d_b, d_c
    if d_c >= d_b - DELTA_C_EQUIV:
        return "COMPRESS", d_b, d_c
    return "KEEP", d_b, d_c


def decide(models, manifest):
    """models: list of (name, doc). Returns {section: (verdict, worst_models, flags)}."""
    names = [name for name, _ in models]
    registered = list(manifest["models"])
    fleet_problems = [f"duplicate model {n}" for n, k in collections.Counter(names).items() if k > 1]
    fleet_problems += [f"missing model {m}" for m in registered if m not in names]
    fleet_problems += [f"unregistered model {n}" for n in names if n not in registered]
    per_model = {name: summarize(doc, manifest) for name, doc in models}
    out = {}
    for s in manifest["sections"]:
        problems = list(fleet_problems)
        for name, (summary, probs) in per_model.items():
            problems += [f"{name}: {p}" for p in probs.get(s, [])]
        if problems:
            out[s] = ("INCOMPLETE", [], problems[:12] + ([f"... {len(problems) - 12} more"] if len(problems) > 12 else []))
            continue
        lowest = min(per_model[name][0][(s, "A")][0] for name in per_model)
        tied = [name for name in per_model if per_model[name][0][(s, "A")][0] == lowest]
        results = {name: verdict_on(per_model[name][0], s) for name in tied}
        verdict = max((v for v, _, _ in results.values()), key=PROTECTION.__getitem__)
        flags = [f"{name}: {v} (dB {db:+.0%}, dC {dc:+.0%})" for name, (v, db, dc) in sorted(results.items())]
        for name, (summary, _) in sorted(per_model.items()):
            a_fp = summary[(s, "A")][1]
            for arm in "BC":
                fp = summary[(s, arm)][1]
                if fp > a_fp + FP_REGRESSION:
                    flags.append(f"{name}: arm {arm} FP regression ({fp:.2f} vs A {a_fp:.2f}); cannot adopt")
        out[s] = (verdict, sorted(tied), flags)
    return out


def main(argv):
    import yaml
    manifest_path = "manifest.yaml"
    seeds_cap = None
    if "--manifest" in argv:
        i = argv.index("--manifest")
        manifest_path = argv[i + 1]
        del argv[i:i + 2]
    if "--seeds" in argv:
        i = argv.index("--seeds")
        seeds_cap = int(argv[i + 1])
        del argv[i:i + 2]
    manifest = yaml.safe_load(open(manifest_path, encoding="utf-8"))
    if seeds_cap is not None:
        manifest["seeds"] = seeds_cap
    models = []
    for path in argv:
        doc = yaml.safe_load(open(path, encoding="utf-8"))
        models.append((doc.get("model") or path, doc))
    for s, (verdict, worst, flags) in decide(models, manifest).items():
        print(f"{s}: {verdict}" + (f" [worst: {', '.join(worst)}]" if worst else ""))
        for f in flags:
            print(f"    {f}")


# ---- self-test ----------------------------------------------------------------

_MANIFEST = {"models": ["m1", "m2"], "seeds": 2, "sections": {"x": ["x-01", "x-02", "x-c1"]}}


def _doc(model, a, b, c, fp=(0, 0, 0), seeds=(1, 2), decoys=True, fixtures=("x-01", "x-02"), null_score=False):
    recs = []
    for arm, det, f in zip(ARMS, (a, b, c), fp):
        for seed in seeds:
            for fx in fixtures:
                recs.append({"arm": arm, "section": "x", "fixture": fx, "seed": seed, "score": None if null_score else det})
            if decoys:
                recs.append({"arm": arm, "section": "x", "fixture": "x-c1", "seed": seed, "false_positives": f})
    return model, {"model": model, "records": recs}


def self_test():
    def v(ms, manifest=_MANIFEST):
        return decide(ms, manifest)["x"]
    assert v([_doc("m1", .5, .55, .5), _doc("m2", .9, 1, 1)])[0] == "DELETE"
    assert v([_doc("m1", .5, .8, .8), _doc("m2", .9, 1, 1)])[0] == "COMPRESS"
    assert v([_doc("m1", .5, .8, .5), _doc("m2", .9, 1, 1)])[0] == "KEEP"
    # tie on A: most protective outcome stands regardless of argument order
    tie = [_doc("m1", .5, .5, .5), _doc("m2", .5, 1, .5)]
    assert v(tie)[0] == "KEEP" and v(tie[::-1])[0] == "KEEP" and v(tie)[1] == ["m1", "m2"]
    # FP guard fires on a model that is not the worst one
    r = v([_doc("m1", .25, .75, .75), _doc("m2", .5, 1, 1, fp=(0, 0, .25))])
    assert r[0] == "COMPRESS" and any("m2: arm C FP regression" in f for f in r[2])
    # incompleteness: registered fixture wholly absent, null grading value, missing decoys,
    # missing model, duplicate model, unregistered model, short seeds
    assert v([_doc("m1", .5, .8, .8, fixtures=("x-01",)), _doc("m2", .9, 1, 1)])[0] == "INCOMPLETE"
    assert v([_doc("m1", .5, .8, .8, null_score=True), _doc("m2", .9, 1, 1)])[0] == "INCOMPLETE"
    assert v([_doc("m1", .5, .8, .8, decoys=False), _doc("m2", .9, 1, 1)])[0] == "INCOMPLETE"
    assert v([_doc("m1", .5, .8, .8)])[0] == "INCOMPLETE"
    assert v([_doc("m1", .5, .8, .8), _doc("m1", .9, 1, 1)])[0] == "INCOMPLETE"
    assert v([_doc("m1", .5, .8, .8), _doc("m3", .9, 1, 1)])[0] == "INCOMPLETE"
    assert v([_doc("m1", .5, .8, .8, seeds=(1,)), _doc("m2", .9, 1, 1)])[0] == "INCOMPLETE"
    capped = dict(_MANIFEST, seeds=1)
    assert v([_doc("m1", .5, .8, .8, seeds=(1,)), _doc("m2", .9, 1, 1, seeds=(1,))], capped)[0] == "COMPRESS"
    print("self-test ok")


if __name__ == "__main__":
    if sys.argv[1:] == ["--self-test"]:
        self_test()
    elif len(sys.argv) < 2:
        sys.exit(__doc__)
    else:
        main(sys.argv[1:])
