# Erdős Problem #99 — complete-solution research run

**Frontier reviewed at:** `2026-10-10.audit.234` (historical review marker). Read `docs/STATE.md` and the manifest for the live state before work.
**LEVEL I STATUS:** still open

## Mission

For unit-separated planar sets let

\[
D(n)=\min\{\operatorname{diam}A:|A|=n,\ |x-y|\ge1\text{ for }x\ne y\}.
\]

Prove that for all sufficiently large `n`, every global minimizer contains a unit equilateral triangle, or disprove this with triangle-free global minimizers for an unbounded sequence of cardinalities.

A local minimum, finite counterexample, dense asymptotic family, shell model, or one triangle-containing minimizer per cardinality does not settle the problem.

## Mandatory bootstrap

Read `docs/STATE.md`, then the theorem manifest, research workflow, problem statement, the chosen route map, its named canonical modules, and the current route prompt. Do not bootstrap from repository-wide report search. Git/PR recency is not theorem authority.

## Current routes

### Target A

Canonical development now runs through Section 177. The sufficient global closure remains

\[
\operatorname{rank}S\le d_{\rm int}+|C^\partial|-\Delta_\Lambda,
\qquad d_{\rm sc}\ge\Delta_\Lambda.
\]

The route has two exact branches.

In the actual-response locked branch, Sections 169–174 supply a locked unit triangle in the actual response optimum, a nonnegative contact/facet stress reaching the response boundary, a proper positive-contact crosscut, three vertex-disjoint reaction channels, and thick-tube sector locality with exact basis balance. Section 175 sharpens the Schur cut. For a stress-generated contact fan `Sigma`, let

\[
T_Z=T_\Sigma\cap Z,
\qquad
Q_\Sigma=\sum_i\max\{0,|O_i|-|C_i|\},
\]

and let `O_iso` be the surviving exterior sinks with no surviving response neighbor. Then

\[
\boxed{
h(G)=|O|-\operatorname{rank}S
\ge |O_{\rm iso}|+Q_\Sigma-|T_Z|.}
\]

With

\[
j_*=N-|Y_0|-m^*,
\qquad
\zeta-s=h(G)-j_*,
\]

the current locked-branch target is exactly

\[
\boxed{
|O_{\rm iso}|+
\sum_i\max\{0,|O_i|-|C_i|\}
\ge j_*+|T_Z|.}
\]

The old Section-174 full basis-closed shield charge is superseded as the live endpoint. Exterior tube sinks cancel. Pointwise `|T_Sigma|<=9|E(Sigma)|`, and translation averaging gives

\[
\mathbb E|T_Z|
\le {\operatorname{area}(K^*\cap N_1(|\Sigma|))\over\sqrt3/2}
\le {2\pi\over\sqrt3}+{4\over\sqrt3}|E(\Sigma)|.
\]

In the zero-slack branch, Section 176 proves that for the fixed-hull capacity source `A^0`,

\[
\boxed{m^*-|A^0\cap K^*|\le12d+9,}
\]

and every saturating `X^* -> A^0` source matching is sector-preserving outside at most

\[
\boxed{5|V(\Sigma)|+12d+9}
\]

response vertices for any finite contact shield `Sigma`. This does not compare the boundary-order defect with the Schur demand and does not identify the independent source matchings. Section 177 adds genuine-source gates and an edge-lens/coarse-Hall alternative; neither closes the zero-slack conversion to Schur deficiency or a strict competitor.

### Target B

The sufficient closure remains

\[
G+E\ge {\sqrt3\over4}B+{\sqrt3\over2}(t+\chi-1).
\]

The promoted coherent near-extremal reduction does not solve the remaining multi-grain/global transfer problem.

The September 11 independent dense-grid/penetration/interpolation audit promotes DT1–DT4, TG1–TG3, PDG, PC1/PC3, MCP1 and the fixed-Section-50-`lambda` form of MCP2, and GPI as canonical scoped tools. In particular, for one dominant coherent component with `M>=b>=a`, `t=b/M>=tau>0`, and local Theorem-51 deficit `Delta`, GPI proves

\[
\liminf\Delta\ge4\cdot10^{-17}\tau^2.
\]

This is not a multi-grain theorem. Several macroscopic coherent grains may still share the global quadratic crossing mass, and density-only PDG can extract grids below the PC3 cancellation threshold. The live Target B obstruction is to couple retained physical crossings, deleted/interface crossings, and virtual noncrossing determinant mass across all macroscopic grains, or construct a strict smaller-diameter competitor from that global data.

### Target C

**C-I: CLOSED.**  
**C-II: OPEN.**

Use the contact-minimal, then diameter-pair-minimal representative and retain every source point, including contact-isolated points. The canonical §57 ZR/ZF theorem is only on the nonisolated positive-contact core `V`:

\[
\ker\Omega_V=\operatorname{span}\{\mathbf1,P_x|_V,P_y|_V\},
\qquad
\operatorname{rank}R_{C\cup H}[V]=2v-3.
\]

Canonical §§58–74 supply full-source geometry and force-hull stability; nonmatching, loaded-hull, and attachment currency; punctured phase control and a forced quadratic coherent physical grain; sharp Woodall-forest endpoint geometry; selected-extreme attachment control; and, in the exact primitive all-loaded shell, the corrected stress-polytope/leaf-forcing theorem. Section 72 gives `dim S=s_Z=2-d_H`, freezes every full-H leaf diameter edge throughout the normalized stress polytope, and for `s_Z>0` forces at least `s_Z+1=3-d_H` nonleaf–nonleaf full-diameter edges. Section 73 additionally forces a linear-by-linear complete phase-pure train grid inside every quadratic coherent grain, even with holes. Section 74 collapses a half-sized complete subgrid to inverse-diameter phase width, so every grid rhombus has defect `O(1/D)`. It still does not supply the remaining common-order/penetration theorem.

The exact remaining C-II split is in `docs/targets/target-c/CURRENT.md`. In the full-core branch, the next theorem must produce a source-realized face-coupled finite move or discrete replacement that passes every source lower constraint, actual-diameter upper constraint, and unary rhombus test, then yields strict contact loss at diameter `D` or a strict sub-`D` competitor. The separate macroscopic-container branch still lacks arbitrary-container packet capacity or a moved-core strict-diameter closure. Audit.230's quarter-fold isolate population count does not supply an integrated endpoint or capacity under moved geometry. Retain all source points, including contact isolates. PR #191's `0.995540...` theorem remains rejected.

## Binding corrections

Do not revive the incident-diameter Euler-path inference, FB4 localization, incompatible-cut C53 pentagon objection, RSR equality uniqueness, Eppstein near-quadrangulation inference, five-host occupancy inference, inward OP/exterior Reuleaux-cap containment, or any argument that drops contact-isolated source points.

For Target A, do not revert to the Section-174 full basis-closed shield penalty as the current endpoint; Section 175 cancels basis-partner and exterior-tube costs in right deficiency. Do not infer a relation between the zero-slack source defect and Schur demand merely because the former is `O(d)`.

## Research standard

Choose a route whose next lemma has a direct chain to a contradiction or strict sub-`D` competitor. Computation can certify arithmetic, finite enumeration, and regressions; it does not prove global optimality without a theorem bridge.

A frontier-changing result must update the state lock, theorem manifest, affected route/current file, and active prompt in the same change.
