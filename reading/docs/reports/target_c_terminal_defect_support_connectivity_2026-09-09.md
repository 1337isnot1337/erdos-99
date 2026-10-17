> Generated reading edition · [exact source](../../../docs/reports/target_c_terminal_defect_support_connectivity_2026-09-09.md) · source SHA-256 `f9361ac8bac1d5bd518147f56702da2507e37348bdb9fe6f2d64ee9a83863f04`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-C32B664373E3","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — maximal terminal defect rank forces 3-connected signed support

**Date:** 2026-09-09  
**Repository base:** `cf790155660ad46797e53c7f44371b078f7eab7b` plus ZR/ZS  
**Run type:** exact PSD/Gale-support theorem  
**Target:** Target C terminal response after ZR  
**Depends on:** ZR/ZS terminal defect kernel, strict convexity of `B_+`  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

ZR/ZS give the terminal defect

$$
M:=\Lambda-L_H\succeq0,
\qquad
\ker M=\operatorname{span}\{\mathbf1,P_x,P_y\},
\qquad
\operatorname{rank}M=q-3.
$$

Because the `q` terminals are vertices of a strict convex polygon, no three are collinear. This maximal PSD rank has a graph-theoretic consequence that was not recorded in the response campaign:

> the nonzero off-diagonal support graph of `M` is 3-vertex-connected.

Thus the strict response/diameter defect cannot be assembled across a one- or two-terminal separator. In particular the non-diameter response support has at least `(3q-2h)/2` edges, even after allowing every diameter edge to contribute to the signed support.

The theorem is coefficient-free. It does not give a conductance floor.

---

## 1. Gale representation of the terminal defect

Let

$$
P=
\begin{pmatrix}
1&p_{1x}&p_{1y}\\
\vdots&\vdots&\vdots\\
1&p_{qx}&p_{qy}
\end{pmatrix}
$$

be the `q x 3` affine-coordinate matrix of the terminal set. ZR/ZS say

$$
\ker M=\operatorname{col}P.
\tag{1.1}
$$

Choose a Gale matrix

$$
Z\in\mathbb R^{q\times(q-3)}
$$

whose columns form `ker(P^T)`. Since `M` is PSD of rank `q-3` and has column space `ker(P^T)`, there is a positive-definite matrix

$$
\Psi\in\mathbb S_{++}^{q-3}
$$

such that

$$
\boxed{M=Z\Psi Z^T.}
\tag{1.2}
$$

Because no three terminals are collinear, every three rows of `P` are independent. By matroid duality, every `q-3` rows of `Z` are independent. Hence every subset of at most `q-3` rows of `Z` is independent.

Equivalently, if `U subset B_+` and `|U|<=q-3`, then

$$
\boxed{\dim\operatorname{span}\{Z_u:u\in U\}=|U|.}
\tag{1.3}
$$

---

## 2. The nonzero support graph is 3-connected

Define the simple graph `G_M` on `B_+` by

$$
ij\in E(G_M)
\iff
i\ne j\text{ and }M_{ij}\ne0.
\tag{2.1}
$$

### Theorem TC.1

For `q>=4`,

$$
\boxed{G_M\text{ is 3-vertex-connected}.}
\tag{TC.1}
$$

### Proof

Suppose a vertex set `S` with `|S|<=2` separates two nonempty vertex sets `A` and `B`, so there is no support edge between `A` and `B`.

Then for every `a in A`, `b in B`,

$$
0=M_{ab}=Z_a\Psi Z_b^T.
\tag{2.2}
$$

Thus the row spans

$$
U_A:=\operatorname{span}\{Z_a:a\in A\},
\qquad
U_B:=\operatorname{span}\{Z_b:b\in B\}
$$

are orthogonal under the positive-definite inner product

$$
\langle x,y\rangle_\Psi=x\Psi y^T.
$$

Hence

$$
\dim U_A+\dim U_B\le q-3.
\tag{2.3}
$$

If `|A|<=q-3`, (1.3) gives `dim U_A=|A|`; if `|A|>q-3`, its row span is all of `R^{q-3}` and in particular has dimension `q-3`. The same holds for `B`.

Neither `A` nor `B` can have size greater than `q-3`, because then its span would be the whole Gale space and could not be orthogonal to the nonzero rows on the other side. Therefore

$$
\dim U_A=|A|,
\qquad
\dim U_B=|B|.
$$

