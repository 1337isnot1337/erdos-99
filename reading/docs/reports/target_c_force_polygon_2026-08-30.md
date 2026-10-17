> Generated reading edition · [exact source](../../../docs/reports/target_c_force_polygon_2026-08-30.md) · source SHA-256 `680a5536db5d1d88fefd8bf085e9028d7cedef9c0b00e09e7e001768b7cbfee7`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-5476B6897067","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C addendum: reciprocal force polygon and contact response

**Date:** 2026-08-30  
**Repository state:** `research/target-c-force-hull-v2-2026-08-30`  
**Run type:** proof / structural reduction / literature no-go  
**Target:** Level I candidate route C  
**Depends on:** `target_c_force_hull_2026-08-30.md`, `target_c_critical_cone_duality_2026-08-30.md`, `target_c_shear_separator_2026-08-30.md`  
**External literature:** Rote--Schulz (2009), used only as a no-go against abstract positive-statics arguments  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

This note derives two exact global objects from a normalized KKT stress:

1. a convex reciprocal **force polygon** whose mixed area with the KKT force hull is
   exactly `D^2/2`; and
2. a circular-planar electrical response identity equating the contact-network
   Dirichlet-to-Neumann map and the diameter network on the two coordinate functions.

The force polygon gives a new scalar invariant

$$
\sqrt3\,D\le P_{\rm force}\le2D,
$$

with an exact equality classification at the upper endpoint.  These statements use
only the actual global-minimizer KKT stress and convex geometry.  They do not use the
Target A lattice scaffold or the Target B rhombic decomposition.

A literature audit also removes a tempting false route: abstract moment-free planar
loads can often be resolved by positive interior stresses on suitable
pseudo-triangulations.  Therefore the Target C separator cannot be excluded by
"positive planar statics" alone.  Any closing theorem must use the fact that our
radial carrier is the **actual unit-contact/diameter framework** of a global minimizer.

---

## 1. Boundary reactions and the force hull

Fix one normalized KKT stress `(\alpha,\beta)`.  Let

$$
C_+=\{ij\in C:\alpha_{ij}>0\},
\qquad
H_+=\{ij\in H:\beta_{ij}>0\},
$$

let `B_+` be the endpoint set of `H_+`, and put

$$
F:=\operatorname{conv}B_+.
\tag{C10.1}
$$

By Theorem C3.1 of `target_c_force_hull_2026-08-30.md`,

$$
F=\operatorname{conv}V(C_+),
\qquad
\operatorname{diam}F=D.
\tag{C10.2}
$$

Every point of `B_+` is a vertex of `F`.

For each `b\in B_+`, define its total positive diameter reaction

$$
\boxed{
g_b:=\sum_{bk\in H_+}\beta_{bk}(b-k).}
\tag{C10.3}
$$

Vertex equilibrium gives the equivalent contact formula

$$
\boxed{
g_b=\sum_{bc\in C_+}\alpha_{bc}(b-c).}
\tag{C10.4}
$$

The diameter formula is the useful one for convexity.

### Lemma C10.1 (strict normal-cone location)

For every `b\in B_+`, `g_b\ne0` and

$$
\boxed{
g_b\cdot(b-x)>0
\qquad(x\in F\setminus\{b\}).}
\tag{C10.5}
$$

Hence `g_b` lies in the relative interior of the outward normal cone of `F` at `b`.
Moreover

$$
\boxed{\sum_{b\in B_+}g_b=0.}
\tag{C10.6}
$$

#### Proof

If `bk\in H_+`, then `|b-k|=D`.  Applying Lemma C5 from the preceding report with
`p=b`, `q=k` gives, for every `x\in F\subseteq\operatorname{conv}A`,

$$
\frac{b-k}{D}\cdot(b-x)
\ge\frac{|b-x|^2}{2D}.
$$

Thus

$$
(b-k)\cdot(b-x)\ge\frac{|b-x|^2}{2}>0
\qquad(x\ne b).
\tag{C10.7}
$$

Every coefficient in (C10.3) is positive.  Summing (C10.7) over the positive
diameter edges incident to `b` proves (C10.5), hence also `g_b\ne0`.

