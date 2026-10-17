> Generated reading edition · [exact source](../../../docs/reports/target_c_response_defect_extreme_circuit_reduction_2026-09-10.md) · source SHA-256 `f33fe10efaad19dffd5146b998e13d1f758331a50e54bd879b4dcf10120c5c40`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-74DEC512A499","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdos Problem #99 - response-defect minimization occurs on an extreme KKT circuit

**Date:** 2026-09-10  
**Repository base:** `5865724326ceeff610d703027d35cb0249bdcdfa`  
**Run type:** exact convexity / Dirichlet-response reduction  
**Target:** Target C C-II, especially the `D epsilon -> 0` phase  
**Depends on:** C41/C53/C65, the normalized KKT polytope, selected-stress support connectivity, C66 for the final star corollary  
**New external literature:** none  
**Computation:** none

## LEVEL I STATUS

**STILL OPEN.**

This report proves a reduction that was missing from the near-zero response branch.
The response defect is a concave function of the normalized KKT stress. Therefore its
minimum over the normalized KKT polytope is attained at a vertex. A normalized KKT
polytope vertex has support equal to one circuit of the actual mixed rigidity-row
matroid.

Consequently, if a full-support relative-interior stress satisfies

$$
D\varepsilon\to0,
$$

then on the same source there is an **extreme PSD circuit stress** with response defect
no larger, hence also satisfying `D epsilon -> 0`. C66 may then be rerun with the fixed
full actual-diameter boundary and forces the selected diameter weight to an asymptotic
star.

Thus the difficult response phase can be attacked on one rigidity circuit rather than
on an arbitrary high-dimensional full-support stress.

---

## 1. Fixed-boundary Dirichlet response with zero conductances allowed

Work on the fixed C65 actual core. Let

$$
B=V(H)
$$

be the full actual diameter-endpoint set and let

$$
I=V(C)\setminus B.
$$

For any nonnegative contact-weight vector `alpha` arising from a normalized selected
KKT stress, and for boundary data `u in R^B`, define

$$
\mathcal E_\alpha(u)
:=
\min_{v\in\mathbb R^I}
\sum_{ij\in C}\alpha_{ij}(w_i-w_j)^2,
\qquad
w|_B=u,
\quad w|_I=v.
\tag{REC.1}
$$

Zero contact coefficients are allowed. Interior zero-conductance components make the
minimizer nonunique, but they do not make the minimum energy ambiguous. The minimum
is a positive-semidefinite quadratic form in `u`. Hence there is a unique symmetric
PSD Laplacian `Lambda(alpha)` on `B` such that

$$
\boxed{
\mathcal E_\alpha(u)=u^T\Lambda(\alpha)u.
}
\tag{REC.2}
$$

Terminals disconnected in the selected contact support simply contribute zero rows
and columns. This energy definition is the singular-conductance extension of ordinary
Kron reduction and agrees with the canonical response matrix whenever the usual
interior block is invertible.

Write

$$
c_{bk}(\alpha):=-\Lambda(\alpha)_{bk}\ge0
\qquad(b\ne k).
$$

Because `Lambda(alpha) 1=0`,

$$
\frac12\operatorname{tr}\Lambda(\alpha)
=
\sum_{b<k}c_{bk}(\alpha).
\tag{REC.3}
$$

For a normalized KKT stress `x=(alpha,beta)`, put

$$
\boxed{
\varepsilon(x)
:=
\frac12\operatorname{tr}\Lambda(\alpha)-1.
}
\tag{REC.4}
$$

The normalization is `sum_H beta=1`.

---

## 2. The response defect remains nonnegative for every selected stress

Every vertex in `I` is not an endpoint of any actual diameter edge. Its KKT equilibrium
therefore has zero diameter reaction:

$$
\sum_{ij\in C}\alpha_{ij}(p_i-p_j)=0.
\tag{REC.5}
$$

Thus the two Euclidean coordinate functions are energy-minimizing harmonic extensions
of their boundary values even when some selected contact weights vanish.

Summing the two coordinate energies gives

$$
\sum_{b<k}c_{bk}(\alpha)|p_b-p_k|^2
=
\sum_{ij\in C}\alpha_{ij}|p_i-p_j|^2.
\tag{REC.6}
$$

