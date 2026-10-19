# Oler slack and the locked fan remainder

**Classification: unreviewed conditional remainder lemma and proof-method obstruction.**
No canonical claim or theorem state changes. Level I and Target A remain open.

## Exact question and hypotheses

Use the actual triangle-free global source (A\subset H=\operatorname{conv}A),
\(|A|=N\), diameter (D\), and the actual Section-165 plateau response
\(X^*\subset K^*=\operatorname{conv}X^*\), \(|X^*|=m^*\), diameter
\(d=D(m^*)\), with \(t=(D-d)/2>1\). Assume the Section-155 hypotheses and
the common placement \(K^*+\mathbb B\subset H\). In the actual-response locked
branch fix the canonical three-channel fan \(\Sigma\), with \(e=|E(\Sigma)|\).
For each generic lattice phase use the Section-102 admissible basis from PR #117.
All source labels, including contact isolates, remain counted in \(N\).

The specific candidate is an exact source-area remainder identity for PR #117's
phase-integrated test. The affected quantity is
\(\Xi_\Sigma-j_*-|T_Z|\). A positive remainder gives a phase with the canonical
locked-branch surplus; a nonpositive remainder only leaves this sufficient test
inconclusive.

## Exact signed remainder

Write
\[
a_0=\frac{\sqrt3}{2},\qquad L=K^*+t\mathbb B,\qquad
B_0=\mathbb E_v[d_{\rm int}(v)+t_\Sigma(v)],
\]
\[
A_\Sigma=\operatorname{area}N_1(|\Sigma|),\qquad
\Delta_H=\operatorname{area}H-\operatorname{area}L,
\]
and define the source Oler slack
\[
\Omega_H=\operatorname{area}H+\frac{a_0}{2}\operatorname{per}(H)
             -a_0(N-1)\ge0.
\]
The inequality in PR #117, equation (1), implies the exact sufficient condition
\[
\boxed{\mathcal R_{\rm exact}:=
\Omega_H-\Delta_H-\frac{a_0}{2}\operatorname{per}(H)
        +a_0B_0-A_\Sigma>0.}
\tag{A}
\]
Indeed,
\[
\mathcal R_{\rm exact}
=\operatorname{area}L+a_0B_0-a_0(N-1)-A_\Sigma.
\]
Thus (A) is exactly PR #117's integer phase threshold with the actual fan
neighborhood retained. Since \(A_\Sigma\le\pi+2e\), the candidate's stated
condition (2) is the stronger test
\[
\boxed{\Omega_H+a_0B_0>
\Delta_H+\frac{a_0}{2}\operatorname{per}(H)+\pi+2e.}
\tag{B}
\]

Section 155 gives \(d_H(H,L)\le3\eta(D)\), with
\(\eta(D)=3^{1/4}\sqrt D\). Steiner's formula therefore gives the general
two-sided estimate
\[
|\Delta_H|\le3\pi D\eta(D)+9\pi\eta(D)^2.
\]
For the sign needed in (B), Section 155's sharper common diameter-area bounds
give
\[
\Delta_H<\frac{\sqrt3\pi}{4}D,
\qquad \operatorname{per}(H)\le\pi D.
\]
Consequently a sufficient condition obtained by bounding these terms separately is
\[
\Omega_H+a_0B_0>
\frac{\sqrt3\pi}{2}D+\pi+2e.
\tag{C}
\]
This keeps both the admissible-basis count and the full fan-neighborhood charge.

## Exact limit of the separate-bound route

The same canonical global-optimum cardinality bound used in Section 155 gives
\(a_0(N-1)>\pi D^2/4\). Together with the isodiametric inequality and
\(\operatorname{per}(H)\le\pi D\), it yields
\[
0\le\Omega_H<\frac{\sqrt3\pi}{4}D.
\]
For every phase, \(d_{\rm int}\le m^*-|Z|\). The unicyclic locked fan has
\(|V(\Sigma)|=e\), so \(t_\Sigma\le e\). Averaging and applying Oler to
\(X^*\) gives
\[
B_0\le m^*-\frac{\operatorname{area}K^*}{a_0}+e
     \le\frac{\operatorname{per}(K^*)}{2}+1+e
     \le\frac{\pi d}{2}+1+e.
\]
Hence
\[
\Omega_H+a_0B_0
<\frac{\sqrt3\pi}{2}D+a_0(1+e)
<\frac{\sqrt3\pi}{2}D+\pi+2e.
\]
The last strict inequality follows from
\(\pi+2e-a_0(1+e)>0\) for every integer \(e\ge0\). Therefore the
separate-envelope sufficient test (C) can never be verified from these Oler
upper bounds. This is an obstruction to that proof method only. It does **not**
show that (A) or (B) fails for an actual source: favorable correlation among
\(\Omega_H\), the signed area gap, the basis counts, and the fan neighborhood
could still make the exact remainder positive.

