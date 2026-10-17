> Generated reading edition · [exact source](../../research/target_c_section125_augmented_route_compression_self_audit.md) · source SHA-256 `c301bde1a812b35d947157b8ffd77854fa24e0ea03a1660e137d1a6bcb6dd417`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "f0edbd17f83e3ce76de803659c4a8b6c0d4ee091", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_section125_augmented_route_compression_self_audit.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "b2620ff3a053528dbc7de1c6aec09add19b8ad2189acd96eab5559adfc51b643"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — Target C Section 125 augmented route compression

**Date:** 2026-09-12  
**Artifact:** `research/target_c_section125_augmented_route_compression.md`  
**State lock:** audit.46; theorem authority unchanged  
**Verdict:** **PASS at proof-only scope.**

## 1. Exact unsimplified outer-walk identity

Let `G_r^0` contain only internal contacts of `I_r` and attachment contacts from `I_r` to `A_r`. It is connected: `I_r` is connected and every member of `A_r` is an actual attachment.

Canonical Section 62 gives

```math
e_r+t_r=2n_r+1+s_r.
```

Thus

```math
V=n_r+a_r,
\qquad E=2n_r+1+s_r,
```

and Euler gives

```math
F_b=n_r+2+s_r-a_r.
```

The graph is a simple triangle-free contact graph. Section 62 already uses the same fact to assert every bounded face-walk has length at least four even when the graph is not 2-connected. Therefore with occurrence-counted outer length `Ltilde_r` and bounded-face excess `Qtilde_r>=0`,

```math
2E=Ltilde_r+4F_b+Qtilde_r.
```

Substitution gives

```math
Ltilde_r+Qtilde_r=4a_r-6-2s_r.
```

No bridge or articulation correction is missing because face incidence and the outer walk both count edge occurrences.

**Verdict:** valid.

## 2. Algebra with canonical Section 123

Canonical Section 123 proves for the augmented graph `J_r^+`

```math
a_r-3-s_r={a_r-T_r+Q_r^+\over2}.
```

Hence

```math
2a_r-6-2s_r=a_r-T_r+Q_r^+.
```

Insert this in the preceding exact identity:

```math
Ltilde_r+Qtilde_r
=2a_r+a_r-T_r+Q_r^+.
```

Therefore

```math
Ltilde_r-2a_r
=a_r-T_r+Q_r^+-Qtilde_r
\le a_r-T_r+Q_r^+.
```

The proof does not require any one-to-one matching of augmented faces to outer routes.

**Verdict:** valid.

## 3. Can loaded-loaded contacts increase the outer-face walk length?

The actual induced harmonic graph is obtained from `G_r^0` by adding its loaded-loaded contact edges. Contact edges are noncrossing straight segments, so add them sequentially in their fixed embedding.

For one added edge:

- if its interior lies in a bounded face, the outer face is unchanged;
- if its interior lies in the current outer face, the edge joins two boundary occurrences and splits that face. One endpoint-to-endpoint boundary subwalk becomes the boundary of the new bounded face; the other remains on the new outer face together with the added edge. The discarded subwalk has at least one edge occurrence because the endpoints are distinct. Hence the new outer length is the old outer length minus `len(W)` plus one and cannot exceed the old length.

An added edge cannot be a bridge because its endpoints were already connected. Multiple boundary occurrences cause no problem: the embedding selects the two sectors/occurrences adjacent to the new edge, and the same face-splitting calculation applies to those occurrences.

Therefore

```math
L_r\le Ltilde_r.
```

**Verdict:** valid.

## 4. Globalization through the exact augmented ledger

Summing the local inequality gives

```math
\sum_r(L_r-2a_r)
\le\sum_r(a_r-T_r+Q_r^+).
```

Canonical Section 123 gives exactly

```math
e_{BB}-k={1\over2}\sum_r(a_r-T_r+Q_r^+)+d_{tile}.
```

Thus

```math
\sum_r(L_r-2a_r)
\le2(e_{BB}-k-d_{tile}).
```

No local edge occurrence is identified across cells; only scalar local face ledgers are summed.

**Verdict:** valid.

## 5. Check `L_r>=2d_r`

Every attachment vertex is extreme in `P_r` and occurs on the outer-face walk of the actual induced harmonic graph. Choose an attachment diameter pair `p,q` with `|p-q|=d_r` and occurrences of them on one cyclic outer walk. The two outer-walk arcs between those occurrences each have Euclidean path length at least `d_r`, because all outer edges are unit segments and each arc joins the same endpoints. Hence

```math
L_r\ge2d_r.
```

This proves the finite compatibility corollary in Section 125 without assuming a simple outer boundary.

**Verdict:** valid.

## 6. Correlated Type-II payment

Canonical Section 122 gives

```math
\liminf D^{-1}\sum_r(L_r+P_{exc,r}-2d_r)\ge R_0.
```

Canonical Section 123 gives the cellwise bound

```math
P_{exc,r}\le5Q_r^+.
```

The Section-125 route bound gives

```math
L_r-2d_r
\le(a_r-T_r+Q_r^+)+2(a_r-d_r).
```

Summing yields the pointwise upper bound

```math
\sum_r(L_r+P_{exc,r}-2d_r)
\le2\Delta_{ad}+A_*+6Q_*.
```

Since the right side is pointwise at least the canonical detour quantity, its normalized liminf is at least `R_0`. Division by two gives

```math
\liminf D^{-1}
\left(\Delta_{ad}+{A_*\over2}+3Q_*\right)
\ge {\pi\over4}(2-\sqrt3).
```

No `liminf` inequality is reversed.

**Verdict:** valid.

## 7. Does `T_r` really identify two-edge triangular teeth?

Every triangle in `J_r^+` must use at least one added attachment-polygon side because `G_r^0` is a triangle-free contact graph.

At every attachment vertex, at least one attachment edge runs from that convex-boundary vertex into `int(P_r)`. In the cyclic rotation at the vertex, such an interior edge lies between the two polygon sides on the bounded side of the hull cycle. Therefore the two polygon sides cannot be consecutive sides of one bounded face. A bounded triangular face cannot contain two added polygon sides.

Hence every triangular bounded face has exactly one added polygon side. Its other two edges belong to `G_r^0`. Their third vertex cannot be loaded, because `G_r^0` contains no loaded-loaded edges. It is therefore one unloaded apex joined by two unit attachment edges to the consecutive loaded endpoints of the artificial side.

If the artificial side also had length one, it would be an actual source contact and these three unit pairs would form a forbidden unit equilateral triangle. Hence its length is strictly greater than one.

Conversely, an attachment interval whose unsimplified route consists of two unit edges is closed by its added polygon side into exactly such a triangular face. Thus `T_r` is precisely the count of two-edge unsimplified teeth.

**Verdict:** valid.

## 8. Scope and surviving obstruction

The theorem retains every source point and never extends the Section-57 kernel to isolates. Its final asymptotic conclusion uses only canonical Section 122 after the finite route theorem has been proved.

The result does not close C-II. In the regime `A_*,Q_*=o(D)`, the return demand becomes a linear lower bound on `sum(a_r-d_r)`. A large collection of near-equilateral two-edge teeth can satisfy that inequality without an exact unit base.

**Final audit verdict:** Section 125 is proof-valid at proof-only scope. C-II remains open.
