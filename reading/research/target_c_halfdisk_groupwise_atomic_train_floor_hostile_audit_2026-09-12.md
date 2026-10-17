> Generated reading edition · [exact source](../../research/target_c_halfdisk_groupwise_atomic_train_floor_hostile_audit_2026-09-12.md) · source SHA-256 `35513e757ed2cfe147376dabe2a126e74b735d57d5107ae3e2daf068f9be81bd`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "484f1fa38a9eb6700249f21ad5fd008193a36318", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_halfdisk_groupwise_atomic_train_floor_hostile_audit_2026-09-12.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "d1a4988813e07c9c1a0c550809b5d8f7b8ee7bb2e8d3a515eb14171f469acb7c"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — groupwise atomic train floor in the two-half-disk branch

**Date:** 2026-09-12  
**Reviewed:** `research/target_c_halfdisk_groupwise_atomic_train_floor_2026-09-12.md`  
**Disposition:** **PASS at proof-only branch-specific scope.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

## 1. Group rhombus density

The preceding all-regime half-disk theorem gives strict-rhombus area

$$
A_{4,i}=\left({\pi\over8}-o(1)\right)D^2
$$

for each dominant group.  Type II has

$$
R_4/D^2\to\Delta_2={\pi\over2\sqrt3},
\qquad
A_4/D^2\to\pi/4.
$$

Every strict triangle-free unit rhombus has area at least `a_0=sqrt(3)/2`, so
`A_4-a_0R_4>=0`; the displayed Type-II limits make this global excess `o(D^2)`.
Group excess is a sub-sum of the same nonnegative terms, hence also `o(D^2)`.  Therefore

$$
R_i/D^2\to{(\pi/8)\over a_0}={\Delta_2\over2}.
$$

No false universal upper bound such as `area(rhombus)<=sqrt(3)/2` is used.

**Verdict:** PASS.

## 2. How a train can change harmonic-cell label

Audited §129 says the number of physical strict rhombi not realized as a local
quadrilateral of a harmonic cell is `o(D)`.  Delete both complete stopped trains
through every such nonlocal rhombus.  This removes `o(D)` trains.

Consider two consecutive surviving local rhombi on one undeleted train.  They share the
contact edge that is the intermediate train side.

- If the shared contact edge has an unloaded endpoint, both local cell graphs contain
  that unloaded vertex.  Connected unloaded components are disjoint, so both rhombi
  have the same component/cell label.
- If both endpoints are loaded, the edge is a loaded-loaded unit contact.  The audited
  Type-II theorem `c_B=0` makes it a global force-hull side.  A contact edge on the
  boundary of the convex force hull has the core on only its inward side.  Two bounded
  rhombus faces incident to the same embedded edge would have to occupy its two local
  sides; the outward one cannot lie in the force hull.  Hence two consecutive local
  rhombi cannot switch cell label across a loaded-loaded edge.

Thus every undeleted train participating in a rhombus has one harmonic-cell label.

**Verdict:** PASS.  This is the load-bearing localization step.

## 3. Crossing mass lost under train deletion

The global stopped-train crossing graph is simple and has `T=O(D)` vertices.  Deleting
`o(D)` train vertices removes at most

$$
o(D)\,T=o(D^2)
$$

crossing edges.  Therefore the retained group crossing counts still satisfy

$$
R'_i/D^2\to\Delta_2/2.
$$

This estimate does not require an individual train-length bound.

**Verdict:** PASS.

## 4. Groupwise reuse of §142.3

For one dominant group, the retained train-crossing graph is an induced/subgraph of the
global one, hence simple and triangle-free.  Its train count is `O(D)` and its crossing
count is `(Delta_2/2-o(1))D^2`, so after a subsequence `T_i/D->x_i>0`.

The global rhombus area excess is `o(D^2)`.  Therefore for every fixed `epsilon>0`, the
number of group crossings whose phase separation is at least `pi/3+epsilon` is
`o(D^2)`.  The §142 product-measure support argument is consequently valid for the
group measure: limiting crossing mass lies on the exact `+-pi/3` relation, which the
product phase measure charges only through atoms.  Weighted Mantel gives

$$
{\Delta_2/2\over x_i^2}\le{s_i^2\over4},
$$

so

$$
x_i s_i\ge2\sqrt{\Delta_2/2}.
$$

No groupwise exposed-hull inequality is assumed.

**Verdict:** PASS.

## 5. Additivity of absolute atomic mass

At finite `D`, the two retained group train sets are disjoint subsets of the full train
set.  Write their absolute empirical measures as

$$
\lambda_{i,D}=D^{-1}\sum_{\tau\in\mathcal T_{i,D}}\delta_{[u_\tau]}.
$$

After a common subsequence,

$$
\lambda=\lambda_1+\lambda_2+\lambda_0
$$

with `lambda_0` positive.  For finite positive measures, the mass of the atomic part is
exactly additive, even if `lambda_1` and `lambda_2` have atoms at the same direction:

$$
\sum_x(\lambda_1+\lambda_2)(\{x\})
=
\sum_x\lambda_1(\{x\})+
\sum_x\lambda_2(\{x\}).
$$

Hence global absolute atomic train mass is at least

$$
4\sqrt{\Delta_2/2}=2\sqrt{2\Delta_2}.
$$

This does not use the false weak-limit semicontinuity of atomic mass rejected elsewhere
in the repository.  Atomic mass is computed directly on the fixed common limit measures
and then added exactly.

**Verdict:** PASS.

## 6. Global exposed-hull conversion

Audited §142.4 applies to the original global train measure and gives

$$
q/T\le2(1-s).
$$

With `T/D->x`, this is

$$
xs\le (T-q/2)/D.
$$

Combining with the groupwise lower bound gives

$$
\liminf(T-q/2)/D\ge2\sqrt{2\Delta_2}.
$$

This is directionally correct.  The proof never substitutes a local half-disk boundary
for the global near-circular exposed hull.

**Verdict:** PASS.

## 7. Derived constants

Using `q<=pi D`,

$$
\liminf{T-q\over D}
\ge2\sqrt{2\Delta_2}-{\pi\over2}
=1.122751047382300\ldots .
$$

Since `T-q=2f-k`, this is the claimed defect-face floor.

For the §146 elimination, a general input

$$
C\le\liminf(T-q/2)/D
$$

gives

$$
\liminf {f\over D}
\ge C/2-y/4+d/4+z/2
$$

and the outer ledger gives `Q/D+2z<=2y-pi`.  With `Q>=f`,

$$
{9y\over4}\ge\pi+C/2+d/4+5z/2.
$$

Setting `C=2sqrt(2Delta_2)` yields

$$
\liminf {1\over D}
\left(h-{d_H\over9}-{10s_Z\over9}\right)
\ge
{4\pi\over9}+{4\over9}\sqrt{\pi/\sqrt3}
=1.994829484745952\ldots .
$$

The constants and coefficients are correct.

## 8. Scope and nonclaims

- This theorem is conditional on the proof-only two-half-disk alternative; it says
  nothing about the center-wrapping branch.
- The auxiliary deletion is of trains, not source points.
- Contact-isolated source points remain in the source.
- No full-source affine-kernel statement is used.
- The result does not contradict `h<=q<=pi D`; it substantially narrows the branch but
  does not close it.

## Final verdict

**PASS at proof-only branch-specific scope.**  The two quadratic half-disk rhombus
systems force independent atomic phase mass, and the global exposed-hull theorem turns
that into the stronger train/defect/diameter-edge floors claimed in the source.
