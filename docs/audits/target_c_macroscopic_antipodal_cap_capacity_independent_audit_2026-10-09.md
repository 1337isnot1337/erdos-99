<!-- theorem-state: {"artifact_id":"ART-7BB2B44A9BCB","canonical":true,"claim_ids":["C-MACROSCOPIC-ANTIPODAL-CAP-PAIR-STRICT-CAPACITY"],"claim_statuses":{"C-MACROSCOPIC-ANTIPODAL-CAP-PAIR-STRICT-CAPACITY":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C Audit.183 — strict capacity for a macroscopic antipodal cap pair

**Date:** 2026-10-09

**Audit base:** `587bd922311b9c0403839741119d44515aa593b2`, state `2026-10-08.audit.176`

**Frozen source branch:** `research/sol/target-c-exterior-cap-closure-20261006` at `f4a362727779f6afc0f01738015112c04fdb73d5`

**Source report:** `docs/reports/target_c_exterior_loaded_tips_and_paired_packet_gluing_2026-10-06.md`, SHA-256 `01e106faa927a78b540a785b1a4d7b5d726a210182c47b1e6d0101710088124f`

**Independent input:** canonical Audit.115, `C-ANTIPODAL-EXTERIOR-CAP-PAIRING`; canonical Audit.85, `C-EXTERIOR-PAIRED-CELL-STRICT-CAPACITY`.
**Audit boundary:** the source report's Section 5 four-tip claim, reconstructed from those canonical results. The other packet-release and exterior-cap closure claims in the source report are not included.

## Exact theorem promoted

Let `A_j` be any unbounded canonical contact-minimal, then diameter-pair-minimal, triangle-free C-II global-minimizer sequence, with the full source retained and diameter `D_j -> infinity`. For any selected actual Section-77 exterior caps `C_j` with

```text
liminf area(C_j)/D_j^2 > 0,
```

choose distinct opposite caps `C'_j` supplied by `C-ANTIPODAL-EXTERIOR-CAP-PAIRING`. Let `Q_j,Q'_j` be their actual convex hull-augmented cells, with isolate populations `S_j,S'_j` and the four loaded hull-arc tips `R_j`. For all sufficiently large `j`, the four tips are distinct extreme points of the full source hull and have pairwise distances at least four. Indeed, for every fixed positive lower bound on `area(C_j)/D_j^2`, there is `gamma>0` such that

```text
min{|x-y| : x,y in R_j, x != y} >= gamma D_j
```

eventually. Consequently the exact hypotheses of `C-EXTERIOR-PAIRED-CELL-STRICT-CAPACITY` hold. If `E_j,E'_j` are its strict guarded regions after omitting guards at the four tips, and `M_j=Pack_1(E_j)`, `M'_j=Pack_1(E'_j)`, then

```text
M_j + M'_j <= |S_j| + |S'_j| + 3.
```

Since each old isolate population is feasible in its strict region, the combined strict-capacity surplus is at most three. This does not produce a packet, a replacement site, a finite source motion, a triangle, or a strict sub-`D` competitor.

## Independent reconstruction of the new bridge

Fix a subsequence on which the normalized cap endpoints converge. By Audit.115 and the canonical source-hull disk sandwich, the selected cap and its opposite partner converge to circular segments of the radius-`1/2` limiting disk, with endpoint pairs `u,v` and `-u,-v`. Write the cap half-angle as `theta`, so `u,v` have angular coordinates `+theta,-theta`.

For a radius-`1/2` disk, the limiting cap area is

```text
A(theta) = (2 theta - sin(2 theta))/8.
```

Choose a fixed `0 < alpha < liminf area(C_j)/D_j^2`. The fixed positive area ratio forces `theta >= theta_alpha > 0`, where `theta_alpha` is the unique value satisfying `A(theta_alpha)=alpha`. The opposite endpoints have the same limiting half-angle by the antipodal pairing theorem.

The cap chord is a supporting side of the full actual force hull `F_j`, and its endpoints are loaded vertices. Audit.115's full-source geometry puts those endpoints on the normalized circumcircle of radius `1/2`. The common-center inradius floor from `C-DB-DENSITY` is

```text
r_o(F_j)/D_j >= sin(rho)/2 - o(1),   rho = cos(rho) > 0.
```

The distance from the normalized center to the limiting chord is `(1/2)cos(theta)`. Since the centered inball lies inside the full force hull, every supporting line is at least that inradius from the center. Therefore `cos(theta) >= sin(rho)` in every subsequential limit, or `theta <= pi/2-rho`.

The four limiting tips lie on the radius-`1/2` circle at angles `theta,-theta,pi+theta,pi-theta`. Their pairwise chord distances are among `sin(theta)`, `cos(theta)`, and `1`. Thus their minimum is bounded below by

```text
delta_alpha = min(sin(theta_alpha), sin(rho), 1) > 0.
```

Compactness gives an eventual physical separation at least `(delta_alpha/2)D_j`. In particular it is at least four for all sufficiently large `j`. The cell endpoints are exactly these cap endpoints: Audit.84's hull-augmented-face theorem assigns each nondegenerate loaded-hull interval one actual cell with that source-hull arc and a unit-contact path; all contact-isolated source points remain assigned to the cell populations.

This verifies the four-tip hypothesis independently. Applying Audit.85's already-audited strict-capacity theorem gives the displayed `+3` bound without any packet extraction or symmetry assumption at finite `D`.

## Hostile checks and verifier boundary

- The inradius bound is for the full actual loaded force hull `F_j`, with the source circumcenter, not a selected diameter subgraph or lattice scaffold.
- A positive area ratio prevents same-cap tips from coalescing; the inradius floor prevents the cap chord from approaching a diameter, which would collapse cross-pair separation. Both bounds are needed.
- The paired-cap six-spoke regression in Audit.94 is nonglobal and fails the canonical loaded-diameter-density hypotheses; it does not have the promoted inradius floor and is outside this theorem.
- The four-tip source endpoints are actual loaded extreme hull points. Contact-isolated source points are retained in `S_j,S'_j` and in every later full-source argument.
- I inspected and reran `research/verify_target_c_exterior_loaded_tip_pairing_2026_10_06.py`. It passed 3,942 exact rational pair checks for its finite sharpness/regression examples. Its docstring explicitly says it proves neither canonical cap extraction nor the missing packet population. It does not verify this asymptotic separation; that conclusion is analytic from Audits.115 and DB.30.
- No numerical or finite verifier is used as evidence for the asymptotic claim.

**Verdict: PASS — promote `C-MACROSCOPIC-ANTIPODAL-CAP-PAIR-STRICT-CAPACITY`.** The result removes the four-tip separation condition from Audit.85 for one chosen antipodal partner of any fixed-positive-area exterior cap. It rules out a combined strict-capacity surplus of four or more for that pair. It creates no capacity or source move. C-II and Level I remain open.

## Dependencies and frontier effect

Dependencies: `C-ANTIPODAL-EXTERIOR-CAP-PAIRING`, `C-DB-DENSITY`, `C-EXTERIOR-HULL-AUGMENTED-CELLS`, and `C-EXTERIOR-PAIRED-CELL-STRICT-CAPACITY`.

For the macroscopic-container branch, a paired-cell argument cannot obtain a contradiction merely by asking the two fixed strict guarded regions to supply four or more net spare sites: their total surplus is at most three. Any further cap-pair closure must use a different source-preserving mechanism, such as a justified moved-wall or core-release argument, and still check every full-source lower and actual-diameter upper constraint. The active full-core face-coupled obligation is unchanged. No discovery branch or tip was modified.