Every contact has length one. The normalized KKT virial identity gives

$$
\sum_{ij\in C}\alpha_{ij}=D^2\sum_{h\in H}\beta_h=D^2.
\tag{REC.7}
$$

Hence

$$
\boxed{
D^2
=
\sum_{b<k}c_{bk}(\alpha)|p_b-p_k|^2.
}
\tag{REC.8}
$$

Since every source distance is at most `D`,

$$
D^2
\le
D^2\sum_{b<k}c_{bk}(\alpha).
$$

Therefore

$$
\boxed{\varepsilon(x)\ge0}
\tag{REC.9}
$$

for every normalized nonnegative KKT stress, not only the C65 relative-interior one.
Moreover

$$
\boxed{
\varepsilon(x)
=
\sum_{b<k}c_{bk}(\alpha)
\left(1-\frac{|p_b-p_k|^2}{D^2}\right).
}
\tag{REC.10}
$$

This is the selected-stress version of C41.

---

## 3. Dirichlet response is concave in the contact conductances

Let `alpha^0,alpha^1` be two nonnegative contact-weight vectors and let

$$
\alpha^t=(1-t)\alpha^0+t\alpha^1,
\qquad 0\le t\le1.
$$

For fixed boundary data `u` and an arbitrary interior extension `v`, the unreduced
energy is linear in the conductances:

$$
E_{\alpha^t}(u,v)
=(1-t)E_{\alpha^0}(u,v)+tE_{\alpha^1}(u,v).
$$

Taking the minimum over `v` gives

$$
\begin{aligned}
\mathcal E_{\alpha^t}(u)
&=
\min_v\bigl[(1-t)E_{\alpha^0}(u,v)+tE_{\alpha^1}(u,v)\bigr]\\
&\ge
(1-t)\min_vE_{\alpha^0}(u,v)
+t\min_vE_{\alpha^1}(u,v).
\end{aligned}
$$

Therefore

$$
\boxed{
\Lambda(\alpha^t)
\succeq
(1-t)\Lambda(\alpha^0)+t\Lambda(\alpha^1)
}
\tag{REC.11}
$$

in Loewner order.

Taking traces yields:

### Theorem REC.1 - response-defect concavity

On the normalized KKT polytope `P`,

$$
\boxed{
\varepsilon((1-t)x^0+tx^1)
\ge
(1-t)\varepsilon(x^0)+t\varepsilon(x^1).
}
\tag{REC.12}
$$

Thus `epsilon` is a nonnegative concave function on `P`.

---

## 4. The minimum response defect occurs at a KKT-polytope vertex

Let the vertices of the compact polytope `P` be

$$
x^{(1)},\ldots,x^{(N)}.
$$

For any

$$
x=\sum_{r=1}^N\lambda_rx^{(r)},
\qquad
\lambda_r\ge0,
\quad\sum_r\lambda_r=1,
$$

concavity gives

$$
\varepsilon(x)
\ge
\sum_r\lambda_r\varepsilon(x^{(r)})
\ge
\min_r\varepsilon(x^{(r)}).
\tag{REC.13}
$$

Because the vertices themselves belong to `P`, this proves:

### Theorem REC.2 - extreme minimizer

$$
\boxed{
\inf_{x\in\mathcal P}\varepsilon(x)
=
\min_{x\in\operatorname{Vert}(\mathcal P)}\varepsilon(x).
}
\tag{REC.14}
$$

No continuity claim at singular support changes is needed. In particular, every
selected full-support stress has an extreme KKT stress on the same source with no
larger response defect.

---

## 5. Every normalized KKT-polytope vertex has circuit support

Let `R` be the ordinary bar-rigidity matrix of the actual mixed equality framework
`C union H`, after changing the sign convention on diameter coefficients. Let `W` be
its signed self-stress space. The normalized KKT polytope is the intersection of one
fixed sign orthant in `W` with `sum_H beta=1`.

Let `x*` be a vertex of `P` and let

$$
S=\operatorname{supp}(x^*).
$$

Let

$$
W_S:=\{w\in W:\operatorname{supp}(w)\subseteq S\}.
$$

Suppose `dim W_S>=2`. Choose `w in W_S` not proportional to `x*` and replace it by

