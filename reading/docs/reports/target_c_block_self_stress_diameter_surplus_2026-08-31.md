> Generated reading edition · [exact source](../../../docs/reports/target_c_block_self_stress_diameter_surplus_2026-08-31.md) · source SHA-256 `f65d73735715182f5468307f6e70bda34eeb32285646e6094b7c300fbd19b970`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-DCD686068D4B","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C39: positive self-stress sharpens every block-diameter budget

**Date:** 2026-08-31  
**Target:** C-II  
**Depends on:** C26, canonical C31 loaded-block pinned diameter budget, positive KKT equilibrium, Eppstein 2018  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

Canonical C31 proves for every bridge block `X`

```math
\delta_X\le2q_X+k_X-2,
```

where `q_X=|B_+\cap X|`, `k_X` is bridge-tree degree, and `delta_X` is internal contact-graph diameter. The strictly positive KKT contact stress supplies additional left-kernel dependencies after the same pinning.

Let

- `U_X=V(X)\setminus B_+`;
- `c_X` be the number of connected components of `C[U_X]`;
- `p_X` be the number of contact rows incident to `X` that become pinned-pinned under the C31 pinning: internal loaded-loaded contacts plus incident bridges whose endpoint in `X` is loaded.

Then

```math
\boxed{e_X+k_X-p_X\ge2(m_X-q_X)+c_X}
```

and hence

```math
\boxed{\delta_X\le k_X+2q_X-p_X-c_X-2.}
```

Summed over all bridge blocks, with `delta_X=0` for singletons,

```math
\boxed{
\sum_X\delta_X
\le2|B_+|-2-\sum_X(p_X+c_X).}
```

For a nontrivial reaction-free block, `q_X=p_X=0` and `c_X=1`, so

```math
\delta_X\le k_X-3.
```

Triangle-free cyclicity gives `delta_X>=2`; therefore

```math
\boxed{k_X\ge5.}
```

This removes the reaction-free square-with-four-bridges regression left open by C28/C34.

---

## 1. Effective pinned block matrix

Use the canonical C31 pinning: pin `B_+\cap X` and every source vertex outside `X`. Only

```math
U_X:=V(X)\setminus B_+
\tag{C39.1}
```

moves. C31's contact-minimal straight-motion argument gives zero pinned expansive cone and therefore full column rank

```math
2(m_X-q_X).
\tag{C39.2}
```

A contact row is identically zero on these columns exactly if it has no unpinned endpoint in `X`. Let `p_X` count these pinned-only rows. The number of effective rows is

```math
e_X+k_X-p_X.
\tag{C39.3}
```

Let `U_{X,1},...,U_{X,c_X}` be the connected components of the induced contact graph on `U_X`.

---

## 2. One positive self-stress dependency per unpinned component

At every `u in U_X`, C26 gives zero positive diameter reaction. KKT equilibrium is

```math
\sum_{uv\in C}\alpha_{uv}(u-v)=0,
\qquad \alpha_{uv}>0.
\tag{C39.4}
```

For each `U_{X,r}`, collect the effective rows incident to that component. Equation C39.4 gives a nonzero left-kernel vector with coefficients equal to the positive `alpha` values. Distinct unpinned components have disjoint effective row supports, so these `c_X` dependencies are independent.

Thus the left nullity is at least `c_X`, while the effective matrix has full column rank. Therefore:

### Theorem C39.1 — local self-stress row surplus

```math
\boxed{e_X+k_X-p_X\ge2(m_X-q_X)+c_X.}
\tag{C39.5}
```

For a nontrivial block, Eppstein gives

```math
e_X\le2m_X-\delta_X-2.
\tag{C39.6}
```

Combining yields:

### Theorem C39.2 — self-stress block diameter surplus

```math
\boxed{
\delta_X\le k_X+2q_X-p_X-c_X-2.}
\tag{C39.7}
```

---

## 3. Singleton audit

Set `delta_X=0` for a singleton.

- Reaction-free singleton: `q_X=p_X=0`, `c_X=1`; C26 gives `k_X>=3`, so C39.7 reads `0<=k_X-3`.
- Loaded singleton: `q_X=1`, `c_X=0`, and every incident bridge row is pinned-only, so `p_X=k_X`; C39.7 is equality `0<=0`.

Thus C39.7 is valid for every bridge-block node under this convention.

---

## 4. Global telescoping deficit

Let `N=|V(T)|`. Summing C39.7 gives

```math
\begin{aligned}
\sum_X\delta_X
&\le\sum_Xk_X+2\sum_Xq_X-\sum_Xp_X-\sum_Xc_X-2N\\
&=2(N-1)+2|B_+|-\sum_X(p_X+c_X)-2N.
\end{aligned}
```

Hence:

### Theorem C39.3 — global block-diameter self-stress deficit

```math
\boxed{
\sum_X\delta_X
\le2|B_+|-2-\sum_X(p_X+c_X).}
\tag{C39.8}
```

This refines canonical C31's `O(D)` global block-diameter budget by an explicit nonnegative deficit.

---

## 5. Reaction-free blocks require five bridge directions

For a nontrivial reaction-free block,

```math
q_X=0,\quad p_X=0,\quad c_X=1.
```

Thus

```math
\boxed{\delta_X\le k_X-3.}
\tag{C39.9}
```

A nontrivial bridge block contains a cycle. Triangle-freeness makes the smallest cycle length four, hence its graph diameter is at least two. Therefore

```math
\boxed{k_X\ge5.}
\tag{C39.10}
```

This improves C34's `k_X>=4` for reaction-free nontrivial blocks.

A one-loaded degree-two nontrivial block is also impossible: if unpinned vertices are present then `q_X=1,k_X=2,c_X>=1`, and C39.7 gives `delta_X<=1-p_X`, contradicting `delta_X>=2`. Thus the C34 conclusion is recovered independently.

---

## 6. Regression audit

- **Loaded singleton:** exact equality.
- **Reaction-free trivalent singleton:** exact equality `delta=0=k-3`.
- **Reaction-free square with four bridges:** excluded: C39 would give `delta<=1`, while the square has `delta=2`.
- **Reaction-free square with five bridges:** not excluded; it can meet the count `delta=2=k-3`.
- **C-I:** not covered because full-contact positivity is essential.

```text
C39:
Under the canonical C31 pinning of one bridge block, every connected unpinned part
carries an independent positive KKT left-kernel dependency.  If p_X pinned-only contact
rows and c_X unpinned components occur, then
    e_X+k_X-p_X >= 2(m_X-q_X)+c_X,
so
    delta_X <= k_X+2q_X-p_X-c_X-2.
Globally
    sum_X delta_X <= 2|B_+|-2-sum_X(p_X+c_X).
A nontrivial reaction-free block has delta_X<=k_X-3 and hence k_X>=5.
```
