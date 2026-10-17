> Generated reading edition · [exact source](../../../docs/reports/target_c_fully_visible_no_neutral_vertices_2026-08-31.md) · source SHA-256 `ae901c3b256e8e3dc420701a3f2ce7bbba8d2815a4df401b483157aad6870cf6`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-0EF64375DDAE","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C addendum: fully force-visible contact cores have no neutral degree-two vertices

**Date:** 2026-08-31  
**Repository base:** `5d9ed6a99c63042c434fd4a7160bf96bced6c507`  
**Run type:** proof / C-II structural collapse  
**Target:** C-II  
**Depends on:** canonical Lemmas 5.1 and 5.3, contact-minimal Theorem 6.1, Target C C21-C25  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

The previous Target C bridge reductions allowed exact straight constant-stress chains of unloaded degree-two positive-contact vertices. In the fully force-visible C-II branch, those chains cannot occur at all.

The point is simple but stronger than the earlier suppression theorem. Choose a relative-interior normalized KKT stress in the fully force-visible branch, so every unit contact has positive contact stress. At any positive-contact vertex with no positive diameter reaction, equilibrium writes the vertex as a strict convex combination of its contact neighbors. Hence that vertex is not an extreme point of the source convex hull and therefore is not an endpoint of any diameter pair. Contact minimality then applies directly: every non-diameter nonisolated vertex must be strictly surrounded by its unit contacts and has contact degree 3, 4, or 5.

Thus:

- every unloaded contact vertex in C-II has full contact degree 3, 4, or 5;
- no unloaded degree-two positive-contact vertex exists;
- every C21 neutral chain has length one at the skeleton level: there are no suppressed internal vertices and every skeleton length is `L_E=1`;
- every C22 reaction-free two-terminal region is impossible;
- the bridge-block tree has no reaction-free degree-two node;
- the C24 common diameter-route intersection contains at most one bridge;
- if positive bridge stress is a fixed fraction of `D^2`, then there must be linearly many positive diameter-reaction vertices.

This removes the principal one-dimensional transport loophole from the fully force-visible branch. The remaining bridge phase is no longer “long straight corridors with occasional events”; every unit of bridge depth passes directly between loaded or genuinely branching/two-edge-connected blocks.

---

## 1. Setup

Let `A` be a contact-minimal, diametrally saturated, triangle-free global minimizer in the Target C fully force-visible branch

$$
C=C_*.
\tag{C26.1}
$$

Choose a relative-interior point of the normalized KKT polytope. Then its positive contact support is exactly the full unit-contact graph:

$$
C_+=C,
\tag{C26.2}
$$

and its positive diameter support is the maximal support `H_+ = H_*`. Let

$$
B_+=V(H_+).
\tag{C26.3}
$$

At every contact vertex `x`, KKT equilibrium is

$$
\sum_{xy\in C}\alpha_{xy}(x-y)
=
\sum_{xz\in H_+}\beta_{xz}(x-z),
\qquad \alpha_{xy}>0.
\tag{C26.4}
$$

The contact-minimal representative remains contact-minimal after Target C diametral saturation because that normalization moves only contact-isolated points and preserves the abstract unit-contact graph.

Let `Q` denote the full set of source diameter endpoints, including endpoints of weak diameter constraints.

---

## 2. Unloaded contact vertices are not diameter endpoints

### Theorem C26.1 (loaded-or-strict-barycenter dichotomy)

If `x` is incident to a unit contact and

$$
x\notin B_+,
\tag{C26.5}
$$

then

$$
\boxed{
x\notin Q.}
\tag{C26.6}
$$

More precisely,

$$
\boxed{
x=
\frac{\sum_{xy\in C}\alpha_{xy}y}
     {\sum_{xy\in C}\alpha_{xy}},}
\tag{C26.7}
$$

with every coefficient in the convex combination strictly positive.

#### Proof

Because `x notin B_+`, the right side of C26.4 is zero. Therefore

$$
\left(\sum_{xy\in C}\alpha_{xy}\right)x
=
\sum_{xy\in C}\alpha_{xy}y.
$$

