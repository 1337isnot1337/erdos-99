# Target C-II — double-ear amplification and pentagonal-hole forcing near the terminal `t` floor

**Date:** 2026-09-18  
**Status:** proof-only structural refinement; theorem-state authority unchanged  
**Scope:** the concrete low-detour terminal FREE window of `target_c_free_terminal_t_near_floor_near_contact_matching_2026-09-18.md` and `target_c_free_terminal_t_near_floor_rhombic_ear_train_graph_2026-09-18.md`  
**Depends on:** the certified `0.4155508927...D` near-orbit pentagon floor; `P_5-F_5^{full}<=2S`; the five-root two-ear closure lemma; the no-return-to-one-face train theorem; the audited full-rhombus-complex boundary/period theorem; promoted edge-aligned-hole estimate HA  
**Certificate:** `research/verify_target_c_free_terminal_t_near_floor_double_ear_period_split_2026_09_18.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The preceding ear/train note loses a factor nine before it uses train coordinates: it chooses one ear per near fully-rhombic pentagon and then asks the ear diagonals to be vertex-disjoint in the source graph. That loss is unnecessary for the train-rate problem.

Keeping **both** guaranteed ears from every near fully-rhombic pentagon produces a maximum-degree-two multigraph directly on stopped-train coordinates. More importantly, a fully-rhombic bounded pentagon is itself a five-edge bounded complementary component of the **full strict-rhombus complex**. This removes a false apparent alternative: the supporting ear trains are not period-free. They all terminate on a genuine rhombic hole.

In the current concrete window, if the singleton stopped-train count is below `0.1D`, the resulting coefficients are

\[
\boxed{0.2155D\text{ raw train-compatible ears}},
\qquad
\boxed{0.1437D\text{ train-coordinate-disjoint ears}},
\]

while the same pentagons force

\[
\boxed{g_R>0.2155D,}
\qquad
\boxed{P_{hole}>1.0777D,}
\]

and at least

\[
\boxed{0.2800D}
\]

of actual edge-aligned rhombic-hole area. Despite the linear hole population, the complete rhombic hole-period system still has a train-angle kernel of dimension at least

\[
\boxed{0.1077D.}
\]

Thus internal topology does not kill all train freedom. The live question is whether enough of this surviving period kernel can shorten the near-unit ears while satisfying the bounded-face/contact closure and active-diameter systems.

---

## 1. Near fully-rhombic pentagons

Use the notation of the two preceding notes. In the concrete terminal window

\[
\limsup t_D\le1.959952849540479\ldots,
\qquad
\limsup {b-P_F\over D}\le10^{-5},
\tag{DH.1}
\]

the certified near-orbit theorem gives

\[
\lim_{\theta\downarrow0}\liminf
{P_5^{near}(\theta)\over D}
\ge
N_0,
\qquad
N_0=0.415550892775345\ldots .
\tag{DH.2}
\]

Let `S` be the singleton stopped-train count. The exact incidence theorem

\[
P_5-F_5^{full}\le2S
\tag{DH.3}
\]

gives

\[
|P_5^{near}(\theta)\cap F_5^{full}|
\ge P_5^{near}(\theta)-2S.
\tag{DH.4}
\]

Write

\[
s:=\limsup {S\over D},
\qquad
p:=N_0-2s.
\tag{DH.5}
\]

Whenever `p>0`, the density of near-orbit fully-rhombic pentagons is at least `p-o(1)`.

For the concrete non-singleton branch `s<0.1`,

\[
\boxed{
p>p_0:=N_0-0.2
=0.215550892775345\ldots .}
\tag{DH.6}
\]

Every pentagon counted here is source-empty by the existing isolate-host theorem.

---

## 2. Every fully-rhombic pentagon is a five-edge rhombic hole

Let `F` be one bounded pentagonal contact face in `F_5^{full}`. By definition, the opposite side of every one of its five contact edges is a strict rhombus.

Let `mathcal R` be the union of **all** closed strict-rhombus faces in the positive-contact core. The simple convex pentagon boundary `partial F` is contained in `mathcal R`, because each of its five edges belongs to an adjacent strict rhombus. The open interior of `F` is disjoint from `mathcal R`, because `F` is itself a nonquadrilateral contact face.

The Jordan curve `partial F` separates its interior from the unbounded plane. Since the entire separating curve lies in the closed set `mathcal R`, `int(F)` is a bounded connected component of the complement of `mathcal R`. Hence `F` is literally a bounded hole of the full strict-rhombus complex, of physical boundary length five.

Distinct bounded contact faces have disjoint interiors, so distinct fully-rhombic pentagons give distinct rhombic holes. If `P` denotes the number of near fully-rhombic pentagons retained above, then

\[
\boxed{g_R\ge P,}
\tag{DH.7}
\]

and, because each contributes five distinct physical hole-boundary occurrences,

\[
\boxed{P_{hole}\ge5P.}
\tag{DH.8}
\]

Therefore asymptotically

\[
\boxed{
\liminf {g_R\over D}\ge p,
\qquad
\liminf {P_{hole}\over D}\ge5p.
}
\tag{DH.9}
\]

In the concrete `s<0.1` branch,

\[
\boxed{
\liminf {g_R\over D}>0.215550892775345\ldots,}
\tag{DH.10}
\]

\[
\boxed{
\liminf {P_{hole}\over D}>1.077754463876728\ldots .}
\tag{DH.11}
\]

This is much stronger than the earlier generic hole-endpoint split. In this fully-rhombic pentagon branch there is no period-free ear support: every pentagon side is itself a hole-boundary train endpoint.

---

## 3. The pentagonal holes force actual linear missing area

The promoted edge-aligned-hole estimate HA gives, for a rhombic hole `H` with physical boundary length `b_H`,

\[
\operatorname{area}(H)
\ge {\sqrt3\over4}(b_H-2).
\tag{DH.12}
\]

For every pentagonal hole from Section 2, `b_H=5`. Hence

\[
\boxed{
\operatorname{area}(H)\ge{3\sqrt3\over4}.}
\tag{DH.13}
\]

The holes have disjoint interiors. If `G_5` is the total area of these near fully-rhombic pentagonal holes, then

\[
\boxed{
G_5\ge {3\sqrt3\over4}P.}
\tag{DH.14}
\]

Therefore

\[
\boxed{
\liminf {G_5\over D}\ge {3\sqrt3\over4}p.}
\tag{DH.15}
\]

In the concrete branch,

\[
\boxed{
\liminf {G_5\over D}
>0.280008823427797\ldots .}
\tag{DH.16}
\]

A conservative coefficient is `0.2800D`.

Because these pentagonal holes are source-empty, this is actual empty bounded-face area, not an Oler area-minus-population surrogate. It is still only first-order area, so it does not by itself contradict the `Theta(D^2)` Type-II bulk.

---

## 4. Keep both ears and build the train multigraph

For sufficiently small orbit tolerance `theta`, the five-root closure lemma gives **two disjoint adjacent edge pairs** in every pentagon counted in Section 1. Each pair spans an ear diagonal `d` satisfying

\[
1<d\le2\cos(\pi/3-\theta).
\tag{DH.17}
\]

Each of the four contact sides used by these two ears is a terminal side of a non-singleton strict-rhombus stopped train. The no-return-to-one-face theorem says one complete nontrivial train cannot have two terminal occurrences on the same bounded face. Therefore the four train coordinates supporting the two ears of one pentagon are distinct.

Keep both ears from every near fully-rhombic pentagon. Form a loopless multigraph `J_2` whose vertices are complete stopped trains and whose edges are these ears, joining the two supporting train coordinates.

A complete stopped train has exactly two terminal face-side occurrences. Every incidence of a train with an edge of `J_2` uses one such terminal occurrence. Hence, with multiplicity,

\[
\boxed{\Delta(J_2)\le2.}
\tag{DH.18}
\]

If `P` is the number of retained near fully-rhombic pentagons, then

\[
\boxed{|E(J_2)|=2P.}
\tag{DH.19}
\]

Parallel edges are possible only as a two-edge cycle. Loops are impossible because the two sides of one ear belong to distinct trains.

---

## 5. Raw simultaneous shortening loses no source-matching factor

For one ear with consecutive oriented unit sides `u,v`, let their train angular rates be `alpha,beta`, with the corrected orientation convention of the preceding note. Its exact first derivative is

\[
{d\over dt}|u+v|^2
=2\sin\vartheta\,(\alpha-\beta),
\qquad 0<\vartheta<\pi.
\tag{DH.20}
\]

Thus the ear shortens to first order exactly when

\[
\alpha<\beta.
\tag{DH.21}
\]

Every connected component of a loopless maximum-degree-two multigraph is a path or a cycle, allowing a two-edge parallel cycle. Delete one edge from each cycle of `J_2`. A cycle has at least two edges, so at least half of all edges remain. The retained graph is a forest and therefore has no directed cycle under any orientation.

Orient each retained edge according to its shortening inequality (DH.21). A topological ordering assigns train rates satisfying every strict inequality simultaneously. Therefore

\[
\boxed{
|\mathcal E_{raw}|
\ge {1\over2}|E(J_2)|
=P.}
\tag{DH.22}
\]

Asymptotically,

\[
\boxed{
\liminf {|\mathcal E_{raw}|\over D}\ge p.}
\tag{DH.23}
\]

In the concrete branch,

\[
\boxed{
\liminf {|\mathcal E_{raw}|\over D}
>0.215550892775345\ldots .}
\tag{DH.24}
\]

A conservative coefficient is `0.2155D`.

This removes the factor-nine source-vertex matching loss from the train-rate problem. It is still an unconstrained train-rate statement; the period and external locking systems have not yet been imposed.

---

## 6. A matching directly in train-coordinate space

A loopless multigraph of maximum degree two with `m` edges has a matching of size at least `m/3`: paths and cycles have the standard half-size matchings, with the triangle giving the worst ratio `1/3` and a two-edge parallel cycle giving ratio `1/2`.

Apply this componentwise to `J_2`. There is an ear family `M_tr` such that no stopped train supports two selected ears and

\[
\boxed{
|M_{tr}|
\ge {1\over3}|E(J_2)|
={2\over3}P.}
\tag{DH.25}
\]

Thus

\[
\boxed{
\liminf {|M_{tr}|\over D}\ge{2p\over3}.}
\tag{DH.26}
\]

In the concrete branch,

\[
\boxed{
\liminf {|M_{tr}|\over D}
>0.143700595183563\ldots .}
\tag{DH.27}
\]

A conservative coefficient is `0.1437D`.

Every supporting train in this matching is hole-ending at the pentagon that supplied its selected ear. The train-coordinate disjointness is therefore useful for studying the sparse period/closure matrix, but it does not remove those period rows.

---

## 7. Linear holes still leave a linear full period kernel

The audited full-rhombus-complex theorem gives the exact stopped-train count

\[
2T=P_R,
\tag{DH.28}
\]

where `P_R` is total physical boundary occurrence count of the full strict-rhombus complex, including outer and hole boundaries. Write

\[
P_R=P_{out}+P_{hole}.
\tag{DH.29}
\]

The same theorem proves every bounded rhombic hole has boundary length at least five, so

\[
5g_R\le P_{hole}.
\tag{DH.30}
\]

For all rhombic holes simultaneously, the train-angle period map has at most two scalar equations per hole. Hence its kernel, and therefore the rhombic train-angle flex space, satisfies

\[
\dim\mathcal F_{train}\ge T-2g_R.
\tag{DH.31}
\]

Use (DH.28)--(DH.30):

\[
\begin{aligned}
T-2g_R
&={P_{out}\over2}+{P_{hole}\over2}-2g_R\\
&\ge {P_{out}\over2}+{P_{hole}\over10}\\
&\ge {P_{hole}\over10}.
\end{aligned}
\tag{DH.32}
\]

Combining with the direct pentagonal-hole floor (DH.8),

\[
\boxed{
\dim\mathcal F_{train}
\ge {P\over2}.}
\tag{DH.33}
\]

Therefore

\[
\boxed{
\liminf {\dim\mathcal F_{train}\over D}
\ge {p\over2}.}
\tag{DH.34}
\]

In the concrete `s<0.1` branch,

\[
\boxed{
\liminf {\dim\mathcal F_{train}\over D}
>0.107775446387672\ldots .}
\tag{DH.35}
\]

A conservative coefficient is `0.1077D`.

This is a full internal-period statement: all bounded rhombic hole periods are imposed simultaneously. The large pentagonal-hole population therefore does not consume all train-angle freedom.

What is not proved is that the surviving kernel has a vector satisfying a positive fraction of the ear inequalities (DH.21). The kernel could, in principle, be positioned badly relative to the ear-difference rows. That relative-position problem is now the exact internal linear-algebraic obstruction.

---

## 8. Concrete terminal near-floor package

Under (DH.1), either

\[
\boxed{S\ge(0.1-o(1))D,}
\tag{DH.36}
\]

or all of the following hold after the standard limit extraction:

\[
\boxed{
P>(0.2155-o(1))D,
\quad
g_R>(0.2155-o(1))D,
\quad P_{hole}>(1.0777-o(1))D,
}
\tag{DH.37}
\]

\[
\boxed{G_5>(0.2800-o(1))D,}
\tag{DH.38}
\]

\[
\boxed{|\mathcal E_{raw}|>(0.2155-o(1))D,}
\qquad
\boxed{|M_{tr}|>(0.1437-o(1))D,}
\tag{DH.39}
\]

and

\[
\boxed{
\dim\mathcal F_{train}>(0.1077-o(1))D.
}
\tag{DH.40}
\]

The ear diagonal lengths can be made arbitrarily close to one from above by shrinking the dominant-orbit tolerance exactly as in the preceding near-contact theorem.

---

## 9. Scope and remaining obstruction

1. **The source-vertex matching loss is intentionally removed.** The older `0.0461D` source near-contact matching remains the correct object when vertex-disjoint nonedges are required. The present `0.2155D` floor concerns compatibility of inequalities in train-coordinate space.
2. **A fully-rhombic pentagon is a hole.** This is stronger than merely saying its sides are rhombic train terminals. The five-edge Jordan boundary lies in the full strict-rhombus complex and encloses the non-rhombic face interior.
3. **There is no period-free ear branch here.** Every ear-support train has a hole endpoint on its defining pentagon. The previous weaker endpoint split has been replaced by the direct five-edge hole count.
4. **The full period kernel remains linear.** Equation (DH.35) imposes every rhombic hole-period equation, not just the selected pentagon rows.
5. **Kernel dimension is not enough.** A `0.1077D`-dimensional period kernel might still lie inside many ear non-shortening halfspaces. A closing theorem needs a rank/oriented-matroid statement coupling the ear-difference map to the period kernel.
6. **Exceptional-face and diameter locking remain live.** Even a favorable period-kernel vector must satisfy the rest of the positive-contact closure system and make all active diameter derivatives nonpositive.
7. **The linear hole area is not by itself a contradiction.** `0.2800D` is first-order against a `Theta(D^2)` bulk. It is, however, an actual localized empty-face payment that can be fed into any future first-order chamber or Section-122/123 inequality without an isolate-population subtraction.
8. **Theorem authority is unchanged.** No canonical theorem-state file is modified.

The next concrete target is now a finite linear-algebra problem. Let `K_per` be the full rhombic period kernel and let `A_ear` be the signed incidence matrix of the `0.2155D` raw ear forest. We now know

\[
\dim K_{per}>0.1077D,
\qquad
\operatorname{rank}A_{ear}>0.2155D-o(D).
\]

A closure theorem would prove that `K_per` is not contained in the union of the ear non-shortening cones, or quantify the rank that the remaining exceptional-face and diameter rows must spend to enforce that containment. The alternative route is to push the explicit `1.0777D` physical-hole boundary and `0.2800D` empty-hole area into the canonical first-order attachment-cell detour ledgers.

**Disposition:** the live near-floor, small-singleton branch contains linearly many actual five-edge rhombic holes, not a possible period-free ear family. Those holes still leave a linear full period kernel, while the double-ear graph supplies a much larger train-coordinate shortening system. C-II remains open.