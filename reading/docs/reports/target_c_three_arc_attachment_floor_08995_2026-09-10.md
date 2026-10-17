> Generated reading edition · [exact source](../../../docs/reports/target_c_three_arc_attachment_floor_08995_2026-09-10.md) · source SHA-256 `294c87f08ab1fd846c63ae7447cbaae94bc2bd33a56ba5ed00c105c345ec1592`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 5 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-33B992564453","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — sharp three-arc attachment envelope raises the renormalized floor above `0.8995`

**Date:** 2026-09-10  
**Repository branch:** `research/c2-renorm-paired-pocket-20260910` after RA  
**Run type:** exact circular-geometry / attachment-capacity sharpening  
**Target:** Target C, all post-ZF survivors  
**External web search:** Hernández Cifre's solved `(A,d,R)` literature was checked as a cross-check; no external theorem is used below  
**Computation:** exact rational sign certificate `research/target_c_three_arc_attachment_check.py`

## LEVEL I STATUS

`STILL OPEN`.

RA used only the coarse endpoint fact that a radius-`1/2` circle subset of diameter at
most `sqrt(3)/2` has convex-hull area at most `3sqrt(3)/16`.  This report solves the
circle-subset extremal problem sharply through the next odd-component transition.

For

```math
z_0:=\frac{\sqrt3}{2},
\qquad
z_5:=\sin\frac{2\pi}{5},
```

define

```math
\theta(z):=2\arcsin z,
\qquad
 g(z):=\frac{4\pi}{3}-\theta(z),
```

and

```math
\boxed{
W_3(z):=
\frac\pi4-
\frac38\bigl(g(z)-\sin g(z)\bigr),
\qquad z_0\le z<z_5.
}
\tag{TA.1}
```

The new geometric theorem is:

> If `S` is any subset of the circle of radius `1/2` and
> `diam(S)<=z in [z_0,z_5)`, then
> ```math
> area(conv S)\le W_3(z).
> ```
> Equality in the wrapping class is approached by three equal circular arcs,
> separated by three equal gaps.

Feeding this into the Target C component ledger gives a unique analytic threshold
`mu_3 in (z_0,z_5)` defined by

```math
\boxed{
W_3(\mu_3)
+
\frac{(2\mu_3+\pi)^2}{36\pi}
=
\Phi(2\rho),
\qquad
\Phi(y)=\frac{y+\sin y}{4},
\quad \rho=\cos\rho.
}
\tag{TA.2}
```

Every post-ZF survivor sequence satisfies

```math
\boxed{
\liminf\mu_D\ge\mu_3.
}
\tag{TA.3}
```

The exact certificate proves

```math
\boxed{\mu_3>0.8995.}
\tag{TA.4}
```

High-precision diagnostic evaluation gives

```math
\mu_3=0.899867166043839\ldots .
```

The decimal is not a proof input.

---

## 1. Circular reformulation

Scale an attachment set by `D` and pass to the FS center.  The limiting loaded
attachment directions lie on the circle

```math
\mathbb S:=\{x:|x|=1/2\}.
```

For two points whose angular separation in the minor direction is `alpha`, the chord
length is

```math
2(1/2)\sin(\alpha/2)=\sin(\alpha/2).
```

Thus the Euclidean diameter condition `diam(S)<=z<1` is equivalent to

```math
d_{\mathbb T}(u,v)\le\theta:=2\arcsin z<\pi
\qquad(u,v\in S),
\tag{1.1}
```

where `d_T` is geodesic angular distance on the circle of circumference `2pi`.

Put

```math
\varphi:=\pi-\theta.
\tag{1.2}
```

Then (1.1) is equivalently

```math
\boxed{
d_{\mathbb T}(S,S+\pi)\ge\varphi.}
\tag{1.3}
```

In the range `z_0<=z<z_5`,

```math
\boxed{\frac\pi5<\varphi\le\frac\pi3.}
\tag{1.4}
```

---

## 2. Maximal feasible circle sets

Let `S` be feasible for (1.3).  By a standard chain/Zorn argument on closed feasible
supersets, enlarge it to an inclusion-maximal closed feasible set `M`.  The closure of
the union of a nested chain remains feasible because (1.3) is a closed pairwise
condition.

Maximality gives the exact fixed-point relation

```math
\boxed{
M=\{x:d_{\mathbb T}(x,M+\pi)\ge\varphi\}.
}
\tag{2.1}
```

Indeed, any point outside `M` satisfying the right-side inequality could be added
without violating (1.3).  Hence

