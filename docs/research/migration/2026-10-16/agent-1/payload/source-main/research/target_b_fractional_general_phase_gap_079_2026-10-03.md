# Target B: fractional general-phase gap above 79% grain mass

Date: 2026-10-03
Base main: be7d22b782ca3b426a78d168f86d5a99600ca857
Status: proof-only candidate, noncanonical. Target B and Level I remain open.

This stays off the current four-persistent-bar (2,1,1) stress route and the
high-t Target C collar/local-train-payment route. It works instead in the
boundary-order phase-coarea multi-grain branch.

The purpose is to remove the dominant-component hypothesis from the explicit
general phase interpolation theorem on a concrete fractional range. The result
uses the proof-only coarea/GMC/GPI modules and does not change theorem-state
authority.

## 1. Setup

Fix a phase-coarea grain H with three coherent phase classes

    M >= b >= a,

and put

    t=b/M,   s=a/M,
    Delta=[M(a+b)-E]/M^2,

where E is the retained physical crossing count of H. Let R_* be the total
retained crossing count after the O_eta(D) coarea cut, and let

    Theta=E/R_*.

In the pure-rhombic Target B branch,

    R_*/D^2 -> Delta_2=pi/(2 sqrt(3))=1/c,
    c=2 sqrt(3)/pi.

Hence the fractional identity from the balanced-grain report is

    D^2/M^2
      = c(s+t-Delta)/Theta + o(1).                       (1)

No dominant-grain assumption is used in (1).

The coarea cut has only O_eta(D) physical crossing edges between distinct
components. Thus for a macroscopic H, crossings involving trains outside H are
o(M^2), which is the external-interface hypothesis needed by the local
dual-tree/trimmed-grid estimates.

Throughout the theorem below assume

    Theta >= 0.79
    and
    t >= tau > 0                                             (2)

eventually along the subsequence.

## 2. A fractional largest-pair missing floor

Let x_AB be the number of missing A-B crossings and put

    mu=x_AB/(Mb).

Use the GPI constant

    mu_0=8*10^(-5)

and set

    d_0=4 sqrt(3) (3 sqrt(mu_0)+mu_0).

The local part of GPI does not use dominance until its final global comparison.
If mu<=mu_0, corrected dual-tree extraction plus the trimmed-grid diameter
estimate gives

    D^2/M^2 >= F(s,t)-d_0-o(1),                            (3)

where

    F(s,t)=1+t+t^2-s(1-t)+s^2,        s<(1-t)/2,
    F(s,t)=3(1+t)^2/4,                s>=(1-t)/2.          (4)

On the other hand Delta>=0, so (1) and Theta>=0.79 give

    D^2/M^2 <= c(s+t)/0.79+o(1).                           (5)

We now prove that (3) and (5) are uniformly incompatible.

### Lemma 2.1

For every 0<=s<=t<=1,

    c(s+t)/(F(s,t)-d_0) < 0.79.                            (6)

Proof.

The elementary bounds

    sqrt(3)<1.7321,
    pi>3.14159,
    sqrt(8*10^(-5))<0.008945

give

    c<1.103,
    d_0<0.187.                                             (7)

First suppose s<(1-t)/2. For fixed t, the numerator in (6) increases with s,
while F decreases with s because

    partial F/partial s=-(1-t)+2s<0.

If t<1/3, the allowed maximum is s=t. If t>=1/3, it is the limit
s=(1-t)/2. In both subcases the resulting ratio is at most

    (2c/3)/(4/3-d_0)<0.65<0.79.                           (8)

Now suppose s>=(1-t)/2. Then t>=1/3, (4) is independent of s, and s+t<=2t.
It suffices to prove

    2ct/[3(1+t)^2/4-d_0] < 0.79.                          (9)

Using (7), (9) follows if

    q(t):=
      (3/4)t^2
      +(3/2-2*1.103/0.79)t
      +(3/4-0.187)
    >0.                                                    (10)

The middle coefficient is exactly -1021/790 and the constant is 563/1000.
The minimum of this comparison quadratic over the real line is

    563/1000 - (1021/790)^2/3
      = 116639/18723000
      > 0.006.                                             (11)

Thus (9), and hence (6), holds uniformly. QED.

Equations (3), (5), and Lemma 2.1 contradict mu<=mu_0 for all sufficiently
large terms. Therefore

    liminf mu >= mu_0=8*10^(-5).                           (12)

