<!-- theorem-state: {"artifact_id":"ART-D3A9A075EC98","canonical":true,"claim_ids":["C-PHASE-CORRIDOR-ENDPOINT-EXCLUSION"],"claim_statuses":{"C-PHASE-CORRIDOR-ENDPOINT-EXCLUSION":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C — Section 102 phase/corridor endpoint-exclusion hostile audit

**Date:** 2026-09-12
**Verdict:** PASS as a proof-only theorem, with one orientation clarification recommended in Lemma 102.1.
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This audit checks `102-phase-corridor-endpoint-exclusion-audit.md`, including the
claim that the Section-101 endpoint

\[
\mu_8=0.9760407652670519821\ldots
\]

cannot be approached by a macroscopic locally rhombus-saturated wrapping Type-II
harmonic carrier.  The argument survives hostile review.  The compactness step then
correctly yields an absolute but presently unquantified strict improvement
`mu_8+epsilon_*`.

The audit treats separately the equality normal form, the curved-tooth dispersion
lemma, the cell-local Section-90 transfer, the corridor/phase alignment step, and the
final compactness upgrade.

## 1. Section-101 equality normal form is used correctly

Section 101 and its independent hostile audit give

\[
2\alpha\le |S|\le U,
\qquad
2\alpha\ge\sum_j\sin(g_j/2)
\ge\sin(\theta/2)+2\sin\theta,
\]

where `U=3theta-2pi`.  At `theta=theta_8` the two scalar endpoints are equal, so every
inequality is sharp.

Strict concavity of `sin(x/2)` on `(0,pi)` forces the positive complement-gap vector,
up to cyclic order, to be exactly

\[
(\theta_8,\phi_8,\phi_8),
\qquad
\phi_8=2\pi-2\theta_8.
\]

There are therefore exactly three connected support components.  The two components
adjacent to the `theta_8` gap are singletons.  To see this directly, move a point by a
small positive angle `epsilon` into either adjacent support component.  Its minor
angular separation from the opposite endpoint of the `theta_8` gap becomes
`theta_8+epsilon` while the complementary separation remains larger than `theta_8`
for `epsilon<phi_8`.  This violates the angular-diameter condition.  The third support
component has no internal complement interval and carries all support measure, hence
is one closed circular arc of angular length

\[
U_8=3\theta_8-2\pi<\pi.
\]

Thus the Section-102 one-arc-plus-two-points normal form is correct.

## 2. The endpoint outer-walk bookkeeping is valid

At the endpoint,

\[
2a_D=U_8D+o(D).
\]

The three complement gaps contribute chord currency

\[
D\bigl(\sin(\theta_8/2)+2\sin\theta_8\bigr)+o(D)
=U_8D+o(D).
\]

Together with the ordinary two-edge attachment-interval floor and the exact canonical
Section-82 identity

\[
L_D+Q_D=4a_D-6-2s_D-2c_D,
\]

the inequalities squeeze all extensive slack to zero.  In particular

\[
Q_D=o(D),\qquad s_D=o(D),\qquad c_D=o(D),
\]

and each of the three macroscopic complement routes has `o(D)` path excess above its
endpoint chord.

Integer route slack also implies that all but `o(D)` ordinary attachment intervals
have exactly two outer-contact edges.  Since a loaded middle vertex on such a route
uses loaded-loaded contacts in the induced harmonic graph, `c_D=o(D)` removes all but
`o(D)` loaded-apex exceptions.

Finally `2alpha=|S|` saturates the Section-100 near-circle unit-spacing estimate on the
single positive-length support arc.  After a standard diagonal Markov discard, all
but `o(D)` retained polygon bases on that arc have length `1+o(1)` uniformly.  Their
two-edge routes are therefore unit-unit near-equilateral teeth with unloaded apices.
The endpoint normal form used later in Section 102 is justified.

## 3. Physical rhombus-boundary endpoints are localized correctly

Every physical boundary edge of the full strict-rhombus complex faces either the
outer face of the induced harmonic contact graph or a bounded nonquadrilateral face.
Canonical Section 82 says every bounded four-face is a strict unit rhombus, so there
is no missing quadrilateral case.

The total degree of bounded nonquadrilateral faces is at most `5Q_D=o(D)`.  Hence only
`o(D)` physical train endpoints can terminate against such faces.  All remaining
physical train endpoints occur on the outer face and, at first order, therefore lie
on the retained tooth arc or on one of the three macroscopic complement corridors.
Bridges are harmless here: a bridge occurrence is not a strict-rhombus boundary edge
unless a rhombus actually lies on the relevant side, and the proof counts only
physical rhombus-boundary edges as train ends.

## 4. Curved-tooth phase dispersion is correct after one orientation clarification

Lemma 102.1 states that a family of physical rhombus-boundary tooth legs whose
projective directions lie in an `o(1)` interval has only `o(D)` members.

The tooth geometry is correct: for a retained base of length `1+o(1)`, either unit leg
makes projective angle

\[
\pi/3+o(1)
\]

with the base.  Splitting by which leg is selected therefore turns a linear family of
nearly fixed projective leg directions into a linear family of polygon bases with
projective directions in an `o(1)` interval.

One sentence should be made explicit at this point.  Projective closeness alone allows
oriented directions that differ by almost `pi`.  That alternative cannot occur here.
All retained bases lie on the single positive support arc, whose angular length is

\[
U_8=3\theta_8-2\pi<\pi.
\]

Along a convex polygon approximating that arc, the total variation of the oriented
boundary-side direction over the retained arc is `U_8+o(1)<pi`.  Consequently two
retained bases that are `o(1)`-close in `RP^1` are in fact `o(1)`-close as oriented
boundary directions; they cannot belong to the opposite lift separated by `pi-o(1)`.

After this lift is fixed, convex boundary direction is monotone.  Hence every boundary
side between the first and last of a linear set of selected bases also lies in the
same `o(1)` direction cone.  The intervening boundary subchain has length `Omega(D)`
and endpoint displacement `Omega(D)`.  After scaling, the subchain converges to a
positive-length straight segment in the boundary of the Hausdorff limit `K`.

That is impossible because its endpoints lie on the same strictly curved radius-1/2
support arc, and the intervening circular arc is also contained in `partial K` while
lying strictly outside its chord.  Thus the dispersion lemma is valid.

This is an expository clarification, not a repair to the theorem statement.

## 5. Canonical Section 90 can be rerun on this specific carrier

This is the most important dependency check.  Section 102 does not merely cite the
existence of some earlier Section-90 carrier; it reruns the local Section-90 argument
on the hypothetical endpoint carrier.  That rerun is legitimate.

Section 90 uses only the following three carrier-local estimates:

\[
R_D\ge rD^2,
\qquad
T_D\le C_TD,
\qquad
\sum_{R\subset P_D}\delta_R\le C_{phase}D.
\]

They all hold here:

- positive macroscopic area plus local rhombic filling gives `R_D=Omega(D^2)`;
- canonical Section 89, or the coarser canonical Section-82 boundary estimate, gives
  `T_D=O(D)`;
- the global canonical phase-defect budget is nonnegative and therefore remains
  `O(D)` when restricted to this cell.

The phase-circle cut in Section 90 removes crossing rhombi from the crossing graph; it
does not replace full physical local train segments by artificial cut fragments.
Thus the selected graph vertices are still full local train segments with two physical
boundary ends.

Section 90 then selects one unordered pair of distinct labels in `Z/3Z` and one
reduced-phase bin of width `O(1/D)`, leaving two linear train families.  If their
labels are distinct, their projective physical directions differ by

\[
\pi/3
\]

because a label difference of `2pi/3` is the same projective separation as `pi/3`.
Section 102's equation (102.26) is therefore correct.

Distinct local train segments of one phase family have distinct physical endpoint
edge occurrences.  A physical boundary edge is an end only of the train using that
edge direction.  Hence each linear train family contributes a linear number of
physical boundary endpoint occurrences, as required.

## 6. Linear endpoint mass must reach a complement corridor

For either selected phase family:

- only `o(D)` physical endpoints can lie against bounded nonquadrilateral faces;
- Lemma 102.1 permits only `o(D)` endpoints on the curved tooth arc;
- the remaining outer-face exceptional edges outside the three corridors and retained
  teeth have total count `o(D)`.

Therefore linearly many endpoints lie on the union of the three macroscopic
near-geodesic complement corridors.  Pigeonholing gives one corridor carrying
`Omega(D)` endpoints of that phase family.

No 2-connectivity or bridge-free hypothesis is being smuggled in.  Bridge-rich pieces
of a corridor simply contribute no rhombus-train endpoints; they cannot absorb the
linear endpoint mass being counted.

## 7. A near-geodesic corridor supports only its chord phase

For a corridor with unit route-edge vectors `z_j`, oriented chord direction `q_D`,
route length `ell_D`, and chord length `d_D`, projection gives exactly

\[
\sum_j(1-q_D\cdot z_j)=\ell_D-d_D=o(D).
\]

If `Omega(D)` route-edge occurrences from one phase family had limiting projective
direction separated from the chord by a fixed positive amount, each would contribute
a fixed positive projection loss.  The total loss would be `Omega(D)`, contradiction.
The opposite orientation of an undirected phase edge can only increase that loss.
Thus a corridor carrying linearly many endpoints of a phase family has the same
limiting projective direction as that family.

The two Section-90 phase families cannot use the same corridor, because their limiting
projective directions differ by `pi/3`.  Hence two distinct complement corridors would
have to be separated projectively by `pi/3`.

## 8. The explicit endpoint corridor angles contradict the phase pair

For complement gaps `(theta_8,phi_8,phi_8)`, the three chord directions have pairwise
projective separations

\[
\left\{\theta_8/2,\theta_8/2,\pi-\theta_8\right\}.
\]

Since `theta_8>2pi/3`,

\[
\theta_8/2>\pi/3,
\qquad
\pi-\theta_8<\pi/3.
\]

No pair differs by `pi/3`.  The numerical angular margin is fixed, not asymptotically
zero.  This contradicts the two-phase requirement and excludes the endpoint.

## 9. Compactness does give a uniform strict carrier gap

The final upgrade is also valid.  If no uniform `epsilon_*>0` existed, choose a
sequence of Type-II survivors for which every fixed-area macroscopic harmonic cell has
diameter below `(mu_8+o(1))D`.  Canonical square-root area control makes the number of
such cells uniformly finite after discarding cells of sufficiently small total area.
Pass to limits of the finite family.

Every wrapping limit below `mu_8` contradicts Section 101.  A wrapping limit at
`mu_8` contradicts the endpoint exclusion above.  Thus every macroscopic limit is cap
type.  The Section-88 laminar cap-family capacity at `mu_8` is strictly below the
diameter-one disk area, while the discarded small cells carry only a chosen small
fraction of that positive gap.  This contradicts the Type-II area identity.

Therefore there are absolute constants

\[
\epsilon_*>0,\qquad c_*>0
\]

such that every sufficiently large Type-II survivor contains a locally
rhombus-saturated harmonic cell of area at least `c_*D^2` and diameter at least
`(mu_8+epsilon_*)D`.

The argument is qualitative; it does not provide a numerical value of `epsilon_*`.

## 10. Disposition

**Audit verdict:** PASS.  Section 102 is suitable for the normal theorem-state
promotion transaction once its Section-101 dependency is canonical.  When the source
is next edited, add the projective-to-oriented lift sentence in Lemma 102.1 for maximum
clarity.

C-II remains open.  Section 102 improves the carrier threshold strictly beyond
`0.976040765267052D`, but it still does not force an exact unit equilateral triangle or
construct a source-preserving strict sub-`D` competitor.
