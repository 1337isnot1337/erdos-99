> Generated reading edition · [exact source](../../../docs/audits/target_c_section120_aggregate_two_arc_detour_self_audit_2026-09-12.md) · source SHA-256 `045ea6ac129cfe766766e4e284f5590ed79200f2df28d0fe4aaf1e5e1c4f0a8c`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-7EC4EB258F25","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — hostile self-audit of Section 120 aggregate two-arc detour

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**  
**Artifact audited:** `research/target_c_section120_aggregate_two_arc_detour.md`  
**Disposition:** proof passes this same-run hostile audit; theorem authority is unchanged.

This audit attacks the only nontrivial globalization step in Section 120: whether the
strict-rhombus area used in the local Section-116 inequalities can be summed over all
harmonic components without losing faces or charging one physical rhombus twice.

## 1. Local Section-116 scope is satisfied

For each unloaded positive-contact component `I_r`, canonical Section 62 supplies its
attachment set `A_r` and convex harmonic cell

$$
P_r=\operatorname{conv}(A_r)\subset F.
$$

The induced graph `H_r` used in Section 120 is exactly the harmonic induced graph used
by the local near-quadrangulation machinery: all vertices of `I_r`, all loaded
attachments `A_r`, all positive contacts among them, and every loaded-loaded unit
contact whose endpoints both lie in `A_r`.

The Section-116 two-arc companion is finite. It requires only the full strict-rhombus
complex of this induced harmonic graph, its occurrence-counted outer walk and bounded
nonquadrilateral face cycles, and the diameter `d_r=diam(P_r)`. It does not require
that the cell be the distinguished Section-78 carrier or that its rhombus area be
quadratic. Thus applying

$$
d_r(L_r+P_{{\rm exc},r}-2d_r)
\ge(4-2\sqrt3)A_{4,r}
$$

to every harmonic component is within scope.

## 2. An unloaded-only global rhombus persists as a face of exactly one `H_r`

Let `R` be a bounded strict-rhombus face of the full positive-contact core and assume
all four of its vertices are unloaded.

1. Its four unit sides form a connected cycle of unloaded contact vertices. Therefore
   all four vertices lie in one unloaded component `I_r`.
2. Canonical Section 67 proves that the interior of a bounded strict unit-rhombus face
   contains no source point.
3. Neither diagonal is a unit contact. For a strict triangle-free unit rhombus the
   acute angle is greater than `pi/3`; the short diagonal is therefore strictly
   greater than one, while the long diagonal is at least `sqrt(2)`. Hence the induced
   graph cannot add a contact chord through the face.
4. Planarity prevents any other contact edge from properly crossing the four boundary
   sides.

Consequently the same four-cycle still bounds a face in `H_r`. Since unloaded
components have disjoint vertex sets, no other `H_s` can contain all four vertices.
Thus every unloaded-only global rhombus is assigned to exactly one harmonic induced
graph.

If `A_{4,r}^0` denotes the total area of these assigned faces, then the identity

$$
\boxed{\sum_r A_{4,r}^0=A_4^0}
$$

is exact. This is the required injectivity statement.

## 3. Loaded-touching rhombi are legitimately discarded

Section 120 never tries to assign a strict rhombus incident to a loaded vertex. This
avoids overlap caused by one loaded vertex belonging to several attachment sets.

Canonical Section 83 bounds the number of strict quadrilateral faces incident to the
loaded set by

$$
\sum_{b\in B}\deg_C(b)\le3q=O(D).
$$

Every unit rhombus has area at most one. Hence

$$
0\le A_4-A_4^0=O(D).
$$

This loss is lower order after division by `D^2` and cannot affect the Type-II
coefficient.

## 4. No boundary occurrence is globally double-charged

A different possible objection is that two induced harmonic graphs can reuse a loaded
contact edge or a loaded attachment vertex on their outer walks. Section 120 does not
identify its summed left-hand side with a global physical boundary length. It merely
adds valid scalar inequalities

$$
E_r\ge(4-2\sqrt3)A_{4,r}^0/d_r.
$$

No assertion that the boundary occurrences in distinct `E_r` are disjoint is needed
for this addition. Any later theorem that tries to pay `sum_r E_r` from one global
boundary/interface budget will need a separate multiplicity theorem. Section 120 does
not smuggle such a theorem in.

## 5. Global diameter comparison is safe

Every attachment polygon satisfies

$$
P_r\subset F\subset\operatorname{conv}(A).
$$

The convex hull of the full source has diameter `D`, so

$$
0<d_r\le D.
$$

Therefore

$$
\frac{A_{4,r}^0}{d_r}\ge\frac{A_{4,r}^0}{D}
$$

term by term. No source point is deleted and no core-only diameter is substituted for
the full-source diameter.

## 6. Type-II limit

The current authoritative Type-II stack gives

$$
A_4/D^2\to\pi/4.
$$

Together with the loaded-touching loss above,

$$
A_4^0/D^2\to\pi/4.
$$

Hence Section 120's finite inequality implies

$$
\liminf {1\over D}
\sum_r(L_r+P_{{\rm exc},r}-2d_r)
\ge {\pi\over4}(4-2\sqrt3)
={\pi\over2}(2-\sqrt3).
$$

The derivation is valid.

## 7. Hostile non-implications

The audit rejects the following stronger readings:

- the summed local detour is **not** yet a globally injective physical-boundary
  quantity;
- Section 120 does **not** upper-bound that detour from Oler or global minimality;
- it does **not** imply that one harmonic cell individually pays a fixed fraction of
  the total detour;
- it does **not** improve the canonical carrier coefficient `mu`;
- it does **not** touch the macroscopic inactive-container branch;
- it does **not** close C-II.

The exact next obstruction is multiplicity/global payment: turn the valid aggregate
local demand into a quantity that the full source can pay only once, or derive a
global-minimality upper bound on the same sum.

**Audit verdict:** Section 120 is a valid proof-only structural theorem. Promotion has
not been attempted. The authoritative theorem state remains audit.44 and C-II remains
open.
