> Generated reading edition · [exact source](../../../../docs/targets/target-c/104-quantitative-phase-gap-audit.md) · source SHA-256 `efbbf554396bc28a4dd3b790906c2493d15b4140d8bd7d694f3c9392b265af9b`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target C — quantitative phase/corridor gap above the Section-101 threshold

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**  
**Status:** canonical after independent hostile audit and theorem-state audit.44 promotion.

Canonical Section 101 gives the explicit carrier threshold

$$
\mu_8=0.9760407652670519821\ldots
$$

and canonical Section 102 excludes equality, but Section 102 leaves the resulting
strict improvement as an unspecified `epsilon_*>0`.  Canonical Section 103 removes
the main quantitative loss: under a common macroscopic diameter cap, the cap-family
area deficit is carried by one unique wrapping cell, giving that cell area about
`0.2023D^2` near `mu_8`.

This section transports the remaining Section-101 scalar slack through the Section-82
outer ledger and the Section-90 two-phase train core.  Conservative constants suffice
to obtain a fully explicit improvement.

Put

$$
\sigma(\theta)
:=3\theta-2\pi-\sin(\theta/2)-2\sin\theta.
\tag{104.1}
$$

Let `theta_9` be the unique solution of

$$
\boxed{\sigma(\theta_9)=10^{-7}}
\tag{104.2}
$$

above the Section-101 root `theta_8`.  Numerically,

$$
\boxed{
\theta_9
=2.7029080509166894011\ldots,
}
\tag{104.3}
$$

and

$$
\boxed{
\mu_9:=\sin(\theta_9/2)
=0.9760407675809149535\ldots .
}
\tag{104.4}
$$

Thus

$$
\boxed{
\mu_9-\mu_8
=2.3138629714\times10^{-9}>0.
}
\tag{104.5}
$$

The numerical gain is small because the constants below are intentionally crude.  The
point is that the qualitative Section-102 gap can be made explicit with only canonical
or independently audited inputs.

---

# 104. An explicit `2.3e-9` carrier improvement from phase stability

## 104.1 Setup and the scalar slack chain

Assume for contradiction that a Type-II full-core near-disk sequence has no
macroscopic harmonic-cell limit of normalized diameter greater than `mu_9`.  By
canonical Section 83, pass to a finite macroscopic limit family after discarding an
arbitrarily small total area of small cells.

Canonical Section 103 then gives a **unique wrapping macroscopic cell** `P_D` whose
normalized area is at least

$$
\Gamma(\mu_9)-o(1)>0.19.
\tag{104.6}
$$

Its local rhombic filling tends to one by the nonnegative summed Section-83 deficit.
Write

$$
{\operatorname{diam}(P_D)\over D}\to\lambda,
\qquad
\theta:=2\arcsin\lambda,
\tag{104.7}
$$

and let its normalized attachment support converge to a wrapping compact set `S` on
the radius-`1/2` circle.  Canonical Section 101 gives

$$
\theta_8\le\theta\le\theta_9.
\tag{104.8}
$$

After a further subsequence put

$$
{a_D\over D}\to\alpha.
\tag{104.9}
$$

Let `g_1>=g_2>=g_3>=...>0` be the connected complement-gap lengths of `S`, sorted by
size, and define

$$
f(x):=\sin(x/2),
\qquad
C:=\sum_jf(g_j),
\tag{104.10}
$$

$$
U:=3\theta-2\pi,
\qquad
\phi:=2\pi-2\theta,
\qquad
M:=f(\theta)+2f(\phi)
=\sin(\theta/2)+2\sin\theta.
\tag{104.11}
$$

Canonical Sections 100 and 101 give the complete scalar chain

$$
\boxed{
M\le C\le2\alpha\le|S|\le U.
}
\tag{104.12}
$$

Since `U-M=sigma(theta)<=10^{-7}`, every individual slack in (104.12) is at most
`sigma:=sigma(theta)`:

$$
\boxed{
0\le U-|S|\le\sigma,
\quad
0\le |S|-2\alpha\le\sigma,
\quad
0\le2\alpha-C\le\sigma,
\quad
0\le C-M\le\sigma.
}
\tag{104.13}
$$

