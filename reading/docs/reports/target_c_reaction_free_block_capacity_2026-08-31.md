> Generated reading edition · [exact source](../../../docs/reports/target_c_reaction_free_block_capacity_2026-08-31.md) · source SHA-256 `22940ea6f0ee9638b508b89adf768a5fe935620925df5b7896571ef283261c7c`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-1E8321744CFB","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C addendum: reaction-free blocks are pinned-rigid and pay bridge degree for internal diameter

**Date:** 2026-08-31  
**Repository branch:** `research/target-c-contact-minimal-neutral-chain-exclusion-2026-08-31`  
**Run type:** proof / local capacity reduction  
**Target:** C-II  
**Depends on:** C26, contact-minimal straight-motion argument, Eppstein's triangle-free penny-graph bound  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

C26 shows that every contact vertex with no positive diameter reaction is not an endpoint of any diameter pair. This makes every reaction-free bridge block a genuinely local strut framework: none of its moving vertices participates in an active upper-distance constraint.

Contact minimality then forces a strong local statement. If the outside endpoints of the incident contact bridges are pinned, the block has zero expansive cone. Hence its pinned contact rigidity matrix has full column rank.

For a reaction-free bridge block with

- `m` vertices,
- `e` internal unit contacts, and
- bridge-tree degree `k`,

this gives

$$
e+k\ge2m.
$$

Eppstein's bound for a connected triangle-free penny graph of graph diameter `delta` gives

$$
e\le2m-\delta-2.
$$

Therefore every nontrivial reaction-free bridge block satisfies the exact inequality

$$
\boxed{\delta\le k-2.}
$$

In particular a reaction-free two-edge-connected block with large graph or Euclidean diameter must emit proportionally many contact bridges. Summing over the bridge tree gives a global `O(D)` budget for the graph diameters of all reaction-free nontrivial blocks.

---

## 1. Setup

Work in the contact-minimal, triangle-free, fully force-visible Target C-II branch and choose a relative-interior normalized KKT stress, so `C_+=C`.

Let `X` be a reaction-free node of the positive-contact bridge-block tree. Write

$$
K:=V(X),
\qquad
m:=|K|.
\tag{C28.1}
$$

Let

$$
e_X:=|C[K]|
\tag{C28.2}
$$

be the number of internal unit contacts in the block, and let

$$
k_X:=\deg_{T_{br}}(X)
\tag{C28.3}
$$

be the number of positive-contact bridges incident to the block.

Because `X` is reaction-free, `K cap B_+=emptyset`. C26.1 then implies

$$
\boxed{K\cap Q=\varnothing,}
\tag{C28.4}
$$

where `Q` is the full source diameter-endpoint set. Thus no vertex of `K` is incident to any active diameter constraint, positive or weak.

Every contact edge leaving `K` is one of the `k_X` contact bridges by definition of the bridge-block decomposition.

---

## 2. The locally pinned expansive cone is zero

Pin every source vertex outside `K`. For a velocity assignment `v=(v_x)_{x in K}`, define the local expansive cone by the inequalities

$$
(x-y)\cdot(v_x-v_y)\ge0
\qquad(xy\in C[K]),
\tag{C28.5}
$$

and

$$
(x-y)\cdot v_x\ge0
\qquad(xy\in C,\ x\in K,\ y\notin K).
\tag{C28.6}
$$

The outside velocity is zero in C28.6.

### Theorem C28.1 (reaction-free block has zero pinned expansive cone)

The only velocity satisfying C28.5-C28.6 is

$$
\boxed{v_x=0\quad(x\in K).}
\tag{C28.7}
$$

#### Proof

Suppose `v` were nonzero. Move only the vertices of `K` along the straight motion

$$
x(t)=x+t v_x,
\tag{C28.8}
$$

and keep every vertex outside `K` fixed.

For every internal contact and every incident contact bridge, the squared length is

$$
|r+t\dot r|^2
=1+2t\,r\cdot\dot r+t^2|\dot r|^2
\ge1
\tag{C28.9}
$$

for all sufficiently small `t>0` by C28.5-C28.6.

By C28.4, no active diameter pair is incident to a moved vertex. Hence every active diameter pair is between fixed outside vertices and remains exactly unchanged. Every other pair incident to `K` has strict two-sided slack at `t=0`: its distance is strictly larger than one and strictly smaller than `D`. Finiteness and continuity preserve those strict inequalities for all sufficiently small positive `t`.

Thus the straight motion remains unit-separated, has diameter exactly `D`, and creates no new unit contact. It remains triangle-free.

It remains to show that at least one old contact is broken. If some contact inequality in C28.5-C28.6 has positive first derivative, that contact becomes strictly longer immediately. Otherwise every incident contact has zero first derivative. Then C28.9 becomes strict on every contact whose relative velocity is nonzero.

