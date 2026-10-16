<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "4ecdcc5332abd0cf8e5ce61e99635d97f5a94390", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_oblique_lattice_structural_regression_2026-09-12.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "1bca698ce485d948f1bc58f9db34aa1f74919f1a371a8f626f95f803b94803d3"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C — oblique-lattice regression for topology-only closure

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**  
**Status:** proof-only regression; theorem authority unchanged.

This note records a structural obstruction to two tempting C-II closing statements.
A large ordered complete train grid, even together with an asymptotically round
source hull, a near-diameter chord, macroscopic transverse train width, quadratic
strict-rhombus area, and vanishing angular defect per rhombus, does **not** by itself
force a unit equilateral triangle.

The missing ingredient must use the actual global-minimizer/KKT/attachment economy,
not only ordered-grid topology or coarse width geometry.

---

## 1. The oblique unit lattice

Fix an angle

\[
 {\pi\over3}<\phi<{\pi\over2}
\]

and put

\[
 u=(1,0),\qquad v=(\cos\phi,\sin\phi),\qquad
 \Lambda_\phi=\{iu+jv:i,j\in\mathbb Z\}.
\]

For integers `m,n`,

\[
 |mu+nv|^2=m^2+n^2+2mn\cos\phi.
\tag{1.1}
\]

### Lemma 1 — the only unit lattice vectors are the two basis directions

For every nonzero `(m,n) in Z^2`,

\[
 |mu+nv|\ge1,
\]

with equality if and only if

\[
 (m,n)\in\{(\pm1,0),(0,\pm1)\}.
\tag{1.2}
\]

### Proof

Write `c=cos(phi)`, so `0<c<1/2`.

If `mn>=0`, then

\[
 m^2+n^2+2mnc\ge m^2+n^2\ge1,
\]

and equality forces exactly one of `|m|,|n|` to equal one and the other to vanish.

If `mn<0`, put `a=|m|`, `b=|n|`. Then

\[
 |mu+nv|^2=a^2+b^2-2abc
> a^2+b^2-ab.
\]

For positive integers `a,b`,

\[
 a^2+b^2-ab\ge1.
\]

Thus the mixed-sign case is strictly larger than one. `square`

Consequently every finite subset of `Lambda_phi` is unit-separated, and its unit
contact graph is a subgraph of the square grid on integer coordinates. In
particular the contact graph is bipartite under the parity coloring `i+j mod 2` and
contains no triangle. Therefore no finite subset contains a unit equilateral
triangle.

---

## 2. Arbitrarily large ordered complete train grids with four boundary corridors

For integers `M,N>=1`, let

\[
 P_{M,N}=\{iu+jv:0\le i\le M,\ 0\le j\le N\}.
\tag{2.1}
\]

Its contact graph is the `(M+1) x (N+1)` rectangular grid. The `MN` bounded faces are
strict unit rhombi of angle `phi>pi/3`.

There are two train families:

- `M` trains obtained by chaining opposite `u`-edges through the rhombi; and
- `N` trains obtained by chaining opposite `v`-edges.

Every train in the first family crosses every train in the second family in exactly
one rhombus. Crossings occur in the same order along every train. Thus the complex
contains an ordered complete `M x N` train grid for arbitrarily large `M,N`.

The convex hull is the parallelogram with sides `Mu` and `Nv`, so its boundary has
only four straight sides. Hence the following implication is false without additional
source-level hypotheses:

```text
arbitrarily large ordered complete train grid
+ O(1) boundary corridors
    => exact unit equilateral triangle.
```

The failure is exact, not asymptotic.

---

## 3. Near-disk truncations retain a linear ordered grid

The preceding parallelogram example leaves open the possibility that global
near-roundness changes the topology. It does not.

For `R>4`, define

\[
 A_R=\Lambda_\phi\cap B(0,R),
 \qquad K_R=\operatorname{conv}(A_R).
\tag{3.1}
\]

The lattice has a uniform covering radius at most one. Indeed, write any point as
`su+tv`, round `s,t` independently to nearest integers, and note that the residual
vector has norm at most

\[
 {1\over2}|u|+{1\over2}|v|=1.
\tag{3.2}
\]

Fix a unit direction `e` and put `x=(R-1)e`. Choose `lambda in Lambda_phi` with
`|lambda-x|<=1`. Then `|lambda|<=R`, so `lambda in A_R`, and

\[
 e\cdot\lambda\ge R-2.
\]

Since this holds for every `e`,

\[
 \boxed{B(0,R-2)\subseteq K_R\subseteq B(0,R).}
\tag{3.3}
\]

