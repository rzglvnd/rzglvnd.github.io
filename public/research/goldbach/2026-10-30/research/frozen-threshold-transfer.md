# Moving thresholds are negligible in the required mean square

Date: 2026-10-30, Asia/Tehran.

Status: proved quantitative reduction using elementary prime upper bounds and the discrete Young inequality; exact finite checks are separate. This result does not by itself bound the frozen convolution's arithmetic error.

## Statement

For X large, define z=X^(1/5), v=X^(1/3). Let f_X,e_X be the existing F,E weights on integers 2<=n<=2X with no prime factor <=z, using J=#{z<p<=v:p|n} and the unchanged canonical condition D=#{p>v:p|n,p^2<=n}. Set both weights to zero elsewhere, including at 1. Thresholds can equivalently be floored because divisors are integers.

For even N in (X,2X], let T_N be the moving-threshold convolution restricted to the odd interval floor(sqrt(N))+1<=n<=N-floor(sqrt(N))-1, as in the earlier notes. Then

    sum_(X<N<=2X, even N) |T_N-(f_X*e_X)(N)|^2
       =O(X^3/log(X)^5).                                  (1)

In particular, any o(X^3/log(X)^4) mean-square asymptotic for the frozen convolution transfers to T_N. No fixed-target error assertion follows from (1).

## 1. A uniform rough-number upper bound

Let R_X={2<=n<=2X:P^-(n)>z}, and let Phi_*(t,z) count its members <=t, excluding 1. For t<z it is zero. For z<=t<=2X,

    Phi_*(t,z) <= C*t/log(X),       |R_X|=O(X/log(X)).      (2)

To prove this without a lower-bound sieve, every such n has at most five prime factors counted with multiplicity, once X>32, since z^6>2X. Order its factors and fix the first k-1, with product m. If a last factor is possible, its upper limit U=t/m satisfies U>=z, so the elementary prime upper bound pi(U)<=C U/log(U) gives at most C' t/(m log(X)) choices. Removing ordering and product restrictions on the first k-1 factors only increases this upper bound. Their reciprocal sum is at most

    [sum_(z<p<=2X)1/p]^(k-1)=O(1).

The last estimate follows either from Mertens' theorem or from partial summation of pi(u)<=C u/log u, because log(2X)/log z is bounded. Summing k=1,...,5 proves (2). Repeated prime factors cause no difficulty for this upper count.

## 2. Only O(X/log squared X) members can change with N

Let B_X be the subset of R_X with a prime factor in at least one of

    (X^(1/5),(2X)^(1/5)],
    (X^(1/3),(2X)^(1/3)].

For either alpha=1/5 or 1/3, the number of possible prime factors in its band is O(X^alpha/log X), and the sum of their reciprocals is O(1/log X). For each such prime p, writing n=pm leaves either m=1 or an integer counted by Phi_*(2X/p,z). Thus (2) gives

    |B_X| <= sum_(p in the two bands)[1+C X/(p log X)]
            =O(X/log(X)^2).                              (3)

On R_X outside B_X, the actual weights at every N in (X,2X] equal the frozen weights. The canonical test p^2<=n depends on the member n, so it does not move with N; only the dividing threshold between J and D changes. The moving rough support is always a subset of R_X.

All the relevant weights have absolute value <=6. Indeed J+D<=5 on frozen rough members, and

    F=1-J-D,
    E=1-J-D+J(J-1)/2+JD.

For nonnegative J,D with J+D<=5, the largest E is 6 and its smallest possible value is at least -4; F lies between -4 and 1. The actual weights have an even smaller factor budget. This bound does not use the stronger pointwise minorant theorem on the actual support.

## 3. Dominating the moving error by a fixed convolution

Let b=1_(B_X), r=1_(R_X), and let h=1_(R_X intersect [2,sqrt(2X)]). Extend the moving weights by zero outside [2,2X], without the square-root endpoint restriction for a moment.

Product subtraction and the absolute bound 6 give, for every N in (X,2X],

    |full moving convolution(N)-f_X*e_X(N)|
       <=4*6^2*(b*r)(N).

Removing pairs with either summand <=sqrt(N) costs at most 2*6^2*(h*r)(N). All weights are supported on odd integers once z>=2, so this also gives the exact odd-domain T_N. With d=1_(B_X union supp(h)), we have the convenient common bound

    |T_N-f_X*e_X(N)| <=4*6^2*(d*r)(N).                    (4)

The discrete Young inequality follows directly by applying the triangle inequality to the sum of translated copies of r:

    ||d*r||_2 <= ||d||_1 ||r||_2.

Therefore, using (2)-(3) and |supp(h)|<=sqrt(2X),

    sum |T_N-f_X*e_X(N)|^2
       <=16*6^4*|supp(d)|^2*|R_X|
       =O((X/log(X)^2+sqrt(X))^2*X/log(X))
       =O(X^3/log(X)^5).

The norm on the right is over all integer convolution coefficients, so restricting the left to the dyadic even targets is legitimate. This proves (1). The proof handles the target-dependent weights by a fixed nonnegative dominating convolution, avoiding an unjustified interchange of target-dependent sequences and Fourier transforms.

## 4. Removing repeated factors and the frozen fifth-factor boundary

Let bad_X comprise rough n<=2X with a repeated prime factor or with five prime factors. The repeated-factor count is O(X^(4/5)), since each is divisible by p^2 with p>z. If there are five factors, every factor is <=2z, since the other four exceed z. Consequently that count is at most pi(2z)^5=O(X/log(X)^5). Thus

    |bad_X|=O(X^(4/5)+X/log(X)^5).                        (5)

Replacing f_X,e_X by their restrictions to squarefree integers with at most four factors changes their Fourier transforms uniformly by O(|bad_X|), hence by O_A(X/log(X)^A) for any fixed A<=5 (the five-factor term controls this particular bound). For convolution transfer, Young gives squared error

    O(|bad_X|^2*X/log(X))
      =O(X^(13/5)/log(X)+X^3/log(X)^11)
      =o(X^3/log(X)^4).                                  (6)

One should not claim arbitrary logarithmic Fourier savings merely from discarding the five-factor set. Keeping its factor-product representation, or using only the O(X/log(X)^5) error actually needed, resolves that distinction.

## 5. Exact finite audit

The standard-library [experiment](../experiments/frozen_threshold_transfer.py) uses the already verified exact scores, reconstructs T_N including the midpoint correction, and computes the frozen convolution with carry-free integer multiplication. It checks (4) at every target in five bands and checks the finite Young bound with exact integers. The stored [results](frozen-threshold-transfer.json) include the source hash.

| X | Threshold-band support size | Exact sum of squared moving/frozen differences |
|---:|---:|---:|
| 1,000 | 61 | 7,876 |
| 10,000 | 961 | 14,735,902 |
| 50,000 | 1,664 | 24,937,895 |
| 100,000 | 5,808 | 6,052,866,368 |
| 125,000 | 7,861 | 18,095,548,034 |

Finite jumps reflect the discrete threshold crossings. These values verify the construction and support domination; they neither establish the asymptotic bound by extrapolation nor give a numerical value for its implied constant. The proof is sections 1-3.

Reproduce with:

    python experiments/frozen_threshold_transfer.py
