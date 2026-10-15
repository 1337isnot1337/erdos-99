# Target C — audited §§156–157 exceptional-face closure rank and two-sided outer-train bracing

**Date:** 2026-09-12  
**Lifecycle:** audited-working proof-only route module; theorem-state authority unchanged.  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This is the renumbered clean replacement for the two exact theorems originally developed on PR #403. Section 155 is already occupied by the quantitative atomic-detour theorem, so the closure-rank theorem is §156 and the response-free bracing theorem is §157.

All rigidity statements below are on the connected nonisolated positive-contact core. Contact-isolated source points remain in the full source and are never inserted into the Section-57 core matrix.

---

# §156 — exceptional-face closure corank and Hall expansion

Let `G=(V,C)` be the connected positive-contact core, with `v=|V|`, `e=|C|`. Let `H` be the full actual diameter graph after C65 normalization, `h=|H|`, and

\[
s_Z=e+h-(2v-2)\ge0.
\]

Canonical mixed rigidity gives

\[
\operatorname{rank}R_{C\cup H}=2v-3.
\tag{156.1}
\]

Let `R` be the number of bounded strict-rhombus faces, `f` the number of bounded nonquadrilateral faces, and `T` the complete stopped-train count. Audited §142 gives

\[
T=e-2R.
\tag{156.2}
\]

Euler gives

\[
e-v=R+f-1,
\tag{156.3}
\]

and the exact train/core ledger gives

\[
T=h-s_Z+2f.
\tag{156.4}
\]

## 156.1 Train angular coordinates

For an oriented unit contact edge `ij`, write `r_{ij}=p_j-p_i`. Every infinitesimal contact flex satisfies

\[
u_j-u_i=\omega_{ij}Jr_{ij}
\]

for a unique scalar `omega_ij`. On each strict rhombus, differentiated vector closure forces equality of angular rates on opposite sides. Therefore the rate is constant on each complete stopped train; denote it `omega_tau`.

Conversely, assign one scalar `omega_tau` to every train and prescribe

\[
\dot r_e=\omega_{\tau(e)}Jr_e.
\]

Strict-rhombus cycles close automatically. The only remaining cycle equations are the vector closures around bounded nonquadrilateral faces.

For each such face `F`, using boundary **occurrences**, impose

\[
\sum_{e\in\partial F}\omega_{\tau(e)}Jr_e=0.
\tag{156.5}
\]

Collecting the two scalar coordinates for all `f` faces defines

\[
C_{face}:\mathbb R^T\to\mathbb R^{2f}.
\]

Because bounded face boundaries span the real cycle space of a connected plane graph even with bridges and articulation vertices, integration along contact paths gives

\[
\boxed{
\ker R_C/\mathrm{Trans}\cong\ker C_{face}.
}
\tag{156.6}
\]

The all-ones train-rate vector is the global infinitesimal rotation modulo translation.

## 156.2 Exact corank identity

Write `r=rank(C_face)` and

\[
\sigma_C:=\dim\ker R_C^T.
\]

From (156.6),

\[
\dim\ker R_C=T-r+2,
\]

hence

\[
\sigma_C=e-\operatorname{rank}R_C=e-2v+T-r+2.
\]

Using (156.2) and (156.3),

\[
e-2v+T+2=2f.
\]

Therefore

\[
\boxed{
2f-\operatorname{rank}C_{face}=\sigma_C.
}
\tag{156.7}
\]

The mixed left nullity from (156.1) is

\[
\dim\ker R_{C\cup H}^T=s_Z+1.
\]

Every pure contact self-stress extends to this mixed kernel with zero diameter coordinates. C65 supplies one mixed KKT stress with nonzero diameter part, independent of that pure-contact subspace. Thus

\[
\boxed{
0\le\sigma_C\le s_Z,
\qquad
\operatorname{rank}C_{face}\ge2f-s_Z.
}
\tag{156.8}
\]

No individual KKT coefficient floor is required.

## 156.3 Hall expansion

For any set `S` of bounded nonquadrilateral faces, let `C_S` be their `2|S|` closure rows and `N(S)` the complete trains having an endpoint occurrence on at least one face in `S`.

Any dependence among rows of `C_S`, extended by zeros, is a dependence of the full matrix. Hence

\[
2|S|-\operatorname{rank}C_S\le\sigma_C.
\]

Since `C_S` is supported only on columns `N(S)`,

\[
\operatorname{rank}C_S\le|N(S)|.
\]

Therefore

\[
\boxed{
|N(S)|\ge2|S|-\sigma_C\ge2|S|-s_Z.
}
\tag{156.9}
\]

This holds simultaneously for every face subset.

## 156.4 Outer-to-outer train capacity

Let `L_OO` be the number of complete trains whose two terminal occurrences are on the outer face. Those are zero columns of `C_face`. Conversely, audited §132 and the singleton bounded-loop exclusion show that any train with a bounded endpoint contributes a nonzero bounded-face column. Thus the zero columns are exactly the outer-to-outer trains.

Hence

\[
\operatorname{rank}C_{face}\le T-L_{OO}.
\]

Using (156.4), (156.7), and `sigma_C<=s_Z`,

