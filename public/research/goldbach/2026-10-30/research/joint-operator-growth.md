# Growing-cutoff joint operator: exact reductions and a sharp restriction

Date: 2026-10-27, Asia/Tehran.

Status: proved operator identities, a uniform exceptional-set estimate, and a counterexample to weakening this particular operator's cutoff. Uniform positivity of the operator sum is not established. No novelty claim is made.

## Setup

For an even target N>=6, work on I=[floor(sqrt(N))+1,N/2]. Put y=floor(N^(1/3)). Choose an integer cutoff w with floor(N^(1/5))<=w<=y, and let W_w contain the candidates r for which neither r nor N-r has a prime factor <=w.

For a member n, define

    J_w(n)=#{prime p: w<p<=y, p|n},
    D(n)=#{prime p>y: p|n, p^2<=n},
    F=1-J-D,       H=binom(J,2)+J*D,       E=F+H.

The joint score is

    q_w(r) = [F(r)*E(N-r)+E(r)*F(N-r)]/2.

Write S_w(N)=sum_(r in W_w) q_w(r), and let C(N) be the restricted prime-pair count. The previously proved ten-state argument gives q_w<=1_(both members prime), so C(N)>=S_w(N).

This pointwise statement is valid for arbitrary targets; the shared-divisor cases do not require a new operator. The older CRT implementation needed a coprimality assumption, which is an implementation restriction, not a hypothesis of the operator proof.

## 1. Increasing the cutoff raises the bound — proved

For w<=v<=y, W_v is a subset of W_w. A surviving candidate has no prime factor in (w,v], so its J count, D count, and score are unchanged. A removed candidate has a factor <=y on at least one member. Since both members exceed sqrt(N)>y, that member is composite. Its score is therefore nonpositive by the pointwise theorem.

Consequently

    S_v(N)-S_w(N) = -sum_(r in W_w minus W_v)q_w(r) >=0.       (1)

At v=y, J=0 on every survivor. Each member is prime or semiprime, D is its composite indicator, and H=0. Thus q_y equals the prime-pair indicator exactly, and

    S_w(N) <= S_v(N) <= S_y(N)=C(N).                          (2)

This is an ordering theorem for the bounds. It does not show that the starting value S_w is positive, and reaching the exact endpoint does not avoid the prime-detection work involved in evaluating it.

There is an exact accounting of the loss by the smallest prime factor of either member. For a starting cutoff w, let

    L_p(N)=-sum q_w(r),

where the sum is over r in W_w with min(P^-(r),P^-(N-r))=p. For w<p<=y, each L_p>=0, and

    C(N)-S_w(N)=sum_(w<p<=y)L_p(N).                          (3)

The finite experiment constructs these losses from divisibility scores and validates the endpoint against prime labels afterward. At N=1,000,000 with w=15 it gives S_w=3274 and total loss 2108, reaching C=5382. At N=999,998 with w=15 it gives S_w=2663 and loss 1528, reaching C=4191.

## 2. An explicit nonnegative penalty identity

On the ten possible single-side states, define P=1_(J=D=0), A=max(J+D-1,0), and B=H-A. Then

    F=P-A,       E=P+B,       0<=B<=A.

The last inequality is precisely A<=H<=2A on composite states; on the prime state A=B=0. Expanding q gives

    q = P_L*P_R
        -[P_L*(A_R-B_R)+(A_L-B_L)*P_R
          +A_L*B_R+B_L*A_R]/2.                              (4)

Every term subtracted is nonnegative. Formula (4) identifies which combinations cause loss. It also shows why the missing estimate remains substantive: the loss involves correlations between prime members and multiply factored members, and between the two composite configurations. Replacing those correlations by a product of marginal densities is not justified for a fixed target.

## 3. Shared prime divisors are a lower-order exceptional set

Let T be the primes dividing N that exceed w. Every p in T exceeds N^(1/5), and |T|<=4, because five such distinct divisors would have product greater than N. A wheel candidate with gcd(r,N-r)>1 has a common prime in T, since gcd(r,N-r)=gcd(r,N).

