"""Exact audit of candidate lower bounds and cubic-root sieve structure.

Prime-pair convolution uses carry-free integer packing. Density comparisons
use outward-rounded fixed-point intervals, with exact rational fallback.
Finite success is not a proof of a uniform lower bound.
"""

from array import array
from fractions import Fraction as F
from math import gcd, isqrt, prod
from pathlib import Path
from time import perf_counter
import json


SCALE = 1 << 64


def sieve(limit):
    spf = array('I', [0])*(limit+1)
    for p in range(2,limit+1):
        if spf[p] == 0:
            spf[p] = p
            if p*p <= limit:
                for n in range(p*p,limit+1,p):
                    if spf[n] == 0:
                        spf[n] = p
    flags = bytearray(int(spf[n]==n) for n in range(limit+1))
    flags[0] = 0
    return spf,flags


def exact_convolution(flags):
    limit = len(flags)-1
    assert limit+1 < 1 << 24
    packed = bytearray(3*(limit+1))
    packed[::3] = flags
    encoded = int.from_bytes(packed,'little')
    square = encoded*encoded
    # Base 2^24 exceeds every convolution coefficient, so no carries occur.
    coefficients = square.to_bytes(3*(2*limit+1),'little')
    return [int.from_bytes(coefficients[3*n:3*n+3],'little') for n in range(limit+1)]


def distinct_factors(n,spf):
    result = []
    while n > 1:
        p = spf[n]
        result.append(p)
        while n % p == 0:
            n //= p
    return result


def density_bounds(total,z,spf,prefix):
    lo,hi = prefix[z]
    for p in distinct_factors(total,spf):
        if 2 < p <= z:
            lo = lo*(p-1)//(p-2)
            hi = (hi*(p-1)+(p-3))//(p-2)
    return lo,hi


def exact_density(total,z,primes):
    ps = [p for p in primes if p<=z]
    return F(prod(p-1 if total%p==0 else p-2 for p in ps),prod(ps))


def fixed_point_prefix(limit,flags):
    lo = hi = SCALE//2
    prefix = [(0,0)]*(limit+1)
    for z in range(2,limit+1):
        if z>2 and flags[z]:
            lo = lo*(z-2)//z
            hi = (hi*(z-2)+z-1)//z
        prefix[z] = lo,hi
    return prefix


