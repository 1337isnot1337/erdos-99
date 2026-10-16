# Erdős Problem #99 — flat-middle injectivity and the loaded/blocker fork

**Date:** 2026-09-14  
**Target:** Target C-II, canonical full-core Type-II branch  
**Claim class:** proof-only structural refinement; theorem-state authority unchanged  
**External input:** none

## LEVEL I STATUS

`STILL OPEN`

The small-residual pentagon program extracts many exceptional pentagons converging to the flat unit trapezoid. Previous counting allowed one source vertex to serve as the almost-flat middle vertex of up to five selected pentagons, using only the contact-degree bound.

That loss is unnecessary. Triangle-freeness makes the flat-middle map asymptotically injective.

If a bounded convex contact face has middle vertex `m` with face angle

\[
\angle lmr>\pi-\varepsilon,
\qquad \varepsilon<\pi/6,
\]

then **no second bounded convex contact face** can have `m` as an almost-flat middle vertex with the same threshold. Consequently, on every small-residual branch, good flat pentagons have distinct middle vertices.

This improves the generic extraction from a `1/5` loss to no first-order loss and gives a useful exact fork: every unloaded flat middle needs an additional actual contact edge outside its two pentagon-chain contacts.

---

## 1. Angular separation of contact rays

Let `m` be any source vertex and let `x,y` be two distinct unit-contact neighbors. If the smaller angle between the rays `mx,my` is `theta`, then

\[
|x-y|=2\sin{\theta\over2}.
\]

The source is triangle-free, so `|x-y|>1`. Hence

\[
\boxed{\theta>{\pi\over3}.}
\tag{1.1}
\]

In particular, whenever two consecutive contact rays around `m` bound an angular sector smaller than `pi`, that sector has angle strictly greater than `pi/3`.

---

## 2. One vertex cannot be the flat middle of two bounded convex faces

### Lemma FM.1 — flat-middle injectivity

Fix

\[
0<\varepsilon<\pi/6.
\]

A source vertex `m` can be the middle vertex of at most one bounded convex contact-face sector whose angle exceeds `pi-epsilon`.

### Proof

Suppose two distinct bounded convex face sectors at `m` have angles

\[
\alpha_1,\alpha_2>\pi-\varepsilon.
\tag{2.1}
\]

Each is strictly smaller than `pi` because the faces are convex.

If `deg_C(m)=2`, the two sectors determined by the same two contact rays have angles `alpha` and `2pi-alpha`. Since one is below `pi`, the other is above `pi`; they cannot both be angles of bounded convex faces. Thus degree two is impossible.

Assume `deg_C(m)>=3`. The two large sectors use at least two sectors in the cyclic decomposition by consecutive contact rays. Their total angle is greater than

\[
2\pi-2\varepsilon.
\]

All remaining contact sectors together therefore have total angle less than `2epsilon`. At least one remaining sector has angle less than `2epsilon<pi/3`. That sector is bounded by two distinct consecutive unit-contact rays. By (1.1) this is impossible.

Therefore at most one such bounded face exists. `square`

The constant `pi/6` is only a convenient strict threshold. Any threshold for which the unused angular budget is below the triangle-free `pi/3` separation gives the same conclusion.

---

## 3. Upgrade the small-residual flat-pentagon extraction

Use the notation of the flat-pentagon chain theorem:

\[
X:=Q-f,
\qquad
f_*:=\sqrt{\Delta_2}-{\pi\over4}+{g\over2},
\]

where the current AG58 proof-only gain is

\[
g=0.00058.
\]

Thus

\[
\boxed{
f_*=0.167204643466509\ldots .}
\tag{3.1}
\]

On a Type-II subsequence with

\[
R_F=o(D),
\]

choose the trapezoid-stability diagonal slowly enough that every retained good pentagon has flat angle greater than `pi-epsilon_D`, with

\[
\varepsilon_D\to0.
\]

For all sufficiently large `D`, `epsilon_D<pi/6`, so Lemma FM.1 applies.

Let `G_D` be the number of good pentagons and `V_flat` the number of their selected flat middle vertices. The standard degree-excess/residual argument gives

\[
X+G_D\ge(f_*-o(1))D.
\tag{3.2}
\]

Lemma FM.1 makes the selection injective:

\[
\boxed{V_{flat}=G_D.}
\tag{3.3}
\]

Therefore

\[
\boxed{
X+V_{flat}\ge(f_*-o(1))D.
}
\tag{3.4}
\]

This replaces the earlier coarse estimate

\[
X+5V_{flat}\ge(f_*-o(1))D.
\]

In particular, if `X=o(D)`, then

\[
\boxed{
\liminf {V_{flat}\over D}
\ge0.167204643466509\ldots .
}
\tag{3.5}
\]

Every counted vertex is an actual positive-core source vertex with two exact unit contacts becoming antipodal.

