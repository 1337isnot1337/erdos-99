<!-- theorem-state: {"artifact_id":"ART-3277611F6658","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-a"} -->
# The zero-slack source controls only the unit collar in the Oler remainder

**Status: unreviewed conditional corollary and method limitation.** No canonical
claim or theorem state changes. This report treats only the zero-slack branch of
Section 168. It does not provide a counterexample to an actual plateau source.

## Question and hypotheses

Investigation: `a-correlated-source-remainder-paired-20261019`; refined scope
key `be528cc487f25af31ea26703`. Baseline:
`7d0a450fe66991036541023f95c44c064a04b6a8`; theorem state
`2026-10-15.publication.2`; priority `public-frontier.3`; catalogue
`public-frontier.9`.

Assume the zero-slack branch of Theorem 168.1. Write
\[
A^0\subset H,\qquad |A^0|=M=\alpha_1(H),\qquad D(M)=D,
\]
where \(A^0\) is the triangle-free global optimum supplied by that branch.
Retain the actual right-endpoint plateau response \(X^*\), its hull \(K^*\),
and the Section-165 placement \(K^*+\mathbb B\subset H\). In the Section-175
locked branch, retain its actual fan \(\Sigma\), its Section-102 admissible
bases, and all source labels of \(A^0\), including contact isolates.
Section 168 gives \(D(M)=D\); thus the phase-integrated condition can be
reinstantiated for this source in the same hull with source cardinality
\(N=M\), retaining the plateau response and replacing \(j_*\) accordingly.
For \(B_0\), use the finite Borel joint basis/matching selector described in
the conditional audit PR #141; the PR #117 phase implication remains subject
to that convention.

Put \(a_0=\sqrt3/2\), \(L_\rho=K^*+\rho\mathbb B\), and
\(t=(D-\operatorname{diam}K^*)/2>1\). Let \(B_0\) and \(A_\Sigma\) be the
phase-averaged basis charge and fan-neighborhood area from PR #138, using source
cardinality \(M\) in \(j_*\). The exact remainder for this source is
\[
R^0_{\rm exact}
=\operatorname{area}(L_t)-a_0(M-1)+a_0B_0-A_\Sigma.
\tag{1}
\]
This changes the source cardinality from the original \(N\) to \(M\), as
required by the Section-168 zero-slack normalization; it makes no identification
between \(A^0\) and the original source.

## A source-specific area bound

For a generic lattice phase \(v\), set
\[
Y_1(v)=(\Lambda+v)\cap\operatorname{int}L_1.
\]
This is the Section-168 set \(Y_{\rm in}(v)\). It is unit-separated as a
subset of the triangular lattice and lies in \(H\) because \(L_1\subset H\).
Thus the zero-slack equality \(M=\alpha_1(H)\) gives
\[
|Y_1(v)|\le M
\quad\hbox{for every generic phase }v.
\tag{2}
\]
This is also the cardinality consequence of Section 168.2's matching into
\(A^0\), but the count uses only maximum capacity and combines no selected
source images.

The fundamental cell of \(\Lambda\) has area \(a_0\). Integrating its
periodization gives the exact lattice average
\[
\mathbb E_v|Y_1(v)|
=\frac{1}{a_0}\int_F\sum_{\lambda\in\Lambda}
  \mathbf1_{\operatorname{int}L_1}(\lambda+v)\,dv
=\frac{\operatorname{area}(L_1)}{a_0}.
\]
The boundary of the convex body \(L_1\) has area zero. Equations (2) and this
identity imply
\[
\boxed{\operatorname{area}(L_1)\le a_0M.}
\tag{3}
\]

Since \(K^*\) is a convex body in the sufficiently-large regime, Steiner's
parallel-area formula gives
\[
\operatorname{area}(L_t)-\operatorname{area}(L_1)
=(t-1)\operatorname{per}(K^*)+\pi(t^2-1).
\tag{4}
\]
Combining (1), (3), and (4) yields the source-specific **upper** bound
\[
\boxed{
R^0_{\rm exact}
\le a_0+(t-1)\operatorname{per}(K^*)+\pi(t^2-1)
       +a_0B_0-A_\Sigma.
}
\tag{5}
\]
Equivalently, the area-population term in (1) obeys
\[
\operatorname{area}(L_t)-a_0(M-1)
\le a_0+(t-1)\operatorname{per}(K^*)+\pi(t^2-1).
\]
More precisely, define the nonnegative unit-collar deficit
\[
\sigma_1=a_0M-\operatorname{area}(L_1)\ge0.
\]
Let \(\Delta_{H,1}=\operatorname{area}(H)-\operatorname{area}(L_1)\ge0\).
The definitions of the source Oler slack and this deficit give the exact
correlation
\[
\sigma_1=a_0+\Delta_{H,1}
       +\frac{a_0}{2}\operatorname{per}(H)-\Omega_H.
\tag{6}
\]
The signed gap at radius \(t\) satisfies
\(\Delta_H=\Delta_{H,1}-(t-1)\operatorname{per}(K^*)-\pi(t^2-1)\).
Substituting these two identities into PR #138's remainder yields the exact
decomposition
\[
\boxed{
R^0_{\rm exact}
=a_0+(t-1)\operatorname{per}(K^*)+\pi(t^2-1)
 -\sigma_1+a_0B_0-A_\Sigma.
}
\tag{7}
\]
Thus positivity is equivalent to the source-specific strict inequality
\[
\sigma_1<a_0+(t-1)\operatorname{per}(K^*)+\pi(t^2-1)
                 +a_0B_0-A_\Sigma.
\tag{8}
\]

