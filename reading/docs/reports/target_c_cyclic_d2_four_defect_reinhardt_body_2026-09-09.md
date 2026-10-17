> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_d2_four_defect_reinhardt_body_2026-09-09.md) · source SHA-256 `3f899da7c031e49ea93db08dd085fa05418eb8574ce54a5699daa229af028d54`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 3 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-FEAFD5063D8C","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cyclic `d_H=2`: four-defect Reinhardt body decomposition

**Date:** 2026-09-09  
**Repository branch:** `research/post-zf-currency-coupling-2026-09-09`  
**Run type:** exact combinatorial/metric refinement of D2S + IB  
**Target:** cyclic primitive endpoint, `d_H=2`  
**Depends on:** D2 four-block normal form, D2S exact within-tree direction saturation, IB isostatic-body reduction  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

D2S associates to every consecutive within-tree diameter-direction pair an exact unit shell side: if

```math
zy,zw\in H,
\qquad
|zy|=|zw|=D,
```

are consecutive in direction order, then their nonshared endpoints satisfy

```math
|yw|=1
```

and `yw` is a shell edge.

There are exactly `q-4` such within-tree transitions.  The four-block order contains exactly `q-4` shell sides internal to the blocks

```math
A_0\mid B_0\mid A_1\mid B_1.
```

The new observation is that these two sets coincide exactly and without multiplicity.

### Theorem D2R

For all sufficiently large cyclic `d_H=2` survivors:

1. every shell edge internal to one of the four color blocks is the base of a unique mixed triangle with two diameter edges;
2. the only shell edges not of this form are the four A/B block-transition contacts;
3. for each diameter-tree vertex `z`, its neighbors in the opposite color block form one consecutive shell interval, and every consecutive pair in that interval is joined by a unit shell side centered at `z`;
4. each isostatic body of IB is a triangle-chain Laman graph: its `n-2` internal shell sides are the bases of `n-2` exact `D,D,1` mixed triangles supported on its diameter tree;
5. a change of the shared diameter center across three consecutive direction edges has one rigid metric form: an exact isosceles trapezoid with bases `D` and `D-1/D` and legs `1`.

Thus the complete mixed framework consists of two exact Reinhardt-type triangle-chain bodies joined by only four exceptional unit transition bars.

---

## 1. The D2S shell-edge map is injective

For every within-tree consecutive direction pair sharing `z`, D2S produces one shell edge `yw` with

```math
|y-w|=1,
\qquad
|z-y|=|z-w|=D.
```

Suppose the same unit shell edge `yw` had two distinct diameter centers `z,z'`. Then `z,z'` would be the two intersection points of the radius-`D` circles about `y,w`.

Their separation is

```math
|z-z'|=2\sqrt{D^2-\frac14}.
```

For `D>1`,

```math
2\sqrt{D^2-\frac14}>D.
```

This contradicts the source diameter bound. Hence a unit shell edge has at most one common diameter center.

Therefore distinct within-tree transitions produce distinct shell edges.

---

## 2. Certified sides cannot cross a color-block boundary

Consider two consecutive diameter edges in `T_A` sharing a terminal `z`.

If `z in A_0`, their two nonshared endpoints both lie in `A_1`; if `z in A_1`, both nonshared endpoints lie in `A_0`. D2S says those nonshared endpoints are consecutive shell vertices.

Since D2 proves each `A_i` is one cyclic shell block, the resulting certified unit side is internal to that block. The same holds for `T_B`.

Thus every D2S-certified shell side is internal to one of

```math
A_0,B_0,A_1,B_1.
```

---

## 3. Counting forces exact exhaustion

The diameter graph has

```math
h=q-2
```

edges and D2S gives exactly two cross-tree direction transitions. Hence the number of within-tree direction transitions is

```math
(h-2)=q-4.
```

By Section 1 these produce `q-4` distinct certified shell sides.

On the other hand, if the four nonempty block sizes are

```math
a_0,b_0,a_1,b_1,
\qquad
a_0+b_0+a_1+b_1=q,
```

then the number of shell sides internal to the four blocks is exactly

```math
(a_0-1)+(b_0-1)+(a_1-1)+(b_1-1)=q-4.
```

Section 2 puts every certified side in this set, and the two sets have the same cardinality. Therefore they are equal.

Hence:

```math
\boxed{
\text{all internal block sides are certified, and exactly four shell sides are not.}
}
\tag{D2R.1}
```

Those four exceptions are precisely the transitions

```math
A_0|B_0,
\quad
B_0|A_1,
\quad
A_1|B_1,
\quad
B_1|A_0.
```

---

## 4. Neighbor intervals at every diameter-tree vertex

Fix `z in A_0`.  D2S shows that whenever two consecutive direction edges incident to `z` occur, their opposite endpoints form a certified shell side in `A_1`.

The total number of within-tree consecutive pairs sharing a vertex equals

```math
q-4.
```

But

```math
\sum_{v\in V(H)}(\deg_H(v)-1)
=2h-q
=q-4,
```

because every terminal has positive diameter degree.

For a vertex `v` with degree `d`, at most `d-1` consecutive pairs in the global linear direction block can share `v`; equality occurs exactly when all `d` incident direction edges form one contiguous run.

Since the sums of the upper bounds and the actual counts are equal, equality holds at every vertex. Therefore the diameter edges incident to every terminal form one contiguous direction run.

Consequently the neighbors of `z` occur consecutively in the opposite shell color block, and every adjacent pair of those neighbors is joined by a certified unit side centered at `z`.

This proves D2R.3.

---