---

## 4. Every unloaded flat middle needs an additional contact blocker

Split the distinct flat middle vertices into

\[
V_{flat}=L_{flat}+U_{flat},
\]

where `L_flat` counts loaded diameter endpoints and `U_flat` counts vertices carrying no positive diameter reaction.

Fix one unloaded flat middle `m`. It already has its two exact pentagon-chain contacts `ml,mr`. Their directions are not exactly antipodal in the actual strictly convex pentagon. If these were the only two positive contacts at `m`, positive contact equilibrium would require

\[
\alpha_{ml}(l-m)+\alpha_{mr}(r-m)=0
\]

with both coefficients positive, which is possible only when the two contact vectors are exactly antiparallel. Therefore `m` has at least one additional actual positive contact edge.

Choose one such extra edge for every unloaded flat middle. Let `E_block` be the number of distinct chosen blocker edges after duplicate choices are identified. One contact edge has only two endpoints, so it can be chosen by at most two middle vertices. Hence

\[
\boxed{U_{flat}\le2E_{block}.}
\tag{4.1}
\]

Combining with (3.4),

\[
\boxed{
X+L_{flat}+2E_{block}
\ge(f_*-o(1))D.
}
\tag{4.2}
\]

This is a finite source-derived fork. In the low-degree-excess corner, the flat pentagon population must be paid by actual loaded hull vertices or actual extra contact edges.

The local KKT regression in
`target_c_flat_chain_local_kkt_regression_2026-09-14.md`
shows why (4.2) cannot be strengthened to a uniform stress-weight charge: an extra blocker edge may carry stress tending to zero with the flat turn.

---

## 5. AG58 low-`t` endpoint specialization

The low-`t` pentagon ledger becomes slightly sharper after AG58. Put

\[
C_0=2\sqrt{\Delta_2}+0.00058,
\]

\[
t_{58}={4\over9}(\pi+\sqrt{\Delta_2})+0.0014085
=1.820922037979444\ldots .
\]

At the most permissive `delta=kappa=0` endpoint values,

\[
{f\over D}\ge0.497372297369096\ldots,
\tag{5.1}
\]

\[
{Q-f\over D}\le0.002879125,
\tag{5.2}
\]

and therefore

\[
\boxed{
{p_5\over D}\ge0.494493172369096\ldots .
}
\tag{5.3}
\]

Assume additionally `R_F=o(D)`. Then all but `o(D)` of these pentagons are empty and trapezoid-close, so Lemma FM.1 gives

\[
\boxed{
{V_{flat}\over D}
\ge0.494493172369096\ldots-o(1).
}
\tag{5.4}
\]

Thus the near-floor/small-residual branch contains almost one half-diameter's worth of **distinct** almost-straight positive-core vertices.

The loaded/blocker fork becomes

\[
\boxed{
{L_{flat}+2E_{block}\over D}
\ge0.494493172369096\ldots-o(1).
}
\tag{5.5}
\]

Consequently at least one of

\[
\boxed{
{L_{flat}\over D},
\quad
{E_{block}\over D}
}
\]

has limsup at least

\[
\boxed{0.164831057456365\ldots .}
\tag{5.6}
\]

The same endpoint also has

\[
{L_{OO}\over D}\ge0.320167770872156\ldots
\]

outer-to-outer two-sidedly diameter-braced trains and more than

\[
1.236232930922740\ldots D
\]

distinct trains touching pentagons, so (5.5) is now part of a genuinely dense boundary/network profile rather than an isolated local count.

---

## 6. What this does and does not close

The improvement is structural, not a decimal endpoint claim:

```text
small residual + low t
  -> ~0.49449 D cheap pentagons
  -> ~0.49449 D distinct almost-flat core vertices
  -> either many loaded flat hull vertices
     or many distinct extra contact blockers.
```

Neither alternative is yet contradictory.

- The loaded alternative needs a global theorem coupling near-flat bounded-face sectors at many force-hull vertices to the diameter-thrackle / hull-turning geometry.
- The blocker alternative needs a train-network theorem showing that the extra contacts cannot all be absorbed by the rhombic bulk or by low-stress defect corridors.

A per-vertex KKT-weight lower bound is explicitly false by the local regression.

## 7. Scope audit

- The injectivity lemma uses only convexity of bounded contact faces and the triangle-free unit-contact angular separation.
- It does not assume the flat middle vertices are loaded or unloaded.
- `E_block` counts actual positive unit-contact edges, not stress weight and not train terminal occurrences.
- The low-`t` constants inherit the proof-only AG58 and Section-171 status.
- The theorem remains conditional on `R_F=o(D)` when invoking trapezoid stability.
- No source point is deleted, and no full-source affine-kernel statement is used.
- No exact unit triangle or strict sub-`D` competitor is produced.

**Disposition:** proof-only structural refinement. C-II remains open.
