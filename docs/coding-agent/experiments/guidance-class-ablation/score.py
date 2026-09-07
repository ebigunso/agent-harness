"""Score the guidance-class ablation and apply the pre-registered rule in protocol.md.

Usage: python score.py results-fable.yaml results-astra.yaml [...]

One results file per model. Verdicts are per measured section on the worst model,
where the worst model is the one with the lowest arm-A detection on that section.
Adapted from 47c409c:docs/coding-agent/experiments/language-guide-ablation/score_stage1.py.
"""

import collections
import sys

import yaml

DELTA_LIFT = 0.10      # dB below this -> DELETE
DELTA_C_EQUIV = 0.05   # dC within this of dB -> COMPRESS
FP_REGRESSION = 0.10   # arm FP rate above A's by more than this -> cannot adopt
SEEDS = 2


def is_clean(fixture):
    return fixture.rsplit("-", 1)[-1].startswith("c")


def load(path):
    doc = yaml.safe_load(open(path, encoding="utf-8"))
    model = doc.get("model") or path
    det = collections.defaultdict(list)   # (section, arm) -> planted scores
    fps = collections.defaultdict(list)   # (section, arm) -> fp counts per decoy review
    seeds = collections.defaultdict(set)  # (section, arm, fixture) -> seeds
    for r in doc.get("records") or []:
        key = (r["section"], r["arm"])
        seeds[(r["section"], r["arm"], r["fixture"])].add(r.get("seed"))
        if is_clean(r["fixture"]):
            fps[key].append(r.get("false_positives") or 0)
        else:
            det[key].append(float(r.get("score") or 0))
    summary = {}
    for key, scores in det.items():
        f = fps.get(key, [])
        summary[key] = (sum(scores) / len(scores), (sum(f) / len(f)) if f else 0.0)
    low = {k[0] for k, v in seeds.items() if len(v) < SEEDS}
    return model, summary, low


def main(paths):
    models = [load(p) for p in paths]
    sections = sorted({s for _, summary, _ in models for s, _ in summary})
    print(f"{'section':<28} {'model':<18} {'A':>5} {'B':>5} {'C':>5} {'fpA':>5} {'fpB':>5} {'fpC':>5}")
    for s in sections:
        for model, summary, _ in models:
            row = [summary.get((s, arm)) for arm in "ABC"]
            det = " ".join(f"{r[0]:>5.0%}" if r else "    -" for r in row)
            fp = " ".join(f"{r[1]:>5.2f}" if r else "    -" for r in row)
            print(f"{s:<28} {model:<18} {det} {fp}")
    print("\nverdicts (pre-registered rule, worst model = lowest arm-A detection):")
    for s in sections:
        candidates = [(summary[(s, "A")][0], model, summary) for model, summary, _ in models if (s, "A") in summary]
        if not candidates:
            print(f"  {s}: incomplete (no arm A)")
            continue
        _, worst, summary = min(candidates, key=lambda c: c[0])
        a, b, c = (summary.get((s, arm)) for arm in "ABC")
        if not b:
            print(f"  {s}: incomplete (need arm B on {worst})")
            continue
        d_b = b[0] - a[0]
        if d_b < DELTA_LIFT:
            verdict = f"DELETE (dB = {d_b:+.0%})"
        elif not c:
            verdict = f"NEEDS ARM C (dB = {d_b:+.0%})"
        elif (c[0] - a[0]) >= d_b - DELTA_C_EQUIV:
            verdict = f"COMPRESS (dB = {d_b:+.0%}, dC = {c[0] - a[0]:+.0%})"
        else:
            verdict = f"KEEP (dB = {d_b:+.0%}, dC = {c[0] - a[0]:+.0%})"
        flags = []
        for arm, r in (("B", b), ("C", c)):
            if r and r[1] > a[1] + FP_REGRESSION:
                flags.append(f"arm {arm} FP regression ({r[1]:.2f} vs A {a[1]:.2f}): cannot adopt")
        if any(s in low for _, _, low in models):
            flags.append(f"<{SEEDS} seeds on some cells")
        print(f"  {s} [{worst}]: {verdict}" + (("  [" + "; ".join(flags) + "]") if flags else ""))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1:])
