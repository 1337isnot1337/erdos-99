> Generated reading edition · [exact source](../../research/target_c_weak_forest_density_regression.md) · source SHA-256 `31f659aed2db27945cdbe97c7ca0b0c5c6ec0a2163faebb7b8aab79dd8d1b0ae`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "8f45f7aaf3d212b13aa1db7df1adf2fb7a88ff5f", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_weak_forest_density_regression.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "009da8a542673d3e8fe627a6335450f008505f774815db1572c919b9c2a7d2d9"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C — regression: weak unit-contact forests can approach triangular packing density

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**  
**Status:** exact geometric regression.  
**Purpose:** rule out a density-only contradiction after the contact-saturation theorem.

The proof-only contact-saturation theorem converts a macroscopic actual-isolate population into an exact zero-force unit-contact forest while leaving the old positive KKT core unchanged. It is tempting to argue that a forest contact graph must waste a fixed amount of packing density compared with the triangular lattice. That is false.

There are triangle-free unit-separated lattice patches whose unit-contact graph is a disjoint union of paths and whose area per point approaches the triangular-lattice value `sqrt(3)/2` arbitrarily closely.

---

## 1. An exact one-parameter lattice

Fix `delta>0` and put

```math
u=(1,0),
\qquad
v=(1+\delta)\left({1\over2},{\sqrt3\over2}\right).
\tag{1.1}
```

Let

```math
\Lambda_\delta:=\{au+bv:a,b\in\mathbb Z\}.
```

For one lattice difference,

```math
|au+bv|^2
=a^2+(1+\delta)ab+(1+\delta)^2b^2.
\tag{1.2}
```

### Lemma 1.1 — exact shortest vectors

For every nonzero `(a,b)\in\mathbb Z^2`,

```math
|au+bv|\ge1,
```

with equality if and only if

```math
(a,b)=(1,0)\quad\text{or}\quad(-1,0).
\tag{1.3}
```

### Proof

If `b=0`, then `|au|=|a|`, so the claim is immediate.

If `|b|\ge2`, the vertical component alone has magnitude

```math
|b|{\sqrt3\over2}(1+\delta)
\ge\sqrt3(1+\delta)>1.
```

It remains to consider `|b|=1`. By symmetry it is enough to take `b=1`. As a function of the integer `a`, (1.2) is a strictly convex quadratic whose real minimizer is

```math
a=-{1+\delta\over2}.
```

The two nearest relevant integers are `a=0` and `a=-1`. They give

```math
|v|=1+\delta>1
```

and

```math
|v-u|^2
=1-(1+\delta)+(1+\delta)^2
=1+\delta+\delta^2>1.
```

All other integers give a larger value. The case `b=-1` is identical. Therefore only `\pm u` have unit length. `square`

Consequently `Lambda_delta` is unit-separated and its unit-contact graph consists exactly of the horizontal nearest-neighbor edges parallel to `u`.

---

## 2. Finite patches are triangle-free contact forests

For integers `M,N\ge1`, take the finite rectangular patch

```math
P_{M,N}(\delta)
:=\{iu+jv:0\le i\le M,\ 0\le j\le N\}.
\tag{2.1}
```

By Lemma 1.1, every unit contact joins

```math
(i,j)\leftrightarrow(i+1,j).
```

Thus the unit-contact graph is the disjoint union of `N+1` paths, each with `M+1` vertices. In particular it is a forest and contains no contact triangle.

Every vertex has a unit neighbor when `M\ge1`, so these examples also show that the no-actual-isolate condition from the saturation theorem does not force cycles or positive two-dimensional contact rigidity.

---

## 3. Density approaches the triangular value

The fundamental parallelogram area is

```math
\det(u,v)
={\sqrt3\over2}(1+\delta).
\tag{3.1}
```

Hence the area per lattice point tends to

```math
\boxed{
{\sqrt3\over2}
}
\tag{3.2}
```

as `delta\downarrow0`, exactly the triangular-lattice packing value.

Equivalently, the density of radius-`1/2` disks is

```math
{\pi/4\over (\sqrt3/2)(1+\delta)}
={\pi\over2\sqrt3}{1\over1+\delta}
\longrightarrow {\pi\over2\sqrt3}.
\tag{3.3}
```

Thus there is no fixed positive density penalty for requiring the exact unit-contact graph to be a forest, even a disjoint union of paths.

The same conclusion survives on arbitrarily large finite patches: boundary terms are `O(M+N)` while population and area are `Theta(MN)`.

---

## 4. Consequence for the inactive-container route

The contact-saturation theorem gives, in the macroscopic-container branch, a second global-minimizer representative in which the old positive force core is unchanged but the former actual isolates support `Omega(D^2)` exact weak contacts arranged as a forest.

The present regression shows that one cannot close that branch by a theorem of the form

```text
unit-separated + triangle-free + contact graph forest
    => packing density <= triangular density - c
```

for any absolute `c>0`.

The obstruction can be made arbitrarily close to triangular packing by taking `delta` arbitrarily small. Therefore any successful forest-based closure must use one of the pieces absent from this regression:

1. exact **global diameter minimality**, not only local packing density;
2. coupling of the weak forest to the unchanged positive KKT/diameter core;
3. a finite equality/stability theorem whose equality case forces `delta=0` and hence additional unit contacts; or
4. a source-preserving deformation that reduces the old global diameter before the weak lattice reaches its triangular limit.

This is the inactive-container analogue of the strict-rhombus full-core obstruction: asymptotic density alone cannot distinguish `delta>0` from `delta=0`.

---

## 5. Scope

This is a local geometric regression, not a global-minimizer construction. The patches `P_{M,N}(delta)` are not claimed to minimize diameter for their cardinality. Their role is to falsify density-only or contact-forest-only closing lemmas.

No KKT weights are assigned, no source points are deleted, and no claim about theorem authority is made.

**Disposition:** exact regression. Any inactive-branch closure must use global minimality or force-core coupling beyond weak-forest density.
