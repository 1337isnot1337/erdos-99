<!-- theorem-state: {"artifact_id":"ART-887D1B04EDE1","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C addendum: positive stress on diameter classes

**Date:** 2026-08-31  
**Run type:** proof / exact structural reduction  
**Target:** C-II  
**Depends on:** Target C force-hull/support-connectivity theorems and C23 diameter-contracted contact rigidity  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

C23 contracts the full diameter graph into translation classes and proves that the
cross-class contact direction matrix has kernel only the two common translations.  In
C-II the relative-interior KKT stress gives more: after summing equilibrium over one
full-diameter class, all positive diameter forces and class-internal contact forces
cancel.  The remaining cross-class unit contacts therefore carry a strictly positive
self-stress on the contracted translation framework.

This adds one exact row beyond the C23 rigidity threshold for every nontrivial
partition of diameter classes.  It also identifies every contact-component endpoint
of the **full** diameter graph with a positive KKT reaction vertex.  Consequently the
C23 macroscopic diameter-rank lower bound forces a macroscopic loaded force-hull
boundary in every relative-interior C-II stress.

---

## 1. Every contact-visible full diameter endpoint is positively loaded

Use C23 notation.  Let `G_C=(V,C)` be the connected nontrivial contact component and
let
\[
B_+=V(H_+)
\tag{C24.1}
\]
be the positive diameter-reaction vertices of a relative-interior normalized KKT
stress.  In C-II, `C_+=C`, and the canonical force-hull theorem gives
\[
\operatorname{conv}B_+
=
\operatorname{conv}V.
\tag{C24.2}
\]

Let
\[
V_D=V\cap V(H)
\tag{C24.3}
\]
be the contact-component vertices incident with at least one edge of the **full**
diameter graph.

### Lemma C24.1 (full diameter endpoint = positive reaction vertex on the contact component)

\[
\boxed{V_D=B_+.}
\tag{C24.4}
\]

#### Proof

The inclusion `B_+ subset V_D` is immediate: every positive diameter edge is a full
diameter edge, and the support-connectivity theorem puts both of its endpoints in the
positive contact component `V`.

Conversely let `b in V_D`, and choose a full diameter partner `z` with
`|b-z|=D`.  Put
\[
u=(b-z)/D.
\]
For any other source point `x`, the diameter inequality `|x-z|<=D` gives
\[
|x-b|^2+2D\,u\cdot(x-b)\le0.
\tag{C24.5}
\]
Thus
\[
u\cdot(x-b)<0
\qquad(x\ne b).
\tag{C24.6}
\]
So `b` is a uniquely exposed vertex of `conv A`, and hence also an extreme point of
the smaller convex hull `conv V` containing it.  Equation (C24.2) says
`conv V=conv B_+`.  An extreme point of the convex hull of a finite set must belong to
that set, so `b in B_+`. `\square`

Therefore the C23 quantity `q_D` is exactly
\[
\boxed{q_D=|B_+|.}
\tag{C24.7}

If `c_D` full-diameter components meet `V`, then
\[
r_D=|B_+|-c_D.
\tag{C24.8}
\]

---

## 2. Cross-class KKT equilibrium

Let `Q` be one C23 diameter class.  Sum the KKT equilibrium equations over the contact
vertices in `Q`.

Every positive diameter edge has both endpoints in `V` and, being an edge of the full
diameter graph, lies entirely inside one diameter class.  Its two endpoint forces
cancel in the sum.  Every contact edge internal to `Q` cancels as well.  Hence only
cross-class contacts remain.

### Lemma C24.2 (positive self-equilibrium of every diameter class)

For every class `Q`,
\[
\boxed{
\sum_{\substack{ij\in C\\i\in Q,\ j\notin Q}}
\alpha_{ij}(p_i-p_j)=0.
}
\tag{C24.9}
\]
All coefficients in the sum are strictly positive.

More generally, if `mathcal U` is any union of diameter classes, then
\[
\boxed{
\sum_{\substack{ij\in C\\i\in\mathcal U,\ j\notin\mathcal U}}
\alpha_{ij}(p_i-p_j)=0.
}
\tag{C24.10}

#### Proof

The first identity is the classwise KKT sum just described.  Sum (C24.9) over all
classes in `mathcal U`; contacts internal to the union cancel pairwise, leaving
(C24.10). `\square`

Thus every proper class cut is supported by a positive vector equilibrium.  In
particular it cannot consist of one crossing contact, and if it consists of two their
contact directions would have to be exactly antiparallel.

---

## 3. Every partition has a positive self-stress

Let
\[
\mathcal P=\{P_1,\ldots,P_p\}
\tag{C24.11}
\]
be a partition of the C23 diameter classes, with `p>=2`.  Restrict class translations
to one vector `s_a in R^2` per partition block.  Let
\[
T_{\mathcal P}
\tag{C24.12}
\]
be the resulting contact tangency matrix, containing one row for every contact whose
endpoints lie in different partition blocks.

C23's finite-amplitude argument applies verbatim on this restricted block-translation
space: any noncommon kernel vector would preserve every full diameter pair exactly and
strictly open at least one contact.  Therefore
\[
\boxed{
\operatorname{rank}T_{\mathcal P}=2p-2.
}
\tag{C24.13}

On the other hand, sum Lemma C24.2 inside every partition block.  The strictly positive
KKT coefficients on the partition-crossing contacts satisfy
\[
\boxed{
T_{\mathcal P}^{\mathsf T}\alpha_{\mathcal P}=0,
\qquad
\alpha_{\mathcal P}>0.
}
\tag{C24.14}

The vector is nonzero because the contracted contact graph is connected and `p>=2`.
Thus `T_mathcalP` has positive left nullity at least one.

### Theorem C24.3 (positive-stress partition surplus)

For every partition into `p>=2` diameter-class groups,
\[
\boxed{
e_C(\mathcal P)\ge2p-1.}
\tag{C24.15}

In particular every proper nonempty union of diameter classes has at least three unit
contacts to its complement.

For the discrete partition into all `k` C23 classes, if `k>=2`,
\[
\boxed{
m_\times\ge2k-1=2(v-r_D)-1.}
\tag{C24.16}

#### Proof

Equation (C24.13) gives row rank `2p-2`, while (C24.14) gives a nonzero linear
dependence among the crossing rows.  Therefore their number is at least
`(2p-2)+1=2p-1`. `\square`

So the diameter-contracted contact multigraph is not merely two-per-partition rigid;
it is positively self-stressed across every partition.  Its edge-connectivity is at
least three in the ordinary cut sense.

---

## 4. Strengthened C23 numerical inequality

Assume `k>=2`.  Combining (C24.16) with the C23 notation
\[
|C|=m_\times+m_{\rm same}
\tag{C24.17}
\]
gives
\[
|C|
\ge2(v-r_D)-1+m_{\rm same}.
\tag{C24.18}
\]
Eppstein's triangle-free penny-graph bound remains
\[
|C|\le2v-\delta_C-2.
\tag{C24.19}
\]
Therefore:

### Theorem C24.4 (positive-stress diameter-rank bound)

If the diameter contraction has at least two classes,
\[
\boxed{
2r_D
\ge
\delta_C+m_{\rm same}+1
\ge
\lceil D\rceil+m_{\rm same}+1.
}
\tag{C24.20}

If `k=1`, then `r_D=v-1` and all contact vertices lie in one full-diameter component;
C23.3 remains the appropriate bound.  Thus in all cases the coarser universal
conclusion
\[
2r_D\ge\lceil D\rceil
\tag{C24.21}
\]
remains valid.

---

## 5. Macroscopic loaded force boundary

Because `r_D=|B_+|-c_D` and `c_D>=1`, C23.3 immediately gives
\[
\boxed{
|B_+|
\ge
1+
\left\lceil\frac{\lceil D\rceil}{2}\right\rceil.
}
\tag{C24.22}

Thus every relative-interior normalized KKT stress in C-II has a **linear** number of
positive diameter-reaction vertices on the force hull.

Every vertex of `B_+` is incident with at least one positive diameter edge, so
\[
2|H_+|=\sum_{b\in B_+}\deg_{H_+}(b)\ge|B_+|.
\tag{C24.23}
\]
Hence
\[
\boxed{
|H_+|
\ge
\left\lceil\frac{|B_+|}{2}\right\rceil
\ge
\left\lceil
\frac{1+\lceil\lceil D\rceil/2\rceil}{2}
\right\rceil.
}
\tag{C24.24}

Asymptotically every relative-interior C-II stress therefore uses at least
`D/4+O(1)` positive diameter edges and at least `D/2+O(1)` loaded boundary vertices.

The reciprocal polygon consequently has at least `D/2+O(1)` nonzero boundary edges.
This is compatible with the canonical perimeter interval
\[
1.806963\ldots D+o(D)
\le P_*\le2D,
\tag{C24.25}
\]
so it is not yet a contradiction.

---

## 6. Low-degree consequence

Take a contact vertex `x in V` that is a singleton diameter class.  Partition the
classes into `{x}` and its complement.  The crossing contacts are exactly the contact
edges incident with `x`.  Theorem C24.3 therefore gives
\[
\boxed{
\deg_C(x)\ge3.
}
\tag{C24.26}

Thus every contact vertex of degree at most two belongs to a nontrivial full-diameter
component.  Eppstein's 2-degeneracy/low-degree structure cannot be supported entirely
by diameter-free interior vertices in a contact-minimal C-II source.

---

## 7. Exact C-II frontier after C24

C23--C24 impose three simultaneous macroscopic facts on every C-II survivor:

1. the full diameter graph contributes connectivity rank at least `D/2` on the
   force-carrying contact component;
2. every diameter-class partition has at least `2p-1` cross contacts carrying a
   positive quotient self-stress;
3. every relative-interior KKT stress loads at least `D/2+O(1)` force-hull vertices
   and at least `D/4+O(1)` positive diameter edges.

This requirement cuts across both C20--C22 articulation alternatives.  A closing
continuation should combine the class-partition rigidity with the global geometry of
the full diameter graph (caterpillar/odd-cycle thrackle structure, the shared-endpoint
angle bound, and long cycle girth) rather than attempt another local KKT coefficient
estimate.
