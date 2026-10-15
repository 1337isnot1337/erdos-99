<!-- theorem-state: {"artifact_id":"ART-5E2C7541EF5C","canonical":true,"claim_ids":["C-COLLECTIVE-WALL-DELETION-BANK","C-COLLECTIVE-WALL-EXTERIOR-SHIELD","C-HEPTAGON-WALL-CAPACITY-REGRESSION"],"claim_statuses":{"C-COLLECTIVE-WALL-DELETION-BANK":"canonical","C-COLLECTIVE-WALL-EXTERIOR-SHIELD":"canonical","C-HEPTAGON-WALL-CAPACITY-REGRESSION":"regression"},"index":"docs/state/artifact-index.jsonl","status":"mixed","target":"target-c"} -->
# Target C independent audit: collective wall shield and capacity limit

Date: 2026-10-06. Audit authority: `35f5843ab9f5d11327d0f4cc803ed00707806ae7`,
state `2026-10-06.audit.65`. Immutable source: Worker 1 branch
`research/sol/target-c-owner-order-closure-20261006` at
`e6d04c4d58f3c104d82714375fe4e886ea864c11`. Classification: **PASS — promote**
for the collective exterior shield and eligible-deletion bank;
**PASS — already subsumed** for the finite contact-loss endpoint;
**REGRESSION VALID** for the exact D(8) capacity counterexample. Target C
C-II and Level I remain open.

## Scope audited

The source report's Sections 1--4 were audited. Its separate common-angle
Boolean claims, hexagon rank-scope regression, and the linked common-angle
amplitude argument in Section 5 were not included in this audit or promoted.
They remain proof-only until separately reviewed.

### Collective exterior shield

Let `F` be a convex polygon whose cyclic sides are actual unit contacts in a
unit-separated source `A`. Let `B` be a nonempty set of wall vertices with
pairwise distances at least two, and put

`W={x in int(F): |x-w|>1 for every wall vertex w not in B}`.

For every `x in W`, every old source point outside `int(F)` other than the
deleted vertices `B` is strictly more than one from `x`. All exterior
contact isolates are included.

To prove this, fix an exterior old point `q`. A retained wall vertex is
strictly guarded by definition. If `q` is not a wall vertex, unit separation
gives `|q-v|>=1` for each original wall vertex `v`. If `x` is at least one
from every original wall vertex, follow segment `xq` to its first wall
exit. At an exit point `y=lambda c+(1-lambda)d` on a unit side `cd`, each
segment endpoint `p` satisfies

`|p-y|^2=lambda|p-c|^2+(1-lambda)|p-d|^2-lambda(1-lambda)>=3/4`.

The two segment pieces therefore total at least `sqrt(3)>1`; exit at a wall
vertex gives total length at least two.

Otherwise `|x-v|=r<1` for a deleted vertex `v`. There is at most one such
vertex: for any other `w in B`, `|x-w|>=|v-w|-r>1`. Its two wall neighbors
`a,b` are retained. Translate `v` to zero. The strict guards imply
`x dot a < r^2/2` and `x dot b < r^2/2`; hence `x` is inside the convex
vertex cone spanned by `a,b`. Let `mu=max(x dot a,x dot b)<r^2/2<1/2`.

If the direction of `q` lies outside that cone, `x dot q<=|q|mu`,
`|q|>=1`, and `s^2-2s mu` is increasing for `s>=1`. Therefore
`|x-q|^2>=r^2+1-2mu>1`. If `q` lies in the cone but outside `F`, segment
`xq` cannot exit through either side incident with `v`. Every vertex on its
first exit side is at least one from `x`: retained vertices are guarded,
and every other deleted vertex is more than one from `x`. The unit-side
identity again gives `|x-q|>=sqrt(3)>1` (or at least two for a vertex exit).
This covers equality in every unused guard. The separation condition on `B`
is essential; adjacent deletions remain outside scope.

### Eligible deletion bank

From any finite `1`-separated set of `M` candidate wall vertices, greedily
retain a vertex and discard remaining candidates within distance `<2`. The
open radius-`1/2` disks around all candidates are disjoint. At each step,
the radius-`1/2` disks centered at all candidates removed at that step lie inside the
radius-`5/2` disk around the retained vertex. The area ratio is 25, so each
step removes at most 25 candidates, including its center. Thus the selected
set has size at least `ceil(M/25)` and pairwise distances at least two.
This supplies eligible wall deletions, not replacement sites.

### Finite endpoint and redundancy check

