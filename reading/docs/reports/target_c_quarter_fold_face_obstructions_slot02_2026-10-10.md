> Generated reading edition · [exact source](../../../docs/reports/target_c_quarter_fold_face_obstructions_slot02_2026-10-10.md) · source SHA-256 `e441995708568951a3dd5eafcd162bf398669a46eaab99c91f142efc46e18f2f`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-498E42B6834E","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II: bowed eight-face exclusion and short-arc parity

**Date:** 2026-10-10. **Worker:** slot 02 (the final user assignment).
**Starting main:** `ab6dd3336f9f8d440f2bada76edb32153391cddc`.
**Theorem state:** `2026-10-10.audit.234`.
**Branch:** `research/sol61-slot02-20261010-integrated-fold`.
**Target:** integrated quarter-fold and isolate transport.
**Classification:** proved candidates awaiting independent audit and promotion;
the report is unreviewed and noncanonical.
**Active prompt:** [current Target C continuation](../prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md).
**Literature:** no external theorem imported.
**Computation:** exact finite checks in `Q(sqrt(15))`, including rational cases.

## Level I status

**STILL OPEN.** No universal finite competitor or unbounded family of globally
optimal triangle-free sources is constructed.

## 1. New endpoint reduction

**Continuation:** the [face-persistence report](target_c_deep_face_persistence_and_isolate_transport_slot02_2026-10-10.md)
uses the existing strict-convexity consequence of canonical local trapping for
contact-minimal global sources. Its Corollary 2.2 strengthens Theorem 5.1 below to constant signs
on **every** actual eight-face in a globally feasible exact-graph quarter-fold.
The straight-eight option below survives only in nonglobal finite models.

The principal result is **not conditional on preserved face correspondence**:

> For a triangle-free global minimizer with the minimum number of unit contacts,
> any full-source placement of diameter at most the old diameter, with exactly
> the old contact graph, can carry a nonconstant quarter-fold on an old simple
> convex actual eight-face only if all four sign arcs are straight. The old face
> is then a parallelogram with two unit edges per side, and has no interior
> source labels. In particular, an occupied convex eight-face cannot be active
> in such a placement, even if every isolate is allowed to relocate arbitrarily.

The proof combines the canonical boundary-local hull cover with a new finite
contact-release argument. A bowed folded eight-cycle is necessarily nonconvex.
The strict hull cover prohibits any other endpoint label in its hull, making
the cycle an actual bounded face automatically. A reflex face vertex admits a
small contact-opening displacement with strict upper slack. That displacement
preserves every source label and lowers the contact count, a contradiction.

The second result is a purely local reduction:

> In any boundary-feasible triangle-free nonconstant quarter-fold of a simple
> convex actual unit-contact face, each of its four sign arcs has total turn
> less than `pi/3`. If their edge counts are `r_0,...,r_3`, then
> `max(r_i,r_(i+2)) < (2/sqrt(3))*min(r_i,r_(i+2))`.
> For face degree at most 18, opposite counts are equal. Consequently every
> convex actual odd face of degrees 5, 7, 9, 11, 13, 15, 17 forces constant signs.

The canonical minimum-face theorem already handles degrees 5--7. Degrees
9--17 and the general arc-turn/count inequalities are the new conclusions.

```text
strict folded-hull cover + mixed turn signs
 -> automatic empty bounded nonconvex endpoint face
 -> finite full-source contact-loss competitor
 -> no bowed/occupied active eight-face in a globally feasible exact-graph fold

transition parallelogram + four >60-degree transition turns
 -> each sign arc turns <60 degrees
 -> matched opposite small arc counts
 -> constant signs on odd convex faces through degree 17
```

Neither chain supplies a nonconstant feasible fold on the remaining faces.

## 2. Definitions and canonical dependencies

Let a face boundary be counterclockwise, with positions `p_i`, unit vectors
`q_i=p_(i+1)-p_i`, and exterior turns `tau_i` in `[0,pi)`. A quarter-fold gives
signs `s_i` in `{+1,-1}` with `sum s_i q_i=0` and positions

