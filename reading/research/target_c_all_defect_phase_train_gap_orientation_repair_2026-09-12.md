> Generated reading edition · [exact source](../../research/target_c_all_defect_phase_train_gap_orientation_repair_2026-09-12.md) · source SHA-256 `134ffb704d72055559204d52e1a68538cc713e22af65749163a73475da6951c7`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "ca5c44604f0216be2963b4bcc2cae0eb4770a90e", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_all_defect_phase_train_gap_orientation_repair_2026-09-12.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "c7b15e217bacb0fcdba8b82e2dc7d28ff5794f9682ee48a0b5b91fd792cb5ae7"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C — orientation repair for the all-defect stopped-train theorem

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**  
**Status:** proof-only repair companion to `target_c_all_defect_phase_train_gap_2026-09-12.md`; theorem authority unchanged.

This note repairs one local orientation sentence in Lemma 1.1 of the all-defect
phase/train-gap theorem. The theorem's conclusion and all later inequalities are
unchanged.

The original proof correctly observes that every component of the auxiliary graph
`Xi` has one fixed projective contact-edge direction, but it then orients each
opposite-edge displacement independently and immediately says that the `Ju` coordinate
increases along the component. Independent orientations of links do not by themselves
orient an undirected component. The missing local fact is the two-sided incidence at an
internal train edge.

## Corrected Lemma 1.1

Fix one component of `Xi` and choose an orientation `u` of its common projective
contact-edge direction. For every contact edge `e` in this component, let

$$
h(e):=J u\cdot m(e),
$$

where `m(e)` is the midpoint of `e`.

If a strict unit rhombus has opposite `u`-parallel sides `e,e'`, then the vector
`m(e')-m(e)` is parallel to the other pair of rhombus sides. Since a triangle-free
unit rhombus has acute projective side-angle in `(pi/3,pi/2]`, the two opposite
`u`-edges have distinct `h`-coordinates. Thus every link of `Xi` joins two vertices
with different `h` values. Orient that link from lower `h` to higher `h`.

Now let `e` be a degree-two vertex of `Xi`. The two strict rhombi incident to `e` lie
on opposite sides of the physical contact segment `e`: two distinct bounded faces of a
plane straight-line contact embedding cannot occupy the same local side of an edge.
Consequently the opposite `u`-edge in one incident rhombus lies on the `+Ju` side of
`e`, while the opposite `u`-edge in the other incident rhombus lies on the `-Ju` side.
Therefore exactly one of the two incident links at `e` is oriented into `e` and exactly
one is oriented out of `e`.

Every vertex of `Xi` has degree at most two. If a component of `Xi` were a cycle, all
of its vertices would have degree two, and the preceding local rule would orient the
cycle consistently: every vertex would have indegree one and outdegree one. But along
every directed link the scalar `h` strictly increases. Following the directed cycle
would therefore give

$$
h(e_0)<h(e_1)<\cdots<h(e_m)=h(e_0),
$$

an impossibility.

Hence `Xi` has no cycle. Since its maximum degree is two, every component is a path;
a contact edge incident to no strict rhombus is a singleton path. Thus, with `e`
vertices and exactly `2R` opposite-edge links,

$$
T=e-2R.
$$

This supplies the missing orientation argument used by the exact stopped-train ledger.
No other part of the all-defect theorem depends on the erroneous wording.

## Scope check

- The argument is entirely on the nonisolated positive-contact core.
- Contact-isolated source points remain in the full source and are not inserted into
  `Xi` or the Section-57 affine kernel.
- The proof uses only planar face incidence and strict-rhombus geometry; it does not use
  a KKT coefficient floor, a train-angle flex theorem, or any rejected Target C route.
- Bridges and articulation vertices are harmless because the statement is about the
  edge-based auxiliary graph `Xi` and its local bounded-face incidences.

**Disposition:** the hostile-review objection to Lemma 1.1 is repaired at proof-only
scope. The all-defect phase/train-gap theorem remains noncanonical and C-II remains
open.