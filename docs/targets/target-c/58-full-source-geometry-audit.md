# Target C — independent full-source geometry audit

**Date:** 2026-09-11  
**LEVEL I STATUS:** **STILL OPEN.**  
**Disposition:** universal full-source geometry and the post-ZF support-dispersion consequence are independently certified below.

This module audits the load-bearing mathematics in three September 10 reports without promoting their unrelated handoff prose:

- `docs/reports/target_c_full_source_circumradius_response_2026-09-10.md`;
- `docs/reports/target_c_full_source_perimeter_and_lattice_excess_2026-09-10.md`;
- `docs/reports/target_c_full_source_post_zf_diameter_dispersion_2026-09-10.md`.

The first two theorem groups hold for **every** noncollinear global minimizer, with every source point retained. The final support-dispersion theorem additionally uses the canonical ZR/ZF normalization from `57-zr-zf-rigidity-audit.md`.

No claim below closes C-II or Level I.

## 1. Universal full-source circumradius

Let `A` be a global `n`-point unit-separated minimum-diameter configuration, let

\[
D=D(n),\qquad K=\operatorname{conv}A,\qquad P=\operatorname{per}K,
\]

and set

\[
a_0={\sqrt3\over2},\qquad c_0={\sqrt3\over4},\qquad
\eta=3^{1/4}\sqrt D.
\]

The finite Oler inequality gives

\[
\operatorname{area}K+c_0P\ge a_0(n-1).
\]

The canonical strict translated-triangular-lattice comparison is

\[
D^2<{2\sqrt3\over\pi}(n-1),
\]

hence

\[
a_0(n-1)>{\pi D^2\over4}.
\]

Therefore

\[
\operatorname{area}K>{\pi D^2\over4}-c_0P.
\]

Using Cauchy's perimeter-diameter inequality `P<=pi D`,

\[
\begin{aligned}
P^2-4\pi\operatorname{area}K
&<P^2-\pi^2D^2+4\pi c_0P\\
&\le \pi^2\sqrt3\,D.
\end{aligned}
\]

Bonnesen's inequality

\[
P^2-4\pi\operatorname{area}K\ge\pi^2(R-r)^2
\]

for circumradius `R` and inradius `r` of `K` now gives

\[
R-r<\eta.
\]

Since every inscribed disk has diameter at most `D`, `r<=D/2`; since `K` contains a diameter pair, `R>=D/2`. Thus

\[
\boxed{{D\over2}\le R(K)<{D\over2}+\eta.}
\tag{FS.1}
\]

This proof is direct. It does not require Target A Section 155 or any bound on the number of contact-isolated points.

For any normalized KKT stress, let `B_s` be its positive diameter endpoints and `F_s=conv(B_s)`. A positive diameter edge exists because `sum beta=1`, so `diam(F_s)=D`; also `F_s subset K`. Circumradius is monotone under inclusion. Hence

\[
\boxed{{D\over2}\le R(F_s)\le R(K)<{D\over2}+\eta.}
\tag{FS.2}
\]

This is valid uniformly over all normalized KKT stresses of the same source.

## 2. Reciprocal-force perimeter saturation

For a normalized stress write

\[
s_b=\sum_k\beta_{bk},\qquad
g_b=\sum_k\beta_{bk}(p_b-p_k),\qquad
P_*=\sum_b|g_b|.
\]

Let `o` be the full-source circumcenter used above. Grouping endpoint contributions of every diameter edge gives the exact virial identity

\[
\sum_b(p_b-o)\cdot g_b=D^2.
\]

Therefore

\[
D^2\le R(K)P_*.
\]

At the same time

\[
|g_b|\le D s_b,
\qquad
\sum_b s_b=2,
\]

so `P_*<=2D`. Substituting FS.1 yields

\[
\boxed{
{2D\over1+2\eta/D}<P_*\le2D,
\qquad
0\le2D-P_*<{4\eta\over1+2\eta/D}<4\eta.
}
\tag{FS.3}
\]

Thus `P_*/D -> 2` uniformly over all normalized stresses of every global source.

## 3. Every diameter star has vanishing angular width

Suppose two distinct diameter edges `by` and `bz` share endpoint `b`, and let their smaller angle be `theta`. Since `|y-z|<=D`, `theta<=pi/3`. The triangle `byz` is acute, with minimum enclosing-circle radius

