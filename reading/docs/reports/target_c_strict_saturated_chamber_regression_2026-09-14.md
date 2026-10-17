> Generated reading edition · [exact source](../../../docs/reports/target_c_strict_saturated_chamber_regression_2026-09-14.md) · source SHA-256 `b70fce08f3c7c91718623e43391191ac4ac216cea53d4716adef3099ec2e25a7`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-87C91B7B4190","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — strict one-point-saturated chamber regression

**Date:** 2026-09-14
**Repository commit:** ef941ab2b44aa393bdc461926769247b45754202
**State version:** 2026-09-12.audit.46
**Run type:** hostile regression / exact computation
**Target:** C-II / macroscopic-container branch
**Starting status:** canonical Sections 122–123; finite exchange obstruction proof-only
**Active prompt:** docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md
**External literature search:** used for status only; no external theorem imported
**Computation:** used: research/verify_target_c_strict_saturated_chamber_regression.py

## LEVEL I STATUS

STILL OPEN.

This report records an exact finite family showing that the currently available
macroscopic-chamber statistics are compatible with strict one-point saturation.
It neither constructs a global minimizer nor disproves Erdős Problem #99.

## 1. Starting canonical endpoint

The current inactive-chamber endpoint is the finite exchange obstruction from the
proof-only Section 122 route. If C is an actual inactive chamber and Z_C its
contact-isolated source points, then

    Y subset C_{-1}, |Y|=|W|+1,
    strictly separated from each other and from Z_C \ W
        -> same-cardinality source after deleting W and one nonisolated core vertex
        -> contradiction to contact-minimality.

For W=emptyset, this gives the exact necessary condition

    C_{-1} subset union_{z in Z_C} closed_B(z,1).                 (1.1)

The proposed next bridge was that boundary-order Oler slack, a macroscopic protected
area, and inverse-diameter near-pairs might force a strict point outside all the
unit disks in (1.1). The construction below disproves that implication at the
fixed-container/feasible-packing level.

## 2. Strongest genuinely new result

Classification: regression / rejected local closure; noncanonical.

### Theorem — strict near-optimal hexagonal chamber with no add-one site

For every integer R >= 8, let u,v be unit vectors making angle pi/3, and define
the regular axial hexagon

    C_R = {s u + t v : max(|s|,|t|,|s+t|) <= R}.

Put

    h_R = 1 + R^{-2},
    Z_R = {h_R(iu+jv): (i,j) in Z^2,
           max(|i|,|j|,|i+j|) <= R-1}.                         (2.1)

Then:

1. every two distinct points of Z_R have distance strictly greater than one;
2. Z_R contains no unit contacts and hence no unit equilateral triangle;
3. Z_R lies in C_R and
       |Z_R| = 1 + 3R(R-1) = 3R^2 - 3R + 1;                  (2.2)
4. the ordinary Oler expression for C_R has exactly boundary-order slack
       area(C_R)/a_0 + per(C_R)/2 + 1 - |Z_R| = 6R,
       a_0 = sqrt(3)/2;                                     (2.3)
5. the one-unit erosion
       (C_R)_{-1} = {x in C_R : dist(x,partial C_R)>1}
   is covered by the closed unit disks centered at Z_R:
       (C_R)_{-1} subset union_{z in Z_R} closed_B(z,1);      (2.4)
6. Z_R contains an explicit matching of at least
       floor((R-1)/2) (2 floor((R-1)/2)+1) = Omega(R^2)        (2.5)
   disjoint pairs, each at distance exactly h_R=1+R^{-2}.

Thus a strict, triangle-free, boundary-order-slack packing can already be one-point
saturated throughout the protected chamber while carrying quadratically many
inverse-square near-contacts. The construction has no contact-isolated points
outside Z_R; it is an explicit chamber model, not a claimed source/core pair.

### Proof

Use the triangular lattice metric

    |iu+jv|^2 = i^2 + ij + j^2.                              (2.6)

For every nonzero integer pair (i,j), the right side is at least one. Therefore
for distinct points of Z_R,

    |h_R(iu+jv)-h_R(i'u+j'v)|^2
      = h_R^2 ((i-i')^2 + (i-i')(j-j') + (j-j')^2)
      >= h_R^2 > 1.                                         (2.7)

