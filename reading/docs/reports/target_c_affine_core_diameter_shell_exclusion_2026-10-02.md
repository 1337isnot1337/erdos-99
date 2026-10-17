> Generated reading edition · [exact source](../../../docs/reports/target_c_affine_core_diameter_shell_exclusion_2026-10-02.md) · source SHA-256 `27040e6dbae64d476daacae3dbc2a4993d8815afaa96d78f8f7042d52f1272b0`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-F3344EE60EF9","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II -- exact single-lattice core excluded by the active-diameter shell

**Date:** 2026-10-02
**Base main:** `d4552892e0b136157cf1938dc7bfd1b5d4739e94`
**Status:** proof-only; no theorem-state promotion claimed
**Target:** C-II exact affine-core subroute
**Computation:** none

## 1. Result

Let $`A`$ be the canonical Target C-II representative: a triangle-free global
minimizer chosen first contact-minimal and then diameter-pair-minimal. Let $`V`$
be its nonisolated positive-contact core and $`H`$ the canonical active diameter
edge set from Section 57. Write $`D=\operatorname{diam}(A)`$ and $`h=|H|`$.

Suppose that, for some translate $`t+\Lambda`$,

```math
 V\subset t+\Lambda,\qquad
 \Lambda=\mathbb Zu+\mathbb Zv,\qquad
 |u|=|v|=1,\qquad
 \angle(u,v)\in[\pi/3,2\pi/3].
\tag{1.1}
```

Then

```math
\boxed{h\le {1\over2}(9\pi\sqrt2\,D)^{2/3}.}
\tag{1.2}
```

Canonical ZF gives $`h\ge\lceil D\rceil`$. Consequently (1.1) is impossible whenever

```math
\boxed{D>{81\pi^2\over4}.}
\tag{1.3}
```

Thus the nonisolated active core of a sufficiently large canonical C-II
counterexample cannot lie in one exact unit-rhombic affine lattice, uniformly all
the way to the triangular angle. Contact-isolated source points may lie anywhere.

This removes the inverse-diameter shear endpoint from the exact single-lattice
core subroute. It does not produce a single affine chart for the general
near-rhombic harmonic carrier, so C-II remains open.

## 2. Uniform lattice-shell bound

Let $`T:\mathbb R^2\to\mathbb R^2`$ be
$`T(a,b)=au+bv`$. Put $`c=u\cdot v`$. Since the basis angle is in
$`[\pi/3,2\pi/3]`$, $`|c|\le1/2`$. The Gram matrix is

```math
T^TT=\begin{pmatrix}1&c\\c&1\end{pmatrix},
```

whose smallest eigenvalue is $`1-|c|\ge1/2`$. Hence

```math
|z|\le\sqrt2\,|Tz|\qquad(z\in\mathbb R^2).
\tag{2.1}
```

For $`R>0`$, define

```math
S_R=\{z\in\mathbb Z^2:|Tz|=R\},\qquad N_R=|S_R|.
\tag{2.2}
```

### Lemma 2.1

For every $`R\ge1`$,

```math
\boxed{N_R\le(9\pi\sqrt2\,R)^{2/3}.}
\tag{2.3}
```

### Proof

If $`N_R<3`$, (2.3) is immediate for $`R\ge1`$. Assume $`N_R\ge3`$. The set $`E_R=\{x:|Tx|=R\}`$ is a strictly convex ellipse. Every point of
$`S_R`$ is exposed by its tangent support line, so the points of $`S_R`$, in
cyclic order $`z_1,\ldots,z_{N_R}`$, are exactly the vertices of a strictly
convex lattice polygon $`P_R`$.

Its oriented edge vectors $`e_i=z_{i+1}-z_i`$ are nonzero integer vectors with
pairwise distinct oriented directions, hence are pairwise distinct. Order their
coefficient-plane Euclidean lengths as
$`\ell_1\le\cdots\le\ell_{N_R}`$.

For $`r\ge1`$, the number of nonzero integer vectors of length at most $`r`$ is
at most

```math
(2r+1)^2-1\le9r^2.
```

Therefore $`j\le9\ell_j^2`$, so $`\ell_j\ge\sqrt j/3`$. Hence

```math
\operatorname{per}(P_R)
=\sum_i|e_i|
\ge {1\over3}\sum_{j=1}^{N_R}\sqrt j
\ge {2\over9}N_R^{3/2}.
\tag{2.4}
```

By (2.1),

```math
\operatorname{per}(P_R)
\le\sqrt2\sum_i|Te_i|
=\sqrt2\,\operatorname{per}(TP_R).
\tag{2.5}
```

All vertices of $`TP_R`$ lie on the Euclidean circle of radius $`R`$, so
$`TP_R`$ is an inscribed convex polygon and
$`\operatorname{per}(TP_R)\le2\pi R`$. Combining with (2.4)--(2.5) gives

