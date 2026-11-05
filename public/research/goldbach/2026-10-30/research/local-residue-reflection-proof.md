# Local residue effects in the reflected operator

Date: 2026-10-29, Asia/Tehran.

Status: proved fixed-modulus asymptotics and exact projection identities, using the prime number theorem in fixed arithmetic progressions. This note proves an obstruction to treating the original reflected remainder as negligible in mean absolute value. It does not prove almost-all or all-target positivity, and it does not give uniform estimates for a modulus growing with the target. No novelty claim is made.

## 1. Definitions and normalization

Use the operator, weights, and odd summand domain from [the averaged proof](joint-operator-average.md) and [the reflection identity](joint-reflection-correlation.md). In particular,

    D_N={odd n: floor(sqrt(N))+1<=n<=N-floor(sqrt(N))-1},
    L_N=|D_N|,
    T_N=sum_(n in D_N) f_N(n)*e_N(N-n),
    U_N=sum f_N(n),       V_N=sum e_N(n),
    m_N=f_N(N/2)*e_N(N/2),
    R_N=T_N-U_N*V_N/L_N,
    2*S(N)=T_N+m_N.

The midpoint is interpreted as zero when N/2 is outside the odd domain, and is uniformly bounded. The constants c_F,c_E and kappa=c_F*c_E>0 have already been proved to exist. Write

    A_X=3*X^2/[4*log(X)^2].

Thus sum_(X<N<=2X, N even) S(N)~kappa*A_X, while

    sum_(X<N<=2X, N even) N/log(N)^2 ~ A_X.

Let M be a fixed odd squarefree positive integer. M=1 is allowed. Set

    rho_M(a)=#{b mod M: gcd(b,M)=gcd(a-b,M)=1},
    K_M(a)=M*rho_M(a)/phi(M)^2.

Here rho_1=K_1=1. By the Chinese remainder theorem,

    rho_M(a)=product_(p|M) [p-1 if p|a, otherwise p-2],
    K_M(a)=product_(p|M, p|a) p/(p-1)
             *product_(p|M, p does not divide a) p*(p-2)/(p-1)^2.       (1)

These factors count the admissible reflected residue pairs; they do not assume that the remaining arithmetic is independent. Also,

    sum_(a mod M) rho_M(a)=phi(M)^2,
    (1/M)*sum_(a mod M) K_M(a)=1.                             (2)

The first equality counts all ordered pairs of reduced residues by their sum.

## 2. Equidistribution of the single-member weights

For each fixed reduced residue b modulo M and each fixed u>0, the frozen weights used in the averaged proof satisfy

    sum_(n<=uX, n=b mod M) F_X(n)
        =[u*c_F/phi(M)+o_M(1)]*X/log(X),
    sum_(n<=uX, n=b mod M) E_X(n)
        =[u*c_E/phi(M)+o_M(1)]*X/log(X).                    (3)

For nonreduced classes both sums are zero once X^(1/5) exceeds every prime divisor of M. The weights at n=1 are set to zero, as in the original averaged proof.

The additional established input is the prime number theorem in arithmetic progressions:

    pi(t;M,c)=[1/phi(M)+o_M(1)]*t/log(t),   gcd(c,M)=1,