This proves strict separation and the absence of unit contacts.

The continuous hexagon C_R has side length R, area
area(C_R)=3a_0R^2, and perimeter 6R. Its lattice-coordinate inequalities have
integer right sides. Since

    h_R(R-1) = R-1 + (R-1)/R^2 < R,                          (2.8)

every point of Z_R lies in C_R. The standard six-side count gives (2.2), and
substitution into the area and perimeter formulas gives (2.3).

It remains to prove the exact covering statement. The triangular lattice with nearest
neighbor distance h_R has covering radius h_R/sqrt(3): triangulate the plane by
elementary equilateral triangles; the farthest point in one triangle is its
circumcenter. Since R>=8,

    h_R^2/3 < 1.                                             (2.9)

Take x in (C_R)_{-1} and choose a lattice point z=h_R(iu+jv) with
|x-z| <= h_R/sqrt(3) < 1. If z were outside C_R, then, because C_R is convex,
the segment from x to z would meet partial C_R and give

    |x-z| >= dist(x,partial C_R) > 1,

a contradiction. Hence z is in C_R. An integer-index lattice point in C_R has
axial norm at most R-1: an index with axial norm at least R is on or beyond one
of the six supporting lines of C_R, while x is more than one from those lines and
z is less than one from x. Consequently z belongs to Z_R, proving (2.4).

For the matching, set m_R=floor((R-1)/2). For every j in {-m_R,...,m_R}, pair
the lattice points with indices

    (-m_R+2k,j) and (-m_R+2k+1,j),  0 <= k < m_R.             (2.10)

Both indices have absolute value at most m_R, and their sum has absolute value at
most 2m_R <= R-1, so all endpoints belong to the radius-(R-1) hexagon. The pairs
are vertex-disjoint, and each has lattice difference (1,0), hence physical distance
h_R. This proves (2.5). □

## 3. Scope and precise obstruction

The theorem proves only a fixed convex-container statement. It does not claim that
C_R is an inactive face of a global minimizer, that Z_R is compatible with a
diameter-carrying contact core, or that no multi-point k -> k+1 exchange exists.
The one-point conclusion is exact: no point in (C_R)_{-1} is strictly farther than
one from all of Z_R. A multi-point rearrangement can still exist, and the theorem
does not address it.

This is stronger than a mere density regression in the relevant direction. The
points are all strictly separated, the protected region is covered by their unit
disks, the Oler slack is 6R, and the near-contact scale is 1+R^{-2}. Consequently
the following local implication is rejected:

    macroscopic convex chamber
    + Oler slack O(perimeter)
    + strict unit separation / triangle-freeness
    + quadratic inverse-D near-pairs
        -> one-point exchange site in the unit-protected interior.

The exact remaining C-II chamber obligation is therefore genuinely multi-point and
source-level: produce a finite strict k -> k+1 (or contact-budgeted) exchange, or
couple the chamber to the diameter-carrying core in a way that yields a strict
sub-D(n) competitor. One-point covering, Oler counting, and near-pair abundance do
not supply that bridge.

## 4. Dependencies

- The geometric construction and proof use only elementary triangular-lattice
  geometry and the stated axial metric.
- The interpretation of (2.3) as the standard Oler slack uses the same normalization
  as canonical Section 77; no new Oler theorem is imported.
- The comparison with the proof-only Section-122 exchange obstruction uses its exact
  scope: a strict new point must be farther than one from every retained source point.
- Contact-isolated source points of a global configuration are not deleted or silently
  identified with this model Z_R.

## 5. Exact frontier effect

This rejects the immediate protected-interior add-one closure of the macroscopic
container branch. It does not alter the canonical theorem-state manifest or close
any C-II branch. The full-core residual from Sections 122–123 is unaffected.

The useful reduction is now sharper:

    one-point covering + O(D) Oler slack + inverse-D near pairs
        -/-> strict exchange;
    the unresolved object is a finite collective rearrangement or a core-coupled
    diameter descent.

## 6. Claim audit table

