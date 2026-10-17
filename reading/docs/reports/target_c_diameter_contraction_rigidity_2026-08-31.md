> Generated reading edition · [exact source](../../../docs/reports/target_c_diameter_contraction_rigidity_2026-08-31.md) · source SHA-256 `90903fdfd2791896c0c1a0be9f8bf8236a4693a5d7db90256df86cdd434ea16d`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 5 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-76F0B92FBF5C","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C addendum: diameter-contracted contact rigidity

**Date:** 2026-08-31  
**Repository state:** `188a2b81fbc292db6d6873fe2c86b6924a5115ea`  
**Run type:** proof / exact structural reduction  
**Target:** C-II  
**External web search:** not used  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

In the fully force-visible branch the complete unit-contact graph has one connected
nontrivial component spanning Euclidean diameter `D`.  Contact minimality gives a new
finite-amplitude rigidity statement that does not use KKT multipliers: contract the
**full** diameter graph into translation classes and allow one planar translation for
each class.  Any class motion tangent to every unit contact preserves every diameter
pair exactly and can only lengthen unit contacts along the resulting straight motion.
Hence a nontrivial such motion would delete a contact while keeping diameter exactly
`D`, contradicting contact minimality.

Therefore the diameter-contracted contact direction matrix has kernel exactly the two
common translations.  This forces a two-per-cut contact-connectivity condition on the
quotient and, combined with Eppstein's triangle-free penny-graph edge bound, gives the
exact necessary inequality

```math
\boxed{2r_D\ge \delta_C+m_{\rm same}\ge\lceil D\rceil,}
```

where `r_D` is the connectivity rank contributed by the full diameter graph on the
contact component, `delta_C` is its contact-graph diameter, and `m_same` counts unit
contacts whose endpoints already lie in one diameter-translation class.

This is a new C-II obstruction.  In particular every surviving fully force-visible
contact-minimal configuration needs diameter-graph connectivity rank at least
`ceil(D)/2` on the force-carrying contact component.

---

## 1. Setup

Let `A` be a contact-minimal, diametrally saturated, triangle-free global minimizer of
diameter `D>1`, and assume the Target C-II condition
```math
C=C_*.
\tag{C23.1}
```
Choose a relative-interior normalized KKT stress.  Then every unit contact has positive
stress, so the canonical support-connectivity theorem implies that all nonisolated
unit contacts form one connected component
```math
G_C=(V,C),
\qquad v=|V|,
\tag{C23.2}
```
and this component contains a pair of vertices at Euclidean distance `D`.
Vertices outside `V` are contact-isolated and will play no role in the contact count.

Let `H` be the **full** diameter graph of `A`, not merely its KKT-positive or strong
subgraph.  Define an equivalence relation on `V` by
```math
x\sim_D y
\iff
x=y\text{ or }x,y\text{ lie in the same connected component of }H.
\tag{C23.3}
```
Thus a contact vertex not incident with any diameter edge is a singleton class.  Let
```math
\mathcal Q=V/{\sim_D},
\qquad k=|\mathcal Q|,
\qquad r_D=v-k.
\tag{C23.4}
```
Equivalently, if `q_D` contact vertices belong to nontrivial components of `H` and
`c_D` distinct components of `H` meet `V`, then
```math
r_D=q_D-c_D.
\tag{C23.5}
```
Components meeting `V` in only one vertex contribute zero, as they should.

For a contact edge `ij`, call it **diameter-internal** when
```math
[i]=[j]\in\mathcal Q.
\tag{C23.6}
```
Let
```math
m_{\rm same}
=|\{ij\in C:[i]=[j]\}|,
\qquad
m_\times=|C|-m_{\rm same}.
\tag{C23.7}
```

---

## 2. Diameter-class translation framework

Assign a translation vector
```math
t_Q\in\mathbb R^2
\qquad(Q\in\mathcal Q).
\tag{C23.8}
```
For every `x in V`, define
```math
w_x=t_{[x]}.
\tag{C23.9}
```
Extend `w` to every point of `A` as follows.  On a component of the full diameter graph
that meets `V`, use the translation assigned to its class on all vertices of that
diameter component.  On a diameter component disjoint from `V`, use zero translation.
On a vertex outside `V` and outside the diameter graph, also use zero.

Then for every diameter pair `ij in H`,
```math
\boxed{w_i=w_j.}
\tag{C23.10}
```
Therefore every active diameter pair remains exactly at distance `D` along the straight
motion `p_i(s)=p_i+s w_i`.

