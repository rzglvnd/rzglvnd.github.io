"""Exact finite band averages for the joint operator, using integer convolution.

For each fixed (w,y) range, convolution of the single-side F and E weights
computes every target simultaneously. Coefficients are recovered without
rounding: digit capacity is proved before multiplying packed integers.
The r<=sqrt(N) boundary and midpoint are corrected exactly afterward.
Old direct-divisibility scores provide an independent comparison.
"""

import argparse
import hashlib
import json
from collections import defaultdict
from fractions import Fraction as Q
from math import comb,isqrt,log
from pathlib import Path
from time import perf_counter

from joint_operator_scaling import floor_root
from sieve_corrections import sieve,distinct_factors

ROOT=Path(__file__).resolve().parents[1]


def exact_convolution(a,b):
    """Return the first len(a) signed convolution coefficients exactly."""
    assert len(a)==len(b)
    count=len(a)
    shift_a=-min(0,min(a))
    shift_b=-min(0,min(b))
    aa=[v+shift_a for v in a]
    bb=[v+shift_b for v in b]
    maximum=count*max(aa)*max(bb)
    width=max(1,(maximum.bit_length()+7)//8)
    base=1<<(8*width)
    assert maximum<base
    x=int.from_bytes(b''.join(v.to_bytes(width,'little') for v in aa),'little')
    y=int.from_bytes(b''.join(v.to_bytes(width,'little') for v in bb),'little')
    raw=(x*y).to_bytes(width*(2*count),'little')
    result=[]
    prefix_a=prefix_b=0
    for n in range(count):
        prefix_a+=a[n]
        prefix_b+=b[n]
        value=int.from_bytes(raw[width*n:width*(n+1)],'little')
        result.append(value-shift_b*prefix_a-shift_a*prefix_b-shift_a*shift_b*(n+1))
    return result


def scores(limit):
    spf,flags=sieve(limit)
    factors=[[] for _ in range(limit+1)]
    for n in range(2,limit+1):
        factors[n]=distinct_factors(n,spf)
    groups=defaultdict(list)
    for n in range(6,limit+1,2):
        groups[(floor_root(n,5),floor_root(n,3))].append(n)
    results={}
    for index,((w,y),targets) in enumerate(groups.items()):
        top=max(targets)
        f=[0]*(top+1)
        e=[0]*(top+1)
        for n in range(1,top+1):
            if n>1 and spf[n]<=w:
                continue
            j=sum(w<p<=y for p in factors[n])
            d=sum(p>y and p*p<=n for p in factors[n])
            f[n]=1-j-d
            e[n]=f[n]+comb(j,2)+j*d
        conv=exact_convolution(f,e)
        for n in targets:
            z=isqrt(n)
            mid=n//2
            twice=conv[n]+f[mid]*e[mid]-sum(f[r]*e[n-r]+e[r]*f[n-r] for r in range(1,z+1))
            results[n]={'target':n,'wheel_cutoff':w,'cubic_cutoff':y,'doubled_operator_sum':twice}
    # Prime-pair convolution is a separate endpoint validation.
    ppconv=exact_convolution(list(flags),list(flags))
    for n,row in results.items():
        z=isqrt(n)
        prime_twice=ppconv[n]+flags[n//2]-2*sum(flags[r] and flags[n-r] for r in range(1,z+1))
        assert prime_twice%2==0
        pp=prime_twice//2
        assert row['doubled_operator_sum']<=2*pp
        row['restricted_prime_pairs']=pp
    return results,{'constant_cutoff_groups':len(groups),'method':'Carry-free signed integer convolution plus exact boundary and midpoint corrections.'}


def band(rows,x):
    selected=[rows[n] for n in range(x+1,2*x+1) if n%2==0]
    assert len(selected)==x//2
    twice=sum(r['doubled_operator_sum'] for r in selected)
    pp=sum(r['restricted_prime_pairs'] for r in selected)
    aggregate=Q(twice,2)
    minimum=min(selected,key=lambda r:r['doubled_operator_sum'])
    maximum=max(selected,key=lambda r:r['doubled_operator_sum'])
    minratio=min(selected,key=lambda r:Q(r['doubled_operator_sum'],2*r['restricted_prime_pairs']))
    maxratio=max(selected,key=lambda r:Q(r['doubled_operator_sum'],2*r['restricted_prime_pairs']))
    scale=3*x*x/(4*log(x)**2)
    return {'X':x,'even_target_interval':[x+2,2*x],'target_count':len(selected),
            'operator_sum_exact':str(aggregate),'prime_pairs_sum':pp,
            'ratio_of_sums_exact':str(aggregate/pp),'ratio_of_sums_decimal':float(aggregate/pp),
            'normalization_A_decimal':scale,'operator_sum_over_A_decimal':float(aggregate)/scale,
            'prime_pairs_sum_over_A_decimal':pp/scale,
            'positive_targets':sum(r['doubled_operator_sum']>0 for r in selected),
            'zero_targets':sum(r['doubled_operator_sum']==0 for r in selected),
            'negative_targets':sum(r['doubled_operator_sum']<0 for r in selected),
            'minimum_operator_sum':{'target':minimum['target'],'value_exact':str(Q(minimum['doubled_operator_sum'],2))},
            'maximum_operator_sum':{'target':maximum['target'],'value_exact':str(Q(maximum['doubled_operator_sum'],2))},
            'minimum_target_ratio':{'target':minratio['target'],'value_exact':str(Q(minratio['doubled_operator_sum'],2*minratio['restricted_prime_pairs']))},
            'maximum_target_ratio':{'target':maxratio['target'],'value_exact':str(Q(maxratio['doubled_operator_sum'],2*maxratio['restricted_prime_pairs']))}}


def run():
    parser=argparse.ArgumentParser()
    parser.add_argument('--limit',type=int,default=250000)
    args=parser.parse_args()
    assert args.limit>=10000 and args.limit%2==0
    start=perf_counter()
    source=ROOT/'research'/'joint-operator-stress.json'
    saved=json.loads(source.read_text())
    # Retain only the proven exhaustive range; selected larger samples are not
    # averaged into bands or used to manufacture a contiguous range.
    old={r['target']:r for r in saved['profiles'] if 'exhaustive-small' in r['families']}
    assert set(old)==set(range(6,10001,2))
    rows,construction=scores(args.limit)
    for n,prior in old.items():
        assert rows[n]['doubled_operator_sum']==prior['doubled_operator_sum']
        assert rows[n]['restricted_prime_pairs']==prior['actual_restricted_prime_pairs']
    additional=[r for r in saved['profiles'] if 10000<r['target']<=args.limit]
    for prior in additional:
        n=prior['target']
        assert rows[n]['doubled_operator_sum']==prior['doubled_operator_sum']
        assert rows[n]['restricted_prime_pairs']==prior['actual_restricted_prime_pairs']
    xs=[x for x in (500,1000,2000,4000,5000,10000,20000,25000,50000,100000,125000) if 2*x<=args.limit]
    bands=[band(rows,x) for x in xs]
    for b in bands:
        print(b['X'],b['operator_sum_exact'],b['prime_pairs_sum'],b['ratio_of_sums_decimal'],b['operator_sum_over_A_decimal'],flush=True)
    result={'status':'Exact finite band totals; logarithmic normalizations are decimal diagnostics, not asymptotic proofs.',
            'date':'2026-10-27','exhaustive_even_interval':[6,args.limit],
            'source_file':str(source.relative_to(ROOT)),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
            'old_direct_profiles_matched':len(old),'additional_direct_profiles_matched':len(additional),
            'construction':construction,'bands':bands,
            'total_targets':len(rows),'positive_targets':sum(r['doubled_operator_sum']>0 for r in rows.values()),
            'zero_targets':[n for n,r in rows.items() if r['doubled_operator_sum']==0],
            'negative_targets':[n for n,r in rows.items() if r['doubled_operator_sum']<0],
            'profiles':list(rows.values()),'elapsed_seconds':perf_counter()-start}
    path=ROOT/'research'/'joint-average-bands.json'
    path.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print('Saved',path,'elapsed',result['elapsed_seconds'],flush=True)


if __name__=='__main__':
    run()
