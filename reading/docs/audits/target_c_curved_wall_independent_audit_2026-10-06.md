> Generated reading edition · [exact source](../../../docs/audits/target_c_curved_wall_independent_audit_2026-10-06.md) · source SHA-256 `651126d56d55b0eca7c0e95c5a9e8d8adfa0798a6dc8a74cead2aa6d3312b1c5`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-ADA0260F528E","canonical":true,"claim_ids":["C-CURVED-WALL-BLOCKER-POPULATION","C-CURVED-WALL-ISOLATE-PRESERVING-RELEASE","C-CURVED-WALL-NONISOLATE-BLOCKER-REGRESSION"],"claim_statuses":{"C-CURVED-WALL-BLOCKER-POPULATION":"canonical","C-CURVED-WALL-ISOLATE-PRESERVING-RELEASE":"canonical","C-CURVED-WALL-NONISOLATE-BLOCKER-REGRESSION":"regression"},"index":"docs/state/artifact-index.jsonl","status":"mixed","target":"target-c"} -->
# Independent promotion audit — curved unit-wall inward release

**Date:** 2026-10-06
**Audit base:** `a2811924d18778e8220c42904c9a5a92b58ffd78` (`2026-10-06.audit.66`)
**Audited source snapshot:** `research/sol/target-c-owner-order-closure-20261006` at
`1ca17812adc0b8741a423d0a19fae61d3fa2332a`
**Candidate:** `docs/reports/target_c_curved_unit_wall_isolate_preserving_inward_release_2026-10-06.md`
**Verdict:** PASS for the curved-wall finite release and the narrowed interior-blocker payment; FAIL for the report's isolate-only blocker conclusion.
**Frontier effect:** no C-II or Level I closure; the active obligation is unchanged.

## Exact promoted statements

### C-CURVED-WALL-ISOLATE-PRESERVING-RELEASE — PASS WITH EXPLICIT CHAMBER SCOPE

Fix `M>=4`, `0<c<1/2`, and `s=sqrt(1-c^2)`. For all sufficiently small
positive `theta` (the threshold may depend on `M,c`), use the four cyclic side
directions `u,v,-u,-v`, where `u=(1,0)` and `v=(c,s)`. On each side take the
`M` unit edges with angle offsets `(2j-M+1)theta`. Their perpendicular
components cancel, so the four side displacements close exactly. The cyclic
edge directions give a strictly convex wall `F_theta` with `4M` actual unit
edges.

With `lambda=1/(100M)`, `ell=1+tan(theta/2)/(50M)`, and the report's centered
oblique grid, the `(M-1)^2` points `z_ij`, `1<=i,j<=M-1`, are strictly inside
the wall, mutually strictly unit-separated, and strictly farther than one
from every wall vertex. The strict claims persist from `theta=0` except at the
unit wall-to-inner first-row/first-column pairs. On the bottom side their
half-squared-distance derivative is

`i(M-i)s + lambda*(c(i-M/2)+(1-M/2)) > 0`.

The error term has magnitude below `3/400`, while the first term is at least
`(M-1)s`; rotations and sign reversals give the same estimate on the other
sides. For the selected indices `i=2,5,8,...<=M-2`, move each selected wall
vertex inward by `h=3 sin(theta)` along its inward bisector. Its two former
unit wall contacts become squared distance `1+3 sin(theta)^2`. The only
borderline root-to-grid pairs have derivative

`(i(M-i)-3)s + lambda*(c(i-M/2)+(1-M/2)) > 0`,

because `i(M-i)-3 >= 2M-7`. All other lower constraints have strict limiting
slack. For fixed `M,c`, the selected old vertices have pairwise distance
strictly greater than two; continuity gives the same for the roots. Every
root is strictly inside `F_theta` for small positive `theta`.

