> Generated reading edition · [exact source](../../../docs/reports/target_c_common_bridge_transfer_exclusion_2026-09-10.md) · source SHA-256 `fc98a1c25b369ca93561a45084df073bd267849f38edf7c37c18c614bee2a467`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-A78445F64670","canonical":true,"claim_ids":["C-COMMON-BLOCK"],"claim_statuses":{"C-COMMON-BLOCK":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Erdős Problem #99 — universal common contact bridge is incompatible with C56 transfer

**Date:** 2026-09-10

**Repository base:** `4647f7e53a1be5e073291259b44fb29ed2a64ae3`

**Run type:** C-II exact branch elimination / electrical transfer sign theorem

**Target:** post-C-I maximal-support Target C source; in particular the `s_Z=0` Woodall forest branch

## LEVEL I STATUS

`STILL OPEN`.

C24 leaves a forest-side possibility in which the common bridge-block-tree intersection
`I_*` contains at least one positive contact bridge.  Then every positive diameter
edge crosses the same contact bridge cut.  This report eliminates that possibility
exactly.

The key observation is electrical.  If a positive contact bridge of conductance
`alpha` separates the loaded terminals into complementary boundary intervals `B_L`
and `B_R`, and every selected diameter pair joins `B_L` to `B_R`, then orient all
those diameter pairs from `B_L` to `B_R`.  The two boundary intervals are strictly
linearly separable, so these chord vectors lie in one open half-plane; this is a valid
C53 projective orientation.

For the contact Dirichlet response `Lambda`, let

```math
K=Q^T\Lambda^+Q
```

be C53's diameter-edge transfer kernel.  Unit current sent along any one cross-cut pair
must cross the unique contact bridge.  The discrete maximum principle on the two
bridge sides shows that every other cross-cut terminal pair sees at least the bridge
voltage drop.  Thus

```math
\boxed{K_{ef}\ge 1/\alpha>0\qquad\text{for all selected diameter edges }e,f.}
\tag{CB.1}
```

In particular every off-diagonal entry is positive.  C56, for the same legitimate
projective orientation, proves

```math
\boxed{\min_{e\ne f}K_{ef}\le0.}
\tag{CB.2}
```

For the sufficiently large C-II source there are at least two selected diameter edges,
so (CB.1) and (CB.2) contradict each other.

Therefore:

```math
\boxed{
I_*\text{ contains no positive contact bridge.}
}
\tag{CB.3}
```

Since C24 already proves that `I_*` is a nonempty path in the contact bridge-block
tree, it follows that

```math
\boxed{I_*\text{ is exactly one bridge block}.}
\tag{CB.4}
```

This holds whether the selected diameter graph is cyclic or a forest.  In the Woodall
forest branch it removes the entire universal-straight-common-chain subcase: all
selected diameter routes meet in one common 2-edge-connected contact block instead.

---

## 1. Setup

Fix the relative-interior normalized KKT stress of the restored C-II representative.
Let

- `C_+` be its connected positive contact graph;
- `H_+` be its full positive diameter graph on loaded terminal set `B`;
- `Lambda` be the Dirichlet response of `C_+` on `B`;
- `R=Lambda^+` on the centered terminal space;
- `Q` be the oriented boundary-by-diameter-edge incidence matrix;
- `K=Q^T RQ` be the C53 transfer kernel.

Assume for contradiction that the C24 common route `I_*` contains a positive contact
bridge `uv`.  Removing that bridge partitions the positive contact graph into sides
`L` and `R`.  Put

```math
B_L=B\cap L,
\qquad
B_R=B\cap R.
\tag{1.1}
```

C20/C22 prove that `B_L` and `B_R` are nonempty complementary cyclic intervals in the
strictly convex loaded-boundary order.  Because `uv` lies in every diameter route
`P_h`, every edge of `H_+` has one endpoint in each set.

The post-ZF/C34 regime has `q=|B|>=6`, and ZS gives `h>=ceil(D)` for sufficiently large
sources.  In particular

```math
|H_+|\ge2.
\tag{1.2}
```

The C53 force hull is two-dimensional, so its affine-span hypothesis holds.

---

## 2. Complementary convex boundary intervals are strictly separable

### Lemma CB.1

Let `B_L,B_R` be two nonempty complementary cyclic intervals of the vertices of a
strictly convex polygon.  Then there is a linear functional `ell` such that

```math
\boxed{
ell(r-l)>0\quad\text{for every }l\in B_L,\ r\in B_R.}
\tag{2.1}
```

### Proof

There are exactly two transition boundary edges between the two vertex intervals.
Choose points `x,y` in the relative interiors of those two transition edges.  The line
through `x,y` cuts the boundary of a strictly convex body exactly at `x,y`; the two
open boundary arcs between them lie in the two opposite open half-planes determined by
that line.  One arc contains all vertices of `B_L` and the other all vertices of
`B_R`.