```math
\boxed{
\mathbb T\setminus M=N_\varphi(M+\pi),
}
\tag{2.2}
```

where `N_varphi` is the open angular `varphi`-neighborhood.

### Lemma TA.1 — component count and total arc measure

Suppose `M` has `m` connected components.  Then

```math
\boxed{m\text{ is odd},\qquad |M|=\pi-m\varphi.}
\tag{2.3}
```

Here `|M|` is total angular Lebesgue measure.

#### Proof

The open set in (2.2) has finitely many components: each of its connected components
contains the open `varphi`-neighborhood of at least one component of `M+pi`, hence has
length at least `2varphi`.  Therefore `M` is a finite union of closed arcs/points; on a
circle its number of components equals the number of components of its complement.

Now `M+pi` has exactly `m` components.  Taking its open `varphi`-neighborhood can merge
components but cannot split them.  Equation (2.2) says the result still has exactly
`m` components.  Hence no two component neighborhoods merge.  Each component of
`M+pi` therefore expands by exactly `varphi` at each end, and

```math
2\pi-|M|=|M|+2m\varphi.
```

This proves the measure formula.

Moreover `M+pi` is disjoint from `M`, and each of its `m` components lies in a distinct
one of the `m` complementary gaps of `M`.  The `M`-components and `(M+pi)`-components
therefore alternate cyclically.  The half-turn is an orientation-preserving involution
of this cyclic list of `2m` components.  Its induced permutation is the half-cycle
shift by `m` positions.  Since it swaps the two alternating colors, `m` is odd.
`square`

---

## 3. The wrapping class has exactly three components

If the origin is outside `conv(M)`, a line through the origin separates it from `M`,
so `M` lies in an open semicircle.  In that case (1.1) puts it in one arc of angular
length at most `theta`; its convex hull is contained in the corresponding circular
segment.  Thus

```math
area(conv M)
\le
B(z):=
\frac{\theta-\sin\theta}{8}.
\tag{3.1}
```

Now assume

```math
0\in conv(M).
```

Then `m` cannot be one, since Lemma TA.1 would make `M` one arc of length
`pi-varphi<pi`, whose convex hull misses the origin.  Hence `m>=3`.

By (1.4) and the nonnegativity of `|M|=pi-mvarphi`,

```math
m<\frac\pi\varphi<5
```

for `varphi>pi/5`.  Since `m` is odd,

```math
\boxed{m=3.}
\tag{3.2}
```

The total occupied angular measure is therefore

```math
|M|=\pi-3\varphi=3\theta-2\pi,
\tag{3.3}
```

and the three complementary gaps `g_1,g_2,g_3` have total

```math
\boxed{g_1+g_2+g_3=\pi+3\varphi=4\pi-3\theta.}
\tag{3.4}
```

Because the origin lies in `conv(M)` and `theta<pi`, each `g_i<pi`.

---

## 4. Sharp area bound in the three-component phase

The convex hull of `M` is the radius-`1/2` disk with the three circular segments over
the complementary gaps removed.  A gap of angular size `g` removes area

```math
\frac18(g-\sin g).
```

Therefore

```math
area(conv M)
=
\frac\pi4-
\frac18\sum_{i=1}^3(g_i-\sin g_i).
\tag{4.1}
```

The function

```math
f(g)=g-\sin g
```

is convex on `[0,pi]`, since `f''(g)=sin g>=0`.  Jensen and (3.4) give

```math
\sum_{i=1}^3f(g_i)
\ge
3f\left(\frac{4\pi-3\theta}{3}\right).
```

Thus

```math
area(conv M)
\le
\frac\pi4-
\frac38\left[
\left(\frac{4\pi}{3}-\theta\right)
-
\sin\left(\frac{4\pi}{3}-\theta\right)
\right]
=W_3(z).
\tag{4.2}
```

Since `conv(S) subset conv(M)`, the same upper bound holds for the original set.

The equality model is explicit: take three equal occupied arcs of length

```math
\theta-\frac{2\pi}{3}
```

separated by three equal gaps of length

```math
\frac{4\pi}{3}-\theta.
```

Their pairwise circular diameter is exactly `theta`, so the envelope is sharp.

Finally the outside-origin cap bound cannot dominate in this interval.  Indeed
`W_3(z)` is increasing and

```math
W_3(z_0)=\frac{3\sqrt3}{16}.
```

Meanwhile