For (C10.6), every diameter edge `bk` contributes
`\beta_{bk}(b-k)` at `b` and the opposite vector at `k`; the pair cancels. `\square`

---

## 2. The reciprocal force polygon

Order the vertices `b_1,...,b_q` of `F` counterclockwise.  The interiors of their
normal cones occur in the same cyclic order and are pairwise disjoint.  Therefore the
nonzero vectors

$$
e_i:=Jg_{b_i}
\tag{C10.8}
$$

have strictly cyclically ordered directions.  By (C10.6),

$$
\sum_i e_i=0.
\tag{C10.9}
$$

Consequently the vectors `e_i`, in that order, are the oriented side vectors of a
convex polygon, unique up to translation.  Denote it by

$$
\boxed{F^*.}
\tag{C10.10}
$$

For a counterclockwise polygon, the outward normal to the side `e_i=Jg_{b_i}` is
`g_{b_i}/|g_{b_i}|`.  Thus the side normals of `F^*` lie strictly inside the vertex
normal cones of `F`: the two polygons are reciprocal at the level of their normal
fans.

### Theorem C10 (exact mixed-area identity)

The force polygon satisfies

$$
\boxed{
2V(F,F^*)=D^2,
\qquad
V(F,F^*)=\frac{D^2}{2},
}
\tag{C10.11}
$$

where `V` is planar mixed area.  Equivalently,

$$
\boxed{
\sum_{b\in B_+}|g_b|\,
h_F\!\left(\frac{g_b}{|g_b|}\right)
=D^2.
}
\tag{C10.12}
$$

#### Proof

For convex polygons, the first variation of area under Minkowski addition gives

$$
2V(F,F^*)
=
\sum_{\text{sides }e\text{ of }F^*}
|e|\,h_F(n_e),
\tag{C10.13}
$$

where `n_e` is the outward unit normal of the side.  Here the side indexed by `b` has
length `|g_b|` and normal `g_b/|g_b|`.  Lemma C10.1 says this normal supports `F`
uniquely at `b`, so its contribution is

$$
|g_b|\,h_F(g_b/|g_b|)=g_b\cdot b.
$$

Hence

$$
2V(F,F^*)=\sum_b g_b\cdot b.
\tag{C10.14}
$$

Now group the right side by diameter edges.  An edge `bk\in H_+` contributes

$$
\beta_{bk}(b-k)\cdot b
+
\beta_{bk}(k-b)\cdot k
=
\beta_{bk}|b-k|^2
=
\beta_{bk}D^2.
$$

Because `\sum_{H_+}\beta=1`, (C10.14) equals `D^2`. `\square`

The identity is translation invariant: translating `F` by `a` changes the right side
of (C10.14) by `a\cdot\sum_b g_b=0`.

---

## 3. Exact perimeter interval and equality cases

Write

$$
P_*:=\operatorname{per}(F^*)=\sum_{b\in B_+}|g_b|.
\tag{C10.15}
$$

### Theorem C10.2 (force-perimeter bounds)

For every normalized KKT stress,

$$
\boxed{
\frac{D^2}{R(F)}
\le
P_*
\le
2D,
}
\tag{C10.16}
$$

where `R(F)` is the circumradius of the force hull.  In particular, planar Jung gives

$$
\boxed{
\sqrt3\,D\le P_*\le2D.
}
\tag{C10.17}
$$

#### Proof

For the upper bound, (C10.3) and the triangle inequality give

$$
|g_b|
\le
D\sum_{bk\in H_+}\beta_{bk}.
$$

Sum over `b`.  Every diameter edge is counted at its two endpoints, so

$$
P_*
\le
2D\sum_{H_+}\beta
=
2D.
\tag{C10.18}
$$

For the lower bound, let `o` be a center of a smallest enclosing circle of `F`, of
radius `R(F)`.  By (C10.6) and (C10.14),

$$
D^2
=
\sum_b g_b\cdot(b-o)
\le
R(F)\sum_b|g_b|
=
R(F)P_*.
\tag{C10.19}
$$

This proves the first inequality.

