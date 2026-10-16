<!-- theorem-state: {"artifact_id":"ART-8DA7170B7199","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_loaded_block_pinned_diameter_budget_2026-08-31.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=7fdd8404e7667df40c6d3b9112d36c5454eff40a; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — Target C addendum: loaded bridge blocks obey a pinned diameter budget

**Date:** 2026-08-31
**Repository branch:** `research/target-c-no-neutral-corridors-2026-08-31`
**Run type:** proof / C-II block-rank strengthening
**Target:** C-II
**Depends on:** canonical Theorem 12.2, C26, C28, and Eppstein's connected triangle-free penny-graph inequality
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

C28 controls reaction-free bridge blocks. Loaded blocks were left outside that theorem because positive diameter reactions supply upper constraints if one tries to move the loaded vertices. In C-II there is a simpler route: pin those vertices.

For a bridge block `X`, let `m_X` be its number of vertices, `e_X` its internal contact count, `k_X` its bridge-tree degree, `q_X=|V(X) cap B_+|`, and, for a nontrivial block, let `delta_X` be its internal contact-graph diameter.

The new estimates are

\[
\boxed{\delta_X\le k_X+2q_X-2}
\tag{C31.1}
\]

for every nontrivial block, and

\[
\boxed{\sum_{X\text{ nontrivial}}\delta_X
\le 2|B_+|-2-q_{sing}
\le 2|B_+|-2
\le 2\pi D-2,}
\tag{C31.2}
\]

where `q_sing` is the number of loaded singleton bridge blocks. Thus the entire two-edge-connected block decomposition, loaded blocks included, has only `O(D)` total internal graph diameter.

---

## 1. Setup

Assume the contact-minimal fully force-visible Target C branch and choose a relative-interior normalized KKT stress, so `C_+=C`. Let `G=(A^circ,C)` be the nonisolated contact core. C26 gives

\[
Q^circ=B_+,
\tag{C31.3}
\]

where `Q^circ` is the full set of source diameter endpoints belonging to the core.

Delete every bridge of `G`. The connected components are the bridge blocks; contracting them gives a tree `T`. For a block `X`, set

\[
k_X=\deg_T(X),\qquad q_X=|V(X)\cap B_+|.
\tag{C31.4}
\]

---

## 2. Pinned rank inside an arbitrary block

### Lemma C31.1

For every bridge block `X`,

\[
\boxed{e_X+k_X\ge2(m_X-q_X).}
\tag{C31.5}
\]

#### Proof

Canonical Theorem 12.2 says that after fixing all vertices of `Q^circ`, the expansive cone of the entire minimum-contact core is zero. By C31.3 these fixed vertices are exactly `B_+`.

Freeze every core vertex outside `X` as well, and let only `V(X)\setminus B_+` move. If the resulting reduced contact-rigidity matrix had a nonzero kernel vector, extend it by zero to every fixed vertex. Internal contacts of `X` and bridges leaving `X` would have zero first variation, all contacts outside `X` would have two fixed endpoints, and every point of `B_+=Q^circ` would be fixed. This would be a nonzero pinned expansive velocity of the full core, contradicting Theorem 12.2.

Hence the reduced matrix has full column rank `2(m_X-q_X)`. There are at most `e_X+k_X` contact rows involving `X`; rows whose endpoints are both pinned only reduce the usable row count. Therefore C31.5 holds. `square`

No diameter row is counted. The diameter endpoints are removed from the variable set instead.

---

## 3. Loaded-block diameter bound

A nontrivial bridge block is a connected triangle-free penny graph. The Eppstein inequality already used in C28 gives

\[
e_X\le2m_X-\delta_X-2.
\tag{C31.6}
\]

Combining C31.5 and C31.6,

\[
2m_X-2q_X\le e_X+k_X\le2m_X-\delta_X-2+k_X,
\]

so

\[
\boxed{\delta_X\le k_X+2q_X-2.}
\]

Every contact edge has Euclidean length one, hence also

\[
\operatorname{diam}_{Eucl}(X)\le\delta_X\le k_X+2q_X-2.
\tag{C31.7}
\]

For `q_X=0` this recovers the C28 estimate `delta_X<=k_X-2`. The new content is the loaded case.

---

## 4. Global sum over all nontrivial blocks

Let `N` be the nontrivial blocks and `S` the singleton blocks. Put

\[
q_N=\sum_{X\in N}q_X,\qquad q_S=\sum_{X\in S}q_X=:q_{sing}.
\tag{C31.8}
\]

The tree identity gives

\[
\sum_{X\in V(T)}(k_X-2)=-2.
\tag{C31.9}
\]

For each singleton block,

\[
k_X-2\ge-q_X.
\tag{C31.10}
\]

Indeed, a loaded singleton has `q_X=1` and tree degree at least one, so `k_X-2>=-1`. A reaction-free singleton is not a leaf by C20 and is not degree two by C26, so `k_X>=3` and `k_X-2>=1>=0=-q_X`. The one-node tree cannot be a singleton because the positive contact core is nontrivial.

Summing C31.1 over `N`,

\[
\begin{aligned}
\sum_{X\in N}\delta_X
&\le\sum_{X\in N}(k_X-2)+2q_N\\
&=-2-\sum_{X\in S}(k_X-2)+2q_N\\
&\le-2+q_S+2q_N\\
&=2|B_+|-2-q_{sing}.
\end{aligned}
\tag{C31.11}
\]

This proves C31.2. The same bound holds for the sum of Euclidean block diameters. `square`

---

## 5. C-II effect

C28 gave a global `O(D)` diameter budget only for nontrivial reaction-free blocks. C31 removes the loaded-block exception:

```text
any nontrivial bridge block X:
    delta_X <= k_X + 2 q_X - 2

all nontrivial blocks together:
    sum delta_X <= 2|B_+|-2-q_sing <= 2*pi*D-2
```

A loaded two-edge-connected block can therefore be large only by paying in bridge degree or positively loaded boundary vertices, both of which have globally controlled totals.

This is still not a packing contradiction: one block of graph diameter `Theta(D)` may contain `Theta(D^2)` unit-separated vertices, and KKT-invisible isolated source points remain outside the core.

---

## 6. Regression audit

- **Bridge-free core:** `T` has one nontrivial node with `k=0`; C31 gives `delta<=2|B_+|-2` by the same proof.
- **Reaction-free block:** `q=0`, recovering C28.
- **Loaded singleton leaf:** excluded from the Eppstein step and handled by C31.10.
- **Reaction-free singleton branch point:** C26 gives degree at least three.
- **Many loaded vertices in one block:** allowed and charged by the `2q_X` term.
- **KKT-invisible isolated points:** outside the core and untouched.
- **C-I:** outside scope because `Q^circ=B_+` is a C26 consequence of full force visibility.

No loaded diameter constraint is linearized or discarded; loaded vertices are pinned before the rank count.

---

## 7. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

C31:
C26 gives Q^circ=B_+. Restrict the canonical Theorem 12.2 pinned core to one bridge block X, pin B_+ cap X and every outside vertex, and obtain
    e_X+k_X >= 2(m_X-q_X).
Eppstein gives
    e_X <= 2m_X-delta_X-2,
therefore
    delta_X <= k_X+2q_X-2.

Summing over nontrivial blocks and using the tree identity plus the C26 singleton-degree restrictions gives
    sum_X delta_X <= 2|B_+|-2-q_sing <= 2*pi*D-2.
```
