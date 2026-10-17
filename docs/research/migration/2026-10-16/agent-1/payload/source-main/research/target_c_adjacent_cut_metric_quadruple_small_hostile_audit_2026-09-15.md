# Hostile audit — metric quadruple-small adjacent O--O pair

**Date:** 2026-09-15  
**Reviewed:**
- `research/target_c_adjacent_cut_metric_quadruple_small_2026-09-15.md`
- `research/verify_target_c_adjacent_cut_metric_quadruple_small.py`
- hostile-audited triple-small adjacent-cut theorem

**Disposition:** **PASS at proof-only `t<=1.844` full-core Type-II scope.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The candidate adds one new quantity to the already-audited three-budget adjacent-cut
averaging: arclength along the common center train between successive selected leaf
crossings.  The audit therefore concentrates on whether the asserted total arclength
budget

\[
\sum_i\ell_i<{2D\over\sqrt3}
\]

is exact and whether it can be averaged on the same adjacent boundaries without
multiplicity loss.

---

## 1. One strict-rhombus train segment has length exactly one

Fix a stopped train with unit contact-edge direction `u`.  In one strict unit rhombus
that the train traverses, its centerline joins the midpoints of the two opposite
`u`-edges.  If the other side vector is `v`, then those two midpoints differ by exactly
`v`.  Hence

\[
|v|=1.
\]

There is one such centerline segment for every rhombus link in the train.  Therefore a
train traversing `R_gamma` strict rhombi has total midpoint-centerline arclength exactly

\[
R_\gamma.
\]

There is no extra terminal segment beyond the midpoint of the terminal train edge, so
no hidden `+1` appears.

**Verdict:** PASS.

---

## 2. Every train segment advances by more than `sqrt(3)/2` in one fixed height

Orient the train so

\[
h_u(p)=\det(u,p)
\]

increases.  The other side vector `v` in any traversed strict unit rhombus has oriented
angle in

\[
(\pi/3,2\pi/3).
\]

This is exactly the audited triangle-free unit-rhombus angle range.  Thus

\[
h_u(p+v)-h_u(p)=\det(u,v)>{\sqrt3\over2}.
\]

The sign is coherent along the complete stopped train by the canonical monotone train
orientation; it is not re-chosen independently in each rhombus.

**Verdict:** PASS.

---

## 3. The available height range is at most the source diameter

Every endpoint of a centerline segment is the midpoint of a source contact edge.  It
therefore lies in `conv(A)`.  The convex hull has the same diameter as the finite source,
namely `D`.

The linear functional `h_u` has unit Lipschitz constant because `|u|=1`.  Hence for any
two points of `conv(A)`,

\[
|h_u(p)-h_u(q)|\le|p-q|\le D.
\]

Summing the strict height advances over all `R_gamma` rhombi gives

\[
R_\gamma{\sqrt3\over2}<D.
\]

Therefore

\[
\boxed{
\operatorname{len}(\gamma)=R_\gamma<{2D\over\sqrt3}.
}
\]

This is finite and does not require near-disk geometry.

**Verdict:** PASS.

---

## 4. Successive selected leaf crossings spend disjoint centerline subarcs

The triple-small parent theorem constructs its leaf path by traversing one center train
`gamma` through the complement-dual tree.  Thus `tau_1,...,tau_m` are listed in the
same order in which `gamma` crosses them.

A crossing of two stopped trains occurs in one strict rhombus and their centerline
segments meet at that rhombus center.  Distinct leaf trains cannot cross the same center
train in the same rhombus, because one rhombus contains exactly the two train classes
formed by its opposite edge pairs.  The crossing points `x_1,...,x_m` are therefore
distinct and occur monotonically along `gamma`.

The subarcs from `x_i` to `x_{i+1}` have pairwise disjoint interiors and concatenate
inside the subarc from `x_1` to `x_m`.  Consequently

\[
\sum_{i=1}^{m-1}\ell_i
\le\operatorname{len}(\gamma)
<{2D\over\sqrt3}.
\]