Writing I=[a,b], L=b-a+1, the exceptional count satisfies the exact union bound

    X_N <= sum_(p in T)(floor(b/p)-floor((a-1)/p))
        <= sum_(p in T)(L/p+1)
        <=4*(L/N^(1/5)+1).                                 (5)

The score lies in [-9,1] on the 100 possible pairs of single-side states. Let S_w^coprime denote the same score sum restricted to gcd(r,N)=1. Therefore

    S_w >= S_w^coprime-9*X_N,
    |S_w-S_w^coprime| <=9*X_N = O(N^(4/5)).                 (6)

This is uniform in the even target. The error is o(N/log(N)^2). Thus a hypothetical uniform lower estimate c*N/log(N)^2 with c>0 for the coprime score would transfer to the full score for all sufficiently large N. No such estimate is established here.

The central pair N/2+N/2, when N/2 is prime, belongs to the exceptional set and has positive score 1; absolute values in (6) cover it. We do not assume every exceptional score is negative.

For example, the direct audit finds exceptional score -13/2 at N=22,000 and -381/2 at N=999,998. Shared factors matter in exact finite counts even though (6) controls their asymptotic size.

## 4. The exponent 1/5 cannot simply be reduced for this operator

The cutoff condition prevents a composite member from having five distinct tail factors. It is essential to the validity of this particular polynomial, not merely a convenience of its proof.

An exact example with the weaker cutoff floor(N^(1/6)) is

    N = 13,357,362,
    r = 6,678,671 = 17*19*23*29*31,
    N-r = 6,678,691, a prime,
    w = 15,     y = 237.

The side states are (J_L,D_L)=(5,0) and (J_R,D_R)=(0,0). The composite side has F=-4,H=10, so

    q = -4+10/2 = 1,

while the prime-pair indicator is 0. Trial division verifies the displayed prime, and all other assertions use exact integer arithmetic. This is a counterexample to the weakened pointwise inequality, not a Goldbach counterexample or a negative total-sum example.

More generally, every fixed exponent 0<alpha<1/5 permits infinitely many such pointwise failures if w=floor(N^alpha). Choose five distinct primes in (t,2t), form r as their product, and choose a prime s in (r,2r). These choices exist for all sufficiently large t by the prime number theorem, as presented in [Tao's multiplicative-number-theory notes](https://terrytao.wordpress.com/2014/12/09/254a-notes-2-complex-analytic-multiplicative-number-theory/). Put N=r+s. Then

    t^5<r<32*t^5,      N<96*t^5.

For large t, N^alpha<t, while all five factors are below N^(1/3). The same states (5,0),(0,0) give q=1 on a non-prime pair. Both numbers are odd, so N is even, and r lies in the required half interval.

Together with the sufficient exponent 1/5 theorem, this establishes a sharp cutoff exponent for universal validity of the unchanged operator. It does not exclude a different polynomial, extra state corrections, or an adaptive cutoff certified by actual prime-product bounds.

## 5. What remains to estimate

The cutoff monotonicity and shared-factor reduction remove two ambiguities. They do not control the signed correlations in (4) for each fixed N. An exact residue identity still has floor remainders, and taking absolute values separately across every channel may destroy the desired lower bound.

This distinction is consistent with established sieve theory: the [linear-sieve theorem](https://terrytao.wordpress.com/2015/01/29/254a-supplement-5-the-linear-sieve-and-chens-theorem-optional/) requires explicit control of remainder sums; it does not turn a positive density expression into an unconditional count. The [Ford–Maynard framework](https://arxiv.org/abs/2407.14368) likewise studies which Type I and Type II information suffices for lower bounds. These are methodological references, not a theorem asserting that our particular operator must fail.

The next useful bound must preserve or explicitly estimate the joint terms in (4). An average over many N is a separate, potentially accessible theorem; it cannot substitute for a uniform fixed-target estimate.

## Reproduction

    python experiments/joint_operator_filtration.py

This saves `research/joint-operator-filtration.json`, including the exact cutoff gains, exceptional-set checks, and weakened-cutoff counterexample. The counting and averaging experiments for this session are saved separately so the earlier benchmark certificates remain unchanged.
