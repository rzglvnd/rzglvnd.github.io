# Bounded residue geometry and the remaining correlation

Date: 2026-10-29, Asia/Tehran.

Status: exact geometric and projection identities, fixed-modulus averaged theorems, and elementary mean-square estimates for the local factors. The final estimate for the arithmetic residual is a proposed target, not a proved result. These constructions use standard CRT, Fourier, and singular-series ideas; no novelty or Goldbach proof is claimed.

## 1. A bounded geometry that changes the distance rule

List the odd primes as p_1=3,p_2=5,..., and represent an integer n by

    iota(n)=(n mod p_1,n mod p_2,...)
       in Omega=product_j Z/p_j Z.

Give Omega the distance

    d(x,y)=sum_(j>=1) 2^(-j) * 1_(x_j != y_j).

This is a bounded metric, with diameter 1. The triangle inequality follows coordinate by coordinate from 1_(x_j!=z_j)<=1_(x_j!=y_j)+1_(y_j!=z_j). Distinct integers have distinct images: a nonzero difference cannot be divisible by every odd prime. Addition is coordinatewise, translation preserves d, and reflection x -> iota(N)-x is an isometry. In particular this distance is not a compressed copy of ordinary line distance.

The space Omega is compact and complete. A diagonal subsequence has all first k coordinates eventually fixed, for every k; agreement on those coordinates bounds distance by 2^(-k). The same observation proves completeness. CRT makes the integer image dense: any prescribed finite collection of residues has an integer representative. The positive and even integers are dense too, since all moduli here are odd.

Thus unbounded integers have an injective bounded representation. No largest integer has been created. For example P_k=p_1...p_k tends to zero in this metric, since d(iota(P_k),iota(0))<=2^(-k), while P_k grows without bound in the ordinary order. The compact completion adds residue configurations, not a single endpoint called infinity. This is a product of prime residue rings; without prime-power coordinates it should not be identified with the full profinite completion of Z.

One can draw the j-th coordinate as exp(2*pi*i*n/p_j). Euler's formula then realizes addition as multiplication on a finite cycle and reflection as a rotation followed by conjugation. This is an equivalent representation of the same residue arithmetic. Pi sets the angular unit; its appearance or disappearance in that notation does not remove the divisibility constraints.

## 2. The projection operator respects Goldbach reflection

Use the odd interval D_N and f_N,e_N from [the reflection note](joint-reflection-correlation.md). Their inner product is the unnormalized sum on D_N. Let J_N h(n)=h(N-n).

For an odd squarefree M, let P_M replace a function by its mean on each nonempty residue class of D_N modulo M. It is an orthogonal projection. Reflection bijects class a with class N-a, so their sizes agree exactly and

    P_M J_N = J_N P_M.

Writing U_a=sum_(n=a mod M)f_N(n), V_a similarly, and L_a for class size gives

    T_N=<f_N,J_N e_N>
       =B_(N,M)+R_(N,M),
    B_(N,M)=sum_(a:L_a>0) U_a V_(N-a)/L_a,
    R_(N,M)=<(1-P_M)f_N,J_N(1-P_M)e_N>,
    2S(N)=B_(N,M)+R_(N,M)+m_N.                            (1)

These identities are exact, even when M includes primes above the current wheel cutoff. The asymptotic statements below need fixed M and N tending to infinity.

