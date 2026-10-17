> Generated reading edition · [exact source](../../../../docs/targets/target-c/108-area-boosted-quantitative-phase-gap-audit.md) · source SHA-256 `173e18cc6ef42720bb9a9f72f0367b6a4c782a9055639cd8778ba9713986eca0`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target C — area-boosted quantitative phase/corridor gap

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**  
**Status:** proved candidate, proof-only pending independent hostile audit/promotion.

Proof-only Section 107 shows that every wrapping carrier with Section-101 scalar slack
`σ<=10^-3` has normalized area above `0.473` and, when locally rhombus-saturated,
contains at least `(0.473-o(1))D^2` strict unit rhombi.  This is much stronger than the
`0.18D^2` conservative count used in the first quantitative phase/corridor estimates.

This section feeds that geometric area rigidity back into the canonical Section-90
inverse-phase extraction.  The larger crossing mass forces much larger phase shores,
which in turn tolerates substantially more Section-101 scalar slack before the
phase/corridor angle contradiction fails.

Define

$$
\sigma(\theta)
:=3\theta-2\pi-\sin(\theta/2)-2\sin\theta.
$$

Let `theta_12` be the unique solution above `theta_8` of

$$
\boxed{\sigma(\theta_{12})=4.5\times10^{-5}.}
$$

The regression certificate gives

$$
\boxed{
\theta_{12}=2.7029176003825130\ldots,
\qquad
\mu_{12}:=\sin(\theta_{12}/2)
=0.9760418064930821\ldots .
}
$$

Thus

$$
\boxed{
\mu_{12}-\mu_8
=1.0412260300\times10^{-6}>0.
}
$$

The improvement is still quantitative rather than a C-II closure, but it is no longer
limited by the old cap-deficit carrier area constant.

---

# 108. Area rigidity raises the explicit carrier coefficient to `0.9760418064`

## 108.1 Contradiction setup

Assume that a full-core Type-II countersequence has every positive-area macroscopic
harmonic-cell limit of normalized diameter at most

$$
\mu_{12}<1.
\tag{108.1}
$$

Canonical Section 103 gives a unique wrapping macroscopic carrier.  Its normalized
angular diameter satisfies

$$
\theta_8\le\theta\le\theta_{12},
\tag{108.2}
$$

because canonical Section 101 excludes wrapping below `theta_8`.

Set

$$
\sigma:=\sigma(\theta)\le4.5\times10^{-5}<10^{-3}.
\tag{108.3}
$$

Proof-only Section 107 therefore applies to this carrier.  Its finite-scale local
rhombic saturation gives

$$
R_D\ge(0.473-o(1))D^2.
\tag{108.4}
$$

For all sufficiently large members of the contradiction sequence we may use the
conservative explicit bound

$$
\boxed{R_D\ge0.472D^2.}
\tag{108.5}
$$

Canonical Sections 68 and 89 still give

$$
\boxed{
T_D\le6D,
\qquad
\sum_R\delta_R<5.317D.
}
\tag{108.6}
$$

## 108.2 Strong inverse-phase shores from the larger rhombus mass

Rerun the local Section-90 extraction on this carrier.

The canonical phase-circle cut deletes only `O(D)` crossing rhombi.  Hence, after
increasing the large-`D` threshold, at least

$$
0.471D^2
\tag{108.7}
$$

crossings remain.

Call a retained crossing good when its angular defect is at most

$$
{K\over D},
\qquad K:=1000.
\tag{108.8}
$$

The total defect bound (108.6) shows that at most

$$
{5.317D\over K/D}
=0.005317D^2
\tag{108.9}
$$

retained crossings are nongood.  Therefore at least

$$
\boxed{0.465683D^2}
\tag{108.10}
$$

good crossings remain.

There are three unordered phase-label pairs.  One fixed pair supports at least

$$
{0.465683\over3}D^2
=0.1552276666\ldots D^2
\tag{108.11}
$$

good crossings.

Use the canonical real reduced-phase coordinates and randomly shift bins of width