\[
R_{byz}={D\over2\cos(\theta/2)}.
\]

It is contained in `K`, so FS.1 gives

\[
{D\over2\cos(\theta/2)}<{D\over2}+\eta.
\]

Therefore

\[
\boxed{
\theta<\vartheta_D:=
2\arccos\!\left({D\over D+2\eta}\right)
=(4\,3^{1/8}+o(1))D^{-1/4}.
}
\tag{FS.4}
\]

Unit separation of two partners on the radius-`D` circle about `b` gives angular separation at least

\[
a_D=2\arcsin{1\over2D}.
\]

Because all partner directions lie in an ordinary arc of width `<min(pi/3,vartheta_D)`, ordering them gives

\[
\boxed{
\deg_H(b)\le
\left\lceil{\min(\pi/3,\vartheta_D)\over a_D}\right\rceil
=O(D^{3/4}).
}
\tag{FS.5}
\]

The ceiling form is the sharp safe integer consequence of `(d-1)a_D<vartheta_D`.

## 4. Common-center midpoint localization and coordinate radialization

Put

\[
L_D=\sqrt{D\eta+\eta^2}=O(D^{3/4}).
\]

For every actual diameter pair `bk`, with midpoint `m=(p_b+p_k)/2`, the parallelogram identity gives

\[
|m-o|^2
={|p_b-o|^2+|p_k-o|^2\over2}-{D^2\over4}
<R(K)^2-{D^2\over4}<D\eta+\eta^2.
\]

Hence

\[
\boxed{\left|{p_b+p_k\over2}-o\right|<L_D.}
\tag{FS.6}
\]

For every selected stress,

\[
g_b-2s_b(p_b-o)
=-\sum_k\beta_{bk}(p_b+p_k-2o),
\]

so

\[
\boxed{
|g_b-2s_b(p_b-o)|\le2s_bL_D,
\qquad
\sum_b|g_b-2s_b(p_b-o)|\le4L_D.
}
\tag{FS.7}
\]

If `X_B` has rows `(p_b-o)/D`, `S_B=diag(s_b)`, and `Lambda` is the actual positive-contact Dirichlet response, C11 gives `Lambda X_B=g/D`. Thus

\[
\boxed{
\sum_b\left|(\Lambda X_B-2S_BX_B)_b\right|
\le {4L_D\over D}=O(D^{-1/4}).
}
\tag{FS.8}
\]

This is only a statement on the two affine coordinate fields. It is not an operator-norm estimate on arbitrary boundary data.

Equation FS.6 also pairs every selected endpoint with a point within `2L_D` of its reflection through `o`, so

\[
\boxed{d_{\rm Haus}(F_s-o,-(F_s-o))\le2L_D.}
\tag{FS.9}
\]

Every selected endpoint has radius between `D-R(K)` and `R(K)`, hence after scaling by `D` every subsequential selected force-hull limit is centrally symmetric and is the convex hull of points on the radius-`1/2` circle. This does **not** imply the limit is the disk.

Finally define

\[
V_b=\sum_{k<l}\beta_{bk}\beta_{bl}|p_k-p_l|^2.
\]

Because

\[
|g_b|^2=D^2s_b^2-V_b,
\]

we obtain the exact aggregate partner-dispersion estimate

\[
\boxed{
\sum_b{V_b\over s_b}
=\sum_b(Ds_b-|g_b|)\left(D+{|g_b|\over s_b}\right)
\le2D(2D-P_*)<8D\eta.
}
\tag{FS.10}
\]

No individual positive `beta` floor follows.

## 5. Absolute source-hull perimeter saturation

The same Oler/lattice inputs give more than the circumradius estimate. By the planar isoperimetric inequality,

\[
\operatorname{area}K\le {P^2\over4\pi}.
\]

Together with

\[
\operatorname{area}K+c_0P>{\pi D^2\over4},
\]

this yields

\[
P^2+\pi\sqrt3\,P-\pi^2D^2>0.
\]

Taking the positive root,

\[
\boxed{
P>{\pi\over2}\left(\sqrt{4D^2+3}-\sqrt3\right).
}
\tag{PW.1}
\]

Since `P<=pi D`,

\[
\boxed{
0\le\pi D-P
<{\pi\over2}\left(2D-\sqrt{4D^2+3}+\sqrt3\right)
<{\pi\sqrt3\over2}.
}
\tag{PW.2}
\]