If M divides M', the projections are nested. With Q=P_(M')-P_M,

    B_(N,M')-B_(N,M)=<Qf_N,J_N Qe_N>.                     (2)

The right side has no fixed sign. Increasing the number of local coordinates need not monotonically decrease |R_(N,M)|. Exact examples occur already in the saved experiment: at N=1000, the residual changes from 1187/234 at M=1 to 554/39 at M=3, increasing its absolute value. Both moduli use only primes within the current wheel. At N=10000, the change from M=3 to M=15 also increases the absolute residual. These are counterexamples to a monotone-improvement claim, not to Goldbach or to positivity of S.

## 3. What every fixed set of coordinates explains

Let rho_M(a) count b modulo M with both b and a-b coprime to M, and put

    K_M(a)=M*rho_M(a)/phi(M)^2.

The [fixed-residue proof](local-residue-reflection-proof.md) derives from the prime number theorem in fixed arithmetic progressions

    B_(N,M)=[2*kappa*K_M(N)+o_M(1)]*N/log(N)^2,             (3)
    sum_(X<N<=2X, even N, N=a mod M) S(N)
       =[kappa*rho_M(a)/phi(M)^2+o_M(1)]*A_X,
    A_X=3X^2/(4log(X)^2).                                 (4)

Here kappa is the positive factor-simplex constant from the earlier work. These are proved averaged statements, not fixed-target independence. The error in (3) is uniform over the finitely many residue classes of a fixed M, not over growing M.

CRT gives the exact factorization

    K_M(N)=product_(p|M) k_p(N),
    k_p(N)=p/(p-1)                      if p|N,
           p(p-2)/(p-1)^2              if p does not divide N. (5)

For M=3, K_3 is 3/2 on multiples of 3 and 3/4 otherwise. The earlier parity-only baseline omitted this distinction.

## 4. Every omitted prime leaves a systematic residual

Fix M and an odd prime ell not dividing M. Summing (4) modulo ell gives

    sum_(X<N<=2X, even N, ell|N) T_N
       =[2*kappa/(ell-1)+o(1)]*A_X.

The midpoint sums are O(X) and do not affect this expression. On the same targets, (3), CRT, and the exact mean (1/M)sum_a K_M(a)=1 give

    sum_(X<N<=2X, even N, ell|N) B_(N,M)
       =[2*kappa/ell+o(1)]*A_X.

Subtracting, and then using the zero leading total residual, proves

    sum_(ell|N) R_(N,M)
       =[2*kappa/(ell*(ell-1))+o(1)]*A_X,
    sum_(ell does not divide N) R_(N,M)
       =[-2*kappa/(ell*(ell-1))+o(1)]*A_X.                 (6)

All sums in (6) are over the same dyadic even-target interval. Consequently

    liminf_(X->infinity) log(X)^2/X^2 * sum |R_(N,M)|
       >=3*kappa/(ell*(ell-1))>0.                         (7)

For M=1 and ell=3, this is kappa/2. Thus no fixed finite residue partition makes the residual little-o of the natural total scale in mean absolute value. This does not exclude a useful one-sided bound strong enough for S>0.

The existing score second moment and (3) give sum R_(N,M)^2=O_M(X^3/log(X)^4). The [independent audit](local-residue-reflection-audit.md) combines this with (6) to prove positive proportions of natural-scale negative residuals and of natural-scale positive residuals. A possible fixed threshold is 3*kappa/[8*ell*(ell-1)] times N/log(N)^2, with unspecified positive proportions and onset. Neither sign alone determines the sign of S, which also includes the positive baseline.

## 5. The full local factor has a controlled mean-square tail

Let M_y be the product of odd primes <=y, for integer y>=3. The pointwise limit of (5), at a fixed positive integer N, is

    K(N)=C_2 * product_(p|N,p>2) (p-1)/(p-2),
    C_2=product_(p>2)(1-1/(p-1)^2)>0.                     (8)

This K is half the usual binary Goldbach singular series, because parity is already accounted for in the baseline 2*kappa*N/log(N)^2. The standard singular series appears in [Tao's sieve notes, Exercise 25](https://terrytao.wordpress.com/2015/01/21/254a-notes-4-some-sieve-theory/). Its use as a fixed-target asymptotic is a conjectural extra step; the algebra and mean values below do not assume that step.

Compactness of the residue space does not make this observable bounded: K(N) can grow along targets divisible by more and more small primes. Its controlled mean square, rather than a uniform upper bound, is what is used below.

There is a simple rigorous lower bound:

    C_2 >= product_(m>=2)(1-1/m^2)=1/2,
    K(N)>=C_2>=1/2.                                      (9)

The larger product on the right includes every factor on the left and additional factors in (0,1); its partial products telescope.

Equip Omega from section 1 with the probability law making all prime residues independent and uniform, and call the random product of local factors Z_y. Each local factor has mean 1. Direct calculation gives

    E[k_p^2]=1+1/(p-1)^3,
    D_y=E[Z_y^2]=product_(2<p<=y)(1+1/(p-1)^3).           (10)

The Z_y form a martingale: the conditional expectation of every added factor is 1. The second moments are bounded, since sum_(p>2)1/(p-1)^3 converges. Hence the products converge in mean square to Z_infinity, and

    E[(Z_infinity-Z_y)^2]=D_infinity-D_y.                 (11)

This probabilistic identity also describes natural averages over the actual integers:

    lim_(Y->infinity) (1/Y)sum_(n<=Y) K(n)=1,
    lim_(Y->infinity) (1/Y)sum_(n<=Y) K(n)^2=D_infinity,
    lim_(Y->infinity) (1/Y)sum_(n<=Y)[K(n)-K_(M_y)(n)]^2
       =D_infinity-D_y.                                  (12)

Here is a direct justification, so no uniform distribution of infinitely many residue coordinates is assumed. Write G(n)=K(n)/C_2 as sum_(d|n) a(d), where a is supported on odd squarefree d and a(p)=1/(p-2). Then G(n)^2 has a nonnegative divisor expansion with h(p)=2/(p-2)+1/(p-2)^2. Both sum a(d)/d and sum h(d)/d converge. Interchange the finite averages and divisor sums, and use floor(Y/d)/Y<=1/d for dominated convergence. This proves the first two limits and their Euler products. For the mixed mean of K*K_(M_y), apply the same argument with the finitely many local factors through y retained separately. Its mean is D_y, since each remaining prime factor has mean 1. The finite periodic mean of K_(M_y)^2 is also D_y, giving the third limit. The same limits hold over even integers, because these functions are unchanged on multiplying the argument by 2. Over a dyadic interval their averages have the same limits by subtraction.

An explicit elementary tail estimate is

    0<D_infinity-D_y<3/(2*y^2).                           (13)

Indeed D_y<exp(sum_(m>=2) m^(-3))<=exp(1/4)<4/3. Also

    t_y=sum_(p>y)1/(p-1)^3
       <=1/y^3+1/(2*y^2)<=1/y^2<=1/9.

Thus D_infinity/D_y<=exp(t_y)<=1/(1-t_y), and the excess is <(4/3)*(9/8)/y^2. The experiment computes sharper rational versions without using floating exponentials.

The residue factors also have a Fourier description:

    K_M(N)=sum_(d|M) c_d(N)/phi(d)^2,                     (14)

where c_d(N) is the Ramanujan sum and all d here are squarefree. For a prime, c_p(N)=p-1 if p|N and -1 otherwise, so (14) follows by multiplying 1+c_p(N)/(p-1)^2. This identifies the local correction with explicit finite-cycle frequencies.

## 6. A corrected next target, with the missing estimate explicit

Define the full locally normalized residual by an exact subtraction:

    E_N=T_N-2*kappa*K(N)*N/log(N)^2,
    2S(N)=2*kappa*K(N)*N/log(N)^2+E_N+m_N.                (15)

No assertion that E_N is small is built into this definition. The full factor has the correct mean in every fixed target residue class:

    lim_(Y->infinity) (1/Y)sum_(n<=Y,n=a mod M) K(n)
       =K_M(a)/M.                                       (16)

The same nonnegative divisor argument proves (16): outside M, divisibility by fixed d is independent of the specified residue by CRT, and the convergent divisor series justifies passage to the limit. Combining partial summation, (4), and (16) shows

    sum_(X<N<=2X, even N, N=a mod M) E_N
       =o_M(X^2/log(X)^2).                               (17)

This removes the fixed-residue signed biases from the proposed remainder. It does not prove a small absolute or square mean of E_N.

Equations (3) and (12)-(13) additionally imply

    lim_(y->infinity) limsup_(X->infinity)
      log(X)^2/X^2 * sum_(X<N<=2X, even N)
        |B_(N,M_y)-2*kappa*K(N)*N/log(N)^2| =0.            (18)

For fixed y the error in (3) sums to little-o; Cauchy-Schwarz in the target variable bounds the remaining normalized limsup by 2*kappa*sqrt(D_infinity-D_y). The order of limits is essential. This does not supply a usable uniform rate for a modulus growing with X.

A concrete sufficient next estimate is

    sum_(X<N<=2X, even N) |E_N|^2 = o(X^3/log(X)^4).       (19)

If (19) held, then S(N)>0 for all but o(X) even targets in each large dyadic interval. To verify the implication, use K>=1/2 in (15) and |m_N|<=9. If S(N)<=0, then for large N,

    |E_N| >= (kappa/2)*N/log(N)^2.

Chebyshev's inequality and (19) bound the number of such targets by o(X). This implication is proved; hypothesis (19) is not. Uniform positivity is stronger still. The finite-residue mean-square calculation (13) controls only K, and must not be substituted for the unproved arithmetic estimate (19).

The bounded geometry therefore supplies an exact organization of local effects and a cleaner formulation of the unknown correlation. It does not by itself establish the missing prime-pair correlation estimate.

## Reproduction

    python experiments/local_singular_factor.py
    python experiments/local_residue_reflection.py

The first script verifies finite pair-residue counts, all Ramanujan expansions for M=1,3,15,105, mean and second-moment products, four refinement identities, and rational infinite-product tail enclosures. The second constructs the actual operator arrays and checks the finite projections. Neither experiment is a proof of (19).