Also

$$
\sigma'(\theta)
=3-\tfrac12\cos(\theta/2)-2\cos\theta
\ge{15\over4}
\tag{104.14}
$$

on `[2pi/3,pi)`.  Hence throughout the present interval

$$
0\le\theta-\theta_8
\le {4\over15}\,10^{-7}
<2.7\times10^{-8}.
\tag{104.15}
$$

All numerical stability estimates below therefore take place in an extremely small
fixed neighborhood of the audited Section-101 endpoint.

## 104.2 Quantitative complement-gap stability

Canonical Section 94 supplies three distinct complement gaps of length at least
`phi`, so

$$
g_1,g_2,g_3\ge\phi.
\tag{104.16}
$$

The total complement measure is

$$
\sum_jg_j
=2\pi-|S|
=\theta+2\phi+e,
\tag{104.17}
$$

where

$$
0\le e=U-|S|\le\sigma.
\tag{104.18}
$$

We first show that the largest gap is very close to `theta`.

### Lemma 104.1 — largest-gap stability

With

$$
\delta:=\theta-g_1,
\tag{104.19}
$$

one has

$$
\boxed{0\le\delta\le{10\over3}\sigma.}
\tag{104.20}
$$

### Proof

Suppose first that `g_1<=theta-0.1`.  Decrease complement gaps if necessary until
their total is exactly `theta+2phi`, never taking the three distinguished gaps below
`phi`.  This can only decrease `C` because `f` is increasing.

Among vectors of that total, with every coordinate at most `theta-0.1` and at least
three coordinates at least `phi`, the vector

$$
(\theta-0.1,\,\phi+0.1,\,\phi,0,\ldots)
$$

majorizes every feasible vector.  Strict concavity of `f` therefore gives

$$
C-M
\ge
f(\theta-0.1)+f(\phi+0.1)-f(\theta)-f(\phi).
\tag{104.21}
$$

On the interval (104.15) the right side is greater than `0.0326`, as checked by the
accompanying regression certificate.  This contradicts `C-M<=10^{-7}`.  Hence
`delta<0.1`.

Now keep the actual value `g_1=theta-delta`.  Given the remaining total mass and the
two mandatory `phi` coordinates, concavity is minimized by concentrating all first
order transferred mass into one other coordinate.  Dropping the nonnegative extra
total mass `e` only lowers the result, so

$$
C-M
\ge
h_\theta(\delta)
:=f(\theta-\delta)+f(\phi+\delta)-f(\theta)-f(\phi).
\tag{104.22}
$$

For `0<=delta<=0.1`,

$$
h_\theta'(\delta)
=f'(\phi+\delta)-f'(\theta-\delta)>0.30
\tag{104.23}
$$

uniformly on (104.15).  Therefore

$$
0.30\,\delta
<h_\theta(\delta)
\le C-M
\le\sigma,
$$

which proves (104.20).  `square`

Write

$$
x_2:=g_2-\phi,
\qquad
x_3:=g_3-\phi,
\qquad
\tau:=\sum_{j\ge4}g_j.
\tag{104.24}
$$

Equation (104.17) gives the exact identity

$$
x_2+x_3+\tau=\delta+e.
$$

Consequently

$$
\boxed{
0\le x_2,x_3,\tau
\le {13\over3}\sigma.
}
\tag{104.25}
$$

Thus the full complement-gap vector is quantitatively close to
`(theta,phi,phi)`; all nonprincipal complement mass is at most `4.34e-7` radians.

## 104.3 The two support spans adjacent to the principal gap are tiny

Take the largest gap `G_1`, oriented clockwise from support endpoint `A` to support
endpoint `B`.  Let `s_+` be the angular distance from `B` to the starting support
endpoint of the next principal gap, and define `s_-` analogously on the other side.

### Lemma 104.2 — adjacent-span bound

$$
\boxed{s_+,s_-\le\delta.}
\tag{104.26}
$$

### Proof

Consider the next principal-gap endpoint `C` after `B`.  Both `A` and `C` belong to
`S`.  Their clockwise separation is

