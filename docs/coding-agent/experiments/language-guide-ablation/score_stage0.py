"""Score Stage 0 regeneration probes. Usage: python score_stage0.py stage0/results.yaml"""
import sys
import collections
import yaml

WEIGHT = {"hit": 1.0, "partial": 0.5, "miss": 0.0}
THRESHOLD_OBSOLETE = 0.80
THRESHOLD_SIGNAL = 0.60


def main(path):
    doc = yaml.safe_load(open(path, encoding="utf-8"))
    by_lang = collections.defaultdict(list)
    for s in doc.get("samples") or []:
        marks = s.get("marks") or {}
        if not marks:
            continue
        by_lang[s["language"]].append(sum(WEIGHT[v] for v in marks.values()) / len(marks))

    if not by_lang:
        sys.exit("no scored samples in " + path)

    print("model: " + (doc.get("model") or "(unset)") + "\n")
    print(f"{'language':<24} {'n':>3} {'coverage':>9}  verdict")
    for lang, scores in sorted(by_lang.items()):
        cov = sum(scores) / len(scores)
        if cov >= THRESHOLD_OBSOLETE:
            verdict = "prima facie obsolete -> run Stage 1"
        elif cov >= THRESHOLD_SIGNAL:
            verdict = "inconclusive -> run Stage 1"
        else:
            verdict = "doc carries signal -> stop"
        print(f"{lang:<24} {len(scores):>3} {cov:>8.0%}  {verdict}")
        if len(scores) < 3:
            print(f"{'':<24} {'':>3} {'':>9}  (warn: <3 samples, variance untrustworthy)")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "stage0/results.yaml")
