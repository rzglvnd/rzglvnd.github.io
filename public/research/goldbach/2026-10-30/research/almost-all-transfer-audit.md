# Independent audit: moving thresholds and the almost-all reduction

Date: 2026-10-30, Asia/Tehran.

Status: the transfer estimates below are proved. The circle-method comparison is identified separately and its proof obligations are audited explicitly. The ordinary prime number theorem and fixed-residue averaged laws alone do not imply the desired mean square. No all-target Goldbach theorem or novelty claim is made.

## 1. The stronger norm required by the new target

Write L=log(X), z=X^(1/5), and let R_X be the indicator of integers 2<=n<=2X with no prime factor <=z. All arrays in this note are zero outside their specified support. The frozen arrays f_X,e_X use wheel z and late threshold X^(1/3), retaining the exact canonical condition p^2<=n. They vanish at n=1.

The existing first-moment proof only needed a changed support of size o(X/L). For squared convolution errors, that qualitative estimate alone is insufficient. Young's inequality gives

    ||b*R_X||_2^2 <= ||b||_1^2 ||R_X||_2^2.

If b is an indicator supported on o(X/L) positions, the right side is only o(X^3/L^3), whereas the new target is o(X^3/L^4). A quantitative gain is necessary.

## 2. Uniform rough counts and the cutoff-band size

Define Phi_*(t,z)=#{2<=n<=t:P^-(n)>z}. Uniformly for z<=t<=2X,

    Phi_*(t,z) << t/L.                                    (1)

Below z the count is zero. Here is an elementary proof adequate for this application. For sufficiently large X, n<=2X has at most five prime factors greater than z, counted with multiplicity. Fix the number k and the first k-1 prime factors in nondecreasing order, with product m. The last prime is at most t/m and at least z. Chebyshev's prime upper bound gives at most C*t/(m*L) possibilities when t/m>=z. Ignore the remaining ordering restrictions for an upper bound and sum 1/m over the preceding factors. The reciprocal prime sum over (z,2X] is bounded by an absolute constant, by partial summation of Chebyshev's bound, so each k contributes O(t/L). This proof permits repeated factors and has constants uniform in t.

For a in {1/5,1/3}, let B_a consist of members of R_X divisible by a prime in

    X^a < p <= (2X)^a.

After choosing such a p, write n=pm. Either m=1, or m is a rough integer counted by (1). Consequently

    |B_a| <= # {p in this band}
              +C*X/L * sum_(p in band) 1/p
           << X^a/L + X/L^2
           << X/L^2.                                    (2)

Both band prime estimates follow from Chebyshev: the interval is a fixed multiplicative interval near X^a. The m=1 term is essential; omitting it would make the intermediate inequality false for prime n in the band. Let B=B_(1/5) union B_(1/3). Then |B|=O(X/L^2).

For each X<N<=2X, the actual rough support is a subset of R_X. Changes in wheel membership or in the J,D weights occur only on B. The condition p^2<=n does not change when N is frozen, because it depends on n rather than the target N. Both actual and frozen weights are bounded absolutely: the latter have J+D<=5, hence |F|<=4 and |E|<=6. The actual ten-state bounds are smaller.

It follows pointwise in the target that the difference between the actual full convolution and the frozen convolution is bounded by a constant times (B*R_X)(N). This domination handles target-dependent changes without pretending that they come from one fixed signed error array. Since |R_X|=O(X/L),

    sum_(X<N<=2X) |moving convolution - f_X*e_X(N)|^2
       << |B|^2 |R_X|
       << X^3/L^5.                                      (3)

Parity merely restricts the target sum and cannot increase this estimate.

## 3. Endpoint, repeated-factor, and five-factor errors

The reflected interval excludes at most O(sqrt(X)) positions at each end. Let A_X be the indicator of possible small endpoint positions. Another application of Young gives

    ||A_X*R_X||_2^2 << X^2/L=o(X^3/L^4).                  (4)

