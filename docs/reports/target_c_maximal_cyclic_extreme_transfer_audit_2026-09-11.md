<!-- theorem-state: {"artifact_id":"ART-7A880A680F81","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_maximal_cyclic_extreme_transfer_audit_2026-09-11.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=d44e3809002a6dc70c57acfb27db73d11be3d889; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — audited transfer from a maximal cyclic extreme circuit

**Date:** 2026-09-11  
**Status:** unpromoted research report; route-map status unchanged  
**Target:** Target C, C-II

## Level-I status

`STILL OPEN`.

This report isolates one branch that can now be transferred without assuming that
the selected extreme support has `o(D)` vertices omitted from the full source.  Let
`x*` be a vertex of the normalized nonnegative KKT stress polytope, and let its
positive support be `S`.  Assume its actual mixed circuit is maximal and cyclic:

\[
\sigma_*:=2v_*-2-(e_*+h_*)=0,
\qquad d_*:=q_*-h_*=0.
\]

The selected graph then obeys the cyclic circuit theorem, including its strict
endpoint gap.  If

\[
L_*:=e_{BB,*}+2s_{C,*},\qquad
L:=e_{BB}+2s_C,
\]

and `s_{B,*}` is the selected loaded-degree slack, then

\[
\boxed{\frac{L_*-(2/3)s_{B,*}}D
\ge \lambda_A+\varepsilon_A}
\tag{1}
\]

for an absolute `\varepsilon_A>0`, where

\[
\lambda_A=
\frac{\pi}{\sqrt{\pi^2+(5/4-\sqrt{\pi/(2\sqrt3)})^2}}
 =0.9955405845\ldots .
\]

The new transfer identity is

\[
\boxed{L\ge L_*-(2/3)s_{B,*}+2d_H+2s_Z.}
\tag{2}
\]

Consequently every such full-source branch satisfies

\[
\boxed{\liminf\frac{e_{BB}+2s_C}{D}
\ge \lambda_A+\varepsilon_A}
\tag{3}
\]

and in fact has the additional finite correction `2(d_H+s_Z)/D`.

This does not close the high-surplus phase: no valid global upper bound below one
is known for `L/D`, and (3) is a lower bound.  The forest maximal-circuit branch and
the underbraced singular-circuit branch remain.

## 1. Selected circuit ledgers

The extreme-support circuit theorem gives

\[
e_*+h_*=2v_*-2,
\qquad \operatorname{rank}R_S=2v_*-3.
\tag{4}
\]

The selected positive contact graph is connected, triangle-free, spans diameter
`D`, and has all selected diameter endpoints on its convex force hull.  Because the
selected diameter graph is cyclic, Woodall gives one odd unicyclic component with
pendant leaves.  The actual diameter cycle traps the entire original source in its
width-`D` Reuleaux container.  The selected contact graph therefore has the same
cyclic perimeter and stopped-train hypotheses as the promoted cyclic proof, even
though the full source may contain contact rows on which `x*` vanishes.

Pin the selected loaded vertices and write `I_*` for the selected unpinned vertices.
The pinned selected contact matrix has full column rank: a pinned contact motion
extends by zero to a motion of the selected mixed framework, and (4) leaves only
Euclidean motions; a Euclidean motion vanishing at a selected diameter pair is zero.
For each selected unpinned contact component `I_{r,*}`, its positive equilibrium
gives one nonzero pinned left-null relation.  Define `s_{C,*}` to be the sum of the
left nullities above these mandatory one-dimensional relations.  Euler and rank
then give

\[
c_{I,*}+e_{BB,*}+s_{C,*}=q_*-2,
\qquad b_*+Q_*=2h_*=2q_*.
\tag{5}
\]

The loaded-degree slack is

\[
s_{B,*}:=3q_*-e_{BI,*}-2e_{BB,*}\ge0.
\tag{6}
\]

The cyclic attachment, rhombic-train, and atomic endpoint argument applied to the
selected circuit gives (1).  Its endpoint is excluded by the same equality-case
contradiction: a macroscopic exceptional face would have asymptotically uniform
edge directions, while equality in the atomic Mantel bound and stopped-endpoint
saturation would force those directions into one three-point `\pi/3` orbit.  This
is a selected-support theorem; it does not invoke an independently optimized
scaffold or discard source points from the Reuleaux container.

## 2. Exact full/selected comparison

Let the corresponding full quantities have no star.  The selected loaded vertices
are a subset of the full loaded vertices.  Put

\[
g:=q-q_*\ge0,
\qquad B_0:=e_{BB}-e_{BB,*}\ge0,
\qquad M_0:=e_{BI}-e_{BI,*}\ge0.
\tag{7}
\]

Let `c_I,c_{I,*}` count full and selected unpinned contact components.  A full
unpinned component meeting `I_*` contains at least one selected component.  Hence
the excess `c_I-c_{I,*}` comes only from full components disjoint from `I_*`.
Each such component has at least three full contacts to the loaded set.  All those
contacts have an omitted unpinned endpoint and are absent from the selected support,
so they are counted by `M_0`.  Therefore

\[
2(c_I-c_{I,*})\le \frac23M_0.
\tag{8}
\]

The full and selected versions of the exact pinned ledger are

\[
c_I+e_{BB}+s_C=q-2+d_H+s_Z,
\qquad
c_{I,*}+e_{BB,*}+s_{C,*}=q_*-2.
\tag{9}
\]

Writing `L=e_{BB}+2s_C` and `L_*=e_{BB,*}+2s_{C,*}`, subtracting (9) gives

\[
L_*-L
=B_0-2g+2(c_I-c_{I,*})-2d_H-2s_Z.
\tag{10}
\]

Finally subtract the two loaded-degree slack identities:

\[
s_B=3q-e_{BI}-2e_{BB},
\qquad
s_{B,*}=3q_*-e_{BI,*}-2e_{BB,*}.
\]

This yields the exact relation

\[
M_0+2B_0=3g+s_{B,*}-s_B.
\tag{11}
\]

Since

\[
B_0+\frac23M_0\le \frac23(M_0+2B_0),
\]

we obtain

\[
B_0+\frac23M_0\le2g+\frac23s_{B,*}.
\tag{12}
\]

Insert (8) and (12) into (10); the unknown number `g` of omitted loaded terminals
cancels:

\[
L_*-L
\le \frac23s_{B,*}-2d_H-2s_Z.
\]

This is (2).  In particular, no estimate of `v-v_*`, `c_I`, or the number of
omitted contact rows is used.

## 3. Branch consequence and exact unresolved obstruction

Combining (1) and (2) gives

\[
\frac LD\ge
\lambda_A+\varepsilon_A
 +2\frac{d_H+s_Z}{D}.
\tag{13}
\]

Thus a maximal cyclic extreme circuit cannot be hidden inside a larger full C-II
source to evade the cyclic atomic floor.  The transfer remains valid when the full
stress has `s_Z>0`, and it retains all contact-isolated source points because the
comparison is only between contact-core ledgers; the selected cyclic Reuleaux proof
counts the entire original source in its capwise Oler step.

There is still no contradiction.  The exact next statement needed for this branch
is an independent upper tradeoff such as

\[
L/D<1-o(1)
\]

under the full-source near-perimeter and population constraints, or a strict
sub-`D` competitor.  The currently proved full-source Oler-slack theorem only gives
`E=O(D)` and does not provide that upper tradeoff.  A lower bound crossing one would
also not settle the problem, because `L` is not known to be bounded above by `D`.

The remaining branch ledger is therefore:

| branch | new reduction | exact live obstruction |
|---|---|---|
| maximal cyclic extreme | (13) | high-surplus full source; no upper tradeoff |
| maximal forest extreme | not transferred | need forest selected-circuit theorem and full comparison |
| every extreme underbraced (`\sigma_*>0`) | selected supports are singular actual circuits | no support-to-motion or population contradiction |

Regular odd shells remain a binding regression for any attempted high-surplus
upper bound: their local PSD/affine-kernel properties do not certify global
minimum-diameter optimality, but they do satisfy the accounting equalities that a
purely local upper-bound argument would use.

## 4. Classification

The selected cyclic floor and the exact transfer are proved from the selected
maximal-circuit infrastructure and the C-II loaded-degree/ledger identities.  The
cyclic endpoint gap is qualitative, so `\varepsilon_A` is nonexplicit.  No route-map
promotion is made here; the report depends on unpromoted selected-circuit reports.
