# Target C — wrapping angular-measure threshold audit

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**  
**Status:** canonical after independent hostile audit and theorem-state audit.40 promotion.

Canonical Section 88 bounds a wrapping attachment limit by six allowed angular
intervals of total measure `6 theta-4 pi`.  That is a useful anchor-based container,
but it does not yet use the pairwise diameter condition between **all** points in the
three allowed clusters.

Keeping that missing information halves the angular-measure ceiling.  If `S` is any
wrapping compact subset of the circle whose pairwise minor angular distances are at
most `theta<pi`, then

\[
\boxed{|S|\le3\theta-2\pi.}
\]

The proof is a one-dimensional antipodal-neighborhood argument using the same three
forbidden arcs already present in canonical Section 94.

For Type-II harmonic attachments, unit separation on the near-circle boundary then
gives

\[
\boxed{
\alpha:=\lim {|A_D|\over D}
\le {3\theta-2\pi\over2}.
}
\]

Canonical Section 96 independently gives

\[
\alpha\ge{3\over2}\sin\theta.
\]

Hence every wrapping harmonic-cell limit satisfies

\[
\boxed{3\sin\theta\le3\theta-2\pi.}
\]

The unique root on `[2pi/3,pi)` is

\[
\boxed{
\theta_7=2.6053256746009026857\ldots,
\qquad
\mu_7:=\sin(\theta_7/2)
=0.9642670742838972841\ldots .
}
\]

Thus every wrapping Type-II harmonic-cell limit has normalized diameter at least
`mu_7`.  This strictly improves both canonical Cauchy bounds: the coarse bound
`0.9370981976...` and the mixed-gap/Cauchy bound `0.9399896933...`.

The Section-88 cap-family transfer then yields an actual macroscopic locally
rhombus-saturated Type-II carrier of diameter at least `(mu_7-o(1))D`.

No Section-97/98 endpoint theorem, Cauchy perimeter inequality, KKT coefficient floor,
or deletion of contact-isolated source points is used.

---

# 100. Pairwise angular diameter halves the six-cluster support ceiling

## 100.1 Circle normalization

Let `S` be a compact subset of the radius-`1/2` circle.  Parameterize the circle by
angle modulo `2pi`, and write `d_T(x,y) in [0,pi]` for minor angular distance.

Assume

\[
\boxed{d_T(x,y)\le\theta<\pi\qquad(x,y\in S)}
\tag{100.1}
\]

and that `S` is wrapping, meaning it is not contained in an open semicircle.
Equivalently, the origin belongs to `conv(S)`.

Put

\[
r:=\pi-\theta>0,
\qquad
\phi:=2r=2\pi-2\theta.
\tag{100.2}
\]

Canonical Sections 88 and 94 choose three cyclic anchors

\[
y_1,y_2,y_3\in S
\]

whose triangle contains the origin.  If their three cyclic gaps are `g_1,g_2,g_3`,
then

\[
g_i\in(0,\pi),
\qquad
\sum_i g_i=2\pi,
\qquad
g_i\le\theta.
\tag{100.3}
\]

Inside each anchor gap, Section 94 identifies a central support-free open arc of exact
length

\[
\phi=2\pi-2\theta=2r.
\tag{100.4}
\]

Call these three disjoint forbidden arcs `J_1,J_2,J_3`.
Removing them partitions the circle into three closed cluster arcs

\[
C_1,C_2,C_3,
\]

each containing one anchor, and

\[
S=S_1\cup S_2\cup S_3,
\qquad
S_i:=S\cap C_i\ne\varnothing.
\tag{100.5}
\]

The interiors of the three cluster arcs are separated cyclically by gaps of length at
least `2r`.

## 100.2 Antipodal neighborhoods are forbidden

Let `x^*:=x+pi` denote the antipode of angle `x`.  For points on the circle,

\[
d_T(y,x^*)=\pi-d_T(x,y).
\tag{100.6}
\]

Thus (100.1) gives

\[
d_T(y,x^*)\ge\pi-\theta=r
\qquad(x,y\in S).
\tag{100.7}
\]

Consequently the open angular `r`-neighborhood of the antipodal set is disjoint from
`S`:

\[
\boxed{
N_r(S+\pi)\cap S=\varnothing.
}
\tag{100.8}
\]