$$
W:={20K\over D}={20000\over D}.
\tag{108.12}
$$

A good crossing has endpoint phase difference at most `K/D`, so a random bin boundary
separates its endpoints with probability at most `1/20`.  Some shift therefore leaves
at least

$$
{19\over20}{0.465683\over3}D^2
=0.1474662833\ldots D^2
\tag{108.13}
$$

good crossings internal to common bins.

Let `a_j,b_j` be the two fixed-label shore sizes in bin `j`.  Since both shores are
subsets of the full local train set,

$$
\sum_ja_j\le6D,
\qquad
\sum_jb_j\le6D.
\tag{108.14}
$$

Suppose every occupied bin had `a_j<0.012D` or `b_j<0.012D`.  Bins small on the first
shore would carry at most

$$
0.012D\sum_jb_j\le0.072D^2
$$

crossings.  Among the remaining bins, those small on the second shore would carry at
most another `0.072D^2`.  Thus all internal-bin crossings would total at most

$$
0.144D^2,
$$

contradicting (108.13).

Hence one common inverse-diameter phase bin contains two fixed, distinct label
families `A_D,B_D` with

$$
\boxed{|A_D|,|B_D|\ge0.012D.}
\tag{108.15}
$$

The bin width tends to zero, so each family has a limiting projective direction
`u_A,u_B`; distinct labels give

$$
\boxed{
\operatorname{dist}_{RP^1}(u_A,u_B)=\pi/3.
}
\tag{108.16}

Every full local train segment has two distinct physical boundary-end occurrences.
Thus each phase family supplies at least