$$
g_1+s_+=\theta-\delta+s_+.
$$

If `s_+>delta`, this exceeds `theta`.  Since their minor angular distance is at most
`theta`, the clockwise separation must then lie in the other allowed branch:

$$
\theta-\delta+s_+\ge2\pi-\theta,
$$

so

$$
s_+\ge\phi+\delta.
\tag{104.27}
$$

But then no support point can occur at offsets strictly between `delta` and
`phi+delta` from `B`: every such point would have angular distance from `A` in the
forbidden interval `(theta,2pi-theta)`.  That entire open interval is therefore
contained in one complement component of length at least `phi` before the next
principal gap.  It would be a fourth gap of length at least `phi`.

This contradicts (104.25), because

$$
\tau\le {13\over3}10^{-7}<\phi.
$$

Hence `s_+<=delta`.  The other side is identical.  `square`

So almost all support angular span lies between the two smaller principal gaps; the
two support pieces adjacent to the largest gap have combined angular span at most

$$
s_++s_-\le2\delta\le{20\over3}\sigma.
\tag{104.28}
$$

## 104.4 Principal corridor directions remain far from `pi/3`

Let `q_1,q_2,q_3 in RP^1` be the limiting chord directions across the three principal
complement gaps.  Normalize cyclic order so `G_1` is the largest gap.  A circle chord
has projective direction equal to its angular midpoint plus `pi/2`, so pairwise chord
direction separations equal pairwise midpoint separations in `RP^1`.

Using (104.20), (104.25), and (104.26), the two separations involving `G_1` differ from
`theta/2` by at most

$$
{43\over6}\sigma,
\tag{104.29}
$$

while the separation between `G_2` and `G_3` differs from `pi-theta` by at most

$$
{73\over6}\sigma.
\tag{104.30}
$$

At the Section-101 endpoint,

$$
{\theta_8\over2}-{\pi\over3}
=0.3042564636\ldots .
\tag{104.31}
$$

Since increasing `theta` only increases this first margin and decreases
`pi-theta` farther below `pi/3`, (104.29)--(104.30) imply, throughout
`sigma<=10^{-7}`,

$$
\boxed{
\left|
\operatorname{dist}_{RP^1}(q_i,q_j)-{\pi\over3}
\right|>0.3042
\qquad(i\ne j).
}
\tag{104.32}

The principal corridor geometry therefore retains essentially the entire fixed angular
margin used qualitatively in Section 102.

## 104.5 Retain the nonnegative outer-ledger slack

The Section-101 finite-gap proof can be rerun without dropping the favorable local
currency.  Along a further subsequence on which normalized defect quantities converge,
its finite-family inequality gives