`U_(i+1)-U_i=s_i Jq_i`, where `J(x,y)=(-y,x)`.

A sign arc is a maximal cyclic string of edges of one sign. A **bowed** arc has
a positive turn at at least one of its internal vertices; a straight arc has
zero turn at every internal vertex. Convexity here permits collinear consecutive
vertices. The core face has a simple actual boundary cycle; degree-zero source
labels are retained separately.

Only the following promoted geometric inputs are used:

1. `C-QUARTER-FOLD-CONVEX-FACE-CLASSIFICATION`, Audit.83:
   [proof, Sections 3--4](../audits/target_c_face_coupled_quarter_fold_independent_audit_2026-10-07.md).
   A locally lower-feasible triangle-free nonconstant fold has four transitions,
   each old transition turn exceeds `pi/3`, and the four corners form a
   nondegenerate inscribed parallelogram. Its proof is boundary-local.
2. `C-QUARTER-FOLD-MINIMUM-FACE-SIZE`, scope broadened by Audit.229:
   [boundary-local proof](../audits/target_c_minimum_face_size_local_endpoint_independent_audit_2026-10-09.md).
   Each arc has at least two edges; degree eight means `2,2,2,2`.
3. `C-QUARTER-FOLD-TRANSFORMED-EIGHT-FACE-HULL-COVER`, scope broadened by
   Audit.228: [boundary-local proof](../audits/target_c_local_quarter_fold_hull_cover_independent_audit_2026-10-09.md).
   The transformed boundary hull is covered by closed unit disks; if any arc
   bows, every point of that hull is strictly within one of a boundary label.

No area excess, uniform stress gap, matrix extension to isolates, preserved
embedding, outside capacity, or report-level unpromoted claim is a premise.

## 3. Finite contact release at a reflex actual face vertex

**Lemma 3.1 (proved candidate).** Let `A` be a triangle-free global minimizer
of diameter `D>1`, with the fewest contacts among triangle-free global minimizers
of its cardinality. Every bounded actual contact face with a simple cycle
boundary is convex.

**Proof.** First the straight-line unit-contact graph is plane. If two unit
edges with distinct endpoints cross, choose on each edge an endpoint at distance
at most `1/2` from the intersection. Their mutual distance is strictly less than
one, since the edges are noncollinear. Collinear overlapping unit edges likewise
have distinct endpoints at distance less than one. A nonincident source label
cannot lie on a unit edge. Thus such crossings and edge overlaps are impossible.

Suppose an actual simple face has a reflex vertex `v`. Its open interior sector
at `v` has angle greater than `pi` and contains no contact edge. Every unit
neighbor vector `w-v` lies in the complementary closed cone, of width less than
`pi`. Choose the unit vector `d` opposite the bisector of that cone. Then
`d dot (w-v)<0` for every unit neighbor.

The reflex vertex is not an extreme point of `conv A`: the polygon is contained
in that convex hull, whereas an extreme vertex cannot have a polygonal interior
sector wider than a half-plane. Every actual diameter endpoint is, in contrast,
strictly exposed. Indeed, if `|v-z|=D`, take `n=(v-z)/D`; for every other label
`w`,

`n dot (w-z) <= |w-z| <= D`,

and equality forces `w=v`. Hence `n dot w < n dot v` for all `w!=v`.
The reflex vertex therefore satisfies `|v-w|<D` for every other source label.

Let `eta_U=min_(w!=v)(D-|v-w|)>0`. Let
`eta_L=min_(w!=v, |v-w|>1)(|v-w|-1)>0` if this set is nonempty,
and omit that bound otherwise. Choose `0<epsilon<eta_U/2` and, when applicable,
`epsilon<eta_L/2`. Replace only `v` by `v+epsilon d`.

For each old neighbor,

`|v+epsilon d-w|^2 = 1-2epsilon d dot (w-v)+epsilon^2 > 1`.

