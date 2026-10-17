> Generated reading edition · [exact source](../../research/target_c_bounded_face_endpoint_simplicity_2026-09-12.md) · source SHA-256 `7bc377c455d215ffc7a57b7b52d328ce5244323e7f5734aed3cd8540a1774afc`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "2b48510071d9c20f6399ab457095e34e88a6c222", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_bounded_face_endpoint_simplicity_2026-09-12.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "f99fe319273d97c8179b611e38c3ac7801226b570fb1deaebc056bceeb3570e4"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C — bounded-face train endpoint simplicity

**Date:** 2026-09-12  
**Status:** proof-only structural candidate; theorem-state authority unchanged.  
**LEVEL I STATUS:** STILL OPEN. C-II REMAINS OPEN.

The bounded-face endpoint multigraph has no repeated edge: two distinct complete
stopped trains cannot have one terminal occurrence on each of the same two bounded
nonquadrilateral faces.

The implication chain is

```text
two trains with the same bounded endpoints
  -> an innermost Jordan cycle using one segment of each train
  -> no active diameter endpoint in the cycle interior
  -> positive KKT contact resultants along at most two train directions
  -> the directions are parallel
  -> the parallel pair-cut theorem gives a mixed-flex contradiction.
```

## 1. Two-train cycle

Represent each complete train by its canonical transverse midpoint arc from one
stopping face to the other. If the arcs are disjoint, join corresponding terminal
midpoints through the open interiors of the two bounded faces. If they cross, choose
an innermost lens (or the two prefixes on one face). In either case planarization and
local smoothing produce a simple Jordan curve `Gamma` whose contact-graph crossings
are precisely the selected train-edge occurrences. All selected rhombi and face arcs
lie in the convex hull `K` of the full source, so

```math
\Gamma\subset K,
\qquad \operatorname{Int}(\Gamma)\subset K.
\tag{1.1}
```

Let `S` be the nonisolated positive-contact-core vertices in the Jordan interior. A
crossed train edge makes `S` nonempty. Every active diameter endpoint is extreme in
`K`, hence outside `S`; no active diameter row crosses the cut.

## 2. KKT resultant

Sum the relative-interior positive KKT equilibrium equations over `S`. Internal
contact forces cancel and there is no diameter contribution. Each connected selected
train portion contributes a nonzero vector

```math
\epsilon_iA_i u_i,
\qquad A_i>0,
\qquad \epsilon_i\in\{+1,-1\},
\tag{2.1}
```

because all crossed edges in that train have one coherent projective direction and
orientation. Thus

```math
\epsilon_1A_1u_1+\epsilon_2A_2u_2=0.
\tag{2.2}
```

If one selected portion is absent, its single nonzero resultant already contradicts
equilibrium. Otherwise (2.2) forces `u_1,u_2` to be projectively parallel.

The already audited parallel stopping-face pair-cut theorem then applies in the
disjoint case and supplies the piecewise transverse mixed flex `Ju` on the inside
shore and zero outside. It annihilates every active contact and diameter row and is
non-Euclidean, contradicting the canonical Section-57 mixed-rigidity rank.

Therefore the repeated bounded-face pair cannot exist.

## 3. Scope

This is a finite proof-only structural result. It uses canonical train pseudosegment
geometry, positive relative-interior KKT equilibrium, active-diameter endpoint
extremality, the bounded-face loop exclusion, and the audited same-direction pair cut.
It retains contact-isolated points and applies rigidity only to the nonisolated core.
It does not control repeated outer-face incidences, mixed outer/bounded pairs, or the
aggregate outer-walk detour. C-II remains open.

**Classification:** proved candidate awaiting promotion; proof-only.