Consequently, if a canonical contact-minimal triangle-free global minimizer
contains this wall and every actual source point in `int(F_theta)` is strictly
farther than one from every selected root, deleting the selected old vertices
and inserting the roots is a valid same-cardinality full-source competitor.
The canonical one-vertex shield covers retained source points outside the
wall. Root-to-source upper distances are strictly below the old diameter since
the roots lie in the interior of the old source hull. No new contact appears,
while at least `2|B|` distinct wall contacts disappear. The new source has
diameter at most the old optimum, so contact-minimality excludes this chamber
from the canonical representative. The exact grid is a sufficient interior
population for this implication; the theorem does not assert that this family
is globally optimal.

### C-CURVED-WALL-BLOCKER-POPULATION — PASS, NARROWED

For the same wall and selected bank in a contact-minimal canonical source, each
root that cannot be inserted must be within distance **strictly less than
one** of an actual source point in `int(F_theta)`. Distinct roots have
distance greater than two, so one interior source point cannot block two
roots. Thus the count of blocked roots is at most the number of actual interior
source points.

Independent local check: use coordinates `q=0`, inward tangent-normal frame
`(a,n)`, wall neighbors `+cos(theta)a+sin(theta)n` and
`-cos(theta)a+sin(theta)n`, and the root `x=h n`. If `|z-x|=1` for an
interior source point and `z_n<=h`, then
`|z-a-coordinate|>=sqrt(1-h^2)` and `|z|^2<=1+h^2`. Separation from both old
wall neighbors instead implies
`|z|^2>=2 cos(theta)*sqrt(1-9 sin(theta)^2)`. For
`0<sin(theta)<=1/10`, the difference after squaring is
`3-58 sin(theta)^2-45 sin(theta)^4 >= 4831/2000 > 0`, a contradiction.
Therefore every equality point has `z_n>h`, and moving the root a sufficiently
small distance in direction `-n` opens all its interior unit contacts. The
root remains inside the wall, retains strict clearance from the other wall
vertices, and retains its strict upper-distance margins. The canonical
one-vertex shield handles the exterior. This finite motion would lose the two
old wall contacts without adding any, contradicting contact-minimality.

The discovery report's further inference that each blocker must be an
**isolate** is not valid. A blocker can be a positive-contact interior point,
including one that contacts the deleted wall vertex. The theorem above makes
no isolate count claim.

### C-CURVED-WALL-NONISOLATE-BLOCKER-REGRESSION — REGRESSION VALID

An exact `M=4` rational instance has a strictly interior point `z` with
`|z-q|=1` at the deleted wall vertex `q`, distance at least one from every
wall vertex, and distance strictly less than one from the proposed inward
root. Hence the root is blocked by a non-isolate. This refutes the
isolate-only deduction from the local wall geometry; it is not a globally
optimal source or a Target C counterexample.

## Dependencies, certificates, and attempted failures

The finite full-source exclusion uses canonical `C-ONE-VERTEX-CONVEX-WALL-SHIELD`
for retained exterior points, plus the canonical source normalization and
finite contact-minimality. It does not identify the source with the explicit
wall-plus-grid family. The local blocker count is source-level only under the
stated canonical-minimizer hypothesis.

The independent exact verifier is
`research/verify_target_c_curved_wall_audit_2026_10_06.py`. It reconstructs all
four rational examples `(M,t)=(4,3/5),(6,3/4),(8,3/5),(12,3/5)`, checks all
18,912 old and 18,912 new source pairs, contact release, strict convexity and
interiority, the 100 rational local-opening inequalities, and the non-isolate
blocker regression. The verifier proves those finite instances only. The
all-`M`, sufficiently-small-`theta` statements above follow from the analytic
finite-margin and derivative arguments, not from extrapolating the verifier.

Hostile checks found no failure in the exact family construction or the
conditional whole-source replacement under its explicit chamber hypothesis.
They did find the isolate overclaim. No actual global minimizer with this
curved wall has been constructed, no arbitrary canonical chamber has been
shown to lie near the grid cloud, and no asymptotic population or C-II closure
follows. C-II and Level I remain open.