Every old noncontact incident to `v` stays strictly above one by the triangle
inequality and `eta_L`; every incident upper pair stays strictly below `D` by
`eta_U`. All other pairs are unchanged. Thus all source labels, including every
isolate, remain; no new contact is created; every contact at `v` is removed;
and diameter stays at most `D`. The contact graph is a subgraph of the old
triangle-free graph. A smaller diameter contradicts global optimality; diameter
`D` contradicts contact minimality. This proves the lemma. `QED`

The argument gives an actual common positive displacement, not just a derivative.

## 4. Convex facial quarter-folds must have straight arcs

**Lemma 4.1 (proved candidate).** Suppose the old and folded boundary cycles
of a nonconstant convex-face quarter-fold are both convex polygons. Assume
boundary unit separation and triangle-freeness at the fold. Then all four sign
arcs are straight. The two polygons are subdivided parallelograms, and the
quarter-fold reverses their cyclic orientation. Each pair of opposite arcs has
equal integer edge counts.

**Proof.** Proper quarter-turns preserve determinants, so at every vertex

`cross(U_i-U_(i-1), U_(i+1)-U_i)
 = s_(i-1)s_i cross(q_(i-1),q_i)`.

At each transition the old turn is strictly between `pi/3` and `2pi/3`: the
lower bound follows from the folded two-step chord and triangle-freeness; the
upper bound follows because the old two-step chord is greater than one.
Therefore all transition determinants at `U` are strictly negative. A convex
`U` cycle must have clockwise orientation. At a same-sign vertex its determinant
equals the nonnegative old determinant, so convexity of the clockwise cycle
forces that determinant to vanish. An old turn of `pi` is impossible, since
two consecutive unit edges would return to the same point. Thus every internal
arc turn is zero. The only remaining corners are the four transition vertices,
which form the canonical parallelogram. Unit collinear steps make each chord
length equal its arc edge count; opposite chords have equal lengths. `QED`

In particular a bowed nonconstant fold has both signs of turn determinant and
cannot be convex in either orientation. Global reflection of the whole cycle
does not repair this.

## 5. Unconditional bowed and occupied eight-face exclusion

**Theorem 5.1 (proved candidate awaiting promotion).** Let `A` satisfy Lemma 3.1
and let `F` be an old simple convex actual unit-contact eight-face. Let `A'` be a
placement of **all** labeled source points, unit-separated, of diameter at most
`D`, with exactly the same unit-contact graph as `A`. Suppose its eight boundary
positions arise from a face-closed nonconstant quarter-fold. Then all four arcs
of `F` are straight, its side lengths are two, and `A` has no source label in
`int F`. Isolates at `A'` can move arbitrarily; no embedding hypothesis is made.

**Proof.** Exact graph preservation makes `A'` triangle-free, with the same
contact count. Global optimality forces its diameter to equal `D`, so it too is
a contact-minimal triangle-free global minimizer.

The boundary-local minimum-face theorem gives four two-edge arcs. Suppose some
arc bows. The strict transformed-hull cover says every point of
`H=conv{U_0,...,U_7}` is strictly within one of a transformed boundary label.
Hence no other label of `A'` can lie in `H`, by unit separation. This excludes
both isolates and positive-contact core labels, without fixing either population.

The eight cycle edges are a simple polygon by the unit-graph planarity argument
in Lemma 3.1. There is no nonconsecutive contact chord, since `A'` has the old
exact graph and `F` was an actual old face. The cycle interior lies in `H` and
contains no other graph vertex. No contact edge can enter it without crossing
the cycle, unless it is such a forbidden chord. Thus the folded cycle is an
actual bounded face **automatically**, even if the rest of the embedding changes.

Lemma 4.1 shows it is nonconvex: transition determinants are negative and a
bowed arc supplies a positive determinant. Lemma 3.1 now supplies a finite
full-source contact-loss move, a contradiction. Therefore no arc bows.

