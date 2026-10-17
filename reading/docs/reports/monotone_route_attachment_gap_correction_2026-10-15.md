> Generated reading edition · [exact source](../../../docs/reports/monotone_route_attachment_gap_correction_2026-10-15.md) · source SHA-256 `7dfdc82217262377128e56af3fe5b85ba7b63aeffc7ed47b89af316ed4a225eb`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-752EFC350D1A","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# Monotone-route source reconciliation and attachment-gap correction

Date: 2026-10-15. Baseline main `5056b01a620858445a6f30877934822066674601`.
Frozen source: `research/c2-deep-port-grid-audit-20261004` at
`e275fc53d92d543c78421e76dacc245832d79b86`.
Classification: noncanonical preservation and proved candidates awaiting
independent human mathematical review. This Codex-assisted audit does not
promote a theorem or close C-II or Level I.

## Complete source disposition

The five unique commits comprise the initial route-obligation note, the
monotone-route report/checker, the deep-port multiplicity extension, one merge,
and an explicit infinite Pell-family update. The report and its separate run
note were read in full and compared with
[Audit 124](../audits/target_c_monotone_route_debit_independent_audit_2026-10-08.md),
which pins the exact source report and checker hashes.

Sections 2–4's strict-successor forest, direction-independent charged vertex
set, exact shared bank, disjoint-tail inequality and overlap formula are
reconstructed in that audit. Section 7's all-size Pell construction and
attachment-triangle debit are likewise preserved there; the audit extends the
displayed greedy-route prefix to a complete route without changing the sharp
limiting ratio. The exact checker already survives at
[its original path](../../../research/verify_target_c_monotone_cap_routes_2026_10_04.py).
Its unmodified source SHA-256 is
`ff6c3beba4fd18ebb811b14b82be0cefa1e6deaab91ae174a75aac4318738a3b`.
The run note supplies no additional theorem. Sections 1, 8 and 9 preserve the
same unresolved route-overlap/payment and full-source endpoint obligations.

Section 6's high-grid application is conditional: a co-located quadratic
coherent cap grain with linear perimeter is supplied. Cutting above height
`area(G)/(4D)` loses at most one quarter of its area and `O(D)` boundary
rhombi. Isoperimetry and the inherited finite pseudogrid argument yield a
quadratic high component with linear grid shores. Strict projection ascent
then ends at a path-selected same-host attachment above that height. This
does not extract the cap from an arbitrary source, select the earlier deepest
port, bound route overlap or give a finite move. Audit 124 already records
that conditional scope.

The remaining distinct content is Section 5, whose rejection in Audit 124
used an incorrect leaf objection. The correction and complete candidate
argument follow. No obsolete source promotion transaction is imported.

## A leaf bridge and a leaf occurrence are different counts

Let `H_0` be the connected plane graph of actual internal and attachment
contacts in one unloaded component `I` and its loaded attachment set `A`.
There are no loaded-loaded edges in `H_0`; every attachment is a strict
vertex of `P=conv(A)`. Deleting an attachment `a` leaves connected `I` and
every remaining attachment adjacent to it. Thus `a` is not a cut vertex.

A nonisolated noncut vertex belongs to exactly one block. If that block is
2-connected, its facial boundaries are simple cycles. Other blocks attach at
other vertices and can insert excursions there, so they add no occurrence of
`a`. If its sole block is a bridge, `a` is a leaf: the outer traversal uses
the bridge in both directions and visits `a` exactly once between them.
Since `a` is an extreme hull vertex, it is on the outer facial walk. In both
cases it therefore has exactly one occurrence on that walk.

For example, the exact positive-equilibrium four-point star from Audit 124's
own attachment-triangle regression has outer walk
`(0,1,0,3,0,2)` when `0` is the center. Every leaf appears once and every
bridge is traversed twice. The new
[exact witness](../../../research/verify_attachment_outer_walk_correction_2026_10_15.py)
checks all six source distances, positive equilibrium, every directed
half-edge, the leaf counts and the three augmented pockets. This disproves
the former objection; the block argument proves the general assertion.

## Preserved finite attachment-gap candidate

Write the attachments in their cyclic hull order as `b_1,...,b_a`, and let
`ell_i` be the occurrence length of the unit-contact outer-walk arc from
`b_i` to `b_(i+1)`. The preceding lemma makes these consecutive arcs
well-defined, including leaf attachments and repeated unloaded occurrences.

Add all `a` sides of `P` as designated polygon edges. They lie outside the
contact graph's bounded faces. Euler's formula creates `a` bounded pockets;
each has a polygon side, and each such side is incident to one bounded
pocket. The `a` pockets and `a` sides are therefore in bijection. The pocket
at side `i` has degree `ell_i+1`. Equivalently, this is the canonical
augmented-cell crosscut topology used by Audit 134. Hence, with
`Q^+=sum_f(deg(f)-4)_+`,

```text
Q^+ >= sum_i (ell_i-3)_+
    >= sum_i (|b_i-b_(i+1)|-3)_+,
per(P) <= 3a+Q^+.
```

Summing once over distinct cells and using the canonical single global
budget gives `sum_r per(P_r)<=3 sum_r |A_r|+2(e_BB-k)`. Polygon sides
are used to count pockets; they are not contact-route edges.

For the source's deep-port consequence, let a measurable `G subset P` have
area `A_G>0` above a designated host chord, and let `eta` be signed unit
height positive on that host arc. The full source diameter is `D`, so every
slice of `P` parallel to the chord has length at most `D`. Put
`H=max_P eta` and `tau=H-A_G/(2D)`. Then `H>=A_G/D`,
`min_P eta<=H-A_G/D`, and `tau>=A_G/(2D)>0`.

Along a convex polygon, total variation of `(eta-tau)_+` around its boundary
is `2(H-tau)=A_G/D`. Only edges incident to vertices with `eta>tau`
contribute, and there are at most twice as many such edges as deep vertices.
Their chord lengths dominate that variation. Apply the pocket estimate to
these distinct sides, charging each pocket once, to obtain

```text
6N_deep+Q^+ >= A_G/D.
```

Thus either `N_deep>=A_G/(12D)` or `Q^+>=A_G/(2D)`. In the latter case
the global budget implies `e_BB-k>=A_G/(4D)`. All positive-height loaded
vertices lie on the designated host arc under the source's explicit chord
separation hypothesis. Different caps in the same cell cannot each spend
another copy of `Q^+`.

These are finite structural candidates. They supply neither a macroscopic
cap, a lower bound on route-excess demand, bounded overlap, stress payment,
nor a cardinality-preserving strict-diameter replacement. They remain outside
the canonical manifest pending independent human review.

```sh
python3 research/verify_target_c_monotone_cap_routes_2026_10_04.py
python3 research/verify_attachment_outer_walk_correction_2026_10_15.py
```
