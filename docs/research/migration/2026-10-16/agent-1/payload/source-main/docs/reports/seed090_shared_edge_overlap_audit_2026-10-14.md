<!-- theorem-state: {"artifact_id":"ART-D33762849A4B","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# Erdős Problem #99 — shared-edge overlap audit of Seed 90

**Date:** 2026-10-14
**Repository commit:** `4a10ce3b6e846f31b167b63aaa41abde9193b345`
**Reviewed PR head:** `1c11b028541570cdd786fc1a8d1dfa337ca99a96`
**State version:** `2026-10-10.audit.234`
**Run type:** audit
**Target:** shared
**Starting status:** the reviewed report and its claims are unreviewed; C-II and Level I are open
**Active prompt:** none; this audit addresses the shared report in PR [#972](https://github.com/1337isnot1337/e-99/pull/972)
**External literature search:** not used
**Computation:** used the PR's finite verifier and added an exact overlap regression

## LEVEL I STATUS

`STILL OPEN`

## 1. Starting canonical endpoint

The canonical Target C endpoint is unchanged: the full-core branch still needs a
source-realized finite move or discrete replacement satisfying every source lower
constraint, every actual-diameter upper constraint, and the unary rhombus tests. The
separate macroscopic-container branch still lacks arbitrary-container capacity or a
moved-core strict-diameter closure.

PR #972 proposes a general finite locking theorem for an edge-connected family of
unit rhombi, then applies it to a square frame. The review question here is narrower:
does the proof of shared-edge propagation cover cycles that share labels beyond their
common edge?

## 2. Strongest new result

**Classification:** exact regression against an overbroad proof step; repair of the
stated locking theorem's propagation argument. This report remains unreviewed and
noncanonical.

### Statement

The sentence “two different cells cannot occupy the same half-plane” is false when
the cycles share a label beyond the common edge. The theorem's conclusion survives:
if two cycles share an extra label, that label fixes the second cell's orientation;
if they share exactly the edge endpoints, the same-half-plane exclusion applies.

### Exact regression

Use the five labelled points

\[
A=(0,0),\quad B=(0,1),\quad
D=(\sqrt3/2,1/2),\quad
C=(\sqrt3/2,3/2),\quad
E=(\sqrt3/2,-1/2).
\]

Take the two cycles \(A\!-\!B\!-\!C\!-\!D\!-\!A\) and
\(A\!-\!B\!-\!D\!-\!E\!-\!A\). Their squared pair distances are

\[
|AB|^2=|AD|^2=|AE|^2=|BD|^2=|BC|^2=|CD|^2=|DE|^2=1,\quad
|AC|^2=|BE|^2=3,\quad |CE|^2=4.
\]

Thus the five points are unit-separated. Each cycle is a unit rhombus, the cycles
share the edge \(AB\) and the additional label \(D\), and all three off-edge
vertices \(C,D,E\) lie in the same open half-plane bounded by \(AB\). In the
shared-edge parameterization from PR #972, the first cell has parameter \(1/2\)
and the second has parameter \(-1/2\); the lower vertex of the first is the
upper vertex of the second, but both occurrences are the same source label \(D\).
So this is not a collision of distinct labels.

The equality case in the original argument therefore does not always violate unit
separation: it does so only when the coincident positions belong to distinct labels.
The PR's statement that it always does is too broad.

The finite fixture does not contradict the locking theorem. The common label \(D\)
is a third noncollinear point shared by both cells, so after one cell is aligned,
the neighboring cell cannot be reflected across \(AB\) without moving \(D\).

### Corrected propagation proof

First align one selected cell with its source placement by a Euclidean isometry.
Every selected cell is congruent to its source cell: for a unit four-cycle, the
two diagonal squares sum to four, so nonincrease of both diagonals forces equality
of both. Its four labels therefore have exactly the source coordinates up to an
isometry.

Now consider an adjacent cell sharing edge \(AB\) with the aligned cell. A
congruent labelled cell fixing \(A,B\) has only two placements: its source placement
and its reflection in the line \(AB\).

If the cycles share any additional label \(X\), then \(X\) lies off \(AB\), since
each four-cycle is a nondegenerate rhombus with distinct labels. The aligned cell
already fixes \(X\). Reflection in \(AB\) changes its position, so the shared label
forces the source placement.

It remains to handle cycles sharing exactly \(A,B\). Normalize \(A=(0,0)\),
\(B=(0,1)\). For a unit rhombus on one side of \(AB\), its two other vertices
have the form

\[
v(t)=(\sqrt{1-t^2},t),\qquad v(t)+(0,1),
\qquad -1/2\le t\le1/2.
\]

The interval follows from unit separation between each off-edge vertex and the
opposite endpoint of \(AB\). Write \(t=\sin\phi\); then
\(-\pi/6\le\phi\le\pi/6\), and
\[
|v(t)-v(u)|=2\sin(|\phi-\psi|/2)\le1.
\]

For two cells sharing only \(A,B\), their lower vertices are distinct labels.
Unit separation rules out a strict inequality. Equality requires the two extreme
parameters \(-1/2,1/2\) (in either order); then the upper vertex of one cell
coincides with the lower vertex of the other. Those are also distinct labels in
this case, again contradicting unit separation. Hence two such cells cannot lie
in the same half-plane. This applies both to the source cells and to the endpoint
cells. Since the source cells occupy opposite sides, the endpoint neighbor must
use its source placement.

Applying this argument along a spanning tree of the edge-adjacency graph aligns
every selected cell. Thus the locking theorem remains valid with the stated
hypotheses; its propagation proof needs the overlap case above.

## 3. Exact frontier effect

The audit repairs a proof step for the finite locking theorem in PR #972. It does
not change canonical theorem state, construct a move for a canonical source, or
close any branch. The square-frame bow still has only two actual diameter pairs
under its stated hypotheses; no extension to the canonical loaded diameter graph
is established here.

## 4. Exact remaining lemma

For this route to affect C-II, one would still need to extract a source-realized
finite move that handles the canonical source's full actual-diameter graph and
retains every source label while preserving all lower constraints. The finite
overlap correction supplies no such extraction or move.

## 5. Claim audit table

| Claim | Status | Dependencies | Reason |
| --- | --- | --- | --- |
| Same-half-plane exclusion for any two distinct cells sharing an edge | Rejected as worded | Exact five-label fixture above | Extra shared labels can identify the coincident positions. |
| Shared-edge propagation for cycles sharing exactly their edge endpoints | Proved in this report | Unit separation; each cell is a nondegenerate unit rhombus | The parameter interval and equality collision involve distinct labels. |
| Propagation when cycles share an additional label | Proved in this report | Congruence of each cell; shared label fixed by the aligned cell | Reflection across the common edge moves every off-edge point. |
| Edge-connected locking theorem of PR #972 | Proof repaired in this report; theorem statement unchanged | The two preceding cases and individual cell congruence | The repaired cases propagate along a spanning tree. |
| Other claims in the Seed 90 report, including its dense population and stress certificates | Not audited here | PR #972 report and verifier | This contribution is limited to shared-edge overlap and propagation. |
| C-II and Level I closure | Open | Canonical theorem state | No canonical source-level move is supplied. |

## 6. Regression checks

| Regression/correction | Result | Exact hypothesis or failure |
| --- | --- | --- |
| Five-point same-side overlap | Pass | Two distinct unit rhombi share edge \(AB\) and label \(D\); all pair distances are at least one. |
| Distinct-label equality collision in the edge-only case | Pass analytically | At parameters \(-1/2,1/2\), the coincident off-edge positions carry distinct labels when the cells share only \(A,B\). |
| Extra-label orientation pin | Pass analytically | A shared off-edge label changes position under reflection across \(AB\). |

## 7. Literature imports

None.

## 8. Computation

The new script `research/verify_seed090_shared_edge_overlap_audit.py` uses exact
rational coefficients in \(\mathbb Q(\sqrt3)\) to enumerate all ten pair distances,
check both four-cycles' unit sides and diagonals, and verify the shared-label and
same-half-plane conditions. Its output confirms this one finite regression only;
the corrected propagation theorem is proved analytically above.

The PR's `research/verify_seed090_rhombus_contraction.py` was also rerun at its
head. It passed its exact fixtures for \(m=24,40,64\), including 46,360,
1,081,185, and 10,208,421 pair checks respectively. That script is the candidate's
own verifier, not an independent implementation, and its finite runs do not prove
the all-size statements.

## 9. Corrections / supersessions

Correct the sentence in PR #972's shared-edge proof that asserts same-side
occupancy is impossible for all different cells. Restrict that claim to cells
sharing only the common edge endpoints; use the shared-label pinning argument
when there is any additional overlap. The theorem statement and other conclusions
are not rejected by this correction.

## 10. Promotion recommendation

**Unreviewed.** This report records an independent proof correction but does not
request canonical promotion. The finite locking theorem remains a candidate in
PR #972; its other claims and the canonical C-II endpoint remain outside this
audit.

## 11. Handoff

1. Strongest result: an exact overlap regression and a complete repair of the
   shared-edge propagation proof.
2. Canonical dependency chain: none; no canonical theorem is added or changed.
3. Exact remaining lemma: construct a full-source feasible finite move for a
   canonical C-II source, handling every actual diameter pair.
4. Binding limit: the audit does not extend the frame bow to the canonical loaded
   diameter graph.
5. Next files: the current Target C frontier and the reviewed Seed 90 report,
   followed by any independent audit of its density, stress, and explicit
   all-size bow estimates.

## Preservation status (2026-10-15)

Frozen source: PR #979 at `9682cab4815fd31d41b6cd2049e15c6a6966b3ca`.
Its corrected propagation case split is incorporated in the
[reconciled Seed 90 report](seed090_finite_rhombus_contraction_2026-10-13.md).
The historical audit above did not check the other Seed 90 theorems. The
subsequent maintainer AI audit and its precise limits are recorded in the
reconciled report; neither audit counts as human peer review or promotion.