\[
\boxed{E_0D,\qquad E_0:=0.024}
\tag{108.17}
$$

physical train endpoints.

## 108.3 Principal-route slack remains at most `σ`

For completeness, rederive the sharpened macroscopic-route excess estimate rather than
using Section 105 or 106 as a premise.

For every fixed finite family `J` of positive complement gaps, the exact Section-82
outer-walk identity plus the ordinary two-edge route floor gives, after normalization
and the large-`D` limit,

$$
\sum_{j\in J}\ell_j\le2\alpha.
\tag{108.18}
$$

Exhausting all positive complement components after the scale limit yields

$$
\sum_{j\ge1}\ell_j\le2\alpha.
\tag{108.19}
$$

Every route dominates its endpoint chord `f(g_j)=sin(g_j/2)`.  Canonical Section 101
has

$$
C:=\sum_jf(g_j)\le2\alpha,
\qquad
2\alpha-C\le\sigma.
$$

Therefore

$$
\boxed{
\sum_{j\ge1}(\ell_j-f(g_j))
\le2\alpha-C
\le\sigma.
}
\tag{108.20}
$$

In particular the total path excess of the three principal corridors is at most
`σD+o(D)`.

## 108.4 Endpoint leakage with the larger phase families

The independently audited Section-104 technical companion proves a scale-free leakage
estimate once the canonical scalar/gap stability bounds hold.  Section 107 rederives
those bounds on the larger `σ<=10^-3` window, so they apply here.

For an excess-base cutoff `h>0`, one selected phase family can place at most

$$
L(\sigma,h)D+o(D)
\tag{108.21}
$$

physical endpoints away from the three principal corridors, where

$$
L(\sigma,h)
=w(h)+\left({1\over h}+{169\over6}\right)\sigma,
\tag{108.22}
$$

$$
w(h):={\pi\over3}-\arccos((1+h)/2).
\tag{108.23}
$$

This single formula includes nonquadrilateral-face boundary, nonprincipal macroscopic
corridors, exceptional micro routes, the two small support spans adjacent to the
largest principal gap, bad-base teeth, good-base tangent-window capacity, and tail-gap
chords.

Take

$$
\boxed{h:=0.0088.}
\tag{108.24}
$$

At the maximal slack `σ=4.5e-5`,

$$
w(h)=0.0050881779786\ldots,
\tag{108.25}
$$

and

$$
\boxed{
L(4.5\times10^{-5},0.0088)
=0.0114693143423\ldots .
}
\tag{108.26}
$$

Subtracting from the endpoint supply (108.17), more than

$$
0.01253068D
$$

endpoints of each phase family lie on the union of the three principal corridors.
Pigeonholing gives one principal corridor carrying more than

$$
0.00417689D
$$

endpoints of that family.  Fix the slightly smaller explicit constant

$$
\boxed{\rho:=0.00417.}
\tag{108.27}
$$

## 108.5 Exact projection loss contradicts the corridor geometry

Suppose one principal corridor carries at least `rho D` endpoints from one selected
phase family.  Let `u` be the limiting projective direction of that family, let `q` be
the corridor chord direction, and put

$$
\Delta:=\operatorname{dist}_{RP^1}(u,q).
$$

Orient the corridor route along its chord.  Each selected phase endpoint edge
contributes projection loss at least `1-cos Delta`.  Equation (108.20) bounds the total
normalized path excess of all three principal corridors by `σ`.  Hence

$$
\boxed{\rho(1-\cos\Delta)\le\sigma.}
\tag{108.28}
$$

At `σ=4.5e-5` and `rho=0.00417`, exact inversion gives

$$
\boxed{
\Delta
\le\arccos\left(1-{4.5\times10^{-5}\over0.00417}\right)
=0.1470430677\ldots .
}
\tag{108.29}
$$

Apply this separately to the two selected phase families.  They cannot use the same
principal corridor because their projective directions are exactly `pi/3` apart.
Thus they use two distinct principal corridors, whose projective direction separation
would have to satisfy

$$
\left|
\operatorname{dist}_{RP^1}(q_i,q_j)-{\pi\over3}
\right|
<2\Delta
<0.294087.
\tag{108.30}
$$

On the other hand the canonical Section-101 gap geometry plus the stability estimates
rederived in Section 107 give the Section-104 principal-direction bound

$$
\left|
\operatorname{dist}_{RP^1}(q_i,q_j)-{\pi\over3}
\right|
>
{\theta_8\over2}-{\pi\over3}-{73\over6}\sigma.
\tag{108.31}
$$

At `σ=4.5e-5` the right side equals

$$
\boxed{0.3037089636\ldots .}
\tag{108.32}
$$

Equations (108.30)--(108.32) contradict each other with margin greater than

$$
\boxed{0.00962\text{ radians}.}
\tag{108.33}
$$

## 108.6 Carrier consequence

The contradiction proves that no full-core Type-II countersequence can have every
positive-area macroscopic harmonic-cell limit of normalized diameter at most
`mu_12`.  The canonical finite-macroscopic-cell transfer then yields an actual locally
rhombus-saturated carrier `P_*` of quadratic area with

$$
\boxed{
\operatorname{diam}(P_*)
\ge
(0.9760418064930821\ldots-o(1))D.
}
\tag{108.34}
$$

The gain above the canonical Section-101 coefficient is

$$
1.0412260\times10^{-6},
$$

and comes from a structural area theorem rather than another adjustment of the
cap-deficit pigeonhole constant.

## 108.7 Dependencies and scope

- **Canonical Sections 101 and 103:** wrapping scalar threshold, unique wrapping cell
  under a common cap, and local train/phase budgets.
- **Proof-only Section 107:** exact support-gap area identity and the resulting
  `R_D>=0.472D^2` carrier constant on `σ<=10^-3`.
- **Independently audited Section-104 technical companion:** finite micro-base and
  tangent-window leakage estimates.  Its formulas are reused only after Section 107
  independently re-establishes the required gap-stability hypotheses on the wider
  window.
- **Canonical Sections 68, 69, 82, 89, and 90:** phase defect, physical train ends,
  outer-walk ledger, local train count, and inverse-phase extraction.
- **Sections 105--106:** not logical premises.  The sharp all-macroscopic-route excess
  bound and stronger shore extraction are rederived here.
- **Bridges and contact-isolated source points:** untouched.
- **No theorem-state mutation.** C-II remains open.
