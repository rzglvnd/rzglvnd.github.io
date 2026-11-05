# The remaining fixed-target estimate as a reflected correlation

Date: 2026-10-27, Asia/Tehran.

Status: exact identities, an averaged cancellation consequence, and a proved limitation of the unrefined Cauchy--Schwarz estimate. No uniform lower bound for the correlation is established.

## 1. Center on the odd summands

Fix even N large enough that w=floor(N^(1/5))>=2, and put y=floor(N^(1/3)), z=floor(sqrt(N)). Let

    D_N={odd n: z+1<=n<=N-z-1},       L_N=|D_N|~N/2.

This set is invariant under n -> N-n. For n in D_N, set f_N(n)=F_N(n) and e_N(n)=E_N(n) when n has no prime factor <=w, and set both values to zero otherwise. The single-side functions are

    F=1-J-D,     H=binom(J,2)+JD,     E=F+H,

with the canonical late-divisor count and thresholds from `joint-survival.md`. Extend both arrays by zero off D_N.

Define

    U_N=sum_(n in D_N)f_N(n),
    V_N=sum_(n in D_N)e_N(n),
    T_N=sum_(n in D_N)f_N(n)*e_N(N-n),
    m_N=f_N(N/2)*e_N(N/2).

The midpoint term is zero if N/2 is even or not a wheel survivor. Pairing n with N-n gives the exact identity

    2*S(N)=T_N+m_N.                                         (1)

Each off-center pair contributes twice its joint score to T_N; the midpoint contributes only once, which explains the correction.

Now center the single-side functions on D_N and define

    R_N=sum_(n in D_N) [f_N(n)-U_N/L_N]
                         *[e_N(N-n)-V_N/L_N].

Reflection preserves the marginal sums. Expanding and summing gives

    T_N=U_N*V_N/L_N+R_N,
    2*S(N)=U_N*V_N/L_N+R_N+m_N.                             (2)

The correlation R_N measures the error in multiplying these two marginal means along the particular reflection n -> N-n. It is not assumed to vanish. Conditioning on odd positions matters: using all integers would build a predictable parity correlation into this remainder and change the marginal baseline by a factor of two.

## 2. What the one-variable and averaged theorems supply

The factor-simplex counting argument in [the averaged proof](joint-operator-average.md), applied at the fixed parameter N, gives

    U_N=[c_F+o(1)]*N/log(N),
    V_N=[c_E+o(1)]*N/log(N).

Removing the O(sqrt(N)) endpoint positions does not change these leading terms. Since L_N~N/2 and kappa=c_F*c_E>0,

    U_N*V_N/L_N=[2*kappa+o(1)]*N/log(N)^2.                  (3)

The midpoint is bounded in absolute value by 9. Combining (2)-(3) with the proved averaged theorem yields

    sum_(X<N<=2X, N even) R_N=o(X^2/log(X)^2).              (4)

Indeed, the sum of twice S has leading term 2*kappa*A_X, and the sum of U_N*V_N/L_N has the same leading term, where A_X=3X^2/(4log(X)^2). The O(X) summed midpoint contribution is negligible.

Equation (4) is signed average cancellation. It neither bounds the average absolute value nor bounds any individual negative R_N.

## 3. The precise one-sided estimate that would suffice

For each fixed target, positivity is equivalent to

    R_N > -U_N*V_N/L_N-m_N.                                (5)

For example, a uniform bound

    R_N >= -(2*kappa-epsilon)*N/log(N)^2                    (6)

for some fixed epsilon>0 and all sufficiently large even N would, together with (3), prove S(N)>0 for all sufficiently large even N. The remaining finite range would still need checking.

No estimate of the form (6) is proved here. Writing it explicitly identifies the missing result; it does not reduce it to a consequence of the known marginals or their positive average.

## 4. Why the first Cauchy--Schwarz estimate loses too much

Let

    A_N=sum f_N(n)^2-U_N^2/L_N,
    B_N=sum e_N(n)^2-V_N^2/L_N.

The exact inequality R_N>=-sqrt(A_N*B_N) gives

    S(N)>=[U_N*V_N/L_N-sqrt(A_N*B_N)+m_N]/2.                (7)

This lower bound is eventually negative. Every prime in D_N contributes 1 to both squared sums. The prime number theorem gives N/log(N)+o(N/log(N)) such primes; the omitted initial interval contains at most O(sqrt(N)) integers. The centering terms U_N^2/L_N and V_N^2/L_N are O(N/log(N)^2). Hence

    A_N>=[1+o(1)]*N/log(N),
    B_N>=[1+o(1)]*N/log(N).

Their square-root product is at least [1+o(1)]N/log(N), which exceeds the positive term in (3) by a growing logarithmic factor. The bounded midpoint cannot repair this.

This proves failure of the particular bound (7), not failure of the actual operator. A useful correlation estimate must exploit the arithmetic structure of the reflection beyond the two separate variances.

## 5. Exact finite audit

The standard-library experiment `experiments/joint_reflection_covariance.py` constructs the two score arrays from divisibility. It checks (1)-(2), reconstructs R_N independently as a sum of centered integer numerators, and verifies Cauchy--Schwarz with exact fractions. Every score agrees with the independently saved direct computation.

| N | Exact S(N) | Exact reflected correlation R_N |
|---:|---:|---:|
| 68 | 1/2 | -5 |
| 212 | 1/2 | -479/46 |
| 1,000 | 23 | 1187/234 |
| 10,000 | 191/2 | -82373/2450 |
| 100,000 | 508 | -4418355/24842 |
| 999,998 | 2663 | -1166452447/498999 |
| 1,000,000 | 3274 | -556669121/499000 |

The bound (7) is negative in every listed case; its sign is checked by rational squared comparisons, independently of the descriptive decimal square roots. At N=1,000,000 it is approximately -48,068 despite the actual positive score 3274.

The [independent audit](joint-reflection-audit.md) checked the identities, asymptotic factors, implementation, and reproducibility. These computations show both signs of R_N and verify the decomposition. They supply no extrapolated uniform correlation bound.

## Reproduction

    python experiments/joint_reflection_covariance.py

Output: `research/joint-reflection-covariance.json`.
