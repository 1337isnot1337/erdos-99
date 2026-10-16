<!-- theorem-state: {"artifact_id":"ART-B2CBEF355743","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — sparse/directional split closes the proof-only full-core window

**Date:** 2026-09-12  
**Repository commit:** `c056e7e` at the start of this subrun  
**State version:** `2026-09-12.audit.44`  
**Run type:** closing proof  
**Target:** C-II, full-core branch  
**Dependencies:** canonical Sections 88--91; proof-only Sections 117--118; the
proof-only sparse/directional split in
[`target_c_sparse_directional_signed_return_split.md`](../../research/target_c_sparse_directional_signed_return_split.md)

## STATUS

`PROVED CANDIDATE AWAITING PROMOTION`

This note supplies the missing all-slack arithmetic for the sparse/directional
signed-return inequality. It eliminates the full-core Type-II branch throughout the
proof-only Section-118 window (sigmale0.0088). The inactive-container branch remains
open, so this is not a C-II or Level-I closure.

## 1. Starting necessary inequality

Use the notation of the sparse/directional split. The slack variables satisfy

\[
 x,y,z,w\ge0,
 \qquad x+y+z+w=\sigma,
 \qquad \sigma\le s_0:=0.0088.
\tag{SC.1}
\]

The proof-only return theorem gives the necessary condition

\[
 \lambda z\ge \kappa[J]_+,
 \qquad \kappa:=2-\sqrt3,
\tag{SC.2}
\]

where

\[
\begin{aligned}
J={}&A_*(x,w)
 -\lambda\left(10z+{x\over2}+{25w\over3}\right)\\
&-2\bigl(U(\theta)-x-y+2z\bigr)
 \left(Q(y)+y+x+{10w\over3}\right),
\end{aligned}
\tag{SC.3}
\]

and (Q=Q_{\rm tooth}) is determined by

\[
 \sin Q+\sqrt3(1-\cos Q)-Q={y\over2}.
\tag{SC.4}
\]

The endpoint quantities from the hostile-audited sharp Section-118 calculation are

\[
\begin{aligned}
 \theta_*&=2.70477923521549347\ldots,\\
 \lambda_*&=\sin(\theta_*/2)=0.976243913742568741\ldots,\\
 U_*&=3\theta_*-2\pi=1.831152398466894\ldots,\\
 A_*^{\min}&=0.470375286800424054\ldots.
\end{aligned}
\tag{SC.5}
\]

For (sigmale s_0), the sharp Section-118 monotonicity gives

\[
 \theta\le\theta_* ,
 \qquad \lambda\le\lambda_* ,
 \qquad U(\theta)\le U_*.
\tag{SC.6}
\]

The circular-segment function (G(t)=(t-\sin t)/8) is increasing for (t\ge0). Since

\[
 r:=x+{10w\over3}\le {10s_0\over3},
\]

the correlated area formula in the split satisfies

\[
 A_*(x,w)
 \ge {\pi\over4}-G(\theta_*)
 -2G\left(\phi_8+{10s_0\over3}\right)
 -G\left({10s_0\over3}\right)
 =A_*^{\min}>0.4703.
\tag{SC.7}
\]

The value (0.4703) is deliberately rounded down; no decimal improvement is being
used as a structural premise.

## 2. A uniform product bound for the directional term

Put

\[
 C:=U_*-x-y+2z,
 \qquad
 B:=Q(y)+y+x+{10w\over3}.
\tag{SC.8}
\]

The actual product in (SC.3) is no larger than (CB), by (SC.6), because (B\ge0).
We prove

\[
\boxed{CB<0.1473.}
\tag{SC.9}
\]

It is enough to maximize over (x+y+z+w\le s_0), since increasing (w) only increases
(B). Replace (w) by (s_0-x-y-z). Then

\[
 B=Q(y)+{10s_0\over3}-{7x\over3}-{7y\over3}-{10z\over3}.
\tag{SC.10}
\]

The endpoint equation (SC.4) has (Q(s_0)<0.072). Indeed the left side of (SC.4) at
(Q=0.072) is (0.0044253ldots>s_0/2=0.0044), and it is strictly increasing on
([0,0.072]). Therefore, throughout the simplex,

\[
 0\le B<0.072+0.0088+{10\over3}(0.0088)<0.1102,
 \qquad C\ge U_*-s_0>1.8223.
\tag{SC.11}
\]

For fixed (y,z),

\[
 {\partial(CB)\over\partial x}=-B-{7C\over3}<0.
\tag{SC.12}
\]

For fixed (x,y),

\[
 {\partial(CB)\over\partial z}=2B-{10C\over3}<0
\tag{SC.13}
\]

by (SC.11). Hence a maximizer has (x=z=0). There (w=s_0-y) and

\[
 P(y):=CB=(U_*-y)
 \left(Q(y)+{10s_0\over3}-{7y\over3}\right).
\tag{SC.14}
\]

Let

\[
 F(q)=\sin q+\sqrt3(1-\cos q)-q.
\]

For (0<yle s_0), implicit differentiation gives

\[
 Q'(y)={1\over2F'(Q(y))}.
\tag{SC.15}
\]

