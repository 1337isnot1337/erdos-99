<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "c3e1c069d6dc9f2b765f54864d4add57d9c4019a", "source_canonical": false, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "unreviewed", "source_path": "docs/reports/five_block_local_optimality_2026-08-30.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "f8ce4734aec871073e18feb670dcb3d6121522f2bf79ff0a4dcbbd49eea24f40"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle was `unreviewed`; it is retained as provenance only. Destination status remains unreviewed/noncanonical.

# Erdős Problem #99 — local five-block quartic optimality

**Date:** 2026-08-30  
**Run type:** closing-route theorem / exact finite geometry  
**Target:** A, free finite-gap route  
**Repository state:** based on `main` after the Section 160 toe-out promotion  
**External web search:** none  
**Computation:** numerical scratch was used to locate the phenomenon; the theorem below is exact and does not depend on computation.

## LEVEL I STATUS

`STILL OPEN`

Section 160 found a much better final translation of the Section 157 five rigid blocks:
in paper normalization its middle lift is

\[
v_{\rm toe}(d)=\frac{\sqrt3}{9}d^4-\frac29d^5+O(d^6),
\]

eight times the old leading coefficient. Section 160 deliberately made no optimality
claim among other five-block translations.

This report proves the missing exponent-level statement. If the exterior lattice is
fixed and the same five blocks may undergo arbitrary simultaneous, asymmetric rigid
translations converging to the identity, then every positive middle lift is `O(d^4)`.
Consequently the Section 160 toe-out branch has the optimal small-gap **exponent** in
that entire local rigid-translation model:

\[
\boxed{V_5^{\rm loc}(d)=\Theta(d^4).}
\]

The coefficient is not proved optimal. The theorem does not solve exterior
compatibility or the global Schur endpoint.

---

## 1. Exact endpoint attacked

The global Target A closure remains

\[
\dim\ker S\ge\Delta_\Lambda-d_{\rm int},
\]

or an actual `N`-point unit-separated competitor of diameter strictly below `D(N)`.

The finite-gap route instead asks for an embedded finite rearrangement. Sections 157
and 160 use the same five-block partition and have one-step gain of order `d^4`, hence
`d^{-3}` widening stages. A possible improvement was that a more general simultaneous
or asymmetric translation of those same five blocks could have gain `d^3` or `d^2`.
The theorem below rules that out locally.

The exact implication proved is

```text
all local rigid translations of the same five blocks have y3 = O(d^4)
    + Section 160 has y3 = Omega(d^4)
    -> local five-block translation exponent is exactly four
    -> the d^{-3} stage exponent cannot be improved by rescheduling/asymmetry alone.
```

---

## 2. Model

Use the exact Section 157 paper-normalized aligned-gap coordinates. The triangular
lattice has nearest-neighbor distance two. The upper half is initially shifted by
`(0,d)`, and the five finite rigid blocks are `B_1,...,B_5`. Every point outside those
blocks is fixed.

Translate block `B_i` by

\[
\tau_i=(x_i,y_i),
\qquad
E=\max_i\|\tau_i\|.
\]

There is no symmetry assumption and no prescribed path. A final endpoint is feasible
when all center distances are at least two. We consider `y_3>=0`, since `y_3` is the
new aligned-gap lift along the base of the middle block.

The exact block partition has four contact subfamilies used below: a horizontal chain
between two fixed upper points through all five blocks; two fixed-upper diagonal
contacts `(\pm1,\sqrt3)` for each nonmiddle block; two fixed-lower contacts for each
outer block; and the two inner-to-middle diagonal interfaces. These are already part
of the complete Section 157/160 nearest-neighbor enumeration.

---

## 3. Horizontal chain

Set `tau_0=tau_6=0`. Each horizontal chain edge has original vector `(2,0)`, hence

\[
|(2,0)+\tau_{i+1}-\tau_i|^2\ge4.
\]

Expanding,

\[
x_{i+1}-x_i
\ge-\frac14\|\tau_{i+1}-\tau_i\|^2.
\]

Summing from the left fixed endpoint and separately from the right fixed endpoint gives

\[
\boxed{|x_i|\le5E^2.}
\tag{3.1}
\]

Thus arbitrary local horizontal motion is automatically second order.

---

## 4. Fixed-point diagonal cages

For `i=1,2,4,5`, add the feasibility inequalities for the two fixed-upper contacts
`(\pm1,\sqrt3)`. The horizontal terms cancel:

\[
2\|\tau_i\|^2-4\sqrt3y_i\ge0,
\]

so

\[
\boxed{y_i\le E^2.}
\tag{4.1}
\]

For the outer blocks, the two lower contacts have relative vectors
`(\pm1,-\sqrt3-d)-\tau_i`. Adding their inequalities gives

\[
2\|\tau_i\|^2+4(\sqrt3+d)y_i+4\sqrt3d+2d^2\ge0.
\]

Hence

\[
\boxed{|y_1|,|y_5|\le d+E^2.}
\tag{4.2}
\]

---

## 5. Exact middle quadratic cage

For the left inner block, use a fixed-upper contact with vector `(-1,\sqrt3)`:

\[
\|\tau_2\|^2+2x_2-2\sqrt3y_2\ge0.
\tag{5.1}
\]

The left middle interface contains a `B_3`-to-`B_2` contact with the same base vector:

\[
\|\tau_2-\tau_3\|^2
-2(x_2-x_3)+2\sqrt3(y_2-y_3)\ge0.
\tag{5.2}
\]

Adding cancels all linear dependence on `tau_2`:

\[
\|\tau_2\|^2+\|\tau_2-\tau_3\|^2
+2x_3-2\sqrt3y_3\ge0.
\tag{5.3}
\]