Choose the sign of a normal covector `ell` so that

```math
\ell(r)>c>\ell(l)
```

for every `r in B_R`, `l in B_L`, with `c=ell(x)=ell(y)`.  Then

```math
ell(r-l)>0,
```

proving (2.1).  `square`

### Consequence for C53 orientation

Orient every selected diameter edge `e=rl`, with `r in B_R,l in B_L`, so its oriented
chord vector is

```math
u_e=p_r-p_l.
\tag{2.2}
```

Lemma CB.1 gives `ell(u_e)>0` for every edge.  Thus all oriented chord vectors lie in
one open half-plane.  C53 explicitly permits choosing any projective cut avoiding the
finite chord directions and then orienting every chord into the corresponding open
half-plane.  Choose the cut whose half-plane contains the vectors (2.2).  Therefore
this common cut orientation is a legitimate C53/C56 orientation, not a second
incompatible orientation imposed after the fact.

With this choice, the incidence column of edge `e=rl` is

```math
q_e=\mathbf e_r-\mathbf e_l,
\tag{2.3}
```

and

```math
K_{ef}=q_e^T\Lambda^+q_f.
\tag{2.4}
```

---

## 3. Transfer impedance across a positive bridge is uniformly positive

### Lemma CB.2 — bridge transfer positivity

Let a connected positive weighted graph have a bridge `uv` of conductance `alpha>0`,
with `u` on side `L` and `v` on side `R`.  Let `Lambda` be its Dirichlet response on a
terminal set meeting both sides.  For any two terminal pairs

```math
e=(r,l),\qquad f=(r',l'),
```

with `r,r' in R` and `l,l' in L`, orient their incidence vectors from `L` to `R`:

```math
q_e=\mathbf e_r-\mathbf e_l,
\qquad
q_f=\mathbf e_{r'}-\mathbf e_{l'}.
```

Then

```math
\boxed{
q_e^T\Lambda^+q_f\ge {1\over\alpha}.
}
\tag{3.1}
```

### Proof

Let `V` be a boundary potential vector, extended harmonically to all graph vertices,
for the unit current demand

```math
\Lambda V=q_f.
\tag{3.2}
```

Potentials are defined only up to an additive constant, which does not affect the
voltage differences below.

The only net source is `+1` at `r'` and the only net sink is `-1` at `l'`.  Since the
bridge `uv` is the unique graph edge between the two sides, cut conservation forces
exactly one unit of current through the bridge from `R` to `L`.  Therefore Ohm's law
gives

```math
\boxed{V(v)-V(u)={1\over\alpha}.}
\tag{3.3}
```

Now restrict the electrical problem to the `R` side after deleting the bridge.  There
is one unit source at `r'`, one unit sink at the bridge vertex `v`, and zero injection
at every other vertex.  By the discrete maximum principle, `v` is a global minimum of
the side potential.  Hence

```math
V(r)-V(v)\ge0
\qquad(r\in B_R).
\tag{3.4}
```

Likewise on the `L` side there is one unit source at the bridge vertex `u`, one unit
sink at `l'`, and zero injection elsewhere.  Thus `u` is a global maximum and

```math
V(u)-V(l)\ge0
\qquad(l\in B_L).
\tag{3.5}
```

For any other cross-cut pair `e=(r,l)`, combine (3.3)--(3.5):

```math
\begin{aligned}
V(r)-V(l)
&=[V(r)-V(v)]+[V(v)-V(u)]+[V(u)-V(l)]\\
&\ge {1\over\alpha}.
\end{aligned}
\tag{3.6}
```

Since `V=Lambda^+q_f` modulo constants and `q_e` has zero sum,

```math
V(r)-V(l)=q_e^T\Lambda^+q_f.
```

This proves (3.1).  `square`

### Remarks

1. The inequality is valid also when the two terminal pairs share an endpoint.
2. No circular-planar sign theorem is needed.  The only inputs are the bridge cut,
   positive conductances, cut conservation, and the discrete maximum principle.
3. Equality in (3.1) is allowed when the observed terminals sit electrically at the
   bridge endpoints on their respective sides.  Strict positivity is all that is
   needed.

---

## 4. Contradiction with C56

Apply Lemma CB.2 to the positive contact graph and the common bridge `uv`.  Every
selected diameter edge crosses `(B_L,B_R)`, and Section 2 gives one legal C53
orientation in which all such edges point from `B_L` to `B_R`.  Hence

```math
\boxed{
K_{ef}\ge{1\over\alpha_{uv}}>0
\quad\text{for all }e,f\in H_+.
}
\tag{4.1}
```

