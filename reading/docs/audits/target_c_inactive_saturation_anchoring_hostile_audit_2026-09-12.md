> Generated reading edition · [exact source](../../../docs/audits/target_c_inactive_saturation_anchoring_hostile_audit_2026-09-12.md) · source SHA-256 `21a52b6873d22af325860e90564aed525f96123284c81696319ea458c673a0f2`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-EAD0B7182B59","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Hostile audit — inactive-chamber saturation and weak-component anchoring

**Date:** 2026-09-12
**Audited artifacts:**

- [`target_c_contact_saturation_no_isolates.md`](../../research/target_c_contact_saturation_no_isolates.md);
- [`target_c_internal_chamber_weak_component_anchoring.md`](../../research/target_c_internal_chamber_weak_component_anchoring.md).

**State lock:** `2026-09-12.audit.46`
**Verdict:** **PASS at proof-only scope; theorem state unchanged.**

This audit validates two finite normalizations for a hypothetical triangle-free
global minimizer. They are useful structural reductions for the macroscopic internal
inactive-chamber branch, but neither supplies the missing source-level contradiction.

## 1. Saturating actual contact isolates

Let `A` be a finite noncollinear unit-separated source, `K=conv(A)`, and let `x` be
strictly farther than one from every other source point. The union of the closed unit
disks centered at the other source points does not contain `x`. Since `K` is
two-dimensional, a small wedge of `K` near any unchanged source point lies inside
one of those disks, so a target point can be chosen in the interior of the union.

The ray from `x` to that target can avoid the finite set of pairwise unit-circle
intersection points. The first entry into the disk union therefore creates exactly
one unit contact. This is a finite genericity argument; it does not assume a
positive KKT multiplier or a preselected contact direction.

If `A` is a global diameter minimizer, the moved point remains in `K`, so the new
source has diameter at most `diam(K)`. Global minimality forces equality. Exactly one
new contact is created, so triangle-freeness is preserved: a triangle through the
moved point would require two new incident contacts. Repeating the move terminates
because the number of contact-isolated vertices decreases at every step.

For the canonical contact-minimal, then diameter-pair-minimal source, the additional
diameter-safe genericity is valid. The polygon `K` meets each diameter circle in a
finite set, so the ray can avoid all old diameter-equality points. The actual diameter
graph is consequently unchanged at every move. This does not delete any source point;
each isolate is moved and remains part of the source.

## 2. KKT-invisible forest check

The old canonical actual contact graph has no weak contacts by the promoted C-I
normalization. Each saturation move adds one edge incident to a vertex that was
isolated immediately beforehand. Thus the new edges form a forest. A new tree can
have at most one attachment to the old core: a later moved vertex was isolated before
its own edge was added, so it cannot add a second edge to an already existing tree.

The diameter-safe choice leaves every noncore saturated vertex without a diameter row.
In an arbitrary KKT stress of the saturated source, peel a leaf of each new forest
tree that is not its possible old-core root. Its equilibrium equation contains only
the multiplier of its incident forest edge, so that multiplier is zero. Repeating
leaf elimination gives zero weight on every new forest edge. Restriction to the old
contact and diameter rows and zero extension are inverse operations, so the old
normalized KKT polytope is unchanged.

This conclusion is deliberately limited to the saturated representative. It does
not extend the Section-57 affine-kernel theorem to the new vertices, and it does not
turn weak forest edges into positive-force rows in the canonical contact-minimal
representative.

## 3. Internal-chamber anchoring check

Fix a bounded inactive chamber whose boundary is a convex unit-contact face of the
old positive core. Keep the old core fixed and maximize the number of triangle-free
unit contacts among the labeled chamber points. The maximum exists at the level of
integer contact counts; no compactness claim is needed.

If a contact component consisting of moved chamber points had no old-core vertex,
its finite rigid body could be moved generically inside the chamber. A cross-contact
must occur before a chamber boundary side can be reached: every boundary side is a
unit edge, and approaching its interior makes the distance to at least one endpoint
strictly less than one before the boundary is reached. A generic first cross-contact
can be chosen unique, so triangle-freeness is preserved. This increases the contact
count without moving the old diameter pair, contradicting maximality.

Any chamber-to-core contact from an interior chamber point lands at a boundary vertex.
Otherwise the contact segment would leave the face, crossing a contact edge or passing
through a boundary vertex; both alternatives violate unit-separation/planarity.

At a boundary vertex, the two boundary neighbors already occupy an angle at most
`pi`. Every distinct unit neighbor pair has angular separation strictly greater than
`pi/3` in a triangle-free unit-separated source. Therefore at most one additional
unit-contact edge can enter the chamber sector. Distinct weak components consume
distinct boundary vertices. If the chamber has `z` moved points and `p` boundary
vertices, some anchored weak component has at least `z/p` vertices. In the canonical
macroscopic chamber, `z=Omega(D^2)` and `p=O(D)`, hence the component is
`Omega(D)`.

## 4. Exact limitations

The audit does **not** certify any of the following stronger statements:

- that the anchored weak component has `Omega(D^2)` vertices;
- that it contains a cycle or any positive KKT stress;
- that it forces a unit equilateral triangle;
- that weak-contact maximization preserves the canonical positive-contact support;
- that an exterior cap obeys the same boundary-escape argument; or
- that the macroscopic chamber admits a protected finite `k -> k+1` exchange.

The close-to-triangular strict-lattice regression and the KKT-realizable activation
regression show why those upgrades cannot be inferred from density or first-contact
creation alone. The exact unresolved bridge is:

$$
\text{large anchored KKT-invisible weak component}
\Longrightarrow
\text{triangle, strict same-cardinality sub-`D` source, or core contradiction}.
$$

## 5. Classification

The two source artifacts are **audited-working / proof-only**. They are not canonical
dependencies, and C-II remains open. Contact-isolated source points are retained in
all finite comparisons; no full-source ZR/ZF assertion is made.