## Source-realized arithmetic control

The verifier uses the finite triangular-lattice hexagonal patch
\[
A_M=\{(i,j)\in\mathbb Z^2:|i|,|j|,|i+j|\le M\},
\]
in the basis \((1,0),(1/2,\sqrt3/2)\). It checks this labeled point set,
its pairwise unit separation, \(N=3M(M+1)+1\), and its regular-hexagon hull
\(H_M\), with
\[
\operatorname{area}H_M=\frac{3\sqrt3}{2}M^2,
\qquad \operatorname{per}(H_M)=6M.
\]
As a second, separately defined source control for \(M=3,6\), retain the
points outside the color class
\((i-j)\bmod3=1\). Every unit triangle in the triangular lattice uses all
three color classes, so the retained source is triangle-free; all six hull
vertices remain because \(M\equiv0\pmod3\). At \(M=6\), the source has
\(85\) labels and exact Oler slack \(21\sqrt3\). Its inner hexagon with
\(k=3\) has diameter \(6\), so the geometric collar is \(t=3\), and
\(K_{3}+\mathbb B\subset H_6\) because the apothem gap is
\(3\sqrt3/2>1\). The exact area difference is
\[
\Delta_H=\frac{81}{2}\sqrt3-54-9\pi.
\]
This checks the source-side signs on a triangle-free finite set with a unit
collar. It is not a global minimizer, does not meet the large-cardinality
Section-155 shell hypotheses, and its inner patch is not an actual plateau
optimum. It has no locked fan or Section-102 basis and is not a counterexample
to Target A.

## Predecessors and provenance

The phase-integrated inequality and admissible-basis convention are from PR #117,
head `52a89ded959be4c96db4bdc4622ee73f7f63c3bd`. Its source README SHA-256 is
`27d223939702a6e0ce72adcdeedd173201ef4a6ae9e0a98a5a2c64b61a5b5cfb`, and its
verifier SHA-256 is
`7265f783cf0a5ebcb7c26169b50796ff7af900a39e086fa3d1560959d0a2b920`.
This contribution does not replay or independently audit that checker. It
continues PR #117's explicit next question using actual source hull terms rather
than another fixed fan. The earlier PR #87 and #89 handoffs settle only their
supplied-fan ledgers and do not provide \(N\) or the global source slack.
A related noncanonical report,
[`research/target_a_one_source_arm_per_contact_edge_2026-10-03.md`](../../research/target_a_one_source_arm_per_contact_edge_2026-10-03.md),
improves fan-crossing costs only in the simultaneous zero-slack source-matching
branch and still leaves its sector-population inequality open. It does not bound
the Oler slack or signed source-to-plateau area gap here.

Baseline: `7d0a450fe66991036541023f95c44c064a04b6a8`; theorem state
`2026-10-15.publication.2`; priority `public-frontier.3`; catalogue
`public-frontier.9`. Assignment: `a-source-area-vs-fan-debt-macbook-20261019`.
Section 155 uses the classical Bonnesen estimate recorded in Klain's
[*An Error Estimate for the Isoperimetric Deficit*](https://faculty.uml.edu/dklain/Klain-Isoperimetric.pdf).
New work is offered under Apache-2.0. OpenAI Codex
(GPT-6 Luna xhigh) derived the remainder and wrote the exact finite control.
No independent AI-agent audit has reviewed this artifact.

## Open next question

Prove a source-specific joint lower bound making (A) or (B) positive, or give a
precise source-bound term that cannot be controlled under the current hypotheses.
Either outcome affects only the actual-response locked branch through
\(\Xi_\Sigma-j_*-|T_Z|\). A proof closes that branch; failure of (B) for one
source is inconclusive and requires a direct lower bound on the sector sink
surplus. The changed hypothesis is retention of the actual \(A,H,N\) and the
actual Section-165 response, rather than using a supplied fan without source
population. The next step is to bound the joint expression
\(\Omega_H-\Delta_H-a_0\operatorname{per}(H)/2+a_0B_0-A_\Sigma\)
on a source-realized Section-165 configuration. No such configuration or
lower-bound theorem appears in the inspected predecessors. Level I, Target A,
and C-II remain open; required full certificate replay is deferred to the
merging agent.