For completeness, Jung's bound `R(F)\le D/\sqrt3` has a short planar proof.  A
minimal enclosing circle is supported either by two antipodal points, giving
`R\le D/2`, or by three boundary points whose center lies in their triangle.  In the
three-point case one of the three central angles is at least `2\pi/3`, so the
corresponding chord has length at least `\sqrt3 R`; that chord is at most the diameter
`D`.  Hence `R\le D/\sqrt3`.  Substitute into (C10.16). `\square`

### Theorem C10.3 (upper equality iff the positive diameter graph is a matching)

$$
\boxed{
P_*=2D
\iff
H_+\text{ is a matching on }B_+.
}
\tag{C10.20}
$$

#### Proof

The deficit in (C10.18) is the sum, over `b`, of the nonnegative triangle-inequality
deficits

$$
D\sum_{bk}\beta_{bk}
-
\left|\sum_{bk}\beta_{bk}(b-k)\right|.
\tag{C10.21}
$$

Therefore equality globally holds exactly when equality holds at every `b`.  Equality
in the Euclidean triangle inequality for positive coefficients requires all incident
vectors `b-k` to have the same direction.  They also all have the same length `D`.
Two distinct partners cannot therefore occur: a ray from `b` contains at most one
point at distance exactly `D`.  Thus every `b` has exactly one positive diameter
partner and `H_+` is a matching.

Conversely, if `H_+` is a matching, each `g_b` consists of one vector of length
`D\beta_h`.  Summing over the two endpoints of every edge gives

$$
P_*=2D\sum_h\beta_h=2D.
$$
`\square`

### Corollary C10.4 (minimum-circumradius branch)

If

$$
R(F)=D/2,
\tag{C10.22}
$$

then

$$
P_*=2D,
$$

`H_+` is a matching, all vertices of `F` lie on the circle of radius `D/2` about its
circumcenter, and every positive diameter edge joins antipodal points of that circle.
Consequently `F` is centrally symmetric.

#### Proof

Theorem C10.2 gives `P_*\ge D^2/(D/2)=2D`, so equality holds throughout and Theorem
C10.3 makes `H_+` a matching.

Let `o` be the circumcenter.  Every `b\in B_+` has a positive diameter partner `k`.
Both lie in the closed radius-`D/2` disk and `|b-k|=D`, so

$$
D=|b-k|\le|b-o|+|k-o|\le D.
$$

Equality forces `|b-o|=|k-o|=D/2` and `k-o=-(b-o)`.  Hence every vertex is paired
with its antipode. `\square`

This exact branch includes the unit square regression, so it is not itself a
contradiction.  It is, however, a complete geometric classification of the extremal
force-perimeter case when the force hull has minimum possible circumradius.

---

## 4. Cancellation deficit

The force-perimeter deficit has a concrete meaning:

$$
\boxed{
2D-P_*
=
\sum_{b\in B_+}
\left[
D\sum_{bk\in H_+}\beta_{bk}
-
\left|\sum_{bk\in H_+}\beta_{bk}(b-k)\right|
\right].
}
\tag{C10.23}
$$

It measures only cancellation among distinct positive diameter reactions at common
hull vertices.  No contact-network quantity appears in (C10.23).

At the same time (C10.16) gives

$$
\boxed{
2D-P_*
\le
2D-\frac{D^2}{R(F)}.
}
\tag{C10.24}
$$

Thus any theorem forcing

$$
R(F)=\frac D2+o(D)
$$

would force `P_*=2D-o(D)` and hence asymptotically small total diameter-reaction
cancellation.  This observation is conditional only: the current theorem state does
**not** show that the force hull has near-minimal circumradius or near-maximal area.
A large KKT-invisible rattler population can separate `F` from the geometric hull.
That is exactly why this does not silently re-import Target A's unresolved capacity
problem.

---

## 5. The contact network as an electrical network

The reciprocal polygon has a second exact formulation.  Regard every positive contact
`ij\in C_+` as an electrical edge of conductance `\alpha_{ij}`.  Let

$$
V_+:=V(C_+),
\qquad
B:=B_+,
\qquad
I:=V_+\setminus B.
$$

Let `L_C` be the weighted graph Laplacian of `C_+`.

Every nontrivial component of `C_+` contains at least two vertices of `B` by canonical
Proposition 5.4.  Hence the Dirichlet principal block `L_C[I,I]` is nonsingular.
Define the Kron-reduced/Dirichlet-to-Neumann response matrix

