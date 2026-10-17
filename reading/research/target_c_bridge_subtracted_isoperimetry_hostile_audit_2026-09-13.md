> Generated reading edition · [exact source](../../research/target_c_bridge_subtracted_isoperimetry_hostile_audit_2026-09-13.md) · source SHA-256 `cf0b513b5821b29f81d498ca2a64639ac6686710e11056579d7fc9fb2e40965b`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "7115333268cea1f2d07e3ae8a869e3951984d6f0", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_bridge_subtracted_isoperimetry_hostile_audit_2026-09-13.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "ec09562dd1f1a62149f6ae1157455b2dec0fa0939f9b37de8ec52aec862aca71"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — bridge-subtracted outer-face isoperimetry

**Date:** 2026-09-13  
**Reviewed:** `target_c_bridge_subtracted_isoperimetry_2026-09-13.md`  
**Disposition:** PASS at the stated finite and conditional scopes. The result is
proof-only and does not close C-II.

## 1. Finite boundary accounting

Let `G` be a finite connected plane graph and let `U` be the union of the closures of
its bounded faces. An edge on `partial U` has a bounded face on one side and the
unbounded face on the other. An outer-face bridge has the unbounded face on both
sides, so neither of its two boundary-walk occurrences belongs to `partial U`.
Every other outer-face occurrence can contribute at most one unit edge to the
perimeter of `U`; repeated vertices and articulation points do not change this
occurrence count. Therefore

```
per(U) <= L - 2 B_o.
```

Applying planar isoperimetry to each positive-area component and using
`sum p_j^2 <= (sum p_j)^2` gives

```
A <= (L - 2 B_o)^2/(4 pi).
```

The rearranged bound on `B_o` has the correct sign because the square-root argument
is nonnegative by the same inequality.

## 2. Strict-rhombus variant

For the union `R` of strict-rhombus faces, a boundary edge has on its other side
either the outer face or a bounded nonquadrilateral face. The outer bridge removal
therefore gives

```
per(R) <= b + P_exc - 2 B_o.
```

Here `P_exc` is the sum of the degrees of bounded nonquadrilateral faces, counted by
physical side occurrences. If an exceptional face and a rhombus share an edge, the
edge is charged at most once to `per(R)` and at least once in `P_exc`, so the upper
bound remains valid. Applying componentwise planar isoperimetry gives the displayed
strict-rhombus area inequality in the reviewed note.

## 3. Type-II limit check

The use of

```
A_4/D^2 -> pi/4,
```

is restricted to the canonical full-core Type-II near-disk branch. It is not valid
for an arbitrary selected harmonic carrier. With `b/D -> M` and
`P_exc/D -> P`, the strict-rhombus inequality yields

```
2 B_o/D <= M - pi + P + o(1).
```

No assertion that `M-pi` or `P` vanishes is made.

## 4. Two-phase composition

The implication `N_o <= P_exc + 2 B_o` is a separate two-phase boundary-occurrence
statement. Substitution of the preceding bridge bound gives

```
N_o/D <= 2 P + M - pi + o(1),
```

which composes with the projection lower bound only under its explicit hypotheses:
two selected directions, reciprocal widths `D-o(D)`, and the stated full-core area
saturation. The factor two on `P` is unavoidable from these two inequalities.

## 5. Scope limits

- `B_o` counts only graph bridges with both sides on the unbounded face. Internal
  bridges and arbitrary singleton stopped trains are not silently included.
- The area sandwich is a full-core fact; it cannot be transferred to one harmonic
  carrier without a separate area theorem.
- The argument does not produce an upper bound on the outer detour, an exact unit
  triangle, or a source-preserving strict-diameter competitor.
- Contact-isolated source points are not removed and no full-source affine-kernel
  claim is used.

The reviewed bridge/isoperimetric statements are mathematically sound as written,
but remain a conditional payment lemma rather than a C-II closure.

**Classification:** audited-working, proof-only.
