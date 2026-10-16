<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "91270505296d08af9973d4559682246b7ec7fd3f", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support6_collapsed_destination_capacity_2026-09-18.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "d3b07549b3f022d43706ee1ce2a1e2ef21e8e0fd377f98f1a4c8b594a4f0843e"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — activated destinations have capacity two for a collapsed anchor direction

**Date:** 2026-09-18  
**Status:** proved candidate; scoped finite capacity reduction  
**Certificate:** `research/verify_target_c_support6_collapsed_destination_capacity_2026_09_18.py`

Let `m_6` be the number of collapsed support-six components and let `r_O` be the
number of their six anchor trains that terminate on the actual outer face.  All
`6m_6` anchors have one common projective direction.  A bounded activated contact
face is a strict convex polygon, so it can contain at most two side occurrences in
that projective direction: repeated sides with the same orientation are impossible,
and the only possible pair is an oppositely oriented pair.  If `a_F` is the number
of activated bounded faces, then

\[
\boxed{6m_6\le r_O+2a_F.}
\tag{DC.1}
\]

The outer face is deliberately not assigned capacity two; its occurrence-counted
boundary can repeat a projective direction.  Thus (DC.1) is valid without a hidden
outer-boundary simplicity assumption.

Combining (DC.1) with the audited pair-shield flex bound gives the exact finite
payment

\[
m_D\ge {b-f\over2}+a_F+{x_A\over2}+{n_0+n_2\over2}+p_U,
\]

so any collapsed population whose anchor mass is not predominantly outer-facing
forces activated-face flex.  In particular, if `r_O=o(m_6)`, then
`a_F\ge3m_6-o(m_6)`.  The remaining sharp branch is the outer-facing alternative
`r_O\approx6m_6`, where common-outer train order, corridor interaction, and source
separation must be resolved.

This does not close the mixed activated-host branch: activated faces may be shared by
two collapsed anchors, and the outer face has no corresponding bounded-face capacity.

**Classification:** proved candidate at exact endpoint-capacity scope; C-II remains
open.
