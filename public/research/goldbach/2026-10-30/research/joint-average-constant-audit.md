# Independent audit of the joint-operator average constants

Date: 2026-10-27, Asia/Tehran.

Status: the integral definitions, state classification, and exact sign certificate pass this audit. A new exact certificate also proves that the proposed averaged coefficient is below 3/10. The asymptotic theorem connecting these integrals to arithmetic counts is a separate proof; this note does not replace it or assert uniform fixed-target positivity.

## Reproduction after the interruption

The standard-library script `experiments/avgconstant_joint_operator.py` was rerun. Its JSON output reproduced byte for byte, with SHA-256

    3b514ebbc5adcdf1c6fa521dfcf405db6f8069bbf9f200054a02d6e524fe3146.

No correction to that script or its saved output was needed. Its Simpson quadrature values remain explicitly numerical; the sign certificate uses rational arithmetic only.

## 1. Normalization and regions

For squarefree k-factor integers whose prime factors exceed the fifth-root cutoff, let t_i be logarithmic factor sizes. In the leading bulk limit, t_i>1/5 and sum t_i=1. The symmetric k-factor mass is

    C_k = 1/k! * integral_(t_i>=1/5, sum t_i=1) 1/(t_1...t_k) dt_1...dt_(k-1).

The notation means t_k=1-sum_(i<k)t_i. Since sum t_i=1,

    1/(t_1...t_k) = sum_i 1/(product_(j!=i)t_j).

Symmetry therefore gives the equivalent (k-1)-dimensional formula

    C_k = 1/(k-1)! * integral_(u_i>=1/5, sum u_i<=4/5) 1/(u_1...u_(k-1)) du.

For k=3 this yields

    C3 = (1/2)*integral_1^3 log(4-t)/t dt.

Alternatively, sort the three factors as u<=v<=1-u-v. Then 1/5<=u<=1/3 and u<=v<=(1-u)/2. Integrating v gives

    C3 = integral_(1/5)^(1/3) log((1-2u)/u)/(u*(1-u)) du.

The original script computes both forms as an internal numerical consistency check. Their equality follows from the exact transformations above, not from their numerical agreement.

The balanced region (largest factor below 1/2) replaces the lower v endpoint by max(u,1/2-u). Thus

    C3_balanced = integral_(1/5)^(1/4) -log(1-2u)/(u*(1-u)) du
                  +integral_(1/4)^(1/3) log((1-2u)/u)/(u*(1-u)) du.

The region with largest factor below 1/2 and middle factor below 1/3 has upper v endpoint 1/3, with the same lower endpoint. Its integral is

    C3_E = integral_(1/5)^(1/4) -log((2-3u)*(1-2u))/(u*(1-u)) du
            +integral_(1/4)^(1/3) log((1-2u)/(u*(2-3u)))/(u*(1-u)) du.

For four factors, the equivalent symmetric formula gives

    C4 = (1/6)*integral_(u,v,w>=1/5, u+v+w<=4/5) 1/(u*v*w) du dv dw.

Integrating w first gives exactly the nested integral used by the script. Its u range is [1/5,2/5] and v range [1/5,3/5-u].

## 2. State classification

The following statements describe the leading bulk regions; equality boundaries have zero simplex measure. Moving-cutoff and negligible-region estimates belong to the accompanying asymptotic proof.

For a prime, F=E=1. For two factors, only the smaller factor is counted by J+D, so F=E=0.

For three distinct factors t_1<=t_2<=t_3 with each t_i>1/5:

| Region | (J,D) | F | E=F+H |
|---|---|---:|---:|
| t_3>1/2 | (2,0) | -1 | 0 |
| t_3<1/2 and t_2>1/3 | (1,2) | -2 | 0 |
| t_3<1/2 and t_2<1/3 | (2,1) | -2 | 1 |