Thus the actual T_N from the reflection note satisfies

    sum_(X<N<=2X, N even)|T_N-f_X*e_X(N)|^2
       =O(X^3/L^5)+O(X^2/L).                             (5)

The midpoint m_N is bounded, so its total squared contribution is O(X).

Repeated rough prime factors occur on at most

    2X*sum_(m>z)1/m^2=O(X^(4/5))

integers. Their squared convolution error against R_X is therefore O(X^(13/5)/L), again negligible at the target scale.

Frozen five-factor integers are also negligible. Each of their five factors lies between z and 2z, since the other four exceed z. Thus their number is at most pi(2z)^5=O(X/L^5). Their squared convolution error is O(X^3/L^11). Both arguments use bounded weights, not an unsupported assumption that repeated factors or the five-factor boundary have zero effect.

## 4. A precise Fourier comparison sufficient for the frozen problem

Let P_X(n) be the prime indicator on 1<=n<=2X. A sufficient comparison is

    ||hat(f_X-c_F P_X)||_infinity
      +||hat(e_X-c_E P_X)||_infinity
        =O(X*loglog(X)/L^2).                             (6)

The transforms are finite Fourier series on R/Z. The single-side squared norms satisfy ||e_X||_2^2, ||P_X||_2^2=O(X/L). Expanding

    f_X*e_X-kappa P_X*P_X
      =(f_X-c_F P_X)*e_X+c_F P_X*(e_X-c_E P_X)

and applying Parseval proves from (6)

    ||f_X*e_X-kappa P_X*P_X||_2^2
       =O(X^3*(loglog X)^2/L^5)
       =o(X^3/L^4).                                     (7)

This reduction does not assume independence of fixed-sum prime pairs. It requires a genuine uniform Fourier estimate, which is much stronger than the previously proved marginal counts.

## 5. Audit of the proposed route to (6)