If every internal and bridge contact had zero relative velocity, then the velocity would be constant on the connected block `K`; any incident bridge has fixed outside endpoint, forcing that constant to be zero. A reaction-free bridge block cannot be the whole positive contact component, because that component contains positive diameter endpoints. Therefore at least one incident bridge exists. Hence a nonzero `v` forces at least one contact to become strictly longer.

The resulting triangle-free global minimizer has fewer unit contacts than the contact-minimal source, contradiction. Therefore the cone is zero. `\square`

---

## 3. Full pinned rank

Let `R_X` be the rigidity matrix whose columns are the `2m` velocity coordinates of vertices in `K` and whose rows are the linear contact forms in C28.5-C28.6.

### Corollary C28.2 (local full rank)

$$
\boxed{\operatorname{rank}R_X=2m.}
\tag{C28.10}
$$

Consequently,

$$
\boxed{e_X+k_X\ge2m.}
\tag{C28.11}
$$

#### Proof

If `R_X v=0` for nonzero `v`, then both `v` and `-v` satisfy the local expansive inequalities, contradicting Theorem C28.1. Thus the kernel is zero and the rank is `2m`. The row count is `e_X+k_X`, proving C28.11. `\square`

This is a local contact-minimal rank statement. No diameter row participates because C26 removed all diameter constraints from the reaction-free block.

---

## 4. Eppstein converts rank into a bridge-degree/diameter inequality

Assume now that `X` is nontrivial, so `m>=2`. The internal contact graph `C[K]` is connected and triangle-free, and it is a penny graph. Let

$$
\delta_X:=\operatorname{diam}_{graph}(C[K]).
\tag{C28.12}
$$

The canonical Eppstein bound gives

$$
\boxed{
e_X\le2m-\delta_X-2.}
\tag{C28.13}
$$

Combine with C28.11.

### Theorem C28.3 (block diameter costs bridge degree)

Every nontrivial reaction-free bridge block satisfies

$$
\boxed{k_X\ge\delta_X+2.}
\tag{C28.14}
$$

Equivalently,

$$
\boxed{\delta_X\le k_X-2.}
\tag{C28.15}
$$

Since every contact edge has Euclidean length one,

$$
\boxed{\operatorname{diam}_{Eucl}(K)\le\delta_X\le k_X-2.}
\tag{C28.16}
$$

A nontrivial reaction-free block therefore cannot be a large hidden two-dimensional event of bounded bridge-tree degree.

As immediate special cases:

- degree `3` is impossible for a nontrivial reaction-free block;
- degree `4` forces graph diameter at most `2`;
- degree `5` forces graph diameter at most `3`.

Together with C26, a reaction-free degree-three bridge-tree node must therefore be a single contact vertex.

---

## 5. Exact finite packing capacity of one reaction-free block

Choose any root vertex of `K`. Every vertex is at graph distance at most `delta_X`, hence Euclidean distance at most `delta_X` from the root. The closed radius-`1/2` disks around the unit-separated vertices of `K` are disjoint and lie inside the disk of radius `delta_X+1/2` about the root.

Therefore

$$
m\frac\pi4
\le
\pi\left(\delta_X+\frac12\right)^2.
\tag{C28.17}
$$

### Corollary C28.4 (degree-capacity bound)

$$
\boxed{
m\le(2\delta_X+1)^2\le(2k_X-3)^2.}
\tag{C28.18}
$$

Thus a reaction-free block containing `Theta(D^2)` positive-contact vertices would require bridge-tree degree `Theta(D)`.

The estimate is deliberately elementary and nonsharp; its role is to turn the exact graph-diameter theorem C28.15 into a finite population bound without importing a lattice or density theorem.

---

## 6. Global budget for reaction-free block diameters

Let `R` be the number of loaded bridge blocks and let `\mathcal R` be the family of nontrivial reaction-free bridge blocks. Every leaf block is loaded. For a finite tree,

$$
L
=2+\sum_{X:\deg X\ge3}(\deg X-2),
\tag{C28.19}
$$

where `L` is the number of leaves. Since `L<=R`,

$$
\sum_{X\in\mathcal R}(k_X-2)
\le R-2.
\tag{C28.20}
$$

Combine with C28.15.

### Theorem C28.5 (global reaction-free diameter budget)

$$
\boxed{
\sum_{X\in\mathcal R}\delta_X
\le R-2
\le |B_+|-2
\le\pi D-2.}
\tag{C28.21}
$$

The same bound holds with each `delta_X` replaced by the Euclidean diameter of the block.

Thus all nontrivial reaction-free two-edge-connected events together have only `O(D)` total internal graph diameter.

This is stronger than the earlier `O(D)` count of structural bridge-tree nodes: a single reaction-free block cannot hide arbitrarily large internal extent without paying proportionally in bridge degree, and those degree surpluses share one global tree budget.

---

