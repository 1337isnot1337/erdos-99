<!-- theorem-state: {"artifact_id":"ART-8C1AB086AA81","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# Conditional global boundary/face inequality and nonglobal obstruction

Source mathematical sections preserved from the exact source blob recorded in the publication manifest. This is a conditional sufficient endpoint and scoped regression, not Level I closure. Administrative campaign/branch material is omitted.

## 4. The shortest remaining scalar theorem on the new C route

Subject to the audited C53–C63 inputs, the following single statement suffices for
Level I. It includes the actual global hypothesis and does not assume away rattlers.

> **Global boundary/face inequality.** There is `n0` such that every triangle-free
> global `n`-point minimizer with `n>=n0`, chosen first to minimize contact count and
> then diameter-pair count, satisfies, on its nonisolated contact core,
> `b+sum_F(deg F-4)>2|H|`.

Here `b` is the outer-face boundary-walk length, bridges counted twice, and the
sum runs over **all** bounded contact faces, not just exceptional rhombi. This
is an exact integer inequality.

To verify sufficiency, Euler and double-counting face incidences give

\[
2e=b+\sum_F\deg F,
\qquad f=e-v+1,
\]

and therefore

\[
e=2v-2-\frac12\left(b+\sum_F(\deg F-4)\right).
\tag{L1}
\]

The asserted strict inequality is equivalent to `e+h<2v-2`, contradicting ZF.
An unbounded sequence of source cardinalities has unbounded diameter, since
disjoint radius-`1/2` disks around its points fit in a bounded enlargement when
diameter is bounded. Thus the finite cutoff `D>=9` causes no asymptotic gap.

This is a shorter sufficient theorem, not a proof that this is the only possible
remaining route or that it follows from existing shell bounds. An equivalent
rank form is `e+h<=2v-3`. The original A and B endpoints remain valid independent
sufficient targets.

### Exact obstruction to dropping global optimality

For a regular unit odd `q`-gon, `C` is its boundary cycle and `H` its diameter
cycle. Then `v=e=h=q`, the outer walk has length `b=q`, and the sole bounded
face has degree `q`. Consequently

\[
b+\sum_F(\deg F-4)=2q-4<2q=2h.
\tag{L2}
\]

This violates the proposed closing inequality at arbitrarily large diameter,
while satisfying exact positive KKT scalar and tensor identities. The normalized
weights are `alpha=D_q^2/q` and `beta=1/q`, where
`D_q=1/(2sin(pi/(2q)))`. For prime `q` the canonical polygon theorem also supplies
local diameter minimality. Thus local rigidity, planarity, positive equilibrium,
and large diameter do not prove the closing inequality.

The unfilled shells are not global minimizers for odd `q>=11`: `sin x<x` gives
`D_q^2>q^2/pi^2`, while `2pi sqrt(3)<11` and the strict lattice bound give
`D(q)^2<(2sqrt(3)/pi)(q-1)<q^2/pi^2`. Filling with isolated near-triangular lattice
points preserves the stress and supplies the known leading-density regression,
but does not certify exact global optimality of the filled configuration.

This is a certified obstruction to the **weaker hypothesis signature**. It is
not a counterexample to the theorem with global optimality retained, and not a
formal independence certificate for the full repository.

## 5. Why the exceptional-face transfer has not been closed

For a pure disk, (L1) is `e=2v-T-2`, so the required inequality is `T>h`.
The canonical exposed-hull theorem proves it with a positive linear margin.
If train segments are terminated at exceptional faces, their naive count is
`T_ext=(b+sum_exceptional deg F)/2`; the Euler currency is instead

\[
\frac12\left(b+\sum_F(\deg F-4)\right)
=T_{\rm ext}-2 f_{\rm exc}.
\]

Thus even where that train interpretation is valid, the necessary extension is
`T_ext-h>2 f_exc`, not merely `T_ext>h`. The canonical bound `f_exc=O(D)` is at
the same scale as the pure margin. No sign or constant comparison was obtained.
The subsequent DT theorem supplies this exact train interpretation even with holes,
bridges, and disconnected rhombic pieces; it also excludes repeated crossings by
a strict direction-cone argument. Its DE extension preserves the pure leading
train/hull margin when `n-v=o(D^2)`. The precise consequence is now
`liminf f_exc/D>=sqrt(pi/(2sqrt(3)))-pi/4=0.166914...`, not a contradiction to
the available `f_exc=O(D)` upper bound. DP disproves a uniform local Oler charge
per exceptional face, and ordinary facewise Oler cancels the count exactly.
Euler's (L1) continues to apply to the full connected contact core.

Isolated points present an additional issue: the near-maximal area bound uses the
total source cardinality, while (L1) uses only core vertices. Replacing one by the
other would assume the missing Target A estimate. The new scalar stress kernel
does not constrain the positions of isolated points.

## 6. Adversarial regression audit

| Regression | Exact limitation retained |
|---|---|
| Regular shells | They satisfy the new rigidity conclusion and violate a global-free version of the closing face inequality, as (L2) shows. |
| Coherent strained monomers | Their independent activation constraints do not create Schur nullity; no activation-to-response rank map is claimed. |
| Annular routing and full-rank responses | Theorem Z uses an electrical resistance metric and a diagonal thrackle transfer matrix. It is not a theorem about arbitrary planar Schur incidence matrices. |
| Common-neighbor SDR collision | Both source-label matchings remain distinct; no perfect common-neighbor SDR is used. |
| Activation and zero-stress families | C63 needs PSD for every equilibrium multiplier, a fixed matrix, and a convergent correction. Zero coefficients alone never imply integration. |
| Diameter stars with small covers | No lower bound on a source diameter-cover number is inferred from C34 or ZF. Small-cover cases still exist in the A bookkeeping. |
| Near-star circular-planar networks | Z is an exact zero-transfer statement. No uniform lower bound on a small nonzero defect is asserted. |
| Crossing diameter matchings | They are expressly covered by the complete interval-sign check; no uncrossing or matching contraction discards an edge. |
| Two-edge crossing square | It has diagonal transfer and nonadditive resistance. Z requires at least three edges. |
| Nonthrackle selected tree | A three-edge path has diagonal edge transfer but nonadditive terminal resistance. Z requires pairwise intersecting selected chords. |
| Disk-clipped oblique grids | They are feasible and asymptotically dense. They have neither a certified global optimum nor the full canonical pure normal form needed by ZB. |
| Pure-rhombic chain-face survivors | The existing exact-chain audit and the new conditional ZB contradiction retain their global and pure-topology hypotheses. |
| Boundary-order losses | The general transfer still needs `T_ext-h>2f_exc`. No `O(D)` remainder is discarded. |
| Hidden source/scaffold changes | The contact stress matrix `Omega` and the A Schur matrix `S` remain different operators on different source data. No rank is transferred between them. |
| Vanishing conductance on many strict minors | ZR is an exact nullity statement, not a spectral-gap estimate. Positive eigenvalues may tend to zero at any rate. |
| Sharp 15-degree path | The exact family in Theorem P's regression is triangle-free and unit-separated, but not globally optimal. It disproves the non-strict threshold without global hypotheses. |
| Almost opposite rays at degree five | Theorem P proves non-diametrality, not degree four. The canonical five-sector rhombic examples forbid that shortcut. |
| Infimum versus minimum | Proposition N gives a unique-unit-pair approximating sequence at every fixed cardinality. Its limit can gain unit triangles. |

## 7. Literature and computation used

The theorem report records the exact circular-planar and Hoffman imports. The
primary [Eppstein paper](https://arxiv.org/abs/1708.05152) confirms the contact-edge
bound with **graph** diameter `delta`, not geometric diameter without a path
comparison. The normalization here uses unit contact lengths, giving `delta>=D`.
The [Bowen complete-saturation paper](https://arxiv.org/abs/math/0110260) concerns
finite replacements in infinite packings. It does not provide a finite variable-
container global diameter theorem, a uniform rearrangement radius at vanishing
strain, or a source-to-Schur transfer. It was not imported as a closing result.
Searches did not identify an exact theorem with the missing global face/shell
hypothesis signature. This is a report of the searches, not a literature-wide
nonexistence claim.

The new exact verifier uses integers and `fractions.Fraction`, including exact
sign comparisons in `Q(sqrt(3))`; its scope and output are in the theorem report.
Earlier floating-point probes were used only to look for false chord-sign claims;
the durable checks replace them with exact arithmetic. No global optimum is
certified by a numerical search.