In the first row, the other two factors sum to less than 1/2 and each exceeds 1/5, so each is below 3/10. In the other rows every factor is below 1/2, hence every late factor meets the canonical square-root condition. These observations justify the D counts, which must not be confused with ordinary factor multiplicity.

For four factors, each is below 2/5, and at most one exceeds 1/3. The possibilities are (J,D)=(4,0) or (3,1), both with F=-3 and E=3.

Therefore the single-side leading coefficients are

    cF = 1-C3-C3_balanced-3*C4,
    cE = 1+C3_E+3*C4.

These agree with the saved definitions. Numerically they are approximately 0.23033522966 and 1.23414681113, with product approximately 0.28426748918. These decimals are not claimed as rigorous enclosures.

## 3. Exact positive sign

The function log(4-t)/t is positive and decreasing for 1<=t<=3. The saved script uses a 256-cell upper rectangle sum for its half integral. Each logarithm is bounded by

    log x = 2*sum_(j>=0) z^(2j+1)/(2j+1),    z=(x-1)/(x+1),

with the first 24 terms below the true value and tail at most

    2*z^49 / (49*(1-z^2)).

Every cell upper bound is rounded upward to a fixed denominator before summation. The final exact upper sum is

    3765350825490954197/9223372036854775808 < 41/100.

The four-factor simplex has volume (1/5)^3/6=1/750. Since its integrand is at most 125,

    C4 <= (1/6)*125*(1/750) = 1/36.

Also 0<=C3_balanced<=C3 and C3_E>=0. It follows that

    cF > 1-2*(41/100)-3*(1/36) = 29/300 >0,
    cE >=1,
    kappa=cF*cE >29/300.

Every inequality in this sign proof is exact.

## 4. A new exact upper certificate: kappa<3/10

The new standard-library script `experiments/joint_average_upper_certificate.py` uses 1024-cell rational rectangle enclosures for the displayed one-variable integrals. The denominator u*(1-u) is positive and increasing throughout all intervals. The logarithm ratios have the following monotonicity:

    (1-2u)/u is decreasing;
    1/(1-2u) is increasing;
    1/((2-3u)*(1-2u)) is increasing;
    (1-2u)/(u*(2-3u)) is decreasing.

For the last assertion the derivative numerator, after multiplying by the positive squared denominator, is -2*(1-3u+3u^2)<0. For the third, the product in the denominator has derivative 12u-7<0 on the interval. Combining numerator endpoint bounds with denominator endpoint bounds gives rigorous lower and upper rectangles even where the whole quotient's monotonicity is not assumed. Logarithms use the same exact series remainder, and fixed-denominator rounding is outward.

The resulting rational enclosures establish

    C3 >405/1000,
    C3_balanced >318/1000,
    C3_E <191/1000.

For the four-factor integral, AM-GM gives u*v*w<=((u+v+w)/3)^3<=(4/15)^3. Therefore

    C4 >= (1/6)*(15/4)^3*(1/750) =3/256.

Write a=1-C3-C3_balanced, b=1+C3_E, c=C4. Then

    kappa=(a-3c)*(b+3c),
    d/dc kappa=3*(a-b-6c)<=0.

Here a<=1, b>=1, c>=0. Since cF=a-3c>0 was already proved, lowering c to 3/256 leaves both factors positive. The three strict integral bounds above now give

    kappa < (1-405/1000-318/1000-9/256)
             *(1+191/1000+9/256)
          =303655143/1024000000
          <3/10.

Together, the exact certificates prove

    29/300 < kappa < 3/10.

The saved output contains the full rational interval endpoints. If the independently proved average theorem identifies kappa as the limiting ratio of total operator score to total restricted prime-pair count, this strict upper bound obstructs an eventual uniform 30% margin. That implication depends on the averaging theorem; the integral certificate alone does not establish it.

## Reproduction

    python experiments/avgconstant_joint_operator.py
    python experiments/joint_average_upper_certificate.py

Outputs: `research/joint-operator-average-constants.json` and `research/joint-average-upper-certificate.json`.