```math
B(z)\le\frac{\theta}{8}<\frac\pi{10}
<\frac{3\sqrt3}{16},
```

where the last strict inequality follows already from `pi<22/7` and `sqrt(3)>17/10`.
This completes the sharp circle-subset theorem.

---

## 5. Concentration over all unloaded components

Let the macroscopic unloaded components have normalized graph diameters

```math
z_j=\lim\delta_j/D.
```

GR gives

```math
\sum_jz_j\le\mu.
\tag{5.1}
```

Suppose

```math
z_0\le\mu<z_5.
```

At most one limiting attachment cell can be in the wrapping class, because two such
components would consume at least `2z_0=sqrt(3)>mu` of the graph-diameter budget.

All nonwrapping components have the cap bound `B(z)`.  RA proved that `B` is increasing,
convex, and superadditive on total argument below one.  Hence their total area is at
most `B(r)` where `r` is their total normalized graph-diameter mass.

If there is no wrapping component, their total is at most `B(mu)<W_3(mu)`.

If a wrapping component has mass `z>=z_0`, the remainder satisfies

```math
r\le z_5-z_0<\frac1{10}.
```

On `[z_0,z_5]`, differentiating (TA.1) gives

```math
W_3'(z)
=
\frac34\frac{1-\cos g(z)}{\sqrt{1-z^2}}
>\frac32,
\tag{5.2}
```

because `g(z)>pi/2` throughout this interval and
`sqrt(1-z^2)<=1/2` for `z>=z_0`.

For `0<=r<=1/10`,

```math
B'(r)=\frac{r^2}{2\sqrt{1-r^2}}<\frac1{100}.
\tag{5.3}
```

Therefore

```math
W_3(z+r)-W_3(z)>B(r),
```

and

```math
W_3(z)+B(r)\le W_3(z+r)\le W_3(\mu).
\tag{5.4}
```

As in RA, components with `delta_r=o(D)` contribute `o(D^2)` after an `eta` truncation.
Thus:

### Theorem TA.2 — sharp attachment-cell capacity in the three-arc phase

For every convergent post-ZF subsequence with

```math
z_0\le\mu<z_5,
```

```math
\boxed{
\limsup\frac{C_{att}}{D^2}\le W_3(\mu).
}
\tag{TA.5}
```

---

## 6. Feed the envelope into the whole Target C ledger

JS gives

```math
x:=\lim\frac{d_P+Q}{D}
\le\frac{2\mu+\pi}{3}
\tag{6.1}
```

after discarding the nonnegative projective side cost.  RP paired-pocket capacity and
ZG give

```math
\boxed{
\limsup\frac G{D^2}
\le
\frac{(2\mu+\pi)^2}{36\pi}.
}
\tag{6.2}
```

Since

```math
area(F)=C_{att}+G,
```

TA.5 gives

```math
\limsup\frac{area(F)}{D^2}
\le
W_3(\mu)+\frac{(2\mu+\pi)^2}{36\pi}.
\tag{6.3}
```

FSDB, independently of `mu`, gives

```math
\boxed{
\liminf\frac{area(F)}{D^2}
\ge
\Phi(2\rho).
}
\tag{6.4}
```

Therefore every survivor limit in the three-arc range must satisfy

```math
\boxed{
J_3(\mu):=
W_3(\mu)+\frac{(2\mu+\pi)^2}{36\pi}
\ge\Phi(2\rho).
}
\tag{TA.6}
```

Both terms in `J_3` are strictly increasing, so there is at most one threshold.
At `mu=z_0`, RA gives a fixed strict deficit.  At `mu=z_5`, the right side is already
strictly above `0.62`, while

```math
\Phi(2\rho)<\frac{1.48+1}{4}=0.62.
```

For example

```math
W_3(z_5)
=
\frac\pi{20}+\frac38\cos\frac\pi{30}
>0.52,
```

and the cavity term is `>0.21`.  Hence TA.2 has a unique root `mu_3 in (z_0,z_5)`.
For every `mu<mu_3`, (TA.6) fails.  This proves TA.3.

---

## 7. Exact rational lower certificate `mu_3>0.8995`

The certificate

```sh
python3 research/target_c_three_arc_attachment_check.py
```

uses only `fractions.Fraction` and integer square-root checks for every asserted sign.
At

```math
\mu=8995/10000,
```

it upper-bounds `asin(mu)` via

```math
\arcsin\mu
=
\frac\pi2-
\arctan\frac{\sqrt{1-\mu^2}}{\mu}
```

