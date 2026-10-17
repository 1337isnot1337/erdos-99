> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_isostatic_body_bar_reduction_2026-09-09.md) · source SHA-256 `3e3ae66be8084f28f7775d9bfb5a267dc3d5ad4a8c633fd96be1e987330454d8`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-64DEC28DA193","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cyclic tree phases reduce to two isostatic bodies joined by a rank-three four-bar circuit

**Date:** 2026-09-09  
**Repository branch:** PR #118 after D2 / corrected EU / WM  
**Run type:** exact rigidity-rank decomposition  
**Target:** cyclic primitive phases `d_H=1,2`  
**Depends on:** CY full mixed-rigidity rank and row-nullity, D2 four-block topology, corrected EU endpoint cut, WM wrench lift  
**External literature:** none  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`

WM left a projective-pencil branch in which the four transition side-line wrench vectors might have rank at most two. The full mixed-rigidity rank eliminates that branch.

More is true: on either side of every relevant four-block cut, the internal unit contacts plus full diameter-tree edges form an isostatic planar framework. The four transition unit contacts are exactly four bars joining two rigid bodies; they have body-bar rank three and one dependence.

### Theorem IB — two isostatic bodies

The following holds in both tree phases.

#### `d_H=2`

Let

```math
H=T_A\sqcup T_B
```

be the D2 two-tree decomposition, with four blocks

```math
A_0\mid B_0\mid A_1\mid B_1.
```

Let `G_A` consist of

1. all diameter edges of `T_A`, and
2. all cycle-contact edges whose two endpoints lie in `A=A_0\cup A_1`.

Define `G_B` analogously.

Then

```math
\boxed{|E(G_A)|=2|A|-3,\qquad \operatorname{rank}R(G_A)=2|A|-3,}
\tag{IB.1}
```

```math
\boxed{|E(G_B)|=2|B|-3,\qquad \operatorname{rank}R(G_B)=2|B|-3.}
\tag{IB.2}
```

Thus both are infinitesimally isostatic.

The four A/B transition contacts contribute exactly three further rigidity ranks. Equivalently their body-bar wrench matrix has rank three.

#### `d_H=1`

Let `H` be the full spanning diameter tree and let `e` be any nonleaf full-tree edge with

```math
\beta_e(s)=0
```

at a KKT endpoint `s`. Let

```math
H-e=T_A\sqcup T_B
```

be the corrected-EU four-block decomposition.

Form `G_A,G_B` from the **full** tree components exactly as above. Then IB.1-IB.2 again hold, and the four transition contacts again have body-bar rank three.

This statement does **not** identify the selected positive endpoint support with `H-e`. Additional internal diameter coefficients may vanish. The isostatic bodies are statements about the full geometric bar rows in `H-e`.

---

## 1. Exact internal edge counts

Let

```math
a:=|A|,
\qquad
b:=|B|,
\qquad
a+b=q.
```

The four-block order makes `A_0` and `A_1` two disjoint boundary runs. Therefore the number of cycle-contact edges internal to `A` is

```math
(|A_0|-1)+(|A_1|-1)=a-2.
\tag{1.1}
```

The diameter component `T_A` is a tree on the `a` A-vertices, so

```math
|E(T_A)|=a-1.
\tag{1.2}
```

Hence

```math
\boxed{|E(G_A)|=(a-2)+(a-1)=2a-3.}
\tag{1.3}
```

Likewise

```math
\boxed{|E(G_B)|=2b-3.}
\tag{1.4}
```

The count is the planar isostatic count on each side.

---

## 2. `d_H=2`: independence follows from the full-support one-dimensional row dependence

In the full `d_H=2` phase,

```math
|C_q|+|H|=q+(q-2)=2q-2.
```

CY/ZF gives mixed rigidity rank

```math
2q-3.
\tag{2.1}
```

Therefore the full row-dependence space has dimension one.

The unique normalized KKT stress is relative-interior in this zero-dimensional KKT polytope, so every cycle and diameter coefficient is strictly positive. Thus the unique row dependence has nonzero coefficient on every full mixed row.

Suppose the rows of `G_A` were dependent. Extend that dependence by zero coefficients on every row outside `G_A`. This gives a nonzero dependence of the full mixed rigidity matrix which vanishes on all four transition contacts. It cannot be proportional to the unique full-support KKT dependence. Contradiction.

Hence all `2a-3` rows of `G_A` are independent. This proves IB.1. The proof for `G_B` is identical.

---

## 3. `d_H=1`: delete the zeroed full-tree row in dependency space, not in selected support

The full `d_H=1` mixed framework has

```math
q+(q-1)=2q-1
```

rows and rigidity rank `2q-3`. Its row-dependence space `mathcal D` therefore has dimension

```math
\boxed{\dim\mathcal D=2.}
\tag{3.1}
```

Fix a full-tree edge `e` with `beta_e(s)=0` at a KKT endpoint `s`.

Consider the linear coordinate functional

```math
\varphi_e:\mathcal D\to\mathbb R,
\qquad
\varphi_e(\omega)=\omega_e.
\tag{3.2}
```

A relative-interior normalized KKT stress has strictly positive coefficient on `e`. Hence `varphi_e` is not the zero functional.

Since `mathcal D` is two-dimensional,

```math
\boxed{\dim\ker\varphi_e=1.}
\tag{3.3}
```

But `ker varphi_e` is exactly the row-dependence space of the full mixed framework with the one geometric row `e` deleted: any dependence of `R(C_q\cup(H-e))` extends by a zero `e`-coordinate, and conversely.

Therefore

```math
\boxed{
\operatorname{null}_{row}R(C_q\cup(H-e))=1.}
\tag{3.4}
```

That framework has `2q-2` rows, so

```math
\boxed{
\operatorname{rank}R(C_q\cup(H-e))
=(2q-2)-1
=2q-3.}
\tag{3.5}
```

This is the correct selected-endpoint rank statement: it concerns the **full geometric row set with only `e` deleted**, not the positive selected support.

The endpoint KKT stress `s`, restricted to those rows, is a nonzero vector in the one-dimensional dependence space (3.3). Its four transition contact coefficients are strictly positive because every cycle contact remains positive at every cyclic KKT stress.

Now suppose `G_A` had an internal row dependence. Extended by zero outside `G_A`, it would give a dependence of `C_q\cup(H-e)` whose four transition-contact coefficients are all zero. It cannot be proportional to the unique endpoint dependence, whose transition coefficients are nonzero. Contradiction.

Thus `G_A` has `2a-3` independent rows. Likewise `G_B`.

This proves IB for `d_H=1` without assuming that every internal beta coefficient is positive at the endpoint. `square`

---

## 4. The four transition bars have body-bar rank three

Delete the four A/B transition contact rows. What remains is the disjoint union of `G_A` and `G_B`, with total row rank

```math
(2a-3)+(2b-3)=2q-6.
\tag{4.1}
```

Restore the four transition contacts.

In `d_H=2`, the full framework rank is `2q-3`. In the `d_H=1` endpoint reduction, (3.5) gives the same rank for `C_q\cup(H-e)`.

Therefore the four transition rows increase rank by exactly

```math
(2q-3)-(2q-6)=3.
\tag{4.2}
```

Once each isostatic side is quotient by its internal Euclidean rigid motions, the relative motion of the two bodies has three degrees of freedom in the plane. Each transition bar contributes one body-bar row, represented by the line wrench vector

```math
L_r=(t_{r,x},t_{r,y},p_r\times t_r).
```

Equation (4.2) is therefore equivalent to

```math
\boxed{
\operatorname{rank}[L_i\ L_j\ L_k\ L_\ell]=3.}
\tag{4.3}
```

Thus WM's projective-pencil branch is impossible.

### Corollary IB.1 — no four-line pencil

The four transition side lines are not all concurrent in the projective plane and do not lie in any rank-two line pencil. At least one triple determinant is nonzero, and the four-line wrench relation has a one-dimensional nullspace.

Consequently WM.5 applies **unconditionally** in both cyclic tree phases:

```math
\boxed{
(\alpha_i,-\alpha_j,\alpha_k,-\alpha_\ell)
\propto
(-\Delta_{jk\ell},\Delta_{ik\ell},-\Delta_{ij\ell},\Delta_{ijk}).}
\tag{4.4}
```

The four transition contact-weight ratios are always determined by shell geometry alone.

---

## 5. Graph-theoretic form of each body

Each body graph `G_A` is the union of

1. two boundary paths, one on `A_0` and one on `A_1`, and
2. the bipartite diameter tree `T_A` joining the two blocks.

Its edge count is `2a-3`. The same holds for B.

The usual Laman sparsity count is in fact automatic combinatorially for this topology. For a vertex subset `U`, let `c_P(U)` be the number of components in the induced two-path forest and `c_T(U)` the number in the induced diameter-tree forest. Then

```math
e(U)=2|U|-c_P(U)-c_T(U).
```

If `U` meets both bipartition/color blocks, `c_P(U)>=2` and `c_T(U)>=1`; if it lies in one color block, the diameter-tree induced graph has no edges, so `c_T(U)=|U|`. Hence

```math
e(U)\le2|U|-3
```

for every `|U|>=2`.

Thus each `G_A,G_B` is a Laman graph abstractly, and IB proves that the actual equal-length geometry realizes it without a rigidity degeneracy.

---

## 6. Mechanical interpretation

The full tree-phase stress problem is now literally a two-body four-bar equilibrium.

- Each side is internally isostatic, so an imposed set of boundary loads determines its internal bar-force response uniquely.
- Four unit transition contacts join the bodies.
- Four body-bar constraints on three relative rigid-body degrees of freedom leave exactly one compatibility/self-stress relation.
- WM computes that relation as the alternating projective dependence among the four supporting side lines.

For `d_H=2`, this is the unique full KKT dependence.

For a `d_H=1` endpoint, the unique dependence of the full row set `C_q union (H-e)` may have zero coefficients on additional internal diameter bars, but the body-bar transition coefficients remain strictly positive and unique up to scale.

This is a considerably sharper normal form than treating the four-force parallelogram as an isolated vector identity.

---

## 7. Regression audit

### Extra beta zeros at a `d_H=1` endpoint

Allowed. They mean the unique equilibrium load on an isostatic body happens to assign zero force to some internal full-tree bars. They do not change geometric row independence.

### WM projective-pencil case

Eliminated by the rank increment (4.2). Retaining it as a live branch would be unnecessarily weak.

### Abstract Laman sparsity

Not a contradiction. The two-path-plus-tree graphs are naturally Laman-sparse. The new information is that the realized geometry is actually isostatic.

### Singleton color block

Then one boundary path has zero edges; the count `(a-2)+(a-1)=2a-3` still holds, and the rigidity argument is unchanged.

---

## 8. What this changes

The tree phases now share the exact finite architecture

```text
isostatic body A
    two unit boundary paths + one full diameter tree

