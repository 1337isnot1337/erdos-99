> Generated reading edition · [exact source](../../research/target_c_section121_augmented_cell_defect_budget.md) · source SHA-256 `48fc295871e9c1579df01d0315bcab1aaa85a6158fe96c5b42d8aaadf437a804`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "efba8059cc78b2a8faf0ce97baa16b49f1ab3276", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_section121_augmented_cell_defect_budget.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "f4229642a67ee2d3b56fb36735edaa4113eae7831c019f775f2cfb769126016e"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C — Section 121: augmented-cell defect budget globalizes local exceptional perimeter

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**  
**Status:** proof-only research candidate.  
**Dependencies:** canonical Sections 62, 63, 83 and elementary planar face counting.

Section 120 produces an aggregate lower bound involving

```math
\sum_r P_{{\rm exc},r},
```

the total bounded-nonquadrilateral perimeter in the induced harmonic graphs.  A
potential multiplicity problem is that these are local induced graphs, not one global
plane graph.  This section proves an exact global payment theorem: after augmenting
each harmonic component by its attachment polygon, all local degree-above-four defect
is paid by the single loaded-loaded contact surplus `e_BB-k`.

The main new corollary in the Section-116 currency is

```math
\boxed{
\sum_r P_{{\rm exc},r}\le10(e_{BB}-k),
\qquad k=d_H+s_Z.
}
\tag{121.1}
```

No source point is removed and no full-source ZR/ZF statement is used.

---

## 121.1 Augment one harmonic component

Fix an unloaded positive-contact component `I_r`.  Use canonical Section-62 notation

```math
n_r=|I_r|,
\qquad A_r\subset B,
\qquad a_r=|A_r|,
```

with `e_r` internal contacts, `t_r` attachment contacts, and

```math
s_r=e_r+t_r-2n_r-1\ge0.
\tag{121.2}
```

Start with the graph containing only the `e_r+t_r` internal/attachment contacts on
`I_r\cup A_r`.  Add every side of the convex attachment polygon

```math
P_r=\operatorname{conv}(A_r).
```

Call the resulting plane graph `J_r^+`.  A side already present as a contact is kept
only once.  The outer face of `J_r^+` is the simple `a_r`-cycle `partial P_r`.

Let

- `T_r` be the number of triangular bounded faces of `J_r^+`; and
- `Q_r^+` be the sum `sum_f(deg f-4)` over bounded faces of degree at least five.

There are no contact triangles.  Therefore every triangular bounded face of `J_r^+`
uses at least one newly added polygon side.  Each polygon side borders at most one
bounded face, so

```math
0\le T_r\le a_r.
\tag{121.3}
```

The vertex and edge counts are

```math
V_r^+=n_r+a_r,
\qquad
E_r^+=e_r+t_r+a_r=2n_r+1+s_r+a_r.
\tag{121.4}
```

If `F_r^+` is the number of bounded faces, Euler gives

```math
F_r^+=E_r^+-V_r^++1.
\tag{121.5}
```

Bounded-face incidence is exact:

```math
2E_r^+-a_r
=4F_r^+-T_r+Q_r^+.
\tag{121.6}
```

Substitute (121.4)--(121.5) into (121.6).  After cancellation,

```math
\boxed{
a_r-3-s_r
={a_r-T_r+Q_r^+\over2}.
}
\tag{121.7}
```

This is an exact finite identity.  Every term on the right is nonnegative.

---

## 121.2 Exact polygon-dissection deficit

Canonical Section 83 proves that the convex cells `P_r` have pairwise disjoint
interiors.  Triangulate every `P_r` using only its attachment vertices.  The resulting
straight-line triangles have disjoint interiors and form a noncrossing graph on the
`q` loaded vertices of the convex force hull.

The total number of triangles is

```math
\sum_r(a_r-2).
```

A noncrossing straight-line graph on `q` vertices in convex position has at most
`q-2` bounded triangular faces.  Hence

```math
\boxed{
d_{tile}:=q-2-\sum_r(a_r-2)\ge0.
}
\tag{121.8}
```

Write

```math
a:=\sum_r a_r,
\qquad c_I:=\#\{I_r\},
\qquad s_C:=\sum_r s_r.
```

Then

```math
d_{tile}=q-2-a+2c_I.
\tag{121.9}
```

Canonical Section 62 gives the exact pinned ledger

```math
c_I+e_{BB}+s_C=q-2+k.
\tag{121.10}
```

Subtract (121.9) and rearrange:

```math
e_{BB}-k
=(a-3c_I-s_C)+d_{tile}.
\tag{121.11}
```

Summing (121.7) over `r` gives

```math
a-3c_I-s_C
={1\over2}\sum_r(a_r-T_r+Q_r^+).
\tag{121.12}
```

Therefore

