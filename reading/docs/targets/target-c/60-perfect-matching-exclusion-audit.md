> Generated reading edition · [exact source](../../../../docs/targets/target-c/60-perfect-matching-exclusion-audit.md) · source SHA-256 `76e001e06be0fe9e4cb15ca37014e7cd42aa8325bd1bf5a07c7f22645530c70b`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 12 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

# Target C — independent perfect-matching branch exclusion

**Date:** 2026-09-11  
**LEVEL I STATUS:** **STILL OPEN.**  
**Disposition:** the post-ZF branch in which the full actual diameter graph is a perfect matching is excluded for all sufficiently large survivors.

This module independently reconstructs the load-bearing part of
`docs/reports/target_c_matching_branch_externalization_2026-09-09.md` and combines it with the canonical full-force area floor from
`59-difference-body-density-audit.md`.

The proof does **not** promote the old external-rattler handoff, does not use the annular Voronoi theorem, and does not use any KKT weight floor. The contradiction is entirely inside the actual force hull.

## 1. Canonical post-ZF setting

Let `A` be the canonical contact-minimal, then diameter-pair-minimal triangle-free C-II survivor. Choose a relative-interior normalized KKT stress. Then

- every actual unit contact is positive;
- every actual diameter edge is positive;
- the positive contact graph `G=C` has one connected nontrivial component;
- its convex hull is the two-dimensional force hull `F` of diameter `D`;
- the loaded endpoint set `B` is exactly the force-hull vertex set;
- `q:=|B|` and `h:=|H|`;
- canonical ZR/ZF gives
  ```math
  s_Z:=e+h-(2v-2)\ge0.
  \tag{M.1}
  
  ```

Assume in this module that the **full actual diameter graph `H` is a perfect matching**. Then every loaded endpoint has degree one in `H`, so

```math
\boxed{q=2h.}
\tag{M.2}
```

We show that this forces an exact pure-rhombic force hull whose area is too small for the canonical post-ZF full-force area theorem.

## 2. Bounded contact faces are simple strict convex unit polygons

We recheck the C51 fact needed below so that the matching proof does not depend on an unaudited face label.

Let `x` be a contact vertex and `S` one component of `G-x`. Suppose `S` contained no loaded vertex. For the relative-interior normalized KKT stress every contact edge has positive weight. At every vertex `p in S` there is no diameter-force term, so equilibrium is

```math
\sum_{q:\,pq\in C}\alpha_{pq}(p-q)=0,
\qquad \alpha_{pq}>0.
```

Thus each Euclidean coordinate is a weighted harmonic function on `S`. Because `S` is a component of `G-x`, its only possible contact boundary outside `S` is the single vertex `x`. The discrete maximum principle therefore forces both coordinate functions to equal their boundary values at `x` throughout `S`. Every vertex of `S` would coincide with `x`, contradicting distinct source points. Hence

```math
\boxed{\text{every component of }G-x\text{ contains a loaded force-hull vertex}.}
\tag{M.3}
```

If the boundary walk of a bounded face repeated a vertex `x`, standard plane block topology would cut off a component of `G-x` entirely inside that bounded face region. Such a component contains no force-hull vertex, contradicting M.3. Therefore every bounded face boundary is a simple cycle.

At an unloaded face vertex, all contact directions lie outside the open face sector. A reflex face angle would place all positive contact-force directions in an open half-plane, so their positive equilibrium sum could not vanish. An angle equal to `pi` would force every contact direction onto one line; unit separation then permits at most two unit neighbors, contradicting the canonical C-II unloaded-degree lower bound `3`.

At a loaded vertex, the whole embedded contact graph lies inside the convex force hull and the bounded face sector lies inside the force-hull tangent cone, whose opening is strictly below `pi`.

Thus every bounded face is a simple strictly convex unit-edge polygon. In particular:

- every bounded face has degree at least four by triangle-freeness;
- every bounded quadrilateral face is a strict convex unit rhombus.

## 3. Exact Euler/terminal partition from canonical ZF

Let

- `b` be the outer-face boundary-walk length, with multiplicity;
- `N_b` be the number of bounded faces;
- 

```math
  Q:=\sum_{f\text{ bounded}}(\deg f-4)\ge0.
  
```

Euler and face incidence give

```math
N_b=e-v+1,
\qquad
2e=b+4N_b+Q,
```

hence

```math
\boxed{e=2v-2-{b+Q\over2}.}
\tag{M.4}
```

Insert M.4 into the definition M.1 of `s_Z`:

```math
\boxed{{b+Q\over2}=h-s_Z.}
\tag{M.5}
```

Every loaded vertex is a force-hull vertex and therefore occurs on the outer-face walk, so