four unit transition bars
    body-bar wrench rank 3
    one alternating positive dependence
    alpha ratios fixed by four side-line determinants

isostatic body B
    two unit boundary paths + one full diameter tree
```

For `d_H=2`, this is the full mixed framework.

For a `d_H=1` endpoint, it is the full framework after deleting the chosen zeroed full-tree edge `e`; the positive selected support may omit further internal tree bars, but the geometric body decomposition remains isostatic.

---

## 9. Next theorem

This reduction suggests two precise attacks.

### IB-WT

Compute the Dirichlet/transfer response of each isostatic body at its two boundary ports and combine the two bodies through the four transition resistances fixed by (4.4). WT already gives the complete weighted-cycle transfer formula. The goal is to contradict C56-G's one-block Robinson kernel.

### IB-sign

Use positivity of the KKT contact stress and the known equal lengths (`1` on both body paths, `D` on every diameter-tree bar) to characterize the unique internal force response of a two-path-plus-thrackle-tree isostatic body under its two endpoint load pairs. A forced zero or sign reversal on an internal diameter bar would close `d_H=2`; in `d_H=1` it would bound the additional endpoint beta zeros.

---

## 10. Promotion recommendation

**Hold as report pending independent audit.**

The rank argument is exact downstream of CY/D2/corrected-EU. It also repairs the ambiguity that led to the earlier endpoint selected-support overclaim: full geometric rows and positive selected rows are kept separate throughout.

---

## 11. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Four-block side A with a=|A| has
  a-2 internal cycle contacts + a-1 full diameter-tree edges = 2a-3 rows.
Same for B.

d_H=2:
  full mixed rows=2q-2, rank=2q-3, unique full-support dependence.
Any internal dependence in A would extend to a second full dependence, impossible.
Thus A and B are isostatic.

d_H=1 endpoint at zeroed full-tree edge e:
  full mixed dependency space before deletion has dimension 2.
The e-coordinate functional is nonzero because a relative-interior stress has beta_e>0.
Its kernel therefore has dimension 1, exactly the dependency space after deleting row e.
Hence C_q union (H-e) has 2q-2 rows, rank 2q-3, one dependence.
That dependence is the endpoint KKT stress and has all four transition alphas positive.
An internal A/B dependence would be independent of it, impossible. So both sides are
again isostatic, even if additional endpoint beta coefficients vanish.

Internal ranks sum 2q-6; restoring four transition contacts raises total rank to 2q-3,
so their body-bar wrench matrix has rank exactly 3. WM's line-pencil branch is dead.
Therefore the four transition alpha ratios are always the cofactor ratios of their
four supporting side-line vectors.

Next: compute body response/signs, then insert the forced four transition resistances
into WT/C56-G.
```