\[
C
\le
2\alpha-\limsup_D
{2s_D+c_D+Q_D\over D}.
\tag{104.33}
$$

Together with (104.13),

$$
\boxed{
\limsup_D{2s_D+c_D+Q_D\over D}\le\sigma.
}
\tag{104.34}
$$

In particular

$$
{c_D\over D},{Q_D\over D}\le\sigma+o(1).
\tag{104.35}
$$

Let

$$
C_{tail}:=\sum_{j\ge4}f(g_j).
$$

Since `sin(x/2)<=x/2`, (104.25) gives

$$
\boxed{C_{tail}\le{\tau\over2}\le{13\over6}\sigma.}
\tag{104.36}
$$

For any finite family of complement gaps, the exact Section-82 outer-walk identity and
the ordinary two-edge route floor give, after normalization,

$$
\sum_{j\in J}\ell_j\le2\alpha,
\tag{104.37}
$$

where `ell_j` is the limiting normalized unit-contact route length across gap `g_j`.
Taking increasing finite families gives two useful consequences.

First, the total normalized outer-route length over all nonprincipal positive
complement gaps satisfies

$$
\boxed{
L_{tail}
\le2\alpha-\sum_{i=1}^3 f(g_i)
\le\sigma+C_{tail}
\le{19\over6}\sigma.
}
\tag{104.38}
$$

Second, the total excess of the three principal routes above their endpoint chords is
at most the same amount:

$$
\boxed{
\sum_{i=1}^3\bigl(\ell_i-f(g_i)\bigr)
\le{19\over6}\sigma.
}
\tag{104.39}
$$

Thus each principal route individually has normalized path excess at most
`(19/6)sigma`.

## 104.6 Micro-route and base-spacing leakage budgets

We next bound all outer-face train endpoints that can avoid the principal corridors.

Call a consecutive-attachment interval **macroscopic** when it converges to a positive
complement component of `S`; the remaining intervals are **micro**.  Direct
loaded-loaded micro routes have total outer-edge density at most `sigma` by
(104.35).

For non-direct micro routes, subtract the two-edge baseline.  If `E_{micro}` is their
total normalized excess above two, the outer identity and the full macro-route lower
bound give

$$
E_{micro}\le(2\alpha-C)+{c_D\over D}+o(1)
\le2\sigma+o(1).
\tag{104.40}
$$

Every micro route of length at least three contributes at least one unit of this
excess.  Their total edge-occurrence density is therefore at most

$$
2(2\sigma)+2\sigma=6\sigma.
\tag{104.41}
$$

A length-two micro route with loaded middle vertex uses loaded-loaded contact edges.
The total outer-face occurrence density of such edges is at most `2c_D/D`, hence at
most `2sigma`.  Including the direct one-edge routes, all micro-route edges outside
length-two unloaded-apex teeth have total density at most

$$
\boxed{9\sigma.}
\tag{104.42}
$$

There is also a quantitative base-spacing statement.  Apply the same polar-arc cover
used in canonical Section 100 to the support `S`, excluding finitely many selected
macroscopic complement gaps and then exhausting the complement components.  The total
normalized force-hull boundary arclength available to micro consecutive-attachment
bases is at most `|S|/2`, while their count density tends to `alpha`.  Since every base
has length at least one,

$$
\boxed{
\limsup_D{1\over D}
\sum_{\text{micro bases}}(|p_k-p_{k+1}|-1)
\le {|S|\over2}-\alpha
\le{\sigma\over2}.
}
\tag{104.43}

This is the quantitative version of the unit-base saturation used at equality in
Section 102.

## 104.7 Explicit Section-90 phase families

Canonical Section 103 gives, throughout the tiny interval
`theta<=theta_9`, a unique wrapping carrier with area greater than `0.19D^2`.
Local rhombic saturation therefore allows the conservative strict-rhombus count

\[
R_D\ge0.18D^2
\tag{104.44}
$$

for all sufficiently large members of the contradiction sequence.

Canonical Section 89 and Section 100 give

$$
T_D\le6a_D+O(1)\le6D
\tag{104.45}
$$

in this neighborhood.  Canonical Section 68 gives

$$
\sum_R\delta_R
<C_{phase}D,
\qquad
C_{phase}
={\pi^2\sqrt3(2+\sqrt3)\over12}
<5.317.
\tag{104.46}
$$

Run the canonical Section-90 binning argument with

$$
r=0.18,
\qquad
C_T=6.
\tag{104.47}
$$

Before the optional minimum-degree pruning, Section 90.3 already gives two fixed,
distinct phase-label train families `A_D,B_D` in one inverse-diameter reduced-phase
bin, each of size at least

$$
\boxed{
\alpha_0D,
\qquad
\alpha_0={r\over32C_T}
={3\over3200}
=0.0009375.
}
\tag{104.48}
$$

Their limiting projective directions `u_A,u_B` satisfy

$$
\boxed{
\operatorname{dist}_{RP^1}(u_A,u_B)=\pi/3.
}
\tag{104.49}

Every full local train segment has two distinct physical boundary-end occurrences, so
each phase family supplies at least

\[
\boxed{
E_0D,
\qquad
E_0:=2\alpha_0={3\over1600}=0.001875
}
\tag{104.50}

physical train endpoints.

## 104.8 Quantitative leakage from one phase family

Fix one of the two Section-90 phase families.  We bound how many of its `E_0D`
physical endpoints can avoid the three principal complement corridors.

### (a) Nonquadrilateral boundary

Canonical Section 82 gives at most `5Q_D` strict-rhombus boundary edge occurrences
against bounded nonquadrilateral faces.  By (104.35), this costs at most

\[
5\sigma D+o(D).
\tag{104.51}
$$

### (b) Nonprincipal macroscopic corridors

Equation (104.38) bounds their total outer-edge occurrence density by

$$
{19\over6}\sigma.
\tag{104.52}
$$

### (c) Exceptional micro routes

Equation (104.42) costs at most

$$
9\sigma D+o(D).
\tag{104.53}
$$

### (d) Teeth on the two tiny support spans adjacent to `G_1`

Their total angular span is at most `2delta`.  The Type-II polar-arc boundary estimate
therefore gives total normalized boundary arclength at most `delta`.  Unit-separated
bases give at most `delta D+o(D)` such teeth, and each has two route legs.  By (104.20)
this costs at most

$$
{20\over3}\sigma D+o(D)
\tag{104.54}
$$

phase endpoint occurrences.

### (e) Bad-base teeth on the main support region

Fix

$$
h:={1\over2000}=0.0005.
\tag{104.55}
$$

Call a regular length-two unloaded-apex tooth **bad-base** if its polygon base length
exceeds `1+h`.  The base-excess budget (104.43) shows that their number density is at
most `sigma/(2h)`.  Each tooth has at most two phase endpoint legs, so bad-base teeth
cost at most

$$
{\sigma\over h}D
=2000\sigma D.
\tag{104.56}
$$

### (f) Good-base teeth on the main support region

For a unit-unit tooth with base `b in [1,1+h]`, either leg makes projective angle

$$
\beta(b)=\arccos(b/2)
$$

with the base.  Hence, after splitting by the two leg choices, the bases corresponding
to endpoints from one inverse-phase family have directions in two intervals, each of
width at most

$$
w_h
:={\pi\over3}-\arccos((1+h)/2)
<0.000289.
\tag{104.57}
$$

We use one elementary convex directional-length fact.  Along the main support region,
the boundary of the normalized limit `K=conv(S)` consists of radius-`1/2` circular
support arcs and chords spanning the tail complement gaps.  In an oriented tangent
direction interval of width `w<pi`, the circular pieces contribute boundary length at
most `w/2`.  The total length of all tail chords is at most `C_tail`.

Convex boundary-direction monotonicity and Hausdorff convergence therefore imply that
finite polygon bases in one such direction window have normalized total length at
most

$$
{w\over2}+C_{tail}+o(1).
\tag{104.58}
$$

Because every base has length at least one, the same expression bounds their count
density.  Applying this to the two leg classes and using (104.36) gives good-base
phase endpoint density at most

$$
\boxed{
w_h+2C_{tail}
\le w_h+\tau
\le w_h+{13\over3}\sigma.
}
\tag{104.59}

### Total leakage

Summing (104.51)--(104.54), (104.56), and (104.59), one phase family can place at
most

\[
\boxed{
\left[
 w_h+{12169\over6}\sigma+o(1)
\right]D
}
\tag{104.60}

physical endpoints away from the three principal corridors.

At `sigma<=10^{-7}` the explicit bracket is

\[
w_h+{12169\over6}10^{-7}
<0.000492.
\tag{104.61}
$$

Subtracting from `E_0=0.001875`, each phase family leaves more than
`0.001383D` endpoints on the three principal corridors.  Pigeonholing gives one
principal corridor carrying at least

$$
\boxed{\rho D,\qquad \rho:=0.00045}
\tag{104.62}

endpoints of that phase family.

## 104.9 Quantitative corridor/phase alignment

Let a principal corridor have limiting projective chord direction `q`, and suppose it
carries at least `rho D` endpoints of a selected phase family with limiting projective
direction `u`.  Let

\[
\Delta:=\operatorname{dist}_{RP^1}(u,q)\in[0,\pi/2].
$$

Orient corridor route edges along its endpoint chord.  Every selected phase endpoint
edge contributes asymptotic projection loss at least

$$
1-\cos\Delta.
$$

Equation (104.39) bounds the total normalized route excess by `(19/6)sigma`.  Therefore

$$
\rho(1-\cos\Delta)
\le {19\over6}\sigma.
\tag{104.63}
$$

Use

$$
1-\cos x\ge{2x^2\over\pi^2}
\qquad(0\le x\le\pi).
$$

At `sigma<=10^{-7}` and `rho=0.00045`,

$$
\boxed{\Delta<0.059\text{ radians}.}
\tag{104.64}

Apply this separately to the two Section-90 phase families.  They cannot use the same
principal corridor, because then (104.64) would put their directions within `0.118`
radians of each other, contradicting their exact `pi/3` separation.  Hence they use
two distinct principal corridors.

For those two corridors, the triangle inequality in `RP^1` gives

\[
\left|
\operatorname{dist}_{RP^1}(q_i,q_j)-{\pi\over3}
\right|<0.118.
\tag{104.65}

But the geometric stability estimate (104.32) gives the incompatible lower bound

\[
\left|
\operatorname{dist}_{RP^1}(q_i,q_j)-{\pi\over3}
\right|>0.3042.
$$

This is the desired contradiction.

## 104.10 Explicit carrier threshold

We have proved that no full-core Type-II sequence can have **all** positive-area
macroscopic harmonic-cell limits of normalized diameter at most `mu_9`.

Indeed, under that assumption canonical Section 103 supplies the unique wrapping
carrier of area greater than `0.19D^2`; canonical Section 101 places its angular
diameter in `[theta_8,theta_9]`; and §§104.1--104.9 contradict the canonical Section-90
two-phase core.

Canonical Section 83's finite-macroscopic-cell reduction now gives an actual carrier
consequence.  There is one absolute `c_9>0` such that every sufficiently large Type-II
survivor contains a locally rhombus-saturated harmonic cell `P_*` with

\[
\boxed{
\operatorname{area}(P_*)\ge c_9D^2,
\qquad
\operatorname{diam}(P_*)
\ge(\mu_9-o(1))D.
}
\tag{104.66}

Equivalently the previous explicit carrier coefficient `mu_8` can be replaced by

\[
\boxed{
\mu_9=0.9760407675809149535\ldots .
}
\tag{104.67}

This is a rigorous but deliberately nonoptimized improvement.  Increasing it now
means improving the stability constants, not finding another qualitative compactness
argument.

## 104.11 Dependency and regression audit

- **Canonical Section 101 / `C-WRAP-COMPLEMENT-CHORD`:** scalar chain, complement-gap
  chord floor, and `theta_8,mu_8`.  Section 101 is canonical from audit.41.
- **Canonical Section 103 / `C-UNIQUE-WRAP-CAP-DEFICIT`:** uniqueness and full
  cap-deficit area concentration in the wrapping carrier.  Section 104 is stacked on
  this input.
- **Canonical Sections 62 and 82:** outer-route partition, exact face identity,
  quadrilateral/rhombus classification.
- **Canonical Sections 68, 89, and 90:** explicit phase-defect budget, local train
  count, and the two inverse-phase train families.  Section 104 uses the larger shore
  size from Section 90.3, not the much smaller optional minimum-degree constant from
  Section 90.4.
- **Canonical Sections 83 and 88:** cell disjointness/area tiling, cap-family capacity,
  and final macroscopic transfer.
- **Canonical Section 102 / `C-PHASE-CORRIDOR-ENDPOINT-EXCLUSION`:** not a logical
  premise.  Section 104 rederives the
  quantitative versions of the endpoint-normal-form and phase/corridor contradiction;
  Section 102 is the qualitative predecessor.
- **Bridges:** safe.  Physical train endpoints are counted only on actual strict-
  rhombus boundary edges.  Bridge occurrences can absorb outer-route length but cannot
  create false train endpoints.
- **Contact-isolated source points:** untouched.
- **No KKT coefficient floor, Cauchy perimeter inequality, rejected Reuleaux-cap
  theorem, or external pseudosegment theorem is used.**

**Theorem state:** promoted as `C-WRAP-QUANT-PHASE-GAP` in audit.44. C-II remains
open.
