> Generated reading edition · [exact source](../../../docs/audits/target_c_fullcore_hull_train_depletion_floor_independent_audit_2026-10-04.md) · source SHA-256 `2df8a76474e1ca80746fe86d42ec72dfb29bbee91064c197342a801dd795627e`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-11408206976A","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Independent audit of PR #667: full-core hull-train depletion

**Date:** 2026-10-04
**Audited PR:** #667, branch `research/sol/c2-high-t-capacity-audit-20261004`, audited head `fdc40cc7844aaa8b5f949f59a8c1607edf43d65a`
**Current-main audit base:** `596445ac32ffd45e2cbb8df9dbeba15be3465cf5`
**State authority:** `2026-09-14.audit.51`
**Verdict:** **PASS at proof-only scope.**
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This is an independent audit of the mathematical core of PR #667. The original
branch had diverged from current main, so its two proof reports and verifier are
preserved on a fresh current-main branch rather than force-rebasing the draft. No
theorem-state promotion is made.

Put
$$
\Delta_2=\frac{\pi}{2\sqrt3},\qquad
s=\sqrt{\Delta_2},\qquad
\mu_{\rm hull}=\frac{\pi+s}{2}.
$$
The following claims pass the audit for every unbounded canonical full-core Type-II
sequence:
$$
\liminf\left(5t_D+\frac{x_B+m_B}{D}\right)\ge3\pi+2s,
\tag{A.1}
$$
$$
\liminf\left(4\mu_D-\frac{k+3m_B}{D}\right)\ge2\pi+2s,
\tag{A.2}
$$
and
$$
\boxed{\liminf\mu_D\ge\mu_{\rm hull}
=2.046952730226875\ldots.}
\tag{A.3}
$$
No canonical full-core Type-II sequence converges to $\mu_{\rm hull}$. Thus
(A.3) plus the endpoint exclusion gives a qualitative non-explicit uniform positive
gap above $\mu_{\rm hull}$ for sufficiently large full-core sources.

This does not close higher-surplus Type II, Type I/macroscopic containers, C-II, or
Level I.

## 1. Finite hull-occurrence audit

For consecutive loaded force-hull vertices $b_i,b_{i+1}$, let $W_i$ be the
outer-walk interval between their distinguished exterior occurrences and let
$\ell_i$ be its occurrence length. The new lemma
$$
\boxed{\ell_i=1\iff |b_i-b_{i+1}|=1}
\tag{A.4}
$$
is valid, including articulation and bridge cases.

If the hull side has length one, it is an actual unit contact. All positive-core
vertices lie in the loaded force hull, while unloaded core vertices are harmonic
convex combinations of their loaded attachments. Hence all other incident contact
rays lie in the inward tangent cone. Unit separation forbids a third source point in
the relative interior of the unit hull segment. The oriented occurrence adjacent to
the exterior half-plane therefore joins exactly the two distinguished exterior
occurrences.

A bridge can create another occurrence of the same physical edge on the outer facial
walk, but that occurrence belongs to the inward excursion. It does not create a
second distinguished hull interval.

For a nonunit hull side the unit-contact route has integer length at least two. If
$m_B$ is the number of nonunit loaded-hull sides, the bad intervals are exactly
those $m_B$ intervals and
$$
\boxed{
B_{\rm bad}=\sum_{\ell_i>1}\ell_i=x_B+m_B.
}
\tag{A.5}
$$
This is the load-bearing improvement over the older $B_{\rm bad}\le2x_B$.

**Verdict:** pass.

## 2. Finite train capacity and exact source identity

Canonical Section 61 gives the exact stopped-train count
$$
T=\frac{b+Q}{2}+2f.
\tag{A.6}
$$
The train crossing graph is simple and triangle-free, and at most two trains have
two good hull ends. Every other train uses a bad outer incidence or an
exceptional-face incidence. Their capacities are $x_B+m_B$ and $4f+Q$, so
$$
T-2\le x_B+m_B+4f+Q.
\tag{A.7}
$$
Using $b=q+x_B$, $b+Q=2(q-k)=2t_DD$, and $f\le Q$ gives
$$
\boxed{5t_DD+x_B+m_B\ge3P_F-2.}
\tag{A.8}
$$

In the full-core loaded-chord branch,
$$
\mu_DD=t_DD+m_B-2c_I-4.
\tag{A.9}
$$
Let $G_D$ be the trains having at least one good hull end, let $d_D\le2$
count trains having two good hull ends, and let $M_D=T-|G_D|$. Since there
are exactly $q-m_B$ good terminal incidences,
$$
|G_D|=q-m_B-d_D.
\tag{A.10}
$$
Direct substitution gives the exact finite identity
$$
\boxed{
4\mu_DD+8c_I+18-2b-M_D-k-3m_B
=2(Q-f)+2-d_D\ge0.
}
\tag{A.11}
$$
No asymptotics enter (A.11).

**Verdict:** pass.

## 3. Independent finite verification

The PR verifier was fetched at the audited head and rerun without modification in an
isolated Python 3.12 environment. It passed:

```text
PASS: {'sources': 383, 'repeated_walks': 354, 'loaded_repeated': 225}
Certified 3pi/5 interval: 1.8849555921538759 1.8849555921538759
Certified x/D lower bound at t<=1.860: 0.06238898038468986
Certified new full-core floor interval: 2.046952730226875 2.046952730226875
PASS: square sharpness, repeated loaded occurrences, exact capacity/slack
PASS: positive pentagon window lies below the excluded low-excess threshold
PASS: linear-excess scalar witness allows S=I5=0; no source realization claimed
PASS: exact depletion/slack ledgers: 183212
```

