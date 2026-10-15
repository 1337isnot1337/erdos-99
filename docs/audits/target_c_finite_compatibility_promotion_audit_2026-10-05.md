<!-- theorem-state: {"artifact_id":"ART-2018D5B086C9","canonical":true,"claim_ids":["C-ACTUAL-CUT-FINITE-BARRIER-REGRESSION","C-DISJOINT-SWAP-2SAT","C-LONG-PAIR-ISOLATE-DISPATCH"],"claim_statuses":{"C-ACTUAL-CUT-FINITE-BARRIER-REGRESSION":"regression","C-DISJOINT-SWAP-2SAT":"canonical","C-LONG-PAIR-ISOLATE-DISPATCH":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"mixed","target":"target-c"} -->
# Independent promotion audit — Target C finite compatibility, isolate dispatch, and cut-barrier regression

**Date:** 2026-10-05  
**Audit base:** \`ad8809fd96c2c0af9a6de4d965e9ab33efe092c6\`  
**Starting theorem state:** \`2026-10-05.audit.59\`  
**Target:** C-II / finite source-motion compatibility  
**Verdict:** **PASS for two canonical finite theorems and one binding regression.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This audit promotes:

1. \`C-LONG-PAIR-ISOLATE-DISPATCH\` — canonical;
2. \`C-DISJOINT-SWAP-2SAT\` — canonical;

and registers:

3. \`C-ACTUAL-CUT-FINITE-BARRIER-REGRESSION\` — regression.

The promotion is deliberately narrower than the source reports. Their conditional TB1/open-cell/O–O applications remain unreviewed unless separately promoted. The finite theorems below require no such phase-extraction input.

## 1. Long-pair geometry is a full-source thrackle

Audited source:
\`docs/reports/target_c_forest_isolate_dispatch_2026-10-01.md\`.

Let \(A\) be the canonical contact-minimal, then diameter-pair-minimal triangle-free global source of diameter \(D>1\). Let \(V\) be its nonisolated positive-contact core and \(Z=A\setminus V\). Let \(H\) be the actual diameter graph on its endpoint set \(B\), with
\[
q=|B|,\qquad h=|E(H)|,\qquad d_H=q-h.
\]

Put
\[
L=\sqrt{D^2-1},
\qquad
\gamma=D-L=\frac1{D+\sqrt{D^2-1}}.
\]

Define the full-source long-pair graph \(T\) by
\[
xy\in E(T)\iff |x-y|>L.
\]

### 1.1 Every long-pair endpoint is extreme

If \(p\) is not extreme, write
\[
p=\sum_i\lambda_i a_i
\]
as a nontrivial convex combination of other source points. For any \(q\in A\),
\[
|p-q|^2
=
\sum_i\lambda_i|a_i-q|^2
-
\sum_i\lambda_i|a_i-p|^2.
\]
Unit separation makes the second sum at least one, while all first terms are at most \(D^2\). Hence
\[
|p-q|^2\le D^2-1=L^2.
\]
So no nonextreme point is incident with \(T\).

### 1.2 \(T\) is a straight-line thrackle

Take two disjoint long edges. Their four endpoints are extreme and form a strictly convex quadrilateral. If the two long edges did not cross, they would be opposite sides. Some quadrilateral angle is at least \(\pi/2\). At that angle one incident side is long and the other source side has length at least one, so the opposite diagonal has squared length
\[
>L^2+1=D^2,
\]
contradicting the source diameter.

Distinct incident long edges cannot overlap because all their endpoints are extreme.

Thus \(T\) is a finite straight-line thrackle. The canonical Woodall classification therefore applies to its abstract graph: \(T\) is either a caterpillar forest or a connected odd-unicyclic graph with pendant leaves.

### 1.3 New long-pair endpoints are actual contact isolates

Every \(T\)-endpoint outside the actual diameter endpoint set \(B\) is contact-isolated.

Indeed, a nonisolated non-diameter point in the canonical relative-interior KKT normalization has positive contact coefficients and no diameter force. Vertex equilibrium expresses it as a positive weighted barycenter of its contact neighbors, so it cannot be extreme. This contradicts Section 1.1.

This argument stays entirely inside the nonisolated-core convention and does not extend the §57 affine-kernel theorem to isolates.

## 2. Fixed isolate dispatch leaves at most \(d_H\) upper exceptions

The promoted theorem is finite and source-wide.

There is a fixed exceptional edge set
\[
E\subseteq E(T)\setminus E(H)
\]
and a fixed assignment sending each contact isolate either to an anchor in \(B\) or to “unanchored,” such that:

- if \(H\) is cyclic, \(E=\varnothing\);
- if \(H\) is a forest and \(T\) is a forest,
  \[
  |E|\le d_H-1;
  \]
- if \(H\) is a forest and \(T\) is odd-unicyclic,
  \[
  |E|\le d_H.
  \]

### 2.1 Forest partition

If \(H\) is a forest, it has exactly \(d_H\) nontrivial components by canonical \`C-WOODALL\`.

If \(T\) has an odd cycle, remove one cycle edge outside \(H\); \(H\) itself is acyclic, so such an edge exists. Now \(T\) is a forest.

Contract each \(H\)-component to a marked root. In every tree, partition the remaining vertices into connected regions each containing at most one marked root. A tree containing \(a\) roots requires exactly \(a-1\) cuts. Summed globally this costs at most \(d_H-1\) additional edges.

After expanding \(H\), every component of \(T\setminus E\) contains at most one \(H\)-component.

Every isolate-only branch attached to that \(H\)-component has a unique attachment vertex \(b\in B\): two attachments would create a cycle using the \(H\)-path between them. Assign every isolate in the branch to that anchor. Components containing no \(B\)-vertex remain unanchored.

Hence every long inactive pair outside \(E\) either has both endpoints assigned to one anchor or both endpoints unanchored.

In the cyclic \(H\) branch, Woodall plus the straight-line edge bound makes every \(T\)-vertex outside the unique old odd cycle a pendant leaf attached to one cycle vertex; no exceptional edge is needed.

## 3. Exact full-source extension of any sufficiently small binary core move

Let
\[
p\mapsto p+f(p)\Delta,
\qquad
f:V\to\{0,1\},
\qquad
s=|\Delta|<\gamma.
\]

Extend it to every source point by moving each anchored isolate exactly with its anchor and leaving unanchored isolates fixed.

Then:

- all old contacts involving isolates are vacuous because isolates have no old contacts;
- every inactive long pair outside \(E\) is unchanged;
- every other inactive pair starts at length at most \(L\), and its relative displacement has norm at most \(s\), so its final length is
  \[
  <L+\gamma=D.
  \]

Therefore **only** pairs in \(E\) can create a new upper-diameter equality or violation.

Assume the core move preserves every old contact, weakly shortens all old diameter pairs, and strictly shortens at least one. Canonical global/contact/diameter-pair minimality then forces one of two finite endpoint obstructions:

\[
\boxed{
1<|xy|\le1+s,
\qquad
|x'-y'|\le1,
}
\]
for a previously strict lower pair, or
\[
\boxed{
xy\in E,
\qquad
|x'-y'|\ge D.
}
\]

If neither occurred, every old noncontact would remain strict and every old nondiameter would remain below \(D\). The endpoint would either have diameter below \(D\), or would have the same diameter and contact count but strictly fewer diameter pairs. Both contradict the canonical normalization.

This is an endpoint theorem. It does not assert feasibility along a straight interpolation.

### 3.1 Simultaneous counting

For \(r\) such proposals with pairwise disjoint moving core sets and common amplitude bound \(s_*<\gamma\), use the same \(E\) and isolate assignment.

Each source point moves in at most one proposal, hence any fixed pair changes in at most two proposals. Therefore at most \(2|E|\) proposals can be blocked only by exceptional upper pairs. Each surviving proposal supplies a near-unit lower witness, and one witness can serve at most two proposals.

Thus
\[
\boxed{
N_1
\ge
\max\{0,\lceil r/2\rceil-|E|\}.
}
\]

In particular
\[
N_1\ge\max\{0,\lceil r/2\rceil-d_H\}
\]
in every forest branch, while the cyclic branch has \(E=\varnothing\).

### 3.2 Fractional lower repair becomes a shortest-path certificate

The report's fractional refinement is also valid at finite scope.

For an unanchored isolate variable \(\lambda\in[0,1]\), let \(r=b-a\) be a previously strict noncontact and assume
\[
p=r\cdot\Delta>0,
\qquad
g=|r|^2-1>0.
\]
The sufficient strict-lower constraint
\[
\lambda_a-\lambda_b
\le
c_{ab}:=\frac{g}{2p}
\]
guarantees
\[
|r-(\lambda_a-\lambda_b)\Delta|>1.
\]

Orient each such constraint \(a\to b\) with cost \(c_{ab}\). Prescribe the core/anchored values \(0\) or \(1\).

The entire system is feasible **iff** no directed path from a prescribed-1 node to a prescribed-0 node has total cost \(<1\).

Necessity follows by summing constraints. Conversely, with \(d(x)\) the shortest-path distance from the prescribed-1 set,
\[
\lambda_x=\max\{0,1-d(x)\}
\]
satisfies every difference constraint, fixes all prescribed-1 nodes at one, and fixes prescribed-0 nodes at zero precisely when no such path has cost below one.

So after upper dispatch, failure of this conservative lower repair has an exact weighted-path certificate rather than an unspecified “blocker cloud.”

### 3.3 Sharpness of the upper exception

The rational three-point packet in the source report has \(D=8\), a tree diameter graph with \(d_H=1\), and a long-pair graph \(T\) that is a triangle. A sufficiently small move strictly shortens one old diameter while making the one inactive long pair exceed \(D\).

Therefore the forest exception budget cannot in general be replaced by \(E=\varnothing\), even at ultrasmall amplitude.

The exact forest verifier was rerun independently and passed:

- 10,524 graph packets;
- 143,852 binary anchor-label checks;
- the rational one-exception source;
- 59,808 weighted-difference packets;
- the collinear total-slack regressions for lengths \(2,10,100\).

**Verdict:** canonical-ready for Sections 1--8.2 of the source report. The later O--O/block-transposition specializations remain unreviewed.

## 4. Exact simultaneous finite moves compile to 2-SAT

Audited source:
\`docs/reports/target_c_simultaneous_disjoint_swaps_exact_2sat_2026-10-01.md\`.

Let \(A\) be any finite unit-separated source of diameter \(D\). Let
\[
L_1,\ldots,L_k
\]
be pairwise disjoint moving subsets with prescribed translations
\[
\Delta_1,\ldots,\Delta_k.
\]

For a binary assignment \(x\in\{0,1\}^k\), move every point of \(L_i\) by \(x_i\Delta_i\), fixing every other source point.

Assume every old unit contact remains exactly unit for **every** binary assignment.

For each source pair \(pq\), its final squared distance depends on at most the two variables owning its endpoints.

Call an assignment strict-inactive admissible when:

- every old contact stays exactly unit;
- every old noncontact stays strictly above one;
- every old diameter pair stays at most \(D\);
- every old nondiameter pair stays strictly below \(D\).

For every local endpoint state violating one of these inequalities, forbid that local binary pattern. A bad two-variable state
\[
(x_i,x_j)=(a,b)
\]
becomes the clause
\[
(x_i\ne a)\lor(x_j\ne b),
\]
and a bad one-variable state becomes a unit clause.

Thus all full-source pair constraints compile **exactly** to a 2-CNF formula \(F\).

### 4.1 Exactness

\[
\boxed{
x\models F
\iff
x\text{ is strict-inactive admissible}.
}
\]

No geometric approximation enters this equivalence: every bad local pair state is forbidden, and no third variable can affect that pair's distance.

Moreover there exists an admissible assignment shortening at least one old diameter iff, for some old diameter and one of its at most four locally shortening states, the corresponding pinned 2-CNF instance is satisfiable.

Hence the complete finite search needs at most \(4|H|\) pinned 2-SAT solves.

If all source and displacement coordinates are exact, every clause and every satisfiability certificate is exact.

### 4.2 Canonical consequence

In the canonical contact-minimal, diameter-pair-minimal global representative, no such pinned shortening instance is satisfiable.

Indeed, a satisfying assignment:

- preserves cardinality;
- preserves the exact old contact graph;
- creates no new contact;
- creates no new diameter pair;
- weakly shortens all old diameters;
- strictly shortens at least one.

If all old diameters shorten, global diameter drops below \(D\). Otherwise the endpoint remains a diameter-\(D\) global minimizer with the same contacts but fewer diameter pairs. Both contradict the canonical normalization.

Thus every proposed disjoint binary finite-motion family has an exact finite obstruction certificate in the implication graph.

### 4.3 Inactive clauses are automatically near-active for small moves

If every
\[
|\Delta_i|\le s,
\]
then changing one local binary state changes a pair distance by at most \(2s\). Therefore:

- every lower-bound clause comes from an old pair with
  \[
  1<|pq|\le1+2s;
  \]
- every inactive upper-bound clause comes from an old pair with
  \[
  D-2s\le|pq|<D.
  \]

This converts the compatibility problem into an exact finite Boolean system supported only on near-unit, near-diameter, and active-diameter source pairs.

The report's repeated two-phase TB1 return theorem requires additional unpromoted strip geometry and is **not** promoted here.

The exact 2-SAT verifier was rerun independently and passed:

- five exact source/move packets;
- all 176 two-variable clause systems with up to three clauses;
- all 4,096 three-variable Horn systems;
- the non-contact-preserving rejection packet.

**Verdict:** canonical-ready for Sections 1--4.

## 5. Regression: active cut data alone do not rule out a strict finite competitor

Audited source:
\`docs/reports/target_c_actual_cut_finite_competitor_regression_2026-10-01.md\`.

For every real \(D\ge13\), the report constructs an exact 16-point unit-separated source with:

- exactly three old unit contacts forming a chain;
- exactly six actual diameter pairs;
- actual nested contact cuts;
- a full-rank three-coordinate old-diameter derivative matrix;
- positive aggregate transverse/axial cut identities;
- a genuine convex diameter matching.

A finite move preserves exactly the old three-edge contact graph and produces a same-cardinality source with diameter strictly below \(D\).

At \(D=13\),
\[
D_{\rm new}^2
=
\frac{28248541}{167281}
=
169-\frac{21948}{167281}
<169.
\]

All 120 source-pair lower and upper inequalities are certified by rational quadratic polynomials valid on the entire real ray \(D\ge13\), not by numerical sampling.

The packet is not a global minimizer and intentionally fails full-source positive KKT equilibrium: every diameter endpoint is contact-isolated with one diameter edge, so its positive diameter force cannot balance.

Therefore the following implication is false:

> actual source cutsets + actual diameter vectors + convex-thrackle geometry + full rank of the selected active derivative matrix + positive aggregate cut identities  
> \(\Longrightarrow\) no strict finite source competitor.

A closing finite-motion theorem must use genuinely canonical information such as full vertex KKT equilibrium, the positive-contact core/train embedding, or exact full-source inactive constraints.

The verifier was rerun independently and passed the entire 16-point real-\(D\ge13\) source family, all 120 pair inequalities, and the exact strict competitor.

**Verdict:** register as regression.

## 6. Effect on the live audit.59 frontier

Audit.59 says strict-safe area averaging cannot repair the finite blockers left by audit.58.

Audit.60 replaces part of that vague blocker picture by two exact finite systems.

For any sufficiently small binary contact-preserving core translation:

- all contact isolates can be dispatched so that only a fixed set of at most \(d_H\) inactive long pairs can create upper-diameter trouble;
- every other failed canonical move must create an explicit near-unit lower blocker;
- for a family of disjoint such proposals, near-unit witnesses accumulate except for the \(d_H\)-sized upper exception budget;
- fractional isolate repair fails only by an explicit short weighted path from a moving-one anchor to a moving-zero anchor.

For any finite family of pairwise disjoint translation packets:

- full-source compatibility is exactly a 2-SAT problem;
- every pinned diameter-shortening attempt is unsatisfiable in a canonical survivor;
- at small amplitude every clause lies on an actual near-unit, near-diameter, or active-diameter source pair.

The next high-value theorem is therefore not another mean-area refill estimate. It is an **implication-path / weighted-path exclusion theorem** using canonical KKT/train/loaded-return geometry, or a construction of a satisfying assignment from the many disjoint local motions already supplied by the audit.58 stack.

**Promotion recommendation:** advance theorem state to \`2026-10-05.audit.60\`, register the two finite theorems as canonical, and register the exact active-cut packet as a regression.
