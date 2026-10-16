<!-- theorem-state: {"artifact_id":"ART-B0EA92837C44","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdos Problem #99 - RSJ surcharge for positive mixed defect

**Date:** 2026-09-11
**Repository state:** \`053e1e1b85643b738b4cde306838d150ea325783\`
**Run type:** closing-proof synthesis / exact asymptotic inequality
**Target:** Target C C-II
**External web search:** not used
**Computation:** decimal evaluation only; no computation is a proof dependency

## LEVEL I STATUS

\`STILL OPEN\`

This is a working artifact. It does not promote ZF/ZE/ZK/PC or RSJ.

## 1. Starting endpoint

The report-level forest and positive-\(s_Z\) branches had no tradeoff charging
positive \(s_Z\) to the same surplus currency. The exact target is an upper
tradeoff, not another scalar lower floor.

## 2. Theorem

Let

\[
S_D=e_{BB}+2s_C,\qquad
u_D=\frac{S_D-3d_H}{D},\qquad
z_D=\frac{s_Z}{D}.
\]

Assume the report-level exact identities

\[
E_{\rm out}+Q_f=e_{BB}-c_B-3d_H-2s_Z+P_F-h,
\tag{2.1}
\]

and

\[
\sum_r\operatorname{area}(\operatorname{conv}A_r)
\le \frac{\pi}{4}(6+S_D-3d_H-3s_Z)^2+O(D),
\tag{2.2}
\]

together with the FSDB/RSJ force-hull and cavity bounds. Let
\(\lambda_R=0.592140543606288\ldots\) be the RSJ threshold, and define

\[
C_*=3\pi^2+\frac83,\qquad M_*=2(\pi^2+1)+\pi,
\]
\[
c_*=\min\left\{\frac{C_*\lambda_R}{M_*},\,3(1-\lambda_R)\right\}
=0.7681271935\ldots .
\tag{2.3}
\]

Then every unbounded report-level survivor sequence satisfies

\[
\boxed{
\liminf_{D\to\infty}
\left(\frac{S_D-3d_H}{D}-c_*\frac{s_Z}{D}\right)
\ge\lambda_R.
}
\tag{2.4}
\]

Consequently,

\[
\boxed{
\frac{e_{BB}+2s_C}{D}
\ge \lambda_R+3\frac{d_H}{D}
+c_*\frac{s_Z}{D}-o(1).
}
\tag{2.5}
\]

## 3. Proof

Pass to a subsequence on which all normalized quantities converge. Write

\[
y=\lim h/D,\quad p=\lim P_F/D,\quad
z=\lim s_Z/D,\quad u=\lim(S_D-3d_H)/D,
\]

and \(m(y,p)=\min\{y,p-y\}\). The nonnegative component ledger gives
\(u-3z\ge0\). From (2.1),

\[
\limsup\frac{E_{\rm out}+Q_f}{D}\le u-2z+m(y,p).
\tag{3.1}
\]

The attachment-cell estimate, the isoperimetric cavity estimate, and FSDB/RSJ
therefore imply

\[
4\pi A_*(y,p)\le
\pi^2(u-3z)^2+(u-2z+m(y,p))^2,
\tag{3.2}
\]

where

\[
A_*(y,p)=\max\left\{
\frac{y+\sin y}{4},
\frac{\pi}{(\pi-2)^2}\left(\frac p2-1\right)^2
\right\}.
\]

Define

\[
Q_0(v;y,p)=\pi^2v^2+(v+m(y,p))^2-4\pi A_*(y,p).
\]

The RSJ two-variable minimization gives

\[
Q_0(\lambda_R;y,p)\le0
\tag{3.3}
\]

throughout the feasible domain, with equality only at the unique RSJ endpoint.

Expanding the right side of (3.2) gives

\[
Q_z(u;y,p)=Q_0(u;y,p)-zB(u,m,z),
\tag{3.4}
\]

where

\[
B(u,m,z)=6\pi^2u+4(u+m)-(9\pi^2+4)z.
\]

Since \(z\le u/3\),

\[
B(u,m,z)\ge\left(3\pi^2+\frac83\right)u=C_*u.
\tag{3.5}
\]

The necessary condition is \(Q_z(u;y,p)\ge0\). Since \(Q_0\) is increasing
in \(u\ge0\), (3.3)--(3.5) first give \(u\ge\lambda_R\).

If \(u\le1\), then \(m\le\pi/2\), so

\[
\partial_uQ_0(u;y,p)\le M_*.
\]

Using \(Q_0(\lambda_R;y,p)\le0\), (3.4)--(3.5) give

\[
M_*(u-\lambda_R)\ge Q_0(u;y,p)
\ge C_*u z\ge C_*\lambda_R z.
\]

Thus \(u-\lambda_R\ge(C_*\lambda_R/M_*)z\). If \(u\ge1\), then
\(z\le u/3\), and the second term in (2.3) gives

\[
c_*z\le c_*u/3\le u-\lambda_R.
\]

This proves \(u\ge\lambda_R+c_*z\) for every subsequential limit, which is
(2.4). Rearranging gives (2.5). \(\square\)

## 4. Exact target implication

The positive-\(s_Z\) branch is no longer free at the lower surplus frontier.
If \(S_D/D\to\lambda_R\), then \(d_H/D\to0\) and \(s_Z/D\to0\). More
generally, linear \(s_Z\) requires linear additional surplus with coefficient
\(c_*\), while each forest component costs three surplus units.

This does not close C-II because no universal upper bound on \(S_D/D\) is known.

## 5. Audit classification

| Claim | Classification | Reason |
| --- | --- | --- |
| (2.1) exact general cavity identity | conditional report-level input | derived in the general-\(s_Z\) addendum; not promoted |
| (2.2) attachment-cell bound | conditional report-level input | uses ZF/ZE/ZK/PC stack |
| RSJ minimization | report-level input | exact two-variable minimization in the RSJ report |
| surcharge (2.4) | proved conditional on listed inputs | algebra above |
| Level I settlement | not proved | no opposing surplus upper bound |

## 6. Regression tests

- Regular odd shells are not excluded; they lie at high surplus.
- The zero-transfer forest branch is handled separately.
- Contact-isolated source points remain in the full-source area input.
- No conductance lower bound is inferred from the surcharge.

## 7. Failed routes and no-go results

The inequality cannot by itself exclude \(s_Z=\Theta(D)\). It only raises the
lower surplus threshold. Closure still requires an upper tradeoff or a global
competitor.

## 8. Promotion recommendation

**Hold as report.** The theorem is conditional on unpromoted report-level identities.

## 9. Highest-value next lemma

Prove an upper tradeoff for the strict-negative-transfer phase
\[
\min_{e\ne f}K_{ef}<0,
\]
using the actual bridgeless common block and the full caterpillar forest, or prove
a source-wide capacity bound for the remaining high-surplus phase.

## 10. Compact handoff

\`\`\`text
LEVEL I STATUS: STILL OPEN.

New conditional theorem:
  u_D=(e_BB+2s_C-3d_H)/D,
  z_D=s_Z/D,
  u_D-c_* z_D >= lambda_R-o(1),
  c_*=0.7681271935... .
Hence
  (e_BB+2s_C)/D >= lambda_R+3d_H/D+c_*s_Z/D-o(1).

Remaining obstruction:
  strict-negative-transfer common-block phase and the absence of an upper bound
  on the surplus currency.
\`\`\`