Equation (2.3) becomes

$$
|A|+|B|\le q-3.
\tag{2.4}
$$

But

$$
|A|+|B|=q-|S|\ge q-2,
$$

contradicting (2.4). Therefore no separator of size at most two exists. `square`

This is the usual maximal-rank PSD/Gale connectivity mechanism, proved here directly so no generic-framework theorem is imported.

---

## 3. Translate the support into response and diameter edges

For distinct terminals,

$$
M_{ij}=\beta_{ij}-c_{ij},
\tag{3.1}
$$

where `c_ij>=0` is the Kron-reduced contact conductance and `beta_ij>0` exactly on actual diameter edges by C65.

Let

$$
G_0:=\{ij\notin H:c_{ij}>0\}
\tag{3.2}
$$

be the non-diameter response graph used by ZM.

Every edge of `G_M` is either

1. an edge of `G_0`; or
2. an actual diameter edge `ij in H` for which `beta_ij-c_ij!=0`.

Thus

$$
E(G_M)\subseteq E(G_0)\cup E(H).
\tag{3.3}
$$

Since a 3-connected graph has minimum degree at least three,

$$
2|E(G_M)|\ge3q.
$$

Using `|H|=h`, (3.3) gives the coefficient-free edge count

### Corollary TC.2

$$
\boxed{
|E(G_0)|
\ge
\frac{3q-2h}{2}.
}
\tag{TC.2}
$$

Equivalently, with `d_H=q-h`,

$$
\boxed{
|E(G_0)|
\ge
\frac q2+d_H.
}
\tag{TC.3}
$$

This strengthens the mere existence of a linear matching as a raw support-edge count, but not as a disjointness or mass theorem: one harmonic attachment component can create a dense response clique.

---

## 4. Separator consequence for response atoms

The Kron response support has the exact atom description already used by ZM:

- a direct loaded-loaded contact gives a response edge;
- an unloaded harmonic component with attachment set `A_r` gives positive response conductance between every pair of distinct terminals in `A_r`.

Therefore TC.1 says that after superimposing

1. the diameter pseudoforest `H` (with possible cancellations on its edges),
2. direct loaded-loaded response contacts, and
3. the attachment cliques induced by the `A_r`,

no one or two terminals can separate the signed defect support.

This is stronger than the C51 statement that every physical articulation branch contains a loaded terminal: it is a boundary-level no-two-separator theorem after harmonic elimination.

A useful immediate dichotomy is qualitative:

> if the diameter graph and direct loaded-loaded contacts admit a two-terminal separator, then at least one harmonic attachment set must meet both shores away from that separator.

Thus large-scale connectivity missing from the sparse diameter support must be supplied by genuine harmonic transfer, not by arbitrarily choosing signed matrix entries.

---

## 5. Relation to strict cut domination

ZS proves for every nonempty proper terminal set `U`

$$
\mathbf1_U^TM\mathbf1_U>0.
$$

TC is independent of the numerical size of those cut defects. It upgrades the support topology:

- ZS: every terminal cut has strictly positive total defect;
- TC: the nonzero defect support survives deletion of any two terminals.

Neither statement alone supplies a quantitative conductance floor. A single large harmonic response clique with very small conductances remains a binding regression.

---

## 6. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| Gale factorization with `Psi>0` | proved | PSD rank `q-3` and affine kernel |
| any `q-3` Gale rows independent | proved | dual of no-three-collinear terminal configuration |
| support graph `G_M` is 3-connected | proved | separator gives two orthogonal Gale row spans of impossible total dimension |
| `|E(G_0)|>=(3q-2h)/2` | proved | min degree three + at most `h` diameter support edges |
| non-diameter response mass is linear | not proved | coefficients may tend to zero |
| one macroscopic harmonic component is forced | not proved | many small atoms can collectively provide 3-connectivity |
| Level I | still open | support connectivity does not resolve coefficient degeneration |

---

## 7. Next target

TC suggests a planar-hypergraph refinement of ZM/AR:

> combine 3-connectivity of the terminal defect support with C37's noncrossing terminal-component incidence graph and the loaded degree-three cap.

The desired conclusion is either

1. one attachment set `A_r` has linear cardinality/diameter, giving a macroscopic harmonic cell; or
2. a linear number of distinct small attachment cells is required, allowing the AR/Wegner cell-capacity correction to add rather than concentrate.

This would directly attack the concentration loophole in WG.10.
