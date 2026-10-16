<!-- theorem-state: {"artifact_id":"ART-A8AFB62D13CE","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_low_mu_macroscopic_outer_shell_2026-09-10.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=75d2825b01a893de23e128aa3d12c852f5e47822; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — low-renormalized-surplus sources have a macroscopic inactive outer shell

**Date:** 2026-09-10  
**Repository base:** `1adc420e9227476135d6891b61f1a75193aa90ab` plus the GR/EA branch  
**Run type:** full-source / force-hull coupling theorem  
**Target:** Target C, all post-ZF survivors  
**Depends on:** strict translated-lattice comparison, Oler, isoperimetry/Cauchy perimeter, C36, C65, GR, EA  
**External input:** none  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`.

This report couples the full-source hull to the new all-phase renormalized currency.
It proves that the low-`mu` force-bulk phase is not merely population-heavy in
rattlers: those rattlers must change the source convex hull at **linear geometric
scale**.

For every global minimizer `A` of diameter `D`, with

\[
K=\operatorname{conv}A,
\qquad
P_K=\operatorname{per}K,
\]

one has the exact universal bound

\[
\boxed{
P_K>
\pi\left(
\sqrt{D^2+\frac34}-\frac{\sqrt3}{2}
\right).
}
\tag{OS.1}
\]

In particular

\[
\boxed{
0\le \pi D-P_K<\frac{\pi\sqrt3}{2}.
}
\tag{OS.2}
\]

Thus the full source hull is within an **absolute constant** of the maximal
perimeter `pi D`, not merely within `o(D)`.

Now let `F=conv(B)` be the positive force hull and let

\[
\mu_D:=\frac{e_{BB}+2s_C-3(d_H+s_Z)}D.
\]

If an unbounded post-ZF survivor sequence satisfies

\[
\mu_D\le0.60+o(1),
\]

then the generalized RSJ inequality implies

\[
\boxed{
P_F<3.03D
}
\tag{OS.3}

for all sufficiently large members of the sequence.  Consequently

\[
\boxed{
P_K-P_F>0.1115D-2.75.
}
\tag{OS.4}
\]

Equivalently, in Cauchy width form,

\[
\boxed{
\int_0^\pi
\bigl(w_K(\theta)-w_F(\theta)\bigr)\,d\theta
>0.1115D-2.75.
}
\tag{OS.5}
\]

Hence for some support direction `theta`,

\[
\boxed{
 w_K(\theta)-w_F(\theta)
 >0.03547D-0.876.
}
\tag{OS.6}
\]

At least one of the two supporting sides in that direction therefore contains a
source point outside `F` whose support-coordinate excess over `F` is

\[
\boxed{
>0.01773D-0.438.
}
\tag{OS.7}
\]

By C36 the whole nonisolated positive contact core lies in `F`; C65 says every source
point outside that core is fully inactive: it is contact-isolated and is not a diameter
endpoint.  Thus every low-`mu` survivor has a **macroscopically protruding inactive
rattler**.

Combining with EA gives the stronger normal form

\[
\boxed{
\mu_D\le0.60+o(1)
\Longrightarrow
\frac{|R|}{n}\ge0.85409-o(1)
\quad\text{and}\quad
\operatorname{dist}_{\rm support}(R,F)\ge0.0177D-O(1)
}
\tag{OS.8}
\]

in some support direction.

This still does not settle C-II.  The missing theorem is now sharply geometric: rule
out a global minimizer whose diameter is carried entirely by the positive core while
more than 85% of the source is inactive and at least one inactive point protrudes a
linear distance beyond the force hull, or construct a strict sub-`D` rearrangement
from that configuration.

---

## 1. Exact full-source perimeter bound

Use the canonical constants

\[
a_0=\frac{\sqrt3}{2},
\qquad
c_0=\frac{\sqrt3}{4}.
\]

For a global minimizer the strict translated triangular-lattice comparison gives

\[
D^2<\frac{2\sqrt3}{\pi}(n-1),
\]

or equivalently

\[
\boxed{a_0(n-1)>\frac{\pi D^2}{4}.}
\tag{1.1}
\]

Oler gives

\[
\operatorname{area}K+c_0P_K\ge a_0(n-1).
\tag{1.2}
\]

Isoperimetry gives

\[
\operatorname{area}K\le\frac{P_K^2}{4\pi}.
\tag{1.3}
\]

Combining (1.1)--(1.3),

\[
\frac{P_K^2}{4\pi}+c_0P_K
>\frac{\pi D^2}{4}.
\]

Multiply by `4pi` and insert `4pi c_0=pi sqrt(3)`:

\[
P_K^2+\pi\sqrt3\,P_K-\pi^2D^2>0.
\tag{1.4}
\]

The positive root of the quadratic is

\[
\frac\pi2\left(\sqrt{4D^2+3}-\sqrt3\right)
=
\pi\left(\sqrt{D^2+\frac34}-\frac{\sqrt3}{2}\right).
\]

Since `P_K>0`, (1.4) proves OS.1.

Every planar convex body of diameter `D` satisfies Cauchy's perimeter-diameter bound

\[
P_K\le\pi D.
\]

Also `sqrt(D^2+3/4)>D`, so OS.1 implies

\[
P_K>\pi D-\frac{\pi\sqrt3}{2},
\]

which is OS.2. `square`

### Remark

FS used the same source inequalities to obtain the Bonnesen circumradius bound
`R(K)=D/2+O(sqrt(D))`.  OS.1 records an independent consequence that is sharper at
the perimeter level: the perimeter deficit is bounded by an absolute constant.

---

## 2. Cauchy-width form

For a convex body `C`, let

\[
w_C(\theta)
\]

be its width in the direction with normal angle `theta`.  Cauchy's formula is

\[
\operatorname{per}C=\int_0^\pi w_C(\theta)\,d\theta.
\tag{2.1}
\]

Since every width of a diameter-`D` body is at most `D`, OS.2 is exactly

\[
\boxed{
\int_0^\pi
\bigl(D-w_K(\theta)\bigr)\,d\theta
<\frac{\pi\sqrt3}{2}.
}
\tag{2.2}
\]

Thus the source hull has only constant total width defect from a constant-width
`D` body.

Because `F subseteq K`,

\[
P_K-P_F
=
\int_0^\pi(w_K-w_F)\,d\theta.
\tag{2.3}
\]

This identity is the full-source-to-rattler coupling used below.

---

## 3. Low `mu` forces `P_F<3.03D`

Pass to a convergent post-ZF subsequence and write

\[
\mu=\lim\mu_D,
\qquad
p=\lim\frac{P_F}{D}.
\]

GR proves the all-phase necessary inequality

\[
\max\{\Phi(y),\Psi(p)\}
\le
\frac\pi4\mu^2+
\frac{(\mu+p/2)^2}{4\pi},
\tag{3.1}
\]

where

\[
\Psi(p)=\frac\pi{(\pi-2)^2}\left(\frac p2-1\right)^2.
\]

Assume `mu<=3/5`.  Since the right side of (3.1) increases with `mu>=0`, a necessary
condition is

\[
\Psi(p)
\le
\frac\pi4\left(\frac35\right)^2
+
\frac{(3/5+p/2)^2}{4\pi}.
\tag{3.2}
\]

We show (3.2) fails for every `p>=303/100`.

Use the already audited rational barriers

\[
\frac{6283}{2000}<\pi<\frac{3927}{1250},
\qquad
\frac1{4\pi}<\frac{500}{6283}.
\tag{3.3}
\]

The function `x/(x-2)^2` decreases for `x>2`, so

\[
\frac\pi{(\pi-2)^2}
>
\frac{3927/1250}{(3927/1250-2)^2}.
\tag{3.4}
\]

At `p_0=303/100`, exact rational arithmetic gives

\[
\begin{aligned}
&
\frac{3927/1250}{(3927/1250-2)^2}
\left(\frac{p_0}{2}-1\right)^2\\
&\qquad-
\left[
\frac{3927}{5000}\left(\frac35\right)^2
+
\frac{500}{6283}\left(\frac35+\frac{p_0}{2}\right)^2
\right]\\
&=
\boxed{
\frac{4002910960071}{6397127553500000}>0.
}
\tag{3.5}
\end{aligned}
\]

The left-minus-right difference in (3.2) is strictly increasing for `p>=p_0`.
Indeed

\[
\Psi'(p)
=
\frac\pi{(\pi-2)^2}\left(\frac p2-1\right)
>2\left(\frac{p_0}{2}-1\right)>1,
\]

whereas throughout `p<=pi`

\[
\frac{d}{dp}
\frac{(3/5+p/2)^2}{4\pi}
=
\frac{3/5+p/2}{4\pi}
<\frac{3}{10}<1.
\]

Thus (3.5) excludes every `p>=3.03`.  Hence any sequence with
`mu_D<=0.60+o(1)` satisfies OS.3 for all sufficiently large terms. `square`

---

## 4. Linear perimeter contribution from inactive points

From OS.1 and OS.3,

\[
P_K-P_F
>
\pi\left(\sqrt{D^2+\frac34}-\frac{\sqrt3}{2}\right)-3.03D.
\tag{4.1}
\]

For a simple rational finite bound use

\[
\sqrt{D^2+3/4}>D,
\qquad
\pi>\frac{6283}{2000}=3.1415,
\]

and

\[
\frac{\pi\sqrt3}{2}
<\frac{22}{7}\cdot\frac78
=\frac{11}{4}=2.75,
\]

because `sqrt(3)/2<7/8`.  Therefore

\[
P_K-P_F
>(3.1415-3.03)D-2.75
=0.1115D-2.75,
\]

proving OS.4.

By (2.3), the nonnegative continuous function `w_K-w_F` has integral exceeding the
right side.  Hence its maximum exceeds its average:

\[
\max_\theta(w_K-w_F)
>
\frac{0.1115D-2.75}{\pi}
>
\frac7{22}(0.1115D-2.75).
\]

The right side is

\[
0.03547727\ldots D-0.875.
\]

Therefore the certified rounded-down form is OS.6:

\[
 w_K(\theta)-w_F(\theta)>0.03547D-0.876.
\]

For the maximizing direction, write widths as sums of opposite support functions after
any common origin:

\[
w_K-w_F
=(h_K(\theta)-h_F(\theta))
+(h_K(-\theta)-h_F(-\theta)).
\]

Both support gaps are nonnegative because `F subseteq K`.  At least one is at least
half their sum.  Since half of the exact rational lower bound above exceeds
`0.01773D-0.438`, this proves OS.7.

A support point of `K` realizing a positive gap from `F` is a source hull point not in
`F`.  C36 places every unloaded positive-contact component inside the convex hull of
its loaded attachment set, hence inside `F`; loaded points are in `F` by definition.
Therefore a source point outside `F` is outside the whole positive core.  C65 identifies
such points as fully inactive rattlers and says all actual diameter endpoints are in
the loaded force set.  This proves the macroscopic-rattler conclusion. `square`

---

## 5. Combine with the exact Eppstein force-bulk theorem

EA gives, along a bounded-`mu` sequence,

\[
\frac vn
\le
\frac4{\pi^2}
\left(\mu-\frac{s_B}{D}\right)^2+o(1)
\le
\frac4{\pi^2}\mu^2+o(1).
\]

At `mu<=0.60`,

\[
\frac vn
\le
\frac{1.44}{\pi^2}+o(1)
<0.14591+o(1),
\]

so

\[
\boxed{
\frac{|R|}{n}>0.85409-o(1).
}
\tag{5.1}
\]

Together with OS.7 this proves OS.8.

The two conclusions are logically distinct:

- EA says the inactive population has positive source density;
- OS says inactive geometry contributes linearly to the convex-hull support.

Neither can be replaced by the other.

---

## 6. Regression audit

### 6.1 Regular odd shell plus dense isolated filling

This regression can have a tiny positive force skeleton and many isolates, so EA alone
does not exclude it.  OS adds a requirement that a low-`mu` **global source** also have
near-maximal full-source perimeter.  A synthetic dense filling can be arranged to do
that as well, so OS still does not manufacture a global-optimality certificate.  The
regression therefore survives, as it must.

### 6.2 Nearly unit-spaced triangular filling with no contacts

A translated lattice scaled by `1+epsilon_D`, with `epsilon_D->0`, can have no exact
unit contacts while approaching optimal packing density.  This shows why the `85%`
rattler fraction cannot alone give a leading-density contradiction.  OS is compatible
with the same construction if the outer hull is nearly constant width.

### 6.3 One large inactive protrusion

A single inactive hull point can create a substantial support gap without carrying a
large population.  OS therefore does **not** infer that `Theta(D)` distinct rattlers lie
on the hull.  The population statement comes separately from EA.

### 6.4 Width versus diameter pairs

`w_K(theta)` can be arbitrarily close to `D` without being exactly `D`; H-minimality
controls exact diameter pairs, not a uniform near-diameter slack.  OS does not infer a
dense diameter graph from the constant total width defect.

### 6.5 Quantifier coverage

OS.1--OS.2 hold for every global minimizer, with no triangle-free or C-II assumption.
OS.3--OS.8 hold for every sufficiently large member of any post-ZF survivor sequence
satisfying `mu_D<=0.60+o(1)`.  They retain all source isolates and use no hull-saturation
normalization.

---

## 7. Exact effect on the C-II frontier

GR gives the all-phase lower theorem

\[
\mu_D>0.5947+\epsilon_G
\]

for large `D`.  OS supplies a concrete near-frontier phase normal form on the narrow but
nonempty window

\[
0.5947+\epsilon_G<\mu_D\le0.60+o(1).
\]

Every survivor in that window has simultaneously:

1. at least `85.4%` C65 fully inactive source points;
2. full-source hull perimeter within `pi sqrt(3)/2` of `pi D`;
3. force-hull perimeter below `3.03D`;
4. at least `0.1115D-O(1)` of perimeter supplied outside the force hull;
5. a fully inactive source point protruding at least `0.0177D-O(1)` beyond `F` in
   some support direction.

This is a substantially narrower geometric class than the previous abstract
`force core + arbitrary isolates` formulation.

---

## 8. Precise remaining implication

A theorem of either of the following forms now closes the low-`mu` window:

- **macroscopic-rattler rearrangement:** every global diameter minimizer with a C65
  inactive point at support distance at least `0.017D` outside the diameter-carrying
  positive force hull admits an `n`-point unit-separated competitor of diameter `<D`;
  or
- **outer-shell incompatibility:** no contact/diameter-lexicographically selected
  triangle-free global source can simultaneously have `|R|/n>=0.85-o(1)`,
  `P_K=pi D-O(1)`, and `P_F<=3.03D`.

Neither theorem is currently proved.  A proof must use information absent from the
regular-shell-plus-dense-isolates regression, most likely exact global optimality or a
finite rearrangement rather than leading packing density.

The complementary high-`mu` phase `mu>0.60` still requires a topology/face upper
tradeoff.

---

## 9. Claim classification

| Claim | Classification | Reason |
| --- | --- | --- |
| full-source perimeter OS.1 | proved | strict lattice comparison + Oler + isoperimetry |
| constant perimeter deficit OS.2 | proved | Cauchy diameter-perimeter upper bound |
| `mu<=0.60 -> P_F<3.03D` | proved | GR/RSR + exact rational barrier |
| linear perimeter gap OS.4 | proved | OS.1 + OS.3 + rational constants |
| macroscopic support gap OS.6--OS.7 | proved after downward constant audit | Cauchy width formula + averaging |
| `>85.4%` rattler population in low window | proved | EA |
| low-window strict competitor | not proved | remaining outer-shell endgame |
| Level I | still open | low-window rearrangement and high-`mu` topology both remain |

---

## 10. Promotion recommendation

**Promote OS.1--OS.2 as a shared full-source shell lemma after independent audit.**
They are unconditional and use only already canonical inputs.

**Keep OS.3--OS.8 report-level until the GR/EA chain is promoted.**  They are a useful
C-II phase normal form but do not themselves close a branch.

---

## 11. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Unconditional new full-source theorem:
    P_K > pi(sqrt(D^2+3/4)-sqrt(3)/2),
so
    0 <= pi D-P_K < pi sqrt(3)/2.
Equivalently total width deficit int_0^pi(D-w_K) is O(1), with the exact
bound pi sqrt(3)/2.

For post-ZF all-phase
    mu=(e_BB+2s_C-3(d_H+s_Z))/D.
GR implies mu<=0.60 forces
    P_F<3.03D.
Hence
    P_K-P_F>0.1115D-2.75,
and some support direction has
    w_K-w_F>0.03547D-O(1).
Therefore a C65 fully inactive rattler lies at least
    0.01773D-O(1)
outside the force hull in support coordinate.

EA simultaneously gives, for mu<=0.60,
    rattler fraction >85.4%-o(1).

Low-mu survivor normal form:
    overwhelmingly inactive population + full hull almost maximal perimeter
    + force hull missing >=0.1115D perimeter + one macroscopic inactive protrusion.

Remaining low-mu target:
turn that macroscopic inactive outer shell into a strict sub-D rearrangement.
High-mu target:
upper-bound the exact face/component currency when mu>0.60.
```