The denominator is positive because `x` is incident to a contact, and every incident contact coefficient is strictly positive by C26.2. This gives C26.7.

The convex combination is nontrivial: every contact neighbor differs from `x`. Hence `x` is not an extreme point of `conv A`. Canonical Lemma 5.1 says every endpoint of every diameter pair is an extreme point of `conv A`. Therefore `x notin Q`. `\square`

This is stronger than saying that `x` has no positive diameter reaction. It cannot be incident to a weak active diameter constraint either.

### Corollary C26.2 (all source diameter endpoints in the contact core are positively loaded)

If `x` is nonisolated in the unit-contact graph and `x in Q`, then

$$
\boxed{x\in B_+.}
\tag{C26.8}
$$

Thus any weak diameter endpoint outside `B_+` must be contact-isolated.

---

## 3. Contact minimality removes every unloaded degree-two vertex

Canonical Theorem 6.1 says that in a contact-minimal triangle-free global minimizer, every non-diameter nonisolated vertex is strictly surrounded by its unit contacts and has contact degree 3, 4, or 5.

Combine this with Theorem C26.1.

### Theorem C26.3 (no neutral degree-two vertex in C-II)

For every contact vertex `x notin B_+`,

$$
\boxed{
3\le \deg_C(x)\le5,
}
\tag{C26.9}
$$

and the contact vectors at `x` positively span `R^2`.

In particular,

$$
\boxed{
\text{there is no unloaded degree-one or degree-two contact vertex.}
}
\tag{C26.10}
$$

#### Proof

Theorem C26.1 gives `x notin Q`. The vertex is nonisolated by hypothesis. Apply canonical Theorem 6.1. `\square`

There is also a direct contradiction with C21 in the degree-two case. C21 would make an unloaded degree-two vertex the midpoint of its two unit-contact neighbors; that is visibly non-extreme, whereas contact-minimal Theorem 6.1 requires every degree-two contact vertex to belong to `Q` and canonical Lemma 5.1 makes every member of `Q` extreme.

---

## 4. C21 neutral-chain suppression becomes trivial

C21 defined a neutral chain as a contact path whose internal vertices are unloaded degree-two positive-contact vertices. In the fully force-visible branch `C_+=C`, Theorem C26.3 says no such internal vertex exists.

### Corollary C26.4 (all structural skeleton lengths equal one)

For the C21 structural skeleton,

$$
\boxed{L_E=1\qquad\text{for every skeleton edge }E.}
\tag{C26.11}
$$

Hence the C21 skeleton is exactly the full positive contact graph, and its stress-length identity reduces to the original virial identity

$$
\boxed{\sum_{e\in C}\alpha_e=D^2.}
\tag{C26.12}
$$

There are no repeated reciprocal diagonals caused by suppressed degree-two series vertices.

This is a genuine C-II strengthening. C21 remains necessary for arbitrary normalized KKT supports and for branches with weak contacts, where `C_+` need not equal the full contact graph.

---

## 5. Reaction-free two-terminal blocks disappear completely

C22 proved that any connected positive-contact region `K` with no positive diameter reaction and exactly two positive-contact edges leaving it is an exact straight unit path, including its two terminal contacts.

### Corollary C26.5 (no reaction-free two-terminal region)

Under the fully force-visible assumptions, no nonempty region `K` satisfying the C22 two-terminal hypotheses exists.

#### Proof

C22 makes every vertex of `K` an unloaded degree-two vertex in the positive contact graph, including the two terminal vertices when their external contacts are counted. Because `C_+=C`, this is their full unit-contact degree. This contradicts Theorem C26.3. `\square`

Thus the C22 collapse theorem changes role inside C-II: it is now an exclusion theorem, not merely a reduction to a straight chain.

---

## 6. Bridge-block tree: every reaction-free node genuinely branches

Delete all positive-contact bridges and contract the remaining components to obtain the bridge-block tree `T_br`.

