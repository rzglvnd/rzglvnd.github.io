"""Exact rational upper bound on the averaged joint-operator constant.

Uses rectangle enclosures and an explicit logarithm-series remainder.
No numerical quadrature or external package supplies a proof step.
The underlying asymptotic theorem is established separately.
"""

from fractions import Fraction as F
from pathlib import Path
import json

from avgconstant_joint_operator import log_bounds

ROOT = Path(__file__).resolve().parents[1]
SCALE = 1 << 56


def integral_enclosure(ratio, start, stop, increasing, cells=1024):
    """Enclose integral log(ratio(u))/(u*(1-u)) on [start,stop].

    Ratio monotonicity is supplied by the documented elementary formulas.
    The denominator is positive and increasing on all these intervals.
    """
    assert 0 < start < stop < F(1,2)
    width = (stop-start)/cells
    lower_scaled = upper_scaled = 0
    for i in range(cells):
        a,b = start+i*width,start+(i+1)*width
        xlo,xhi = (ratio(a),ratio(b)) if increasing else (ratio(b),ratio(a))
        assert 1 <= xlo <= xhi
        lo = log_bounds(xlo)[0]/(b*(1-b))
        hi = log_bounds(xhi)[1]/(a*(1-a))
        lower_scaled += (lo*SCALE).numerator//(lo*SCALE).denominator
        scaled = hi*SCALE
        upper_scaled += -(-scaled.numerator//scaled.denominator)
    return width*F(lower_scaled,SCALE),width*F(upper_scaled,SCALE)


def run():
    full = lambda u:(1-2*u)/u
    balanced_first = lambda u:1/(1-2*u)
    e_first = lambda u:1/((2-3*u)*(1-2*u))
    e_second = lambda u:(1-2*u)/(u*(2-3*u))
    c3 = integral_enclosure(full,F(1,5),F(1,3),False)
    bal_a = integral_enclosure(balanced_first,F(1,5),F(1,4),True)
    bal_b = integral_enclosure(full,F(1,4),F(1,3),False)
    balanced = tuple(a+b for a,b in zip(bal_a,bal_b))
    e_a = integral_enclosure(e_first,F(1,5),F(1,4),True)
    e_b = integral_enclosure(e_second,F(1,4),F(1,3),False)
    epositive = tuple(a+b for a,b in zip(e_a,e_b))
    assert c3[0] > F(405,1000)
    assert balanced[0] > F(318,1000)
    assert epositive[1] < F(191,1000)
    c4_lower = F(3,256)
    # k(c)=(a-3c)(b+3c) decreases for a<=1,b>=1,c>=0.
    # Positivity of the true cF is established by the older sign certificate.
    a_upper = 1-F(405,1000)-F(318,1000)
    b_upper = 1+F(191,1000)
    k_upper = (a_upper-3*c4_lower)*(b_upper+3*c4_lower)
    assert a_upper-3*c4_lower > 0
    assert k_upper < F(3,10)
    result = {
        'status':'Exact rational certificate for the constant only; the asymptotic theorem is separate.',
        'method':'1024-cell rectangle enclosures, 24-term atanh logarithm bounds, outward rounding at denominator 2^56.',
        'enclosures_exact':{
            'C3':list(map(str,c3)),
            'C3_balanced':list(map(str,balanced)),
            'C3_E_positive':list(map(str,epositive)),
            'C4_lower':str(c4_lower)},
        'coarse_strict_bounds':{'C3_lower':'405/1000','C3_balanced_lower':'318/1000',
                                'C3_E_positive_upper':'191/1000'},
        'averaged_pair_coefficient_strict_upper_exact':str(k_upper),
        'averaged_pair_coefficient_strict_upper':'3/10',
        'uses_previous_positive_sign_certificate':True}
    target=ROOT/'research'/'joint-average-upper-certificate.json'
    target.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    run()