If `Y subset W` is a finite unit-separated packet with `|Y|>=|A intersect
int(F)|+|B|`, choose the required number of points and dilate the finite
packet by a factor just above one. Openness keeps it inside `W`, while all
internal distances become strictly greater than one. The collective shield
checks every retained exterior lower constraint; interior source points and
deleted vertices were removed. Since each deleted wall vertex removes its
two distinct incident side contacts and vertices of `B` are nonadjacent,
the move deletes at least `2|B|` contacts and creates none. The retained
contact graph is induced, hence triangle-free. New pairs are strictly below
the old global diameter because the inserted points lie in `int(F)` and
therefore in the interior of the full source hull.

This implication is valid, but it does not need a new theorem ID: it is a
special case of canonical `C-CONTACT-BUDGET-DIAMETER-EXCHANGE-ENDPOINT`
(Audit.64), with `j=0<t`. If every old actual diameter pair meets `B`, the
same finite replacement is a strict sub-`D` competitor. The report's exact
endpoint is therefore **already subsumed**, not an additional canonical
dependency.

### Exact D(8) capacity regression

The original Bezdek--Fodor Theorem 1.1 states that
`D(8)=1/(2 sin(pi/14))` and that an optimal eight-point configuration has a
regular unit heptagon as its convex hull (printed p.106). The original PDF
and transcription were checked locally:

- [`Bezdek--Fodor original PDF`](https://doi.org/10.1006/jcta.1998.2889)
- [`Original-paper transcription`](https://doi.org/10.1006/jcta.1998.2889)
- [Publisher record and DOI](https://doi.org/10.1006/jcta.1998.2889)

Take the regular unit heptagon with circumradius `R=1/(2 sin(pi/7))` and
retain its center as the eighth point. Then `1<R<7/6`, so the center is a
strict contact isolate. The source is a global D(8) minimizer by the
original theorem. Its contact graph is `C_7`, hence triangle-free; it has
seven actual diameter pairs, all on the wall. The wall has seven actual
unit contacts, so this source also attains the minimum contact count and
then minimum diameter-pair count among triangle-free minimizers.

Let `B` be any nonempty set of pairwise-distance-at-least-two heptagon
vertices. It is an independent set in the wall cycle. Consecutive retained
wall vertices then have angular gaps at most `4pi/7`, so every direction
has a retained wall vertex within `2pi/7`. For `x in int(F)` with
`r=|x|<R`,

`min_{w notin B}|x-w|^2 <= r^2+R^2-2rR cos(2pi/7)`.

Using `cos(2pi/7)=1-1/(2R^2)`, the right side minus one is
`(r-R)(r-(R-1/R))`. If `x` is in `W`, every retained guard is strict, so
necessarily `r<R-1/R<13/42<1/2`. Thus `diam(W)<1` and its unit-separated
capacity is exactly one: it contains the center, but no two points can be
unit-separated. The actual old interior population has size one. For every
nonempty eligible `B`, a replacement requires at least `1+|B|>=2` points,
so the proposed capacity inequality fails even at a globally optimal,
contact-minimal D(8) source with positive shell multipliers, PSD core stress,
and mixed core rank `2v-3`.

This is a genuine finite regression against an unrestricted capacity-gain
claim. It does not refute a sufficiently-large theorem, establish a
large-wall counterexample, or disprove Level I.

## Exact verification and limits

The source verifier passed. The independent audit verifier
`research/verify_target_c_collective_wall_capacity_audit_2026_10_06.py`
uses self-contained directed rational intervals and exact arithmetic in
the seventh cyclotomic field. It checks all 28 full-source pairs, the seven
contacts and seven actual diameter pairs, positive equilibrium, PSD core
stress rank four, mixed core rank eleven, all 28 independent deletion sets,
and the 14 deletion sets whose vertices are pairwise at least two apart.
It confirms `1<R<7/6`; it does not prove global optimality or the universal
shield/capacity statements. Those come respectively from the original
paper and the analytic arguments above.

## Canonical disposition

Promote `C-COLLECTIVE-WALL-EXTERIOR-SHIELD` and the narrowly scoped
`C-COLLECTIVE-WALL-DELETION-BANK` for `1`-separated candidate sets. Record
`C-HEPTAGON-WALL-CAPACITY-REGRESSION` as a regression. Do not add a second
ID for the finite replacement endpoint because Audit.64's contact-budget
theorem already covers it. Keep Section 5 of the source report and its
linked amplitude claims proof-only.

The macroscopic-container obligation remains: prove capacity for actual
large canonical interiors or construct a valid source-level competing
packet. The active C-II face-coupled finite-move target is unchanged.