The relevant primary source is [Tao, Notes 8](https://terrytao.wordpress.com/2015/03/30/254a-notes-8-the-hardy-littlewood-circle-method-and-vinogradovs-theorem/), especially Theorem 14(ii), Proposition 18 and Exercise 20 for minor arcs, Proposition 24 for the major-arc mechanism, and Exercise 34 for the classical almost-all Goldbach conclusion. These are inputs and templates; none states (6) for the present weights without checking their structure.

After removing the negligible sets in section 3, every weight is a finite linear combination of prime and squarefree three- or four-prime product classes. Semiprime weights vanish. On four factors the weights are F=-3 and E=3 for large X. Every factor is canonical: the largest is at most 2X^(2/5), while the product of the other three exceeds X^(3/5). The nontrivial canonical condition for triples concerns only their largest factor and is p_3<=p_1*p_2. The smaller two automatically satisfy p_i^2<=n. All class constraints are finitely many monomial inequalities, including order, wheel threshold, late threshold, and canonical comparison.

The following details are necessary in a proof of (6), and the stated mechanisms are consistent with the available bounds:

1. Remove n<X/L^D for a sufficiently large fixed D. Its total bounded weight is at most O(X/L^D), harmless even by a crude count. This ensures every retained bilinear block has product size at least X/L^D.
2. Dyadically split prime variables and separate the finite monomial comparisons using a truncated Perron formula. Integer monomial ratios unequal to 1 have polynomially bounded reciprocal separation. Equality cases must be handled with the intended strict/non-strict convention or removed if they force a repeated factor. Truncation at a sufficiently large power of X makes the aggregate error negligible and costs a fixed power of log(X) in the integrated absolute kernel.
3. Group at least one prime into each bilinear variable. Both block sizes exceed a fixed power of X. The grouped coefficients are bounded by a fixed factorial times a bounded Perron modulus; twisting by Perron frequencies does not enlarge their magnitudes. Theorem 14(ii) then forces any large sum into polylogarithmic major arcs. The prime component is treated by Proposition 18/Exercise 20. A sufficiently large major-arc exponent absorbs the finitely many logarithmic losses.
4. On major arcs a/q+beta with q and X|beta| polylogarithmic, use Siegel--Walfisz, not merely the fixed-modulus PNT. First hold all but one prime fixed, with product m. Eventually m is coprime to q. Averaging the final prime over reduced residues gives the coefficient mu(q)/phi(q), independent of m. The exponential phase left afterward is e(beta*n).
5. Replace remaining prime measures by dt/log(t) using ordinary quantitative PNT. A safe justification uses telescoping product measures and Fubini: with all other variables fixed, each variable has finitely many interval sections from the monomial constraints. Summation by parts costs at most a fixed multiple of 1+X|beta|. Reciprocal sums or integrals over the other factors are O(1). Arbitrarily strong logarithmic errors in PNT and Siegel--Walfisz absorb the polylogarithmic losses.
6. Keep the resulting finite-X continuous density v_f(t),v_e(t) until the replacements are finished. For X/L^D<=t<=2X its normalized factor coordinates have boundaries displaced by O(loglog(X)/L), and the integration densities are bounded away from singular coordinate faces. Therefore

       v_f(t)=c_F/log(t)+O(loglog(X)/L^2),
       v_e(t)=c_E/log(t)+O(loglog(X)/L^2).

   These are L1 errors O(X*loglog(X)/L^2), so their Fourier transforms are bounded uniformly in beta. This is the reason no major-arc-volume factor is needed. Replacing the density prematurely and multiplying a weak pointwise error by the whole major-arc measure would not justify (6).

The remaining full circle-method proof should state these steps as lemmas with the appropriate quantified constants. In particular, fixed-AP equidistribution alone must never be substituted for step 4.

## 6. Transferring classical weighted Goldbach to prime indicators

The primary source's almost-all statement uses von Mangoldt weights. There is an elementary norm bridge to the unweighted P_X needed in (7). Put A_X(n)=Lambda(n)/L on n<=2X. Partial summation of a prime upper bound, splitting off n<=sqrt(X) if desired, gives

    ||P_X-A_X||_1=O(X/L^2),
    ||P_X||_2^2, ||A_X||_2^2=O(X/L).                      (8)

For primes, the summand in the first norm is |log(p/X)|/L; the sum is O(X/L^2). Prime powers contribute only O(sqrt(X)*log(X)) before the division by L, which is smaller. Young's inequality then yields

    ||P_X*P_X-A_X*A_X||_2^2=O(X^3/L^5).                  (9)

Exercise 34 gives, for any prescribed positive A, the weighted Goldbach asymptotic with error O_A(X/L^A) outside O_A(X/L^A) exceptional targets. This implies a weighted mean-square error o(X^3): on the exceptional set the crude convolution bound is O(X*L^2). The main term is no larger than O(X*L), since for distinct odd prime divisors p_1<...<p_k,

    product_j (p_j-1)/(p_j-2)
       <=product_(j=1)^k (j+1)/j=k+1=O(log X).

Choose A>4, or increase A further for any desired logarithmic saving. Divide by L^4 to obtain the mean-square statement for A_X*A_X. Finally replace L^2 in the main term by log(N)^2 for X<N<=2X. The change is O(K(N)*X/L^3), whose squared sum is O(X^3/L^6) by the already proved bounded mean square of K.

Consequently the classical input supplies

    sum_(X<N<=2X, N even)
      |P_X*P_X(N)-2K(N)*N/log(N)^2|^2=o(X^3/L^4).        (10)

No new exceptional-set theorem for ordinary prime pairs is being claimed. Its role is to transfer (7), once the Fourier comparison has been established, to the specific operator under study.

## 7. Combined implication and scope

Combining (5), (7), and (10) proves the desired normalized residual estimate provided (6) is established with the detailed steps audited above:

    sum_(X<N<=2X, N even)
      |T_N-2*kappa*K(N)*N/log(N)^2|^2=o(X^3/log(X)^4).

Because K(N)>=1/2 and |m_N|<=9, this implies S(N)>0 for all but o(X) even targets in each dyadic interval. It does not eliminate each individual exceptional target. The finite computations test identities and constants, but cannot replace the Fourier estimates.
