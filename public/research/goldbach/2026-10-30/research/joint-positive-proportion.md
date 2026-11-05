# Positive operator sums for a positive proportion of targets

Date: 2026-10-27, Asia/Tehran.

Status: a consequence of the proved positive first moment, a standard upper-bound sieve, and an elementary singular-factor second moment. No uniform positivity or almost-all theorem is established. No novelty claim is made; the result concerns this particular operator, not a new proof of an unproved Goldbach statement.

## 1. Statement and inputs

Use the operator S(N) from [the averaged theorem](joint-operator-average.md), with the initial sieve through floor(N^(1/5)), late cutoff floor(N^(1/3)), and smaller member in I_N=[floor(sqrt(N))+1,N/2]. Let W_N be the number of initial-sieve survivors, C(N) the restricted prime-pair count, and

    S_+(N)=max(S(N),0).

The pointwise ten-state proof gives

    S_+(N)<=C(N)<=W_N,       |S(N)|<=9*W_N.                  (1)

The previously established first moment is

    sum_(X<N<=2X, N even) S(N)
       =[a+o(1)]*X^2/log(X)^2,
    a=3*kappa/4>0,                                         (2)

where kappa=c_F*c_E and 29/300<kappa<3/10.

**Theorem.** There are absolute constants eta,delta>0 and X_0 such that, for every X>=X_0,

    #{even N in (X,2X] : S(N)>=eta*N/log(N)^2} >=delta*X.    (3)

One may take eta=3*kappa/16; in particular eta>29/1600. No numerical value of delta or X_0 is claimed here. Since (X,2X] contains X/2+O(1) even targets, (3) is a positive-proportion result among even targets. Every target counted in (3) has at least eta*N/log(N)^2 restricted prime pairs, because C(N)>=S(N).

The new ingredient beyond the first moment is an upper bound preventing all the positive mass from concentrating on a vanishing fraction of targets. This proof does not show that the exceptional fraction tends to zero.

## 2. A sieve bound uniform in the target

Define the target-dependent singular factor

    G(N)=product_(p|N, p>2) (p-1)/(p-2).                    (4)

We prove that an absolute constant A exists such that, uniformly for sufficiently large even N,

    W_N <= A*G(N)*N/log(N)^2.                              (5)

It is important that A does not depend on the prime divisors of N. Applying a fixed-shift theorem with an unspecified shift-dependent constant would not suffice for the averaging argument.

For a prime p let E_p be the forbidden residues r=0 or r=N modulo p. Their number is

    nu_N(p)=1 if p|N, and 2 otherwise.

In particular nu_N(2)=1 because N is even. Put g_N(p)=nu_N(p)/p and extend multiplicatively to squarefree integers. For each squarefree d, CRT and interval floor counts give

    #{r in I_N : r in E_p for every p|d}
       = L_N*g_N(d)+r_d,
    |r_d|<=nu_N(d)<=2^omega(d)=tau(d),                     (6)

where L_N=|I_N|<=N/2.

The dimension-two hypothesis needed for the fundamental lemma holds with a constant independent of N. Indeed g_N(2)=1/2 and g_N(p)<=2/p for odd p, so, for 2<=u<=v,

    product_(u<=p<v) (1-g_N(p))^(-1)
       <=K*(log(v)/log(u))^2,                              (7)

with an absolute K, by Mertens' product bounds for the reference density 1/2 at p=2 and 2/p at odd primes. Also g_N(p)<=2/3 uniformly. These estimates cover every possible pattern of target prime divisors.

Fix a sufficiently large absolute constant s>=10 for the fundamental lemma, and use only a weaker preliminary sieve with

    D=N^(1/2),       z=N^(1/(2s))=D^(1/s).

The desired wheel removes all primes through N^(1/5), so its survivors are a subset of the set sifted by primes p<z. The upper-bound part of the fundamental lemma, with fixed dimension and this fixed ratio s, gives

    W_N <= A_0*L_N*V_N(z)
               +A_1*sum_(d<=D, d squarefree)|r_d|,
    V_N(z)=product_(p<z)(1-g_N(p)),                        (8)

