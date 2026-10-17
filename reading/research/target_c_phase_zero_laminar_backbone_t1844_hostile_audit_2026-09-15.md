> Generated reading edition · [exact source](../../research/target_c_phase_zero_laminar_backbone_t1844_hostile_audit_2026-09-15.md) · source SHA-256 `80d07867d1246a2866082c64fcf2c5ca9aa5cfc1cdb8e4a3580bf8b2c25e3ca7`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "d3e490e183dc229020483c039764a7d6c46d7d91", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_phase_zero_laminar_backbone_t1844_hostile_audit_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "5cf2a91c04b1853dea5a56667ddb8054f990f56e8b4086a43f69e48b88c3bf17"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — phase-zero laminar O--O backbone at `t<=1.844`

**Date:** 2026-09-15  
**Reviewed:**
- `research/target_c_phase_zero_laminar_backbone_t1844_2026-09-15.md`
- `research/verify_target_c_phase_zero_laminar_backbone_t1844.py`
- upstream hostile-audited `0.7404D` weighted center-fan theorem
- hostile-audited Section-157 normal-arc / outer-train bracing-energy geometry
- exact laminar multi-train interval shear and the previous live-backbone rank theorem

**Disposition:** **PASS after the marker-tie repair in commit `c620bf0f`.**  
**Scope:** proof-only full-core Type-II branch with `t=(q-k)/D<=1.844`.  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The candidate replaces the old center-extracted `>0.017104D` dual-path backbone by a
`>0.0295D` nested non-singleton O--O family obtained directly from retained boundary
pair mass and Section-157 phase-zero localization.  The core idea is valid, but the
first draft had one real finite-order ambiguity: two distinct terminal occurrences on
the same loaded-hull side can collapse to one normal-angle atom.  Merely requiring the
collapsed shorter arcs to contain the phase marker is therefore not enough to conclude
that the original occurrence intervals share an interior point.  Commit `c620bf0f`
repairs this by deleting every train with an endpoint normal inside a shrinking marker
neighborhood.  The endpoint-capacity theorem makes that deletion `o(D)` in retained
pair weight.  After that repair the nesting argument is exact.

The checks below are intentionally independent of the candidate's prose.

---

## 1. The weighted fan really forces non-singleton O--O mass

The audited inputs are

```math
P_V>{53\over625}-o(1)=0.0848-o(1)
```
for retained smallest-leaf O--O pair weight,

```math
{\sum_\tau w_\tau d_\tau D\over\sum_\tau w_\tau}
>{1851\over2500}D-o(D)=0.7404D-o(D),
```
and a total center-phase train count below

```math
{1063\over1000}D+o(D)=1.063D+o(D).
```

A singleton stopped train is one contact edge incident to no strict rhombus.  Hence it
has zero crossings in the strict-rhombus train graph and contributes `d_tau=0` to the
fan numerator.  If `W_ns` is the retained pair weight on non-singleton O--O trains,
then

```math
(1.063D+o(D))W_{ns}
\ge \sum_\tau w_\tau d_\tau D.
```
Therefore

```math
W_{ns}
>{(0.7404)(0.0848)\over1.063}D-o(D)
={196206\over3321875}D-o(D).
```

The companion `Fraction` certificate verifies the exact rational value.  No invalid
operation of deleting singleton vertices from an all-train Mantel graph occurs here;
only their literal zero contribution to this already-defined crossing incidence is
used.

**Verdict:** PASS.

---

## 2. The Section-157 zero localization has exactly two full-circle classes

For one non-singleton O--O train, the hostile-audited bracing-energy theorem chooses
the smaller Jordan shore and retracts its two outer terminal occurrences to loaded-hull
boundary positions.  In the Type-II near-disk limit, Section 157's two transverse
diameter signs imply that the shore's normal-angle interval contains a zero of

```math
n\mapsto n\cdot Ju_\tau
```
up to a uniform `o(1)` angular error.

For a projective train phase there are exactly two such normal zeros on the oriented
full circle, separated by `pi`.  The smallest-leaf phase window shrinks to one
projective atom.  Passing to the usual diagonal subsequence therefore gives one common
error scale `eta_D->0` such that every retained non-singleton train's smaller normal arc
comes within `eta_D` of one of two fixed antipodal marker lifts.

