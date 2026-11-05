# Fourier comparison for the frozen joint-operator weights

Date: 2026-10-30, Asia/Tehran.

Status: a reduction using established prime exponential-sum and Siegel--Walfisz estimates, with the factor constraints checked below. The conclusion concerns an averaged convolution of the frozen weights. Applying it to the original moving-cutoff operator requires the separate stability argument. It does not prove uniform Goldbach or claim a new general prime theorem.

## 1. Statement of the comparison

Write L=log X. On integers 1<=n<=2X let f_X and e_X be the frozen weights F_X,E_X from `joint-operator-average.md`, with prime cutoff z=X^(1/5), late cutoff y=X^(1/3), and the canonical condition p^2<=n retained exactly. Set their values at 1 to zero. Define

    lambda_X(n)=Lambda(n)/L * 1_(1<=n<=2X).

The constants c_F,c_E are the factor-simplex constants in the earlier averaged proof; kappa=c_F*c_E>0. We obtain

    sup_theta |sum_n [f_X(n)-c_F*lambda_X(n)]e(theta*n)|
       << X*loglog(X)/log(X)^2,
    sup_theta |sum_n [e_X(n)-c_E*lambda_X(n)]e(theta*n)|
       << X*loglog(X)/log(X)^2.                           (1)

All implied constants are fixed; the thresholds for the estimates can be ineffective because Siegel--Walfisz is used. The bound is needed only as X tends to infinity, so loglog X causes no small-X issue.

The two weights and lambda_X obey

    ||f_X||_2^2+||e_X||_2^2+||lambda_X||_2^2 << X/L.       (2)

For the first two, weights are bounded and supported on z-rough integers, whose count is O(X/L). For lambda_X use Lambda(n)^2<=log(2X)*Lambda(n) and the PNT upper bound. Parseval, (1), and (2) imply

    sum_N |(f_X*e_X)(N)-kappa*(lambda_X*lambda_X)(N)|^2
       << X^3*(loglog X)^2/log(X)^5
       =o(X^3/log(X)^4).                                 (3)

Indeed the difference is (f_X-c_F*lambda_X)*e_X+c_F*lambda_X*(e_X-c_E*lambda_X). Bound each convolution in l2 by the supremum of one Fourier factor times the l2 norm of the other, and then square the triangle inequality. The sum in (3) can be over all integers, not just even targets.

The rest of the note verifies (1), rather than assuming a general theorem for an unspecified class of almost-prime weights.

## 2. Established analytic inputs

