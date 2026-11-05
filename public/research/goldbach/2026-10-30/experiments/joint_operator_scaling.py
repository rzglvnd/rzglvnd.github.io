"""Direct divisibility experiment for the oriented F/H minorant.

This is a finite scaling experiment, not CRT certificate construction and
not a uniform positive-bound theorem. All arithmetic and reported bounds
are exact. Prime labels are used only for pointwise validation.
"""

import json
from collections import Counter
from fractions import Fraction
from math import comb, isqrt
from pathlib import Path
from time import perf_counter

from sieve_corrections import sieve, distinct_factors

ROOT = Path(__file__).resolve().parents[1]
TARGETS = [1000,10000,100000,1000000,2000000,5000000,10000000]
ALLOWED_SIDE_STATES = {(0,0),(0,1),(1,0),(1,1),(1,2),
                       (2,0),(2,1),(3,0),(3,1),(4,0)}


def floor_root(n,k):
    lo,hi = 0,n+1
    while hi-lo>1:
        mid = (lo+hi)//2
        if mid**k<=n:
            lo = mid
        else:
            hi = mid
    assert lo**k<=n<(lo+1)**k
    return lo


def doubled_operator(jl,jr,dl,dr):
    fl,fr = 1-jl-dl,1-jr-dr
    hl,hr = comb(jl,2)+jl*dl,comb(jr,2)+jr*dr
    return 2*fl*fr+hl*fr+hr*fl


def run():
    start = perf_counter()
    # First verify the proposed pointwise algebra on the full allowed set,
    # including states that need not occur in the finite scans.
    for jl,dl in ALLOWED_SIDE_STATES:
        for jr,dr in ALLOWED_SIDE_STATES:
            assert doubled_operator(jl,jr,dl,dr)<=2*int(jl+dl+jr+dr==0)
    spf,flags = sieve(max(TARGETS))
    sieve_seconds = perf_counter()-start
    print('SPF table ready in',sieve_seconds,'seconds',flush=True)
    rows = []
    for total in TARGETS:
        tick = perf_counter()
        y,w,z = floor_root(total,3),floor_root(total,5),isqrt(total)
        histogram = Counter()
        twice_sum = pairs = wheel_candidates = 0
        for r in range(z+1,total//2+1):
            s = total-r
            if spf[r]<=w or spf[s]<=w:
                continue
            wheel_candidates += 1
            side_states = []
            for n in (r,s):
                ps = distinct_factors(n,spf)
                j = sum(w<p<=y for p in ps)
                d = sum(p>y and p*p<=n for p in ps)
                assert (j,d) in ALLOWED_SIDE_STATES
                side_states.append((j,d))
            (jl,dl),(jr,dr) = side_states
            value = doubled_operator(jl,jr,dl,dr)
            actual = int(bool(flags[r] and flags[s]))
            assert actual==int(jl+dl+jr+dr==0)
            assert value<=2*actual
            twice_sum += value
            pairs += actual
            histogram[(jl,jr,dl,dr)] += 1
        # Every prime pair in this interval survives the wheel.
        independently_counted_pairs = sum(bool(flags[r] and flags[total-r])
                                          for r in range(z+1,total//2+1))
        assert pairs==independently_counted_pairs
        lower = -(-twice_sum//2)
        assert lower<=pairs
        record = {'target':total,'cubic_cutoff':y,'wheel_cutoff':w,
                  'wheel_primes':[p for p in range(2,w+1) if flags[p]],
                  'interval':[z+1,total//2], 'wheel_candidates':wheel_candidates,
                  'operator_sum_exact':str(Fraction(twice_sum,2)),
                  'integer_lower_bound':lower,'nonnegative_pair_lower_bound':max(0,lower),
                  'actual_restricted_prime_pairs':pairs,
                  'pointwise_checks':wheel_candidates,'all_checks_passed':True,
                  'state_histogram':[{'state':list(s),'count':count} for s,count in sorted(histogram.items())],
                  'elapsed_seconds':perf_counter()-tick}
        rows.append(record)
        print(json.dumps({k:record[k] for k in ('target','wheel_cutoff','operator_sum_exact',
                      'nonnegative_pair_lower_bound','actual_restricted_prime_pairs','elapsed_seconds')}),flush=True)
    result = {'status':'Exact finite direct-divisibility scaling experiment; no uniform positivity theorem and no CRT construction in this script.',
              'date':'2026-10-26','operator':'F_L*F_R+(H_L*F_R+H_R*F_L)/2, F=1-J-D, H=binom(J,2)+J*D',
              'rule':'wheel includes every prime <= floor(N^(1/5)); late cutoff floor(N^(1/3))',
              'algebraic_state_pairs_checked':len(ALLOWED_SIDE_STATES)**2,
              'allowed_side_states':[list(s) for s in sorted(ALLOWED_SIDE_STATES)],
              'profiles':rows,'spf_sieve_seconds':sieve_seconds,
              'total_elapsed_seconds':perf_counter()-start}
    output = ROOT/'research'/'joint-operator-scaling.json'
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print('Saved',output,flush=True)


if __name__=='__main__':
    run()