All four arcs are now straight with two unit steps, so `F` is a subdivided
parallelogram of side lengths two. To exclude old interior isolates, apply the
weak hull cover in the reverse direction. Consider just the eight transformed
labels as a source. They form a convex actual contact eight-cycle with no
nonconsecutive unit chord, by exact graph preservation. Applying the same signs
again gives increments `s_i J(s_i Jq_i)=-q_i`, hence positions `-p_i` up to a
translation. This reverse fold meets all boundary-local hypotheses. The weak
cover therefore covers `conv{p_i}` by closed unit disks about its boundary labels.
Every old source point inside the actual face is a contact isolate, strictly
farther than one from every boundary label. Such a point is impossible. `QED`

**Corollary 5.2.** In the full-diameter, exact-graph endpoint subcase of
Audit.230, every nonconstant eight-face is empty both before and after the fold.
The old nonconstant-eight-face population debit is zero. The positive-debit
occupied-eight-face subcase has no such integrated endpoint; outside transport
cannot make it feasible at diameter `D`.

Audit.230 itself assumes no endpoint upper bound and remains valid at its stated
scope. This corollary does not reject it, change its canonical status, or assert
an exterior capacity bound.

**Corollary 5.3 (source-dependent angular exclusion).** Fix an old face and a
nonconstant integrated field as above, with a bowed eight-face and a locally
unit-separated, triangle-free quarter-turn boundary. For the boundary family
`X_i(phi)=cos(phi)p_i+sin(phi)U_i`, there is `epsilon>0` such that no placement
of all other labels can complete an exact-contact-graph source of diameter at
most `D` for `|phi-pi/2|<epsilon`. In particular, every strictly convex eight-face
forces constant signs at any admissible quarter-turn endpoint.

**Proof.** On the compact quarter-turn hull, the continuous function
`min_i |x-U_i|` has a maximum `rho<1` by the strict cover. If all eight boundary
positions move by at most `eta`, every point of their new hull lies within
`eta` of the old hull. Its distance from some new boundary label is at most
`rho+2eta`, which is less than one for `eta<(1-rho)/2`. Continuity of the finite
boundary family supplies such an angular interval. The strictly negative
transition determinant and a strictly positive bowed-arc determinant also
persist on a sufficiently small interval. Whenever a full endpoint is lower
feasible, its cycle is simple; exact graph preservation prohibits chords.
The same strict-cover faciality and reflex-release argument therefore applies
throughout that interval. This proves a finite-source interval, with no
uniform width as bowing or pair margins vanish. The strictly convex conclusion
follows directly from Theorem 5.1, since every two-edge arc then bows. `QED`

## 6. Each transition arc turns less than sixty degrees

**Theorem 6.1 (proved candidate).** Let `F` be a simple convex actual unit-contact
face with `m>=5`, and a face-closed nonconstant fold of its boundary have
unit-separated, triangle-free boundary labels. Let `r_i` be its four arc lengths
in edges, and `T_i` each arc's total internal exterior turn. Then

`0<=T_i<pi/3`, `r_i>=2`, and

`max(r_i,r_(i+2)) < (2/sqrt(3))*min(r_i,r_(i+2))`.

If `m<=18`, `r_0=r_2` and `r_1=r_3`, so `m` is even.

**Proof.** The canonical classification gives four transition turns greater
than `pi/3` and a transition parallelogram. The remaining old turns sum to
less than `2pi/3`; in particular each arc's tangent span is less than `pi`.
Its chord direction therefore lies between its first and last edge directions.
Write these directions as chord angle minus `a_i` and chord angle plus `b_i`,
where `a_i,b_i>=0` and `a_i+b_i=T_i`.

Let `kappa_i` be the turn from the preceding chord to chord `i`. Parallelogram
chords alternate turns `gamma` and `pi-gamma`, so
`kappa_i+kappa_(i+1)=pi`. The transition turn at the start of arc `i` is

`tau_i=kappa_i-b_(i-1)-a_i`.

Adding the transitions at its two ends gives

`tau_i+tau_(i+1)=pi-T_i-b_(i-1)-a_(i+1)>2pi/3`.

