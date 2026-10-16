<!-- theorem-state: {"artifact_id":"ART-E7CABC15F7F7","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II -- threshold internal staircase admits a two-cut cross-shore escape

Date: 2026-10-02
Base main: fbeae9b3fa18a63e07573676b4e2e512a91ca4d5
Status: proof-only strengthening of the threshold exact-phase branch; C-II remains open.

Dependencies:
- [paired staircase](target_c_exact_phase_threshold_paired_staircase_2026-10-01.md)
- [transverse rail saturation](target_c_exact_phase_threshold_transverse_rail_saturation_2026-10-01.md)
- [exact outer-train multishear](../../research/target_c_global_outer_train_exact_multishear_2026-09-15.md)
- [source hostile audit of the exact outer-train multishear](../../research/target_c_global_outer_train_exact_multishear_hostile_audit_2026-09-15.md)
- [historical train-closure route snapshot](../archive/source-e99-main-42f0296d/docs/targets/target-c/train-closure-bracing-audited.md.source)

## Theorem

Let
\[
A=\{\tau_1,\ldots,\tau_m\},\qquad
B=\{\sigma_1,\ldots,\sigma_n\}
\]
be the two retained shores of the current fixed-star complete O--O rectangle, and
assume that \(A\) is in the threshold exact-phase branch with common oriented train
vector \(u\).

Let \(T\) be the paired-staircase simple gap tree on \(A\)-layers
\(0,\ldots,m\). Define \(\mathcal H_{\rm int}\) to be the set of all actual
diameter rows whose nonempty exact \(A\)-support is
\[
(a,b],\qquad 1\le a<b\le m-1.
\]

Then one of the following holds.

1. **Opposite shore exact phase.** All projective train directions on \(B\) are
   equal.

2. **Two-cut escape.** There are two trains \(\sigma_p,\sigma_q\in B\) and real
   coefficients \(\gamma_p,\gamma_q\) such that the exact two-coordinate
   \(B\)-multishear
   \[
   \theta_p=t\gamma_p,\qquad
   \theta_q=t\gamma_q,\qquad
   \theta_j=0\quad(j\ne p,q)
   \]
   preserves every old contact exactly, preserves unit separation for all
   sufficiently small \(t\), and satisfies
   \[
   \boxed{
   \frac{d}{dt}|r_h(t)|^2\Big|_{t=0}
   =-2|c_h|<0
   \qquad(h\in\mathcal H_{\rm int}),
   }
   \tag{1}
   \]
   where, orienting \(h\) from its lower to higher \(A\)-layer,
   \[
   c_h=r_h\cdot Ju\ne0.
   \]

Thus every diameter row whose two distinct \(A\)-endpoint layers are internal can be
made strictly shorter simultaneously by an exact contact-preserving motion using
only two opposite-shore train coordinates, unless the entire opposite shore is itself
exact phase.

Moreover, in case 2, KKT stationarity forces a strict first-order blocker outside
\(\mathcal H_{\rm int}\). For a relative-interior KKT diameter stress
\(\beta_h>0\),
\[
\boxed{
\sum_{h\notin\mathcal H_{\rm int}}
\beta_h \frac{d}{dt}|r_h(t)|^2\Big|_{0}
=
2\sum_{h\in\mathcal H_{\rm int}}\beta_h|c_h|>0.
}
\tag{2}
\]
Hence some actual diameter row \(g\notin\mathcal H_{\rm int}\) has positive first
variation. Such a blocker has either

- empty \(A\)-support, meaning its two endpoints lie in one \(A\)-layer; or
- nonempty \(A\)-support touching layer \(0\) or layer \(m\).

If the current transverse-rail fork is internal-heavy,
\[
e_{\rm int}\ge \frac m2,
\]
then
\[
|\mathcal H_{\rm int}|\ge 2e_{\rm int}\ge m
\]
because every internal staircase edge has the two actual-diameter representatives
from the paired-staircase theorem. Therefore case 2 simultaneously makes at least
\[
m\ge(c_*-o(1))D
\]
actual diameter constraints strict to first order.

Combining this with the current-main boundary-heavy alternative gives the threshold
branch the refinement
\[
\boxed{
\text{boundary-heavy staircase}
\quad\text{or}\quad
\text{opposite shore exact phase}
\quad\text{or}\quad
\begin{matrix}
\text{a two-cut exact multishear shortens a linear internal diameter family,}\\
\text{and every positive first-order obstruction is \(A\)-boundary/layer-local.}
\end{matrix}}
\tag{3}
\]

## 1. Cross-shore sign rectification

Use the threshold reference diameter \(h_0=za\parallel u\) and the hull arcs
\(L,U\) from the paired-staircase theorem. Orient an arbitrary
\(h\in\mathcal H_{\rm int}\) from its lower \(A\)-layer \(a\) to its higher
\(A\)-layer \(b\), and write its vector as \(r_h\).

The paired-staircase sign theorem gives exactly two possibilities:
\[
c_h>0:\quad h=L_aU_b,
\qquad
c_h<0:\quad h=U_aL_b.
\tag{4}
\]

Because \(a,b\) are both internal, the transverse-rail theorem puts every
\(L\)-endpoint in \(B\)-layer \(0\) and every \(U\)-endpoint in \(B\)-layer \(n\).
Thus \(h\) has full support on all of \(B\).

Now orient the same physical diameter from \(B\)-layer \(0\) to \(B\)-layer \(n\),
and call that vector \(\widehat r_h\). Equation (4) gives
\[
\widehat r_h=
\begin{cases}
r_h,&c_h>0,\\
-r_h,&c_h<0.
\end{cases}
\]
Therefore
\[
\boxed{
\widehat r_h\cdot Ju=|c_h|>0.
}
\tag{5}
\]

Thus the two opposite transverse signs seen from the exact \(A\)-shore become one
common strict sign when the same bars are oriented across the full \(B\)-shore.

## 2. Two opposite-shore coordinates realize \(-Ju\)

Orient each \(B\)-train contact vector \(v_j\) according to the nested \(B\)-layer
shore convention of the exact multishear.

If \(B\) is not exact projective phase, choose \(p,q\) with
\[
[v_p]\ne[v_q].
\]
Then \(Jv_p,Jv_q\) are linearly independent and form a basis of \(\mathbb R^2\).
Hence there are unique real numbers \(\gamma_p,\gamma_q\) satisfying
\[
\boxed{
\gamma_pJv_p+\gamma_qJv_q=-Ju.
}
\tag{6}
\]

Apply the audited exact arbitrary-O--O multishear using only these two train
coordinates:
\[
\theta_p=t\gamma_p,\qquad
\theta_q=t\gamma_q.
\tag{7}
\]
Every old contact remains exactly unit for every \(t\) in the finite placement
formula, and all strict old noncontacts remain longer than one for sufficiently
small \(|t|\).

For \(h\in\mathcal H_{\rm int}\), full \(B\)-support means both selected cuts
separate its endpoints with the same sign when \(h\) is oriented from \(B\)-layer
\(0\) to \(n\). The exact multishear first variation of its relative vector is
therefore
\[
\widehat r_h'(0)
=
\gamma_pJv_p+\gamma_qJv_q
=
-Ju.
\tag{8}
\]
Consequently,
\[
\frac{d}{dt}|\widehat r_h(t)|^2\Big|_0
=
2\widehat r_h\cdot(-Ju)
=
-2|c_h|<0,
\]
proving (1).

The family \(\mathcal H_{\rm int}\) is finite, so for sufficiently small positive
\(t\), every member becomes strictly shorter than \(D\).

## 3. KKT transfers the obstruction to the boundary

For any exact contact-preserving multishear tangent, relative-interior KKT
stationarity gives
\[
\sum_{h\in H}\beta_h
\frac{d}{dt}|r_h(t)|^2\Big|_0=0.
\tag{9}
\]

Split the sum into \(\mathcal H_{\rm int}\) and its complement and use (1):
\[
\sum_{h\notin\mathcal H_{\rm int}}
\beta_h L_h'(0)
=
-\sum_{h\in\mathcal H_{\rm int}}\beta_hL_h'(0)
=
2\sum_{h\in\mathcal H_{\rm int}}\beta_h|c_h|.
\]
If \(\mathcal H_{\rm int}\ne\varnothing\), the right side is strictly positive
because every \(\beta_h>0\) and every \(|c_h|>0\). This proves (2) and forces a row
outside \(\mathcal H_{\rm int}\) with positive first variation.

If an actual diameter has two distinct internal \(A\)-endpoint layers
\(1\le a<b\le m-1\), then it cannot be parallel to \(u\): projective
diameter-direction uniqueness says the only actual diameter parallel to \(u\) is the
threshold reference edge \(h_0\), whose \(A\)-support is full. Hence its transverse
coefficient is nonzero and it belongs to \(\mathcal H_{\rm int}\).

Therefore a positive blocker outside \(\mathcal H_{\rm int}\) must either have equal
\(A\)-endpoint layers, hence empty \(A\)-support, or have a nonempty support interval
with at least one endpoint layer equal to \(0\) or \(m\).

## 4. Linear consequence in the internal-heavy staircase

Let \(e_{\rm int}\) be the number of simple staircase edges
\(\{a,b\}\) with \(1\le a<b\le m-1\).

Every such simple edge has at least the two opposite hull-arc representatives proved
by the paired-staircase theorem, and representatives over distinct simple support
types are distinct actual diameter rows. Hence
\[
|\mathcal H_{\rm int}|\ge2e_{\rm int}.
\tag{10}
\]

If \(e_{\rm int}\ge m/2\), equations (1) and (10) show that the two-cut escape
strictly shortens at least \(m\) actual diameter rows simultaneously. Current main has
\[
m\ge(c_*-o(1))D.
\tag{11}
\]

If instead \(e_{\rm int}<m/2\), the current transverse-rail theorem already gives the
boundary-heavy branch: one extreme \(A\)-layer is incident to more than \(m/4\)
staircase edges and contains \(\Omega(D^{1/4})\) distinct selected diameter carriers.

This proves the trichotomy (3).

## Remaining bottleneck

The internal full-support diameter family is not, by itself, a first-order pinning
mechanism once the opposite shore has two projectively distinct train directions.
Two opposite-shore coordinates can make that entire linear family strict at once.

The obstruction is now pushed to one of two places:

1. the opposite shore is itself exact phase; or
2. some positive first-order blocker is \(A\)-boundary/layer-local.

The next target is to combine this blocker localization with the four-host corner
order and the joint switch budget. A useful closing statement would show that repeated
two-cut escapes force too many distinct boundary-local blockers, or that the
double-exact-phase alternative produces incompatible paired staircases on the two
shores.

No computation, numerical evidence, verifier execution, CI result, or unexecuted
verifier code is used.

## Recovery provenance — Slot 1, 2026-10-05

Copied to fresh `main` from `research/threshold-cross-shore-two-cut-escape-clean-2026-10-02` at exact tip `32fc39b332409a8b207a86ddcd639194dde14a75`. This report remains an unreviewed, proof-only candidate; no theorem status or Target C route state is promoted. Its listed staircase, transverse-rail, and exact-multishear dependencies are present on the salvage base. The source artifact contains no verifier or computational certificate.