For each contact `ij in C`, impose the tangency equation
```math
(p_i-p_j)\cdot(t_{[i]}-t_{[j]})=0.
\tag{C23.11}
```
Diameter-internal contacts give the zero row automatically.  Let
```math
T_D:\mathbb R^{2\mathcal Q}\longrightarrow\mathbb R^{C}
\tag{C23.12}
```
be the matrix of these contact tangency rows.

---

## 3. Finite-amplitude release theorem

### Theorem C23.1 (diameter-contracted contact rigidity)

For a contact-minimal C-II source,
```math
\boxed{
\ker T_D
=
\{(t_Q)_Q:t_Q=t\text{ for one }t\in\mathbb R^2\}.
}
\tag{C23.13}
```
Consequently
```math
\boxed{
\operatorname{rank}T_D=2k-2=2(v-r_D)-2.
}
\tag{C23.14}
```

#### Proof

Common translations plainly lie in the kernel.  Suppose conversely that
`t=(t_Q)` lies in `ker T_D` and is not common.  Because the contact graph `G_C` is
connected, some contact edge `ij` has
```math
t_{[i]}\ne t_{[j]}.
\tag{C23.15}
```
Extend the class translations to the full source as above and consider
```math
p_x(s)=p_x+s w_x.
\tag{C23.16}
```
For every full diameter pair, (C23.10) gives
```math
|p_i(s)-p_j(s)|=D
\tag{C23.17}
```
for all `s`.

For a unit contact `ij`, the tangency equation gives
```math
\begin{aligned}
|p_i(s)-p_j(s)|^2
&=1
+2s(p_i-p_j)\cdot(w_i-w_j)
+s^2|w_i-w_j|^2\\
&=1+s^2|w_i-w_j|^2
\ge1.
\end{aligned}
\tag{C23.18}
```
The contact from (C23.15) is strictly longer than one for every `s ne0`.

Every pair that is neither a contact nor a diameter pair has a strict distance margin
inside `(1,D)`.  There are finitely many pairs, so for all sufficiently small nonzero
`s`, all such distances remain strictly between one and `D`.  Hence `A(s)` is
unit-separated and has diameter exactly `D`.  Since `D=D(n)`, it is another global
minimizer.  Its unit-contact graph is a proper subgraph of the original one and no new
unit contact appears.  Triangle-freeness is therefore preserved.

This contradicts contact minimality.  Thus every kernel vector is common translation,
proving (C23.13).  The rank formula follows by rank-nullity. `\square`

The theorem is genuinely finite-amplitude.  It is not a generic rigidity statement
and it does not require a KKT stress beyond the C-II fact that the entire contact graph
is one connected force-carrying component.

---

## 4. Every partition needs two contact constraints per relative translation

Let
```math
\mathcal P=\{P_1,\ldots,P_p\}
\tag{C23.19}
```
be any partition of the diameter classes `mathcal Q`.  Let `e_C(mathcal P)` denote the
number of unit-contact edges whose two diameter classes lie in different parts of the
partition.

### Theorem C23.2 (two-per-partition contact connectivity)

For every partition with `p>=1`,
```math
\boxed{
e_C(\mathcal P)\ge2(p-1).}
\tag{C23.20}
```

#### Proof

Restrict the class translations to be constant inside each partition block:
```math
t_Q=s_a\in\mathbb R^2
\qquad(Q\in P_a).
\tag{C23.21}
```
There are `2p` scalar variables.  Contact edges internal to one partition block impose
no condition on this restricted space.  The crossing edges impose at most
`e_C(mathcal P)` homogeneous scalar equations.

If `e_C(mathcal P)<2p-2`, their common kernel has dimension greater than two.  It
therefore contains a block translation not equal on all `p` parts.  The quotient of
the connected contact graph by the diameter classes is connected, so some contact edge
joins two parts receiving different translations.  The finite-amplitude argument of
Theorem C23.1 then deletes that contact while fixing every diameter pair exactly,
contradicting contact minimality.  Hence (C23.20). `\square`

For the discrete partition into all `k` diameter classes,
```math
\boxed{
m_\times\ge2k-2=2(v-r_D)-2.}
\tag{C23.22}
```

This is stronger than merely requiring the quotient contact graph to be connected or
bridgeless.

---

## 5. Combine with the triangle-free penny-graph deficit

