# Actual plateau source-demand and fan-sink budget

**Classification: unreviewed proof candidate with exact finite regression controls.**
No canonical claim or theorem state changes. Originating agent: OpenAI Codex,
GPT-6 Luna xhigh. New material is offered under Apache-2.0; the seed-63 and seed-66
predecessors retain their own attribution and notices.

## Exact question and hypotheses

Investigation: `frontier-target-a-locked-sector-surplus-20261018`.
Baseline: `7d0a450fe66991036541023f95c44c064a04b6a8`; state
`2026-10-15.publication.2`; priority `public-frontier.3`; catalogue
`public-frontier.9`.

For every triangle-free global source optimum $A\subset H=\operatorname{conv}A$,
$|A|=N$, of diameter $D=D(N)$, assume the Section-165 common placement
$K^*+\mathbb B\subset H$. Let $X^*\subset
K^*=\operatorname{conv}X^*$ be the actual right-endpoint plateau optimum, with
$|X^*|=m^*$ and diameter $d=D(m^*)$, and set $t=(D-d)/2>1$. In the actual-response locked
branch use its canonical three-channel contact fan $\Sigma\subset X^*$, fixed while
the lattice phase varies. For each generic triangular-lattice translate $v$, choose
a measurable Section-102 admissible basis: a basis of the restricted deep-column
matroid extended to a basis of the full interior-row matroid (a lexicographically
least choice suffices). Do not substitute the superseded depth-only matching test.

Use the Section-175 sets $Z(v),O(v),Y_0(v),T_\Sigma(v),T_Z(v),T_O(v),C_i(v),O_i(v),
O_{\rm iso}(v)$, and define
\[
\Xi_\Sigma(v)=|O_{\rm iso}(v)|+\sum_i(|O_i(v)|-|C_i(v)|)_+,
\qquad
j_*(v)=N-m^*-|Y_0(v)|.
\]
Let $e=|E(\Sigma)|$, $a_0=\sqrt3/2$,
\(A_\Sigma=\operatorname{area}(N_1(|\Sigma|))\), and let
\(d_{\rm int}(v)=|C^\circ(v)|\) and
\(t_\Sigma(v)=|C^\partial(v)\cap V(\Sigma)|\) be the exact Section-102/175
quantities for that admissible basis.

## Phase-integrated inequality

For uniform translation over one lattice cell, the candidate proves
\[
\boxed{\mathbb E_v[\Xi_\Sigma-j_*-|T_Z|]
\ \ge\ \frac{\operatorname{area}(K^*+t\mathbb B)-A_\Sigma}{a_0}
 -N+\mathbb E_v[d_{\rm int}+t_\Sigma].}
\tag{1}
\]
Here $\mathbb E_v$ means $a_0^{-1}\int_F\,dv$ over a fundamental cell $F$ of the
triangular lattice; the nongeneric phase set has measure zero.
Since the fan is a connected unit-edge graph, Section 175.5 gives
\(A_\Sigma\le\pi+2e\). The exact integer residual in (1) implies the refined
sufficient condition
\[
\boxed{\operatorname{area}(K^*+t\mathbb B)+a_0\mathbb E_v[d_{\rm int}+t_\Sigma]
\ >\ a_0(N-1)+\pi+2e}
\tag{2}
\]
forces a generic phase with \(\Xi_\Sigma(v)\ge j_*(v)+|T_Z(v)|\). Indeed, if no such
phase existed, the integer residual would be at most \(-1\) at every generic phase,
so its mean would be at most \(-1\), contradicting (1)--(2). Dropping the
nonnegative basis terms gives the basis-independent sufficient condition
\(\operatorname{area}(K^*+t\mathbb B)>a_0(N-1)+\pi+2e\). By Sections 175.4 and
175.6, that phase has \(h(G)\ge j_*\) and hence \(\zeta-s\ge0\), the canonical
locked-branch Schur endpoint.

### Proof reconstruction

