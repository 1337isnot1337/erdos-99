> Generated reading edition · [exact source](../../research/target_c_cell_pure_full_5faces_hostile_audit_2026-09-15.md) · source SHA-256 `f15bb9a8e7cd45a992f469e74ce401f8d7c76d5126e2390920757313fd8d0ad5`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "570ca10db1995e672c8557599c87b97fb3c1d22b", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_cell_pure_full_5faces_hostile_audit_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "7a1f7f4d93ff3a34b14ff1d53fbc90325e2ae7aed257c02da3bb1bc135718be5"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — harmonic-cell purity of full rhombic 5-faces

**Date:** 2026-09-15
**Reviewed:** `research/target_c_cell_pure_full_5faces_2026-09-15.md`
**Verdict:** `PASS` at the stated proof-only scope.

> **Preservation provenance (2026-10-05):** copied with the reviewed source report from `research/c2-flower-high-t-sol-20260915` at exact source tip `7de4cdc3e9aa0cac5b278c2ccc17158bd8d66bdb`. The original audit's `PASS` is at the stated proof-only scope; the claim remains unreviewed and noncanonical in the current state lock. The Section-129 localization dependency named by the report is not state-locked as canonical.

The proof has three possible local failure modes; none survives.

1. **A neighboring rhombus cannot reuse the other 5-face side at the vertex.** A bounded rhombus adjacent across `AB` occupies the face sector on the side of `AB` opposite the 5-face. Its second edge at `B` therefore cannot be `BC`, which bounds the 5-face sector. Equivalently, two distinct bounded face sectors cannot both occupy the same local sector at `B`. Thus each of the two rhombi really contributes a contact at `B` in addition to `BA,BC`, unless the two rhombi share that new contact with each other.

2. **The loaded-vertex branch is exhaustive.** Canonical Section 78 gives contact degree at most three at a `B_D` vertex. Since `BA,BC` already consume two distinct contacts, the two transverse rhombus contacts must be one common edge `BX`. If `X` were also in `B_D`, the Type-II unit-chord theorem would make `BX` a force-hull side. A force-hull side has the source on only one side and cannot be incident to bounded rhombus faces on both sides. Hence `X` is in `V minus B_D`, giving the common unloaded component used by the label argument.

3. **The `o(D)` cleanup has bounded multiplicity.** A nonlocal rhombus has only four sides and hence can touch at most four full 5-faces. The standard deletion removes at most two complete trains per nonlocal rhombus. Each complete train has at most two terminal occurrences. Therefore both the rhombus cleanup and the train cleanup contaminate only `o(D)` flowers.

The cyclic propagation then gives one cell label on all five neighboring rhombi and, after train cleanup, on all five terminal trains.

The theorem does not claim that different cell-pure 5-faces have different cells, that one cell contains linearly many such faces, or that cell purity alone forces a metric gap.

**Disposition:** PASS. C-II remains open.