Half-rhombus pieces at the first and last selected crossing are automatically included
in arclength and only make the inequality weaker; there is no integer-rounding issue.

**Verdict:** PASS.

---

## 5. The four costs really live on the same boundary index

For each internal backbone boundary the candidate defines

\[
T_i=N_i+DB_i+D(a_i+a_{i+1})+100\ell_i.
\]

All four terms are nonnegative and indexed by the same adjacent pair
`(tau_i,tau_{i+1})`.

The inherited global budgets are

\[
\sum_iN_i\le2\pi D+o(D),
\]

\[
\sum_iB_i\le2+o(1),
\]

and

\[
\sum_j a_j\le {C_{phase}\over d_{low}}+o(1).
\]

Since

\[
\sum_{i=1}^{m-1}(a_i+a_{i+1})
\le2\sum_{j=1}^m a_j,
\]

the phase term spends no more than the parent triple-small proof.  Section 4 above gives
the new arclength budget.  Hence

\[
\sum_iT_i
\le
\left(2\pi+2+{2C_{phase}\over d_{low}}+{200\over\sqrt3}\right)D+o(D).
\]

The path has `m>pD-o(D)`, so `m-1=pD-o(D)` as well.  Dividing by the number of internal
boundaries is therefore asymptotically legitimate.

**Verdict:** PASS.

---

## 6. Exact constant certificate passes in Pyroam

The companion script uses only exact `Fraction` arithmetic and the same outward bounds
as the existing stack:

\[
\pi<{355\over113},
\qquad
\sqrt3<{17321\over10000},
\qquad
\sqrt3>{433\over250}.
\]

It was independently executed in Pyroam and returned

```text
PASS: metric quadruple-small adjacent pair
path density p = 0.0035641799199485342
base three-budget average = 21175.903313762472
train arclength coefficient upper = 1.1547344110854503
combined average = 53574.223180345536
54000 slack = 425.7768196544612
arclength bound = 535.7422318034554
540 arclength slack = 4.257768196544612
```

The new rounding margins are therefore hundreds of units for the combined cusp constant
and more than four units for the arclength bound.  No floating-point sign is
load-bearing.

**Verdict:** PASS.

---

## 7. Resultant and Euclidean-distance consequences are safe

The parent rooted interval theorem gives

\[
\|F_{i+1}-F_i\|\le DB_i.
\]

Thus the selected boundary with `T_i<54000+o(1)` satisfies the advertised resultant
bound.  Reverse triangle inequality gives the scalar resultant bound.

For crossing centers,

\[
|x_{i+1}-x_i|
\le\operatorname{len}_\gamma[x_i,x_{i+1}]
=\ell_i,
\]

so the arclength estimate also gives Euclidean separation `<540+o(1)`.

The theorem correctly does **not** infer that the entire dual strip between the two
O--O cuts has bounded diameter.  Only one actual transversal path is controlled.

**Verdict:** PASS.

---

## 8. Local-jamming warning remains binding

The theorem weakens the previous algebraic constant `21200` to `54000` in exchange for
bounded metric separation.  It does not alter the KKT stationarity fact that no nonzero
exact train-shear direction is first-order diameter-feasible componentwise.

Thus the bounded corridor cannot be used by simply ignoring the switching cusps.  A
valid downstream argument must use a finite/nonlocal replacement, allow controlled
contact breaking, or derive an impossible geometric arrangement of the switching
diameter chords.

This limitation is stated explicitly in the candidate.

**Verdict:** PASS.

---

## Final disposition

The fourth metric budget is exact and compatible with all three previously audited
adjacent-cut costs.  Therefore the live branch contains one adjacent O--O pair that is
simultaneously

```text
O(1) switching diameter rows
+ O(1/D) switching beta mass
+ O(1/D) projective phase gap
+ O(1) center-train transversal arclength.
```

With the safe rounded package, the constants are `54000, 54000/D, 54000/D, 540`.

**Final verdict:** PASS at proof-only `t<=1.844` full-core Type-II scope. C-II and Level I remain open.
