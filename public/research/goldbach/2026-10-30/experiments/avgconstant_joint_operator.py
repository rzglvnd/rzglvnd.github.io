"""Exact sign certificate and numerical factor integrals for the joint operator.

Standard library only. The rational certificate proves positivity of the
derived leading constant. Decimal quadrature is labeled numerical and is
not used to prove the sign or the underlying asymptotic theorem.
"""

from fractions import Fraction as F
import json
from math import log
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def log_bounds(x, terms=24):
    assert x >= 1
    t = (x-1)/(x+1)
    lo = 2*sum((t**(2*j+1)/F(2*j+1) for j in range(terms)), F(0))
    tail = 2*t**(2*terms+1)/(F(2*terms+1)*(1-t*t))
    return lo, lo+tail


def exact_sign_certificate(cells=256):
    # C3 = (1/2) integral_1^3 log(4-t)/t dt. The integrand is decreasing.
    # Upper-round every rational log bound to a shared fixed denominator,
    # avoiding huge denominator growth when summing the rigorous upper sum.
    scale = 1 << 56
    upper_scaled = 0
    for i in range(cells):
        t = 1+F(2*i, cells)
        upper = log_bounds(4-t)[1]/t
        scaled = upper*scale
        upper_scaled += -(-scaled.numerator//scaled.denominator)
    c3_upper = F(upper_scaled, cells*scale)
    assert c3_upper < F(41, 100)
    c4_upper = F(1, 36)
    # C3_balanced <= C3, and cE >= 1.
    cF_lower = 1-2*F(41, 100)-3*c4_upper
    assert cF_lower == F(29, 300) > 0
    return {'method': 'Exact rational decreasing-integrand upper sum and atanh-series remainder.',
            'riemann_cells': cells, 'log_series_terms': 24,
            'C3_upper_sum_exact': str(c3_upper), 'C3_strict_upper': '41/100',
            'C4_upper': str(c4_upper), 'cF_strict_lower': str(cF_lower),
            'cE_lower': '1', 'averaged_pair_coefficient_strict_lower': str(cF_lower)}


def simpson(fn, a, b, cells):
    assert cells % 2 == 0
    if a == b:
        return 0.0
    h = (b-a)/cells
    return h/3*(fn(a)+fn(b)+sum((4 if i % 2 else 2)*fn(a+i*h)
                               for i in range(1, cells)))


def numerical_constants(cells):
    full = lambda u: log((1-2*u)/u)/(u*(1-u))
    c3 = simpson(full, 1/5, 1/3, cells)
    c3_symmetric = simpson(lambda t: log(4-t)/t, 1, 3, cells)/2
    c3_balanced = simpson(lambda u: -log(1-2*u)/(u*(1-u)), 1/5, 1/4, cells)
    c3_balanced += simpson(full, 1/4, 1/3, cells)
    c3_E = simpson(lambda u: -log((2-3*u)*(1-2*u))/(u*(1-u)), 1/5, 1/4, cells)
    c3_E += simpson(lambda u: log((1-2*u)/(u*(2-3*u)))/(u*(1-u)), 1/4, 1/3, cells)
    def inner(u):
        return simpson(lambda v: log((4/5-u-v)/(1/5))/(u*v),
                       1/5, 3/5-u, cells)
    c4 = simpson(inner, 1/5, 2/5, cells)/6
    cF = 1-c3-c3_balanced-3*c4
    cE = 1+c3_E+3*c4
    return {'C3': c3, 'C3_symmetric_formula': c3_symmetric,
            'C3_balanced': c3_balanced, 'C3_E_positive': c3_E,
            'C4': c4, 'cF': cF, 'cE': cE, 'averaged_pair_coefficient': cF*cE,
            'rough_density_coefficient': 1+log(4)+c3+c4}


def run():
    exact = exact_sign_certificate()
    coarse, fine = numerical_constants(128), numerical_constants(256)
    assert abs(fine['C3']-fine['C3_symmetric_formula']) < 1e-8
    differences = {key: abs(fine[key]-coarse[key]) for key in fine}
    result = {'status': 'Exact sign certificate; decimal quadrature is numerical only. Asymptotic proof is separate.',
              'exact_certificate': exact,
              'numerical_quadrature_not_a_rigorous_enclosure': fine,
              'numerical_resolution_difference_128_vs_256': differences}
    path = ROOT/'research'/'joint-operator-average-constants.json'
    path.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    run()
