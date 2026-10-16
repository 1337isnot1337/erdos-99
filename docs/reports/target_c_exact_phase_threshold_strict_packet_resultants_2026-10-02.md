<!-- theorem-state: {"artifact_id":"ART-074CF0B1E689","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II -- strict threshold packet resultants and one-peak KKT cuts

Date: 2026-10-02
Base main: `fbeae9b3fa18a63e07573676b4e2e512a91ca4d5`
Status: proof-only strengthening of the threshold exact-phase branch; C-II remains open.

Dependencies:
- `docs/reports/target_c_exact_phase_threshold_paired_staircase_2026-10-01.md`
- `docs/reports/target_c_exact_phase_threshold_transverse_rail_saturation_2026-10-01.md`
- `research/target_c_interval_shear_kkt_curvature_identity_2026-09-15.md`
- `docs/reports/target_c_positive_prefix_thrackle_collapse_2026-09-01.md`

## Setup

Let \(\tau_1,\ldots,\tau_m\) be a retained threshold exact-phase shore, with all
coherently oriented train vectors equal to \(u\). Let \(h_0=za\) be the unique
actual diameter parallel to \(u\), oriented from layer \(0\) to layer \(m\), so its
vector is \(Du\).

Let \(T\) be the paired-staircase simple gap tree on \(0,\ldots,m\). For
\(e=\{a,b\}\in E(T)\), \(a<b\), let \(H_e\) be all transversely active actual
diameters with support \((a,b]\). Orient each \(h\in H_e\) from lower to higher
layer and write
\[
r_h=p_{y_h}-p_{x_h},\qquad
c_h=r_h\cdot Ju,\qquad
d_h=r_h\cdot u.
\]
Fix a relative-interior normalized KKT stress, so every actual-diameter multiplier
\(\beta_h\) is positive.

## Theorem

For every simple staircase edge \(e\),
\[
\boxed{\sum_{h\in H_e}\beta_h r_h=R_eu\quad\text{with }R_e>0.}
\tag{1}
\]

If
\[
A_i:=\sum_{q\in E(\tau_i)}\alpha_q
\]
is the total positive contact stress crossing train \(\tau_i\), and
\(\beta_0:=\beta_{h_0}\), then
\[
\boxed{
A_i=\beta_0D+\sum_{\substack{e=\{a,b\}\in E(T)\\a<i\le b}}R_e.
}
\tag{2}
\]

If \(r\) is the common retained train crossed by every staircase interval, then
\[
\boxed{A_1<\cdots<A_r>\cdots>A_m,}
\tag{3}
\]
with an empty side omitted when \(r=1\) or \(r=m\). More precisely,
\[
A_{j+1}-A_j
=
\sum_{e:\,a_e=j}R_e>0
\qquad(j<r),
\tag{4}
\]
and
\[
A_j-A_{j+1}
=
\sum_{e:\,b_e=j}R_e>0
\qquad(j\ge r).
\tag{5}
\]

Thus the exact-phase axial strip reactions
\[
G_j=(A_j-A_{j+1})u
\]
have one sign before the common cut and the opposite sign after it. The threshold
staircase has one strict KKT load peak.

## 1. Edgewise transverse balance

The paired-staircase theorem gives the positive directed circulation
\[
\sum_h\beta_hc_h(e_{a_h}-e_{b_h})=0.
\]
Delete one simple edge \(e\) from the collapsed tree \(T\) and sum node balance on
one component. Only actual edges in \(H_e\) cross that tree cut. Therefore
\[
\sum_{\substack{h\in H_e\\c_h>0}}\beta_hc_h
=
\sum_{\substack{h\in H_e\\c_h<0}}\beta_h(-c_h)
=:W_e>0.
\tag{6}
\]
Hence the packet resultant has zero transverse component.

## 2. Every packet has strictly positive longitudinal resultant

Split the convex-hull boundary at \(z,a\) into arcs \(L,U\), both ordered from
\(z\) to \(a\). Since \(za\) is a diameter parallel to \(u\), the projection
\(s(x)=p_x\cdot u\) is nondecreasing on each arc.

For one packet \(e=\{a,b\}\), a positive-transverse diameter has physical form
\(L_aU_b\), while a negative-transverse diameter has form \(U_aL_b\). Thus for
arbitrary \(p\in H_e^+\) and \(n\in H_e^-\),
\[
d_p+d_n
=
[s(U_b)-s(U_a)]+[s(L_b)-s(L_a)]
\ge0.
\tag{7}
\]

Put
\[
q_h:=|c_h|=\sqrt{D^2-d_h^2},\qquad
\phi(t):=\frac{t}{\sqrt{D^2-t^2}},\qquad
f_h:=\beta_hq_h.
\]
The function \(\phi\) is odd and strictly increasing. Equation (6) says that the
total \(f\)-mass on \(H_e^+\) and \(H_e^-\) is the same number \(W_e\). Therefore
the longitudinal packet resultant is
\[
R_e
=
\frac1{W_e}
\sum_{\substack{p\in H_e^+\\n\in H_e^-}}
f_pf_n\,[\phi(d_p)+\phi(d_n)]
\ge0.
\tag{8}
\]

Equality is impossible. If \(R_e=0\), every bracket in (8) must vanish. Hence all
positive-orientation vectors equal one vector \(v\) of length \(D\), and all
negative-orientation vectors equal \(-v\). The packet contains both orientations,
so this gives two distinct actual diameter segments with the same projective
direction.

A diameter-\(D\) set has at most one diameter segment in any projective direction.
Indeed, if
\[
y-x=Dw,\qquad y'-x'=Dw
\]
for a unit vector \(w\), then both pairs attain the full width in direction \(w\),
so \(x'-x\perp w\). Since all pair distances are at most \(D\),
\[
D^2\ge|y'-x|^2
=|Dw+(x'-x)|^2
=D^2+|x'-x|^2,
\]
forcing \(x'=x\) and \(y'=y\). Reversing one pair handles the antiparallel case.
Thus \(R_e>0\), proving (1).

## 3. Exact cut decomposition

The audited laminar cut law gives
\[
A_i u=\sum_{h:\,i\in I_h}\beta_h r_h.
\tag{9}
\]
The parallel full-support diameter contributes \(\beta_0Du\) to every cut. Any other
diameter crossing the shore has nonzero transverse component, because a second
diameter parallel to \(u\) is impossible by the same parallel-diameter uniqueness.
The remaining rows partition into the packets \(H_e\). Substituting (1) into (9)
gives (2).

Every staircase interval contains \(r\). If \(j<r\), no staircase edge can have
right endpoint \(j\), so moving from cut \(j\) to cut \(j+1\) adds exactly the packets
with left endpoint \(j\). The gap vertex \(j\) has positive degree in the spanning
tree, so the sum in (4) is nonempty. Since every \(R_e>0\), it is strictly positive.

If \(j\ge r\), the symmetric argument shows that moving from \(j\) to \(j+1\)
removes exactly the packets with right endpoint \(j\), again a nonempty set of
strictly positive resultants. This proves (3)--(5).

## Consequence for the transverse-rail fork

The previous transverse-rail theorem split the threshold branch into an
internal-heavy case and a boundary-heavy case. The present theorem adds force
direction to both sides:

- every internal staircase support type carries a strictly positive packet
  resultant along \(u\), and every row in such a packet has full support across
  the opposite retained shore;
- every boundary staircase support type also carries a strictly positive packet
  resultant, so the boundary-heavy alternative is a concentration of positive
  packet loads, not only a support-count phenomenon.

No uniform lower bound on an individual \(R_e\) follows. The remaining bottleneck is
to combine the strict one-peak decomposition (2)--(5) with the opposite-shore cut
equations. Coefficient degeneration remains possible, so the present theorem does not
close C-II.

No computation, numerical evidence, verifier execution, CI result, or unexecuted
verifier code is used.