| Claim | Status | Dependencies | Reason |
|---|---|---|---|
| Strict separation of Z_R | proved in this report | axial quadratic form | Exact inequality h_R^2>1 |
| Boundary-order Oler expression 6R | proved in this report | hexagon area/perimeter/count | Exact arithmetic identity |
| Protected unit-disk cover | proved in this report | triangular-lattice covering radius | h_R^2/3<1 and convexity |
| Quadratic matching at 1+R^{-2} | proved in this report | explicit row pairing | Exact index construction |
| Container statistics force a strict add-one site | rejected | new regression | (2.4) shows the opposite |
| No finite multi-point exchange exists | unresolved | none | One-point cover does not imply collective saturation |
| Model is a global minimizer | rejected as unclaimed | global source bridge absent | C_R,Z_R are only a feasible fixed-container model |
| Level I | open | original quantifiers | No global-minimality conclusion |

## 7. Regression checks

The construction was checked against relevant failure modes:

| Regression | Result | Exact reason |
|---|---|---|
| Near-equilateral triangle-free packing | pass | All pair distances are >1, so the contact graph is empty |
| One-point protected exchange | blocked exactly | Unit disks cover every point of (C_R)_{-1} |
| Boundary-order slack | pass | Slack is exactly 6R |
| Inverse-diameter pairs | pass | The matching has Omega(R^2) pairs at 1+R^{-2} |
| Contact-isolated source convention | pass | No source points are removed; Z_R is explicitly only a model set |
| Global optimality | not claimed | No diameter-minimizing source certificate is supplied |
| Multi-point exchanges | unresolved | The regression intentionally proves only one-point saturation |

The exact script command is

    python3 research/verify_target_c_strict_saturated_chamber_regression.py

It checks all displayed integer/rational identities at R=8,16,32,64,128. The
continuum covering proof is analytic; the script is not being used as a numerical
global-optimization certificate.

## 8. Literature imports

No external theorem is imported. The internet check only reconfirmed that the official
Problem #99 page still lists the problem as open and that the wording concerns every
diameter-minimizing set. The triangular-lattice covering-radius calculation is proved
directly above.

## 9. Computation

The exact verifier uses Python Fraction arithmetic and finite integer index sets. It
checks:

- |H_R| and |H_{R-1}|;
- strict source separation via the exact minimum quadratic form;
- containment of the homothetic source in the chamber;
- the exact Oler expression 6R;
- the explicit quadratic matching count; and
- the strict covering-radius inequality h_R^2/3<1.

The command and representative output are:

    python3 research/verify_target_c_strict_saturated_chamber_regression.py
    PASS R=8 h=65/64 z=169 sigma=48 matching=12 cover_radius^2=4225/12288
    PASS R=16 h=257/256 z=721 sigma=96 matching=56 cover_radius^2=66049/196608
    PASS R=32 h=1025/1024 z=2977 sigma=192 matching=465 cover_radius^2=1050625/3145728
    PASS R=64 h=4097/4096 z=12097 sigma=384 matching=1953 cover_radius^2=16785409/50331648
    PASS R=128 h=16385/16384 z=48769 sigma=768 matching=8001 cover_radius^2=268468225/805306368
    PASS: exact strict one-point-saturated chamber regression
    Scope: fixed convex container and feasible source only; no global-optimality claim

The computation does not test a multi-point exchange, a KKT stress, a diameter pair,
or global optimality.

## 10. Corrections / supersessions

This report does not supersede a canonical theorem. It narrows the use of the
proof-only Section-122 one-point covering consequence: that consequence is valid for
global survivors, but its converse/add-one interpretation is invalid even for a
boundary-order-slack, near-optimal strict chamber.

## 11. Promotion recommendation

Regression/rejection only — update state only to prevent reuse.

No theorem-state version, route map, or canonical dependency was changed.

## 12. Handoff

1. Strongest new result: the exact family (C_R,Z_R) is strictly separated,
   boundary-order Oler-close, quadratically near-contacted, and one-point saturated.
2. Canonical dependency chain: none beyond the normalization of Section 77 and the
   proof-only Section-122 exchange interpretation.
3. Exact remaining lemma: a source-preserving finite collective exchange or a
   core-coupled strict diameter descent for the actual macroscopic chamber.
4. Binding dead route: one-point covering, Oler slack, and near-pair matching alone.
5. Files to read next: docs/targets/target-c/CURRENT.md,
   research/target_c_section122_finite_exchange_saturation.md, and
   docs/targets/target-c/80-global-isolate-concentration-fullcore-disk-audit.md.
