"""Score the guidance-class ablation and apply the pre-registered rule in protocol.md.

Usage: python score.py [--seeds N] results-fable.yaml results-astra.yaml [...]
       python score.py --self-test

One results file per model; every registered model must be present. Verdicts are per
measured section on the worst model (lowest arm-A detection); ties are evaluated on every
tied model and the most protective outcome stands. The FP guard is checked on every model.
A section missing any arm, fixture, seed, or decoy on any model is INCOMPLETE, never scored.
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


def summarize(doc, seeds_required):
    """(section, arm) -> (detection, fp_rate) plus per-section incompleteness reasons."""
    scores = collections.defaultdict(list)      # (section, arm) -> planted scores
    fps = collections.defaultdict(list)         # (section, arm) -> fp counts on decoys
    seen = collections.defaultdict(set)         # (section, arm, fixture) -> seeds
    fixtures = collections.defaultdict(set)     # section -> fixture ids
    for r in doc.get("records") or []:
        key = (r["section"], r["arm"])
        seen[(r["section"], r["arm"], r["fixture"])].add(r.get("seed"))
        fixtures[r["section"]].add(r["fixture"])
        if is_clean(r["fixture"]):
            fps[key].append(float(r.get("false_positives") or 0))
        else:
            scores[key].append(float(r.get("score") or 0))
    summary, problems = {}, collections.defaultdict(list)
    for section, ids in fixtures.items():
        for arm in ARMS:
            key = (section, arm)
            if key not in scores:
                problems[section].append(f"arm {arm} has no planted records")
                continue
            if key not in fps:
                problems[section].append(f"arm {arm} has no decoy records")
            short = [f for f in ids if len(seen.get((section, arm, f), ())) < seeds_required]
            if short:
                problems[section].append(f"arm {arm}: {len(short)} fixture(s) below {seeds_required} seeds")
            f = fps.get(key, [])
            summary[key] = (sum(scores[key]) / len(scores[key]), (sum(f) / len(f)) if f else None)
    return summary, problems


def verdict_on(summary, section):
    a, b, c = (summary[(section, arm)] for arm in ARMS)
    d_b, d_c = b[0] - a[0], c[0] - a[0]
    if d_b < DELTA_LIFT:
        return "DELETE", d_b, d_c
    if d_c >= d_b - DELTA_C_EQUIV:
        return "COMPRESS", d_b, d_c
    return "KEEP", d_b, d_c


def decide(models, seeds_required):
    """models: list of (name, doc). Returns {section: (verdict, worst_models, flags)}."""
    per_model = {name: summarize(doc, seeds_required) for name, doc in models}
    sections = sorted({s for _, (summary, _) in per_model.items() for s, _ in summary}
                      | {s for _, (_, problems) in per_model.items() for s in problems})
    out = {}
    for s in sections:
        problems = []
        for name, (summary, probs) in per_model.items():
            problems += [f"{name}: {p}" for p in probs.get(s, [])]
            if any((s, arm) not in summary for arm in ARMS):
                problems.append(f"{name}: section absent or missing an arm")
        if problems:
            out[s] = ("INCOMPLETE", [], sorted(set(problems)))
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
    seeds_required = 2
    if "--seeds" in argv:
        i = argv.index("--seeds")
        seeds_required = int(argv[i + 1])
        del argv[i:i + 2]
    models = []
    for path in argv:
        doc = yaml.safe_load(open(path, encoding="utf-8"))
        models.append((doc.get("model") or path, doc))
    if len(models) < 2:
        sys.exit("need one results file per fleet model (at least two)")
    for s, (verdict, worst, flags) in decide(models, seeds_required).items():
        print(f"{s}: {verdict}" + (f" [worst: {', '.join(worst)}]" if worst else ""))
        for f in flags:
            print(f"    {f}")


def _doc(model, section, a, b, c, fp=(0, 0, 0), seeds=(1, 2), decoys=True):
    recs = []
    for arm, det, f in zip(ARMS, (a, b, c), fp):
        for seed in seeds:
            recs.append({"arm": arm, "section": section, "fixture": f"{section}-01", "seed": seed, "score": det})
            if decoys:
                recs.append({"arm": arm, "section": section, "fixture": f"{section}-c1", "seed": seed, "false_positives": f})
    return model, {"model": model, "records": recs}


def self_test():
    v = lambda ms, **kw: decide(ms, kw.get("seeds", 2))["x"]
    assert v([_doc("m1", "x", .5, .55, .5), _doc("m2", "x", .9, 1, 1)])[0] == "DELETE"
    assert v([_doc("m1", "x", .5, .8, .8), _doc("m2", "x", .9, 1, 1)])[0] == "COMPRESS"
    assert v([_doc("m1", "x", .5, .8, .5), _doc("m2", "x", .9, 1, 1)])[0] == "KEEP"
    # tie on A: most protective outcome stands regardless of argument order
    tie = [_doc("m1", "x", .5, .5, .5), _doc("m2", "x", .5, 1, .5)]
    assert v(tie)[0] == "KEEP" and v(tie[::-1])[0] == "KEEP" and v(tie)[1] == ["m1", "m2"]
    # FP guard fires on a model that is not the worst one
    r = v([_doc("m1", "x", .25, .75, .75), _doc("m2", "x", .5, 1, 1, fp=(0, 0, .25))])
    assert r[0] == "COMPRESS" and any("m2: arm C FP regression" in f for f in r[2])
    # incompleteness: missing decoys, missing model records, short seeds
    assert v([_doc("m1", "x", .5, .8, .8, decoys=False), _doc("m2", "x", .9, 1, 1)])[0] == "INCOMPLETE"
    assert v([_doc("m1", "x", .5, .8, .8), ("m2", {"model": "m2", "records": []})])[0] == "INCOMPLETE"
    assert v([_doc("m1", "x", .5, .8, .8, seeds=(1,)), _doc("m2", "x", .9, 1, 1)])[0] == "INCOMPLETE"
    assert v([_doc("m1", "x", .5, .8, .8, seeds=(1,)), _doc("m2", "x", .9, 1, 1, seeds=(1,))], seeds=1)[0] == "COMPRESS"
    print("self-test ok")


if __name__ == "__main__":
    if sys.argv[1:] == ["--self-test"]:
        self_test()
    elif len(sys.argv) < 2:
        sys.exit(__doc__)
    else:
        main(sys.argv[1:])