for absolute constants A_0,A_1. The primary reference is [Tao's sieve notes, Lemma 17 and Corollary 19](https://terrytao.wordpress.com/2015/01/21/254a-notes-4-some-sieve-theory/). Only this coarse upper-bound form is needed; no lower-bound sieve is invoked. The constant is uniform because the dimension hypothesis (7) and the distance from g_N(p)=1 are uniform.

The exact floor remainder in (6) is small enough at this weaker level:

    sum_(d<=D, d squarefree)|r_d|
       <=sum_(d<=D)tau(d)
       =sum_(ab<=D)1
       <=D*sum_(a<=D)1/a
       =O(N^(1/2)*log(N)).                                (9)

Next compare the sieve density to the fixed two-root reference product

    V_0(z)=(1/2)*product_(2<p<z)(1-2/p).

For z>2,

    V_N(z)=V_0(z)
              *product_(p|N, 2<p<z)(p-1)/(p-2)
           <=V_0(z)*G(N).

Since 1-2/p<=(1-1/p)^2 for odd p,

    V_0(z)<=2*product_(p<z)(1-1/p)^2
           <<1/log(z)^2
           <<1/log(N)^2.                                 (10)

Combining (8)-(10), and using G(N)>=1 to absorb the lower-order remainder, proves (5). No coprimality assumption between r and N-r is made. Shared prime factors are already included in nu_N(p).

## 3. The singular factor has a bounded mean square

For odd primes put

    h(p)=((p-1)/(p-2))^2-1
        =2/(p-2)+1/(p-2)^2.

Extend h multiplicatively to odd squarefree integers, put h(1)=1, and set h(d)=0 on other positive integers. All h(d) are nonnegative. The finite divisor expansion is

    G(n)^2=sum_(d|n)h(d).                                 (11)

The Euler product

    K_2=sum_(d>=1)h(d)/d
       =product_(p>2)(1+h(p)/p)                           (12)

converges: h(p)/p=O(1/p^2). For a completely uniform majorant, h(p)/p<=9/p^2 for p>=3, because the difference after clearing denominators is (p-3)*(7p-12)>=0. Thus K_2<=exp(9/2), using sum_(m>=3)1/m^2<=1/2. This deliberately crude bound is sufficient.

Nonnegativity lets us use the exact floor inequality without an accumulated floor error:

    sum_(n<=Y)G(n)^2
       =sum_(d<=Y)h(d)*floor(Y/d)
       <=Y*K_2.                                          (13)

Because G(2m)=G(m),

    sum_(X<N<=2X, N even)G(N)^2
       <=sum_(m<=X)G(m)^2
       <=K_2*X.                                          (14)

This is where the dependence on the prime factors of the target is controlled in the second moment.

## 4. A second moment for the positive part, and for the full score

For N in (X,2X], (1) and (5) give

    S_+(N)^2 <= A^2*G(N)^2*N^2/log(N)^4
              <=4*A^2*G(N)^2*X^2/log(X)^4.

Summing and using (14), there is an absolute B=4*A^2*K_2 such that

    sum_(X<N<=2X, N even) S_+(N)^2
       <=B*X^3/log(X)^4.                                 (15)

The full signed second moment also satisfies

    sum_(X<N<=2X, N even) S(N)^2
       <=81*B*X^3/log(X)^4,                               (16)

by |S(N)|<=9W_N. The positive-part estimate is stronger and is enough for the conclusion. These are upper bounds, not asymptotic formulas for the second moment or variance.

## 5. Cauchy-Schwarz gives a positive proportion with a positive margin

Let

    T_X={even N in (X,2X] : S(N)>(a/2)*X/log(X)^2}.

There are X/2+O(1) even targets in the interval. On the complement of T_X, each score is at most the displayed threshold, including any negative scores. Hence (2) gives

    sum_(N in T_X)S(N)
       >=sum S(N)-(a/2)*X/log(X)^2*(X/2+O(1))
       =[3a/4+o(1)]*X^2/log(X)^2
       >=(a/2)*X^2/log(X)^2                               (17)

for sufficiently large X. All scores on T_X are positive, so Cauchy-Schwarz and (15) imply

    (a^2/4)*X^4/log(X)^4
       <=|T_X|*sum_(N in T_X)S_+(N)^2
       <=|T_X|*B*X^3/log(X)^4.

Therefore

    |T_X|>=(a^2/(4B))*X.                                  (18)

For N<=2X and log(N)>=log(X),

    (a/2)*X/log(X)^2 >=(a/4)*N/log(N)^2.

Taking eta=a/4=3*kappa/16 and any delta<=a^2/(4B) proves (3). A numerical delta is not supplied because the absolute sieve constant A has not been numerically optimized or tracked. The existence of fixed positive eta and delta is unaffected.

## 6. Interpretation and remaining gap

The earlier first moment alone gave only a lower bound of order X/log(X) for the number of positive-score targets. The uniform sieve envelope and the bounded mean square of G(N) strengthen this to order X, with scores of order N/log(N)^2 on that set.

This conclusion is compatible with infinitely many targets having S(N)<0 or S(N)=0. It does not bound the exceptional fraction by a quantity tending to zero, and it does not remove any individual exceptional target. An almost-all or uniform result would need additional information about the fixed-sum correlations beyond the upper bounds used here.

This proof also does not improve a prime-distribution theorem simply because it yields Goldbach representations on a positive proportion. Its specific content is that the constructed F/H operator itself has positive values of the expected scale on a positive proportion of even targets. The result should be read with that scope.

## Dependencies and reproducibility

The input first moment and the exact positive sign of kappa are proved in `research/joint-operator-average.md` and checked by `experiments/avgconstant_joint_operator.py`. The bound |q|<=9 and the stronger q<=prime-pair-indicator are checked on the ten-state product domain in the existing exact operator verifiers. The upper-bound sieve in (8) is an established theorem with its hypotheses verified above; it is not inferred from finite experiments. Equations (11)-(18) are elementary exact inequalities.
