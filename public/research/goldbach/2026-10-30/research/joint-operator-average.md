# A positive averaged limit for the joint operator

Date: 2026-10-27, Asia/Tehran.

Status: an averaged asymptotic derived from the prime number theorem, with an exact sign certificate for its leading constant. The decimal constant is numerical quadrature, not a rigorous decimal enclosure. No fixed-target independence assumption, uniform positivity theorem, or proof of Goldbach is asserted. No novelty claim is made.

## 1. Statement

For each even N>=6, set

    w_N=floor(N^(1/5)),     y_N=floor(N^(1/3)),
    I_N={floor(sqrt(N))+1,...,N/2}.

Retain r in I_N when both n=r and n=N-r have no prime factor <=w_N. On a retained member define

    J_N(n)=#{prime p: w_N<p<=y_N, p|n},
    D_N(n)=#{prime p>y_N: p|n and p^2<=n},
    F_N(n)=1-J_N(n)-D_N(n),
    H_N(n)=binom(J_N(n),2)+J_N(n)*D_N(n),
    E_N(n)=F_N(n)+H_N(n).

The operator and its sum are

    q_N(r)=[F_N(r)*E_N(N-r)+E_N(r)*F_N(N-r)]/2,
    S(N)=sum_(retained r in I_N) q_N(r).

The earlier pointwise proof gives S(N)<=C(N), where C(N) counts prime pairs in I_N. Put

    A_X=3*X^2/[4*log(X)^2].

**Theorem.** There are explicitly defined constants c_F,c_E such that

    sum_(X<N<=2X, N even) S(N) = [c_F*c_E+o(1)]*A_X,          (1)

and

    c_F>29/300,     c_E>=1.

In particular the coefficient kappa=c_F*c_E is strictly positive. An independently certified upper bound also gives 29/300<kappa<3/10. Numerical evaluation of the defining integrals gives

    c_F approximately 0.2303352296596,
    c_E approximately 1.2341468111331,
    kappa approximately 0.2842674891760.

Also, by the prime number theorem applied to the two-dimensional pair region,

    sum_(X<N<=2X, N even) C(N) ~ A_X,
    sum S(N) / sum C(N) -> kappa.                            (2)

Thus the operator retains a positive fraction of the prime-pair total on average in a large dyadic interval. Equations (1)-(2) do not prove S(N)>0 for every N, or for almost every N. They give no explicit onset for positivity of the dyadic sum.

## 2. The prime-factor counting lemma used below

Fix alpha=1/5. A squarefree integer with k prime factors is written in increasing order as

    n=p_1*...*p_k,       p_1<...<p_k.

For factors exceeding X^alpha and n on the scale of X, set t_i=log(p_i)/log(X). The limiting ordered exponent simplex is

    Delta_k={alpha<t_1<=...<=t_k, t_1+...+t_k=1}.

Integration on Delta_k means ordinary integration in t_1,...,t_(k-1), with t_k=1-sum_(i<k)t_i; it is not Euclidean surface measure. For a region R of this simplex whose boundary has measure zero, define

    C_k(R)=integral_R dt_1...dt_(k-1)/(t_1*...*t_k).           (3)

For every fixed u>0, the prime number theorem and partial summation give

    #{n<=uX: n squarefree, all p_i>X^alpha,
              k factors, normalized exponent type in R}
       = [u*C_k(R)+o(1)]*X/log(X),                          (4)

where boundaries may be perturbed by O(1/log(X)) without changing the coefficient. For k=1 the coefficient is 1. The phrase "exponent type in R" can be implemented by the inequalities defining R on the actual exponents; their sum is log(n)/log(X), tending to 1 in the part contributing to the leading term.

Here is a direct derivation of the lemma, to specify the input and the boundary control. Fix the first k-1 primes and put m=p_1*...*p_(k-1), U=uX/m. The final prime is at most U and greater than the preceding prime and X^alpha. Away from the faces where log(U)/log(X) equals alpha or the preceding exponent, both lower restrictions are negligible relative to U. The prime number theorem applies uniformly because U is at least a fixed positive power of X. The number of possible last primes is consequently

    [1+o(1)]*uX/[m*log(uX/m)].

For a fixed small delta>0, primes below U*X^(-delta) contribute at most O(X^(-delta)) of this upper estimate, uniformly on the interior. Hence the final exponent may be replaced by log(U)/log(X), and then by 1-sum_(i<k)t_i, with vanishing error away from the type boundaries.

The logarithmic prime measures obey

    sum_(X^a<p<=X^b) 1/p -> log(b/a)

