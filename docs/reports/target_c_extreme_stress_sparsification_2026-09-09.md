<!-- theorem-state: {"artifact_id":"ART-A1BC657FB44B","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — extreme-stress sparsification from the mixed-row surplus

**Date:** 2026-09-09  
**Run type:** exact convex-geometric / KKT-polytope theorem  
**Target:** Target C C-II after ZF  
**Depends on:** C53 universal selected-stress PSD, C65 full actual KKT support, connected diameter-spanning positive support for every normalized stress, ZF mixed rigidity rank, NB branching theorem  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

The post-ZF currency

\[
s_Z:=e+h-(2v-2)\ge0
\]

has so far been used mainly as a mixed-row surplus. It has a second exact meaning: it is the affine dimension of the normalized KKT stress polytope. Consequently every extreme normalized stress simultaneously deletes at least `s_Z` actual contact/diameter constraints from its positive support, while retaining universal PSD and the canonical connected diameter-spanning positive contact component.

This converts the NB branch `s_Z=Omega(D)` into a literal sparse-support selected-stress problem.

---

## 1. Signed equilibrium space

Work on the nonisolated C65 core. Let `v` be its vertices, `e` its actual unit contacts, `h` its actual diameter pairs, and `m=e+h`.

Let `R` be the ordinary planar bar-rigidity matrix for the equality framework on `C union H`. ZF gives

\[
\boxed{\operatorname{rank}R=2v-3.}
\tag{ES.1}
\]

A KKT multiplier is `x=(alpha,beta)>=0` with equilibrium

\[
\sum_{j:ij\in C}\alpha_{ij}(p_i-p_j)
=
\sum_{j:ij\in H}\beta_{ij}(p_i-p_j).
\tag{ES.2}
\]

Changing the sign of the diameter coordinates identifies the full linear KKT equilibrium space `W` with the ordinary bar self-stress space. Hence

\[
\begin{aligned}
\dim W
&=m-\operatorname{rank}R\\
&=(e+h)-(2v-3)\\
&=s_Z+1.
\end{aligned}
\tag{ES.3}
\]

The normalized KKT polytope is

\[
\mathcal P
=
\left\{(\alpha,\beta)\in W\cap\mathbb R^m_{\ge0}:\sum_{h\in H}\beta_h=1\right\}.
\tag{ES.4}
\]

C65 supplies a normalized point `x^0=(alpha^0,beta^0)` with every actual contact and diameter coordinate strictly positive.

---

## 2. The normalization functional is transverse

Let `K=W cap R^m_{>=0}` and `L(alpha,beta)=sum_H beta`.

### Lemma ES.1

Every nonzero `x in K` satisfies

\[
\boxed{L(x)>0.}
\tag{ES.5}
\]

### Proof

If `L(x)=0`, nonnegativity gives `beta=0`. Equilibrium becomes a nonnegative contact-only self-stress. Dot the equation at each vertex with its position and sum. Every unit contact contributes `alpha_ij`, so

\[
\sum_{ij\in C}\alpha_{ij}=0.
\]

All `alpha_ij` are nonnegative, hence all vanish. Thus `x=0`, contradiction. `square`

The same calculation gives the unnormalized virial identity

\[
\boxed{\sum_C\alpha=D^2\sum_H\beta.}
\tag{ES.6}
\]

Therefore on `P`,

\[
\sum_C\alpha=D^2,
\qquad
\sum_H\beta=1,
\tag{ES.7}
\]

so `P` is compact.

---

## 3. `s_Z` is exactly the normalized stress-polytope dimension

### Theorem ES.2

\[
\boxed{\dim_{aff}\mathcal P=s_Z.}
\tag{ES.8}
\]

### Proof

By ES.3, `dim W=s_Z+1`. Since `x^0` is strictly positive, for every `w in W` one has `x^0+-tw>=0` for sufficiently small `t`; thus the nonnegative KKT cone has full relative dimension in `W`.

The functional `L` is nonzero on `W` by Lemma ES.1. Hence `W cap {L=1}` has dimension `s_Z`. The same two-sided perturbation argument for every `w in W cap ker L` shows `x^0` is a relative-interior point of `P` in that hyperplane. Therefore `dim_aff P=s_Z`. `square`

Thus `s_Z` is an actual moduli dimension of normalized nonnegative equilibrium stresses, not only a row-count slack.

---

## 4. Extreme stresses delete at least `s_Z` actual rows

### Theorem ES.3 — extreme-support sparsification

For any vertex `x*=(alpha*,beta*)` of `P`, at least `s_Z` coordinates vanish. Equivalently,

\[
\boxed{|supp(x^*)|\le m-s_Z=2v-2.}
\tag{ES.9}
\]

### Proof

Let `Z={j:x*_j=0}`. If `|Z|<s_Z=dim_aff P`, the tangent space of `aff P` contains a nonzero vector `w` satisfying `w_j=0` for every `j in Z`: fewer than `s_Z` homogeneous coordinate conditions cannot kill an `s_Z`-dimensional tangent space.

All coordinates outside `Z` are strictly positive at `x*`. For sufficiently small `t>0`, both `x*+tw` and `x*-tw` remain nonnegative, normalized, and in equilibrium. Hence

\[
x^*=\tfrac12(x^*+tw)+\tfrac12(x^*-tw)
\]

is a nontrivial convex decomposition in `P`, contradicting extremality. Thus `|Z|>=s_Z`. `square`

Write

\[
z_C=|\{e\in C:\alpha^*_e=0\}|,
\qquad
z_H=|\{h\in H:\beta^*_h=0\}|.
\]

Then

\[
\boxed{z_C+z_H\ge s_Z,}
\tag{ES.10}
\]

so at least one of

\[
\boxed{z_C\ge s_Z/2}
\qquad\text{or}\qquad
\boxed{z_H\ge s_Z/2}
\tag{ES.11}
\]

holds.

---

## 5. The sparse extreme stress remains a valid Target C selected stress

C53 proves universal selected-stress PSD. Hence for every vertex `x*` of `P`,

\[
\boxed{\Omega(x^*)=L_C(\alpha^*)-L_H(\beta^*)\succeq0.}
\tag{ES.12}
\]

The canonical support theorem applies to every normalized KKT stress: the positive contact graph has exactly one nontrivial connected component, it contains the endpoints of every positive diameter edge, and it spans Euclidean diameter `D`.

Therefore ES.3 supplies, on the same source, a normalized stress with all of the following simultaneously:

1. KKT equilibrium and nonnegative multipliers;
2. PSD stress matrix;
3. one connected positive contact component spanning `D`;
4. at least `s_Z` actual mixed constraints absent from positive support.

No equivalent network, replacement hull, or modified source is used.

---

## 6. Quantitative consequence in the NB `s_Z` branch

NB proves

\[
x_B+Q+2s_Z\ge(c_*-o(1))D,
\qquad c_*=0.6099043189\ldots .
\tag{ES.13}
\]

Its crude three-way split includes

\[
s_Z\ge(c_*/6-o(1))D
=0.1016507198\ldots D-o(D).
\tag{ES.14}
\]

In that branch, an extreme normalized PSD stress omits at least

\[
\boxed{(0.1016507198\ldots-o(1))D}
\tag{ES.15}
\]

actual rows. Moreover either at least

\[
(0.0508253599\ldots-o(1))D
\]

actual contacts vanish from its positive support, or at least that many actual diameter pairs vanish from its positive support.

This is not yet a contradiction. It turns the `s_Z` alternative into a concrete selected-support theorem that can be attacked by C30-C32/C50, maximal-support duality, C63 finite integration, and the ZM response defect.

---

## 7. Extreme PSD kernels recover the affine kernel collectively

Let `x^(1),...,x^(N)` be the vertices of `P`. A relative-interior point `x^0` admits a convex representation with positive coefficients on a finite vertex family,

\[
x^0=\sum_r\lambda_r x^{(r)},
\qquad \lambda_r>0.
\tag{ES.16}
\]

Linearity and universal PSD give

\[
\Omega(x^0)=\sum_r\lambda_r\Omega(x^{(r)}),
\]

and for PSD matrices the kernel of a positive sum is the intersection of the kernels. Therefore

\[
\boxed{\ker\Omega(x^0)=\bigcap_r\ker\Omega(x^{(r)}).}
\tag{ES.17}
\]

ZR gives

\[
\ker\Omega(x^0)=span\{\mathbf1,P_x,P_y\}.
\]

By Caratheodory, a representation of `x^0` needs at most `s_Z+1` vertices after discarding zero coefficients. Thus one may choose `k<=s_Z+1` sparse extreme PSD stresses such that

\[
\boxed{span\{\mathbf1,P_x,P_y\}=\bigcap_{r=1}^{k}\ker\Omega(x^{(r)}).}
\tag{ES.18}
\]

Individual extreme stresses may have larger kernels; no non-affine scalar mode survives all of them.

---

## 8. Regression audit

- Zero multipliers do not imply weak geometric constraints. Other stresses may support those actual rows.
- The deleted rows need not be predominantly diameters; ES.11 is only a two-way half-size dichotomy.
- No lower bound on remaining positive coefficients is obtained.
- Extreme stresses may have stress-matrix rank below `v-3`; ZR belongs to the relative-interior full-support stress. ES.17 is the correct collective replacement.
- The theorem does not use global optimality beyond the existing C65/ZF stack, so local shell regressions are not falsely excluded.

---

## 9. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| `dim W=s_Z+1` | proved | ZF mixed bar rank |
| normalization is positive on the nonnegative stress cone | proved | virial identity |
| `dim_aff P=s_Z` | proved | C65 full-positive point |
| every extreme stress has at least `s_Z` zero coordinates | proved | tangent-space argument |
| extreme stresses remain PSD | C53 input | universal selected-stress PSD |
| extreme positive contact support remains connected and spans `D` | canonical input | every normalized stress |
| linear `s_Z` gives linear simultaneous row deletion | proved | ES.3 + NB branch threshold |
| row deletion closes Level I | not proved | support omission is not geometric release |

---

## 10. Next theorem

The `s_Z` branch is now an explicit selected-support problem.

- If many omitted rows are diameter pairs, compare the sparse positive diameter support with the full actual diameter thrackle using C30-C32/C50 and ZM.
- If many omitted rows are contacts, use maximal-support critical-cone duality and C63 finite integration to quantify how many simultaneously zero contact multipliers can remain strong without a common release.

The direct Level I endpoint remains the exact face contradiction.