The verifier checks finite packets and algebra only; it is not evidence for global
optimality or the sequence-level depletion theorem.

**Verdict:** pass.

## 4. Directional hull-side count

In Type II, translate so that
$$
B(0,r_D)\subset F_D\subset B(0,R_D),
\qquad r_D/D,R_D/D\to1/2,
$$
and put $\alpha_D=\arccos(r_D/R_D)\to0$. For hull sides whose outward
normal lies in an oriented interval of width $w$, radial parametrization gives a
total side-length bound
$$
\frac{R_D}{\cos\alpha_D}(w+2\alpha_D).
\tag{A.12}
$$
Since every unit hull side has length one, this also bounds their count. A reduced
phase bin of width $\varepsilon<\pi/6$ produces six oriented normal intervals,
hence
$$
N_{\rm hull}(\varepsilon)
\le(3\varepsilon+o_\varepsilon(1))D.
\tag{A.13}
$$
The estimate is uniform in the bin position and uses no curvature lower bound or
disk-convergence rate.

**Verdict:** pass.

## 5. Phase depletion and order of limits

Fix $\varepsilon>0$ first. Canonical phase coarea deletes
$O_\varepsilon(D)$ rhombus crossings and splits retained trains into phase bins.
If $g_j$ good-hull trains and $T_j$ total trains lie in bin $j$, then
(A.13) gives
$$
g_j\le(3\varepsilon+o_\varepsilon(1))D.
$$
The train graph is simple, so retained rhombi incident to the good-hull family satisfy
$$
R_G^{\rm retained}\le\sum_jg_jT_j.
$$
Canonical ledgers give $T=O(D)$. Restoring the
$O_\varepsilon(D)$ deleted crossings yields
$$
\limsup_{D\to\infty}\frac{R_G}{D^2}\le C\varepsilon
$$
for every fixed $\varepsilon>0$. Only after this limit is taken is
$\varepsilon\downarrow0$. Therefore
$$
\boxed{R_G=o(D^2).}
\tag{A.14}
$$
No unsupported diagonal $\varepsilon_D$ is used, and deleting auxiliary crossing
edges is never interpreted as deleting source constraints.

**Verdict:** pass.

## 6. Mantel after deleting good-hull trains

The induced train graph on the $M_D$ remaining actual trains contains exactly
the strict-rhombus crossings not incident to the removed train family. Hence
$$
R_{\rm bulk}=R_4-R_G=(\Delta_2-o(1))D^2.
\tag{A.15}
$$
It is still simple and triangle-free, so Mantel gives
$$
\boxed{M_D\ge(2s-o(1))D.}
\tag{A.16}
$$
Combining (A.11), $b\ge P_F$, $P_F/D\to\pi$, $c_I=o(D)$, and the
nonnegative $k,m_B$ terms proves (A.2)--(A.3).

**Verdict:** pass.

## 7. Endpoint restriction

If $\mu_D\to\mu_{\rm hull}$, equality in the preceding nonnegative chain forces
$$
\frac{M_D}{D}\to2s,\qquad
\frac{b}{D}\to\pi,\qquad
\frac{k}{D}\to0,\qquad
\frac{m_B}{D}\to0.
\tag{A.17}
$$
Together with (A.15),
$$
\frac{R_{\rm bulk}}{M_D^2}\to\frac14.
\tag{A.18}
$$

The canonical full-core endpoint proof remains valid on this restricted actual train
family. Pseudosegment geometry, simplicity, triangle-freeness, train labels and phase
potentials are hereditary. The global $O(D)$ phase cut and angular-defect budget
remain valid after restriction. Mantel stability, the audited unequal-shore
Fox--Pach--Suk extraction, orientation cleanup, phase-tail trim, and canonical
Section 76 therefore apply unchanged.

The resulting shores satisfy
$$
a_D+b_D\ge\frac34M_D-o(D),
$$
so Section 76 gives
$$
D\ge\frac{\sqrt3}{2}(a_D+b_D)-O(1)
\ge\frac{3\sqrt3}{4}sD-o(D).
$$
Since $\Delta_2>16/27$, the leading coefficient exceeds one. Contradiction.

No source point is removed; only auxiliary train vertices are discarded from a
crossing graph.

**Verdict:** pass.

## 8. Uniform-gap quantifier

The endpoint theorem is sequence-level. If there were no uniform positive gap above
$\mu_{\rm hull}$ for sufficiently large full-core sources, choose sources with
$D_j\ge j$ and $\mu_{D_j}<\mu_{\rm hull}+1/j$. The floor squeezes this sequence
to the excluded endpoint. Thus the gap exists but remains non-explicit.

**Verdict:** pass.

## 9. Corrections and scope

- The theorem remains proof-only and noncanonical in this commit.
- The October scope $x_B=O(\sqrt D),\,t_D\le1.860+o(1)$ is asymptotically
  empty, but its finite conditional inequalities are not thereby false.
- Large $m_B$ produces near-unit **lower-constraint** pairs when hull perimeter
  excess is small. It does **not** produce the inverse-$D$ near-diameter
  **upper-constraint** pairs of PR #664. Any direct $m_B\to$#664 implication is
  rejected.
- Type I/macroscopic-container sources are outside the full-core premise.
- Higher-surplus Type II remains open.

**Disposition:** PR #667's hull-train depletion theorem and endpoint exclusion pass
independent mathematical audit at proof-only scope. Preserve the proof artifacts on
current-main ancestry and use the companion synthesis for the new closure routes.