The disjoint-sector decomposition gives
\[
\Xi_\Sigma\ge |O|-|T_O|-\sum_i|C_i|
=|O|-|T_O|-|C^\partial|+t_\Sigma.
\]
The admissible Section-102 basis is essential for
\(|C^\partial|=m^*-|Z|-d_{\rm int}\); this identity is not inferred from a
depth-only matching. Subtract \(|T_Z|\) and \(j_*=N-m^*-|Y_0|\) to obtain
\[
\Xi_\Sigma-j_*-|T_Z|
\ge |O|+|Y_0|+|Z|-|T_\Sigma|-N+d_{\rm int}+t_\Sigma.
\]
Lattice-cell integration gives
\[
\mathbb E|Z|=\frac{\operatorname{area}(K^*)}{a_0},\quad
\mathbb E|O|+\mathbb E|Y_0|
=\frac{\operatorname{area}(K^*+t\mathbb B)-\operatorname{area}(K^*)}{a_0},
\]
and \(T_Z\sqcup T_O\) counts the lattice sites in the fan's open unit
neighborhood, so
\(\mathbb E(|T_Z|+|T_O|)=A_\Sigma/a_0\). Substitution yields (1). If its right
side exceeds \(-1\), some generic phase has nonnegative integer residual, which is
exactly the Section-175 closing inequality. This phase choice averages demand and
sink population together; it does not minimize the tube separately.

## Open next questions and scope

The result gives an actual-source population criterion for the exact Section-175
quantity \(\Xi_\Sigma-j_*-|T_Z|\), and therefore a new sufficient test for the
locked branch. It does **not** prove (2) for every sufficiently large global source,
does not establish a lower bound on the sector sink surplus beyond this criterion,
does not resolve the zero-slack branch, and does not close Target A or Level I.
Every source label, including any contact-isolated point, remains counted in \(N\);
no source-to-scaffold identification, deletion, motion, or replacement is asserted.

The decisive remaining lemma is to derive (2), or a stronger bound on the left side
of (1), from global source geometry while retaining every source label and the
actual plateau response. If (2) fails for an actual source, the next step is a
source-specific lower bound on \(\mathbb E\Xi_\Sigma\) that preserves the sector
sets; an independently optimized tube or abstract source-image overlap does not
supply it.

- **Downstream decision and quantity:** this can close the actual-response locked
  branch by making the exact residual \(\Xi_\Sigma-j_*-|T_Z|\) nonnegative at one
  phase.
- **Changed hypothesis:** predecessors supplied response fans without the actual
  source cardinality or phase-dependent demand. Here \(N,D,H\), the actual \(X^*\),
  and the source-to-response collar placement are retained.
- **Either outcome:** proving (2) from global-source geometry closes the locked
  branch. Failure of (2) for an actual source would leave this sufficient criterion
  inconclusive, not refute the desired surplus, and direct the next result toward a
  sector-specific lower bound on \(\mathbb E\Xi_\Sigma\).
- **First action:** apply Oler's bound to \(N\) in \(H\), then use the Section-155
  hull-alignment estimate to bound the gap
  \(\operatorname{area}(H)-\operatorname{area}(K^*+t\mathbb B)\), retaining the
  fan-neighborhood and admissible-basis terms.
- **Blocker:** no current theorem supplies this source-specific area/population
  comparison or the alternative sector-sink lower bound.

## Falsification and controls

`verify.py` reconstructs the sink surplus, checks the complete exterior-sink and
Schur-terminal partitions, and checks the pointwise population inequality underlying
(1) against every stored corrected seed-63 admissible ledger and every seed-66 case. It
explicitly excludes the 18 seed-63 relaxed-optimum records marked
`section102_admissible=false`; they are a negative control against the superseded
depth-only basis test. Both predecessor packages are also replayed independently.
Those fixtures have no canonical source demand $(N,j_*)$, and remain regression
controls rather than global-source counterexamples.

The exact inputs, code and saved evidence are SHA-pinned in `SOURCES.json`. Run from
the repository root:

```sh
python research-packages/e99-pass-20261018-local-01/verify.py
python research-packages/target-a-fan-tube-ledger/verify.py
python research-packages/target-a-full-tube-fan-ledger/verify.py
python scripts/research_package.py --package research-packages/e99-pass-20261018-local-01 --check-only
```

## Predecessors and review status

This complements, rather than repeats, PR #102's abstract source-image Hall formula:
the present result concerns the actual plateau phase and the full-tube sink budget.
It also follows the corrected seed-63 admissible basis optimum and the seed-66
pointwise phase obstruction. The predecessor evidence remains at its pinned source
commits in `SOURCES.json`. This proof candidate has not received an independent
mathematical audit; required repository-wide theorem-certificate replay is deferred
to the merging agent.