This is the first point at which the 79% grain fraction is used.

## 3. General fractional phase gap

Write

    e_AB=Mb-x,
    e_AC=Ma-y,
    e_BC=z.

The no-transversal-triangle count used in GPI gives

    M z <= a x+b y.

Consequently

    Delta M^2=x+y-z
      >=(1-s)x+(1-t)y
      >=(1-s)x.                                            (13)

Combining (12) with t>=tau gives

    Delta >= mu_0 tau (1-s)-o(1).                         (14)

Assume for contradiction that along a subsequence

    Delta < 4*10^(-17) tau^2.                             (15)

Then (14) yields

    1-s < 5*10^(-13) tau+o(1)
        <=5*10^(-13)+o(1).                                (16)

The random balanced restriction from GPI now applies unchanged: choose subsets
of A and B of size a and keep the entire C class. Its balanced tripartite
deficit is eventually below 10^(-12). The audited balanced grid extraction and
trimmed-grid estimate, including the trains deleted by the balancing step,
therefore give the same safe lower bound as GPI,

    D^2/a^2 > 2.95.                                       (17)

The coarea external interface contributes only o(a^2) crossings and hence only
the same o(1) term in this estimate, because (16) gives a=(1-o(1))M.

But the exact fractional identity (1) gives

    D^2/a^2
      = c(s+t-Delta)/(Theta s^2)+o(1)
      <= 2c/(0.79 s^2)+o(1).                              (18)

Using c<1.103 and (16), the right side of (18) is below 2.80 for all
sufficiently large terms. This contradicts (17).

Therefore:

### Theorem 3.1 — 79% fractional GPI

For every fixed tau>0, any macroscopic phase-coarea grain satisfying

    Theta>=0.79,
    t>=tau

eventually must obey

    liminf Delta >= 4*10^(-17) tau^2.                     (19)

This is a fixed positive Theorem-51 phase deficit without requiring
Theta->1.

## 4. Concrete low-train corollary

Let H_* be the largest coarea grain and put

    x=T/D.

GMC2 gives, whenever x<2 sqrt(2 Delta_2),

    Theta_* >=
      1/2 [1+sqrt(1-(x^2/(4 Delta_2)-1)^2)]-o(1).        (20)

At x=2.56 the right side is greater than 0.795, so every subsequence with

    x<=2.56                                                (21)

has

    Theta_*>0.79

eventually.

Also no same-phase train pair crosses. Hence

    E_* <= Mb+Ma+ab <=3Mb=3tM^2.                         (22)

Since M<=T<=2.56D and E_*=(Theta_* Delta_2+o(1))D^2,
(22) gives

    t >= 0.79 Delta_2/[3(2.56)^2]-o(1)
      >0.036-o(1).                                        (23)

Applying Theorem 3.1 with tau=0.036 yields

    liminf Delta_*
      >=4*10^(-17)(0.036)^2
      =5.184*10^(-20).                                    (24)

Thus:

### Corollary 4.1

Every surviving phase-coarea decomposition with

    limsup T/D <=2.56

has a largest grain with a fixed positive general-phase extremal deficit,

    liminf Delta_* >=5.184*10^(-20).                      (25)

The number is intentionally conservative. Its role is qualitative: the
dominant-component hypothesis in GPI is no longer needed throughout this
nontrivial low-train interval.

For reference, solving the GMC2 equation Theta=0.79 gives the larger numerical
endpoint 2.56567..., but 2.56 is used above so the proof keeps visible slack.

## 5. Scope and remaining bottleneck

This is proof-only. No numerical search or verifier result is used as a proof
premise. The displayed decimals are certified by the elementary inequalities
in Section 2 and direct substitution in the explicit GMC2 formula.

The result does not close Target B. A fixed positive internal phase deficit can
still be absorbed by the residual coarea grains and by the global virtual-area
budget.

The remaining step on this route is quantitative transfer: convert the largest
grain's forced Delta_* into either

1. enough additional train population to contradict T/D<=2.56;
2. enough PC3/MCP penetration cost to exceed the global rhombus budget; or
3. enough cross-grain virtual determinant mass to violate the zonotope allowance.

The useful reduction is that, below T/D=2.56, the largest grain can no longer
approach a Theorem-51 extremizer through arbitrary three-phase interpolation.
