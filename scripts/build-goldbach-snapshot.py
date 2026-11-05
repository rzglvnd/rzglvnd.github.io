"""Prepare a dated, curated public research snapshot; never export chat logs."""
import argparse
import ast
import hashlib
import json
import shutil
import zipfile
from pathlib import Path

NOTES = [
    "joint-operator-growth.md", "joint-operator-average.md",
    "joint-positive-proportion.md", "joint-reflection-correlation.md",
    "joint-average-constant-audit.md",
    "compact-residue-normalization.md", "local-residue-reflection-proof.md",
    "frozen-threshold-transfer.md", "almost-all-circle-method.md",
    "almost-all-transfer-audit.md", "cross-defect-moments.md",
    "oriented-state-constraints.md",
]
SCRIPTS = [
    "joint_cross_verify.py", "oriented_joint_verify.py", "local_singular_factor.py",
    "joint_average_bands.py", "joint_operator_scaling.py", "sieve_corrections.py",
    "frozen_threshold_transfer.py", "avgconstant_joint_operator.py",
    "joint_average_upper_certificate.py",
]
DATA = [
    "joint-cross-search-results.json", "cross-defect-moments.json",
    "joint-cross-verification.json", "local-singular-factor.json",
    "joint-average-bands.json", "joint-operator-stress.json",
    "frozen-threshold-transfer.json", "joint-operator-average-constants.json",
    "joint-average-upper-certificate.json",
]

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    args = parser.parse_args()
    source = args.source.resolve()
    destination = Path(__file__).resolve().parents[1] / "public/research/goldbach/2026-10-30"
    destination.mkdir(parents=True, exist_ok=True)
    files = [*(f"research/{n}" for n in NOTES + DATA), *(f"experiments/{n}" for n in SCRIPTS)]
    manifest = []
    for name in files:
        data = (source / name).read_bytes()
        # Fail if a selected source accidentally contains a private local path or chat link.
        content = data.decode("utf-8")
        assert "C:/Users/" not in content and "C:\\Users\\" not in content and "codex://" not in content
        if name.endswith(".py"):
            ast.parse(content, filename=name)
        if name.endswith(".json"):
            json.loads(content)
        manifest.append({"path": name, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()})
        # Serve compact notes and certificates individually; large population files stay in the ZIP.
        if name.endswith(".md") or len(data) < 100_000:
            path = destination / name
            path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source / name, path)

    bands = json.loads((source / "research/joint-average-bands.json").read_text())
    profiles = bands["profiles"]
    assert [p["target"] for p in profiles] == list(range(6, 250001, 2))
    assert len(profiles) == bands["total_targets"] == bands["positive_targets"] == 124998
    assert all(p["doubled_operator_sum"] > 0 for p in profiles)
    assert not bands["zero_targets"] and not bands["negative_targets"]
    certificate = json.loads((source / "research/joint-cross-verification.json").read_text())
    pair_certificate = next(c for c in certificate["certificates"] if c["objective"] == "pairs")
    assert pair_certificate["exact_relaxed_optimum"] == "1705/2"
    assert pair_certificate["integer_lower_bound"] == 853
    assert pair_certificate["exact_primal_dual_equality_verified"]
    summary = {
        "researchThrough": "2026-10-30", "published": "2026-11-05",
        "finite": {"first": 6, "last": 250000, "targets": len(profiles),
                   "positive": bands["positive_targets"], "zero": 0, "negative": 0,
                   "sourceSha256": next(f["sha256"] for f in manifest if f["path"] == "research/joint-average-bands.json"),
                   "bands": [{"X": b["X"], "targets": b["target_count"],
                              "scoreSum": b["operator_sum_exact"], "pairSum": b["prime_pairs_sum"],
                              "ratioExact": b["ratio_of_sums_exact"], "ratio": b["ratio_of_sums_decimal"]}
                             for b in bands["bands"]]},
        "certificate": {"target": certificate["target"], "wheel": certificate["wheel_cutoff"],
                        "exactBound": pair_certificate["exact_relaxed_optimum"], "integerBound": 853,
                        "observedPairs": certificate["independent_truth_check_only"]["restricted_prime_pairs"],
                        "moments": certificate["moments_checked"]},
        "scope": "Finite results and project derivations; the October 30 Fourier comparison is a draft under review. No all-target Goldbach theorem or novelty is claimed.",
    }
    (destination / "summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    (destination / "manifest.json").write_text(json.dumps({"snapshot": "2026-10-30", "files": manifest}, indent=2) + "\n", encoding="utf-8")
    readme = """# Goldbach research snapshot — through 30 October 2026

Published 5 November 2026 by Reza Ghalavand, from research developed with ChatGPT Codex.
This is a curated mathematical working snapshot, not a conversation export or a peer-reviewed publication.
The circle-method comparison is a draft under review. The last research session had no final completion report.
The moving-threshold reduction and earlier project derivations have their own stated scope.
No all-target Goldbach proof, novelty, or numerical onset for asymptotic results is claimed.

## Reproduce exact checks

Extract the ZIP and run from its root with Python 3 (standard library only):

    python experiments/joint_cross_verify.py
    python experiments/local_singular_factor.py
    python experiments/joint_average_upper_certificate.py
    python experiments/joint_average_bands.py
    python experiments/frozen_threshold_transfer.py

The first verifies the 853-pair benchmark from saved moment inputs by an independent divisibility scan.
The second checks local residue identities and rational product-tail certificates.
The upper-certificate script checks the strict 3/10 upper bound by exact rational arithmetic.
The last two recompute the full finite range and the five moving/frozen comparison bands; allow time and memory.
Scripts write their results inside the extracted snapshot. Timings are machine dependent.
The optional standalone oriented_joint_verify.py entry point requires an older input not included here;
its helper functions are included as dependencies of joint_cross_verify.py.

The ZIP includes full population data. summary.json retains the finite counts and band totals for the website.
manifest.json records original source hashes and sizes. The archive is a selection; links in working notes
to earlier notes outside the selection may be unavailable. Analytic proofs require mathematical review;
passing a finite check does not prove an asymptotic estimate.
"""
    (destination / "README.md").write_text(readme, encoding="utf-8")
    with zipfile.ZipFile(destination / "research-snapshot.zip", "w", zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name in files:
            info = zipfile.ZipInfo(name, (2026, 10, 30, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, (source / name).read_bytes())
        for name in ["README.md", "manifest.json", "summary.json"]:
            info = zipfile.ZipInfo(name, (2026, 10, 30, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, (destination / name).read_bytes())
    print(json.dumps({"destination": str(destination), "source_files": len(files),
                      "targets_validated": len(profiles), "zip_bytes": (destination / "research-snapshot.zip").stat().st_size}))

if __name__ == "__main__":
    main()