$$
\widetilde w
:=w-L(w)x^*,
\qquad
L(w):=\sum_{h\in H}w_h.
$$

Then `widetilde w` is nonzero, is supported in `S`, lies in the signed stress space,
and satisfies `L(widetilde w)=0`. Since every coordinate of `x*` on `S` is strictly
inside the prescribed sign orthant, for sufficiently small `t>0` both

$$
x^*+t\widetilde w,
\qquad
x^*-t\widetilde w
$$

remain normalized nonnegative KKT stresses. This contradicts extremality. Therefore

$$
\boxed{\dim W_S=1.}
\tag{REC.15}
$$

If a proper subset `T subsetneq S` of mixed rigidity rows were dependent, there would
be a nonzero signed bar self-stress supported in `T`. That vector belongs to `W_S`
but cannot be proportional to `x*`, because `x*` is nonzero on `S setminus T`. This
contradicts REC.15.

Thus:

### Theorem REC.3 - extreme support is one actual rigidity circuit

$$
\boxed{
S\text{ is a circuit of the actual mixed rigidity-row matroid.}
}
\tag{REC.16}
$$

The circuit dependence is unique up to scale and every coefficient on `S` is nonzero.
This gives a direct proof of the circuit statement needed here; it does not rely on an
unmerged circuit-cover report.

C53 applies to every normalized selected stress, so

$$
\boxed{
\Omega(x^*)=L_C(\alpha^*)-L_H(\beta^*)\succeq0.
}
\tag{REC.17}
$$

The canonical selected-support theorem also gives one nontrivial positive contact
component containing every positive diameter endpoint and spanning Euclidean diameter
`D`.

---

## 6. The selected PSD defect on the fixed full boundary

Keep the full actual diameter-endpoint set `B=V(H)` as boundary, even if some boundary
vertices have zero selected beta incidence. Write the selected PSD stress matrix in
boundary/interior block form:

$$
\Omega(x^*)=
\begin{pmatrix}
L_{BB}(\alpha^*)-L_H(\beta^*)&L_{BI}(\alpha^*)\\
L_{IB}(\alpha^*)&L_{II}(\alpha^*)
\end{pmatrix}
\succeq0.
\tag{REC.18}
$$

For a PSD block matrix, every vector in `ker L_II` is annihilated by the cross block;
otherwise a vector supported on that kernel direction and an arbitrarily small
boundary perturbation would make the quadratic form negative. Hence the generalized
Schur complement is PSD:

$$
L_{BB}-L_H-L_{BI}L_{II}^{\dagger}L_{IB}\succeq0.
\tag{REC.19}
$$

But by the minimum-energy definition REC.1--REC.2,

$$
\Lambda(\alpha^*)
=
L_{BB}(\alpha^*)
-L_{BI}(\alpha^*)L_{II}(\alpha^*)^{\dagger}L_{IB}(\alpha^*).
$$

Therefore

$$
\boxed{
M(x^*):=\Lambda(\alpha^*)-L_H(\beta^*)\succeq0.
}
\tag{REC.20}
$$

This is the selected-stress version of C64. It is important that no zero-beta actual
boundary terminal was demoted to the interior.

The selected contact network is still circular planar on the fixed cyclic boundary
`B`: every `b in B` is an extreme vertex of the original force hull, and deleting
zero-conductance edges or leaving an isolated boundary terminal does not change that
embedding. Circular minors remain nonnegative; disconnected cases are obtained
literally as resistor networks with zero conductances, not by an unsupported
continuity step.

---

## 7. Near-zero full-support phase reduces to a near-zero PSD circuit

Let `x_D^ri` be any sequence of full-support relative-interior normalized KKT stresses
on hypothetical C-II sources with

$$
D\varepsilon(x_D^{ri})\to0.
\tag{REC.21}
$$

By REC.2 choose a polytope vertex `x_D^*` with

$$
0\le\varepsilon(x_D^*)
\le\varepsilon(x_D^{ri}).
$$

Then

$$
\boxed{
D\varepsilon(x_D^*)\to0.
}
\tag{REC.22}
$$

By REC.3 its entire positive mixed support is one actual rigidity circuit, and by C53
its selected stress matrix is PSD. REC.20 gives the fixed-boundary PSD response defect
needed by C66.