Boundary contacts at angular distance exactly `r` have zero one-dimensional measure,
so for angular Lebesgue measure `|.|`,

\[
\boxed{|N_r(S+\pi)|\le2\pi-|S|.}
\tag{100.9}
\]

## 100.3 Three separated clusters force three neighborhood-expansion credits

Translate the decomposition (100.5) by `pi`.  Since the original cluster groups are
separated by the three forbidden gaps `J_i` of length `2r`, the open neighborhoods

\[
N_r(S_1+\pi),
\quad N_r(S_2+\pi),
\quad N_r(S_3+\pi)
\]

have pairwise disjoint interiors.  They may touch at endpoints, which does not affect
measure.

For each nonempty compact `S_i`, choose the first and last points of `S_i` in the
linear angular coordinate on its cluster arc.  The two exterior intervals of length
`r` immediately beyond those extremal points lie in `N_r(S_i)` and are disjoint from
`S_i`.  They are also disjoint from one another: the other two forbidden gaps already
contribute total complementary angular length at least `4r`.

Therefore

\[
\boxed{|N_r(S_i+\pi)|\ge|S_i|+2r.}
\tag{100.10}

Summing over the three disjoint neighborhoods,

\[
|N_r(S+\pi)|
=\sum_{i=1}^3|N_r(S_i+\pi)|
\ge |S|+6r.
\tag{100.11}

Combine (100.9) and (100.11):

\[
2\pi-|S|\ge|S|+6r.
\]

Hence

\[
2|S|\le2\pi-6(\pi-\theta)=6\theta-4\pi,
\]

so

\[
\boxed{|S|\le3\theta-2\pi.}
\tag{100.12}

This is exactly half the Section-88 six-interval container measure
`6theta-4pi`.

The factor two is real.  Section 88 only intersects the `theta`-neighborhood
constraints coming from the three anchors.  Equation (100.12) also enforces the
pairwise `theta`-distance constraint between points lying in different anchor
clusters.

### Sharpness of the circle lemma

The measure bound (100.12) cannot be improved using only wrapping and pairwise angular
diameter.  Put three arc centers at angles `0,2pi/3,4pi/3` and give each arc angular
length

\[
t:=\theta-{2\pi\over3}.
\]

For `theta in [2pi/3,pi)`, the three arcs are disjoint.  The largest minor angular
distance between points in adjacent arcs is

\[
{2\pi\over3}+t=\theta,
\]

so the union has pairwise angular diameter `theta`, is wrapping, and has measure

\[
3t=3\theta-2\pi.
\]

Thus (100.12) is the sharp one-dimensional support theorem.

---

# 100.4 Transfer angular support measure to attachment density

Now return to a wrapping Type-II harmonic-cell sequence

\[
P_D=\operatorname{conv}(A_D)
\]

with source diameter `D->infinity` and

\[
{\operatorname{diam}(P_D)\over D}\to\lambda<1.
\tag{100.13}
\]

After passing to a subsequence, canonical Type-II annular compactness gives Hausdorff
convergence of the normalized attachment sets to a compact wrapping set `S` on the
radius-`1/2` circle.  Put

\[
\theta:=2\arcsin\lambda.
\tag{100.14}
\]

Because diameter of a convex polygon is attained at vertices, a limiting pair of
attachment vertices realizes the limiting diameter; hence `S` has Euclidean diameter
`lambda`.  On the radius-`1/2` circle this is equivalent to angular diameter `theta`,
so the circle theorem applies.

After another subsequence let

\[
{a_D\over D}\to\alpha,
\qquad a_D:=|A_D|.
\tag{100.15}

We claim

\[
\boxed{\alpha\le{|S|\over2}.}
\tag{100.16}

Fix `delta>0`.  Let `E_delta` be the open angular `delta`-neighborhood of `S` on the
circle.  Since `S` is compact, `E_delta` is a finite union of angular intervals; the
number of components depends on `delta` but not on `D`.  Hausdorff convergence puts
every attachment angle in `E_delta` for all sufficiently large `D`.

Canonical Type-II near-disk geometry gives

\[
B\left(0,\left({1\over2}-o(1)\right)D\right)
\subset F_D\subset
B\left(0,\left({1\over2}+o(1)\right)D\right).
\tag{100.17}
\]

The polar-arc estimate used in canonical Section 88 therefore bounds the total
force-hull boundary arclength over `E_delta` by

\[
\left({D\over2}+o(D)\right)|E_\delta|.
\tag{100.18}
\]

On each component of `E_delta`, consecutive loaded attachments are source points at
Euclidean distance at least one.  Boundary arclength dominates chord length, so a
boundary arc of length `L` contains at most `L+1` such points.  Since the number of
components is `O_delta(1)`, (100.18) gives

\[
a_D\le
\left({D\over2}+o(D)\right)|E_\delta|+O_\delta(1).
\tag{100.19}
\]

Divide by `D` and pass to the subsequence limit:

\[
\alpha\le{|E_\delta|\over2}.
\tag{100.20}
\]

As `delta downarrow0`, continuity from above of angular measure for the compact set
`S` gives

\[
|E_\delta|\downarrow|S|.
\]

This proves (100.16).  Combining with (100.12),

\[
\boxed{
\alpha\le {3\theta-2\pi\over2}.
}
\tag{100.21}

This is the new finite-density consequence.  It is strictly stronger than the
canonical Section-88 ceiling

\[
\alpha\le3\theta-2\pi.
\]

---

# 100.5 Canonical Section 96 gives the opposite density floor

Canonical Section 96 is independent of the new support-measure argument.  Its exact
outer-walk/face ledger gives every wrapping limit

\[
\boxed{
\alpha\ge {3\over2}\sin\theta.
}
\tag{100.22}

Combining (100.21) and (100.22),

\[
{3\over2}\sin\theta
\le
{3\theta-2\pi\over2}.
\]

Therefore

\[
\boxed{
3\sin\theta\le3\theta-2\pi.
}
\tag{100.23}

Define

\[
G(\theta):=3\theta-2\pi-3\sin\theta,
\qquad
{2\pi\over3}\le\theta<\pi.
\tag{100.24}

Then

\[
G'(\theta)=3-3\cos\theta>0
\tag{100.25}
\]

throughout the interval.  Also

\[
G(2\pi/3)=-{3\sqrt3\over2}<0,
\qquad
\lim_{\theta\uparrow\pi}G(\theta)=\pi>0.
\]

Hence there is a unique root `theta_7`, and (100.23) forces

\[
\boxed{\theta\ge\theta_7.}
\tag{100.26}

Numerically,

\[
\boxed{
\theta_7=2.6053256746009026857\ldots,
\qquad
\mu_7:=\sin(\theta_7/2)
=0.9642670742838972841\ldots .
}
\tag{100.27}

Thus every wrapping Type-II harmonic-cell limit obeys

\[
\boxed{\lambda\ge\mu_7.}
\tag{100.28}

For comparison,

\[
\mu_7
>0.9399896933531978
>\sqrt{1-(\pi/9)^2}
>0.9362157414095831.
\tag{100.29}

So the canonical mixed-gap/Cauchy and coarse-Cauchy thresholds remain correct but are
strictly subsumed by (100.28).

---

# 100.6 Transfer to an actual macroscopic carrier

The cap-family part of canonical Section 88 uses a threshold `mu` only through the
following dichotomy for a macroscopic circle-supported cell limit of diameter at most
`mu`:

- either its support is cap type; or
- it is wrapping.

Section 100 excludes the second alternative for every fixed

\[
\mu<\mu_7.
\]

Therefore the same cap-family capacity proof applies verbatim with any fixed
`mu<mu_7`.  Its short-cell area ceiling remains strictly below the diameter-one disk
area `pi/4` for every fixed `mu<1`.

Canonical Section 83 supplies the total harmonic-cell perimeter/square-root tail
budget and the summed local rhombic deficit `o(D^2)`.  Taking `mu upward mu_7`
diagonally as in Sections 88, 94, and 96 yields actual harmonic cells `P_*` with

\[
\boxed{
\operatorname{diam}(P_*)
\ge(\mu_7-o(1))D,
}
\tag{100.30}

\[
\boxed{
\operatorname{area}(P_*)\ge c_7D^2
}
\tag{100.31}

for one absolute `c_7>0`, and

\[
\boxed{
{A_{4,*}\over\operatorname{area}(P_*)}\to1.
}
\tag{100.32}

Canonical Section 82 then makes the selected carrier boundary-order
near-quadrangulated, and canonical Sections 73--76 retain their ordered train-grid
consequences inside the quadratic rhombic part.

---

# 100.7 What this invalidates and what remains

The following lower thresholds are now obsolete as live Type-II frontiers, although
their proofs may remain valid historical steps:

- Section 88: `0.8896708101...`;
- Section 94: `0.9197786626...`;
- Section 96: `0.9362157414...`;
- canonical coarse Cauchy: `0.9370981976...`;
- canonical mixed-gap/Cauchy: `0.9399896933...`.

Likewise, Sections 97 and 98 analyze the sharp `mu_4` endpoint conditionally.  Since
`mu_4<mu_7`, that asymptotic regime is empty and those modules are no longer live
closure branches.  Their internal conditional geometry need not be false.

The full-core Type-II obligation is now:

```text
near-disk force hull
  -> one macroscopic locally rhombus-saturated harmonic carrier
     with diameter at least (0.9642670742...-o(1))D
  -> ordered near-triangular train-grid structure inside its quadratic rhombic part
  -> still need an exact triangle or a source-preserving strict sub-D competitor.
```

The inactive-container branch is unchanged.

---

# 100.8 Dependency and regression audit

- **Canonical Sections 88 and 94:** existence of three wrapping anchors and three
  pairwise disjoint central forbidden arcs of length `2pi-2theta`.
- **Canonical Type-II near-disk geometry:** normalized attachments lie on the
  radius-`1/2` limit circle and fixed angular unions have force-hull boundary length
  `(D/2+o(D))` times angular measure.
- **Canonical Section 96 / `C-WRAP-OUTER-WALK-GAP`:** independent density floor
  `alpha>=(3/2)sin(theta)`.
- **Canonical Section 83:** macroscopic-cell tail and local rhombic-saturation transfer.
- **Canonical Section 82:** carrier near-quadrangulation handoff only.
- **Pairwise diameter is used twice:** first to forbid the antipodal `r`-neighborhood,
  and second through the canonical Section-96 outer-walk floor.
- **No Cauchy inequality is used.**
- **No Section-97/98 endpoint theorem is used.**
- **No KKT coefficient floor, rejected cap theorem, or deletion of contact-isolated
  source points is used.**

## 100.9 Independent hostile audit — PASS

The two steps that can fail silently in this argument were re-derived independently.

First, the support-measure ceiling has a second proof. For anchor gap `g_i`, put
`delta_i=theta-g_i` and parameterize the two equal `delta_i` support pieces outside its
endpoints by compact sets `A_i,B_i subset [0,delta_i]`. Pairwise circular diameter gives

\[
a+b\le\delta_i\quad\hbox{or}\quad a+b\ge\delta_i+(2\pi-2\theta).
\]

With `C_i=delta_i-B_i`, this is
`(A_i-C_i) cap (0,2pi-2theta)=empty`. For every fixed
`0<t<2pi-2theta`, the sets `A_i` and `C_i+t` are disjoint and both lie in
`[0,delta_i+t]`. Therefore

\[
|A_i|+|B_i|\le\delta_i+t.
\]

Letting `t` decrease to zero and summing the three pairs gives independently
`|S|<=sum delta_i=3theta-2pi`. This is the core of the separate PR #289 proof and
checks the cluster-neighborhood argument without reusing it.

Second, the finite-to-limit transfer was checked directly against canonical Section 88,
equation (88.8). A fixed finite open cover `U` of the compact limit support contains all
attachment angles for large `D`, and Section 88 gives

\[
|A_D|\le (|U|/2+o(1))D+O_U(1).
\]

Outer regularity then gives `alpha<=|S|/2`. No angular equidistribution assumption is
present.

The scalar equation and numerical root are independently reproduced by
`research/verify_target_c_wrapping_angular_measure_threshold.py`. No Section-97/98
endpoint theorem is used. The old `mu_4` endpoint analyses remain conditional proofs on
an empty asymptotic regime, not counterexamples and not live C-II branches.

**Audit verdict:** PASS. The wrapping threshold and actual-carrier consequence are
canonical as `C-WRAP-ANGULAR-MEASURE` in theorem-state audit.40. C-II remains open.
