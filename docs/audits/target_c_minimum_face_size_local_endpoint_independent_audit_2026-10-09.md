<!-- theorem-state: {"artifact_id":"ART-AA950DC3CAB0","canonical":true,"claim_ids":["C-QUARTER-FOLD-MINIMUM-FACE-SIZE"],"claim_statuses":{"C-QUARTER-FOLD-MINIMUM-FACE-SIZE":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit: boundary-local minimum face size for quarter-folds

**Date:** 2026-10-09. **Audit:** 229.
**Audit base:** `origin/main=a049689b13907387e058e4351d27ec63748cf853`, state `2026-10-09.audit.222`.
**Frozen source:** `origin/research/level-i-fused-review-20261009` at `6132201c1d3056ca68a222217094acb819f5b4d7`.
**Source report:** `docs/reports/target_c_small_convex_contact_face_quarter_fold_exclusion_2026-10-09.md`, SHA-256 `ec4bb6ac4e7c6096d7921074d1326c6ec55494d422d67cbff976637c55802f23`, Section 5.1.
**Prior audit:** Audit.222, `docs/audits/target_c_quarter_fold_minimum_face_size_independent_audit_2026-10-09.md`.

## Verdict

**PASS — broaden `C-QUARTER-FOLD-MINIMUM-FACE-SIZE` to boundary-local endpoint feasibility.** The prior result assumed all nonface labels were retained and the complete source endpoint was feasible. Its proof uses only the actual old face and the eight folded boundary labels. In particular, every nonconstant lower-feasible triangle-free fold on a simple convex actual face with at least five sides has four transition arcs of length at least two; an eight-sided such face has pattern `2,2,2,2`.

## Exact broadened statement

Let a finite unit-separated source contain a simple convex actual unit-contact face `F` with `m>=5` cyclic labels `p_i` and unit edge vectors `q_i=p_{i+1}-p_i`. Choose signs `s_i∈{−1,+1}` with nonconstant face-closed pattern, `sum_i s_iq_i=0`, and let folded boundary labels satisfy `U_{i+1}-U_i=s_iJq_i`, where `J(x,y)=(-y,x)`. Assume only that the `m` folded boundary labels are unit-separated and triangle-free; no other source label is required to remain fixed or feasible.

Then every transition arc has at least two edges. Thus `m>=8`; if `m=8`, all four transition arcs have exactly two edges. Consequently, for `m=5,6,7`, a boundary-feasible triangle-free face fold must be constant.

## Independent reconstruction

Canonical `C-QUARTER-FOLD-CONVEX-FACE-CLASSIFICATION` applies at this boundary-local scope. It gives exactly four transition vertices for a nonconstant pattern, and those actual vertices form an inscribed parallelogram. Opposite transition arcs therefore have equal endpoint chords.

Suppose one transition arc has a single edge. Its chord has length one. The opposite arc has the same chord; if that opposite arc had at least two edges, its endpoints would be nonconsecutive actual face vertices and their unit chord would split the old face. Therefore the opposite arc also has one edge. If both opposite pairs had one edge, the whole face would have four edges, contrary to `m>=5`. Thus, if a one-edge pair exists, it is the only such pair and the remaining two opposite arcs each have at least two edges.

Write the transition parallelogram as

\[
a=0,\qquad b=Lt,\qquad d=v,\qquad c=Lt+v,
\]

where `t,v` are unit vectors meeting at angle `gamma`. The two one-edge arcs are the opposite sides `ad` and `bc`, so `|v|=1`; the two longer arcs run from `a` to `b` and from `d` to `c`. By convexity, their first unit edges have the form

\[
e=(\cos\alpha)t-(\sin\alpha)Jt,\qquad
f=(\cos\beta)t+(\sin\beta)Jt,
\]

with `alpha,beta>=0`.

At every transition, the old two-edge chord has length `2cos(tau/2)` and is strictly longer than one: equality would be an actual contact chord inside the old face. The sign change makes the folded exterior turn supplementary to `tau`; the folded two-edge chord is `2sin(tau/2)`. Boundary lower-feasibility and triangle-freeness force this chord to be strictly longer than one, since equality would form a unit triangle. Hence each old transition turn lies in `(pi/3,2pi/3)`.

At `a` and `d`, the old turns are `pi-gamma-alpha` and `gamma-beta`. Their lower bounds give

\[
\pi/3+\beta<\gamma<2\pi/3-\alpha.
\]

Put `delta=(alpha+beta)/2` and `d0=(beta-alpha)/2`. These inequalities imply `0<=delta<pi/6` and

\[
\pi/3+\delta<\gamma-d0<2\pi/3-\delta.
\]

Undo the common quarter-turn. Up to reversing all signs, the two longer arcs have positive signs and the one-edge arcs have negative signs. The bottom long arc stays in place and the top long arc translates by `-2v`. The two first internal boundary labels in the folded endpoint therefore differ by `f-e-v`, and direct expansion gives

\[
|f-e-v|^2=1+4\sin^2\!\delta-4\sin\delta\sin(\gamma-d0).
\]

If `delta>0`, then `sin(gamma-d0)>sin(delta)`, so this squared distance is strictly less than one. That contradicts lower-feasibility of the folded boundary labels. If `delta=0`, then `alpha=beta=0`; the two old first internal labels are separated by the unit vector `v`. They are nonconsecutive vertices of the old actual face, again impossible. Thus no transition arc has one edge.

There are four arcs, each with at least two edges, proving `m>=8`. Equality at `m=8` forces all four lengths to equal two.

## Hostile checks and scope

- **Quadrilateral exception:** the theorem assumes `m>=5`; the exact rectangular four-face regression is outside scope and does not contradict it.
- **Eight-face sharpness:** I re-enumerated the canonical rational eight-cycle after scaling by 41. Integer cross products on the old boundary are all positive (minimum 720); all 28 old and folded pair distances give exactly eight unit contacts and no triangles, with minimum noncontact squared distances `4802/1681` and `1922/1681`, respectively. The signed edge sum is zero, and every folded edge is exactly `s_iJq_i`. This confirms a nonconstant locally feasible boundary fold at `m=8`, so the threshold is sharp. The folded polygon need not be convex; only the old boundary is the actual convex face. The example is nonglobal and proves no source-level fold exists.
- **Moving outside labels:** none are used in the proof. The boundary-local premise is exactly what is needed for the collision and triangle tests.
- **Upper/global hypotheses:** no diameter upper ledger, source globality, contact-minimality, or stress hypothesis is used.

No finite verifier encodes the analytic one-edge exclusion. The existing rational example is a separate finite sharpness check, not a proof of the universal statement.

## Dependencies and frontier effect

The only theorem dependency is canonical `C-QUARTER-FOLD-CONVEX-FACE-CLASSIFICATION`. It supplies the four-transition parallelogram under the same boundary-local endpoint premise. The proof does not use `C-QUARTER-FOLD-EIGHT-FACE-AREA-LOWER-BOUND` or any source-wide endpoint fact.

This scope extension makes the four-two-edge pattern available for every nonconstant eight-face whose transformed boundary is lower-feasible and triangle-free. Combined with Audit.228's local hull cover, such a face cannot hold an isolate inside its transformed hull. It still provides no full integrated endpoint, outside placement, outer-capacity estimate, C-II closure, or Level-I consequence.