The reflected right pair gives

\[
\|\tau_4\|^2+\|\tau_4-\tau_3\|^2
-2x_3-2\sqrt3y_3\ge0.
\tag{5.4}
\]

Adding these gives the central new identity-free inequality

\[
\boxed{
4\sqrt3y_3
\le
\|\tau_2\|^2+\|\tau_2-\tau_3\|^2
+\|\tau_4\|^2+\|\tau_4-\tau_3\|^2.
}
\tag{5.5}
\]

In particular `y_3<2E^2`.

This is the mechanism missing from the preceding free-gap analysis: the two sides form
a quadratic cage for the middle lift even when all five block translations are chosen
simultaneously and asymmetrically.

---

## 6. Bootstrap to the gap scale

Rearrange (5.2):

\[
y_2
\ge y_3+\frac{x_2-x_3}{\sqrt3}
-\frac{\|\tau_2-\tau_3\|^2}{2\sqrt3}.
\]

Using `y_3>=0`, (3.1), and `||tau_2-tau_3||<=2E` gives

\[
y_2\ge-7E^2.
\]

The reflected inequality gives the same result for `y_4`. With (4.1),

\[
|y_2|,|y_4|\le7E^2.
\]

Together with (3.1) and `y_3<2E^2`, this gives the coarse bounds

\[
\|\tau_2\|,\|\tau_4\|\le12E^2,
\qquad
\|\tau_3\|\le7E^2.
\tag{6.1}
\]

For the outer blocks, (3.1) and (4.2) give

\[
\|\tau_1\|,\|\tau_5\|\le d+6E^2.
\tag{6.2}
\]

Therefore

\[
E\le d+12E^2.
\tag{6.3}
\]

In the fixed local neighborhood `E<=1/24`, equation (6.3) yields

\[
\boxed{E\le2d.}
\tag{6.4}
\]

Consequently

\[
\|\tau_2\|,\|\tau_4\|\le48d^2,
\qquad
\|\tau_3\|\le28d^2,
\]

and

\[
\|\tau_2-\tau_3\|,
\|\tau_4-\tau_3\|
\le76d^2.
\]

Substitute into (5.5):

\[
4\sqrt3y_3
\le2(48^2+76^2)d^4=16160d^4.
\]

Thus

\[
\boxed{
0\le y_3\le\frac{4040}{\sqrt3}d^4.
}
\tag{6.5}
\]

This proves the universal local upper bound.

---

## 7. Matching lower order and exact classification

Define

\[
V_5^{\rm loc}(d)
=
\sup\{y_3:\text{feasible rigid five-block endpoint with }E\le1/24\}.
\]

The Section 160 toe-out branch is feasible, converges to the identity, and has

\[
y_3=\frac{\sqrt3}{9}d^4-\frac29d^5+O(d^6).
\]

Therefore it belongs to the defining class for all sufficiently small `d` and gives
`V_5^{loc}(d)=Omega(d^4)`. Equation (6.5) gives the reverse bound. Hence

\[
\boxed{V_5^{\rm loc}(d)=\Theta(d^4).}
\tag{7.1}
\]

Equivalently, every feasible family of same-five-block rigid translations satisfying
`E(d)->0` and `y_3(d)>=0` has `y_3(d)=O(d^4)`.

The Section 160 toe-out construction is therefore exponent-optimal in the complete
local identity branch of this rigid five-block translation model. The theorem does not
claim coefficient optimality.

---

## 8. Target A consequence

The result kills a concrete open repair of the Section 160 strain route. The support
stage exponent cannot be improved by keeping the same five blocks and merely choosing
better simultaneous, asymmetric translation vectors. A one-step gain of order `d^3`
or `d^2` is impossible in the identity branch.

An exponent-level improvement must instead use at least one of:

- a different finite contact/block architecture;
- rotations or internal deformation;
- a nonlocal branch not converging to the identity; or
- the exterior source/scaffold points constructively rather than treating them only as
  blockers.

The current Section 160 toe-out construction remains the strongest known free five-block
witness. Its principal unsolved issue remains exterior compatibility in an actual
Target A monomer domain.

---

## 9. Audit and regressions

| Item | Classification |
| --- | --- |
| Horizontal quadratic pinning | proved exactly from six original contact inequalities |
| Middle quadratic cage | proved exactly from four original diagonal contact inequalities |
| Universal local `O(d^4)` lift | proved for arbitrary asymmetric simultaneous translations with `E<=1/24` |
| `V_5^{loc}(d)=Theta(d^4)` | proved using the Section 160 toe-out lower branch |
| Toe-out coefficient optimality | not claimed |
| Nonlocal five-block translations | not excluded |
| Rotations/internal deformation | outside scope |
| Exterior-compatible embedded witness | open |
| Schur nullity endpoint | open |

The theorem uses no source Hall surplus, no activation/KKT implication, no planarity-to-
Schur shortcut, and no coordinate identification between independent global optima. It
is compatible with the Section 146 witness-complexity divergence and with all exterior-
blocker warnings: it is only a theorem about the free finite five-block architecture.

## 10. Exact next obligation

For the finite-gap route, do not spend further effort seeking a lower-order gain by
rescheduling or asymmetrically translating these same five rigid blocks near the
identity. The next exact obligation is either

\[
\boxed{\text{an exterior-compatible embedding of the Section 160 quartic witness}}
\]

or

\[
\boxed{\text{a genuinely different finite architecture/motion with gain }\omega(d^4).}
\]

Either route must ultimately produce the exact Schur inequality or a strict sub-`D(N)`
competitor.