## 7. A high-degree-block dichotomy for large reaction-free populations

Let

$$
M_{rf}:=\sum_{X\in\mathcal R}|V(X)|
\tag{C28.22}
$$

and put

$$
K_{max}:=\max_{X\in\mathcal R}k_X.
\tag{C28.23}
$$

For nontrivial reaction-free blocks, C28.14 gives `k_X>=4`, so

$$
k_X\le2(k_X-2).
\tag{C28.24}
$$

Hence C28.20 gives

$$
\sum_{X\in\mathcal R}k_X
\le2(R-2)
\le2|B_+|.
\tag{C28.25}
$$

Using C28.18 and `(2k-3)^2<=4k^2`,

$$
M_{rf}
\le4\sum_X k_X^2
\le4K_{max}\sum_Xk_X
\le8K_{max}|B_+|.
\tag{C28.26}
$$

Since `|B_+|<=pi D`,

$$
\boxed{M_{rf}\le8\pi D\,K_{max}.}
\tag{C28.27}
$$

Therefore if, along a sequence, reaction-free nontrivial bridge blocks contain at least `rho D^2` vertices, then some such block satisfies

$$
\boxed{
K_{max}\ge\frac{\rho}{8\pi}D.
}
\tag{C28.28}
$$

So a macroscopically populated reaction-free block phase necessarily contains a block incident to linearly many contact bridges.

This conditional statement is not yet a Level I contradiction because the positive contact core need not currently be known to contain `Theta(D^2)` source vertices.

---

## 8. C-II effect

C26 removed neutral series transport. C28 now controls the size of the genuinely two-dimensional reaction-free events that remain.

The bridge branch has the exact local alternatives:

```text
reaction-free bridge-tree node X
    singleton:
        degree >=3 by C26
    nontrivial block:
        pinned expansive cone = 0
        e_X + k_X >= 2|X|
        graph diameter delta_X <= k_X-2
        Euclidean diameter <= k_X-2
        |X| <= (2k_X-3)^2
```

Globally,

```text
sum reaction-free block graph diameters <= |B_+|-2 <= pi D-2.
```

Thus a future loaded-event transport theorem can treat reaction-free blocks as quantitatively charged events rather than arbitrary black boxes.

A high-value continuation is to combine C28.21 with C23 weighted bridge depth and C27 macroscopic bridge cuts: either deep transport repeatedly passes through loaded blocks, or it spends the finite `O(D)` reaction-free-diameter budget; in the latter case a macroscopic reaction-free block forces high bridge degree and hence many disjoint loaded boundary branches.

---

## 9. Regression audit

- **Reaction-free singleton of degree three:** allowed. Three positive unit-contact forces can positively balance at one non-diameter vertex.
- **Unit square block with four bridge attachments:** compatible with the numerical inequalities `delta=2`, `k=4`. The theorem does not claim such a locally pinned gadget is globally realizable in a minimizer.
- **Large rhombic/penny block with bounded number of bridge attachments:** excluded in the reaction-free C-II setting by C28.15/C28.18; this uses contact minimality and absence of all diameter constraints on the block.
- **Loaded block:** not covered. Positive diameter reactions supply additional pinned rows and can support large blocks with small bridge degree.
- **Weak-contact branch:** not covered because `C_+=C` is essential to C26 and hence to C28.4.
- **Bridge-free whole positive network:** loaded, not reaction-free, because positive support contains positive diameter endpoints.

No generic global rigidity theorem is used; the zero-cone argument is the same exact straight-motion mechanism already canonical in the repository.

---

## 10. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

C28 reaction-free block capacity:
In fully force-visible C-II, C26 implies every reaction-free contact vertex is not a
source diameter endpoint.  Let X be a reaction-free bridge block with m vertices,
e_X internal contacts, and k_X incident contact bridges.  Pin all outside vertices.
Any nonzero local expansive velocity would integrate by the straight motion to a
same-D triangle-free minimizer with fewer contacts, because no moved vertex participates
in any diameter constraint.  Therefore the local expansive cone is zero and
    rank R_X = 2m,
    e_X + k_X >= 2m.

For nontrivial X, Eppstein gives
    e_X <= 2m - delta_X - 2,
so
    delta_X <= k_X - 2,
and Euclidean diameter(X) <= k_X-2.
Elementary disk packing gives
    |X| <= (2k_X-3)^2.

Tree degree surplus yields the global budget
    sum_{nontrivial reaction-free X} delta_X
      <= R-2 <= |B_+|-2 <= pi D-2.

If reaction-free nontrivial blocks contain rho D^2 vertices, some block has
    degree >= (rho/(8*pi))D.

Next use:
combine this O(D) reaction-free diameter budget with C23 weighted depth and C27
macroscopic bridge cuts to force deep bridge transport to spend linearly many loaded
boundary events or one linearly high-degree reaction-free block.
```
