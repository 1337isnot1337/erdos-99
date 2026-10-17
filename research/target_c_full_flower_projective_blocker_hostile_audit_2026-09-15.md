<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "e35fc3ffe7519b618df96100c8edd519331dd530", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_full_flower_projective_blocker_hostile_audit_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "dc32b364885e6275ae87462789e281a74c88cf40438531b589a8e7dd2c6883de"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — full-flower projective two-blocker theorem

**Date:** 2026-09-15\
**Audited source:** `research/target_c_full_flower_projective_blocker_2026-09-15.md`\
**Verdict:** **PASS at proof-only exact finite scope.**\
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

This audit attacks the four points on which the two-blocker theorem could fail:

1. a projective arc might not lift to the claimed two-cone geometry across the cut at
   angle `0=pi`;
2. the `2+2` lift distribution might permit polygon closure despite the two large
   complementary gaps;
3. one full pentagon might use the same complete train on two boundary sides;
4. summing blockers over many flowers might count one train more than twice.

All four checks pass.

---

## 1. Projective wraparound is harmless

The projective direction space is a circle of circumference `pi`.  Any closed arc `A`
of length at most `pi/3` can be rotated so that it does not cross the coordinate cut.
Its oriented lifts are then exactly two antipodal closed arcs `A_+` and `A_-`, each of
the same width.  Rotating the physical plane does not change polygon closure,
consecutive turn angles, train crossing, or any incidence count.

Thus the proof's use of a horizontal midpoint axis loses no projective cases.

---

## 2. The pentagon turn inequality is strict

A bounded pentagonal contact face in the canonical full-force-visible core is a simple
strictly convex unit pentagon.  If successive counterclockwise unit sides have positive
turn `g`, the skipped-vertex diagonal has length

\[
2\cos(g/2).
\]

That diagonal lies in the convex face interior.  If its length were exactly one it
would be an actual contact chord and the purported pentagon would not be a face.
Unit separation excludes length below one.  Hence the diagonal is strictly longer
than one and

\[
0<g<2\pi/3.
\]

The theorem therefore needs no asymptotic diagonal-slack lower bound; only strictness
is used.

---

## 3. The `4+0` and `3+1` projection cases are genuinely impossible

If the projective arc has width `w<=pi/3`, every selected side has axial projection
magnitude at least

\[
c=\cos(w/2)\ge\sqrt3/2.
\]

For four selected sides in one lift cone, the four-side axial sum is at least `4c`;
one arbitrary fifth unit vector cannot cancel it because `4c-1>0`.

For a `3+1` split, the adverse selected minority side may have projection `-1`, not
merely `-c`, and the arbitrary fifth side may also contribute `-1`.  Even with those
worst values the sum is at least

\[
3c-2\ge3\sqrt3/2-2>0.
\]

So the proof uses the correct adverse projection bounds.

If all five projective directions lie in the arc, the majority lift cone has at least
three sides and the minority at most two; the same bound `3c-2>0` contradicts closure.

---

## 4. The `2+2` case really leaves one forbidden consecutive gap

Assume exactly four projective directions lie in `A` and their oriented lifts split
`2+2` between `A_+` and `A_-`.  Since the lifted arcs are antipodal and each has width
`w`, the two open direction-circle regions separating them each have length at least

\[
\pi-w\ge2\pi/3.
\]

The fifth side's projective direction is outside `A`, hence its oriented direction is
outside `A_+ union A_-`.  It occupies at most one of those two separating regions.
The other separating region contains no side direction at all.  Therefore the last
side direction in one lifted cone and the first in the other are consecutive in the
cyclicly ordered side-direction list, with gap at least `2pi/3`.

For a strictly convex polygon, cyclic side order is the same as cyclic direction
order.  This contradicts the strict turn inequality from Section 2.  No assumption
about which physical side realizes which direction is missing.

This is the only place strict convexity, rather than mere vector closure, is needed.

---

## 5. The constant three is sharp for the local direction statement

The existing exact pentagon lattice-phase regression has projective side directions
converging with multiplicities

\[
1,3,1
\]

on the three triangular-lattice projective axes.  For sufficiently small regression
parameter, one projective arc of width below `pi/3` contains the middle three side
directions.  A train direction near the projective antipode of that middle cluster has
projective separation greater than `pi/3` from all three while remaining within
`pi/3` of the other two.

Thus the theorem cannot replace "at most three crossing-compatible flower trains" by
"at most two" using only strict convex equilateral-pentagon geometry.

---

## 6. One full flower has five distinct non-singleton trains

Every side of a fully rhombic pentagon has a strict rhombus on its opposite side, so
its stopped train is non-singleton.  If one complete train supplied two side
occurrences of the same bounded pentagon, both terminal occurrences of that train
would lie on the same bounded face.  The exact bounded-face train-loop exclusion
forbids this.  Hence `I(F)` has five distinct train vertices.

The bounded-face endpoint fan says any two trains incident with one bounded face are
noncrossing.  Therefore there are no hidden internal edges when the proof identifies

\[
\sum_{tau\in I(F)}d_R(tau)
\]

with crossings from `I(F)` to the `T_R-5` external trains.

---

## 7. Crossing compatibility is used only as a necessary condition

For fixed projective direction `phi`, the set

\[
C_phi=\{psi:d_proj(phi,psi)>pi/3\}
\]

is an open arc of length `pi/3` on the projective circle.  A strict-rhombus train
crossing requires membership in this arc, but membership does not guarantee a
physical crossing.  The theorem uses only the forward implication

\[
\text{actual crossing}\Longrightarrow psi\in C_phi.
\]

Hence replacing physical crossings by direction-compatible pairs can only increase the
count, which is the safe direction for the upper bound of three.

---

## 8. Global blocker deduplication uses only two terminal occurrences

Fix a train `sigma`.  It terminates on at most two full flowers.  Every other full
flower supplies at least two blocker incidences `(F,tau)` with `tau` nonadjacent to
`sigma`.

A complete stopped train `tau` has exactly two terminal occurrences.  Therefore it can
appear as a flower-terminal blocker for at most two distinct full flowers, regardless
of whether bounded-face endpoint simplicity is invoked.  Dividing the at least
`2(M-2)` blocker incidences by this exact capacity two gives at least `M-2` distinct
blocker trains.

There is no self-count: only flowers not incident with `sigma` are used, so every
selected blocker `tau` is distinct from `sigma`.

Summing nondegrees over all train vertices counts every unordered noncrossing train pair
exactly twice, giving

\[
{T_R\choose2}-R_4\ge {T_R(M-2)\over2}.
\]

The finite `-2` is necessary and was retained.

---

## 9. Scope and non-implications

The theorem does **not** claim:

- that direction compatibility implies an actual train crossing;
- that the new scalar missing-pair bound beats the already-known full-flower Mantel
  deficit numerically;
- that all flower trains lie in the dominant atomic orbit;
- that one flower has a uniform angular-defect payment; or
- that the localized degree loss alone yields a diameter-decreasing motion.

Its new content is exact localization: every full flower is a five-train independent
fan that every external train can meet in at most three places.  This survives the
known near-three-axis pentagon regression and applies without phase purity.

**Final audit verdict:** PASS at proof-only exact finite scope.  The next useful
composition is dominant-vs-complement allocation of the `5M` full-flower terminal
occurrences, using the blocker degree inequality on the dominant side and bounded
endpoint mass on the complement side.