The primary reference is [Tao, Notes 8: The Hardy--Littlewood circle method and Vinogradov's theorem](https://terrytao.wordpress.com/2015/03/30/254a-notes-8-the-hardy-littlewood-circle-method-and-vinogradovs-theorem/).

* **Theorem 14(ii):** for arbitrary l2 coefficient sequences on [1,M] and [1,N], a bilinear exponential sum restricted by mn in an interval can be large only when one side is small or the frequency has a small-denominator rational approximation. More specifically, exceeding delta*(MN)^(1/2)*||a||_2*||b||_2 forces either min(M,N)<<delta^(-4), or q<<delta^(-2) with ||q*theta||<<delta^(-4)/(MN).
* **Proposition 18, and Exercise 20 by partial summation:** prime exponential sums on intervals have arbitrarily strong logarithmic savings away from rational frequencies with logarithmically bounded denominator and logarithmically small scaled distance.
* **Proposition 24:** near theta=a/q+beta, the von Mangoldt sum has main term mu(q)/phi(q) times the integral of e(beta*t), with an arbitrarily strong logarithmic error after allowing fixed powers of log X for q and X*|beta|. Its proof uses Siegel--Walfisz, stated in Notes 2.
* **Exercise 34:** the classical binary prime convolution has a singular-series asymptotic outside an exceptional set smaller than X/log(X)^A for every fixed A. It is for the von Mangoldt weights used there. It does not directly assert the same theorem for our F/E weights; (1)-(3) are the additional transfer argument.

Only bounded powers of log X occur in the moduli and phases here. The much weaker fixed-modulus PNT from the preceding session would not justify these steps.

## 3. A bounded number of prime factors and separable constraints

An integer <=2X whose prime factors all exceed z has at most five prime factors, counted with multiplicity, for sufficiently large X. Numbers with a repeated prime factor have total count

    <=2X*sum_(m>z)1/m^2 << X^(4/5).                      (4)

Their weights are bounded, so deleting them changes every exponential sum by O(X^(4/5)). It is permissible to insert or delete repeated tuples again during an intermediate decomposition at the same cost: each such number has at most 5! ordered factorizations of the relevant kind.

For squarefree n with k factors, use ordered tuples p_1,...,p_k of primes >z, dividing the resulting symmetric sum by k!. There is no ordering restriction between the tuple coordinates. Put

    j_i=1_(p_i<=y),
    d_i=1_(p_i>y)*1_(p_i^2<=p_1...p_k),
    J=sum_i j_i,       D=sum_i d_i.

The expansions

    F=1-J-D,
    E=1-J-D+sum_(i<j)j_i*j_j+sum_(i,j)j_i*d_j             (5)

are finite linear combinations with absolute coefficients bounded in terms of k<=5. Each term contains either no canonical condition or exactly one canonical condition. The term j_i*d_i vanishes because its two prime ranges are disjoint.

For a term containing d_j, group m=p_j and n=product_(i!=j)p_i. The only coupled condition besides the product range is m<=n, since p_j^2<=mn is equivalent to p_j<=n. All requirements p_i>z or p_i<=y or p_i>y are restrictions on individual prime coordinates. The coefficient of n sums at most (k-1)! tuples, so its absolute value is bounded independently of X. For terms without d_j, choose any coordinate as m. The case k=1 is the ordinary prime sum, up to its small initial segment.

This expansion avoids assuming that primality of the factors is independent, and avoids silently treating the canonical late-divisor condition as a one-variable cutoff at sqrt(X).

## 4. Minor arcs

Fix a large absolute D, for example D=20, and remove n<X/L^D temporarily. Its absolute weight is O(X/L^D). Separate the remaining prime-product sums into dyadic ranges of their individual factors; there are O(L^5) boxes. In a nonempty box the product of the factor-range endpoints is between a fixed multiple of X/L^D and a fixed multiple of X. Grouping one prime against the remaining factors gives ranges with

    min(M,N) >= c*X^(1/5),
    X/L^D << MN << X.                                   (6)

If a canonical condition m<=n is present, separate it by truncated Perron integration. On distinct squarefree tuples m=n is impossible. Otherwise m,n are positive integers of size at most a fixed multiple of X, and |log(n/m)|>>1/X. The standard truncated formula with c=1/L and height T=X^H, for a fixed sufficiently large H, expresses 1_(m<n) as an integral of (n/m)^(c+it)/(c+it), with a total error O(X^(-2)) after summing all tuples. Its kernel has L1 norm O(L). The real factors (n/m)^c are bounded because both m,n lie between fixed powers of X; the imaginary powers have modulus 1 and are absorbed into the separate coefficient sequences. Repeated tuples may be added to the separated sums and removed again by (4).

For clarity, the truncation remainder for a nonunit ratio v is O(v^c/(T*|log v|)); on these ranges v^c is bounded. Taking H sufficiently large handles the O(X) integer products and their bounded factorization multiplicities. Thus no unbounded-frequency norm loss has been suppressed.

The l2 coefficient norms in each separated bilinear sum are O(sqrt(M)) and O(sqrt(N)). Apply Theorem 14(ii) with delta=L^(-C), where C is a fixed sufficiently large constant. The alternative min(M,N)<<delta^(-4) is impossible for large X by (6). Therefore a large such sum forces

    q << L^(2C),       ||q*theta|| << L^(4C+D)/X.

Choose a fixed B larger than all these powers, including the harmless dyadic and Perron losses, and define

    major arcs = {theta: some 1<=q<=L^B has ||q*theta||<=L^B/X}.

Outside these arcs the composite contribution is O(X/L^4), after making C large enough. The prime contribution has the same bound by Proposition 18 and partial summation; the discarded initial segment and (4) are smaller. Thus

    sup_(minor arcs) (|hat f_X|+|hat e_X|+|hat lambda_X|)
       << X/L^4.                                        (7)

Only this fixed logarithmic saving is needed. There is no appeal to a power-saving assertion for an arbitrary arithmetic sequence.

## 5. Major arcs and an exact continuous density

On a major arc choose a reduced fraction a/q with q<=L^B and theta=a/q+beta, |beta|<=L^B/X. For large X all factors p>z are coprime to q.

Consider any term of (5), in a dyadic prime box and with product in [X/L^D,2X]. Fix all but one prime. Its permitted set is a finite union of intervals (indeed an interval for each conjunction): product inequalities and the condition p_j^2<=product give lower or upper monomial bounds for that remaining variable. Apply Siegel--Walfisz in each reduced residue class to this last-prime sum, followed by partial summation for e(beta*m*p). Summing the rational phase over its reduced residues gives

    sum_(b mod q, gcd(b,q)=1) e(a*m*b/q)=mu(q),

because gcd(m,q)=1. The resulting main factor is mu(q)/phi(q), independently of the fixed remaining primes.

Replace each of those remaining prime sums in turn by its integral dt/log t using the ordinary PNT with its arbitrarily strong logarithmic error. The rational phase has already disappeared. These replacements yield

    hat f_X(a/q+beta)
       =mu(q)/phi(q) * integral_0^(2X) v_F,X(t)e(beta*t)dt
         +O_A(X/L^A),                                   (8)

and likewise for e_X, apart from the harmless O(X/L^D)+O(X^(4/5)) initial and repeated-factor contributions if D is kept fixed. It is enough to take A and D larger than 4 throughout.

Here v_F,X is the density obtained by replacing every prime variable in the symmetric factor integrals by dt/log t, retaining the exact rough, late, canonical, and product conditions, and summing with the same coefficients as (5). It is not replaced prematurely by c_F/log X.

The error bookkeeping in this iteration is as follows. On each dyadic box all variables are >=X^(1/5). Every interval endpoint is a minimum or maximum of finitely many monomials in the fixed variables. The exponents are fixed and bounded, and the nonempty box has total product O(X). As one variable moves over its dyadic range, the variation of an integrated section is bounded by a fixed constant times its section-size bound, multiplied by 1+X*|beta|. Differentiating a monomial endpoint gives a fixed multiple of that endpoint divided by the moving variable; differentiating the phase gives the same factor times X*|beta|. Min/max endpoints split into only finitely many pieces. Integrating previously replaced variables preserves this variation bound by the triangle inequality. Consequently partial summation incurs only fixed powers of L, from q, X*|beta|, and O(L^5) boxes. Siegel--Walfisz and the ordinary PNT supply any fixed logarithmic power needed to absorb them. No interval shorter than a dyadic factor range needs its own short-interval prime theorem: interval errors are differences of the uniform cumulative prime-counting errors.

This argument is also valid for the symmetric five-factor boundary terms; their total mass is treated separately below. The endpoint t=1 is assigned zero.

## 6. Comparing the continuous density with c_F/log X

For t>=X/L^D, put s_i=log(p_i)/log t. On the product surface product p_i=t, their sum is 1. The lower and late thresholds become

    alpha(t)=log z/log t=1/5+O(loglog X/L),
    beta(t)=log y/log t=1/3+O(loglog X/L),

whereas the canonical boundary is exactly s_i<=1/2. Changing variables in the continuous product integral gives

    v_F,X(t)=C_F(alpha(t),beta(t))/log t,                  (9)

with C_F the same finite weighted exponent-simplex integral as in the earlier work, now at the displayed thresholds. The corresponding formula holds for E.

All exponent coordinates lie above, say, 1/6 for sufficiently large X. The reciprocal-product density and its derivatives are bounded on this compact region. The weights are bounded and change only across finitely many hyperplanes. Moving a threshold by h changes the simplex integral by O(|h|): the changed region is contained in a finite union of strips of volume O(|h|). The contribution of the five-factor simplex, which appears only when alpha is slightly below 1/5, satisfies the same bound (in fact it is smaller, of fourth order in the width). Hence

    C_F(alpha(t),beta(t))=c_F+O(loglog X/L),
    C_E(alpha(t),beta(t))=c_E+O(loglog X/L).

Since log t=L+O(loglog X),

    v_F,X(t)=c_F/L+O(loglog X/L^2),
    v_E,X(t)=c_E/L+O(loglog X/L^2)                        (10)

uniformly on [X/L^D,2X]. The omitted origin has total continuous mass O(X/L^(D+1)). Indeed on its supported range t>=z, the same product-density formula has all exponent coordinates >=1/6, at most five factors, and bounded weights. Its simplex integral is uniformly bounded, and 1/log t<=5/L; below z the density vanishes. The constant comparison density also has origin mass O(X/L^(D+1)). Thus

    integral_0^(2X) |v_F,X(t)-c_F/L|dt
       << X*loglog X/L^2,                                (11)

and similarly for E. The prime class supplies density 1/log t on t>z; its small omitted interval obeys the same bound.

Proposition 24 gives the major-arc expression for lambda_X with density 1/L. Subtract it from (8), use |mu(q)/phi(q)|<=1, and bound the remaining Fourier integral by (11). This proves (1) on the major arcs. The minor-arc estimate (7) proves it on their complement.

The use of an L1 bound on the exact continuous density is important: replacing it by its limiting constant inside a rough partial-summation estimate can introduce unnecessary powers of the major-arc width. Inequality (11) is uniform in beta without any such factor.

## 7. Passing the classical prime result through the comparison

Let K(N)=C_2*product_(p|N,p>2)(p-1)/(p-2), as in the preceding checkpoint. The classical binary convolution result in Exercise 34 implies

    sum_(X<N<=2X, even N)
      |(lambda_X*lambda_X)(N)-2*K(N)*N/log(N)^2|^2
        =o(X^3/log(X)^4).                               (12)

For precision, first take the weighted theorem with ambient range 2X: outside O_A(X/L^A) targets it gives (Lambda*Lambda)(N)=2K(N)N+O_A(X/L^A). On exceptional targets use the elementary bound |Lambda*Lambda|<=2X*log(2X)^2 and K(N)<<L^2, the latter following from the finite Euler product or the crude divisor bound. Choosing A large enough makes their squared contribution negligible after division by L^4. On the other targets the arbitrary-log error does the same. Finally replace L^2 by log(N)^2 in the main term; their relative difference is O(1/L) uniformly on the dyadic interval, and the already proved sum_(dyadic even N)K(N)^2=O(X) controls the squared error.

Combining (3) and (12) yields the frozen convolution theorem

    sum_(X<N<=2X, even N)
      |(f_X*e_X)(N)-2*kappa*K(N)*N/log(N)^2|^2
        =o(X^3/log(X)^4).                               (13)

The passage from (13) to the original target-dependent weights is a distinct step, documented by the root agent's moving-threshold stability argument. The endpoint and midpoint corrections must also be included there. The conclusion (13) alone is already beyond a signed first-moment identity, but remains an averaged result and cannot exclude every exceptional target.
