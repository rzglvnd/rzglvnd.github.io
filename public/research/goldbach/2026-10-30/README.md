# Goldbach research snapshot — through 30 October 2026

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