The candidate correctly keeps **two** marker classes.  Collapsing them into one would
be invalid on the oriented boundary circle.

**Verdict:** PASS.

---

## 3. The near-marker deletion costs only `o(D)` pair weight

This is the main measure-theoretic check.

For a train with retained terminal weights `a_tau,b_tau`, the pair weight is

```math
w_\tau=\min(a_\tau,b_\tau),
```
so charging the entire pair to either terminal occurrence is always safe:

```math
w_\tau\le a_\tau,
\qquad
w_\tau\le b_\tau.
```

The hostile audit of dominant-orbit routewise retention proves that the retained
projective occurrence measure is dominated by round loaded-hull perimeter measure:

```math
\nu\le d\theta.
```
Equivalently, on the oriented full normal circle the corresponding endpoint measure is
dominated by `(1/2)dtheta`.  Thus an oriented normal neighborhood whose width tends to
zero carries `o(D)` retained occurrence weight.  The two antipodal marker
neighborhoods together also carry `o(D)` weight.

The repaired candidate deletes every train whose assigned marker is absent from its
smaller arc **or whose arc endpoint lies within `2 eta_D` of that marker**.  In either
case there is a terminal occurrence in the `2 eta_D` marker neighborhood.  Since one
terminal occurrence belongs to one stopped train, the charge is injective at the
occurrence level; even without injectivity, summing `w_tau` against the chosen endpoint
weights would remain safe.

Hence the deleted retained pair mass is `o(D)`.

Finite side-normal atoms do not create a macroscopic exception.  The audited Type-II
interface collapse has maximal normalized loaded-hull side length `o(1)`, and routewise
retention on one side is bounded by that side length.  Thus a whole tied side has only
`o(D)` retained weight.

**Verdict:** PASS after the marker-tie repair.

---

## 4. Common interior marker plus noncrossing implies one chain

All surviving trains lie in one shrinking exact leaf-phase window.  For sufficiently
large sources their projective direction separation is below `pi/3`, whereas a strict
rhombus crossing requires separation **strictly greater** than `pi/3`.  Therefore the
selected train midpoint crosscuts are pairwise disjoint.

The audited convex-pocket retraction preserves their cyclic endpoint order.  For a
noncrossing chord family, chosen shorter boundary arcs are laminar: partial overlap
without containment would put the four endpoints in alternating order and force a
crossing.

After the repaired deletion, every arc in one marker class contains the fixed marker
strictly in its interior, away from both retracted endpoints.  Two such arcs cannot be
disjoint.  Hence laminarity reduces to total inclusion.

The final transfer back from retracted hull order to the actual outer-face crosscuts is
also safe.  Retraction preserves occurrence order, and the marker is not a collapsed
endpoint after the repair.  Nested boundary endpoint intervals for pairwise disjoint
proper crosscuts give nested Jordan shores.  The selected train edges therefore form
one simple path in the complement dual tree.

There are at most two marker chains.  One carries at least half of the surviving
non-singleton pair weight:

```math
{1\over2}{196206\over3321875}D-o(D)
={98103\over3321875}D-o(D)
=0.02953241768\ldots D-o(D).
```
Since each `w_tau<=1`, that chain contains more than `0.0295D-o(D)` distinct trains.

**Verdict:** PASS.

---

## 5. The full-rank shear argument does not need a common crossing center train

Let `M` be the actual-diameter first-variation matrix in the selected laminar train
coordinates.  Suppose `M theta=0`.  The exact O--O shear construction preserves all
positive contacts to first order, so this vector is an infinitesimal flex of the mixed
positive-contact/actual-diameter framework.  Canonical mixed infinitesimal rigidity
therefore makes the flex Euclidean.

The old live-backbone proof killed the Euclidean rotation using the particular center
train that crossed its whole extracted path.  That crossing hypothesis is stronger
than necessary.  Under a selected leaf-train shear, every contact belonging to any
**unselected** train is exactly unchanged: by the audited cutset theorem, only contacts
of the selected train cross its shore cut.  Thus every unselected train has angular
rate zero.

