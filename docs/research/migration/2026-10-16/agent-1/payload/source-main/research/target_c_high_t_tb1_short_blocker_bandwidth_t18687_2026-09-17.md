# Target C-II — short TB1 blockers have path bandwidth at most fourteen

**Date:** 2026-09-17  
**Status:** proof-only strengthening of the one-sign strong-TB1 finite-swap reduction; no canonical promotion claimed  
**Scope:** selected O--O path coordinates in the high-`t` branch through `t=(q-k)/D<=1.8687`  
**Dependencies:** proper pairwise-disjoint O--O midpoint crosscuts; canonical strict unit-rhombus angle bounds; exact layer support for finite TB1 swaps; common-super-swap arborescence; genuine binary shell alignment  
**Certificate:** `research/verify_target_c_high_t_tb1_short_blocker_bandwidth_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The latest directed common-super-swap theorem leaves a concrete ordering seam: the inactive obstruction arborescence is a graph on path layers, but its source pairs were not yet metrically related to the distance between their path-layer tags.

For short pairs there is a uniform relation. A source segment of length `1+o(1)` can cross at most fourteen selected O--O rows. The reason is elementary area packing: every selected row crossed by the segment contributes a distinct strict unit rhombus of area greater than `sqrt(3)/2`, while every such rhombus lies in the `sqrt(3)`-tube around the segment.

Consequently every inverse-`D` near-unit blocker in the common-super-swap graph joins path regions at index distance at most fourteen. This has a second use in the exact-swap Boolean system. Keeping one residue class of one-sign layer indices modulo fifteen produces a still-linear exact-swap family in which no near-unit source pair can involve two retained coordinates. After deleting the `O(1)` coordinates incident to the already-bounded genuine upper binary blockers, the remaining linear family has no genuinely new two-coordinate obstruction at either metric boundary.

More precisely, there is a retained exact-swap family `P_D` with

\[
\boxed{
|P_D|>{s_0\over30}D-o(D)
=(8.23958333333\ldots\times10^{-8})D-o(D),
\qquad
s_0={791\over320{,}000{,}000},
}
\]

such that:

1. every two retained layer indices differ by at least `15`;
2. every near-unit blocker of a retained singleton swap has its other endpoint outside all retained layers, so that blocker is persistent under every other retained swap;
3. no previously strict pair can be safe under both of its singleton retained swaps and become bad only when both are applied;
4. hence under an arbitrary simultaneous retained-swap subset, every newly invalid source pair was already invalid under at least one selected singleton swap of one of its endpoints.

Thus the finite-swap problem can be thinned at constant cost so that combinations of swaps create no new inactive constraints. The remaining difficulty is purely disarming/persistence: a blocker present at a singleton state can disappear after another endpoint is swapped, and near-diameter blockers can still carry that coupling.

---

## 1. Short-segment row-crossing lemma

Use the ordered selected O--O crosscuts

\[
R_0\xleftrightarrow{\tau_1}R_1\xleftrightarrow{\tau_2}\cdots
\xleftrightarrow{\tau_m}R_m.
\tag{BW.1}
\]

The selected crosscuts are proper and pairwise disjoint. Their portions inside the contact complex run along midpoint centerlines of complete stopped trains through strict unit rhombi.

Let `x,y` be source vertices in path regions `R_p,R_q`, with `p<q`, and let

\[
L=|x-y|.
\]

The straight segment `xy` is contained in the convex hull. Since each `tau_j`, `p<j<=q`, separates `R_p` from `R_q`, the segment meets every one of

\[
\tau_{p+1},\ldots,\tau_q.
\tag{BW.2}
\]

For each such row choose a strict unit rhombus in that row whose closure meets `xy` at the crossing. At a centerline vertex either adjacent rhombus may be chosen; at an outer midpoint endpoint choose the terminal rhombus. Because the selected O--O trains are pairwise disjoint, rhombi chosen for distinct rows are distinct.

A strict unit rhombus has an angle

\[
{\pi\over3}<\theta<{2\pi\over3}.
\]

Therefore its area obeys

\[
\boxed{
\operatorname{area}(F)=\sin\theta>{\sqrt3\over2},
}
\tag{BW.3}
\]

and both diagonals are strictly shorter than `sqrt(3)`, so

\[
\boxed{\operatorname{diam}(F)<\sqrt3.}
\tag{BW.4}
\]

If `F` meets `xy`, (BW.4) puts all of `F` inside the closed `sqrt(3)`-neighborhood of the segment. The area of that tube is

\[
2\sqrt3\,L+3\pi.
\tag{BW.5}
\]

The interiors of distinct contact faces are disjoint. If `N=q-p` selected rows separate the endpoints, (BW.3)--(BW.5) give

\[
N{\sqrt3\over2}
<2\sqrt3\,L+3\pi,
\]

hence

\[
\boxed{
N<4L+2\pi\sqrt3.
}
\tag{BW.6}
\]

This estimate is independent of KKT stress, diameter activity, TB1, or the train phase.

---

## 2. Inverse-`D` near-unit pairs cross at most fourteen rows

Fix any constant `K>0` and suppose

\[
1<|x-y|\le1+{K\over D}.
\tag{BW.7}
\]

Then (BW.6) gives

\[
q-p
<4+2\pi\sqrt3+{4K\over D}.
\tag{BW.8}
\]

The limiting constant is strictly below fifteen:

\[
4+2\pi\sqrt3
=14.8827961854\ldots<15.
\tag{BW.9}
\]

For a fully elementary fixed margin, use `pi<22/7` and `sqrt(3)<1733/1000` to obtain

\[
4+2\pi\sqrt3
<{26063\over1750}
=14.8931428571\ldots,
\tag{BW.10}
\]

leaving margin `187/1750`. Thus, for instance, `D>7000K/187` makes the right side of (BW.8) strictly below `15`.

Since `q-p` is an integer,

\[
\boxed{
|p-q|\le14
}
\tag{BW.11}
\]

for all sufficiently large sources.

Call this the **short-pair path-bandwidth lemma**.

The same conclusion of course holds for any `1+O(D^-2)` pair.

---

## 3. Every LOWER common-super-swap arborescence edge is 14-local

In the directed common-super-swap arborescence, every LOWER arc is realized by a previously strict source pair satisfying

\[
1<|r|\le1+{K\over D}
\tag{BW.12}
\]

for the one fixed common-super-swap constant `K`.

Do not aggregate the outside endpoint into the root for this statement. Give each endpoint its actual path-region label. The short-pair path-bandwidth lemma immediately yields

\[
\boxed{
|\operatorname{reg}(x)-\operatorname{reg}(y)|\le14
}
\tag{BW.13}
\]

for every LOWER arborescence pair.

Thus the LOWER winner in the three-way directed-arborescence fork is not an arbitrary linear near-unit family. It is a linear family of inactive pairs supported inside a fixed-width band of the ordered O--O path.

The root aggregation in the arborescence can hide this locality graphically, because different root arcs can use different residual path regions. Equation (BW.13) records the source-level locality that survives that aggregation.

---

## 4. Fifteen-spacing removes all lower two-coordinate coupling

Return to the local exact contact swaps on the one-sign strong-TB1 population `M_D`. The one-sign winner has

\[
|M_D|>{s_0\over2}D-o(D).
\tag{BW.14}
\]

Partition its integer path-layer indices into the fifteen residue classes modulo `15` and keep a largest class `P_D^0`. Then

\[
|P_D^0|\ge {|M_D|\over15}
>{s_0\over30}D-o(D),
\tag{BW.15}
\]

and distinct retained indices satisfy

\[
\boxed{|i-j|\ge15.}
\tag{BW.16}
\]

In particular they are nonadjacent, so the simultaneous exact-swap active-constraint decoupling theorem applies to every subset of `P_D^0`: old contacts remain exactly unit, and every old actual diameter is unchanged or strictly shortened.

Now take a previously strict pair that reaches the **unit lower boundary** under the singleton exact swap at retained coordinate `i`. The local exact-swap window gives

\[
1<|xy|\le1+q_i,
\qquad q_i=O(D^{-1}).
\tag{BW.17}
\]

By the short-pair path-bandwidth lemma its endpoint regions differ by at most fourteen. Therefore its other endpoint cannot belong to any other retained layer `R_j`, `j in P_D^0`.

Hence, relative to the retained finite-swap system, that pair has support on exactly one coordinate. Its state is unaffected by all other retained swaps. We have proved

\[
\boxed{
\text{every lower singleton blocker on }P_D^0
\text{ is a permanent one-coordinate blocker.}
}
\tag{BW.18}
\]

In particular there are no lower genuine binary blockers and no lower disarming implications between retained coordinates.

This is stronger than the earlier statement that lower genuine binary blockers form a row-parallel path forest: after the residue thinning, that forest has no edges at all.

---

## 5. Delete the bounded genuine upper binary exception

The genuine-binary shell-alignment theorem gives a source-wide bound

\[
\boxed{
N_{\rm genuine\ binary,upper}=O(1).
}
\tag{BW.19}
\]

for pairs that are safe under both singleton exact swaps but violate the diameter bound under their joint swap.

Delete from `P_D^0` every coordinate incident to one of those `O(1)` source pairs. At most `O(1)` coordinates are removed. Call the result `P_D`. Then

\[
\boxed{
|P_D|>{s_0\over30}D-o(D)
={791\over9{,}600{,}000{,}000}D-o(D).
}
\tag{BW.20}

Numerically,

\[
{s_0\over30}
=8.23958333333\ldots\times10^{-8}.
\tag{BW.21}

By Section 4 there is no genuine lower binary blocker on `P_D`, and by construction there is no genuine upper binary blocker. Therefore for every previously strict pair supported on two retained coordinates `i,j`,

\[
\boxed{
11\text{ bad}\quad\Longrightarrow\quad
10\text{ bad or }01\text{ bad}.
}
\tag{BW.22}
\]

Here `10,01,11` have the exact-swap meaning from the two-swap truth-table theorem. No boundary type is suppressed in (BW.22).

---

## 6. Global no-new-obstruction corollary

Take any subset

\[
\varnothing\ne S\subseteq P_D
\]

and apply the exact local swap at every layer in `S` simultaneously.

Every source vertex belongs to at most one physical path layer. Therefore every source pair depends on at most two retained Boolean coordinates.

Suppose a previously strict pair becomes invalid in the final state for `S`.

- If the pair has retained support of size one, its final vector is exactly its singleton-swap vector, so that singleton state is already bad.
- If its retained support is `{i,j}` and both are selected, its final state is `11`. Equation (BW.22) says at least one of its singleton states `10` or `01` was already bad.

Thus

\[
\boxed{
\text{every inactive violation created by an arbitrary retained subset}
\text{ has a bad selected singleton ancestor.}
}
\tag{BW.23}
\]

Equivalently, simultaneous exact swaps on `P_D` can **delete/disarm** singleton obstructions but cannot create a previously unseen obstruction that requires two selected coordinates.

This removes genuine multi-coordinate synergy from a linear-dimensional exact-swap subsystem. Since every pair has support at most two, there is no higher-arity loophole hidden beyond the two-swap analysis.

---

## 7. What remains

This does not yet produce a feasible nonzero exact-swap subset.

A singleton blocker can be disarmed when the layer containing its other endpoint is also selected. After the 15-spacing reduction:

- every lower-bound singleton blocker is permanent and therefore makes its coordinate unusable;
- every genuinely new two-coordinate blocker is gone;
- all remaining disarming interaction is carried by near-diameter upper blockers already present at singleton states.

So the finite-swap closure problem has become one-sided in metric type. The next useful target is to classify the upper disarming relation on `P_D`. A closing result would follow from either of the following:

1. show that a positive-density set of retained coordinates has no permanent lower blocker and that the upper disarming digraph admits a nonempty closed subset with no persistent upper blocker; or
2. show that blocking every nonempty retained subset forces a linear ordered family of persistent/signed/superdiameter upper pairs, then contradict that family against the common train grid.

The important new restriction is that short near-unit geometry can no longer participate in the two-coordinate coupling at all.

**Disposition:** proved a universal fourteen-row bandwidth for inverse-`D` near-unit source pairs, made all LOWER common-super-swap blockers path-local, and extracted a linear 15-spaced exact-swap subsystem with no genuinely new multi-coordinate inactive obstruction. C-II and Level I remain open.
