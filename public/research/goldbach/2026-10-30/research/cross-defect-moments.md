# Exact cross-side late-defect moments

Date: 2026-10-26, Asia/Tehran. Status: three exact finite CRT counts, independently checked by a divisibility scan. These counts provide additional inputs for a joint minorant; they do not themselves assert a positive Goldbach bound.

Use the oriented notation in `oriented-state-constraints.md`. For each ordered pair of late primes (p,q), let p be a counted divisor of r and q a counted divisor of N-r. Under the wheel hypothesis gcd(r,N-r)=1, p and q must be different. The canonical-divisor conditions and the original interval are exactly

    max(z+1,p^2) <= r <= min(N/2,N-q^2),
    r = 0 (mod p),    r = N (mod q).

Combine these congruences with each allowed wheel residue. A residue a modulo M contributes exactly

    floor((hi-a)/M) - floor((lo-1-a)/M)

members of the channel interval. Summing over (p,q) gives sum D_L*D_R because a candidate with counts (D_L,D_R) occurs in exactly D_L*D_R ordered channels.

For every omitted prime ell, adding the CRT root r=0 (mod ell) counts an additional left hit; adding r=N (mod ell) counts a right hit. Summing these intersections over ell and all late-prime channels therefore gives sum D_L*D_R*J_L and sum D_L*D_R*J_R. All moduli being merged are coprime. Empty wheel classes can be skipped before constructing the further intersections.

For N=1,000,000 and w=7, this produces:

| Moment | Exact value |
|---|---:|
| sum D_L*D_R | 4,636 |
| sum D_L*D_R*J_L | 2,977 |
| sum D_L*D_R*J_R | 2,857 |

The construction visits 12,905 ordered late-prime channels and 258,100 wheel classes. A separate smallest-prime-factor scan of all 47,524 wheel candidates gives the same three integers. The construction and validation do not use prime-pair indicators.

These are new correlations relative to the previous 22-feature basis: that basis is affine in the two defect counts, while the new features retain their cross product. Reflection exchanges the last two moments, but does not force them to be equal on the chosen half interval.

Reproduce with `python experiments/cross_defect_moments.py`. The script writes `research/cross-defect-moments.json` after all three exact validation assertions pass.