Therefore, if `D_R=diam(A_R)=diam(K_R)`,

\[
 2R-4\le D_R\le2R,
\tag{3.4}
\]

and after scaling by `D_R` the convex hulls converge in Hausdorff distance to a
radius-`1/2` disk.

For a rectangular block, set

\[
 m_R=\lfloor R/4\rfloor.
\]

Then the whole index rectangle

\[
 |i|,|j|\le m_R
\]

lies in `A_R`, since

\[
 |iu+jv|\le |i|+|j|\le2m_R\le R/2<R.
\]

It therefore contains an ordered complete train grid with both shore sizes

\[
 2m_R=\Theta(R)=\Theta(D_R).
\tag{3.5}
\]

At the same time `A_R` remains triangle-free by Lemma 1.

---

## 4. Near-diameter chords coexist with macroscopic transverse width

Apply the covering argument in directions `e` and `-e`. There are points
`p_+,p_- in A_R` satisfying

\[
 |p_+-(R-1)e|\le1,
 \qquad
 |p_-+(R-1)e|\le1.
\]

Hence

\[
 |p_+-p_-|\ge2R-4\ge D_R-4.
\tag{4.1}
\]

Thus the same triangle-free source has a chord of length

\[
 (1-O(D_R^{-1}))D_R
\]

and simultaneously contains the linear-by-linear ordered train grid (3.5), whose
transverse width is macroscopic.

Therefore a qualitative statement of the form

```text
near-diameter chord + macroscopic transverse ordered-grid width
    => diameter strictly larger than D
```

is false without an additional quantitative relation supplied by global minimality,
attachment geometry, or the loaded diameter structure.

---

## 5. The regression survives inverse-diameter and smaller angular defects

The construction may vary with `R`. Let

\[
 \phi_R={\pi\over3}+\varepsilon_R,
 \qquad \varepsilon_R>0,
 \qquad \varepsilon_R\to0.
\tag{5.1}
\]

All arguments above remain uniform because

\[
 0<\cos\phi_R<1/2
\]

and the covering-radius estimate (3.2) is independent of `phi_R`.

Choose, for example,

\[
 \varepsilon_R=R^{-2}.
\tag{5.2}
\]

Then every retained rhombus is still strict and triangle-free, while a central
`Theta(R^2)`-rhombus block has total angular defect only

\[
 \Theta(R^2)\varepsilon_R=\Theta(1).
\tag{5.3}
\]

The rhombus covolume is

\[
 \sin\phi_R
 ={\sqrt3\over2}+{1\over2}\varepsilon_R+O(\varepsilon_R^2),
\tag{5.4}
\]

so even the density loss from the triangular lattice may be pushed below the ordinary
boundary scale while all contacts remain strictly triangle-free.

Moreover the union of full lattice rhombi contained in `B(0,R)` covers
`B(0,R-2)`: every fundamental rhombus has diameter below two. Hence its missing area
is only `O(R)`, while the retained strict-rhombus area is `pi R^2-O(R)`.
The number of train lines meeting the disk is `O(R)` in each of the two directions.

Thus the following collection of coarse structural properties is simultaneously
compatible with exact triangle-freeness:

- asymptotically round diameter-`D` convex hull;
- `Theta(D^2)` strict-rhombus area filling the hull to boundary order;
- only `O(D)` trains;
- an ordered complete grid with both shores `Theta(D)`;
- crossing defects `o(1/D)` if desired;
- total crossing angular defect `O(1)` if desired; and
- a `(1-O(1/D))D` source chord.

None of these properties alone or in this combination forces an exact unit triangle.

---

## 6. Consequence for the live C-II attacks

This regression does **not** model a global diameter minimizer and does not satisfy the
full canonical KKT/attachment stack. That distinction is exactly the point.

It rules out topology-only or coarse-width versions of Routes C and D. A successful
closure using the ordered carrier must spend a source-level currency absent from the
oblique-lattice truncations, for example:

1. the strict translated-lattice comparison/global diameter economy;
2. the actual loaded-diameter KKT equilibrium and attachment response;
3. the harmonic-cell outer-walk/interface ledger; or
4. a source-preserving deformation whose obstruction can be tied to an active diameter
   pair.

The construction also explains why merely improving the phase defect from `O(D)` to
`o(D)` cannot be a closing theorem: one can make the total defect `O(1)` while
remaining strictly triangle-free.

**Disposition:** rigorous regression. It narrows the live structural target but does
not alter theorem authority and does not close either C-II branch.