Let
```math
\delta_C=\operatorname{diam}_{\rm graph}(G_C).
\tag{C23.23}
```
The component contains two points at Euclidean distance `D`, and every contact edge has
length one, so
```math
\boxed{\delta_C\ge\lceil D\rceil.}
\tag{C23.24}
```
Eppstein's connected triangle-free penny-graph bound gives
```math
\boxed{|C|\le2v-\delta_C-2.}
\tag{C23.25}
```
On the other hand (C23.22) and (C23.7) give
```math
|C|
=m_\times+m_{\rm same}
\ge
2(v-r_D)-2+m_{\rm same}.
\tag{C23.26}
```
Comparing the two inequalities proves the main numerical consequence.

### Theorem C23.3 (diameter-rank lower bound)

Every contact-minimal triangle-free C-II source satisfies
```math
\boxed{
2r_D\ge\delta_C+m_{\rm same}
\ge\lceil D\rceil+m_{\rm same}.
}
\tag{C23.27}
```
In particular
```math
\boxed{
2r_D\ge\lceil D\rceil,
\qquad
r_D\ge\left\lceil\frac{\lceil D\rceil}{2}\right\rceil.
}
\tag{C23.28}
```

Since connecting `q_D` marked contact vertices into `c_D` diameter components requires
at least `q_D-c_D=r_D` diameter edges even when paths are allowed to use vertices
outside the contact component,
```math
\boxed{|H|\ge r_D\ge\left\lceil\frac{\lceil D\rceil}{2}\right\rceil.}
\tag{C23.29}
```

Every contact whose endpoints already lie in one diameter component strengthens the
required diameter rank by one half through the `m_same` term.

---

## 6. Structural interpretation

Theorem C23.1 says that the full diameter graph acts as a collection of rigid
translation ties.  After those ties are contracted, the unit contacts must remove
**all** relative translational freedom of the remaining classes.  Each unit contact
provides only one scalar tangency equation, so every partition into `p` class groups
must have at least `2(p-1)` crossing contacts.

The triangle-free penny graph simultaneously loses at least `delta_C+2` edges from the
planar `2v` scale.  The only way both facts can hold is for the diameter graph to have
connectivity rank at least half of that graph-diameter deficit.  Thus the macroscopic
unit-contact path forced by Target C support connectivity must be paid for by a
macroscopic amount of diameter connectivity.

This is independent of the reciprocal bridge decomposition C20--C22 and therefore
cuts across both the bridge-heavy and two-edge-connected C-II subbranches.

---

## 7. Regression audit

### Unit square

The diameter graph is the two-diagonal matching.  Thus `v=4`, `r_D=2`,
`m_same=0`, while the contact cycle has graph diameter two.  The bound
`2r_D>=delta_C` holds with room to spare.  The quotient has two classes and four
crossing contact rows, enough to kill relative translation.

### Regular pentagon

The diameter graph is one 5-cycle, hence `r_D=4` and all five side contacts are
diameter-internal.  Thus `m_same=5` and `delta_C=2`; the inequality reads `8>=7`.
This example shows why the `m_same` correction is real and why diameter cycles can
supply contact rigidity without many quotient edges.

### Straight contact chain

If its only diameter edge joins the two endpoints, then `r_D=1` while
`delta_C` is the chain length.  The theorem excludes a long chain from being a
contact-minimal C-II global minimizer: it admits transverse diameter-fixing contact
release.  This does not contradict C21's local straight-chain regression, which never
claimed global contact minimality.

### KKT-invisible source points

They are allowed.  The diameter-class translation is extended through every full
diameter component, including contact-isolated vertices.  Only the connected contact
component enters the rank count.

### Weak diameter pairs

They are not a problem: C23 fixes **every** full diameter pair exactly.  The theorem
does not assume `H=H_*`.

---

## 8. Exact next Target C question

C-II now has an additional global requirement:
```math
\boxed{
r_D\ge\lceil\lceil D\rceil/2\rceil.}
\tag{C23.30}
```
The highest-value continuation is to combine this macroscopic diameter connectivity
with the already-promoted diameter geometry:

- no diametral triangle for sufficiently large sources;
- shared-endpoint diameter angles below `50.7608...` degrees asymptotically;
- diameter cycles have length `Omega(sqrt(D))`;
- positive diameter reactions live on the two-dimensional force hull with reciprocal
  perimeter at most `2D`.

A sufficient closing theorem would show that a planar diameter graph on the saturated
hull cannot have connectivity rank `>=D/2` while coexisting with the two-per-partition
contact requirement (C23.20) and the global minimum-diameter packing bounds.