```math
\boxed{b\ge q.}
\tag{M.6}
```

Put

```math
x_B:=b-q\ge0.
```

Let `f` be the number of bounded nonquadrilateral faces. Each such face has degree at least five, so if

```math
g_F:=Q-f,
```

then `g_F>=0` and

```math
Q=f+g_F.
```

Finally put

```math
d_H:=q-h\ge0,
```

the ordinary diameter-graph edge deficit. Equations M.5–M.6 give

```math
q+x_B+f+g_F
=b+Q
=2h-2s_Z
=2q-2d_H-2s_Z,
```

so the exact nonnegative terminal partition is

```math
\boxed{
q=x_B+f+g_F+2d_H+2s_Z.
}
\tag{M.7}
```

No older ZT report is required for M.7; it is Euler plus canonical ZF.

Under the perfect-matching hypothesis M.2,

```math
d_H=q-h={q\over2}.
```

Substitute in M.7:

```math
q=x_B+f+g_F+q+2s_Z.
```

Every displayed defect is nonnegative, hence

```math
\boxed{x_B=f=g_F=s_Z=0.}
\tag{M.8}
```

Therefore

```math
\boxed{b=q,\qquad Q=0.}
\tag{M.9}
```

## 4. The contact core is a strict unit-rhombic disk

The outer-face walk has `b=q` edge occurrences and contains all `q` distinct force-hull vertices. Hence each loaded hull vertex occurs exactly once and no other vertex occurs on that walk. Thus the outer-face walk is the simple force-hull cycle in cyclic order.

Every outer edge is an actual contact and has length one. Consequently

```math
\boxed{\operatorname{per}(F)=q.}
\tag{M.10}
```

Because `Q=0`, every bounded face has degree four. Section 2 makes each one a strict convex unit rhombus. Every face boundary, including the outer face, is a simple cycle, so the plane contact graph is 2-connected. Its bounded rhombi tile the whole convex force hull.

Let `R` denote the number of bounded rhombi. Then

```math
\boxed{
\operatorname{area}(F)
=\sum_{j=1}^{R}\operatorname{area}(\mathcal R_j)
\le R,
}
\tag{M.11}
```

because a unit rhombus has area at most one.

## 5. Rhombus trains and the Mantel bound

Join the midpoints of opposite edges across every rhombus. Equivalently, make a graph whose vertices are the contact edges and whose links pair opposite edges of each rhombus.

Opposite edges are parallel, so each connected component has one fixed unoriented transverse edge direction `u`. In a strict triangle-free unit rhombus, both diagonals exceed one. Therefore the acute projective angle `delta` between its two edge directions satisfies

```math
{\pi\over3}<\delta\le{\pi\over2}.
\tag{M.12}
```

Orient `u`. Passage between the midpoints of the two opposite `u`-edges is parallel to the other edge direction and makes angle strictly below `pi/6` with the normal `Ju`. Its projection onto `Ju` is strictly positive. Hence a train component cannot close into a cycle; in this rhombic disk it is a path from one boundary edge to another.

Every boundary edge belongs to exactly one train endpoint and every train has exactly two boundary endpoints. Since the boundary has `q` edges,

```math
\boxed{T={q\over2}.}
\tag{M.13}
```

If two trains cross in a rhombus, their transverse projective directions differ by more than `pi/3`. The same narrow-cone monotonicity used above, projected onto the bisector of their two normals, makes the two complete train centerlines graphs with strictly ordered slope intervals. Their difference is strictly monotone, so two trains cross at most once.

Three trains cannot cross pairwise: three directions on the projective circle of circumference `pi` cannot have all three cyclic gaps strictly larger than `pi/3`.

Thus the train-crossing graph is simple and triangle-free. Its vertices are the `T` trains and its edges are exactly the `R` rhombi. Mantel's theorem gives

```math
\boxed{
R\le {T^2\over4}={q^2\over16}.
}
\tag{M.14}
```

Combining M.11 and M.14,

```math
\boxed{
\operatorname{area}(F)\le {q^2\over16}.
}
\tag{M.15}
```

Cauchy's convex perimeter-diameter inequality and M.10 give

```math
q=\operatorname{per}(F)\le\pi D.
```

Therefore every perfect-matching post-ZF survivor satisfies the exact force-hull area upper bound

```math
\boxed{
\operatorname{area}(F)
\le {\pi^2\over16}D^2.
}
\tag{M.16}
```

## 6. Exact positive separation from the canonical full-force area floor

The canonical theorem `C-FS-STABILITY` says that every unbounded post-ZF survivor sequence satisfies

```math
\liminf {\operatorname{area}(F)\over D^2}
\ge
A_{SC}:={2\rho+\sin(2\rho)\over4},
\tag{M.17}
```