## 5. Each IB body is a chain of exact mixed triangles

Take one tree component `T_A` on `a` vertices. IB gives its isostatic body

```math
G_A=T_A\cup P(A_0)\cup P(A_1),
```

with

```math
|E(G_A)|=2a-3.
```

The two shell paths contribute exactly `a-2` contact edges. By D2R.1 every one is certified: for each contact edge `uv` there is a unique `z` in the opposite color class with

```math
zu,zv\in E(T_A),
\qquad
|zu|=|zv|=D,
\qquad
|uv|=1.
```

Thus every internal contact edge is the base of an exact isosceles mixed triangle with two diameter sides.

There are `a-2` such triangles, exactly the number of triangles in a 2-tree/Laman triangle-chain construction on `a` vertices.  Their incidence is controlled by the caterpillar `T_A`: star runs glue consecutive triangles along diameter spokes, while center switches glue across a diameter-tree spine edge.

The same statement holds for `G_B`.

No abstract Laman body remains. The metric on every internal body triangle is fixed to

```math
(D,D,1).
```

---

## 6. Exact center-switch gadget

Suppose three consecutive diameter directions inside one tree are

```math
us,
\qquad
st,
\qquad
tv,
```

so the shared endpoint changes from `s` to `t` across the middle edge.

D2S gives the two certified shell contacts

```math
|u-t|=1,
\qquad
|s-v|=1.
\tag{6.1}
```

Normalize

```math
s=(0,0),
\qquad
t=(D,0).
```

The equations

```math
|u-s|=D,
\qquad
|u-t|=1
```

give

```math
u=
\left(
D-\frac1{2D},
\sigma\sqrt{1-\frac1{4D^2}}
\right)
```

for a sign `sigma in {+1,-1}`.

Likewise

```math
|v-t|=D,
\qquad
|v-s|=1
```

gives

```math
v=
\left(
\frac1{2D},
\tau\sqrt{1-\frac1{4D^2}}
\right).
```

If `sigma=-tau`, then

```math
|u-v|^2
=\left(D-\frac1D\right)^2
+4\left(1-\frac1{4D^2}\right)
=D^2+2>D^2,
```

contradicting the source diameter. Hence `sigma=tau`.

Therefore `u,v` lie on the same side of the diameter `st` and

```math
\boxed{|u-v|=D-\frac1D.}
\tag{D2R.2}
```

The convex quadrilateral on these four points is an isosceles trapezoid with bases

```math
|s-t|=D,
\qquad
|u-v|=D-1/D,
```

and legs

```math
|u-t|=|s-v|=1.
```

Thus every shared-center change in a D2S body has exactly one metric realization up to Euclidean congruence and reflection.

---

## 7. Relation to Reinhardt equality geometry

For an internal shell side `uv` with common diameter center `z`, the center lies on the inward perpendicular bisector of `uv` at distance

```math
\sqrt{D^2-\frac14}
```

from the supporting line of `uv`.

Therefore the width of the shell in the normal direction to every internal block side attains the maximum permitted by the simultaneous diameter constraints from `u` and `v`.

Only the four A/B transition sides can fail this local antipodal-side equality.

Hence the `d_H=2` shell is literally a four-side defect from the local side/antipode condition appearing in Reinhardt/clipped-Reuleaux perimeter extremizers. RP independently proves that its total perimeter is within `O(D^-2)` of the sharp Reinhardt scale after the universal `pi/(24D)` polygonal term is removed.

The remaining task is therefore concentrated at four transition sides, not spread through `Theta(D)` shell edges.

---

## 8. Interaction with the unique KKT stress

IB says `G_A,G_B` are isostatic and the four exceptional transition contacts are exactly four bars joining the two rigid bodies. Their body-bar wrench rank is three, so the four transition contact forces have one unique dependence.

D2 gives that dependence in vector form:

```math
v_i+v_k=v_j+v_\ell,
\qquad
v_r=\alpha_rt_r.
```

D2R shows every internal force in either body propagates through a chain of fixed `D,D,1` triangles. Thus the only geometric freedom relevant to the unique stress is now:

1. the combinatorial sequence of star runs and center switches inside each tree;
2. the four exceptional transition side directions;
3. the two strict cross-tree projective gap defects.

No additional internal side-length parameter remains.

---

## 9. Next target

The sharp remaining theorem is a **four-transition stress incompatibility**:

> Show that two exact `D,D,1` triangle-chain bodies in the D2 four-block order cannot be joined by four unit shell transition bars so that all internal contact coefficients and all diameter coefficients have the Target C positive KKT signs while the transition wrench dependence is positive and C56-G holds.

A local method-of-joints calculation is now viable because each body is statically determinate and every internal triangle has the same two lengths `D,D,1`.

If that sign test survives, the alternative is to classify the star-run/center-switch word and compare its four exceptional side widths with RP's `O(D^-2)` Reinhardt deficit.

---

## 10. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| certified shell-edge map injective | proved | two radius-D circle centers would be farther than D |
| certified sides = all internal block sides | proved | injectivity + exact `q-4` count |
| every diameter neighborhood is one shell interval | proved | exact sum of `deg_H-1` adjacency capacities |
| every internal body contact belongs to a `D,D,1` mixed triangle | proved | exact exhaustion |
| center-switch trapezoid | proved | direct circle intersection + diameter bound |
| only four local Reinhardt side defects remain | proved in the side/antipode sense | exactly the block transitions |
| transition KKT incompatibility | open | requires statics/sign analysis |
| Level I | still open | four-bar/two-body stress remains feasible abstractly |
