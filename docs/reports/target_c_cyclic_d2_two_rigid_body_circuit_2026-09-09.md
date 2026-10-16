<!-- theorem-state: {"artifact_id":"ART-7344CAA673B4","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cyclic `d_H=2` is exactly two rigid bodies joined by a four-contact circuit

**Date:** 2026-09-09  
**Run type:** exact rigidity/body-bar reduction  
**Target:** Target C primitive cyclic endpoint, `d_H=2`, `s_Z=0`  
**Depends on:** D2 four-block two-tree normal form; CY unique full-support stress / ZF mixed rigidity. The row-circuit argument is reproved here and does not require PR #123.  
**External literature:** none  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`

The `d_H=2` endpoint is substantially more rigid than the statement “two diameter trees on four alternating blocks.” Each diameter-tree component, together with the shell contacts internal to its two boundary blocks, is itself a maximally ranked infinitesimally rigid framework. The complete shell is therefore a two-body framework with exactly four interbody bars.

Let

\[
H=T_A\sqcup T_B
\]

be the two full diameter-tree components from D2, with vertex sets `A,B`. Then:

\[
\boxed{
G[A]=T_A\cup C[A]
\text{ has }2|A|-3\text{ independent rigidity rows},
}
\tag{RB.1}
\]

and symmetrically

\[
\boxed{
G[B]=T_B\cup C[B]
\text{ has }2|B|-3\text{ independent rigidity rows}.
}
\tag{RB.2}
\]

Hence both induced frameworks are infinitesimally rigid.

Exactly four shell contacts join `A` to `B`, namely the four transitions between the cyclic blocks

\[
A_0\mid B_0\mid A_1\mid B_1.
\]

After quotienting the internal Euclidean motions of the two rigid subframeworks, these four contact rows have rank exactly three in the three-dimensional relative rigid-motion space and have one full-support positive dependence.

Thus:

\[
\boxed{
\text{cyclic }d_H=2
=
\text{two planar rigid bodies joined by a positive four-bar circuit}.}
\tag{RB.3}
\]

Deleting any one of the four transition contacts still leaves the full mixed framework infinitesimally rigid; deleting any two leaves at least one relative infinitesimal degree of freedom.

This isolates the remaining geometric obstruction to one finite four-contact body-bar cage. No internal diameter or contact row participates in the relative-motion problem after the two rigid blocks are contracted.

---

## 1. Row count inside one diameter component

D2 gives four nonempty cyclic blocks

\[
A_0\mid B_0\mid A_1\mid B_1,
\]

where `A=A_0\sqcup A_1` is the vertex set of the tree `T_A` and `B=B_0\sqcup B_1` is the vertex set of `T_B`.

Because `A_0` and `A_1` are two distinct nonempty intervals of the shell cycle, the shell contacts with both endpoints in `A` are precisely the path edges internal to these two intervals. Therefore

\[
|C[A]|
=(|A_0|-1)+(|A_1|-1)
=|A|-2.
\tag{1.1}
\]

Since `T_A` is a tree on `A`,

\[
|E(T_A)|=|A|-1.
\tag{1.2}
\]

Thus the induced mixed row set on `A` contains exactly

\[
\boxed{|C[A]|+|E(T_A)|=2|A|-3}
\tag{1.3}
\]

rows. The same calculation gives `2|B|-3` rows on `B`.

---

## 2. Every proper subset of the full mixed row set is independent

In the `d_H=2` cyclic phase,

\[
s_Z=0.
\]

The full mixed framework has

\[
q+(q-2)=2q-2
\]

rows. ZF gives rigidity rank

\[
2q-3.
\]

Therefore the row-dependence space is one-dimensional.

The unique normalized KKT stress is strictly positive on every shell contact and every actual diameter row. In the signed mixed rigidity dependence, every coefficient is consequently nonzero. Hence the unique row dependence has full support.

### Lemma RB.1 — full-support one-circuit property

Every proper subset of the full mixed row set is linearly independent.

### Proof

If a proper row subset had a nonzero dependence, extend it by zero coefficients on the omitted rows. This would be a dependence of the full row set. Since the full dependence space is one-dimensional, it must be a scalar multiple of the unique KKT dependence. But that dependence has no zero coefficient, whereas the extended proper-subset dependence has at least one zero coefficient. Contradiction. `square`

Thus the complete realized mixed row set is a rigidity-matroid circuit, proved here directly from the `s_Z=0` data.

---

## 3. Each diameter component is a rigid block

The row set of `G[A]` is a proper subset of the full row set because `B` is nonempty and there are four interbody shell contacts. By Lemma RB.1 its `2|A|-3` rows are independent.

A planar framework on `|A|` vertices has rigidity rank at most

\[
2|A|-3.
\]

Therefore

\[
\boxed{\operatorname{rank}R(G[A])=2|A|-3.}
\tag{3.1}
\]

This is exactly infinitesimal rigidity of the induced framework on `A`. The same proof yields

\[
\boxed{\operatorname{rank}R(G[B])=2|B|-3.}
\tag{3.2}
\]

No generic-coordinate assumption is used. These are rigidity statements at the actual Target C coordinates.

---

## 4. Exactly four rows couple the two rigid blocks

The cyclic order

\[
A_0\mid B_0\mid A_1\mid B_1
\]

has exactly four transitions between an A vertex and a B vertex. Since the complete contact graph is the shell cycle, those four transition edges are exactly all A-B contact rows.

There are no A-B diameter rows because `T_A,T_B` are the connected components of the full diameter graph.

Hence, after the two induced rigid frameworks are treated as rigid bodies, the full active framework contains precisely four interbody bars, all of unit length.

Fix body `B` modulo a common global Euclidean motion. An infinitesimal relative rigid motion of body `A` has three parameters:

\[
\xi=(v_x,v_y,\omega)\in\mathbb R^3.
\]

Each transition contact gives one linear first-derivative constraint on `xi`. Let

\[
W\in\mathbb R^{4\times3}
\]

be this relative contact matrix.

Internal rigidity contributes rank

\[
(2|A|-3)+(2|B|-3)=2q-6.
\]

The full mixed rigidity rank is `2q-3`. Therefore

\[
\boxed{\operatorname{rank}W=3.}
\tag{4.1}
\]

Thus the four relative rows span the complete relative rigid-motion dual space and have exactly one linear dependence.

---

## 5. The interbody dependence is positive and full support

Restrict the unique full mixed KKT row dependence to the quotient by the internal rows. Internal contact and diameter forces cancel inside each rigid block. What remains is the dependence among the four transition contact rows.

All four KKT contact coefficients satisfy

\[
\alpha_i>0.
\]

Hence, using the natural length-derivative row convention for the relative motion,

\[
\boxed{
\alpha_1 W_1+\alpha_2 W_2+\alpha_3 W_3+\alpha_4 W_4=0,
\qquad
\alpha_i>0.
}
\tag{5.1}
\]

The row orientation is immaterial: a squared-distance rigidity row is unchanged by swapping its two endpoints. Equivalently, after fixing which body moves, (5.1) is the summed force-and-torque equilibrium of one rigid block.

Since `rank W=3`, this is the unique dependence up to scale.

Thus the origin lies in the relative interior of the tetrahedral convex hull of the four contact wrenches in `R^3`. The four contacts are an exact positive circuit/form-closure cage for relative infinitesimal motion.

D2.2 is the translational two-coordinate projection of (5.1): if the four transition contact tangents are `t_i,t_j,t_k,t_l` in cyclic order, then

\[
\alpha_i t_i-\alpha_jt_j+\alpha_kt_k-\alpha_lt_l=0.
\]

The third coordinate of (5.1) is the corresponding torque identity, which D2 did not need to state explicitly.

---

## 6. Deleting transition contacts

Because the full row set is a circuit, deleting **any one** row leaves an independent set of size

\[
2q-3.
\]

In particular, deleting any one of the four A-B contacts leaves the full framework with rank `2q-3`; it remains infinitesimally rigid.

After contracting the two internal rigid blocks this says any three of the four rows of `W` are independent.

If any two transition contacts are deleted, at most two relative rows remain. Their rank is at most two in the three-dimensional relative-motion space, so there is at least one non-Euclidean relative infinitesimal motion preserving all internal active lengths and the two retained contact lengths to first order.

Thus:

\[
\boxed{
4\text{ interbody contacts: positive circuit};
\quad3:\text{ rigid};
\quad2:\text{ at least one relative infinitesimal mode}.}
\tag{6.1}
\]

This is an exact finite reduction, not a counting heuristic.

---

## 7. Why this is useful

Before RB, the `d_H=2` endpoint was an ordered pair of caterpillar trees plus a reciprocal parallelogram. After RB, all internal complexity can be quotiented out for any local source-preserving motion that treats the two induced frameworks rigidly.

The only active constraints coupling the two sides are four unit shell contacts. Every actual diameter pair is internal to one rigid body and is therefore preserved exactly by independent rigid motions of the two bodies.

Consequently a finite release of the `d_H=2` endpoint can be sought entirely in the three-dimensional relative pose space `SE(2)`:

> Can one perturb the relative pose of the two rigid blocks so that all four transition distances stay at least one, at least one opens, and all previously inactive cross-body distances remain below `D` by finite slack?

The first-order answer is **no**, exactly because (5.1) is a positive circuit. Therefore any successful release must exploit second-order/nonlinear geometry of this four-contact cage. This identifies the precise remaining local obstruction rather than rediscovering KKT first-order balance.

---

## 8. Regression audit

### Abstract four-block examples

Retained. RB does not claim the four-bar cage is impossible; it proves that every genuine `d_H=2` survivor reduces to one.

### Three transition bars

They are enough for infinitesimal rigidity because any one row deletion from the full rigidity circuit leaves rank `2q-3`. No false “four bars are needed for rigidity” claim is made.

### Two transition bars

Only an infinitesimal relative mode is claimed. Finite integration with the other two contact inequalities is not automatic.

### Internal rattlers

They are not vertices of the mixed shell framework. UFB/ID keep them fixed with strict slack under sufficiently small shell motions. RB concerns the active shell framework and is compatible with that source-wide transfer.

### Generic body-bar theory

No generic theorem is imported. All rank statements follow directly from the actual-coordinate full-support circuit.

---

## 9. Next theorem

The next `d_H=2` target is now a three-variable finite problem.

Let the four transition contact rows be the boundary shell edges at the four block corners. Use their actual convex cyclic order and the exact positive wrench dependence (5.1) to classify the local feasible set

\[
\{g_r(\xi)\ge0:r=1,2,3,4\}
\]

in relative `SE(2)` coordinates through second order.

Two possible closing outcomes:

1. prove the positive four-contact cage has a nontrivial finite branch on which all four distances are `>=1` and one is `>1`; SL+ would then contradict contact/diameter lexicographic minimality, because all diameter rows are internal and remain exactly fixed;
2. prove the cage is genuinely second-order isolated, then derive the resulting curvature/wrench equalities and combine them with the near-Reinhardt difference-body normal forms P2/PS/S2.

Either outcome advances the actual endpoint.

---

## 10. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Cyclic d_H=2 has H=T_A disjoint union T_B and four blocks
    A0 | B0 | A1 | B1.
For A, the two shell intervals contribute |A|-2 internal contact edges and T_A
contributes |A|-1 diameter edges, total 2|A|-3. Since s_Z=0, the full 2q-2 mixed rows
have rank 2q-3 and their unique dependence has full support. Hence every proper row
subset is independent, so G[A] has rank 2|A|-3 and is infinitesimally rigid. Same B.

There are exactly four A-B active rows: the four unit shell transition contacts. After
contracting the two rigid subframeworks, their relative row matrix W is 4x3 with rank 3.
The unique KKT dependence restricts to
    sum alpha_i W_i=0, alpha_i>0.
Thus the whole d_H=2 shell is exactly two rigid bodies joined by a positive four-bar
relative-motion circuit. Any three transition bars still rigidify the relative pose;
with only two there is at least one infinitesimal relative mode.

Next: analyze this four-contact cage to second order in SE(2). All diameter constraints
are internal to the two bodies and stay exactly fixed under relative rigid motions, so a
finite opening branch would directly contradict SL+/C65.
```