and an alternating rational arctangent series.  It uses the canonical rational
barriers

```math
6283/2000<\pi<3927/1250,
\qquad
\sqrt3<97/56,
```

and the already audited FSDB floor

```math
\Phi(2\rho)>154451/250000.
```

The resulting exact rational margin in

```math
\Phi(2\rho)-J_3(0.8995)
```

is strictly positive; its decimal diagnostic is about

```math
2.18\times10^{-4}.
```

The script also proves `0.8995<0.95<sin(2pi/5)` exactly using
`sqrt(5)>20/9`, so the candidate lies safely inside the three-component regime.

Thus

```math
\boxed{\mu_3>0.8995.}
```

---

## 8. Equality structure at the new scalar endpoint

Any sequence with

```math
\mu_D\to\mu_3
```

must make both (6.3) and (6.4) sharp.  In particular:

1. the attachment graph-diameter budget concentrates in one macroscopic component;
2. its limiting attachment set is the three-equal-arc extremizer;
3. `R_I+s_B=o(D)` and `sum delta_r/D->mu_3`;
4. the remaining attachment components have only `o(D)` total graph-diameter mass;
5. the RP/JS outer-cavity upper bound is also asymptotically sharp.

The first component has three equal complementary angular gaps of size

```math
g_*=\frac{4\pi}{3}-2\arcsin\mu_3
\approx1.95\text{ radians}.
```

The force hull itself need not have those gaps: other loaded vertices may lie between
attachment arcs.  This prevents an immediate reuse of the projective side-cost
endpoint contradiction.

---

## 9. Literature cross-check

The classical `(A,d,R)` Blaschke-Santalo problem for arbitrary planar convex bodies was
solved by Hernandez Cifre.  The published complete-system literature confirms that
`(A,d,R)` has a known sharp upper boundary.  It is not used here because an arbitrary
convex body of circumradius `1/2` and diameter `z` may have boundary points away from
the circumcircle; Target C attachment cells are convex hulls of points constrained to
the common FS circle.  TA.1 is therefore a stronger special-class statement in the
range needed by this proof.

---

## 10. Next target

The new endpoint has one giant unloaded component whose attachment pins occupy three
macroscopic boundary arcs but leave three large attachment gaps.  At the same time the
whole force hull remains in the near-antipodal FS response regime and the cavity bound
must be sharp.

Two concrete next routes are now available:

1. use C37/C38 noncrossing attachment incidence plus loaded degree capacity to show that
a single component with three macroscopic attachment arcs forces too many repeated
boundary pins or too much loaded degree slack `s_B`, contradicting endpoint equality;
2. extend the circle-subset envelope to the next odd phase `z>=sin(2pi/5)`, where the
maximal closed feasible sets have five components.  This would continue the explicit
constant iteration even if the three-arc endpoint survives.

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Let z in [sqrt3/2, sin(2pi/5)), theta=2asin z, phi=pi-theta.
For a maximal feasible circle subset M, diameter<=z is equivalent to
  dist_T(M,M+pi)>=phi.
Maximality gives
  T\M=N_phi(M+pi).
If M has m components, no phi-neighborhoods merge, so
  |M|=pi-m phi.
The M and M+pi components alternate; the half-turn exchanges colors, hence m is odd.
If 0 in conv(M), m!=1. Since phi>pi/5, m<5, hence m=3.
Thus the three complement gaps sum 4pi-3theta. Since g-sin g is convex,
  area(conv M)<=W3(z)
  =pi/4-(3/8)(g-sin g), g=4pi/3-2asin z.
Outside-center sets have the smaller one-cap bound.

GR has sum delta_r<=mu D+O(1). In the three-arc range at most one attachment cell can
wrap the center; superadditivity for the remaining cap cells and W3'>3/2 show all
diameter mass can be concentrated into the wrapped cell for an upper bound:
  C_att/D^2<=W3(mu).
JS/RP gives
  G/D^2<=(2mu+pi)^2/(36pi).
FSDB gives
  area(F)/D^2>=Phi(2rho).
Hence every survivor needs
  W3(mu)+(2mu+pi)^2/(36pi)>=Phi(2rho).
The left side is strictly increasing and has a unique root
  mu_3=0.8998671660... (diagnostic),
with exact Fraction certificate
  mu_3>0.8995.
Therefore
  liminf mu_D>=mu_3>0.8995.

Next: exclude the three-arc endpoint using attachment incidence/degree slack, or extend
the circle-subset theorem to the five-component phase.
```