for fixed 0<a<b. This is a standard partial-summation consequence of the prime number theorem. Applying its product version to the first k-1 primes turns the displayed sum into (3), with the last denominator supplied by log(uX/m)/log(X).

Boundary neighborhoods are controlled by the same upper estimate. For all U>=X^alpha, the prime upper bound gives pi(U)<=K*U/log(X), with K depending only on alpha. The reciprocal sums over the other primes are bounded on the compact exponent domain [alpha,1]^k. The normalized upper bound for a boundary neighborhood therefore tends to at most a constant times its exponent-domain volume, which tends to zero as the neighborhood shrinks. The density in (3) is bounded because every t_i>=alpha. This justifies passage from interior boxes to the stated regions and to bounded piecewise constant weights. Equal-prime diagonals can be omitted using the repeated-factor estimate below.

This argument uses one-variable prime counts only. The same PNT reduction to finite prime-factor integrals appears in [Tao's linear-sieve notes, Exercise 6 and the surrounding prime-product calculation](https://terrytao.wordpress.com/2015/01/29/254a-supplement-5-the-linear-sieve-and-chens-theorem-optional/). The [Buchstab discussion in Supplement 4](https://terrytao.wordpress.com/2015/01/04/254a-supplement-4-probabilistic-models-and-heuristics-for-the-primes-optional/) gives another route to the unweighted rough-number case. Neither source supplies independence for fixed-sum prime pairs, and no such assertion is used here.

## 3. Single-member weight constants

First freeze the thresholds at X^(1/5) and X^(1/3). Let F_X and E_X be the corresponding weights on X^(1/5)-rough integers n<=2X, retaining the canonical condition p^2<=n in D. Put both weights equal to zero outside the rough set, and at n=1.

Several negligible exceptions can be removed before computing the leading constants.

* A rough n with a repeated prime factor is divisible by p^2 for some p>X^(1/5). The number of such integers n<=2X is at most

      2X*sum_(m>X^(1/5))1/m^2 = O(X^(4/5))

  and hence is o(X/log(X)).
* Frozen rough integers may have five prime factors, even though the actual N-dependent cutoff permits at most four below N. If five factors exceed X^(1/5) and their product is <=2X, each factor is <=2*X^(1/5). Their number is therefore at most pi(2*X^(1/5))^5=O(X/log(X)^5), again negligible. Six factors are impossible for large X.
* On any interval epsilon*X<=n<=2X with fixed epsilon>0, the exponent of sqrt(n) is 1/2+O_epsilon(1/log(X)). Thus replacing the canonical boundary by t=1/2 changes only a shrinking exponent strip. The lemma shows that strip has o(X/log(X)) members. The same argument applies to type boundaries t=1/3 and t=1/5.

The weights remain absolutely bounded on all these frozen rough integers: J+D is at most the number of prime factors, at most five, so F,H,E have bounds independent of X. Discarding the preceding exceptions is therefore also negligible for weighted counts.

For the remaining squarefree bulk integers, the weights are determined as follows. Endpoint equalities have zero limiting measure and may be assigned either value.

| Number of factors | Exponent condition, in increasing order | (J,D) | F | E |
|---:|---|:---:|---:|---:|
| 1 | prime | (0,0) | 1 | 1 |
| 2 | either location of the smaller factor relative to 1/3 | (1,0) or (0,1) | 0 | 0 |
| 3 | t_3>1/2 | (2,0) | -1 | 0 |
| 3 | t_3<1/2 and t_2>1/3 | (1,2) | -2 | 0 |
| 3 | t_3<1/2 and t_2<1/3 | (2,1) | -2 | 1 |
| 4 | either location of the largest factor relative to 1/3 | (4,0) or (3,1) | -3 | 3 |

For example, three factors with largest exponent >1/2 have the other two exponents below 3/10, hence both are tail factors and no late factor is canonical. If all three exponents are below 1/2, all three factors are canonical or tail, and the number exceeding 1/3 is one or two. Four exponents exceeding 1/5 all lie below 2/5, and at most one can exceed 1/3; this gives the last row.

Define

    C_3 = C_3(Delta_3),
    B_3 = C_3({t_3<1/2}),
    R_3 = C_3({t_3<1/2, t_2<1/3}),
    C_4 = C_4(Delta_4).

The table and (4) give the constants

    c_F = 1-C_3-B_3-3*C_4,
    c_E = 1+R_3+3*C_4.                                     (5)

In particular the second late canonical factor on the (1,2) triple state is counted. Replacing D there by a single composite indicator would change c_F and would not describe this operator.

For every fixed u>0,

    sum_(n<=uX) F_X(n) = [u*c_F+o(1)]*X/log(X),
    sum_(n<=uX) E_X(n) = [u*c_E+o(1)]*X/log(X).              (6)

To justify including n close to zero in these statements, first work on epsilon*X<=n<=uX. The unweighted version of (4), summed over k, gives

    #{n<=epsilon*X: P^-(n)>X^(1/5)}
      = [epsilon*(1+log(4)+C_3+C_4)+o(1)]*X/log(X).

The bounded weights make the limsup contribution from this region O(epsilon). Let epsilon tend to zero after X tends to infinity. This also proves that the normalized absolute-value measures have no mass escaping to the origin and have uniformly bounded total variation.

## 4. Exact positivity of the constants

The complete symmetric-simplex integral has the equivalent form

    C_k = 1/(k-1)! * integral_(u_i>=1/5, sum u_i<=4/5)
                              du_1...du_(k-1)/(u_1*...*u_(k-1)).   (7)

Indeed, in the symmetric integral with all k denominator factors, use sum t_i=1 and symmetry to replace their reciprocal product by k copies with one denominator omitted, then divide by k! to pass to the ordered simplex.

For k=3, integrating one variable and rescaling gives

    C_3=(1/2)*integral_1^3 log(4-t)/t dt.                    (8)

The integrand is positive and decreasing on [1,3]. The saved standard-library certificate uses a 256-cell left Riemann sum. Each logarithm is bounded above by the finite rational atanh series plus its explicit geometric tail:

    log(x)=2*sum_(j>=0) z^(2j+1)/(2j+1),
    z=(x-1)/(x+1),
    remainder after m terms <=2*z^(2m+1)/[(2m+1)*(1-z^2)].

It proves, with exact rational arithmetic,

    C_3 <= 3765350825490954197/9223372036854775808 <41/100.

For C_4, the domain in (7), after shifting the three variables by 1/5, has volume (1/5)^3/6. Its integrand is at most 125, and its prefactor is 1/6. Consequently

    C_4 <= (1/6)*125*((1/5)^3/6) =1/36.

Since 0<=B_3<=C_3 and R_3>=0, (5) yields

    c_F >=1-2*C_3-3*C_4
         >1-2*(41/100)-3*(1/36)=29/300>0,
    c_E >=1.

The sign of kappa is thus independent of the decimal quadrature. The values printed in `joint-operator-average-constants.json` for B_3, R_3, C_4 and the more precise coefficient are numerical estimates of the defining integrals, with a resolution comparison rather than an interval-arithmetic error certificate.

There is also an exact upper certificate, proved in [the independent constant audit](joint-average-constant-audit.md). Outward-rounded rational rectangle sums give C_3>405/1000, B_3>318/1000 and R_3<191/1000. AM-GM in (7) gives C_4>=3/256. If a=1-C_3-B_3, b=1+R_3 and c=C_4, then kappa=(a-3c)*(b+3c), and its derivative with respect to c is 3*(a-b-6c)<=0. Using the already proved positivity of the first factor yields

    kappa < (1-405/1000-318/1000-9/256)
             *(1+191/1000+9/256)
          =303655143/1024000000 <3/10.                       (9)

These strict bounds use exact rational enclosures, not the decimal estimates.

## 5. From single-member measures to an average over targets

On [0,2], form the signed measures

    mu_F,X=(log(X)/X)*sum_n F_X(n)*delta_(n/X),
    mu_E,X=(log(X)/X)*sum_n E_X(n)*delta_(n/X).

Equation (6), together with the absolute-value control just proved, gives

    mu_F,X -> c_F*Lebesgue measure,
    mu_E,X -> c_E*Lebesgue measure.

More explicitly, each is a finite linear combination of the positive type-counting measures in the preceding table, plus an error whose total variation tends to zero. Thus products converge, and integration over regions with boundary of area zero is justified separately for those positive components. This avoids applying a positive-measure portmanteau statement directly to an arbitrary signed sequence.

Use the half-pair region

    D={(a,b): 0<a<=b, 1<a+b<=2}.

Its area is

    (1/2)*[(2^2/2)-(1^2/2)]=3/4.

Both product integrals mu_F,X tensor mu_E,X and mu_E,X tensor mu_F,X therefore tend to (3/4)*c_F*c_E on D. Their half-sum is exactly the frozen-threshold operator sum over all unordered pairs whose sum belongs to (X,2X]. Restoring the normalization gives the right side of (1).

This step counts all pairs in a two-dimensional region. It does not assert that F(r) and E(N-r), or primality of the two members, are independent when N is fixed.

## 6. Moving thresholds, parity, and the lower endpoint

The actual threshold depends on N=r+s. For X<N<=2X it lies in the fixed bands

    X^(1/5) <= N^(1/5) <= 2^(1/5)*X^(1/5),
    X^(1/3) <= N^(1/3) <= 2^(1/3)*X^(1/3).

A frozen rough integer can change its membership or its J,D weights only if it has a prime factor in one of those bands. These correspond to exponent strips of width O(1/log(X)) around 1/5 or 1/3. The number B_X of such frozen rough integers <=2X is o(X/log(X)). To see this without assuming a uniform version of (4), contain each shrinking strip in a fixed delta-neighborhood, apply (4), and then let delta tend to zero. The limiting densities are bounded and the relevant hyperplanes have zero measure. Repeated factors and the frozen five-factor boundary were already shown negligible. The k=1 prime class has limiting exponent 1, so it gives no extra atom on either threshold hyperplane.

The number R_X of possible frozen rough partners is O(X/log(X)). Since the scores are uniformly bounded on the actual and frozen supports, the change in the entire pair sum is at most a constant times

    B_X*R_X=o(X^2/log(X)^2).

This comparison uses a bound for the support of the difference; it does not use monotonicity of signed weights to squeeze them. The canonical condition p^2<=n is unchanged by freezing N, because it depends on the same member n. Its replacement by an exponent boundary was used only to derive the limiting single-member type constants and was handled separately above.

The additional restriction r>sqrt(N) removes at most O(sqrt(X)) possible smaller integers, each with at most R_X possible partners. Its contribution is O(X^(3/2)/log(X))=o(X^2/log(X)^2). The diagonal r=s has O(X/log(X)) rough members and bounded weights, also negligible.

For sufficiently large X, every frozen and actual rough member is odd. Their sums are therefore already even. There is **no additional factor of 1/2 for even targets**. The half-pair region has already handled ordering. Floors cause no further discrepancy: for an integer prime p, p>floor(N^alpha) is equivalent to p>N^alpha.

These observations complete the passage from the frozen product-measure calculation to the actual S(N), proving (1). Replacing the weights by prime indicators gives sum C(N)~A_X by the same PNT/product-measure argument, proving (2).

## 7. Consequences and the unresolved fixed-target question

The proof establishes eventual positivity of each large dyadic total, hence targets with S(N)>0 in every sufficiently large dyadic interval. There is also a weak quantitative consequence. If K_X counts such targets, then S(N)<=C(N)<=pi(X) for X<N<=2X. Discarding nonpositive summands and using the prime number theorem gives

    K_X*pi(X) >= sum S(N),
    liminf_(X->infinity) K_X*log(X)/X >=3*kappa/4>0.

This lower bound has density tending to zero. The first-moment argument here does not establish a positive proportion, almost-all positivity, or positivity at every target. Positive values might compensate negative ones.

The upper constant bound has a different rigorous consequence: every sufficiently large dyadic interval contains some even N with S(N)<(3/10)*C(N). Indeed, the sum of S-(3/10)C is [kappa-3/10+o(1)]*A_X<0. Thus an eventual uniform 30% margin is impossible for this unchanged operator and cutoff rule. This does not disprove the weaker conjecture S(N)>0; it also supplies no explicit first large failure.

The exact finite scan has now been extended through 250,000, separately from the larger selected samples: it finds no nonpositive S(N) in that range. It neither proves (1) nor fills its fixed-target gap. See `joint-average-bands.json` and `experiments/joint_average_bands.py`.

The remaining question is to control how the signed pair correlations concentrate along a single line r+s=N. A subsequent [upper second-moment argument](joint-positive-proportion.md) proves that the operator is positive on a positive proportion of targets. That uses an additional standard sieve theorem, not the first moment alone. Almost-all and uniform positivity remain unresolved. The positive average should therefore be used as a constraint on a proposed model, not as a replacement for the missing uniform lower bound.

## Reproduction

    python experiments/avgconstant_joint_operator.py
    python experiments/joint_average_upper_certificate.py

This reproduces the exact sign certificate and the explicitly labeled numerical quadrature in `research/joint-operator-average-constants.json`. The script certifies the constants; the asymptotic argument is the proof above. The finite checks are separately reproducible with `experiments/joint_operator_stress.py`.