C22 already proved that every reaction-free degree-two bridge block is a single unloaded contact vertex. C26.3 excludes that vertex.

### Corollary C26.6 (loaded-or-branching bridge tree)

If `T_br` has at least one edge, then

1. every leaf block is loaded;
2. every reaction-free block has bridge-tree degree at least three;
3. there are no reaction-free degree-two blocks at all.

Hence no neutral suppression is needed in the bridge-block tree.

Let `R` be the number of loaded bridge blocks and `I_0` the number of reaction-free bridge blocks. The usual tree identity gives

$$
\boxed{I_0\le R-2,}
\tag{C26.13}
$$

and therefore

$$
\boxed{|V(T_{br})|\le2R-2\le2|B_+|-2,}
\tag{C26.14}
$$

$$
\boxed{|E(T_{br})|\le2R-3\le2|B_+|-3.}
\tag{C26.15}
$$

The earlier `O(D)` event bound remains valid, but every tree edge now joins actual structural blocks directly; there are no hidden unit-length series vertices between events.

---

## 7. The C24 common route is either one block or one bridge

C24 defined

$$
I_*:=\bigcap_{h\in H_+}P_h,
\tag{C26.16}
$$

where `P_h` is the bridge-block-tree path between the endpoint blocks of positive diameter edge `h`. C24 proved that `I_*` is a path and that every internal node of this path is reaction-free of degree exactly two in the whole bridge-block tree.

Those internal nodes are impossible by Corollary C26.6.

### Theorem C26.7 (binary common-route theorem)

The common positive-diameter route has exactly one of the following two forms:

$$
\boxed{I_*\text{ is one bridge block},}
\tag{C26.17}
$$

or

$$
\boxed{I_*\text{ is one bridge joining two bridge blocks}.}
\tag{C26.18}
$$

It cannot contain two or more bridge edges.

#### Proof

A tree path with at least two edges has an internal node. C24 makes every such internal node reaction-free of bridge-tree degree two. Corollary C26.6 excludes it. `\square`

If C26.18 holds, every positive diameter edge crosses that single universal contact bridge. C24 therefore makes `H_+` a forest, and C25 upgrades it to a common-cut caterpillar forest.

If C26.17 holds, all positive diameter paths meet in one block. This includes every positive-diameter cycle phase and is the natural interface with the two-edge-connected stress-bulk branch.

Thus the earlier “universal straight contact-chain core of length at most `D`” is replaced in C-II by the much sharper dichotomy

$$
\boxed{
\text{single common block}
\quad\text{or}\quad
\text{single universal contact bridge}.}
\tag{C26.19}
$$

---

## 8. Bridge-dominant stress forces linearly many loaded diameter vertices

C23 gives, for any common hub root `X_*`,

$$
S_{br}\le
D\sum_{b\in B_+}s_b\,d_T(\tau(b),X_*),
\tag{C26.20}
$$

with `sum_b s_b=2`. Hence

$$
S_{br}\ge\eta D^2
\quad\Longrightarrow\quad
\frac12\sum_b s_b d_T(\tau(b),X_*)\ge\frac{\eta D}{2}.
\tag{C26.21}
$$

The weighted mean depth is at most the maximum tree depth, which is at most the total number of bridge-tree edges. By C26.15,

$$
\frac{\eta D}{2}
\le |E(T_{br})|
\le 2|B_+|-3.
\tag{C26.22}
$$

Therefore:

### Corollary C26.8 (linear loaded-boundary cost of bridge stress)

If

$$
S_{br}\ge\eta D^2,
\tag{C26.23}
$$

then

$$
\boxed{
|B_+|
\ge
\frac{\eta D}{4}+\frac32.
}
\tag{C26.24}
$$

In particular any bridge-dominant sequence has `|B_+|=Omega(D)`.

This is not yet a contradiction: the general hull-perimeter bound permits `|B_+|<=pi D`. It does convert bridge stress into a compulsory linear population of positively diameter-loaded extreme vertices.

---

## 9. Effect on the C-II endgame