$$
\boxed{
\Lambda
=
L_C[B,B]
-
L_C[B,I]L_C[I,I]^{-1}L_C[I,B].
}
\tag{C11.1}
$$

Let `L_H` be the weighted Laplacian on `B` whose edges are the positive diameter pairs
`H_+` with conductances `\beta_h`.

Write `P_B` for the `|B|\times2` matrix whose row at `b` is the coordinate vector
`p_b`.

### Theorem C11 (force-hull response identity)

$$
\boxed{
\Lambda\mathbf1=L_H\mathbf1=0,
\qquad
\Lambda P_B=L_H P_B.
}
\tag{C11.2}
$$

Equivalently,

$$
\boxed{
M:=\Lambda-L_H
\quad\text{satisfies}\quad
M\mathbf1=0,
\qquad
MP_B=0.
}
\tag{C11.3}
$$

Thus `M` is an exact self-stress matrix on the convex boundary point set `B`: it
annihilates every affine scalar function on the force hull.

Moreover

$$
\boxed{
P_B^{\mathsf T}\Lambda P_B
=
P_B^{\mathsf T}L_HP_B
=
\sum_{ij\in C_+}\alpha_{ij}(p_i-p_j)(p_i-p_j)^{\mathsf T}
=
\sum_{ij\in H_+}\beta_{ij}(p_i-p_j)(p_i-p_j)^{\mathsf T}.
}
\tag{C11.4}
$$

#### Proof

At every interior vertex `i\in I`, no positive diameter edge is incident.  KKT
equilibrium therefore gives

$$
\sum_{j:ij\in C_+}\alpha_{ij}(p_i-p_j)=0,
$$

which is exactly

$$
(L_CP)_I=0.
\tag{C11.5}
$$

Thus the two coordinate functions on the contact framework are the harmonic extensions
of their boundary values `P_B`.  Eliminating the interior variables gives boundary
contact current

$$
(L_CP)_B=\Lambda P_B.
\tag{C11.6}
$$

At a boundary vertex, KKT equilibrium says this contact current equals the positive
diameter reaction

$$
\sum_{k:bk\in H_+}\beta_{bk}(b-k),
$$

which is precisely `(L_HP_B)_b`.  This proves the coordinate identity in (C11.2).
Both Laplacians annihilate constants, giving the first identity.

For (C11.4), the Dirichlet energy of the harmonic coordinate extension is

$$
P_B^{\mathsf T}\Lambda P_B
=
\sum_{ij\in C_+}\alpha_{ij}(p_i-p_j)(p_i-p_j)^{\mathsf T}.
$$

The analogous edge expansion for `L_H` gives the diameter sum.  Equality also follows
from (C11.2), and it is the canonical KKT tensor identity restricted to the positive
supports. `\square`

### Distinction from Target A's Schur response

The matrix `\Lambda` in C11 is **not** the Target A scaffold Schur matrix.  It is the
ordinary electrical response of the actual positive unit-contact framework of the
source minimizer.  No independent smaller optimum, triangular lattice, matching
matrix, or conflict graph is present.

This gives a second Target C language:

$$
\boxed{
\text{actual contact-network response}
\times
\text{affine coordinate data}
=
\text{actual diameter-network response}.
}
\tag{C11.7}
$$

The identity is exact but only on the three-dimensional affine data space spanned by
`1,x,y`; it does not say `\Lambda=L_H` as matrices when `|B|>3`.

---

## 6. Literature no-go: abstract positive statics is too flexible

Günter Rote and André Schulz, *Resolving Loads with Positive Interior Stresses*, WADS
2009, prove that every moment-free planar load admits, under their genericity
framework, a pointed pseudo-triangulation resolving the load with nonnegative interior
stress; for loads supported only on convex-hull vertices they identify a weighted
Delaunay construction.  Their paper also invokes the Maxwell--Cremona correspondence
between planar equilibrium stresses and polyhedral liftings.

The exact relevance here is negative.  The tangential load produced by Theorem C9 is
moment-free by construction: its total force is zero and `\sum_h\gamma_h=0` is its
total torque condition.  Therefore a proof of Target C4 cannot proceed from the bare
principle

