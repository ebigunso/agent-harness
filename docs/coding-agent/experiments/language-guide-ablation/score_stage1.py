"""Score Stage 1 ablation results and apply the pre-registered decision rule.

Usage: python score_stage1.py stage1/results.yaml
"""

import sys
import collections

import yaml

DELTA_OBSOLETE = 0.10   # B - A below this -> obsolete
DELTA_C_EQUIV = 0.05    # C within this of B -> salience-only
FP_REGRESSION = 0.10    # arm FP rate above A's by more than this -> regression flag
MIN_SEEDS = 3


def is_clean(fixture):
    return "-c" in fixture


def main(path):
    doc = yaml.safe_load(open(path, encoding="utf-8"))
    records = doc.get("records") or []
    if not records:
        sys.exit("no records in " + path)

    det = collections.defaultdict(list)    # (lang, arm) -> planted scores
    fps = collections.defaultdict(list)    # (lang, arm) -> fp counts per clean review
    toks = collections.defaultdict(list)
    seeds = collections.defaultdict(set)   # (lang, arm, fixture) -> seeds seen

    for r in records:
        key = (r["language"], r["arm"])
        seeds[(r["language"], r["arm"], r["fixture"])].add(r.get("seed"))
        toks[key].append(r.get("output_tokens") or 0)
        if is_clean(r["fixture"]):
            fps[key].append(r.get("false_positives") or 0)
        else:
            det[key].append(float(r.get("score") or 0))

    langs = sorted({lang for lang, _ in det})
    print("model: " + (doc.get("model") or "(unset)") + "\n")
    header = f"{'language':<24} {'arm':>3} {'detect':>7} {'fp/rev':>7} {'tokens':>7}"
    print(header)

    summary = {}
    for lang in langs:
        for arm in "ABC":
            d = det.get((lang, arm), [])
            f = fps.get((lang, arm), [])
            t = toks.get((lang, arm), [])
            if not d:
                continue
            detect = sum(d) / len(d)
            fprate = (sum(f) / len(f)) if f else 0.0
            summary[(lang, arm)] = (detect, fprate)
            print(f"{lang:<24} {arm:>3} {detect:>6.0%} {fprate:>7.2f} {sum(t)/len(t):>7.0f}")
        print()

    print("verdicts (pre-registered rule):")
    for lang in langs:
        a = summary.get((lang, "A"))
        b = summary.get((lang, "B"))
        c = summary.get((lang, "C"))
        if not (a and b):
            print(f"  {lang}: incomplete (need arms A and B)")
            continue
        delta = b[0] - a[0]
        if delta < DELTA_OBSOLETE:
            verdict = f"OBSOLETE (B-A = {delta:+.0%}) -> delete language ref"
        elif c and c[0] >= b[0] - DELTA_C_EQUIV:
            verdict = f"SALIENCE-ONLY (B-A = {delta:+.0%}, C ~= B) -> compress"
        elif c:
            verdict = f"LOAD-BEARING (B-A = {delta:+.0%}, C < B) -> keep full ref"
        else:
            verdict = f"NEEDS ARM C (B-A = {delta:+.0%})"
        flags = []
        for arm in "BC":
            s = summary.get((lang, arm))
            if s and s[1] > a[1] + FP_REGRESSION:
                flags.append(f"arm {arm} FP regression ({s[1]:.2f} vs A {a[1]:.2f})")
        low_seeds = any(len(v) < MIN_SEEDS for k, v in seeds.items() if k[0] == lang)
        if low_seeds:
            flags.append(f"<{MIN_SEEDS} seeds on some cells — variance untrustworthy")
        print(f"  {lang}: {verdict}" + (("  [" + "; ".join(flags) + "]") if flags else ""))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "stage1/results.yaml")
