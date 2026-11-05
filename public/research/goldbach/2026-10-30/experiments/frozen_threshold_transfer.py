"""Exact finite audit of the moving-to-frozen convolution transfer.

Checks finite support domination and the discrete Young inequality with integers.
The asymptotic support estimates have a separate written proof.
"""

from fractions import Fraction
from math import comb, isqrt, log
from pathlib import Path
import hashlib
import json

from joint_average_bands import exact_convolution
from joint_operator_scaling import floor_root
from sieve_corrections import sieve, distinct_factors

ROOT = Path(__file__).resolve().parents[1]
XS = [1000, 10000, 50000, 100000, 125000]


def weights(n, w, y, spf, factors):
    if n < 2 or spf[n] <= w:
        return 0, 0
    j = sum(w < p <= y for p in factors[n])
    d = sum(p > y and p*p <= n for p in factors[n])
    f = 1-j-d
    return f, f+comb(j, 2)+j*d


def profile(x, saved, spf, factors):
    limit = 2*x
    w0, y0 = floor_root(x, 5), floor_root(x, 3)
    w1, y1 = floor_root(limit, 5), floor_root(limit, 3)
    ff, ee, rough, bad, edge = [[0]*(limit+1) for _ in range(5)]
    for n in range(2, limit+1):
        if spf[n] <= w0:
            continue
        rough[n] = 1
        ff[n], ee[n] = weights(n, w0, y0, spf, factors)
        assert abs(ff[n]) <= 6 and abs(ee[n]) <= 6
        bad[n] = int(any(w0 < p <= w1 or y0 < p <= y1 for p in factors[n]))
        edge[n] = int(n <= isqrt(limit))
    frozen = exact_convolution(ff, ee)
    union = [int(a or b) for a, b in zip(bad, edge)]
    envelope = exact_convolution(union, rough)
    rsize, bsize, hsize, dsize = map(sum, [rough, bad, edge, union])
    # Full Young norm includes convolution coefficients beyond the returned
    # prefix. Bounding the prefix by the full Young bound remains valid.
    envelope_prefix_square_sum = sum(v*v for v in envelope)
    assert envelope_prefix_square_sum <= dsize*dsize*rsize
    errors = []
    examples = []
    for n in range(x+2, limit+1, 2):
        row = saved[n]
        w, y = row['wheel_cutoff'], row['cubic_cutoff']
        fm, em = weights(n//2, w, y, spf, factors)
        midpoint = fm*em
        actual_t = row['doubled_operator_sum']-midpoint
        delta = actual_t-frozen[n]
        assert abs(delta) <= 4*6**2*envelope[n]
        errors.append(delta)
        if delta and len(examples) < 3:
            examples.append({'target': n, 'actual_T': actual_t,
                             'frozen_convolution': frozen[n], 'difference': delta,
                             'midpoint': midpoint})
    squared = sum(v*v for v in errors)
    young_upper = 16*6**4*dsize*dsize*rsize
    assert squared <= young_upper
    return {
        'X': x, 'target_count': len(errors),
        'frozen_cutoffs': [w0, y0], 'maximum_moving_cutoffs': [w1, y1],
        'rough_support_size': rsize, 'threshold_band_support_size': bsize,
        'endpoint_support_size': hsize, 'union_support_size': dsize,
        'exact_transfer_squared_error': squared,
        'exact_transfer_absolute_error': sum(abs(v) for v in errors),
        'maximum_absolute_transfer_error': max(map(abs, errors)),
        'nonzero_differences': sum(v != 0 for v in errors),
        'envelope_prefix_square_sum': envelope_prefix_square_sum,
        'exact_Young_upper_bound': young_upper,
        'all_pointwise_support_bounds_verified': True,
        'first_nonzero_examples': examples,
        'descriptive_log_normalizations': {
            'support_B_times_log_squared_over_X': bsize*log(x)**2/x,
            'squared_error_times_log_fourth_over_X_cubed': squared*log(x)**4/x**3,
            'squared_error_times_log_fifth_over_X_cubed': squared*log(x)**5/x**3,
        },
    }


def run():
    source = ROOT/'research'/'joint-average-bands.json'
    saved = {r['target']: r for r in json.loads(source.read_text())['profiles']}
    limit = 2*max(XS)
    spf, _ = sieve(limit)
    factors = [[] for _ in range(limit+1)]
    for n in range(2, limit+1):
        factors[n] = distinct_factors(n, spf)
    rows = []
    for x in XS:
        row = profile(x, saved, spf, factors)
        rows.append(row)
        print(x, row['threshold_band_support_size'],
              row['exact_transfer_squared_error'], flush=True)
    result = {
        'date': '2026-10-30',
        'scope': 'Exact finite support and norm audit; no inferred asymptotic or all-target result.',
        'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
        'weight_absolute_bound': 6,
        'profiles': rows,
    }
    path = ROOT/'research'/'frozen-threshold-transfer.json'
    path.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print('Saved', path, flush=True)


if __name__ == '__main__':
    run()
