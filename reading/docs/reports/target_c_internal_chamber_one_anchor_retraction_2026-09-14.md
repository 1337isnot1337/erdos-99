> Generated reading edition · [exact source](../../../docs/reports/target_c_internal_chamber_one_anchor_retraction_2026-09-14.md) · source SHA-256 `5524c249d1bf9a911629acaa88e3d2af9e85aff7cf82ad9a9f57058bb8edb57f`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-23F3D9094298","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_internal_chamber_one_anchor_retraction_2026-09-14.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=6798f510f9b46f518e218ad6e9d3a923aeaa7922; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — retraction of the one-anchor chamber deformation

**Date:** 2026-09-14
**Repository commit:** `ef941ab2b44aa393bdc461926769247b45754202`
**State version:** `2026-09-12.audit.46`
**Run type:** adversarial audit / rejected route
**Target:** C-II / macroscopic-container branch
**Starting status:** proof-only contact-max chamber normalization
**External literature search:** not used
**Computation:** not used

## LEVEL I STATUS

STILL OPEN.

An attempted refinement claimed that a contact-maximized weak chamber component with
one old-core anchor could be rotated about that anchor until a new admissible contact
appeared. The claim is false in the triangle-free class and is rejected here.

## Failed claim

The proposed implication was

```text
one chamber component + one core edge
    -> rotate about the core endpoint
    -> first new contact is triangle-free
    -> contact-maximality contradiction.
```

The failure is the exact missing hypothesis in the phrase “the first new contact is
triangle-free.” A new contact to a second core neighbor of the anchor can create a
unit equilateral triangle with the preserved anchor edge.

## Exact local regression

Let the fixed core anchor be (b=(0,0)), and let two fixed core neighbors of (b)
lie on the unit circle at polar angles (-80^circ) and (+80^circ). Let the sole
chamber component be the single point (x) at polar angle (0^circ), so

[
 |b-x|=1,
 qquad |b-a_-|=|b-a_+|=1.
]

The two angular gaps from (x) to the fixed neighbors are (80^circ), so all three
displayed contacts are initially compatible with strict separation between (x) and
the two fixed neighbors:

[
 |x-a_\pm|=2\sin(40^\circ)>1.
]

The chamber sector at (b) may be chosen to contain the ray interval
([-80^circ,+80^circ]), as occurs at a convex face corner with interior angle
(160^circ). The only rigid motions of the one-point component that preserve the
sole anchor edge (bx) are rotations of (x) about (b). Rotating in either
direction reaches angular separation (60^circ) from one of the fixed neighbors
before leaving the sector. At that first event,

[
 |x-a_\pm|=|x-b|=|a_\pm-b|=1,
]

so the new contact creates an exact unit equilateral triangle. The motion is not an
admissible triangle-free contact-maximization path. There is no reason for another
cross-contact to occur first: the local source can be isolated from the rest by
strict gaps.

This is a geometric regression, not a claim that the four-point local picture is a
global minimizer. It is sufficient to refute the universal first-contact lemma used
by the attempted proof.

## Precise diagnosis

The earlier valid chamber normalization proves only that a weak component cannot be
completely floating: a rigid translation of a component with no core contact reaches
a new cross-contact before boundary escape, and the first new edge cannot close a
triangle across the old component cut.

Once a component already has a core attachment, that cut argument changes. The old
anchor edge is itself an existing cross-edge relative to the chamber-only component.
A new edge to a neighboring core vertex can therefore complete a triangle through
the anchor. Rotating about the anchor preserves the old edge but does not preserve
triangle-freeness at the first event.

The rejected route therefore does not prove a two-anchor lower bound, a stronger
component-size bound, or any macroscopic-chamber contradiction.

## Scope and regressions

- The local obstruction keeps all source points and uses exact unit distances.
- It does not delete contact-isolated points or invoke KKT positivity.
- It respects the convex-face angle bound: a convex angle below (pi) can still be
  wider than (120^circ), allowing a sole anchor ray with strict (>60^circ)
  gaps to both boundary-neighbor rays.
- The vanishing-shear and square-grid regressions remain independent obstructions to
  density-only chamber closure.
- Exterior caps remain outside the internal-chamber normalization.

## Disposition

**Rejected attempt.** Do not cite the one-anchor rotation as a theorem. The valid
remaining endpoint is the proof-only statement in
`research/target_c_internal_chamber_weak_component_anchoring.md`: every floating
component can be forced to acquire an anchor under contact maximization. The exact
next question is a two-step deformation or exchange that handles already-anchored
components without crossing the triangle-free boundary.