Since `|H_+|>=2`,

```math
\boxed{
c:=\min_{e\ne f}K_{ef}>0.}
\tag{4.2}
```

But C56 is an exact theorem for the same C53 edge-space data.  It proves, for every
legitimate common-half-plane projective orientation,

```math
\boxed{c\le0.}
\tag{4.3}
```

Equations (4.2) and (4.3) contradict each other.  Therefore the assumed common
positive-contact bridge cannot exist.

This argument does not invoke C56-Z or any equality case.  It contradicts the first
sign conclusion of C56 before the generic/zero-transfer dichotomy is entered.

---

## 5. C24 consequence

C24 proves that

```math
I_*:=\bigcap_{h\in H_+}P_h
```

is a nonempty path in the contact bridge-block tree.  If it contained two distinct
block nodes, it would contain their intervening bridge edge.  Section 4 excludes every
such common bridge.  Therefore

```math
\boxed{|V(I_*)|=1.}
\tag{5.1}
```

for every sufficiently large two-dimensional C-II source in the restored maximal
support setting.

Thus C24's former split

```text
(A) diameter forest + universal straight common contact chain,
(B) one common bridge block,
```

collapses to the second alternative universally:

```text
all selected diameter routes meet in one common bridge block;
no positive contact bridge is traversed by every selected diameter pair.
```

For Woodall's `s_Z=0` forest phase this is a genuine branch elimination.  The forest
topology survives, but its caterpillar components must be coupled through one common
2-edge-connected positive-contact block rather than one universal bridge corridor.

---

## 6. Regression audit

- **Order-reversing crossing matching.**  C24 correctly warns that a bridge cut need
  not make the diameter graph a star.  CB does not use a star.  It orients every
  cross-cut chord consistently by the geometric separation of the two terminal
  intervals; arbitrary pairwise crossings are allowed.
- **Projective-orientation mismatch.**  This was the September 5 C53 failure mode.  CB
  explicitly proves that the cut orientation lies in one open half-plane, so the same
  orientation is used simultaneously for geometry, the incidence matrix `Q`, the
  transfer kernel `K`, and C56.
- **Single diameter edge.**  C56's off-diagonal minimum needs at least two edges.  The
  large post-ZF source has `h>=ceil(D)`, so this regression is outside the theorem's
  stated sufficiently large scope.
- **Bridge-free contact graph.**  CB is vacuous and leaves the one-block case intact.
- **Contact isolates.**  They are not part of the positive contact graph and play no
  role in the bridge response.  No small-isolate assumption is introduced.
- **Regular odd shell.**  Its positive contact graph is a cycle with no contact bridge,
  so it is retained.

---

## 7. Exact remaining forest obligation

Woodall still permits a caterpillar forest `H` with `d_H` components.  CB now proves
that all its diameter routes meet in one common **bridge block**.  Therefore the
remaining forest mechanism is genuinely two-dimensional at the shared contact core;
it cannot hide in a long one-dimensional universal corridor.

The next direct targets are:

1. combine the common 2-edge-connected hub block with the exact `3d_H` E597 component
   charge and RR/CS bypass cuts to obtain an upper restriction on `d_H` or on
   `e_BB+2s_C`; or
2. use the hub block's circular-planar response to show that the caterpillar forest
   diameter transfer cannot realize the maximal-rank `s_Z=0` Schur defect without a
   forbidden zero-transfer/additive phase.

No such closure is claimed here.

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Suppose one positive contact bridge uv lies in every diameter route.  C20 gives
nonempty complementary loaded boundary intervals B_L,B_R, and every H edge crosses
that cut.

The two intervals are strictly separable by a line through points in the two boundary
transition edges.  Orient every diameter chord from B_L to B_R.  All chord vectors
then lie in one open half-plane, so this is a legitimate single C53 projective
orientation.

Let K=Q^T Lambda^+ Q.  For unit current along any cross-cut diameter pair f, exactly
one unit crosses uv.  If alpha is the bridge conductance, its voltage drop is 1/alpha.
By the maximum principle, every other cross-cut terminal pair e sees that bridge drop
plus two nonnegative side drops.  Hence
    K_ef >= 1/alpha >0
for every e,f.
Thus min_{e!=f} K_ef>0.

C56, for the same legal orientation, proves min_{e!=f}K_ef<=0.  Contradiction.
Therefore no positive contact bridge is common to all diameter routes.  Since C24's
common intersection I_* is a nonempty path in the bridge-block tree, I_* must be one
block.

Next: Woodall forest now means caterpillar diameter components coupled through one
common 2-edge-connected positive-contact hub block; attack that hub with E597 +
RR/CS or the Schur transfer kernel.
```
