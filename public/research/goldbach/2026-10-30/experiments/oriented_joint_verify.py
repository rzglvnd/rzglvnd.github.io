"""Standalone exact verifier for an oriented joint-moment certificate.

Uses only the Python standard library. No imports from the LP discovery or
CRT moment implementations. A direct divisibility scan validates the CRT
inputs; observed states are never used to restrict the allowed state set.
"""

import argparse
from array import array
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
from math import comb, gcd, isqrt, prod
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def prime_flags(limit):
    flags = bytearray(b'\x01')*(limit+1)
    flags[0:2] = b'\x00\x00'
    for p in range(2, isqrt(limit)+1):
        if flags[p]:
            flags[p*p:limit+1:p] = b'\x00'*((limit-p*p)//p+1)
    return flags


def cube_root(n):
    lo, hi = 0, n+1
    while hi-lo > 1:
        mid = (lo+hi)//2
        if mid**3 <= n:
            lo = mid
        else:
            hi = mid
    return lo


def feature_basis():
    return [(None, a, k-a) for k in range(4) for a in range(k+1)] + [
        (side, a, k-a) for side in (0, 1) for k in range(3) for a in range(k+1)]


def feature_values(state, basis):
    jl, jr, dl, dr = state
    return [comb(jl, a)*comb(jr, b)*(1 if side is None else (dl, dr)[side])
            for side, a, b in basis]


def value(state, objective):
    jl, jr, dl, dr = state
    return 0 if jl+jr else (1-dl-dr if objective == 'signed' else int(dl+dr == 0))


def rebuild_support(n, y, z, tail, primes):
    small = [prod(tail[:j]) for j in range(len(tail)+1)]
    late = [p for p in primes if p > y][:4]
    assert len(late) == 4
    late_products = [prod(late[:d]) for d in range(5)]
    permitted = set()
    for jl, jr in product(range(len(tail)+1), repeat=2):
        if jl+jr > len(tail):
            continue
        for dl, dr in product(range(3), repeat=2):
            if (dl == 2 and jl == 0) or (dr == 2 and jr == 0):
                continue
            left_min = max(z+1, small[jl]*late_products[dl], late[dl-1]**2 if dl else 1)
            right_min = max(n//2, small[jr]*late_products[dr], late[dr-1]**2 if dr else 1)
            r_upper = min(n//2, n-right_min)
            if left_min > r_upper:
                continue
            if small[jl+jr]*late_products[dl+dr] > r_upper*(n-r_upper):
                continue
            permitted.add((jl, jr, dl, dr))
    return permitted


def verify(path):
    data_bytes = path.read_bytes()
    data = json.loads(data_bytes)
    n, w = data['target'], data['wheel_cutoff']
    y, z = cube_root(n), isqrt(n)
    assert n % 2 == 0 and 2 <= w <= y
    flags = prime_flags(n)
    primes = [p for p in range(2, n+1) if flags[p]]
    wheel = [p for p in primes if p <= w]
    remainder = n
    for p in wheel:
        while remainder % p == 0:
            remainder //= p
    assert remainder == 1, 'The no-shared-prime hypothesis must hold.'
    q = prod(wheel)
    tail = [p for p in primes if w < p <= y]
    assert tail == data['tail_primes']
    basis = feature_basis()
    assert [tuple(row) for row in data['feature_basis']] == basis
    support = rebuild_support(n, y, z, tail, primes)
    assert support == {tuple(state) for state in data['safe_states']}
    assert len(support) == len(data['safe_states'])

    # Independently mark divisibility; this does not use the discovery SPF scan.
    hits = array('B', [0])*(n+1)
    defects = array('B', [0])*(n+1)
    for p in tail:
        for m in range(p, n, p):
            hits[m] += 1
    for p in primes:
        if p > y and p*p < n:
            for m in range(p*p, n, p):
                defects[m] += 1
    histogram = Counter()
    for r in range(z+1, n//2+1):
        if gcd(r*(n-r), q) == 1:
            histogram[(hits[r], hits[n-r], defects[r], defects[n-r])] += 1
    assert set(histogram) <= support
    moments = [sum(mass*feature_values(state, basis)[i] for state, mass in histogram.items())
               for i in range(len(basis))]
    assert moments == data['moments']
    labeled_pairs = sum(flags[r] and flags[n-r] for r in range(z+1, n//2+1))
    signed = sum(mass*value(state, 'signed') for state, mass in histogram.items())
    pair_count = sum(mass*value(state, 'pairs') for state, mass in histogram.items())
    assert pair_count == labeled_pairs
    assert signed == data['independent_validation']['signed_margin']
    assert pair_count == data['independent_validation']['restricted_prime_pairs']

    certificates = []
    for certificate in data['certificates']:
        objective = certificate['objective']
        assert objective in ('signed', 'pairs')
        coefficients = [Fraction(v) for v in certificate['coefficients_exact']]
        assert len(coefficients) == len(basis)
        for state in support:
            score = sum(a*b for a, b in zip(coefficients, feature_values(state, basis)))
            assert score <= value(state, objective)
        dual = sum(a*b for a, b in zip(coefficients, moments))
        assert dual == Fraction(certificate['lower_bound_exact'])
        witness = [(tuple(row['state']), Fraction(row['mass_exact']))
                   for row in certificate['rational_witness']]
        assert all(state in support and mass >= 0 for state, mass in witness)
        assert len({state for state, _ in witness}) == len(witness)
        primal_moments = [sum(mass*feature_values(state, basis)[i] for state, mass in witness)
                          for i in range(len(basis))]
        assert primal_moments == moments
        primal = sum(mass*value(state, objective) for state, mass in witness)
        assert primal == Fraction(certificate['primal_objective_exact']) == dual
        assert certificate['exact_optimum_certified'] is True
        assert certificate['integer_lower_bound'] == -(-dual.numerator//dual.denominator)
        assert dual <= (signed if objective == 'signed' else pair_count)
        certificates.append({'objective': objective, 'exact_optimum': str(dual),
                             'all_state_inequalities_verified': True,
                             'all_primal_moments_verified': True,
                             'primal_dual_equality_verified': True})
    assert {record['objective'] for record in certificates} == {'signed', 'pairs'}
    result = {'status': 'Independent standard-library exact verification; no uniform Goldbach theorem.',
              'source_file': path.name, 'source_sha256': sha256(data_bytes).hexdigest(),
              'target': n, 'wheel_cutoff': w, 'safe_states_reconstructed': len(support),
              'observed_states_checked': len(histogram), 'moments_checked': len(moments),
              'independently_scanned_moments': moments,
              'restricted_prime_pairs': pair_count, 'signed_margin': signed,
              'certificates': certificates}
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=Path,
                        default=ROOT/'research'/'oriented-joint-1000000-w7.json')
    args = parser.parse_args()
    result = verify(args.input)
    destination = ROOT/'research'/'oriented-joint-verification.json'
    destination.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
