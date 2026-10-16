<!-- theorem-state: {"artifact_id":"ART-4CB7FB26E9AD","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — protected lattice exchange in an inactive chamber

**Date:** 2026-09-12
**Repository commit at start:** `7fd6982`
**State version:** `2026-09-12.audit.46`
**Run type:** closing proof / source-level competitor
**Target:** C-II, macroscopic internal inactive-chamber branch
**Starting status:** canonical inactive-chamber reduction, with the exchange obstruction recorded in proof-only Section 122
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md`
**External literature search:** not used
**Computation:** not used; the proof is finite convex geometry plus translation averaging

## LEVEL I STATUS

**STILL OPEN. C-II remains open.**

## 1. Starting canonical endpoint

The canonical chamber reduction gives an actual convex inactive chamber `C` whose
contact-isolated population `Z` has isolate-only Oler slack

\[
\sigma={\operatorname{area}(C)\over a_0}
       +{\operatorname{per}(C)\over2}+1-|Z|,
\qquad a_0={\sqrt3\over2},
\]

with `sigma=O(D)` and, on the macroscopic branch, `area(C)=Omega(D^2)`.
Proof-only Section 122 shows that a protected replacement of `Z` by one additional
point, after deleting one loaded contact vertex, would contradict the
contact-minimal normal form. The missing issue was a quantitative sufficient
condition guaranteeing such a protected replacement.

The implication tested here is

```text
large protected-chamber Oler slack
 -> a spacing-(1+eta) triangular-lattice replacement with |Z|+1 points
 -> delete one nonisolated contact vertex and preserve all source constraints
 -> strict contact-count decrease at the same global diameter
 -> contradiction to the contact-minimal triangle-free representative.
```

This does not assume that the chamber points themselves form a lattice and does not
delete contact-isolated points without replacing them.

## 2. Strongest genuinely new result

**Classification:** proved candidate, unreviewed and noncanonical.

### Theorem — protected lattice exchange

Let `A` be a contact-minimal triangle-free global minimizer of diameter `D`, with
`K=conv(A)`. Let `C` be a convex chamber and `Z subset A cap int(C)` satisfy:

1. every point of `A\Z` lies outside `int(C)`;
2. `C_{-lambda}:={x in C: dist(x,partial C)>=lambda}` is nonempty and is contained
   in `int(K)`; and
3. `lambda>1`.

Set `A_C=area(C)`, `P_C=per(C)`, `z=|Z|`, and

\[
\sigma={A_C\over a_0}+{P_C\over2}+1-z.
\]

If

\[
\boxed{
\sigma>
{A_C\over a_0}\left(1-{1\over\lambda^2}\right)
 +P_C\left({\lambda\over a_0}+{1\over2}\right)+2,
}
\tag{PLE.1}
\]

then no such chamber can occur in `A`.

In particular, for an internal macroscopic chamber in the canonical branch, take
`lambda=1+D^{-2}`. Since `area(C)<=pi D^2/4`, (PLE.1) implies the necessary
boundary-order restriction

\[
\boxed{
\sigma\le
\left({1\over a_0}+{1\over2}\right)P_C+O(1)
 =\left({2\over\sqrt3}+{1\over2}\right)P_C+O(1).
}
\tag{PLE.2}
\]

Thus the remaining macroscopic chamber branch is not merely an arbitrary `O(D)`
Oler-slack branch: its slack must be no larger than the cost of eroding one unit
depth from the chamber, up to a bounded lattice-scale term.

### Proof

Let `Lambda` be a triangular lattice of nearest-neighbor spacing `lambda`; its
fundamental-cell area is `a_0 lambda^2`. Translation averaging over one fundamental
cell gives a translate `Lambda+t` with at least

\[
|Y|\ge
\left\lfloor {\operatorname{area}(C_{-lambda})\over a_0\lambda^2}\right\rfloor
\tag{PLE.3}
\]

lattice points in `C_{-lambda}`. Distinct points of `Y` are at distance at least
`lambda>1`, so they create no unit contacts or unit triangles.

For any `a in A\setminus Z`, the segment from a point `y in C_{-lambda}` to `a`
meets `partial C` before it can leave `C`. Consequently

\[
|y-a|\ge dist(y,partial C)\ge lambda>1.
\tag{PLE.4}
\]

So `Y` is strictly unit-separated from every retained old point outside `Z`.

For a convex body, inner parallel perimeter is nonincreasing. Integrating the
perimeter of the inner parallel bodies gives

\[
area(C_{-lambda})
\ge A_C-lambda P_C.
\tag{PLE.5}
\]

Therefore (PLE.3) and the slack definition imply

\[
\begin{aligned}
|Y|-z
&\ge {A_C-lambda P_C\over a_0\lambda^2}-1
    -\left({A_C\over a_0}+{P_C\over2}+1-\sigma\right)\\
&=\sigma-{A_C\over a_0}\left(1-{1\over\lambda^2}\right)
 -P_C\left({lambda\over a_0}+{1\over2}\right)-2.
\end{aligned}
\tag{PLE.6}
\]

Under (PLE.1), `|Y|>=z+1`. Select a subset `Y' subset Y` with `|Y'|=z+1`.

The contact graph of `A'=(A\setminus(Z union {v})) union Y'` is triangle-free if
`v` is any nonisolated contact vertex: all old contacts not incident to `v` remain,
and (PLE.4) shows that no new unit contact is created. Choose such a `v`, which
exists for every nontrivial contact core. The source cardinality is unchanged.

All retained old points and all points of `Y'` lie in `K`; the latter lie in `int(K)`
by assumption. Hence `diam(A')<=diam(K)=D`. Since `A'` is an `n`-point unit-separated
configuration and `D=D(n)` is globally minimal, its diameter is exactly `D`.

Deleting `v` removes at least one old unit contact, while deleting `Z` removes none
and inserting `Y'` creates none. Thus `A'` has strictly fewer unit contacts than the
chosen contact-minimal triangle-free global representative, a contradiction.
This proves the theorem.

For `lambda=1+D^{-2}`, the first term on the right of (PLE.1) is `O(1)` because
`area(C)<=pi D^2/4`, while `lambda/a_0=1/a_0+O(D^{-2})`. This gives (PLE.2).
`square`

## 3. Exact frontier effect

This eliminates the high-slack subbranch of every internal macroscopic inactive
chamber for which (PLE.1) holds. It is a source-level strict same-cardinality
competitor, not a local contact-activation claim. It also supplies an exact split
for the remaining chamber obstruction:

```text
protected chamber with slack above the erosion threshold -> impossible;
protected chamber with slack at or below the erosion threshold -> still live.
```

The canonical `O(D)` slack bound does not currently give the strict inequality in
(PLE.1). The threshold coefficient is explicit and is not asserted to be sharp.
The result does not apply to exterior caps without a separate protected-cap
hypothesis, and it does not address the full-core branch.

## 4. Exact remaining lemma

The next useful theorem is a **boundary-conflict improvement**: replace the full
one-unit erosion in (PLE.5) by the actual union of unit neighborhoods of retained
source points on `partial C`, and prove that its area is strictly less than `P_C`
for the canonical chamber boundary. Such an improvement would lower the threshold
in (PLE.1) and may make the canonical `O(D)` slack bound incompatible.

The full C-II closure still needs either that improvement, a collective deformation
of the chamber together with its diameter-carrying core, or an independent closure
of the full-core aggregate detour branch.

## 5. Claim audit table

| Claim | Status | Dependencies | Reason |
| --- | --- | --- | --- |
| Translation-average lower bound (PLE.3) | proved candidate | elementary fundamental-cell averaging | exact finite lattice count |
| Inner-parallel area bound (PLE.5) | proved candidate | convex coarea/perimeter monotonicity | valid for convex chambers with nonempty erosion |
| Protected exchange (PLE.1) | proved candidate | PLE.3--PLE.5; contact-minimal normal form | explicit same-cardinality strict contact reduction |
| Canonical chamber has `sigma=O(D)` | canonical | `C-INACTIVE-CHAMBER`, Sections 77/80 | lifecycle controlled by audit.46 |
| Canonical chamber satisfies PLE.1 | unproved | none | the coefficient comparison is the live obstruction |
| C-II closure | open | PLE.1 or another source-level bridge | exterior caps and full-core branch remain |

## 6. Regression checks

| Regression/correction | Result | Exact hypothesis or failure |
| --- | --- | --- |
| Contact-isolated points retained | pass | `Z` is removed only together with `|Z|+1` replacement points |
| Full-source ZR/ZF misuse | pass | no stress or affine-kernel claim is made for `Z` |
| Simultaneous exchange compatibility | pass | all replacement points have spacing `lambda>1` and are at depth `lambda` |
| Boundary points of `K` | pass | replacement points are required to lie in `int(K)` |
| Triangle-free comparison class | pass | replacement points create no unit contacts |
| Global versus local optimality | pass | global minimality forces `diam(A')=D`; contact minimality gives the contradiction |

## 7. Literature imports

None.

## 8. Computation

No script is logically required. The only numerical specialization is the exact
choice `lambda=1+D^{-2}`; the proof uses the displayed symbolic inequality.

## 9. Corrections / supersessions

This result does not supersede Section 95. It strengthens the separate finite-exchange
obstruction by supplying a sufficient protected replacement criterion. It does not
revive the rejected claim that first contacts necessarily transfer positive KKT force.

## 10. Promotion recommendation

**unreviewed** — preserve as a proof-only source-level candidate. The theorem-state
manifest is unchanged because the canonical threshold needed for closure is not yet
proved.

## 11. Handoff

1. Strongest new theorem: (PLE.1), the explicit protected lattice-exchange threshold.
2. Canonical dependency chain: `C-INACTIVE-CHAMBER` / Section 77 and the contact-minimal
   normal form; proof-only finite-exchange audit in
   `research/target_c_section122_finite_exchange_saturation.md`.
3. Exact remaining lemma: improve the chamber boundary-conflict estimate enough to
   violate (PLE.1), or couple the protected chamber to the global diameter-carrying
   core.
4. Binding dead routes: KKT activation alone (Section 95), density-only arguments,
   and deletion of contact-isolated points.
5. Files to read next: `docs/targets/target-c/CURRENT.md`, Section 77, `docs/targets/target-c/80-global-isolate-concentration-fullcore-disk-audit.md`,
   and the finite-exchange audit before attempting a chamber/core coupling.