```math
\boxed{
e_{BB}-k
={1\over2}\sum_r(a_r-T_r+Q_r^+)+d_{tile}.
}
\tag{121.13}
```

This is the exact augmented-cell defect ledger in the current post-ZF notation.
In particular,

```math
\boxed{
\sum_rQ_r^+\le2(e_{BB}-k).
}
\tag{121.14}
```

Canonical Section 63 further identifies

```math
e_{BB}=Q+2k+u_B+c_B,
```

so equivalently

```math
\boxed{
e_{BB}-k=Q+k+u_B+c_B.}
\tag{121.15}
```

Thus local harmonic-cell face defect is paid by the global bounded-face/topology/outer
loaded-contact slack and cannot be replicated independently in many cells.

---

## 121.3 Compare the actual induced harmonic graph to `J_r^+`

Let `H_r` be the actual induced harmonic graph used in Sections 82, 116 and 120.  It
contains all internal and attachment contacts and every loaded-loaded unit contact
whose endpoints both lie in `A_r`.  Let

```math
Q_r:=\sum_{f\text{ bounded in }H_r}(\deg f-4)
```

over its bounded nonquadrilateral faces, and let `f_r` be their number.  Then

```math
P_{{\rm exc},r}=4f_r+Q_r.
\tag{121.16}
```

Add the missing polygon sides of `P_r` to `H_r`, obtaining `\widehat H_r`.  This
changes only the outer face, so every bounded nonquadrilateral face of `H_r` remains a
bounded face of `\widehat H_r`.  Therefore

```math
Q_r\le Q(\widehat H_r).
\tag{121.17}
```

On the other hand `\widehat H_r` is obtained from `J_r^+` by adding the remaining
loaded-loaded contact chords between vertices of `A_r`.  These chords are noncrossing.
Adding a chord to a face cannot increase total degree-above-four defect: if a face of
degree `m` is split into degrees `m_1,m_2`, then

```math
m_1+m_2=m+2
```

and

```math
(m_1-4)_++(m_2-4)_+\le(m-4)_+.
\tag{121.18}
```

Iterating over all loaded-loaded chords gives

```math
Q(\widehat H_r)\le Q_r^+.
\tag{121.19}
```

Hence

```math
\boxed{Q_r\le Q_r^+.}
\tag{121.20}
```

Every bounded nonquadrilateral face has degree at least five, so `f_r<=Q_r`.  Thus

```math
P_{{\rm exc},r}=4f_r+Q_r\le5Q_r\le5Q_r^+.
\tag{121.21}
```

Summing and using (121.14),

```math
\boxed{
\sum_rP_{{\rm exc},r}
\le5\sum_rQ_r^+
\le10(e_{BB}-k).
}
\tag{121.22}
```

This proves (121.1).

---

## 121.4 Interaction with Section 120

Section 120 proves in Type II

```math
\liminf {1\over D}
\sum_r(L_r+P_{{\rm exc},r}-2d_r)
\ge {\pi\over2}(2-\sqrt3).
\tag{121.23}
```

Section 121 shows that the bounded-defect-face part of this demand is globally paid:

```math
\sum_rP_{{\rm exc},r}
\le10(e_{BB}-k).
\tag{121.24}
```

The remaining uncontrolled quantity is therefore the aggregate outer-walk detour

```math
\boxed{\sum_r(L_r-2d_r).}
\tag{121.25}
```

This is a sharper closure target than the original sum.  A theorem making
`e_{BB}-k` small would force a positive fraction of the Section-120 demand directly
onto (121.25); alternatively one can try to pay (121.25) from the global
loaded-hull/diameter structure.

The coefficient `10` in (121.22) cannot be reduced by generic face degree alone: a
pentagonal face has `P_exc=5` and `Q=1`.  Any useful improvement must use additional
geometry or the contact/diameter structure, not a different rewriting of Euler.

---

## 121.5 Scope and hostile checks

- All `I_r` are nonisolated positive-contact components. Contact-isolated source
  points are retained globally and are never inserted into the §57 affine kernel.
- Section 121 uses the current canonical Section-62 pinned ledger, not stale PA/ZJ
  labels from the older unreviewed attachment-tiling report.
- The dissection inequality uses only canonical Section-83 interior disjointness of
  the actual convex attachment cells.
- Loaded-loaded contact chords can only decrease the augmented degree defect; equation
  (121.18) covers triangular and quadrilateral daughter faces as well as large ones.
- The theorem controls local exceptional-face perimeter with one global scalar
  `e_BB-k`; it makes no claim that local outer-walk occurrences are globally disjoint.
- The factor `5` in `P_exc<=5Q` is exact at the combinatorial level and the final
  factor `10` comes solely from (121.14).

**Disposition:** proof-only structural theorem.  The theorem-state manifest is not
modified. C-II remains open.