## What this does and does not establish

This is a source-specific correlation from the actual zero-slack source matching,
but Section 168 establishes only \(\sigma_1\ge0\); the remainder needs an
upper bound on \(\sigma_1\) as in (8). Section 168 and the Section-165
placement certify only the unit collar \(L_1\subset H\). They do not place
\(L_t\) in \(H\), and their matching does not cover the lattice sites in the
annulus \(L_t\setminus L_1\). Equation (4) isolates that annular area exactly.
The signed gap \(\operatorname{area}(H)-\operatorname{area}(L_t)\) cannot be
replaced by an assumed containment or by the unit-collar matching.

Thus the proved bound is not a feasible countermodel and does not show that the
exact remainder is nonpositive. It shows that the zero-slack Hall consequence
alone cannot supply the desired lower bound: a further argument must couple the
outer annulus, the actual basis demand, and the fan neighborhood. It also cannot
be used in the locked-transition alternative of Section 168.1.

The downstream decision is whether PR #117's integrated sufficient condition
makes \(R^0_{\rm exact}>0\), which would yield a phase with nonnegative
Section-175 residual \(\Xi_\Sigma-j_*-|T_Z|\) for the Section-168 source of
size \(M\). The remainder is an integrated sufficient bound, not the pointwise
residual itself. Failure of the sufficient condition remains inconclusive.

## Falsification controls and stopping condition

The proof has three direct checks: (i) any phase with \(|Y_1(v)|>M\) would
contradict \(M=\alpha_1(H)\); (ii) the phase integral tiles the plane by
fundamental cells and counts the area of \(L_1\) exactly; and (iii) (4) is the
standard parallel-area identity for the convex polygon \(K^*\). Any use of (3)
for \(L_t\) would require a new source inclusion and matching proof; Section
168 does not supply one.

Stop condition: this unit-collar consequence does not prove an upper bound on
\(\sigma_1\), nor a lower bound on \(R^0_{\rm exact}\) or on
\(a_0B_0-A_\Sigma\). The remaining lemma is a single source-capacitated
phase statement that bounds \(\sigma_1\) using the \(L_t\setminus L_1\)
annulus and the actual Section-102 basis/fan demand, or a direct lower bound on
(1) under the full Section-168 hypotheses.

## Provenance and limitations

- Section 168 source: `docs/targets/target-a/20-zero-slack-normalization.md`
  at baseline `7d0a450fe66991036541023f95c44c064a04b6a8`.
- Section 165 placement: `docs/targets/target-a/17-plateau-response-lift.md`
  at the same baseline.
- Phase-integrated premise: PR #117, head
  `52a89ded959be4c96db4bdc4622ee73f7f63c3bd`; pinned README SHA-256
  `27d223939702a6e0ce72adcdeedd173201ef4a6ae9e0a98a5a2c64b61a5b5cfb`.
- Exact remainder and notation: PR #138, head
  `d17d45aebb04811c920d03f46c50a2337fe19a98`; pinned README SHA-256
  `f96ef081c91c7c3779c3b8ec99109bb7722a6d3460d39b64509d632974b3ac52`.
- Finite overlap limit: merged PR #98, head
  `2e4a3e1e73877df4f4756fcb4c7d331dcda1327f`, gives a nonglobal fixture where
  independently selected source-match images overlap. This proof uses only one
  `Y_1` matching and makes no claim that separate source matchings can be
  combined or their capacities added.
- PR #121 and its audit PR #148 give geometric matching-overlap fixtures, but
  their source sets fail `|A|=alpha_1(H)`. They therefore do not falsify (2),
  whose source-capacity hypothesis is essential.
- Open PR #102, head `025628b23df11470d4eb87ee981edbf250498691`, gives an
  abstract formula for overlap of two source-image shores. This result uses
  only the single lattice shore `Y_1`; it neither extends nor composes that
  formula, and it does not price the outer annulus.
- PR #141 gives a conditional pass for PR #117's published implication, with
  a clarification needed for a measurable joint basis/matching selector. This
  report does not independently audit that full implication or PR #138.
- New proof material is offered under Apache-2.0. OpenAI Codex (GPT-6 Luna
  xhigh) produced this corollary and prose. No independent AI-agent review is
  claimed. Required full theorem-certificate replay is deferred to the merging
  agent. Level I, Target A, Target B, and C-II remain open; C-I remains closed.
