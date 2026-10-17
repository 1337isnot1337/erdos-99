# Target B: coupled phase-sum bootstrap

Date: 2026-10-03
Base main: 7a327e1ad95cd2e9cb035b9b96fb34fd8f12114d
Parent candidate: 142e4e14b1c314fa75ff89b3e68b070a742ec162
Status: proof-only candidate, noncanonical. Target B and Level I remain open.

The parent atomic-coarea note loses information twice: it first minimizes the
local missing-pair floor over all phase shapes, then independently minimizes the
resulting train inefficiency over the phase sum. Those extrema occur at different
phase sums. Keeping the phase sum through both steps gives a stronger
one-dimensional bootstrap and excludes its equality endpoint.

Put

    c = 2 sqrt(3)/pi,
    Delta2 = 1/c,
    x0 = (8/3) sqrt(Delta2).

For a retained coarea grain write M>=b>=a, s=a/M, t=b/M, u=s+t, and
E=(u-Delta)M^2. Let theta be its limiting fraction of retained quadratic
crossings. Current main gives, for A-B missing density m,

    m <= p  =>  D^2/M^2 >= F(s,t)-d(p)-o(1),

where d(p)=4 sqrt(3)(3 sqrt(p)+p), and

    F(s,t)=1+t+t^2-s(1-t)+s^2       if s<(1-t)/2,
           (3/4)(1+t)^2             otherwise.

The fractional identity gives D^2/M^2 <= c u/theta+o(1). Define

    phi(g)=(1/4)(sqrt(9+g/sqrt(3))-3)^2,

so d(phi(g))=g.

## 1. Exact fixed-u optimization

For fixed u=s+t,

    F(s,t) >= Fmin(u),

with equality at s=t=u/2, where

    Fmin(u)=1+(3/4)u^2                    for 0<u<=2/3,
             (3/4)(1+u/2)^2              for 2/3<=u<=2.      (1)

In the first branch, after s=u-t,

    F=t^2-ut+2t+u^2-u+1,

whose t-derivative is 2t-u+2>0. For u<=2/3 the smallest allowed t
is u/2. For u>=2/3 the second branch contains t=u/2 and is increasing
in t; the first-branch boundary t=2u-1 has value 3u^2, no smaller than
the second-branch balanced value exactly for u>=2/3.

Let

    theta_c = 2c/3,
    G_theta(u)=Fmin(u)-c u/theta,
    p_theta(u)=phi(G_theta(u)).                              (2)

For theta>theta_c, the parent identity Q(0)=theta_c implies G_theta(u)>0.
The local trimmed-grid implication therefore yields

    liminf m >= p_theta(u).                                  (3)

Indeed, if m were below p_theta(u), choose p strictly between them. Then
d(p)<G_theta(u), so the local lower bound exceeds c u/theta by fixed
positive slack, contradicting the fractional upper bound.

## 2. Coupled component inefficiency

The no-transversal-triangle inequality gives

    Delta >= m t(1-s)-o(1).

At fixed u and s<=t,

    t(1-s) >= u(2-u)/4,                                     (4)

again with equality at s=t=u/2. Hence

    Delta >= p_theta(u) u(2-u)/4-o(1).

Since V=M(1+u),

    V >= 2 k_theta(u) sqrt(E)-o(D),

where

    k_theta(u)
      =(1+u)/(2 sqrt(u-p_theta(u)u(2-u)/4)).                 (5)

Define

    K(theta)=inf_{0<u<=2} k_theta(u).                        (6)

Then every such grain obeys V>=2K(theta)sqrt(E)-o(D).
Also K(theta)>1, K is continuous and nondecreasing, and K(theta)<=3/(2sqrt(2)).
Near theta=1 it is strictly increasing: p_theta(u) strictly increases with
theta for every u<2, while evaluating (5) at u=1 gives K(theta)<1.001;
therefore a minimizer is not u=2.

## 3. Stronger atomic bootstrap

The parent shrinking-bin atomic inequality gives, with lambda=(T/D)/x0,

    Theta >= C(lambda)
          =(1+sqrt(1-(lambda^2-1)^2))/2.                    (7)

Use factor K(C(lambda)) for that grain and ordinary Mantel for all other
macroscopic grains. The Section-39 atomic mass cap gives

    lambda >= K(C(lambda)) sqrt(Theta)+sqrt(1-Theta).        (8)

For 1<=lambda<=1.001, C(lambda)>0.99 and K(C(lambda))<1.001. Hence the
right side of (8) is at least K(C(lambda)); thus

    lambda >= K(C(lambda)).                                  (9)

The right side is continuous and strictly decreasing. It is >1 at lambda=1
and <1.001 at lambda=1.001. Therefore there is a unique lambda_dagger in
(1,1.001) satisfying

    lambda_dagger = K(C(lambda_dagger)).                    (10)

Consequently every sufficiently large pure-rhombic-disk Target-B survivor has

    liminf T/D >= x0 lambda_dagger.                          (11)

A high-precision evaluation of the exact formulas gives, only as numerical
evidence,

    lambda_dagger = 1.0000971539092626683156691413955...
    C(lambda_dagger)=0.9999999905602007793046496339514...
    u_min=1.0003593086996963130865665541189...
    x0 lambda_dagger=2.5397475407359602232590308102258....

## 4. The endpoint is unattainable

Suppose a survivor sequence had lambda -> lambda_dagger and pass to a
subsequence with largest-grain fraction Theta -> z. Then z>=C(lambda_dagger).
Using the actual factor K(z), the limiting atomic budget gives

    lambda_dagger >= H(z):=K(z)sqrt(z)+sqrt(1-z).            (12)

For z<1, strict monotonicity gives K(z)>=K(C(lambda_dagger))=lambda_dagger,
and because z>0.99,

    lambda_dagger sqrt(z)+sqrt(1-z) > lambda_dagger.

For z=1,

    H(1)=K(1)>K(C(lambda_dagger))=lambda_dagger.

Thus (12) is impossible. Therefore the endpoint in (11) cannot be approached.
Equivalently there is an absolute, presently non-explicit epsilon_cpl>0 such that

    liminf T/D >= x0 (lambda_dagger+epsilon_cpl)             (13)

throughout this pure-rhombic-disk branch.

This is theorem/proof work. The decimal values above are computational
evaluation only; no verifier or CI result is a proof premise.

## Remaining bottleneck

The improvement is still a train-ratio statement, not the Target-B shell/Oler
closure inequality. The next step is to quantify epsilon_cpl or convert the
forced strictness in one of (3), (4), (8), or the Section-39 atomic budget into
physical shell, penetration, or boundary-chain currency.