Since (Q(y)<0.072) and

\[
 F'(q)=\cos q+\sqrt3\sin q-1\le\sqrt3 q,
\]

we have

\[
 Q'(y)>{1\over2\sqrt3(0.072)}>4.009,
 \qquad
 {d\over dy}\left(Q(y)+{10s_0\over3}-{7y\over3}\right)>1.676.
\tag{SC.16}
\]

Together with (SC.11), this implies

\[
 P'(y)>-0.1102+1.8223(1.676)>0.
\tag{SC.17}
\]

Thus (P) is increasing and

\[
 CB\le P(s_0)
 <(1.8312-0.0088)(0.072+0.0088)
 =0.14724992<0.1473.
\]

This proves (SC.9). Notice that the product bound uses the (x,y,z,w) correlations;
the separate bounds (C\le U_*+2s_0) and (B\le0.1102) would be far too weak.

## 3. The strict endpoint contradiction

Define

\[
 \widetilde J:=J-{\lambda z\over\kappa}.
\]

Using (SC.7), (SC.9), and (lambda\le\lambda_*),

\[
\begin{aligned}
 \widetilde J
 &\ge 0.4703
 -\lambda_*\left(10z+{x\over2}+{25w\over3}+{z\over\kappa}\right)
 -2(0.1473).
\end{aligned}
\tag{SC.18}
\]

The coefficient of (z) in the parenthesis is largest, because

\[
 10+{1\over\kappa}=13.7320508\ldots>{25\over3}>{1\over2}.
\]

Using (x+y+z+w\le s_0),

\[
\begin{aligned}
 \widetilde J
 &>0.4703
 -0.9763\left(10+{1\over2-\sqrt3}\right)(0.0088)
 -0.2946\\
 &=0.0577219\ldots>0.
\end{aligned}
\tag{SC.19}
\]

Therefore (J>\lambda z/\kappa\ge0), so (SC.2) would require

\[
 \lambda z\ge\kappa J>\lambda z,
\]

which is impossible. We have proved:

> **Theorem SC — proof-only full-core elimination.** Under the canonical full-core
> Type-II carrier hypotheses and the proof-only Sections 117--118 sparse/directional
> split, no triangle-free survivor exists in the entire sharp Section-118 window
> (sigma\le0.0088).

## 4. Hostile audit and exact frontier effect

The result is an all-regime slack-simplex contradiction, not a sampled numerical
optimization. Its dependencies and limitations are explicit:

* The sparse/directional split and the sharp Section-118 return inequality are
  proof-only and must be independently promoted before this branch becomes canonical.
* The inequalities use only rounded-down/up endpoint constants with a margin exceeding
  (0.057), so the conclusion is not sensitive to the displayed decimal precision.
* The proof uses the correlated product (CB). Dropping the correlation or charging all
  sparse trains directionally would invalidate the (0.1473) bound.
* The argument is full-core only. It does not touch the macroscopic inactive-container
  branch and does not turn a protected-isolate first-contact motion into a strict
  diameter decrease.
* All source points remain part of the underlying minimizer. The proof counts/charges
  the carrier; it never deletes contact-isolated points and never extends the ZR/ZF
  affine-kernel theorem to them.

Thus this theorem removes one of the two surviving C-II branches, but C-II remains
open until the inactive-container branch is closed by an exact triangle, a strict
same-cardinality sub-(D) competitor, or another global-minimality contradiction.

The companion verifier checks the scalar inequalities and the product monotonicity
certificate. It does not certify the inherited geometric return theorem or the
inactive branch.