Thus `T_i+b_(i-1)+a_(i+1)<pi/3`, proving the claimed strict arc-turn bound.
Projection of its `r_i` unit vectors on the middle of their tangent interval
gives its chord length `L_i` the bounds

`L_i >= r_i*cos(T_i/2) > (sqrt(3)/2)*r_i`, and `L_i<=r_i`.

Opposite parallelogram chords satisfy `L_i=L_(i+2)`. Combining the lower bound
for the larger edge count and the upper bound for the smaller gives the ratio.
Every arc has at least two edges by Audit.229.

If opposite counts differ and the smaller count is `k<=6`, the ratio is
impossible: `k+1 >= (2/sqrt(3))*k`, since
`3(k+1)^2-4k^2=-k^2+6k+3>0` on `1<=k<=6`.
An unequal pair thus has at least seven and eight edges. The other two arcs
have at least two each, so `m>=7+8+2+2=19`. For `m<=18`, both opposite pairs
are equal and `m=2(r_0+r_1)` is even. `QED`

**Corollary 6.2.** Every convex actual face of odd degree at most 17 has constant
sign in a boundary-feasible triangle-free quarter-fold. Such a face forces all
its incident train signs equal. This can be added to the canonical source sign
relations; it is a necessary condition, not a realization or endpoint theorem.

## 7. Exact finite adversarial checks

The companion verifier uses rational arithmetic and exact sign comparisons in
`Q(sqrt(15))`. No floating-point comparisons nominate or certify extrema.

1. **Bowed eight-cycle.** In units of `1/41`, use
   `(0,0),(40,-9),(80,0),(89,40),(80,80),(40,89),(0,80),(-9,40)`.
   Signs are `++--++--`. The old and folded configurations have exactly eight
   cycle contacts, are triangle-free, and both have diameter squared
   `12800/1681`. Old area is `7840/1681`; folded signed area is `-4960/1681`.
   After undoing the common quarter-turn, the folded positions are
   `(0,0),(40,-9),(80,0),(71,-40),(80,-80),(40,-71),(0,-80),(9,-40)`,
   again divided by 41. Moving label 1 down by `1/100` removes exactly its two
   contacts, creates none, and leaves every pair at most the same diameter.
   Adding the old strict isolate `(40,40)/41` gives four lower collisions if
   that isolate stays fixed through the actual `J` fold. This is a nonglobal
   finite regression, not a source minimizer: a regular unit octagon has diameter
   squared `4+2sqrt(2)<7<12800/1681`.
2. **Straight eight-cycle.** The perimeter of the two-by-two grid generated by
   `u=(1,0)`, `v=(5/13,12/13)` admits the mixed fold. Both endpoints have exactly
   the cycle contacts and diameter squared `144/13`; the old diameter `(0,4)`
   is replaced by `(2,6)`. Both polygons are convex, oppositely oriented. This
   prevents extending Theorem 5.1 to forbid all nonconstant eight-face states.
3. **Odd 21-cycle.** A bottom arc has four copies of `(7,-sqrt(15))/8`, followed
   by four copies of `(7,+sqrt(15))/8`; the other arcs have vectors `(0,1)`
   three times, `(-1,0)` seven times, and `(0,-1)` three times. Signs are
   constant and alternate on these arcs: `+,-,+,-`. Opposite chords cancel.
   Both endpoints have exactly 21 cycle contacts and diameter squared 58.
   The folded minimum noncontact squared distance is
   `2-sqrt(15)/4>1`; source area is `21+7sqrt(15)/4` and folded signed area is
   `-21+7sqrt(15)/4`. A 21-point subset of a five-by-five square grid has
   diameter squared 32, proving nonglobality. This prevents extending the
   short-odd-face exclusion to all odd face degrees. It does **not** decide
   whether degree 19 can occur; 19 is only the first degree not excluded by
   the edge-count ratio.
4. **Exact count reduction.** Enumerating the finite count vectors with all
   arcs at least two and total degree 8--18, the strict squared ratio tests
   leave 21 vectors; all have equal opposite counts and even degree.

Commands:

