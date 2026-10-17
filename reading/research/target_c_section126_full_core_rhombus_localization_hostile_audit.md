> Generated reading edition · [exact source](../../research/target_c_section126_full_core_rhombus_localization_hostile_audit.md) · source SHA-256 `95f167b7c3e45f5217c974d7e7cc26d0f326244ac0139e5a15b6920ff2fe4443`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "d79eb1b37ec68c39ce899a93f8dc85f4cd337e6a", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_section126_full_core_rhombus_localization_hostile_audit.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "aa50238982242786ec97f0e7030a0968d730c712db2441cc1f8d121f996d9d7b"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C — hostile audit of Section 126 full-core rhombus localization

**Date:** 2026-09-12
**Base theorem state:** `2026-09-12.audit.46`
**Reviewed source:** `research/target_c_section126_full_core_rhombus_localization.md`
**Verdict:** **PASS at proof-only Type-II scope after one repair to the older draft.**
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

## 1. Claim under review

The section claims that, after proof-only Section 124 gives `c_B=0`, the number of
full-core strict-rhombus faces not realized as local quadrilateral faces of the
canonical harmonic graphs satisfies

$$
0\le R_4-\sum_rR_r\le3c_I+5=o(D).
$$

It also claims the same `o(D)` bound for missing strict-rhombus area.

The proof is a corrected and strengthened extraction from the older proof-only PR #353.
The important repair is numerical: the older draft said a unit rhombus has area at most
`sqrt(3)/2`, which is false because a unit square has area one. Section 126 uses the
correct universal bound `area<=1`; the `o(D)` conclusion is unchanged.

## 2. Local quadrilateral fidelity

A local quadrilateral in `H_r` is a strict unit rhombus by canonical Section 82. Both
diagonals are at least one by source separation and cannot equal one without forming a
unit equilateral triangle. For a unit rhombus, the squared diagonals sum to four, so
every half-diagonal is strictly less than one.

Splitting at the rhombus center produces four triangles of diameter one whose unique
unit-length edge is a rhombus side. Any omitted source point in the relative interior
would be strictly less than one from a side endpoint. Unit separation therefore rules
out omitted source points in the rhombus interior or in the relative interior of a
side. Straight-line contact planarity rules out an omitted crossing contact edge, and
the diagonals are noncontacts.

Thus every local quadrilateral is an actual full-core face.

Duplicate local counting is impossible. An unloaded rhombus vertex determines its
component. If all four vertices are loaded, duplicate counting would give two distinct
components at least three common attachments, contradicting canonical Section 83.

**Verdict:** PASS.

## 3. Missing-rhombus classification

### Zero or one loaded vertex

The unloaded contact path lies in one component and every loaded cycle vertex attaches
to it. The full-core face is local. No missing face occurs.

### Two adjacent loaded vertices

The two unloaded vertices are contact-adjacent and hence lie in one component; both
loaded vertices attach. Again the face is local.

### Two opposite loaded vertices

A missing face requires two distinct unloaded components sharing the same two opposite
loaded attachments. Their interior-disjoint convex cells both contain the loaded
segment, so that segment is a common side. A fixed component pair cannot share two
different loaded pairs without violating the Section-83 common-attachment bound. A
fixed loaded opposite pair determines at most one unit rhombus. Hence missing faces of
this type inject into cell-side adjacencies. The dual adjacency graph of pairwise
interior-disjoint convex cells is planar, giving the coarse bound `<=3c_I`.

### Three loaded vertices

If the middle loaded vertex attached to the unloaded component, the face would be
local. Otherwise both unit edges incident to that middle loaded vertex are
loaded-loaded contacts. Section 124 makes them consecutive global hull sides. The
rhombus angle at the middle vertex is therefore the global hull interior angle.
Triangle-freeness makes both diagonals strictly larger than one, forcing the angle into
`(pi/3,2pi/3)`, hence exterior turn `>pi/3`. Total hull turn is `2pi`, so at most five
such vertices occur. The two hull neighbors determine at most one fourth rhombus
vertex, so the class size is at most five.

### Four loaded vertices

Section 124 makes all four unit sides global hull sides. That would force the global
loaded hull to have exactly four vertices. Type II has `q=Omega(D)`, so this class is
empty for all sufficiently large members.

**Verdict:** PASS.

## 4. Asymptotic and area conversion

The classification gives exactly

$$
0\le R_4-\sum_rR_r\le3c_I+5.
$$

Canonical Section 75 supplies `c_I=O(D^(2/3))`, hence the count loss is `o(D)`.

For the area statement the safe universal fact is

$$
\operatorname{area}(\text{unit rhombus})=\sin\theta\le1.
$$

Therefore the missing-area sum is at most the missing-face count and is also `o(D)`.
No stronger area cap is used.

**Verdict:** PASS after correcting the older `sqrt(3)/2` sentence.

## 5. Scope checks

- Section 126 is Type II only because it depends on proof-only Section 124.
- Contact-isolated source points remain part of the full source.
- No full-source affine-kernel statement is used.
- The theorem is about actual full-core strict-rhombus faces and actual induced
  harmonic cells.
- It strengthens the earlier `O(D)` loaded-touching discard to `o(D)` but does not
  control the aggregate outer-walk detour or close C-II.

**Final verdict:** PASS, proof-only. The corrected theorem safely absorbs the unique
missing-rhombus content of PR #353 into the newer post-123 structural branch.