<!-- theorem-state: {"artifact_id":"ART-4CF928B28A87","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — the cyclic `d_H=0` KKT polytope is an exact polar polygon

**Date:** 2026-09-09  
**Run type:** exact KKT-cone / polytope classification  
**Target:** Target C C-II cyclic primitive endpoint, `d_H=0`  
**Depends on:** KL cycle localization; EZ strict convexity of beta-functional points; AS uniform interior stress; CY universal contact positivity  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

EZ proves that the unique-cycle beta functionals are represented by the vertices `K_i` of a strictly convex odd polygon and that every normalized KKT extreme kills exactly two cycle edges. This report identifies the **entire** KKT cone and polytope.

Let the unique diameter cycle have odd length `r`, with cycle edges in ordinary cycle/projective order

\[
h_{t_0},h_{t_1},\ldots,h_{t_{r-1}}.
\]

In the signed stress coordinates `(A,c in R^2)` from EZ,

\[
D^2\beta_{t_i}=A-c\cdot K_i.
\]

Then the complete nonnegative equilibrium-stress cone is exactly

\[
\boxed{
\mathcal C
=
\{(A,c):A-c\cdot K_i\ge0\text{ for every }i\}.
}
\tag{PP.1}

No additional contact or pendant-diameter inequality cuts this cone.

Consequently:

1. every unique-cycle coordinate `beta_{t_i}` defines a genuine facet of `C`;
2. the normalized KKT polytope has exactly `r` facets and exactly `r` vertices;
3. its face lattice is combinatorially dual to the strictly convex `K` polygon;
4. the two zero diameter edges at an extreme are exactly adjacent vertices in the convex order of the `K_i`;
5. EZ identifies that convex order as step two in ordinary cycle-edge order.

Thus the extreme zero pairs are exactly

\[
\boxed{
\{h_{t_i},h_{t_{i+2}}\}
\qquad(i\in\mathbb Z/r\mathbb Z).
}
\tag{PP.2}

For `r>=5`, the two deleted cycle edges are nonadjacent and have exactly one cycle edge between them. For `r=3`, PP.2 gives the three possible pairs of triangle edges.

This completely determines the combinatorics of the two-dimensional normalized KKT stress family.

---

## 1. Cycle halfspaces

EZ parametrizes the full three-dimensional signed equilibrium-stress space by `(A,c_x,c_y)` and associates a strictly convex polygon

\[
K=\operatorname{conv}\{K_0,\ldots,K_{r-1}\}
\]

to the unique-cycle diameter coordinates, with

\[
\boxed{
D^2\beta_{t_i}=A-c\cdot K_i.
}
\tag{1.1}

Define the cycle halfspace cone

\[
\mathcal C_{cyc}
:=
\{(A,c):A\ge c\cdot K_i\text{ for all }i\}.
\tag{1.2}

The actual nonnegative KKT cone `C` is contained in `C_cyc`, because every KKT stress has nonnegative cycle coefficients.

AS supplies the uniform full-support stress `x_0`, which lies strictly inside the actual KKT cone and therefore strictly inside every cycle halfspace.

---

## 2. Cycle nonnegativity forces all other coefficients nonnegative

### Theorem PP.1

\[
\boxed{\mathcal C=\mathcal C_{cyc}.}
\]

### Proof

Suppose otherwise. Choose

\[
x\in\mathcal C_{cyc}\setminus\mathcal C.
\]

At least one contact coefficient or pendant-diameter coefficient of `x` is negative.

Consider the segment

\[
x(s)=(1-s)x_0+s x,
\qquad0\le s\le1.
\]

Every cycle coefficient stays nonnegative along the whole segment because `C_cyc` is convex. At `s=0`, every coefficient is strictly positive.

Let `s_*` be the first value at which some non-cycle coefficient reaches zero. Then

- every cycle beta coefficient is nonnegative at `x(s_*)`;
- every contact coefficient is nonnegative;
- every pendant-diameter coefficient is nonnegative;
- at least one contact or pendant coefficient is exactly zero.

The stress `x(s_*)` is nonzero. Indeed, if the segment passed through the origin, `x` would be a negative multiple of the strictly cycle-positive vector `x_0`, contradicting `x in C_cyc` unless `x=0`, which has no negative coordinate.

Thus `x(s_*)` is a nonzero nonnegative equilibrium stress. The virial identity gives positive total diameter mass, so it can be normalized.

CY proves that every contact coefficient of every normalized KKT stress in this cyclic endpoint is strictly positive. KL proves that every pendant diameter coefficient is also strictly positive. Both contradict the defining zero coordinate of `x(s_*)`.

Therefore no such `x` exists and `C_cyc subset C`. The reverse inclusion was immediate. `square`

This argument also explains why contact positivity, although essential mechanically, contributes no additional facet to the stress cone.

---

## 3. Every cycle inequality is a genuine facet

EZ proves every `K_i` is a vertex of the strictly convex polygon `K`. Therefore each `K_i` is exposed: there is a vector `c_i` such that

\[
c_i\cdot K_i
>
c_i\cdot K_j
\qquad(j\ne i).
\]

Set

\[
A_i=c_i\cdot K_i.
\]

Then `(A_i,c_i)` belongs to `C_cyc=C` and satisfies

\[
A_i-c_i\cdot K_i=0,
\]

while every other cycle inequality is strict.

Hence

\[
\boxed{
\beta_{t_i}=0
}
\]

defines a two-dimensional facet of the three-dimensional KKT cone for every `i`.

Thus every actual unique-cycle diameter edge can be switched off somewhere on the KKT boundary; no cycle coordinate is permanently positive.

---

## 4. The cone is the homogenized polar of `K`

Equation PP.1 is the epigraph cone of the support function of `K`:

\[
A\ge h_K(c).
\]

Choose any strictly positive normalization functional on the nonzero KKT cone, for example

\[
\sum_{h\in H}\beta_h=1.
\]

Its affine section is the normalized KKT polytope `S`. Since the section intersects every ray exactly once, `S` has the same face lattice as the projectivized cone.

The cone has one facet for every vertex of `K`. Its extreme rays occur when two adjacent support inequalities of `K` are equalities. Therefore `S` is a convex `r`-gon combinatorially polar to `K`.

In particular

\[
\boxed{
\#\operatorname{vert}(\mathcal S)
=
\#\operatorname{edge}(\mathcal S)
=r.
}
\tag{4.1}

No genericity assumption is involved; strict convexity of `K` gives the exact simple-polygon face lattice.

---

## 5. Exact zero-pair classification

EZ proves that the boundary order of the `K` vertices is

\[
K_i,
K_{i+2},
K_{i+4},\ldots
\tag{5.1}
\]

with indices modulo the odd integer `r`.

Adjacent facets of the polar stress polygon therefore correspond to the pair

\[
K_i,K_{i+2}.
\]

At their intersection ray,

\[
\beta_{t_i}=\beta_{t_{i+2}}=0.
\]

EZ excludes every third zero coordinate. Hence:

### Theorem PP.2 — complete extreme list

The `r` normalized KKT extremes are indexed by `i in Z/rZ`. Extreme `s_i` has

\[
\boxed{
Z(s_i)=\{h_{t_i},h_{t_{i+2}}\}.
}
\tag{5.2}

No other zero pair occurs.

Because consecutive unique-cycle edges in the `t_i` order share a cycle vertex, this is also the ordinary graph-cycle edge order. For `r>=5`, the removed pair is separated by exactly the surviving edge `h_{t_{i+1}}` and the two removed edges do not share a vertex.

---

## 6. Structure of every extreme diameter forest

Deleting `h_{t_i}` and `h_{t_{i+2}}` from the connected unicyclic diameter graph breaks the unique cycle in two places. The surviving graph is a forest with exactly two components.

For `r>=5`, one component contains the one-edge cycle segment

\[
h_{t_{i+1}}
\]

and its two cycle endpoints, together with all pendant diameter leaves attached to those two endpoints. The other component contains the complementary `r-3` cycle edges and their pendant leaves.

Thus every extreme selected diameter graph has one distinguished **short component** supported on two adjacent cycle vertices.

This is substantially sharper than the abstract statement that an extreme support is some diameter forest.

For `r=3`, deleting two triangle edges leaves the third cycle edge; selected edge-cover then forces the third triangle vertex to be covered by a pendant diameter edge. PP itself does not need to classify which pendant branch supplies that cover.

---

## 7. Interaction with CG and circuit rigidity

Every extreme stress still satisfies CG:

\[
\Omega_s\succeq0,
\qquad
\ker\Omega_s=\operatorname{span}\{1,P_x,P_y\},
\qquad
\operatorname{rank}\Omega_s=q-3.
\]

EZ gives that its mixed support is an actual-coordinate rigidity circuit with `2q-2` rows.

PP now gives an exact list of these circuits: there are precisely `r`, obtained by deleting the step-two cycle pairs (5.2). All pendant diameter rows occur in every one of the `r` circuits.

Therefore the two-dimensional stress polytope is no longer an uncontrolled family. It is one explicit `r`-cycle of maximal-rank PSD rigidity circuits.

---

## 8. What this removes

Before PP, the remaining KKT ambiguity was:

```text
which cycle beta coordinates can reach zero?
which pairs meet at extremes?
could some cycle coordinates be permanently positive?
```

All three are now resolved:

```text
every cycle beta coordinate is a facet;
there are exactly r KKT extremes;
extreme i deletes exactly cycle edges i and i+2;
all contacts and all pendant diameters remain positive everywhere.
```

The next obstruction must therefore use the geometry or mechanics of this explicit circuit cycle, not stress-polytope combinatorial uncertainty.

---

## 9. Next theorem

For `r>=5`, each extreme circuit isolates a short diameter-tree component on two adjacent cycle vertices. The strongest next target is:

> combine CG maximal-rank PSD transfer with that two-vertex short component and the circular contact cycle to derive a forbidden response/cut pattern, or a source-preserving finite release.

Equivalently, intersect the `r` exact circuit constraints around the stress polygon and exploit that the short component walks once around the unique diameter cycle.

This is now a finite local-to-global problem on the Reuleaux/Reinhardt skeleton rather than a continuous stress-family problem.

---

## 10. Regression audit

- PP does not assume regularity, periodicity, or a uniform gap composition.
- The proof that `C=C_cyc` uses the existing CY/KL strict-positivity theorems and the uniform AS interior stress; it does not assume positivity outside the actual KKT cone.
- The normalized section need not be `A=1`; any positive normalization has the same face lattice.
- For `r=3`, the step-two rule gives all three pairs, as it should.
- No claim is made that an extreme forest is itself in the C56 zero-transfer phase; CG proves the opposite.

---

## 11. Compact handoff

```text
EZ gives D^2 beta_{t_i}=A-c.K_i with K_i the vertices of a strictly convex odd polygon.
Let C_cyc={A-c.K_i>=0 for all i}. Actual KKT cone C is contained in C_cyc.

AS gives a strictly positive interior stress x0. If x in C_cyc had a negative contact or
pendant-beta coordinate, move from x0 toward x until the first such coordinate hits zero.
Cycle betas remain nonnegative. The first-hit stress is a nonzero nonnegative equilibrium
stress with a zero contact or pendant beta; after normalization this contradicts CY or KL.
Hence C=C_cyc.

Since every K_i is exposed, every beta_{t_i}=0 is a genuine facet. Thus the normalized
KKT polytope is the polar polygon of K and has exactly r vertices. EZ gives K convex order
    i,i+2,i+4,...,
so extreme i has exactly
    beta_{t_i}=beta_{t_{i+2}}=0.
For r>=5 these removed cycle edges are nonadjacent with exactly one surviving cycle edge
between them. Each extreme diameter forest has two components, one supported on that
short two-cycle-vertex segment plus its pendant leaves.
```