```text
python3 research/verify_target_c_quarter_fold_face_obstructions_2026_10_10.py
python3 tools/build_artifact_index.py --write --write-headers
python3 tools/check_theorem_state.py
git diff --check
```

The saved certificate is
`research/target_c_quarter_fold_face_obstructions_certificate_2026_10_10.json`.
The three source/fold/release ledgers plus the old centered-isolate ledger check
596 full pairs; the 21-point nonglobal competitor separately checks 210 upper
pairs. The finite calculations do not prove the analytic universal theorems.

Executed in the isolated worktree: the new saved certificate matches rerun output
byte-for-byte; the canonical Audit.83 finite verifier reproduces its saved JSON;
the theorem-state and PR-transaction checkers pass; the active-route checker and
all 22 theorem-state tooling tests pass; `git diff --check` passes; and every
relative report link resolves. Main was refreshed and remained at the recorded
SHA. No independent mathematical referee has audited these new proofs.

The focused submission is [PR #948](../publication/provenance.md#source-records).
No hosted job steps executed for this historical run; only the local checks
above are reported as executed. The complete registered certificate suite was not rerun:
no canonical dependency, theorem-state authority, or certificate registration
was changed, and the relevant Audit.83 finite regression was rerun separately.

## 8. Other attacks and their precise limits

- A direct finite path from the source to the quarter-turn was not obtained.
  Mixed turn signs give a topological obstruction to convex face preservation;
  checking old diameter weighted means would still omit inactive upper pairs.
  Audits.83, 120 and 121 remain binding at their exact scopes.
- Exterior capacity was not inferred from old Oler slack. Instead Theorem 5.1
  excludes the occupied-eight-face endpoint itself, before any outside capacity
  estimate is needed. It leaves isolates in larger faces and the outside region.
- Face orientation alone does not force a single orientation throughout a
  contact graph with separations. The proof uses the strict eight-hull cover to
  establish faciality for that cycle; it does not assume global embedding
  uniqueness or infer source feasibility from an abstract sign assignment.
- The local parity reduction is not extended to all odd degrees: the exact
  21-cycle is an adversarial counterexample to that stronger local claim.

## 9. Classification, frontier effect, and next theorem

| Claim | Classification | Exact effect |
| --- | --- | --- |
| Reflex-vertex finite contact release | Proved candidate awaiting promotion | Full-source contact-loss construction for an actual nonconvex face |
| Globally feasible active eight-faces are straight and empty | Proved candidate awaiting promotion | Excludes bowed and occupied eight-face endpoint branches without embedding assumptions |
| Arc-turn and opposite-count inequalities | Proved candidate awaiting promotion | Constant-sign constraints on odd convex faces through degree 17 |
| Rational bowed/straight eight examples | Regression | Distinguishes nonglobal folds, finite release, and the surviving straight case |
| Algebraic odd 21-cycle | Regression | Refutes universal odd-face sign collapse under local hypotheses |
| Universal integrated fold or full Level I conclusion | Unresolved | No source-realized assignment or universal competitor constructed |

No canonical state file, route prompt, or certificate registration is changed.
Independent audit should check Lemma 3.1's finite full-source margin, the
automatic faciality step from the strict hull cover, the reverse weak cover,
and the adjacent-transition identity in Theorem 6.1.

**One next obligation:** for every canonical `D>=9` C-II survivor, construct a
nonaffine integrated train field and a placement of every source isolate such
that every old contact stays unit, every old noncontact stays strictly above
one, every old diameter is at most `D`, and every old nondiameter is strictly
below `D`, with signs constant on every occupied or bowed convex eight-face
and on every convex odd face of degree at most 17. Such a placement would pass
the complete Audit.83 endpoint theorem and contradict the canonical
lexicographic source. Its existence is not established here.

Before attempting it, read this report, Audits.83/228/229, and the current Target C
ledger. Larger active faces, isolates outside the rigid faces, and all newly
active upper constraints remain live. The subsequent strict-convexity argument
excludes the straight active eight-face case for canonical global sources.
