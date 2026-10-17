> Generated reading edition · [exact source](../../../docs/reports/target_c_nearcircle_no_bounded_harmonic_components_2026-09-09.md) · source SHA-256 `6a9aa1f65799dc4495834890025334af316791088aeccbc415ec5bb8d86aa01e`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-E1CA24798E45","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — near-circle harmonic components have diverging graph diameter

**Date:** 2026-09-09  
**Repository branch:** `research/post-uf-attachment-fill-2026-09-09`  
**Run type:** local smooth-boundary / positive-equilibrium theorem  
**Target:** PR #119 near-circle harmonic decomposition  
**Depends on:** DC force-hull convergence to the disk, C26 positive unloaded degree, C36 harmonic containment, C44 attachment-diameter bound  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

The near-circle harmonic decomposition cannot contain a linear family of bounded-size components.

More strongly, along every `x_B=o(D)` near-circle sequence,

$$
\boxed{
\min_{1\le r\le c_I}\delta_r\longrightarrow\infty
}
\tag{HBd.1}
$$

whenever unloaded components are present.

Since the exact near-circle boundary budget gives

$$
S:=\sum_r\delta_r=O(D),
$$

it follows that

$$
\boxed{c_I=o(D).}
\tag{HBd.2}
$$

Thus the remaining harmonic geometry may involve several mesoscopic/macroscopic components, but never linearly many graph-bounded atoms.

Combining HBd.2 with NC and ZU yields the useful asymptotic identification

$$
\boxed{
 d_H+s_Z=s_C+o(D).
}
\tag{HBd.3}

$$

ZT then becomes

$$
\boxed{
Q+2s_C=(\pi+o(1))D
}
\tag{HBd.4}

$$

throughout the near-circle branch.

This is a structural simplification, not a Level I closure.

---

## 1. Suppose one component has bounded graph diameter

Assume for contradiction that HBd.1 fails. Then there is a fixed integer `M`, an unbounded subsequence, and an unloaded component `I_j` such that

$$
\delta_j\le M.
\tag{1.1}
$$

Let

$$
A_j\subset B_{+,j}
$$

be its distinct loaded attachment set and

$$
P_j:=\operatorname{conv}(A_j).
$$

C44 gives

$$
\boxed{
\operatorname{diam}(A_j)
=\operatorname{diam}(P_j)
\le\delta_j+2
\le M+2.
}
\tag{1.2}

$$

C36 gives

$$
\boxed{I_j\subseteq P_j.}
\tag{1.3}

$$

The force hulls satisfy, after translation and scaling,

$$
F_j/D_j\to B_{1/2}
$$

by DC.

---

## 2. A bounded attachment set lies on one tangent-flat local hull arc

Choose one attachment `a_j in A_j`. After normalization and subsequence extraction,

$$
a_j/D_j\to p\in\partial B_{1/2}.
$$

By (1.2), every other attachment differs from `a_j` by `O(1)`, so every normalized attachment also converges to `p`.

Let `Gamma_j` be the smallest local force-hull boundary arc containing all vertices of `A_j`.

The local tangent convergence proved in NC applies uniformly on such a shrinking normalized arc: every force-hull side vector on `Gamma_j`, oriented along the arc, makes angle `o(1)` with the unique tangent direction `tau` of the limiting disk at `p`.

There is one finite-scale point to check: `Gamma_j` cannot have arbitrarily large absolute length while its endpoints remain `O(1)` apart. If its side vectors are `w_1,...,w_k`, then for all large `j`,

$$
\tau\cdot w_i\ge(1-o(1))|w_i|.
$$

Hence

$$
\sum_i|w_i|
\le
(1+o(1))\left|\sum_iw_i\right|_
\le O_M(1),
\tag{2.1}
$$

where the final bound follows because the extreme attachments are at distance at most `M+2`.

Therefore the total displacement of `Gamma_j` in the normal direction to `tau` is

$$
\boxed{o(1).}
\tag{2.2}
$$

In particular all attachments lie in a strip of width `o(1)` parallel to `tau`. Their convex hull `P_j` lies in the same strip, and by C36 so does the entire component `I_j`.

---

## 3. Positive unit-contact equilibrium is impossible in an `o(1)` strip

Take any vertex `x_j in I_j`.

Every positive contact neighbor of `x_j` is either

1. another vertex of the same unloaded component `I_j`; or
2. a loaded terminal in the attachment set `A_j`.

There are no contact edges between distinct unloaded components after deleting `B_+` by definition of the components.

Hence every positive contact neighbor of `x_j` lies in the same `o(1)`-width strip as `I_j union A_j`.

All contact edges have length one. Let `nu` be a unit normal to the strip. For every neighbor `y` of `x_j`,

$$
|\nu\cdot(y-x_j)|=o(1).
$$

Thus every contact direction tends to one of the two tangent directions `+tau` or `-tau`.