for fixed M. One source for the statement and its fixed-modulus qualification is [Tao's exposition of the prime number theorem in arithmetic progressions](https://terrytao.wordpress.com/2009/09/24/the-prime-number-theorem-in-arithmetic-progressions-and-dueling-conspiracies/). This is a stronger input than the ordinary PNT, although no varying-modulus result is used here.

To obtain (3), repeat the factor-simplex argument separately for every positive factor-type measure. After fixing the first k-1 factors of a squarefree rough integer, write their product as d. Every factor is larger than X^(1/5), so d is invertible modulo fixed M for sufficiently large X. The last prime is required to lie in the single reduced class b*d^(-1) modulo M. On the interior of the exponent simplex, its upper limit is at least a fixed positive power of X, so the PNT in progressions inserts exactly the factor 1/phi(M) into the last-prime count. Its error is uniform over the finitely many reduced residue classes. The first k-1 factors need no residue restriction.

The earlier upper estimates handle the boundaries of factor-type regions and the small-n region unchanged. Repeated prime factors, the frozen five-factor boundary, and all moving-cutoff strips still have negligible total weight; restricting a set to one residue class cannot enlarge its absolute error. Thus each positive type measure has the same limiting density as before divided by phi(M). Their finite linear combinations give (3). This also supplies bounded total variation and justifies products of the resulting signed measures.

Taking the fixed-parameter version at scale N, with the actual thresholds N^(1/5) and N^(1/3), yields on D_N

    U_(N,b):=sum_(n in D_N, n=b mod M) f_N(n)
        =[c_F/phi(M)+o_M(1)]*N/log(N),
    V_(N,b):=sum_(n in D_N, n=b mod M) e_N(n)
        =[c_E/phi(M)+o_M(1)]*N/log(N)                     (4)

for reduced b. Removing the endpoints costs O(sqrt(N)) positions and does not alter these leading terms. Since M is fixed, all statements may be taken uniformly over its finitely many residue classes.

## 3. Averaging the operator within one target residue class

For every a modulo M,

    sum_(X<N<=2X, N even, N=a mod M) S(N)
       =[kappa*rho_M(a)/phi(M)^2+o_M(1)]*A_X.              (5)

Proof: in the half-pair region 0<r<=s, X<r+s<=2X, sum the product measures from (3) over all reduced residue pairs (b,c) with b+c=a modulo M. There are rho_M(a) such pairs. Each contributes density c_F*c_E/phi(M)^2 over a region of area 3/4 after division by X. The symmetrized F/E operator has the same limiting coefficient. The original proof's diagonal, lower endpoint, and moving-cutoff estimates remain valid after this residue restriction. All sufficiently large rough summands are odd, so their targets are automatically even; there is no further parity factor.

Equivalently, the ratio of the restricted sum in (5) to the unrestricted sum tends to rho_M(a)/phi(M)^2. The even targets themselves are equally distributed among the M classes, but their operator mass is generally not.

Combining (5) with U_N*V_N/L_N=[2*kappa+o(1)]N/log(N)^2 and the bounded midpoint gives

    sum_(X<N<=2X, N even, N=a mod M) R_N
       =[2*kappa*(rho_M(a)/phi(M)^2-1/M)+o_M(1)]*A_X
       =[2*kappa*(K_M(a)-1)/M+o_M(1)]*A_X.                (6)

For the baseline term, the elementary count of even integers in a fixed class gives

    sum_(X<N<=2X, N even, N=a mod M) N/log(N)^2
        =[1/M+o_M(1)]*A_X.

All target progressions are infinite because M is odd. Equation (6) explains how the signed unrestricted average of R_N can be zero to leading order while different congruence classes have persistent biases.

## 4. The modulo-three obstruction to an uncorrected absolute-error target

For M=3,

    rho_3(0)=2,      rho_3(1)=rho_3(2)=1,
    K_3(0)=3/2,     K_3(1)=K_3(2)=3/4.

Therefore the fractions of the total asymptotic S-mass in the target classes 0,1,2 modulo 3 are respectively 1/2,1/4,1/4. Formula (6) gives

    sum_(X<N<=2X, N even, 3|N) R_N
        =[kappa/3+o(1)]*A_X,
    sum_(X<N<=2X, N even, 3 does not divide N) R_N
        =[-kappa/3+o(1)]*A_X.                             (7)

Applying the triangle inequality to these two disjoint classes proves

    liminf_(X->infinity)
      [sum_(X<N<=2X, N even) |R_N|]/A_X >= 2*kappa/3,

or equivalently

    liminf_(X->infinity)
      [log(X)^2/X^2]*sum_(X<N<=2X, N even) |R_N| >= kappa/2>0.       (8)

In particular, sum |R_N|=o(X^2/log(X)^2) is false for this uncorrected remainder. Also each of its positive and negative parts has dyadic total at least [kappa/3-o(1)]A_X. These statements are compatible with S(N)>0 everywhere: the systematic negative bias is a shift of the positive expected baseline, not a proof of a negative operator value.

## 5. Exact projection onto residue classes

For any fixed N and odd M, partition D_N into

    D_(N,b)={n in D_N: n=b mod M},       L_(N,b)=|D_(N,b)|.

Reflection maps D_(N,b) bijectively onto D_(N,N-b), so

    L_(N,b)=L_(N,N-b).                                    (9)

For nonempty classes define the class means

    fbar_(N,b)=U_(N,b)/L_(N,b),
    ebar_(N,b)=V_(N,b)/L_(N,b).

Set terms from empty classes to zero. Define the projected baseline and residual by

    B_(N,M)=sum_(b mod M, L_(N,b)>0)
                    U_(N,b)*V_(N,N-b)/L_(N,b),

    R_(N,M)=sum_(n in D_N)
              [f_N(n)-fbar_(N,n mod M)]
              *[e_N(N-n)-ebar_(N,N-n mod M)].

Expansion gives the exact identities

    T_N=B_(N,M)+R_(N,M),
    2*S(N)=B_(N,M)+R_(N,M)+m_N.                           (10)

The two cross terms vanish because the centered values sum to zero within every class and reflection matches the class sizes. This is an algebraic orthogonal projection identity; it needs no probabilistic independence assumption. For M=1 it recovers B_(N,1)=U_N*V_N/L_N and R_(N,1)=R_N.

For fixed M, once its prime divisors lie inside the wheel, the nonreduced classes have zero weights. Also L_(N,b)=N/(2M)+O_M(sqrt(N)+1), with relative error tending to zero. Applying (4) to the rho_M(N) admissible reduced pairs gives

    B_(N,M)=[2*kappa*K_M(N)+o_M(1)]*N/log(N)^2.            (11)

Because M is fixed, this holds uniformly as N ranges over even integers. In particular, the baseline is eventually positive, but it need not have that sign in an arbitrary small finite example where some U_(N,b) can be negative.

The conditional averages of the new residual vanish to leading order within every class already included in the projection:

    sum_(X<N<=2X, N even, N=a mod M) R_(N,M)
        =o_M(X^2/log(X)^2).                               (12)

This follows by subtracting (11) from twice (5), using (10) and the bounded midpoint. It is still signed cancellation, and it is still only a fixed-modulus theorem.

## 6. Fixed-modulus Cauchy--Schwarz still loses a logarithm

Write

    A_(N,b)=sum_(n in D_(N,b)) f_N(n)^2-U_(N,b)^2/L_(N,b),
    C_(N,b)=sum_(n in D_(N,b)) e_N(n)^2-V_(N,b)^2/L_(N,b),

with empty classes contributing zero. Global Cauchy--Schwarz gives

    R_(N,M)>=-sqrt[(sum_b A_(N,b))*(sum_b C_(N,b))].        (13)

A class-by-class use gives the potentially sharper estimate

    R_(N,M)>=-sum_(b mod M) sqrt[A_(N,b)*C_(N,N-b)].         (14)

Both resulting lower bounds for S(N) are eventually negative when M is fixed.

To see this, each prime in a reduced class and in D_N has f=e=1. The PNT in progressions supplies [1/phi(M)+o_M(1)]N/log(N) such primes in each reduced class. By (4), each mean-square subtraction U_(N,b)^2/L_(N,b), and likewise for V, is O_M(N/log(N)^2). Consequently,

    A_(N,b), C_(N,b)
       >=[1/phi(M)+o_M(1)]*N/log(N)

for every reduced b. The square-root error allowance in (13) is therefore at least [1+o_M(1)]N/log(N). The error allowance in (14) is at least

    [rho_M(N)/phi(M)+o_M(1)]*N/log(N).

Every local factor p-2 is positive, so rho_M(N)>=1. Both allowances exceed the baseline (11), which is O_M(N/log(N)^2), by a growing logarithmic factor. The bounded midpoint cannot close this gap. This proves failure of these two particular variance estimates, not negativity of the actual reflected residual or of S(N).

## 7. Scope and next use

The residue factor is an explicitly derived correction to the geometry of reflection: each prime divisor of M changes the number of admissible channels from p-2 to p-1 when it also divides N. The projected operator keeps those channels distinct instead of combining them into one unconditioned mean.

This identifies and removes the bias of every prime included in fixed M. It does not remove the effects of omitted primes, control the new residual in absolute value, or justify taking M to grow with N. The latter would require quantitative uniform distribution estimates beyond the fixed-modulus PNT argument used here. The continued failure of the separate-variance bounds also shows that merely making a fixed partition more detailed cannot supply the missing fixed-target correlation estimate.

The main mathematical gains are the exact correction (10), the local averaged law (5), and the proved obstruction (8). Almost-all and all-target positivity remain unresolved.
