<!-- theorem-state: {"artifact_id":"ART-F3CF8901C039","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — ZRI: almost every bulk rhombus has two vanishing-stress transverse sides

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-deep-harmonic-capture`  
**Run type:** rhombic-bulk / radial-path-forest coupling  
**Target:** Target C, ZCQ branch  
**Depends on:** ZCQ, ZRP, C42/C51; reconciled with current-main PI/GU  
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

ZCQ forces a quadratic force-visible core in the sublinear-reset bridge branch. C42 then gives a quadratic number of strict unit-rhombus faces. ZRP says all but `o(D^2)` contact stress lies on a strongly-radial path forest `C_rad`.

At any vertex other than the center `z`, one inward and one outward strongly-radial contact meet at angle strictly greater than `135 degrees`, while every strict unit-rhombus interior angle lies strictly between `60` and `120 degrees`. Therefore **two strongly-radial edges can never be adjacent on a strict rhombus**.

Consequently every strict rhombus away from `z` has at least two nonradial boundary edges; if it has two radial edges, they are opposite. Since the nonradial edges carry only `o(D^2)` total stress, all but `o(D^2)` bulk rhombi have at least two nonradial sides whose KKT stresses tend uniformly to zero along a suitable scale.

Current main's PI theorem has meanwhile raised the universal force-hull area floor to `0.4978566363...D^2` and the GU low-surplus threshold to `0.7961725673...D`. Those stronger constants do not numerically contradict ZCQ for arbitrary fixed bridge fraction `eta`; the new ZRI endpoint remains a genuine geometric/stress incompatibility problem rather than a scalar constant comparison.

---

## 1. Quadratic strict-rhombus population

ZCQ gives, for fixed bridge fraction `eta>0`,

\[
 v\ge c_\eta D^2-o(D^2)
\tag{1.1}
\]

with `c_eta>0`.

C42 gives

\[
F_4\ge v-O(D),
\tag{1.2}

where `F_4` is the number of bounded quadrilateral contact faces. Every such face is a strict unit rhombus. Therefore

\[
\boxed{
F_4\ge c_\eta D^2-o(D^2).
}
\tag{ZRI1}

Only `O(1)` rhombi can be incident to the distinguished center `z`, because `deg_C(z)<=3`. They are discarded below.

---

## 2. Angle separation of two strongly-radial contacts at one vertex

Let

\[
c_*:=\cos15^\circ.
\]

A contact `uv` is strongly radial when

\[
\bigl||u-z|-|v-z|\bigr|>c_*.
\]

Fix `v!=z`, put `r=|v-z|>=1`, and suppose `u` is a smaller-radius strongly-radial neighbor. With

\[
d=r-|u-z|>c_*,
\]

ZRP computes the inward radial projection

\[
n_{in}\cdot(u-v)
=d+\frac{1-d^2}{2r}
\ge d
>\cos15^\circ.
\tag{2.1}
\]

Thus the ray `vu` lies within strictly less than `15 degrees` of the inward radial ray.

Now suppose `w` is a larger-radius strongly-radial neighbor and put

\[
d'=|w-z|-r>c_*.
\]

ZRP computes the outward radial projection

\[
n_{out}\cdot(w-v)
=d'-\frac{1-d'^2}{2r}.
\tag{2.2}

For `r>=1` and `d'>c_*`, this is larger than

\[
c_*-\frac{1-c_*^2}{2}
>\frac{\sqrt3}{2}.
\tag{2.3}

Hence `vw` lies within strictly less than `30 degrees` of the outward radial ray.

The inward and outward radial rays are opposite. Therefore the smaller angle between the two contact rays `vu` and `vw` is strictly larger than

\[
180^\circ-15^\circ-30^\circ
=135^\circ.
\tag{2.4}
\]

Thus:

### Lemma ZRI.1 — radial pair angle gap

At every vertex `v!=z`, if two strongly-radial contacts meet at `v`, their angle is strictly greater than `135 degrees`.

ZRP already proves there can be at most one inward and at most one outward strongly-radial neighbor, so this covers every possible pair.

---

## 3. A strict rhombus has at most two radial sides, and they are opposite

Every bounded quadrilateral contact face is a nondegenerate unit rhombus. Unit separation makes both diagonals strictly larger than one, so every interior angle lies strictly between

\[
60^\circ
\quad\text{and}\quad
120^\circ.
\tag{3.1}

Take a strict-rhombus face not incident to `z`. If two of its adjacent sides were strongly radial, they would meet at a face vertex `v!=z`. Lemma ZRI.1 would make their angle greater than `135 degrees`, contradicting (3.1).

Therefore no two adjacent boundary sides of the rhombus belong to `C_rad`.

A four-cycle with no adjacent selected edges contains at most two selected edges, and if there are two they are opposite. Hence:

### Theorem ZRI.2 — exact radial pattern in one rhombus

Every strict-rhombus face not incident to `z` has

\[
\boxed{
|E(F)\cap C_{rad}|\le2,
}
\tag{ZRI2}

and if equality holds, the two radial sides are opposite.

Equivalently, every such rhombus has at least two boundary contacts in

\[
E_{nr}:=C\setminus C_{rad}.
\]

---

## 4. Quadratic nonradial edge population with the sharp face-incidence factor

Count incidences `(F,e)` where `F` is a strict-rhombus face not incident to `z` and `e in E_nr` lies on its boundary.

By ZRI2 every such face contributes at least two incidences. Every plane contact edge is incident to at most two bounded faces. Hence

\[
2(F_4-O(1))
\le2|E_{nr}|.
\]

Therefore:

### Corollary ZRI.3 — quadratic transverse-edge population

\[
\boxed{
|E_{nr}|
\ge
F_4-O(1)
\ge
c_\eta D^2-o(D^2).
}
\tag{ZRI3}

---

## 5. The nonradial population has negligible total stress

ZRP/C68 gives

\[
\boxed{
\sum_{e\in E_{nr}}\alpha_e=o(D^2)
}
\tag{5.1}

under `D epsilon->0`.

Combined with ZRI3,

\[
\boxed{
\frac1{|E_{nr}|}\sum_{e\in E_{nr}}\alpha_e=o(1).
}
\tag{ZRI4}

Choose a sequence `a_D>0` tending to zero sufficiently slowly that

\[
\frac1{a_DD^2}
\sum_{e\in E_{nr}}\alpha_e
\to0.
\tag{5.2}

Then the number of nonradial contacts satisfying

\[
\alpha_e\ge a_D
\]

is `o(D^2)`.

Each such mechanically visible nonradial edge borders at most two strict rhombi. Hence only `o(D^2)` rhombi are incident to any mechanically visible nonradial edge.

For every other strict rhombus, **all** of its nonradial sides satisfy `alpha_e<a_D`. By ZRI2 it has at least two such sides.

Thus:

### Theorem ZRI.4 — two weak transverse sides on almost every rhombus

All but `o(D^2)` strict-rhombus faces have at least two boundary contacts `e_1,e_2` such that

\[
\boxed{
 e_1,e_2\notin C_{rad},
\qquad
\alpha_{e_1},\alpha_{e_2}<a_D,
\qquad
a_D\to0.
}
\tag{ZRI5}

If the rhombus has two radial sides, they form the opposite side pair and the other opposite side pair is entirely weak/nonradial.

If it has zero or one radial side, at least three or four sides respectively are nonradial, and every such side is weak outside the `o(D^2)` exceptional face family.

---

## 6. Mechanical normal form of the quadratic rhombic bulk

The ZCQ/ZRI branch therefore has the following local structure on all but a vanishing fraction of its `Omega_eta(D^2)` strict rhombi:

1. at most one opposite side pair can belong to the strongly-radial path forest;
2. at least two boundary contacts have absolute KKT stress tending to zero;
3. the complete finite contact support remains positive and the mixed framework remains universally/redundantly rigid.

The binding local regression is an oblique square-grid cell: one nearly axial opposite pair may carry the mechanical load while the transverse opposite pair has vanishing stress. Pure graph rigidity and local equilibrium do not exclude this model.

---

## 7. Train-track consequence

Opposite sides of a rhombus belong to the same train and are exactly parallel. Therefore a typical rhombus with two radial sides has one radial opposite pair and a weak transverse opposite pair.

ZRI does not imply that the same train remains weak across many consecutive rhombi, because stress can change at vertices with additional incident contacts. The next train-scale problem is therefore precise:

> Can a quadratic near-60-degree rhombic complex in a globally diameter-minimal source support one-directional force transport while, on almost every face, at least two transverse boundary contacts have stress `o(1)`?

The oblique-grid regression shows that local rhombus equilibrium alone allows this. A closing proof must use loaded-boundary/global-diameter information, the ZSP diameter chord, or the stopped-train exposed-hull structure.

---

## 8. Reconciliation with current-main PI/GU

Current main proves

\[
\liminf area(F)/D^2
\ge
A_{PI}=0.4978566363\ldots
\]

and forces a quadratic attachment-cell gap whenever

\[
\lambda_2:=\limsup(e_{BB}+2s_C)/D
<0.7961725673\ldots .
\]

ZCQ's explicit lower coefficient `c_eta` depends on the bridge fraction `eta` and can be arbitrarily small as `eta->0`. Therefore PI's area floor plus ZCQ's packing lower bound does **not** yield a universal numerical contradiction.

The correct combined branch statement is:

- ZEG-B / high reset is already charged to PI/GU high-surplus or macroscopic-pocket/giant-face geometry;
- ZEG-A / low reset yields ZSP, ZCQ, and ZRI: an almost-geodesic diameter path plus quadratic rhombic bulk whose transverse mechanical stresses vanish.

These are complementary closing targets, not competing estimates.

---

## 9. PR handoff state

The stacked branch now contains the following progressively stronger reductions beyond PR #108:

- **ZHC/ZHS/ZSR/ZHA:** one response-visible deep harmonic cell, series resistance control, linear attachments and short-response matching;
- **ZHH/ZHT/ZHN:** one complete consecutive `Omega(D)` macroscopic bridge trunk inside that cell, with bounded/near-neutral force corridors in almost all fixed-scale blocks;
- **ZRF/ZRP:** near-zero response puts `D^2-o(D^2)` contact stress on a radial path forest;
- **ZOB:** bridge stress itself pays exact outer-walk currency `x_B>=S_br/D-1`;
- **ZAC/ZDC:** all but `o(D)` trunk blocks admit moving-scale, directed, asymptotically radial force corridors;
- **ZEG:** exceptional-block reset is either sublinear or paid by the exact PI/GU surplus/gap currency;
- **ZSP:** the sublinear-reset branch contains an actual diameter contact path of length `D+o(D)` in an `o(D)` tube;
- **ZCQ:** ZHA attachments along central trunk positions force `v=Omega_eta(D^2)`;
- **ZRI:** this quadratic core has `Omega_eta(D^2)` strict rhombi and almost every rhombus has at least two vanishing-stress nonradial sides.

The direct Level I face inequality remains open. No report in this stack is promoted canonically merely by inclusion here.

---

## 10. Exact remaining local theorem

The next high-value statement is a **weak-transverse-train exclusion**:

> In the post-ZF globally diameter-minimal C-II source, the quadratic strict-rhombic bulk cannot have all but `o(D^2)` faces with at least two nonradial boundary contacts of stress `o(1)` while the strong mechanical support is a radial path forest and one captured diameter contact path has length `D+o(D)`.

Any proof must use more than positive self-stress and rhombus geometry. Promising extra inputs are ZSP/ZHA, stopped-train exposed-hull structure, current-main PI/PC pocket geometry, and exact global packing optimality.

---

## 11. Classification

**Status:** proved report-level strengthening of ZRI, reconciled with PI/GU.  
**Level I:** still open.  
**External literature:** none newly imported by ZRI.  
**Computation:** none.
