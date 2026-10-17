> Generated reading edition · [exact source](../../../docs/audits/target_c_mu_one_cell_concentration_independent_audit_2026-09-14.md) · source SHA-256 `a1992180cfce68263fae64dae833f39d22503fd00c52c8577d0f83b8b612aafb`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-C9C12ED6C764","canonical":true,"claim_ids":["C-FULLCORE-MU-ONE-CELL"],"claim_statuses":{"C-FULLCORE-MU-ONE-CELL":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit — Target C-II μ=1 one-cell concentration

**Date:** 2026-09-14
**Target:** Target C-II, full-core branch
**Audited artifact:** docs/reports/target_c_mu_one_cell_concentration_2026-09-14.md
**Verdict:** PASS for the stated equality-case theorem; its $\mu_D\to1$ antecedent
is excluded by the stronger canonical train-coupled floor; no C-II or Level I closure.

## Audited statement

Let D_j tend to infinity be a canonical full-core Type-II sequence. For each
unloaded positive-contact component let P_{r,j} be the actual convex hull of its
loaded attachment set, a_{r,j} its area, d_{r,j} its Euclidean diameter, and
delta_{r,j} its contact-graph diameter. Assume the canonical hypotheses

    sum a_{r,j} = (pi/4) D_j^2 - o(D_j^2)
    sum sqrt(a_{r,j}) <= C D_j
    d_{r,j} <= delta_{r,j} + 2
    sum delta_{r,j} <= 6 + mu_j D_j
    c_{I,j} = O(D_j^(2/3))

and mu_j tends to 1. Then one actual cell P_{*,j} has

    d_{*,j}/D_j -> 1,
    a_{*,j}/D_j^2 -> pi/4,
    sum_{r != *} d_{r,j} = o(D_j),
    sum_{r != *} a_{r,j} = o(D_j^2),
    per(P_{*,j})/D_j -> pi,
    sum_r per(P_{r,j}) = pi D_j + o(D_j).

After translation and scaling by D_j, the dominant cells converge in Hausdorff
distance along every subsequence to a disk of radius 1/2. The cells are
source-derived attachment hulls; all contact-isolated source points remain in the
global source and are not included in this auxiliary cell ledger.

## Proof audit

Fix eta > 0 and call a cell large when its area is at least eta D_j^2. The
square-root budget bounds the number of large cells by C/sqrt(eta), while the
small cells have total area at most C sqrt(eta) D_j^2. Hence the large cells carry
at least (pi/4 - C sqrt(eta) - o(1)) D_j^2 area.

Planar isodiametry then gives

    sum_large d_{r,j}^2 >= (1 - (4C/pi) sqrt(eta) - o(1)) D_j^2.

Let S_j = sum_r d_{r,j}. The component-diameter budget and the retained additive
two give

    S_j <= 6 + mu_j D_j + 2 c_{I,j} = D_j + o(D_j).

If d_{*,j} is the largest cell diameter, a large cell exists eventually and
sum_large d_{r,j}^2 <= d_{*,j} S_j. Therefore d_{*,j}/D_j is at least
1 - (4C/pi) sqrt(eta) - o(1). Since P_{*,j} is contained in the force hull,
d_{*,j} <= D_j. First taking j to infinity and then eta down to zero proves
d_{*,j}/D_j -> 1.

Put T_j = S_j - d_{*,j}. Because the dominant cell is large, the quantity
S_j^2 - sum_large d_{r,j}^2 contains 2 d_{*,j} T_j and all remaining terms are
nonnegative. The preceding estimates therefore imply

    d_{*,j} T_j <= (4C/pi sqrt(eta) + o(1)) D_j^2.

The same order of limits gives T_j = o(D_j). This includes every small cell in
T_j; no small-cell contribution is silently discarded.

Isodiametry now gives the non-dominant area as at most pi/4 times the sum of their
diameter squares, hence o(D_j^2). Full-core cell-area saturation gives the dominant
area limit. The convex perimeter-diameter inequality gives non-dominant perimeter
o(D_j). The exact attachment-perimeter estimate gives

    sum_r per(P_{r,j}) <= pi (6 + mu_j D_j + 2 c_{I,j}) = pi D_j + o(D_j).

Isoperimetry gives per(P_{*,j}) at least 2 sqrt(pi a_{*,j}) = pi D_j - o(D_j),
so the asserted perimeter limits follow.

Finally normalize P_{*,j} by D_j. The canonical full-core near-disk statement
places the normalized bodies in a common bounded set, so Blaschke selection applies.
Every Hausdorff limit is convex, has diameter one, and has area pi/4. Equality in
the ordinary planar isodiametric inequality forces that limit to be a disk of radius
1/2. No RSR equality theorem, Eppstein equality classification, phase alignment,
or finite deformation is being used.

## Scope and regression audit

The result is asymptotic and conditional on the canonical full-core hypotheses and
mu_j tending to 1. The stronger canonical theorem `C-FULLCORE-TRAIN-SURPLUS-FLOOR`
gives $\liminf\mu_D\ge1.637562\ldots$, so this antecedent is not realized by
any canonical Type-II sequence. The formal implication itself does not assert a finite threshold, lattice structure,
source-preserving motion, or an exact unit equilateral triangle. It does not apply
to the Type-I macroscopic chamber or exterior-cap branch.

The audit checked the additive +2 in the diameter conversion, the fixed-eta order
of limits, inclusion of all small cells in the non-dominant diameter sum, the
actual-cell versus scaffold distinction, and retention of contact-isolated source
points. The sheared-lattice and saturated-chamber regressions remain compatible
because the theorem supplies no exact triangle or finite global competitor.

## Promotion verdict

The proof is valid as a consequence of canonical C-FULLCORE-NEAR-DISK,
C-HARMONIC-CELL-TILING, C-ATTACH-CURRENCY, and C-COMP-DEATOMIZATION. Promote it as
C-FULLCORE-MU-ONE-CELL. The promotion does not change the Level I or C-II status:
the formal one-cell implication is vacuous under the stronger floor, while the
genuine high-surplus detour closure remains unresolved.