def ratio_scan(limit,spf,flags,convolution):
    primes = [p for p in range(2,isqrt(limit)+1) if flags[p]]
    prefix = fixed_point_prefix(isqrt(limit),flags)
    smallest = None
    records = []
    failures = []
    exact_fallbacks = 0
    selected = []
    for total in range(6,limit+1,2):
        z = isqrt(total)
        length = total//2-z
        exceptions = 0
        for p in primes:
            if p>z:
                break
            exceptions += flags[total-p]
        ordered = convolution[total]
        assert (ordered+flags[total//2])%2 == 0
        count = (ordered+flags[total//2])//2-exceptions
        lo,hi = density_bounds(total,z,spf,prefix)
        if 2*count*SCALE < length*hi:
            rho = exact_density(total,z,primes)
            exact_fallbacks += 1
            if F(count) < F(length,2)*rho:
                failures.append(total)
        if smallest is None or count*SCALE*smallest.denominator < length*hi*smallest.numerator:
            rho = exact_density(total,z,primes)
            exact_fallbacks += 1
            ratio = F(count)/(length*rho)
            if smallest is None or ratio < smallest:
                smallest = ratio
                records.append({"target":total,"count":count,"density_mean_exact":str(length*rho),
                                "ratio_exact":str(ratio)})
        if total in (68,284,1022,3582,8850,20000,100000,250000,500000,1000000):
            rho = exact_density(total,z,primes)
            assert lo*rho.denominator <= rho.numerator*SCALE <= hi*rho.denominator
            selected.append({"target":total,"rough_prime_pairs":count,
                             "density_mean":float(length*rho),"ratio":float(F(count)/(length*rho))})
    return {"range":[6,limit],"even_targets":(limit-4)//2,
            "half_density_bound_failures":failures,"exact_rational_fallbacks":exact_fallbacks,
            "minimum_ratio_exact":str(smallest),"record_minima":records,"selected":selected}


def stage_correction_audit(flags,limit=10000):
    first = {}
    worst = F(0)
    worst_data = None
    for total in range(6,limit+1,2):
        z = isqrt(total)
        candidates = list(range(z+1,total//2+1))
        for p in range(2,z+1):
            if not flags[p]:
                continue
            previous = len(candidates)
            nu = 1 if total%p==0 else 2
            candidates = [r for r in candidates if r%p and (total-r)%p]
            epsilon = F(p*len(candidates)-(p-nu)*previous,p)
            row = {"target":total,"prime":p,"before":previous,"after":len(candidates),
                   "epsilon_exact":str(epsilon)}
            if epsilon < worst:
                worst,worst_data = epsilon,row
            for threshold in (1,2,5,10):
                if str(threshold) not in first and epsilon < -threshold:
                    first[str(threshold)] = row
    return {"range":[6,limit],"first_below_negative_threshold":first,"most_negative":worst_data}


def integer_cuberoot(n):
    r = round(n**(1/3))
    while (r+1)**3 <= n:
        r += 1
    while r**3 > n:
        r -= 1
    return r


def cubic_profile(total,spf,flags):
    y = integer_cuberoot(total)
    ps = [p for p in range(2,y+1) if flags[p]]
    # Fix the same sqrt-cutoff half interval as the full-depth experiments.
    z = isqrt(total)
    pairs = [(r,total-r) for r in range(z+1,total//2+1)
             if all(r%p and (total-r)%p for p in ps)]
    cells = {"PP":0,"PS":0,"SP":0,"SS":0}
    moment_left = moment_right = moment_product = 0
    both_composite = []
    prime_pairs = []
    def omega(n):
        count = 0
        while n>1:
            n //= spf[n]
            count += 1
        return count
    for r,s in pairs:
        left,right = omega(r),omega(s)
        assert left in (1,2) and right in (1,2)
        category = ('P' if left==1 else 'S')+('P' if right==1 else 'S')
        cells[category] += 1
        a,b = (-1)**left,(-1)**right
        moment_left += a
        moment_right += b
        moment_product += a*b
        if category=='SS' and len(both_composite)<4:
            both_composite.append([r,s])
        if category=='PP':
            prime_pairs.append([r,s])
    size = len(pairs)
    assert 4*cells['PP']==size-moment_left-moment_right+moment_product
    marginal_lower = max(0,cells['PP']-cells['SS'])
    # Same lower bound from inclusion-exclusion of the two prime subsets.
    assert marginal_lower == max(0,(cells['PP']+cells['PS'])+(cells['PP']+cells['SP'])-size)
    return {"target":total,"partial_cutoff":y,"interval":[z+1,total//2],
            "survivors":size,"categories":cells,
            "liouville_sums":{"left":moment_left,"right":moment_right,"product":moment_product},
            "marginals_only_lower_bound":marginal_lower,"prime_pairs":prime_pairs,
            "semiprime_pair_examples":both_composite}


def cubic_marginal_scan(spf,flags,limit=20000):
    failures = []
    minimum = None
    witness = None
    for total in range(6,limit+1,2):
        y,z = integer_cuberoot(total),isqrt(total)
        size = pp = ss = 0
        for r in range(z+1,total//2+1):
            s = total-r
            if spf[r] > y and spf[s] > y:
                size += 1
                if flags[r] and flags[s]:
                    pp += 1
                elif not flags[r] and not flags[s]:
                    ss += 1
        margin = pp-ss
        if margin <= 0:
            failures.append({"target":total,"PP":pp,"SS":ss})
        ratio = F(margin,size) if size else F(0)
        if minimum is None or ratio < minimum:
            minimum = ratio
            witness = {"target":total,"survivors":size,"PP":pp,"SS":ss,
                       "lower_bound":margin,"margin_fraction_exact":str(ratio)}
    return {"range":[6,limit],"targets":(limit-4)//2,
            "nonpositive_margin_cases":failures,"minimum_fraction_witness":witness}


def translated_window_audit(total):
    z = isqrt(total)
    f = bytearray(b'\x01')*(z+1)
    f[:2] = b'\x00\x00'
    for p in range(2,isqrt(z)+1):
        if f[p]:
            f[p*p:z+1:p] = b'\x00'*len(range(p*p,z+1,p))
    ps = [p for p in range(2,z+1) if f[p]]
    modulus,length = prod(ps),total//2-z
    allowed = [int(gcd(r*(total-r),modulus)==1) for r in range(modulus)]
    current = sum(allowed[:length])
    counts = []
    for start in range(modulus):
        counts.append(current)
        current += allowed[(start+length)%modulus]-allowed[start]
    mean = F(sum(counts),modulus)
    variance = F(sum(c*c for c in counts),modulus)-mean*mean
    assert mean == F(length*sum(allowed),modulus)
    # Exact two-point CRT product gives the same second moment.
    second = length*F(sum(allowed),modulus)
    for h in range(1,length):
        correlation = F(1)
        for p in ps:
            forbidden = {0,total%p,(-h)%p,(total-h)%p}
            correlation *= F(p-len(forbidden),p)
        second += 2*(length-h)*correlation
    assert variance == second-mean*mean
    empty = [a for a,c in enumerate(counts) if c==0]
    return {"target":total,"period":modulus,"length":length,
            "mean_exact":str(mean),"variance_exact":str(variance),
            "empty_window_count":len(empty),
            "first_empty_window":[empty[0],empty[0]+length-1] if empty else None,
            "goldbach_window":[z+1,total//2],"goldbach_window_count":counts[(z+1)%modulus]}


def run(limit=1000000):
    start = perf_counter()
    spf,flags = sieve(limit)
    convolution = exact_convolution(flags)
    # Independent direct counts for all small targets and a deterministic large sample.
    targets = list(range(4,2001,2))+[10000,20000,100000,250000,500000,limit]
    for total in targets:
        assert convolution[total] == sum(flags[r] and flags[total-r] for r in range(2,total-1))
    result = {
        "status":"Finite audit only; no uniform bound or Goldbach proof.",
        "method":"Exact base-2^24 integer convolution; rationally enclosed density comparisons.",
        "direct_convolution_cross_checks":len(targets),
        "ratio_scan":ratio_scan(limit,spf,flags,convolution),
        "local_corrections":stage_correction_audit(flags),
        "cubic_profiles":[cubic_profile(n,spf,flags) for n in (68,100,284,1000,10000,100000,1000000)],
        "cubic_marginal_scan":cubic_marginal_scan(spf,flags),
        "translated_window_audits":[translated_window_audit(n) for n in (50,68,100,284)],
        "elapsed_seconds":perf_counter()-start,
    }
    output = Path(__file__).resolve().parents[1]/'research'/'sieve-corrections-results.json'
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({"ratio_scan":result['ratio_scan'],"local_corrections":result['local_corrections'],
                      "cubic_summary":[{k:r[k] for k in ('target','partial_cutoff','survivors','categories','marginals_only_lower_bound')} for r in result['cubic_profiles']],
                      "elapsed_seconds":result['elapsed_seconds']},indent=2))


if __name__=='__main__':
    run()
