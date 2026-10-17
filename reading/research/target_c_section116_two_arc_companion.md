> Generated reading edition · [exact source](../../research/target_c_section116_two_arc_companion.md) · source SHA-256 `d78b889939abf7e553f7f4ba26c4d72facf3f5319ef92a1086470f58175b466b`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "05f4aa75c894492932e50fb0b46b0e00d2ef6fb2", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_section116_two_arc_companion.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "0a7e9724cb5483c2c3705a2036d9789eb0008c7a9ca48fafcc9b60a718bd4820"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C Section 116 companion — two outer arcs double the universal return constant

**Date:** 2026-09-12  
**Status:** proof-only companion to `target_c_section116_zero_host_closed_faces.md`.

Section 116 absorbs every bounded nonquadrilateral face into the common zero host.
Its three-outer-arc theorem is useful when a large inscribed triangle perimeter is
available.  There is a stronger universal variant: cut the occurrence-counted outer
walk only at a diameter pair of attachment vertices.  The two open outer arcs then
have opposite unit chord hosts `q,-q`, while every bounded defect-face cycle still has
host `0`.

For a strict-rhombus carrier with attachment-cell diameter `d`, outer-walk length `L`,
strict-rhombus area `A_4`, and total bounded-nonquadrilateral face perimeter
`P_exc`,

```math
\boxed{
 d\bigl(L+P_{\rm exc}-2d\bigr)
 \ge(4-2\sqrt3)A_4.
}
\tag{116.TA}
```

Since canonical Section 82 gives `P_exc<=5Q`,

```math
\boxed{
 d(L+5Q-2d)
 \ge(4-2\sqrt3)A_4.
}
\tag{116.TB}
```

Equivalently, using `L+Q=4a-6-2s-2c`,

```math
\boxed{
 d\bigl(4a-6-2s-2c+4Q-2d\bigr)
 \ge(4-2\sqrt3)A_4.
}
\tag{116.TC}
```

This doubles the area coefficient of the coarse three-cut corollary while retaining
the same universal displacement subtraction `2d`.

## 1. Two outer arcs give the host set `{q,-q,0}`

Choose attachment vertices `p_-,p_+` with

```math
|p_+-p_-|=d.
```

Both are extreme vertices of the attachment polygon and hence occur on the outer-face
walk.  Cutting that closed occurrence-counted walk at these two vertices gives two
directed arcs.  Orient the outer walk with the bounded side on the left.  Their
displacements are

```math
z=p_+-p_-,
\qquad -z,
```

so their unit chord hosts are

```math
q={z\over d},
\qquad -q.
```

As in the main Section 116 theorem, orient every bounded nonquadrilateral face boundary
clockwise.  Each such cycle is closed and therefore has host vector `0`.  Every
physical strict-rhombus boundary end is assigned injectively either to one of the two
outer-walk arc occurrences or to its bounded-face cycle occurrence.  Thus every
complete train has two good ends.

The exact total walk excess is

```math
\boxed{
E=L+P_{\rm exc}-2d.
}
\tag{116.T1}
```

## 2. Exact local return cost for two antipodal hosts plus zero

For the host set

```math
Q=\{q,-q,0\},
```

one has, for any unit train direction `u`,

```math
w_Q(u)=2|q\cdot u|,
```

and hence

```math
2-w_Q(u)=2-2|q\cdot u|.
\tag{116.T2}
```

Let `u,v` be the two train directions crossing in one strict unit rhombus, and let
`varphi in (pi/3,pi/2]` be their projective angle.  Choose signs so the oriented angle
between them is `varphi`.  Then

```math
\max_{|q|=1}
\left(|q\cdot u|+|q\cdot v|\right)
=2\cos(\varphi/2).
\tag{116.T3}
```

Indeed, after choosing the two signs that make both scalar products nonnegative, the
maximum is the norm of `u+v`; the alternative sign gives `|u-v|<=|u+v|` because
`varphi<=pi/2`.

Therefore every strict rhombus satisfies

```math
\begin{aligned}
&(2-w_Q(u))+(2-w_Q(v))\\
&\qquad=4-2\left(|q\cdot u|+|q\cdot v|\right)\\
&\qquad\ge4-4\cos(\varphi/2)\\
&\qquad>4-2\sqrt3.
\end{aligned}
\tag{116.T4}
```

The weak uniform constant

```math
\boxed{c_2:=4-2\sqrt3=2(2-\sqrt3)}
\tag{116.T5}
```

is sharp as `varphi downarrow pi/3`.

## 3. Area transport

For each complete train `tau` put

```math
\delta_\tau=2-w_Q(u_\tau).
```

Multiply (116.T4) by rhombus area and sum over the full strict-rhombus complex.  After
reorganizing by trains,

```math
c_2A_4
\le
\sum_\tau\delta_\tau
\sum_{R\in\tau}\operatorname{area}(R).
```

The exact train transverse-span identity gives

```math
\sum_{R\in\tau}\operatorname{area}(R)\le d.
```

The zero-host signed-return theorem gives

```math
E\ge\sum_\tau\delta_\tau.
```

Consequently

```math
c_2A_4\le dE.
```

Substitution of (116.T1) proves (116.TA).

## 4. Relation to the one-arc and three-arc bounds

Using the entire outer walk as one closed zero-displacement host gives

```math
d(L+P_{\rm exc})\ge4A_4,
```

which is the exact signed-return form of the ordinary train-span inequality.

The two-arc theorem gives

```math
L+P_{\rm exc}
\ge2d+(4-2\sqrt3){A_4\over d}.
```

The three-arc theorem gives instead

```math
L+P_{\rm exc}
\ge\Pi_3^{\max}+(2-\sqrt3){A_4\over d}.
```

Thus the two- and three-arc bounds are complementary.  The two-arc bound has the
larger universal area coefficient; the three-arc bound can win when the actual best
outer three-cut triangle has perimeter substantially larger than `2d`.

Compared with the one-arc train-span bound, the two-arc theorem is stronger whenever

```math
{A_4\over d^2}<{1\over\sqrt3}.
```

Indeed this is exactly the condition

```math
2+(4-2\sqrt3){A_4\over d^2}
>4{A_4\over d^2}.
```

The near-disk wrapping carriers occurring in the current Target-C quantitative chain
lie on this side of the comparison, so the two-arc inequality is a genuinely new
finite boundary constraint there even though it does not by itself close C-II.

## 5. Scope

No endpoint is discarded.  Hole and bounded-face boundaries are occurrence-counted.
The theorem is exact before asymptotics and uses no phase extraction, scalar-gap
stability, or near-endpoint assumption.

The remaining full-core question is whether global minimality or the canonical Oler /
interface currencies can force an upper bound on the same detour

```math
L+P_{\rm exc}-2d
```

that conflicts with (116.TA), or whether a carrier with the required linear detour can
be deformed source-preservingly to smaller global diameter.

**Theorem state:** unchanged.  C-II and LEVEL I remain open.