```math
{2\over9}N_R^{3/2}\le2\pi\sqrt2\,R,
```

which proves (2.3). $`\square`$

This is a self-contained Jarnik-type perimeter argument. It uses no arithmetic
assumption on $`\cos\theta`$, so rational, irrational, and $`D`$-dependent angles
are covered uniformly.

## 3. One projective shell vector supports at most one diameter edge

### Lemma 3.1

Let $`xy`$ and $`x'y'`$ be two diameter edges in a planar set of diameter $`D`$.
If their displacement vectors are equal after orienting the two segments, then
the edges are identical.

### Proof

Write
```math
r=y-x=y'-x',\qquad |r|=D,\qquad w=x'-x.
```
The cross distances obey
```math
|r+w|=|y'-x|\le D,\qquad |r-w|=|y-x'|\le D.
```
Adding squares,
```math
2D^2+2|w|^2=|r+w|^2+|r-w|^2\le2D^2.
```
Hence $`w=0`$, so the edges coincide. $`\square`$

If two diameter segments have the same projective direction, reverse one
orientation if necessary and apply the lemma. Thus distinct diameter edges give
distinct antipodal pairs $`\{z,-z\}`$ in $`S_D`$.

Every endpoint of every $`H`$-edge lies in $`V`$. Under (1.1), every $`H`$-edge
therefore has displacement $`Tz`$ for some $`z\in S_D`$. Hence

```math
\boxed{h\le N_D/2.}
\tag{3.1}
```

Lemma 2.1 now proves (1.2).

## 4. Canonical ZF closes the exact affine-core branch

The promoted Section-57 ZR/ZF theorem is a theorem on the nonisolated
positive-contact core $`V`$. For the canonical lexicographically normalized
Target C-II source it gives

```math
e+h\ge2v-2,\qquad
\boxed{h\ge\delta\ge\lceil D\rceil.}
\tag{4.1}
```

No full-source affine-kernel assertion is used. Contact-isolated source points are
irrelevant to this argument.

Combining (1.2) and (4.1),

```math
D\le {1\over2}(9\pi\sqrt2\,D)^{2/3}.
```

For $`D>0`$, this implies

```math
D\le {1\over8}(9\pi\sqrt2)^2={81\pi^2\over4}.
\tag{4.2}
```

Therefore no canonical C-II survivor with $`D>81\pi^2/4`$ can satisfy (1.1).

## 5. Relation to existing affine-lattice work

The older proof-only report
\`target_c_affine_lattice_boundary_vertex_exclusion_2026-09-11.md\`
also obtained a Jarnik-type $`O(D^{2/3})`$ estimate, but for vertices of a
convex lattice polygon, and combined it with a C34/C65 force-hull vertex floor.

The present load-bearing step is different:

- it counts exact diameter displacement vectors on one lattice ellipse;
- it uses the currently promoted ZF edge floor $`h\ge\lceil D\rceil`$;
- it needs only the active core $`V`$ to lie in one lattice;
- it does not require every actual diameter pair to be visible or the force hull
  itself to be the lattice polygon being counted.

The canonical restricted theorem \`C-OBLIQUE-LATTICE-COMPETITOR\` and the newer
proof-only mixed-area/Pick/Voronoi comparisons leave an $`O(D^{-1})`$ shear
window because they compare bulk population with a boundary correction. For the
canonical lexicographically normalized C-II source, the shell argument bypasses
that boundary competition: an exact single-lattice core has too few projective
diameter vectors to support the ZF-required linear active diameter graph.

This does not assert that every affine-lattice global minimizer under an arbitrary
non-lexicographic choice of representative is excluded by ZF. The application is
to the canonical Target C-II representative used by the current route.

## 6. Remaining bottleneck

The result closes only the exact one-grain affine-core model. Current main still
allows a near-rhombic harmonic carrier whose train directions drift and whose
cells need not share one global affine coordinate system. Multiple grains and
interfaces can therefore evade the single ellipse $`S_D`$.

The next useful extension is an approximate/multigrain shell theorem: show that
the canonical linear active-diameter family cannot be distributed among the
small-phase-error or bounded-interface affine charts of the harmonic carrier
without paying the live aggregate detour/interface currency
$`\sum_r(L_r-2d_r)`$.

The macroscopic inactive-container branch is untouched.

## 7. Proof classification

- Theorem/proof: Lemmas 2.1 and 3.1, the shell edge bound (1.2), and the finite
  exclusion $`D>81\pi^2/4`$, under the exact single-lattice core hypothesis and
  promoted Section-57 ZF.
- Computation: none.
- Verifier code: none added or required.
- Canonical promotion: not claimed; C-II remains open.