By Cauchy's width formula,

\[
P=\int_0^\pi w_K(\theta)\,d\theta,
\]

so

\[
\boxed{
\int_0^\pi(D-w_K(\theta))\,d\theta
=\pi D-P<{\pi\sqrt3\over2}.
}
\tag{PW.3}
\]

Consequently for every `tau>0`,

\[
\boxed{
\left|\{\theta:w_K(\theta)\le D-\tau\}\right|
<{\pi\sqrt3\over2\tau}.
}
\tag{PW.4}
\]

In particular a fixed relative width deficit occurs on only `O(D^{-1})` angular measure.

## 6. Exact population-excess identity

Define

\[
\Delta={\pi\over2\sqrt3},
\qquad
g_A=n-1-\Delta D^2,
\]

and

\[
\delta_K={\pi D^2\over4}-\operatorname{area}K,
\qquad
\mathscr O_A=\operatorname{area}K+c_0P-a_0(n-1).
\]

The strict lattice comparison gives `g_A>0`. Direct cancellation of the area term gives

\[
\boxed{
\delta_K+\mathscr O_A=c_0P-a_0g_A.
}
\tag{GE.1}
\]

Hence

\[
\boxed{
\delta_K+\mathscr O_A\ge c_0P
\iff g_A\le0
\iff n-1\le{\pi\over2\sqrt3}D^2.
}
\tag{GE.2}
\]

Thus the formerly proposed full-source NC endpoint is exactly the negation of the strict translated-lattice population excess. It is a valid sufficient contradiction, but GE.2 does not prove it from triangle-freeness.

## 7. Post-ZF diameter-support dispersion

Now specialize to the canonical contact-minimal then diameter-pair-minimal C-II representative with `D>=9`, so `H=H_*`. The canonical ZR/ZF audit gives

\[
h=|H|\ge\delta\ge\lceil D\rceil.
\tag{FSD.1}
\]

Set

\[
\Delta_D=
\left\lceil{\min(\pi/3,\vartheta_D)\over a_D}\right\rceil.
\]

FS.5 gives `Delta(H)<=Delta_D`. Therefore every vertex cover `S` satisfies

\[
h\le\sum_{v\in S}\deg_H(v)\le|S|\Delta_D,
\]

so

\[
\boxed{
\tau(H)\ge\left\lceil{h\over\Delta_D}\right\rceil
\ge\left\lceil{\lceil D\rceil\over\Delta_D}\right\rceil.
}
\tag{FSD.2}
\]

The endpoints of a maximum matching form a vertex cover, hence `tau(H)<=2nu(H)` and

\[
\boxed{
\nu(H)\ge\left\lceil{h\over2\Delta_D}\right\rceil
\ge\left\lceil{\lceil D\rceil\over2\Delta_D}\right\rceil.
}
\tag{FSD.3}
\]

Every two disjoint diameter edges cross properly: the planar diameter graph is a straight-line thrackle. FS.6 places the midpoint of every one of these matching edges in `B(o,L_D)`. Since

\[
\Delta_D=(4\,3^{1/8}+o(1))D^{3/4},
\]

we obtain

\[
\boxed{
\tau(H)\ge\left({1\over4\,3^{1/8}}+o(1)\right)D^{1/4},
\qquad
\nu(H)\ge\left({1\over8\,3^{1/8}}+o(1)\right)D^{1/4}.
}
\tag{FSD.4}
\]

Thus bounded-hub and `O(1)`-vertex-cover models of the actual post-ZF diameter support are impossible.

This is a support theorem only. Relative-interior positivity gives no uniform lower bound on the `beta`-mass carried by the matching.

## 8. Regression audit

The regular odd unit shell is a necessary regression. Let `h>=5` be odd, `a=pi/(2h)`, and

\[
D_h={1\over2\sin a}.
\]

With contact weights `alpha=D_h^2/h` on the side cycle and diameter weights `beta=1/h` on the diameter cycle,

\[
P_*=2D_h\cos a,
\qquad
2D_h-P_*=\tan(a/2)\sim{1\over4D_h}.
\]

Yet a matching in the odd diameter cycle retains at most `(h-1)/(2h)->1/2` of the total `beta` weight. Therefore near equality `P_*->2D` does not imply near-matching support after deleting `o(1)` weight.