\[
\boxed{L_{OO}\le h.}
\tag{156.10}
\]

If `f>0`, the coordinate subspace supported only on those outer-to-outer columns does not contain the all-trains rotation vector. It gives `L_OO` independent non-Euclidean contact-flex directions. Mixed rigidity maps them injectively into the `h` diameter first-variation coordinates, while KKT stationarity places the image in the codimension-one hyperplane orthogonal to the positive diameter multiplier vector. Therefore

\[
\boxed{f>0\Longrightarrow L_{OO}\le h-1.}
\tag{156.11}
\]

---

# §157 — response-free two-sided bracing of every outer-to-outer train

Section 156 is a rank statement. Section 157 proves a signed geometric strengthening for each individual outer train.

## 157.1 Uniqueness of parallel diameter segments

If a finite Euclidean set of diameter `D` contains two parallel diameter segments, orient them in the same direction:

\[
b-a=Du,
\qquad d-c=Du,
\qquad |u|=1.
\]

Put `v=c-a`. Since all distances are at most `D`,

\[
|Du-v|\le D,
\qquad |Du+v|\le D.
\]

Squaring and adding gives `2D^2+2|v|^2<=2D^2`, so `v=0`. Thus the two unordered diameter pairs coincide.

## 157.2 KKT cut resultant

Let `tau` be an outer-to-outer complete stopped train. The audited finite train cut/shear primitive gives a Jordan shore split

\[
V=S\sqcup T
\]

whose contact cut is exactly the parallel contact edges of `tau`.

Orient every cut contact from `T` into `S` with common unit vector `u`. With positive KKT contact weights `alpha_e` and actual diameter weights `beta_h`, put

\[
A_\tau=\sum_{e\in E(\tau)}\alpha_e>0.
\]

Summing equilibrium over the shore `S` cancels all internal forces and gives

\[
\boxed{
A_\tau u
=\sum_{\substack{h=xy\in H\\x\in T,\ y\in S}}
\beta_h(p_y-p_x).
}
\tag{157.1}
\]

So at least one actual diameter edge crosses the train cut. If the crossing vector is oriented `r_h=p_y-p_x`, dotting with `Ju` gives

\[
\boxed{
\sum_{h\pitchfork\tau}\beta_h(r_h\cdot Ju)=0.
}
\tag{157.2}
\]

## 157.3 Two transverse signs are mandatory

Assume the values `r_h dot Ju` do not contain both signs. Because every `beta_h>0`, (157.2) forces every one to be zero. All crossing diameter segments are then parallel to `u`, so by the uniqueness lemma there is exactly one crossing diameter pair. Equation (157.1) fixes its oriented vector as

\[
r_h=Du.
\tag{157.3}
\]

Apply the exact finite one-train shear: keep shore `T` fixed and translate the entire other source shore `S` by

\[
\Delta_\theta=R_\theta u-u.
\tag{157.4}
\]

Every old cut contact vector changes from `u` to `R_theta u`, preserving unit length; every same-shore old contact is unchanged. For sufficiently small `theta`, all strict old noncontacts stay strictly longer than one.

The unique crossing diameter changes from `Du` to `Du+Delta_theta`, with

\[
\begin{aligned}
|Du+\Delta_\theta|^2
&=D^2+2D(\cos\theta-1)+2(1-\cos\theta)\\
&=D^2-2(D-1)(1-\cos\theta)
<D^2
\end{aligned}
\tag{157.5}
\]

for nonzero small `theta` and `D>1`.

All same-shore old diameter pairs are unchanged; there are no other crossing old diameter pairs. Every strict old nondiameter pair remains below `D` for small enough `theta` by finite slack. The **full source**, including contact-isolated points assigned to their geometric shore, therefore stays unit-separated, keeps its cardinality and contact graph, and has diameter at most `D`.

If any same-shore diameter remains, the result is another global minimizer with the same contacts but strictly fewer actual diameter pairs, contradicting the secondary lexicographic normalization. If none remains, the new source has diameter strictly below `D`, contradicting global minimality.

Therefore the assumption was impossible:

\[
\boxed{
\forall\tau\text{ outer-to-outer},\quad
\exists h_+,h_-\pitchfork\tau:
\quad r_{h_+}\cdot Ju>0,
\quad r_{h_-}\cdot Ju<0.
}
\tag{157.6}
\]

In particular every outer-to-outer train is crossed by at least two distinct actual diameter edges.

---

## Frontier effect and scope

Sections 156–157 eliminate low-rank exceptional-face closure systems and one-sided/unbraced outer trains. They do **not** yet imply a large number of distinct diameter edges: one diameter edge may cross many nested train cuts. The live next steps are therefore multi-train shear correlations, cut order versus the convex diameter thrackle, or use of the full positive KKT vector resultants rather than support incidence alone.

- contact isolates remain outside all core rigidity matrices and are retained in finite source shears;
- bridges/articulations and face occurrence signs are retained;
- pure contact self-stress is not set to zero; its exact dimension is `sigma_C`;
- no response conductance theorem or KKT coefficient lower bound is used.

**Disposition:** §§156–157 are audited-working proof-only structural theorems. C-II and Level I remain open.