where `rho` is the unique positive root of

```math
\rho=\cos\rho.
```

We now certify, with rational inequalities only, that

```math
\boxed{A_{SC}>{\pi^2\over16}.}
\tag{M.18}
```

Let

```math
r_0={369\over500}.
```

The alternating cosine series gives

```math
\cos r_0
>
1-{r_0^2\over2}+{r_0^4\over24}-{r_0^6\over720}.
```

Direct rational subtraction yields

```math
1-{r_0^2\over2}+{r_0^4\over24}-{r_0^6\over720}-r_0
=
{2266859362173191\over1250000000000000000}>0.
```

Thus `cos r_0>r_0`. Since `cos x-x` is strictly decreasing on `(0,pi/2)`,

```math
\boxed{\rho>r_0.}
\tag{M.19}
```

The function

```math
A(x)={2x+\sin(2x)\over4}
```

has derivative `cos^2 x>=0` on `[0,pi/2]`, so `A_SC=A(rho)>A(r_0)`.

Put

```math
x=2r_0={369\over250}.
```

The alternating sine series gives

```math
\sin x
>
x-{x^3\over6}+{x^5\over120}-{x^7\over5040}.
```

The amount needed to prove `A(r_0)>121/196` is

```math
4\cdot{121\over196}-2r_0
={12169\over12250}.
```

Again direct rational subtraction gives

```math
\left(x-{x^3\over6}+{x^5\over120}-{x^7\over5040}\right)
-{12169\over12250}
=
{486315765024227353\over239257812500000000000}>0.
```

Hence

```math
A(r_0)>{121\over196}.
```

Finally the classical rational bound `pi<22/7` gives

```math
{\pi^2\over16}<{121\over196}.
```

Therefore

```math
\boxed{
A_{SC}>A(r_0)>{121\over196}>{\pi^2\over16}.
}
\tag{M.20}
```

The contradiction uses no floating-point computation. Numerically the true gap is

```math
A_{SC}-{\pi^2\over16}
=0.0016206097016009\ldots .
```

## 7. Perfect-matching branch exclusion

### Theorem MFS — no sufficiently large post-ZF perfect matching

There exists `D_0<infinity` such that no canonical triangle-free post-ZF C-II survivor of diameter `D>=D_0` has its full actual diameter graph equal to a perfect matching.

#### Proof

If such survivors existed for arbitrarily large `D`, choose an unbounded sequence. M.16 gives

```math
\limsup {\operatorname{area}(F)\over D^2}
\le{\pi^2\over16}.
```

Canonical `C-FS-STABILITY` and M.20 give

```math
\liminf {\operatorname{area}(F)\over D^2}
\ge A_{SC}>{\pi^2\over16},
```

contradiction. `square`

Equivalently, every sufficiently large post-ZF survivor has at least one actual loaded diameter vertex of degree at least two.

In Woodall language, the forest branch cannot consist entirely of isolated one-edge caterpillar components.

## 8. Regression audit

### Unit square

The unit square has a perfect-matching diameter graph and a rhombic contact disk. It is a genuine small global minimizer. MFS is asymptotic and therefore correctly retains this finite regression.

### Equilateral noncentrally-symmetric hexagons

Perfect-matching diameter graphs occur in exact convex unit-edge polygons that are not centrally symmetric. MFS does not use the false implication `matching -> central symmetry`. Such polygons do not satisfy the post-ZF defect collapse M.8: their bounded exceptional face contribution is nonzero.

### Contact-isolated source points

No source point is deleted in the proof. The contradiction is obtained entirely from the force-hull core before any attempt to count exterior rattlers. Thus an arbitrarily large KKT-invisible external population cannot rescue the perfect-matching branch.

### KKT weights and response traces

MFS uses only support, planar/contact geometry, canonical mixed rigidity, and full-force area. It does not claim a lower bound on any `beta` coefficient, nor does it convert the canonical affine response radialization into an operator or trace estimate.

## 9. Canonical effect

The Woodall forest branch is now strictly smaller:

```math
\boxed{
D\text{ sufficiently large}
\Longrightarrow
H\text{ is not a perfect matching}.}
```

At least one caterpillar component contains two adjacent diameter edges. Future forest arguments may therefore assume a genuine shared-endpoint diameter event while retaining the stronger canonical global facts

```math
{h\over D}\ge2\rho-o(1),
\qquad
{\operatorname{area}(F)\over D^2}\ge A_{SC}-o(1),
```

and the full-source midpoint/half-turn geometry.

This does not close the general forest branch: one nontrivial caterpillar can coexist with many matching components, and no positive stress-weight floor on the nontrivial component follows.
