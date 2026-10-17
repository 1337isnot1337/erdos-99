> Generated reading edition · [exact source](../../../docs/reports/target_c_no_generic_triangle_free_density_gap_2026-09-11.md) · source SHA-256 `cc7c9bec8be1412bdb198d459cbd29f68c8ff7bed03f536fc11e10f1e5c2f1bb`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-2A9EF2B65837","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — no generic quadratic density loss for inactive points

**Date:** 2026-09-11  
**Run type:** adversarial capacity regression  
**Target:** full-source annular-capacity closure  
**LEVEL I STATUS:** STILL OPEN

The full-source annular inequality leaves a normalized margin
`0.0197873937... D^2`. A possible shortcut would be to claim that contact-isolated
or triangle-free points suffer a fixed density loss from triangular packing. That
claim is false without global-minimality information. Strictly separated points can
have triangular-lattice density up to an `O(D)` boundary loss.

## Theorem

For every sufficiently large real `D` there is a triangle-free finite set `A_D` of
diameter exactly `D`, with minimum distance exactly one, and

$$
 |A_D|\ge \frac{\pi}{2\sqrt3}D^2-O(D),
$$

such that all but two points have distance strictly greater than one from every
other point. In particular, no inequality of the form

$$
 |A_D|\le (\Delta-c)D^2+O(D),\qquad c>0,
$$

can follow from triangle-freeness or contact-isolation alone.

## Proof

Let `s_D=1+D^{-1}` and let `\Lambda_D` be the triangular lattice with nearest-neighbor
distance `s_D`. Let

$$
R=D/2-3
$$

and retain all lattice points in the open disk `B(0,R)`, after deleting a bounded
neighborhood of the origin if needed. The standard fundamental-cell count gives

$$
 |\Lambda_D\cap B(0,R)|
 =\frac{2}{\sqrt3s_D^2}\pi R^2+O(R/s_D)
 =\frac{\pi}{2\sqrt3}D^2-O(D).
\tag{2.1}
$$

The retained lattice points have all mutual distances strictly greater than one.
Put a fixed unit pair at

$$
u=(-1/2,0),\qquad v=(1/2,0).
$$

They have distance one. Delete the bounded number of lattice points within distance
one of `u` or `v`; this changes (2.1) by only `O(1)`. Add the diameter pair

$$
z=(-D/2,0),qquad a=(D/2,0),
$$

Delete the `O(D)` lattice points within distance one of `z` or `a`; this does not
change (2.1) at its displayed scale. The resulting set consists of the dense lattice
cloud, the unit pair `u,v`, and the diameter pair `z,a`.

All distances involving `z` or `a` are at least one and at most `D`, after the
boundary deletion. The unit pair is separated from the lattice cloud and from the
diameter pair by more than one. Thus the only unit pair is `uv`; the configuration
contains no unit equilateral triangle, and its diameter is exactly `|z-a|=D`.

The count is (2.1) minus only `O(D)` deleted points plus four fixed points. This proves
the theorem. `square`

## Scope and correction

This is not a global-optimality certificate for any cardinality. It is an adversarial
regression against a proposed local capacity lemma. The points in the lattice cloud
are deliberately inactive, and the diameter pair is deliberately fixed separately.
The construction shows why the missing step must use the fact that `D` is the minimum
diameter for the **same cardinality**, not merely unit separation, triangle-freeness,
or the presence of a diameter pair.

The construction also explains the exact status of the full-source capacity bound:
the annular margin cannot be removed by a universal density estimate for inactive
points. A successful closure must use a source-preserving competitor, a second-order
minimum-diameter expansion, or the actual KKT/contact geometry.

## Audit notes

- The fixed pair `z,a` is at distance `D`; all points lie in the diameter-`D` disk,
  so no pair exceeds `D`.
- The lattice spacing is strictly larger than one, so its points have no unit
  contacts at all.
- The single unit pair supplies minimum distance exactly one and cannot form a unit
  equilateral triangle because all other distances from its endpoints exceed one.
- Only `O(D)` boundary points are removed to protect the diameter endpoints and the
  fixed unit pair.
- No assertion is made that `D` is globally minimal for the displayed cardinality.

## Classification

| Claim | Status | Reason |
|---|---|---|
| no fixed density loss from strict separation | proved | scaled triangular-lattice construction |
| full-source annular margin closes C-II | rejected | the proposed generic density step is false |
| Level I settlement | not proved | global-minimality information remains the missing input |