For the actual side-cycle response `Lambda`,

\[
\operatorname{tr}(\Lambda-L_H)=2D_h^2-2.
\]

Its Fourier eigenvalues are

\[
{4\over h}\left[
D_h^2\sin^2{\pi j\over h}-
\sin^2{\pi ((h-1)/2)j\over h}
\right].
\]

They vanish exactly for `j=0,1,h-1` and are positive otherwise. Thus

\[
\Lambda-L_H\succeq0,
\qquad
\ker(\Lambda-L_H)=\operatorname{span}\{1,P_x,P_y\},
\]

while the trace defect is quadratic. Dense strictly separated interior fillings preserve this response/stress regression and can have asymptotically hexagonal density, but they have no global-optimality certificate.

Accordingly none of the following may be promoted from FS/PW/FSD alone:

- `P_*=2D-o(1)` implies almost all `beta` weight lies in a matching;
- coordinate radialization implies a small response trace defect;
- near-centered crossing diameter support implies a positive matching-weight floor;
- near-circular full-source geometry alone proves the population-excess contradiction;
- C-II or Level I is closed.

## 9. Canonical effect

The audited universal input available to every future C-II argument is now:

\[
R(K)={D\over2}+O(\sqrt D),
\qquad
\pi D-P=O(1),
\]

uniformly over selected stresses,

\[
R(F_s)={D\over2}+O(\sqrt D),
\qquad
P_*=2D-O(\sqrt D),
\]

with actual diameter-star angles `O(D^{-1/4})`, diameter-pair midpoints within `O(D^{3/4})` of one source circumcenter, and coordinate-field response radialization `O(D^{-1/4})`.

On the post-ZF lexicographic C-II source, the actual diameter graph additionally has

\[
\Delta(H)=O(D^{3/4}),
\qquad
\tau(H),\nu(H)=\Omega(D^{1/4}),
\]

and the guaranteed matching chords cross pairwise near the common source center.

The exact full-source scalar closure remains GE.2. A future proof must use global optimality plus triangle-free/contact-response structure to force nonpositive population excess, or construct a strict sub-`D` competitor. The regular-shell regressions show why local stress, leading density, and near-antipodality alone are insufficient.

## 10. Audit.206 midpoint sharpening

The support-function area-energy estimate in the independent Audit.206 sharpens the universal midpoint conclusion without additional hypotheses: for every noncollinear global minimizer with `D>=7`, the full-source support derivative satisfies `|h'|<6D^(2/3)` at differentiability directions and at one-sided limits, and each actual diameter midpoint lies within `7D^(2/3)` of the full-source circumcenter. For `D>=21952`, the full actual diameter graph has maximum degree at most `56D^(2/3)+1`. These bounds retain every source point, including contact isolates. They improve the earlier `O(D^(3/4))` midpoint and degree estimates; they do not provide a source motion or change the full-source scalar closure. See [the independent Audit.206](../../audits/target_c_midpoint_and_quantitative_hull_train_independent_audit_2026-10-09.md).

## 11. Audit.207 hull-face terminal normals and pentagon budget

The independent Audit.207 uses the support-derivative bound above to show that the outward normal of a bounded face terminal edge of a hull-ended train agrees with its actual full-source loaded-hull side normal, which is within `O(D^(-1/3))` of the radial direction. Its all-branch face-end count is `E_HF<=Q+f_5+O(D^(5/6))`; exact loaded-hull incidence then gives `f_5>=2(k-m)-O(D^(5/6))` and `q+m>=4k+u_B-O(D^(5/6))`. This is compatible with the finite pentagonal-flower regression because the result is asymptotic and charges long trains; it creates no source motion or full-source scalar closure. See [the independent Audit.207](../../audits/target_c_hull_face_end_pentagon_budget_independent_audit_2026-10-09.md).

## 12. Audit.208 single-port lattice chain

The finite seven-site lemma shows that five triangular-lattice neighbors, each unit from a seven-site unit chain and separated from every chain site, force the chain tangent to a lattice unit direction when consecutive anchor pairs are distinct. In a canonical triangle-free source, compactness transfers this to any qualifying seven-vertex loaded hull window with five actual one-port neighbors that are uniformly close to one translated lattice from a fixed finite orientation set. The proof uses the full-source midpoint and support-derivative bounds and keeps every source point. Under the explicit local chart and defect hypotheses, at most `6m+5b_0+4R_D+o(D)` loaded vertices can occur, contradicting `q>=D` when all three defect counts are sublinear. No atlas extraction, positional transport, source move, or C-II closure is claimed. See [the independent Audit.208](../../audits/target_c_single_port_lattice_chain_independent_audit_2026-10-09.md).

