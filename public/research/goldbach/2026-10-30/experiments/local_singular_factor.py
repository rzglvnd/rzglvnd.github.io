"""Exact finite certificates for the local Goldbach normalization.

All identities and bounds use integers/Fractions. Decimal displays are descriptive.
This script tests local residue geometry, not a prime-pair asymptotic.
"""

from fractions import Fraction as F
from math import gcd, prod
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]


def primes_up_to(limit):
    flags = bytearray(b"\1") * (limit + 1)
    flags[:2] = b"\0\0"
    for p in range(2, int(limit**0.5) + 1):
        if flags[p]:
            flags[p*p:limit+1:p] = b"\0" * ((limit-p*p)//p+1)
    return [p for p in range(2, limit+1) if flags[p]]


def local_factor(p, n):
    return F(p, p-1) if n % p == 0 else F(p*(p-2), (p-1)**2)


def ramanujan_squarefree(ps, n):
    return prod(p-1 if n % p == 0 else -1 for p in ps)


def factor_certificate(ps):
    modulus = prod(ps)
    phi = prod(p-1 for p in ps)
    units = [a for a in range(modulus) if gcd(a, modulus) == 1]
    counts = [0] * modulus
    for a in units:
        for b in units:
            counts[(a+b) % modulus] += 1
    factors = []
    for n in range(modulus):
        value = F(modulus*counts[n], phi*phi)
        assert value == prod((local_factor(p, n) for p in ps), start=F(1))
        fourier = F(0)
        for mask in range(1 << len(ps)):
            selected = [p for j, p in enumerate(ps) if mask & (1 << j)]
            fourier += F(ramanujan_squarefree(selected, n),
                         prod(p-1 for p in selected)**2)
        assert value == fourier
        factors.append(value)
    mean = sum(factors, F(0))/modulus
    second = sum((v*v for v in factors), F(0))/modulus
    expected_second = prod((1 + F(1, (p-1)**3) for p in ps), start=F(1))
    assert mean == 1 and second == expected_second
    return {
        "modulus": modulus, "primes": ps, "phi": phi,
        "residue_factors_exact": [str(v) for v in factors],
        "mean_exact": str(mean), "second_moment_exact": str(second),
        "all_pair_counts_and_Ramanujan_expansions_match": True,
    }


def refinement_certificate(ps, ell):
    modulus = prod(ps)
    assert ell not in ps
    squared_difference = F(0)
    bias_divisible = F(0)
    bias_not_divisible = F(0)
    for n in range(modulus*ell):
        base = prod((local_factor(p, n) for p in ps), start=F(1))
        refined = base*local_factor(ell, n)
        change = refined-base
        squared_difference += change*change
        if n % ell == 0:
            bias_divisible += change
        else:
            bias_not_divisible += change
    denominator = modulus*ell
    squared_difference /= denominator
    bias_divisible /= denominator
    bias_not_divisible /= denominator
    d_m = prod((1 + F(1, (p-1)**3) for p in ps), start=F(1))
    assert squared_difference == d_m/F((ell-1)**3)
    assert bias_divisible == F(1, ell*(ell-1))
    assert bias_not_divisible == -bias_divisible
    return {
        "old_modulus": modulus, "new_prime": ell,
        "mean_squared_increment_exact": str(squared_difference),
        "mean_increment_on_divisible_targets_exact": str(bias_divisible),
        "mean_increment_on_other_targets_exact": str(bias_not_divisible),
        "absolute_mean_increment_exact": str(2*bias_divisible),
    }


def product_tail_certificate(y, primes):
    ps = [p for p in primes if 2 < p <= y]
    c_y = prod((1-F(1, (p-1)**2) for p in ps), start=F(1))
    d_y = prod((1+F(1, (p-1)**3) for p in ps), start=F(1))
    # Product of the omitted prime factors is >= product of ALL m>=y.
    # The latter telescopes to (y-1)/y, so this encloses the infinite C_2.
    c_lower = c_y * F(y-1, y)
    c_upper = c_y
    # Sum_{p>y}1/(p-1)^3 <= 1/y^3+1/(2y^2)=:t<1.
    # prod(1+a_p)<=exp(sum a_p)<=1/(1-t).
    t = F(1, y**3) + F(1, 2*y*y)
    d_tail_upper = d_y*t/(1-t)
    coarse_tail = F(3, 2*y*y)
    assert c_lower >= F(1, 2)
    assert d_y < F(4, 3)
    assert d_tail_upper < coarse_tail
    return {
        "prime_cutoff": y,
        "C2_lower_exact": str(c_lower), "C2_upper_exact": str(c_upper),
        "D_y_exact": str(d_y),
        "D_infinity_minus_D_y_upper_exact": str(d_tail_upper),
        "coarse_upper_exact": str(coarse_tail),
        "descriptive_decimals": {
            "C2_lower": float(c_lower), "C2_upper": float(c_upper),
            "D_y": float(d_y), "mean_square_tail_upper": float(d_tail_upper),
        },
    }


def run():
    rows = [factor_certificate(ps) for ps in [[], [3], [3, 5], [3, 5, 7]]]
    refinements = [refinement_certificate(ps, ell) for ps, ell in
                   [([], 3), ([3], 5), ([3, 5], 7), ([3, 5, 7], 11)]]
    primes = primes_up_to(101)
    tails = [product_tail_certificate(y, primes) for y in [3, 5, 7, 11, 31, 101]]
    result = {
        "date": "2026-10-29", "arithmetic": "exact integers and rational numbers",
        "scope": "Finite residue identities and infinite-product tail certificates; no prime-pair error bound.",
        "finite_moduli": rows, "refinements": refinements, "tail_certificates": tails,
    }
    output = ROOT/"research"/"local-singular-factor.json"
    output.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"moduli_checked": [r["modulus"] for r in rows],
                      "refinements_checked": len(refinements),
                      "tail_certificates": len(tails),
                      "output": str(output)}, indent=2))


if __name__ == "__main__":
    run()
