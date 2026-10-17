> Generated reading edition · [exact source](../../research/target_c_triangular_tooth_curvature_2026-09-12.md) · source SHA-256 `a187a915631d301b4dce492c595df50a7b1a5fce735e31a2778b1ee7f6afa581`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "b67fad918f8e3f86569bf486a6124da0711a25ca", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_triangular_tooth_curvature_2026-09-12.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "38cc9bed0488e50432630e21184bb7fdad2b27f3d2b5957e8d12f994ab22593f"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C — triangular teeth must pay convex turning

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**  
**Status:** proof-only finite geometry lemma. Theorem authority unchanged.

The augmented-route compression work isolates a difficult regime in which almost every
attachment-polygon side bounds a two-edge triangular tooth. Such a tooth is not an
exact source triangle: its two actual sides have length one, while its artificial base
has length strictly between one and two.

There is nevertheless an exact local obstruction. Two consecutive inward triangular
teeth cannot both be arbitrarily close to equilateral across a positively turning
convex attachment vertex. Their base-angle excesses must pay the exterior turning of
the attachment polygon.

## 1. Finite adjacent-tooth inequality

Let

```math
A_1,A_2,\ldots,A_a
```

be the vertices of a convex attachment polygon in counterclockwise order. Write

```math
s_i=|A_iA_{i+1}|
```

with cyclic indices, and let `delta_i in [0,pi)` be the exterior turning angle from
the directed side `A_{i-1}A_i` to `A_iA_{i+1}`. Thus

```math
\sum_i\delta_i=2\pi.
```

Call side `i` a **triangular tooth side** if there is one source vertex `X_i` in the
interior side of the polygon with

```math
|A_iX_i|=|A_{i+1}X_i|=1.
```

In the triangle-free harmonic setting one has

```math
1<s_i<2.
```

The lower inequality is triangle-freeness. The upper inequality is strict because the
unloaded tooth apex lies in the interior of the attachment polygon rather than on its
base segment.

For a tooth side define

```math
\alpha_i:=\arccos(s_i/2)\in(0,\pi/3),
\qquad
\varepsilon_i:=\pi/3-\alpha_i>0.
```

### Theorem 1 — adjacent teeth pay turning

If both sides `i-1` and `i` are triangular tooth sides, then

```math
\boxed{
\delta_i<\varepsilon_{i-1}+\varepsilon_i.
}
\tag{1}
```

### Proof

Let `phi_j` be the argument of the directed side `A_jA_{j+1}`, using a real lift near
vertex `A_i`, so

```math
\phi_i-\phi_{i-1}=\delta_i.
```

Because `X_i` lies on the interior, left side of `A_iA_{i+1}`, elementary isosceles
triangle geometry gives

```math
\arg(A_iX_i)=\phi_i+\alpha_i.
```

Likewise `A_i` is the right endpoint of the previous tooth base, hence

```math
\arg(A_iX_{i-1})=\phi_{i-1}+\pi-\alpha_{i-1}.
```

Both rays lie in the convex interior wedge at `A_i`. Their angular separation is
therefore

```math
\theta_i
=\pi-\delta_i-\alpha_{i-1}-\alpha_i.
```

The two tooth apices are source points at unit distance from `A_i`. Unit separation
therefore gives

```math
|X_{i-1}-X_i|=2\sin(\theta_i/2)\ge1,
```

so `theta_i>=pi/3`. Equality would make

```math
|A_iX_{i-1}|=|A_iX_i|=|X_{i-1}X_i|=1,
```

an exact unit equilateral triangle in the source. Under the standing triangle-free
hypothesis the inequality is strict:

```math
\theta_i>\pi/3.
```

Substituting the expression for `theta_i` gives

```math
\delta_i
< {2\pi\over3}-\alpha_{i-1}-\alpha_i
=(\pi/3-\alpha_{i-1})+(\pi/3-\alpha_i),
```

which is (1). `square`

## 2. Global turning consequence

Let `G` be the set of triangular-tooth sides and let `B` be the set of attachment
vertices at which at least one adjacent side is not in `G`. Summing Theorem 1 over all
vertices outside `B` gives

```math
\sum_{i\notin B}\delta_i
<2\sum_{j\in G}\varepsilon_j.
```

Consequently

```math
\boxed{
2\sum_{j\in G}\varepsilon_j
+\sum_{i\in B}\delta_i
>2\pi.
}
\tag{2}
```

In particular, if every attachment side is a triangular tooth,

```math
\boxed{
\sum_{j=1}^a\varepsilon_j>\pi.
}
\tag{3}
```

Thus an all-tooth convex attachment polygon cannot approach an exact equilateral-tooth
ring with total angular error `o(1)`. Convex curvature has to be absorbed either by
base slack or by non-tooth vertices.

Since

```math
s_i
=2\cos(\pi/3-\varepsilon_i)
=\cos\varepsilon_i+\sqrt3\sin\varepsilon_i,
```

this is a source-level geometric statement about the artificial base lengths, not a
phase-bin counting convention.

A useful quantitative corollary is the following. If at most `m` sides are non-tooth
and every exterior turn is at most `kappa`, then `|B|<=2m`, hence

```math
\boxed{
\sum_{j\in G}\varepsilon_j>\pi-m\kappa.
}
\tag{4}
```

## 3. Exact scope and failure mode

This lemma does not close the triangular-tooth regression by itself. A sublinear set
of exceptional sides can still carry the full `2pi` turning when their individual
turns are small but not small enough relative to their count. Likewise (3) is only a
constant total angular payment, whereas C-II requires a source-level diameter or
minimality contradiction.

Its value is narrower and exact:

- exact equilateral teeth cannot wrap a convex attachment polygon;
- adjacent tooth bases approaching length one must do so slowly enough to pay local
  convex turning;
- any all-regime closing theorem for the Section-125 triangular-tooth branch must
  account for this curvature payment rather than treating the tooth bases as
  independent scalar slacks.

Every source point is retained. No affine-kernel statement is applied to isolated
coordinates, and no theorem-state mutation is proposed.

**Disposition:** proved finite structural lemma; C-II remains open.
