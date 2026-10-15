<!-- theorem-state: {"artifact_id":"ART-70983A90468E","canonical":true,"claim_ids":["C-FULL-FLOWER-K-PAYMENT"],"claim_statuses":{"C-FULL-FLOWER-K-PAYMENT":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C: full-flower blocker converts loaded-rank currency into train defects

Date: 2026-10-05

Base main: cd5fabd6f1cec3e11887bf0e2f8507a155342428

Scope: Target C-II, full-core Type-II branch only.

Status: canonical in `2026-10-05.audit.55` as `C-FULL-FLOWER-K-PAYMENT`. C-II and Level I remain open.

## 1. Result

Current-main hull depletion leaves a train graph with \(M_D\) vertices and
\(R_{\rm bulk}\) strict-rhombus crossings. Write

\[
r_4=\sqrt{R_4},\qquad r_b=\sqrt{R_{\rm bulk}},\qquad
\delta_G=r_4-r_b\ge0,
\]
\[
\eta_D=M_D-2r_b\ge0,\qquad
\sigma_R=2T_R-4r_4\ge0.
\]

Let \(S_G\) count singleton stopped trains deleted with the good
unit-loaded-hull family, \(m_B\) count nonunit loaded-hull sides,
\(k=d_H+s_Z\), and \(d_D\le2\) be the double-good-end correction.

Then every finite source in this proof stack satisfies

\[
\boxed{
k\le
2\delta_G+2+
\Psi(\sigma_R,r_4)+3\eta_D+m_B+d_D+2(Q-f)+4S_G,
}
\tag{1}
\]

where

\[
\boxed{
\Psi(\sigma,r)=
\sigma\,{3r+\sigma/2\over 2r+\sigma/2}.
}
\tag{2}
\]

For \(r>0\) and \(\sigma\ge0\),

\[
\sigma\le\Psi(\sigma,r)\le{3\over2}\sigma,
\]

so

\[
\boxed{
k\le
2\delta_G+2+{3\over2}\sigma_R+3\eta_D+m_B+d_D+2(Q-f)+4S_G.
}
\tag{3}
\]

Current-main hull depletion gives
\(R_4-R_{\rm bulk}=o(D^2)\) and
\(R_4,R_{\rm bulk}=(\Delta_2-o(1))D^2\). Hence

\[
\delta_G=
{R_4-R_{\rm bulk}\over\sqrt{R_4}+\sqrt{R_{\rm bulk}}}
=o(D).
\]

Thus every full-core Type-II sequence in this proof stack obeys

\[
\boxed{
{k\over D}\le
{3\over2}{\sigma_R\over D}
+3{\eta_D\over D}
+{m_B\over D}
+2{Q-f\over D}
+4{S_G\over D}
+o(1).
}
\tag{4}
\]

A linear \(k=d_H+s_Z\) therefore cannot be paid only by producing a linear
population of fully rhombic pentagonal holes. It must reappear as actual train slack,
depleted Mantel excess, nonunit loaded-hull sides, high-degree face excess, or
good-hull singleton edges.

In particular,

\[
\sigma_R,\eta_D,m_B,Q-f,S_G=o(D)
\quad\Longrightarrow\quad k=o(D).
\tag{5}
\]

If \(\liminf k/D\ge\kappa>0\), then the balanced consequence is

\[
\boxed{
\liminf{\max\{\sigma_R,\eta_D,m_B,Q-f,S_G\}\over D}
\ge{2\kappa\over23}.
}
\tag{6}
\]

## 2. Depleted singleton payment

Let \(S_0\) count singleton trains among the \(M_D\) depleted trains. A singleton
train is an isolated vertex of the strict-rhombus crossing graph. Removing all
\(S_0\) such vertices removes no crossing. The remaining graph has
\(M_D-S_0\) vertices, still has \(R_{\rm bulk}\) edges, and is simple and
triangle-free. Mantel gives

\[
R_{\rm bulk}\le{(M_D-S_0)^2\over4},
\]

hence

\[
\boxed{S_0\le M_D-2\sqrt{R_{\rm bulk}}=\eta_D.}
\tag{7}
\]

This is a finite auxiliary-graph deletion, not a modification of the source.

## 3. Finite lower bound for full flowers

Current main gives

\[
T=q-k+2f,\qquad |G_D|=q-m_B-d_D,
\]

so

\[
\boxed{M_D=m_B-k+2f+d_D.}
\tag{8}
\]

Let \(P_5\) be the number of bounded pentagonal contact faces. Every bounded
exceptional face that is not pentagonal has degree at least six and contributes at
least one to \(Q-f\). Therefore

\[
f-P_5\le Q-f.
\tag{9}
\]

Using \(M_D=2r_b+\eta_D\) in (8) gives

\[
\boxed{
P_5\ge
r_b+{\eta_D\over2}-{m_B\over2}+{k\over2}
-{d_D\over2}-(Q-f).
}
\tag{10}
\]

Let \(F\) denote the number of fully rhombic bounded pentagons. The exact finite
singleton/full-flower incidence inequality is

\[
P_5-F\le2S,
\tag{11}
\]

where \(S=S_G+S_0\) is the total singleton count. Combining (7), (10), and (11),

\[
\boxed{
F\ge
r_b-{3\over2}\eta_D-{m_B\over2}+{k\over2}
-{d_D\over2}-(Q-f)-2S_G.
}
\tag{12}
\]

No flower-terminal train is assumed to survive the hull depletion. Only singleton
incidence is used.

## 4. Finite projective-blocker upper bound

The hostile-audited full-flower projective blocker on current main proves

\[
{T_R\choose2}-R_4\ge{T_R(F-2)\over2}.
\tag{13}
\]

For \(R_4>0\), hence \(T_R>0\), this rearranges to

\[
\boxed{F\le T_R+1-{2R_4\over T_R}.}
\tag{14}
\]

Put

\[
a=T_R-2r_4={\sigma_R\over2}.
\]

Then \(T_R=2r_4+a\), and exact algebra gives

\[
T_R-{2r_4^2\over T_R}
=
r_4+a\,{3r_4+a\over2r_4+a}.
\]

Therefore

\[
\boxed{
F\le r_4+1+a\,{3r_4+a\over2r_4+a}
\le r_4+1+{3\over4}\sigma_R.
}
\tag{15}
\]

The blocker theorem already allows a complete train to terminate on two different
full flowers; no stronger endpoint injectivity is used here.

## 5. Eliminate the flower variable

Comparing (12) and (15) gives

\[
r_b-{3\over2}\eta_D-{m_B\over2}+{k\over2}
-{d_D\over2}-(Q-f)-2S_G
\le
r_4+1+a\,{3r_4+a\over2r_4+a}.
\]

Move \(r_b\) to the right, use \(\delta_G=r_4-r_b\), and multiply by two:

\[
k\le
2\delta_G+2+
2a\,{3r_4+a\over2r_4+a}
+3\eta_D+m_B+d_D+2(Q-f)+4S_G.
\]

Since \(2a=\sigma_R\), the nonlinear term is exactly \(\Psi\) from (2).
This proves (1). The bound \(\Psi\le3\sigma_R/2\) proves (3).

For (6), if all five quantities
\(\sigma_R,\eta_D,m_B,Q-f,S_G\) were below \(cD\), (4) would give

\[
{k\over D}\le
\left({3\over2}+3+1+2+4\right)c+o(1)
={23\over2}c+o(1).
\]

Any \(c<2\kappa/23\) contradicts \(\liminf k/D\ge\kappa\).

## 6. Hostile checks

A singleton edge may witness non-fullness of two pentagons, so the factor two in
(11) is retained. Singleton bridges may witness none; counting them only weakens
(12).

The good-hull depletion and projective blocker act on different train subsets.
No identification between them is assumed. The lower flower bound uses the global
pentagon/singleton incidence after partitioning singleton trains by depletion; the
upper bound uses the complete global strict-rhombus train graph.

The term \(\delta_G\) is retained in the finite theorem. It becomes \(o(D)\) only
after invoking the analytic current-main depletion result
\(R_4-R_{\rm bulk}=o(D^2)\).

The lower-bound mechanism through (12) overlaps the recent unmerged automation
report target_c_depleted_pentagon_flower_singleton_fork_2026-10-05.md. It is
rederived here against current main and is not a theorem premise. The new step is the
composition with the now-canonical `C-FULL-FLOWER-PROJECTIVE-BLOCKER`, eliminating \(F\) and
producing the direct \(k\)-payment inequality (1).

A repository search before this write found no existing report combining
\(\eta_D,\sigma_R,S_G\) and the projective blocker into this \(k\)-payment theorem.

No verifier, numerical search, CI output, or computational experiment is a proof
premise. Equations (7)--(15) are finite analytic/counting statements once the
current-main depletion classification is fixed. The asymptotic use of
\(R_{\rm bulk}\) uses the canonical `C-FULLCORE-HULL-DEPLETION-FLOOR` theorem.

## 7. Remaining Target C obligation

Equation (4) removes one escape: a large \(k=d_H+s_Z\) cannot be hidden inside a
linear full-flower population while all train and hull defects stay small.

The remaining full-core obligation is to spend one of

\[
\sigma_R,\qquad \eta_D,\qquad m_B,\qquad Q-f,\qquad S_G
\]

against the actual Woodall diameter topology or a source-preserving strict-diameter
competitor. The \(\eta_D\) branch already raises the hull-depletion surplus floor.
The \(m_B\) and \(Q-f\) branches feed existing loaded-hull and high-degree-face
machinery. The less-processed branches are linear strict-rhombus train-isoperimetric
slack \(\sigma_R\) and linear good-hull singleton population \(S_G\).

The macroscopic-container branch is separate. C-II and Level I remain open.

## Preservation status and provenance (2026-10-05)

Recovered from `automation/target-c-flower-blocker-k-payment-2026-10-05` at
source tip `849b955344f2e52b4508405a738417885c089f5f`. The report is based on
main `cd5fabd6f1cec3e11887bf0e2f8507a155342428`; it predates the later
Target C `audit.52` promotion. Its registered composition was independently re-audited and promoted in `2026-10-05.audit.55`. The exact coefficient/cancellation ledger is covered by `research/verify_target_c_audit55_singleton_flower_ledger_2026_10_05.py`. It does not
close C-II or Level I.
