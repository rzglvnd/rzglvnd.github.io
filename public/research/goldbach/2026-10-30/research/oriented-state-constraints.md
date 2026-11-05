# Oriented states: rigorous size restrictions and reflection

Date: 2026-10-26, Asia/Tehran. Status: proved necessary constraints for the oriented moment experiment, with a finite audit of optional stronger constraints. These are safe supersets of arithmetic states, not assertions that every permitted state is realized.

## Population and hypothesis

Let N be even, y=floor(N^(1/3)), z=floor(sqrt(N)), and 2<=w<=y. For wheel survivors r in [z+1,N/2], write s=N-r. Assume every prime divisor of N belongs to the wheel Q=product_(p<=w) p. Then gcd(r,s)=1: a common prime divisor would divide N and hence Q, contradicting wheel survival.

Let J_L,J_R count distinct omitted primes w<ell<=y dividing r,s respectively. Let D_L,D_R count distinct primes p>y dividing the indicated member n and satisfying p^2<=n. Consequently J=J_L+J_R and D=D_L+D_R, with no factor shared across the two sides.

Put P_j equal to the product of the j smallest omitted primes, with P_0=1. Let q_1<q_2<... be the primes above y and L_d=product_(i<=d) q_i, with L_0=1.

## Safe single-member constraints

Every member is less than N, so it has at most two distinct prime divisors above N^(1/3). Thus 0<=D_L,D_R<=2.

If D_side=2, its two counted primes p<q leave a nontrivial cofactor a=n/(pq): otherwise n=pq<q^2. Also a<N^(1/3), so a has a prime divisor at most y. Wheel survival puts that divisor in the omitted-prime set. Therefore D_side=2 implies J_side>=1.

For a side with state (j,d), the distinct selected factors divide n, and the largest selected late prime is at least q_d. Hence the following lower bound is necessary:

    n >= m(j,d) = max(P_j*L_d, q_d^2)       if d>=1,
    n >= m(j,0) = P_j.

Define m(0,2)=N+1 to encode the impossible state. This is precisely the `min_size` restriction in `experiments/oriented_joint_moments.py`.

At N=1,000,000, w=7, the first omitted primes are 11,13,17,19,... and the first late primes are 101,103,107,109. The simple bounds already give:

- j<=4 on either side, because 11*13*17*19*23=1,062,347>N.
- d=1 implies j<=3, because 11*13*17*19*101=4,665,089>N.
- d=2 implies j=1, because j=0 is impossible and 11*13*101*103=1,487,629>N.

## Endpoints and the coupled product budget

For a proposed quadruple (j_L,j_R,d_L,d_R), put

    A=max(z+1,m(j_L,d_L)),
    B=max(N/2,m(j_R,d_R)).

An actual pair must have r>=A and s>=B, hence A+B<=N. This one test also enforces r<=N/2 and s<=N-z-1 when combined with the specified interval. If it passes, every possible r lies at most

    r_max=min(N/2,N-B).

All selected small and late primes across the two sides are distinct. Their product divides r*s, giving

    P_(j_L+j_R)*L_(d_L+d_R) <= r*(N-r)
                               <= r_max*(N-r_max).

The final inequality follows because t*(N-t) increases on [0,N/2]. Also j_L+j_R cannot exceed the number of omitted primes. These observations justify all exclusions made by `safe_states`. No state frequency or primality histogram is used to choose this superset.

For the benchmark, the implementation retains 99 states.

## Optional refinements: proved, but no extra benchmark exclusion

The canonical condition p^2<=n sometimes improves a crude product lower bound. At the benchmark, state (j,d)=(1,1) implies n>=101*11^2=12,221. To prove it, write n=p*m with p>=101 counted and m>=p. The unique omitted prime ell divides m. If m has no late prime factor, m=ell^a with a>=2 since ell<=97<101, so m>=121. If m has a late prime factor, m>=11*101>121. Therefore n>=101*121. The example n=11^2*101 attains this bound as a standalone member.

At (j,d)=(1,2), necessarily n=ell*p*q with a single omitted prime ell and two distinct late primes p,q. Indeed, an additional prime factor above y would exceed N, while any second omitted-prime factor, even another copy of ell, would force n>=11^2*101*103=1,258,763>N. Thus ell<=47 on the left (ell*101*103<=500,000) and ell<=89 on the right (ell*101*103<=998,999). These prime-identity constraints do not shrink the count-only state space here.

A further safe test allocates the globally smallest j_L+j_R omitted primes and d_L+d_R late primes into two groups of the required sizes. Keep a state only if at least one allocation has product lower bounds within both side caps and with sum at most N. This test is necessary: sort the actual distinct primes globally and replace the kth smallest by the kth smallest available prime, retaining its side assignment. Both products weakly decrease. It must not be claimed sufficient for arithmetic realization.

A finite enumeration of these allocations, also imposing the stronger 12,221 minimum, leaves the same 99 benchmark states. Therefore these optional refinements were not added to `safe_states`; they would add code without improving this certificate.

## Reflection and bounded factor geometry

Reflection r -> N-r swaps (J_L,D_L) and (J_R,D_R). On the chosen half interval it does not imply equal oriented moments: reflection maps to the other half, and the two members have different size ranges. Retaining left/right labels therefore preserves information that the aggregate state (J,D) discards.

Normalized factor lengths log(p)/log(N) give a bounded bookkeeping geometry: the sum of selected factor lengths on a side is at most log(n)/log(N), and the two sides share the constraint n_left+n_right=N. The product budget above is an exact integer version of this statement, requiring no numerical logarithms. Reflection exchanges the two factor budgets. This provides a concrete use for bounded coordinates without claiming that a coordinate change removes the original arithmetic difficulty.

The orientation experiment evaluates whether this retained information improves a finite certificate. Neither the 99-state superset nor a successful finite certificate supplies a uniform Goldbach theorem.