```text
moment-free tangential hull load
+ nonnegative radial interior stress
is impossible in the plane.
```

That principle is false in broad generality.

What Rote--Schulz do **not** supply is a realization using our pre-existing unit-contact
edges, all of exact length one, together with our pre-existing diameter edges of exact
length `D`, inside a globally minimum-diameter packing.  Those are the properties a
Target C contradiction must exploit.

Accordingly, the separator theorem should be combined with one of:

1. the exact unit-length geometry and triangle-free angular gaps of `C`;
2. the diameter support inequality C5 and cyclic order of `B_*`;
3. the reciprocal mixed-area identity C10.11;
4. the actual contact response identity C11.2; or
5. cross-cardinality/global insertion information such as Theorem C2.

Generic Maxwell--Cremona or positive-stress existence alone is a dead route.

---

## 7. Revised Target C program

The current Target C stack now has three exact layers.

### Layer 1: support/core

- C1: contact-preserving diametral hull saturation;
- C3-C4: finite contraction rigidity and the canonical force hull.

### Layer 2: first-order duality

- C6: maximal KKT support is exactly the set frozen on the fixed-`D` critical cone;
- C7: common diameter angular rate integrates the simultaneous weak release;
- C9: failure produces a zero-torque tangential diameter load with a nonnegative
  radial carrier.

### Layer 3: convex/electrical boundary geometry

- C10: the diameter reactions close to a convex reciprocal polygon with
  `V(F,F^*)=D^2/2` and `sqrt(3)D<=per(F^*)<=2D`;
- C11: the actual positive contact network has a Dirichlet-to-Neumann response matching
  the diameter network on affine coordinate data.

The shortest plausible new closing theorem is now one of the following.

> **Target C5a (unit-network separator exclusion).**  Show that a triangle-free
> unit-distance planar network satisfying C10-C11 cannot carry the nontrivial
> tangential separator C9 once `n` is sufficiently large and the source is globally
> diameter-minimal.

or

> **Target C5b (force-hull bulk theorem).**  Show that failure of C5a forces only
> `O(D)` points outside the KKT-positive contact network.  Then global packing density
> applies to the force hull itself; the reciprocal perimeter deficit (C10.24) becomes
> boundary-order currency rather than an uncontrolled bulk error.

C5b would connect to the old rattler issue, but through a new invariant: KKT force
support and reciprocal convex geometry rather than an independent lattice scaffold.

---

## 8. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

New C10 reciprocal polygon:
For any normalized KKT stress, let g_b=sum_{bk in H+} beta_bk(b-k) at every positive
diameter endpoint and F=conv B+.  Each g_b lies strictly inside the outward normal cone
of F at b and sum_b g_b=0.  The side vectors J g_b therefore form a convex force
polygon F*.  Exact mixed area:
    2 V(F,F*) = sum_b g_b dot b = D^2.
Its perimeter P*=sum|g_b| satisfies
    D^2/R(F) <= P* <= 2D,
so by planar Jung
    sqrt(3)D <= P* <= 2D.
Upper equality holds iff H+ is a matching.  If R(F)=D/2, then F is centrally symmetric,
all vertices lie on the radius-D/2 circle, and positive diameter edges are antipodal.

New C11 contact response:
With conductances alpha on C+, eliminate interior vertices I=V(C+)\B+ to obtain the
Dirichlet response Lambda.  Let L_H be the beta-weighted diameter Laplacian on B+.
Then
    Lambda 1=L_H 1=0,
    Lambda P_B=L_H P_B.
Thus Lambda-L_H annihilates all affine coordinate data on the convex force-hull
boundary, and both networks have exactly the same coordinate-energy tensor.

Literature no-go:
Rote--Schulz 2009 show broad moment-free loads can be resolved by positive interior
stresses on suitable pointed pseudo-triangulations.  Therefore generic positive planar
statics / Maxwell--Cremona cannot by itself exclude the C9 separator.  A proof must use
the actual unit-contact graph, exact lengths, triangle-freeness, and global optimality.

Next viable targets:
C5a exclude C9 using C10-C11 plus unit-distance/diameter geometry, or
C5b prove all but O(D) source points lie in the KKT-positive force network so that the
force hull itself inherits bulk packing density.
```