The upstream phase theorem gives positive center-phase train mass, and center-phase
trains are not members of the selected smallest-leaf family.  Hence at least one
unselected non-singleton train has rate zero.  A nonzero Euclidean rotation would give
one common nonzero angular rate to every train.  Therefore the rotation rate vanishes,
and translations give zero selected train rates.  Thus `theta=0`.

So

```math
\operatorname{rank}M=m.
```

Contact isolates do not create a new freedom in this inference; this is the same
canonical mixed-rigidity statement used by the audited live-backbone theorem, and the
new proof only weakens how its Euclidean rotation mode is killed.

**Verdict:** PASS.

---

## 6. Proper-interval and switching-position counts are inherited correctly

On a laminar O--O path every actual diameter row has contiguous signed support.  A
full-span row has coordinates

```math
s_h(r_h\cdot Ju_1,\ldots,r_h\cdot Ju_m).
```
As `r_h` ranges over the plane, all such rows lie in the span of two fixed coordinate
sequences.  Hence full-span rows contribute rank at most two.  Every proper interval
row contributes at most one further row dimension.  Full rank therefore gives

```math
N_{prop}\ge m-2>0.0295D-o(D).
```

If support changes at only `s` internal boundaries, the columns split into `s+1`
constant-incidence blocks.  On each block every row lies in a two-dimensional
coordinate span, so

```math
m\le2(s+1).
```
Thus

```math
s\ge\lceil m/2\rceil-1>0.01475D-o(D).
```

For an interval row, starting or ending at one internal boundary means one physical
diameter endpoint projects to the corresponding layer vertex.  One physical endpoint
has one projection layer.  Distinct switching layers therefore force distinct loaded
actual-diameter endpoints.  This is exactly the endpoint-localization argument of the
previous audited live-backbone theorem, with only the path length changed.

**Verdict:** PASS.

---

## 7. The `<281` adjacent support/multiplier corollary is normalized correctly

For internal boundary `i`, put

```math
N_i=\#\{h:\varepsilon_{h,i+1}\ne\varepsilon_{hi}\},
\qquad
B_i=\sum_h\beta_h|\varepsilon_{h,i+1}-\varepsilon_{hi}|.
```

One interval row starts and stops at most once, so

```math
\sum_iN_i\le2|H|\le2\pi D.
```
With the normalized positive KKT vector `sum_h beta_h=1`, the same interval variation
gives

```math
\sum_iB_i\le2.
```

For `m>(59/2000)D-o(D)`, averaging `N_i+D B_i` and using `pi<355/113` gives

```math
{2\pi+2\over59/2000}<281.
```
The companion exact verifier checks the outward rational inequality.  Hence one pair
has simultaneously

```math
N_i<281+o(1),
\qquad
B_i<281D^{-1}+o(D^{-1}).
```

Averaging only `B_i` yields the separate `<68/D` beta-switch pair.  The candidate does
**not** conflate these two pairs.

Most importantly, the candidate explicitly declines to infer an `O(D^{-1})` train
phase mismatch from mere membership in a shrinking atom.  It claims only `o(1)`.  Thus
it does not silently replace the current Pareto `<1800` finite-cusp pair, whose
inverse-`D` phase gap is a separate quantitative input.

**Verdict:** PASS.

---

## 8. Scope and remaining obstruction

The result is a real source-level strengthening:

```text
old center-extracted laminar backbone: >0.017104D
new phase-zero laminar backbone:       >0.0295D
new proper diameter intervals:         >0.0295D
new switching layers/endpoints:        >0.01475D
one adjacent switching set:            <281 rows with beta mass <281/D
```

But it does not supply a uniformly finite feasible deformation at scale `1/D`, does not
bound inactive noncontact slack, and does not prove the selected `<281` pair has
inverse-`D` phase mismatch.  Therefore it does not by itself close the hostile-audited
finite-cusp obstruction or C-II.

**Final disposition:** **PASS after marker-tie repair.  Keep proof-only status.  C-II
and Level I remain open.**