Unit separation between distinct neighbors implies there can be at most one neighbor in the `+tau+o(1)` cluster and at most one in the `-tau+o(1)` cluster. Indeed two unit vectors whose angle tends to zero have endpoint distance tending to zero, contradicting the source separation `>=1`.

Therefore for all sufficiently large `j`,

$$
\boxed{\deg_C(x_j)\le2.}
\tag{3.1}

$$

But `x_j` is an unloaded vertex of the positive contact core. C26 proves that every such vertex has positive contact equilibrium and contact degree in

$$
\{3,4,5\}.
$$

Contradiction.

Hence no fixed `M` can bound the graph diameter of an unloaded component along an unbounded near-circle sequence. This proves HBd.1.

---

## 4. Component count is sublinear

Let

$$
m_j:=\min_r\delta_r.
$$

HBd.1 gives

$$
m_j\to\infty.
$$

Every component contributes at least `m_j` to

$$
S_j=\sum_r\delta_r.
$$

NBd gives

$$
S_j\le q_j+2x_{B,j}=O(D_j).
$$

Therefore

$$
 c_{I,j}m_j\le S_j=O(D_j),
$$

so

$$
\boxed{c_{I,j}/D_j\to0.}
$$

This proves HBd.2.

---

## 5. ZU and ZT simplify

ZU gives exactly

$$
c_I+e_{BB}+s_C=q-2+(d_H+s_Z).
\tag{5.1}
$$

NC gives

$$
e_{BB}=q+o(D)
$$

in the near-circle branch. HBd gives

$$
c_I=o(D).
$$

Therefore

$$
\boxed{d_H+s_Z=s_C+o(D),}
$$

proving HBd.3.

ZT gives

$$
q=x_B+Q+2(d_H+s_Z).
$$

Use

$$
q=(\pi+o(1))D,
\qquad
x_B=o(D),
$$

and HBd.3:

$$
\boxed{Q+2s_C=(\pi+o(1))D.}
$$

This proves HBd.4.

The near-circle terminal/mixed defect is therefore carried asymptotically by only two scalar currencies: bounded-face defect `Q` and pinned-contact stress surplus `s_C`.

---

## 6. Additional budget simplification

NBd gives

$$
S+R_I+s_B+2E_{BB}+3c_I+s_C=q+2x_B.
$$

NC gives `E_BB=o(D)`, HBd gives `c_I=o(D)`, and the near-circle endpoint gives `q+2x_B=(pi+o(1))D`. Thus

$$
\boxed{
S+R_I+s_B+s_C=(\pi+o(1))D.
}
\tag{6.1}

$$

Together with HBd.4 this may be written

$$
\boxed{
S+R_I+s_B
=\frac{\pi D+Q}{2}+o(D).
}
\tag{6.2}

$$

This exact asymptotic exchange is useful downstream: increasing face defect raises the amount of harmonic-diameter/internal-edge/unused-degree budget that must be present.

---

## 7. Scope and regressions

- The theorem is specific to the `x_B=o(D)` branch where the **force hull** converges to the disk. The global source hull being near a disk is not enough, because unloaded attachment terminals belong to the force hull.
- The proof does not give a rate for `min delta_r`; it only proves divergence.
- Mesoscopic components with `delta_r->infinity` but `delta_r=o(D)` remain allowed.
- A long thin component can fit in a shrinking normalized cap; the strip contradiction applies only when its **absolute** graph diameter stays bounded.
- No KKT coefficient lower bound is used.

---

## 8. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| bounded-diameter attachment cell becomes absolutely tangent-flat | proved | bounded hull-arc length + local tangent convergence |
| bounded component impossible | proved | unit separation gives at most two tangent-cluster neighbors, contradicting C26 |
| `min delta_r->infinity` | proved | contradiction for every fixed `M` |
| `c_I=o(D)` | proved | `S=O(D)` divided by diverging minimum diameter |
| `d_H+s_Z=s_C+o(D)` | proved | ZU + NC |
| `Q+2s_C=pi D+o(D)` | proved | ZT + preceding identity |
| Level I | still open | mesoscopic/macroscopic components and linear `Q,s_C` remain |

---

## 9. Next target

HBd removes the last linear-count collection of microscopic harmonic atoms. In the cap-minimal full-core branch, LI already forces

$$
Q_B\ge(2-o(1))D.
$$

The loaded-interface defect can therefore only be carried by

1. a sublinear number of mesoscopic/giant convex interface faces; or
2. a sublinear number of mesoscopic harmonic components that force large internal Eppstein slack.

A length-threshold argument can now use sublinear **count** as well as total perimeter/diameter, which was unavailable before HBd. The next useful theorem is to show that `2D` of interface defect concentrated in `o(D)` convex faces creates a macroscopic area loss in one of the two Oler-saturated semicircle carriers.