The fully force-visible bridge branch is now substantially narrower.

Previous normal form:

```text
bridge stress
  -> deep bridge tree
  -> long straight neutral corridors between sparse 2D events
  -> common route could be a straight chain of length up to D
```

New normal form:

```text
C=C_*
  -> every unloaded contact vertex has degree 3,4,5
  -> no neutral degree-two vertex anywhere
  -> no reaction-free two-terminal region
  -> no reaction-free degree-two bridge block
  -> common diameter-route intersection is:
       (a) one block, or
       (b) one universal contact bridge
  -> in case (b), H_+ is the C25 common-cut caterpillar forest
  -> bridge stress eta D^2 forces |B_+| >= eta D/4 + 3/2
```

There is no longer an `Omega(D)` straight-corridor loophole in C-II. If bridge depth is `Omega(D)`, it consists of `Omega(D)` actual loaded/branching block transitions.

The next bridge theorem should therefore target **linear event density**, not sparse-event straight transport. A useful exact endpoint would be:

> **C-II loaded-event transport theorem.** No sufficiently large global minimizer can have a Target C bridge tree of depth `Omega(D)` in which every reaction-free block branches and `Omega(D)` distinct loaded boundary vertices route positive diameter mass through a single common block or single universal bridge.

The complementary single-block/two-edge-connected stress-bulk branch remains open.

---

## 10. Regression audit

- **Unit square:** all four contact vertices are positive diameter-loaded, so C26.3 does not apply to them. No contradiction.
- **Straight-chain toy framework:** its internal vertices are unloaded degree two and are therefore excluded only under the full C-II hypotheses `C_+=C` plus contact minimality. This is exactly why C21 remains valid in the more general KKT setting.
- **Weak-contact branch:** not covered. A vertex can have additional weak unit contacts outside `C_+`, so positive-support degree two need not equal full contact degree two.
- **Weak diameter endpoints:** an unloaded contact vertex cannot be one, because positive contact equilibrium makes it non-extreme. Weak diameter endpoints can still occur at contact-isolated hull vertices or at already positively loaded vertices via additional weak diameter edges.
- **Reaction-free branch vertex of degree three or more:** allowed. The theorem removes neutral series transport, not genuine 2D branching.
- **Bridge-free positive contact graph:** allowed and unchanged; this remains the two-edge-connected stress-bulk branch.
- **Nonuniform KKT weights:** fully allowed. No lower bound on an individual `alpha`, `beta`, or `s_b` is used.

No generic rigidity, PSD response comparison, density gap, or lattice structure is used.

---

## 11. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

C26 fully-visible no-neutral theorem:
Assume the contact-minimal Target C C-II branch C=C_* and choose a relative-interior
normalized KKT stress, so C_+=C.

If a contact vertex x is not positively diameter-loaded, KKT equilibrium gives
    x = sum_y alpha_xy y / sum_y alpha_xy
with every incident alpha_xy>0.
Thus x is a nontrivial convex combination of its contact neighbors, hence is not an
extreme hull point. Canonical Lemma 5.1 then gives x notin Q, the full diameter-endpoint
set. Contact-minimal Theorem 6.1 therefore forces
    deg_C(x) in {3,4,5}
and strict positive spanning of its contact directions.

Consequences:
- no unloaded degree-1/2 contact vertex;
- no C21 neutral-chain internal vertices, so every skeleton length L_E=1;
- no C22 reaction-free two-terminal region;
- no reaction-free degree-2 bridge block;
- C24 common route I_* has at most one bridge edge:
      either one common block or one universal contact bridge;
- in the universal-bridge phase, H_+ is the C25 common-cut caterpillar forest;
- if S_bridge >= eta D^2, then
      |B_+| >= eta D/4 + 3/2.

The bridge endgame is no longer a sparse-event/long-straight-corridor problem.
Any Omega(D) bridge depth now contains Omega(D) genuine loaded or branching events.
Exact next target: exclude that linear event-density transport, or collapse to the
single common block/two-edge-connected reciprocal-response phase.
```