Rerun C66 using the selected positive diameter edges. Its proof needs only:

1. `M(x_D^*)>=0`;
2. circular-planar response inequalities on the fixed boundary `B`;
3. C43 for source triples;
4. the fact that selected positive diameter edges are actual diameter edges; and
5. `|supp beta^*|<=|H|<=pi D`.

Therefore the same C66 constant `C_0` gives a selected diameter vertex `z_D` with

$$
\boxed{
\sum_{\substack{h\in H\\z_D\in h}}\beta_h^*
\ge
1-C_0D\varepsilon(x_D^*)
=1-o(1).
}
\tag{REC.23}
$$

### Corollary REC.4 - circuit-star reduction

Every hypothetical full-support C66 sequence contains, on the same source, a sequence
of normalized PSD rigidity-circuit stresses whose response defects are no larger and
whose diameter weights converge to one star.

---

## 8. Exact zero defect lands on the C80 chain face

If an extreme stress has

$$
\varepsilon(x^*)=0,
$$

then C66 on its selected support gives exact star support:

$$
\sum_{h\ni z}\beta_h^*=1.
$$

The C68/C80 exact-star argument applies to the positive selected support: zero radial
defect forces every positive contact onto radial rays from `z`; the large-D star-angle
gap leaves one positive branch and one diameter leaf. Thus the selected support is the
straight unit contact chain joining one actual diameter pair, with its endpoint
diameter bar.

So the minimum-defect circuit endpoint is not an abstract network equality. Its exact
zero face is the already identified straight-chain KKT atom.

This does **not** imply that the complete actual source framework is a chain. Other
actual contacts and diameter rows may have zero coefficient at this extreme stress and
remain geometrically active.

---

## 9. What this changes in the live frontier

Previously the C66 phase was formulated using a relative-interior stress because full
support was needed for the global ZR/ZF stack. REC separates those jobs:

1. keep the relative-interior stress for the full-support ZR/ZF rigidity and exact
   ledgers;
2. minimize `epsilon` over the same normalized KKT polytope;
3. analyze the resulting extreme PSD **circuit** stress for the near-zero response
   obstruction.

Therefore a closing theorem for the near-zero phase only needs to exclude

> PSD rigidity circuits contained in the actual C65 mixed framework whose selected
> response defect is `o(1/D)` and whose diameter stress is `1-o(1)` on one star,

unless the complete source already contains a triangle or admits a strict diameter
release.

This is exactly the setting where the C80--C85 chain-face Hessian and secondary-stress
machinery becomes relevant: a near-zero full-source certificate has an extreme circuit
representative approaching the straight-chain KKT face.

---

## 10. Regression audit

- Concavity has the correct direction: Dirichlet energy is a minimum of functions
  linear in the conductances, hence concave, not convex.
- The fixed-boundary energy definition remains valid when selected conductances vanish;
  zero-conductance interior components only make the minimizing extension nonunique.
- `epsilon>=0` is reproved for every selected stress from coordinate energy; it is not
  assumed from the full-support C64 theorem.
- The selected PSD Schur defect is taken on the fixed actual boundary; zero-beta
  boundary terminals are not silently demoted.
- The extreme circuit may omit many actual rows. REC does not infer that those rows are
  geometrically inactive.
- Circuit support does not give a uniform lower bound on its nonzero coefficients.
  Tiny positive nonstar diameter weights remain possible.
- Exact zero selected defect yields a straight-chain selected support, not a straight
  full source.
- No Level I conclusion is claimed.

---

## 11. Next target

The shortest follow-up is a **chain-face isolation theorem** for circuit stresses:

> prove that an actual Target C mixed framework cannot contain a sequence of PSD
> rigidity circuits with `D epsilon -> 0` converging to the C80 straight-chain stress
> while the full relative-interior stress retains ZR affine kernel and ZF rigidity.

There are two existing handles.

1. C84/C85 describe the first- and second-order diameter blockers needed around the
   straight-chain KKT face.
2. Full-support ZF plus the new main mixed-redundant-rigidity/cut theorems constrain how
   the omitted actual rows can attach to that circuit.

REC turns those previously separate statements into one finite selected-support
problem.