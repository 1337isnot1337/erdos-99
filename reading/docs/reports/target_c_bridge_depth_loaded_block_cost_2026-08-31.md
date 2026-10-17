> Generated reading edition · [exact source](../../../docs/reports/target_c_bridge_depth_loaded_block_cost_2026-08-31.md) · source SHA-256 `9c6901b551e493db121c541fb027a5ececa781b158f7ba7a81a5d6b212fea9b5`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-B730A811E103","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C addendum: bridge depth consumes loaded blocks one-for-one

**Date:** 2026-08-31  
**Repository branch:** `research/target-c-contact-minimal-neutral-chain-exclusion-2026-08-31`  
**Run type:** proof / quantitative tree reduction  
**Target:** C-II  
**Depends on:** C23 and C26  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

C23 converts total bridge stress into positive-diameter endpoint mass times bridge-tree depth. C26 removes every reaction-free degree-two bridge block. Those two facts imply a sharper combinatorial bound: every unit of root-to-loaded depth consumes a distinct loaded bridge block.

If `R` is the number of loaded bridge blocks, every loaded block lies at bridge-tree depth at most `R-1` from a C23 common hub. Consequently

$$
\boxed{S_{br}\le2D(R-1).}
$$

Therefore

$$
S_{br}\ge\eta D^2
\quad\Longrightarrow\quad
\boxed{R\ge\frac{\eta D}{2}+1.}
$$

and hence `|B_+| >= eta D/2+1`.

---

## 1. Rooted bridge tree

Work in the fully force-visible C-II branch. Let `T` be the positive-contact bridge-block tree and root it at any C23 common hub block `X_*`.

C26 gives:

1. every leaf block is loaded;
2. every reaction-free block has degree at least three;
3. no reaction-free degree-two block exists.

Let `R` be the number of loaded blocks of `T`.

---

## 2. A root-to-loaded path injects into loaded blocks

### Lemma C29.1

For every loaded block `Y`,

$$
\boxed{d_T(X_*,Y)\le R-1.}
\tag{C29.1}
$$

#### Proof

Let

$$
X_*=v_0,v_1,\ldots,v_L=Y
\tag{C29.2}
$$

be the unique tree path, so `L=d_T(X_*,Y)`.

For each path node `v_i` with `1<=i<=L`, assign a loaded block as follows.

- If `v_i` is loaded, assign `v_i` itself.
- If `v_i` is reaction-free, then `i<L` because `Y` is loaded. C26 gives `deg(v_i)>=3`. Two incident edges are the path edges toward `v_{i-1}` and `v_{i+1}`. Hence there is an off-path component attached at `v_i`. Every finite tree component contains a leaf, and every leaf block of `T` is loaded. Choose one loaded leaf in that off-path component.

The assigned loaded blocks for distinct `i` are distinct: loaded path nodes are distinct, and off-path components attached at different path nodes are pairwise disjoint and disjoint from the path.

Thus the nodes `v_1,...,v_L` already produce `L` distinct loaded blocks.

If the root `X_*` is loaded, it is an additional loaded block distinct from those `L`, giving `R>=L+1`.

If the root is reaction-free and `T` has an edge, C26 gives `deg(X_*)>=3`. The path uses only one edge incident to the root, so at least two off-path components remain. Each contains a loaded leaf, and these leaves are distinct from all `L` assigned blocks. Hence in this case `R>=L+2`.

If `T` has one node then `L=0` and the result is trivial.

In all cases `R>=L+1`, proving C29.1. `\square`

---

## 3. Weighted depth and bridge stress

For each positive diameter endpoint `b`, let `tau(b)` be its loaded bridge block and

$$
s_b:=\sum_{bk\in H_+}\beta_{bk}.
\tag{C29.3}
$$

Then

$$
\sum_{b\in B_+}s_b=2.
\tag{C29.4}
$$

C23 proves

$$
S_{br}
\le
D\sum_{b\in B_+}s_b\,d_T(\tau(b),X_*).
\tag{C29.5}
$$

By Lemma C29.1 every depth is at most `R-1`, so

$$
S_{br}
\le
D(R-1)\sum_b s_b
=2D(R-1).
\tag{C29.6}
$$

### Theorem C29 (loaded-block cost of bridge stress)

$$
\boxed{S_{br}\le2D(R-1).}
\tag{C29.7}
$$

Consequently, if

$$
S_{br}\ge\eta D^2,
\tag{C29.8}
$$

then

$$
\boxed{R\ge\frac{\eta D}{2}+1,}
\tag{C29.9}
$$

and because each loaded block contains at least one distinct positive diameter endpoint,

$$
\boxed{|B_+|\ge\frac{\eta D}{2}+1.}
\tag{C29.10}
$$

This improves the earlier factor-`1/4` endpoint-count consequence obtained only from the total structural-node bound.

---

## 4. Interpretation

Bridge-dominant stress now pays simultaneously in three currencies:

1. **loaded-block population:** C29 gives `Omega_eta(D)` loaded blocks;
2. **single-cut scale:** C27 gives one bridge with `alpha_e=Omega_eta(D)` and crossing `beta` mass `Omega_eta(1)`;
3. **reaction-free complexity:** C28 bounds the total internal graph diameter of reaction-free nontrivial blocks by `O(D)`.

Thus a bridge-dominant counterexample cannot achieve linear depth by a neutral series chain and cannot achieve it using only a bounded number of loaded events. It requires linearly many distinct positive-diameter-loaded blocks, while any large reaction-free 2D event must spend proportional bridge degree.

This still does not contradict the perimeter bound `|B_+|<=pi D`; a linearly populated loaded boundary is geometrically possible. The next step must use the ordered diameter geometry, reciprocal cut forces, or global packing capacity of those linearly many loaded events.

---

## 5. Regression audit

- A path consisting entirely of loaded blocks is allowed; depth `R-1` shows C29.1 is sharp at the level of abstract trees.
- Reaction-free trivalent comb nodes are allowed, but each such node consumes a distinct off-path loaded subtree.
- Nonuniform `beta` weights are allowed; the theorem uses only the total endpoint mass `sum s_b=2`.
- The bridge-free phase has `S_br=0` and is unaffected.

---

## 6. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

C29:
Root the C-II bridge-block tree at a C23 common hub.  C26 says every reaction-free
node has degree >=3 and every leaf is loaded.  For any path from the hub to a loaded
block Y, each nonroot path node either is itself loaded or, if reaction-free, has an
off-path subtree containing a distinct loaded leaf.  Including the root case gives
    d_T(X_*,Y) <= R-1,
where R is the number of loaded blocks.

C23 gives
    S_bridge <= D sum_b s_b d_T(tau(b),X_*),
    sum_b s_b=2.
Therefore
    S_bridge <= 2D(R-1).
So
    S_bridge >= eta D^2
implies
    R >= eta D/2 + 1,
    |B_+| >= eta D/2 + 1.

Bridge-dominant stress now forces linearly many distinct loaded blocks, in addition to
C27's macroscopic individual bridge and C28's O(D) reaction-free diameter budget.
```