## 13. Audit.209 three-port finite direction bound

For distinct anchors `a_0,a_1,a_2` and integer contact indices `0<r<s`, the squared-distance equations produce at most two determinant-singular directions and a degree-four equation for every regular direction. The possible rational identity branch is impossible under the distinct-anchor and `r<s` hypotheses, giving at most ten directions total. The result is an exact finite lemma; its repeated-anchor variant, source extraction, and any finite motion are not promoted. See [the independent Audit.209](../../audits/target_c_three_port_finite_direction_independent_audit_2026-10-09.md).

## 14. Audit.210 finite-atlas single-port scarcity

For a fixed finite atlas of unit-rhombic charts with uniform `o(1)` approximation on each fixed-size loaded unit run, any canonical C-II sequence with `m=o(D)` nonunit loaded-hull sides has only `o(D)` loaded vertices carrying chosen actual neighbors in the atlas. Three same-chart ports in a rich block give a distinct-anchor chain pattern controlled by Audit.209, and full-source diameter-normal windows count all rich-block vertices. The finite ledger includes an extra `2m` for nonunit sides at block boundaries. This does not extract the atlas or `m=o(D)` and supplies no source move or C-II closure. See [the independent Audit.210](../../audits/target_c_finite_atlas_single_port_scarcity_independent_audit_2026-10-09.md).

## 15. Audit.211 repeated-anchor and near-unit port scarcity

`C-THREE-PORT-REPEATED-ANCHOR-DIRECTION-BOUND` permits coincident anchors provided the explicit cross-pair lower bound from the first anchor to the middle chain site is retained; the direction count is at most ten. Under the fixed finite local atlas hypothesis, `C-NEAR-UNIT-ATLAS-PORT-SCARCITY` replaces the `m=o(D)` premise with `P_F-q=o(D)`, deriving `a_D=o(D)` by discarding the `o(D)` sides whose excess exceeds a shrinking threshold. The local translated-lattice approximation must hold uniformly on every bounded physical loaded window. The atlas and saturation are not extracted; no motion or C-II closure follows. See [the independent Audit.211](../../audits/target_c_near_unit_atlas_port_scarcity_independent_audit_2026-10-09.md).

## 16. Audit.212 bounded-variation chart ports

`C-ACTUAL-DIAMETER-ENDPOINT-STRIP-BOUND` gives `|E intersect S|<=4*sqrt(2Dw)+4w+4` for the actual diameter endpoints of any finite unit-separated source. A fixed finite family of actual additive charts with uniformly bounded total shore variation can therefore have only `o(D)` chosen loaded-to-unloaded unit ports when `P_F-q=o(D)`: remove the `o(D)` endpoints near the `O(D^(1/4))` large shore increments, use the growing index radius `D^(1/8)`, and apply Audit.211's near-unit finite-atlas scarcity to the retained ports. The chart family and saturation are not extracted, and there is no motion or C-II closure. See [the independent Audit.212](../../audits/target_c_bounded_variation_chart_port_scarcity_independent_audit_2026-10-09.md).

## 17. Audit.213 tau-D binary loaded-owner side pocket budget

`C-TAU-D-BINARY-OWNER-SIDE-POCKET-BUDGET` bounds by `u_B` all distinct loaded endpoint pairs with distinct nonzero owners and `1<|a-b|<tau_D`, where `tau_D=3D/(sqrt(3D^2+4)+1)`. Canonical loaded-near-unit adjacency puts each pair on the loaded hull. A two-edge outer interval would give two unit contacts whose projective direction separation exceeds `pi/3`, so each counted pair uses a distinct interval of length at least three. For `D>=4`, the admissible threshold exceeds `sqrt(2)` and tends to `sqrt(3)`. The prior `13/12` lower-witness theorem is subsumed; unary clauses and arbitrary-angle or crossing-multishear pairs remain outside. No source motion or C-II closure follows. See [the independent Audit.213](../../audits/target_c_tau_d_binary_loaded_witness_pocket_independent_audit_2026-10-09.md).
