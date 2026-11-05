"""Independent standard-library verification of the 25-moment certificate.

No LP solver or CRT discovery code is imported. Counts are obtained by
marking divisibility, and every primal/dual identity uses exact fractions.
The support is reconstructed from proved factor-size restrictions, never
from an observed histogram.
"""

from array import array
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
from math import comb, gcd, isqrt, prod
from pathlib import Path

from oriented_joint_verify import (prime_flags, cube_root, feature_basis,
                                   feature_values, rebuild_support, value)


ROOT = Path(__file__).resolve().parents[1]
ADDITIONAL = ['D_L*D_R', 'D_L*D_R*J_L', 'D_L*D_R*J_R']


def extended_features(state, basis):
    jl, jr, dl, dr = state
    return feature_values(state, basis)+[dl*dr, dl*dr*jl, dl*dr*jr]


def run():
    source = ROOT/'research'/'joint-cross-search-results.json'
    source_bytes = source.read_bytes()
    data = json.loads(source_bytes)
    cross = json.loads((ROOT/'research'/'cross-defect-moments.json').read_text())
    n, w = data['target'], data['wheel_cutoff']
    assert (n, w) == (cross['target'], cross['wheel_cutoff'])
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
    wheel_modulus = prod(wheel)
    tail = [p for p in primes if w < p <= y]
    basis = feature_basis()
    assert [tuple(row) for row in data['base_feature_basis']] == basis
    assert data['additional_features'] == cross['features'] == ADDITIONAL
    support = rebuild_support(n, y, z, tail, primes)
    assert support == {tuple(state) for state in data['safe_states']}
    assert len(support) == len(data['safe_states'])

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
        if gcd(r*(n-r), wheel_modulus) == 1:
            histogram[(hits[r], hits[n-r], defects[r], defects[n-r])] += 1
    assert set(histogram) <= support
    moments = [sum(mass*extended_features(state, basis)[i] for state, mass in histogram.items())
               for i in range(25)]
    assert moments == data['moments']
    assert moments[-3:] == cross['moments']
    # Truth labels are consulted only after reconstructing all certificate inputs.
    pairs = sum(mass*value(state, 'pairs') for state, mass in histogram.items())
    signed = sum(mass*value(state, 'signed') for state, mass in histogram.items())
    labeled_pairs = sum(flags[r] and flags[n-r] for r in range(z+1, n//2+1))
    assert pairs == labeled_pairs

    checked = []
    for certificate in data['certificates']:
        kind = certificate['objective']
        assert kind in ('signed', 'pairs')
        coefficients = [Fraction(v) for v in certificate['coefficients_exact']]
        assert len(coefficients) == 25
        for state in support:
            polynomial = sum(a*b for a, b in zip(coefficients, extended_features(state, basis)))
            assert polynomial <= value(state, kind)
        lower = sum(a*b for a, b in zip(coefficients, moments))
        assert lower == Fraction(certificate['lower_bound_exact'])
        witness = [(tuple(row['state']), Fraction(row['mass_exact']))
                   for row in certificate['rational_witness']]
        assert all(state in support and mass >= 0 for state, mass in witness)
        assert len({state for state, _ in witness}) == len(witness)
        for i in range(25):
            assert sum(mass*extended_features(state, basis)[i] for state, mass in witness) == moments[i]
        primal = sum(mass*value(state, kind) for state, mass in witness)
        assert primal == Fraction(certificate['primal_objective_exact']) == lower
        assert certificate['exact_optimum_certified'] is True
        integer_lower = -(-lower.numerator//lower.denominator)
        assert integer_lower == certificate['integer_lower_bound']
        assert integer_lower <= (signed if kind == 'signed' else pairs)
        checked.append({'objective': kind, 'exact_relaxed_optimum': str(lower),
                        'integer_lower_bound': integer_lower,
                        'all_99_state_inequalities_verified': len(support) == 99,
                        'all_25_primal_moments_verified': True,
                        'nonnegative_primal_witness_verified': True,
                        'exact_primal_dual_equality_verified': True})
    assert {record['objective'] for record in checked} == {'signed', 'pairs'}
    # Check the concise algebraic proof independently of the 99-state support.
    pair_certificate = next(row for row in data['certificates'] if row['objective'] == 'pairs')
    pair_coefficients = [Fraction(v) for v in pair_certificate['coefficients_exact']]
    expected_coefficients = [Fraction(v) for v in [
        '1', '-1', '-1', '1/2', '1', '1/2', '0', '-1/2', '-1/2', '0',
        '-1', '1', '1/2', '-1/2', '-1/2', '0',
        '-1', '1/2', '1', '0', '-1/2', '-1/2', '1', '-1/2', '-1/2']]
    assert pair_coefficients == expected_coefficients
    side_states = [(0, 0), (0, 1), (1, 0), (1, 1), (1, 2),
                   (2, 0), (2, 1), (3, 0), (3, 1), (4, 0)]
    late = [p for p in primes if p > y]
    assert prod(tail[:5]) > n
    assert prod(tail[:4])*late[0] > n
    assert prod(tail[:2])*prod(late[:2]) > n
    for j, d in side_states:
        if j+d:
            a, h = j+d-1, comb(j, 2)+j*d
            assert 0 <= a <= h <= 2*a
    for (jl, dl), (jr, dr) in product(side_states, repeat=2):
        state = (jl, jr, dl, dr)
        fl, fr = 1-jl-dl, 1-jr-dr
        hl, hr = comb(jl, 2)+jl*dl, comb(jr, 2)+jr*dr
        factored = fl*fr+Fraction(hl*fr+hr*fl, 2)
        expanded = sum(a*b for a, b in zip(pair_coefficients, extended_features(state, basis)))
        assert factored == expanded <= value(state, 'pairs')
    result = {'status': 'Independent exact finite certificate verification; no uniform Goldbach theorem.',
              'source_file': source.name, 'source_sha256': sha256(source_bytes).hexdigest(),
              'target': n, 'wheel_cutoff': w, 'wheel_modulus': wheel_modulus,
              'safe_states_reconstructed': len(support),
              'observed_states_checked': len(histogram), 'moments_checked': 25,
              'independently_scanned_moments': moments,
              'factored_pair_minorant': {'saved_coefficients_match_expansion': True,
                                        'ten_side_states_certified_by_factor_sizes': True,
                                        'side_A_H_inequalities_checked': True,
                                        'all_100_side_combinations_checked': True},
              'independent_truth_check_only': {'restricted_prime_pairs': pairs, 'signed_margin': signed},
              'certificates': checked}
    path = ROOT/'research'/'joint-cross-verification.json'
    path.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    run()
