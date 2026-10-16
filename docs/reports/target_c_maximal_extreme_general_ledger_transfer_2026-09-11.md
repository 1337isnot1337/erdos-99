<!-- theorem-state: {"artifact_id":"ART-0E6BE01F1F1B","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_maximal_extreme_general_ledger_transfer_2026-09-11.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=20f59747b9c0d91a80603233b52f335d3fb13482; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — general maximal-extreme ledger transfer and the forest obstruction

**Date:** 2026-09-11  
**Status:** unpromoted research report  
**Target:** Target C, C-II

## Result

Let \(x^*\) be a maximal extreme KKT circuit, so

\[
e_*+h_*=2v_*-2,\qquad d_*:=q_*-h_*\ge0.
\]

Put
\[
L_*:=e_{BB,*}+2s_{C,*},\qquad L:=e_{BB}+2s_C,\qquad
s_{B,*}:=3q_*-e_{BI,*}-2e_{BB,*}.
\]

The selected and full exact ledgers imply

\[
\boxed{L\ge L_*-\frac23s_{B,*}-2d_*+2d_H+2s_Z.}
\tag{1}
\]

Equivalently,

\[
L\ge
\left(L_*-3d_*-\frac23s_{B,*}\right)+d_*+2d_H+2s_Z.
\tag{2}
\]

For \(d_*=0\), this is the cyclic transfer proved in the companion audit. For a
selected forest, (2) identifies the exact missing input: a forest theorem must
lower-bound \(L_*-3d_*-\frac23s_{B,*}\), not merely \(L_*-3d_*\).

## 1. Exact transfer proof

Let
\[
g=q-q_*\ge0,\quad B_0=e_{BB}-e_{BB,*}\ge0,\quad
M_0=e_{BI}-e_{BI,*}\ge0.
\tag{3}
\]

Every full unpinned component containing no selected unpinned component has at
least three contacts to the full loaded set. Those contacts have omitted unpinned
endpoints, so they are counted by \(M_0\). Hence

\[
2(c_I-c_{I,*})\le\frac23M_0.
\tag{4}
\]

The selected maximal-circuit and full post-ZF ledgers are

\[
c_{I,*}+e_{BB,*}+s_{C,*}=q_*-2+d_*,
\tag{5}
\]
\[
c_I+e_{BB}+s_C=q-2+d_H+s_Z.
\tag{6}
\]

Rewriting each ledger in terms of \(L\) and subtracting gives

\[
L_*-L
=B_0-2g+2(c_I-c_{I,*})+2d_*-2d_H-2s_Z.
\tag{7}
\]

The loaded-degree slack identities give

\[
M_0+2B_0=3g+s_{B,*}-s_B.
\tag{8}
\]

Since
\[
B_0+\frac23M_0\le\frac23(M_0+2B_0),
\]
equations (4) and (8) imply
\[
2(c_I-c_{I,*})+B_0\le2g+\frac23s_{B,*}.
\tag{9}
\]
Substitution into (7) cancels \(g\) and yields (1).

No bound on \(v-v_*\), on the number of omitted contact rows, or on the number of
contact-isolated source points is used.

## 2. Attempted forest closure and exact failure

The selected \(s_Z=0\) forest cavity argument gives, at report level, a bound of
the form
\[
\frac{L_*-3d_*}{D}\ge\lambda_R+\varepsilon_R,
\qquad \lambda_R\approx0.59214.
\tag{10}
\]
The explicit version replaces the right side by \(0.597+\varepsilon\).
Substitution into (2) is not a closure because of the retained negative term
\(-2s_{B,*}/3\).

The needed replacement is
\[
\frac{L_*-3d_*-(2/3)s_{B,*}}D\ge\lambda_R+\varepsilon.
\tag{11}
\]
The existing scalar forest inequalities do not prove (11). Writing
\[
\nu=\frac{L_*-3d_*}{D},\qquad u=\frac{s_{B,*}}D,\qquad \eta=\nu-u,
\]
the attachment-cell estimate controls \(\eta\), while the outer/exceptional cavity
estimate controls \(\nu\). Their relaxed feasibility inequality has the form
\[
A_*(y,p)\le
\frac\pi4(\nu-u)^2+
\frac{(\nu+m(y,p))^2}{4\pi},
\qquad m(y,p)=\min\{y,p-y\}.
\tag{12}
\]
The desired quantity is \(\nu-\frac23u\). Inequality (12) does not bound it below:
increasing \(u\) decreases the attachment radius but leaves enough cavity capacity
through the larger allowed \(\nu\). This is an accounting compatibility check, not a
geometric construction.

Thus a valid forest closure must use extra caterpillar/hub structure or a
support-to-motion theorem for the loaded-degree-defect rows. Dropping \(s_{B,*}\)
would assert precisely the unproved implication isolated here.

## 3. Remaining branches

The general transfer closes the selected-to-full bookkeeping problem for maximal
circuits. The substantive gates remain:

1. prove the retained forest bound (11), with exceptional faces and isolates;
2. exclude the maximal cyclic high-surplus full phase;
3. handle the case where every extreme circuit is underbraced
   (\(\sigma_*>0\)).

This report is a theorem-level branch reduction, not a Level-I settlement.
