<!-- theorem-state: {"artifact_id":"ART-A897AD1EB73C","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"provenance","target":"shared"} -->
# Erdős Problem #99 — Canonical Working Report v1.7.0

**Version:** 1.7.0

**Date:** 2026-08-30

**LEVEL I STATUS:** **STILL OPEN — TARGET A UNRESOLVED**

This is the canonical research state for the investigation of Erdős Problem #99.
It supersedes `erdos_problem_99_1.5.1.md`, `erdos_problem_99_1.5.0.md`,
`erdos_problem_99_1.4.1.md`, `erdos_problem_99_1.4.0.md`, all earlier theorem-state
files, old working reports, `FINAL(1)`, `FINAL(2)`, synthesized reports, and
continuation addenda as a theorem-state file.

The seven supplied papers remain the literature baseline supporting the canonical
stack. Internet literature search was permitted during the post-v1.5.1 research run,
but no additional web result is promoted here as a theorem dependency: the v1.7.0
continuation below is proved internally from the trusted canonical stack.

**2026-08-30 audit note.** This is an append-only research record. Some late
sections intentionally retain historical duplicate numbers so that existing
cross-references remain stable; use the full section title and the Contents map
when navigating. The detailed disposition of repaired, conditional, historical,
and unproved claims is in
docs/audits/mathematical_audit_2026-08-30.md.


## Version 1.5.1 audit policy

Version 1.5.1 is the audited patch successor to v1.5.0. It preserves the complete
v1.5.0 theorem state but corrects the source-localization statements and restores exact
bounds/identities omitted from the first v1.5 build. **Sections 109 onward are
authoritative wherever they sharpen or correct Sections 97--108.** Sections 97--102
survive the v1.5.1 re-audit unchanged.

The principal corrections are: branchwise rather than unqualified face-by-face latent
forest confinement; an explicit outer-terminal row bound for the Schur response; an
exact O(D) one-root component-incidence budget; a corrected thermodynamic-cage
localization; safer wording for the strained-monomer regression; restoration of the
general biphasic Hall-core bounds; and restoration of the exact two-sided
finite-packing-defect transfer identity.

The authoritative Target A endpoint remains the exact Schur-response inequality
\[
\operatorname{rank}S\le d_{\rm int}+|C^\partial|-\Delta_\Lambda.
\]

## Version 1.5.0 audit policy

Version 1.5.0 is the first major Target A consolidation after v1.4.1. It preserves
the complete audited v1.4.1 theorem stack and promotes the subsequently audited
fixed-basis tight-core, phase-selective contraction, plateau-terminalization,
phase-pure boundary-minor, Schur-response, quantized Hall-core, and source-specific
rattler/forest refinements.

**Sections 97 onward are the authoritative v1.5.0 frontier.** Sections 88--96 are
retained as the frozen v1.4.1 endpoint and are historical wherever Sections 97
onward explicitly sharpen or supersede them.

The central change is conceptual. Target A is no longer treated as one undifferentiated
monomer--dimer Hall problem. The audited reductions now separate:

1. **scaffold-only structure**, valid for an independently chosen smaller optimum;
2. **plateau/boundary structure**, which contracts the quadratic scaffold bulk to
   an exact boundary-order rank problem; and
3. **source-specific structure**, which remembers that the scaffold was extracted
   from a genuine triangle-free global minimizer with a super-boundary population
   of strict rattlers.

The first two levels by themselves cannot close Target A. A surviving counterexample
already satisfies
\[
h(G)\le j-1,
\qquad
d_{\rm sc}\le\Delta_\Lambda-1,
\]
so no theorem that depends only on the independent smaller optimum, its plateau
saturation, or its monomer--dimer scaffold can imply the reverse inequality without
using additional source information.

The promoted Target A results include:

- fixed-basis fundamental-circuit unions have **exactly additive signed Hall
  deficiency**, with every successive overlap Hall-tight;
- the full fixed-basis tight core contracts exactly, leaving a fully matchable
  residual and the invariant
  \[
  g=\Delta_\Lambda-d_{\rm sc};
  \]
- every hypothetical survivor has
  \[
  d_{\rm sc}=O(D)
  \]
  with an explicit coefficient;
- all dimers together with either complete monomer orientation form an independent
  transversal set and may be contracted without losing any scaffold nullity;
- the contracted matroid has six layered planar gammoid presentations and exact
  directed-contour formulas;
- terminalizing the smaller optimum at the right endpoint of its diameter plateau
  makes its interior lattice conflict graph right-Hall-tight:
  \[
  \nu(G_0)=|Z|;
  \]
- after exact interior contraction, all live matching obstruction is boundary-order;
- after contracting dimers and one monomer phase, an exact phase-pure quotient has
  only \(O(D)\) nonloop ground elements;
- positive Hall cores have a quantized convexification gap; every unit-nullity
  circuit has at least fourteen monomers in total and at least six of each
  orientation;
- the full quadratic matching problem admits an exact boundary Schur complement
  \(S\), with
  \[
  d_{\rm sc}=d_{\rm int}+|C^\partial|-\operatorname{rank}S,
  \qquad
  h(G)=|O|-\operatorname{rank}S;
  \]
- source strict rattlers are almost all independent over the source core in a
  natural triangular-lattice transversal matroid: their conditional nullity is
  \(O(D)\);
- the unchanged contact-minimal backbone in the hybrid representative satisfies an
  exact facial-defect budget, and the latent forest can be chosen too short to cross
  a fixed unit core edge;
- the explicit strained-monomer regression shows that a triangle-free
  \(D^2\)-scale near-lattice phase can spend only \(O(D)\) total clearance while
  preserving exact monomer scaffold combinatorics.

The last item is a binding warning: **no proof may assign a fixed positive geometric
cost to every triangle-free monomer cell, near-equilateral face, or strict rattler.**
The missing theorem must detect exact global diameter optimality at the boundary.

The authoritative Target A endpoint in v1.5.0 is the source-specific
boundary-response inequality
\[
\boxed{
\operatorname{rank}S
\le
d_{\rm int}+|C^\partial|-\Delta_\Lambda,
}
\]
equivalently
\[
\boxed{d_{\rm sc}\ge\Delta_\Lambda}
\]
and equivalently
\[
\boxed{h(G)\ge j.}
\]

A useful geometric restatement of the missing mechanism is:

> **Boundary-to-bulk first-variation theorem.** A super-boundary triangle-free
> strict-rattler population may distribute \(O(1/D)\)-scale expansive strain through
> \(D^2\)-scale near-triangular bulk at only \(O(D)\) total local cost. Prove that an
> exact global minimum-diameter boundary cannot support that strain: either the
> boundary admits a strict diameter decrease, or the source information forces the
> exact Schur-response rank loss required above.

No such theorem is proved in v1.5.0.

The authoritative Target B endpoint is unchanged:
\[
\boxed{
\operatorname{rank}\overline{\mathcal B}_\xi+I+r
\le T-q-r_\alpha,
}
\]
followed by exact topology-corrected transport. The `s_C=1` tree-specific obstruction
remains the projected active-bar-average span \(\mathcal A_{1\rm t}\).

### Binding v1.5.0 audit corrections

The following refinements supersede older wording:

- Fundamental circuits relative to one fixed maximum basis **may overlap heavily but
  their signed Hall deficiency is exactly additive along the fixed-basis union flag**.
  What is not available is disjointness or absolute/spatial interface-charge
  additivity.
- The old prohibition on contracting zero-charge phase regions is narrowed:
  **arbitrary** phase-region contraction remains invalid, but the audited
  phase-selective contractions of Section 98 and the fixed-basis tight-core
  contraction of Section 97 preserve transversal-matroid nullity exactly.
- A residual set obtained after matroid contraction or deletion is **not**
  automatically a global optimum at its new cardinality.
- Plateau terminalization creates a boundary-terminal planar gammoid; it does not
  prove that all routing lies in a width-one annulus.
- The contact-minimal and maximal-contact representatives need not coincide. When
  source-face and forest information are combined, the legitimate bridge is the
  hybrid representative of Theorem 12.4, which contains the unchanged
  contact-minimal backbone pointwise.
- Asymptotic convergence to the triangular lattice is not a contradiction:
  triangle-freeness is not closed under the relevant limit.

## Version 1.4.1 audit policy

Version 1.4.1 is a patch-level canonical successor to v1.4.0. It preserves the
complete audited v1.4.0 theorem stack and promotes the subsequently audited dual-Hall,
phase-charge, peeling, transversal-matroid, and bounded-`s_C=1`-tree refinements.
Sections 88 onward are the authoritative v1.4.1 frontier. Sections 79--87 are retained
as the frozen v1.4.0 endpoint and are historical wherever Sections 88 onward explicitly
supersede their frontier language.

The promoted Target A refinements are:

1. if `R=Y_in`, `y=|R|`, `nu=nu(G)`,
   \[
   d_{\rm sc}=\max_{S\subseteq X_m}(|S|-|N(S)|)=m-\nu
   \]
   is the left Hall nullity and
   \[
   \Delta_\Lambda=N-|Y|\ge1
   \]
   is the exact lattice-population deficit, then
   \[
   \boxed{h(G)-j=d_{\rm sc}-\Delta_\Lambda};
   \]
   hence Target A is exactly `d_sc >= Delta_Lambda`;
2. every selected monomer--dimer cell family `S` satisfies the exact cell-complex
   identity
   \[
   |S|-|N(S)|=\frac{m_3(S)-b(S)}2-\chi(S)
   \]
   and the exact local incidence-charge identity
   \[
   |S|-|N(S)|
   =\frac1{12}\sum_{v\in N(S)}(4p_v(S)+3q_v(S)-12);
   \]
3. a positive-deficiency maximizer of minimum cardinality is a Hall core: every
   lattice vertex has selected incidence degree at least two and every connected
   incidence component has positive deficiency;
4. on such a core the only zero local phase-charge states are
   \[
   (p_v,q_v)=(3,0)\quad\text{and}\quad(0,4),
   \]
   corresponding exactly to monomer and dimer crystalline cancellation phases;
5. if `U=N_G(X_m)` and `z=|Y_in setminus U|`, then Hall deficiency has the exact cell-peeling
   representation
   \[
   \boxed{h(G)=z+\max_{\rm deletion\ sequences}\sum_i(\pi_i-1)};
   \]
6. the matchable cell subsets form a transversal matroid of rank `nu`; every
   fundamental circuit has Hall deficiency exactly one and therefore net local phase
   charge exactly `12`;
7. fundamental circuits need not be disjoint or weakly separated. Section 97
   supersedes the old unqualified nonadditivity warning: relative to one fixed maximum
   basis, unions of fundamental circuits have exactly additive **signed Hall
   deficiency**, while disjoint/absolute spatial interface charge is still not
   available; and
8. the preferred v1.4.1 Target A endpoint is the exact global scaffold phase-charge
   inequality
   \[
   \boxed{
   \max_{S\subseteq X_m}
   \sum_{v\in N(S)}(4p_v(S)+3q_v(S)-12)
   \ge12\Delta_\Lambda,
   }
   \]
   equivalently `d_sc>=Delta_Lambda`, equivalently the peeling inequality
   `z+max sum(pi_i-1)>=j`, equivalently the older `h(G)>=j` statement.

The promoted Target B refinements are:

1. the cyclic hypothesis in the old two-direction conclusion is unnecessary:
   \[
   \boxed{s_C=1\Longrightarrow C\text{ uses exactly two train directions}};
   \]
2. if an `s_C=1` terminal component is a tree, then
   \[
   \boxed{|V(C)|\le10,\qquad |E(C)|\le9};
   \]
3. if `k_{1t}` is the number of `s_C=1` tree components that are strict-backward
   origins, origin concentration gives
   \[
   k_{1t}\le r_\alpha+1,
   \]
   and `k_{1t}<=r_alpha` in the proper-origin case;
4. consequently the total train population in such origin components is at most
   `9(r_alpha+1)`, or `9r_alpha` in the proper-origin case; and
5. if `A_{1t}` denotes the span of the projected active-bar average functionals
   arising from blockers whose origins lie in `s_C=1` trees, then
   \[
   \boxed{
   \operatorname{rank}\overline{\mathcal B}_{\xi,1t}
   \le8k_{1t}+\operatorname{rank}\mathcal A_{1t}.
   }
   \]
   Thus unbounded train multiplicity is removed from the `s_C=1` tree class. The
   surviving tree-specific obstruction is repeated-bar diversity through
   `rank A_{1t}`.

The following v1.4.1 warnings are binding:

- a charge identity is not by itself a lower bound; zero-charge monomer and dimer
  bulk can be arbitrarily large in local models;
- the `d_sc` fundamental circuits may overlap heavily, so one cannot sum one
  spatially distinct unit of interface charge per circuit without an additional
  theorem;
- if `d_sc=0`, the empty set is an allowed minimum-cardinality maximizer. Statements
  about nonempty Hall cores are to be read in the positive-deficiency case;
- `s_C=1` trees are now exactly two-directional and bounded by nine trains, but they
  are **not** automatically cyclic/Ferrers systems;
- the new tree bound does not control the active-bar average span `A_{1t}`; and
- the exact pure Target B endpoint remains
  \[
  \operatorname{rank}\overline{\mathcal B}_\xi+I+r
  \le T-q-r_\alpha,
  \]
  followed by exact topology-corrected transport.

## Version 1.4.0 audit policy

Version 1.4.0 preserves the complete audited v1.3.0 theorem stack and promotes two
independent post-v1.3 advances, one on each surviving branch. Sections 79 onward are
the authoritative v1.4 frontier. Sections 75--78 are retained as the frozen v1.3
endpoint and are historical where v1.4 explicitly supersedes them.

The promoted Target A additions are:

1. a generic safe-collar translate may be chosen so that no relevant lattice point
   lies on either parallel-body boundary and no scaffold cross-distance is exactly
   `0` or `1`, without sacrificing the strict collar population estimate;
2. because `t>1`, every lattice point within open unit distance of a point of the
   independent optimum `X_m` automatically lies in the inner scaffold
   `Y_in = Lambda_v cap int(K_m+B)`;
3. every scaffold blocker `x in X_m` has **exactly three or four** lattice conflicts;
   the full conflict neighborhood is respectively an elementary unit equilateral
   triangle or a unit lozenge, and `x` lies strictly in the interior of that cell;
4. distinct blocker cells have disjoint interiors, so the scaffold blockers form an
   exact **monomer--dimer packing** on the honeycomb dual of the triangular tiling;
5. the radial conflict graph is planar and every lattice-side vertex has degree at
   most five;
6. the full-complex Euler identity
   \[
   \delta=m_3+2m_4+\gamma-s-g
   \]
   and, for every induced Hall subgraph,
   \[
   |Q|-|N(Q)|
   =\gamma_Q-\mu_Q-b_1(Q)+b_3(Q)+2b_4(Q)
   \]
   are exact;
7. a maximum-deficiency Hall set of minimum cardinality has no degree-one left
   vertices, giving the exact leafless formula
   \[
   h(G)=\max_{b_1(Q)=0}
   \bigl(\gamma_Q-\mu_Q+b_3(Q)+2b_4(Q)\bigr);
   \]
8. the full complex admits exact face-shell identities separating monomer gaps,
   dimer shared edges, outer boundary, and nontriangular gap excess; and
9. the new Target A endpoint is the **monomer--dimer cycle-cut rigidity lemma**
   `h(G)>=j`.  The old cross-configuration two-well transfer problem remains a
   valid alternate route, but it is no longer the only route and is not needed if
   the scaffold-internal cycle-cut theorem is proved.

The promoted Target B additions are:

1. every stochastic Minkowski width coefficient is in fact strictly positive:
   `a_{hC}>0` for every active diameter bar `h` and every terminal component `C`;
2. every `s_C=0` terminal component is atomic: it consists of one train edge, its
   Minkowski summand is a unit segment, and that train is strictly forward for every
   active diameter bar, hence can never be a strict-backward origin; in the nonzero
   minimal-face-kernel branch, the same atomic train forces all selected bar
   potentials to coincide and hence `r=1`;
3. common component rotations admit an exact second-variation formula whose
   zero-first-derivative term is a strictly negative weighted variance modulo common
   rotation;
4. local diameter minimality therefore forces the active component-rotation
   derivative covectors to positively span the full quotient
   `R^{c(Theta)}/<1>`, so their rank is exactly `c(Theta)-1` and at least
   `c(Theta)` nonzero active restrictions are required when `c(Theta)>=2`;
5. a strict-backward blocker row whose origin is component `C` restricts to the
   full-support stochastic row `e_C^*-a_h`; rows selected from distinct origins are
   independent until all components are used, and all-component selection has rank
   exactly `c(Theta)-1`;
6. if `k_org` is the number of distinct strict-backward origin components, then
   \[
   r_\alpha\ge\min\{k_{\rm org},c(\Theta)-1\},
   \qquad
   k_{\rm org}\le r_\alpha+1,
   \]
   with the sharper `k_org<=r_alpha` whenever `r_alpha<c(Theta)-1`; and
7. strict-backward origins are proved only to satisfy `s_C>0`.  **They are not
   proved to be cyclic.**  In particular, `s_C=1` tree components remain a live
   residual case and must be handled explicitly in any Target B closure.

The following v1.4 warnings are binding:

- the new scaffold monomer--dimer theorem does **not** identify the original
  saturated minimizer with the independent `m`-optimum; it avoids that invalid
  identification by deriving a second exact two-well structure entirely within the
  scaffold;
- planarity, Euler charge, and motif counts alone do not imply the required Hall
  surplus.  Shifted-lattice monomer and lozenge phases provide exact local
  cancellation regressions;
- the exact Target A gap remains one Hall-rank unit: `h(G)>=j` versus survivor
  bound `h(G)<=j-1`;
- the face-shell quantity `b_infty` used below is the **radial-graph unbounded
  facial boundary-walk length**.  Equivalently, the number of exposed lattice cell
  edges on the unbounded side is `b_infty/2`;
- the Dulmage--Mendelsohn/dual-contour, Ferrers-strip, and monomer phase-rigidity
  continuations are proposed routes, not promoted theorems;
- the Target B positive-spanning theorem controls only common component rotations;
  it does not by itself prove the internal `xi` coforest inequality;
- `s_C=1` trees cannot be silently merged into the cyclic two-family case;
- the pure Target B residual remains
  \[
  \operatorname{rank}\overline{\mathcal B}_\xi+I+r
  \le T-q-r_\alpha,
  \]
  followed by exact topology-corrected transport; and
- no width-one-annulus gammoid or plateau-terminalization theorem is part of v1.4.0
  unless separately proved and audited.  Such language is a research target, not a
  canonical result.

## Version 1.3.0 audit policy

Version 1.3.0 preserves the complete audited v1.2.0 theorem stack and promotes the
subsequent compatible-collar, clearance, Delaunay-matching, and Hall-conflict-graph
continuation. Sections 71 onward are the authoritative frontier. Earlier Target A
frontier language is retained for provenance and should not be treated as the current
endgame. Target B is unchanged except for restatement with the already-corrected
component-rotation rank budget.

The promoted v1.3 additions are:

1. the **unconditional compatible-collar dichotomy** with
   \(C_{\rm col}=\pi(1/2+2/\sqrt3)\): either \(\rho<C_{\rm col}D\), or the
   independently chosen \(m=N-\rho\) optimum admits a common strict sub-\(D\)
   scaffold containing \(>N-C_{\rm col}D\) points;
2. the sharper safe-collar count, including the uniform additive gain
   \(2\pi/\sqrt3\) and the stronger \(t\)-dependent form;
3. the **deep Voronoi containment theorem** and the sharp local Delaunay clearance
   inequality
   \[
   \operatorname{area}(T)-\frac{\sqrt3}{4}
   \ge\frac{\sqrt3}{6}\sum_{v\in T}\mu_T(v),
   \]
   with exact equality side multisets \(\{1,1,1\}\) and
   \(\{1,1,\sqrt3\}\);
4. the global nearest-neighbor clearance budget
   \[
   \sum_{p\in A}\delta(p)
   <\left(24+\frac\pi2\right)D+18;
   \]
5. the degree-six nearest-neighbor graph bound, the matching estimate
   \( |M|\ge\rho/24-D-3/4 \), and the fact that the selected matching edges are
   strong Gabriel edges that can be included simultaneously in a Delaunay triangulation;
6. the **matched two-well theorem**: along \(\rho/D\to\infty\),
   \(\rho/24-o(\rho)\) disjoint matched edges have both incident deep Delaunay
   faces approaching one of the two exact equality wells
   \(\{1,1,1\}\) or \(\{1,1,\sqrt3\}\);
7. the **exact Hall--Kőnig conflict-graph theorem** for the independently constructed
   scaffold,
   \[
   m+|Y|-\nu\le N-1,
   \qquad
   |S|-|N(S)|\le\rho-1;
   \]
8. the resulting **inner-band near-perfect conflict matching**: after removing the
   conflict-free safe-collar sites, all but at most \(\rho-k-1=O(D)\) remaining
   lattice sites can be matched injectively to distinct conflicting points of the
   \(m\)-optimum; and
9. the resulting v1.3 Target A endpoint: a **two-well configuration-transfer /
   inner-band Hall-rigidity theorem**, not another forest-rigidity statement.

The following v1.3 warnings are binding:

- the original saturated minimizer \(A\), in which the clearance matching and
  two-well Delaunay geometry live, is **not co-embedded** with the independently
  chosen \(m\)-optimum scaffold; transporting capacity between them is exactly the
  unresolved step;
- triangle-freeness excludes the exact \(\{1,1,1\}\) equality triangle but does
  **not** exclude convergence to that well. The scaled equilateral family is a
  regression against every “\(120^\circ\)-only” conclusion;
- strict rattlers have no uniform positive clearance. In a super-boundary survivor,
  the total clearance is only \(O(D)\), so most rattlers become increasingly
  near-contact;
- the Hall--Kőnig theorem is a necessary expansion property of a surviving
  counterexample, not by itself a contradiction;
- Target B receives no new blocker-rank theorem in v1.3. The exact residual target
  remains
  \(\operatorname{rank}\overline{\mathcal B}_\xi+I+r\le T-q-r_\alpha\),
  followed by exact topology-corrected transport.

## Version 1.2.0 audit policy

Version 1.2.0 preserves the complete audited v1.1.0 theorem stack and integrates the
subsequent hybrid-forest and terminal-component continuation. Within the historical
v1.2 layer, Sections 60 onward were the authoritative frontier. In v1.3, Sections 71
onward supersede the old Target A frontier. Earlier language is retained only for
provenance.

The promoted additions are:

1. the exact rooted-forest rank/self-stress identity
   \(\ell=u-r+c+\sigma\), with \(0\le\sigma\le r-c\), replacing the historical
   coarse estimate \(u\ge\ell/2\);
2. the root-skeleton exactification theorem: after pinning at most \(r-c\) branch
   junctions and opening at most \(2(r-c)\) old forest contacts, the hybrid branch
   contains a smooth one-root exact-unit-bar manifold of dimension at least
   \(u-r+c\);
3. the affine forest triangle-factor exclusion theorem and the forest rattlerization
   theorem: a nearby same-diameter triangle-free global minimizer contains at least
   \(u-r+c\) genuine strict rattlers and hence a local open set of dimension at least
   \(2(u-r+c)\);
4. the same-diameter saturation theorem: any triangle-free minimizer can be extended
   inside its fixed hull to a unit-covering triangle-free minimizer by adding fewer
   than \((\pi/2)D\) points;
5. the strict open-disk replacement and collar inequalities, which reduce a
   super-boundary rattler population to an exact packing/grafting problem rather than
   a linkage problem;
6. the terminal-component Minkowski decomposition of the convex hull;
7. the componentwise vector-closure strengthening of the terminal-turn inequality and
   its exact \(s_C=0,1,2\) equality classification;
8. the stochastic Minkowski-width formula for component rotations of the true inverse
   blocker, giving component-rotation blocker rank at most \(c(\Theta)-1\); and
9. the resulting v1.2.0 endgame: **saturated rattler capacity** for Target A and
   **internal terminal-component blocker rank** for Target B.

The following warnings are part of the audit:

- deletion optimality \(D(n-u)=D(n)\) is still not assumed;
- raw triangle-wall normal rank on the exact-bar torus can be \(u-O(1)\); the affine
  factor-exclusion theorem concerns the straight same-\(D\) forest flat instead;
- the root-skeleton theorem does not claim that all \(r-c\) root-separating edges can
  always be opened while preserving a full \(u\)-dimensional bar manifold; branch
  junctions may have to be pinned;
- the cycle-lift shortcut remains rejected because \(\mathcal D\) is injective;
- the new component-rotation calculation controls only the common rotation of each
  terminal component.  Internal relative-angle coordinates remain the pure Target B
  obstruction;
- neither the strict-lattice population estimate nor saturation alone proves the
  required rattler-capacity/grafting theorem.

## Version 1.1.0 audit policy

Version 1.1.0 preserves the complete audited v1.0.0 theorem stack and integrates the subsequently audited continuation. The new material is promoted only where its proof survives a second review. In particular:

1. the minimal-face harmonic--Dirichlet reduction and its six-potential bound are promoted;
2. visible tangent quartic freedom is compressed to at most five non-rotational terminal-potential degrees;
3. the peripheral-dual rank theorem is promoted;
4. the terminal direction-network, terminal-turn factorization, and boundary-velocity blocker normal form are promoted;
5. the proposed cycle-lift deficit is explicitly rejected: the terminal direction map is already injective, and its scalar cycle space is not the neutral train-angle space;
6. the six-block facial-peeling algebra is promoted only in corrected form. A globally diameter-invisible terminal train set is not claimed impossible. Instead, such a terminal set itself yields a local same-diameter optimal train-angle flat;
7. the exact diameter-plateau theorem `D(m)=D(n)=D => n-m < (pi/2)D` is promoted; and
8. the hybrid bridge-forest lineality is promoted to an exact local optimal-flat statement, while deletion optimality remains open.

The older Section 18 two-potential wall reduction from the continuation is not used as a trusted dependency in v1.1.0; the later harmonic--Dirichlet theorem supersedes it. Historical statements from v1.0.0 remain in the file for provenance, but Sections 48 onward are the authoritative frontier.

## Version 1.0.0 audit policy (retained history)

Sections 1--23 below are the previously synthesized and adversarially audited base
record. Their theorem statements and proofs are retained in full because later work
uses them extensively. Some *frontier descriptions* in Sections 18, 21--23 are now
historical and are explicitly superseded by Sections 24 onward.

Sections 24 onward consolidate the post-synthesis work and a fresh second-pass audit
of the recent Sol/Pro derivations. Recent claims were re-derived rather than accepted
merely because they appeared in an addendum. The audit produced several corrections:

1. the translated-lattice `n-1` improvement survives and sharpens the exact shell
   threshold to `G+E<c0 B` in the pure rhombic-disk case;
2. the sixfold phase-energy and phase-atomic/exposed-hull machinery survives, and in
   fact yields a **uniform macroscopic gap** `T-q >= 0.333829... D-o(D)`;
3. the train-angle Hessian, signed-variance formula, stress-projected signed
   Laplacian, and backward-flip rank reduction survive;
4. the older claim that higher-order locking must be "backward or invisible" was
   too strong: **tangent incidences with lambda=0 can produce genuine quartic
   blocking** and must be retained;
5. the previously displayed tangent expansion omitted a generally nonzero fifth
   order term. The corrected expansion is recorded below; its quartic conclusion
   remains valid;
6. a claim that two diameter-bar rotation classes automatically give a global
   same-diameter flex is **not established** because unsupported active equality
   bars can still block. Only the stress-supported bars are controlled by that
   argument;
7. raw support depth remains non-Oler currency because of exact support-turning
   cancellation;
8. Target A, the super-boundary bridge-forest branch, remains genuinely open.

Accordingly, the authoritative current frontier is Sections 45--48, not the older
"current target" language embedded in Sections 18 or 23.

## Source provenance for v1.0.0

This version consolidates, deduplicates, and where necessary corrects the mathematical
content of the earlier canonical/synthesis files, the post-synthesis Sol Max addenda,
and the two most recent independent continuation runs (backward-flip/terminal-rank and
stress-projected signed-Laplacian/quartic-tangent work), together with the subsequent
in-context audit that produced the generalized phase-atomic theorem and secondary-cusp
reduction. Superseded prompts and duplicated transcript text are not treated as
independent evidence. The seven supplied papers remain the literature baseline.

---

## Contents

The report preserves the numbering of the audited research record. Sections 28--35
were intermediate post-synthesis notebooks whose surviving content is folded into
Sections 24--27 and 36 onward; their numbers are intentionally retired so that later
cross-references remain stable.

- **1--20:** problem, literature baseline, KKT/rigidity framework, almost-rhombic
  structure, nonlinear stress, canonical representatives, regressions, and original
  audit.
- **21--23:** Oler-surplus shell decomposition, exact train-end depth, and the first
  combined continuation frontier. Their old capacity thresholds are historical and
  superseded below.
- **24:** perimeter saturation, uniform width, and linear support depth.
- **25:** exact support-turning and mixed-area identities.
- **26:** sixfold phase energy, grain decomposition, zonotope identities, train-angle
  modes, and difference-body transport.
- **27:** historical post-synthesis route log.
- **36:** strict translated-lattice \(n-1\) diameter improvement and the current
  shell threshold \(G+E<c_0B\) in the pure disk.
- **37:** exact train-angle Hessian, signed variance, backward trains, and tangent
  equality.
- **38:** second-pass audit ledger for the recent work.
- **39:** generalized phase-atomic/exposed-hull theorem and quantitative train/hull
  ratios.
- **40:** macroscopic common first-order-neutral train space.
- **41:** stress-projected signed train Laplacian.
- **42:** backward-flip rank, terminal localization, secondary cusp, tangent
  potential transfer, and the conditional invisible-coordinate normalization.
- **43:** corrected quartic tangent-class mechanism.
- **44:** stronger support-depth tail and boundary-curvature consequences.
- **45:** v1.0.0 Target B frontier (historical after Sections 49--69).
- **46:** v1.0.0 Target A frontier (historical after Sections 60--64).
- **47:** regression tests and dead routes.
- **48:** v1.1.0 continuation audit and notation.
- **49--50:** minimal-face harmonic--Dirichlet reduction, ordered tangent collapse,
  harmonic transport, and peripheral-dual rank.
- **51--52:** terminal direction-network normal form, terminal-turn factorization,
  and the exact boundary-velocity/inverse-blocker representation.
- **53:** corrected six-block facial peeling: backward rank or same-diameter optimal flat.
- **54:** exact diameter-plateau theorem and the historical v1.1 Target A flat formulation.
- **55:** Ferrers endpoint, terminal resources, and correct phase-atomic bookkeeping.
- **56--58:** historical v1.1 remaining lemmas, strategy, and status; superseded by
  Sections 60--69 except where individual inequalities are explicitly reused.
- **59:** v1.1.0 version history.
- **60:** rooted-forest rank/self-stress identity.
- **61:** root-skeleton exactification.
- **62:** affine forest triangle-factor exclusion and forest rattlerization.
- **63:** same-diameter saturation, strict lattice replacement, and collar growth.
- **64:** authoritative v1.2 Target A: saturated rattler capacity / scaffolded grafting.
- **65:** terminal-component Minkowski decomposition.
- **66:** componentwise turn closure and the exact \(s_C=0,1,2\) classification.
- **67:** stochastic Minkowski-width formula and explicit component-rotation rank budget.
- **68:** authoritative v1.2 remaining lemmas and topology correction.
- **69:** version 1.2.0 exact status.
- **70:** version history and provenance through v1.2.0 (historical).
- **71:** unconditional compatible-collar dichotomy and exact safe-collar population.
- **72:** deep Voronoi containment, local Delaunay clearance, and global clearance budget.
- **73:** degree-six nearest-neighbor matching, Gabriel/Delaunay promotion, and the matched two-well theorem.
- **74:** exact Hall--Kőnig scaffold conflict graph and inner-band near-perfect conflict matching.
- **75:** authoritative v1.3 Target A: two-well configuration transfer / Hall rigidity.
- **76:** authoritative v1.3 Target B: unchanged internal blocker/coforest rank plus topology transport.
- **77:** version 1.3.0 exact status and unified endgame.
- **78:** current version history and provenance.

---

## 1. The problem and its quantifiers

For $n\ge 2$, define

\[
D(n)=\min\left\{\operatorname{diam}(A):
A\subset\mathbb R^2,\ |A|=n,\ |x-y|\ge1\text{ for }x\ne y\right\}.
\]

A minimizing configuration is an $n$-point set $A$ with minimum pairwise distance (1) and diameter $D(n)$. Its **unit-contact graph** $G(A)$ has vertex set $A$ and edge set

\[
C(A)=\{xy:|x-y|=1\}.
\]

A unit equilateral triangle is exactly a triangle in $G(A)$, or equivalently three mutually tangent radius-$1/2$ disks in the associated equal-disk packing.

Erdős asks whether

\[
\exists n_0\ \forall n\ge n_0\ \forall A,
\quad A\text{ minimizing}\Longrightarrow G(A)\text{ contains a triangle}.
\]

The negation requires triangle-free global minimizers for arbitrarily large $n$. One finite counterexample, even a very large one, does not disprove the conjecture. Conversely, constructing one triangle-containing minimizer for every $n$ does not prove it, because the conjecture concerns **every** minimizer.

The disk formulation will be used throughout: the radius-$1/2$ disks centered at the points of $A$ have disjoint interiors, and

\[
\operatorname{diam}\left(\bigcup_{p\in A}B(p,1/2)\right)=D(n)+1.
\]

---

## 2. What the supplied literature proves

### 2.1 Exact small cases

Bateman and Erdős [2] establish

\[
D(2)=D(3)=1,\qquad D(4)=\sqrt2,
\]

\[
D(5)=\frac{1+\sqrt5}{2},\qquad D(6)=2\sin72^\circ,
\]

and prove

\[
D(7)=2,
\]

with the unique $n=7$ minimizer equal to a regular unit hexagon together with its center.

Bezdek and Fodor [3, Theorem 1.1] prove

\[
D(8)=\frac1{2\sin(\pi/14)},
\]

and show that every minimizer has a regular unit heptagon as its convex hull; the eighth point is not uniquely determined.

The exact contact structures show nonmonotonicity:

- $n=4$: the unit square is triangle-free.
- $n=5$: the regular unit pentagon is triangle-free.
- $n=6$: the regular pentagon has circumradius \(1\), so the center-to-vertex contacts form \(K_{1,5}\); the configuration is triangle-free.
- $n=7$: the center and every pair of adjacent hexagon vertices form a unit equilateral triangle.
- $n=8$: taking the eighth point at the heptagon center gives contact graph $C_7$ plus an isolated vertex, hence a triangle-free minimizer.

These cases disprove every naive monotonicity principle.

### 2.2 Diameter bounds and normalization

Bondarenko, Hardin, and Saff [5] define

\[
D_2(n)=\min
\frac{\max_{i\ne j}|p_i-p_j|}{\min_{i\ne j}|p_i-p_j|},
\]

which is exactly the present $D(n)$ after normalizing the minimum distance to (1). With

\[
\Delta_2=\frac{\pi}{\sqrt{12}}=\frac{\pi}{2\sqrt3},
\]

their general Theorem 2 yields

\[
\sqrt{\frac n{\Delta_2}}-2\le D(n)\le\sqrt{\frac n{\Delta_2}}.
\tag{2.1}
\]

For the plane, however, Bezdek and Fodor give the sharper lower estimate in the introduction to [3]:

\[
\boxed{
\sqrt{\frac n{\Delta_2}}-1\le D(n)<\sqrt{\frac n{\Delta_2}}.
}
\tag{2.2}
\]

Indeed, Fejes Tóth's finite packing inequality gives

\[
\operatorname{area}\bigl(\operatorname{conv}A+B(0,1/2)\bigr)
\ge \frac{\sqrt3}{2}n.
\]

The parallel body has diameter $D(n)+1$, and the isodiametric inequality gives the lower half of (2.2). For the strict upper half, average the number of points of the unit triangular lattice in an open disk of radius $\frac12\sqrt{n/\Delta_2}$. The average over lattice translations is exactly $n$, so some translate contains at least $n$ lattice points; any finite subset of that open disk has diameter strictly smaller than its diameter. The same argument is recorded in Theorem 10.9.

This correction matters: several imported drafts used the weaker (-2) bound even when working specifically in the plane.

### 2.3 Nonlattice optimality

Schürmann [4, Theorem 9] includes the minimum-diameter packing function and proves that, for all sufficiently large $n$, extremal packings are nonlattice. His proof uses loose boundary edges and sequential movements of disks in a lattice packing.

This rules out an eventual classification by finite triangular-lattice patches. It does **not** imply that large minimizers are triangle-free, nor does it exclude a nonlattice configuration with a large triangular contact core.

### 2.4 Triangle-free penny graphs

Eppstein [6] proves:

1. Every triangle-free penny graph is (2)-degenerate [6, Theorem 1].
2. Every connected triangle-free penny graph containing a cycle has at least four non-articulation vertices of degree at most (2) [6, Lemma 2].
3. If $G$ is connected with graph diameter $d_G$, then

   \[
   |E(G)|\le2|V(G)|-d_G-2
   \tag{2.3}
   \]

   [6, Theorem 2].
4. For arbitrary $n$-vertex triangle-free penny graphs,

   \[
   |E(G)|
   \le
   2n-\frac12\sqrt{2\pi\sqrt3\,n}+O(1)
   \tag{2.4}
   \]

   [6, Theorem 4].

These results are exact graph-theoretic restrictions, but they do not alone imply geometric flexibility of a cable-strut framework.

### 2.5 Rigidity terminology

Bezdek, Bezdek, and Connelly [7] define tensegrity stresses with nonnegative coefficients on cables and nonpositive coefficients on struts. Their paper develops stability and infinitesimal-rigidity ideas for sphere packings.

One imported argument relied on an all-strut characterization quoted in Section 4 of [7] from another paper. Because the present project permits results actually proved in the supplied sources, the consolidated arguments below do not rely on that quotation. The needed pinned result is instead proved directly by elementary finite-dimensional cone duality.

---

## 3. Audit of the imported GPT arguments

The imported work contains several valuable results, but also some statements that require repair.

| Imported claim | Audit result | Treatment here |
|---|---|---|
| Regular unit $p$-gons are triangle-free strict local diameter minima for odd primes $p$ | Correct, modulo Euclidean congruence | Included as Proposition 13.1 |
| Pinned rigidity provides a stress strictly positive on every contact | The cited justification was unsafe for pinned frameworks and relied on a theorem merely quoted in [7] | Reproved directly from the zero expansive cone using cone duality |
| In the jammed branch every hull vertex is diametral | Correct; there is also a direct outward-flex proof | Included as Lemma 7.2 and Theorem 8.2 |
| A rigid triangle-free minimizer with forest contact graph has $n\le43$ | Correct after replacing “rigid” by the precisely defined zero-cone branch | Included as Corollary 9.2 |
| BHS gives the operative planar lower bound with (-2) | True but not sharp | Replaced by Bezdek-Fodor's planar (-1) bound |
| Every minimizer has an ordinary KKT stress | Correct; MFCQ has an explicit strict direction | Included with full proof |
| Positive contact-stress components must be boundary loaded | Correct | Included in Section 5 |
| A contact-minimal triangle-free minimizer has all non-diameter nonisolated vertices trapped by (3)-(5) contacts | Correct | Included in Section 6 |
| In the pinned zero-cone branch almost all faces are near-equilateral unit rhombi | Correct after direct rank proof | Included in Section 10 |
| One fixed KKT multiplier is nonnegative on the whole second-order critical cone | Not justified by MFCQ | Replaced by a direction-dependent multiplier theorem |
| An affine shear produces a negative second-order stress energy | False | The tensor identity makes the quadratic energy exactly zero |
| The pinned rank count may omit contacts joining two fixed vertices | Correct | Strengthened to $e^\circ\ge2(n-q)$ in Theorem 7.1 |
| The total rhombus angular excess is $O(\sqrt n)$ | Correct by the concavity chord bound | Included as Corollary 10.4 |
| The midpoint, quartic, annular-mass, and high-moment stress identities | Correct after direct algebraic verification | Included as Theorems 11.3--11.5 |
| A maximal-contact representative has every contact component diameter-anchored | Correct after handling coincident boundary circles | Included as Theorem 12.3 |
| The minimum- and maximum-contact normal forms can be partly combined | Correct only after freezing the original core and all original diameter endpoints | Included as Theorems 12.4--12.5; the remaining bridge forest is not silently declared jammed |
| Rhombus tracks are pseudolines and satisfy $R\le B^2/16$ | Correct after replacing an informal crossing-sign argument by the strict displacement-cone proof | Included as Theorem 10.6 |
| A two-direction rhombic core needs $\Omega(\sqrt R)$ non-hull supports | Correct with explicit simple-boundary and no-pinch hypotheses | Included as Theorem 10.12, with the one-rhombus and five-rhombus-cross classification at zero support |
| Boundary-pinned almost-equilateral rhombus meshes must contain a $60^\circ$ face | False | Proposition 10.10 gives total positive defect $8/s\to0$ with zero boundary-pinned cone |
| A triangle-free packing has a uniform density gap | False as a proposed principle | Explicit near-triangular perturbations and shell fillings disprove such a gap |
| Schürmann implies an eventual triangular or rhombic lattice structure | False | His theorem only excludes lattice extremizers |

The imported reports were therefore used as sources of candidate lemmas, not as authorities. Every theorem retained below is either quoted with its exact hypotheses from a supplied paper or reproved in this document.

### 3.1 Disposition of the latest strengthening

The outward hull-vertex flex, the degree-$\le2$ local motions, the effective row count $e^\circ$, the $n-O(\sqrt n)$ cyclomatic bound, the component estimates, and the angular-defect conversion are correct as stated after replacing the informal word “rigid” by the exact condition $\mathcal E_Q(A)=\{0\}$.

The virtual-work, midpoint, quartic, dispersion, annular-mass, and high-moment radius formulas are also correct; their constants were recomputed directly. Two proof repairs were made:

1. Full pinned rank follows directly from the zero expansive cone, so no rigidity theorem merely quoted in [7] is invoked.
2. A regular boundary translation can activate several coincident constraints. They need not be unique, but the corresponding new unit edges form a matching and therefore cannot create a triangle. This is the form proved in Theorem 12.3.

### 3.2 Audit of the bridge-forest and train-track strengthening

The later imported investigation was also treated as candidate mathematics rather than authority. Its main claims were checked against the definitions and retained in the following precise forms.

1. The proposed representative combination is valid after freezing the contact-minimal core and every original diameter endpoint throughout the construction. New unit contacts can be made one at a time and always join distinct current components, so they remain bridges. This gives Theorem 12.4, not the stronger and still unproved assertion that the entire final representative is pinned-jammed.
2. Contracting the frozen core leaves a forest. A direct row count, allowing several fixed roots in one component, gives the lower bound $u-r+c$ in Theorem 12.5. Thus the residual obstruction is quantitatively high-dimensional whenever more than boundary-order many vertices lie outside the core.
3. The train-track monotonicity, at-most-one-crossing theorem, triangle-free crossing graph, width inequality, and Cartesian determinant inequality all survive without a disk assumption; the disk hypothesis is used only for the Euler relation in Theorem 10.8 and related boundary classifications.
4. The fixed-two-direction support theorem is valid with the regularity hypotheses stated in Theorem 10.12. In particular, hole-boundary incidences and pinched boundaries cannot be silently ignored.
5. The apparent five-direction escape is geometrically real. Proposition 10.10 realizes the balanced $C_5$ blow-up by a unit-separated rhombic disk, so no large Cartesian block follows merely from a dense triangle-free track-crossing graph.

These audits narrow the two branches but do not close either one. The five-sector construction is not certified globally optimal. The 11-point sun following Proposition 10.10 is stronger as a local regression test but is proved not globally optimal by an explicit smaller-diameter lattice competitor.

---

## 4. Exact first-order KKT stress for every minimizer

Let

\[
A=\{p_1,\ldots,p_n\}
\]

be any minimizer, and put

\[
T=D(n)^2.
\]

Define the active contact and diameter sets

\[
C=\{ij:|p_i-p_j|=1\},\qquad
H=\{ij:|p_i-p_j|^2=T\}.
\]

### Theorem 4.1: normalized signed equilibrium stress

There exist multipliers

\[
\alpha_{ij}\ge0\quad(ij\in C),\qquad
\beta_{ij}\ge0\quad(ij\in H)
\]

such that

\[
\sum_{ij\in H}\beta_{ij}=1,
\tag{4.1}
\]

\[
\sum_{j:ij\in C}\alpha_{ij}(p_i-p_j)
=
\sum_{j:ij\in H}\beta_{ij}(p_i-p_j)
\qquad(i=1,\ldots,n),
\tag{4.2}
\]

\[
\sum_{ij\in C}\alpha_{ij}=T,
\tag{4.3}
\]

and

\[
\sum_{ij\in C}\alpha_{ij}
(p_i-p_j)(p_i-p_j)^{\mathsf T}
=
\sum_{ij\in H}\beta_{ij}
(p_i-p_j)(p_i-p_j)^{\mathsf T}.
\tag{4.4}
\]

Equivalently, if

\[
u_{ij}=p_i-p_j\quad(ij\in C),\qquad
w_{ij}=\frac{p_i-p_j}{D}\quad(ij\in H),
\]

then

\[
\boxed{
\sum_{ij\in C}\frac{\alpha_{ij}}{D^2}u_{ij}u_{ij}^{\mathsf T}
=
\sum_{ij\in H}\beta_{ij}w_{ij}w_{ij}^{\mathsf T}.
}
\tag{4.5}
\]

Both sides of (4.5) are convex combinations of rank-one projections.

#### Proof

Minimize $T$ in the variables $(p_1,\ldots,p_n,T)$ subject to

\[
g_{ij}=1-|p_i-p_j|^2\le0,
\qquad
h_{ij}=|p_i-p_j|^2-T\le0.
\]

MFCQ holds explicitly. At any feasible point take

\[
v_i=p_i,\qquad \tau=3T.
\]

For every active contact,

\[
Dg_{ij}(v)=-2|p_i-p_j|^2=-2<0,
\]

and for every active diameter constraint,

\[
Dh_{ij}(v,\tau)=2T-3T=-T<0.
\]

Thus ordinary KKT applies. The Lagrangian is

\[
L=T+
\sum_{ij}\alpha_{ij}(1-|p_i-p_j|^2)
+\sum_{ij}\beta_{ij}(|p_i-p_j|^2-T).
\]

Stationarity in $T$ gives (4.1), while stationarity in every $p_i$ gives (4.2).

Multiply (4.2) by $p_i^{\mathsf T}S$, sum over $i$, and let $S$ range over all symmetric $2\times2$ matrices. The two endpoint contributions of each edge combine, yielding (4.4). Taking $S=I$, using the active lengths, and then using (4.1) gives (4.3). Dividing (4.4) by $D^2$ gives (4.5). ∎

With the sign convention of [7], the coefficients

\[
\omega_{ij}=-\alpha_{ij}\quad(ij\in C),\qquad
\omega_{ij}=+\beta_{ij}\quad(ij\in H)
\]

form a proper mixed cable-strut equilibrium stress.

---

## 5. Consequences for the positive stress support

Let

\[
C_+=\{ij\in C:\alpha_{ij}>0\},\qquad
H_+=\{ij\in H:\beta_{ij}>0\},
\]

and let $B_+$ be the vertex set of $H_+$.

### Lemma 5.1: diameter endpoints are extreme

Every endpoint of a diameter pair is a vertex of $\operatorname{conv}A$.

#### Proof

If $p_i=\sum_k\lambda_kx_k$ were a nontrivial convex combination and $|p_i-p_j|=D$, then

\[
D=|p_i-p_j|
\le\sum_k\lambda_k|x_k-p_j|
\le D.
\]

Equality in the Euclidean triangle inequality would force all vectors $x_k-p_j$ occurring with positive coefficient to be the same length-$D$ vector, contradicting nontriviality. ∎

### Lemma 5.2: positive diameter load requires positive contact load

Every vertex in $B_+$ is incident to an edge of $C_+$.

#### Proof

Otherwise (4.2) would express the extreme point $p_i$ as a convex combination of its diameter partners. ∎

### Lemma 5.3: unloaded stress vertices are contact barycenters

If $p_i\notin B_+$ but is incident to positive contact stress, then

\[
p_i=
\frac{\sum_j\alpha_{ij}p_j}{\sum_j\alpha_{ij}}.
\tag{5.1}
\]

Consequently, its $C_+$-degree cannot be (1). If its $C_+$-degree is (2), its two neighbors are exactly opposite unit contacts, the two stresses agree, and the neighbors are distance (2) apart.

### Proposition 5.4: every stressed contact component is boundary loaded twice

Every nontrivial connected component of $C_+$ contains at least two vertices incident to $H_+$.

#### Proof

If a component had no $H_+$-loaded vertex, choose a direction in which one of its vertices is uniquely extreme. The positive contact forces there all have strictly positive projection in that direction, contradicting equilibrium.

If a component had exactly one loaded vertex $p_i$, sum equilibrium over the component. Internal contact forces cancel, leaving

\[
\sum_j\beta_{ij}(p_i-p_j)=0.
\]

For any two diameter partners $p_j,p_k$,

\[
(p_i-p_j)\cdot(p_i-p_k)
=D^2-\frac{|p_j-p_k|^2}{2}
\ge\frac{D^2}{2}>0.
\]

A positive combination of these vectors cannot vanish. ∎

### Proposition 5.5: forest-supported stress

Let $m=|V(C_+)|$, let $c_+$ be the number of components of $C_+$, and let $L$ be the unloaded $C_+$-degree-(2) vertices. If $C_+$ is a forest, then

\[
m-|L|\le2|B_+|-2c_+\le2\pi D-2c_+.
\tag{5.2}
\]

Indeed, vertices in $B_+$ have degree at least (1), vertices in $L$ have degree (2), and all other vertices have degree at least (3). The forest degree sum gives the first inequality. Lemma 5.1, unit-separated hull sides, and Cauchy's perimeter-diameter inequality give

\[
|B_+|\le |V(\operatorname{conv}A)|
\le\operatorname{per}(\operatorname{conv}A)
\le\pi D.
\]

In particular, if $V(C_+)=A$, $L=\varnothing$, and $C_+$ is a forest, then

\[
n\le2\pi\sqrt{\frac n{\Delta_2}}-2c_+,
\]

which is impossible for \(n\ge44\).

### Proposition 5.6: cyclic stress components

If the full contact graph is triangle-free, every cyclic component of $C_+$ has at least four vertices in $B_+\cup L$.

This follows by applying Eppstein's Lemma 2 to that component and then using Lemma 5.3 at every low-degree vertex.

### Exact warning example: the unit square

For the unit square, put weight $\alpha=1/2$ on each of the four contact sides and weight $\beta=1/2$ on each of the two diameter diagonals. Then

\[
\sum\beta=1,
\qquad
\sum\alpha=2=D(4)^2,
\]

and equilibrium holds at every vertex. Thus triangle-free (2)-degeneracy, a normalized positive mixed stress, and exact global optimality are mutually compatible. Any argument asserting that a contact-degree-(2) vertex is automatically movable is already false at $n=4$: the diameter cables can supply the missing reactions.

These propositions explain the precise limitation of stress plus (2)-degeneracy: stress may travel through exact straight unit chains, and sparse boundary diameter forces may support a large interior network.

---

## 6. A contact-minimal normal form

Assume that, for a fixed $n$, at least one triangle-free minimizer exists. Among all triangle-free minimizers choose $A^*$ with the minimum number of unit contacts. Let

\[
Q=\{p_i:\exists j,\ |p_i-p_j|=D(n)\}
\]

be the full set of diameter endpoints.

### Theorem 6.1: local trapping after contact minimization

For $A^*$:

1. Every non-diameter, nonisolated vertex is strictly surrounded by its unit contacts: its contact vectors positively span $\mathbb R^2$.
2. Every such vertex has contact degree (3), (4), or (5).
3. Every nonisolated contact vertex of degree (1) or (2) belongs to $Q$.

#### Proof

Let $p_i\notin Q$ have at least one contact. If its contact vectors do not positively span the plane, finite-dimensional separation gives a nonzero vector $w$ satisfying

\[
(p_i-p_j)\cdot w\ge0
\]

for every contact $ij$. Move only $p_i$:

\[
p_i(t)=p_i+tw.
\]

For every old contact,

\[
|p_i(t)-p_j|^2
=1+2t(p_i-p_j)\cdot w+t^2|w|^2>1.
\tag{6.1}
\]

The quadratic term handles two exactly opposite contacts: a perpendicular motion has zero first derivative but strictly increases both lengths.

All noncontacts involving $p_i$ have positive slack above (1), and because $p_i\notin Q$, all its distances have positive slack below $D$. Hence, for sufficiently small $t>0$, feasibility and diameter $D$ are preserved while every contact at $p_i$ is broken.

If another contact remains elsewhere, this contradicts contact minimality. If no contact remains, the new minimum distance is $>1$, and rescaling produces diameter $<D(n)$, contradicting global optimality. Thus the contact vectors positively span the plane.

Positive spanning requires at least three directions. Triangle-freeness gives at most five unit neighbors, because equality in a $60^\circ$ angular gap would make a unit triangle, while six gaps strictly larger than $60^\circ$ cannot fit around $360^\circ$. ∎

### Corollary 6.2: boundary count

Every diameter endpoint is a convex-hull vertex, and

\[
|Q|\le\pi D(n)
\le
\sqrt{2\pi\sqrt3}\,\sqrt n.
\tag{6.2}
\]

Write

\[
C_0:=\sqrt{2\pi\sqrt3}=3.298908\ldots.
\]

Then $|Q|\le C_0\sqrt n$.

### Corollary 6.3: tree components

If $T$ is a nontrivial tree contact component and

\[
b_T=|Q\cap V(T)|,
\]

then

\[
|V(T)|\le2b_T-2.
\tag{6.3}
\]

Therefore all nontrivial tree components together contain $O(\sqrt n)$ vertices.

### Corollary 6.4: cyclic components

Every cyclic contact component contains at least four vertices of $Q$. Thus there are at most $|Q|/4=O(\sqrt n)$ cyclic components.

### Corollary 6.5: cyclomatic number

Let $z$ be the number of contact-isolated vertices, $m=n-z$, $e$ the number of contact edges, and $c_*$ the number of nontrivial contact components. Then

\[
e\ge\frac32m-|Q|,
\]

and the cyclomatic number

\[
\kappa=e-m+c_*
\]

satisfies

\[
\boxed{
\kappa\ge\frac{n-z}{2}-C_0\sqrt n+c_*.
}
\tag{6.4}
\]

Thus a contact-minimal triangle-free counterexample is either rattler dominated or has a linear number of independent contact cycles anchored to only $O(\sqrt n)$ diameter vertices.

---

## 7. The pinned expansive-cone dichotomy

The strongest framework statement can be proved without invoking any external rigidity theorem.

For a triangle-free minimizer $A$, let $Q$ be all diameter endpoints and define

\[
\mathcal E_Q(A)=
\left\{
v=(v_i):
v_i=0\ (p_i\in Q),\quad
(p_i-p_j)\cdot(v_i-v_j)\ge0\ (ij\in C)
\right\}.
\tag{7.1}
\]

### Theorem 7.1: exact dichotomy

Exactly one of the following holds.

#### Flexible branch

If $\mathcal E_Q(A)\ne\{0\}$, then $A$ belongs to a nonconstant continuous family of noncongruent triangle-free global minimizers of diameter $D(n)$, with all points in $Q$ fixed.

#### First-order-jammed branch

If $\mathcal E_Q(A)=\{0\}$, let $e^\circ$ denote the number of contact edges that do not have both endpoints in $Q$. Then the reduced contact rigidity matrix has full column rank and

\[
\boxed{e^\circ\ge2(n-q).}
\tag{7.2}
\]

In particular, $e\ge2(n-q)$, where $q=|Q|$.

#### Proof

If $v\in\mathcal E_Q(A)\setminus\{0\}$, take the straight motion

\[
p_i(t)=p_i+tv_i.
\]

For each contact,

\[
|p_i(t)-p_j(t)|^2
=1+2t(p_i-p_j)\cdot(v_i-v_j)
+t^2|v_i-v_j|^2\ge1.
\]

Every active diameter pair has both endpoints fixed. All initially noncontact and nondiameter pairs have strict slack, so sufficiently small $t$ preserves feasibility, diameter $D$, and triangle-freeness. Because two distinct diameter endpoints are fixed, a nonzero continuous motion cannot be a nontrivial Euclidean congruence.

If the cone is zero, any vector in the kernel of the reduced contact rigidity matrix would belong to the cone together with its negative. Hence the kernel is zero and the matrix has rank $2(n-q)$. A contact joining two pinned vertices gives a zero row, so only the $e^\circ$ remaining rows can contribute to this rank. This proves (7.2). ∎

### Lemma 7.2: direct local witnesses for the flexible branch

The following statements hold for every minimizer $A$.

1. If a convex-hull vertex $p$ is not in $Q$, then $\mathcal E_Q(A)\ne\{0\}$.
2. If a vertex $p\notin Q$ has contact degree at most $2$, then $\mathcal E_Q(A)\ne\{0\}$.

Consequently, in the first-order-jammed triangle-free branch,

\[
\boxed{Q=V(\operatorname{conv}A)}
\tag{7.3}
\]

and every vertex outside $Q$ has contact degree $3$, $4$, or $5$. In particular, every contact-isolated vertex belongs to $Q$.

#### Proof

For the first statement, choose a strict supporting normal $u$ at the hull vertex $p$, so

\[
u\cdot(p-x)>0\qquad(x\in A\setminus\{p\}).
\]

Moving only $p$ with velocity $u$ strictly expands every incident contact. Because $p\notin Q$, all distances from $p$ have strict slack below $D$, while a diameter pair not using $p$ remains fixed. Thus this velocity lies in the pinned expansive cone and produces the same-diameter flex of Theorem 7.1. Lemma 5.1 gives the reverse inclusion $Q\subseteq V(\operatorname{conv}A)$, proving (7.3) in the zero-cone branch.

For the second statement, degree $0$ is immediate. At degree $1$, move $p$ perpendicular to its unique contact direction; that contact expands quadratically. At degree $2$, let $a,b$ be the two unit vectors from the neighbors toward $p$. If $a\ne-b$, the velocity $w=a+b$ satisfies

\[
a\cdot w=b\cdot w=1+a\cdot b>0.
\]

If $a=-b$, move perpendicular to them and both contacts expand quadratically. Since $p\notin Q$, all upper constraints incident to it have slack. Triangle-freeness supplies the upper degree bound $5$. ∎

### Corollary 7.3: cycle count and size of the diameter boundary

Let $c$ be the number of contact-graph components and

\[
\kappa=e-n+c
\]

its cyclomatic number. In the first-order-jammed branch,

\[
\boxed{
\kappa\ge n-2q+c
\ge n-2\sqrt{2\pi\sqrt3}\,\sqrt n+1.
}
\tag{7.4}
\]

Thus

\[
\kappa\ge n-6.597816\ldots\sqrt n+1,
\]

and in particular $\kappa=n-O(\sqrt n)$.

Eppstein's bound (2.4) and (7.2) imply

\[
q\ge\frac14\sqrt{2\pi\sqrt3\,n}-O(1)
=0.824727\ldots\sqrt n-O(1).
\tag{7.5}
\]

Together with (6.2),

\[
q=\Theta(\sqrt n),\qquad e=2n-\Theta(\sqrt n).
\tag{7.6}
\]

If the contact graph is connected, (2.3) yields

\[
q\ge\frac{d_G+2}{2}
\ge\frac{D(n)+2}{2}
\ge\frac12\left(\sqrt{\frac n{\Delta_2}}+1\right),
\tag{7.7}
\]

where the last step uses the sharper planar lower bound (2.2).

---

## 8. Strict pinned stress and interior trapping

Lemma 7.2 already identifies the hull geometrically. Cone duality gives additional exact information: every unpinned vertex is strictly trapped by a positive stress on every incident contact. This replaces the imported reliance on an all-strut theorem that is only quoted, not proved, in [7].

### Lemma 8.1: strict positive dependence from a zero expansive cone

Let $R$ be a real matrix. If

\[
\{x:Rx\ge0\}=\{0\},
\tag{8.1}
\]

then $R$ has full column rank and there exists a vector $c$ with every coordinate strictly positive such that

\[
R^{\mathsf T}c=0.
\tag{8.2}
\]

#### Proof

The kernel is zero because both $x$ and $-x$ satisfy $Rx=0$. Let $r_1,\ldots,r_e$ be the rows. Condition (8.1) says that the dual cone of $\operatorname{pos}\{r_1,\ldots,r_e\}$ is ${0}$, hence the positive hull of the rows is the full column space.

For every nonzero row $r_i$, express $-r_i$ as a nonnegative combination of the rows. This produces a nonnegative linear dependence with a positive coefficient on $r_i$. Summing these dependences over $i$, and assigning arbitrary positive coefficients to any zero rows, gives (8.2) with $c_i>0$ for every $i$. ∎

### Theorem 8.2: strict positive pinned stress and local trapping

Assume $\mathcal E_Q(A)=\{0\}$. Then:

1. Every contact edge admits a strictly positive pinned equilibrium stress.
2. At every unpinned vertex $p_i\notin Q$,

   \[
   \sum_{j\sim i}c_{ij}(p_j-p_i)=0,
   \qquad c_{ij}>0.
   \tag{8.3}
   \]

3. The contact neighbors of every unpinned vertex affinely span the plane.
4. Every unpinned vertex lies in the strict interior of the convex hull of its contact neighbors and has contact degree at least (3).
5. The diameter endpoints are exactly the convex-hull vertices:

   \[
   \boxed{Q=V(\operatorname{conv}A).}
   \tag{8.4}
   \]

#### Proof

Apply Lemma 8.1 to the reduced contact rigidity matrix whose columns correspond to unpinned coordinates. Equation (8.2) is exactly (8.3). It first places $p_i$ in the affine hull of its contact neighbors. If those neighbors failed to span the plane, they and $p_i$ would lie on one line, and moving only $p_i$ perpendicular to that line would give a nonzero vector in the kernel of the reduced matrix, contrary to full column rank. Thus the neighbors affinely span the plane, and the positive equilibrium relation makes $p_i$ a strict convex combination of them.

No equilibrium equation is asserted at a pinned vertex; the missing force there is the pin reaction. Contacts joining two pinned vertices give zero rows in the reduced matrix and may be assigned arbitrary positive coefficients without affecting the unpinned equations.

An unpinned point therefore cannot be extreme in $\operatorname{conv}A$. Hence every hull vertex lies in $Q$. Lemma 5.1 gives the reverse inclusion, consistently with the direct proof in Lemma 7.2. ∎

Under the triangle-free hypothesis, every unpinned vertex consequently has degree (3), (4), or (5).

This theorem is stronger than the earlier estimate $Q\subseteq V(\operatorname{conv}A)$: in the first-order-jammed branch, **all** hull vertices are diameter endpoints.

---

## 9. The forest exclusion and boundary anchoring

### Proposition 9.1: component anchoring in every jammed counterexample

In the first-order-jammed triangle-free branch:

1. If $T$ is a nontrivial tree contact component with $n_T$ vertices and $q_T=|Q\cap V(T)|$, then

   \[
   \boxed{n_T\le2q_T-2.}
   \tag{9.1}
   \]

2. All nontrivial tree components together contain at most $2q=O(\sqrt n)$ vertices.
3. Every cyclic contact component contains at least four diameter endpoints.
4. Every isolated contact vertex is a diameter endpoint.

#### Proof

Every non-$Q$ vertex has degree at least $3$ by Lemma 7.2, while every vertex of a nontrivial tree has degree at least $1$. Therefore

\[
2(n_T-1)
=\sum_{v\in T}\deg v
\ge3(n_T-q_T)+q_T,
\]

which gives (9.1). Sum over the tree components. For a cyclic component, Eppstein's Lemma 2 supplies four non-articulation vertices of degree at most $2$; Lemma 7.2 puts all four in $Q$. Its degree-$0$ case also proves the last assertion. ∎

### Corollary 9.2: no forest for $n\ge44$

If $A$ is a triangle-free minimizer in the first-order-jammed branch and $n\ge44$, then its contact graph is not a forest.

#### Proof

Let $h=|Q|$, which equals the number of hull vertices by (8.4). Let $U$ be the unpinned vertices, $Q'\subseteq Q$ the nonisolated pinned vertices, and $c$ the number of nontrivial forest components.

Every vertex in $U$ has degree at least (3), and every vertex in $Q'$ has degree at least (1). Since a forest on $|U|+|Q'|$ nonisolated vertices with $c$ components has $|U|+|Q'|-c$ edges,

\[
2(|U|+|Q'|-c)
\ge3|U|+|Q'|.
\]

Thus

\[
|U|\le|Q'|-2c,
\]

and therefore

\[
n=|U|+h\le2h.
\tag{9.2}
\]

Every hull side has length at least (1), while Cauchy's inequality gives

\[
h\le\operatorname{per}(\operatorname{conv}A)
\le\pi D(n).
\]

Using the upper bound in (2.2),

\[
n\le2\pi\sqrt{\frac n{\Delta_2}},
\]

so

\[
n\le\frac{4\pi^2}{\Delta_2}=8\pi\sqrt3=43.531\ldots.
\]

Hence $n\ge44$ is impossible. ∎

### Corollary 9.3: four low-degree diametral hull vertices

For $n\ge44$, every triangle-free minimizer in the first-order-jammed branch has a cyclic contact component. Eppstein's Lemma 2 supplies at least four non-articulation vertices of contact degree at most (2) in that component. Lemma 7.2 forces all four to be diameter endpoints on the convex hull.

Thus a hypothetical large jammed counterexample must simultaneously have:

- every hull vertex diametral;
- every interior vertex strictly surrounded by at least three contacts;
- at least four hull vertices of contact degree at most (2); and
- $\Theta(\sqrt n)$ hull/diameter vertices in total.

---

## 10. The almost-rhombic structure theorem

Continue in the triangle-free first-order-jammed branch. Let $e$ be the number of contact edges, $c$ the number of contact-graph components, and $k$ the number of edge incidences with the unbounded face.

Euler's formula gives the number of bounded faces:

\[
f_b=e-n+c.
\tag{10.1}
\]

Every bounded face has length at least (4). Define its total excess over quadrilateral length by

\[
X=\sum_{F\text{ bounded}}(|\partial F|-4).
\]

Counting edge-face incidences gives

\[
X=2e-k-4f_b=4n-2e-k-4c.
\tag{10.2}
\]

Using $e\ge2(n-q)$,

\[
0\le X\le4q-k-4c\le4q.
\tag{10.3}
\]

Let $F_4$ be the number of bounded faces of length (4). Since every other bounded face contributes at least (1) to $X$,

\[
F_4\ge f_b-X
=3e-5n+k+5c
\ge n-6q+k+5c.
\tag{10.4}
\]

In particular,

\[
F_4=n-O(\sqrt n).
\tag{10.5}
\]

### Lemma 10.1: geometry of a four-face

Every bounded four-face is a simple unit rhombus. If $\theta_F\in(0,\pi/2]$ is its acute angle, then

\[
\boxed{
\frac\pi3<\theta_F\le\frac\pi2.
}
\tag{10.6}
\]

Indeed, the short diagonal has length $2\sin(\theta_F/2)\ge1$. Equality would add the short diagonal as a unit contact and form unit equilateral triangles. Therefore equality is forbidden in a triangle-free contact graph.

The face area is

\[
\operatorname{area}(F)=\sin\theta_F>\frac{\sqrt3}{2}.
\tag{10.7}
\]

### Theorem 10.2: total rhombus defect

Define

\[
\eta_F=\sin\theta_F-\frac{\sqrt3}{2}>0.
\]

Then

\[
\boxed{
\sum_{F\in\mathcal F_4}\eta_F
\le
\frac{\sqrt3}{2}(n-F_4)
\le
\frac{\sqrt3}{2}(6q-k-5c).
}
\tag{10.8}
\]

#### Proof

The bounded contact faces have disjoint interiors and lie in $\operatorname{conv}A$. Therefore

\[
\sum_{F\in\mathcal F_4}\operatorname{area}(F)
\le\operatorname{area}(\operatorname{conv}A).
\]

The isodiametric inequality and the BHS upper bound give

\[
\operatorname{area}(\operatorname{conv}A)
\le\frac{\pi D^2}{4}
\le\frac\pi4\frac n{\Delta_2}
=\frac{\sqrt3}{2}n.
\]

Substitute (10.7) and then use (10.4). ∎

### Corollary 10.3: almost every rhombus is nearly equilateral

For fixed $0<\varepsilon\le\pi/6$, the number $N_\varepsilon$ of four-faces satisfying

\[
\theta_F\ge\frac\pi3+\varepsilon
\]

obeys

\[
N_\varepsilon
\le
\frac{(\sqrt3/2)(6q-k-5c)}
{\sin(\pi/3+\varepsilon)-\sqrt3/2}
=O_\varepsilon(\sqrt n).
\tag{10.9}
\]

Hence all but $O_\varepsilon(\sqrt n)$ bounded faces have acute angle in

\[
60^\circ<\theta_F<60^\circ+\varepsilon.
\]

### Corollary 10.4: total angular excess is boundary order

Put

\[
\delta_F=\theta_F-\frac\pi3\in(0,\pi/6].
\]

The concave function

\[
f(\delta)=\sin\left(\frac\pi3+\delta\right)-\frac{\sqrt3}{2}
\]

lies above the chord joining its endpoint values on $[0,\pi/6]$. Hence

\[
f(\delta)
\ge
\frac6\pi\left(1-\frac{\sqrt3}{2}\right)\delta.
\]

Together with (10.8), this gives the explicit estimate

\[
\boxed{
\sum_{F\in\mathcal F_4}
\left(\theta_F-\frac\pi3\right)
\le
\frac{\pi\sqrt3}{12(1-\sqrt3/2)}(6q-k-5c)
=O(\sqrt n).
}
\tag{10.10}
\]

Since $F_4=n-O(\sqrt n)$, the mean angular excess is $O(n^{-1/2})$.

### Corollary 10.5: almost every vertex has degree four

Only $O(q)$ vertices are isolated, lie on the unbounded contact face, or are incident to a nonquadrilateral bounded face. Every other vertex is surrounded by rhombi whose angles lie strictly between $60^\circ$ and $120^\circ$, so its degree is (4) or (5).

Moreover,

\[
0\le\sum_v(4-\deg v)=4n-2e\le4q.
\]

The left inequality follows, for example, from Eppstein's (2)-degeneracy bound $e\le2n-3$ on every nonempty graph with at least two vertices. Let $E_0$ be the exceptional vertex set and let $N_5$ count the nonexceptional degree-(5) vertices. The nonexceptional vertices have degree (4) or (5), while triangle-freeness gives degree at most (5) everywhere. Hence

\[
0\le \sum_{v\in E_0}(4-\deg v)-N_5
\le 4|E_0|-N_5,
\]

so $N_5\le4|E_0|=O(q)$. Consequently,

\[
\boxed{
\text{all but }O(\sqrt n)\text{ vertices have degree }4
\text{ and are incident only with unit-rhombus faces.}
}
\tag{10.11}
\]

For each fixed $\varepsilon>0$, excluding also the vertices incident to the $O_\varepsilon(\sqrt n)$ exceptional rhombi in Corollary 10.3 shows that all but $O_\varepsilon(\sqrt n)$ vertices are surrounded by rhombi whose acute angles lie between $60^\circ$ and $60^\circ+\varepsilon$.

The estimate remains asymptotic. It does not force any exact equality $\theta_F=60^\circ$.

### Theorem 10.6: exact train-track bounds

Let $\mathcal R$ be any finite collection of the bounded four-faces from Lemma 10.1, regarded as an edge-to-edge rhombic complex. It may be disconnected and may have holes. Write

\[
R=|\mathcal R|
\]

and let $B_{\mathcal R}$ be the number of contact edges incident to exactly one face of $\mathcal R$.

Declare opposite edges of a rhombus equivalent and take the transitive closure. The resulting equivalence classes are the **train tracks** of $\mathcal R$. If $T$ is their number, then

\[
\boxed{
B_{\mathcal R}=2T,
\qquad
R\le \frac{T^2}{4}=\frac{B_{\mathcal R}^2}{16}.
}
\tag{10.12}
\]

Consequently,

\[
\boxed{B_{\mathcal R}\ge4\sqrt R.}
\tag{10.13}
\]

#### Proof

All edges belonging to one track are parallel. Orient a unit vector $u$ along them and draw the track centerline by joining midpoints of opposite track edges across each rhombus. Orient this centerline so that

\[
h_u(x)=\det(u,x)
\]

increases. It increases strictly across every rhombus. At a shared edge the next rhombus lies on the other side, so the same orientation continues. A track therefore cannot close or self-intersect. Since the complex is finite, it is a path with two boundary edges. Conversely, every boundary edge ends exactly one track. Hence $B_{\mathcal R}=2T$.

Two tracks can cross only in a rhombus, and they cross at most once. Here the strict angle bound is essential. Every directed segment of the $u$-track has angle from $u$ in

\[
\left(\frac\pi3,\frac{2\pi}3\right).
\tag{10.14}
\]

Therefore every forward displacement along it belongs to the open convex cone $C_u$ with that angular interval. If a $v$-track crosses it, orient $v$ so that its direction at the crossing belongs to $C_u$, and write $\phi=\arg_u v$. Then

\[
\frac\pi3<\phi<\frac{2\pi}3,
\]

while the forward-displacement cone of the $v$-track has angular interval

\[
\left(\phi+\frac\pi3,\phi+\frac{2\pi}3\right).
\]

This interval is disjoint from both $C_u$ and $-C_u$. If the tracks crossed at two points $P,Q$, label them so that $Q-P$ is a forward displacement on the $v$-track. According to their order on the $u$-track, the same vector would lie in $C_u$ or $-C_u$, a contradiction. This argument does not use simple connectedness.

Form the graph whose vertices are tracks and whose edges are their crossings. It is simple by the preceding paragraph. It is triangle-free: three pairwise crossing tracks would give three points on the projective direction circle, of circumference $\pi$, whose three pairwise circular separations were all strictly greater than $\pi/3$. The three circular gaps cannot then sum to $\pi$.

Mantel's inequality gives at most $T^2/4$ crossing pairs. Every rhombus is one crossing, proving (10.12) and (10.13). ∎

### Corollary 10.7: almost every track enters the defect network

Return to the jammed hypotheses, and take $\mathcal R=\mathcal F_4$. Let $h_{\mathcal R}$ count its boundary edges lying on $\partial\operatorname{conv}A$, and put

\[
b_{\mathcal R}=B_{\mathcal R}-h_{\mathcal R}.
\]

At most two train tracks have both end edges on the convex hull. Therefore

\[
\boxed{
b_{\mathcal R}
\ge \frac{B_{\mathcal R}}2-2
\ge2\sqrt{F_4}-2
=2\sqrt n-O(1).
}
\tag{10.15}
\]

Also $h_{\mathcal R}\le q$, and hence

\[
b_{\mathcal R}\ge4\sqrt{F_4}-q.
\tag{10.16}
\]

Every edge counted by $b_{\mathcal R}$ either borders a bounded nonquadrilateral face or lies on a non-hull boundary component or indentation of the rhombic complex.

#### Proof

Theorem 8.2 makes every point of $A$ on the convex hull an extreme vertex, so directed hull-edge angles turn strictly. A directed track centerline enters the rhombic complex through one end edge and leaves through the other; the two parallel end edges consequently have opposite induced boundary orientations. Strict turning also means that two different hull-to-hull tracks cannot use the same unoriented direction. Thus the end edges of any two such tracks alternate in the cyclic hull order. Their centerlines are arcs in the convex disk with alternating endpoints and must cross. The crossing graph induced by hull-to-hull tracks is therefore complete; Theorem 10.6 makes it triangle-free, so it has at most two vertices.

Every remaining track supplies at least one non-hull end edge. This proves (10.15). A hull contact edge joins consecutive hull vertices, so there are at most $q$ such edges; (10.13) now gives (10.16). ∎

There is also an exact convex exception theorem. If the closed strict rhombi tile a convex polygon and every boundary vertex is extreme, then every track is hull-to-hull, so the preceding proof leaves two tracks and one crossing: the complex is one rhombus. Under the jammed hypotheses, if the rhombi tile all of $\operatorname{conv}A$, all four vertices of that rhombus belong to $Q$. A nonsquare rhombus has only the endpoints of its longer diagonal in $Q$, so the rhombus must be the unit square.

For comparison with the planar excess variables, if $s$ is the number of bounded nonquadrilateral faces, then

\[
B_{\mathcal R}
\le k+\sum_{F\notin\mathcal R}|\partial F|
=k+4s+X
\le k+5X
\le20q-4k-20c.
\tag{10.17}
\]

Thus (10.15) is a real boundary-order demand, but the existing face-excess budget is still large enough to absorb it.

### Theorem 10.8: track width and exact angular-defect charge

Let

\[
D_{\mathcal R}=\operatorname{diam}V(\mathcal R),
\qquad
\chi_*=\frac{6-3\sqrt3}{\pi}.
\]

Then, with no connectedness or disk assumption,

\[
\boxed{
B_{\mathcal R}D_{\mathcal R}
\ge4\sum_{F\in\mathcal R}\sin\theta_F
\ge2\sqrt3R+4\chi_*\sum_{F\in\mathcal R}\delta_F.
}
\tag{10.18}
\]

If $\mathcal R$ is a topological disk and $v=|V(\mathcal R)|$, then

\[
v=R+\frac{B_{\mathcal R}}2+1
\]

and

\[
\boxed{
v\ge R+2\sqrt R+1=(\sqrt R+1)^2,
\qquad
R\le(\sqrt v-1)^2.
}
\tag{10.19}
\]

#### Proof

Across a rhombus $F$, the increase of the track coordinate $h_u$ in the proof of Theorem 10.6 is exactly $\sin\theta_F$. The two endpoint midpoints lie in $\operatorname{conv}V(\mathcal R)$, so every track $\tau$ satisfies

\[
\sum_{F\in\tau}\sin\theta_F\le D_{\mathcal R}.
\]

There are $B_{\mathcal R}/2$ tracks and every rhombus belongs to two of them. This proves the first inequality in (10.18). Concavity of sine on $[\pi/3,\pi/2]$ gives the chord estimate

\[
\sin\left(\frac\pi3+\delta\right)
\ge\frac{\sqrt3}{2}+\chi_*\delta,
\]

which proves the second.

For a disk quadrangulation, Euler and edge-face incidence counting give

\[
v-e+R=1,
\qquad
4R=2e-B_{\mathcal R}.
\]

Eliminate $e$ and use (10.13) to obtain (10.19). ∎

### Theorem 10.9: a global restriction on Cartesian train grids

Suppose a rhombic complex contains an additive $a\times b$ train-grid block with vertices

\[
p_{ij}=p+x_i+y_j,
\qquad
0\le i\le a,\qquad 0\le j\le b,
\]

where

\[
u_i=x_i-x_{i-1},\quad |u_i|=1,
\qquad
v_j=y_j-y_{j-1},\quad |v_j|=1,
\]

and all cell orientations are consistent:

\[
\det(u_i,v_j)=\sin\theta_{ij}>0.
\]

Here \(\theta_{ij}\) denotes the acute angle between the two edge directions, and
the coherent orientation hypothesis includes
\(\theta_{ij}\in(\pi/3,\pi/2]\) for every cell. The determinant condition by
itself is not enough: it also permits an obtuse oriented angle, for which the
chord estimate used below is not valid.

Then

\[
\boxed{
D_{\mathcal R}^2
\ge2\sum_{i=1}^a\sum_{j=1}^b\sin\theta_{ij}
\ge\sqrt3ab+2\chi_*\Delta_{a,b},
}
\tag{10.20}
\]

where $\Delta_{a,b}=\sum_{i,j}(\theta_{ij}-\pi/3)$. Moreover, for every $n$,

\[
\boxed{D(n)^2<\frac{2\sqrt3}{\pi}n.}
\tag{10.21}
\]

Consequently every such block in an $n$-point global minimizer obeys

\[
\boxed{
ab+\frac{4\sqrt3-6}{\pi}\Delta_{a,b}
<\frac2\pi n.
}
\tag{10.22}
\]

In particular $ab<2n/\pi$.

#### Proof

Put $U=\sum_i u_i$ and $V=\sum_jv_j$. The block contains

\[
p,\qquad p+U,\qquad p+V,\qquad p+U+V,
\]

and

\[
\det(U,V)=\sum_{i,j}\sin\theta_{ij}.
\]

Both $U+V$ and $U-V$ are differences of block vertices. Hence

\[
2|\det(U,V)|
=|\det(U+V,U-V)|
\le|U+V|\,|U-V|
\le D_{\mathcal R}^2.
\]

This proves (10.20).

For (10.21), average the number of points of the unit triangular lattice in an **open** radius-$r$ disk over translations modulo a fundamental cell. The average is

\[
\frac{\pi r^2}{\sqrt3/2}.
\]

Choose $r$ so that this average is $n$. Some translate contains at least $n$ lattice points. Any chosen $n$ of them form a finite subset of the open disk and therefore have diameter strictly less than $2r$. This proves (10.21). Combining it with (10.20), and using

\[
\frac{2\chi_*}{\sqrt3}=\frac{4\sqrt3-6}{\pi},
\]

gives (10.22). ∎

The additive block hypothesis is substantive. A dense triangle-free train-crossing graph need not contain a Cartesian block holding a comparable fraction of all its crossings.

### Proposition 10.10: a five-sector boundary-pinned countermodel

The local train-track, defect, stress, and pinned-jamming conclusions still do not use the decisive diametral-hull condition.

Fix $s\ge2$ and $0<\varepsilon<\pi/24$. Choose unit vectors $w_0,\ldots,w_4$ in counterclockwise order with successive oriented gaps

\[
\gamma_0=\gamma_1=\gamma_2=\gamma_3
=\frac\pi3+\varepsilon,
\qquad
\gamma_4=\frac{2\pi}3-4\varepsilon,
\]

where $w_5=w_0$. Define

\[
S_{s,\varepsilon}
=\bigcup_{i\in\mathbb Z/5\mathbb Z}
\left\{aw_i+bw_{i+1}:0\le a,b\le s, a,b\in\mathbb Z\right\}.
\tag{10.23}
\]

The five sector grids meet along their radial sides. Their union is an edge-to-edge disk complex with

\[
\boxed{
n=5s^2+5s+1,
\qquad
R=5s^2,
\qquad
B_{\mathcal R}=10s.
}
\tag{10.24}
\]

Its $T=5s$ tracks fall into five classes of size $s$, one for each direction $w_i$. Every track crosses precisely the tracks in the two adjacent direction classes. Thus the crossing graph is the balanced blow-up of $C_5$. Its largest complete bipartite subgraph contains only

\[
2s^2=\frac{2R}{5}
\]

crossings.

Four sectors have rhombus defect $\varepsilon$ and the fifth has defect $4\varepsilon$, so

\[
\boxed{
\sum_F\delta_F=8\varepsilon s^2.
}
\tag{10.25}
\]

The vertex set is unit-separated, its contact graph consists exactly of the grid edges, and it is triangle-free. All but $O(s)$ vertices have degree four, and its diameter is $O(s)=O(\sqrt n)$.

If every vertex on the boundary of this five-sector complex is pinned, its expansive cone is zero and it admits a stress positive on every contact edge. In particular, choosing

\[
\varepsilon_s=s^{-3}
\]

gives arbitrarily large, triangle-free, boundary-pinned jammed complexes with

\[
R=n-O(\sqrt n),
\qquad
\sum_F\delta_F=\frac8s=o(1).
\tag{10.26}
\]

#### Proof

Within one sector, the difference of two vertices is $aw_i+bw_{i+1}$ with integers $a,b$. Let $\gamma\in(\pi/3,2\pi/3)$ be the oriented angle between the two generators. If $ab\ge0$ and both coefficients are nonzero, the shortest case is their unit sum and has squared length $2+2\cos\gamma>1$. If $ab<0$ and $\cos\gamma>0$, writing $r=|a|$ and $t=|b|$ gives

\[
r^2+t^2-2rt\cos\gamma
=(r-t)^2+2rt(1-\cos\gamma)>1.
\]

The case $\cos\gamma\le0$ is immediate. Equality therefore occurs only for a coordinate unit vector.

For adjacent sectors, points off their shared radial ray lie on opposite sides of it, each at perpendicular distance at least $\sin(\pi/3)$; if one point lies on the ray, the same two-generator calculation applies. Two nonadjacent sector cones are separated by an angle $\alpha>\pi/3$. Their nonzero lattice points have norms $r,t\ge1$, and

\[
|x-y|^2=(r-t)^2+2rt(1-\cos\alpha)>1.
\]

This proves unit separation and identifies all contacts. The five sector cones have disjoint interiors, so their rhombi do not overlap. Gluing five $(s+1)\times(s+1)$ grids along their radial chains gives (10.24), and (10.25) is immediate.

Across a radial seam, the $s$ half-tracks of direction $w_i$ in its two adjacent sectors join pairwise. Hence there are exactly $s$ complete tracks in each of the five direction classes. A class-$i$ track crosses all $s$ tracks in classes $i-1$ and $i+1$ and no others. This proves the asserted balanced $C_5$ crossing graph. In a $C_5$ blow-up, a complete bipartite subgraph is maximized by taking one full class on one side and its two neighboring classes on the other, giving $2s^2$ crossings.

To see full rank after the outer boundary is pinned, first consider a contact-preserving infinitesimal motion. In each sector the vertex $(s-1)w_i+(s-1)w_{i+1}$ has two nonparallel contacts to pinned outer-side vertices, so its velocity is zero. The same two-direction argument fixes the rest of the layer $\max\{a,b\}=s-1$. Induction on the layers fixes the whole complex.

It remains to construct a positive pinned equilibrium stress. At the radial seam in direction $w_i$, the vector $w_i$ lies strictly inside the cone generated by $w_{i-1}$ and $w_{i+1}$, because

\[
\gamma_{i-1}+\gamma_i<\pi.
\]

Choose positive $a_i^-,a_i^+,\lambda_i$ such that

\[
a_i^-w_{i-1}+a_i^+w_{i+1}=\lambda_iw_i.
\tag{10.27}
\]

Give every off-seam grid line ending at that seam its corresponding weight $a_i^-$ or $a_i^+$. Opposite edges then cancel at every ordinary grid vertex. Give the radial edge from $rw_i$ to $(r+1)w_i$ weight $\rho_{i,r}$. At an internal seam vertex equilibrium is exactly

\[
\rho_{i,r-1}=\rho_{i,r}+\lambda_i.
\tag{10.28}
\]

Because the five rays surround the origin with every gap less than $\pi$, there are $d_i>0$ with $\sum_i d_iw_i=0$. Scale them until $d_i>s\lambda_i$, put $\rho_{i,0}=d_i$, and define $\rho_{i,r}=d_i-r\lambda_i$. All weights are positive, (10.28) holds, and the center is in equilibrium.

For an expansive velocity pinned on the boundary, multiply every contact inequality by this positive stress and sum. Interior equilibrium makes the sum zero, so every contact derivative is zero. The full-rank argument in the preceding paragraph then makes the velocity zero. ∎

There is also a useful exact finite regression test in which the pins really are the diameter endpoints. Let $w_0,\ldots,w_4$ be the five unit vectors at successive angles $2\pi/5$ and take

\[
S=\{0\}\cup\{w_i:0\le i<5\}
\cup\{w_i+w_{i+1}:0\le i<5\}.
\tag{10.27a}
\]

This is an 11-point, triangle-free union of five $72^\circ$ unit rhombi. Its five outer points $w_i+w_{i+1}$ form a regular pentagon, are exactly the convex-hull vertices, and every one is a diameter endpoint. Pinning only these five points gives zero expansive cone. Indeed, at each radial point $w_i$, its two contacts to the pinned hull have directions $w_{i-1}$ and $w_{i+1}$; a positive stress with weight (1) on those edges and weight $2\cos(2\pi/5)$ on the edge to the center is in equilibrium. The five center-edge forces sum to zero. Positivity turns every expansive derivative into an equality, the two nonparallel pinned contacts fix each $w_i$, and the radial contacts then fix the center.

For an exact distance check, put $\varphi=(1+\sqrt5)/2$ and $z_i=w_i+w_{i+1}$. Then $|z_i|=\varphi$, the inner pentagon has side length $2\sin(\pi/5)>1$, and every outer-pentagon side is also longer than (1). Rotational symmetry reduces the mixed distances to

\[
|z_j-w_i|^2=
\begin{cases}
1,&j-i\equiv0,-1\pmod5,\\[2mm]
(7+\sqrt5)/2,&j-i\equiv1,3\pmod5,\\[2mm]
(7+3\sqrt5)/2,&j-i\equiv2\pmod5.
\end{cases}
\]

Thus the displayed edges are exactly all unit contacts. The outer pentagon has inradius $\varphi^2/2>1$, so it contains the five $w_i$ strictly. Its diagonals are the unique longest distance class and have squared length $5+2\sqrt5$. This verifies the hull and diameter assertions.

Thus even the exact conditions $Q=V(\operatorname{conv}A)$, positive pinned stress, zero pinned cone, and strict rhombic faces do not force a $60^\circ$ face at finite size. Its diameter is

\[
\sqrt{5+2\sqrt5}>3,
\]

whereas the unit triangular lattice contains the following 12-point set of diameter (3):

\[
\{(a,b):
(a,b)\in
\{(0,1),(0,2),(0,3),(1,0),(1,1),(1,2),(1,3),
(2,0),(2,1),(2,2),(3,0),(3,1)\}\},
\tag{10.27b}
\]

where $(a,b)$ denotes $a(1,0)+b(1/2,\sqrt3/2)$. For every nonzero integer difference, $a^2+ab+b^2\ge1$, while a direct check of the finitely many displayed differences gives $a^2+ab+b^2\le9$, with equality for $(0,1)$ and $(3,1)$. Thus the set is unit-separated and has diameter (3). Any 11 of these points beat the sun. The sun is therefore an exact adversarial test of local arguments, not a candidate for Target C.

The large five-sector family is an exact warning. It defeats any proposed quantization of positive rhombus defect, any maximum principle based only on a pinned boundary, and any argument using only positive equilibrium stress. What that large family does **not** satisfy is Theorem 8.2: most pinned boundary points are nonextreme and nondiametral. The 11-point sun shows in turn that the diametral-hull condition alone is not a finite local contradiction. Global capacity, or an equivalent large-scale extremality input, remains indispensable.

### Corollary 10.11: the exact ideal-disk boundary budget

Suppose an $n$-point global minimizer is exactly the vertex set of a topological-disk rhombic complex $\mathcal R$. Put

\[
G=\operatorname{area}(\operatorname{conv}A)
-\sum_{F\in\mathcal R}\operatorname{area}(F),
\qquad
\Delta=\sum_F\delta_F.
\]

Then

\[
\boxed{
4G+4\chi_*\Delta
<\sqrt3B_{\mathcal R}+2\sqrt3.
}
\tag{10.29}
\]

Indeed, Theorem 10.8 gives $n=R+B_{\mathcal R}/2+1$, while (10.21), the isodiametric inequality, and the sine chord estimate give

\[
\frac{\sqrt3}{2}R+\chi_*\Delta+G
\le\operatorname{area}(\operatorname{conv}A)
<\frac{\sqrt3}{2}n.
\]

Thus a reverse boundary-shell inequality, with exact correction terms for exceptional faces, holes, components, and vertices outside the rhombic core, would eliminate the jammed branch. Proposition 10.10 proves that no such reverse inequality follows from strict defects, positive stress, and boundary-pinned jamming alone.

### Theorem 10.12: support cost and classification for two fixed directions

Let $\mathcal R$ be a connected finite unit-rhombus complex whose cell union has a simple outer boundary, with holes allowed but no pinched boundary vertices. Assume all edges use two fixed unoriented directions. Let $K_\partial$ consist of all hole-boundary incidences together with selected outer-boundary incidences only at vertices that are not vertices of $\operatorname{conv}V(\mathcal R)$, chosen so that:

1. every incidence on a hole boundary belongs to $K_\partial$; and
2. every outer-boundary vertex that is not a vertex of $\operatorname{conv}V(\mathcal R)$ and is uncharged admits a strictly positive equilibrium using only the incident edges of $\mathcal R$.

Thus any non-hull vertex that needs a contact outside $\mathcal R$ or another external reaction must be charged to $K_\partial$. Put $k=|K_\partial|$. Then

\[
\boxed{
R\le(k+3)^2,\qquad k\ge\sqrt R-3.
}
\tag{10.30}
\]

If $k=0$, there is a complete classification:

\[
\boxed{
\mathcal R\text{ is either one rhombus or the five-rhombus cross.}
}
\tag{10.31}
\]

#### Proof

Apply an invertible affine map carrying the two unit edge vectors to the coordinate vectors. The complex becomes a finite union of unit squares. Positive linear equilibrium and convexity are preserved.

At a locally convex outer-boundary vertex, all incident internal edge vectors lie in a closed half-plane and at least one points strictly inward, so no strictly positive combination can vanish. At a straight boundary vertex, the two tangent directions may cancel but every remaining internal edge points strictly inward. Hence every outer-boundary vertex outside $K_\partial$ is either a convex-hull vertex or a reflex vertex with all four coordinate edge directions present.

Consider the boundary path between two consecutive convex-hull vertices. If its interior contains no incidence from $K_\partial$, every internal turn is reflex. There can be at most two such turns: three consecutive right-angle reflex turns produce four successive unit coordinate vectors whose sum is zero, returning to the initial vertex before reaching the next hull vertex. The hull chord is therefore a sum of one, two, or three successive coordinate unit vectors. Its direction is one of

\[
\pm e_1,\quad\pm e_2,\quad
\pm(e_1+e_2),\quad\pm(e_1-e_2).
\tag{10.32}
\]

A convex polygon has at most one side in each of these eight oriented directions. If $q$ is its number of vertices and $k_{\rm out}$ is the number of charged outer-boundary incidences, at most eight of the $q$ gaps between consecutive hull vertices are uncharged. Therefore

\[
q\le k_{\rm out}+8.
\tag{10.33}
\]

Let $C,L,Z$ denote the numbers of convex, reflex, and straight incidences of the outer orthogonal boundary. Then

\[
C-L=4,\qquad
B_{\rm out}=C+L+Z=2C+Z-4.
\]

Write $C=q+C_K$, where $C_K$ counts the charged non-hull convex incidences. Since every straight incidence is also charged, (10.33) gives

\[
B_{\rm out}
\le12+2k_{\rm out}+2C_K+Z
\le12+4k_{\rm out}.
\]

All inner-boundary incidences are charged, and a simple orthogonal inner boundary has the same number of edge and vertex incidences. Consequently

\[
B_{\mathcal R}\le12+4k.
\tag{10.34}
\]

The tracks split into two straight families of sizes $m$ and $r$. Tracks in one family do not cross, and an opposite-family pair crosses at most once. Hence

\[
R\le mr
\le\frac{(m+r)^2}{4}
=\frac{B_{\mathcal R}^2}{16}
\le(k+3)^2,
\]

proving (10.30).

It remains to classify equality-free support, $k=0$. There are no holes or straight boundary vertices; every convex boundary vertex is a hull vertex and every other boundary vertex is reflex. Between consecutive convex turns let $r_i\in\{0,1,2\}$ be the number of reflex turns. Total turning and (10.33) give

\[
\sum_{i=1}^{C}(1-r_i)=4,\qquad 4\le C\le8.
\tag{10.35}
\]

This leaves a finite exact closure check. Start with $d_1=e_1$, let $J$ be a positive quarter-turn, and set

\[
d_{i+1}=J^{1-r_i}d_i,\qquad
s_i=\sum_{j=0}^{r_i}J^{-j}d_i.
\tag{10.36}
\]

Here $s_i$ is the hull chord between consecutive convex turns. Impose $\sum_i s_i=0$, no repeated proper partial sum of the individual unit steps, and strict consistent turning of the hull chords. Direct substitution of $r_i\in\{0,1,2\}$ gives, up to cyclic shift and reversal,

\[
\begin{array}{c|c|c}
C&\text{closed words}&\text{simple word with strict hull}\\ \hline
4&0000&0000\\
5&-&-\\
6&001001&-\\
7&-&-\\
8&00020002,\ 00101002,\ 00110011,\ 01010101
&01010101.
\end{array}
\]

The word $0000$ bounds one square. The alternating word bounds the plus-shaped union of a central square and its four edge-neighbors. Applying the inverse affine map proves (10.31). ∎

Thus a large two-direction oblique-lattice core cannot be supported only at its diametral hull vertices. An $R$-face core needs at least $\sqrt R-3$ non-hull interface supports. The general $O(\sqrt n)$ defect shell can pay this cost, so the theorem sharply constrains but does not eliminate the jammed branch.

---

## 11. Second-order and nonlinear stress identities

The ordinary KKT stress is not automatically a universal prestress-stability certificate. The correct necessary statement is direction dependent.

Let $v=(v_1,\ldots,v_n)$ satisfy the first-order critical inequalities with no first-order change in $T$:

\[
(p_i-p_j)\cdot(v_i-v_j)\ge0\quad(ij\in C),
\tag{11.1}
\]

\[
(p_i-p_j)\cdot(v_i-v_j)\le0\quad(ij\in H).
\tag{11.2}
\]

Let $C_0(v)$ and $H_0(v)$ be the active edges on which equality holds.

### Theorem 11.1: second-order normal stress for each critical direction

There exist multipliers

\[
\alpha_{ij}\ge0\quad(ij\in C_0(v)),\qquad
\beta_{ij}\ge0\quad(ij\in H_0(v))
\]

satisfying the equilibrium, scalar, and tensor identities (4.1)-(4.5), supported on the zero-derivative edges, and additionally

\[
\boxed{
\sum_{H_0(v)}\beta_{ij}|v_i-v_j|^2
-
\sum_{C_0(v)}\alpha_{ij}|v_i-v_j|^2
\ge0.
}
\tag{11.3}
\]

#### Proof

Suppose there were accelerations $a_i$ and $s<0$ such that

\[
p_i(t)=p_i+tv_i+\frac{t^2}{2}a_i,
\qquad
T(t)=T+\frac{t^2}{2}s
\]

strictly satisfy every second-order condition on the zero-derivative active edges. Those conditions are

\[
-2(p_i-p_j)\cdot(a_i-a_j)-2|v_i-v_j|^2<0
\quad(ij\in C_0(v)),
\tag{11.4}
\]

\[
2(p_i-p_j)\cdot(a_i-a_j)-s+2|v_i-v_j|^2<0
\quad(ij\in H_0(v)).
\tag{11.5}
\]

Edges with strict first-order slack remain feasible automatically for sufficiently small $t>0$, as do inactive constraints. Thus (11.4)-(11.5) with $s<0$ would produce a feasible configuration of smaller diameter, contradicting optimality.

The strict linear system in the variables $(a,s)$ is therefore infeasible. Apply the strict Farkas alternative also to the row $s<0$. It gives nonnegative multipliers $\alpha,\beta,\lambda$, not all zero, with stationarity in $(a,s)$, where stationarity in $s$ says

\[
\lambda=\sum\beta.
\]

If $\lambda=0$, then $\beta=0$ and the remaining equations would be a nonzero nonnegative equilibrium stress supported only on contacts. That is impossible for a finite free framework: choose a vertex uniquely extreme in a generic direction among the vertices incident to positive stress; every positive incident contact force has strictly positive projection there. Thus $\lambda>0$. Normalize it to (1), obtaining $\sum\beta=1$. The constant term in the Farkas alternative is precisely (11.3), and the scalar and tensor identities follow as in Theorem 4.1. ∎

### Corollary 11.2: affine second-order neutrality

For an affine velocity field

\[
v_i=Mp_i+b,
\]

write $r_{ij}=p_i-p_j$ on contacts and $R_{ij}=p_i-p_j$ on diameter edges. Then the quadratic stress expression is identically zero:

\[
\begin{aligned}
&\sum_H\beta_{ij}|M(p_i-p_j)|^2
-\sum_C\alpha_{ij}|M(p_i-p_j)|^2\\
&\qquad=
\operatorname{tr}\!\left(
M^{\mathsf T}M
\left[
\sum_H\beta_{ij}R_{ij}R_{ij}^{\mathsf T}
-\sum_C\alpha_{ij}r_{ij}r_{ij}^{\mathsf T}
\right]
\right)=0.
\end{aligned}
\tag{11.6}
\]

Thus the tensor identity blocks the hoped-for contradiction from a global affine shear. Also, the multiplier in Theorem 11.1 may depend on $v$; MFCQ alone does not justify one stress with nonnegative quadratic energy on the entire critical cone.

### Theorem 11.3: virtual work and the common stress midpoint

Fix any KKT stress from Theorem 4.1. For arbitrary vectors $\xi_i\in\mathbb R^2$, equilibrium gives the exact virtual-work identity

\[
\boxed{
\sum_{ij\in C}\alpha_{ij}(p_i-p_j)\cdot(\xi_i-\xi_j)
=
\sum_{ij\in H}\beta_{ij}(p_i-p_j)\cdot(\xi_i-\xi_j).
}
\tag{11.7}
\]

Let

\[
m_{ij}=\frac{p_i+p_j}{2},
\qquad
a_{ij}=\frac{\alpha_{ij}}{D^2}\quad(ij\in C).
\]

Both $(a_{ij})_{C}$ and $(\beta_{ij})_{H}$ are probability weights. Their midpoint barycenters agree:

\[
\boxed{
\sum_C a_{ij}m_{ij}
=
\sum_H\beta_{ij}m_{ij}
=:\mu.
}
\tag{11.8}
\]

In particular, $\mu\in\operatorname{conv}A$.

#### Proof

Dot the vertex equilibrium equation (4.2) with $\xi_i$ and sum over $i$; the two endpoint terms of every edge combine to give (11.7).

For a fixed vector $b$, choose

\[
\xi(x)=|x|^2b-2(b\cdot x)x.
\]

A direct calculation, with $d=x-y$, gives

\[
d\cdot\bigl(\xi(x)-\xi(y)\bigr)
=-|d|^2b\cdot(x+y).
\]

Use this field in (11.7), substitute the active lengths $1$ and $D$, and divide by $2D^2$. Since $b$ is arbitrary, (11.8) follows. ∎

### Theorem 11.4: quartic identity and macroscopic contact-stress mass

Write

\[
\bar m_{ij}=m_{ij}-\mu,
\qquad
u_{ij}=p_i-p_j\quad(ij\in C),
\qquad
w_{ij}=\frac{p_i-p_j}{D}\quad(ij\in H).
\]

Then

\[
\boxed{
\begin{aligned}
&\sum_C a_{ij}
\left[|\bar m_{ij}|^2+2(\bar m_{ij}\cdot u_{ij})^2\right]\\
&\quad-
\sum_H\beta_{ij}
\left[|\bar m_{ij}|^2+2(\bar m_{ij}\cdot w_{ij})^2\right]
=\frac{D^2-1}{4}.
\end{aligned}
}
\tag{11.9}
\]

Consequently,

\[
\boxed{
\sum_C a_{ij}|m_{ij}-\mu|^2
\ge\frac{D^2-1}{12}.
}
\tag{11.10}
\]

For $D>2$, the normalized contact-stress mass whose midpoint lies at distance at least $D/4$ from $\mu$ satisfies

\[
\boxed{
\sum_{\substack{ij\in C\\|m_{ij}-\mu|\ge D/4}}a_{ij}
\ge\frac{D^2-4}{45D^2}.
}
\tag{11.11}
\]

Equivalently, the corresponding unnormalized $\alpha$-mass is at least $(D^2-4)/45$, which is $\Theta(n)$ along any sequence with $n\to\infty$ by (2.2).

#### Proof

Translate the origin to $\mu$ and use $\xi(x)=|x|^2x$ in (11.7). For $d=x-y$ and $m=(x+y)/2$,

\[
d\cdot\bigl(|x|^2x-|y|^2y\bigr)
=|m|^2|d|^2+\frac{|d|^4}{4}+2(m\cdot d)^2.
\]

Insert the contact and diameter lengths, divide by $D^2$, and use $\sum_Ca=\sum_H\beta=1$ to obtain (11.9). The diameter sum in (11.9) is nonnegative, while

\[
|m|^2+2(m\cdot u)^2\le3|m|^2,
\]

which proves (11.10).

Every midpoint and $\mu$ lie in $\operatorname{conv}A$, whose diameter is $D$, so $|m_{ij}-\mu|\le D$. If $s$ denotes the left side of (11.11), then

\[
\sum_Ca_{ij}|m_{ij}-\mu|^2
\le (1-s)\frac{D^2}{16}+sD^2.
\]

Combine this with (11.10) and solve for $s$ to get (11.11). ∎

### Theorem 11.5: positive contact stress reaches radius $(D-1)/2$

For every normalized KKT certificate,

\[
\boxed{
\max_{\alpha_{ij}>0}|m_{ij}-\mu|
\ge\frac{D-1}{2}.
}
\tag{11.12}
\]

#### Proof

Translate again so $\mu=0$. For an integer $k\ge1$, put

\[
\xi_k(x)=|x|^{2k}x
=\nabla\left(\frac{|x|^{2k+2}}{2k+2}\right).
\]

Its Jacobian, equivalently the Hessian of the displayed convex function, is

\[
H_k(x)=|x|^{2k}I+2k|x|^{2k-2}xx^{\mathsf T}.
\]

For a segment $[x,y]$ of length $L$, unit direction $u$, and midpoint $m$, define its normalized work

\[
W_k(x,y)
=\frac{(x-y)\cdot(\xi_k(x)-\xi_k(y))}{L^2}
=\frac1L\int_{-L/2}^{L/2}u^{\mathsf T}H_k(m+tu)u\,dt.
\]

For a diameter segment, write $m\cdot u=s_0$. Since

\[
u^{\mathsf T}H_k(z)u
\ge(2k+1)|z\cdot u|^{2k},
\]

and the integral of $|s_0+t|^{2k}$ over an interval of fixed length is minimized when $s_0=0$,

\[
W_k(x,y)\ge\left(\frac D2\right)^{2k}
\qquad(ij\in H).
\tag{11.13}
\]

Let

\[
R=\max_{\alpha_{ij}>0}|m_{ij}|.
\]

Every point on a positively stressed unit contact lies within distance $R+1/2$ of the origin. The largest eigenvalue of $H_k(z)$ is $(2k+1)|z|^{2k}$, so

\[
W_k(x,y)\le(2k+1)(R+1/2)^{2k}
\qquad(ij\in C,\ \alpha_{ij}>0).
\tag{11.14}
\]

Apply (11.7) with $\xi_i=\xi_k(p_i)$ and divide by $D^2$. It becomes

\[
\sum_Ca_{ij}W_k(p_i,p_j)
=\sum_H\beta_{ij}W_k(p_i,p_j).
\]

Equations (11.13)--(11.14) give

\[
(2k+1)(R+1/2)^{2k}
\ge(D/2)^{2k}.
\]

Let $k\to\infty$ to obtain $R+1/2\ge D/2$, proving (11.12). ∎

---

## 12. Rattlers and canonical representatives

### Theorem 12.1: every isolated point can be attached

Let $A$ be a triangle-free minimizer and let $p\in A$ be contact-isolated. Then $p$ can be moved, without increasing the diameter or creating a unit triangle, until it has exactly one unit contact. Repeating this process gives a triangle-free minimizer with the same $n$ and $D(n)$ and no contact-isolated points.

#### Proof

For $n\ge4$, a diameter minimizer is noncollinear: a collinear feasible $n$-point set has diameter at least $n-1$, whereas the regular unit $n$-gon has strictly smaller diameter. The smaller cases have no isolated point. Thus the convex hull below has nonempty interior.

Work inside the convex polygon $K=\operatorname{conv}A$. Every point $y\in K$ satisfies

\[
|y-x|\le D\qquad(x\in A\setminus\{p\})
\]

by convexity of the distance function. Starting from $p$, choose a path in $K$ toward one of the existing points. It must meet the boundary of the forbidden union

\[
\bigcup_{x\in A\setminus\{p\}}B(x,1).
\]

The finitely many points at which two of the boundary circles meet can be avoided by a generic small perturbation of the path. Stop at its first boundary point. Exactly one distance is then (1), every other lower-distance constraint is still strict, and every upper-distance constraint is at most $D$. Thus no unit triangle is created.

The resulting diameter is at most $D$. If it were smaller than $D(n)$, global optimality would be contradicted. Hence it remains exactly $D(n)$. ∎

This theorem does **not** imply that a no-isolate representative can simultaneously be chosen contact-minimal or first-order jammed. The exact $n=8$ family warns against such a simultaneous normalization.

### Theorem 12.2: structure of a minimum-contact core

Choose a triangle-free minimizer with the minimum possible number of contacts. Delete its isolated vertices, leaving a nonisolated core with $m$ vertices. Let $Q^\circ$ be the diameter endpoints belonging to that core.

Then:

1. Every nontrivial contact component meets $Q^\circ$.
2. Fixing $Q^\circ$, the expansive cone of the core is zero.
3. If the core has $e$ contact edges, then

   \[
   e\ge2(m-|Q^\circ|).
   \tag{12.1}
   \]

4. Under triangle-freeness,

   \[
   |Q^\circ|
   \ge\frac14\sqrt{2\pi\sqrt3\,m}-O(1).
   \tag{12.2}
   \]

#### Proof

If a nontrivial contact component contains no diameter endpoint, give every vertex $p_i$ in that component the velocity

\[
v_i=J(p_i-c),
\]

where $J$ is a quarter-turn and $c$ is fixed. Along the straight path, every internal contact vector $r$ changes by $tJr$, so its squared length becomes

\[
|r+tJr|^2=|r|^2+t^2|r|^2>1.
\]

Cross-component pairs and diameter constraints have strict slack. This breaks contacts without increasing the diameter, contradicting contact minimality. Hence every component meets $Q^\circ$.

Now suppose the core has a nonzero pinned expansive velocity. Along the straight motion, every contact with positive first derivative breaks immediately; a zero-derivative contact with nonzero relative velocity breaks at second order. If every contact has zero relative velocity, the velocity is constant on each component, and the pinned vertex in that component forces the constant to be zero. Thus every nonzero expansive velocity would reduce the contact count, a contradiction. The cone is zero, and the rank and Eppstein arguments give (12.1)-(12.2). ∎

If the number $z=n-m$ of isolated vertices in this contact-minimal representative is $O(\sqrt n)$, the face-counting argument applied to the core again yields $m-O(\sqrt n)$ near-equilateral rhombi. If $z$ is large, that representative is genuinely rattler dominated; Theorem 12.3 controls a different, maximal-contact representative.

### Theorem 12.3: a maximal-contact representative has no unanchored component

Assume that a triangle-free minimizer exists for a fixed $n$. Among all such minimizers, choose $A_{\max}$ with the maximum number of unit contacts; subject to that choice, maximize the number $q$ of diameter endpoints. Then every contact component contains a diameter endpoint. Consequently, if $z$ is the number of isolated contact vertices and $c$ the number of contact components,

\[
\boxed{
z\le q\le C_0\sqrt n,
\qquad
c\le q\le C_0\sqrt n.
}
\tag{12.3}
\]

#### Proof

Suppose a contact component $K$ contains no diameter endpoint. Translate every point of $K$ by the same vector $t$. Internal distances remain unchanged. For every $p\in K$ and $x\notin K$, the original cross-distance is strictly between $1$ and $D$. Define the feasible translation set

\[
\mathcal T=
\left\{
t\in\mathbb R^2:
1\le|p+t-x|\le D
\text{ for all }p\in K, x\notin K
\right\}.
\]

It is closed and bounded, and $0$ lies in its interior. Boundedness follows already from any one upper constraint $|p+t-x|\le D$; a point outside $K$ exists because every diameter edge lies outside $K$.

The boundary lies in finitely many unit or diameter circles in the translation plane. Choose a ray from $0$ that avoids every intersection point of two noncoincident circles, and move along it until the first boundary point of $\mathcal T$. All newly active cross-constraints then belong to one geometric circle. Distinct constraints defining the same circle have the same center $x-p$ and radius. For unit constraints, the resulting new contact edges form a matching: two distinct such pairs cannot share $p$ or share $x$. A matching of new intercomponent edges cannot create a triangle, because any triangle using the old components would require two new edges sharing a vertex.

If the active circle is a unit circle, at least one contact is added and none is lost, contradicting maximality of the contact count. If it is a diameter circle, the contact graph is unchanged but a vertex of $K$ becomes a new diameter endpoint, contradicting the secondary maximization. Existing diameter edges lie outside $K$ and remain fixed, so every translated configuration still has diameter exactly $D$. This proves the anchoring assertion.

Each component contains a distinct vertex of $Q$, proving $c\le q$; an isolated vertex is itself a component, proving $z\le q$. Corollary 6.2 supplies the remaining bounds. ∎

The minimum-contact and maximum-contact representatives serve different purposes. The former has a jammed nonisolated core; the latter eliminates an arbitrarily large collection of unanchored rattlers or components. They need not be the same minimizer.

### Theorem 12.4: a hybrid representative with a fixed jammed backbone

Assume that a triangle-free minimizer exists for a fixed $n$. There is a triangle-free minimizer $\widehat A$ with the same $n$ and $D(n)$, together with a distinguished contact subgraph $K$, such that:

1. $K$ is the unchanged nonisolated core of a contact-minimal triangle-free minimizer. If $Q_K$ denotes its original diameter endpoints, then the expansive cone of $K$ pinned at $Q_K$ is zero.
2. Every contact component of $\widehat A$ contains a diameter endpoint, and

   \[
   \#\{\text{contact components}\},
   \quad
   \#\{\text{contact-isolated vertices}\}
   \le C_0\sqrt n.
   \tag{12.4}
   \]

3. Every contact edge of $\widehat A$ outside $K$ is a bridge. Thus every contact cycle and every nonbridge contact edge lies in $K$.
4. If $\widehat Q$ is the full diameter-endpoint set of $\widehat A$, every velocity in $\mathcal E_{\widehat Q}(\widehat A)$ vanishes on $V(K)$. All surviving pinned flexibility is confined to the forest left after the fixed vertices $V(K)\cup\widehat Q$ are deleted.

#### Proof

Start with a contact-minimal triangle-free minimizer $A_0$. Let $K$ be its nonisolated core and $Q_0$ its full diameter-endpoint set. By Theorem 12.2, every component of $K$ meets

\[
Q_K=Q_0\cap V(K),
\]

and the expansive cone of $K$ pinned at $Q_K$ is zero.

Keep every point of $K$ and every point of $Q_0$ fixed from now on. In particular, an original diameter pair remains fixed, so every configuration constructed below has diameter exactly $D(n)$, not merely at most $D(n)$.

First treat the isolated points. Whenever a currently isolated point $p\notin Q_0$ remains, apply the path construction from Theorem 12.1 while all other points stay fixed, choosing the path generically so that its first lower-distance boundary point creates exactly one contact. That edge joins two previously distinct contact components, so it is a bridge and cannot create a triangle. Repeat until every remaining isolated point belongs to $Q_0$. There are at most $|Q_0|=O(\sqrt n)$ such points.

Next take a contact component $L$ containing no current diameter endpoint. Every cross-distance between $L$ and its complement is strictly between (1) and $D$. Make an arbitrarily small generic rigid rotation of $L$, preserving all its internal distances and all strict cross-inequalities. After that rotation, parameterize a translation by $t$. Each cross-constraint has boundary circle

\[
|Rp+t-x|=r,
\qquad r\in\{1,D\},\qquad p\in L,\qquad x\notin L.
\tag{12.5}
\]

Two distinct constraints of the same radius have coincident circles only if

\[
x-y=R(p-q).
\tag{12.6}
\]

For each pair this excludes at most finitely many rotation angles unless the constraints are identical. The two radii are distinct in every nontrivial case. Thus the preliminary rotation can make all distinct boundary circles noncoincident.

The feasible translation set

\[
\mathcal T_L=
\left\{t:
1\le|Rp+t-x|\le D
\text{ for all }p\in L, x\notin L
\right\}
\]

is closed and bounded and contains the current translation in its interior. Choose a ray avoiding the finitely many intersection points of distinct boundary circles and stop at its first boundary point. Exactly one cross-constraint becomes active.

If it is a unit constraint, one new bridge joins two contact components and their number decreases. If it is a diameter constraint, the contact graph stays unchanged and $L$ acquires a diameter endpoint. In either case the number of components without a diameter endpoint decreases by at least one. Never move a component after it has acquired a diameter endpoint. Repetition terminates with every component anchored.

Every added unit edge joined two distinct current components. The quotient graph of these mergers is therefore a forest, so every added contact remains a bridge. Since every final component contains a distinct point of $\widehat Q$,

\[
\#\{\text{components}\},
\quad
\#\{\text{isolates}\}
\le|\widehat Q|
\le C_0\sqrt n.
\]

Finally let $v\in\mathcal E_{\widehat Q}(\widehat A)$. Every point of $Q_K$ remains an endpoint of its fixed original diameter pair, so $Q_K\subseteq\widehat Q$. Restrict $v$ to the unchanged contacts of $K$. This is an element of the expansive cone of $K$ pinned at $Q_K$, hence it vanishes throughout $K$. Every edge outside $K$ is a bridge, proving the last assertion. A remaining forest piece may have several fixed attachments; no one-root assertion is being made. ∎

### Theorem 12.5: quantitative size of the bridge-forest obstruction

Use $\widehat A,K,\widehat Q$ from Theorem 12.4 and put

\[
U=V(\widehat A)\setminus\bigl(V(K)\cup\widehat Q\bigr),
\qquad u=|U|.
\]

Contract each component of $K$ to one fixed root, retain each point of $\widehat Q\setminus V(K)$ as a fixed root, and retain all contact edges incident with $U$. Let $r$ be the number of incident fixed roots and $c$ the number of nonempty connected components of this quotient forest. Define the pinned contact-preserving lineality space

\[
\mathcal L_{\widehat Q}(\widehat A)=
\left\{v:
v_i=0\ (i\in\widehat Q),
\quad
(p_i-p_j)\cdot(v_i-v_j)=0\ (ij\in C)
\right\}.
\tag{12.7}
\]

Then

\[
\boxed{
\dim\mathcal L_{\widehat Q}(\widehat A)
\ge u-r+c
\ge u-|\widehat Q|+c.
}
\tag{12.8}
\]

In particular, if the full pinned expansive cone is zero, then

\[
\boxed{
u\le r-c\le|\widehat Q|-c.
}
\tag{12.9}
\]

Writing $\ell=\dim\mathcal L_{\widehat Q}(\widehat A)$, one has

\[
\boxed{
|V(\widehat A)\setminus V(K)|
\le \ell+2|\widehat Q|.
}
\tag{12.10}
\]

Consequently, if $\ell=O(\sqrt n)$, then $K$ contains $n-O(\sqrt n)$ vertices and itself has

\[
n-O(\sqrt n)
\]

strict unit-rhombus faces with total angular defect $O(\sqrt n)$.

#### Proof

Every contact edge outside $K$ is a bridge. After the components of $K$ are contracted, a cycle or a pair of parallel quotient edges would put its uncontracted edges on a contact cycle in the original graph, contradicting that bridge property. The quotient is therefore a forest.

A forest on $u+r$ vertices with $c$ components has $u+r-c$ edges. Its contact-equality matrix has $2u$ columns and at most $u+r-c$ nonzero rows, so its kernel has dimension at least

\[
2u-(u+r-c)=u-r+c.
\]

Extend a kernel vector by zero on $V(K)\cup\widehat Q$. Every contact derivative is zero, so the extension belongs to (12.7). Every component of $K$ contains an original diameter endpoint, and all other roots are in $\widehat Q\setminus V(K)$; hence $r\le|\widehat Q|$. This proves (12.8).

The lineality space lies inside the pinned expansive cone. If that cone is zero, its lineality is zero, and (12.9) follows from (12.8). In general, $u\le\ell+|\widehat Q|-c$. Adding the at most $|\widehat Q|$ pinned vertices outside $K$ gives (12.10). If $\ell=O(\sqrt n)$, (12.10) and Corollary 6.2 give $|V(K)|=n-O(\sqrt n)$. The core is triangle-free and has zero expansive cone after $Q_K$ is pinned. Applying the rank and Euler counts to $K$, and using the ambient area bound

\[
\operatorname{area}(\operatorname{conv}A)
<\frac{\sqrt3}{2}n,
\]

gives the stated almost-rhombic conclusions exactly as in Sections 8--10. ∎

Thus Target A has an exact scale dichotomy. Either one representative already has an almost-spanning jammed rhombic backbone, or its bridge forest carries more than boundary-order many independent contact-preserving motions. Eliminating only the latter, super-boundary-dimensional alternative would reduce all sufficiently large counterexamples to the boundary-capacity problem of Target B.

---

## 13. Arbitrarily large triangle-free local minima

The local-rigidity route cannot prove Erdős #99.

### Proposition 13.1: regular prime polygons

For every odd prime $p\ge5$, the regular unit $p$-gon is a triangle-free strict local minimum of diameter among feasible $p$-point configurations, modulo Euclidean congruence.

#### Proof

In a regular unit $p$-gon, a diagonal spanning $k$ boundary steps has length

\[
\frac{\sin(k\pi/p)}{\sin(\pi/p)}>1
\qquad
\left(2\le k\le\frac{p-1}{2}\right).
\]

Thus its only contacts are its sides, and the contact graph is $C_p$.

Bezdek and Fodor [3, Theorem 1.2] prove that, for odd prime $p$, every convex $p$-gon with sides at least (1) has diameter at least

\[
d_p=\frac1{2\sin(\pi/(2p))},
\]

with equality only for the regular unit $p$-gon.

Convexity and cyclic order persist under sufficiently small perturbations. Every nearby feasible configuration is therefore a convex $p$-gon with consecutive side lengths at least (1), so the theorem applies. Equality forces congruence. ∎

There are arbitrarily large odd primes, so there are arbitrarily large triangle-free strict local minima. Consequently, no proof can rely on the assertion that every sufficiently large triangle-free feasible configuration is locally diameter-improvable.

The proposition does not produce global minimizers for the full $p$-point problem: other configurations may have fewer hull vertices and smaller diameter, as already happens at $p=7$.

---

## 14. The regular-shell obstruction

The exact stress identities also cannot distinguish global minimizers from large, dense triangle-free local minima.

Let $h=2k+1\ge5$ be odd and let $P_h$ be a regular unit $h$-gon. Its diameter is

\[
D_h=\frac1{2\sin(\pi/(2h))}.
\tag{14.1}
\]

Its contact graph is the boundary cycle. Its diameter graph joins each vertex to the two vertices $k$ steps away and is another $h$-cycle.

### Proposition 14.1: exact shell stress

Assign

\[
\alpha_e=\frac{D_h^2}{h}
\]

to every contact edge and

\[
\beta_e=\frac1h
\]

to every diameter edge. These coefficients satisfy all equations (4.1)-(4.5).

#### Verification

At a vertex, the sum of its two contact edge vectors is radial with factor $2(1-\cos(2\pi/h))$, while the sum of its two diameter vectors is radial with factor $2(1+\cos(\pi/h))$. The identity

\[
D_h^2\bigl(1-\cos(2\pi/h)\bigr)
=1+\cos(\pi/h)
\]

gives equilibrium. Rotational symmetry gives the tensor identity; both sides equal $D_h^2I/2$.

### Proposition 14.2: dense triangle-free shell fillings

For arbitrarily large odd $h$, one can place

\[
n_h=\Delta_2D_h^2+o(D_h^2)
\tag{14.2}
\]

points in $P_h$, including its vertices, so that the configuration is unit-separated, has diameter $D_h$, and has no unit equilateral triangle.

#### Construction

Retain the unit polygon vertices. Inside $P_h$, exclude the unit neighborhoods of those vertices and place a generically translated and rotated triangular lattice of spacing $1+\varepsilon_h$, where $\varepsilon_h\downarrow0$. All interior-interior distances are at least $1+\varepsilon_h$, and all shell-interior distances are strictly greater than (1). A generic placement avoids accidental equalities. Thus the only unit contacts are the shell sides.

The excluded boundary area is $O(h)$, while

\[
\operatorname{area}(P_h)\sim\frac{h^2}{4\pi}
\quad\text{and}\quad
D_h\sim\frac h\pi.
\]

For completeness, if $\Lambda$ is a lattice with fundamental-cell area $a$, averaging over a fundamental cell of translations gives

\[
\frac1a\int_{\mathbb R^2/\Lambda}|(K+t)\cap\Lambda|\,dt
=\frac{\operatorname{area}(K)}a
\]

for every measurable bounded region $K$. Hence some translate contains at least the average number of lattice points. Apply this to the polygon after deleting the forbidden shell neighborhoods. Its area is $\operatorname{area}(P_h)-O(h)$, and the spacing-$1+\varepsilon_h$ triangular lattice has cell area $\frac{\sqrt3}{2}(1+\varepsilon_h)^2$. Choosing $\varepsilon_h\downarrow0$ slowly gives (14.2); a further generic translation or rotation avoids the finitely many unwanted equality conditions without changing the asymptotic count.

For prime $h$, Proposition 13.1 makes the shell locally diameter minimizing. The interior points may move, so the filled configuration need not be a strict local minimum, but no sufficiently small feasible perturbation can lower its diameter because the shell subset cannot be improved locally.

These configurations are **not certified global minimizers**. They prove instead that all of the following may coexist at arbitrarily large scale:

- triangle-freeness;
- asymptotically hexagonal density;
- exact KKT scalar and tensor identities;
- a boundary-supported proper stress;
- a flexible or completely unstressed interior; and
- local diameter minimality.

Therefore any Level I proof must use a sharp global finite-capacity comparison, not merely local rigidity, stress, or leading density.

---

## 15. Computational exploration

Numerical optimization was used only for conjecture formation and falsification of local lemmas.

### 15.1 Moderate-$n$ nonlinear searches

SLSQP searches were run for $9\le n\le13$, minimizing a diameter variable subject to all squared-distance lower and upper constraints. Multiple perturbed triangular-patch starts were used.

For $n=9$, one run produced an apparent triangle-free local optimum with

\[
D\approx2.56923698,
\]

with (11) apparent unit contacts and (5) apparent diameter pairs. Its hull had seven vertices. This is consistent with the Vincze-type upper-bound discussion in [3], but it is **not** an exact configuration and no global lower bound was obtained.

For $n=10,11,12,13$, the best runs found in the limited search included apparent unit triangles in several active sets. These computations are neither exhaustive nor exact.

No numerical equality was treated as a unit contact. The experiment supplies no proof for or against Erdős #99.

### 15.2 Polygon-area experiment

A separate constrained numerical experiment minimized the area of convex equilateral $m$-gons with all vertex distances at least (1), for $4\le m\le8$. It repeatedly found the value

\[
(m-2)\frac{\sqrt3}{4}
\]

at degenerate triangular-lattice-type limits. A complete proof for the general face class was not established, and even such a face inequality would not control the possibly winding outer contact face. It was therefore not used as a theorem.

### 15.3 Train-track and boundary-word falsification

The balanced $C_5$ crossing pattern was first tested by explicit coordinate generation for small sector sizes. Those tests detected no unintended unit distances or edge crossings and led to Proposition 10.10. The proposition's final statement does not rely on those computations: its unit separation, planarity, track graph, positive stress, and pinned rank are proved exactly.

The $k=0$ case of Theorem 10.12 was independently checked by enumerating the words $r_i\in\{0,1,2\}$ for $4\le C\le8$. Before simplicity is imposed, the canonical closed words are exactly those displayed after (10.36); all except $0000$ and $01010101$ repeat a boundary vertex. Again the theorem uses the explicit finite recurrence (10.36), not floating-point evidence.

Finally, the pairwise distances in the 11-point sun and the 12-point triangular-lattice competitor were enumerated during discovery and then replaced by the exact cyclotomic and quadratic-form calculations in Proposition 10.10.

---

## 16. Routes that were tested and why they do not close the problem

### 16.1 Leading density

A triangular lattice can be perturbed by an arbitrarily small amount so that no exact unit triangle remains, then rescaled to minimum distance (1). Thus triangle-free configurations can approach $\Delta_2$ arbitrarily closely. There is no uniform density gap based only on the absence of exact contacts.

### 16.2 Raw edge counts and Laman-style counting

Eppstein gives a contact deficit of order $\sqrt n$, but the diameter graph also lives on $\Theta(\sqrt n)$ boundary vertices. Those cable constraints can compensate for the missing contact rows. The square is the smallest exact example.

### 16.3 Recursive use of (2)-degeneracy

A low-degree contact vertex need not be removable. It may be a diameter-loaded polygon corner, as in the square and every regular odd shell. Deleting it also destroys the equilibrium equations at its neighbors. A degeneracy ordering is not a recursively valid stress ordering.

### 16.4 First-order flexibility

The zero-cone branch is possible, and Proposition 13.1 gives arbitrarily large triangle-free local minima. In the nonzero-cone branch, the result is only a family of same-diameter minimizers, not a diameter improvement.

### 16.5 Second-order prestress

The correct multiplier may depend on the critical direction. Furthermore, the tensor identity makes every affine critical shear quadratic-neutral. A fixed-stress negative-curvature claim is unjustified.

### 16.6 Exact rhombus equality

The total defect

\[
\sum_F\left(\sin\theta_F-\frac{\sqrt3}{2}\right)
\]

is only $O(\sqrt n)$. This permits $n-O(\sqrt n)$ strictly positive defects of size $O(1/n)$, or smaller. No exact $60^\circ$ angle follows.

### 16.7 Lattice classification

Schürmann rules out eventual lattice extremizers. Nonlattice does not mean triangle-free, and a nonlattice rhombic mesh is not excluded.

### 16.8 Simultaneous normalizations

The full normalization $\mathcal E_Q(A)=\{0\}$ still cannot be imposed by selection. Theorem 12.4 does combine the two useful partial normalizations in one representative: it has only $O(\sqrt n)$ components and isolates, and every pinned motion vanishes on a fixed contact-minimal core. The residue is exactly a bridge forest. Theorem 12.5 quantifies it: if its contact-preserving lineality is only $O(\sqrt n)$, the fixed core already contains $n-O(\sqrt n)$ vertices. What remains is a genuinely high-dimensional forest-flex alternative, not the old arbitrary-representative gap.

### 16.9 Regular shells as counterexamples

Regular prime shells certify local polygonal optimality and carry exact stresses. What is missing for a disproof is an infinite sequence of $n$ for which a filled shell has diameter exactly $D(n)$. Bezdek-Fodor's polygon theorem does not compare against configurations with fewer hull vertices and many interior points.

### 16.10 Nonlinear stress moments

The identities (11.7)--(11.14) are exact and substantially restrict where positive stress can live. They are nevertheless necessary conditions, not global certificates. The regular-shell stress satisfies every virtual-work identity automatically, including the midpoint and high-moment consequences. Their remaining promise lies in combining them with the degree-four rhombic bulk, not in using them alone.

### 16.11 Train tracks without diametral boundary control

The crossing graph of the rhombus tracks is simple and triangle-free, giving

\[
F_4\le B_{\mathcal R}^2/16.
\]

At most two tracks can have both ends on the strictly turning convex hull, so at least

\[
2\sqrt n-O(1)
\]

track ends enter the non-hull or non-rhombic defect network. The exact width inequality also charges every angular defect. These facts eliminate an exception-free convex rhombic crystal but do not control the compulsory boundary shell sharply enough.

Proposition 10.10 is the exact limitation. Its five-sector complexes have zero expansive cone when their full boundary is pinned, a positive stress on every edge, $n-O(\sqrt n)$ strict rhombi, diameter $O(\sqrt n)$, and total defect tending to zero. They fail precisely because most boundary pins are neither extreme nor diametral. Thus a local curvature maximum principle, positive stress, or ordinary boundary-pinned rigidity cannot replace $Q=V(\operatorname{conv}A)$.

Theorem 10.12 sharpens the opposite side of this picture. A two-fixed-direction $R$-face core needs at least $\sqrt R-3$ non-hull interface supports, apart from the one-rhombus and five-rhombus-cross exceptions. This proves that the $\Theta(\sqrt n)$ support shell is genuinely necessary for an ordinary oblique grid, but the general theorem stack still permits a shell of exactly that order.

### 16.12 Why the Cartesian estimate does not automatically globalize

Theorem 10.9 is a genuine global-capacity exclusion: an additive $a\times b$ block occupying at least $2n/\pi$ cells cannot occur in a minimizer. A dense track-crossing graph need not supply such a block. Five projective direction classes can have crossing graph a balanced blow-up of $C_5$; Proposition 10.10 realizes the corresponding five-sector geometry with $R=5s^2$ crossings. Its largest complete bipartite subgraph has only $2s^2=2R/5$ crossings, below the $2R/\pi$ scale needed for the Cartesian estimate to contradict global optimality when $R\sim n$. No extraction of a sufficiently large Cartesian block follows from triangle-freeness, quadratic track density, unit separation, or even total defect $o(1)$ alone.

### 16.13 Schürmann's deformation mechanism

Schürmann's proof was rechecked at the level of its actual sequential motion. It uses missing neighbors in one fixed four- or six-neighbor packing lattice, frees sites one at a time, and propagates the free sites to the boundary. An almost-rhombic mesh has varying track directions and may devote $\Theta(\sqrt n)$ exceptional vertices to blocking exactly this propagation. The lattice deformation remains a useful model, but its hypotheses do not extend to the surviving defect shell without a new boundary-peeling theorem.

---

## 17. Strongest consolidated unconditional theorem

### Theorem 17.1: audited triangle-free minimizer alternatives

Let $A$ be a triangle-free diameter-minimizing $n$-point configuration with minimum distance (1), and let $Q$ be its diameter endpoints.

Then:

1. **Exact stress and moments.** $A$ carries a normalized proper mixed contact/diameter KKT stress satisfying (4.1)-(4.5) and the virtual-work identity (11.7). The two normalized edge-stress measures have the same midpoint barycenter $\mu$, satisfy the quartic identity (11.9), and obey

   \[
   \sum_C\frac{\alpha_{ij}}{D^2}|m_{ij}-\mu|^2
   \ge\frac{D^2-1}{12},
   \qquad
   \max_{\alpha_{ij}>0}|m_{ij}-\mu|
   \ge\frac{D-1}{2}.
   \]

2. **Second-order normality.** Every critical first-order direction has a direction-dependent normalized stress supported on its zero-derivative active edges and satisfying (11.3).

3. **Pinned dichotomy.** Exactly one of the following occurs:

   - $A$ belongs to a nontrivial continuous family of triangle-free global minimizers with all diameter endpoints fixed; or
   - the pinned expansive cone is zero.

4. **Jammed branch.** In the zero-cone branch:

   \[
   Q=V(\operatorname{conv}A),
   \]

   every non-hull vertex is a strict convex combination of at least three unit-contact neighbors,

   \[
   |Q|=\Theta(\sqrt n),\qquad
   e^\circ\ge2(n-|Q|),\qquad
   |E(G(A))|=2n-\Theta(\sqrt n),
   \]

   and its cyclomatic number is at least $n-2|Q|+c=n-O(\sqrt n)$. All nontrivial tree components together contain $O(\sqrt n)$ vertices, every cyclic component contains at least four diameter endpoints, and for $n\ge44$ at least one cyclic component exists.

5. **Rhombic bulk.** In the zero-cone branch there are $n-O(\sqrt n)$ bounded unit-rhombus faces and

   \[
   \sum_{F\in\mathcal F_4}\left(\theta_F-\frac\pi3\right)=O(\sqrt n).
   \]

   All but $O(\sqrt n)$ vertices have contact degree (4) and are incident only with these rhombi. For every fixed $\varepsilon>0$, all but $O_\varepsilon(\sqrt n)$ vertices are surrounded by rhombi with acute angles in

   \[
   60^\circ<\theta<60^\circ+\varepsilon.
   \]

   If $B_{\mathcal R}$ is the boundary-edge count of the full rhombic face complex, then

   \[
   F_4\le\frac{B_{\mathcal R}^2}{16},
   \qquad
   B_{\mathcal R}D_{\mathcal R}
   \ge4\sum_F\sin\theta_F
   \ge2\sqrt3F_4+4\chi_*\sum_F\left(\theta_F-\frac\pi3\right).
   \]

   At most two tracks have both ends on the convex hull, so at least $2\sqrt n-O(1)$ track ends enter the defect network. If the rhombi tile the whole convex hull, the configuration is the unit square.

   If a connected $R$-face subcomplex uses only two fixed edge directions, has regular boundary topology as in Theorem 10.12, and needs external support at only $k$ non-hull boundary incidences, then

   \[
   R\le(k+3)^2.
   \]

   With no such incidences it is either one rhombus or the five-rhombus cross.

6. **Existential normal forms.** If any triangle-free minimizer exists for a given $n$, there is a contact-minimal one for the same $n,D(n)$ in which every non-diameter nonisolated vertex is surrounded by (3)-(5) contacts, every contact vertex of degree (1) or (2) is diametral, all nontrivial tree components together contain $O(\sqrt n)$ vertices, and

   \[
   \kappa\ge\frac{n-z}{2}-C_0\sqrt n+c_*
   \]

   for the cyclomatic number of the nonisolated contact graph.

   More strongly, one hybrid representative has only $O(\sqrt n)$ components and isolates and contains the unchanged contact-minimal core $K$, pointwise fixed under every pinned expansive motion. Every contact edge outside $K$ is a bridge. If $u$ unpinned vertices lie outside $K$ and the contracted bridge forest has $r$ fixed roots and $c$ components, then

   \[
   \dim\mathcal L_{\widehat Q}\ge u-r+c\ge u-|\widehat Q|+c.
   \]

   Hence lineality $O(\sqrt n)$ already forces $|V(K)|=n-O(\sqrt n)$ and puts that core in the almost-rhombic regime.

7. **Exact global block restriction.** Every additive Cartesian $a\times b$ rhombic train block in a global minimizer satisfies

   \[
   ab+\frac{4\sqrt3-6}{\pi}\Delta_{a,b}<\frac2\pi n.
   \]

8. **Exact limitations.** There are arbitrarily large triangle-free strict local diameter minima, arbitrarily large asymptotically dense triangle-free shell configurations carrying the full exact KKT stress, and arbitrarily large boundary-pinned jammed rhombic complexes with positive stress and total positive angular defect tending to zero. The 11-point sun additionally has a diametral convex hull, positive stress, zero hull-pinned cone, and five strict rhombi, yet no $60^\circ$ face. It is provably not global: a 12-point triangular-lattice set of diameter (3) is already smaller than its diameter $\sqrt{5+2\sqrt5}$.

Every statement above is unconditional. None implies that a hypothetical triangle-free configuration is globally nonoptimal.

---

## 18. Exact remaining Level I target

The investigation reduces the affirmative problem to eliminating two sharply defined possibilities.

### 18.1 Flexible anchored-component obstruction

One must prove that, for sufficiently large $n$, no triangle-free global minimizer can have a nonzero pinned expansive cone. Equivalently, one must rule out a same-diameter triangle-free minimizer family supported by a diametral shell.

Theorems 12.4 and 12.5 reduce this to an exact scale question. In one representative, all nonbridge structure lies in a fixed pinned-jammed core $K$, and the remaining contact graph is a bridge forest. If its pinned contact-preserving lineality has dimension $\ell$, then

\[
|V(A)\setminus V(K)|\le\ell+2|Q|.
\]

Thus $\ell=O(\sqrt n)$ already puts $n-O(\sqrt n)$ vertices into the almost-rhombic core. The genuinely separate flexible obstruction is now:

> **Super-boundary forest-capacity lemma.** No sufficiently large triangle-free global minimizer in the hybrid normal form has $\ell=\omega(\sqrt n)$.

This lemma would not by itself finish Level I, but it would reduce every counterexample to the same boundary-order rhombic problem. The $n=8$ family and the regular-shell fillings show why it requires global capacity, not another local rigidity count.

### 18.2 First-order-jammed almost-rhombic obstruction

One must prove that a global minimizer cannot satisfy all of the following for arbitrarily large $n$:

\[
Q=V(\operatorname{conv}A),\qquad |Q|=\Theta(\sqrt n),
\]

\[
e^\circ\ge2(n-|Q|),\qquad
e=2n-\Theta(\sqrt n),\qquad
F_4=n-O(\sqrt n),
\]

\[
\theta_F>60^\circ\text{ for every rhombus},
\]

\[
\sum_F\left(\theta_F-\frac\pi3\right)=O(\sqrt n),
\]

together with cyclomatic number $n-O(\sqrt n)$, the first- and second-order stress identities, the common midpoint barycenter, the quartic identity, and positive contact stress reaching radius at least $(D-1)/2$ from that barycenter.

In addition, the surviving rhombic complex must satisfy

\[
F_4\le\frac{B_{\mathcal R}^2}{16},
\qquad
b_{\mathcal R}\ge2\sqrt{F_4}-2,
\]

where $b_{\mathcal R}$ counts non-hull boundary edges, as well as

\[
B_{\mathcal R}D_{\mathcal R}
\ge2\sqrt3F_4+4\chi_*\sum_F\delta_F.
\]

For an ideal disk rhombic minimizer, its exact permitted shell budget is

\[
4G+4\chi_*\Delta
<\sqrt3B_{\mathcal R}+2\sqrt3.
\tag{18.1}
\]

Theorem 10.12 eliminates one important model case: a large two-direction core cannot be held only by its diametral hull vertices. It must use at least $\sqrt R-3$ non-hull support incidences. This does not yet contradict the general $O(\sqrt n)$ exceptional budget; it identifies the exact boundary scale that a sharp capacity theorem must charge.

The required conclusion is an exact equality

\[
\theta_F=60^\circ
\]

for at least one face, not merely $\theta_F=60^\circ+o(1)$.

### 18.3 A sufficient missing global theorem

One sufficient theorem would be:

> **Sharp boundary-capacity theorem.** For all sufficiently large $n$, every unit-separated triangle-free $n$-point set satisfying either branch of Theorem 17.1 has diameter strictly larger than an explicitly constructed $n$-point competitor.

Such a theorem must include a boundary-order term and an exact equality analysis. The leading Thue density constant, an $O(\sqrt n)$ contact deficit, or an $O(1)$ diameter estimate is insufficient unless its constants and equality cases actually separate the two configurations.

After the new train-track theorem, a focused jammed-branch version is:

> **Diametral-shell cost lemma.** In a sufficiently large jammed triangle-free minimizer, the non-hull interfaces forced by at least $2\sqrt n-O(1)$ bad track ends have a strict area/diameter cost exceeding the right side of (18.1), with the exact exceptional-face, hole, component, and outside-vertex corrections.

Proposition 10.10 shows that “pinned boundary” cannot replace “diametral convex hull” in this statement. The five-sector examples satisfy all the local premises, even with total defect $o(1)$, and fail only at the hull condition.

For a disproof, the exact missing theorem is the opposite:

> **Globally optimal shell theorem.** There are arbitrarily large $n$ for which a triangle-free shell or rhombic configuration can be proved to have diameter $D(n)$.

No such global certificate was obtained.

---

## 19. Final adversarial audit

The following checks were applied to every consolidated claim.

### Quantifiers

- No result replaces “every minimizer” by “some minimizer” except the explicitly labeled contact-minimal normal-form theorem, which is used only under an existential contradiction hypothesis.
- No finite counterexample is presented as a disproof.
- No infinite family of local minima is presented as an infinite family of global minimizers.

### Exact distances

- Every asserted unit triangle consists of three exact unit edges.
- Near-equilateral rhombi are never counted as exact unit triangles.
- Numerical distances are not used as equality evidence.

### Optimization

- Ordinary KKT is justified by an explicit MFCQ direction.
- The second-order multiplier is allowed to depend on the critical direction.
- The nonlinear midpoint and moment formulas are derived from the vertex equilibrium equations by exact virtual work, not by an asymptotic approximation.
- The high-moment radius estimate uses the explicit Hessian of $|x|^{2k+2}/(2k+2)$ and then takes $k\to\infty$ only after a valid inequality for every integer $k\ge1$.
- Global and local optimality are kept distinct.
- Same-diameter flexes are not called diameter improvements.

### Rigidity

- No Laman theorem is applied to the cable-strut problem.
- The pinned positive stress is obtained by a direct cone-duality proof, not by an unchecked transfer of an unpinned theorem.
- Contacts joining two pinned vertices are removed from the effective row count, giving $e^\circ\ge2(n-q)$.
- First-order zero-cone rigidity is not silently upgraded to global rigidity.

### Boundary and packing

- The planar lower bound uses Bezdek-Fodor's sharper (-1) constant.
- The triangular-lattice averaging argument uses an open disk, so the upper bound in (2.2) is strict.
- Cauchy's perimeter-diameter inequality is used only for convex hulls.
- The enclosing-circle problem is never substituted for the diameter problem.
- Schürmann's theorem is used only to exclude large lattice extremizers.
- Train monotonicity and the two-crossing exclusion do not assume simple connectedness; the latter uses disjoint open $60^\circ$ displacement cones.
- The Cartesian determinant bound is invoked only for an actual additive block, not for an abstract biclique or a dense crossing graph.
- The two-direction support theorem assumes a connected cell complex, a simple outer boundary, and no pinched boundary vertices. Every hole-boundary incidence is explicitly charged; none disappears in the affine square-complex reduction.
- The zero-support classification in Theorem 10.12 is an exact finite turn-word check. The closed but rejected words repeat a boundary vertex; numerical polyomino enumeration is not being used as proof.

### Rattlers and disconnected graphs

- Contact-isolated vertices are retained as a genuine possibility.
- Theorem 12.4 does not conflate minimum- and maximum-contact representatives. It freezes the original contact-minimal core and every original diameter endpoint, then creates only bridge contacts while anchoring the other components.
- An original diameter pair remains fixed throughout the hybrid construction, so its diameter never silently falls below $D(n)$.
- The generic preliminary rotation separates coincident equal-radius translation circles; the subsequent ray avoids their intersections, so each new contact is unique.
- The bridge-forest count permits several fixed roots in one forest component; no false one-root or freely hinged-leaf assertion is used.
- In the maximal-contact representative, coincident active translation circles are handled explicitly: their new unit edges form a matching and cannot create a triangle.
- Euler formulas use the correct component term.

### Regression against the exact small minimizers

- The unit square lies in the zero-cone branch because every vertex is diametral; its single bounded contact face is the allowed $90^\circ$ rhombus.
- The five-rhombus cross is the exact nontrivial $k=0$ exception in Theorem 10.12. It blocks the stronger but false assertion that an internally equilibrated two-direction core must be a single rhombus.
- The regular unit pentagon also has every hull vertex diametral and supplies an arbitrarily extensible model for polygonal local rigidity.
- For $n=6$, the five hull vertices are diametral and the center is trapped by its five radial contacts; the contact graph is a tree, consistent with the threshold $n<44$.
- The $n=7$ hexagon-plus-center configuration is excluded by the triangle-free hypothesis exactly because its six center-side triples are unit triangles.
- For $n=8$, the regular unit heptagon plus its center lies in the flexible branch: all seven hull vertices are fixed diameter endpoints and the contact-isolated center can move. The attachment or maximum-contact selection moves it to a representative with additional anchoring, whereas contact minimization prefers the isolated representative. This confirms why the normalizations must not be conflated.
- The 11-point five-rhombus sun is triangle-free, has a regular-pentagon diametral hull, and has zero cone after exactly those hull vertices are pinned. Its contact distances and diameter $\sqrt{5+2\sqrt5}$ are checked exactly. The explicit 12-point triangular-lattice set of diameter (3) proves that the sun is not globally minimizing.
- The five-sector family has exactly $5s^2+5s+1$ vertices, $5s^2$ rhombi, $10s$ rhombic boundary edges, and a balanced $C_5$ blow-up on $5s$ tracks. With $\varepsilon=s^{-3}$ its positive total defect is $8/s$, while its boundary-pinned cone is still zero. It is not a jammed-branch counterexample because most of those pins are nonextreme and nondiametral.

### Conclusion

The Level I problem remains unresolved in this record. Target A is reduced to a super-boundary-dimensional bridge-forest capacity question; Target B is reduced to charging at least $2\sqrt n-O(1)$ forced bad track ends against the exact diametral shell budget. Both remaining statements are global finite-capacity comparisons, not omitted routine rigidity or train-track calculations.

---

## 20. References

1. P. Erdős, “Some problems in number theory, combinatorics and combinatorial geometry,” *Mathematica Pannonica* **5** (1994), 261-269. [Supplied PDF](../../papers/primary/mp05-2-261-269.pdf)
2. P. Bateman and P. Erdős, “Geometrical Extrema Suggested by a Lemma of Besicovitch,” *American Mathematical Monthly* **58** (1951), 306-314. [Supplied PDF](../../papers/primary/1951-03.pdf)
3. A. Bezdek and F. Fodor, “Minimal Diameter of Certain Sets in the Plane,” *Journal of Combinatorial Theory, Series A* **85** (1999), 105-111. [Supplied PDF](../../papers/primary/1-s2.0-S0097316598928898-main.pdf)
4. A. Schürmann, “On Extremal Finite Packings,” *Discrete & Computational Geometry* **28** (2002), 389-403. [Supplied PDF](../../papers/primary/s00454-002-0747-6.pdf)
5. A. V. Bondarenko, D. P. Hardin, and E. B. Saff, “Minimal $N$-Point Diameters and $f$-Best-Packing Constants in $\mathbb R^d$,” *Proceedings of the American Mathematical Society* **142** (2014), 981-988. [Supplied PDF](../../papers/primary/1204.4403v1.pdf)
6. D. Eppstein, “Edge Bounds and Degeneracy of Triangle-Free Penny Graphs and Squaregraphs,” *Journal of Graph Algorithms and Applications* **22** (2018), 483-499. [Supplied PDF](../../papers/primary/463.pdf)
7. A. Bezdek, K. Bezdek, and R. Connelly, “Finite and Uniform Stability of Sphere Packings,” *Discrete & Computational Geometry* **20** (1998), 111-130. [Supplied PDF](../../papers/primary/10.1007_PL00009374.pdf)

---

## 21. Addendum: an exact Oler-surplus decomposition for the defect shell

This addendum records the strongest new boundary-capacity result obtained in the
subsequent investigation.  It does not close Level I.  Its point is that the area,
perimeter, topology, holes, rhombic components, and vertices outside the rhombic
complex can be placed in one exact inequality with no unspecified boundary-order
constant.

Put

\[
a_0=\frac{\sqrt3}{2},\qquad c_0=\frac{\sqrt3}{4},\qquad
c=\frac{2\sqrt3}{\pi},\qquad
C_0=\pi\sqrt c=\sqrt{2\pi\sqrt3}.
\]

### 21.1 The finite Oler inequality and an improved universal diameter bound

The following finite packing inequality is the unsummed cell inequality relevant to
the present boundary problem.

**Lemma 21.1 (Oler inequality).**  If \(X\subset K\subset\mathbb R^2\), where
\(K\) is convex, \(|X|=N\), and the mutual distances in \(X\) are at least \(1\),
then

\[
\boxed{
N\le \frac{2}{\sqrt3}\operatorname{area}(K)
       +\frac12\operatorname{per}(K)+1.
}
\tag{21.1}
\]

Equivalently,

\[
\boxed{
\operatorname{area}(K)+c_0\operatorname{per}(K)
\ge a_0(N-1).
}
\tag{21.2}
\]

For completeness, the standard proof is the Dirichlet-cell proof of the finite
hexagonal packing inequality before its boundary terms are discarded.  Intersect the
Voronoi cells of \(X\) with a polygonal approximation to \(K\), and join each cell
center to the consecutive vertices of its clipped cell.  Every internal Voronoi side
is at distance at least \(1/2\) from each of its two centers.  On the resulting
triangles, symmetrization about the side and

\[
\tan u+\tan v\ge2\tan\frac{u+v}{2}
\]

give the regular circumscribed-hexagon value \(a_0\) for each full cell after the
cell angles are summed.  Internal side terms cancel in pairs.  The uncancelled
boundary triangles contribute at worst \(c_0\) times their total base length, and the
outer-face term in Euler's formula contributes one further \(a_0\).  Thus

\[
a_0N\le \operatorname{area}(K)+c_0\operatorname{per}(K)+a_0.
\]

Passing from polygonal approximations to an arbitrary convex \(K\) proves (21.2).
This is also sharp: collinear unit chains and convex triangular-lattice patches give
equality.

Applying (21.2), the isodiametric inequality, and Cauchy's perimeter inequality gives
a universal improvement of (2.2):

\[
a_0(n-1)
\le \frac{\pi D(n)^2}{4}+c_0\pi D(n).
\]

Consequently,

\[
\boxed{
D(n)\ge
\sqrt{\frac{2\sqrt3}{\pi}(n-1)+\frac34}
-\frac{\sqrt3}{2}.
}
\tag{21.3}
\]

Thus the additive loss in the universal planar lower bound improves from \(1\) to
\(\sqrt3/2=0.8660254037\ldots\).  The constant check is important: this remains a
positive constant below the strict lattice-averaging upper bound
\(D(n)<\sqrt{cn}\), so (21.3) alone cannot prove Erdős #99.

### 21.2 Exact topology-corrected shell window

Let \(A\) be an \(n\)-point unit-separated set and put
\(K=\operatorname{conv}A\), \(P=\operatorname{per}K\).  Let \(\mathcal R\) be
any finite edge-to-edge complex of strict unit-rhombus faces whose vertices belong to
\(A\).  Write

\[
R=|\mathcal R|,
\qquad B=B_{\mathcal R},
\qquad v=|V(\mathcal R)|,
\qquad t=n-v,
\]

and let \(\chi=\chi(\mathcal R)\) be its Euler characteristic.  For a regular
planar complex with \(r\) components and \(h\) holes, \(\chi=r-h\).  Define

\[
E_{\mathcal R}
=\sum_{F\in\mathcal R}
\left(\sin\theta_F-a_0\right),
\qquad
G_{\mathcal R}
=\operatorname{area}(K)-\sum_{F\in\mathcal R}\sin\theta_F.
\tag{21.4}
\]

The edge-face incidence count and Euler's formula give the exact identity

\[
4R=2e-B,
\qquad
v-e+R=\chi,
\qquad
\boxed{v=R+\frac B2+\chi.}
\tag{21.5}
\]

**Theorem 21.2 (Oler shell window).**  For every such complex,

\[
\boxed{
G_{\mathcal R}+E_{\mathcal R}
\ge
c_0(B-P)+a_0(t+\chi-1).
}
\tag{21.6}
\]

If \(A\) is a global diameter minimizer, then additionally

\[
\boxed{
G_{\mathcal R}+E_{\mathcal R}
<
c_0B+a_0(t+\chi).
}
\tag{21.7}
\]

The difference between the right sides of (21.7) and (21.6) is exactly

\[
\boxed{c_0P+a_0.}
\tag{21.8}
\]

In particular, all component, hole, and outside-vertex corrections cancel from the
remaining capacity window.

**Proof.**  Since the rhombi have disjoint interiors,

\[
\operatorname{area}(K)
=a_0R+E_{\mathcal R}+G_{\mathcal R}.
\]

Insert this expression into (21.2), use \(n=v+t\), and then use (21.5):

\[
\begin{aligned}
G_{\mathcal R}+E_{\mathcal R}
&\ge a_0(n-R-1)-c_0P\\
&=c_0(B-P)+a_0(t+\chi-1).
\end{aligned}
\]

This proves (21.6).  For a global minimizer, Theorem 10.9 gives
\(D(n)^2<cn\), and hence the isodiametric inequality gives
\(\operatorname{area}(K)<a_0n\).  Therefore

\[
G_{\mathcal R}+E_{\mathcal R}
<a_0(n-R)
=c_0B+a_0(t+\chi),
\]

which is (21.7).  Subtraction gives (21.8). \(\square\)

The theorem incorporates, with exact signs, all of the following quantities requested
in Target B: holes, multiple rhombic components, vertices outside the rhombic core,
and the full convex-hull perimeter.  A bridge forest outside the core is counted in
\(t\).  The cancellation in (21.8) also shows why area accounting alone cannot prove
the super-boundary forest-capacity theorem: each outside vertex receives exactly one
bulk allowance \(a_0\) on both sides.

For an ideal rhombic disk, \(t=0\) and \(\chi=1\), so (21.6)-(21.7) reduce to

\[
c_0(B-P)
\le G+\sum_F(\sin\theta_F-a_0)
<c_0B+a_0.
\tag{21.9}
\]

This is the exact perimeter-refined version of the ideal budget (10.29).

### 21.3 Convex defect faces, pockets, and a local surplus decomposition

There is a useful local form of Theorem 21.2 in the jammed branch.

**Lemma 21.3 (convexity of simple contact faces).**  In the zero pinned-cone
branch, every simple bounded contact face is a strictly convex equilateral polygon.

Indeed, at a non-hull vertex the positive spanning relation in Theorem 8.2 makes every
angular gap between consecutive contact rays strictly smaller than \(\pi\).  At a hull
vertex, every bounded face angle is contained in the strictly smaller-than-\(\pi\)
interior angle of the convex hull.  Thus every face angle is smaller than \(\pi\).

Two immediate specializations of (21.1) are:

1. If \(F\) is a convex equilateral \(m\)-gon whose vertices are unit-separated, then

   \[
   \boxed{
   \operatorname{area}(F)\ge c_0(m-2).
   }
   \tag{21.10}
   \]

2. If \(C\) is a convex pocket bounded by a chain of \(r\) unit edges and its
   closing hull chord of length \(L\), then

   \[
   \boxed{
   \operatorname{area}(C)\ge c_0(r-L).
   }
   \tag{21.11}
   \]

For (21.10), use \(N=m\) and perimeter \(m\) in (21.1).  For (21.11), use
\(N=r+1\) and perimeter \(r+L\).  The vertices of a pocket are a subset of
\(A\), so the separation hypothesis is automatic.

Suppose now that the full contact graph is connected, has a simple outer boundary,
and its bounded faces form a topological disk.  Its non-hull outer-boundary vertices
are reflex for the bounded region, because their outer-face angular gaps are smaller
than \(\pi\).  Hence the indentation between consecutive hull vertices, together with
the hull chord, is a convex pocket to which (21.11) applies.

If the bounded contact faces have lengths \(m_F\), the outer boundary has \(k\)
unit edges, and there are \(f\) bounded faces, Euler and incidence counting give

\[
\sum_F(m_F-2)=2n-k-2.
\tag{21.12}
\]

Writing

\[
s_F=\operatorname{area}(F)-c_0(m_F-2)\ge0,
\qquad
s_C=\operatorname{area}(C)-c_0(r_C-L_C)\ge0,
\]

and noting that \(\sum_C(r_C-L_C)=k-P\), one obtains the exact local identity

\[
\boxed{
\operatorname{area}(K)+c_0P-a_0(n-1)
=\sum_Fs_F+\sum_Cs_C.
}
\tag{21.13}
\]

For a rhombus, its summand is exactly
\(s_F=\sin\theta_F-a_0\).  Thus the global Oler surplus is literally the sum
of the strict-rhombus, exceptional-face, and indentation-pocket slacks.  This is the
local-cell decomposition that is lost when the finite packing inequality is used only
in its already-summed form.

A nonquadrilateral contact face has \(m\ge5\), so (21.10) gives the sharp uniform
track-end charge

\[
\operatorname{area}(F)
\ge \frac{3c_0}{5}m
\ge \frac{3c_0}{5}\,r_F,
\qquad
\boxed{\frac{3c_0}{5}=\frac{3\sqrt3}{20}
=0.2598076211\ldots,}
\tag{21.14}
\]

where \(r_F\) is the number of rhombic boundary edges incident with \(F\).
The constant is forced by pentagons and cannot be improved using only (21.10).

Let \(B\) now denote the boundary-edge count of all rhombic faces in this regular
contact disk, and let

\[
G=\operatorname{area}(K)-\sum_{F\in\mathcal R}\operatorname{area}(F).
\]

Partition the rhombic boundary edges into those incident with bounded
nonquadrilateral faces and those incident with the outer face.  Apply (21.14) to the
first class and (21.11) to the outer pockets.  A two-case comparison according as the
number of outer rhombic edges is at least \(P\) gives

\[
\boxed{
G\ge\frac{3\sqrt3}{20}(B-P).
}
\tag{21.15}
\]

If every bounded face is a rhombus, the sharper coefficient \(c_0\) holds:

\[
\boxed{G\ge c_0(B-P).}
\tag{21.16}
\]

Finally, in the jammed almost-rhombic regime,

\[
B\ge4\sqrt R=4\sqrt n-O(1),
\qquad
P\le\pi D<C_0\sqrt n.
\]

Therefore

\[
\boxed{
B-P\ge(4-C_0)\sqrt n-O(1)
=0.7010916676\ldots\sqrt n-O(1).
}
\tag{21.17}
\]

Under the regular contact-disk hypotheses, (21.15) yields the unconditional shell
area charge

\[
\boxed{
G\ge0.1821489584\ldots\sqrt n-O(1).
}
\tag{21.18}
\]

In the pure rhombic-disk case, (21.16) improves this to

\[
\boxed{
G\ge0.3035815973\ldots\sqrt n-O(1).
}
\tag{21.19}
\]

These are genuine boundary-order lower bounds.  The five-sector examples escape for
the correct global reason: their boundary perimeter is too large to satisfy
\(P<C_0\sqrt n\).  The 11-point sun is below the asymptotic range and remains a
valid finite local regression example.

### 21.4 Constant audit and exact remaining lemma

The new estimates do not close Target B.  Define the Oler surplus

\[
\mathscr O(A)
=\operatorname{area}(K)+c_0P-a_0(n-1).
\tag{21.20}
\]

Equation (21.13) decomposes it into nonnegative local face and pocket slacks.  For a
global minimizer,

\[
\mathscr O(A)
<c_0\pi D+a_0
<c_0C_0\sqrt n+a_0,
\]

where

\[
\boxed{
c_0C_0
=\frac{\sqrt3}{4}\sqrt{2\pi\sqrt3}
=1.4284692103\ldots.
}
\tag{21.21}
\]

Thus an affirmative closure by this route requires the genuinely new large-scale
stability estimate

\[
\boxed{
\mathscr O(A)\ge c_0\pi D+a_0
}
\tag{21.22}
\]

for every sufficiently large triangle-free minimizer in the normalized rhombic/forest
regime, with the forest contribution included.  Equation (21.22) would imply

\[
\operatorname{area}(K)\ge a_0n+c_0(\pi D-P)\ge a_0n,
\]

contradicting \(D^2<cn\).

The bad train-track count by itself cannot prove (21.22).  The local constants
\(3\sqrt3/20\), (21.18), and (21.19) are all below the required coefficient
(21.21), and the face and pocket inequalities can be approached arbitrarily closely
by near-triangular geometry.  What remains is a quantitative *simultaneous stability*
theorem: near equality in the local Oler cells must be incompatible, at large scale,
with both the diametral-hull condition and near equality in the isodiametric bound.

This addendum therefore narrows Target B and supplies its exact topology-corrected
bookkeeping, but it closes neither Target A nor Target B.  The most promising next
step is to prove a joint Oler/isodiametric stability inequality in which shallow
pockets with near-unit hidden diagonals are charged either to a definite support-width
loss or to a feasible diameter-decreasing boundary motion.  Target A must enter that
same inequality, since (21.8) proves that plain area accounting assigns a forest vertex
exactly the same bulk allowance as a core vertex.

---

## 22. Exact track-end depth and defect-extended span

This section incorporates the second continuation run. It does not solve Level I, but it removes one previously unquantified class of train-track terminations from Target B and complements the Oler-surplus bookkeeping of Section 21. Its first lemma strengthens Lemma 21.3 by proving that every bounded contact face has a single simple boundary cycle, rather than assuming simplicity.

Continue in the triangle-free first-order-jammed branch and let
\(\mathcal R=\mathcal F_4\) be the full strict-rhombus face complex.  A boundary
edge of \(\mathcal R\) is called **face-terminated** if the contact face on its
non-rhombic side is bounded.  Let \(b_F\) be the number of face-terminated
rhombic boundary edges.

If a rhombic boundary edge \(e\) instead borders the unbounded contact face,
orient its unit normal \(\nu_e\) away from its incident rhombus and put

\[
 \rho_e=
 \max_{x\in A}\nu_e\cdot(x-m_e),
\]

where \(m_e\) is the midpoint of \(e\).  Thus \(\rho_e=0\) for a hull edge,
whereas \(\rho_e>0\) for a non-hull edge on the unbounded contact face.  Put

\[
 H_\infty=\sum_{e\text{ bordering the unbounded face}}\rho_e.
\]

### Lemma 22.1: bounded contact faces are strictly convex

Every bounded face of the contact graph has one simple boundary cycle and is a
strictly convex unit-sided polygon.

#### Proof

The straight unit-contact graph is plane.  At a vertex \(v\notin Q\), Theorem
8.2 says that the contact directions positively span the plane.  Equivalently,
every angular gap between consecutive contact rays is strictly smaller than
\(\pi\).  Every face angle at \(v\) is one of these gaps and is therefore less
than \(\pi\).

At a vertex \(v\in Q=V(\operatorname{conv}A)\), the tangent cone of the convex
hull has angle strictly smaller than \(\pi\), because \(v\) is an extreme
polygon vertex.  A bounded face lies locally inside the convex hull, so its
face angle at \(v\) is again smaller than \(\pi\).

A bounded plane-graph face with an inner boundary component, a bridge slit, or
a repeated boundary vertex necessarily has a reflex corner on one of its
boundary walks.  The preceding paragraph excludes this.  Hence the boundary
is one simple cycle, and all its interior angles are smaller than \(\pi\).
The face is therefore strictly convex.  Every one of its boundary edges is a
unit contact. \(\square\)

### Lemma 22.2: sharp width of a convex contact face

Let \(P\) be a convex unit-sided polygon whose distinct vertices are mutually
at distance at least \(1\).  Then

\[
 \boxed{\operatorname{width}(P)\ge\frac{\sqrt3}{2}.}
 \tag{22.1}
\]

In particular, measured normally from any side of \(P\), the opposite support
line is at distance at least \(\sqrt3/2\).

#### Proof

A minimum-width direction of a convex polygon is normal to one of its sides.
Put that unit side at

\[
 A=(0,0),\qquad B=(1,0),
\]

and suppose that the polygon lies in the strip \(0\le y\le w\).  If
\(w<\sqrt3/2\), set

\[
 a=\sqrt{1-w^2}>\frac12.
\]

For any two vertices, their vertical separation is at most \(w\), while their
Euclidean separation is at least \(1\).  Their horizontal coordinates are
therefore separated by at least \(a\).  No third vertex can have horizontal
coordinate strictly between those of \(A\) and \(B\), since it would be within
horizontal distance at most \(1/2<a\) of one of them.  Thus \(A,B\) are
consecutive in the ordering of all vertex coordinates by \(x\).

If the polygon has \(m\) vertices and horizontal span \(L\), the one gap from
\(A\) to \(B\) has length \(1\), and the other \(m-2\) gaps have length at
least \(a\).  Hence

\[
 L\ge1+(m-2)a.
\]

The two boundary arcs between a leftmost and a rightmost vertex each have
length at least \(L\).  Since the perimeter is \(m\),

\[
 m\ge2L\ge2+2(m-2)a.
\]

As \(m\ge3\), this implies \(a\le1/2\), a contradiction.  This proves
(22.1).  The constant is sharp, already for the unit equilateral triangle and
as a limiting constant for admissible equilateral polygons. \(\square\)

### Theorem 22.3: exact defect-extended train-span inequality

For each train track \(\tau\), let

\[
 L_\tau=\sum_{F\in\tau}\sin\theta_F.
\]

If \(s_F(\tau)\in\{0,1,2\}\) is the number of its end edges that are
face-terminated, then

\[
 \boxed{
 L_\tau+\frac{\sqrt3}{2}s_F(\tau)
 +\sum_{e\in\partial\tau,\ e\text{ on the unbounded face}}\rho_e
 \le D.
 }
 \tag{22.2}
\]

Consequently, since there are \(T=B_{\mathcal R}/2\) tracks and every rhombus
belongs to two tracks,

\[
 \boxed{
 \frac{B_{\mathcal R}}2D
 \ge
 2\sum_{F\in\mathcal R}\sin\theta_F
 +\frac{\sqrt3}{2}b_F+H_\infty,
 }
 \tag{22.3}
\]

or equivalently

\[
 \boxed{
 B_{\mathcal R}D
 \ge
 4\sum_{F\in\mathcal R}\sin\theta_F
 +\sqrt3\,b_F+2H_\infty.
 }
 \tag{22.4}
\]

This strictly refines (10.18).

#### Proof

Orient the transverse coordinate of a train as in Theorem 10.6.  Crossing a
rhombus increases that coordinate by exactly \(\sin\theta_F\), so the two end
edge midpoints differ in transverse coordinate by \(L_\tau\).

At a face-terminated end, Lemmas 22.1 and 22.2 provide a vertex of the bounded
contact face at transverse distance at least \(\sqrt3/2\) beyond the end-edge
line.  At an end bordering the unbounded contact face, the definition of
\(\rho_e\) provides a vertex of \(A\) at transverse distance \(\rho_e\) beyond
that line.  Choosing such a vertex at each end gives two points of \(A\) whose
transverse separation is at least the left side of (22.2).  Their Euclidean
distance is at most \(D\), proving (22.2).

Sum over all tracks.  Each rhombus is counted on its two tracks, every
face-terminated edge is one track end, and every unbounded-face end contributes
its \(\rho_e\) once.  This gives (22.3) and (22.4). \(\square\)

### Exact consequence and limitation

Every bad track end now has an explicit disposition:

1. a bounded-face end costs at least \(\sqrt3/2\) of additional transverse
   span;
2. a non-hull end on the unbounded contact face costs its exact positive depth
   \(\rho_e\);
3. a hull end has zero additional depth.

Thus bounded nonquadrilateral faces and bounded holes are no longer merely
combinatorial defect objects: they carry the sharp metric charge
\(\sqrt3/2\) per incident train end.  The five-sector complexes and the
11-point sun evade this conclusion in precisely the correct way: their hard
train ends lie on the nonconvex unbounded boundary, rather than in bounded
defect faces.

The new term is boundary order and does not by itself finish Target B.  With
\(B_{\mathcal R}\ge4\sqrt{F_4}\), the old product bound has order-\(n\) slack,
whereas the new contribution in (22.4) is only order \(\sqrt n\).  A closing
argument must therefore combine \(H_\infty\) and the bounded-face term with
actual convex-hull perimeter or parallel-body area; substituting only
\(\operatorname{span}(\tau)\le D\) still loses too much.

The exact remaining metric lemma after this continuation is an aggregate
outer-shell inequality that charges the compulsory non-hull unbounded-face
edges through their depths \(\rho_e\), their convexification area, and the
actual perimeter of \(\operatorname{conv}A\), with a coefficient strong enough
to beat the finite packing boundary slack.  Target A, the super-boundary
bridge-forest alternative, is unchanged.

---

## 23. Combined continuation frontier

Sections 21 and 22 attack the same boundary-scale obstruction from complementary sides. This section records the exact synthesis that should be treated as the current research frontier. It is a reduction and bookkeeping statement, not a Level I solution.

### 23.1 The bad train ends now have only two nontrivial dispositions

Continue in the triangle-free first-order-jammed branch and take the full strict-rhombus complex $\mathcal R=\mathcal F_4$. Let $b_F$ be the number of rhombic boundary edges whose non-rhombic side is a bounded contact face, and let $b_\infty$ be the number of non-hull rhombic boundary edges on the unbounded contact face. Then

\[
 b_F+b_\infty=b_{\mathcal R}\ge2\sqrt{F_4}-2=2\sqrt n-O(1).
\tag{23.1}
\]

A bounded-face end has a universal metric charge $\sqrt3/2$ in the transverse train-span inequality. An unbounded non-hull end has an exact positive depth $\rho_e$, and their aggregate is

\[
H_\infty=\sum_{e\text{ on the unbounded face}}\rho_e.
\tag{23.2}
\]

Thus the defect network can no longer hide a train end in an unquantified bounded face. The only soft escape is through many shallow non-hull ends on the unbounded face.

### 23.2 Directional train-width refinement

The proof of Theorem 22.3 yields a strictly stronger per-track inequality than the displayed diameter bound. Let $\nu_\tau$ be the oriented transverse unit normal of a train track and let

\[
w_K(\nu)=\max_{x\in K}\nu\cdot x-\min_{x\in K}\nu\cdot x
\]

be the width of $K=\operatorname{conv}A$ in direction $\nu$. The two witness points used in the proof of Theorem 22.2 belong to $A\subset K$, so their transverse separation is at most $w_K(\nu_\tau)$. Hence

\[
\boxed{
L_\tau+\frac{\sqrt3}{2}s_F(\tau)
+\sum_{e\in\partial\tau,\ e\text{ on the unbounded face}}\rho_e
\le w_K(\nu_\tau)\le D.
}
\tag{23.3}
\]

Summing over tracks gives the exact directional form

\[
\boxed{
\sum_\tau w_K(\nu_\tau)
\ge
2\sum_{F\in\mathcal R}\sin\theta_F
+\frac{\sqrt3}{2}b_F+H_\infty.
}
\tag{23.4}
\]

This is the most direct bridge between the two continuation runs. Cauchy's formula

\[
P=\int_0^\pi w_K(\phi)\,d\phi
\tag{23.5}
\]

controls the integral of the same width function, while the train geometry supplies a highly structured discrete multiset of directions. A closing argument may therefore be formulated as a sharp discrete-to-continuous width inequality rather than as another estimate involving only $D$.

### 23.3 Exact simultaneous inequalities for a surviving jammed counterexample

Such a counterexample must satisfy the Oler shell window

\[
G_{\mathcal R}+E_{\mathcal R}
\ge c_0(B-P)+a_0(t+\chi-1),
\tag{23.6}
\]

\[
G_{\mathcal R}+E_{\mathcal R}
<c_0B+a_0(t+\chi),
\tag{23.7}
\]

whose remaining allowance is exactly $c_0P+a_0$, together with the refined train inequality

\[
BD
\ge
4\sum_{F\in\mathcal R}\sin\theta_F
+\sqrt3\,b_F+2H_\infty.
\tag{23.8}
\]

For regular contact disks, the Oler surplus

\[
\mathscr O(A)=\operatorname{area}(K)+c_0P-a_0(n-1)
\tag{23.9}
\]

has the exact local decomposition

\[
\mathscr O(A)=\sum_F s_F+\sum_C s_C,
\tag{23.10}
\]

where the summands are nonnegative face and indentation-pocket slacks. For global minimizers,

\[
\mathscr O(A)<c_0\pi D+a_0,
\tag{23.11}
\]

and proving the reverse inequality for every sufficiently large triangle-free survivor would close the jammed branch.

### 23.4 The precise missing Target B theorem

The current Target B is no longer merely a generic ``sharp boundary-capacity theorem.'' A sufficient focused statement is:

> **Joint outer-shell stability theorem.** For every sufficiently large triangle-free global minimizer in the normalized jammed/almost-rhombic regime, the compulsory train-end data satisfy a quantitative inequality coupling $b_F$, $H_\infty$, the indentation-pocket slacks, the convexification area, and the actual hull perimeter strongly enough to force
> \[
> \mathscr O(A)\ge c_0\pi D+a_0.
> \]

Equivalently, near equality in the local Oler cells must be incompatible at large scale with both the diametral-hull condition $Q=V(\operatorname{conv}A)$ and near equality in the isodiametric/perimeter bounds.

A particularly promising route is to replace the final use of $\operatorname{span}(\tau)\le D$ by the actual hull width in the train's transverse direction and then aggregate those directional widths through the support function or Cauchy perimeter formula. The unbounded-face depth $\rho_e$ is already a support-function deficit:

\[
\rho_e=h_K(\nu_e)-\nu_e\cdot m_e
\]

for a non-hull outer train end. The missing step is therefore to convert the sum of these support deficits, together with the bounded-face charges, into the Oler/pocket surplus with a sharp enough coefficient.

### 23.5 Target A is now cleanly separated from plain area bookkeeping

The bridge-forest alternative remains:

\[
\ell=\dim\mathcal L_{\widehat Q}=\omega(\sqrt n).
\tag{23.12}
\]

Section 21 shows why simply adding forest vertices to the Oler area count cannot eliminate this branch: the topology/outside-vertex terms cancel from the global shell window. A successful Target A argument must therefore exploit information not visible to plain area alone, for example the configuration-space dimension of the forest, free volume, saturation by new constraints, or a coupling between forest occupancy and the same outer-shell support resources charged in Target B.

The most attractive unified endpoint would prove that every forest degree of freedom or every forest vertex consumes a definite amount of the same support-function/pocket budget appearing in the joint outer-shell stability theorem. Such a theorem would simultaneously force $\ell=O(\sqrt n)$ and close Target B on the resulting $n-O(\sqrt n)$ jammed core.

### 23.6 Current exact status

No Level I proof or disproof is established. The two remaining tasks are now:

1. **Target A:** rule out super-boundary-dimensional bridge-forest lineality, preferably by charging forest freedom to finite shell capacity;
2. **Target B:** prove the joint Oler/isodiametric/track-depth stability theorem above, with constants strong enough to exceed the global-minimizer allowance.

Sections 21--23 supersede the less quantitative formulation of the Target B endpoint in Sections 18--19. The older statements remain valid, but the present formulation is the sharper continuation state.

---

# 24. Perimeter saturation and the linear support-depth theorem

Throughout, let

\[
K=\operatorname{conv}A,\qquad
P=\operatorname{per}(K),\qquad
D=D(n),
\]

and use

\[
a_0=\frac{\sqrt3}{2},
\qquad
c_0=\frac{\sqrt3}{4},
\qquad
c=\frac{2\sqrt3}{\pi},
\qquad
C_0=\sqrt{2\pi\sqrt3}.
\]

The following results were obtained in the subsequent continuation and are to be treated as part of the established research state.

## 24.1 Perimeter lower bound for every global minimizer

Every global minimizer satisfies

\[
\boxed{
P\ge
\sqrt{
C_0^2(n-1)+\frac{3\pi^2}{4}
}
-\frac{\pi\sqrt3}{2}.
}
\tag{24.1}
\]

Together with Cauchy's perimeter-diameter inequality \(P\le \pi D\) and the
strict \(n-1\) lattice bound of Section 36, this in fact gives the uniform strict
estimate

\[
\boxed{
0\le \pi D-P
<
\frac{\pi\sqrt3}{2}
=
2.7206990463\ldots .
}
\tag{24.2}
\]

Thus the convex hull of a global minimizer has perimeter within an absolute \(O(1)\) error of the maximum possible perimeter for its diameter.

This is a much stronger global statement than the previous \(P=O(D)\).

**Audit derivation.** Finite Oler gives

\[
\operatorname{area}(K)+c_0P\ge a_0(n-1),
\]

while the planar isoperimetric inequality gives

\[
\operatorname{area}(K)\le\frac{P^2}{4\pi}.
\]

Therefore

\[
P^2+4\pi c_0P-4\pi a_0(n-1)\ge0,
\]

and the positive quadratic root is exactly (24.1). The strict translated-lattice
bound of Section 36 gives \(\pi D<C_0\sqrt{n-1}\). Since
\[
\sqrt{C_0^2(n-1)+3\pi^2/4}>C_0\sqrt{n-1},
\]
subtracting (24.1) yields the strict estimate (24.2) directly.

## 24.2 Uniform width saturation

Let \(w_K(\phi)\) denote the width of \(K\) in direction \(\phi\).

The bounded perimeter deficit implies

\[
\boxed{
\min_\phi w_K(\phi)
=
D-O(n^{1/6}).
}
\tag{24.3}
\]

Since \(D=\Theta(\sqrt n)\),

\[
w_K(\phi)=D-o(D)
\]

uniformly in direction.

Thus every surviving global minimizer is asymptotically constant-width at the scale relevant to the rhombic train system.


**Audit derivation.** Let \(m=\min w_K\) and put \(L=K-K\). Then \(L\) is centrally
symmetric, \(L\subset B(0,D)\), and

\[
h_L(u)=w_K(u).
\]

In a direction attaining \(m\), central symmetry therefore places \(L\) inside the
strip \(|u\cdot x|\le m\). Brunn--Minkowski gives

\[
\operatorname{area}(L)\ge4\operatorname{area}(K).
\]

Hence \(4\operatorname{area}(K)\) is at most the area of the radius-\(D\) disk with
the two caps beyond \(|u\cdot x|=m\) removed. If \(\delta=D-m\), one such cap has
area

\[
D^2\arccos\frac mD-m\sqrt{D^2-m^2}
\asymp
D^{1/2}\delta^{3/2}
\]

for \(\delta=o(D)\). Since Section 36 and Oler give

\[
\frac{\pi D^2}{4}-\operatorname{area}(K)=O(D),
\]

we obtain \(D^{1/2}\delta^{3/2}=O(D)\), hence

\[
\delta=O(D^{1/3})=O(n^{1/6}).
\]

This proves (24.3) without assuming smoothness of the hull.

## 24.3 Exact support depth of a train end

For a rhombic boundary edge \(e\), let \(\nu_e\) be its outward unit normal and \(m_e\) its midpoint. Define its support depth

\[
\boxed{
d_e
=
h_K(\nu_e)-\nu_e\cdot m_e.
}
\tag{24.4}
\]

For a train track \(\tau\), whose two end edges are \(e_-,e_+\), let

\[
L_\tau
=
\sum_{F\in\tau}\sin\theta_F.
\]

Then the train span is exactly

\[
\boxed{
w_K(\nu_\tau)
=
L_\tau+d_{e_-}+d_{e_+}.
}
\tag{24.5}
\]

Summing over all tracks gives

\[
\boxed{
\sum_\tau w_K(\nu_\tau)
=
2\sum_F\sin\theta_F+H_*,
}
\tag{24.6}
\]

where

\[
\boxed{
H_*=\sum_{e\in\partial\mathcal R}d_e.
}
\tag{24.7}
\]

This completes the earlier directional train-width inequality to an equality.

## 24.4 Linear support-depth budget

Every sufficiently large triangle-free jammed survivor satisfies

\[
\boxed{
H_*
\ge
\left(
2\sqrt{\frac{2\sqrt3}{\pi}}-\sqrt3
\right)n
-
O(n^{2/3}).
}
\tag{24.8}
\]

Numerically,

\[
\boxed{
H_*
\ge
0.3680994640\ldots\,n
-
O(n^{2/3}).
}
\tag{24.9}
\]

Equivalently,

\[
\boxed{
\frac{H_*}{D}
\ge
0.3505458338\ldots\sqrt n-o(\sqrt n).
}
\tag{24.10}
\]

This is an order-\(n\) support-depth constraint.

**Audit derivation of (24.8).** For the full rhombic core,
\(T=B/2=O(D)\) and Mantel gives \(T\ge2\sqrt R\). Uniform width saturation and the
exact train identity give

\[
H_*
\ge
T\bigl(D-O(D^{1/3})\bigr)
-2\sum_F\sin\theta_F.
\]

Moreover

\[
2\sum_F\sin\theta_F
=\sqrt3R+O(D),
\qquad
R=n-O(D),
\qquad
D=\sqrt{cn}+O(1).
\]

Therefore

\[
H_*
\ge
2\sqrt R\,D-\sqrt3R-O(D^{4/3})
=
(2\sqrt c-\sqrt3)n-O(n^{2/3}),
\]

which is (24.8).

## 24.5 Deep-end tail: audit disposition

The earlier continuation recorded a specific numerical lower bound on the number of
macroscopically deep train ends. On second audit, that numerical statement was not
self-contained at this stage because a lower bound on the number of boundary ends is
not, by itself, an upper bound on how widely support depth can be distributed.

The underlying total-depth theorem (24.8)--(24.10) **is retained**. In the pure
rhombic-disk branch, the later audited phase/exposed-hull theorem gives the stronger
bound

\[
\frac{T}{D}\ge 2.5395008183\ldots+o(1),
\]

which in turn yields a rigorous and substantially stronger support-depth tail theorem.
That theorem is proved in Section 44. Thus the old constants are not used as an
independent premise anywhere in v1.0.0.

## 24.6 Important negative conclusion: raw depth is not Oler currency

The coefficient in (24.9) does not directly close the finite packing inequality.

If one attempted a scalar conversion

\[
\mathscr O(A)
\ge
\Lambda \frac{H_*}{D}
-o(\sqrt n),
\]

then the previously identified Oler threshold would require

\[
\boxed{
\Lambda>4.0749855583\ldots.
}
\tag{24.13}
\]

No such valid scalar conversion was obtained.

More strongly, explicit near-equilateral triangular or pentagonal indentation geometries show that a train end can be macroscopically deep while the associated local Oler slack tends to zero.

Therefore:

> **Raw support depth is not an independent positive contribution to Oler surplus.**

Any successful use of \(H_*\) must exploit global transport, support turning, diametral-hull geometry, train coherence, or a variational obstruction.

---

# 25. Exact support-turning and mixed-area identities

The next continuation completed the support-depth bookkeeping. These results supersede any attempt to count \(H_*\) as an independent shell surplus.

For clarity, write the full support depth as

\[
\rho_e^K
=
h_K(\nu_e)-\nu_e\cdot m_e.
\]

This is the same geometric quantity as \(d_e\) above.

## 25.1 Exact train equality

For every finite edge-to-edge strict unit-rhombus complex \(\mathcal R\subset K\),

\[
\boxed{
w_K(\nu_\tau)
=
L_\tau+\rho_{e_-}^K+\rho_{e_+}^K.
}
\tag{25.1}
\]

Hence

\[
\boxed{
\sum_\tau w_K(\nu_\tau)
=
2\sum_{F\in\mathcal R}\sin\theta_F
+
H_\partial^K,
}
\tag{25.2}
\]

where

\[
H_\partial^K
=
\sum_{e\in\partial\mathcal R}\rho_e^K.
\]

## 25.2 Pocket support-turning defect

In the pure rhombic-disk case, consider one indentation pocket \(C\).

Suppose its unit-edge chain has outward normals

\[
\nu_1,\ldots,\nu_r
\]

and its closing hull chord has length \(L\) and outward normal \(n\).

Define

\[
\boxed{
\mathfrak J(C)
=
\sum_{i=1}^r h_K(\nu_i)
-
Lh_K(n).
}
\tag{25.3}
\]

Support-function sublinearity gives

\[
\boxed{
\mathfrak J(C)\ge0.
}
\tag{25.4}
\]

The exact pocket identity is

\[
\boxed{
\sum_{i=1}^r \rho_{e_i}^K
=
2\operatorname{area}(C)
+
\mathfrak J(C).
}
\tag{25.5}
\]

The proof uses

\[
\sum_i\nu_i=Ln
\]

and the signed Green identity

\[
\sum_i\nu_i\cdot m_{e_i}
-
Ln\cdot m_f
=
-2\operatorname{area}(C).
\]

## 25.3 Global pure-disk identity

Let

\[
G=
\operatorname{area}(K)
-
\sum_{F\in\mathcal R}\operatorname{area}(F)
\]

be the total convexification/pocket area and put

\[
\mathfrak J
=
\sum_C\mathfrak J(C).
\]

Then

\[
\boxed{
H_\partial^K
=
2G+\mathfrak J.
}
\tag{25.6}
\]

Combining with the train equality gives

\[
\boxed{
\sum_\tau w_K(\nu_\tau)
=
2\operatorname{area}(K)+\mathfrak J.
}
\tag{25.7}
\]

This is the exact cancellation hidden in the raw support-depth theorem.

## 25.4 Train zonotope formulation

For every train \(\tau\), let \(u_\tau\) be its unit edge direction and define the train zonotope

\[
\boxed{
Z=
\sum_\tau
[-u_\tau/2,u_\tau/2].
}
\tag{25.8}
\]

Then

\[
\boxed{
\operatorname{per}(Z)=B,
}
\tag{25.9}
\]

where \(B\) is the rhombic boundary-edge count.

Mixed area gives

\[
\boxed{
2V(K,Z)
=
\sum_\tau w_K(\nu_\tau).
}
\tag{25.10}
\]

Therefore, in the pure rhombic-disk case,

\[
\boxed{
\mathfrak J
=
2\bigl(
V(K,Z)-\operatorname{area}(K)
\bigr).
}
\tag{25.11}
\]

Thus the order-\(n\) support-turning mass is a mixed-area excess.

## 25.5 Global area and perimeter deficits

For every global minimizer, with no triangle-free or rigidity hypothesis, the later
translated-lattice \(n-1\) improvement in Section 36 strengthens the area-deficit
estimate to

\[
\boxed{
\frac{\pi D^2}{4}
-
\operatorname{area}(K)
<
c_0P.
}
\tag{25.12'}
\]

This supersedes the earlier bound \(c_0\pi D+a_0\).

Also, the stronger pointwise form of Section 24 is

\[
\boxed{
0\le
\pi D(n)-\operatorname{per}(\operatorname{conv}A)
<
\frac{\pi\sqrt3}{2}
}
\tag{25.13}
\]

for every global minimizer in the range where the finite Oler formulation applies.
Thus both the isodiametric area deficit and the perimeter deficit are sharply controlled at boundary scale or better.

## 25.6 Exact cancellation identity

Define

\[
\mathfrak M(K)
=
\frac{DP}{2}
-
2\operatorname{area}(K)
\ge0
\tag{25.14}
\]

The nonnegativity is itself exact. Let \(L=K-K\). Brunn--Minkowski gives
\(\operatorname{area}(L)\ge4\operatorname{area}(K)\). Since \(L\) is centrally
symmetric and has circumradius at most \(D\), its support function satisfies
\(h_L\le D\). The planar Minkowski area formula then gives

\[
\operatorname{area}(L)
=\frac12\int h_L\,dS_L
\le \frac D2\operatorname{per}(L)
=DP,
\]

because \(\operatorname{per}(K-K)=2P\). Hence
\(4\operatorname{area}(K)\le DP\), which is exactly \(\mathfrak M(K)\ge0\).

and

\[
\Delta_\tau
=
\sum_\tau
\left(
D-w_K(\nu_\tau)
\right)
\ge0.
\tag{25.15}
\]

Then

\[
\boxed{
\mathfrak J
=
\frac D2(B-P)
+
\mathfrak M(K)
-
\Delta_\tau.
}
\tag{25.16}
\]

This equation explains exactly why the large support-depth term cannot simply be added to the Oler shell budget: support turning and train-width deficit cancel it.

## 25.7 Sharpened exact contradiction threshold

The support/perimeter bookkeeping first improved the sufficient Oler contradiction
threshold from

\[
\mathscr O(A)\ge c_0\pi D+a_0
\]

to

\[
\mathscr O(A)\ge c_0P+a_0.
\]

Section 36 subsequently removes the remaining \(+a_0\) by proving the stronger
translated-lattice bound

\[
D(n)^2<\frac{2\sqrt3}{\pi}(n-1).
\]

Hence the current exact sufficient threshold is

\[
\boxed{
\mathscr O(A)\ge c_0P.
}
\tag{25.17'}
\]

This is the threshold that should be used from now on.

## 25.8 Exact remaining Target B lemma in the pure rhombic-disk case

Let

\[
E=
\sum_{F\in\mathcal R}
\left(
\sin\theta_F-a_0
\right).
\]

The strengthened shell window from Section 36 gives, for every pure rhombic-disk
global minimizer,

\[
\boxed{
G+E<c_0B.
}
\tag{25.18'}
\]

Therefore a sufficient contradiction is now simply

\[
\boxed{
G+E\ge c_0B.
}
\tag{25.19'}
\]

Equivalently, using

\[
H_\partial^K-\mathfrak J=2G,
\]

it is enough to prove

\[
\boxed{
2E+H_\partial^K-\mathfrak J
\ge
a_0B.
}
\tag{25.20'}
\]

The former \(+a_0\) term is obsolete.

The general topology-corrected version must still incorporate:

- bounded nonquadrilateral faces;
- holes;
- multiple rhombic components;
- vertices outside the rhombic core;
- the bridge-forest residue.

## 25.9 Order-\(n\) support turning has zero guaranteed Oler coefficient

Since

\[
H_\partial^K=2G+\mathfrak J
\]

and \(G\) is only boundary order in the relevant regime, (24.9) implies

\[
\boxed{
\mathfrak J
\ge
\bigl(0.3680994640\ldots+o(1)\bigr)n.
}
\tag{25.21}
\]

This is a genuine order-\(n\) support-turning mass.

However, after the exact subtraction in the Oler identity, the guaranteed usable Oler-surplus coefficient contributed by this term is

\[
\boxed{0.}
\tag{25.22}
\]

This is a decisive strategic correction.

The next proof must work with the residual

\[
\boxed{
H_\partial^K-\mathfrak J=2G,
}
\]

not with \(H_\partial^K\) alone.

---

# 26. Further deductions developed after Sections 24–25

The results in this section were derived from the established theorem stack during the continuation in ChatGPT. They are included because they appear structurally important.

Where a result has not yet received the same adversarial audit as Sections 24–25, that is stated explicitly.

---

## 26.1 Sixfold phase energy of the train graph

For every train \(\tau\), let

\[
\phi_\tau\in\mathbb R/\pi\mathbb Z
\]

be its unoriented edge direction and define

\[
\boxed{
z_\tau=e^{6i\phi_\tau}.
}
\tag{26.1}
\]

If tracks \(\tau,\sigma\) cross, their rhombus has acute angle

\[
\theta_{\tau\sigma}
=
\frac\pi3+\delta_{\tau\sigma}.
\]

Therefore

\[
\frac{z_\sigma}{z_\tau}
=
e^{\pm6i\delta_{\tau\sigma}}
\]

and

\[
|z_\tau-z_\sigma|
\le
6\delta_{\tau\sigma}.
\]

Since \(0<\delta\le\pi/6\),

\[
|z_\tau-z_\sigma|^2
\le
6\pi\delta_{\tau\sigma}.
\]

Summing over crossings gives

\[
\boxed{
\sum_{\tau\sigma\in E(\Gamma)}
|z_\tau-z_\sigma|^2
\le
6\pi\sum_F\delta_F
=
O(D).
}
\tag{26.2}
\]

Since

\[
|E(\Gamma)|=F_4=\Theta(D^2),
\]

the average sixfold phase energy per crossing is \(O(D^{-1})\).

This converts the local statement “almost every rhombus is nearly \(60^\circ\)” into a global coherence constraint on train orientations.

### Status

The derivation of (26.2) is elementary from the established angular-defect theorem.

---

## 26.2 Macroscopic grain decomposition

Fix \(0<\eta<1\).

Delete every train crossing with

\[
\delta_{\tau\sigma}>D^{-1+\eta}.
\]

Because

\[
\sum\delta_{\tau\sigma}=O(D),
\]

only

\[
O(D^{2-\eta})=o(D^2)
\]

crossings are deleted.

Next repeatedly delete any track of current degree \(<\lambda D\), for fixed \(\lambda>0\).

Since there are \(T=O(D)\) tracks, this deletes at most

\[
O(\lambda D^2)
\]

additional crossings.

Every surviving component has minimum degree \(\lambda D\), while containing only \(O(D)\) tracks. A shortest-path neighborhood argument therefore bounds its graph diameter by \(O_\lambda(1)\).

Consequently all tracks in one surviving component have sixfold phases differing by

\[
O_\lambda(D^{-1+\eta}).
\]

Thus every component has a phase \(\phi_0\) such that

\[
\boxed{
\phi_\tau
=
\phi_0
+
k_\tau\frac\pi3
+
O_\lambda(D^{-1+\eta})
\pmod\pi,
\qquad
k_\tau\in\{0,1,2\}.
}
\tag{26.3}
\]

Hence, for every fixed \(\varepsilon>0\), after deleting at most \(\varepsilon n+o(n)\) rhombi, the remaining rhombic bulk is a bounded number of macroscopic grains, each asymptotically aligned with one triangular-lattice orientation modulo \(60^\circ\).

A quantitative choice such as defect cutoff \(D^{-2/3}\) yields an all-but-\(O(n^{5/6})\) version with \(O(n^{1/6})\) components and phase error \(O(D^{-1/3})\).

### Status

This is a direct graph-theoretic consequence of (26.2) and the already established \(T=O(D)\) train bound. It should nevertheless receive a short audit before being promoted into the core report.

---

## 26.3 Scalar phase-potential structure inside a grain

Choose local representatives of the three direction classes as

\[
A:\quad \phi=a,
\]

\[
B:\quad \phi=\frac\pi3+b,
\]

\[
C:\quad \phi=\frac{2\pi}3+c,
\]

where the offsets are small.

Then strict triangle-freeness gives, at a crossing,

\[
A\text{-}B:
\qquad
b-a>0,
\]

\[
B\text{-}C:
\qquad
c-b>0,
\]

\[
C\text{-}A:
\qquad
a-c>0.
\tag{26.4}
\]

Thus crossing incidences inside a coherent grain can be oriented by a genuine scalar phase potential.

Any directed cycle in this induced inequality system is impossible.

This is a promising way to replace arbitrary defect transport by an ordered continuation network.

### Status

The local sign calculation is exact. Its strongest global combinatorial consequence has not yet been fully extracted.

---

## 26.4 Train zonotope: missing crossings and mixed area

For the train zonotope

\[
Z=
\sum_\tau[-u_\tau/2,u_\tau/2],
\]

one has

\[
\operatorname{area}(Z)
=
\sum_{\tau<\sigma}
|\det(u_\tau,u_\sigma)|.
\tag{26.5}
\]

Let

\[
S=
\sum_{F\in\mathcal R}\sin\theta_F
\]

and define the missing-crossing determinant mass

\[
M
=
\sum_{\substack{\tau<\sigma\\
\tau,\sigma\text{ do not cross}}}
|\det(u_\tau,u_\sigma)|.
\]

Because each crossing pair contributes exactly one rhombus,

\[
\boxed{
\operatorname{area}(Z)
=
S+M.
}
\tag{26.6}
\]

Combined with (25.10),

\[
2V(K,Z)
=
2S+H_\partial^K.
\]

Thus both support depth and missing train crossings have exact convex-geometric interpretations.

---

## 26.5 Exact zonotope anisotropy identity

Define

\[
C_k
=
\sum_\tau e^{2ik\phi_\tau}.
\]

The Fourier expansion of the zonotope support function gives

\[
\boxed{
\operatorname{per}(Z)^2
-
4\pi\operatorname{area}(Z)
=
8\sum_{k\ge1}
\frac{|C_k|^2}{4k^2-1}.
}
\tag{26.7}
\]

In a hexatically coherent grain,

\[
|C_3|
=
(1-o(1))T_{\rm grain}.
\]

Therefore its zonotopal completion obeys

\[
\boxed{
P_Z^2
-
4\pi A_Z
\ge
\frac8{35}
(1-o(1))
T_{\rm grain}^2.
}
\tag{26.8}
\]

So a macroscopic triangularly coherent grain has a quantitatively anisotropic zonotopal completion, even though the true minimizing hull satisfies

\[
P(K)=\pi D-O(1)
\]

and is asymptotically constant-width.

### Strategic interpretation

A large survivor must reconcile strongly anisotropic crystalline train systems with an almost constant-width diametral hull through only a boundary-order defect network.

Scalar mixed-area inequalities alone appear too weak; the missing information is the **incidence/transport structure** of the trains.

---

## 26.6 Train-angle realization modes

A pure rhombic complex admits train-coordinate realizations.

Choose a side label

\[
\epsilon_\tau(v)\in\{0,1\}
\]

for each vertex relative to every train.

Up to translation,

\[
p_v
=
\sum_\tau
\epsilon_\tau(v)u_\tau.
\tag{26.9}
\]

Replacing each train vector \(u_\tau\) independently by another unit vector preserves every rhombic contact length.

Thus an unconstrained pure rhombic complex carries one angle parameter per train.

Modulo global Euclidean motions, this suggests at least

\[
\boxed{
T-1
}
\tag{26.10}
\]

independent train-angle modes before the defect/hull shell constraints are imposed.

### Strategic interpretation

The \(n-O(D)\) rhombic bulk carries \(\Theta(D)\) natural shear modes, and the \(O(D)\)-scale hull/defect structure must lock them all.

### Status

The train-coordinate representation is standard for simply connected rhombic tilings. Extension across holes, multiple components, and all topologies in the full survivor requires explicit hypothesis management before this becomes a universal theorem.

---

## 26.7 Difference-body transport bound for a convex defect face

Let \(F\) be a convex unit-sided contact face.

For each side \(e\), let \(\nu_e\) be its outward normal.

Then the polygonal mixed-area formula gives

\[
\boxed{
\sum_{e\subset\partial F}
w_F(\nu_e)
=
\operatorname{area}(F-F).
}
\tag{26.11}
\]

The planar Rogers-Shephard difference-body inequality gives

\[
\boxed{
\operatorname{area}(F-F)
\le
6\operatorname{area}(F).
}
\tag{26.12}
\]


For completeness, the planar constant \(6\) can be derived self-containedly. Put
\(C=F-F\) and

\[
f(x)=\operatorname{area}(F\cap(F+x)),
\qquad x\in C.
\]

Fubini gives

\[
\int_C f(x)\,dx=\operatorname{area}(F)^2.
\]

Moreover \(g=f^{1/2}\) is concave on \(C\): for \(x,y\in C\), convexity gives

\[
(1-t)(F\cap(F+x))+t(F\cap(F+y))
\subseteq
F\cap(F+((1-t)x+ty)),
\]

and planar Brunn--Minkowski yields concavity of square roots of areas. Along every
ray from \(0\) to \(\partial C\),

\[
g(rx)\ge(1-r)g(0),
\qquad 0\le r\le1.
\]

Integrating the square of this cone lower bound over homothetic shells \(rC\) gives

\[
\int_C f(x)\,dx
\ge
\frac16\operatorname{area}(F)\operatorname{area}(C).
\]

Comparison with the Fubini identity proves (26.12). Thus no external use of the
full Rogers--Shephard theorem is needed here.

Hence

\[
\boxed{
\sum_{e\subset\partial F}
w_F(\nu_e)
\le
6\operatorname{area}(F).
}
\tag{26.13}
\]

A weighted analogue applies to an outer convex pocket: the unit-edge chain cannot absorb more than a constant multiple of the pocket area in local transverse width.

### Consequence

A boundary-order amount of defect-face/pocket area can absorb only boundary-order local width.

Therefore the order-\(n\) global support-depth mass cannot be interpreted as order-\(n\) *local defect-cell width*. Most depth is transported globally through the rhombic body.

This reinforces the exact cancellation in Section 25.

---

## 26.8 Correction: large \(H_*\) is not itself anomalous

A disk-like family of chord tracks naturally has quadratic total support-depth deficit.

For a Euclidean disk of radius \(R=D/2\), a unit-spaced parallel family has asymptotic missing span

\[
\int_{-R}^{R}
\left(
2R-2\sqrt{R^2-x^2}
\right)\,dx
=
(4-\pi)R^2.
\tag{26.14}
\]

Thus one family naturally contributes

\[
\left(1-\frac\pi4\right)D^2,
\]

and two such families contribute

\[
\boxed{
\left(
2-\frac\pi2
\right)D^2
=
0.4292036\ldots D^2.
}
\tag{26.15}
\]

The Section 24 lower bound is only approximately

\[
0.3338\,D^2.
\]

Therefore a quadratic \(H_*\) is compatible with ordinary disk-like geometry.

The anomaly is not the **amount** of raw depth; it is the need to realize it simultaneously with:

- strict triangle-freeness;
- almost-equilateral rhombi;
- diametral hull vertices;
- near-constant width;
- exact global diameter optimality;
- boundary-order Oler budget;
- locking of all train/shear modes.

This correction should be treated as a regression test against future scalar-depth arguments.

---

## 26.9 Fixed-oblique-lattice scaling heuristic

Suppose a large relevant region really lies in a single rank-two unit lattice generated by two unit vectors at angle

\[
\theta>\frac\pi3.
\]

The fundamental-cell area is

\[
s=\sin\theta>a_0.
\]

A finite lattice-polygon capacity estimate of Pick/Oler type gives schematically

\[
n
\lesssim
\frac{\pi D^2}{4\sin\theta}
+
O(D).
\]

Combining with the global competitor

\[
D^2<\frac{2\sqrt3}{\pi}n
\]

forces

\[
\boxed{
\theta-\frac\pi3
=
O(D^{-1}).
}
\tag{26.16}
\]

This identifies the natural final scale:

\[
\boxed{
\delta\asymp D^{-1}.
}
\]

Bulk density loss from a positive shear and boundary-order gains compete exactly at this scale.

### Status

This scaling conclusion is highly plausible and consistent with the exact capacity calculations. Any use of the precise finite-lattice formula or lattice-point constants should be independently checked before becoming part of the trusted theorem stack.

---

# 27. Historical post-synthesis route log

The intermediate Sections 27--35 of the pre-v1 addendum were strategic working
notes rather than independent theorem blocks. Their surviving mathematical content
is retained elsewhere in this report:

- raw support depth is quadratic but is cancelled by support turning and cannot be
  converted directly into Oler surplus;
- low-slack defect cells should be viewed as train continuation/merge structures,
  not as local scalar penalties;
- the sixfold phase energy motivates a polycrystalline decomposition into
  near-triangular grains;
- pure rhombic disks carry train-angle realization modes that must be locked by the
  boundary shell;
- Target A remains the separate super-boundary bridge-forest problem;
- the essential regression examples are the unit square, the \(n=8\) rattler,
  regular odd-prime shells, dense shell fillings, five-sector \(C_5\) complexes,
  the 11-point sun, near-equilateral low-slack pockets, and disk-like chord depth.

The old numerical thresholds and "current frontier" language from those sections
are superseded by Sections 38--48 below and are intentionally not duplicated here.

---

# 36. Translated-lattice \(n-1\) improvement

This section records a later exact improvement that supersedes every previous
\(n\)-based triangular-lattice upper bound in the report.

## 36.1 Strict \(n-1\) diameter upper bound

Let \(\Lambda\) be the unit triangular lattice, whose fundamental-cell area is

\[
a_0=\frac{\sqrt3}{2}.
\]

Choose an open disk \(B_r\) so that the average number of lattice points in a
translated copy is exactly \(n-1\):

\[
\frac{\pi r^2}{a_0}=n-1.
\]

Periodize the indicator of \(B_r\) over \(\Lambda\).  The resulting translated
lattice-point count is integer valued and has mean \(n-1\).

It is not constant.  Indeed, choose a generic point of one circular boundary
away from all pairwise boundary intersections.  Crossing that boundary changes
the periodized count by exactly one locally.

An integer-valued nonconstant function with integer mean \(n-1\) must exceed its
mean somewhere.  Hence some translate of the open disk contains at least \(n\)
lattice points.

Any \(n\) of them are unit-separated and, because the disk is open, have
diameter strictly less than \(2r\).  Therefore

\[
\boxed{
D(n)
<
\sqrt{\frac{2\sqrt3}{\pi}(n-1)}.
}
\tag{36.1}
\]

Equivalently,

\[
\boxed{
D(n)^2
<
c(n-1),
\qquad
c=\frac{2\sqrt3}{\pi}.
}
\tag{36.2}
\]

This is unconditional.

## 36.2 Topology-corrected shell consequence

For a rhombic complex \(\mathcal R\), recall

\[
n=R+\frac B2+\chi+t,
\]

and

\[
\operatorname{area}(K)
=
a_0R+E_{\mathcal R}+G_{\mathcal R}.
\]

The isodiametric inequality and (36.2) give

\[
\operatorname{area}(K)
<
a_0(n-1).
\]

Hence

\[
\boxed{
G_{\mathcal R}+E_{\mathcal R}
<
c_0B+a_0(t+\chi-1).
}
\tag{36.3}
\]

Combined with the existing Oler lower side,

\[
G_{\mathcal R}+E_{\mathcal R}
\ge
c_0(B-P)+a_0(t+\chi-1),
\]

the exact remaining shell window becomes

\[
\boxed{
c_0(B-P)+a_0(t+\chi-1)
\le
G_{\mathcal R}+E_{\mathcal R}
<
c_0B+a_0(t+\chi-1).
}
\tag{36.4}
\]

Its width is exactly

\[
\boxed{c_0P.}
\tag{36.5}
\]

All previous \(+a_0\) closing thresholds are superseded.

## 36.3 Pure rhombic disk

For \(t=0,\chi=1\),

\[
\boxed{
c_0(B-P)
\le
G+E
<
c_0B.
}
\tag{36.6}
\]

Thus the exact sufficient contradiction is

\[
\boxed{
G+E\ge c_0B.
}
\tag{36.7}
\]

## 36.4 Oler-surplus and area-deficit consequences

The Oler surplus

\[
\mathscr O(A)
=
\operatorname{area}(K)+c_0P-a_0(n-1)
\]

satisfies

\[
\boxed{
0\le\mathscr O(A)<c_0P.
}
\tag{36.8}
\]

Also,

\[
\boxed{
\frac{\pi D^2}{4}
-
\operatorname{area}(K)
<
c_0P.
}
\tag{36.9}
\]

The Cartesian-block restriction sharpens correspondingly to

\[
\boxed{
ab+
\frac{4\sqrt3-6}{\pi}\Delta_{a,b}
<
\frac2\pi(n-1).
}
\tag{36.10}
\]

---

# 37. Train-angle Hessian and the exact backward-train mechanism

This section records the exact second-variation identities found by projecting the
diameter objective into train-angle coordinates.

Assume for this section a simply connected pure rhombic disk so that standard
train coordinates are available.

Let

\[
u_\tau=(\cos\phi_\tau,\sin\phi_\tau)
\]

be the unit edge vector of train \(\tau\).

For vertices \(i,j\), write

\[
r=p_i-p_j
=
\sum_\tau d_\tau u_\tau,
\qquad
d_\tau\in\{-1,0,1\}.
\]

Let

\[
f_{ij}(\phi)
=
\frac12|r|^2.
\]

## 37.1 Exact Hessian trace

Let

\[
k_{ij}
=
\#\{\tau:d_\tau\ne0\}.
\]

Differentiation with respect to the independent train angles gives

\[
\boxed{
\operatorname{tr}\nabla_\phi^2 f_{ij}
=
k_{ij}-|p_i-p_j|^2.
}
\tag{37.1}
\]

For an active diameter pair,

\[
|p_i-p_j|=D,
\]

hence

\[
\boxed{
\operatorname{tr}\nabla_\phi^2 f_{ij}
=
k_{ij}-D^2
\le
T-D^2
=
-\Theta(D^2).
}
\tag{37.2}
\]

Thus each active diameter function is strongly superharmonic in aggregate on the
train-angle space.

## 37.2 Exact signed-variance formula

Put

\[
a_\tau=d_\tau u_\tau,
\qquad
\lambda_\tau=r\cdot a_\tau.
\]

For an angle velocity \(v=(v_\tau)\), set

\[
c=\sum_\tau v_\tau a_\tau.
\]

The first variation of the diameter vector is \(Jc\). First-order neutrality is

\[
r\cdot Jc=0.
\]

In the plane this means \(c\) is parallel to \(r\). Since

\[
r\cdot c=\sum_\tau\lambda_\tau v_\tau,
\]

write

\[
\bar v=
\frac{1}{D^2}\sum_\tau\lambda_\tau v_\tau,
\qquad
c=\bar v\,r.
\]

Using \(\sum_\tau\lambda_\tau=D^2\), the exact second variation is

\[
\boxed{
\mathrm d^2f_{ij}[v,v]
=
-\sum_\tau
\lambda_\tau(v_\tau-\bar v)^2.
}
\tag{37.3'}
\]

This identity is valid with arbitrary signs of \(\lambda_\tau\). If every
\(\lambda_\tau\ge0\), it is nonpositive; equality requires common angular velocity
on all trains with positive \(\lambda_\tau\).

## 37.3 What backward and tangent trains can do

A separating train is **backward** for the diameter pair if

\[
\boxed{
\lambda_\tau=d_\tau\,r\cdot u_\tau<0.
}
\tag{37.4}
\]

Equation (37.3') shows that **positive quadratic curvature requires at least one
backward incidence whose deviation \(v_\tau-\bar v\) is nonzero**.

The second-pass audit corrects an earlier overstatement: this does *not* classify all
higher-order locking. A separating train with

\[
d_\tau\ne0,
\qquad
\lambda_\tau=0
\]

is tangent to the diameter vector and contributes no quadratic sign, but balanced
classes of such tangent trains can block at quartic order. That exact mechanism is
proved in Section 43. A train with \(d_\tau=0\) is instead invisible to this particular
diameter bar at every order.

## 37.4 Coordinate-flip obstruction

If \(a_\tau=d_\tau u_\tau\) is backward, then

\[
|r-a_\tau|^2
=
D^2+1-2r\cdot a_\tau
>
D^2.
\tag{37.6}
\]

Hence the coordinate-flipped extreme vertex cannot exist while all other train
coordinates are held fixed; otherwise the configuration would already contain a
pair longer than \(D\).

This gives the geometric interpretation of backwardness:

> a backward train certifies a missing train-coordinate flip.

The natural next step is to propagate this missing flip along the ordered train to
its terminal boundary/fault structures and charge it without overcounting.

## 37.5 Proposed boundary backtracking estimate (UNPROVED)

The following estimate is a research target, not an available theorem. A suitable
boundary arc of length \(L\) joining a diameter pair has not been defined with a
non-overcounted charging map. If such an arc and charging map can be constructed,
one would seek

\[
\boxed{
\sum_{\lambda_\tau<0}
(-\lambda_\tau)
\le
\frac D2(L-D).
}
\tag{37.7}
\]

Until that missing construction is supplied, (37.7) must not be used to bound
positive curvature or to close a rank contradiction.

## 37.6 Pure-disk hull contact degree

At a hull vertex of a pure strict-rhombic disk, if the contact degree is \(d\),
then \(d-1\) rhombi occupy the convex interior angle.

Every rhombic corner is \(>\pi/3\), while the hull interior angle is \(<\pi\).
Therefore

\[
(d-1)\frac\pi3<\pi
\]

and

\[
\boxed{d\le3.}
\tag{37.8}
\]

Thus each diametral hull reaction is transmitted into the rhombic bulk through
only two or three unit bars.

---

---

# 38. Second-pass audit ledger for the recent work

This section is authoritative for the disposition of claims developed after the
post-synthesis addendum.

## 38.1 Claims that survive the second review

The following are retained as established under their stated hypotheses:

- the strict translated-lattice bound
  \[
  D(n)^2<\frac{2\sqrt3}{\pi}(n-1);
  \]
- the sharpened topology-corrected shell window and, in a pure rhombic disk,
  \[
  G+E<c_0B;
  \]
- the perimeter deficit \(\pi D-P=O(1)\), isodiametric area deficit \(O(D)\),
  and uniform width estimate \(\min w_K=D-O(D^{1/3})\);
- the exact support-depth, support-turning, pocket, and mixed-area identities;
- the sixfold phase-energy inequality and macroscopic grain decomposition;
- the train-coordinate realization of a simply connected pure rhombic disk;
- the exact train-angle gradient, Hessian, trace, and signed-variance formulas;
- the forbidden-coordinate-flip interpretation of a strict backward incidence;
- the stress-projected signed train-Laplacian identity and its negative-coupling
  positive-inertia bound;
- the backward-flip rank/equality-space dichotomy proved below;
- the terminal-pair localization of every separating train with \(\lambda\le0\);
- the generalized phase-atomic/exposed-hull theorem proved in Section 39, which
  strengthens the earlier full-cusp exclusion theorem;
- the secondary stressed-cusp theorem and tangent transfer identity of Section 42;
- the conditional invisible-coordinate continuation lemma for a lexicographically maximal pure representative;
- the existence of a genuine quartic tangent-class blocking mechanism.

## 38.2 Claims corrected or downgraded

The audit made the following changes.

### (a) Tangent trains cannot be discarded

The old sentence that every genuinely positive higher-order blocker must be
"backward or diameter-invisible" is false. Strict backward trains are necessary for
positive **quadratic** curvature. At quadratic equality, separating tangent trains
with \(\lambda=0\) can produce positive quartic curvature.

### (b) Corrected tangent expansion

A previous expansion through sixth order omitted the generally present term
\(-DS_5t^5/60\). The corrected expansion appears in Section 43. The omission does
not invalidate the main quartic conclusion because, when \(S_3=0\) and \(S_2\ne0\),
the positive \(t^4\) term dominates all fifth-order terms for sufficiently small
nonzero \(t\).

### (c) Full backward rank has an equality alternative

Local optimality does not by itself imply that the strict backward-flip map is
injective. The correct statement is:

\[
\operatorname{rank}\mathcal B=\dim\mathcal L
\]

**or** its kernel is contained in the exact quadratic-equality space of at least one
active diameter bar. The equality branch is precisely where tangent quartic locking
lives.

### (d) One diameter bar can have linear quartic capacity

It is false that one active diameter bar can kill only \(O(1)\) higher-order modes.
A same-oriented class of \(2s\) parallel tangent trains can quartically block an
\(s\)-dimensional paired-angle subspace. Any final proof must therefore charge train
classes / fault structure, not merely active diameter bars.

### (e) Two bar-rotation values are not a proved global flex theorem

For a secondary stress, two rotation values strongly constrain the bars in the
*stress support*. However an unsupported active equality bar can still block the
same train-angle line at higher order. Therefore no theorem in v1.0.0 claims that
"two rotation classes imply a global same-diameter family" without an additional
support-saturation hypothesis.

### (f) The old deep-end numerical claim is superseded

The old deep-end constants are not used as an independent lemma. Section 44 derives
a stronger pure-disk tail estimate from the newly audited lower bound on \(T/D\).

## 38.3 Claims still unproved

The following remain targets, not theorems:

- an ordered pseudoline/matroid bound forcing insufficient rank for the combined
  backward/tangent shell blockers;
- a conversion from that rank failure to \(G+E\ge c_0B\) in the general
  topology-corrected shell;
- an extension of the pure train-angle argument across all \(O(D)\) exceptional
  faces, holes, components, and outside vertices;
- the super-boundary forest-capacity theorem \(\ell=O(D)\) in Target A.

---

# 39. Generalized phase-atomic and exposed-hull theorem

This section strengthens the earlier full first-order cusp exclusion. It applies to
**every** sufficiently large triangle-free pure-rhombic-disk global minimizer in the
jammed branch.

Let \(R\) be the number of rhombi, \(T\) the number of trains, and \(q\) the number
of hull/diameter vertices. Then

\[
n=R+T+1,
\qquad
B=2T,
\qquad
R=n-O(D),
\qquad
T=\Theta(D),
\qquad
\frac{R}{D^2}\to\frac1c.
\tag{39.1}
\]

For train \(\tau\), let \(\phi_\tau\in\mathbb R/\pi\mathbb Z\) be its unoriented
direction and put

\[
\mu_T=\frac1T\sum_\tau\delta_{\phi_\tau}.
\]

Pass to an arbitrary subsequence on which \(\mu_T\) converges weakly to a probability
measure \(\mu\). Let \(s\) be the total mass of the atomic part of \(\mu\), and write

\[
y=\lim\frac qT
\]

along a further subsequence.

## 39.1 Leading crossing mass is carried only by phase atoms

For a crossing pair \(\tau,\sigma\), the rhombus defect satisfies

\[
\operatorname{dist}_{S^1}(6\phi_\tau,6\phi_\sigma)
\le6\delta_{\tau\sigma},
\]

and

\[
\sum_{\tau\sigma\in E(\Gamma)}\delta_{\tau\sigma}=O(D)=O(T).
\]

To keep the normalization explicit, define the symmetric **ordered** crossing
measure

\[
\eta_T
=\frac1{T^2}
\sum_{\{\tau,\sigma\}\in E(\Gamma)}
\left(
\delta_{(\phi_\tau,\phi_\sigma)}+
\delta_{(\phi_\sigma,\phi_\tau)}
\right).
\tag{39.2a}
\]

Its total mass is \(2R/T^2\). Since the crossing graph is simple,
\(\eta_T\) is dominated on rectangles, up to the vanishing diagonal term, by
\(\mu_T\times\mu_T\). The defect estimate and Markov's inequality imply that any
weak limit \(\eta\) is supported on the projective \(60^\circ\)-relation

\[
\mathcal S=
\{(\phi,\psi):\psi-\phi\equiv\pm\pi/3\pmod\pi\}.
\]

For a product measure, this graph has mass only through atoms:

\[
(\mu\times\mu)(\mathcal S)
=
\int \bigl(\mu\{\phi+\pi/3\}+\mu\{\phi-\pi/3\}\bigr)\,d\mu(\phi),
\]

so the non-atomic part of \(\mu\) carries no positive-density crossing mass.
Restricting to the atomic train mass, the limiting crossing graph remains
triangle-free because every finite train-crossing graph is triangle-free. Weighted
Mantel therefore gives an unordered edge density at most one quarter of the square
of the total atomic mass:

\[
\boxed{
\limsup\frac{R}{T^2}\le\frac{s^2}{4}.
}
\tag{39.2}
\]

This formulation is deliberately weaker than saying that the whole train measure is
atomic. A survivor may retain a non-atomic train population; that population simply
cannot carry \(\Theta(T^2)\) crossings.

## 39.2 Exposed hull chains force non-atomic train mass

The \(2T\) outer rhombic boundary edges are partitioned into \(q\) chains between
consecutive convex-hull vertices. Every hull side has length at least \(1\).

Fix a large integer \(M\). At most \(2T/(M+1)\) of these chains contain more than
\(M\) unit edges. Thus

\[
q-O(T/M)
\]

chains have bounded length.

Now choose finitely many atoms of \(\mu\) carrying at least \(s-\varepsilon\) of
its atomic mass. Fix these atoms, fix \(M\), and let \(U_\delta\) be disjoint
\(\delta\)-neighborhoods of their projective directions. If a bounded chain uses
only train ends whose directions lie in \(U_\delta\), its hull chord is a sum of at
most \(M\) such unit vectors. Because the chord has length at least \(1\), its
normal lies in a finite union \(V_{M,\delta}\) of arcs whose total circular measure
is \(O_M(\delta)\). The constant is uniform for sufficiently small \(\delta\):
the lower bound on the chord length excludes the cancellation singularity.

On the other hand, after scaling by \(D\), the minimizing hulls converge in Hausdorff
distance to the disk of diameter \(1\): the area deficit is \(O(D)\), so every
subsequential convex limit has diameter at most \(1\) and maximal area \(\pi/4\),
forcing the disk. The corresponding perimeter/surface-area measures converge weakly
to the non-atomic circular measure. In the plane this can be seen directly from
support functions: after translation, Hausdorff convergence is uniform convergence
of \(h_K\), while the curvature/perimeter measure is \(h_K+h_K''\) in the
distributional sense, so it converges weakly to the constant measure of the disk.
Since every hull side has length at least \(1\), the number of bounded chains whose
entire terminal-direction list lies in \(U_\delta\) is at most
\[
C_M\delta T+o_\delta(T).
\]
This is \(O(\delta T)\) for fixed \(\delta\), not \(o(T)\) for a fixed neighborhood.
Apart from these chains and the \(O(T/M)\) long chains, every hull chain contains a
train end outside \(U_\delta\). In the weak limit the fraction of trains capable of
supplying such an end is at most \(1-s+\varepsilon+o(1)\), and each such train has
only two terminal ends. Consequently

\[
\frac qT
\le C_M\delta+o_\delta(1)+2(1-s+\varepsilon)+O(1/M).
\]

Let \(T\to\infty\) first, then \(\delta\downarrow0\), then \(M\to\infty\), and
finally \(\varepsilon\downarrow0\). This gives

\[
\boxed{
s\le1-\frac y2.
}
\tag{39.3}
\]

Consequently,

\[
\boxed{
\limsup\frac{R}{T^2}
\le
\frac14\left(1-\frac y2\right)^2.
}
\tag{39.4}
\]

## 39.3 Exact pinned-rank lower bound on \(q/T\)

For a pure rhombic disk,

\[
|E(C)|=2R+T,
\qquad
n=R+T+1.
\]

Let \(e_{QQ}\) be the number of contact edges with both endpoints on the pinned
hull. Pinned rigidity gives

\[
2R+T-e_{QQ}\ge2(R+T+1-q),
\]

hence

\[
\boxed{
2q\ge T+2+e_{QQ},
\qquad
q\ge\frac T2+1.
}
\tag{39.5}
\]

Thus every asymptotic limit has \(y\ge1/2\).

## 39.4 Quantitative train and hull ratios

Put

\[
x=\frac TD.
\]

Because \(R/D^2\to1/c\), (39.4) gives

\[
\boxed{
x\ge\frac{2}{\sqrt c(1-y/2)}+o(1).}
\tag{39.6}
\]

Using \(y\ge1/2\),

\[
\boxed{
\liminf\frac TD
\ge
\frac8{3\sqrt c}
=2.5395008183\ldots.
}
\tag{39.7}
\]

Therefore

\[
\boxed{
\liminf\frac BD
\ge
5.0790016366\ldots.
}
\tag{39.8}
\]

Since \(q\le P=\pi D+o(D)\), one also has \(xy\le\pi+o(1)\). Combining with
(39.6) yields

\[
\boxed{
\limsup\frac qT
\le
\frac{2C_0}{4+C_0}
=0.9039456812\ldots.
}
\tag{39.9}
\]

Thus

\[
\boxed{
\liminf\frac{T-q}{D}
\ge
\frac{4-C_0}{2\sqrt c}
=0.3338292869\ldots.
}
\tag{39.10}
\]

This strengthens the earlier theorem \(q<T\) to a macroscopic linear gap.

---

# 40. Macroscopic first-order-neutral train space

Let \(H\) be the set of active diameter pairs and work in the train-angle quotient

\[
V=\mathbb R^T/\langle\mathbf1\rangle,
\qquad
\dim V=T-1.
\]

For \(h\in H\), let \(g_h\) be the train-angle gradient of
\(f_h=|r_h|^2/2\). The ordinary normalized KKT stress satisfies

\[
\sum_{h\in H}\beta_hg_h=0,
\qquad
\beta_h\ge0,
\qquad
\sum_h\beta_h=1,
\]

because every unit contact is exactly preserved by train-angle first variations.
Hence

\[
\operatorname{rank}\{g_h:h\in H\}\le |H|-1.
\]

The diameter graph on the \(q\) convex-hull vertices has at most \(q\) edges. Here is
a self-contained support-cone proof. For a diameter pair \(h=ij\), orient

\[
r=p_i-p_j.
\]

Then \(p_i\) is the **unique** maximizer of \(r\cdot x\) on \(K\), and \(p_j\) is
the unique minimizer. Indeed, if \(x\ne p_i\) shared the maximum support value, then
\(r\cdot(x-p_i)=0\) and

\[
|x-p_j|^2
=|r+(x-p_i)|^2
=D^2+|x-p_i|^2>D^2,
\]

a contradiction; the minimum case is identical.

For a convex \(q\)-gon, the directions on \(S^1\) for which a fixed vertex is the
unique support maximizer form the interior of its normal cone. These \(q\) open
normal-cone intervals partition the circle up to their \(q\) boundary rays. The
unique support minimizer is the maximizer in the antipodal direction, so the common
refinement of the maximizer partition and its antipodal copy has at most \(2q\) open
cells. On each cell the ordered pair (unique maximizer, unique minimizer) is constant.

The direction \(r/D\) of every oriented diameter pair lies in one of these open
cells, and distinct ordered diameter pairs require distinct cells. Every unordered
diameter pair appears twice, in antipodal cells with the two orientations reversed.
Therefore

\[
2|H|\le2q,
\qquad
\boxed{|H|\le q}.
\tag{40.0}
\]

This is the only diameter-graph edge bound needed below.

Define

\[
\mathcal L=\bigcap_{h\in H}\ker g_h\subset V.
\]

Then

\[
\boxed{
\dim\mathcal L\ge T-|H|\ge T-q.
}
\tag{40.1}
\]

Combining with (39.10),

\[
\boxed{
\dim\mathcal L
\ge
0.3338292869\ldots D-o(D).
}
\tag{40.2}
\]

Therefore the higher-order problem is intrinsically macroscopic: a survivor must
block \(\Theta(D)\) independent train-angle directions after all first-order
diameter gradients have been annihilated.

The former "full first-order train cusp" is consequently impossible as an immediate
corollary, with a fixed asymptotic gap rather than merely \(q<T\).

---

# 41. Stress-projected signed train Laplacian

Retain the pure simply connected train-coordinate representation

\[
p_v=p_0+\sum_{\tau=1}^T\epsilon_\tau(v)u_\tau,
\qquad
u_\tau=(\cos\phi_\tau,\sin\phi_\tau).
\]

For an oriented active diameter pair \(h=ij\), write

\[
r_h=\sum_\tau d_{h\tau}u_\tau,
\qquad
 a_{h\tau}=d_{h\tau}u_\tau,
\qquad
\lambda_{h\tau}=r_h\cdot a_{h\tau},
\]

and \(k_h=\#\{\tau:d_{h\tau}\ne0\}\).

The gradient and Hessian are

\[
(g_h)_\tau=r_h\cdot J a_{h\tau},
\tag{41.1}
\]

\[
(H_h)_{\tau\tau}=d_{h\tau}^2-\lambda_{h\tau},
\qquad
(H_h)_{\tau\sigma}=a_{h\tau}\cdot a_{h\sigma}
\quad(\tau\ne\sigma).
\tag{41.2}
\]

Fix any normalized KKT stress \((\alpha,\beta)\). For train \(\tau\), put

\[
A_\tau=\sum_{e\text{ a contact edge of }\tau}\alpha_e.
\]

Define

\[
M_{\tau\sigma}
=(u_\tau\cdot u_\sigma)
\sum_h\beta_h d_{h\tau}d_{h\sigma}.
\tag{41.3}
\]

Using the virtual-work field \(\xi_v=\epsilon_\tau(v)u_\tau\) gives

\[
\boxed{
A_\tau=\sum_h\beta_h\lambda_{h\tau}\ge0,
\qquad
\sum_\sigma M_{\tau\sigma}=A_\tau.
}
\tag{41.4}
\]

Therefore the stress-weighted train Hessian

\[
Q=\sum_h\beta_hH_h
\]

is exactly

\[
\boxed{
Q
=-\sum_{\tau<\sigma}
M_{\tau\sigma}
(e_\tau-e_\sigma)(e_\tau-e_\sigma)^{\mathsf T}.
}
\tag{41.5}
\]

Its trace is

\[
\boxed{
\operatorname{tr}Q
=\sum_h\beta_h(k_h-D^2)
\le T-D^2
=-\Theta(D^2).
}
\tag{41.6}
\]

If \(N_\beta\) is the graph of train pairs for which \(M_{\tau\sigma}<0\), then on
any train-angle subspace \(W\), the positive index obeys

\[
\boxed{
n_+(Q|_W)
\le
\operatorname{rank}
(B_{N_\beta}^{\mathsf T}|_W).
}
\tag{41.7}
\]

Indeed, the terms with \(M\ge0\) are negative semidefinite; all positive inertia is
contained in the span of incidence vectors belonging to negative couplings.

**Limitation.** A fixed KKT stress is not known to make \(Q\) nonnegative on the
whole critical space; the second-order normal stress may depend on the chosen
critical direction. Thus (41.7) is a rank diagnostic, not by itself a contradiction.

---

# 42. Backward-flip rank, terminal localization, and the secondary cusp

For \(v\in\mathcal L\), define

\[
s_h(v)=\frac1{D^2}\sum_\tau\lambda_{h\tau}v_\tau,
\qquad
\ell_{h\tau}(v)=v_\tau-s_h(v).
\tag{42.1}
\]

The exact neutral signed-variance identity is

\[
\boxed{
H_h[v,v]
=-\sum_\tau
\lambda_{h\tau}\ell_{h\tau}(v)^2.
}
\tag{42.2}
\]

## 42.1 Backward-flip map

Define

\[
\mathcal B:\mathcal L\to
\mathbb R^{\{(h,\tau):\lambda_{h\tau}<0\}},
\qquad
(\mathcal Bv)_{h\tau}=\ell_{h\tau}(v).
\tag{42.3}
\]

For each active bar put

\[
\mathcal Z_h=
\left\{
 v\in\mathcal L:
 \ell_{h\tau}(v)=0
 \text{ for every }\lambda_{h\tau}>0
\right\}.
\tag{42.4}
\]

On \(K=\ker\mathcal B\), equation (42.2) becomes

\[
H_h[v,v]
=-\sum_{\lambda_{h\tau}>0}
\lambda_{h\tau}\ell_{h\tau}(v)^2
\le0.
\tag{42.5}
\]

Therefore a locally diameter-minimal strict-rhombic realization satisfies the exact
dichotomy

\[
\boxed{
\operatorname{rank}\mathcal B=\dim\mathcal L
\quad\text{or}\quad
\ker\mathcal B\subseteq\mathcal Z_h
\text{ for some active }h.
}
\tag{42.6}
\]

**Proof.** If \(K\ne0\) and no \(\mathcal Z_h\) contains \(K\), then the finite union
of proper subspaces \(K\cap\mathcal Z_h\) cannot cover \(K\). Choose
\(v\in K\) outside their union. Then every active diameter has
\(H_h[v,v]<0\). Along the exact train-angle line \(\phi+tv\), all unit contacts stay
unit and every active diameter decreases to second order; all inactive inequalities
retain their strict slack for sufficiently small \(t\). This contradicts global (and
local) diameter minimality. \(\square\)

Thus full higher-order survival requires either at least \(\dim\mathcal L\) independent
backward-flip covectors, or a genuine tangent/equality branch.

## 42.2 Forbidden coordinate flip

If \(\lambda_{h\tau}<0\), then

\[
\boxed{
|r_h-a_{h\tau}|^2
=D^2+1-2\lambda_{h\tau}>D^2.
}
\tag{42.7}
\]

Hence the train-coordinate vertex obtained by toggling \(\tau\) toward the opposite
endpoint cannot exist with all other train coordinates fixed. Each backward row is
therefore an actual missing coordinate flip, not a merely formal Hessian sign.

Rows belonging to the same train have the form

\[
 e_\tau^*-s_h^*.
\]

Modulo the span of the bar-rotation functionals \(s_h^*\), all rows from one train
have the same class \([e_\tau^*]\). Repeated use of one terminal train cannot create
arbitrary rank for free; extra rank is carried explicitly by the bar-rotation space.

## 42.3 Terminal localization for every nonpositive separating train

Let \(h=ij\) be an active diameter and let \(\tau\) separate its endpoints.
If

\[
\lambda_{h\tau}\le0,
\]

then **both terminal boundary edges of \(\tau\) are non-hull edges**.

For \(\lambda<0\), orient either disk-boundary arc from \(j\) to \(i\). It crosses
\(\tau\) at one terminal edge with displacement \(a_{h\tau}\). A hull edge on either
convex-hull chain from the minimum support point \(j\) to the maximum support point
\(i\) has nonnegative \(r_h\)-projection, contradicting \(\lambda<0\).

For \(\lambda=0\), a hull terminal edge would be perpendicular to \(r_h\) and hence
would lie in a support face perpendicular to \(r_h\). Those maximum and minimum
support faces are singletons: if \(x\ne p_i\) shared the maximum support value with
\(p_i\), then

\[
|x-p_j|^2
=D^2+|x-p_i|^2>D^2.
\]

Thus equality is impossible as well.

Consequently, every strict-backward or tangent separating train consumes a pair of
non-hull terminal edges.

## 42.4 Secondary-cusp theorem

Take nonzero \(v\in\ker\mathcal B\), so every active diameter has
\(H_h[v,v]\le0\). Put

\[
E(v)=\{h:H_h[v,v]=0\}.
\]

Then

\[
\boxed{
0\in\operatorname{conv}\{g_h:h\in E(v)\}.
}
\tag{42.8}
\]

Otherwise strict separation supplies a train-angle acceleration \(w\) with
\(g_h\cdot w<0\) for every \(h\in E(v)\). For

\[
\phi(t)=\phi+t v+\frac{\varepsilon t^2}{2}w,
\]

the coefficient

\[
H_h[v,v]+\varepsilon g_h\cdot w
\]

is negative for every equality bar and remains negative for all bars with
\(H_h[v,v]<0\) when \(\varepsilon\) is sufficiently small. Every active diameter
would decrease to second order, contradicting minimality.

More strongly, apply the direction-dependent second-order normal-stress theorem to
this critical velocity. Along the exact train-angle path every unit contact has
identically constant length. Applying the first-order equilibrium identity to the
path acceleration converts the theorem's velocity-square expression exactly into
the weighted second derivative of the diameter functions. Thus it supplies a
normalized proper stress \((\alpha^{(v)},\beta^{(v)})\) for which

\[
\sum_h\beta_h^{(v)}H_h[v,v]
=
\sum_h\beta_h^{(v)}|\dot r_h|^2
-
\sum_e\alpha_e^{(v)}|\dot r_e|^2
\ge0.
\]

Every summand is nonpositive, hence

\[
\boxed{
\beta_h^{(v)}>0
\Longrightarrow
h\in E(v),
\qquad
\sum_h\beta_h^{(v)}H_h[v,v]=0.
}
\tag{42.9}
\]

Thus every surviving equality direction carries an actual **secondary stressed
cusp** supported only on second-order-flat diameter bars.

## 42.5 Train-by-train vector balance and tangent transfer

For the secondary stress, use the virtual field
\(\xi_x=\epsilon_\tau(x)w\) with arbitrary \(w\in\mathbb R^2\). This gives the vector
identity

\[
\boxed{
\sum_{h\in E(v)}
\beta_h d_{h\tau}r_h
=A_\tau u_\tau,
\qquad
A_\tau\ge0.
}
\tag{42.10}
\]

Suppose \(h\) is a stress-supported equality bar, \(\tau\) separates its endpoints,
and

\[
\lambda_{h\tau}=0,
\qquad
v_\tau\ne s_h(v).
\]

The term \(\beta_h d_{h\tau}r_h\) is nonzero and perpendicular to \(u_\tau\), whereas
the right side of (42.10) is parallel to \(u_\tau\). Another stress-supported bar
\(k\ne h\) must therefore separate \(\tau\) and have a nonzero perpendicular
component.

There is at most one active diameter segment in any prescribed unoriented direction:
if two distinct parallel length-\(D\) segments differed by a nonzero translation
\(s\), then

\[
|r+s|^2+|r-s|^2=2D^2+2|s|^2,
\]

so one cross-distance would exceed \(D\). Hence \(k\) cannot also be tangent to
\(\tau\); therefore \(\lambda_{k\tau}\ne0\).

Since \(k\in E(v)\), equality in (42.5) forces

\[
\boxed{
v_\tau=s_k(v).
}
\tag{42.11}
\]

Thus every moving tangent train of a stress-supported bar transports an exact
**difference of diameter-bar rotation potentials**:

\[
\boxed{
v_\tau-s_h=s_k-s_h.}
\tag{42.12}
\]

This is a major refinement of the raw quartic model. Tangent velocities in an actual
secondary cusp are not arbitrary; they are coupled to rotation potentials of other
loaded diameter bars.


## 42.6 Proposed invisible-coordinate selection (UNPROVED)

Call a train \(\tau\) **globally invisible to the active diameter support** if

\[
d_{h\tau}=0\qquad(h\in H).
\tag{42.13}
\]

There is a useful canonical-selection idea, but the first-event argument below has
an unresolved triangle-wall case.

> **Proposed Lemma 42.6.** Among all
> triangle-free global minimizers for a fixed \(n\), choose one first maximizing the
> number of unit contacts and then maximizing the number of active diameter pairs.
> **If that lexicographically maximal representative is a pure strict-rhombic disk,**
> then it has no globally invisible train.

The proposed proof varies an invisible train until the first constraint event. A
first event may be a rhombus reaching the \(60^\circ\) boundary, which creates a
unit triangle. That endpoint is not an admissible triangle-free minimizer, so it
does not contradict the lexicographic choice. The other first events (a new
triangle-free unit contact or a new active diameter pair) would give the intended
contradiction, but they do not exhaust the possibilities. No downstream theorem
may invoke Lemma 42.6 until this gap is closed. Section 53 correctly keeps the
local same-diameter train-flat alternative instead of relying on this lemma.

This lemma does **not** say that every pure survivor can be replaced by a pure
lexicographically maximal survivor; the canonical selection can change the contact
complex. It is therefore retained as an auxiliary normalization, not used in the
main pure-disk contradiction unless that compatibility is established.

---

# 43. Corrected tangent-class higher-order expansion

Fix an active diameter bar \(h\) and a direction \(v\in\mathcal L\) satisfying the
quadratic equality conditions for \(h\). Subtract the common bar rotation
\(s_h(v)\). Every separating train with \(\lambda\ne0\) is then stationary relative
to the bar. Only tangent trains

\[
d_{h\tau}\ne0,
\qquad
\lambda_{h\tau}=0
\]

can move it.

Let

\[
e_h=\frac{r_h}{D},
\qquad
 a_{h\tau}=\sigma_{h\tau}J e_h,
\qquad
\sigma_{h\tau}\in\{\pm1\},
\]

and let

\[
w_\tau=v_\tau-s_h(v).
\]

Define the signed moments

\[
S_m=\sum_\tau\sigma_{h\tau}w_\tau^m.
\tag{43.1}
\]

First-order neutrality gives

\[
S_1=0.
\tag{43.2}
\]

The exact bar change is

\[
\Delta r_h(t)
=
-\left(\sum_\tau\sigma_{h\tau}\sin(w_\tau t)\right)e_h
+
\left(\sum_\tau\sigma_{h\tau}(\cos(w_\tau t)-1)\right)J e_h.
\tag{43.3}
\]

Therefore the corrected expansion is

\[
\boxed{
\begin{aligned}
|r_h(t)|^2-D^2
={}&
\frac D3S_3t^3
+
\frac{S_2^2}{4}t^4
-
\frac D{60}S_5t^5\\
&+
\left(
\frac{S_3^2}{36}
-
\frac{S_2S_4}{24}
\right)t^6
+O(t^7).
\end{aligned}
}
\tag{43.4}
\]

The omitted fifth-order term is the principal formula correction made in the
v1.0.0 audit.

Consequences:

1. if \(S_3\ne0\), one sign of \(t\) decreases this diameter at cubic order;
2. if \(S_3=0\) and \(S_2\ne0\), the positive \(t^4\) term dominates, so the bar is a
   genuine two-sided quartic blocker for sufficiently small nonzero \(t\);
3. if \(S_2=S_3=0\), still higher signed moments must be examined.

## 43.1 One bar can have linear quartic capacity

Suppose \(2s\) tangent trains have the same oriented contribution

\[
a_{h\tau_j}=\sigma J e_h
\]

and choose paired relative velocities

\[
w_{2j-1}=x_j,
\qquad
w_{2j}=-x_j.
\]

Then exactly

\[
\boxed{
|r_h(t)|^2-D^2
=
\left[
2\sum_{j=1}^s(\cos(x_jt)-1)
\right]^2.
}
\tag{43.5}
\]

Its leading term is

\[
t^4\left(\sum_{j=1}^s x_j^2\right)^2.
\]

Thus one active diameter can quartically block an \(s\)-dimensional paired train
subspace. This definitively rules out any closing argument that charges only one
higher-order mode per active diameter bar.

## 43.2 What simultaneous optimality adds

Equation (43.5) is a valid warning model, but Section 42.5 shows that in a genuine
secondary stressed cusp every moving tangent train of a supported bar must satisfy

\[
w_\tau=s_k-s_h
\]

for another supported diameter bar \(k\). Hence the true residual object is an
ordered train network carrying differences of bar-rotation potentials, not a set of
independent paired variables.

This coupling is established. What is **not** established is that the potential
network has too little rank, or that two potential values automatically produce a
global flex. Unsupported active equality bars remain a possible higher-order
obstruction.

---

# 44. Additional audited quantitative consequences

## 44.1 Stronger pure-disk support-depth theorem

For a pure rhombic disk, the exact train identity gives

\[
H_\partial^K
=
\sum_\tau w_K(\nu_\tau)
-2\sum_F\sin\theta_F.
\]

Uniform width saturation gives

\[
\sum_\tau w_K(\nu_\tau)
=TD-o(D^2),
\]

while

\[
2\sum_F\sin\theta_F
=\sqrt3R+o(D^2)
=\frac\pi2D^2+o(D^2).
\]

Therefore

\[
\boxed{
\frac{H_\partial^K}{D^2}
=
\frac TD-\frac\pi2+o(1).
}
\tag{44.1}
\]

Using (39.7),

\[
\boxed{
H_\partial^K
\ge
0.9687044915\ldots D^2-o(D^2)
}
\tag{44.2}
\]

and, since \(D^2/n\to c\),

\[
\boxed{
H_\partial^K
\ge
1.0681495546\ldots n-o(n).
}
\tag{44.3}
\]

This does **not** create Oler surplus: \(H_\partial^K=2G+\mathfrak J\), and the
order-\(n\) support-turning term \(\mathfrak J\) still cancels.

## 44.2 Audited support-depth tail

Every support depth satisfies \(0\le\rho_e^K\le D\), and there are \(2T\) train ends.
For fixed \(0<a<1/2\), let \(N_a\) be the number with

\[
\rho_e^K\ge aD.
\]

Then

\[
H_\partial^K
\le
N_aD+(2T-N_a)aD.
\]

Combining with (44.1), for every fixed \(a\) for which the numerator below is
positive,

\[
\boxed{
\liminf\frac{N_a}{D}
\ge
\frac{
\frac8{3\sqrt c}(1-2a)-\frac\pi2
}{1-a}.
}
\tag{44.4}
\]

For the clean choice \(a=0.1\),

\[
\boxed{
N_{0.1}
\ge
0.5120048087\ldots D-o(D)
=
0.5376435191\ldots\sqrt n-o(\sqrt n).
}
\tag{44.5}
\]

This is the audited replacement for the earlier, weaker deep-end numerical claim.

## 44.3 Boundary curvature identity

Let \(h_2,h_3\) count hull boundary vertices of contact degree \(2,3\); let
\(r_3,r_4,r_5\) count non-hull boundary vertices of degree \(3,4,5\); and let
\(i_5\) count interior degree-five vertices. In a pure strict-rhombic disk, Euler and
degree counting give

\[
\boxed{
h_2=4+r_4+2r_5+i_5.
}
\tag{44.6}
\]

Since \(q=h_2+h_3\) and the boundary has \(2T\) vertices,

\[
\boxed{
r_3\ge2(T-q)+4.
}
\tag{44.7}
\]

Using (39.10),

\[
\boxed{
r_3
\ge
0.6676585739\ldots D-o(D).
}
\tag{44.8}
\]

Thus a hypothetical pure survivor has a linear family of non-hull degree-three
reflex boundary vertices. These are natural terminal resources for any future
missing-flip/fault-wall rank theorem.

---

# 45. Current exact Target B frontier

The pure-rhombic-disk branch is now forced into the following simultaneous regime:

\[
\boxed{
\begin{array}{c}
G+E<c_0B,\\[1mm]
q/T\le0.9039456812\ldots+o(1),\\[1mm]
T/D\ge2.5395008183\ldots+o(1),\\[1mm]
(T-q)/D\ge0.3338292869\ldots-o(1),\\[1mm]
\dim\mathcal L\ge0.3338292869\ldots D-o(D),\\[1mm]
\text{full first-order train locking is impossible},\\[1mm]
\text{quadratic survival requires full backward-flip rank or an equality kernel},\\[1mm]
\text{every nonpositive separating train terminates twice off-hull},\\[1mm]
\text{every equality-kernel direction carries a secondary stressed cusp},\\[1mm]
\text{moving tangent trains transport differences of bar-rotation potentials},\\[1mm]
\text{one tangent class can nevertheless have linear quartic capacity.}
\end{array}
}
\tag{45.1}
\]

The exact unresolved pure-disk theorem can therefore be stated as follows.

> **Ordered higher-order shell-rank theorem (open).** In a sufficiently large
> triangle-free pure-rhombic-disk global minimizer with \(G+E<c_0B\), the ordered
> pseudoline/fault network cannot simultaneously support either
>
> 1. full rank of the backward-flip map on the macroscopic neutral space
>    \(\mathcal L\); or
> 2. a residual secondary cusp whose tangent train classes provide enough quartic
>    rank to block the remaining kernel,
>
> unless a rhombus phase difference becomes exactly zero (equivalently an acute
> angle is exactly \(60^\circ\)), a forbidden Cartesian block appears, or there is an
> actual diameter-decreasing feasible motion.

The most concrete data available for proving this theorem are:

- each backward/tangent train has a pair of non-hull terminals;
- same-phase train families are internally noncrossing and ordered;
- leading crossing mass lies in a small number of near-triangular phase classes;
- tangent velocities are exact differences \(s_k-s_h\) of loaded diameter-bar
  potentials;
- the shell contains at least \(0.6676585739D-o(D)\) degree-three reflex boundary
  vertices;
- one cannot charge by active-bar cardinality because of the quartic tangent-class
  example;
- one cannot charge raw support depth because of support-turning cancellation.

## 45.1 General topology correction remains necessary

Even a proof of the pure-disk theorem is not by itself the entire jammed branch.
The actual almost-rhombic core may have \(O(D)\) exceptional nonquadrilateral faces,
holes, multiple components, and vertices outside the rhombic complex. The Oler shell
window already handles these corrections exactly at scalar level, but the
train-coordinate/higher-order rank argument must either be extended through them or
combined with a reduction that removes them without losing global optimality.

Thus Target B has two final layers:

1. close the pure ordered higher-order shell-rank theorem;
2. make the argument topology-correct at the same boundary scale.

---

# 46. Target A: flexible bridge-forest branch

The hybrid normal form from Sections 12 and 18 remains valid. There is a fixed
contact-minimal pinned-jammed core \(K\); every contact edge outside it is a bridge,
and after contraction the residue is a forest. If

\[
\ell=\dim\mathcal L_{\widehat Q}
\]

is the pinned contact-preserving lineality, then

\[
|V(\widehat A)\setminus V(K)|
\le
\ell+2|\widehat Q|.
\]

Since \(|\widehat Q|=O(D)\), the case \(\ell=O(D)\) already leaves an
\(n-O(D)\) jammed almost-rhombic core. The genuinely separate obstruction is

\[
\boxed{\ell=\omega(D).}
\tag{46.1}
\]

The post-synthesis train-Hessian work does **not** eliminate this branch. These
forest modes are already actual first-order contact-preserving motions with the
relevant pinned roots fixed. Plain Oler area accounting also cannot see the excess
lineality because outside vertices receive the same bulk allowance on both sides of
the topology-corrected shell identity.

The still-open theorem is:

> **Super-boundary forest-capacity theorem.** No sufficiently large triangle-free
> global minimizer in the hybrid normal form has
> \(\ell=\omega(D)\).

A successful proof must use a global occupancy/configuration-space mechanism, or a
unified shell-rank principle that charges independent forest motions to the same
finite diametral/fault resources used by Target B.

---

# 47. Regression models and routes that the final proof must survive

The complete regression suite is now:

1. **unit square:** triangle-free exact global minimizer, zero-cone branch;
2. **regular unit pentagon and the small exact cases:** diameter-loaded polygon
   corners defeat naive low-degree movement claims;
3. **\(n=8\) heptagon plus center:** triangle-free global minimizer with a rattler;
4. **regular odd-prime unit polygons:** arbitrarily large triangle-free strict local
   diameter minima;
5. **dense regular-shell fillings:** asymptotically optimal density, exact stress,
   local diameter optimality, but no global certificate;
6. **five-sector \(C_5\)-blowup rhombic complexes:** strict near-equilateral rhombi,
   positive pinned stress and zero pinned cone, but non-diametral/nonextreme pins;
7. **11-point sun:** true diametral hull and local pinning but explicit global
   suboptimality;
8. **disk-clipped near-\(60^\circ\) oblique grids:** near-disk rhombic bulk showing
   that no uniform density gap or naive angular-collapse argument can work;
9. **near-equilateral pentagonal/triangular pocket degenerations:** local Oler slack
   can approach zero;
10. **disk chord systems:** quadratic raw support depth is normal and therefore not a
    contradiction currency;
11. **parallel tangent quartic class:** one diameter bar can block linearly many
    paired modes at fourth order.

Dead routes remain:

- uniform triangle-free density gaps;
- eventual lattice classification;
- raw contact counts or Laman counts;
- degeneracy alone;
- KKT or positive stress alone;
- a fixed universal prestress Hessian;
- affine shear alone;
- angular defect quantization;
- raw support depth converted directly to Oler surplus;
- arbitrary dense-graph biclique extraction;
- counting one higher-order mode per diameter bar;
- assuming a same-diameter local family is already a diameter decrease.

---

# 48. Version 1.1.0 continuation audit and notation

**LEVEL I STATUS: STILL OPEN.**

The continuation after v1.0.0 produces a sharper normal form for the two remaining
branches but does not prove either final capacity theorem.  The central change is
that the macroscopic higher-order train obstruction is no longer an undifferentiated
mixture of backward and tangent effects.  After minimal-face reduction, visible
tangent transport has only constant-dimensional freedom; any large residual freedom
is forced into strict-backward/Dirichlet rank or into a genuine same-diameter optimal
flat.

Throughout Sections 48--57 we retain the pure simply connected strict-rhombic-disk
notation

\[
V=\mathbb R^T/\langle\mathbf1\rangle,
\qquad
\mathcal L=\bigcap_{h\in H}\ker g_h,
\qquad
K=\ker\mathcal B\subseteq\mathcal L.
\tag{48.1}
\]

The v1.0.0 quantitative stack gives

\[
G+E<c_0B,
\qquad
\dim\mathcal L\ge T-q,
\tag{48.2}
\]

and

\[
\boxed{
\frac{T-q}{D}
\ge0.3338292869\ldots-o(1).
}
\tag{48.3}
\]

Thus any residual higher-order mechanism is macroscopic unless it is compressed by
the structure proved below.

The exact pure-disk contradiction gate remains

\[
\boxed{G+E\ge c_0B.}
\tag{48.4}
\]

For topology-corrected rhombic complexes the exact window remains

\[
c_0(B-P)+a_0(t+\chi-1)
\le G_{\mathcal R}+E_{\mathcal R}
<c_0B+a_0(t+\chi-1).
\tag{48.5}
\]

No result below silently absorbs an uncontrolled \(O(D)\) topology error into the
one-integer pure-disk rank contradiction.

---

# 49. Minimal-face harmonic--Dirichlet reduction

Assume \(K\ne0\), and lift it to

\[
\widetilde K=\{x\in\mathbb R^T:[x]\in K\},
\qquad
\dim\widetilde K=\dim K+1.
\tag{49.1}
\]

For an active diameter bar \(h\), write

\[
s_h(x)=\frac1{D^2}\sum_\tau\lambda_{h\tau}x_\tau.
\tag{49.2}
\]

Let

\[
E_0=\{h:H_h|_K\equiv0\}.
\tag{49.3}
\]

The signed-variance theorem makes every \(H_h|_K\) negative semidefinite.  If
\(h\notin E_0\), its equality set in \(K\) is a proper subspace.  Choosing a vector
outside the finite union of these subspaces and applying the secondary-cusp theorem
gives

\[
0\in\operatorname{conv}\{g_h:h\in E_0\}.
\tag{49.4}
\]

Let \(F\) be the minimal face of this convex hull containing \(0\), and put

\[
S=\{h\in E_0:g_h\in F\}.
\tag{49.5}
\]

Then there are coefficients

\[
\beta_h>0\quad(h\in S),
\qquad
\sum_{h\in S}\beta_hg_h=0.
\tag{49.6}
\]

Define the \(S\)-invisible train set

\[
\mathcal I=\{\tau:d_{h\tau}=0\text{ for every }h\in S\},
\qquad I=|\mathcal I|.
\tag{49.7}
\]

Let \(m\) be the number of distinct functionals
\(s_h|_{\widetilde K}\), \(h\in S\).

## 49.1 Visible coordinates factor through bar potentials

For \(h\in S\), equality of the signed-variance formula on \(K\) gives

\[
x_\tau=s_h(x)
\qquad
(d_{h\tau}\ne0,\ \lambda_{h\tau}\ne0,
\ x\in\widetilde K).
\tag{49.8}
\]

If \(d_{h\tau}\ne0\), \(\lambda_{h\tau}=0\), and the coordinate functional
\(x_\tau\) is not identically \(s_h\), then the \(\tau\)-coordinate of \(g_h\)
has magnitude \(D\).  Taking the \(\tau\)-coordinate in (49.6) supplies another
\(k\in S\) with \((g_k)_\tau\ne0\).  Two distinct active diameter segments cannot
have the same unoriented direction; hence \(k\) is non-tangent to \(\tau\), and
(49.8) gives

\[
x_\tau=s_k(x).
\tag{49.9}
\]

Therefore every \(S\)-visible train coordinate factors through one of the \(m\)
bar-potential functionals.

Choose representatives \(h_1,\dots,h_m\), and put

\[
N_j=\{\tau:d_{h_j\tau}\ne0,\ \lambda_{h_j\tau}\ne0\}.
\tag{49.10}
\]

If a train belonged to both \(N_i\) and \(N_j\), then (49.8) would make the two
potential functionals equal; thus the sets \(N_j\) are pairwise disjoint.  Let
\(e_j=r_{h_j}/D\).  Tangent trains have zero longitudinal projection, so

\[
D=e_j\cdot r_{h_j}
 =\sum_{\tau\in N_j}e_j\cdot a_{h_j\tau}
 \le |N_j|.
\tag{49.11}
\]

Hence

\[
\boxed{mD\le T-I.}
\tag{49.12}
\]

Recording the \(I\) invisible coordinates and the \(m\) potential values gives an
injective linear map

\[
\widetilde K\longrightarrow
\mathbb R^{\mathcal I}\oplus\mathbb R^m,
\tag{49.13}
\]

so

\[
\boxed{
\dim K+1\le I+m
\le I+\left\lfloor\frac{T-I}{D}\right\rfloor.
}
\tag{49.14}
\]

Pinned rigidity already gives \(T\le2q-2\), while \(q\le P\le\pi D\).  Thus

\[
T\le2\pi D-2,
\qquad
\boxed{m\le6.}
\tag{49.15}
\]

In particular,

\[
\boxed{\dim K\le I+5,}
\tag{49.16}
\]

or equivalently

\[
\boxed{
\operatorname{rank}\mathcal B+I
\ge\dim\mathcal L-5
\ge0.3338292869\ldots D-o(D)-5.
}
\tag{49.17}
\]

This is the first constant-dimensional compression of the residual tangent/equality
branch.

---

# 50. Ordered tangent collapse, harmonic transport, and peripheral duality

## 50.1 Sign coherence of a tangent family

Fix an active diameter bar \(h\), and let \(e_h=r_h/D\).  All trains tangent to
\(h\) are parallel crosscuts perpendicular to \(r_h\).  Orient their common train
vector consistently.  Their crosscuts are nested, and because each separates the two
endpoints of \(h\), the endpoint-side relation cannot reverse between two nested
crosscuts.  Hence there is one sign \(\sigma_h\in\{\pm1\}\) such that

\[
\boxed{
a_{h\tau}=d_{h\tau}u_\tau=\sigma_hJe_h
}
\tag{50.1}
\]

for every tangent train \(\tau\) of \(h\).

Suppose a bar in potential class \(j\) has tangent trains \(\mathcal T_h\), and let
\(c(\tau)\) denote the potential class transported by \(\tau\).  First-order
neutrality, together with (50.1), gives the exact positive averaging law

\[
\boxed{
s_j=\frac1{t_h}\sum_{\tau\in\mathcal T_h}s_{c(\tau)},
\qquad t_h=|\mathcal T_h|>0.
}
\tag{50.2}
\]

## 50.2 Terminal potential classes

Construct the directed graph of potential classes by directing \(j\) to every class
transported by a tangent train of a bar in class \(j\).  The scalar maximum principle
applied to (50.2) shows that a terminal strongly connected component cannot contain
two distinct potential functionals.  Thus every terminal component is one potential
class, and every transient potential is a convex combination of terminal potentials.

Let \(r\) be the number of terminal potential classes.  Recording the \(I\)
invisible coordinates and the \(r\) terminal potentials determines every train
coordinate on \(\widetilde K\), so

\[
\boxed{\dim K+1\le I+r.}
\tag{50.3}
\]

For a terminal representative \(h_j\), every train separating its endpoints has
coordinate functional \(s_j\); an extremal terminal potential cannot have a moving
tangent train, because a positive average equals an extremum only when all entries
equal that extremum.  Distinct terminal classes therefore have disjoint complete
separator sets \(\Sigma_{h_j}\).  The triangle inequality gives

\[
D=|r_{h_j}|
\le\sum_{\tau\in\Sigma_{h_j}}|a_{h_j\tau}|
=|\Sigma_{h_j}|.
\tag{50.4}
\]

Hence

\[
\boxed{
rD\le T-I,
\qquad
r\le6.
}
\tag{50.5}
\]

The visible tangent obstruction has at most

\[
\boxed{r-1\le5}
\tag{50.6}
\]

non-rotational potential degrees of freedom.

If \(r\ge2\), two disjoint terminal cuts have at least \(D^2\) cross pairs.  Since
only

\[
R=\frac{\pi}{2\sqrt3}D^2+o(D^2)
\tag{50.7}
\]

pairs cross in rhombi, the two cuts contain at least

\[
\boxed{
\left(1-\frac{\pi}{2\sqrt3}\right)D^2-o(D^2)
=0.093100317882891\ldots D^2-o(D^2)
}
\tag{50.8}
\]

noncrossing pairs.  This is a structural resource, not by itself Oler surplus.

## 50.3 Tangent cubic/quartic trichotomy under sign coherence

After subtracting the common bar rotation, put

\[
w_\tau=x_\tau-s_h(x),
\qquad
S_m=\sum_\tau\sigma_{h\tau}w_\tau^m.
\tag{50.9}
\]

The exact expansion from v1.0.0 is

\[
\begin{aligned}
|r_h(t)|^2-D^2
={}&\frac D3S_3t^3+\frac{S_2^2}{4}t^4-\frac D{60}S_5t^5\\
&+\left(\frac{S_3^2}{36}-\frac{S_2S_4}{24}\right)t^6+O(t^7).
\end{aligned}
\tag{50.10}
\]

Because of (50.1),

\[
\boxed{S_2=\sigma_h\sum_\tau w_\tau^2.}
\tag{50.11}
\]

Therefore:

1. \(S_3\ne0\) is one-sided at cubic order;
2. \(S_3=0\), \(S_2\ne0\) is a genuine positive two-sided quartic blocker;
3. \(S_2=0\) forces every tangent deviation to vanish.

Thus there is no higher straight-line tangent branch once the ordered minimal-face
sign coherence is imposed.  Curved paths and changes of active face still require
the facial analysis below.

## 50.4 Dirichlet-boundary theorem

For \(\tau\), let

\[
p_\tau=x_\tau|_{\widetilde K}\in\widetilde K^*,
\qquad
\mathscr P=\operatorname{conv}\{p_\tau:\tau\text{ a train}\}.
\tag{50.12}
\]

All coordinate functionals take value \(1\) on common rotation and span
\(\widetilde K^*\), so

\[
\dim\operatorname{aff}\mathscr P=\dim K.
\tag{50.13}
\]

Call a vertex class of \(\mathscr P\) **free** if every train in it is
\(S\)-invisible and no train in it is backward for any active diameter bar.

For a backward incidence, the exact positive averaging identity on \(K\) is

\[
\boxed{
p_\tau
=\sum_{\lambda_{h\sigma}>0}
\frac{\lambda_{h\sigma}}{\Lambda_h^+}p_\sigma,
\qquad
\Lambda_h^+\ge D^2.
}
\tag{50.14}
\]

Since \(\lambda_{h\sigma}\le D\), at least \(D\) forward trains occur.  If
\(p_\tau\) is an extreme point of \(\mathscr P\), extremality forces every
\(p_\sigma\) in (50.14) to equal \(p_\tau\); hence a vertex class containing a
backward train contains at least \(D\) trains.

A visible vertex is a convex combination of terminal potentials and therefore must
itself be terminal.  Its complete terminal separator cut again contributes at least
\(D\) trains in the same vertex class.  Distinct vertex classes are disjoint.  Thus
at most

\[
\left\lfloor\frac TD\right\rfloor\le6
\tag{50.15}
\]

vertex classes are nonfree.

If \(J\) is the number of free vertex classes, every \(d\)-dimensional polytope has
at least \(d+1\) vertices, so

\[
\boxed{
J\ge\dim K+1-\left\lfloor\frac TD\right\rfloor
\ge\dim K-5.
}
\tag{50.16}
\]

## 50.5 Free trains are peripheral zero-secondary-stress cuts

Take an extreme normalized secondary stress on the minimal face \(S\).  The
train-by-train balance is

\[
\sum_{h\in S}\beta_hd_{h\tau}r_h=A_\tau u_\tau,
\qquad A_\tau\ge0.
\tag{50.17}
\]

If \(\tau\) is \(S\)-invisible, the left side is zero, hence \(A_\tau=0\).  Because
\(A_\tau\) is a sum of nonnegative contact-stress coefficients on the edges of the
train, every such coefficient vanishes.  No supported diameter bar crosses the cut
either.

If positive diameter support lay on both sides, the equilibrium stress would split
into two nonzero proper positive stresses, contradicting extremality.  A side with
contact stress but no diameter stress is also impossible: multiplying its contact-
only equilibrium equations by the vertex positions and summing gives

\[
0=\sum_{ij}\omega_{ij}|p_i-p_j|^2,
\tag{50.18}
\]

forcing every nonnegative contact coefficient \(\omega_{ij}\) to vanish.  Thus all
positive secondary support lies on one side of every free train.  These are genuine
peripheral zero-stress cuts.

## 50.6 Peripheral-dual rank theorem

Let \(M\) be the number of nonfree vertex classes and
\(\mathcal V_{\rm free}\) the free vertices of \(\mathscr P\).  Define

\[
W_{\rm per}
=\operatorname{span}\{p-p':p,p'\in\mathcal V_{\rm free}\}
\subseteq K^*.
\tag{50.19}
\]

Adding \(M\) points to an affine set raises affine dimension by at most \(M\), hence

\[
\dim K
\le\dim\operatorname{aff}(\mathcal V_{\rm free})+M.
\tag{50.20}
\]

The translation space of the free-vertex affine hull is exactly \(W_{\rm per}\), so

\[
\boxed{
\dim W_{\rm per}\ge\dim K-M\ge\dim K-6.
}
\tag{50.21}
\]

Equivalently, with

\[
K_{\rm core}
=\{x\in K:(p-p')(x)=0\ \forall p,p'\in\mathcal V_{\rm free}\},
\tag{50.22}
\]

we have

\[
\boxed{\dim K_{\rm core}\le M\le6.}
\tag{50.23}
\]

Thus, modulo at most six dimensions, the residual equality kernel is dual-detected
by differences of peripheral backward-free zero-secondary-stress train cuts.

## 50.7 Exact rank consequences

Rank-nullity together with (50.3) gives

\[
\boxed{
\operatorname{rank}\mathcal B+I+r
\ge\dim\mathcal L+1
\ge T-q+1.
}
\tag{50.24}
\]

Likewise (50.16) gives

\[
\boxed{
\operatorname{rank}\mathcal B+J
\ge T-q+1-\left\lfloor\frac TD\right\rfloor
\ge T-q-5.
}
\tag{50.25}
\]

Asymptotically,

\[
\boxed{
\operatorname{rank}\mathcal B+J
\ge0.3338292869\ldots D-o(D)-5.
}
\tag{50.26}
\]

The unreduced \(m\)-potential form also gives a useful quantitative corollary.
From

\[
\operatorname{rank}\mathcal B+I+m\ge T-q+1
\tag{50.27}
\]

and \(I\le T-mD\),

\[
\boxed{
\operatorname{rank}\mathcal B
\ge [m(D-1)-q+1]_+.
}
\tag{50.28}
\]

Using \(q\le\pi D+o(D)\), this yields

\[
\begin{array}{c|c}
m&\operatorname{rank}\mathcal B/D\\\hline
4&\ge0.8584073464\ldots-o(1)\\
5&\ge1.8584073464\ldots-o(1)\\
6&\ge2.8584073464\ldots-o(1).
\end{array}
\tag{50.29}
\]

For \(m=6\),

\[
\boxed{I\le(2\pi-6)D-2
=0.2831853071\ldots D-2.}
\tag{50.30}
\]

These are diagnostic bounds; the final theorem still needs ordered geometry rather
than potential count alone.

These inequalities expose the one-integer pure-disk target: a geometric shell upper
bound

\[
\operatorname{rank}\mathcal B+I+r\le T-q
\tag{50.31}
\]

would contradict (50.24) immediately.

---

# 51. Terminal direction-network normal form

Let \(z_1,\ldots,z_q\) be the hull vertices, cyclically ordered, and let \(C_j\) be
the rhombic-boundary chain from \(z_j\) to \(z_{j+1}\).

Construct a multigraph \(\Theta\) whose vertices are \(C_1,\ldots,C_q\).  Every train
\(\tau\) gives an edge joining the two chains containing its terminal boundary
edges.  Orient the train vectors consistently.  The two terminal boundary edges of a
train appear with opposite induced orientations, so there is an oriented incidence
matrix \(\partial\) such that

\[
\boxed{
z_{j+1}-z_j=\sum_\tau\partial_{j\tau}u_\tau.
}
\tag{51.1}
\]

## 51.1 No loops

If both terminal edges of one train belonged to the same chain, their contributions
to every chain vector in (51.1) would cancel.  Rotating that train alone would then
leave every hull-chain displacement unchanged.  After fixing one hull vertex, all
hull vertices would be fixed, while the train-angle motion preserves all contacts to
first order.  Pinned jamming would force the train velocity to vanish, contradiction.
Thus \(\Theta\) has no loops.

## 51.2 Hull chords are interval cuts

If \(U\) is a cyclic interval of boundary chains, summing (51.1) over \(j\in U\)
telescopes to the chord joining its endpoints.  Therefore, for an active diameter
bar \(h\) and either cyclic interval \(U_h\) between its endpoints,

\[
\boxed{
d_{h\tau}=(\partial^{\mathsf T}\mathbf1_{U_h})_\tau,
\qquad
r_h=\sum_\tau d_{h\tau}u_\tau.
}
\tag{51.2}
\]

Thus every active diameter constraint is an interval-cut constraint on the terminal
graph.

## 51.3 Terminal direction map

Define

\[
(\mathcal Dv)_j
=\sum_\tau\partial_{j\tau}Ju_\tau v_\tau.
\tag{51.3}
\]

This is the derivative of the chain vector in (51.1).  If \(\mathcal Dv=0\), all
hull-chain vectors are fixed.  After one translation, all hull vertices are fixed.
The train-angle motion preserves all contacts to first order, so pinned jamming
forces every vertex velocity to vanish.  Along an edge of train \(\tau\), relative
velocity is \(Ju_\tau v_\tau\); hence \(v_\tau=0\).  Therefore

\[
\boxed{\ker\mathcal D=\{0\}.}
\tag{51.4}
\]

Every subset of columns is consequently independent.  If a subgraph \(\Theta'\)
has \(V'\) vertices and \(c(\Theta')\) nonempty components, its vector-incidence
matrix has two row-sum dependencies per component.  Hence

\[
\boxed{
|E(\Theta')|\le2|V'|-2c(\Theta').
}
\tag{51.5}
\]

The scalar incidence matrix has rank \(q-c(\Theta)\), so its scalar cycle space
satisfies

\[
\boxed{
\dim\ker\partial=T-q+c(\Theta)\ge T-q+1.
}
\tag{51.6}
\]

This explains why the same one-integer scale \(T-q+1\) appears in the blocker rank
lower bound, but it does **not** identify scalar circulations with neutral train-angle
motions.

---

# 52. Terminal-turn theorem and boundary-velocity blocker form

## 52.1 Terminal-turn factorization

Put

\[
C(\Theta)=\ker\partial.
\tag{52.1}
\]

For each terminal-chain vertex \(j\), define

\[
t_j=\dim\operatorname{aff}
\{u_\tau:\partial_{j\tau}\ne0\}\in\{0,1,2\}.
\tag{52.2}
\]

For \(z\in C(\Theta)\), choose an incident reference train \(\rho(j)\).  Since
\(\sum_\tau\partial_{j\tau}z_\tau=0\),

\[
\begin{aligned}
(\mathcal Dz)_j
&=\sum_\tau\partial_{j\tau}Ju_\tau z_\tau\\
&=\sum_\tau\partial_{j\tau}
J(u_\tau-u_{\rho(j)})z_\tau.
\end{aligned}
\tag{52.3}
\]

Thus the \(j\)-th block lies in a space of dimension at most \(t_j\).  Since
\(\mathcal D\) remains injective on \(C(\Theta)\),

\[
\boxed{
T-q+c(\Theta)
=\operatorname{rank}(\mathcal D|_{C(\Theta)})
\le\sum_{j=1}^qt_j.
}
\tag{52.4}
\]

Combining with (48.3),

\[
\boxed{
\sum_jt_j
\ge0.3338292869\ldots D-o(D)+c(\Theta).
}
\tag{52.5}
\]

Because \(t_j\le2\), at least

\[
\boxed{
\frac{T-q+c(\Theta)}2
\ge0.1669146434\ldots D-o(D)
}
\tag{52.6}
\]

terminal chains contain a genuine affine direction turn.  Repeated incidences of one
common direction carry no scalar-cycle rank.

## 52.2 Boundary velocity of an active chord

For a train-angle velocity \(x\), put

\[
y=\mathcal Dx.
\tag{52.7}
\]

Summing (51.3) over the interval \(U_h\) and using (51.2) gives

\[
\boxed{
\dot r_h(x)=\sum_{j\in U_h}y_j.
}
\tag{52.8}
\]

Hence

\[
\boxed{
g_h(x)=r_h\cdot\sum_{j\in U_h}y_j.}
\tag{52.9}
\]

Moreover,

\[
Jr_h\cdot\dot r_h(x)
=\sum_\tau\lambda_{h\tau}x_\tau,
\tag{52.10}
\]

so

\[
\boxed{
s_h(x)=
\frac{Jr_h}{D^2}\cdot\sum_{j\in U_h}y_j.
}
\tag{52.11}
\]

On the neutral space \(\mathcal L\), (52.9) vanishes, so \(\dot r_h\perp r_h\), and

\[
\boxed{
x\in\mathcal L
\Longrightarrow
\dot r_h(x)=s_h(x)Jr_h.
}
\tag{52.12}
\]

Thus \(s_h\) is exactly the angular velocity of the active diameter chord.

Since \(\mathcal D\) is injective, the strict-backward row on
\(Y=\operatorname{im}\mathcal D\) becomes

\[
\boxed{
\ell_{h\tau}(\mathcal D^{-1}y)
=(\mathcal D^{-1}y)_\tau
-
\frac{Jr_h}{D^2}\cdot\sum_{j\in U_h}y_j.
}
\tag{52.13}
\]

This inverse-coordinate minus interval-rotation functional is the correct object for
a determinant/matroid analysis of shell capacity.

## 52.3 Rejected cycle-lift inference

The tempting statement

\[
\operatorname{rank}(\mathcal D|_{\ker\partial})
<\dim\ker\partial
\tag{52.14}
\]

after "imposing" blocker conditions cannot be obtained by restricting the domain.
Indeed, for every subspace \(W\subseteq\ker\partial\), injectivity (51.4) gives

\[
\boxed{
\ker(\mathcal D|_W)=0,
\qquad
\operatorname{rank}(\mathcal D|_W)=\dim W.
}
\tag{52.15}
\]

Shrinking the domain merely lowers its dimension.  Projecting the codomain can
create a kernel, but such a vector need not satisfy \(\mathcal Dz=0\) and therefore
is not a pinned flex.  Furthermore,

\[
\ker\partial\not\subseteq\mathcal L,
\qquad
\mathcal L\not\subseteq\ker\partial
\tag{52.16}
\]

in general: scalar circulation equations \(\partial z=0\) and the weighted radial
interval-cut equations \(g_hz=0\) are different systems.

Accordingly, a valid closing theorem must construct an actual intertwining between
(52.13), the radial-neutral subspace of \(Y\), and the terminal-turn quotient.  Pure
cycle-space counting is a dead route.

---

# 53. Corrected six-block facial peeling: backward rank or optimal flat

The algebraic peeling mechanism from the continuation is valid, but the earlier
claim that a globally diameter-invisible train is automatically impossible is not
needed and is not promoted.  The correct theorem is the following.

> **Theorem 53.1 (six-block peeling dichotomy).**
> Let \(K=\ker\mathcal B\subseteq\mathcal L\), \(k=\dim K\), in a pure simply
> connected strict-rhombic-disk global minimizer.  Then either
>
> \[
> k\le5,
> \tag{53.1}
> \]
>
> or there exists a triangle-free pure-rhombic-disk global minimizer of the same
> diameter \(D\), arbitrarily close to the original (possibly the original itself),
> whose train-angle realization space contains a local same-\(D\) manifold of
> dimension at least
>
> \[
> \boxed{k-5.}
> \tag{53.2}
> \]
>
> If the construction reaches a strict-separation stage after at least one face has
> been protected, the nearby minimizer may additionally be chosen with strictly
> fewer active diameter bars.

### Proof

Lift \(K\) to \(\widetilde K\), so \(\dim\widetilde K=k+1\).  At a peeling stage let
\(U\) be the trains still allowed to vary, \(W\subseteq\mathbb R^U\) the surviving
subspace, and \(P\) the already protected active bars satisfying

\[
d_{h\tau}=0
\qquad(h\in P,\ \tau\in U).
\tag{53.3}
\]

Thus every bar in \(P\) is exactly independent of the remaining \(U\)-angle
coordinates.

Let

\[
E_0=\{h:H_h|_W\equiv0\}
\tag{53.4}
\]

among the unprotected active bars.  Choose \(v\in W\) outside the finite union of
proper quadratic equality subspaces, so \(H_h[v,v]<0\) for every unprotected
\(h\notin E_0\).

If there is a \(U\)-supported acceleration \(y\) with

\[
g_h\cdot y<0
\qquad(h\in E_0),
\tag{53.5}
\]

then for sufficiently small \(\varepsilon>0\)

\[
\phi(t)=\phi+t v+\frac{\varepsilon t^2}{2}y
\tag{53.6}
\]

strictly shortens every unprotected active diameter at order \(t^2\), while the bars
in \(P\) remain exactly at \(D\).  At the first stage \(P=\varnothing\), this would
contradict the definition of \(D(n)\).  At a later stage the protected bars keep the
diameter equal to \(D\), all formerly unprotected active bars acquire strict slack,
and all inactive constraints retain slack for small \(t\).  Hence the resulting
configuration is another global minimizer, with fewer active diameter bars.  A small
open set of \(U\)-angle variations remains feasible and same-\(D\), giving a local
optimal manifold of dimension at least \(\dim W\).

If (53.5) has no solution, finite-dimensional separation gives a nonempty
\(S\subseteq E_0\) and positive coefficients with

\[
\sum_{h\in S}\beta_hg_h^U=0.
\tag{53.7}
\]

The minimal-face factorization from Section 49 applies on \(W\).  If \(m\) distinct
nonzero potential functionals occur and \(I\subseteq U\) is the train set invisible
to all bars in \(S\), then

\[
mD\le|U\setminus I|.
\tag{53.8}
\]

Setting all \(S\)-potentials equal to zero removes at most \(m\) dimensions and
leaves a subspace \(W'\) supported on \(I\):

\[
\dim W'\ge\dim W-m.
\tag{53.9}
\]

Replace \((U,W,P)\) by \((I,W',P\cup S)\) and iterate.  The train sets removed at
different rounds are disjoint, so

\[
D\sum_jm_j\le T.
\tag{53.10}
\]

Since \(T<2\pi D\),

\[
\sum_jm_j\le6.
\tag{53.11}
\]

Therefore any terminal surviving subspace has dimension at least

\[
(k+1)-6=k-5.
\tag{53.12}
\]

If the iteration terminates because no trains remain, then \(k\le5\).  Otherwise the
surviving train set \(U\) is invisible to **every** active diameter bar.  For every
active bar \(h\), its coefficient vector has \(d_{h\tau}=0\) for all \(\tau\in U\),
so its diameter vector is exactly independent of arbitrary \(U\)-angle variations.
All unit rhombus contacts are preserved exactly by the train-angle realization, and
all inactive distance inequalities have a strict margin.  Consequently a sufficiently
small neighborhood in the surviving \(W\)-directions consists of triangle-free
global minimizers of diameter exactly \(D\).  This is the local same-\(D\) manifold
in (53.2).  No global-invisible-train impossibility claim is required.  \(\square\)

A direct corollary is the corrected macroscopic alternative

\[
\boxed{
\operatorname{rank}\mathcal B
\ge\dim\mathcal L-5
\ge T-q-5
}
\tag{53.13}
\]

**unless a local same-diameter optimal train flat occurs.**  Using (48.3),

\[
\boxed{
\operatorname{rank}\mathcal B
\ge0.3338292869\ldots D-o(D)-5
}
\tag{53.14}
\]

unless the pure branch exits into the optimal-flat alternative.

This is the authoritative replacement for the earlier statement that a globally
invisible train must be impossible.

---

# 54. Exact diameter-plateau theorem and Target A optimal flat

> **HISTORICAL FRONTIER NOTE.** Theorem 54.1 remains part of the trusted stack.
> The coarse dimensional bookkeeping in Section 54.2 is retained for provenance but
> is superseded by the exact rooted-forest identity in Section 60 and the rattlerized
> Target A normal form in Sections 62--64.

## 54.1 Diameter plateaus have boundary-order length

> **Theorem 54.1.**  For arbitrary integers \(2\le m<n\), if
>
> \[
> D(m)=D(n)=D,
> \tag{54.1}
> \]
>
> then
>
> \[
> \boxed{n-m<\frac\pi2D.}
> \tag{54.2}
> \]

### Proof

Apply finite Oler, the isodiametric inequality, and the perimeter-diameter inequality
to an \(n\)-point minimizer:

\[
\begin{aligned}
n-1
&\le\frac2{\sqrt3}\operatorname{area}(K)+\frac12\operatorname{per}(K)\\
&\le\frac2{\sqrt3}\frac{\pi D^2}{4}+\frac{\pi D}{2}\\
&=\frac{D^2}{c}+\frac{\pi D}{2}.
\end{aligned}
\tag{54.3}
\]

The strict translated-lattice theorem at \(m\) gives

\[
D^2=D(m)^2<c(m-1),
\qquad
\frac{D^2}{c}<m-1.
\tag{54.4}
\]

Substitution in (54.3) yields

\[
n-1<m-1+\frac{\pi D}{2},
\]

which is (54.2).  \(\square\)

Thus an exact plateau of the optimal-diameter sequence cannot have super-boundary
length.

## 54.2 The hybrid forest lineality is an actual optimal flat

Let \(\mathcal L_{\widehat Q}(\widehat A)\) be the pinned bridge-forest lineality of
dimension \(\ell\).  For every sufficiently small
\(w\in\mathcal L_{\widehat Q}\), an old unit contact \(ij\) satisfies

\[
(p_i-p_j)\cdot(w_i-w_j)=0,
\]

so

\[
\boxed{
|p_i+w_i-p_j-w_j|^2
=1+|w_i-w_j|^2\ge1.
}
\tag{54.5}
\]

Every active diameter pair has pinned endpoints and therefore remains exactly fixed.
Every inactive inequality retains strict slack in a sufficiently small ball.
Consequently the triangle-free global-minimizer set contains a genuine local affine
ball of dimension \(\ell\).

Target A is therefore not a missing higher-order rigidity problem.  It is an
**optimal-flat capacity/occupancy problem**.

Let \(u\) be the number of genuinely moving forest vertices after contracting every
edge fixed throughout the flat.  Since the flat lives in \(2u\) scalar coordinates,

\[
u\ge\left\lceil\frac\ell2\right\rceil.
\tag{54.6}
\]

A particularly strong sufficient bridge would be

\[
\boxed{D(n-u)=D(n).}
\tag{54.7}
\]

At the v1.1 stage, Theorem 54.1 combined only with the coarse estimate (54.6), giving

\[
u<\frac\pi2D,
\qquad
\boxed{\ell<\pi D.}
\tag{54.8}
\]

**Superseding note.** Theorem 60.1 later proves \(\ell\le u\). Therefore, under the
same still-unproved deletion-inheritance hypothesis (54.7), the current conditional
conclusion is the stronger

\[
\boxed{\ell\le u<\frac\pi2D.}
\tag{54.8a}
\]

Equation (54.8) is retained only as historical v1.1 bookkeeping.

But (54.7) is **not** automatic: deleting the moving vertices leaves a unit-separated
configuration of diameter \(D\), not necessarily a globally optimal configuration
for cardinality \(n-u\).  Thus the exact Target A gap is either a proof of
same-diameter deletion inheritance or a direct occupancy/reattachment proof of

\[
\boxed{\ell=O(D).}
\tag{54.9}
\]

---

# 55. Ferrers endpoint and ordered shell resources

> **HISTORICAL FRONTIER NOTE.** The Ferrers estimate, terminal resources, and
> phase-atomic inequalities in this section remain trusted. Their v1.1 frontier
> interpretation is superseded by the componentwise decomposition in Sections 65--68.

The shell theorem is now a rank-and-order problem rather than a scalar boundary
count.

## 55.1 Ferrers staircase estimate

Let a Ferrers diagram have row lengths

\[
d_1\ge d_2\ge\cdots\ge d_a,
\qquad d_i\le b,
\tag{55.1}
\]

and let

\[
L=\max_i i\,d_i
\tag{55.2}
\]

be the largest all-ones Cartesian rectangle.  Since \(d_i\le\min(b,L/i)\), putting
\(k=\lfloor L/b\rfloor\) gives

\[
\begin{aligned}
e=\sum_{i=1}^ad_i
&\le kb+\sum_{i=k+1}^a\frac Li\\
&\le L+L\log\frac{ab}{L}+O(a+b).
\end{aligned}
\tag{55.3}
\]

Hence

\[
\boxed{
e\le L\left(1+\log\frac{ab}{L}\right)+O(a+b).
}
\tag{55.4}
\]

For a tight wall with \(a,b=D+o(D)\), if no actual Cartesian block of asymptotic
area \(D^2/\sqrt3\) is present, then

\[
L\le\frac{D^2}{\sqrt3}+o(D^2),
\tag{55.5}
\]

and therefore

\[
\boxed{
e\le
\frac{1+\log\sqrt3}{\sqrt3}D^2+o(D^2)
=0.8944923195\ldots D^2+o(D^2).
}
\tag{55.6}
\]

The rhombus crossing count is

\[
R=\frac{\pi}{2\sqrt3}D^2+o(D^2)
=0.9068996821\ldots D^2+o(D^2),
\tag{55.7}
\]

leaving the positive leading-order gap

\[
\boxed{0.0124073626\ldots D^2+o(D^2).}
\tag{55.8}
\]

This becomes a contradiction only after proving that the relevant blocker/crossing
mass is concentrated in one tight ordered wall or in a controlled collection of
walls.  That concentration theorem is open.

## 55.2 Terminal and boundary resources

The v1.0.0 terminal-pair theorem remains in force: every separating train with
\(\lambda_{h\tau}\le0\) has both terminal edges off the convex hull, and different
trains have different terminal pairs.  The boundary-curvature theorem gives

\[
\boxed{
r_3\ge2(T-q)+4
\ge0.6676585739\ldots D-o(D).
}
\tag{55.9}
\]

The terminal-turn theorem adds a rank-sensitive resource:

\[
\sum_jt_j\ge T-q+c(\Theta).
\tag{55.10}
\]

Thus repeated equal-direction walls cannot provide unlimited independent scalar
circulation rank.

## 55.3 Phase-atomic bounds: correct logical use

Let \(s\) be the limiting atomic train mass, \(y=q/T\), and \(x=T/D\).  The audited
bounds are

\[
\boxed{s\le1-\frac y2,}
\tag{55.11}
\]

\[
\boxed{
\limsup\frac{R}{T^2}
\le\frac14\left(1-\frac y2\right)^2,
}
\tag{55.12}
\]

and

\[
\boxed{s\ge\frac{2}{\sqrt c\,x}.}
\tag{55.13}
\]

The **combination** of the lower and upper bounds, not (55.11) alone, shows that a
positive fraction of train mass is forced into finitely many near-triangular phase
grains while another controlled fraction remains available for the non-atomic hull
regularization.  Within a coherent grain, same-phase train families are internally
noncrossing and ordered.  This is the geometric setting in which an interval/Ferrers
blocker theorem must be proved.

---

# 56. Exact v1.1.0 remaining lemmas

> **HISTORICAL -- SUPERSEDED FRONTIER.** This section records the v1.1 target.
> Equations (56.1)--(56.2) remain the total pure upper/lower rank targets, but the
> authoritative v1.2 residual budget after isolating component rotations is Section 68.2.
> Target A is superseded by Sections 60--64.

The continuation compresses the Level I problem to the following statements.

## 56.1 Pure ordered blocker--turn coforest lemma

Under the pure strict-rhombic-disk hypotheses and \(G+E<c_0B\), with the convention
\(I=0,r=1\) if \(K=0\), prove

\[
\boxed{
\operatorname{rank}\mathcal B+I+r\le T-q
}
\tag{56.1}
\]

unless at least one of the following already occurs:

1. \(G+E\ge c_0B\);
2. an exact \(60^\circ\) rhombus occurs;
3. an actual Cartesian block violates the audited global capacity bound;
4. a genuine diameter-decreasing feasible motion exists; or
5. the configuration enters the same-diameter optimal-flat alternative of
   Theorem 53.1.

This would contradict the proved lower bound

\[
\boxed{
\operatorname{rank}\mathcal B+I+r\ge T-q+1.
}
\tag{56.2}
\]

The proof must operate on the actual blocker functionals (52.13), the peripheral dual
span (50.21), and the terminal-turn quotient (52.4).  It must **not** invoke the
rejected cycle-lift argument.

The desired combinatorial content is that independent backward rows, peripheral
Dirichlet data, and terminal potential blocks leave at least \(q\) protected ordered
continuation slots.  Equality should force exact triangular continuation, a zero
phase difference, or an oversized Cartesian block.

## 56.2 Topology-corrected extension

The pure theorem must be transported through the \(O(D)\) exceptional shell:
nonquadrilateral faces, holes, multiple rhombic components, boundary pinches, and
vertices outside the rhombic core.  Each exception must be represented as a finite-
rank transfer gadget whose rank is charged to the exact topology-corrected shell
residual (48.5).  An uncontrolled \(O(D)\) rank loss is not sufficient, because the
pure contradiction is a one-integer deficit.

## 56.3 Optimal-flat / bridge-forest capacity theorem

The unified flat branch now contains both:

- the local same-\(D\) train-angle flat supplied by Theorem 53.1; and
- the hybrid bridge-forest affine flat of Section 54.2.

For the forest branch it is sufficient to prove

\[
\boxed{\ell=O(D),}
\tag{56.3}
\]

or the stronger deletion-inheritance statement (54.7).  More ambitiously, prove a
single optimal-flat capacity theorem saying that a triangle-free global minimizer
cannot possess a same-diameter contact-preserving flat of super-boundary dimension
unless its boundary hits an exact triangle event or an independently chargeable
shell obstruction.

This would absorb the train-flat alternative of Target B and Target A into one
mechanism.

---

# 57. Preferred next proof architecture

> **HISTORICAL -- SUPERSEDED STRATEGY.** Retained to document the v1.1 route.
> For current work use the saturated-rattler program of Section 64 and the
> component-quotiented internal blocker program of Sections 67--68.

## 57.1 Work in the boundary-velocity image

Let

\[
Y=\operatorname{im}\mathcal D,
\]

and define the radial-neutral subspace

\[
Y_0=
\left\{
y\in Y:
 r_h\cdot\sum_{j\in U_h}y_j=0
 \text{ for every active }h
\right\}.
\tag{57.1}
\]

On \(Y_0\), each backward row is the exact functional

\[
b_{h\tau}(y)
=(\mathcal D^{-1}y)_\tau
-
\frac{Jr_h}{D^2}\cdot\sum_{j\in U_h}y_j.
\tag{57.2}
\]

Every peripheral free datum is a difference of coordinate functionals associated to
peripheral zero-stress cuts.

## 57.2 Ordered blocker-to-turn matroid target

At each terminal chain, quotient its incidence data by the common train direction;
the resulting local turn space has dimension \(t_j\).  Construct an explicit
intertwining map taking:

- independent backward rows;
- peripheral Dirichlet differences; and
- terminal rigid-potential blocks

into ordered turn/coforest slots.  The map must satisfy:

1. repeated use of one staircase wall contributes only its actual independent turns;
2. cycles of wall potentials telescope;
3. a complement of a blocker basis contains at least \(q\) protected continuation
   slots;
4. equality forces exact triangular continuation or a Cartesian block.

The Ferrers gap (55.8) is the quantitative endpoint if most crossing mass
concentrates in a tight wall.  If the blocker rank spreads across many walls, the
alternative endpoint should be a lower bound on independent terminal turns strong
enough to force the exact shell gate.

## 57.3 Optimal-flat route

For a same-diameter optimal flat, contract every edge fixed throughout the flat and
study the first-event walls of the remaining moving rooted clusters.  Generic-event
selection alone is insufficient because codimension-one triangle walls can bound the
flat.  The desired theorem is instead one of:

1. flat-to-deletion inheritance \(D(n-u)=D(n)\);
2. an occupancy/free-volume bound giving \(u=O(D)\);
3. a Dirichlet/turn theorem charging at least one independent shell slot per bounded
   number of flat dimensions.

The exact plateau theorem then turns any genuine same-diameter cardinality
inheritance into an explicit \(O(D)\) dimension bound.

## 57.4 Routes not to repeat

The following remain dead or superseded:

- pure scalar cycle-space counting;
- interpreting a restriction of injective \(\mathcal D\) as a new kernel;
- abstract averaging-degree arguments without order;
- tangent incidence counting;
- one active diameter bar per higher-order mode;
- a fixed KKT stress as a universal Hessian certificate;
- raw support depth as Oler currency;
- generic dense-graph biclique extraction;
- generic first-event selection in an optimal flat;
- assuming deletion from an optimal flat preserves optimality;
- the unconditional globally-invisible-train exclusion used in the raw continuation;
- the older two-potential wall theorem as a required dependency.

---

# 58. Version 1.1.0 exact status

> **HISTORICAL STATUS.** This section is the frozen v1.1 status and is superseded
> by the v1.2 status in Section 69.

**LEVEL I STATUS: STILL OPEN.**

The v1.1.0 theorem state sharpens the final architecture substantially.

## Target B — jammed almost-rhombic branch

For the pure disk, the first-order-neutral train space has dimension at least

\[
0.3338292869\ldots D-o(D).
\]

The minimal-face and harmonic--Dirichlet theorems show that visible tangent quartic
transport has at most five non-rotational potential degrees, while all but at most
six dimensions of an equality kernel are dual-detected by peripheral zero-stress
cuts.  The terminal direction graph gives an exact interval-cut representation of
active diameter bars and identifies affine direction turns as the scalar terminal
cycle-rank resource.  The corrected facial-peeling theorem yields the macroscopic
dichotomy

\[
\boxed{
\text{macroscopic strict-backward/Dirichlet rank}
\quad\text{or}\quad
\text{macroscopic same-}D\text{ optimal flat}.
}
\tag{58.1}
\]

The unresolved pure theorem is the ordered blocker--turn/coforest upper bound
(56.1).  It must then be made topology-correct without losing the exact one-integer
deficit.

## Target A — flexible bridge-forest branch

The bridge-forest lineality is now known to be an actual local affine family of
triangle-free global minimizers.  Exact plateaus of \(D(n)\) have length
\(<(\pi/2)D\), but deletion of moving vertices is not known to preserve global
optimality.  The unresolved theorem remains

\[
\boxed{\ell=O(D),}
\]

or a stronger optimal-flat inheritance theorem implying it.

## Unified endgame

The most economical Level I proof would establish two compatible capacity facts:

1. an ordered shell cannot carry the macroscopic independent backward/Dirichlet rank
   forced by Target B while \(G+E<c_0B\); and
2. a triangle-free global minimizer cannot support a same-diameter optimal flat of
   super-boundary dimension.

The first should terminate in the exact shell gate, a \(60^\circ\) rhombus, or an
oversized Cartesian block.  The second should terminate in the plateau theorem,
occupancy saturation, or an exact triangle wall.

No theorem in v1.1.0 closes both statements, and no infinite family of triangle-free
**global** minimizers is known.  No proof or disproof is claimed.

---

# 59. Version history and provenance

- **v1.0.0 (2026-08-26):** canonical synthesis and second-pass audit through the
  translated-lattice, phase-atomic, first-order cusp, backward-flip, tangent-quartic,
  support-turning, and hybrid-forest reductions.
- **v1.1.0 (2026-08-26):** promotes the audited minimal-face harmonic--Dirichlet,
  peripheral-dual, terminal direction-network/turn, boundary-velocity, exact plateau,
  and optimal-flat results; rejects the cycle-lift shortcut; corrects facial peeling
  to the backward-rank-or-optimal-flat dichotomy.

The only supplied external literature remains:

1. `mp05-2-261-269.pdf`;
2. `1951-03.pdf`;
3. `1-s2.0-S0097316598928898-main.pdf`;
4. `s00454-002-0747-6.pdf`;
5. `1204.4403v1.pdf`;
6. `463.pdf`;
7. `10.1007_PL00009374.pdf`.

No internet source is part of this theorem-state file.

---

# 60. Rooted-forest rank and self-stress theorem

Let \(F\) be the quotient bridge forest in the hybrid representative.  Let

- \(u\) be the number of unpinned forest vertices;
- \(r\) be the number of incident fixed roots;
- \(c\) be the number of nonempty forest components;
- \(R_F\) be the pinned contact-equality matrix, with \(2u\) scalar columns;
- \(\ell=\dim\ker R_F\) be the pinned contact-preserving lineality; and
- \(\sigma=\dim\ker R_F^{\mathsf T}\) be the pinned forest self-stress dimension.

Here a self-stress is an unrestricted linear dependence among the forest contact
rows; equilibrium is imposed only in the unpinned columns.

> **Theorem 60.1 (rooted-forest rank/self-stress identity).**
> One has
> \[
> \boxed{
> \ell=u-r+c+\sigma,
> \qquad
> 0\le\sigma\le r-c.
> }
> \tag{60.1}
> \]
> Consequently
> \[
> \boxed{
> u-r+c\le\ell\le u,
> \qquad
> 0\le u-\ell=r-c-\sigma\le r-c.
> }
> \tag{60.2}
> \]
> Since \(r\le |\widehat Q|\le\pi D\),
> \[
> \boxed{0\le u-\ell\le\pi D.}
> \tag{60.3}
> \]

### Proof

The forest has

\[
e=u+r-c
\tag{60.4}
\]

edges.  Every retained edge is incident with an unpinned vertex, so every edge gives
one nonzero row of \(R_F\).  Since

\[
\operatorname{rank}R_F=e-\sigma,
\]

rank-nullity gives

\[
\ell
=2u-(e-\sigma)
=u-r+c+\sigma.
\tag{60.5}
\]

It remains to prove \(\operatorname{rank}R_F\ge u\).  In one tree component with
\(u_i\) unpinned vertices and \(r_i\ge1\) fixed roots, delete \(r_i-1\) edges so that
each resulting component contains exactly one root.  The retained forest has exactly
\(u_i\) edges.

These \(u_i\) contact rows are independent.  In every nontrivial one-root tree there
is an unpinned leaf.  The two coordinate columns of that leaf occur in only its unique
incident row, whose contact vector is nonzero.  Hence the coefficient of that row in
any row dependence is zero.  Remove the leaf and iterate.  All coefficients vanish.
Summing over components gives \(u\) independent rows.  Thus

\[
\sigma=e-\operatorname{rank}R_F
\le (u+r-c)-u=r-c.
\]

This proves (60.1)--(60.3). \(\square\)

The estimate is sharp.  A tree with one fixed root has \(e=u\), \(\sigma=0\), and
\(\ell=u\).  Therefore rooted-forest linear algebra alone cannot yield
\(\ell\le\alpha u+O(D)\) with any \(\alpha<1\).

The authoritative Target A parameter is henceforth \(u\), not an abstract lineality:

\[
\boxed{\ell=u-O(D).}
\tag{60.6}
\]

A super-boundary hybrid flat is asymptotically one degree of freedom per moving
forest vertex.

---

# 61. Root-skeleton exactification

The affine flat from Section 54.2 is enough for rattlerization, but the hybrid branch
also admits a large genuine exact-unit-bar manifold after paying only boundary-order
contacts.

Let \(S\) be the minimal subtree of each forest component spanning its fixed roots.
Pin every nonroot vertex of \(S\) having degree at least three in \(S\).  Let \(b\)
be the total number of such newly pinned branch vertices.

> **Lemma 61.1 (branch count).**
> \[
> \boxed{b\le r-c.}
> \tag{61.1}
> \]

### Proof

In a tree whose minimal root-spanning subtree has \(r_i\) root leaves/vertices and
\(b_i\) nonroot vertices of degree at least three, the usual degree identity
\(\sum_v(\deg v-2)=-2\) gives \(b_i\le r_i-1\).  Summing gives
\(b\le r-c\). \(\square\)

Suppress the remaining degree-two vertices of the root skeleton.  The resulting
forest has

\[
k=r+b-c
\tag{61.2}
\]

skeleton paths between roots and/or pinned branch vertices.  Cut one old contact edge
on each such path.

> **Theorem 61.2 (root-skeleton exactification).**
> There is a nearby triangle-free global minimizer of the same diameter carrying a
> smooth exact-contact manifold \(\mathcal M\) such that
> \[
> \boxed{
> \dim\mathcal M=u-b\ge u-r+c,
> }
> \tag{61.3}
> \]
> while the number of old forest contacts made strict is at most
> \[
> \boxed{
> L_{\rm lost}\le r+b-c\le2(r-c).
> }
> \tag{61.4}
> \]

### Proof

After cutting one edge from each skeleton path, every remaining forest component
contains exactly one fixed vertex: either an original root or a newly pinned branch
vertex.  There are \(u-b\) unpinned vertices and exactly \(u-b\) retained forest
edges.

For a one-fixed-root tree, the unit vector of every edge may be chosen independently;
positions are then recovered uniquely by summing edge vectors from the root.  Hence
the abstract bar-realization space is a product of circles and is smooth of dimension
equal to the number of retained edges.  Locally, all previously inactive pair
inequalities remain open conditions.  Thus the retained forest supplies a smooth
\((u-b)\)-dimensional exact-unit-bar manifold.

It remains to open the cut contacts.  Consider one skeleton path and one of its two
halves.  Let \(A\) be the fixed special endpoint of the half, \(x=A+v\) its movable
endpoint at the cut, and \(y\) the opposite cut endpoint.  Rigidly rotate the entire
half, including all off-skeleton branches attached to it, about \(A\).  All retained
contacts in that half remain exactly unit.  Put

\[
F(\phi)=|A+R_\phi v-y|^2.
\tag{61.5}
\]

At \(\phi=0\), \(F(0)=1\), and

\[
F'(0)=2(x-y)\cdot Jv.
\tag{61.6}
\]

If this is nonzero, choose the sign of \(\phi\) for which the cut edge length
increases.  If \(F'(0)=0\), then \(x-y=\pm v/|v|\), and

\[
F''(0)=2\bigl(|v|^2\mp|v|\bigr).
\tag{61.7}
\]

In the minus-sign case this is positive.  In the plus-sign case, unit separation
between \(A\) and \(y\) excludes \(|v|<1\); equality \(|v|=1\) would force
\(y=A\), impossible for the two distinct endpoints of a simple cut path.  Hence
\(F''(0)>0\) in the only remaining case.

The supports associated with distinct suppressed skeleton paths are disjoint except
at fixed special vertices, so sufficiently small opening rotations may be chosen
simultaneously.  All inactive lower and upper inequalities retain strict slack.
Original diameter pairs have fixed endpoints and remain exactly \(D\).  The nearby
configuration is therefore another triangle-free global minimizer.  The number of
cut contacts is \(k=r+b-c\), giving (61.4). \(\square\)

Combining Sections 60 and 61,

\[
\boxed{
\dim\mathcal M\ge u-(r-c)\ge \ell-(r-c)\ge\ell-\pi D.
}
\tag{61.8}
\]

The stronger claim that one can always retain a full \(u\)-dimensional exact-bar
manifold is not promoted: a branch junction can be locally caged by several fixed unit
neighbors.  Pinning at most \(r-c\) such junctions is the sharp safe reduction used
below.

---

# 62. Affine forest factor exclusion and rattlerization

After the root-skeleton reduction, let \(F\) denote the remaining forest of one-root
components.  Put

\[
v=u-b.
\tag{62.1}
\]

Then \(F\) has exactly \(v\) unpinned vertices and \(v\) retained unit edges.
Orient each retained edge away from the unique fixed vertex of its component and
write its unit vector as \(u_e\).

The pinned first-order contact-preserving space is parametrized by one scalar \(x_e\)
per retained edge:

\[
w_{\operatorname{child}(e)}-w_{\operatorname{parent}(e)}
=x_eJu_e.
\tag{62.2}
\]

Because the graph is a one-root forest, this gives a linear isomorphism

\[
\mathbb R^{E(F)}\cong W,
\qquad
\dim W=v.
\tag{62.3}
\]

For two labels \(a,b\), fixed or moving, let

\[
F_{ab}(x)
=
\left|
 p_a-p_b+w_a(x)-w_b(x)
\right|^2-1.
\tag{62.4}
\]

For an oriented retained edge \(e\), let \(T_e\) be the descendant subtree below
its child endpoint, and define

\[
\eta_e(a)=
\begin{cases}
1,&a\in T_e,\\
0,&a\notin T_e,
\end{cases}
\qquad
\epsilon_e^{ab}=\eta_e(a)-\eta_e(b)\in\{-1,0,1\}.
\tag{62.5a}
\]

Every fixed label has \(\eta_e=0\) for every retained edge. Equivalently, one may
identify all fixed vertices to one abstract super-root; then \(\epsilon_e^{ab}\ne0\)
exactly when the cut defined by \(e\) separates \(a\) and \(b\) in this super-rooted
forest. This convention works whether the labels lie in the same one-root component
or in different components. The rooted path formula gives

\[
w_a-w_b
=
\sum_e\epsilon_e^{ab}x_eJu_e.
\tag{62.5}
\]

Hence the coefficient of \(x_e^2\) in \(F_{ab}\) is
\((\epsilon_e^{ab})^2\). Therefore

\[
\boxed{
F_{ab}\text{ depends on }x_e
\iff
\eta_e(a)\ne\eta_e(b).
}
\tag{62.6}
\]

## 62.1 Algebraic triangle-wall lemma

> **Lemma 62.1.**
> Suppose three nonzero real polynomials on \(\mathbb R^v\) vanish simultaneously on
> a relatively open codimension-one smooth semialgebraic set.  Then their common
> zero set has a height-one real algebraic component; equivalently the three
> polynomials share a nonconstant irreducible factor.

### Proof

The Zariski closure of a real semialgebraic set of dimension \(v-1\) has algebraic
dimension at least \(v-1\).  Since the defining polynomials are nonzero, the closure
has a codimension-one irreducible component.  Its prime ideal has height one.  The
polynomial ring over \(\mathbb R\) is a UFD, so every height-one prime is generated by
one irreducible polynomial.  That generator divides all three polynomials. \(\square\)

> **Theorem 62.2 (affine forest triangle-factor exclusion).**
> Every relatively open codimension-one triangle wall in the affine forest flat has
> an identically unit side.  Moreover that persistent side lies entirely in the fixed
> part: the old core, a fixed diameter vertex, or one of the \(b\) pinned branch
> junctions.

### Proof

Suppose a codimension-one wall carries a unit triangle \(i,j,k\), while none of
\(F_{ij},F_{jk},F_{ki}\) is identically zero on \(W\).  By Lemma 62.1 they have a
common nonconstant irreducible factor \(P\).  Choose a variable \(x_e\) on which
\(P\) depends.  Degree in one variable is additive under multiplication in a domain,
so every polynomial divisible by \(P\) depends on \(x_e\).  By (62.6), edge \(e\)
must separate each of the three pairs

\[
ij,\qquad jk,\qquad ki.
\]

But for a fixed descendant set \(T_e\), membership of the three labels is a
\(0+3\) or \(1+2\) bipartition. Thus \(\eta_e\) differs on either no pair or exactly
two of the three pairs, never all three. Contradiction.

Thus one triangle side is identically unit on \(W\). If either endpoint of that side
were an unpinned forest vertex, some retained edge has a descendant subtree containing
exactly one endpoint, so (62.6) would give a nonzero quadratic term. Hence both
endpoints are fixed. \(\square\)

This theorem does not contradict the regression that length-two triangle walls on the
exact-bar torus can have rank \(v-O(1)\).  The theorem concerns the affine straight
forest flat, on which nonfixed old bars open quadratically.

## 62.2 Rattlerization

> **Theorem 62.3 (forest rattlerization).**
> There is a nearby triangle-free global minimizer of the same diameter in which all
> \(v=u-b\) unpinned vertices of the reduced forest are genuine strict rattlers.
> Denote this strict-rattler set by \(\mathscr R\). Its vertices have no unit contact,
> no active diameter incidence, and strict slack in every constraint involving them.
> Consequently
> \[
> \boxed{
> |\mathscr R|\ge v=u-b\ge u-r+c\ge\ell-(r-c),
> }
> \tag{62.7}
> \]
> and the local same-\(D\) minimizer set contains an open ball of dimension at least
> \[
> \boxed{
> 2|\mathscr R|\ge2(u-r+c)\ge2\ell-2(r-c).
> }
> \tag{62.8}
> \]
> In particular, since \(r-c\le\pi D\),
> \[
> \boxed{
> |\mathscr R|\ge\ell-\pi D,
> \qquad
> \dim_{\rm local}\mathcal O_D\ge2\ell-2\pi D.
> }
> \tag{62.9}
> \]

### Proof

Choose \(x\in\mathbb R^{E(F)}\) with \(x_e\ne0\) for every retained edge and let
\(w=w(x)\).  For sufficiently small nonzero \(t\), move every unpinned forest vertex
by \(tw_i\).  For a retained forest edge \(e=ij\),

\[
p_i(t)-p_j(t)=u_e+t x_eJu_e,
\]

so

\[
\boxed{
|p_i(t)-p_j(t)|^2=1+t^2x_e^2>1.
}
\tag{62.10}
\]

The contacts cut in Section 61 already have strict slack.  Every other inactive
lower- or upper-distance constraint remains strict for sufficiently small \(t\).
The unpinned forest vertices are not diameter endpoints; all active diameter pairs
have fixed endpoints and remain exactly \(D\).  Hence the new configuration is a
triangle-free global minimizer of diameter \(D\).

Every reduced forest vertex is now strict against every other point.  A sufficiently
small product neighborhood in their \(2v\) Cartesian coordinates preserves all
inequalities while the fixed diameter pair keeps the diameter equal to \(D\).  This
proves (62.7)--(62.9). \(\square\)

Thus a surviving super-boundary Target A branch has the much stronger consequence

\[
\boxed{
\ell=\omega(D)
\Longrightarrow
\text{a nearby global minimizer has }\omega(D)
\text{ mutually independent strict rattlers.}
}
\tag{62.11}
\]

Target A is no longer a linkage-regularity problem.

---

# 63. Same-diameter saturation and strict replacement

## 63.1 Triangle-free saturation inside the fixed hull

> **Theorem 63.1 (same-diameter saturation).**
> Let \(A\) be a triangle-free \(n\)-point global minimizer of diameter \(D\), with
> \(K=\operatorname{conv}A\).  Then \(A\) is contained in a triangle-free global
> minimizer \(A^+\subset K\) of the same diameter satisfying
> \[
> \boxed{|A^+\setminus A|<\frac\pi2D,}
> \tag{63.1}
> \]
> and
> \[
> \boxed{
> K\subseteq\bigcup_{p\in A^+}\overline B(p,1).
> }
> \tag{63.2}
> \]
> If a specified finite subset of \(A\) consists of strict rattlers, the added points
> may be chosen generically so that those vertices remain non-diametral strict
> rattlers.

### Proof

While there is a point \(y\in K\) with \(|y-p|>1\) for every point in the current
set, add such a \(y\).  It creates no unit contact, hence no triangle.  All points
remain in \(K\), so their diameter is at most \(D\); the original diameter pair
remains, so the diameter is exactly \(D\).  Monotonicity of the optimal-diameter
sequence therefore makes every intermediate configuration globally optimal at its
new cardinality.

The process terminates because a bounded region contains only finitely many mutually
unit-separated points.  At termination (63.2) holds.  If the final cardinality is
\(N\), then \(D(N)=D(n)=D\), so Theorem 54.1 gives
\(N-n<(\pi/2)D\).

At each insertion step the available uncovered set is relatively open in \(K\).
Avoiding finitely many diameter circles around a prescribed strict-rattler set does
not exhaust it, so the original strict rattlers can be kept non-diametral. \(\square\)

Consequently, if Target A survives at super-boundary scale, it may be normalized to a
**unit-covering saturated** global minimizer while retaining \(\omega(D)\) strict
rattlers and adding only boundary-order many points.

## 63.2 Open-disk lattice replacement

The finite Oler inequality for an \(n\)-point minimizer gives

\[
n-1\le\frac{D^2}{c}+\frac{\pi D}{2}.
\tag{63.3}
\]

The mean number of points of a translated triangular lattice in the open disk of
diameter \(D\) is \(D^2/c\).  As in the strict translated-lattice argument, a
translate has strictly more than the mean.  Therefore there is a unit-separated set
of diameter strictly less than \(D\) with cardinality

\[
\boxed{
N_0>n-\frac{\pi}{2}D-1.
}
\tag{63.4}
\]

Thus fewer than \((\pi/2)D+1\) additional sites separate a strict sub-\(D\) lattice
replacement from the full cardinality \(n\).

## 63.3 Parallel-body identity and collar growth

Let an \(m\)-point minimizer have diameter \(d\), hull \(K_m\), area deficit

\[
\delta_m=\frac{\pi d^2}{4}-\operatorname{area}K_m
\]

and perimeter deficit

\[
\varepsilon_m=\pi d-\operatorname{per}K_m.
\]

Put

\[
t=\frac{D-d}{2}.
\]

Steiner's formula gives the exact identity

\[
\boxed{
\operatorname{area}(K_m+tB)
=
\frac{\pi D^2}{4}-\delta_m-\varepsilon_mt.
}
\tag{63.5}
\]

Using \(\delta_m<c_0P_m\) and the audited strict perimeter deficit
\(\varepsilon_m<2\pi c_0\), one obtains

\[
\boxed{
\delta_m+\varepsilon_mt<c_0\pi D.
}
\tag{63.6}
\]

This parallel-body population estimate is exact, but by itself is weaker than the
open-disk estimate (63.4).  Its value is geometric: it provides a scaffold and a
collar in which missing sites might be grafted.

Now let \(\rho=|\mathscr R|\) be the number of strict rattlers and put \(m=n-\rho\).  The Oler lower
bound at \(n\) and the strict translated-lattice upper bound at \(m\) give

\[
\boxed{
D^2-D(m)^2
>
c\left(\rho-\frac{\pi}{2}D\right).
}
\tag{63.7}
\]

Hence, with \(d=D(m)\),

\[
\boxed{
\frac{D-d}{2}
>
\frac{c}{4D}
\left(\rho-\frac{\pi}{2}D\right).
}
\tag{63.8}
\]

If \(\rho/D\to\infty\), the available collar width tends to infinity.

Equations (63.4) and (63.8) reduce Target A to a precise packing problem: a strict
sub-\(D\) replacement misses only \(O(D)\) points while a super-boundary rattler
population produces a diverging-width geometric collar.

---

# 64. Target A after rattlerization

The exact remaining Target A theorem can now be stated without any forest-kinematic
language.

> **Target A1 (saturated rattler-capacity theorem).**
> Let \(A\) be a triangle-free global minimizer of diameter \(D\), normalized as in
> Theorems 62.3 and 63.1.  Let \(\mathscr R\subset A\) be the set of vertices satisfying
> \[
> 1<|p-q|<D
> \qquad(q\in A\setminus\{p\}).
> \tag{64.1}
> \]
> Put \(\rho=|\mathscr R|\). Prove
> \[
> \boxed{\rho=O(D).}
> \tag{64.2}
> \]

Since \(\rho\ge\ell-\pi D\), this immediately gives \(\ell=O(D)\) and closes the
hybrid branch.

A stronger sufficient geometric form is:

> **Target A2 (scaffolded grafting theorem).**
> If \(\rho/D\to\infty\), use the \(m=n-\rho\) optimum, the collar (63.8), and the
> strict lattice replacement (63.4) to embed the missing \(O(D)\) sites compatibly
> inside a region of diameter \(<D\), producing \(n\) unit-separated points of
> diameter \(<D\).

The correct next language is Hall/matching or local finite-Oler capacity, not
single-ray linkage deformation.  A Hall deficiency should force one of:

1. a boundary-order region containing too many strict rattlers;
2. an exact area-plus-perimeter capacity violation;
3. an oversized ordered Cartesian block; or
4. a reusable saturated covering cell from which a missing replacement site can be
   grafted.

The following approaches are explicitly superseded for Target A:

- another rooted-forest rank count;
- raw first-event normal rank;
- assuming deletion of the rattlers preserves optimality;
- treating codimension-one triangle walls on the exact-bar torus as low-rank;
- requiring the forest linkage itself to realize prescribed lattice positions.

---

# 65. Terminal-component Minkowski decomposition

Return to the pure simply connected strict-rhombic disk.  Let \(\Theta\) be the
terminal graph from Section 51, with hull-chain vertices \(1,\ldots,q\), train edges,
and oriented incidence matrix \(\partial\).  Put

\[
e_j=z_{j+1}-z_j
=
\sum_\tau\partial_{j\tau}u_\tau.
\tag{65.1}
\]

Let \(C\) be a connected component of \(\Theta\), and let \(J_C\) be its hull-chain
vertex set.

> **Theorem 65.1 (component closure and Minkowski splitting).**
> For every terminal component,
> \[
> \boxed{
> \sum_{j\in J_C}e_j=0.
> }
> \tag{65.2}
> \]
> The vectors \(\{e_j:j\in J_C\}\), in their inherited cyclic angular order, are the
> edge vectors of a possibly degenerate convex polygon \(K_C\).  Up to translation,
> \[
> \boxed{
> K=K_1+\cdots+K_{c(\Theta)}.
> }
> \tag{65.3}
> \]

### Proof

Every train edge of component \(C\) has both terminal vertices in \(J_C\).  Hence

\[
\sum_{j\in J_C}e_j
=
\sum_{\tau\in E(C)}u_\tau
\sum_{j\in J_C}\partial_{j\tau}
=0.
\]

The hull side vectors are already cyclically ordered by direction.  Any subsequence
inherits that order; together with zero sum it forms the edge sequence of a convex
polygon, allowing degenerate segment summands.  Minkowski addition merges convex
polygon edge sequences in angular order, so the union of the component edge
sequences reconstructs the original hull sequence.  This proves (65.3). \(\square\)

This identifies the formerly mysterious terminal components as genuine convex
Minkowski summands of the hull.

---

# 66. Componentwise turn closure and equality classification

For terminal chain \(j\), choose an incident reference train \(\rho(j)\) and put

\[
L_j=
\operatorname{span}
\{J(u_\tau-u_{\rho(j)}):\partial_{j\tau}\ne0\},
\qquad
t_j=\dim L_j\in\{0,1,2\}.
\tag{66.1}
\]

For component \(C\), define

\[
s_C=
\dim\operatorname{span}_{j\in J_C}L_j.
\tag{66.2}
\]

> **Theorem 66.1 (componentwise closure-corrected turn inequality).**
> \[
> \boxed{
> |E(C)|-|V(C)|+1
> \le
> \sum_{j\in J_C}t_j-s_C.
> }
> \tag{66.3}
> \]
> Summing over components,
> \[
> \boxed{
> T-q+c(\Theta)
> \le
> \sum_jt_j-\sum_Cs_C.
> }
> \tag{66.4}
> \]

### Proof

On the scalar cycle space \(\ker\partial_C\), the terminal direction lift factors
through \(\bigoplus_{j\in J_C}L_j\).  Moreover every direction velocity
\(y=\mathcal Dz\) satisfies

\[
\sum_{j\in J_C}y_j=0,
\tag{66.5}
\]

because summing the incidence columns over a component gives zero.  The summation map

\[
\bigoplus_{j\in J_C}L_j
\longrightarrow
\operatorname{span}_{j\in J_C}L_j
\]

is surjective and has rank \(s_C\).  Thus the closure-constrained codomain has
dimension \(\sum t_j-s_C\).  Since \(\mathcal D\) is injective, its restriction to
\(\ker\partial_C\) is injective.  The domain has dimension
\(|E(C)|-|V(C)|+1\), proving (66.3).  Sum over \(C\). \(\square\)

The missing \(c(\Theta)\)-scale geometric closure relations are therefore literal
vector-closure relations of the Minkowski summands; they are not supplied by a fake
kernel of \(\mathcal D\).

> **Theorem 66.2 (equality geometry of \(s_C\)).**
> \[
> \boxed{
> \begin{array}{ll}
> s_C=0
> &\Longrightarrow
> C\text{ is a tree and all its trains have one oriented direction};\\[1mm]
> s_C=1,\ C\text{ cyclic}
> &\Longrightarrow
> C\text{ uses exactly two train directions};\\[1mm]
> s_C=2
> &\Longrightarrow
> C\text{ contains genuine two-dimensional phase turning}.
> \end{array}
> }
> \tag{66.6}
> \]

### Proof

If \(s_C=0\), then all \(L_j=0\).  At each terminal vertex all incident oriented
train vectors are equal, and connectivity propagates one common vector \(u\) through
\(C\).  If \(C\) had a scalar cycle \(z\ne0\), then
\(\mathcal Dz=Ju\,\partial z=0\), contradicting injectivity.  Hence \(C\) is a tree.

If \(s_C=1\), all local direction-difference spaces lie in one common line \(L\).
At a terminal vertex with at least two incident directions, all incident unit vectors
lie on one affine line parallel to \(L\).  Shared train edges propagate that same
affine line through the connected component.  An affine line meets the unit circle in
at most two points.  A cyclic component cannot use only one direction by the first
case, so it uses exactly two.  The \(s_C=2\) statement is the definition of genuine
two-dimensional turning. \(\square\)

Thus every cyclic component either pays two-dimensional closure or is an exact
two-family ordered system, precisely the regime where the Ferrers endpoint applies.

---

# 67. Stochastic Minkowski-width formula for component rotations

Let \(h\) be an active diameter bar with

\[
r_h=De_h.
\]

For terminal component \(C\), define

\[
r_{h,C}
=
\sum_{j\in U_h\cap J_C}e_j.
\tag{67.1}
\]

Then

\[
r_h=\sum_Cr_{h,C}.
\tag{67.2}
\]

Because every active diameter direction has unique support maximizer and minimizer,
\(r_{h,C}\) is the support chord of the Minkowski summand \(K_C\) in direction
\(e_h\).  Hence

\[
\boxed{
 r_h\cdot r_{h,C}=D\,w_{K_C}(e_h),
}
\tag{67.3}
\]

and width additivity gives

\[
\boxed{
\sum_C w_{K_C}(e_h)=D.
}
\tag{67.4}
\]

Now give every train in component \(C\) the same angular velocity \(\alpha_C\).
Then

\[
\dot r_{h,C}=\alpha_CJr_{h,C}.
\tag{67.5}
\]

Using the exact bar-rotation formula from Section 52,

\[
\boxed{
 s_h(\alpha)
 =
 \sum_C
 \frac{w_{K_C}(e_h)}D\,\alpha_C.
}
\tag{67.6}
\]

Put

\[
a_{hC}=\frac{w_{K_C}(e_h)}D.
\tag{67.7}
\]

Then

\[
\boxed{
 a_{hC}\ge0,
 \qquad
 \sum_Ca_{hC}=1.
}
\tag{67.8}
\]

Thus on the component-rotation quotient a backward/blocker row belonging to a train
of component \(C\) has the stochastic harmonic-difference form

\[
\boxed{
 \alpha_C-
 \sum_{C'}a_{hC'}\alpha_{C'}.
}
\tag{67.9}
\]

Every such row annihilates common component rotation. Therefore

\[
\boxed{
\operatorname{rank}\mathcal B_{\rm comp.rot.}
\le c(\Theta)-1.
}
\tag{67.10}
\]

Potential cycles telescope because (67.9) is an exact stochastic averaging system.
This is the first explicit intertwining of a nontrivial part of the **actual inverse
blocker** with the Minkowski terminal decomposition.

For rank bookkeeping, let \(\mathscr S_\alpha\) be the span in the blocker-row space
of the component-rotation restrictions (67.9), and put

\[
\boxed{
r_\alpha:=\dim\mathscr S_\alpha\le c(\Theta)-1.
}
\tag{67.10a}
\]

Write henceforth

\[
x_\tau=\alpha_C+\xi_\tau
\qquad(\tau\in E(C)),
\tag{67.11}
\]

where \(\alpha_C\) is common component rotation and \(\xi\) is the internal
relative-angle coordinate. Quotient the blocker-row span by \(\mathscr S_\alpha\),
and denote the induced internal row family by \(\overline{\mathcal B}_\xi\). Then

\[
\boxed{
\operatorname{rank}\mathcal B
\le r_\alpha+\operatorname{rank}\overline{\mathcal B}_\xi.
}
\tag{67.12}
\]

Thus the component-rotation contribution is **isolated and bounded, not free**. The
remaining unbounded contribution is the internal \(\xi\)-part, but any final coforest
inequality must explicitly reserve the rank budget \(r_\alpha\).

---

# 68. Exact v1.2.0 remaining lemmas

> **HISTORICAL v1.2 FRONTIER.** Target A in this section is superseded by Sections 71--75.
> Target B remains valid and is restated without substantive change in Section 76.

## 68.1 Target A: saturated rattler capacity

The hybrid branch is closed if one proves

\[
\boxed{
\rho=O(D)
}
\tag{68.1}
\]

for the saturated rattlerized representative of Sections 62--63, where
\(\rho=|\mathscr R|\).

Equivalently, it is sufficient to prove the scaffolded grafting theorem of Target A2:
when \(\rho/D\to\infty\), the diverging collar (63.8) and the boundary-order missing
population (63.4) permit an \(n\)-point unit-separated configuration of diameter
strictly below \(D\).

The next viable mechanism is a Hall-type matching/capacity theorem.  Candidate missing
replacement sites should be matched to disjoint rattler/Voronoi covering cells in the
saturated hull.  A Hall deficiency must be converted into a finite Oler or ordered
shell capacity violation.

## 68.2 Target B: internal component blocker/coforest theorem

Let \(\mathscr S_\alpha\), \(r_\alpha\), and
\(\overline{\mathcal B}_\xi\) be as in Section 67. After quotienting the component
rotations, construct an explicit injective matroidal map from the **internal** parts of

- the backward rows \(b_{h\tau}\);
- the peripheral free-coordinate differences; and
- the terminal rigid-potential blocks

into the componentwise closure-corrected turn/coforest spaces. The exact sufficient
residual inequality is

\[
\boxed{
\operatorname{rank}\overline{\mathcal B}_\xi+I+r
\le T-q-r_\alpha.
}
\tag{68.2a}
\]

Since \(r_\alpha\le c(\Theta)-1\), the stronger component-count-only statement

\[
\boxed{
\operatorname{rank}\overline{\mathcal B}_\xi+I+r
\le T-q-c(\Theta)+1
}
\tag{68.2b}
\]

is also sufficient. Indeed, (67.12) and either residual bound give the desired total
pure inequality

\[
\boxed{
\operatorname{rank}\mathcal B+I+r\le T-q.
}
\tag{68.2}
\]

This contradicts the established lower bound

\[
\boxed{
\operatorname{rank}\mathcal B+I+r\ge T-q+1.
}
\tag{68.3}
\]

The proof should split terminal components by Theorem 66.2:

1. if \(s_C=2\), use both vector-closure equations and the internal turn quotient;
2. if \(s_C=1\) and \(C\) is cyclic, use the exact two-family ordering and the
   Ferrers staircase theorem;
3. tree/one-direction components contribute no scalar cycle obstruction;
4. component rotations are paid separately by the explicit budget \(r_\alpha\) in
   (67.10a)--(67.12), not silently discarded or mixed into the internal rank count.

The available two-family numerical endpoint remains

\[
0.8944923195\ldots D^2
<
0.9068996821\ldots D^2,
\tag{68.4}
\]

with gap

\[
\boxed{0.0124073626\ldots D^2.}
\tag{68.5}
\]

No improved constant is presently required.

## 68.3 Topology-corrected Target B

After (68.2) is proved in the pure disk, it must still be transported through
nonquadrilateral faces, holes, multiple components, boundary pinches, and vertices
outside the rhombic core.  Each exceptional gadget must be charged **exactly** to the
topology-corrected residual.  An uncontrolled \(O(D)\) rank loss remains fatal to the
one-integer contradiction.

---

# 69. Version 1.2.0 exact status

> **HISTORICAL STATUS.** Retained as the frozen v1.2 endpoint. The authoritative
> status is Section 77.

**LEVEL I STATUS: STILL OPEN.**

Version 1.2.0 compresses the two remaining branches substantially beyond v1.1.0.

## Target A — saturated strict-rattler branch

The hybrid forest now has the exact rank identity

\[
\ell=u-r+c+\sigma,
\qquad
0\le\sigma\le r-c,
\]

and can be transformed, after losing only \(O(D)\) old contacts, into a nearby
triangle-free global minimizer containing

\[
\boxed{
\rho=|\mathscr R|\ge u-r+c\ge\ell-\pi D
}
\tag{69.1}
\]

genuine strict rattlers.  The local same-\(D\) minimizer set then has dimension at
least

\[
2\rho\ge2\ell-2\pi D.
\tag{69.2}
\]

After adding fewer than \((\pi/2)D\) further points, the fixed hull may also be
assumed unit-covering saturated without destroying the original strict rattlers.

Therefore the old forest-flex problem is superseded by the precise global question:

\[
\boxed{
\text{Can a triangle-free globally optimal diameter-}D\text{ packing contain }
\omega(D)\text{ strict rattlers?}
}
\tag{69.3}
\]

The remaining proof target is the saturated rattler-capacity theorem or an equivalent
Hall/grafting contradiction.

## Target B — internal terminal-component rank

The terminal graph components are exact Minkowski summands of the hull.  Their scalar
cycle rank satisfies the strengthened closure inequality

\[
T-q+c(\Theta)
\le
\sum_jt_j-\sum_Cs_C.
\tag{69.4}
\]

Cyclic \(s_C=1\) components are exactly two-direction systems; \(s_C=2\) components
carry genuine two-dimensional closure. Uniform component rotations enter every
active diameter bar through stochastic width weights. Their row span
\(\mathscr S_\alpha\) has explicit rank budget \(r_\alpha\le c(\Theta)-1\).

Thus the common component rotations are isolated rather than mysterious, but their
rank is not free: it must be reserved in the final count. The exact remaining pure
theorem is the internal residual inequality (68.2a), or the stronger universal
version (68.2b), which together with (67.12) yields the total blocker--turn/coforest
inequality (68.2). The topology-corrected extension then remains.

## Unified endgame

A Level I proof now needs two global capacity statements:

1. **rattler capacity:** a saturated diameter minimizer cannot carry a
   super-boundary population of strict rattlers; and
2. **internal shell rank:** after Minkowski component rotations are quotiented, the
   ordered terminal shell cannot carry the independent internal backward/Dirichlet
   rank forced by the pure survivor while \(G+E<c_0B\).

The first is now a packing/covering/grafting theorem.  The second is now a
componentwise ordered matroid/Ferrers theorem.  Neither is a first-order rigidity
problem.

No theorem in v1.2.0 closes both statements, and no infinite sequence of triangle-free
**global** minimizers is known.  No proof or disproof is claimed.

---

# 70. Version history and provenance through v1.2.0

> **HISTORICAL VERSION LEDGER.** This section was the v1.2 endpoint. The current
> version ledger is Section 78.

- **v1.0.0 (2026-08-26):** canonical synthesis and second-pass audit through the
  translated-lattice, phase-atomic, first-order cusp, backward-flip, tangent-quartic,
  support-turning, and hybrid-forest reductions.
- **v1.1.0 (2026-08-26):** promotes the minimal-face harmonic--Dirichlet,
  peripheral-dual, terminal direction-network/turn, boundary-velocity, exact plateau,
  and optimal-flat results; rejects the cycle-lift shortcut; corrects facial peeling.
- **v1.2.0 (2026-08-26):** promotes the rooted-forest self-stress identity,
  root-skeleton exactification, affine triangle-factor exclusion, forest
  rattlerization, same-diameter saturation, strict replacement/collar reduction,
  terminal-component Minkowski splitting, componentwise closure/equality theorem, and
  stochastic-width control of component rotations.  The authoritative remaining
  branches are saturated rattler capacity and internal terminal-component blocker
  rank.

The only supplied external literature remains:

1. `mp05-2-261-269.pdf`;
2. `1951-03.pdf`;
3. `1-s2.0-S0097316598928898-main.pdf`;
4. `s00454-002-0747-6.pdf`;
5. `1204.4403v1.pdf`;
6. `463.pdf`;
7. `10.1007_PL00009374.pdf`.

No internet source is part of this theorem-state file.

---

# 71. Compatible collar and exact safe-scaffold population

This section upgrades the population-only replacement of Section 63 to a scaffold
that is already geometrically compatible with an independently chosen smaller
optimum.

Keep the saturated Target A normalization. Thus

\[
|A|=N,
\qquad
\operatorname{diam}(A)=D,
\qquad
\rho=|\mathscr R|,
\]

where \(\mathscr R\) is the retained strict-rattler set. Put

\[
m=N-\rho,
\qquad
d=D(m),
\qquad
t=\frac{D-d}{2}.
\tag{71.1}
\]

Let \(X_m\) be an independently chosen \(m\)-point optimum, let
\(K_m=\operatorname{conv}X_m\), and write

\[
P_m=\operatorname{per}K_m,
\qquad
\varepsilon_m=\pi d-P_m.
\tag{71.2}
\]

The trusted perimeter-deficit theorem gives

\[
0\le\varepsilon_m<2\pi c_0=\pi a_0,
\qquad
a_0=\frac{\sqrt3}{2}.
\tag{71.3}
\]

Define

\[
\boxed{
C_{\rm col}
:=
\pi\left(\frac12+\frac2{\sqrt3}\right)
=
5.198395055263\ldots .
}
\tag{71.4}
\]

## 71.1 Unconditional compatible-collar dichotomy

> **Theorem 71.1 (compatible-collar dichotomy).**
> One has
> \[
> \boxed{
> \rho<C_{\rm col}D
> }
> \tag{71.5}
> \]
> or else \(t>1\) and there is a translated unit triangular-lattice set
> \(S\) such that
> \[
> X:=X_m\cup S
> \subset
> \operatorname{int}(K_m+t\mathbb B),
> \tag{71.6}
> \]
> \(X\) is unit-separated,
> \[
> \boxed{\operatorname{diam}(X)<D,}
> \tag{71.7}
> \]
> and
> \[
> \boxed{
> |X|>N-C_{\rm col}D+\frac{2\pi}{\sqrt3}.
> }
> \tag{71.8}
> \]
> In particular, the weaker but cleaner statement
> \[
> |X|>N-C_{\rm col}D
> \tag{71.9}
> \]
> always holds in the second alternative.

### Proof

If \(t\le1\), then

\[
D^2-d^2
=(D-d)(D+d)
=2t(D+d)
\le4D.
\tag{71.10}
\]

The trusted collar inequality (63.7) says

\[
D^2-d^2
>
c\left(\rho-\frac{\pi D}{2}\right),
\qquad
c=\frac{2\sqrt3}{\pi}.
\tag{71.11}
\]

Hence

\[
\rho
<
\frac{\pi D}{2}+\frac{4D}{c}
=
\pi\left(\frac12+\frac2{\sqrt3}\right)D
=C_{\rm col}D.
\tag{71.12}
\]

Thus \(\rho\ge C_{\rm col}D\) forces \(t>1\).

Assume now \(t>1\) and define the safe collar

\[
\Omega
:=
\operatorname{int}(K_m+t\mathbb B)
\setminus
(K_m+\mathbb B).
\tag{71.13}
\]

Every point of \(\Omega\) is at distance strictly greater than \(1\) from every
point of \(X_m\). Steiner's formula gives

\[
\begin{aligned}
|\Omega|
&=P_m(t-1)+\pi(t^2-1)\\
&=\frac{\pi}{4}(D^2-d^2)-\pi(d+1)-\varepsilon_m(t-1).
\end{aligned}
\tag{71.14}
\]

Using (71.3), (71.11), and \(\pi c/4=a_0\),

\[
\frac{|\Omega|}{a_0}
>
\rho-
\left[
\frac{\pi D}{2}
+
\frac{\pi(d+1)}{a_0}
+
\pi(t-1)
\right].
\tag{71.15}
\]

Since \(d=D-2t\), the bracket equals

\[
C_{\rm col}D
+
\pi\left(1-\frac4{\sqrt3}\right)t
+
\pi\left(\frac2{\sqrt3}-1\right).
\tag{71.16}
\]

Therefore

\[
\boxed{
\frac{|\Omega|}{a_0}
>
\rho-C_{\rm col}D
+
\pi\left(\frac4{\sqrt3}-1\right)t
+
\pi\left(1-\frac2{\sqrt3}\right).
}
\tag{71.17}
\]

For \(t\ge1\), this implies the uniform estimate

\[
\boxed{
\frac{|\Omega|}{a_0}
>
\rho-C_{\rm col}D+\frac{2\pi}{\sqrt3}.
}
\tag{71.18}
\]

For completeness, the strictness needed below is a property of this particular
parallel-body collar, not of arbitrary measurable sets.  If

\[
F(v):=|(\Lambda+v)\cap\Omega|,
\qquad v\in\mathbb R^2/\Lambda,
\]

then \(F\) has mean \(|\Omega|/a_0\) by periodization.  It is also a nonconstant
integer-valued function.  Indeed, \(K_m\) is the convex hull of finitely many
points, so an outer offset \(\partial(K_m+t\mathbb B)\) contains a nonempty
circular arc (with the degenerate segment/point cases giving the usual capsule or
circle).  Choose a regular point of such an arc away from the finitely many other
translated boundary sheets in a fundamental cell.  Distinct circular sheets of
the same radius can coincide only when their centers coincide; coincident outer
sheets have the same inside side and therefore contribute with the same sign.
The inner sheets have a different radius, so they cannot cancel this jump.  A
small translation across the chosen point therefore changes \(F\) by a nonzero
integer.  Consequently some translate has
\(F(v)>|\Omega|/a_0\): if every value were at most its mean, integrality would
force the mean down to the largest attained integer, while nonconstancy makes
that inequality strict.

The same strict translation-averaging argument used in the translated-lattice
theorem supplies a translate of the unit triangular lattice having

\[
k>
\rho-C_{\rm col}D+\frac{2\pi}{\sqrt3}
\tag{71.19}
\]

sites in \(\Omega\). Let \(S\) be those sites. The lattice sites are mutually
unit-separated and are strictly more than unit distance from \(X_m\), so
\(X_m\cup S\) is unit-separated.

The closed parallel body \(K_m+t\mathbb B\) has diameter \(d+2t=D\). No two
interior points can realize that diameter: otherwise one endpoint could be moved a
small positive distance farther along the joining line while remaining in the closed
parallel body, contradicting its diameter. Hence every finite subset of its interior,
in particular \(X_m\cup S\), has diameter strictly less than \(D\).
Finally

\[
|X_m\cup S|
=m+k
>
N-C_{\rm col}D+\frac{2\pi}{\sqrt3}.
\]

This proves the theorem. \(\square\)

## 71.2 Interpretation

The theorem is stronger than the open-disk population estimate (63.4): the new sites
are already simultaneously compatible with the chosen \(m\)-point optimum. It does
**not** yet provide all \(N\) points. In a surviving counterexample the exact number
of missing sites after the safe-collar insertion is

\[
j:=N-(m+k)=\rho-k.
\tag{71.20}
\]

If \(j\le0\), the theorem already contradicts \(D(N)=D\). Hence every survivor must
satisfy

\[
\boxed{
1\le j=\rho-k
<
C_{\rm col}D-\frac{2\pi}{\sqrt3}.
}
\tag{71.21}
\]

Thus the remaining compatible-grafting demand is explicitly boundary-order.

---

# 72. Deep Voronoi containment and global clearance budget

Return to the original saturated triangle-free global minimizer \(A\), with
\(K=\operatorname{conv}A\). Define the nearest-neighbor clearance

\[
\delta(p):=
\min_{q\ne p}|p-q|-1
\ge0.
\tag{72.1}
\]

A crucial warning is already visible here: strictness gives \(\delta(p)>0\) for a
strict rattler, but there is no uniform lower bound on \(\delta(p)\).

## 72.1 Deep Voronoi cells remain in the saturated hull

Let

\[
B_\partial
:=
\{p\in A:\operatorname{dist}(p,\partial K)\le1\},
\qquad
b:=|B_\partial|.
\tag{72.2}
\]

> **Lemma 72.1 (deep Voronoi containment).**
> If \(p\notin B_\partial\), then its Voronoi cell satisfies
> \[
> \boxed{V_p\subset K.}
> \tag{72.3}
> \]

### Proof

Suppose some \(x\in V_p\) lies outside \(K\). Since \(V_p\) is convex and contains
\(p\), the first point

\[
y=[p,x]\cap\partial K
\]

also belongs to \(V_p\). But \(p\) is more than unit distance from \(\partial K\), so
\(|p-y|>1\). Saturation of \(K\) supplies \(q\in A\) with \(|q-y|\le1\), contradicting
the nearest-site inequality defining \(V_p\). \(\square\)

Consequently every Delaunay face incident to a deep vertex has circumcenter in \(K\)
and circumradius at most \(1\). In a cocircular degeneracy, triangulate the empty
Delaunay polygon arbitrarily; all resulting triangles share the same admissible
circumcenter.

## 72.2 Sharp local Delaunay clearance inequality

For a Delaunay triangle \(T\) and a vertex \(v\in T\), define

\[
\mu_T(v)
:=
\min\{\text{the two side lengths of }T\text{ incident to }v\}-1.
\tag{72.4}
\]

> **Theorem 72.2 (local clearance inequality).**
> If \(T\) has all side lengths at least \(1\) and circumradius at most \(1\), then
> \[
> \boxed{
> \operatorname{area}(T)-\frac{\sqrt3}{4}
> \ge
> \frac{\sqrt3}{6}
> \sum_{v\in T}\mu_T(v).
> }
> \tag{72.5}
> \]
> The coefficient \(\sqrt3/6\) is sharp. Equality holds exactly for the ordered side
> multisets
> \[
> \boxed{
> \{1,1,1\}
> \quad\text{or}\quad
> \{1,1,\sqrt3\}.
> }
> \tag{72.6}
> \]

### Proof

Order the sides \(1\le a\le b\le c\), and let \(C\) be the angle opposite \(c\).
The circumradius bound and the lower side bound force every angle to be at least
\(\pi/6\). Hence

\[
\frac\pi3\le C\le\frac{2\pi}{3}.
\tag{72.7}
\]

Also \(b\le2\le2a\). Therefore

\[
\operatorname{area}(T)
=\frac12ab\sin C
\ge
\frac{\sqrt3}{4}ab
\ge
\frac{\sqrt3}{12}(2a^2+b^2),
\tag{72.8}
\]

because

\[
3ab-2a^2-b^2=(b-a)(2a-b)\ge0.
\tag{72.9}
\]

The three local minima in (72.4) are \(a,a,b\), so

\[
\sum_{v\in T}\mu_T(v)=2(a-1)+(b-1).
\tag{72.10}
\]

Applying \(x^2-1\ge2(x-1)\) to \(a\) and \(b\) proves (72.5).
Equality forces \(a=b=1\) and \(\sin C=\sqrt3/2\), so
\(C=\pi/3\) or \(2\pi/3\), yielding exactly (72.6). \(\square\)

## 72.3 Boundary-layer and global clearance estimates

Let

\[
h:=|A\cap\partial K|.
\tag{72.11}
\]

The disjoint radius-\(1/2\) disks centered at points of \(B_\partial\) lie in the
radius-\(3/2\) tube around \(\partial K\). Its area is at most

\[
3P+\frac{9\pi}{4},
\qquad P=\operatorname{per}K.
\]

Hence

\[
\boxed{
b\le\frac{12P}{\pi}+9\le12D+9.
}
\tag{72.12}
\]

Consecutive hull sites have boundary-arc separation at least their Euclidean
separation, hence at least \(1\), so

\[
\boxed{h\le P\le\pi D.}
\tag{72.13}
\]

Choose a Delaunay triangulation and let \(f_0\) be the number of faces whose three
vertices lie in \(B_\partial\). Planarity gives

\[
\boxed{f_0\le2b.}
\tag{72.14}
\]

There are

\[
F=2N-h-2
\tag{72.15}
\]

triangulation faces. Let \(E_{\rm deep}\) be the total excess
\(\operatorname{area}(T)-a_0/2\) over faces containing a deep vertex. The strict
translated-lattice theorem and isodiametricity give

\[
\operatorname{area}(K)<a_0(N-1).
\tag{72.16}
\]

Therefore

\[
\boxed{
E_{\rm deep}
<
\frac{a_0}{2}(h+f_0).
}
\tag{72.17}
\]

Every deep vertex is incident to at least three deep faces, and in each such face its
\(\mu_T\)-contribution is at least \(\delta(p)\). Since
\(\sqrt3/6=a_0/3\), summing (72.5) gives

\[
a_0\sum_{p\notin B_\partial}\delta(p)
\le E_{\rm deep},
\]

hence

\[
\boxed{
\sum_{p\notin B_\partial}\delta(p)
<
\frac{h+f_0}{2}.
}
\tag{72.18}
\]

Saturation also gives \(\delta(p)\le1\) for every \(p\in A\): if a nearest-neighbor
distance were \(r>2\), the midpoint of a nearest-neighbor pair would lie in \(K\)
and be farther than \(1\) from every site, contradicting unit covering.
Combining (72.12)--(72.18) yields the global theorem.

> **Theorem 72.3 (global clearance budget).**
> \[
> \boxed{
> \sum_{p\in A}\delta(p)
> <
> \left(24+\frac{\pi}{2}\right)D+18.
> }
> \tag{72.19}
> \]

Put

\[
L_D:=
\left(24+\frac{\pi}{2}\right)D+18.
\tag{72.20}
\]

The theorem says that a super-boundary strict-rattler population can survive only by
becoming overwhelmingly near-contact.

---

# 73. Near-unit Gabriel matching and the two-well theorem

Assume the saturated Target A survivor contains \(\rho\) retained strict rattlers.
If

\[
\rho\ge20L_D,
\tag{73.1}
\]

then at least \(\rho/2\) of those rattlers satisfy

\[
\delta(p)\le\frac{2L_D}{\rho}.
\tag{73.2}
\]

After discarding the boundary layer, at least \(\rho/2-b\) selected deep rattlers
remain. Join each selected rattler to one nearest neighbor.

## 73.1 Degree six and a linear matching

Under (73.1), every selected edge has length at most \(1.1\). If a vertex had seven
selected-edge neighbors, two would make angle at most \(2\pi/7\). Their mutual
distance would satisfy

\[
|q_1-q_2|^2
\le
\frac1{100}
+
\frac{121}{25}\sin^2\frac\pi7
=
0.9211546795\ldots<1,
\tag{73.3}
\]

contradicting unit separation. Thus the selected-edge graph has maximum degree at
most six.

A maximal matching edge \(uv\) accounts for at most
\(|N[u]\cup N[v]|\le12\) selected rattlers. Therefore:

> **Theorem 73.1 (deep near-unit matching).**
> There is a matching \(M\) of nearest-neighbor edges, every edge containing a deep
> strict rattler, such that
> \[
> \boxed{
> |M|
> \ge
> \frac{\rho}{24}-D-\frac34,
> }
> \tag{73.4}
> \]
> and
> \[
> \boxed{
> 1<|p-q|
> \le
> 1+\frac{2L_D}{\rho}
> \qquad(pq\in M).
> }
> \tag{73.5}
> \]

## 73.2 Strong Gabriel/Delaunay promotion

If \(pq\) is one of the selected edges and \(q\) is nearest to \(p\), the closed disk
with diameter \(pq\) contains no third site. Indeed, any third point in that disk is
strictly closer to \(p\) than \(q\). At the midpoint \(z\) of \(pq\), every third
site satisfies

\[
|z-x|>\frac{|p-q|}{2}.
\tag{73.6}
\]

Hence \(V_p\cap V_q\) contains a nondegenerate segment: \(pq\) is a strong Gabriel,
and therefore strong Delaunay, edge. All edges of the matching \(M\) can be included
simultaneously in one Delaunay triangulation. Rechoose such a triangulation from now
on. The global excess estimate (72.17) applies to this triangulation as well.

Because every matching edge contains a deep endpoint, it is not a hull edge and has
two incident deep Delaunay faces. A Delaunay triangle contains at most one matching
edge.

## 73.3 Matched two-well theorem

From (72.12)--(72.14),

\[
E_{\rm deep}
<
\frac{a_0}{2}\bigl((24+\pi)D+18\bigr).
\tag{73.7}
\]

Therefore, for every \(\eta>0\), fewer than

\[
\boxed{
\frac{a_0\bigl((24+\pi)D+18\bigr)}{2\eta}
}
\tag{73.8}
\]

matching edges are incident to a Delaunay face whose area excess above
\(\sqrt3/4\) exceeds \(\eta\).

> **Theorem 73.2 (matched two-well structure).**
> If \(\rho/D\to\infty\), choose
> \[
> \eta=\sqrt{\frac D\rho}.
> \tag{73.9}
> \]
> Then
> \[
> \boxed{
> \frac{\rho}{24}-o(\rho)
> }
> \tag{73.10}
> \]
> pairwise vertex-disjoint strong Delaunay edges have length \(1+o(1)\), and both
> incident Delaunay triangles have side triples at distance \(o(1)\) from
> \[
> \boxed{
> \mathcal E
> :=
> \bigl\{\{1,1,1\},\ \{1,1,\sqrt3\}\bigr\}.
> }
> \tag{73.11}
> \]

### Proof of the stability conclusion

The admissible side-length triples for deep Delaunay faces lie in a compact set:
all sides are in \([1,2]\), the triangle inequalities hold, and the circumradius is
at most \(1\). By Theorem 72.2, area excess tends to zero only at the equality set
(72.6). Compactness gives the stated two-well stability. \(\square\)

### Essential caveat: both wells survive asymptotically

Triangle-freeness forbids the exact \(\{1,1,1\}\) unit triangle but does **not** remove
that well from an asymptotic argument. An equilateral triangle of side
\(1+\varepsilon\) has no unit edge and has circumradius at most \(1\) for small
\(\varepsilon>0\), while

\[
\operatorname{area}(T_\varepsilon)-\frac{\sqrt3}{4}
-
\frac{\sqrt3}{6}\sum_v\mu_{T_\varepsilon}(v)
=
\frac{\sqrt3}{4}\varepsilon^2
\to0.
\tag{73.12}
\]

Therefore every “low excess implies only the \(120^\circ\) wedge” assertion is false.
The canonical equality regime is genuinely two-well: near-equilateral and
near-\(120^\circ\).

Equivalently, for every fixed \(\varepsilon_0>0\), compactness supplies
\(\kappa(\varepsilon_0)>0\) such that any admissible deep Delaunay face whose side
triple stays at least \(\varepsilon_0\) from both wells has area excess at least
\(\kappa(\varepsilon_0)\). Hence only
\(O(D/\kappa(\varepsilon_0))\) such exceptional faces can occur.

---

# 74. Exact Hall--Kőnig scaffold obstruction

The matched Delaunay geometry of Section 73 lives in the original saturated minimizer
\(A\). The scaffold of Section 71 lives around the independently chosen optimum
\(X_m\). They are not co-embedded. This section records what can nevertheless be
said exactly inside the scaffold itself.

Assume \(t>1\) and put

\[
L:=\operatorname{int}(K_m+t\mathbb B).
\tag{74.1}
\]

Choose the same translated unit triangular lattice used for the safe-collar estimate,
and let

\[
Y:=(\Lambda+v)\cap L.
\tag{74.2}
\]

Construct a bipartite conflict graph \(G\) with parts \(X_m\) and \(Y\), joining
\(x\in X_m\) to \(y\in Y\) exactly when

\[
|x-y|<1.
\tag{74.3}
\]

Let \(\nu\) be its maximum matching size.

> **Theorem 74.1 (exact Hall--Kőnig conflict inequality).**
> Every surviving triangle-free global minimizer satisfies
> \[
> \boxed{
> m+|Y|-\nu\le N-1.
> }
> \tag{74.4}
> \]
> Equivalently, for every \(S\subseteq Y\),
> \[
> \boxed{
> |S|-|N_G(S)|\le\rho-1.
> }
> \tag{74.5}
> \]

### Proof

Both \(X_m\) and \(Y\) are internally unit-separated. Hence a subset of
\(X_m\cup Y\) is unit-separated exactly when it is an independent set of the
bipartite conflict graph. Kőnig's theorem gives

\[
\alpha(G)
=|X_m|+|Y|-\tau(G)
=m+|Y|-\nu.
\tag{74.6}
\]

Every independent set lies in the open body \(L\) and therefore has diameter
strictly below \(D\). Since an \(N\)-point unit-separated subset of diameter below
\(D=D(N)\) is impossible, \(\alpha(G)\le N-1\), proving (74.4).
The standard deficiency form of Hall--Kőnig gives (74.5). \(\square\)

## 74.1 Safe collar plus inner-band near-perfect conflict matching

Let

\[
Y_0:=Y\cap\Omega,
\qquad
k:=|Y_0|,
\qquad
Y_{\rm in}:=Y\setminus Y_0.
\tag{74.7}
\]

By construction,

\[
N_G(Y_0)=\varnothing.
\tag{74.8}
\]

For every \(Q\subseteq Y_{\rm in}\), apply (74.5) to \(S=Y_0\cup Q\). Then

\[
k+|Q|-|N_G(Q)|\le\rho-1,
\]

so

\[
\boxed{
|Q|-|N_G(Q)|
\le
\rho-k-1
=j-1.
}
\tag{74.9}
\]

Hall's deficiency theorem therefore yields:

> **Corollary 74.2 (inner-band near-perfect conflict matching).**
> There is a matching from \(Y_{\rm in}\) into \(X_m\) that leaves at most
> \[
> \boxed{
> j-1=\rho-k-1
> <
> C_{\rm col}D-\frac{2\pi}{\sqrt3}-1
> }
> \tag{74.10}
> \]
> inner-band lattice sites unmatched.

This matching is a matching of **conflicts**, not a placement of missing points. It
states that a surviving counterexample must arrange for almost every inner-band
lattice site to be blocked by a distinct point of the smaller optimum.

## 74.2 Exact Hall-surplus contradiction target

The preceding theorem identifies an exact finite contradiction criterion.

> **Target 74.A (inner-band Hall surplus).**
> Produce some \(Q\subseteq Y_{\rm in}\) satisfying
> \[
> \boxed{
> |Q|-|N_G(Q)|\ge\rho-k=j.
> }
> \tag{74.11}
> \]

Then \(Y_0\cup Q\) has deficiency at least \(\rho\), so (74.5) fails. Equivalently,
the conflict graph contains an independent set of at least \(N\) vertices, yielding an
\(N\)-point unit-separated subset of \(L\) of diameter strictly below \(D\).

Thus Target A can now be closed either by constructing the missing \(j\) sites
directly or by forcing the one-integer Hall surplus (74.11).

---

# 75. Authoritative v1.3 Target A frontier

The forest, exact-bar, triangle-wall, and abstract-rattler stages are no longer the
current obstruction. In a super-boundary survivor \(\rho/D\to\infty\), the following
facts hold simultaneously:

1. a compatible strict sub-\(D\) scaffold already contains
   \(N-O(D)\) points;
2. the exact remaining demand is
   \[
   1\le j=\rho-k
   <C_{\rm col}D-\frac{2\pi}{\sqrt3};
   \tag{75.1}
   \]
3. the original saturated minimizer satisfies
   \[
   \sum_{p\in A}\delta(p)=O(D);
   \tag{75.2}
   \]
4. it carries
   \[
   \frac{\rho}{24}-o(\rho)
   \tag{75.3}
   \]
   disjoint strong-Delaunay near-unit edges with two-well neighborhoods; and
5. the independently constructed scaffold conflict graph has an inner-band matching
   missing only at most \(j-1=O(D)\) lattice sites.

Since \(|M|=\rho/24-o(\rho)\) and \(j=O(D)\), every super-boundary sequence with
\(j>0\) satisfies the divergent supply-to-demand ratio

\[
\boxed{
\frac{|M|}{j}\longrightarrow\infty.
}
\tag{75.4}
\]

The issue is therefore not a shortage of local structures. It is the absence of an
exact theorem transporting the enormous two-well supply in the original minimizer to
capacity in the independently positioned scaffold.

## 75.1 Exact remaining theorem

> **Target A v1.3 (two-well configuration-transfer / inner-band Hall-rigidity
> theorem).**
> In the simultaneous setting of Sections 71--74, prove that a super-boundary
> survivor cannot satisfy both
> \[
> |M|=\frac{\rho}{24}-o(\rho)
> \tag{75.5}
> \]
> with two-well Delaunay neighborhoods in the original saturated minimizer and the
> inner-band conflict deficiency bound
> \[
> |Q|-|N_G(Q)|\le j-1
> \quad\text{for all }Q\subseteq Y_{\rm in}
> \tag{75.6}
> \]
> in the independently constructed scaffold.
>
> It is enough to force one of:
>
> 1. a subset \(Q\subseteq Y_{\rm in}\) with Hall surplus (74.11);
> 2. \(j\) genuine pairwise compatible cavities in \(L\), producing an \(N\)-point
>    strict sub-\(D\) configuration;
> 3. a macroscopic near-equilateral phase whose interface/defect cost exceeds the
>    global \(O(D)\) Delaunay-excess budget;
> 4. a macroscopic near-\(120^\circ\) wedge-chain system whose ordered geometry forces
>    the required scaffold capacity; or
> 5. a mixed two-well interface carrying a positive finite charge per independent
>    obstruction, again exceeding the \(O(D)\) budget.

The natural combinatorial object is the collection of alternating components of the
near-perfect conflict matching from Corollary 74.2. The natural geometric objects are
the matched two-well Gabriel neighborhoods from Theorem 73.2. A closing proof must
build an invariant or capacity certificate that survives the fact that these live in
different coordinate configurations.

### What is explicitly *not* enough

- using the original rattler Voronoi cells directly as scaffold cavities;
- assuming deletion optimality;
- assuming a uniform rattler clearance;
- discarding the near-equilateral well because the exact unit triangle is forbidden;
- counting candidate cavities without proving simultaneous realizability;
- returning to generic one-ray triangle-wall events or raw wall-normal rank.

---

# 76. Authoritative v1.3 Target B frontier

No new Target B rank theorem was obtained in the v1.3 Target A continuation. The
corrected v1.2 component bookkeeping remains authoritative.

Let \(\mathscr S_\alpha\) be the component-rotation row span and

\[
\boxed{
r_\alpha=\dim\mathscr S_\alpha\le c(\Theta)-1.
}
\tag{76.1}
\]

Let \(\overline{\mathcal B}_\xi\) be the induced blocker family after quotienting
\(\mathscr S_\alpha\). Then

\[
\operatorname{rank}\mathcal B
\le
r_\alpha+
\operatorname{rank}\overline{\mathcal B}_\xi.
\tag{76.2}
\]

The exact sufficient residual theorem remains

\[
\boxed{
\operatorname{rank}\overline{\mathcal B}_\xi+I+r
\le
T-q-r_\alpha.
}
\tag{76.3}
\]

The stronger component-count-only sufficient form is

\[
\boxed{
\operatorname{rank}\overline{\mathcal B}_\xi+I+r
\le
T-q-c(\Theta)+1.
}
\tag{76.4}
\]

Either gives

\[
\operatorname{rank}\mathcal B+I+r\le T-q,
\tag{76.5}
\]

contradicting the established lower bound

\[
\boxed{
\operatorname{rank}\mathcal B+I+r\ge T-q+1.
}
\tag{76.6}
\]

The proof must remain componentwise:

1. \(s_C=2\): use both vector-closure equations and the internal turn quotient;
2. cyclic \(s_C=1\): use the exact two-family ordering and Ferrers staircase theorem;
3. one-direction tree components: no scalar cycle obstruction;
4. common component rotations: reserve exactly the cost \(r_\alpha\), neither dropping
   nor double-counting it.

The two-family numerical endpoint remains

\[
0.8944923195\ldots D^2
<
0.9068996821\ldots D^2,
\tag{76.7}
\]

with gap

\[
\boxed{0.0124073626\ldots D^2.}
\tag{76.8}
\]

After the pure inequality, the proof must still pass through nonquadrilateral faces,
holes, multiple components, pinches, and outside vertices with every transfer rank
charged to the exact topology-corrected shell residual. An uncontrolled \(O(D)\) loss
is fatal.

---

# 77. Version 1.3.0 exact status

**LEVEL I STATUS: STILL OPEN.**

Version 1.3.0 makes a substantial Target A advance and leaves Target B unchanged at
its corrected v1.2 frontier.

## Target A — exact finite conflict obstruction

A super-boundary hybrid survivor can now be normalized to a saturated triangle-free
global minimizer with \(\rho=\omega(D)\) genuine strict rattlers. It then forces all
of the following simultaneously:

\[
\boxed{
\begin{array}{c}
\text{a compatible strict sub-}D\text{ scaffold with only }O(D)\text{ missing sites},\\[1mm]
\displaystyle \sum_{p\in A}\delta(p)=O(D),\\[2mm]
\displaystyle \rho/24-o(\rho)\text{ disjoint near-unit strong-Delaunay edges},\\[1mm]
\text{two-well local geometry near }\{1,1,1\}\text{ or }\{1,1,\sqrt3\},\\[1mm]
\text{and an inner-band scaffold conflict graph of deficiency at most }j-1=O(D).
\end{array}
}
\tag{77.1}
\]

The exact contradiction target is now the one-integer Hall surplus

\[
\boxed{
\exists Q\subseteq Y_{\rm in}:
|Q|-|N_G(Q)|\ge j.
}
\tag{77.2}
\]

or an equivalent explicit construction of the \(j\) missing scaffold sites.

The remaining conceptual gap is **configuration transfer**. The original two-well
Delaunay matching and the smaller-optimum scaffold are logically simultaneous but
geometrically independent. No theorem currently transfers the former into actual
cavities of the latter.

## Target B — exact one-integer internal rank gap

The terminal-component decomposition, vector closure, two-direction equality
classification, and stochastic-width component-rotation formula remain trusted. The
component-rotation cost is explicitly

\[
r_\alpha\le c(\Theta)-1,
\]

and the exact unproved internal theorem is (76.3), followed by topology-corrected
transport.

## Unified endgame

A Level I proof now requires one theorem on each side:

1. **Target A:** two-well configuration transfer / inner-band Hall rigidity;
2. **Target B:** internal terminal-component blocker/coforest rank with exact topology
   correction.

Both statements are global finite-capacity theorems. Neither is a missing generic
rigidity count. No infinite family of triangle-free global minimizers is known, so no
disproof is available either.

---

# 78. Current version history and provenance

- **v1.0.0 (2026-08-26):** canonical synthesis and second-pass audit through the
  translated-lattice, phase-atomic, first-order cusp, backward-flip, tangent-quartic,
  support-turning, and hybrid-forest reductions.
- **v1.1.0 (2026-08-26):** minimal-face harmonic--Dirichlet, peripheral-dual,
  terminal direction-network/turn, boundary-velocity, exact plateau, and optimal-flat
  results; rejection of the cycle-lift shortcut; corrected facial peeling.
- **v1.2.0 (2026-08-26):** rooted-forest self-stress, root-skeleton exactification,
  affine factor exclusion, forest rattlerization, saturation, strict replacement and
  collar growth, terminal-component Minkowski splitting, componentwise closure, and
  stochastic-width component-rotation bookkeeping.
- **v1.3.0 (2026-08-26):** unconditional compatible-collar dichotomy, sharp safe-collar
  population, deep Voronoi containment, global clearance budget, degree-six
  near-neighbor matching, strong Gabriel/Delaunay promotion, matched two-well
  structure, exact Hall--Kőnig scaffold conflict theorem, and inner-band near-perfect
  conflict matching. Target A is reduced to two-well configuration transfer / Hall
  rigidity. Target B remains the corrected v1.2 internal blocker/coforest problem.

The only supplied external literature remains:

1. `mp05-2-261-269.pdf`;
2. `1951-03.pdf`;
3. `1-s2.0-S0097316598928898-main.pdf`;
4. `s00454-002-0747-6.pdf`;
5. `1204.4403v1.pdf`;
6. `463.pdf`;
7. `10.1007_PL00009374.pdf`.

No internet source is part of this theorem-state file.

---

# 79. Exact scaffold monomer--dimer structure

This section supersedes the v1.3 claim that configuration transfer is the only
available Target A route.  The original cross-configuration two-well theorem remains
valid, but the conflict scaffold itself has an exact two-well cell structure.

Assume the second branch of Theorem 71.1. Thus

\[
t>1,
\qquad
L=\operatorname{int}(K_m+t\mathbb B),
\qquad
\Omega=L\setminus(K_m+\mathbb B).
\tag{79.1}
\]

Choose a triangular-lattice translate \(\Lambda_v=\Lambda+v\) from the positive-measure
set realizing the strict safe-collar population bound and outside the measure-zero
exceptional set on which a lattice point lies on either parallel-body boundary or a
cross-distance from \(X_m\) equals \(0\) or \(1\). Put

\[
Y=\Lambda_v\cap L,
\qquad
Y_0=Y\cap\Omega,
\qquad
Y_{\rm in}=Y\setminus Y_0.
\tag{79.2}
\]

Then

\[
\boxed{
Y_{\rm in}=\Lambda_v\cap\operatorname{int}(K_m+\mathbb B).
}
\tag{79.3}
\]

Let \(G\) be the bipartite conflict graph on \(X_m\sqcup Y_{\rm in}\), with

\[
x\sim y
\quad\Longleftrightarrow\quad
|x-y|<1.
\tag{79.4}
\]

For \(x\in X_m\), define the full lattice conflict neighborhood and its cell by

\[
N_\Lambda(x)=\{y\in\Lambda_v:|x-y|<1\},
\qquad
C_x=\operatorname{conv}N_\Lambda(x).
\tag{79.5}
\]

Because \(x\in K_m\) and \(t>1\), every \(y\in N_\Lambda(x)\) lies in
\(\operatorname{int}(K_m+\mathbb B)\subset L\). Hence

\[
\boxed{N_G(x)=N_\Lambda(x).}
\tag{79.6}
\]

Thus there is no boundary truncation of any left conflict neighborhood.

## 79.1 Full-neighborhood classification

> **Theorem 79.1 (exact triangular-lattice blocker classification).**
> For every \(x\in X_m\),
> \[
> \boxed{|N_G(x)|\in\{3,4\}.}
> \tag{79.7}
> \]
> If \(|N_G(x)|=3\), then \(C_x\) is an elementary unit equilateral triangle.
> If \(|N_G(x)|=4\), then \(C_x\) is a unit lozenge.

### Proof

Write

\[
\Lambda=\mathbb Ze_1+\mathbb Ze_2,
\qquad
|e_1|=|e_2|=1,
\qquad
e_1\cdot e_2=\frac12.
\tag{79.8}
\]

For a lattice vector \(ae_1+be_2\),

\[
Q(a,b)=|ae_1+be_2|^2=a^2+ab+b^2.
\tag{79.9}
\]

If \(y,y'\in N_\Lambda(x)\), then

\[
|y-y'|
<|y-x|+|x-y'|<2.
\tag{79.10}
\]

Thus every nonzero difference inside one conflict neighborhood has squared norm
\(1\) or \(3\). Two lattice sites in the same class modulo \(2\Lambda\) have
squared distance at least \(4\). There are four parity classes, so

\[
|N_\Lambda(x)|\le4.
\tag{79.11}
\]

Every point of the plane belongs to a closed elementary unit lattice triangle. Its
three vertices are all at distance at most one. Genericity excludes equality and
lattice coincidence for every \(x\in X_m\), so those three distances are strictly
below one. Hence

\[
|N_\Lambda(x)|\ge3.
\tag{79.12}
\]

The possible side-square multisets for three triangular-lattice points with all
pairwise distances below two are

\[
\{1,1,1\},
\qquad
\{1,1,3\},
\qquad
\{3,3,3\}.
\tag{79.13}
\]

The last is an equilateral triangle of side \(\sqrt3\), whose minimum enclosing
radius is one, so it cannot lie in an open unit disk.

A \(\{1,1,3\}\) triple consists of three vertices of a unit lozenge. Write the
lozenge as

\[
0,u,v,u+v,
\qquad
|u|=|v|=1,
\qquad
u\cdot v=\frac12.
\tag{79.14}
\]

If \(p\) is within unit distance of \(0,u,u+v\), then

\[
|p-v|^2+|p-u|^2
=|p|^2+|p-u-v|^2-1<1.
\tag{79.15}
\]

Thus \(|p-v|<1\), so the fourth lozenge vertex is also a conflict. Therefore a
**complete** degree-three neighborhood cannot have type \(\{1,1,3\}\), and must be
an elementary unit triangle.

A finite check of four-cliques in the distance-\(<2\) triangular-lattice graph gives
only two types: the four vertices of a unit lozenge, or one lattice point together
with three alternating unit neighbors. In the second type the latter three vertices
form an equilateral triangle of side \(\sqrt3\), again with minimum enclosing radius
one. Hence the second type cannot fit in an open unit disk. Every degree-four
neighborhood is therefore a unit lozenge. \(\square\)

## 79.2 Interior location and cell disjointness

> **Theorem 79.2 (exact monomer--dimer packing).**
> For every \(x\in X_m\),
> \[
> \boxed{x\in\operatorname{int}C_x.}
> \tag{79.16}
> \]
> If \(x\ne x'\), then
> \[
> \boxed{
> \operatorname{int}C_x\cap\operatorname{int}C_{x'}=\varnothing.
> }
> \tag{79.17}
> \]
> Consequently the cells \(C_x\) form an exact monomer--dimer packing on the
> honeycomb dual of the elementary triangular tiling: a degree-three blocker occupies
> one elementary triangle and a degree-four blocker occupies two adjacent elementary
> triangles.

### Proof

Take a boundary edge of \(C_x\). On the cell side lies an elementary lattice triangle
whose third vertex \(w\) belongs to \(N_\Lambda(x)\). Let \(w'\) be the reflected
lattice vertex across that boundary edge. If \(x\) lay on or beyond the edge, then

\[
|x-w'|\le|x-w|<1,
\tag{79.18}
\]

contradicting the completeness of the neighborhood classification. Hence
\(x\in\operatorname{int}C_x\).

Each cell is the union of one or two elementary lattice triangles. If two cell
interiors overlapped, they would share an elementary triangle \(\Delta\). The two
associated points of \(X_m\) would both lie in the intersection of the three open
unit disks centered at the vertices of \(\Delta\), the interior of the unit Reuleaux
triangle. That set has diameter one, and two of its interior points have distance
strictly below one. This contradicts the unit separation of \(X_m\). \(\square\)

## 79.3 Radial planarity and right degree

Join every \(x\in X_m\) by straight segments to the vertices of \(C_x\). Since each
radial edge stays in its own convex cell and cell interiors are disjoint, distinct
radial edges do not cross. Genericity excludes coincident cross-vertices and radial
edge degeneracies.

> **Corollary 79.3.** The radial drawing is a simple plane drawing of \(G\).
> Every lattice-side vertex has degree at most five.

For the degree bound, if six points of \(X_m\) lay in the open unit disk centered at
a lattice vertex, two consecutive polar angles would differ by at most \(\pi/3\).
For radii \(r,s<1\),

\[
|p-q|^2\le r^2+s^2-rs<1,
\tag{79.19}
\]

contradicting unit separation.

The two exact scaffold cell motifs already contain both equality wells from the v1.3
Delaunay analysis. A monomer has side multiset \(\{1,1,1\}\). A three-vertex subset
of a lozenge has side multiset \(\{1,1,1\}\) or \(\{1,1,\sqrt3\}\). This is a
new co-embedded occurrence of the wells; it is not a transport of the original
saturated minimizer's Delaunay faces.

---

# 80. Exact Hall charge, leafless reduction, and face-shell identities

Let \(m_3,m_4\) be the numbers of monomer and dimer cells. Then

\[
m_3+m_4=m.
\tag{80.1}
\]

Let

- \(\gamma\) be the number of connected components of the full radial graph \(G\),
  including isolated lattice-side vertices;
- \(s\) be the number of unit lattice edges shared by two distinct cells;
- \(g\) be the number of bounded complementary gap components of the cell union; and
- \(\delta=|Y_{\rm in}|-m\).

## 80.1 Full-complex Euler identity

> **Theorem 80.1.**
> \[
> \boxed{\mu(G)=s+g}
> \tag{80.2}
> \]
> and
> \[
> \boxed{
> \delta=m_3+2m_4+\gamma-s-g.
> }
> \tag{80.3}
> \]

### Proof

Add all cell-boundary lattice edges to the radial graph. Within each monomer or dimer
this produces the fan decomposition from its interior point. Deleting the cell
boundary edges has two topological effects. A boundary edge shared by two cells
produces one quadrilateral radial face, and each bounded complementary gap component
produces one radial face after its adjacent fan triangles are merged into the gap.
Thus the bounded faces of the plane graph are in bijection with the \(s\) shared
edges and the \(g\) bounded gaps. For a plane graph with \(\gamma\) components the
number of bounded faces equals its cyclomatic number, proving (80.2).

Also

\[
|E(G)|=3m_3+4m_4,
\qquad
|V(G)|=m+|Y_{\rm in}|=2m+\delta.
\tag{80.4}
\]

Hence

\[
\mu(G)=|E|-|V|+\gamma
=m_3+2m_4-\delta+\gamma.
\tag{80.5}
\]

Combine with (80.2). \(\square\)

The canonical survivor Hall inequality applied to \(Q=Y_{\rm in}\) gives

\[
\delta\le j-1.
\tag{80.6}
\]

Therefore

\[
\boxed{
 s+g\ge m_3+2m_4+\gamma-j+1.
}
\tag{80.7}
\]

Using the v1.3 collar bound

\[
j<C_{\rm col}D-\frac{2\pi}{\sqrt3},
\qquad
C_{\rm col}=\pi\left(\frac12+\frac2{\sqrt3}\right),
\tag{80.8}
\]

we obtain the strict quantitative form

\[
\boxed{
 s+g>
 m_3+2m_4+\gamma-C_{\rm col}D+\frac{2\pi}{\sqrt3}+1.
}
\tag{80.9}
\]

Thus all but \(O(D)\) of the elementary-triangle cell mass must be canceled by
shared-edge or bounded-gap faces in every surviving super-boundary scaffold.

## 80.2 Arbitrary Hall sets and the leafless formula

For \(Q\subseteq Y_{\rm in}\), let

\[
H_Q=G[Q\sqcup N(Q)].
\tag{80.10}
\]

Write \(\gamma_Q\) and \(\mu_Q\) for its component and cyclomatic numbers, and let
\(b_d(Q)\) count left vertices of degree \(d\) in \(H_Q\).

> **Theorem 80.2 (exact Hall charge).** For every \(Q\subseteq Y_{\rm in}\),
> \[
> \boxed{
> |Q|-|N(Q)|
> =\gamma_Q-\mu_Q-b_1(Q)+b_3(Q)+2b_4(Q).
> }
> \tag{80.11}
> \]

### Proof

Since

\[
\mu_Q=|E(H_Q)|-|Q|-|N(Q)|+\gamma_Q
\tag{80.12}
\]

and

\[
|E(H_Q)|=\sum_{x\in N(Q)}\deg_{H_Q}(x),
\tag{80.13}
\]

we have

\[
|Q|-|N(Q)|
=\gamma_Q-\mu_Q
+\sum_{x\in N(Q)}(\deg_{H_Q}(x)-2).
\tag{80.14}
\]

Every left degree is between one and four, giving (80.11). \(\square\)

Define the Hall deficiency

\[
h(G)=\max_{Q\subseteq Y_{\rm in}}\bigl(|Q|-|N(Q)|\bigr).
\tag{80.15}
\]

> **Theorem 80.3 (leafless maximizing Hall set).** A maximizing \(Q\) can be chosen
> with \(b_1(Q)=0\). Consequently
> \[
> \boxed{
> h(G)=
> \max_{\substack{Q\subseteq Y_{\rm in}\\ b_1(Q)=0}}
> \bigl(\gamma_Q-\mu_Q+b_3(Q)+2b_4(Q)\bigr).
> }
> \tag{80.16}
> \]

### Proof

Choose a maximum-deficiency \(Q\) of minimum cardinality. Suppose a left vertex has
degree one in \(H_Q\), with unique neighbor \(y\in Q\). Let \(r\ge1\) be the number
of left vertices whose only \(Q\)-neighbor is \(y\). Then

\[
(|Q|-1)-(|N(Q)|-r)
=(|Q|-|N(Q)|)+(r-1).
\tag{80.17}
\]

Deleting \(y\) therefore does not reduce deficiency. It cannot increase deficiency
past the global maximum, so it gives a smaller maximizing set, contradiction.
\(\square\)

The positive local Hall charges in (80.11) and (80.16) are exactly the scaffold's two
crystalline wells. The negative term is cycle rank. Target A has therefore become an
exact branch-versus-cycle problem in one common geometry.

## 80.3 Exact face-shell refinement

Let \(b_\infty\) be the length, with multiplicity, of the unbounded **radial-graph**
facial boundary walk. Thus \(b_\infty/2\) is the number, with multiplicity, of
exposed lattice cell edges on the unbounded side. For the bounded gaps, let \(b_i\)
be the number of lattice cell-edge incidences on the boundary of gap \(i\), and put

\[
\eta=\sum_i(b_i-3)\ge0.
\tag{80.18}
\]

> **Theorem 80.4 (face-shell identities).**
> \[
> \boxed{
> g=m_3+2\delta-2\gamma-\eta-\frac{b_\infty}{2},
> }
> \tag{80.19}
> \]
> \[
> \boxed{
> s=2m_4-3\delta+3\gamma+\eta+\frac{b_\infty}{2}.
> }
> \tag{80.20}
> \]
> In particular,
> \[
> \boxed{
> s\ge2m_4-3j+3+3\gamma.
> }
> \tag{80.21}
> \]

### Proof

The total number of cell-boundary edge incidences is

\[
3m_3+4m_4.
\tag{80.22}
\]

Every shared edge consumes two incidences. The remaining exposed lattice cell edges
lie either on a bounded gap or on the unbounded side. Hence

\[
3m_3+4m_4-2s
=3g+\eta+\frac{b_\infty}{2}.
\tag{80.23}
\]

Combine (80.23) with (80.3) and solve for \(g\) and \(s\), obtaining (80.19) and
(80.20). Finally use \(\delta\le j-1\) and the nonnegativity of \(\eta\) and
\(b_\infty\). \(\square\)

Equation (80.21) is the exact dimer endpoint: if \(m_4\gg j\), nearly the maximum
possible dimer-side mass must be absorbed into shared-edge quadrilateral faces.
Equation (80.19) is the monomer endpoint: absent large outer boundary or
nontriangular gap excess, there is nearly one elementary triangular gap per monomer.

---

# 81. Authoritative v1.4 Target A frontier

The v1.3 configuration-transfer obstruction remains logically correct but is no
longer the unique Target A route. The new scaffold-internal theorem removes the need
to transport the original minimizer's Delaunay neighborhoods if one can control cycle
cancellation directly.

Recall

\[
N=m+\rho=m+k+j,
\qquad
1\le j=\rho-k
<C_{\rm col}D-\frac{2\pi}{\sqrt3}.
\tag{81.1}
\]

By Kőnig's theorem, the maximum independent set in the conflict graph on
\(X_m\sqcup Y_{\rm in}\) has size

\[
m+h(G).
\tag{81.2}
\]

Every point of \(Y_0\) can be added because \(Y_0\) has no conflicts with \(X_m\),
and lattice sites are mutually unit-separated. Thus the maximum compatible subset of
\(X_m\cup Y\) has size

\[
m+k+h(G).
\tag{81.3}
\]

Since \(N=m+k+j\), Target A closes exactly when

\[
\boxed{h(G)\ge j.}
\tag{81.4}
\]

Using Theorem 80.3, the exact remaining statement is:

> **Target A v1.4 (monomer--dimer cycle-cut rigidity).**
> For every scaffold arising from a super-boundary triangle-free global minimizer,
> prove
> \[
> \boxed{
> \max_{\substack{Q\subseteq Y_{\rm in}\\b_1(Q)=0}}
> \bigl(\gamma_Q-\mu_Q+b_3(Q)+2b_4(Q)\bigr)
> \ge j.
> }
> \tag{81.5}
> \]

If (81.5) holds, \(X_m\cup Y\) contains \(N\) mutually unit-separated points in the
open body \(L\), while

\[
\operatorname{diam}(L)<D,
\tag{81.6}
\]

contradicting \(D=D(N)\).

A hypothetical survivor must therefore arrange **every** leafless Hall set so that

\[
\mu_Q
\ge
\gamma_Q+b_3(Q)+2b_4(Q)-j+1.
\tag{81.7}
\]

This is the exact cycle-cancellation obstruction.

## 81.1 Local zero-charge regressions

Planarity and motif counting alone cannot prove (81.5). There are exact local
crystalline cancellation models:

1. a generic triangular-lattice shift to centers of one orientation of elementary
   triangles yields a monomer phase in which positive branch charge is canceled by
   elementary triangular gap faces;
2. another generic shift yields a lozenge/dimer phase in which positive branch charge
   is canceled by a quadrangulation of shared-edge faces.

These are not known large global diameter extremizers, but their local conflict
combinatorics survive boundary perturbation. Any proof of (81.5) must therefore use
the global-optimality origin of \(X_m\), the collar parameter \(j\), or a genuinely
global planar-dual invariant.

## 81.2 Next viable route

A viable next program is the Dulmage--Mendelsohn decomposition of a
maximum-deficiency minimum-cardinality Hall set, coupled to the planar dual of the
monomer--dimer complex.

In a dimer-rich domain, (80.20)--(80.21) force near-maximal shared-edge cancellation.
A new **type-resolved dual-strip theorem** would be needed to cut such a domain into
ordered lozenge strips after paying only the exact Hall defect. Only after proving
that bridge may one invoke the already-audited two-family Ferrers/Cartesian endpoint

\[
0.8944923195\ldots D^2
<
0.9068996821\ldots D^2.
\tag{81.8}
\]

In a monomer-rich domain, (80.19) forces almost every bounded face to be an elementary
triangular gap unless outer-boundary or nontriangular-gap excess is large. The needed
new theorem is an exact phase-rigidity/dual-cut statement: a Hall-saturating monomer
phase must either create an augmenting dual cut, force a globally coherent
translated-lattice extremizer, or produce a certified diameter-decreasing
deformation.

Mixed domains must be measured by **absolute** dual-contour/interface charge. Signed
global Euler charge can cancel and is not enough.

The following are research routes, not canonical consequences:

- automatic contraction to a width-one annulus;
- an exact gammoid representation after plateau terminalization;
- automatic import of the Target B Ferrers theorem into scaffold lozenge strips; or
- a Schürmann deformation from a monomer phase without a proved global hypothesis.

The old v1.3 cross-configuration two-well transfer theorem remains an alternate
closure route, but the scaffold-internal cycle-cut theorem (81.5) is now the preferred
Target A endpoint.

---

# 82. Strict stochasticity and atomic terminal components

Return to the pure simply connected strict-rhombic Target B survivor and the terminal
component decomposition of Sections 65--67. Let

\[
c=c(\Theta).
\tag{82.1}
\]

For an active diameter bar \(h\), recall

\[
r_h=De_h,
\qquad
r_h=\sum_Cr_{h,C},
\tag{82.2}
\]

and

\[
a_{hC}
=\frac{w_{K_C}(e_h)}D,
\qquad
\sum_Ca_{hC}=1.
\tag{82.3}
\]

## 82.1 Strict positivity of every component width

> **Theorem 82.1 (strict stochasticity).** For every active diameter bar \(h\) and
> every terminal component \(C\),
> \[
> \boxed{a_{hC}>0.}
> \tag{82.4}
> \]

### Proof

An active diameter direction has a unique support maximizer and a unique support
minimizer in \(K\). Under the Minkowski decomposition

\[
K=\sum_CK_C,
\tag{82.5}
\]

the support face in any direction is the Minkowski sum of the corresponding support
faces of the summands. A singleton support face of \(K\) therefore forces every
summand support face in that direction to be a singleton; the same holds in the
opposite direction.

Every terminal component contains a train edge and hence contributes a nonzero hull
edge vector, so \(K_C\) is not a singleton. If
\(w_{K_C}(e_h)=0\), all points of \(K_C\) have the same \(e_h\)-coordinate and the
support face in direction \(e_h\) is the whole nontrivial summand \(K_C\),
contradicting singleton support. Thus the width is strictly positive. \(\square\)

Hence the stochastic vectors

\[
a_h=(a_{hC})_C
\tag{82.6}
\]

have **full support**, not merely nonnegative support.

## 82.2 Atomicity of the s_C=0 class

> **Theorem 82.2 (atomic one-direction component).** If \(s_C=0\), then \(C\) has
> exactly two terminal vertices and one train edge \(\tau\). Its Minkowski summand is
> a unit segment parallel to \(u_\tau\). For every active diameter bar \(h\),
> \[
> \boxed{
> d_{h\tau}\ne0,
> \qquad
> \lambda_{h\tau}=d_{h\tau}\,r_h\cdot u_\tau
> =D|e_h\cdot u_\tau|>0.
> }
> \tag{82.7}
> \]
> In particular, an \(s_C=0\) component can never be the origin component of a
> strict-backward blocker row.

### Proof

By Theorem 66.2, \(C\) is a tree and all its trains have one oriented unit direction
\(u\). For \(j\in J_C\), the vector
\(e_j=z_{j+1}-z_j\) is a nonzero side between consecutive extreme hull vertices.
The incidence formula therefore gives

\[
e_j=k_ju,
\qquad
k_j\in\mathbb Z\setminus\{0\}.
\tag{82.8}
\]

The sides \(e_j\) occur in cyclic convex order. Since the \(z_j\) are extreme
hull vertices, collinear boundary subdivisions have already been removed; a convex
hull has at most one side in the oriented direction \(u\) and at most one in the
opposite direction \(-u\). Component closure gives
\(\sum_{j\in J_C}e_j=0\), so both orientations occur and \(|J_C|=2\). Since
\(C\) is a connected tree on two vertices, it has one train edge. Its incidence
relation gives the two summand edge vectors \(u\) and \(-u\), so \(K_C\) is a unit
segment.

By Theorem 82.1 the width of this segment in every active diameter direction is
positive, so \(e_h\cdot u\ne0\). Its support chord is

\[
r_{h,C}=\operatorname{sgn}(e_h\cdot u)u.
\tag{82.9}
\]

The train decomposition of the diameter chord gives the same vector as
\(d_{h\tau}u\); hence \(d_{h\tau}=\pm1\) with the displayed sign and
\(\lambda_{h\tau}=D|e_h\cdot u|>0\). \(\square\)

Thus every strict-backward origin lies in a component with

\[
\boxed{s_C>0.}
\tag{82.10}
\]

This statement must not be strengthened to "cyclic" without a new theorem.

## 82.3 Atomic component collapses the nonzero minimal-face potential space

> **Corollary 82.3.** Suppose an \(s_C=0\) component is present and the
> minimal-face equality kernel \(K\) is nonzero. Then the selected active-bar
> potentials all coincide. In the notation of the harmonic--Dirichlet reduction,
> the terminal-potential count is therefore
> \[
> \boxed{r=1.}
> \tag{82.11}
> \]

### Proof

Let \(\tau\) be the unique train of the atomic component. By Theorem 82.2,
for every active diameter bar \(h\),
\(d_{h\tau}=\pm1\) and \(\lambda_{h\tau}>0\). Hence \(\tau\) is
visible to every bar selected in the minimal-face equality system. On that face the
equality relation is \(x_\tau=s_h\) for every selected \(h\). Thus all
selected bar potentials \(s_h\) take the same value on the nonzero equality
kernel. The terminal-potential factorization from the harmonic--Dirichlet theorem
therefore has a single potential class, so \(r=1\). \(\square\)

This corollary is only asserted in the nonzero minimal-face-kernel branch; it is not a
replacement for the separate \(K=0\) convention.

---

# 83. Component-rotation variance and strict-backward origin rank

For every active diameter bar \(h\) and component \(C\), decompose its support chord
in the orthonormal frame \((e_h,Je_h)\):

\[
\boxed{
 r_{h,C}=D(a_{hC}e_h+b_{hC}Je_h).
}
\tag{83.1}
\]

Since \(r_h=De_h=\sum_Cr_{h,C}\),

\[
\boxed{
\sum_Ca_{hC}=1,
\qquad
\sum_Cb_{hC}=0,
\qquad
a_{hC}>0.
}
\tag{83.2}
\]

Give every train in component \(C\) a common angular motion \(t\alpha_C\). The exact
train-coordinate realization theorem permits independent unit train-vector rotations,
so all rhombic unit contacts remain exact. Put

\[
r_h(t)=\sum_CR_{t\alpha_C}r_{h,C},
\qquad
f_h(t)=\frac12|r_h(t)|^2.
\tag{83.3}
\]

## 83.1 Exact second variation

> **Theorem 83.1 (component-rotation variance formula).**
> \[
> \boxed{
> f_h'(0)=-D^2\sum_Cb_{hC}\alpha_C.
> }
> \tag{83.4}
> \]
> If \(f_h'(0)=0\), then
> \[
> \boxed{
> f_h''(0)
> =-D^2\left[
> \sum_Ca_{hC}\alpha_C^2
> -\left(\sum_Ca_{hC}\alpha_C\right)^2
> \right].
> }
> \tag{83.5}
> \]
> Because every \(a_{hC}>0\), equality in (83.5) holds if and only if all
> \(\alpha_C\) are equal.

### Proof

Differentiate (83.3):

\[
r_h'(0)=\sum_C\alpha_CJr_{h,C}
=D\left[-\sum_Cb_{hC}\alpha_C\,e_h
+\sum_Ca_{hC}\alpha_C\,Je_h\right].
\tag{83.6}
\]

Since \(r_h(0)=De_h\), this gives (83.4). Also

\[
r_h''(0)=-\sum_C\alpha_C^2r_{h,C}.
\tag{83.7}
\]

If (83.4) vanishes, then

\[
|r_h'(0)|^2
=D^2\left(\sum_Ca_{hC}\alpha_C\right)^2,
\tag{83.8}
\]

while

\[
r_h(0)\cdot r_h''(0)
=-D^2\sum_Ca_{hC}\alpha_C^2.
\tag{83.9}
\]

Use \(f_h''=|r_h'|^2+r_h\cdot r_h''\). The bracket in (83.5) is the variance of
\(\alpha\) under the full-support probability weights \(a_{hC}\), so it vanishes
only on common rotation. \(\square\)

## 83.2 Positive spanning of the component-rotation quotient

Let

\[
V_\alpha=\mathbb R^c/\langle\mathbf1\rangle
\tag{83.10}
\]

and define the active first-derivative covector

\[
L_h(\alpha)=-\sum_Cb_{hC}\alpha_C.
\tag{83.11}
\]

> **Theorem 83.2 (positive spanning).** The active covectors \(L_h\) positively span
> \(V_\alpha^*\). Equivalently,
> \[
> \boxed{
> \{[\alpha]\in V_\alpha:L_h(\alpha)\le0\text{ for every active }h\}
> =\{0\}.
> }
> \tag{83.12}
> \]
> Consequently their linear rank is exactly
> \[
> \boxed{c-1,}
> \tag{83.13}
> \]
> and if \(c\ge2\), at least \(c\) nonzero active restrictions are required for
> positive spanning.

### Proof

Suppose \([\alpha]\ne0\) and \(L_h(\alpha)\le0\) for every active \(h\). If the
inequality is strict, (83.4) decreases that active squared diameter to first order for
small positive \(t\). If equality holds, (83.5) is strictly negative because
\([\alpha]\ne0\) and every weight is positive. Thus every active diameter becomes
strictly shorter for small positive \(t\).

The exact component-rotation path preserves all unit rhombic contacts. The realization
is strict, so every inactive lower-distance, upper-diameter, and rhombus-angle
inequality retains its slack for sufficiently small \(t\). Hence the whole
configuration has diameter strictly below \(D\), contradicting local, and therefore
global, diameter minimality. This proves (83.12).

The polar-cone theorem now says that the positive cone generated by the \(L_h\) is all
of \(V_\alpha^*\). Its span therefore has dimension \(c-1\). A positive spanning set
of a vector space of dimension \(c-1\ge1\) requires at least \(c\) nonzero vectors.
\(\square\)

This is stronger than the v1.2 upper bound on component-rotation blocker rank: the
**active diameter derivatives** themselves are globally full rank on the quotient.
It does not, however, identify the internal \(\xi\)-blocker rank.

## 83.3 Rank consumed by distinct strict-backward origins

A strict-backward blocker row belonging to a train in component \(C\), supported by
active bar \(h\), restricts to common component rotations as

\[
\boxed{
 v_{h,C}=e_C^*-a_h,
 \qquad
 a_h=(a_{hC'})_{C'},
 \qquad
 a_{hC'}>0,
 \qquad
 \sum_{C'}a_{hC'}=1.
}
\tag{83.14}
\]

Call \(C\) a **strict-backward origin component** if at least one such row originates
in \(C\). Let \(\mathcal O\) be the set of distinct origins and

\[
k_{\rm org}=|\mathcal O|.
\tag{83.15}
\]

> **Theorem 83.3 (full-support origin independence).** Choose one strict-backward row
> from each of \(k\) distinct origin components.
>
> - If \(k<c\), the selected component-rotation rows are linearly independent.
> - If \(k=c\), their rank is exactly \(c-1\).
>
> Therefore
> \[
> \boxed{
> r_\alpha\ge\min\{k_{\rm org},c-1\},
> }
> \tag{83.16}
> \]
> \[
> \boxed{k_{\rm org}\le r_\alpha+1,}
> \tag{83.17}
> \]
> and if \(r_\alpha<c-1\), then
> \[
> \boxed{k_{\rm org}\le r_\alpha.}
> \tag{83.18}
> \]

### Proof

Suppose rows from distinct origins \(C_i\) satisfy

\[
\sum_{i=1}^kc_i(e_{C_i}^*-a_i)=0.
\tag{83.19}
\]

Then

\[
\sum_ic_ie_{C_i}^*=\sum_ic_ia_i.
\tag{83.20}
\]

The \(\ell^1\)-norm of the left side is \(\sum_i|c_i|\), while

\[
\left\|\sum_ic_ia_i\right\|_1
\le\sum_i|c_i|\|a_i\|_1
=\sum_i|c_i|.
\tag{83.21}
\]

Equality must hold. Since every coordinate of every \(a_i\) is strictly positive,
equality in the coordinatewise triangle inequality forces all nonzero \(c_i\) to
have the same sign.

If \(k<c\), take a component coordinate not among the selected origins. The left side
of (83.20) is zero in that coordinate, whereas the right side is a same-sign sum of
strictly positive numbers unless every \(c_i=0\). Thus the rows are independent.

If \(k=c\), every proper subset is independent by the first case, while all rows
annihilate common rotation, so their rank is at most \(c-1\). Hence it is exactly
\(c-1\). Equations (83.16)--(83.18) follow. \(\square\)

Combining with Theorem 82.2 gives

\[
\boxed{
\mathcal O\subseteq\{C:s_C>0\}.
}
\tag{83.22}
\]

No stronger inclusion is currently audited.

## 83.4 The s_C=1 tree correction

The statement

\[
\mathcal O\subseteq
\{\text{cyclic }s_C=1\text{ components}\}\cup\{s_C=2\text{ components}\}
\tag{83.23}
\]

is **not proved** and must not be used. Theorem 66.2 classifies cyclic \(s_C=1\)
components but does not exclude \(s_C=1\) trees.

An abstract consistent local model is a three-vertex path using two train directions
\(u,v\) whose inherited convex-summand edge vectors are

\[
-u,
\qquad
u-v,
\qquad
v,
\tag{83.24}
\]

which close to zero and can form a triangular Minkowski summand. Thus a tree can have
\(s_C=1\). Any Target B coforest theorem must include this case explicitly rather
than assigning every strict-backward origin to a cyclic or two-dimensional component.

---

# 84. Authoritative v1.4 Target B frontier

The established lower-rank theorem remains

\[
\boxed{
\operatorname{rank}\mathcal B+I+r\ge T-q+1.
}
\tag{84.1}
\]

The total desired pure upper bound remains

\[
\boxed{
\operatorname{rank}\mathcal B+I+r\le T-q.
}
\tag{84.2}
\]

Let \(\mathscr S_\alpha\) be the component-rotation restriction row span and

\[
r_\alpha=\dim\mathscr S_\alpha\le c(\Theta)-1.
\tag{84.3}
\]

After quotienting it, let \(\overline{\mathcal B}_\xi\) be the internal relative-angle
row family. Then

\[
\operatorname{rank}\mathcal B
\le
r_\alpha+
\operatorname{rank}\overline{\mathcal B}_\xi.
\tag{84.4}
\]

The exact residual theorem is still

> **Target B v1.4 (internal coforest with origin budget).** Prove
> \[
> \boxed{
> \operatorname{rank}\overline{\mathcal B}_\xi+I+r
> \le T-q-r_\alpha.
> }
> \tag{84.5}
> \]

The stronger component-count-only sufficient form remains

\[
\boxed{
\operatorname{rank}\overline{\mathcal B}_\xi+I+r
\le T-q-c(\Theta)+1.
}
\tag{84.6}
\]

The new information is that strict-backward origins themselves consume the reserved
rotation rank:

\[
\boxed{
 r_\alpha\ge\min\{k_{\rm org},c(\Theta)-1\}.
}
\tag{84.7}
\]

Hence blocker origins cannot be distributed freely over many terminal components.
If the rotation span is not already full, each distinct origin costs a full independent
unit of \(r_\alpha\). If an \(s_C=0\) component is present, then it is not an
origin, so \(\mathcal O\) is a proper subset of the \(c(\Theta)\) components.
The proper-origin case of Theorem 83.3 then gives the sharper bound

\[
\boxed{k_{\rm org}\le r_\alpha.}
\tag{84.8}
\]

In the nonzero minimal-face-kernel branch the same atomic component also forces
\(r=1\) by Corollary 82.3.

A closing proof should split the component geometry into at least the following four
classes:

1. \(s_C=0\): atomic one-edge segment components; never strict-backward origins;
2. \(s_C=1\) trees: a genuine residual class that must be controlled directly;
3. cyclic \(s_C=1\): exact two-direction ordered/Ferrers components;
4. \(s_C=2\): genuine two-dimensional turning components paying both vector-closure
   directions.

The common component rotations must be paid exactly once through \(r_\alpha\).
The origin concentration theorem may be used to force internal blocker mass into a
small number of non-atomic components, but it does not itself prove the internal
coforest inequality.

The audited two-family numerical endpoint remains

\[
0.8944923195\ldots D^2
<
0.9068996821\ldots D^2,
\tag{84.9}
\]

with gap

\[
\boxed{0.0124073626\ldots D^2.}
\tag{84.10}
\]

After the pure inequality, all nonquadrilateral faces, holes, multiple components,
pinches, and outside vertices must still be transported through the exact
topology-corrected shell residual. An uncontrolled \(O(D)\) rank loss remains fatal.

---

# 85. v1.4 regression additions and rejected inferences

All regressions from Section 47 and the v1.3 continuation remain binding. Add the
following v1.4 tests.

1. **Shifted-lattice monomer phase.** One orientation of elementary triangle-center
   blockers can realize local zero Hall charge through triangular gap faces.
2. **Shifted-lattice lozenge phase.** Dimer cells can realize local zero Hall charge
   through shared-edge quadrilateral faces.
3. **Mixed monomer--dimer interfaces.** Signed Euler charge can cancel across
   interfaces; a proof must control absolute interface/dual-contour charge if it
   relies on interfaces.
4. **s_C=1 tree.** A two-direction terminal tree is not excluded by the canonical
   component theorem and cannot be treated as cyclic Ferrers geometry.
5. **Atomic s_C=0 component.** A one-edge segment component is strictly forward for
   every active bar and supplies no strict-backward origin; any theorem demanding a
   backward origin from every component is false.

The following inferences are explicitly rejected unless separately proved:

- planarity of the scaffold conflict graph implies the Hall surplus;
- the full-complex Euler identity alone implies the Hall surplus;
- every positive Hall cell charge survives after cycle cancellation;
- every dimer-rich scaffold automatically contains a Target B Ferrers block;
- every monomer-rich scaffold automatically admits a Schürmann diameter decrease;
- the monomer--dimer complex automatically contracts to a width-one annulus;
- the Hall problem is automatically a gammoid without an explicit directed linkage
  construction and exact rank equivalence;
- every strict-backward origin is cyclic;
- every \(s_C=1\) component is cyclic; or
- positive spanning of component rotations proves the internal \(\xi\)-rank bound.

---

# 86. Version 1.4.0 exact status

**LEVEL I STATUS: STILL OPEN.**

Version 1.4.0 makes genuine structural advances on both surviving branches but does
not close either one.

## Target A -- exact planar cycle-cancellation gap

The independent compatible scaffold is now itself an exact planar monomer--dimer Hall
complex. Every blocker occupies one elementary triangle or one unit lozenge, cell
interiors are disjoint, and the exact Hall deficiency is

\[
\boxed{
 h(G)=
 \max_{\substack{Q\subseteq Y_{\rm in}\\b_1(Q)=0}}
 \bigl(\gamma_Q-\mu_Q+b_3(Q)+2b_4(Q)\bigr).
}
\tag{86.1}
\]

The contradiction threshold is the one integer

\[
\boxed{h(G)\ge j,}
\tag{86.2}
\]

while every survivor has

\[
\boxed{h(G)\le j-1.}
\tag{86.3}
\]

Thus the preferred new Target A problem is exact cycle-cut rigidity. The v1.3
cross-configuration two-well transfer problem remains an alternate route but is no
longer necessary if (86.2) can be proved scaffold-internally.

## Target B -- strict rotation rigidity and concentrated origins

Every terminal component has strictly positive width in every active diameter
direction. The \(s_C=0\) class is atomic and never a backward origin; when the
minimal-face equality kernel is nonzero, its presence also forces \(r=1\). Common
component rotations have a strict weighted-variance second variation modulo global
rotation, forcing active derivative covectors to positively span the full
\(c(\Theta)-1\)-dimensional quotient. Distinct strict-backward origins consume
component-rotation rank according to

\[
\boxed{
 r_\alpha\ge\min\{k_{\rm org},c(\Theta)-1\}.
}
\tag{86.4}
\]

The remaining pure theorem is still

\[
\boxed{
\operatorname{rank}\overline{\mathcal B}_\xi+I+r
\le T-q-r_\alpha,
}
\tag{86.5}
\]

now with the residual blocker origins forced into \(s_C>0\) components and with
\(s_C=1\) trees explicitly retained. Exact topology-corrected transport still follows
that pure theorem.

## Unified endgame

A Level I proof requires both survivor branches to be eliminated:

1. **Target A:** prove monomer--dimer cycle-cut rigidity (86.2), or close an
   equivalent scaffold-capacity route;
2. **Target B:** prove the internal relative-angle coforest inequality (86.5) with the
   origin budget and then transport it with exact topology correction.

Disproving one proposed Target A or Target B lemma is not a disproof of Erdős #99.
A Level I disproof requires an infinite sequence of triangle-free **global**
minimizers with exact optimal diameter.

No such infinite family is known.

---

# 87. Current version history and provenance through v1.4.0

- **v1.0.0 (2026-08-26):** canonical synthesis and second-pass audit through the
  translated-lattice, phase-atomic, first-order cusp, backward-flip, tangent-quartic,
  support-turning, and hybrid-forest reductions.
- **v1.1.0 (2026-08-26):** minimal-face harmonic--Dirichlet, peripheral-dual,
  terminal direction-network/turn, boundary-velocity, exact plateau, and optimal-flat
  results; rejection of the cycle-lift shortcut; corrected facial peeling.
- **v1.2.0 (2026-08-26):** rooted-forest self-stress, root-skeleton exactification,
  affine factor exclusion, forest rattlerization, saturation, strict replacement and
  collar growth, terminal-component Minkowski splitting, componentwise closure, and
  stochastic-width component-rotation bookkeeping.
- **v1.3.0 (2026-08-26):** unconditional compatible-collar dichotomy, sharp safe-collar
  population, deep Voronoi containment, global clearance budget, degree-six
  near-neighbor matching, strong Gabriel/Delaunay promotion, matched two-well
  structure, exact Hall--Kőnig scaffold conflict theorem, and inner-band near-perfect
  conflict matching.
- **v1.4.0 (2026-08-26):** exact scaffold monomer--dimer blocker classification,
  interior-disjoint cell packing, planar radial conflict graph, exact Hall/Euler and
  leafless deficiency formulas, face-shell identities, strict positivity of all
  terminal-component widths, atomic `s_C=0` components with the nonzero-kernel
  corollary `r=1`, exact component-rotation variance and positive spanning,
  strict-backward origin-rank concentration, and the
  explicit correction retaining `s_C=1` tree components. Target A is reduced to the
  monomer--dimer cycle-cut rigidity inequality `h(G)>=j`; Target B remains the exact
  internal `xi` coforest inequality with the now-concentrated origin budget and exact
  topology transport.

The only supplied external literature remains:

1. `mp05-2-261-269.pdf`;
2. `1951-03.pdf`;
3. `1-s2.0-S0097316598928898-main.pdf`;
4. `s00454-002-0747-6.pdf`;
5. `1204.4403v1.pdf`;
6. `463.pdf`;
7. `10.1007_PL00009374.pdf`.

No internet source is part of this theorem-state file.

---

# 88. Dual Hall nullity and exact lattice-population deficit

Retain the Target A compatible-collar scaffold of Sections 79--81. Put

\[
X=X_m,
\qquad
R=Y_{\rm in},
\qquad
y=|R|,
\tag{88.1}
\]

and let \(\nu=\nu(G)\) be the maximum matching size of the scaffold conflict graph.
Define the **left scaffold Hall nullity**

\[
\boxed{
 d_{\rm sc}
 =\max_{S\subseteq X}\bigl(|S|-|N(S)|\bigr)
 =m-\nu.
}
\tag{88.2}
\]

Define also the **lattice population deficit**

\[
\boxed{\Delta_\Lambda=N-|Y|.}
\tag{88.3}
\]

Because \(Y\subset L\) is a triangular-lattice subset, its mutual distances are at
least one. Because \(L\) is open and \(\operatorname{diam}(L)<D=D(N)\), no
\(N\)-point subset of \(Y\) can exist. Hence

\[
|Y|\le N-1,
\qquad
\boxed{\Delta_\Lambda\ge1.}
\tag{88.4}
\]

Recall

\[
h(G)=y-\nu,
\qquad
\delta=y-m,
\qquad
N=m+k+j,
\qquad
|Y|=k+y.
\tag{88.5}
\]

Therefore

\[
h(G)=\delta+d_{\rm sc},
\tag{88.6}
\]

while

\[
\Delta_\Lambda
=N-|Y|
=(m+k+j)-(k+y)
=j-\delta.
\tag{88.7}
\]

Subtracting \(j\) from (88.6) and using (88.7) gives the exact duality identity

> **Theorem 88.1 (dual Hall/lattice-deficit identity).**
> \[
> \boxed{
> h(G)-j=d_{\rm sc}-\Delta_\Lambda.
> }
> \tag{88.8}
> \]
> Consequently the Target A contradiction is equivalent to
> \[
> \boxed{d_{\rm sc}\ge\Delta_\Lambda.}
> \tag{88.9}
> \]

Thus the older right-deficiency target \(h(G)\ge j\) and the new left-nullity target
\(d_{\rm sc}\ge N-|Y|\) are exactly the same one-integer theorem.

---

# 89. Cell-complex phase charge and Hall cores

For \(S\subseteq X\), let \(m_3(S)\) and \(m_4(S)\) be the numbers of selected
monomer and dimer cells. Let \(\mathcal P_S\) be the elementary-triangle complex
occupied by those cells. Put

- \(b(S)\): the number of elementary lattice edges incident with exactly one occupied
  elementary triangle of \(\mathcal P_S\);
- \(\chi(S)\): the combinatorial Euler characteristic of \(\mathcal P_S\).

The complex has

\[
F=m_3(S)+2m_4(S)
\tag{89.1}
\]

elementary triangles. If \(E,V\) are its lattice-edge and lattice-vertex counts, then

\[
3F=2E-b(S),
\qquad
V=|N(S)|,
\qquad
\chi(S)=V-E+F.
\tag{89.2}
\]

Solving for \(V\) gives

> **Theorem 89.1 (cell-complex Hall formula).**
> \[
> \boxed{
> |S|-|N(S)|
> =\frac{m_3(S)-b(S)}2-\chi(S).
> }
> \tag{89.3}
> \]

At a lattice vertex \(v\in N(S)\), define

\[
p_v(S)=\#\{\text{selected monomer cells incident with }v\},
\qquad
q_v(S)=\#\{\text{selected dimer cells incident with }v\}.
\tag{89.4}
\]

Each selected monomer has three lattice vertices and each selected dimer has four, so

\[
m_3(S)=\frac13\sum_{v\in N(S)}p_v(S),
\qquad
m_4(S)=\frac14\sum_{v\in N(S)}q_v(S).
\tag{89.5}
\]

Subtracting \(|N(S)|\) yields the exact local phase decomposition.

> **Theorem 89.2 (integer phase-charge formula).**
> \[
> \boxed{
> |S|-|N(S)|
> =\sum_{v\in N(S)}
> \left(\frac{p_v(S)}3+\frac{q_v(S)}4-1\right)
> =\frac1{12}\sum_{v\in N(S)}\omega_v(S),
> }
> \tag{89.6}
> \]
> where
> \[
> \boxed{\omega_v(S)=4p_v(S)+3q_v(S)-12.}
> \tag{89.7}
> \]
> Consequently
> \[
> \boxed{
> d_{\rm sc}
> =\max_{S\subseteq X}
> \left[\frac{m_3(S)-b(S)}2-\chi(S)\right]
> =\frac1{12}
> \max_{S\subseteq X}
> \sum_{v\in N(S)}\omega_v(S).
> }
> \tag{89.8}
> \]

## 89.1 Minimum Hall cores

Choose a maximizer \(S\) of \(|S|-|N(S)|\) having minimum cardinality. If
\(d_{\rm sc}=0\), the empty set is allowed and is such a maximizer. Assume now
\(d_{\rm sc}>0\), so the chosen core is nonempty.

Suppose a lattice vertex has selected incidence degree one, with unique incident cell
\(x\). Let \(a\ge1\) be the number of vertices of \(C_x\) having selected incidence
degree one. Removing \(x\) changes the deficiency by

\[
(|S|-1)-(|N(S)|-a)
=(|S|-|N(S)|)+(a-1).
\tag{89.9}
\]

If \(a>1\) this contradicts maximality; if \(a=1\) it preserves deficiency with a
smaller maximizing set. Therefore every lattice vertex of a positive minimum core has
selected incidence degree at least two.

Deficiency is additive over connected incidence components. A component of
nonpositive deficiency could be deleted, increasing total deficiency or preserving it
with fewer selected cells. Hence every component of a positive minimum core has
strictly positive deficiency.

> **Theorem 89.3 (Hall-core normal form).** A positive-deficiency maximizing set may
> be chosen so that:
> 1. every lattice vertex in its neighborhood is incident with at least two selected
>    cells; and
> 2. every connected incidence component has strictly positive Hall deficiency.

The full scaffold lattice degree is at most five, so every lattice vertex of such a
core satisfies

\[
2\le p_v+q_v\le5.
\tag{89.10}
\]

Solving

\[
4p_v+3q_v=12
\tag{89.11}
\]

over nonnegative integers in this range gives exactly two states:

> **Corollary 89.4 (only zero-charge phases).**
> \[
> \boxed{\omega_v=0
> \Longleftrightarrow
> (p_v,q_v)=(3,0)\ \text{or}\ (0,4).}
> \tag{89.12}
> \]

Thus the only locally Hall-neutral bulk incidence phases are three incident monomers
and four incident dimers. Every other core vertex carries a nonzero integer interface
charge. This does **not** imply that the nonzero charges have one sign; mixed-interface
cancellation remains possible.

---

# 90. Exact Hall peeling and transversal-matroid circuits

Let

\[
U=N_G(X),
\qquad
z=|R\setminus U|.
\tag{90.1}
\]

Thus \(z\) counts inner-band lattice sites conflicting with no scaffold point.
Start with all cells and delete any collection \(D=X\setminus S\) in any order. Just
before deleting the \(i\)-th cell, let \(\pi_i\) be the number of its lattice
vertices whose current selected incidence degree is one.

Every lattice vertex in \(U\setminus N(S)\) is counted exactly once: when its final
incident cell is deleted. Therefore

\[
\sum_i\pi_i=|U|-|N(S)|.
\tag{90.2}
\]

Since \(|D|=m-|S|\) and \(y=z+|U|\),

\[
\begin{aligned}
z+\sum_i(\pi_i-1)
&=z+|U|-|N(S)|-|D|\\
&=y-|N(S)|-(m-|S|)\\
&=\delta+|S|-|N(S)|.
\end{aligned}
\tag{90.3}
\]

Every residual subset \(S\subseteq X\) can be obtained by some deletion sequence,
and the value in (90.3) depends only on the residual set. Maximizing gives:

> **Theorem 90.1 (exact Hall-peeling identity).**
> \[
> \boxed{
> h(G)
> =z+\max_{\rm cell\ deletion\ sequences}
> \sum_i(\pi_i-1).
> }
> \tag{90.4}
> \]

Deleting one scaffold point costs one point and frees exactly \(\pi_i\) lattice sites
at that step. Hall deficiency is therefore the maximum cumulative net gain from cell
peeling, plus the lattice sites that were free from the start.

## 90.1 Transversal matroid and charge-12 Hall circuits

The subsets of \(X\) that can be matched injectively to distinct neighboring lattice
vertices form a transversal matroid \(\mathcal M_{\rm sc}\). Its rank is \(\nu\), so

\[
\boxed{
 d_{\rm sc}=|X|-\operatorname{rank}\mathcal M_{\rm sc}.
}
\tag{90.5}
\]

Let \(B\) be a maximum matchable basis. For each \(x\in X\setminus B\), let
\(C_x\subseteq B\cup\{x\}\) be its fundamental circuit. Every proper subset of
\(C_x\) is matchable, while \(C_x\) is not. Hall's theorem therefore forces the
only deficient subset of the circuit to be the entire circuit, and its deficiency is
exactly one:

\[
\boxed{|C_x|-|N(C_x)|=1.}
\tag{90.6}
\]

By Theorem 89.2,

> **Corollary 90.2 (charge-12 fundamental circuits).**
> \[
> \boxed{
> \sum_{v\in N(C_x)}
> \bigl(4p_v(C_x)+3q_v(C_x)-12\bigr)=12.
> }
> \tag{90.7}
> \]

There are \(|X\setminus B|=d_{\rm sc}\) nonbasis elements and hence
\(d_{\rm sc}\) fundamental-circuit certificates of unit nullity. However:

> **Permanent circuit-overlap warning.** Fundamental circuits need not be disjoint,
> laminar, or weakly separated. Their charge-12 certificates cannot be summed as
> spatially distinct interface charge without an additional theorem. Any contraction,
> packing, or contour argument using these circuits must preserve transversal-matroid
> nullity exactly and must control circuit overlap explicitly.

---

# 91. Authoritative v1.4.1 Target A frontier

The cycle-cut formula of Section 81 remains correct, but the preferred v1.4.1 endpoint
is now its exact dual nullity/phase-charge/peeling normal form.

The following statements are equivalent:

\[
\boxed{h(G)\ge j,}
\tag{91.1}
\]

\[
\boxed{d_{\rm sc}\ge\Delta_\Lambda,}
\tag{91.2}
\]

\[
\boxed{
\max_{S\subseteq X}
\sum_{v\in N(S)}
\bigl(4p_v(S)+3q_v(S)-12\bigr)
\ge12\Delta_\Lambda,
}
\tag{91.3}
\]

and

\[
\boxed{
 z+\max_{\rm cell\ deletion\ sequences}
 \sum_i(\pi_i-1)
 \ge j.
}
\tag{91.4}
\]

Because \(\Delta_\Lambda=N-|Y|\ge1\), any certificate of (91.2)--(91.3) has positive
nullity and may be taken in the Hall-core normal form of Theorem 89.3.

Thus the exact new Target A statement is:

> **Target A v1.4.1 (global scaffold phase-charge lemma).** For every scaffold arising
> from a super-boundary triangle-free global minimizer, prove that there exists
> \(S\subseteq X_m\) such that every lattice vertex of \(N(S)\) has selected
> incidence degree at least two and
> \[
> \boxed{
> \sum_{v\in N(S)}
> \bigl(4p_v(S)+3q_v(S)-12\bigr)
> \ge12\bigl(N-|Y|\bigr).
> }
> \tag{91.5}
> \]

The local obstruction is now exact. There are only two zero-charge incidence phases:

1. monomer phase: \((p,q)=(3,0)\);
2. dimer phase: \((p,q)=(0,4)\).

A Hall circuit may contain arbitrarily large regions of either zero-charge phase while
carrying only net charge \(12\) on its interface. Therefore the remaining theorem is
not local motif classification. It must use the global-optimality origin of \(X_m\),
the exact lattice deficit \(\Delta_\Lambda\), exact transversal-matroid nullity, or an
exact diameter-decreasing consequence of coherent zero-charge bulk.

## 91.1 Preferred next route

Choose a maximum matchable basis \(B\). Every nonbasis cell has a fundamental Hall
circuit of charge \(12\). A viable new theorem would establish an exact alternative for
one or a controlled family of such circuits:

1. its nonzero-charge interface yields an additional independent Hall circuit or
   augmenting planar-dual cut;
2. after a **nullity-preserving** contraction, it contains a coherent monomer-type
   domain to which an audited diameter-decreasing deformation applies; or
3. after a **nullity-preserving** contraction, it contains a coherent dimer-strip
   system satisfying the actual hypotheses of the audited Ferrers/Cartesian endpoint.

Scalar charge preservation is not enough; the contraction must preserve the
transversal-matroid nullity relevant to (91.2). Likewise, the existence of
\(d_{\rm sc}\) fundamental circuits does not permit their charges to be added unless
circuit overlap is controlled.

---

# 92. Strengthened two-direction theorem for s_C=1 and bounded tree components

Return to the terminal graph \(\Theta\) in the pure strict-rhombic Target B branch.
For a connected terminal component \(C\), recall

\[
L_j=
\operatorname{span}
\{J(u_\tau-u_{\rho(j)}):\partial_{j\tau}\ne0\},
\qquad
s_C=\dim\operatorname{span}_{j\in J_C}L_j.
\tag{92.1}
\]

> **Theorem 92.1 (all `s_C=1` components are two-directional).**
> If \(s_C=1\), then all trains of \(C\) use exactly two unit direction vectors.

### Proof

Let

\[
W=\operatorname{span}_{j\in J_C}L_j,
\qquad
\dim W=1,
\qquad
M=J^{-1}W.
\tag{92.2}
\]

At a terminal vertex with \(t_j=1\), all incident train vectors lie on one affine line
\(A_j\) parallel to \(M\). At a vertex with \(t_j=0\), all incident train vectors
are equal. Choose a vertex \(j_0\) with \(t_{j_0}=1\), which exists because
\(s_C=1\), and let \(A=A_{j_0}\). Following a path through the connected component,
a \(t_j=0\) vertex preserves the incoming direction, while at a \(t_j=1\) vertex
the unique affine line parallel to \(M\) through the incoming train vector is again
\(A\). Hence

\[
u_\tau\in A\cap S^1
\qquad(\tau\in E(C)).
\tag{92.3}
\]

An affine line meets the unit circle in at most two points. If only one train direction
occurred, then every \(L_j=0\), contradicting \(s_C=1\). Hence exactly two occur.
\(\square\)

The cyclic hypothesis in Theorem 66.2 was therefore unnecessary for the
**two-direction** conclusion. It remains necessary for the currently audited automatic
ordered/Ferrers conclusion: a two-direction tree is not thereby a Ferrers system.

## 92.1 Exact size bound for s_C=1 trees

Assume now that \(C\) is a tree, with its two train directions denoted \(u,v\). The
canonical terminal divergence vectors are

\[
e_j=\sum_{\tau\ni j}\partial_{j\tau}u_\tau.
\tag{92.4}
\]

They are nonzero convex-hull side vectors and occupy distinct oriented rays in their
inherited cyclic order.

At a leaf,

\[
e_j\in\{\pm u,\pm v\},
\tag{92.5}
\]

so there are at most four leaves. If \(n_d\) denotes the number of degree-\(d\)
vertices, the tree identity

\[
n_1=2+\sum_{d\ge3}(d-2)n_d
\tag{92.6}
\]

implies that every vertex has degree at most four and there are at most two vertices
of degree at least three.

At a degree-two vertex, two equal train directions yield an edge vector on a ray
\(\pm u\) or \(\pm v\), while two different train directions yield a ray among
\(\pm u\pm v\). Thus leaves and degree-two vertices together use at most the eight
oriented rays

\[
\pm u,
\quad
\pm v,
\quad
\pm u\pm v.
\tag{92.7}
\]

Because distinct hull-edge vectors occupy distinct oriented rays,

\[
n_1+n_2\le8.
\tag{92.8}
\]

Adding at most two branching vertices gives:

> **Theorem 92.2 (bounded `s_C=1` tree).**
> \[
> \boxed{|V(C)|\le10,\qquad |E(C)|\le9.}
> \tag{92.9}
> \]

The bound is sharp for the abstract terminal-direction/Minkowski data. For example,
with \(u=(1,0)\), \(v=(0,1)\), take the ten convexly ordered edge vectors

\[
\begin{aligned}
&(1,0),(2,1),(1,1),(0,1),(-1,1),\\
&(-1,0),(-2,-1),(-1,-1),(0,-1),(1,-1).
\end{aligned}
\tag{92.10}
\]

They sum to zero and have distinct cyclic directions. With incidence sign positive at
the head and negative at the tail, they are realized as terminal divergences by the
nine-edge tree whose \(u\)-edges are

\[
7\to9,
\quad6\to0,
\quad6\to1,
\quad5\to1,
\quad4\to2,
\tag{92.11}
\]

and whose \(v\)-edges are

\[
9\to1,
\quad8\to2,
\quad7\to3,
\quad6\to4.
\tag{92.12}
\]

This is an abstract regression model, not a claimed global minimizer.

---

# 93. Rank budget for s_C=1 tree origins

Let \(k_{1\rm t}\) be the number of `s_C=1` tree components that occur as distinct
strict-backward origins. Since these components are a subset of all origin components,
Theorem 83.3 gives

\[
\boxed{k_{1\rm t}\le r_\alpha+1.}
\tag{93.1}
\]

If the origin set is proper, in particular whenever an atomic \(s_C=0\) component is
present, then

\[
\boxed{k_{1\rm t}\le r_\alpha.}
\tag{93.2}
\]

By Theorem 92.2, the total number of distinct trains lying in these origin components
satisfies

\[
\boxed{|P_{1\rm t}|\le9(r_\alpha+1),}
\tag{93.3}
\]

or

\[
\boxed{|P_{1\rm t}|\le9r_\alpha}
\tag{93.4}
\]

in the proper-origin case.

Let \(\mathcal A_{1\rm t}\) be the span, in the internal \(\xi\)-quotient, of the
projected active-bar average functionals \(\bar s_h\) occurring in blocker rows whose
strict-backward origins lie in `s_C=1` tree components. For one such component the
internal train-coordinate space modulo common rotation has dimension at most

\[
|E(C)|-1\le8.
\tag{93.5}
\]

Every projected blocker row has the form

\[
\bar e_\tau^*-\bar s_h.
\tag{93.6}
\]

Therefore the coordinate terms from \(k_{1\rm t}\) components contribute at most
\(8k_{1\rm t}\) rank, and the remaining bar-average terms contribute at most
\(\operatorname{rank}\mathcal A_{1\rm t}\).

> **Theorem 93.1 (`s_C=1` tree-origin rank bound).**
> \[
> \boxed{
> \operatorname{rank}\overline{\mathcal B}_{\xi,1\rm t}
> \le
> 8k_{1\rm t}+\operatorname{rank}\mathcal A_{1\rm t}.
> }
> \tag{93.7}
> \]
> Hence
> \[
> \operatorname{rank}\overline{\mathcal B}_{\xi,1\rm t}
> \le
> 8(r_\alpha+1)+\operatorname{rank}\mathcal A_{1\rm t},
> \tag{93.8}
> \]
> with \(8r_\alpha\) in place of \(8(r_\alpha+1)\) in the proper-origin case.

Thus `s_C=1` tree origins can no longer hide unbounded train multiplicity. The
remaining tree-specific obstruction is the possible diversity of the active-bar
averages \(\bar s_h\): many bars may still produce an independent
\(\mathcal A_{1\rm t}\) even when all backward origins lie among finitely many tree
trains.

---

# 94. Authoritative v1.4.1 Target B frontier

The global pure-branch target itself is unchanged:

\[
\boxed{
\operatorname{rank}\overline{\mathcal B}_\xi+I+r
\le T-q-r_\alpha.
}
\tag{94.1}
\]

The correct component classification for a closing proof is now:

1. \(s_C=0\): atomic one-edge segment component, strictly forward for every active
   bar, never a strict-backward origin;
2. \(s_C=1\), tree: exactly two train directions, at most nine trains, and tree-origin
   internal rank controlled by (93.7), with the residual bar-average span
   \(\mathcal A_{1\rm t}\) still live;
3. \(s_C=1\), cyclic: exactly two train directions and, with the additional audited
   cyclic ordering hypotheses, the legitimate two-family/Ferrers class;
4. \(s_C=2\): genuine two-dimensional turning component paying both vector-closure
   directions.

The old v1.4 warning that `s_C=1` trees were an unclassified potentially large class
is superseded. They remain possible, but their coordinate population is uniformly
bounded componentwise.

The next exact Target B subproblem is therefore to charge

\[
\boxed{
\mathcal A_{1\rm t}
=\operatorname{span}
\{\bar s_h:
 h\text{ has a strict-backward incidence in an }s_C=1\text{ tree}\}
}
\tag{94.2}
\]

to the terminal coforest/cycle budget or to the already reserved \(I+r\) dimensions.
A successful theorem here would eliminate repeated-bar diversity as the last
`s_C=1`-tree-specific loophole. It would not by itself finish the `s_C=2` or cyclic
`s_C=1` contributions, nor the topology-corrected transport.

The audited Ferrers numerical endpoint remains unchanged and need not be improved:

\[
0.8944923195\ldots D^2
<
0.9068996821\ldots D^2.
\tag{94.3}
\]

---

# 95. v1.4.1 regressions, rejected shortcuts, and next routes

All earlier regression suites remain binding. Add the following v1.4.1 regressions.

1. **Overlapping Hall circuits.** A transversal matroid can have many fundamental
   circuits sharing most of their support. Section 97 proves exact signed-deficiency
   additivity for fixed-basis unions, but one charge-12 certificate per nonbasis
   element still does not imply spatially disjoint or absolute interface charge
   `12 d_sc`.
2. **Large zero-charge bulk inside one Hall circuit.** A minimally unmatchable circuit
   can contain an arbitrarily large locally neutral monomer or dimer region while its
   net charge remains exactly 12.
3. **Empty nullity core.** When `d_sc=0`, the empty set is a legitimate
   minimum-cardinality maximizer; core minimum-degree conclusions are for positive
   nullity.
4. **Ten-vertex `s_C=1` tree.** The abstract example (92.10)--(92.12) shows that the
   `10`-vertex/`9`-train bound is sharp from terminal-direction/Minkowski data alone.
5. **Repeated-bar diversity.** Bounding the number of tree-origin trains does not
   bound the rank of the active-bar averages `A_{1t}`.

The following shortcuts are rejected unless separately proved:

- treating the charge 12 of all fundamental Hall circuits as disjoint or absolute spatial charge;
- contracting an arbitrary zero-charge phase region without one of the exact
  nullity-preserving contraction theorems of Sections 97--100;
- treating scalar phase-charge conservation as equivalent to matching-rank
  conservation;
- inferring a global Hall surplus from the fact that only two local zero-charge phases
  exist;
- treating every two-direction `s_C=1` component as cyclic/Ferrers;
- replacing the residual `rank A_{1t}` by the number of tree-origin trains without a
  theorem; or
- using the `9(r_alpha+1)` train bound as if it were already the full internal
  coforest inequality.

The preferred new Target A route is a nullity-preserving circuit/phase contraction
or planar-dual theorem that either accumulates independent Hall nullity or converts a
coherent zero-charge phase into an actual global diameter improvement.

The preferred new Target B route is an exact bound on `rank A_{1t}` in terms of
terminal coforest/cycle data or the existing `I+r` budget, followed by the residual
componentwise coforest theorem and exact topology transport.

---

# 96. Version 1.4.1 exact status and provenance

**LEVEL I STATUS: STILL OPEN.**

Version 1.4.1 does not close either survivor branch. It sharpens both.

Target A is now equivalently one of the exact statements

\[
h(G)\ge j,
\qquad
 d_{\rm sc}\ge\Delta_\Lambda,
\tag{96.1}
\]

\[
\max_{S\subseteq X_m}
\sum_{v\in N(S)}
(4p_v(S)+3q_v(S)-12)
\ge12\Delta_\Lambda,
\tag{96.2}
\]

or

\[
z+\max\sum_i(\pi_i-1)\ge j.
\tag{96.3}
\]

The two locally neutral phases are exactly `(3,0)` monomer incidence and `(0,4)`
dimer incidence. The missing theorem is global phase-charge/nullity rigidity, not
another local motif classification.

Target B remains

\[
\boxed{
\operatorname{rank}\overline{\mathcal B}_\xi+I+r
\le T-q-r_\alpha
}
\tag{96.4}
\]

followed by exact topology-corrected transport. The new theorem says every `s_C=1`
component is two-directional and every `s_C=1` tree has at most nine trains. The
remaining tree-specific rank obstruction is the projected active-bar-average span
\(\mathcal A_{1\rm t}\).

Version history:

- v1.0.0: structural synthesis, KKT/stress, almost-rhombic and hybrid normal forms;
- v1.1.0: minimal-face harmonic transport, terminal network, plateau theorem;
- v1.2.0: forest exactification/rattlerization and terminal Minkowski components;
- v1.3.0: compatible collar, clearance matching, two wells, exact Hall scaffold;
- v1.4.0: scaffold monomer--dimer Hall complex plus strict stochasticity and
  strict-backward origin-rank concentration;
- **v1.4.1:** dual Hall/lattice deficit, exact phase-charge and peeling forms,
  transversal-matroid Hall circuits, all-`s_C=1` two-direction theorem, bounded
  `s_C=1` trees, and their internal rank budget.

`erdos_problem_99_1.4.1.md` was the sole canonical theorem-state file at the v1.4.1
stage; Sections 97 onward and the v1.5.0 audit policy now supersede that frontier.

---

# 97. Fixed-basis tight unions, exact full-core contraction, and boundary-order nullity

Retain the Target A scaffold conflict graph
\[
G=(X\sqcup R,E),
\qquad
f(S):=|S|-|N(S)|,
\qquad
d_{\rm sc}=\max_{S\subseteq X}f(S).
\tag{97.1}
\]

Let \(B\subseteq X\) be a maximum matchable basis of the scaffold transversal
matroid. For \(e\in X\setminus B\), let \(C_e\subseteq B\cup\{e\}\) be its
fundamental circuit. For \(A\subseteq X\setminus B\), put
\[
U_A:=\bigcup_{e\in A}C_e.
\tag{97.2}
\]

## 97.1 Exact fixed-basis union theorem

> **Theorem 97.1 (tight fundamental-circuit unions).**
> For every \(A\subseteq X\setminus B\),
> \[
> \boxed{f(U_A)=|A|.}
> \tag{97.3}
> \]
> Consequently
> \[
> \boxed{
> \sum_{v\in N(U_A)}
> \bigl(4p_v(U_A)+3q_v(U_A)-12\bigr)=12|A|.
> }
> \tag{97.4}
> \]

### Proof

Let
\[
B_A:=U_A\cap B.
\tag{97.5}
\]
Every \(e\in A\) lies in the matroid closure of
\(C_e\setminus\{e\}\subseteq B_A\), while \(B_A\) is independent. Hence
\[
r(U_A)=|B_A|,
\qquad
|U_A|-r(U_A)=|A|.
\tag{97.6}
\]

Any matching of \(U_A\) can use only vertices in \(N(U_A)\), so
\[
r(U_A)\le |N(U_A)|.
\tag{97.7}
\]
Therefore
\[
f(U_A)
=|U_A|-|N(U_A)|
\le |U_A|-r(U_A)
=|A|.
\tag{97.8}
\]

Order \(A=\{e_1,\ldots,e_k\}\) and put
\[
U_i:=\bigcup_{j\le i}C_{e_j}.
\tag{97.9}
\]
Because \(C_{e_i}\subseteq B\cup\{e_i\}\) and no earlier fundamental circuit contains
\(e_i\),
\[
U_{i-1}\cap C_{e_i}\subseteq B.
\tag{97.10}
\]
Thus the intersection is matchable and has deficiency at most zero. Also
\[
f(C_{e_i})=1.
\tag{97.11}
\]

The neighborhood function is submodular, so \(f\) is supermodular:
\[
f(S\cup T)+f(S\cap T)\ge f(S)+f(T).
\tag{97.12}
\]
Inductively, if \(f(U_{i-1})=i-1\), then
\[
f(U_i)+f(U_{i-1}\cap C_{e_i})\ge i.
\tag{97.13}
\]
But (97.8) gives \(f(U_i)\le i\) and (97.10) gives
\(f(U_{i-1}\cap C_{e_i})\le0\). Therefore equality holds in both:
\[
\boxed{
f(U_i)=i,
\qquad
f(U_{i-1}\cap C_{e_i})=0.
}
\tag{97.14}
\]
This proves (97.3). Equation (97.4) follows from the exact phase-charge identity.
\(\square\)

The important correction is precise:

> Fundamental circuits relative to one fixed maximum basis may overlap heavily, but
> every successive overlap is Hall-tight. Signed Hall deficiency is exactly additive
> along the fixed-basis union flag. This does **not** make the circuit interfaces
> disjoint and does not make absolute/spatial phase charge additive.

## 97.2 Full tight-core contraction

Take
\[
A=X\setminus B,
\qquad
U:=U_A,
\qquad
W:=N(U),
\qquad
d:=d_{\rm sc}.
\tag{97.15}
\]
Since
\[
|A|=|X|-r(X)=d_{\rm sc},
\tag{97.16}
\]
Theorem 97.1 gives
\[
|U|-|W|=d.
\tag{97.17}
\]

Let \(B_U=U\cap B\). Then
\[
|W|=|U|-d=|B_U|.
\tag{97.18}
\]
Any matching saturating \(B\) maps \(B_U\) into \(W\). Equal cardinalities force a
bijection \(B_U\to W\), and consequently map
\[
B\setminus B_U=X\setminus U
\tag{97.19}
\]
into \(R\setminus W\).

Thus the residual left side is fully matchable.

Moreover \(W=N(U)\), so there are no conflict edges from \(U\) to \(R\setminus W\).
Every independent set in the residual conflict graph therefore lifts by adjoining
all of \(U\).

Define the residual population data
\[
N^0:=N-|U|,
\qquad
Y^0:=Y\setminus W.
\tag{97.20}
\]
Then
\[
\boxed{
N^0-|Y^0|
=\Delta_\Lambda-d_{\rm sc}.
}
\tag{97.21}
\]

> **Theorem 97.2 (nullity-zero full-core contraction).**
> The entire scaffold nullity can be extracted as one fixed-basis tight core
> \(U\cup W\). After deleting that core, the residual left side is fully matchable,
> and the exact surviving lattice-population gap is
> \[
> \boxed{g=\Delta_\Lambda-d_{\rm sc}.}
> \tag{97.22}
> \]

A hypothetical Target A survivor has
\[
d_{\rm sc}\le\Delta_\Lambda-1,
\tag{97.23}
\]
so
\[
\boxed{g\ge1.}
\tag{97.24}
\]

The residual \(X\setminus U\) is a subset of a global optimum, but it is **not**
known to be globally optimal for \(N^0\). No optimum-only theorem may be recursively
applied to it without a separate argument.

## 97.3 Boundary-order bound on all scaffold nullity

Let \(d_m=D(m)\), \(D=D(N)\), and
\[
t=\frac{D-d_m}{2}>1.
\tag{97.25}
\]
For the same generic triangular-lattice translate, the Voronoi cells centered at
lattice sites in the inner band cover
\[
K_m+\left(1-\frac1{\sqrt3}\right)\mathbb B.
\tag{97.26}
\]
Combining the resulting lattice count with Steiner and finite Oler gives, for
\[
\delta=|Y_{\rm in}|-m,
\tag{97.27}
\]
the exact lower estimate
\[
\boxed{
\delta\ge
-1-\frac{7-4\sqrt3}{6}P_m
+\frac{8\pi}{3\sqrt3}
-\frac{4\pi}{3}.
}
\tag{97.28}
\]

Combining this with the trusted \(t\)-dependent safe-collar estimate yields
\[
\boxed{
\Delta_\Lambda
<
\pi D+\frac{2\pi}{3}d_m
+1+\frac{\pi}{3}-\frac{2\pi}{3\sqrt3}.
}
\tag{97.29}
\]
A survivor therefore satisfies
\[
\boxed{
d_{\rm sc}
<
\pi D+\frac{2\pi}{3}d_m
+\frac{\pi}{3}-\frac{2\pi}{3\sqrt3}.
}
\tag{97.30}
\]

Since \(t>1\) implies \(d_m<D-2\),
\[
\boxed{
\Delta_\Lambda
<
\frac{5\pi}{3}D
+1-\pi-\frac{2\pi}{3\sqrt3},
}
\tag{97.31}
\]
and
\[
\boxed{
d_{\rm sc}
<
\frac{5\pi}{3}D
-\pi-\frac{2\pi}{3\sqrt3}
=
5.23598775598\ldots D-4.35079222975\ldots.
}
\tag{97.32}
\]

Thus **all scaffold nullity is boundary-order** in every hypothetical survivor.

---

# 98. Phase-selective contraction and six planar gammoid presentations

Fix a lattice basis \(e_1,e_2\). Write the two orientations of elementary unit
triangles as
\[
T_z^+=\operatorname{conv}\{z,z+e_1,z+e_2\},
\tag{98.1}
\]
\[
T_z^-=\operatorname{conv}\{z+e_1,z+e_2,z+e_1+e_2\}.
\tag{98.2}
\]

Partition the scaffold blocker cells as
\[
X=\mathcal D\sqcup\mathcal M_+\sqcup\mathcal M_-,
\tag{98.3}
\]
where \(\mathcal D\) are dimers and \(\mathcal M_\pm\) are monomers of the two
orientations.

## 98.1 Entire crystalline phases are independent

Every dimer contains exactly one \(+\)-triangle and one \(-\)-triangle. Every
\(+\)-monomer contains exactly one \(+\)-triangle. Since distinct blocker cells have
disjoint interiors, distinct cells in
\[
\mathcal I_+:=\mathcal D\cup\mathcal M_+
\tag{98.4}
\]
contain distinct \(+\)-triangles.

The map
\[
T_z^+\longmapsto z
\tag{98.5}
\]
matches every such triangle to one of its actual conflict vertices and is injective
over the selected cells. Therefore \(\mathcal I_+\) is independent. Symmetrically,
\[
\mathcal I_-:=\mathcal D\cup\mathcal M_-
\tag{98.6}
\]
is independent.

> **Theorem 98.1 (phase-selective independence).**
> \[
> \boxed{
> \mathcal D\cup\mathcal M_+,
> \quad
> \mathcal D\cup\mathcal M_-
> \text{ are independent in }\mathcal M_{\rm sc}.
> }
> \tag{98.7}
> \]

If \(m_\pm=|\mathcal M_\pm|\), contraction by either independent phase preserves the
entire nullity:
\[
\boxed{
d_{\rm sc}
=
m_-
-r_{\mathcal M_{\rm sc}/\mathcal I_+}(\mathcal M_-)
=
m_+
-r_{\mathcal M_{\rm sc}/\mathcal I_-}(\mathcal M_+).
}
\tag{98.8}
\]

This is an exact matroid theorem, not a scalar zero-charge argument.

## 98.2 Alternating-gammoid representation

Fix a matching \(\mu_+\) of \(\mathcal I_+\) to the distinguished \(+\)-triangle
vertices and put
\[
T_+:=Y_{\rm in}\setminus\mu_+(\mathcal I_+).
\tag{98.9}
\]
Orient the radial conflict graph alternately relative to \(\mu_+\):

- residual \(-\)-monomer \(\to\) lattice vertex;
- matched lattice vertex \(\to\) its \(\mathcal I_+\)-cell;
- every other edge of an \(\mathcal I_+\)-cell points from the cell to the lattice
  vertex.

Let \(\lambda_+\) be the maximum number of pairwise vertex-disjoint directed paths
from distinct residual \(-\)-monomers to distinct sinks in \(T_+\).

The usual symmetric-difference argument gives
\[
J\subseteq\mathcal M_-
\text{ independent in }\mathcal M_{\rm sc}/\mathcal I_+
\iff
J\text{ links vertex-disjointly to }T_+.
\tag{98.10}
\]
Hence
\[
\boxed{
\nu(G)=|\mathcal I_+|+\lambda_+,
}
\tag{98.11}
\]
\[
\boxed{
d_{\rm sc}=m_- -\lambda_+,
\qquad
h(G)=|T_+|-\lambda_+.
}
\tag{98.12}
\]
The symmetric equations hold with \(+\) and \(-\) exchanged.

In particular
\[
\boxed{
d_{\rm sc}
=
m_- -\lambda_+
=
m_+ -\lambda_-,
}
\tag{98.13}
\]
and
\[
\boxed{d_{\rm sc}\le\min(m_+,m_-).}
\tag{98.14}
\]

## 98.3 Six anchor choices and layered DAGs

For each orientation there are three choices of distinguished vertex of the
elementary triangle. For the \(+\)-contraction, label the anchors \(a=0,1,2\).
In lattice coordinates
\[
v=pe_1+qe_2,
\tag{98.15}
\]
take the height functions
\[
\ell_0(v)=p+q,
\qquad
\ell_1(v)=-p,
\qquad
\ell_2(v)=-q.
\tag{98.16}
\]

For each anchor, every directed alternating arc is nondecreasing in the
corresponding height. Strict arcs raise height. Zero-height transitions are unit
steps along one lattice line and come from dimers. Two oppositely directed
zero-height transitions would force two dimers to occupy the same elementary
triangle, contradicting disjoint cell interiors.

> **Theorem 98.2 (six layered phase-anchor DAGs).**
> Each of the three anchor presentations for either monomer orientation is a planar
> directed acyclic graph, and for every anchor \(a\)
> \[
> \boxed{
> d_{\rm sc}=m_- -\lambda_a,
> \qquad
> h(G)=|T_a|-\lambda_a
> }
> \tag{98.17}
> \]
> in the \(+\)-contraction, with the symmetric statement for the \(-\)-contraction.

## 98.4 Exact directed-contour formula

For a fixed phase-anchor DAG \(\Gamma_a\), let \(S=\mathcal M_-\) denote the sources
and \(T_a\) the free sinks. For \(W\subseteq V(\Gamma_a)\), define
\[
\partial^+W
=
\{v\notin W:\exists u\in W,\ u\to v\},
\tag{98.18}
\]
\[
\partial^-W
=
\{v\notin W:\exists u\in W,\ v\to u\}.
\tag{98.19}
\]

Directed vertex-Menger, with source vertices of indegree zero, gives
\[
\boxed{
d_{\rm sc}
=
\max_{W\cap T_a=\varnothing}
\bigl(|S\cap W|-|\partial^+W|\bigr).
}
\tag{98.20}
\]
Applying the same argument to the reversed digraph gives
\[
\boxed{
h(G)
=
\max_{W\cap S=\varnothing}
\bigl(|T_a\cap W|-|\partial^-W|\bigr).
}
\tag{98.21}
\]

This replaces signed local interface bookkeeping by an exact absolute directed
boundary quantity. It is still not a width-one-annulus terminalization, and abstract
planarity alone does not imply the Target A inequality.

---

# 99. Plateau terminalization and exact boundary-terminal matching

Let \(m\) be the smaller cardinality arising in Target A and
\[
d=D(m).
\tag{99.1}
\]
Define the right endpoint of the \(d\)-plateau by
\[
m^\ast:=\max\{q\ge m:D(q)=d\}.
\tag{99.2}
\]
The exact plateau theorem gives
\[
\boxed{
0\le m^\ast-m<\frac{\pi}{2}d.
}
\tag{99.3}
\]
Replacing \(m\) by \(m^\ast\) costs only \(O(D)\) points, so a super-boundary
rattler population remains super-boundary.

Choose an \(m^\ast\)-point optimum \(X^\ast\) and put
\[
K^\ast=\operatorname{conv}X^\ast.
\tag{99.4}
\]
By maximality of the plateau,
\[
D(m^\ast+1)>d.
\tag{99.5}
\]

## 99.1 Unit-covering saturation at the plateau endpoint

If \(z\in K^\ast\) satisfied
\[
|z-x|\ge1
\qquad(x\in X^\ast),
\tag{99.6}
\]
then \(X^\ast\cup\{z\}\) would be an \((m^\ast+1)\)-point unit-separated set of
diameter at most \(d\), contradicting (99.5). Therefore
\[
\boxed{
\forall z\in K^\ast,\qquad
\min_{x\in X^\ast}|z-x|<1.
}
\tag{99.7}
\]

The strict inequality matters.

The same saturated clearance and Delaunay arguments used earlier can therefore be
run on \(X^\ast\) itself. In particular,
\[
\sum_{x\in X^\ast}
\left(\min_{x'\ne x}|x-x'|-1\right)
<
\left(24+\frac{\pi}{2}\right)d+18.
\tag{99.8}
\]
The local equality wells remain
\[
\{1,1,1\},
\qquad
\{1,1,\sqrt3\}.
\tag{99.9}
\]
This co-embeds the saturated Delaunay geometry and the exact scaffold geometry on the
same smaller optimum. It does **not** by itself imply the Target A Hall surplus.

## 99.2 The interior lattice has exactly zero right deficiency

For the generic scaffold translate define
\[
Z=(\Lambda+v)\cap\operatorname{int}K^\ast,
\qquad
O=Y_{\rm in}\setminus Z.
\tag{99.10}
\]
Genericity excludes lattice points on \(\partial K^\ast\), so
\[
O\subset
\operatorname{int}(K^\ast+\mathbb B)\setminus K^\ast.
\tag{99.11}
\]

Let
\[
G_0=G[X^\ast\sqcup Z].
\tag{99.12}
\]
An independent set in \(G_0\) is exactly a unit-separated subset of \(K^\ast\). By
(99.5) it has at most \(m^\ast\) elements, while \(X^\ast\) itself has \(m^\ast\)
elements. Therefore
\[
\alpha(G_0)=m^\ast.
\tag{99.13}
\]
Kőnig gives
\[
\boxed{\nu(G_0)=|Z|.}
\tag{99.14}
\]
Equivalently,
\[
\boxed{
|Q|\le|N_{G_0}(Q)|
\qquad(Q\subseteq Z).
}
\tag{99.15}
\]

Thus the interior lattice has zero right Hall deficiency.

Because plateau saturation also excludes isolated vertices of \(Z\), the exact
peeling identity gives
\[
\boxed{
\max_{\text{interior cell deletions}}
\sum_i(\pi_i^{\rm int}-1)=0.
}
\tag{99.16}
\]

## 99.3 Exact deep-nullity plus boundary-linkage split

Let \(\mathcal M_Z\) be the transversal matroid on \(X^\ast\) represented by
conflicts with \(Z\). Put
\[
X_{\rm deep}
=
\{x\in X^\ast:N(x)\subseteq Z\}.
\tag{99.17}
\]
Define
\[
\boxed{
d_{\rm int}
=
|X_{\rm deep}|-r_{\mathcal M_Z}(X_{\rm deep}).
}
\tag{99.18}
\]

Choose a basis \(I_{\rm deep}\) of the restriction to \(X_{\rm deep}\), extend it to
a basis \(I_0\) of \(\mathcal M_Z\), and choose a matching \(\mu_0\) of \(I_0\) onto
all of \(Z\). Put
\[
U_{\rm int}=X_{\rm deep}\setminus I_{\rm deep},
\tag{99.19}
\]
\[
X_\partial=X^\ast\setminus X_{\rm deep},
\qquad
S_\partial=X_\partial\setminus I_0.
\tag{99.20}
\]
Then
\[
\boxed{
m^\ast-|Z|
=d_{\rm int}+s_\partial,
\qquad
s_\partial:=|S_\partial|.
}
\tag{99.21}
\]

No augmenting path from \(O\) relative to \(\mu_0\) can end at a vertex of
\(U_{\rm int}\). Flipping such a path would match
\(I_{\rm deep}\cup\{x\}\) into \(Z\), contradicting maximality of the restricted
basis.

Let \(\lambda_\partial\) be the maximum number of vertex-disjoint augmenting paths
from distinct \(O\)-vertices to distinct \(S_\partial\)-vertices. Then
\[
\boxed{
\nu(G)=|Z|+\lambda_\partial,
}
\tag{99.22}
\]
hence
\[
\boxed{
d_{\rm sc}
=
d_{\rm int}+s_\partial-\lambda_\partial.
}
\tag{99.23}
\]
On the right,
\[
\boxed{
h(G)=|O|-\lambda_\partial.
}
\tag{99.24}
\]

This is the exact boundary-terminal normal form. Deep unmatched blockers are not
discarded; their exact cost is \(d_{\rm int}\).

Every \(x\in X_\partial\) lies within unit distance of \(\partial K^\ast\), and every
\(y\in O\) lies in the exterior unit band. Both terminal populations are
boundary-order:
\[
\boxed{
s_\partial\le|X_\partial|\le12d+9,
}
\tag{99.25}
\]
and
\[
\boxed{
d_{\rm int}+s_\partial
=m^\ast-|Z|
\le1+\frac{7\pi}{6}d.
}
\tag{99.26}
\]

The routing graph may still traverse the \(O(d^2)\) interior. Boundary terminality
does not imply width-one-annulus routing.

## 99.4 Two-sided plateau normalization

For a genuine super-boundary source survivor, let
\[
N_-:=\min\{q:D(q)=D\},
\qquad
m_+:=\max\{q:D(q)=d\},
\tag{99.27}
\]
and put
\[
p_N=N-N_-,
\qquad
p_m=m_+-m.
\tag{99.28}
\]
The plateau theorem gives
\[
p_N<\frac{\pi D}{2},
\qquad
p_m<\frac{\pi d}{2}.
\tag{99.29}
\]

Since the source contains \(\rho=\omega(D)\) strict rattlers, sufficiently large
survivors satisfy
\[
\rho>p_N+p_m.
\tag{99.30}
\]
Deleting \(p_N\) non-diametral strict rattlers leaves an \(N_-\)-point
triangle-free global minimizer of the same diameter \(D\). Designating
\[
\rho^\dagger:=\rho-p_N-p_m
\tag{99.31}
\]
further rattlers for removal makes the target smaller cardinality exactly \(m_+\).

Define the finite-packing defect
\[
E(n)
=
\frac{D(n)^2}{c}
+\frac{\pi D(n)}2
-(n-1).
\tag{99.32}
\]
At fixed diameter, \(E\) decreases by one when the cardinality increases by one, so
\[
\boxed{
E(N_-)=E(N)+p_N,
\qquad
E(m_+)=E(m)-p_m.
}
\tag{99.33}
\]
Thus two-sided endpoint normalization improves the defect transfer by exactly
\(p_N+p_m\).

This normalization is useful, but the sign of the residual defect transfer remains
uncontrolled.

---

# 100. Phase-pure boundary minors and exterior interface charge

Retain the plateau-terminalized scaffold of Section 99 and split
\[
X^\ast=X^\circ\sqcup X^\partial,
\tag{100.1}
\]
where
\[
X^\circ=\{x:N(x)\subseteq Z\},
\qquad
X^\partial=X^\ast\setminus X^\circ.
\tag{100.2}
\]
Then \(d_{\rm int}\) is the exact nullity of the deep restriction.

Fix the \(+\)-phase contraction
\[
\mathcal A_+=\mathcal D\cup\mathcal M_+,
\qquad
\mathcal E=\mathcal M_-,
\tag{100.3}
\]
and split both sets into deep and boundary parts.

Let
\[
\mathcal L=\mathcal M/\mathcal A_+^\circ.
\tag{100.4}
\]
Since \(\mathcal A_+^\circ\) is independent,
\[
|\mathcal E^\circ|-r_{\mathcal L}(\mathcal E^\circ)=d_{\rm int}.
\tag{100.5}
\]

Define the deep-rank transfer
\[
\theta_+
=
r_{\mathcal L}(\mathcal E^\circ)
+
|\mathcal A_+^\partial|
-
r_{\mathcal L}
(\mathcal E^\circ\cup\mathcal A_+^\partial).
\tag{100.6}
\]
Submodularity and independence give
\[
\boxed{
0\le\theta_+\le|\mathcal A_+^\partial|.
}
\tag{100.7}
\]

After contracting all of \(\mathcal A_+\),
\[
\boxed{
|\mathcal E^\circ|
-
r_{\mathcal M/\mathcal A_+}(\mathcal E^\circ)
=
d_{\rm int}+\theta_+.
}
\tag{100.8}
\]

Choose a basis \(J_+\) of \(\mathcal E^\circ\) in the contracted matroid and put
\[
\mathcal Q_+
=
\mathcal M/(\mathcal A_+\cup J_+).
\tag{100.9}
\]
The elements of
\[
\mathcal E^\circ\setminus J_+
\tag{100.10}
\]
are loops. The only remaining possibly nonloop ground elements are
\[
\mathcal E^\partial
=
\mathcal M_-\cap X^\partial.
\tag{100.11}
\]

Define
\[
d_{\partial,-}^{(+)}
=
|\mathcal E^\partial|
-r_{\mathcal Q_+}(\mathcal E^\partial).
\tag{100.12}
\]

> **Theorem 100.1 (phase-pure boundary decomposition).**
> \[
> \boxed{
> d_{\rm sc}
> =
> d_{\rm int}
> +\theta_+
> +d_{\partial,-}^{(+)}.
> }
> \tag{100.13}
> \]
> Symmetrically,
> \[
> \boxed{
> d_{\rm sc}
> =
> d_{\rm int}
> +\theta_-
> +d_{\partial,+}^{(-)}.
> }
> \tag{100.14}
> \]

The complete residual ground set obeys
\[
\boxed{
|\operatorname{ground}(\mathcal Q_\pm)|
\le
d_{\rm int}+|X^\partial|
\le
\left(12+\frac{7\pi}{6}\right)d+10
=
15.665191\ldots d+10.
}
\tag{100.15}
\]

Thus the exact matroid ground set, not merely its terminal set, can be reduced to
\(O(d)\) elements. Its alternating routing may still pass through bulk lattice
vertices.

## 100.1 Exterior degree and phase-interface theorem

For generic lattice translate and \(y\in O\),
\[
\boxed{\deg_G(y)\le3.}
\tag{100.16}
\]
Indeed all conflict vectors \(x-y\) lie in one open semicircle. Four such vectors
would contain two consecutive vectors separated by angle \(<\pi/3\), and for
lengths \(r,s<1\),
\[
|x-x'|^2
<
r^2+s^2-rs
<1,
\tag{100.17}
\]
contradicting unit separation.

Around one triangular-lattice vertex, the three monomer sectors of one fixed
orientation alternate. Three such sectors cannot all fit into one open semicircle.
Therefore
\[
\boxed{
\deg_{\mathcal M_+}(y)\le2,
\qquad
\deg_{\mathcal M_-}(y)\le2
\qquad(y\in O).
}
\tag{100.18}
\]

Let \(S\) be a connected positive Hall core of deficiency \(r\). At
\(y\in N(S)\cap O\), write
\[
p_y=p_y^++p_y^-,
\qquad
\tau_y=p_y^+-p_y^-,
\tag{100.19}
\]
and define
\[
\beta_y=12-4p_y-3q_y\ge0.
\tag{100.20}
\]
Every outer core vertex has selected degree two or three. If \(\beta_y=0\), then
\((p_y,q_y)=(3,0)\), and (100.18) forces a \(2{:}1\) orientation split, so
\[
|\tau_y|=1.
\tag{100.21}
\]
Hence
\[
\boxed{
\beta_y+|\tau_y|\ge1.
}
\tag{100.22}
\]

Splitting the exact phase-charge identity into \(Z\) and \(O\) gives
\[
\boxed{
\sum_{z\in N(S)\cap Z}\omega_z
+
\sum_{y\in N(S)\cap O}|\tau_y|
\ge
12r+|N(S)\cap O|.
}
\tag{100.23}
\]

Thus the scalar-neutral monomer phase cannot meet the physical exterior boundary as
a pure orientation: every neutral exterior terminal carries an absolute orientation
interface.

---

# 101. Quantized convexification gap for positive Hall cores

Let \(S\) be a connected positive Hall core of deficiency \(r>0\). Let

- \(m_3=m_++m_-\) be the monomer count;
- \(m_4\) the dimer count;
- \(F=m_3+2m_4\) the number of occupied elementary triangles;
- \(q\) the number of holes;
- \(b_0\) the outer boundary length;
- \(b_h\) the total hole-boundary length;
- \(b=b_0+b_h\);
- \(\mathcal P_S\) the occupied elementary-triangle complex;
- \(H=\operatorname{conv}\mathcal P_S\).

Put
\[
g_H
=
\frac{\operatorname{area}(H)-\operatorname{area}(\mathcal P_S)}{c_0}.
\tag{101.1}
\]
Because \(H\) is a triangular-lattice polygon,
\[
g_H\in\mathbb Z_{\ge0}.
\tag{101.2}
\]

The blocker points lie strictly inside \(H\). Finite Oler applied to those
\(m_3+m_4\) points, together with
\[
\operatorname{per}H\le b_0,
\tag{101.3}
\]
gives
\[
m_3+m_4-1
<
\frac{F+g_H}{2}+\frac{b_0}{2}.
\tag{101.4}
\]
After multiplying by two and using integrality,
\[
g_H\ge m_3-1-b_0.
\tag{101.5}
\]

The cell-complex formula for a connected core is
\[
r=\frac{m_3-b}{2}-1+q,
\tag{101.6}
\]
so
\[
m_3=b+2r+2-2q.
\tag{101.7}
\]
Since
\[
b_h\ge3q,
\tag{101.8}
\]
we obtain the exact quantized gap:

> **Theorem 101.1 (convexification-gap theorem).**
> \[
> \boxed{
> g_H\ge2r+q+1.
> }
> \tag{101.9}
> \]

In particular, no positive Hall core has a convex occupied cell complex.

Let
\[
\varepsilon=b-3(q+1)\ge0.
\tag{101.10}
\]
Then
\[
b_0\le\varepsilon+3.
\tag{101.11}
\]
Isoperimetry gives
\[
c_0(F+g_H)
=
\operatorname{area}(H)
\le
\frac{b_0^2}{4\pi},
\tag{101.12}
\]
hence
\[
\boxed{
F+2r+q+1
\le
\frac{(\varepsilon+3)^2}{\pi\sqrt3}.
}
\tag{101.13}
\]

For a circuit \(r=1\). If \(\varepsilon\le6\), then
\[
\frac{(\varepsilon+3)^2}{\varepsilon+10}
\le
\frac{81}{16}
<
\pi\sqrt3,
\tag{101.14}
\]
contradicting (101.13), because
\[
m_3=\varepsilon+q+7
\quad\text{and}\quad
F\ge m_3.
\tag{101.15}
\]
Therefore
\[
\boxed{\varepsilon\ge7}
\tag{101.16}
\]
for every Hall circuit.

The phase-orientation side count gives
\[
3(m_+-m_-)=b_+-b_-,
\qquad
|m_+-m_-|\le\frac b3.
\tag{101.17}
\]
Combining with (101.7) and \(\varepsilon\ge7\) yields:

> **Corollary 101.2 (strong biphasic circuit kernel).**
> Every scaffold Hall circuit satisfies
> \[
> \boxed{
> m_3\ge14,
> \qquad
> m_+\ge6,
> \qquad
> m_-\ge6.
> }
> \tag{101.18}
> \]

This does not sum convexification gaps over overlapping circuits.

---

# 102. Exact boundary Schur response

Retain the plateau-terminalized scaffold and write
\[
Z=(\Lambda+v)\cap\operatorname{int}K,
\qquad
O=Y_{\rm in}\setminus Z.
\tag{102.1}
\]

Use a generic bipartite incidence matrix \(A\), with algebraically independent
nonzero entries on conflict edges. Generic matrix rank equals matching rank.

Let
\[
X^\circ=\{x\in X:N(x)\subseteq Z\},
\qquad
X^\partial=X\setminus X^\circ.
\tag{102.2}
\]
Choose a basis \(I^\circ\subseteq X^\circ\) for the restricted column matroid on
\(Z\), and extend it to a basis \(B\subseteq X\) of the full \(Z\)-row matroid.
Since the \(Z\)-rows have full rank,
\[
|B|=|Z|,
\qquad
A[Z,B]\text{ is invertible}.
\tag{102.3}
\]

Put
\[
C=X\setminus B.
\tag{102.4}
\]
The deep nonbasis columns
\[
C^\circ=C\cap X^\circ
\tag{102.5}
\]
become loops after contracting \(B\), because they lie in the span of
\(I^\circ\) and have zero entries on \(O\). Therefore
\[
|C^\circ|=d_{\rm int},
\tag{102.6}
\]
and only
\[
C^\partial=C\cap X^\partial
\tag{102.7}
\]
survives.

Define the Schur response matrix
\[
\boxed{
S
=
A[O,C^\partial]
-
A[O,B]A[Z,B]^{-1}A[Z,C^\partial].
}
\tag{102.8}
\]

Block Gaussian elimination gives:

> **Theorem 102.1 (boundary-response rank theorem).**
> \[
> \boxed{
> \nu(G)=|Z|+\operatorname{rank}S,
> }
> \tag{102.9}
> \]
> \[
> \boxed{
> d_{\rm sc}
> =
> d_{\rm int}
> +|C^\partial|
> -\operatorname{rank}S,
> }
> \tag{102.10}
> \]
> \[
> \boxed{
> h(G)
> =
> |O|-\operatorname{rank}S.
> }
> \tag{102.11}
> \]

Thus the entire quadratic matching problem contracts to an
\(O(D)\)-by-\(O(D)\) exact boundary response matrix.

For \(I\subseteq O\), \(J\subseteq C^\partial\), and \(|I|=|J|=k\),
the Schur determinant identity gives
\[
\boxed{
\det S[I,J]
=
\pm
\frac{
\det A[Z\cup I,B\cup J]
}{
\det A[Z,B]
}.
}
\tag{102.12}
\]
Therefore a response minor is nonzero exactly when the corresponding induced
conflict system admits a matching saturating \(Z\cup I\). Relative to a fixed
\(Z\)-perfect matching, the symmetric difference consists of vertex-disjoint
alternating \(I\)-to-\(J\) paths together with possible alternating cycles.

This is an exact boundary linkage theorem. It does not imply a width-one-annulus
routing graph or an acyclic orientation.

## 102.1 Two-phase connectivity interpretation

After contracting all dimers, the two monomer phases are each independent. Let the
resulting matroid still be denoted \(M\). Then
\[
r(M_+)=|M_+|,
\qquad
r(M_-)=|M_-|,
\tag{102.13}
\]
and
\[
\boxed{
d_{\rm sc}
=
r(M_+)+r(M_-)-r(M_+\cup M_-).
}
\tag{102.14}
\]

Thus all scaffold nullity is exactly the matroid connectivity between two
individually matchable crystalline phases.

Split
\[
M_\pm=M_{\pm,0}\sqcup M_{\pm,1}
\tag{102.15}
\]
into deep and boundary monomers. For
\[
I(U;V\mid W)
=
r(U\cup W)+r(V\cup W)-r(W)-r(U\cup V\cup W),
\tag{102.16}
\]
the matroid chain rule gives
\[
\boxed{
d_{\rm sc}
=
\kappa_{00}+\kappa_{01}+\kappa_{10}+\kappa_{11},
}
\tag{102.17}
\]
where
\[
\begin{aligned}
\kappa_{00}&=I(M_{+,0};M_{-,0}),\\
\kappa_{01}&=I(M_{+,0};M_{-,1}\mid M_{-,0}),\\
\kappa_{10}&=I(M_{+,1};M_{-,0}\mid M_{+,0}),\\
\kappa_{11}&=I(M_{+,1};M_{-,1}\mid M_{+,0}\cup M_{-,0}).
\end{aligned}
\tag{102.18}
\]
Every \(\kappa_{ij}\) is a nonnegative integer. Adding one boundary element changes
connectivity by at most one, so
\[
\boxed{
d_{\rm sc}-\kappa_{00}
\le
|M_{+,1}|+|M_{-,1}|
\le12d+9.
}
\tag{102.19}
\]

This is the overlap-safe replacement for spatially summing charge-12 circuits.

---

# 103. Source-specific contact-core and rattler-cage structure

The scaffold-only theorems above cannot close Target A. We now record the exact
information that genuinely remembers the triangle-free source minimizer.

The legitimate common representative is the hybrid representative of Theorem 12.4:
it contains, pointwise unchanged, the jammed nonisolated core \(K\) of a
contact-minimal triangle-free minimizer, while every contact edge outside \(K\) is a
bridge. Root-skeleton exactification and forest rattlerization act on those bridge
trees while keeping \(K\) fixed.

This is the bridge that permits source-face and latent-forest statements to be used
together. The unrelated maximal-contact representative is not substituted here.

## 103.1 Exact facial-defect budget of the fixed core

Let the fixed contact-minimal core have

- \(v\) vertices;
- \(e\) unit-contact edges;
- \(c\) connected components;
- \(q\) diameter endpoints in the core.

Every bounded face has length at least four. Let \(m_F\) be bounded face length and
let \(b_\infty\) be the outer facial boundary-walk length, counting bridge
incidences with multiplicity.

Euler and face-edge incidence give
\[
\boxed{
b_\infty+\sum_{F\ {\rm bounded}}(m_F-4)
=
4v-2e-4c.
}
\tag{103.1}
\]
The canonical low-degree/contact-core bound gives
\[
e\ge2(v-q),
\tag{103.2}
\]
hence
\[
\boxed{
0\le
b_\infty+\sum_F(m_F-4)
\le4(q-c)
\le4\pi D.
}
\tag{103.3}
\]

Thus the **total nonquadrilateral facial excess plus the entire outer boundary walk
is boundary-order**.

## 103.2 Strict-rattler cage inequality

Consider a simple convex equilateral bounded face \(F\) of the fixed core with
\(m_F\) unit edges, containing \(k_F\) strict contact-isolated points of the hybrid
configuration. Finite Oler applied to the \(m_F\) boundary vertices together with
the \(k_F\) interior rattlers gives
\[
\boxed{
k_F
\le
\frac{
\operatorname{area}(F)-c_0(m_F-2)
}{a_0}.
}
\tag{103.4}
\]

Consequently a unit rhombus carries no strict rattler, and
\[
\boxed{
k_F\ge1\Longrightarrow m_F\ge7.
}
\tag{103.5}
\]

For the family \(\mathcal F_R\) of such rattler-bearing bounded faces,
(103.3) and \(m_F\ge7\) give
\[
\boxed{
\sum_{F\in\mathcal F_R}m_F
\le
\frac{28}{3}(q-c)
\le
\frac{28\pi}{3}D.
}
\tag{103.6}
\]

If
\[
\rho_b=\sum_{F\in\mathcal F_R}k_F
\tag{103.7}
\]
and \(M=\max_{F\in\mathcal F_R}m_F\), isoperimetry gives
\[
k_F
<
\frac{m_F^2}{2\pi\sqrt3}.
\tag{103.8}
\]
Therefore
\[
\boxed{
M
>
\frac{3\pi\sqrt3}{14(q-c)}\rho_b
\ge
\frac{3\sqrt3}{14}\frac{\rho_b}{D}.
}
\tag{103.9}
\]

Hence a super-boundary bounded-face rattler population forces an actual source cage
whose unit-contact perimeter tends to infinity.

## 103.3 Long low-degree boundary run

Let \(\alpha_i\) be the interior angles of a convex equilateral \(M\)-gon source
cage. Unit separation and triangle-freeness imply
\[
\alpha_i>\frac{\pi}{3}.
\tag{103.10}
\]
At most five vertices can satisfy
\[
\alpha_i<\frac{2\pi}{3},
\tag{103.11}
\]
because the exterior turns \(\pi-\alpha_i\) sum to \(2\pi\).

Therefore some consecutive run has length at least
\[
\boxed{
L_{120}\ge\frac{M-5}{5}.
}
\tag{103.12}
\]
Every vertex on such a run has total contact degree at most four. Combining with
(103.9),
\[
\boxed{
L_{120}
>
\frac{3\sqrt3}{70}\frac{\rho_b}{D}-1.
}
\tag{103.13}
\]

This is an actual ordered run in the source core. It is **not** automatically a
Schürmann loose edge or a Ferrers strip.

## 103.4 Latent forest confinement

The bridge forest survives inside the same hybrid representative. After
rattlerization, choose the deformation sufficiently small that every opened former
forest edge has length \(<\sqrt3\).

> **Lemma 103.1 (unit-edge crossing barrier).**
> Let \(ab\) be a unit segment. Suppose a segment \(pq\) crosses the relative interior
> of \(ab\), while
> \[
> |p-a|,|p-b|,|q-a|,|q-b|\ge1.
> \]
> Then
> \[
> \boxed{|p-q|\ge\sqrt3.}
> \tag{103.14}
> \]

### Proof

The closed \(\sqrt3/2\)-tube around the unit segment \([a,b]\) lies in
\[
\overline B(a,1)\cup\overline B(b,1).
\tag{103.15}
\]
If the orthogonal projection lies inside \([a,b]\), one endpoint is horizontally at
distance at most \(1/2\), giving squared distance at most
\[
\frac14+\frac34=1.
\tag{103.16}
\]
Outside the segment, the nearest endpoint is still no farther than the distance to
the segment.

A crossing segment with endpoints outside both unit disks must traverse this tube
from one side to the other, a distance at least \(\sqrt3\). \(\square\)

Hence no latent opened forest edge can cross a fixed unit edge of the core:
\[
\boxed{
\text{the latent forest is trapped face-by-face in the fixed core embedding.}
}
\tag{103.17}
\]

This source-specific topological fact is not present in the independent scaffold.

## 103.5 Thermodynamic cage normal form

After same-diameter saturation, retain the original strict rattlers. The global
clearance theorem gives
\[
\sum_p\delta(p)=O(D),
\tag{103.18}
\]
and the global deep Delaunay excess is \(O(D)\).

For a regular rattler-bearing bounded face \(F\), let

- \(L_F\) be the total clearance of its retained rattlers;
- \(E_F\) be the Delaunay excess of deep Delaunay triangles contained in the face;
- \(r_F\) be the number of latent rooted-forest components represented in the face.

The total sums of \(m_F\), \(L_F\), \(E_F\), and \(r_F\) over the regular bounded-face
branch are \(O(D)\). Therefore, if that branch contains
\[
\rho_b=\omega(D)
\tag{103.19}
\]
retained rattlers, some face \(F\) with \(k_F\to\infty\) satisfies
\[
\boxed{
\frac{m_F+L_F+E_F+r_F}{k_F}\to0.
}
\tag{103.20}
\]

Consequently
\[
m_F=o(k_F),
\qquad
L_F=o(k_F),
\qquad
E_F=o(k_F),
\qquad
r_F=o(k_F).
\tag{103.21}
\]

The localized boundary-layer estimate gives only \(o(k_F)\) rattlers within distance
one of \(\partial F\). The degree-six nearest-neighbor argument therefore produces
\[
\boxed{
\frac{k_F}{24}-o(k_F)
}
\tag{103.22}
\]
pairwise disjoint strong Gabriel/Delaunay edges inside the cage whose lengths are
\(1+o(1)\). Since \(E_F=o(k_F)\), both incident Delaunay triangles on all but
\(o(k_F)\) of these edges approach one of the two equality wells
\[
\boxed{
\{1,1,1\},
\qquad
\{1,1,\sqrt3\}.
}
\tag{103.23}
\]

Because \(r_F=o(k_F)\), the cage also contains a latent rooted tree with unbounded
size; finite Oler forces its graph depth to diverge at least on a square-root scale.

This is a genuine source normal form, but it is not a contradiction. Near-equilateral
triangle-free configurations may approach the equality lattice without ever forming
an exact unit triangle.

The complementary source branches -- outer-face rattlers, pinched/non-simple pockets,
or topology not covered by the regular bounded-face hypothesis -- remain separate and
must not be silently absorbed into (103.20).

---

# 104. Source lattice transversal: almost all strict rattlers are conditionally independent

There is a second exact source theorem which limits what a closing argument can hope
to extract from Hall dependence alone.

Let \(A\) be a same-diameter saturated triangle-free source minimizer of cardinality
\(N\), hull \(K\), and diameter \(D\). Let
\[
N_+:=\max\{q:D(q)=D\},
\qquad
p:=N_+-N.
\tag{104.1}
\]
The plateau theorem gives
\[
p<\frac{\pi D}{2}.
\tag{104.2}
\]

Choose a generic triangular-lattice translate and put
\[
Y=(\Lambda+v)\cap\operatorname{int}K.
\tag{104.3}
\]
Form the conflict graph on \(A\sqcup Y\). Every independent set is a unit-separated
subset of \(K\), hence has at most \(N_+\) points. Therefore
\[
N+|Y|-\nu\le N_+,
\tag{104.4}
\]
or
\[
\boxed{
\nu\ge|Y|-p.
}
\tag{104.5}
\]

Let \(M_A\) be the resulting source transversal matroid and
\[
\Delta_{\rm src}=N-|Y|.
\tag{104.6}
\]
Then
\[
n(M_A):=N-r(M_A)
\le\Delta_{\rm src}+p.
\tag{104.7}
\]

Choose the translate with more lattice points than its translation mean.
Finite Oler gives
\[
\Delta_{\rm src}
<
1+\frac{P}{2}
\le1+\frac{\pi D}{2}.
\tag{104.8}
\]
Together with (104.2),
\[
\boxed{
n(M_A)<\pi D+1.
}
\tag{104.9}
\]

Write
\[
A=B\sqcup R,
\tag{104.10}
\]
where \(R\) is the retained strict-rattler population. Define its conditional
transversal nullity over the source core:
\[
\eta_R
=
|R|-
\bigl(r_{M_A}(A)-r_{M_A}(B)\bigr).
\tag{104.11}
\]
Conditional nullity is at most total nullity, so

> **Theorem 104.1 (source almost-independence).**
> \[
> \boxed{
> 0\le\eta_R<\pi D+1.
> }
> \tag{104.12}
> \]
> Equivalently,
> \[
> \boxed{
> r_{M_A/B}(R)>\rho-\pi D-1.
> }
> \tag{104.13}
> \]

Thus a super-boundary strict-rattler population is **not** forced to create
super-boundary Hall nullity in the source lattice transversal. All but \(O(D)\)
rattlers may be independent over the source core.

This is a no-go theorem for another tempting closure route.

---

# 105. Strained-monomer regression: boundary-order strain can destroy all exact contacts

The remaining Target A theorem must detect exact global diameter optimality, not
merely local crystallinity.

Choose one open degree-three monomer chamber for the \(+\)-orientation. Fix an
interior offset \(c\) having positive distance from every chamber boundary and every
additional lattice conflict circle. For an \(L\times L\) patch \(P_L\) of lattice
indices, put
\[
p_z=z+c
\qquad(z\in P_L).
\tag{105.1}
\]
Choose a patch center \(z_0\) and define
\[
p'_z
=
z+c
+
\frac{\alpha}{L}(z-z_0),
\tag{105.2}
\]
where \(\alpha>0\) is a sufficiently small fixed constant.

The displacement from \(p_z\) is \(O(\alpha)\), uniformly in \(L\). Choosing
\(\alpha\) below the chamber margin keeps every \(p'_z\) in the **same degree-three
monomer chamber** and therefore preserves the exact monomer scaffold combinatorics.

For every pair \(z,w\),
\[
p'_z-p'_w
=
\left(1+\frac{\alpha}{L}\right)(z-w).
\tag{105.3}
\]
In particular every former unit lattice-neighbor distance becomes
\[
\boxed{
1+\frac{\alpha}{L}>1.
}
\tag{105.4}
\]
All other separations increase as well. Hence the entire patch is contact-free and
therefore triangle-free.

There are \(\Theta(L^2)\) points, while the total nearest-neighbor clearance is
\[
\boxed{
\Theta(L^2)\frac{\alpha}{L}
=
\Theta(L).
}
\tag{105.5}
\]

> **Regression 105.1 (distributed infinitesimal strain).**
> A \(D^2\)-scale triangle-free strict-rattler phase can retain exact zero-charge
> monomer scaffold combinatorics while paying only boundary-order total clearance.

The construction is not asserted to be globally diameter-optimal. Its purpose is to
kill the inference that triangle-freeness, strict-rattler status, near-triangular
bulk, or monomer phase purity automatically costs positive bulk defect.

Any closing theorem must use the global diameter boundary or an equivalent exact
optimality invariant.

---

# 106. Authoritative v1.5.0 Target A frontier

All audited Target A reductions now point to the same one-integer obstruction.

The original exact equivalence remains
\[
\boxed{
h(G)-j=d_{\rm sc}-\Delta_\Lambda.
}
\tag{106.1}
\]
Thus Target A closes exactly when
\[
\boxed{d_{\rm sc}\ge\Delta_\Lambda}
\tag{106.2}
\]
or equivalently
\[
\boxed{h(G)\ge j.}
\tag{106.3}
\]

The preferred structural forms are now much sharper.

## 106.1 Nullity-zero residual form

The full fixed-basis tight core can be contracted, leaving a fully matchable residual
with
\[
\boxed{
g=\Delta_\Lambda-d_{\rm sc}.
}
\tag{106.4}
\]
A survivor has \(g\ge1\).

A sufficient closing theorem is therefore:

> **Nullity-zero global phase-rigidity theorem.**
> A nullity-zero residual obtained by the globally derived Target A scaffold cannot
> have \(g\ge1\); global optimality forces \(g\le0\) or a strict diameter decrease.

This is not a statement about arbitrary nullity-zero monomer--dimer complexes.

## 106.2 Phase-gammoid form

After contracting all dimers and either monomer orientation,
\[
\boxed{
d_{\rm sc}=m_- -\lambda_+=m_+-\lambda_-.
}
\tag{106.5}
\]
The six anchor presentations give exact absolute-contour formulas. A sufficient
closing theorem is
\[
\boxed{
m_- -\lambda_+\ge\Delta_\Lambda.
}
\tag{106.6}
\]

Planarity and the six height orders alone do not imply this.

## 106.3 Plateau-boundary form

After right-endpoint terminalization of the smaller optimum,
\[
\boxed{
d_{\rm sc}
=
d_{\rm int}+s_\partial-\lambda_\partial.
}
\tag{106.7}
\]
Thus, if \(d_{\rm int}<\Delta_\Lambda\), the exact boundary lemma is
\[
\boxed{
s_\partial-\lambda_\partial
\ge
\Delta_\Lambda-d_{\rm int}.
}
\tag{106.8}
\]

## 106.4 Phase-pure boundary-minor form

For either phase,
\[
\boxed{
d_{\rm sc}
=
d_{\rm int}
+\theta_+
+d_{\partial,-}^{(+)}
}
\tag{106.9}
\]
and symmetrically. The exact required inequality is
\[
\boxed{
\theta_+
+d_{\partial,-}^{(+)}
\ge
\Delta_\Lambda-d_{\rm int}.
}
\tag{106.10}
\]

The quotient has only \(O(D)\) ground elements and only one orientation of boundary
monomers as possibly nonloop residual elements.

## 106.5 Boundary-response form -- preferred endpoint

The Schur response is the cleanest exact endpoint:
\[
\boxed{
d_{\rm sc}
=
d_{\rm int}+|C^\partial|-\operatorname{rank}S.
}
\tag{106.11}
\]
Therefore Target A is exactly:

> **Target A v1.5.0 (source-specific boundary-response theorem).**
> For the plateau-terminalized scaffold extracted from a genuine super-boundary
> triangle-free global minimizer,
> \[
> \boxed{
> \operatorname{rank}S
> \le
> d_{\rm int}+|C^\partial|-\Delta_\Lambda.
> }
> \tag{106.12}
> \]

Equivalently,
\[
\boxed{
|O|-\operatorname{rank}S\ge j.
}
\tag{106.13}
\]

## 106.6 Why the theorem must be source-specific

The independent smaller optimum and scaffold exist for arbitrary pairs of diameter
optima. In a surviving Target A configuration, global \(N\)-optimality itself gives
\[
d_{\rm sc}\le\Delta_\Lambda-1.
\tag{106.14}
\]
Therefore no theorem depending only on the smaller optimum, plateau saturation,
Delaunay wells, phase contraction, boundary planarity, or Schur algebra can prove
(106.12).

The extra input must come from the original triangle-free source minimizer.

The source information now available is:

1. a super-boundary population of mutually independent strict rattlers;
2. an unchanged jammed contact-minimal backbone inside the hybrid representative;
3. exact facial-defect budget (103.3);
4. strict-rattler cage capacity (103.4);
5. latent-forest face confinement (103.17);
6. thermodynamic near-triangular cage structure in the regular bounded-face branch;
7. source lattice almost-independence (104.12);
8. the global KKT contact/diameter equilibrium stress and exact diameter boundary.

Items 1--7 still do not close the theorem. Regression 105.1 shows why purely local
bulk cost cannot.

## 106.7 The actual missing mechanism

The best current formulation is:

> **Boundary-to-bulk first-variation theorem.**
> Suppose a triangle-free global minimizer has the Target A source structure and a
> super-boundary strict-rattler population. The bulk may realize an
> \(O(1/D)\)-scale expansive strain with only \(O(D)\) total clearance/area defect.
> Prove that the exact minimum-diameter boundary cannot support such a strain:
> either
> 
> 1. there is a strict same-cardinality diameter-decreasing deformation; or
> 2. the source structure forces at least
>    \(\Delta_\Lambda\) units of scaffold nullity, equivalently the Schur-response
>    rank loss (106.12).

This theorem is not proved.

A closing proof should now focus on coupling the source strain to the exact active
diameter/KKT boundary, or on converting source-specific structure into a vanishing
family of response minors. It should not return to local phase-charge counting.

---

# 107. Authoritative v1.5.0 Target B frontier

No post-v1.4.1 result in this continuation changes the pure Target B endpoint.

The required exact theorem remains
\[
\boxed{
\operatorname{rank}\overline{\mathcal B}_\xi+I+r
\le T-q-r_\alpha,
}
\tag{107.1}
\]
followed by exact topology-corrected transport.

The component classification remains:

1. \(s_C=0\): atomic one-edge unit segment, strictly forward for every active bar;
2. \(s_C=1\), tree: exactly two directions, at most nine trains, with residual
   active-bar-average obstruction \(\mathcal A_{1\rm t}\);
3. \(s_C=1\), cyclic: exactly two directions and, under the audited cyclic order
   hypotheses, the legitimate Ferrers/two-family class;
4. \(s_C=2\): genuine two-dimensional turning component.

The next tree-specific theorem remains an exact charge of
\[
\operatorname{rank}\mathcal A_{1\rm t}
\tag{107.2}
\]
to terminal coforest/cycle data or the existing \(I+r\) budget.

No uncontrolled \(O(D)\) loss is acceptable in the final topology transport.

---

# 108. v1.5.0 regressions, rejected shortcuts, and exact status

All earlier regressions remain binding. Add the following v1.5.0 tests.

1. **Fixed-basis overlap is signed-additive, not spatially additive.** Fundamental
   circuits relative to one maximum basis have exact signed deficiency additivity,
   but their supports may overlap almost completely.
2. **Arbitrary phase contraction remains invalid.** Only the exact fixed-basis and
   phase-selective contractions proved above may be used without further rank proof.
3. **Residual optimality is not inherited.** A residual after contraction/deletion is
   not automatically a global optimum for its new cardinality.
4. **Boundary terminals do not imply boundary routing.** Alternating paths may still
   traverse the quadratic bulk.
5. **Planar annular networks can have full linkage rank.** Planarity alone cannot
   prove the boundary deficit.
6. **Near-equilateral equality remains live.** Triangle-free configurations may
   converge to the \(\{1,1,1\}\) well.
7. **Strained monomer patch.** A \(D^2\)-scale exact monomer scaffold phase can be
   made contact-free and triangle-free with only \(O(D)\) total clearance.
8. **Source rattlers need not create bulk Hall nullity.** Their conditional source
   transversal nullity can be only \(O(D)\).
9. **Long obtuse source runs are not automatically Schürmann loose edges.**
10. **Contact-minimal/maximal-contact normal forms are not interchangeable.** Use the
    hybrid theorem when transporting the unchanged jammed backbone into the flexible
    representative.

The following shortcuts are explicitly rejected unless separately proved:

- a fixed positive defect per triangle-free monomer cell;
- a fixed positive defect per strict rattler;
- asymptotic convergence to triangular lattice as a contradiction;
- use of phase-anchor DAGs as though the boundary-terminal matching had the same
  anchor orientation automatically;
- a width-one-annulus gammoid without a rank-preserving terminalization theorem;
- a claim that all response routing lies near \(\partial K\);
- recursively applying optimum-only theorems to contracted residual configurations;
- treating the source and independent smaller optimum as coordinate-identified;
- replacing exact Schur rank loss by an \(O(D)\) separator estimate; or
- invoking Schürmann without an actual polygon satisfying the precise loose-edge and
  obtuse-vertex hypotheses.

## 108.1 Exact status

**LEVEL I STATUS: STILL OPEN.**

Target A has been reduced to the source-specific boundary-response/first-variation
theorem (106.12). The quadratic scaffold bulk, dimer population, one complete
monomer phase, deep matching obstruction, and most circuit-overlap ambiguity can all
be removed exactly. The remaining rank object is boundary-order.

Target B remains (107.1) plus exact topology transport.

A Level I affirmative proof still requires closing **both** Target A and Target B.

## 108.2 Version history through v1.5.0

- **v1.0.0:** global KKT/stress, almost-rhombic and hybrid normal forms,
  translated-lattice and higher-order blocker machinery;
- **v1.1.0:** minimal-face harmonic transport, terminal direction network, exact
  plateau theorem;
- **v1.2.0:** rooted-forest exactification, affine triangle-factor exclusion,
  rattlerization, saturation, terminal Minkowski splitting;
- **v1.3.0:** compatible collar, clearance budget, strong Delaunay matching,
  two-well theorem, exact Hall scaffold;
- **v1.4.0:** exact monomer--dimer blocker complex and Target B component-rotation
  refinements;
- **v1.4.1:** dual Hall/lattice deficit, exact phase charge and peeling,
  transversal-matroid circuits, bounded `s_C=1` trees;
- **v1.5.0:** fixed-basis tight-core contraction, phase-selective exact contraction,
  six planar gammoid presentations, plateau interior terminalization,
  phase-pure \(O(D)\) boundary minors, quantized Hall-core convexification,
  exact boundary Schur response, source facial/forest localization,
  source transversal almost-independence, and the distributed-strain regression.

`erdos_problem_99_1.5.0.md` was the sole canonical theorem-state file at the v1.5.0
stage. Sections 109 onward and the v1.5.1 audit policy supersede its corrected frontier.
---

# 109. v1.5.1 audit corrections, restored identities, and source-localization repair

This section is the authoritative audit patch to Sections 97--108.  It records the
results of a full post-build audit of v1.5.0.  Unless explicitly corrected below, the
mathematics of Sections 97--102 survives unchanged.  The corrections are concentrated
in the source-localization layer of Section 103, one overstrong phrase in Regression
105.1, and two exact supporting identities that v1.5.0 inadvertently omitted.

## 109.1 Audit classification of Sections 97--102

The following v1.5.0 results survive re-derivation without correction:

1. The fixed-basis tight-union theorem (97.3)--(97.14).
2. The full tight-core contraction and exact residual gap
   \[
   g=\Delta_\Lambda-d_{\rm sc}.
   \]
3. The boundary-order estimates (97.28)--(97.32).
4. Phase-selective independence and exact nullity preservation (98.7)--(98.14).
5. The six phase-anchor layered DAG presentations and the directed Menger/contour
   formulas (98.17)--(98.21).
6. Right-endpoint plateau saturation, the exact interior matching
   \[
   \nu(G_0)=|Z|,
   \]
   and the deep-nullity/boundary-linkage split (99.14)--(99.26).
7. The two-sided plateau endpoint normalization (99.27)--(99.33).
8. The phase-pure boundary-minor decomposition (100.13)--(100.15).
9. The exterior degree/interface theorem (100.16)--(100.23).
10. The quantized convexification-gap theorem and the circuit bounds
    \[
    m_3\ge14,\qquad m_+\ge6,\qquad m_-\ge6.
    \]
11. The Schur response theorem (102.9)--(102.12) and the two-phase matroid
    connectivity interpretation (102.14)--(102.19).

The generic incidence matrix in Section 102 is understood over the rational-function
field generated by algebraically independent nonzero edge variables.  With that
convention, generic matrix rank equals transversal-matroid rank, and a Schur minor is
nonzero exactly when the corresponding square conflict submatrix has a perfect
matching.

## 109.2 Explicit outer-terminal population bound

Section 99 correctly states that the physical terminal populations are boundary-order,
but v1.5.0 omitted the explicit proof for the outer lattice set
\[
O=(\Lambda+v)\cap\bigl(\operatorname{int}(K+\mathbb B)\setminus K\bigr).
\]
Restore it as follows.

Let
\[
r_\Lambda=\frac1{\sqrt3}.
\]
The triangular-lattice Voronoi cells centered at the points of \(O\) are disjoint,
have area \(a_0\), lie in \(K+(1+r_\Lambda)\mathbb B\), and are disjoint from
\(K\ominus r_\Lambda\mathbb B\).  The elementary inner-tube inequality for a convex
body gives
\[
\operatorname{area}(K\ominus r\mathbb B)
\ge
\operatorname{area}(K)-rP;
\]
if the right side is negative this is simply trivial.  Hence
\[
\begin{aligned}
a_0|O|
&\le
\operatorname{area}(K+(1+r_\Lambda)\mathbb B)
-
\operatorname{area}(K\ominus r_\Lambda\mathbb B)\\
&\le
(1+2r_\Lambda)P+\pi(1+r_\Lambda)^2.
\end{aligned}
\]
Therefore
\[
\boxed{
|O|
\le
\frac{(1+2/\sqrt3)P+\pi(1+1/\sqrt3)^2}{a_0}
\le
7.816389\ldots\, d+9.025589\ldots
<12d+10.
}
\tag{109.1}
\]
Thus the Schur response really is \(O(D)\)-by-\(O(D)\), with an explicit row bound
rather than only a qualitative assertion.

## 109.3 Restored general biphasic Hall-core bounds

The stronger circuit theorem in Section 101 supersedes the old circuit constants, but
v1.5.0 inadvertently dropped a useful exact statement for arbitrary connected positive
Hall cores.

Let such a core have deficiency \(r>0\), \(q\) holes, boundary length \(b\), and
monomer counts \(m_+,m_-\).  Then
\[
m_++m_-=b+2r+2-2q,
\]
while every boundary component has at least three elementary lattice edges, so
\[
b\ge3(q+1).
\]
The orientation side count gives
\[
3(m_+-m_-)=b_+-b_-,
\qquad
|m_+-m_-|\le\frac b3.
\]
Consequently
\[
\boxed{m_+\ge r+2,\qquad m_-\ge r+2}
\tag{109.2}
\]
and
\[
\boxed{m_3=m_++m_-\ge2r+q+5.}
\tag{109.3}
\]
These are exact integer bounds and require no circuit decomposition.

## 109.4 Restored two-sided finite-packing-defect identity

The continuation prompt in v1.5.0 retained two-sided plateau defect transfer as a
research route but the canonical state omitted the exact scalar identity that makes
that route meaningful.

Use the two-sided normalization of Section 99.4.  Thus
\[
N_-=\min\{q:D(q)=D\},
\qquad
m_+=\max\{q:D(q)=d\},
\]
\[
\rho^\dagger=N_--m_+,
\qquad
t=\frac{D-d}{2},
\]
and let \(K\) be an \(m_+\)-point optimum of diameter \(d\), with perimeter \(P\) and
perimeter deficit
\[
\varepsilon^*=\pi d-P.
\]
Recall
\[
E(n)=\frac{D(n)^2}{c}+\frac{\pi D(n)}2-(n-1).
\]
Then subtraction of the two exact cardinality identities gives
\[
\boxed{
\rho^\dagger
=
\frac{D^2-d^2}{c}
+\pi t
+E(m_+)-E(N_-).
}
\tag{109.4}
\]

Let
\[
\Omega=(K+t\mathbb B)\setminus(K+\mathbb B)
\]
and define the translation-average residual after the safe collar by
\[
J_{\rm av}:=\rho^\dagger-\frac{\operatorname{area}(\Omega)}{a_0}.
\]
The normalized area of the physical unit exterior band is
\[
B_{\rm av}:=\frac{P+\pi}{a_0}.
\]
Steiner's formula gives
\[
\frac{\operatorname{area}(\Omega)}{a_0}
=
\frac{D^2-d^2}{c}
-
\frac{\pi(d+1)+\varepsilon^*(t-1)}{a_0}.
\]
Combining with (109.4) yields the exact transfer identity
\[
\boxed{
J_{\rm av}-B_{\rm av}
=
\pi t
+\frac{\varepsilon^*t}{a_0}
+E(m_+)-E(N_-).
}
\tag{109.5}
\]
Moreover, if
\[
p_N=N-N_-,\qquad p_m=m_+-m,
\]
then
\[
\boxed{
E(m_+)-E(N_-)
=
E(m)-E(N)-p_m-p_N.
}
\tag{109.6}
\]
The endpoint normalization therefore spends the full available plateau length
\(p_N+p_m\) against the finite-packing defect transfer.  The sign of (109.5) remains
uncontrolled; this is an identity, not a Target A closure.

## 109.5 Correction to latent-forest confinement

Lemma 103.1 is valid, but the sentence following it was too strong.  A one-root tree
whose fixed root is a core vertex can have different branches entering different faces
incident to that root without any edge crossing a core edge.  The correct theorem is
branchwise.

> **Lemma 109.1 (branchwise core-face confinement).**
> Choose the forest rattlerization sufficiently small that every opened former forest
> edge has length less than \(\sqrt3\).  No such edge crosses the relative interior of a
> fixed unit core edge.  Consequently every moving branch obtained after deleting its
> fixed core root is contained in one complementary face of the fixed core.  A one-root
> component whose root does not lie on the core is contained in one face.  A component
> rooted at a core vertex may meet several incident faces, but at most five.

The crossing estimate remains
\[
|pq|\ge\sqrt3
\]
for an edge \(pq\) crossing a unit core edge \(ab\) while all four endpoint distances
to \(a,b\) are at least one.  A rigorous short proof is: if \(x=pq\cap ab\), then the
closed disk \(\overline B(x,\sqrt3/2)\) is contained in the \(\sqrt3/2\)-stadium of
\([a,b]\), and that stadium is contained in
\(\overline B(a,1)\cup\overline B(b,1)\).  Since \(p,q\) lie outside both unit disks and
\(x\in[p,q]\), the line through \(p,q\) must traverse a chord of
\(\overline B(x,\sqrt3/2)\) of length \(\sqrt3\); hence \(|pq|\ge\sqrt3\).

The post-root-skeleton forest has exactly
\[
r+b
\]
one-root components, because the original \(c\) components are cut along
\(r+b-c\) skeleton paths.  Since
\[
b\le r-c,
\qquad
r\le\pi D,
\]
\[
\boxed{
\#\{\text{one-root components}\}
=r+b
\le2r-c
\le2\pi D.
}
\tag{109.7}
\]
Every component not rooted on the core contributes to one face; a core-rooted
component contributes to at most five face incidences.  Therefore the total number of
regular bounded-face component incidences is at most
\[
\boxed{10\pi D.}
\tag{109.8}
\]
This supplies the previously implicit \(O(D)\) justification for the \(r_F\) term in
Section 103.5.

## 109.6 Corrected thermodynamic-cage theorem

Retain only the branch in which a super-boundary number of the **forest-rattlerized
vertices** lies in simple convex bounded faces of the fixed core.  For such a face
\(F\), let

- \(k_F\) be its number of retained forest rattlers;
- \(m_F\) its unit-contact boundary length;
- \(L_F\) the sum of their nearest-neighbor clearances after same-diameter saturation;
- \(E_F\) the deep Delaunay excess of triangles contained in \(F\), in a Delaunay
  triangulation containing the fixed unit core edges; and
- \(r_F\) the number of one-root component--face incidences in \(F\).

The fixed unit core edges are strong Gabriel edges, so they may be included
simultaneously in the Delaunay triangulation and the triangulation respects every
simple core-face boundary.  Equations (103.6), the global clearance/excess budgets,
and (109.8) give
\[
\sum_F(m_F+L_F+E_F+r_F)=O(D).
\]
If
\[
\sum_F k_F=\omega(D),
\]
a weighted-average argument gives a face with \(k_F\to\infty\) and
\[
\boxed{
\frac{m_F+L_F+E_F+r_F}{k_F}\to0.
}
\tag{109.9}
\]

To localize the nearest-neighbor argument correctly, choose
\[
\epsilon_F
=
\max\left\{
\sqrt{L_F/k_F},\ k_F^{-1/4}
\right\}
\longrightarrow0.
\]
Only \(o(k_F)\) rattlers have clearance greater than \(\epsilon_F\).  The disjoint
radius-\(1/2\) disks around rattlers within distance \(1+\epsilon_F\) of
\(\partial F\) lie in a radius \(3/2+\epsilon_F\) tube around the polygonal boundary,
so their number is
\[
O(m_F)+O(1)=o(k_F).
\]
Every remaining selected rattler has a nearest neighbor at distance
\(\le1+\epsilon_F\) that still lies inside \(F\).  The degree-six/maximal-matching
argument therefore gives
\[
\boxed{
|M_F|\ge\frac{k_F}{24}-o(k_F).
}
\tag{109.10}
\]
All these matching edges are strong Gabriel edges and their two incident Delaunay
triangles lie in \(F\).  Since \(E_F=o(k_F)\), all but \(o(k_F)\) of them have both
incident triangles converging to
\[
\{1,1,1\}
\qquad\text{or}\qquad
\{1,1,\sqrt3\}.
\]
Finally, (109.9) and the fact that the \(k_F\) selected vertices are forest rattlers
imply that one represented forest branch/tree has unbounded population.  Because every
latent edge has uniformly bounded length, finite Oler in a disk gives graph depth
\(\Omega(\sqrt s)\) for a tree of \(s\) moving vertices.

Thus the thermodynamic-cage normal form survives, but only with the corrected
branchwise confinement and component-incidence bookkeeping above.  Outer-face,
non-simple, and pinched/topological source branches remain separate.

## 109.7 Correction to Regression 105.1

The strained-monomer construction itself is valid: the finite patch is contact-free,
triangle-free, remains in the same monomer chambers, and has only boundary-order total
nearest-neighbor clearance.  The phrase "strict-rattler phase" in (105.1) was too
strong if the patch is considered by itself, because some patch points realize its own
diameter.

The safe canonical wording is:

> **Regression 109.2 (distributed infinitesimal monomer strain).**  A
> \(\Theta(L^2)\)-point triangle-free contact-free patch can retain the exact local
> same-orientation monomer scaffold combinatorics while paying only \(\Theta(L)\) total
> nearest-neighbor clearance.  If desired, it can be placed strictly inside a larger
> fixed frame of diameter \(\Theta(L)\), making the patch vertices non-diametral, but
> no global optimality is claimed.

Also, "zero-charge monomer phase" refers to the local interior incidence phase
\((p,q)=(3,0)\); a finite patch still has boundary charge of boundary order.

---

# 110. v1.5.1 exact status and audit verdict

**LEVEL I STATUS: STILL OPEN.**

The full audit finds **no fatal mathematical error in the principal v1.5 Target A
reductions**.  In particular, the fixed-basis contraction, phase-selective contraction,
six DAG/contour forms, plateau interior matching, phase-pure boundary minor, quantized
Hall-core theorem, and boundary Schur response all survive.

The v1.5.0 defects were:

1. an overstrong face-by-face statement for a core-rooted latent forest;
2. an omitted proof/bound for the \(O(D)\) outer row population of the Schur response;
3. an implicit rather than proved \(O(D)\) component-incidence budget in the
   thermodynamic-cage theorem;
4. a boundary-strip localization step that needed thickness \(1+\epsilon_F\), not
   exactly one;
5. an overstrong use of the phrase "strict-rattler phase" for the standalone strained
   monomer regression; and
6. omission of the exact two-sided finite-packing-defect identity (109.5) and the
   general biphasic core bounds (109.2)--(109.3).

All six are repaired in Section 109 without changing the authoritative Target A
endpoint:
\[
\boxed{
\operatorname{rank}S
\le
d_{\rm int}+|C^\partial|-\Delta_\Lambda.
}
\tag{110.1}
\]
Equivalently,
\[
\boxed{d_{\rm sc}\ge\Delta_\Lambda}
\qquad\Longleftrightarrow\qquad
\boxed{h(G)\ge j}.
\tag{110.2}
\]

The best current research target remains the exact boundary-to-bulk first-variation /
source-to-response theorem.  The restored scalar identity (109.5) should be used when
pursuing the two-sided plateau-defect route.  Purely local monomer cost, asymptotic
triangular-lattice convergence, planar separator estimates, and unqualified
face-by-face forest confinement remain invalid shortcuts.

Target B remains unchanged:
\[
\operatorname{rank}\overline{\mathcal B}_\xi+I+r\le T-q-r_\alpha,
\]
followed by exact topology-corrected transport.

`erdos_problem_99_1.5.1.md` is the sole canonical theorem-state file for subsequent
runs.


---

# 111. v1.6.0 post-v1.5.1 audit policy

Sections 111 onward are the authoritative v1.6.0 continuation.  They preserve the
v1.5.1 theorem stack but add the exact post-v1.5.1 results that survived re-audit.
Two proposed strengthenings from intermediate runs are **not** promoted:

1. the genuine triangle-free source minimizer may not simply be replaced by an
   unrelated right endpoint of its diameter plateau; source continuum Hall statements
   therefore carry the exact plateau slack defined below unless a same-source endpoint
   extension is separately proved; and
2. no individual Voronoi cell is known to have area at least
   \(a_0=\sqrt3/2\).  Oler's hexagonal constant is an aggregate finite-packing
   inequality.  Consequently the proposed \(m_+-O(D)\) inner-parallel source count is
   not canonical.

The authoritative Target A endpoint remains
\[
\boxed{
\operatorname{rank}S
\le d_{\rm int}+|C^\partial|-\Delta_\Lambda.
}
\tag{111.1}
\]
Equivalently,
\[
\boxed{d_{\rm sc}\ge\Delta_\Lambda}
\qquad\Longleftrightarrow\qquad
\boxed{h(G)\ge j}.
\tag{111.2}
\]

---

# 112. Strict-rattler product germ and the local-KKT no-go theorem

Let
\[
A=C\sqcup R
\]
be a triangle-free global \(N\)-point minimizer of diameter \(D\), and suppose every
\(r\in R\) is a genuine strict rattler:
\[
1<|r-q|<D
\qquad(q\ne r).
\tag{112.1}
\]
Put
\[
\gamma=
\min_{\substack{r\in R\\q\ne r}}
\min\{|r-q|-1,\ D-|r-q|\}>0.
\tag{112.2}
\]

## 112.1 Exact product germ

Choose the product neighborhood sufficiently small that each point moves by less than
\(\gamma/4\), and shrink the core neighborhood further if necessary.  Every distance
involving a rattler then remains strictly in \((1,D)\).  Since every diameter pair of
\(A\) lies in \(C\), an original core diameter pair remains longer than every
rattler-involving pair.  Thus the local diameter depends only on the core coordinates.
Moreover no unit edge involving \(R\) can appear, so triangle-freeness involving a
rattler is automatic in the neighborhood.

> **Theorem 112.1 (strict-rattler product germ).**  There are neighborhoods
> \(U_C,U_R\) such that the local triangle-free diameter-\(D\) minimizer germ factors
> as
> \[
> \boxed{
> \mathcal F_D^\triangle(A)\cap(U_C\times U_R)
> =
> \bigl(\mathcal F_{D,C}^\triangle(C)\cap U_C\bigr)\times U_R,
> }
> \tag{112.3}
> \]
> and throughout this product neighborhood
> \[
> \boxed{
> \operatorname{diam}(C',R')=\operatorname{diam}(C').
> }
> \tag{112.4}
> \]

In particular \(\{C\}\times U_R\) is an open \(2|R|\)-dimensional family of
triangle-free global minimizers of diameter exactly \(D\).

## 112.2 Active-jet consequence

Every active unit edge and active diameter edge lies entirely in \(C\).  Therefore:

- every active constraint Jacobian has zero \(R\)-columns;
- every finite jet of the active constraint system has zero pure-rattler entries;
- every KKT multiplier on an \(R\)-incident inequality is zero; and
- the KKT Lagrangian Hessian has a zero \(R\)-block.

Hence a velocity supported on \(R\) has identically zero active first variation,
stress work, and active second variation.  This is stronger than merely saying that
rattlers are first-order invisible.

> **Corollary 112.2 (local-KKT no-go).**  No theorem using only finite-order local
> active KKT/stress data can transfer the \(2|R|\)-dimensional rattler freedom into the
> independent scaffold response.  Any closing argument must use a finite first
> constraint event, global cardinality optimality, or another genuinely nonlocal
> source-to-scaffold invariant.

There is also an algebraic consequence.  Any polynomial relation in the rattler
coordinates that is claimed to hold for **every** nearby global minimizer must vanish
identically on the open product germ.  This does **not** prohibit selecting a special
lower-dimensional representative satisfying an additional alignment equation; it
prohibits deriving such an equation universally from local optimality.

---

# 113. Boundary Schur response as an exact planar strict gammoid

Section 102 gives the Schur response matrix
\[
S=
A[O,C^\partial]
-A[O,B]A[Z,B]^{-1}A[Z,C^\partial],
\tag{113.1}
\]
where \(B\) is matched bijectively to the interior lattice set \(Z\).
The alternating-linkage interpretation can be sharpened to a full gammoid theorem.

Fix a matching \(\mu_0:B\to Z\).  Orient the planar bipartite conflict graph by

- every unmatched conflict edge from left to right; and
- every matching edge of \(\mu_0\) from right to left.

The free right vertices are exactly \(O\).

> **Theorem 113.1 (contracted-transversal gammoid).**  For every
> \(J\subseteq C^\partial\),
> \[
> \boxed{
> J\text{ is independent after contracting }B
> \iff
> J\text{ links by }|J|\text{ pairwise vertex-disjoint directed alternating paths}
> \text{ to distinct vertices of }O.
> }
> \tag{113.2}
> \]

Indeed, a matching of \(B\cup J\) differs from \(\mu_0\) by alternating cycles and
vertex-disjoint augmenting paths from \(J\) to right vertices unmatched by \(\mu_0\),
which are precisely \(O\).  Conversely, flipping \(\mu_0\) along such a path family
matches \(B\cup J\).

Since \(S\) represents this contraction,
\[
\boxed{
\operatorname{rank}S=\lambda_S,
}
\tag{113.3}
\]
where \(\lambda_S\) is the maximum number of pairwise vertex-disjoint directed paths
from distinct vertices of \(C^\partial\) to distinct vertices of \(O\).
The orientation does not change the trusted planar radial embedding, so this is a
planar strict gammoid.

Directed vertex-Menger therefore gives the exact cut form
\[
\boxed{
\operatorname{rank}S
=
\min\{|W|:
W\text{ meets every directed }C^\partial\!\to O\text{ path}\},
}
\tag{113.4}
\]
where terminal vertices may be used in the separator.  The trivial source cut has
size \(|C^\partial|\).

Writing
\[
\zeta:=\dim\ker S
=|C^\partial|-\operatorname{rank}S,
\tag{113.5}
\]
Target A becomes the assertion that the true minimum separator saves at least
\(\Delta_\Lambda-d_{\rm int}\) vertices relative to that trivial source cut.
Planarity alone still does not imply this saving.

---

# 114. Exact response-corrected collar identities

Use the two-sided plateau normalization
\[
N_-:=\min\{q:D(q)=D\},
\qquad
m_+:=\max\{q:D(q)=d\},
\tag{114.1}
\]
\[
\rho^\dagger=N_--m_+,
\qquad
t=\frac{D-d}{2}>1.
\tag{114.2}
\]
Let \(K\) be the hull of the independent \(m_+\)-point optimum.  For a generic
triangular-lattice translate put
\[
Z=(\Lambda+v)\cap\operatorname{int}K,
\tag{114.3}
\]
\[
O=(\Lambda+v)\cap
\bigl(\operatorname{int}(K+\mathbb B)\setminus K\bigr),
\tag{114.4}
\]
\[
Y_0=(\Lambda+v)\cap
\bigl(\operatorname{int}(K+t\mathbb B)\setminus(K+\mathbb B)\bigr),
\tag{114.5}
\]
and
\[
\Gamma_t=O\sqcup Y_0.
\tag{114.6}
\]

Because
\[
\nu(G)=|Z|+\operatorname{rank}S,
\]
direct subtraction yields

> **Theorem 114.1 (response-corrected collar identity).**
> Define
> \[
> \Phi(v):=|\Gamma_t(v)|-\operatorname{rank}S(v).
> \tag{114.7}
> \]
> Then
> \[
> \boxed{
> d_{\rm sc}(v)-\Delta_\Lambda(v)
> =\Phi(v)-\rho^\dagger.
> }
> \tag{114.8}
> \]
> Equivalently,
> \[
> \boxed{
> \Phi(v)=|Y_0(v)|+h(G_v).
> }
> \tag{114.9}
> \]

Thus Target A is exactly the existence of an admissible generic translate satisfying
\[
\boxed{\Phi(v)\ge\rho^\dagger.}
\tag{114.10}
\]
A surviving counterexample has the pointwise integer inequality
\[
\boxed{\Phi(v)\le\rho^\dagger-1}
\tag{114.11}
\]
for every admissible generic translate.

## 114.1 Translation average

Let
\[
\overline r_S
=\frac1{a_0}\int_F\operatorname{rank}S(v)\,dv
\tag{114.12}
\]
over one lattice fundamental cell \(F\), normalized so \(\operatorname{area}F=a_0\).
Translation averaging gives
\[
\boxed{
\overline\Phi
=\frac{Pt+\pi t^2}{a_0}-\overline r_S.
}
\tag{114.13}
\]
If
\[
g(v):=\Delta_\Lambda(v)-d_{\rm sc}(v)=\rho^\dagger-\Phi(v),
\tag{114.14}
\]
then
\[
\boxed{
\overline g
=\rho^\dagger-\frac{Pt+\pi t^2}{a_0}+\overline r_S.
}
\tag{114.15}
\]

Let
\[
J_{\rm av}:=\rho^\dagger-
\frac{\operatorname{area}((K+t\mathbb B)\setminus(K+\mathbb B))}{a_0},
\tag{114.16}
\]
\[
B_{\rm av}:=\frac{P+\pi}{a_0}.
\tag{114.17}
\]
Then
\[
\boxed{
\overline g=J_{\rm av}-B_{\rm av}+\overline r_S.
}
\tag{114.18}
\]
A survivor therefore necessarily satisfies
\[
\boxed{
\overline r_S\ge1-(J_{\rm av}-B_{\rm av}).
}
\tag{114.19}
\]
This is necessary, not contradictory.

## 114.2 Scalar plateau defect in its shortest form

Define
\[
q_r:=r-1-\frac{D(r)^2}{c}.
\tag{114.20}
\]
The strict translated-lattice theorem and finite Oler give
\[
0<q_r\le\frac{\pi D(r)}2.
\tag{114.21}
\]
Exact subtraction gives
\[
\boxed{
\rho^\dagger
=\frac{D^2-d^2}{c}+q_{N_-}-q_{m_+}.
}
\tag{114.22}
\]
Writing
\[
\varepsilon^*=\pi d-P,
\tag{114.23}
\]
Steiner's formula gives the particularly clean transfer identity
\[
\boxed{
J_{\rm av}-B_{\rm av}
=\frac{\varepsilon^*t}{a_0}+q_{N_-}-q_{m_+}.
}
\tag{114.24}
\]
Equivalently, with
\[
E(n)=\frac{D(n)^2}{c}+\frac{\pi D(n)}2-(n-1),
\]
this is the restored v1.5.1 identity
\[
J_{\rm av}-B_{\rm av}
=\pi t+\frac{\varepsilon^*t}{a_0}+E(m_+)-E(N_-).
\tag{114.25}
\]
The sign remains uncontrolled at boundary order.

## 114.3 Minimal kernel certificate

Put
\[
s:=\Delta_\Lambda-d_{\rm int}.
\tag{114.26}
\]
If \(s\le0\), Target A is already closed.  For \(s>0\), the desired response
inequality is exactly
\[
\boxed{\dim\ker S\ge s.}
\tag{114.27}
\]
Equivalently there must exist a full-rank map
\[
\boxed{
T:\mathbb F^s\longrightarrow\mathbb F^{C^\partial},
\qquad
\operatorname{rank}T=s,
\qquad
ST=0.
}
\tag{114.28}
\]
Lifting through the interior basis gives
\[
W=-A[Z,B]^{-1}A[Z,C^\partial]T,
\tag{114.29}
\]
with
\[
A[Z,B]W+A[Z,C^\partial]T=0,
\tag{114.30}
\]
\[
A[O,B]W+A[O,C^\partial]T=0.
\tag{114.31}
\]
Because the representation is generic over the rational-function field, Schur minors
are rational functions.  After multiplying by \(\det A[Z,B]\), their numerators are
the corresponding block-determinant polynomials.  A response-rank loss must therefore
come from structural absence of alternating linkages, not accidental numerical
cancellation with unrelated source-coordinate equations.

---

# 115. Continuum source Hall theorem with the exact plateau slack

Let \(A\) be the genuine triangle-free source minimizer used by Target A, with
\[
|A|=N,
\qquad
H=\operatorname{conv}A,
\qquad
\operatorname{diam}H=D.
\tag{115.1}
\]
Define the right endpoint of the \(D\)-plateau by
\[
N_+:=\max\{q:D(q)=D\},
\qquad
p:=N_+-N.
\tag{115.2}
\]
The plateau theorem gives
\[
0\le p<\frac{\pi D}{2}.
\tag{115.3}
\]

For every finite unit-separated set \(Q\subseteq H\), define its strict source
conflict neighborhood
\[
N_A(Q)
=
\{a\in A:\exists q\in Q,\ |a-q|<1\}.
\tag{115.4}
\]

> **Theorem 115.1 (continuum Hall inequality with plateau slack).**
> \[
> \boxed{
> |Q|-|N_A(Q)|\le p
> \qquad
> \text{for every finite unit-separated }Q\subseteq H.
> }
> \tag{115.5}
> \]

### Proof

The replacement set
\[
A_Q=(A\setminus N_A(Q))\cup Q
\tag{115.6}
\]
is unit-separated and lies in \(H\), hence has diameter at most \(D\).  By definition
of \(N_+\), it has at most \(N_+\) points.  Therefore
\[
N-|N_A(Q)|+|Q|\le N_+=N+p,
\]
which is exactly (115.5). \(\square\)

This is a continuum Hall theorem: the candidate replacement set need not be a lattice
translate.

## 115.1 Deletion-cavity capacity

For \(T\subseteq A\), define
\[
\mathcal U_A(T)
=
\{x\in H:|x-a|\ge1\text{ for every }a\in A\setminus T\}.
\tag{115.7}
\]
Let \(\alpha_1(U)\) be the maximum size of a unit-separated subset of \(U\).  Since
\(T\subseteq\mathcal U_A(T)\), while every unit-separated
\(Q\subseteq\mathcal U_A(T)\) has \(N_A(Q)\subseteq T\), Theorem 115.1 gives
\[
\boxed{
|T|\le\alpha_1(\mathcal U_A(T))\le|T|+p.
}
\tag{115.8}
\]
Translation averaging with the triangular lattice yields the area consequence
\[
\boxed{
\operatorname{area}\mathcal U_A(T)
\le a_0(|T|+p).
}
\tag{115.9}
\]

If one separately proves that the **same source representative** is already at the
right endpoint, so \(p=0\), then (115.8) sharpens to exact hereditary cavity
saturation
\[
\alpha_1(\mathcal U_A(T))=|T|.
\tag{115.10}
\]
In that special case singleton deletion cavities have diameter \(<1\) and distinct
singleton cavities are disjoint.  These zero-slack conclusions must **not** be used for
the genuine Target A source unless \(p=0\) has actually been established without
changing the source geometry.

## 115.2 Finite-amplitude cross-matching

Let \(T\subseteq A\) and let \(T'\subset H\) be another placement of \(|T|\) points
such that
\[
(A\setminus T)\cup T'
\tag{115.11}
\]
is unit-separated.  Form the bipartite graph on \(T\sqcup T'\) with
\[
t\sim t'\iff |t-t'|<1.
\tag{115.12}
\]

> **Theorem 115.2 (cross-matching with plateau slack).**
> \[
> \boxed{
> \nu(T,T')\ge |T|-p.
> }
> \tag{115.13}
> \]

If \(\nu<|T|-p\), Kőnig gives an independent set in the bipartite graph of size
\[
2|T|-\nu>|T|+p.
\]
Adjoining this independent old/new mixture to \(A\setminus T\) produces more than
\(N+p=N_+\) unit-separated points in \(H\), a contradiction.

For \(p=0\) this becomes a perfect old/new cross-matching theorem and implies that the
feasible rigid-translation set of every source subset has diameter \(<1\).  Again,
this stronger caging corollary is conditional on a proved zero-slack source endpoint.

The source theorem therefore supplies a genuine nonlocal invariant, but with an
unavoidable \(O(D)\) plateau allowance in the current normalization.

---

# 116. Inner-parallel source capacity: exact one-sided form only

Let \(A\subset H\) be any unit-separated source configuration of diameter \(D\).  Let
\(m_+\) be the right endpoint of a smaller diameter plateau with
\[
D(m_+)=d<D,
\qquad
t=\frac{D-d}{2}.
\tag{116.1}
\]
When the inner parallel body
\[
H_t:=H\ominus t\mathbb B
\tag{116.2}
\]
is nonempty, it satisfies
\[
\boxed{\operatorname{diam}H_t\le d.}
\tag{116.3}
\]
Indeed, for \(x,y\in H_t\) and \(u=(x-y)/|x-y|\), both \(x+tu\) and \(y-tu\) lie in
\(H\), so
\[
|x-y|+2t\le w_H(u)\le D.
\]
Therefore the source points lying in \(H_t\) form a unit-separated diameter-\(d\)
packing, and hence
\[
\boxed{
|A\cap H_t|\le m_+.
}
\tag{116.4}
\]
Equivalently,
\[
\boxed{
|A\setminus H_t|\ge |A|-m_+.
}
\tag{116.5}
\]
Thus the entire cardinality drop to the smaller plateau must be physically supported
in a source boundary shell of thickness \(t\).

A stronger claim from an intermediate run asserted
\[
|A\cap H_t|\ge m_+-O(D).
\tag{116.6}
\]
That claim is **not promoted**.  Its proof assigned area at least \(a_0\) to each
individual full Voronoi cell.  The finite Oler constant \(a_0\) is an aggregate
Dirichlet-cell inequality after planar cancellation; an individual many-sided Voronoi
cell need not have area \(\ge a_0\).  No replacement argument currently recovers
(116.6) with an exact boundary-order error.

---

# 117. v1.6.0 source-to-response formulation and exact status

The post-v1.5.1 work makes the last gap more explicit but does not close it.

Write
\[
\zeta:=\dim\ker S
=|C^\partial|-\operatorname{rank}S,
\tag{117.1}
\]
\[
s:=\Delta_\Lambda-d_{\rm int}.
\tag{117.2}
\]
Then
\[
\boxed{
\Delta_\Lambda-d_{\rm sc}=s-\zeta.
}
\tag{117.3}
\]
Using the response-corrected collar,
\[
\boxed{
\Delta_\Lambda-d_{\rm sc}
=\rho^\dagger-\Phi(v).
}
\tag{117.4}
\]
Thus a survivor has the positive integer
\[
\boxed{
g:=\Delta_\Lambda-d_{\rm sc}=s-\zeta=\rho^\dagger-\Phi(v)\ge1.}
\tag{117.5}
\]

## 117.1 Authoritative Target A theorem

Target A is resolved exactly by proving
\[
\boxed{
\zeta\ge s,
}
\tag{117.6}
\]
or equivalently
\[
\boxed{
\operatorname{rank}S
\le d_{\rm int}+|C^\partial|-\Delta_\Lambda.
}
\tag{117.7}
\]

In the planar-gammoid presentation, this says that the minimum alternating
\(C^\partial\)-to-\(O\) vertex cut must save at least \(s\) vertices relative to the
trivial source cut.

## 117.2 Preferred source-exchange transfer lemma

The continuum Hall theorem supplies an exact source-side contradiction target.  Let
\[
p=N_+-N
\tag{117.8}
\]
be the source plateau slack.  A sufficient closing theorem is:

> **Source-to-response exchange theorem.**  If the scaffold survivor has
> \(g>0\), then the genuine source structure produces a finite unit-separated
> \(Q\subseteq H\) such that
> \[
> \boxed{
> |Q|-|N_A(Q)|\ge p+1.
> }
> \tag{117.9}
> \]

Equation (117.9) contradicts Theorem 115.1.  Equivalently, one may produce a source
subset and an alternative feasible placement whose old/new cross-matching loses more
than \(p\) ranks, contradicting Theorem 115.2.

No map from the Schur deficit \(g\) to such a source replacement is known.  This is
now the cleanest exact source-to-scaffold bridge.

## 117.3 Binding no-go statements

The following are now explicitly ruled out as standalone closures:

1. **Finite-order local KKT/stress transfer.**  The strict-rattler product germ has a
   zero active \(R\)-block to every finite order.
2. **Scaffold-only response algebra.**  The independent smaller optimum exists without
   the source rattlers; global \(N\)-optimality of a survivor itself forces the opposite
   one-integer inequality.
3. **Planarity alone.**  The exact response is a planar gammoid, but planar annular
   networks may have full linkage rank.
4. **Scalar plateau defect alone.**  The exact quantity
   \(\varepsilon^*t/a_0+q_{N_-}-q_{m_+}\) has uncontrolled sign at boundary order.
5. **Zero-slack source Hall without proof.**  The genuine source carries plateau slack
   \(p\) unless a same-source right-endpoint extension is separately established.
6. **Per-cell Voronoi \(a_0\) accounting.**  Oler's \(a_0\) coefficient is aggregate,
   not an individual-cell lower bound.
7. **Near-triangular or strained-monomer bulk cost.**  Regression 109.2 remains binding.
8. **Long obtuse source runs as automatic Schürmann loose edges.**  Exact Schürmann
   hypotheses are still required.

An exploratory internet literature search conducted during the v1.6 run did not
identify a published theorem that supplies (117.6) or (117.9).  No web-only statement
is incorporated as a trusted theorem here.

## 117.4 Target B

Target B is unchanged and should not be revisited until Target A is closed unless a
Target B theorem directly supplies the missing source-to-response bridge:
\[
\boxed{
\operatorname{rank}\overline{\mathcal B}_\xi+I+r
\le T-q-r_\alpha,
}
\tag{117.10}
\]
followed by exact topology-corrected transport.

## 117.5 Version history through v1.6.0

- **v1.5.1:** audited fixed-basis/phase contractions, plateau terminalization,
  phase-pure boundary minors, Schur response, source cage localization, corrected
  branchwise forest confinement, explicit outer-terminal bound, and exact two-sided
  defect transfer.
- **v1.6.0:** strict-rattler product-germ/local-KKT no-go; exact planar strict-gammoid
  completion of the Schur response; response-corrected collar capacity \(\Phi\);
  minimal kernel-map certificate; continuum source Hall and cross-matching with the
  exact plateau slack; exact inner-parallel capacity; and audit corrections rejecting
  an unjustified zero-slack source terminalization and per-Voronoi-cell \(a_0\)
  accounting.

**LEVEL I STATUS: STILL OPEN.  TARGET A REMAINS UNRESOLVED.**



`erdos_problem_99_1.6.0.md` is the sole canonical theorem-state file for subsequent
runs.

---

# 118. v1.7.0 post-v1.6 audit policy and status

Sections 118 onward are the authoritative v1.7.0 continuation.  They preserve the
full v1.6.0 theorem stack and add only post-v1.6 results that survive direct audit.

The principal change is conceptual.  The genuine source hull now carries its own
exact finite-capacity Hall theory, and that capacity can be decomposed into an
explicit flag of adjacent-cardinality global optima.  In parallel, every genuine
source has a same-cardinality capacity shadow at pointwise displacement less than
one, with an exact finite-amplitude stress identity.

The following distinctions are binding throughout this continuation.

1. The source-hull capacity slack is not assumed to vanish.
2. A maximal triangle-free source extension need not preserve the old hybrid
   contact-minimal core or bridge-forest decomposition; the scaffold must be rebuilt
   if that extension is substituted for the source.
3. Oler's coefficient a_0 is an aggregate finite-packing coefficient and is never
   assigned as a lower bound to an arbitrary individual Voronoi cell.
4. The source-capacity endpoint and its exchange flag are exact finite-container
   statements.  External results on infinite completely saturated packings are
   research templates only unless an explicit finite-container transfer is proved.
5. The exact Level I target remains the Target A Schur-rank inequality.  No theorem
   below is to be interpreted as a proof of Erdős Problem #99.

**LEVEL I STATUS: STILL OPEN.  TARGET A REMAINS UNRESOLVED.**

---

# 119. Exact source-hull capacity slack

Let A be the genuine triangle-free source minimizer used by Target A, with

\[
|A|=N,
\qquad
H=\operatorname{conv}A,
\qquad
\operatorname{diam}H=D=D(N).
\tag{119.1}
\]

Let

\[
N_+=\max\{q:D(q)=D\},
\qquad
p=N_+-N,
\tag{119.2}
\]

and define the exact unit-packing capacity of the actual source hull by

\[
\widehat N_H:=\alpha_1(H)
=\max\{|X|:X\subset H,\ |x-y|\ge1\ (x\ne y)\}.
\tag{119.3}
\]

Put

\[
\widehat p_H:=\widehat N_H-N.
\tag{119.4}
\]

> **Theorem 119.1 (source-hull capacity bound).**
> \[
> \boxed{0\le \widehat p_H\le p<\frac{\pi D}{2}.}
> \tag{119.5}
> \]

Indeed, A itself shows \(\widehat N_H\ge N\).  If \(q=\widehat N_H\), a
q-point packing in H has diameter at most D.  Monotonicity gives

\[
D=D(N)\le D(q)\le D,
\]

so \(D(q)=D\) and hence \(q\le N_+\).

For every finite unit-separated \(Q\subset H\), define

\[
N_A(Q)=\{a\in A:\exists q\in Q,\ |a-q|<1\}.
\tag{119.6}
\]

The replacement

\[
(A\setminus N_A(Q))\cup Q
\tag{119.7}
\]

is unit-separated and lies in H.  Its cardinality is therefore at most
\(\widehat N_H\).

> **Theorem 119.2 (exact same-source Hall budget).**
> \[
> \boxed{|Q|-|N_A(Q)|\le\widehat p_H}
> \qquad(Q\subset H\text{ unit-separated}).
> \tag{119.8}
> \]

Thus v1.6.0 Theorem 115.1 may be sharpened from the global plateau allowance p to
the exact capacity allowance of the genuine source hull.

## 119.1 Deletion cavities and joint source budget

For \(T\subset A\), put

\[
\mathcal U_A(T)
=
\{x\in H:|x-a|\ge1\text{ for all }a\in A\setminus T\}.
\tag{119.9}
\]

Then

\[
\boxed{
|T|\le \alpha_1(\mathcal U_A(T))\le |T|+\widehat p_H.
}
\tag{119.10}
\]

More generally, let \(T_i\subset A\), and let finite sets
\(Q_i\subset\mathcal U_A(T_i)\) be such that their union
\(Q=\bigcup_iQ_i\) is unit-separated.  Then

\[
N_A(Q)\subseteq\bigcup_iT_i
\]

and therefore

\[
\boxed{
|Q|-\left|\bigcup_iT_i\right|\le\widehat p_H.
}
\tag{119.11}
\]

The source has one global hull-capacity budget; overlapping deletion regions do not
create independent copies of that budget.

## 119.2 Cross-matching with exact source-hull slack

Let \(T\subset A\), and let \(T'\subset H\) have \(|T'|=|T|\) such that

\[
(A\setminus T)\cup T'
\]

is unit-separated.  Join \(t\in T\) to \(t'\in T'\) when \(|t-t'|<1\).
The same independent-set argument as in Theorem 115.2 gives

\[
\boxed{
\nu(T,T')\ge |T|-\widehat p_H.
}
\tag{119.12}
\]

The threshold \(\widehat p_H\), not p, is the authoritative same-source
finite-amplitude allowance.

---

# 120. Self-container tightness and boundary reserve

Assume H is full-dimensional.  Fix \(c\in\operatorname{int}H\).  Every finite set
\(X\subset\operatorname{int}H\) is contained in a strict homothetic contraction

\[
c+\lambda(H-c),
\qquad
\lambda<1.
\tag{120.1}
\]

Consequently \(\operatorname{diam}X< D\) whenever \(|X|\ge N\) would otherwise
contradict \(D(N)=D\).

> **Theorem 120.1 (source self-container theorem).**
> \[
> \boxed{\alpha_1(\operatorname{int}H)\le N-1.}
> \tag{120.2}
> \]

Hence every unit-separated \(X\subset H\) with

\[
|X|=N+k,
\qquad
k\ge1,
\]

satisfies

\[
\boxed{|X\cap\partial H|\ge k+1.}
\tag{120.3}
\]

In particular, if the source Hall replacement (119.7) has positive surplus

\[
\sigma=|Q|-|N_A(Q)|\ge1,
\]

then

\[
\boxed{
|(A\setminus N_A(Q))\cap\partial H|+|Q\cap\partial H|
\ge \sigma+1.
}
\tag{120.4}
\]

This is a boundary-reserve condition on the complete replacement.  It does not
force Q itself to meet \(\partial H\); retained source boundary vertices may supply
the reserve.

---

# 121. Maximal triangle-free extension inside the genuine source hull

Define

\[
\alpha^\triangle(H;A)
=
\max\{|B|:A\subseteq B\subseteq H,\ B\text{ unit-separated and triangle-free}\}.
\tag{121.1}
\]

Put

\[
k=\alpha^\triangle(H;A)-N
\]

and choose a maximizing extension B.  Then

\[
A\subseteq B\subseteq H,
\qquad
|B|=q=N+k,
\qquad
0\le k\le\widehat p_H.
\tag{121.2}
\]

B contains an original diameter pair of A while lying in H, so
\(\operatorname{diam}B=D\).  Monotonicity therefore gives

\[
\boxed{D(q)=D,}
\tag{121.3}
\]

and B is a triangle-free global minimizer at its new cardinality q.

Let R be any original strict-rattler set of A, meaning that every
\(r\in R\) is non-diametral in A and
\[
1<|r-a|<D
\qquad(a\in A\setminus\{r\}),
\]
and define

\[
R_B=
\{r\in R:|r-b|>1\text{ for every }b\in B\setminus\{r\}\}.
\tag{121.4}
\]

Every original rattler remains at distance strictly less than D from every new
point of B: for fixed r the convex function \(x\mapsto|r-x|\) attains its maximum
on H at an extreme point of H, every such extreme point belongs to A, and r was
originally non-diametral.

One newly added point can be at unit distance from at most five original strict
rattlers.  Six unit-distance rattlers around one new point would have six angular
gaps each at least \(\pi/3\), forcing all six gaps to equal \(\pi/3\) and hence a
unit equilateral triangle.

> **Theorem 121.1 (rattler retention under maximal triangle-free extension).**
> \[
> \boxed{|R_B|\ge |R|-5k\ge |R|-5\widehat p_H.}
> \tag{121.5}
> \]

Thus a super-boundary strict-rattler population remains super-boundary.

## 121.1 Append-maximality and unit covering

Put

\[
\mathcal F_B
=
\{x\in H:|x-b|\ge1\text{ for every }b\in B\}.
\tag{121.6}
\]

If \(x\in\mathcal F_B\), the unit-separated set \(B\cup\{x\}\) cannot remain
triangle-free.  Since B itself is triangle-free, x must complete a unit equilateral
triangle on a unit edge of B.  Hence

\[
\boxed{
\mathcal F_B
\subseteq
\{\text{equilateral apices of unit edges of }B\},
}
\tag{121.7}
\]

and in particular \(|\mathcal F_B|\le2e_1(B)\).

Moreover, if some x had \(|x-b|>1\) for all b, then adding x would create no unit
edge and therefore no triangle.  Thus

> **Corollary 121.2 (same-hull unit covering).**
> \[
> \boxed{H\subseteq\bigcup_{b\in B}\overline B(b,1).}
> \tag{121.8}
> \]

This saturation is obtained in the genuine source hull.  It does not assert that
the old contact-minimal core or hybrid bridge forest remains the contact normal form
of B.

Define the residual source-hull capacity

\[
\boxed{
\tau:=\widehat N_H-|B|=\widehat p_H-k.
}
\tag{121.9}
\]

Repeating Theorem 119.2 with B gives

\[
\boxed{|Q|-|N_B(Q)|\le\tau}
\tag{121.10}
\]

for every unit-separated \(Q\subset H\), and every feasible old/new replacement
of \(T\subset B\) satisfies

\[
\boxed{\nu(T,T')\ge |T|-\tau.}
\tag{121.11}
\]

The quantity \(\tau\) is the remaining same-hull capacity after all triangle-free
append-only capacity compatible with retaining A has been exhausted.

---

# 122. Fixed-container capacity endpoint theorem

The following statement is more general than the source normalization and is useful
independently.

Let H be any compact set of finite unit-packing capacity

\[
M=\alpha_1(H).
\]

Let \(P\subset H\) be any unit-separated q-point set and choose a capacity-maximizing
unit-separated set

\[
X_{\max}\subset H,
\qquad
|X_{\max}|=M.
\]

Form the strict conflict graph on \(P\sqcup X_{\max}\), with

\[
p\sim x\iff |p-x|<1.
\tag{122.1}
\]

Every independent set in this graph is a unit-separated subset of H, so its size is
at most M.  The whole shore \(X_{\max}\) is independent of size M.  Hence
\(\alpha(G)=M\).  Koenig's theorem gives

> **Theorem 122.1 (capacity endpoint matching).**
> \[
> \boxed{\nu(P,X_{\max})=|P|=q.}
> \tag{122.2}
> \]

Thus every smaller packing in the same container can be injected into a
capacity-maximizing packing by strict-conflict edges of length less than one.

For unit-separated \(Q\subset H\), the replacement

\[
(P\setminus N_P(Q))\cup Q
\]

has at most M points.  Taking \(Q=X_{\max}\), Theorem 122.1 shows
\(N_P(X_{\max})=P\).  Therefore:

> **Theorem 122.2 (exact fixed-container Hall slack).**
> \[
> \boxed{
> \max_{\substack{Q\subseteq H\\ Q\text{ unit-separated}}}
> \bigl(|Q|-|N_P(Q)|\bigr)
> =M-|P|.
> }
> \tag{122.3}
> \]

Applied to A this gives exact maximum Hall slack \(\widehat p_H\).  Applied to B it
gives exact maximum Hall slack \(\tau\):

\[
\boxed{
\max_Q\bigl(|Q|-|N_B(Q)|\bigr)=\tau.
}
\tag{122.4}
\]

The source capacity allowance is therefore not merely an upper bound; it is attained
by every capacity endpoint through an appropriate matching.

## 122.1 Diameter graph at a source capacity endpoint

For the normalized source B, \(|B|=q\), \(D(q)=D\), and
\(X_{\max}\subset H\) has diameter at most D.  Therefore every q-point subset
\(Y\subset X_{\max}\) satisfies

\[
\boxed{\operatorname{diam}Y=D.}
\tag{122.5}
\]

Let \(\mathcal D(X_{\max})\) be the graph whose edges join pairs at distance D.
Then

\[
\alpha(\mathcal D(X_{\max}))\le q-1,
\]

so its vertex-cover number satisfies

\[
\boxed{
\tau_{\rm VC}(\mathcal D(X_{\max}))\ge M-q+1=\tau+1.
}
\tag{122.6}
\]

Because every D-edge realizes the diameter of H, both endpoints lie on
\(\partial H\).  Consequently

\[
\boxed{|X_{\max}\cap\partial H|\ge\tau+1.}
\tag{122.7}
\]

## 122.2 Complete finite-container saturation

A capacity endpoint is completely saturated relative to H in the elementary finite
sense: for no \(r\ge1\) can r-1 of its points be removed and r new points inserted
inside H while preserving unit separation, since that would produce M+1 points in H.
This observation is exact but should not be conflated with the stronger infinite-space
notions in the saturation literature.

---

# 123. Planarity of strict conflict graphs

Let P and Q be finite, spatially disjoint, internally unit-separated point sets in the
plane.  Join \(p\in P\) to \(q\in Q\) when \(|p-q|<1\), drawing each edge as the
straight segment pq.

> **Theorem 123.1 (straight-line planarity of strict conflicts).**
> The resulting bipartite graph is planar in its straight-line drawing.

If two disjoint edges \(p_1q_1\) and \(p_2q_2\) crossed at z, then

\[
2
\le |p_1-p_2|+|q_1-q_2|
\le |p_1q_1|+|p_2q_2|
<2,
\]

contradiction.  The same metric obstruction prevents an edge from passing through an
unrelated vertex.  This supplies a genuine planar source-capacity conflict network,
but planarity alone still does not imply a Target A rank deficit.

---

# 124. Source-capacity plateau exchange flag

Return to the maximal triangle-free extension B in H.  Put

\[
|B|=q,
\qquad
M=\alpha_1(H)=q+\tau,
\]

and choose a capacity endpoint \(X\subset H\), \(|X|=M\).  Regard the strict
conflict graph as a transversal-matroid presentation on the ground set X with right
shore B.  By Theorem 122.1 its rank is q.

Choose a maximum matchable basis

\[
\mathcal B\subset X,
\qquad
|\mathcal B|=q,
\]

and write

\[
E_0=X\setminus\mathcal B,
\qquad
|E_0|=\tau.
\tag{124.1}
\]

For \(e\in E_0\), let \(C_e\subset\mathcal B\cup\{e\}\) be its fundamental circuit.
For \(A_0\subseteq E_0\), put

\[
U_{A_0}=\bigcup_{e\in A_0}C_e,
\qquad
W_{A_0}=N_B(U_{A_0}).
\tag{124.2}
\]

The fixed-basis tight-union theorem of Section 97 is a general transversal-matroid
statement and gives

\[
\boxed{|U_{A_0}|-|W_{A_0}|=|A_0|.}
\tag{124.3}
\]

Define the mixed configuration

\[
P_{A_0}=(B\setminus W_{A_0})\cup U_{A_0}.
\tag{124.4}
\]

It is unit-separated, lies in H, and has exactly q+|A_0| points.  Since
\(D(q)=D\) and \(D(\cdot)\) is nondecreasing,

> **Theorem 124.1 (source-capacity plateau exchange theorem).**
> \[
> \boxed{
> |P_{A_0}|=q+|A_0|,
> \qquad
> \operatorname{diam}P_{A_0}=D(q+|A_0|)=D.
> }
> \tag{124.5}
> \]
>
> Thus every subset of the nonbasis capacity elements produces an explicit global
> optimum at the corresponding intermediate cardinality.

In particular

\[
\boxed{D(q+r)=D\qquad(0\le r\le\tau).}
\tag{124.6}
\]

This is stronger than the scalar statement that q and M lie on the same plateau: the
intermediate global optima are coupled to one fixed source and one fixed capacity
endpoint by nested Hall-tight supports.

## 124.1 Adjacent-cardinality flag

Order

\[
E_0=\{e_1,\ldots,e_\tau\}
\]

and put

\[
U_i=\bigcup_{r\le i}C_{e_r},
\qquad
W_i=N_B(U_i),
\qquad
P_i=(B\setminus W_i)\cup U_i.
\tag{124.7}
\]

Then

\[
P_0=B,
\qquad
|P_i|=q+i,
\qquad
\operatorname{diam}P_i=D.
\tag{124.8}
\]

Let

\[
\Delta X_i=U_i\setminus U_{i-1},
\qquad
\Delta B_i=W_i\setminus W_{i-1}.
\tag{124.9}
\]

Subtracting successive deficiencies gives

\[
\boxed{|\Delta X_i|-|\Delta B_i|=1,}
\tag{124.10}
\]

and

\[
\boxed{
P_i=(P_{i-1}\setminus\Delta B_i)\cup\Delta X_i.
}
\tag{124.11}
\]

Therefore the entire residual capacity decomposes into a flag of exact net-+1
exchanges between adjacent-cardinality global optima.

## 124.2 First-triangle localization

If all \(P_i\) are triangle-free, then \(P_\tau\) is a triangle-free global optimum
at full source-hull capacity, so its same-hull capacity slack is zero.

Otherwise let j be the first index for which \(P_j\) contains a unit equilateral
triangle.  Since \(P_{j-1}\) was triangle-free and the step only deletes
\(\Delta B_j\) and inserts \(\Delta X_j\), every newly appearing triangle contains
at least one point of \(\Delta X_j\).  Thus the first triangle is localized to one
Hall-tight adjacent plateau transition satisfying

\[
\boxed{|\Delta X_j|=|\Delta B_j|+1.}
\tag{124.12}
\]

## 124.3 Rattler-loss concentration along the flag

Let \(R\subset B\) be a retained strict-rattler population of size \(\rho\).  Either
the capacity endpoint \(P_\tau\) retains at least \(\rho/2\) original rattler
positions, or more than \(\rho/2\) are removed across the \(\tau\) increments.
If \(\tau>0\), the latter case implies that some i satisfies

\[
|R\cap\Delta B_i|
\ge\frac{\rho}{2\tau}.
\]

Since \(q\) and \(M=q+\tau\) lie on the D-plateau and the plateau theorem gives
\(\tau<\pi D/2\),

\[
\boxed{
|R\cap\Delta B_i|>\frac{\rho}{\pi D}.
}
\tag{124.13}

If \(\tau=0\), the second alternative is impossible and the endpoint retains all
of R.
\]

Hence a super-boundary source has the exact dichotomy: either a capacity endpoint
retains \(\Omega(\rho)\) original rattler positions, or one single n-to-(n+1)
plateau transition replaces a diverging number of original strict rattlers.

---

# 125. Same-cardinality saturation by replacements

Canonical Theorem 63.1 obtains unit covering by adding boundary-order many points.
For the flexible Target A source one can instead saturate at the same cardinality by
replacements while preserving any specified strict-rattler set pointwise.

Let A be a triangle-free N-point global minimizer of diameter D in the fixed original
hull H, and let \(R\subset A\) consist of strict rattlers.  If a point
\(y\in H\) satisfies

\[
|y-a|>1
\qquad(a\in A),
\tag{125.1}
\]

then the current minimizer has at least one unit contact: otherwise its finite minimum
separation would exceed one and a uniform contraction would contradict global
minimality.  No endpoint of a unit contact lies in R.  Delete one such endpoint x and
insert y.  The new N-point set is unit-separated, triangle-free, and contained in H,
so its diameter is at most D and hence exactly D(N)=D.

The inserted point creates no unit contact.  Therefore the total number of unit
contacts strictly decreases.  Repeating terminates after finitely many replacements.

Every r in R remains non-diametral against every inserted point because

\[
\max_{z\in H}|r-z|
=
\max_{z\in\operatorname{ext}H}|r-z|
<D,
\]

and all extreme points of H belong to the original source A.

> **Theorem 125.1 (same-cardinality rattler-preserving saturation).**
> There is a triangle-free N-point global minimizer \(A^{\rm sat}\subset H\) such
> that every point of R remains at its original position and remains a genuine strict
> rattler, while
> \[
> \boxed{
> H\subseteq\bigcup_{a\in A^{\rm sat}}\overline B(a,1).
> }
> \tag{125.2}
> \]

This removes the boundary-order cardinality expenditure of Theorem 63.1 when only
same-cardinality saturation and the strict-rattler population are needed.  It does
not preserve the old contact-minimal core or hybrid forest automatically.

---

# 126. Capacity shadow and bounded-displacement optimum partner

Let A be the genuine N-point source in H and let

\[
M=\alpha_1(H)=N+\widehat p_H.
\]

Choose \(X_{\max}\subset H\) with \(|X_{\max}|=M\).  Theorem 122.1 gives an
injection

\[
\mu:A\hookrightarrow X_{\max}
\]

such that

\[
\boxed{|a-\mu(a)|<1\qquad(a\in A).}
\tag{126.1}
\]

Let

\[
Y=\mu(A).
\]

Then Y is a unit-separated N-point subset of H.  Hence

\[
\boxed{\operatorname{diam}Y=D(N)=D.}
\tag{126.2}
\]

Thus Y is a same-cardinality global optimum contained in one capacity endpoint and
pointwise matched to the source at displacement less than one.

Put

\[
L=\operatorname{conv}Y,
\qquad
\delta=\max_{a\in A}|a-\mu(a)|<1.
\tag{126.3}
\]

Since \(L\subseteq H\), while every convex combination of source points can be
matched coefficientwise to a convex combination of their images,

> **Theorem 126.1 (capacity-shadow hull control).**
> \[
> \boxed{
> L\subseteq H\subseteq L+\delta\mathbb B,
> \qquad
> d_{\rm H}(H,L)\le\delta<1.
> }
> \tag{126.4}
> \]

Consequently

\[
\boxed{0\le P_H-P_L\le2\pi\delta<2\pi,}
\tag{126.5}
\]

and

\[
\boxed{
0\le \operatorname{area}H-\operatorname{area}L
\le \delta P_L+\pi\delta^2.
}
\tag{126.6}
\]

This is the first exact pointwise coupling of the genuine source to another global
optimum inside its own capacity endpoint.

---

# 127. Finite-chord stress identity

Label the source and its capacity shadow by

\[
p_i\in A,
\qquad
y_i=\mu(p_i),
\qquad
v_i=y_i-p_i.
\tag{127.1}
\]

Fix any normalized proper KKT stress \((\alpha,\beta)\) of A from Theorem 4.1.
For an active source contact ij,

\[
2(p_i-p_j)\cdot(v_i-v_j)+|v_i-v_j|^2\ge0,
\tag{127.2}
\]

while for an active source diameter edge ij,

\[
2(p_i-p_j)\cdot(v_i-v_j)+|v_i-v_j|^2\le0.
\tag{127.3}
\]

The virtual-work identity (11.7) cancels the weighted linear terms.  Therefore:

> **Theorem 127.1 (finite-chord stress inequality).**
> \[
> \boxed{
> \sum_{ij\in C}\alpha_{ij}|v_i-v_j|^2
> \ge
> \sum_{ij\in H_D}\beta_{ij}|v_i-v_j|^2.
> }
> \tag{127.4}
> \]

More exactly,

\[
\boxed{
\begin{aligned}
&\sum_{ij\in C}\alpha_{ij}\bigl(|y_i-y_j|^2-1\bigr)
+\sum_{ij\in H_D}\beta_{ij}\bigl(D^2-|y_i-y_j|^2\bigr)\\
&\qquad=
\sum_{ij\in C}\alpha_{ij}|v_i-v_j|^2
-\sum_{ij\in H_D}\beta_{ij}|v_i-v_j|^2
\ge0.
\end{aligned}
}
\tag{127.5}
\]

Equality holds exactly when every positively stressed source contact remains an exact
unit contact in Y and every positively stressed source diameter edge remains an exact
diameter edge in Y.

This is a finite-amplitude identity along an actual chord between two same-cardinality
global optima.  As required by the product-germ theorem, strict rattlers carry no
direct local stress term; their importance is that their capacity images are coupled
to the stressed backbone in the same finite optimum partner.

---

# 128. Fundamental-circuit sequentialization and exact cycle budget

Let C be a fundamental circuit of any strict conflict transversal matroid, with right
neighborhood W.  Then

\[
|C|=|W|+1,
\tag{128.1}
\]

and every proper subset of C is matchable.  In particular every \(w\in W\) has
degree at least two: if w had unique neighbor x, then \(C\setminus\{x\}\) would
have at most \(|W|-1\) neighbors and would be unmatchable.

The induced circuit graph is connected.  Suppose first that it is acyclic.  If
\(w=|W|\), then the tree has \(2w+1\) vertices and 2w edges.  Since every right
vertex has degree at least two, every right vertex has degree exactly two.  Contracting
right vertices therefore gives an ordinary tree on the |C| left vertices.

Peel a leaf left vertex x and its unique adjacent blocker w.  In the packing exchange,
x conflicts with no retained source point except w, so w may be swapped for x.  The
residual bipartite graph is again a circuit of the same tree type.  Iteration ends with
one left point and no blocker, which is appended in the final net-+1 step.

> **Theorem 128.1 (tree-circuit sequentialization).**
> A tree fundamental circuit admits an exact sequence of one-for-one feasible swaps,
> followed by one final append.  In the source-capacity plateau each intermediate
> same-cardinality configuration is a global optimum, and the final configuration is
> the adjacent-cardinality global optimum.

No triangle-free conclusion is asserted for the intermediate swaps; exact unit
triangles may first appear during this sequence.

For a general connected planar circuit let e be its number of strict-conflict edges
and \(w=|W|\).  Define

\[
\kappa=e-2w.
\tag{128.2}
\]

Since every right degree is at least two,

\[
\boxed{
\kappa=\sum_{b\in W}(\deg b-2)\ge0.
}
\tag{128.3}
\]

Euler's formula for the straight-line planar circuit graph gives simultaneously

\[
\boxed{
\kappa=\#\{\text{bounded faces of the circuit graph}\}.
}
\tag{128.4}
\]

Thus the obstruction to pure sequential tree exchange has an exact planar cycle
budget rather than an unspecified Hall-circuit complexity.

---

# 129. Codimension-one triangle walls require straight root paths

Retain the affine one-root forest flat of Section 62.  Theorem 62.2 proves that every
relatively open codimension-one unit-triangle wall has one side identically unit and
that this persistent side lies entirely in the fixed part.

Consider such a triangle wall whose third vertex a is an unpinned forest vertex and
whose fixed persistent side is bc.  Since \(|b-c|=1\), the conditions

\[
|a(x)-b|=|a(x)-c|=1
\]

force \(a(x)\) to equal one of the two fixed equilateral apices of bc.

The affine displacement map of a is

\[
x\longmapsto
\sum_{e\in P(a)}x_eJu_e,
\tag{129.1}
\]

where \(P(a)\) is the root path to a.  Its rank is

\[
\dim\operatorname{span}\{u_e:e\in P(a)\}.
\tag{129.2}
\]

> **Theorem 129.1 (straight-path triangle-wall criterion).**
> If the root path of a contains two nonparallel retained unit-edge directions, then
> every triangle locus involving a has codimension at least two in the affine forest
> coordinates.  Hence a codimension-one triangle wall involving a moving forest
> vertex is possible only when every retained edge on its root path is parallel to one
> common line.

Thus only straight-chain prefixes can genuinely separate the affine forest parameter
space by codimension-one triangle walls.  This refines the general factor-exclusion
theorem; it does not yet bound the number or total length of those straight chains.

---

# 130. Exact Oler-capacity split

For a fixed convex hull H with perimeter P_H and a unit-separated r-point packing P in
H, define

\[
\mathscr O_H(r)
=
\operatorname{area}H+c_0P_H-a_0(r-1).
\tag{130.1}
\]

Let \(M=\alpha_1(H)\).  Since the geometric hull terms are identical,

\[
\boxed{
\mathscr O_H(r)=a_0(M-r)+\mathscr O_H(M).
}
\tag{130.2}
\]

Finite Oler gives \(\mathscr O_H(M)\ge0\).  For the maximal triangle-free source
extension B this becomes

\[
\boxed{
\mathscr O_H(|B|)=a_0\tau+\mathscr O_H(M),
\qquad
\mathscr O_H(|B|)\ge a_0\tau.
}
\tag{130.3}
\]

The source Oler surplus therefore contains an exact integer capacity term plus the
nonnegative residual Oler slack of a capacity endpoint.  This identity does not by
itself distinguish forest vertices from core vertices; the cancellation warning of
Section 21 remains binding.

---

# 131. External literature checked during the v1.7 run

Internet literature search is permitted for subsequent Target A work.  The following
results were checked for applicability but are not imported as Target A theorems.

1. **Bondarenko--Hardin--Saff, mesh ratios for best packings**
   (arXiv:1212.6211).  For best-packing
   configurations that arise as limits of Riesz s-energy minimizers as
   \(s\to\infty\), the covering-radius/separation mesh ratio is at most one.  This
   does not state that every arbitrary best-packing representative has that property.
   The self-contained replacement-saturation Theorem 125.1 is what is trusted here.

2. **Fejes Toth--Kuperberg--Kuperberg, highly saturated packings and reduced coverings**
   (arXiv:math/9511225).  Their notions of
   n-saturation and complete saturation formalize the impossibility of replacing
   n-1 packed bodies by n.  A finite capacity endpoint in H is completely saturated
   relative to H for the trivial cardinality reason recorded in Section 122.2, but
   infinite-plane density conclusions do not automatically transfer to a bounded
   source hull.

3. **G. Kuperberg--K. Kuperberg--W. Kuperberg, lattice packings with gap defects are
   not completely saturated** (arXiv:math/0303366).  They prove that a planar honeycomb circle packing
   with an arbitrarily narrow linear gap defect is not completely saturated.  This is
   directly suggestive for the coherent strained-monomer regression: small distributed
   clearance may be concentratable by a finite rearrangement until one extra point
   fits.  No theorem has yet transferred their infinite linear-gap construction to a
   finite monomer/dimer scaffold in the source hull.

4. **Gensane, generation of optimal packings from optimal packings**
   (Electronic Journal of Combinatorics 16 (2009), R24; DOI 10.37236/113).  The paper
   defines weak and strong generation and conjectures an infinite sequence of strong
   generators for every compact convex container.  The general generation statement
   is conjectural, not available as a black-box bridge.  The exchange flag of Section
   124 is an unconditional discrete generation result specific to the source-capacity
   conflict matroid.

These references sharpen the research direction but do not alter the Level I status.

---

# 132. Regressions and no-go statements added in v1.7

The following remain binding.

1. The exact source Hall slack \(\widehat p_H\) and residual slack \(\tau\) need not
   vanish.
2. Capacity alone cannot produce a Hall surplus above its own exact endpoint:
   Theorem 122.2 proves that the maximum source deficiency is exactly the available
   capacity slack.
3. A maximal triangle-free extension can be unit-covering saturated, retain a
   super-boundary rattler population, and still have positive exchange-only capacity.
4. The source-capacity exchange flag consists of global optima, but the intermediate
   configurations need not remain triangle-free.
5. Tree-circuit sequentialization does not prevent the first unit triangle from
   appearing during one of the swaps.
6. Planarity of the source conflict graph and of the target gammoid does not alone
   imply the required rank loss.
7. The capacity shadow gives a bounded-displacement same-cardinality optimum partner,
   not a coordinate identification with the independent smaller optimum used in the
   Schur scaffold.
8. The finite-chord stress identity is nonnegative but does not yet force a positive
   lower bound from the strict rattler population, since strict rattlers carry no
   active source stress.
9. The same-cardinality replacement-saturation theorem may destroy the old hybrid
   core/forest contact normal form.  Use it only where that structure is unnecessary,
   or rebuild the normal form after the replacement.
10. Codimension-one affine triangle walls are confined to straight root paths, but
    arbitrarily long straight rooted chains are not yet excluded.
11. The Kuperberg gap-defect theorem is an external infinite-packing result; applying
    it to finite coherent monomer regions requires a new quantitative transfer
    theorem.
12. No individual Voronoi cell is assigned area a_0.

The strained near-triangular finite-patch regression remains valid: append-maximality,
unit covering, many strict points, and boundary-order unused capacity do not imply
global diameter optimality.  Global extremality remains essential.

---

# 133. Authoritative Target A frontier in v1.7.0

The direct canonical endpoint is unchanged.  For the plateau-terminalized Schur
response write

\[
\zeta=\dim\ker S=|C^\partial|-\operatorname{rank}S,
\qquad
s=\Delta_\Lambda-d_{\rm int}.
\tag{133.1}
\]

A survivor has

\[
\boxed{
g=\Delta_\Lambda-d_{\rm sc}=s-\zeta=\rho^\dagger-\Phi(v)\ge1.
}
\tag{133.2}
\]

Target A is resolved exactly by

\[
\boxed{\zeta\ge s,}
\tag{133.3}
\]

or equivalently

\[
\boxed{
\operatorname{rank}S
\le d_{\rm int}+|C^\partial|-\Delta_\Lambda.
}
\tag{133.4}
\]

The source-side contradiction threshold has sharpened.  For the original genuine
source A, Theorem 119.2 shows that it is enough to prove

\[
\boxed{
g>0
\Longrightarrow
\exists Q\subset H\text{ unit-separated with }
|Q|-|N_A(Q)|\ge\widehat p_H+1.
}
\tag{133.5}
\]

No scaffold rebuild is needed for this improvement from p+1 to
\(\widehat p_H+1\).

If one legally replaces A by the maximal triangle-free extension B and rebuilds the
Target A scaffold for B, the stronger residual-capacity endpoint is

\[
\boxed{
g_B>0
\Longrightarrow
\exists Q\subset H\text{ unit-separated with }
|Q|-|N_B(Q)|\ge\tau+1.
}
\tag{133.6}
\]

Theorem 122.2 shows why this cannot follow from fixed-hull capacity bookkeeping alone:
\(\tau\) is exactly the maximum Hall deficiency available from H and B.  A proof of
(133.6) must therefore use the global relationship to the independent smaller-optimum
scaffold, or derive a contradiction before reaching the capacity endpoint.

## 133.1 Preferred next theorem: first-transition alternative

Use the source-capacity flag

\[
B=P_0\rightsquigarrow P_1\rightsquigarrow\cdots\rightsquigarrow P_\tau.
\]

A high-value closure theorem would prove the following exact alternative for the first
Hall-tight transition that creates a unit triangle:

> **First-transition alternative.**  If \(P_{j-1}\) is triangle-free and \(P_j\)
> is the first member containing a unit triangle, then either
> 1. the transition admits a triangle-free perturbation or different basis/circuit
>    choice producing a triangle-free global optimum of cardinality q+j; or
> 2. the transition support produces at least the missing Schur nullity
>    \(\Delta_\Lambda-d_{\rm int}\).

The tree-circuit theorem reduces the acyclic case to a sequence of one-for-one swaps;
the cyclic obstruction is measured exactly by the bounded-face count \(\kappa\).

## 133.2 Preferred next theorem: finite gap-concentration for monomer bulk

The surviving scaffold has only two locally Hall-neutral phases.  The monomer phase is
a bounded-displacement deformation of the triangular lattice.  The Kuperberg gap
mechanism suggests the following finite theorem:

> **Finite monomer gap-concentration theorem.**  A sufficiently large coherent
> zero-charge monomer domain in a globally optimal source/scaffold, carrying positive
> distributed nearest-neighbor clearance but only boundary-order total clearance,
> admits a finite rearrangement inside the relevant hull/collar that frees one extra
> unit-separated site without increasing the diameter.

Such a theorem would convert the main strained-monomer regression from an obstruction
into a contradiction.  It must be proved in the finite container with explicit
boundary control; the infinite gap-defect theorem cannot simply be quoted.

## 133.3 Preferred next theorem: capacity-shadow transport

The capacity shadow supplies a same-cardinality global optimum Y with

\[
|p_i-y_i|<1,
\qquad
d_{\rm H}(\operatorname{conv}A,\operatorname{conv}Y)<1,
\]

and the finite stress identity (127.5).  A second possible closure is to transport this
bounded-displacement chord through deletion of the strict-rattler population to the
smaller plateau endpoint and prove that the induced boundary displacement lies in the
kernel of the Schur response with dimension at least s.

No such transport theorem is currently proved.

## 133.4 Preferred next theorem: straight-chain barrier elimination

The affine forest triangle-wall theorem now shows that only collinear root paths can
form codimension-one triangle barriers.  A fourth closure route is to prove that a
super-boundary number of forest degrees of freedom cannot all be confined behind
straight-chain barriers in a global minimizer.  Any proof must use global finite
capacity or exact source-face geometry; long rooted chains are valid local
regressions.

---

# 134. Version history through v1.7.0

- **v1.5.1:** fixed-basis/phase contractions, plateau terminalization, phase-pure
  boundary minors, Schur response, source cage localization, corrected branchwise
  forest confinement, explicit outer-terminal bound, exact two-sided defect transfer.
- **v1.6.0:** strict-rattler product-germ/local-KKT no-go; exact planar strict-gammoid
  completion of the Schur response; response-corrected collar capacity Phi; minimal
  kernel-map certificate; continuum source Hall and cross-matching with global plateau
  slack; exact inner-parallel capacity; correction of zero-slack and per-cell-Voronoi
  overclaims.
- **v1.7.0:** exact genuine-hull capacity slack \(\widehat p_H\); self-container and
  boundary-reserve theorems; maximal triangle-free same-hull extension and residual
  exchange-only capacity \(\tau\); universal fixed-container endpoint matching and
  exact Hall slack; source-capacity plateau exchange flag; same-cardinality
  rattler-preserving saturation; bounded-displacement capacity shadow with
  Hausdorff/perimeter control; finite-chord stress identity; tree-circuit
  sequentialization and exact planar cycle budget; straight-root-path criterion for
  codimension-one affine triangle walls; exact Oler-capacity split; and audited
  external leads from generation and saturation theory.

**LEVEL I STATUS: STILL OPEN.  TARGET A REMAINS UNRESOLVED.**

`erdos_problem_99_1.7.0.md` supersedes v1.6.0 as the sole canonical theorem-state
file for subsequent runs.


# 135. Exact source-Hall profile of the capacity exchange flag

This continuation records one further exact consequence of Section 124.  It does not
close Target A, but it couples the exchange flag to the genuine fixed source A rather
than only to the extension B.

Retain the notation of Section 124:

\[
A\subseteq B\subseteq H,
\qquad |A|=N,
\qquad |B|=q=N+k,
\qquad M=\alpha_1(H)=q+\tau,
\]

and let \(X\) be a capacity endpoint, \(|X|=M\).  For a maximum matchable basis
\(\mathcal B\subseteq X\), let \(E_0=X\setminus\mathcal B\), and for
\(E\subseteq E_0\) use

\[
U_E=\bigcup_{e\in E}C_e,
\qquad
W_E=N_B(U_E),
\qquad
P_E=(B\setminus W_E)\cup U_E.
\tag{135.1}
\]

Theorem 124.1 gives \(|P_E|=q+|E|\) and that \(P_E\) is a unit-separated
global optimum in H.

> **Theorem 135.1 (source-Hall-tight exchange flag).** For every
> \(E\subseteq E_0\),
> \[
> \boxed{N_A(P_E)=A,}
> \tag{135.2}
> \]
> and consequently
> \[
> \boxed{
> |P_E|-|N_A(P_E)|=k+|E|.
> }
> \tag{135.3}
> \]

### Proof

The inclusion \(N_A(P_E)\subseteq A\) is tautological.  Conversely, fix \(a\in A\).
Since \(A\subseteq B\), either \(a\notin W_E\) or \(a\in W_E\).

If \(a\notin W_E\), then \(a\in B\setminus W_E\subseteq P_E\), so the coincident
pair \(a,a\) is a strict conflict in the replacement graph and
\(a\in N_A(P_E)\).  If \(a\in W_E=N_B(U_E)\), then by definition there is
\(u\in U_E\subseteq P_E\) with \(|a-u|<1\), again giving
\(a\in N_A(P_E)\).  Thus \(N_A(P_E)=A\).  Now use
\(|P_E|=q+|E|=N+k+|E|\).  \(\square\)

At the terminal flag member \(E=E_0\), \(|E_0|=\tau\) and

\[
|P_{E_0}|=q+\tau=M=N+\widehat p_H,
\qquad
|P_{E_0}|-|N_A(P_{E_0})|=\widehat p_H.
\tag{135.4}
\]

Thus the terminal exchange endpoint attains the exact maximum source-Hall deficiency
from Theorem 119.2.  The adjacent flag spends that source capacity one integer at a
time:

\[
\bigl(|P_i|-|N_A(P_i)|\bigr)
 -
\bigl(|P_{i-1}|-|N_A(P_{i-1})|\bigr)=1.
\tag{135.5}
\]

There is an exact two-sided slack conservation law.  Applying Theorem 122.2 to the
unit-separated set \(P_E\subset H\) and the same capacity endpoint X gives

\[
\max_{Q\subset H}\bigl(|Q|-|N_{P_E}(Q)|\bigr)
 =M-|P_E|=\tau-|E|.
\tag{135.6}
\]

Combining (135.3) and (135.6),

\[
\boxed{
\bigl(|P_E|-|N_A(P_E)|\bigr)
 +
 \max_Q\bigl(|Q|-|N_{P_E}(Q)|\bigr)
 =k+\tau=\widehat p_H.
}
\tag{135.7}
\]

If \(k+|E|\ge1\), the self-container theorem also supplies the exact reserve

\[
\boxed{|P_E\cap\partial H|\ge k+|E|+1.}
\tag{135.8}
\]

This reserve concerns the complete exchanged configuration \(P_E\); it does not imply
that \(U_E\), the nonbasis elements, or any first-triangle support meets
\(\partial H\).

## 135.1 Exact limitation for Target A

Theorem 135.1 rules out a tempting but invalid use of the exchange flag.  The flag
does not itself produce the required source contradiction

\[
|Q|-|N_A(Q)|\ge\widehat p_H+1,
\]

because its terminal member reaches exactly \(\widehat p_H\) and Theorem 119.2 forbids
any larger deficiency for a unit-separated \(Q\subset H\).  Likewise, the intermediate
members spend the fixed source slack while leaving exactly the complementary capacity
slack in (135.7).  A closure must therefore add information from the independent
smaller optimum, the triangle-free condition at a first exchange transition, or an
exact source-to-Schur transport.  This lemma supplies none of those three missing
inputs.

The following regressions remain active after this result:

1. \(\tau\) and \(\widehat p_H\) need not be zero.
2. \(P_E\) need not contain A and need not be triangle-free.
3. The boundary reserve (135.8) is a reserve for \(P_E\), not for \(U_E\).
4. No old Target A scaffold may be transferred from A or B to \(P_E\) without a
   rebuild.
5. The exact source-Hall profile gives no rank saving for the Schur response.

Accordingly, the authoritative endpoint remains

\[
\boxed{\dim\ker S\ge\Delta_\Lambda-d_{\rm int}},
\]

or equivalently

\[
\boxed{\operatorname{rank}S
\le d_{\rm int}+|C^\partial|-\Delta_\Lambda.}
\]

No Level I proof or certified infinite counterexample has been obtained.


# 136. Two exact first-transition and finite-strain reductions

This section adds two finite statements aimed at the remaining Target A routes.  The
first is a sufficient perturbation criterion for the first triangle-producing member
of the source-capacity flag.  The second is an explicit finite model of gap
concentration.  Neither statement supplies the missing Schur nullity.

## 136.1 A simultaneous triangle-breaking cone criterion

Let

\[
T=P_{j-1},
\qquad P=P_j
\]

be the first adjacent member of the exchange flag for which a unit equilateral
triangle occurs.  Thus \(T\) is triangle-free, \(P\) is a global optimum of diameter
\(D\), and

\[
P=(T\setminus\Delta B_j)\cup\Delta X_j.
\]

Put

\[
U_\triangle
=\{x\in\Delta X_j:x\text{ belongs to a unit equilateral triangle of }P\}.
\]

For \(x\in U_\triangle\), define the finite vector set

\[
\mathcal V_P(x)
:=
\{x-y:y\in P,\ |x-y|=1\}
\cup
\{y-x:y\in P,\ |x-y|=D\}.
\tag{136.1}
\]

The first set records directions in which a displacement of \(x\) increases every
active unit separation.  The second set has the reversed sign, so a positive scalar
product decreases every active diameter separation.

> **Theorem 136.1 (simultaneous first-transition perturbation).**
> Suppose that for every \(x\in U_\triangle\) there is a vector \(u_x\in\mathbb R^2\)
> such that
> \[
> v\cdot u_x>0
> \qquad(v\in\mathcal V_P(x)).
> \tag{136.2}
> \]
> Then \(P\) has a triangle-free global optimum of the same cardinality and diameter
> \(D\).  More precisely, for all sufficiently small positive \(\epsilon\), moving
> each \(x\in U_\triangle\) to \(x+\epsilon u_x\) and leaving all other points fixed
> gives a unit-separated set of diameter at most \(D\) with no unit equilateral
> triangle.

### Proof

Every triangle in \(P\) contains a point of \(\Delta X_j\), because the points of
\(T\) that remain in \(P\) form a subset of the triangle-free set \(T\).  Hence every
triangle in \(P\) contains a point of \(U_\triangle\).

For a unit edge \(xy\) with \(x\in U_\triangle\) and \(y\notin U_\triangle\), (136.2)
gives
\[
(x-y)\cdot u_x>0.
\]
If both endpoints lie in \(U_\triangle\), then
\[
(x-y)\cdot(u_x-u_y)
=(x-y)\cdot u_x+(y-x)\cdot u_y>0.
\tag{136.3}
\]
Thus every unit edge incident with a moved point becomes strictly longer under the
displacement.  Unit edges with neither endpoint moved do not become shorter.  Since
every edge of every old unit triangle is incident with a moved point, all old unit
triangles are destroyed.

For a diameter edge \(xy\) with \(x\in U_\triangle\) and \(y\notin U_\triangle\),
(136.2) gives
\[
(x-y)\cdot u_x<0.
\]
If both endpoints move, then
\[
(x-y)\cdot(u_x-u_y)
=(x-y)\cdot u_x-(x-y)\cdot u_y<0,
\tag{136.4}
\]
because (136.2) at \(y\) gives \((x-y)\cdot u_y>0\).  Therefore every diameter
edge incident with a moved point becomes strictly shorter, and every diameter edge
with neither endpoint moved stays unchanged.

There are finitely many pairs.  Every nonactive pair has distance strictly between
\(1\) and \(D\), while every active pair has the strict first-order sign just proved
unless it is unchanged.  Consequently a sufficiently small positive \(\epsilon\)
preserves all lower constraints and does not increase any upper constraint.  The
resulting set is unit-separated and has diameter at most \(D\).  It has no unit
equilateral triangle: any such triangle would have to be a triangle of \(P\) for
small enough \(\epsilon\), but every triangle of \(P\) had an incident unit edge
strictly increased.

Since \(P=P_j\) is a global optimum at this cardinality, a unit-separated set of
smaller diameter would contradict the definition of \(D(q+j)=D\).  Hence the
perturbed set has diameter exactly \(D\) and is a global optimum.  \(\square\)

The criterion has an exact local alternative.  For a finite nonzero vector set
\(V\subset\mathbb R^2\), either there is a \(u\) with \(v\cdot u>0\) for every
\(v\in V\), or there are coefficients \(\lambda_v\ge0\), not all zero, with
\[
\sum_{v\in V}\lambda_vv=0.
\tag{136.5}
\]
Indeed, the first case holds precisely when \(0\notin\operatorname{conv}V\), and
then strict separation of the compact convex hull from \(0\) supplies \(u\).  If
\(0\in\operatorname{conv}V\), its convex-combination coefficients give (136.5).

Therefore, if the independent perturbation in Theorem 136.1 is unavailable, some
\(x\in U_\triangle\) has a nonnegative equilibrium among its unit-contact vectors
and reversed diameter vectors.  In the special case that \(x\) has no diameter
partner, the two contact vectors supplied by a triangle make an angle of \(60^\circ\)
and cannot themselves positively balance.  Thus (136.5) then forces at least one
additional unit contact:

\[
\boxed{
x\text{ is triangle-supported and non-diametral, but the cone test fails}
\Longrightarrow \deg_{E_1(P)}(x)\ge3.
}
\tag{136.6}
\]

This is only a reduction of the first-transition branch.  The remaining three-contact
and diameter-supported cases are not excluded by the source-capacity flag.

## 136.2 An explicit finite strain-transfer theorem

Let \(e_1,e_2\) be unit vectors with \(e_1\cdot e_2=1/2\), and let
\[
\Lambda_0=\mathbb Ze_1+\mathbb Ze_2.
\]
For \(L\ge2\), \(\epsilon>0\), and \(s=1+\epsilon\), define
\[
P_{L,\epsilon}
=s\{ie_1+je_2:0\le i,j\le L-1\},
\qquad
K_{L,\epsilon}=\operatorname{conv}P_{L,\epsilon}.
\tag{136.7}
\]

> **Theorem 136.2 (finite homothetic gap concentration).**
> The set \(P_{L,\epsilon}\) is triangle-free, has \(L^2\) points, and
> \[
> \operatorname{diam}P_{L,\epsilon}
> =\operatorname{diam}K_{L,\epsilon}
> =s\sqrt3\,(L-1).
> \tag{136.8}
> \]
> If
> \[
> \epsilon\ge\frac1{L-1},
> \tag{136.9}
> \]
> then \(K_{L,\epsilon}\) contains a unit-separated set of \(L^2+1\) points,
> namely
> \[
> Q_L
> =\{ie_1+je_2:0\le i,j\le L-1\}\cup\{Le_1\},
> \tag{136.10}
> \]
> and \(\operatorname{diam}Q_L\le\operatorname{diam}P_{L,\epsilon}\).

### Proof

For a nonzero integer pair \((i,j)\),
\[
|ie_1+je_2|^2=i^2+ij+j^2\ge1.
\]
Thus distinct points of \(P_{L,\epsilon}\) have distance at least \(s>1\), so
the set has no unit edges and is triangle-free.  On the coordinate parallelogram
\[
K_{L,\epsilon}
=\{ae_1+be_2:0\le a,b\le s(L-1)\},
\]
the squared norm \(a^2+b^2+ab\) is maximized at opposite vertices.  This gives
(136.8).

The condition (136.9) is equivalent to
\[
L\le s(L-1).
\]
Consequently \(Le_1\in K_{L,\epsilon}\), and the other \(L^2\) points in (136.10)
also lie in that parallelogram.  All points of \(Q_L\) belong to the unit triangular
lattice \(\Lambda_0\), so their mutual distances are at least one.  Since
\(Q_L\subseteq K_{L,\epsilon}\), its diameter is at most the diameter in (136.8).
\(\square\)

For the strained-patch scale \(\epsilon=\alpha/L\), condition (136.9) requires
\[
\alpha\ge\frac{L}{L-1}.
\tag{136.11}
\]
If \(0<\alpha<1\), then \(s(L-1)<L\), and the coordinate parallelogram contains
exactly the original \(L^2\) lattice sites with integer coordinates
\(0\le i,j\le L-1\).  Thus the straight homothetic compression followed by a
lattice insertion cannot produce the extra site in this regime, despite the patch
having \(\Theta(L^2)\) total nearest-neighbor clearance of order \(\Theta(L)\).
This is a precise finite boundary obstruction, not a claim that no arbitrary
nonlattice rearrangement exists.

## 136.3 Target A audit after the two reductions

Theorem 136.1 removes the first-transition configurations satisfying the explicit
strict cone condition, but it does not control a three-contact equilibrium or a
diameter-supported triangle vertex.  Theorem 136.2 supplies a finite gap-transfer
model only when a full homothetic patch has accumulated one lattice spacing of
longitudinal slack and has no incompatible fixed environment.  The actual source
scaffold supplies neither condition in the surviving general branch.

In particular, the exact unresolved implication remains
\[
\boxed{
\dim\ker S=|C^\partial|-\operatorname{rank}S
\ \ge\ \Delta_\Lambda-d_{\rm int},
}
\]
or, on the source side, a unit-separated \(Q\subset H\) with
\[
|Q|-|N_A(Q)|\ge\widehat p_H+1.
\]
The strained-monomer, three-contact/diameter-support, overlapping-circuit, and
annular-routing regressions all remain live.  No Level I proof or certified infinite
counterexample has been obtained.



# 136. Finite transfer of a honeycomb gap witness

The Kuperberg--Kuperberg--Kuperberg theorem on a honeycomb packing with a linear gap
defect is a finite-rearrangement theorem after rescaling the circle centers to
minimum separation one.  In particular, for every gap width \(d>0\) and direction
there are finite sets \(S_d,T_d\) of centers such that

\[
|T_d|=|S_d|+1,
\qquad
(\mathcal H_d\setminus S_d)\cup T_d
\text{ is unit-separated},
\tag{136.1}
\]

where \(\mathcal H_d\) is the corresponding infinite honeycomb packing with a
linear gap.  The finite witness sets \(S_d,T_d\) are implicit in their finite block
rearrangement; no uniform bound on their diameter as \(d\downarrow0\) is asserted.

> **Theorem 136.1 (protected finite-container transfer).** Let \(L\) be an open
> bounded set with \(\operatorname{diam}L<D\), and let \(F\subset L\) be a finite
> unit-separated set.  Suppose that, for some \(d>0\), there are finite witness sets
> \(S_d,T_d\) satisfying (136.1), and some set \(F_{\rm far}\), such that:
>
> 1. \(S_d\subseteq F\subseteq \mathcal H_d\cup F_{\rm far}\);
> 2. \(F\setminus S_d\) contains no points outside \(\mathcal H_d\) that are within
>    unit distance of \(T_d\);
> 3. \(T_d\subset L\); and
> 4. \(T_d\cap(\mathcal H_d\setminus S_d)=\varnothing\).
>
> Then
> \[
> (F\setminus S_d)\cup T_d
> \]
> is unit-separated and has \(|F|+1\) points in \(L\).

### Proof

The set \(F\setminus S_d\) is unit-separated.  Its points lying in
\(\mathcal H_d\setminus S_d\) are at distance at least one from every point of
\(T_d\) by (136.1), and hypothesis 2 gives the same conclusion for the remaining
points.  Thus the displayed replacement is unit-separated.  Its cardinality is
\[
|F|-|S_d|+|T_d|=|F|+1.
\]
Hypothesis 3 and \(F\subset L\) put every point in \(L\).  \(\square\)

Consequently, if \(F\) has the cardinality \(N\) of a diameter-minimizing
configuration with \(D(N)=D\), Theorem 136.1 contradicts the definition of \(D(N)\):
the replacement has \(N+1\) points and diameter strictly below \(D\).

## 136.1 Exact scope and remaining finite gap

This is a genuine finite-container transfer, but it does not yet supply the
finite monomer gap-concentration theorem required by Target A.  The scaffold's
coherent monomer phase is only known to have bounded-displacement triangular-lattice
combinatorics.  The current theorem does not prove that it contains an exact
protected copy of \(\mathcal H_d\), nor that all non-modeled source points are at
least one from \(T_d\).

Moreover, the strained-monomer regression can have gap width \(d=d_D\downarrow0\).
The external theorem and its finite block construction do not provide a quantitative
bound showing that the witness diameter is \(o(D)\), or even \(O(D)\), in that regime.
Thus the transfer eliminates the following conditional branch:

\[
\boxed{
\text{a fixed-width, protected honeycomb gap inside the open target hull is
impossible.}
}
\tag{136.2}
\]

It leaves the exact branch

\[
\boxed{
\text{vanishing-width or non-protected coherent monomer strain.}
}
\tag{136.3}
\]

No Schur nullity saving follows from (136.1)--(136.3), and no source Hall deficiency
above \(\widehat p_H\) follows.  The Target A endpoint therefore remains

\[
\dim\ker S\ge\Delta_\Lambda-d_{\rm int}.
\]


# 137. Exact one-point test at a first tree-circuit triangle

The tree-circuit sequentialization reduces a tree transition to one-point insertions
and deletions.  The following lemma gives an exact test for the insertion point when
the preceding configuration is triangle-free.  It separates a removable first
triangle from a locally isolated contact cage; it does not use, and does not imply,
global optimality of an arbitrary preceding configuration.

Let \(P\) be a finite triangle-free unit-separated set, let \(x\notin P\), and assume
that \(P\cup\{x\}\) is unit-separated.  Put

\[
C_x=\{p\in P:|p-x|=1\},
\qquad
E_x=\{\{p,q\}\subset C_x:|p-q|=1\}.
\tag{137.1}
\]

The edges in \(E_x\) are exactly the unit triangles created by inserting \(x\).

> **Theorem 137.1 (semicircle/cage dichotomy).** Suppose that every distance from
> \(x\) to \(P\) is strictly less than a prescribed diameter \(D\).  Then exactly
> the following alternatives apply to a one-point motion of \(x\):
>
> 1. If the direction set
>    \[
>    \{p-x:p\in C_x\}\subset\mathbb S^1
>    \]
>    is contained in a closed semicircle, there are a vector \(\xi\ne0\) and
>    \(\epsilon>0\) such that, for every \(0<t<\epsilon\),
>    \[
>    (P\cup\{x+t\xi\})
>    \]
>    is unit-separated, has diameter at most \(D\), and is triangle-free.
>
> 2. If the direction set is not contained in a closed semicircle, then \(x\) is
>    locally isolated in the one-point feasible slice: there is \(\epsilon>0\) such
>    that the only \(y\) with \(|y-x|<\epsilon\) and \(|y-p|\ge1\) for every
>    \(p\in C_x\) is \(y=x\).

### Proof

Write \(a_p=p-x\), so \(|a_p|=1\) for \(p\in C_x\).  If the directions lie in
a closed semicircle, choose a supporting unit normal \(\xi\) so that

\[
a_p\cdot\xi\le0\qquad(p\in C_x).
\tag{137.2}
\]

For a contact \(p\),

\[
|x+t\xi-p|^2
=1-2t\,a_p\cdot\xi+t^2|\xi|^2\ge1.
\tag{137.3}
\]

If \(\{p,q\}\in E_x\), the two direction vectors cannot both be endpoints of
the containing semicircle: those endpoints are antipodal, whereas \(|p-q|=1\)
would require their angular separation to be \(\pi/3\).  Consequently at least one
of \(a_p\cdot\xi,a_q\cdot\xi\) is strictly negative.  Equation (137.3) then makes
at least one of the two sides of every newly created triangle strictly longer than
one for all sufficiently small \(t>0\).  All other pairs involving \(x\) have
strict separation slack and remain feasible after shrinking \(\epsilon\).  The
strict upper slack \(|x-p|<D\) likewise preserves the diameter bound.  Since \(P\)
was triangle-free, all triangles have been removed.

If the direction set is not contained in a closed semicircle, the planar separation
criterion gives

\[
c:=\min_{|u|=1}\max_{p\in C_x}a_p\cdot u>0.
\tag{137.4}
\]

For \(y=x+h\) with \(|h|>0\), choose \(p\in C_x\) with
\(a_p\cdot h\ge c|h|\).  Feasibility against that contact would require

\[
|a_p-h|^2\ge1
\quad\Longrightarrow\quad
a_p\cdot h\le\frac{|h|^2}{2},
\tag{137.5}
\]

which is impossible when \(0<|h|<2c\).  Thus \(x\) is locally isolated. \(\square\)

## 137.1 Consequence for a tree first transition

Consider the first triangle in the one-for-one swap sequence supplied by a tree
fundamental circuit.  Before that insertion the current set is triangle-free, so
the new point \(x\) is the only possible vertex of a newly created triangle.  If
\(x\) is non-diametral, Theorem 137.1 gives the exact alternative:

\[
\boxed{
\text{closed contact semicircle}\ \Longrightarrow\ \text{triangle-free global optimum
after a small perturbation};
}
\tag{137.6}
\]

whereas a first triangle that cannot be removed by a one-point perturbation must
come from a contact direction set that positively surrounds \(x\), hence from a
locally isolated exact-contact cage.  Unit separation gives at most six such
contacts, and at least three are needed in the surrounding case.  The latter
statement follows directly from the angular gaps: two directions always lie in a
closed semicircle.

This is a reduction of the non-diametral tree branch, not the required Target A
theorem.  It leaves three cases untouched:

1. the locally isolated exact-contact cage;
2. a first-triangle insertion at a diameter endpoint, where upper diameter
   constraints must be included in the displacement cone; and
3. cyclic or multi-point transition supports, where the first triangle can contain
   more than one newly inserted point.

## 137.2 Sharp local cage witness

The cage alternative is nonempty even with a triangle-free preceding set.  Take

\[
x=(0,0),
\quad
p_1=(1,0),
\quad
p_2=\left(\frac12,\frac{\sqrt3}{2}\right),
\quad
p_3=\left(-\frac{\sqrt3}{2},-\frac12\right).
\tag{137.7}
\]

The set \(P=\{p_1,p_2,p_3\}\) is unit-separated and triangle-free: \(|p_1-p_2|=1\),
while the other two pairwise distances are \(2\sin(5\pi/12)>1\).  Inserting \(x\)
creates the unit triangle \(xp_1p_2\).  The three contact directions satisfy

\[
(p_1-x)+(p_2-x)+\sqrt3\,(p_3-x)=0,
\tag{137.8}
\]

with all coefficients positive.  Hence they are not contained in a closed
semicircle, and Theorem 137.1 makes \(x\) locally isolated when the other points
are held fixed.  All distances from \(x\) are one, while the diameter of \(P\) is
\(2\sin(5\pi/12)>1\), so this witness is already in the non-diametral regime.

The witness is only local: it is not a global diameter certificate and supplies no
Schur nullity.  Therefore the exact remaining Target A implication is still

\[
\boxed{
\dim\ker S\ge\Delta_\Lambda-d_{\rm int},
}
\]

and the source-side alternative remains a Hall excess of at least
\(\widehat p_H+1\).  In particular, Theorem 137.1 does not justify promoting the
tree-circuit branch to either conclusion.

## 136.2 Compatible finite witnesses and exact source slack

The same transfer works for several separated finite witnesses and gives the exact
source-Hall threshold rather than only a one-point contradiction.  Let
\((S_i,T_i)_{i=1}^k\) be finite Kuperberg witnesses for one honeycomb gap packing,
with the \(S_i\) and \(T_i\) pairwise disjoint.  Let \(F\) be a finite unit-separated
set containing \(\bigcup_iS_i\), and assume

\[
\bigcup_iT_i\subset L,
\qquad
\left(F\setminus\bigcup_iS_i\right)\cup\bigcup_iT_i
\text{ is unit-separated},
\qquad
\left(F\setminus\bigcup_iS_i\right)\cap\bigcup_iT_i=\varnothing.
\tag{136.4}
\]

Then, directly,

\[
\left|
\left(F\setminus\bigcup_iS_i\right)\cup\bigcup_iT_i
\right|
=|F|+k.
\tag{136.5}
\]

If \(F=A\) is the genuine source in its hull \(H\), with
\(T_i\subset H\), the union \(Q=\bigcup_iT_i\) also satisfies

\[
N_A(Q)\subseteq\bigcup_iS_i,
\qquad
|Q|-|N_A(Q)|\ge k.
\tag{136.6}
\]

Indeed, the displayed replacement in (136.4) is unit-separated by hypothesis, and
pairwise disjointness gives the cardinality identity (136.5).  If
\(a\in A\setminus\bigcup_iS_i\) and \(t\in Q\), unit separation of the replacement
gives \(|a-t|\ge1\), so \(N_A(Q)\subseteq\bigcup_iS_i\).  Since
\(\sum_i(|T_i|-|S_i|)=k\), (136.6) follows.  Applying (119.8) proves (136.7).

Therefore the exact fixed-source bound forces

\[
\boxed{k\le\widehat p_H.}
\tag{136.7}
\]

This is the finite multi-witness form of the gap-concentration route.  It is useful
only after compatibility with the actual source points has been verified; separate
infinite witnesses need not be mutually compatible after insertion into a finite
configuration.  In particular, positive distributed clearance in the strained
monomer regression still supplies neither the witness sets nor their compatibility.


# 137. Finite concentration of homothetic monomer strain

Section 136 transfers a protected honeycomb gap of fixed positive width.  The
homothetic strained-monomer regression has no such gap at the pointwise scale: its
nearest-neighbor excess can be only \(\alpha/L\).  For a free rhombic patch, however,
the excess from \(L\) rows can be concentrated into one fixed-width internal gap
without leaving the original finite hull.

Normalize the triangular lattice as

\[
\Lambda=\mathbb Z e_1+\mathbb Z e_2,
\qquad
e_1=(1,0),
\qquad
e_2=\left(\frac12,\frac{\sqrt3}{2}\right),
\tag{137.1}
\]

and put

\[
h=\frac{\sqrt3}{2},
\qquad
n=(0,1).
\tag{137.2}
\]

For an integer \(L\ge1\), let

\[
R_L=\{ie_1+je_2:-L\le i,j\le L\}.
\tag{137.3}
\]

> **Theorem 137.1 (finite homothetic-strain concentration).**  Fix
> \(\eta>0\).  There is \(L_0(\eta)\) with the following property.  If
> \(L\ge L_0(\eta)\), \(\varepsilon>0\), and
> \[
> L\varepsilon\ge\eta,
> \tag{137.4}
> \]
> then, for
> \[
> P_L=(1+\varepsilon)R_L,
> \qquad
> H_L=\operatorname{conv}P_L,
> \tag{137.5}
> \]
> there is a unit-separated set \(P_L^+\subset H_L\) such that
> \[
> \boxed{|P_L^+|=|P_L|+1.}
> \tag{137.6}
> \]
> Thus a homothetically strained triangular patch whose accumulated strain
> \(L\varepsilon\) stays bounded away from zero is not completely saturated even
> relative to its own finite convex hull.

### Proof

Put

\[
a=\frac{h\eta}{2}.
\tag{137.7}
\]

Inside \(H_L\), replace the homothetic patch by the same number of points

\[
\begin{aligned}
Q_L^-&=\{ie_1+je_2-an:-L\le i\le L,\ -L\le j\le-1\},\\
Q_L^+&=\{ie_1+je_2+an:-L\le i\le L,\ 0\le j\le L\},\\
Q_L&=Q_L^-\cup Q_L^+.
\end{aligned}
\tag{137.8}
\]

Each half is a translate of a triangular-lattice half-patch.  For a point in the
upper half and one in the lower half, the vertical component of their difference is
positive before the translations and is increased by \(2a\).  The horizontal
component is unchanged.  Hence no cross-half distance decreases, and

\[
Q_L\text{ is unit-separated},
\qquad
|Q_L|=|P_L|=(2L+1)^2.
\tag{137.9}
\]

To check the container exactly, use

\[
n=-\frac1{2h}e_1+\frac1h e_2.
\tag{137.10}
\]

Thus adding \(an\) changes the two lattice coefficients by

\[
\left(-\frac{a}{2h},\frac ah\right)
=\left(-\frac\eta4,\frac\eta2\right),
\tag{137.11}
\]

and subtracting \(an\) changes them by the opposite vector.  Since

\[
H_L=(1+\varepsilon)\bigl([-L,L]e_1+[-L,L]e_2\bigr)
\tag{137.12}
\]

and its coefficient margin beyond \([-L,L]^2\) is
\(L\varepsilon\ge\eta\), (137.11) proves

\[
Q_L\subset H_L.
\tag{137.13}
\]

Let

\[
\mathcal H_a=
\{ie_1+je_2-an:j\le-1\}
\cup
\{ie_1+je_2+an:j\ge0\}.
\tag{137.14}
\]

This is, up to one global translation, the honeycomb packing with a linear gap of
width \(2a=h\eta>0\).  After rescaling their circle-center normalization, the
Kuperberg--Kuperberg--Kuperberg theorem quoted in Section 136 supplies finite sets
\(S\subset\mathcal H_a\) and \(T\subset\mathbb R^2\) such that

\[
|T|=|S|+1,
\qquad
(\mathcal H_a\setminus S)\cup T
\text{ is unit-separated},
\qquad
T\cap(\mathcal H_a\setminus S)=\varnothing.
\tag{137.15}
\]

The witness is finite.  Therefore, for all sufficiently large \(L\),

\[
S\subset Q_L,
\qquad
T\subset H_L.
\tag{137.16}
\]

The second inclusion holds because \(T\) is fixed while the centered parallelograms
\(H_L\) have inradius tending to infinity.  Now set

\[
P_L^+=(Q_L\setminus S)\cup T.
\tag{137.17}
\]

It is a subset of the unit-separated set in (137.15), lies in \(H_L\), and has

\[
|P_L^+|=|Q_L|-|S|+|T|=|P_L|+1.
\]

This proves the theorem. \(\square\)

The theorem applies in particular to the exact strain scale

\[
\varepsilon_L=\frac\alpha L,
\qquad \alpha>0,
\tag{137.18}
\]

that occurs in Regression 105.1.  Although every individual nearest-neighbor excess
tends to zero, the two half-patches in (137.8) expose a gap of the fixed width
\(h\alpha\) (or any smaller fixed width), after which one finite Kuperberg witness
fits for all sufficiently large \(L\).

There is also an immediate protected-subcontainer version.  If a finite packing
\(F\subset H\) contains an isometric copy of \(P_L\), its rhombic hull is contained
in \(H\), and

\[
\operatorname{dist}
\bigl(F\setminus P_L,\operatorname{conv}P_L\bigr)\ge1,
\tag{137.19}
\]

then the replacement (137.17) adds one point to \(F\) inside \(H\).  Condition
(137.19) is much stronger than the monomer-chamber information in the actual
scaffold.

## 137.1 Regression audit and exact limitation

Theorem 137.1 eliminates the **free homothetic rhombus** version of the
strained-monomer regression.  It does not eliminate the canonical Target A monomer
branch for the following exact reasons.

1. A monomer phase records strict-conflict combinatorics, not an exact homothetic
   copy of \((1+\varepsilon)\Lambda\).
2. The construction moves the whole rhombic patch, including its boundary rows.
   An embedded coherent domain may be locked to exterior source or scaffold points,
   and (137.19) is not available.
3. If \(L\varepsilon_L\to0\), the proof creates no fixed positive gap and gives no
   quantitative control on a vanishing-gap Kuperberg witness.
4. One compatible add-one witness does not yield the
   \(\widehat p_H+1\) fixed-source Hall deficiency required by (119.9), nor does it
   yield \(s\) independent Schur null directions.

Thus the remaining finite gap theorem is now more precise: one must concentrate
strain while preserving the actual exterior boundary constraints of a globally
derived monomer domain, or else extract enough mutually compatible witnesses to
exceed the exact source slack.


# 138. Simultaneous triangle breaking or an infinitesimally locked triangle

The first triangle-producing plateau transition can be sharpened without assuming
that its circuit is a tree.  The relevant alternative is an exact fixed-container
statement.

Let \(H\) be a convex polygon with nonempty interior and let

\[
P=\{p_1,\ldots,p_r\}\subset H
\tag{138.1}
\]

be unit-separated.  Let \(E_1(P)\) be its unit-contact edges and let
\(\mathcal T(P)\) be its unit equilateral triangles.  Write the facet inequalities
of \(H\) as

\[
n_f\cdot z\le c_f.
\tag{138.2}
\]

For a velocity \(v=(v_1,\ldots,v_r)\), put

\[
a_{ij}(v)=(p_i-p_j)\cdot(v_i-v_j).
\tag{138.3}
\]

Define the fixed-container expansive cone

\[
\mathcal C_H(P)=\left\{
v:
\begin{array}{ll}
a_{ij}(v)\ge0& (ij\in E_1(P)),\\
n_f\cdot v_i\le0& (n_f\cdot p_i=c_f)
\end{array}
\right\}.
\tag{138.4}
\]

For \(T\in\mathcal T(P)\), define

\[
\ell_T(v)=\sum_{ij\in E(T)}a_{ij}(v).
\tag{138.5}
\]

Every term in (138.5) is nonnegative on \(\mathcal C_H(P)\).

> **Theorem 138.1 (locked-triangle alternative).**  Suppose
> \(\mathcal T(P)\ne\varnothing\).  Exactly one of the following holds.
>
> 1. There is \(v\in\mathcal C_H(P)\) such that
>    \[
>    \ell_T(v)>0
>    \qquad(T\in\mathcal T(P)).
>    \tag{138.6}
>    \]
>    For every sufficiently small \(t>0\), the linearly perturbed configuration
>    \(P_t=\{p_i+tv_i\}\) is unit-separated, lies in \(H\), and is triangle-free.
> 2. There is a triangle \(T_\ast\in\mathcal T(P)\) such that
>    \[
>    \boxed{
>    a_{ij}(v)=0
>    \quad
>    (ij\in E(T_\ast),\ v\in\mathcal C_H(P)).
>    }
>    \tag{138.7}
>    \]
>    Thus all three sides of \(T_\ast\) are fixed to first order by every
>    fixed-container infinitesimally feasible motion.

### Proof

If alternative 2 fails, then for every \(T\in\mathcal T(P)\) there is
\(v^T\in\mathcal C_H(P)\) with \(\ell_T(v^T)>0\).  The set
\(\mathcal C_H(P)\) is a convex cone, so

\[
v=\sum_{T\in\mathcal T(P)}v^T
\tag{138.8}
\]

belongs to it.  Since every \(\ell_{T'}(v^T)\ge0\),

\[
\ell_{T'}(v)
\ge
\ell_{T'}(v^{T'})>0
\qquad(T'\in\mathcal T(P)),
\tag{138.9}
\]

which is alternative 1.

Conversely, if alternative 1 fails, the same summation argument shows that some
\(T_\ast\) must satisfy

\[
\ell_{T_\ast}(v)=0
\qquad(v\in\mathcal C_H(P)).
\tag{138.10}
\]

All three summands are nonnegative on the cone, so each is zero.  This gives
(138.7) and also proves mutual exclusivity.

It remains to justify the finite perturbation in alternative 1.  For a unit edge,

\[
\begin{aligned}
&|p_i+tv_i-p_j-tv_j|^2\\
&\qquad=
1+2t a_{ij}(v)+t^2|v_i-v_j|^2
\ge1.
\end{aligned}
\tag{138.11}
\]

Every noncontact pair has a positive finite slack, so it remains separated for all
sufficiently small \(t\).  The active facet inequalities in (138.4), together with
the positive slack at inactive facets, keep every point in \(H\).  For each original
unit triangle, (138.6) makes at least one side strictly longer than one.  Finally, a
triple which was not originally a unit triangle had at least one side strictly
longer than one, and the finitely many such strict inequalities persist for small
\(t\).  Hence no new unit triangle appears. \(\square\)

Apply this theorem to the first triangle-producing member \(P_j\) of the exact flag
in Section 124.  Since

\[
|P_j|=q+j,
\qquad
D(q+j)=D,
\qquad
P_j\subset H,
\tag{138.12}
\]

alternative 1 produces a triangle-free **global optimum at the same new
cardinality**.  In alternative 2, every triangle of \(P_j\), and hence the locked
triangle \(T_\ast\), contains a point of \(\Delta X_j\), because
\(P_{j-1}\) was triangle-free.

> **Corollary 138.2 (sharpened first-transition alternative).**  At the first bad
> source-capacity transition, either a fixed-container perturbation gives a
> triangle-free global optimum at cardinality \(q+j\), or the transition creates a
> unit triangle containing a newly inserted point whose three sides are universally
> first-order locked in the cone \(\mathcal C_H(P_j)\).

This conclusion applies equally to tree and cyclic circuits.  It is stronger than
the statement that every new triangle merely meets \(\Delta X_j\), but it supplies
one locked triangle, not \(s\) independent failures of the Schur linkage.


# 139. Interior cage geometry for a bad tree swap

The locked branch of Corollary 138.2 has a sharp one-vertex geometric shadow.  Let
\(P^-\subset H\) be triangle-free and unit-separated.  Suppose a tree-circuit leaf
swap removes \(b\in P^-\) and inserts \(x\), where

\[
|x-b|=r<1,
\qquad
|x-u|\ge1
\quad(u\in P^-\setminus\{b\}).
\tag{139.1}
\]

Let

\[
U_x=\{u\in P^-\setminus\{b\}:|x-u|=1\}.
\tag{139.2}
\]

If \(x\in\operatorname{int}H\) and the directions \(u-x\), \(u\in U_x\), lie in
an open semicircle, then there is a vector \(v\) for which

\[
(x-u)\cdot v>0
\qquad(u\in U_x).
\tag{139.3}
\]

Moving only \(x\) a sufficiently small positive distance in direction \(v\) breaks
all its unit contacts and hence every triangle created by that swap.  Therefore an
interior one-point obstruction requires the contact directions not to lie in an
open semicircle; equivalently their largest circular gap is at most \(\pi\).

The removed blocker forces a gap in the opposite direction.  If \(w=(b-x)/r\) and
\(u\in U_x\), then

\[
1\le|b-u|^2
=r^2+1-2r\,w\cdot(u-x),
\tag{139.4}
\]

so

\[
w\cdot(u-x)\le\frac r2.
\tag{139.5}
\]

Consequently the contact directions have an empty circular arc centered on \(w\)
of width

\[
\boxed{
2\arccos\frac r2>\frac{2\pi}{3}.
}
\tag{139.6}
\]

Thus every interior caged leaf event has a largest angular gap in the exact range

\[
\boxed{
\frac{2\pi}{3}<\gamma\le\pi.
}
\tag{139.7}
\]

If the event creates a triangle through \(x\), two contact directions are separated
by exactly \(\pi/3\).  These conditions are compatible; they do not yield a local
contradiction.

The boundary alternative is genuinely boundary-order.  If \(x\in\partial H\), then
(139.1) gives \(\operatorname{dist}(b,\partial H)<1\).  The boundary-layer estimate
(72.12), applied to any unit-separated source extension in the same diameter-\(D\)
hull, bounds the number of such blocker positions by \(12D+9\).  This does not show
that the first bad leaf in a chosen elimination order has a deep blocker.

## 139.1 Exact two-leaf cage regression

The interior interval (139.7) is nonempty even for the smallest tree circuit.  The
following family rules out a leaf-ordering or one-point-perturbation proof based only
on tree-circuit geometry.

For

\[
\frac\pi3<\theta<\frac\pi2,
\qquad
c=\cos\theta,
\qquad
a=\frac34+\frac c2,
\tag{139.8}
\]

put \(u_\phi=(\cos\phi,\sin\phi)\),

\[
x_-=(-a,0),
\qquad
x_+=(a,0),
\qquad
b=(0,0),
\tag{139.9}
\]

and define the angle sets

\[
\begin{aligned}
L_\theta&=\left\{\theta,\frac{5\pi}{6},\frac{7\pi}{6},2\pi-\theta\right\},\\
R_\theta&=\left\{\frac\pi6,\pi-\theta,\pi+\theta,\frac{11\pi}{6}\right\}.
\end{aligned}
\tag{139.10}
\]

Let

\[
B=\{b\}
\cup\{x_-+u_\phi:\phi\in L_\theta\}
\cup\{x_++u_\phi:\phi\in R_\theta\},
\qquad
C=\{x_-,x_+\}.
\tag{139.11}
\]

> **Proposition 139.1 (two-leaf caged circuit).**  The sets \(B\) and \(C\) are
> internally unit-separated, \(B\) is triangle-free, and the strict conflict graph
> from \(C\) to \(B\) is the three-vertex path
> \[
> x_- - b - x_+.
> \tag{139.12}
> \]
> Hence \(C\) is a two-element transversal-matroid circuit whose contracted
> right shore has one degree-two blocker.  Both possible leaf swaps create a unit
> triangle, and the inserted leaf is infinitesimally pinned when the eight cage
> points are held fixed.

### Proof

Within the left cage, the consecutive angular gaps are

\[
\frac{5\pi}{6}-\theta,
\quad
\frac\pi3,
\quad
\frac{5\pi}{6}-\theta,
\quad
2\theta.
\tag{139.13}
\]

All are at least \(\pi/3\), with equality only for the middle pair.  The same holds
for the reflected right cage.  Thus the only unit edges internal to the two cages
are the pairs at angles \(5\pi/6,7\pi/6\) and \(\pi/6,11\pi/6\).

Every left-cage point has horizontal coordinate at most \(-a+c\), while every
right-cage point has horizontal coordinate at least \(a-c\).  Their cross distance
is therefore at least

\[
2(a-c)=\frac32-c>1.
\tag{139.14}
\]

For either of the two left-cage points directed toward \(b\),

\[
|b-(x_-+u_\phi)|^2=a^2-2ac+1>1,
\tag{139.15}
\]

because

\[
a-2c=\frac34-\frac{3c}{2}>0.
\tag{139.16}
\]

The two outward points are still farther; the right side is symmetric.  This proves
that \(B\) is unit-separated and that its unit graph consists of two disjoint edges,
so it is triangle-free.

Now \(|x_--x_+|=2a>1\), while

\[
|x_\pm-b|=a<1.
\tag{139.17}
\]

Each \(x_\pm\) is exactly unit distance from its own four cage points.  Its distance
to every point of the opposite cage is greater than one: the minimum horizontal
separation is

\[
2a-c=\frac32.
\tag{139.18}
\]

Thus (139.12) is the complete strict conflict graph.

After swapping \(b\) for \(x_-\), the latter and the left-cage points at angles
\(5\pi/6,7\pi/6\) form a unit equilateral triangle.  The symmetric statement holds
for \(x_+\).  Finally, the largest gap among the four contact directions in either
cage is \(2\theta<\pi\).  Their positive cone is all of \(\mathbb R^2\), so the
polar cone of one-point noncontracting velocities is \(\{0\}\).  Each inserted
leaf is infinitesimally pinned. \(\square\)

As \(\theta\downarrow\pi/3\), the strict blocker length \(a\) tends to one, the
cross-cage minimum (139.14) tends to one, and the nearest blocker-to-cage distances
in (139.15) tend to one.  Hence no uniform strict-margin charge can be extracted from
this local tree event.

This is an exact local regression, not a global minimizer or a finite-container
capacity endpoint.  It does not defeat Corollary 138.2: allowing the whole
configuration to move is strictly stronger than moving the inserted leaf while its
cage is fixed.


# 140. Post-continuation Target A status

The new results narrow two preferred attacks but do not close Target A.

1. The fixed positive-gap transfer of Section 136 now extends to the vanishing
   pointwise strain \(\varepsilon_L=\alpha/L\) for a free homothetic rhombus.  What
   remains is the exterior-compatible concentration theorem for a globally derived
   monomer subdomain.
2. Every first triangle-producing exchange now has an exact alternative: a
   triangle-free same-cardinality global perturbation, or a newly supported unit
   triangle universally locked to first order in the fixed hull.
3. In the tree branch, a deep blocker forces the locked inserted vertex into the
   angular cage (139.7).  Proposition 139.1 shows that neither leaf ordering nor a
   one-point perturbation eliminates that cage from local circuit geometry alone.

The exact missing implication is therefore one of the following.

\[
\boxed{
\begin{array}{l}
\text{Transport the locked first-transition triangle(s) to at least }s
\text{ independent failures of the}\ C^\partial\!\to O
\text{ alternating linkage};\\[2mm]
\text{or produce exterior-compatible finite gap witnesses whose source Hall}\
\text{deficiency is at least }\widehat p_H+1.
\end{array}}
\tag{140.1}
\]

Neither transport is supplied here.  In particular, one locked triangle need not
give one Schur null direction, locked triangles from different circuit orderings
need not be independent, and the free-rhombus rearrangement can violate all of the
actual boundary contacts of an embedded monomer domain.

Accordingly the authoritative endpoint remains

\[
\boxed{
\dim\ker S\ge\Delta_\Lambda-d_{\rm int},
}
\tag{140.2}
\]

equivalently

\[
\boxed{
\operatorname{rank}S
\le d_{\rm int}+|C^\partial|-\Delta_\Lambda.
}
\tag{140.3}
\]

**LEVEL I STATUS: STILL OPEN.  TARGET A REMAINS UNRESOLVED.**

# 137. First-transition incidence bound for retained strict rattlers

The source-capacity flag gives one further exact restriction on the first
triangle-producing transition.  It distinguishes a triangle supported by the
retained strict-rattler population from one supported entirely by the exchanged
backbone; the latter remains uncontrolled here.

Use the notation of Sections 124 and 135.  Thus \(B\) is triangle-free,
\(P_i=(B\setminus W_i)\cup U_i\), \(X\) is the capacity endpoint, and \(j\) is the
first index for which \(P_j\) contains a unit equilateral triangle.  Let

\[
R\subseteq B
\]

be a set of strict rattlers of \(B\), meaning

\[
|r-b|>1\qquad(r\in R, b\in B\setminus\{r\}).
\tag{137.1}
\]

Put

\[
R_j:=R\cap(B\setminus W_j),
\qquad
a_j:=|\Delta X_j|.
\tag{137.2}
\]

Let \(\mathcal T_j(R)\) be the set of unit equilateral triangles in \(P_j\) that
contain a point of \(R_j\).  Since \(P_{j-1}\) is triangle-free, these are all
new triangles at this transition.

> **Theorem 137.1 (retained-rattler incidence bound).** Every triangle in
> \(\mathcal T_j(R)\) contains exactly one point of \(R_j\) and two points of
> \(U_j\).  The two \(X\)-points form a unit edge of the unit-contact graph of
> \(X\), and that edge has at least one endpoint in \(\Delta X_j\).  Consequently
> \[
> \boxed{
> |\mathcal T_j(R)|\le 2e_X(\Delta X_j)\le 12|\Delta X_j|,
> }
> \tag{137.3}
> \]
> where \(e_X(\Delta X_j)\) is the number of unit edges of \(X\) incident to
> \(\Delta X_j\).  In addition, the number of new unit contacts between
> \(R_j\) and \(\Delta X_j\) is at most \(6|\Delta X_j|\).

### Proof

Take \(T\in\mathcal T_j(R)\), and let \(r\in R_j\) be a rattler in \(T\).  The
other vertices of \(T\) cannot be distinct points of \(B\): by (137.1) they would
be at distance strictly greater than one from \(r\).  They therefore both lie in
\(U_j\).  A point of \(U_j\) cannot coincide with \(r\), because then \(r\) would
belong to \(W_j=N_B(U_j)\) and would not be in \(R_j\).  The triangle cannot contain
two points of \(R_j\), since two distinct points of \(R\subseteq B\) are strictly
more than one apart.  This proves the first assertion.

Write the two \(X\)-vertices as \(x,y\).  They are a unit edge of \(X\).  If both
belonged to \(U_{j-1}\), the same triangle would already lie in \(P_{j-1}\), so at
least one belongs to \(\Delta X_j\).

For a fixed unit edge \(xy\), the equations

\[
|z-x|=|z-y|=1
\]

have at most two solutions in the plane.  Thus at most two rattler triangles can be
assigned to the same \(X\)-edge.  The unit-contact graph of a unit-separated planar
set has maximum degree six: the angular gaps between unit neighbors of any point are
at least \(60^\circ\).  Hence

\[
e_X(\Delta X_j)\le
\sum_{x\in\Delta X_j}\deg_X(x)\le6|\Delta X_j|,
\]

which proves (137.3).  Finally, a fixed \(x\in\Delta X_j\) has at most six points
of the unit-separated set (R_j) at distance exactly one, giving the last claim. ∎

For the first flag step, \(U_0=\varnothing\).  In particular, if
\(|\Delta X_1|=1\), its first triangle cannot contain a retained strict rattler:
such a triangle would require two \(X\)-vertices.  More generally, Theorem 137.1
shows that a rattler-supported first triangle is a two-capacity-point event; a
one-capacity-point first triangle is necessarily supported by the non-rattler
backbone.

This does not close Target A.  The bound is only an upper bound on rattlers that are
actually used by the first triangle; no theorem forces a positive fraction of the
retained rattlers to participate, and \(|\Delta X_j|\) is not bounded by the number
of flag increments.  A first triangle can therefore be supported entirely away from
\(R_j\), including in the strained-monomer or regular-shell regressions.  No Schur
separator or source-Hall surplus follows from (137.3).

The exact remaining implication is still

\[
g>0\Longrightarrow
\exists Q\subset H\text{ unit-separated with }
|Q|-|N_A(Q)|\ge\widehat p_H+1,
\]

equivalently

\[
\dim\ker S\ge\Delta_\Lambda-d_{\rm int}.
\]

**LEVEL I STATUS: STILL OPEN.  TARGET A REMAINS UNRESOLVED.**


# 141. Exact multi-layer capacity of a homothetic monomer patch

The free homothetic-strain regression admits a sharper finite statement than the
one-site witness in Section 137. It is elementary, exact, and does not invoke an
infinite packing theorem.

Let \(e_1,e_2\) be unit vectors with \(e_1\cdot e_2=1/2\). For an integer
\(L\ge2\) and \(\varepsilon>0\), set

\[
P_{L,\varepsilon}
=(1+\varepsilon)
\{ie_1+je_2:0\le i,j\le L-1\},
\qquad
H_{L,\varepsilon}=\operatorname{conv}P_{L,\varepsilon}.
\tag{141.1}
\]

Define the exact number of exposed lattice layers by

\[
r=\left\lfloor\varepsilon(L-1)\right\rfloor.
\tag{141.2}
\]

> **Theorem 141.1 (multi-layer lattice capacity).** The triangular-lattice patch
> \[
> Q_{L,r}
> =\{ie_1+je_2:0\le i,j\le L-1+r\}
> \]
> is contained in \(H_{L,\varepsilon}\), is unit-separated, and satisfies
> \[
> \boxed{
> |Q_{L,r}|=(L+r)^2
> =L^2+2Lr+r^2,
> }
> \tag{141.3}
> \]
> and
> \[
> \boxed{
> \operatorname{diam}(Q_{L,r})^2
> =3(L+r-1)^2
> \le
> 3(1+\varepsilon)^2(L-1)^2
> =\operatorname{diam}(P_{L,\varepsilon})^2.
> }
> \tag{141.4}
> \]

### Proof

The hull is the coordinate parallelogram

\[
H_{L,\varepsilon}
=\{ae_1+be_2:0\le a,b\le(1+\varepsilon)(L-1)\}.
\tag{141.5}
\]

By (141.2),

\[
L-1+r
\le L-1+\varepsilon(L-1)
=(1+\varepsilon)(L-1),
\]

so every point of \(Q_{L,r}\) lies in the parallelogram. For distinct lattice
points, the difference \(ie_1+je_2\) has squared length
\(i^2+ij+j^2\ge1\), so \(Q_{L,r}\) is unit-separated.

The same quadratic form is maximized over the coordinate rectangle at opposite
corners. Its largest difference has coordinates
\((L+r-1,L+r-1)\), giving the first equality in (141.4). The second follows from
the definition of \(r\). The original patch has opposite-corner difference
\((1+\varepsilon)(L-1)(e_1+e_2)\), whose squared length is the final expression.
\(\square\)

The gain is quantized:

\[
\boxed{
r\ge1
\Longrightarrow
|Q_{L,r}|-|P_{L,\varepsilon}|
=2Lr+r^2\ge2L+1.
}
\tag{141.6}
\]

For the strain scale \(\varepsilon=\alpha/L\), one has
\(r=\lfloor\alpha(1-1/L)\rfloor\). Thus the elementary rectangular lattice
candidate sees no new integer layer when \(0<\alpha<1\), and sees at least one
complete layer only when \(\alpha\ge L/(L-1)\). This is an exact statement about
this candidate orientation; it does not rule out a nonlattice rearrangement.

> **Corollary 141.2 (protected multi-site exchange).** Let \(\Omega\) be an open
> set with \(\operatorname{diam}\Omega<D\), and let \(F\subset\Omega\) be a
> unit-separated finite set containing \(P_{L,\varepsilon}\). If \(r\ge1\),
> \(Q_{L,r}\subset\Omega\), and
> \[
> (F\setminus P_{L,\varepsilon})\cup Q_{L,r}
> \]
> is a disjoint unit-separated union, then it has
> \[
> |F|+2Lr+r^2
> \]
> points and diameter strictly below \(D\). In particular, \(F\) cannot be an
> \(N\)-point global minimizer with \(D(N)=D\).

The corollary isolates a genuine finite frontier advance. A homothetic monomer
patch with one accumulated lattice spacing of coordinate slack carries
\(2L+1\) extra sites, not merely one. The unresolved Target A issue is precisely
the missing protection hypothesis: a monomer domain extracted from the actual
source may be coupled to exterior points, so its enlarged lattice candidate need
not be separated from the exterior.

**LEVEL I STATUS: STILL OPEN. TARGET A REMAINS UNRESOLVED.**

# 146. Exact free-sink lower bound from scaffold cell unions

Retain the inner lattice shore \(Y_{\rm in}\), the blocker set \(X\), and the
strict conflict graph \(G\) from the scaffold construction.  Assume the established
no-boundary-truncation identity \(N_G(x)=N_\Lambda(x)\), together with the complete
local blocker classification from Section 79: for every \(x\in X\),

\[
N_\Lambda(x)=\{y\in\Lambda_v:|y-x|<1\}
\]

has either three vertices forming an elementary unit triangle or four vertices
forming an elementary unit lozenge.  Write

\[
C_x=\operatorname{conv}N_\Lambda(x).
\tag{146.1}
\]

The cell geometry gives the exact lattice trace

\[
\boxed{\Lambda_v\cap C_x=N_\Lambda(x).}
\tag{146.2}
\]

Indeed, every vertex of \(C_x\) lies in the open unit disk \(B(x,1)\), and the
open disk is convex, so \(C_x\subset B(x,1)\).  The classified elementary triangle
and elementary lozenge contain no lattice points other than their displayed
vertices, which proves the reverse inclusion in (146.2).

Define the geometric free-sink set

\[
Y_{\rm free}
=Y_{\rm in}\setminus\bigcup_{x\in X}C_x.
\tag{146.3}
\]

> **Theorem 146.1 (cell-union free-sink bound).** Under the preceding
> classification and with \(N_G(\cdot)\) denoting right neighborhoods in \(G\),
> \[
> \boxed{
> Y_{\rm free}=Y_{\rm in}\setminus N_G(X),
> \qquad
> N_G(Y_{\rm free})=\varnothing,
> }
> \tag{146.4}
> \]
> and consequently
> \[
> \boxed{
> h(G)\ge |Y_{\rm free}|.
> }
> \tag{146.5}
> \]
> In particular, any survivor satisfying \(h(G)\le j-1\) must obey
> \[
> \boxed{|Y_{\rm free}|\le j-1.}
> \tag{146.6}
> \]

### Proof

By (146.2),

\[
Y_{\rm in}\cap\bigcup_{x\in X}C_x
=\bigcup_{x\in X}\bigl(Y_{\rm in}\cap C_x\bigr)
=\bigcup_{x\in X}N_\Lambda(x)
=N_G(X).
\]

Taking complements inside \(Y_{\rm in}\) proves the first identity in (146.4).
The second follows because no blocker has a strict conflict edge to a site outside
its own cell, so a site in \(Y_{\rm free}\) has right degree zero.  The established
Hall-deficiency formula

\[
h(G)=\max_{Q\subseteq Y_{\rm in}}\bigl(|Q|-|N_G(Q)|\bigr)
\]

then gives (146.5) by choosing \(Q=Y_{\rm free}\).  The final implication is
immediate. \(\square\)

The bound is exact for the degree-zero part of the right shore, but it does not
control the remaining Hall deficiency generated by overlapping neighborhoods or
long narrow lattice-hole-free regions.  Thus it is a measurable source-side
constraint, not the missing \(h(G)\ge j\) theorem.  The exact lattice-trace and
free-sink operations are regression-tested in
research/cell_union_certificate.py.

**LEVEL I STATUS: STILL OPEN. TARGET A REMAINS UNRESOLVED.**

# 147. Exact alternating Hall-core decomposition

Let \(\mathcal I\) be the bipartite incidence graph whose left vertices are the
selected scaffold cells and whose right vertices are their incident lattice sites.
Fix a maximum matching \(\mu\).  Orient every unmatched incidence edge from left to
right and every matching edge from right to left, and start an alternating search
at every unmatched left vertex.

> **Theorem 147.1 (alternating Hall-core decomposition).** Let \(S\) be the set of
> left vertices reached by this search and \(N(S)\) its right neighborhood.  Then
> \[
> \boxed{|S|-|N(S)|=|\{\text{unmatched left roots}\}|=d_{\rm sc}.}
> \tag{147.1}
> \]
> The connected components of the induced incidence graph on
> \(S\cup N(S)\) have strictly positive deficiencies, and those component
> deficiencies add to \(d_{\rm sc}\).  If the components are
> \(S_\ell,R_\ell\), then
> \[
> \boxed{d_\ell:=|S_\ell|-|R_\ell|\ge1,
> \qquad d_{\rm sc}=\sum_\ell d_\ell.}
> \tag{147.2}
> \]
> Applying the exact cell-complex charge identity to each component gives
> \[
> \boxed{
> 12d_\ell=\sum_{v\in R_\ell}
> \bigl(4p_v(S_\ell)+3q_v(S_\ell)-12\bigr).
> }
> \tag{147.3}
> \]

### Proof

Every reached left vertex is either an unmatched root or is reached through the
matching edge of a reached right vertex.  Thus every nonroot left vertex is matched
by \(\mu\) to a distinct vertex of \(N(S)\), while no root is matched.  Conversely,
the matching edge of each nonroot left vertex is already reached, and every
unmatched incidence edge from a reached left vertex is traversed.  Therefore every
right neighbor of \(S\) is reached, so the matching restricts to an injection
\[
S\setminus\{\text{roots}\}\hookrightarrow N(S)
\]
whose image has size \(|S|-|\text{roots}|\).  It follows that
\[
|S|-|N(S)|=|\text{roots}|.
\]
The maximum matching leaves exactly \(d_{\rm sc}\) left vertices unmatched, and the
alternating witness is a maximum Hall-deficiency witness, proving (147.1).

Every reached vertex has an alternating path from a root, so each connected
component contains at least one root.  Within one component the same matching
count gives deficiency equal to its number of roots, hence positive.  Summing over
components gives (147.2).  Applying (89.6) to the selected cells in one component
gives (147.3). \(\square\)

This decomposition is a matching statement, not an assertion that geometric
interface charges are spatially additive.  Fundamental circuits can overlap
inside one component, and a remote neutral or negative-charge region can change the
raw charge of a full selected family without removing a deficient Hall core.  The
components are disjoint inside the induced witness, but a cell outside \(S\) may
still be adjacent in the full graph to a lattice vertex in \(N(S)\).  Thus the
decomposition does not provide spatial isolation or source-to-Schur transport.

It does give a non-overlapping exact reformulation of the Target A inequality:

\[
\boxed{\sum_\ell d_\ell\ge\Delta_\Lambda.}
\tag{147.4}
\]

The exact implementation and disconnected/remote-core regressions are in
research/scaffold_cells.py and research/test_scaffold_cells.py.  No source-side
argument currently forces (147.4).

**LEVEL I STATUS: STILL OPEN. TARGET A REMAINS UNRESOLVED.**

# 145. Exact bad-cell hazard masking

The cellwise covering criterion can be used locally rather than imposed on every
cell.  Let \(C_{ij}\) be the closed coordinate cell between
\(x_i e_1+y_j e_2\), \(x_{i+1}e_1+y_j e_2\), \(x_i e_1+y_{j+1}e_2\), and
\(x_{i+1}e_1+y_{j+1}e_2\).  Define the bad-cell index set

\[
\mathcal B
=\{(i,j):\sigma_{ij}\ge3\},
\tag{145.1}
\]

where \(\sigma_{ij}\) is (144.1).  Write \(H=\operatorname{conv}P\),
\(K_1=\lfloor X\rfloor\), and \(K_2=\lfloor Y\rfloor\).  The finite
bad-cell-safe candidate set is

\[
\mathcal Q_{\mathrm{safe}}
=\left\{
x_0e_1+y_0e_2+ae_1+be_2:
\begin{array}{l}
a,b\in\mathbb Z,\quad 0\le a\le K_1,\quad 0\le b\le K_2,\\
\operatorname{dist}(q,\partial H)\ge1,\quad
\operatorname{dist}(q,C_{ij})\ge1\ \text{for every }(i,j)\in\mathcal B
\end{array}
\right\}.
\tag{145.2}
\]

> **Theorem 145.1 (local bad-cell protection).** Let \(F\supseteq P\) be a
> unit-separated finite set.  Every point of
> \(\mathcal Q_{\mathrm{safe}}\) is at distance at least one from
> \(F\setminus P\).  The points of \(\mathcal Q_{\mathrm{safe}}\) are mutually
> unit-separated as well.

### Proof

The integer sites in (145.2) lie in the triangular lattice, so their mutual
distances are at least one.  Let \(z\in F\setminus P\).  If
\(z\notin\operatorname{int}H\), a segment from \(q\in\mathcal Q_{\mathrm{safe}}\)
to \(z\) would cross \(\partial H\) before reaching \(z\).  The boundary
condition in (145.2) therefore rules out \(|q-z|<1\).

Now suppose \(z\in\operatorname{int}H\).  The closed cells \(C_{ij}\) cover
\(H\).  If \(z\) belonged to a cell with \(\sigma_{ij}<3\), the strict
cellwise covering theorem would put \(z\) within distance \(<1\) of a point of
\(P\), contradicting the unit separation of \(F\).  Hence \(z\) belongs to a
bad cell \(C_{ij}\), and the second condition in (145.2) gives
\(|q-z|\ge1\).  Thus every cross-distance is at least one. \(\square\)

> **Corollary 145.2 (finite exchange with localized defects).** If
> \(\lvert\mathcal Q_{\mathrm{safe}}\rvert\ge L^2=\lvert P\rvert\) and an open
> set \(\Omega\) of diameter \(<D\) contains
> \((F\setminus P)\cup\mathcal Q_{\mathrm{safe}}\), then \(F\) is not a global
> \(N\)-point minimizer with \(D(N)=D\).

This criterion strictly contains the all-good and hull-isolated cases.  It does
not declare a bad cell occupied; it treats its entire closed region as a possible
blocker and removes only lattice sites within one unit of that region.  The
distance tests are exact: in oblique coordinates, projection to a cell edge has
rational parameter, so squared distances are computed by the quadratic form
\(u^2+uv+v^2\).

The executable regression includes a nontrivial localized-defect example.  For
\(L=15\), take \(x_i=(9/5)i\) for \(0\le i<15\), take
\(y_j=j\) for \(0\le j\le13\), and set \(y_{14}=13+9/5\).  There are fourteen
bad cells in the final \(y\)-row, while
\[
\lvert\mathcal Q_{\mathrm{safe}}\rvert=230>225=L^2.
\]
The candidate diameter still fits the source diameter.  Thus a single
localized bad row does not consume all finite replacement capacity.  The
remaining Target A gap is structural: the scaffold currently provides local
monomer/dimer cells, but no theorem turns a large scaffold region into a
rectilinear patch with a controlled bad-cell mask and enough safe sites.

\[
\boxed{\text{LEVEL I STATUS: STILL OPEN. TARGET A REMAINS UNRESOLVED.}}
\]

# 144. Interior blocker exclusion for coherent product patches

The protected capacity statements above can be strengthened on the source side
when the coherent region is an actual product patch with small enough local gaps.
Let

\[
P=\{x_i e_1+y_j e_2:0\le i,j<L\}
\]

be as in Theorem 142.1, and write

\[
a_i=x_{i+1}-x_i,\qquad b_j=y_{j+1}-y_j.
\]

For each coordinate cell define its short-diagonal squared length

\[
\sigma_{ij}=a_i^2-a_i b_j+b_j^2.
\tag{144.1}
\]

> **Theorem 144.1 (strict closed-hull unit covering).** If
> \(\sigma_{ij}<3\) for every cell, then
> \[
> \boxed{
> \operatorname{conv}P
> \subseteq
> \bigcup_{p\in P}B(p,1).
> }
> \tag{144.2}
> \]
> Consequently, if \(F\supseteq P\) is unit-separated, then
> \[
> \boxed{
> (F\setminus P)\cap\operatorname{conv}P=\varnothing.
> }
> \tag{144.3}
> \]

### Proof

The cell with side vectors \(a_i e_1\) and \(b_j e_2\) is split along its short
diagonal \(a_i e_1-b_j e_2\).  Both resulting triangles have side lengths

\[
a_i,\qquad b_j,\qquad d_{ij}=\sqrt{\sigma_{ij}},
\]

and the angle between the first two sides is \(60^\circ\).  The gap hypotheses in
Theorem 142.1 give \(a_i,b_j\ge1\).  The strict inequality
\(\sigma_{ij}<3\) implies \(a_i,b_j<2\): for example, if \(a_i\ge2\), minimizing
\(a_i^2-a_i b+b^2\) over \(b\ge1\) gives a value at least \(3\), and the other
coordinate is symmetric.  Hence all three sides are below two and

\[
d_{ij}<\sqrt3.
\]

The covering radius of the three vertices of a triangle with included angle
\(60^\circ\) is at most its circumradius in the acute case and at most half its
longest side in the obtuse case.  Here the circumradius is

\[
R_{ij}=\frac{d_{ij}}{2\sin60^\circ}
=\frac{d_{ij}}{\sqrt3}<1,
\]

while the half-longest-side bound is also \(<1\).  Thus every point of either
closed triangle is strictly within one unit of one of its vertices.  The cell
triangulations cover the closed product hull, proving (144.2).  If a point of
\(F\setminus P\) lay in the closed hull, (144.2) would put it at distance \(<1\) from
some point of P, contradicting unit separation.  \(\square\)

The threshold is sharp.  In a cell with \(a=b=\sqrt3\), the short diagonal has
squared length \(3\), and the circumcenter of one of the two equilateral triangles
is at distance exactly one from its three vertices.  Thus an interior point can
first appear at the equality threshold.

> **Corollary 144.2 (source-side isolation criterion).** A coherent rectilinear
> source patch whose every local gap pair satisfies (144.1) with strict inequality
> cannot coexist with any other source point in its closed product hull.  Therefore,
> every other source point lies strictly outside the patch hull.  Combining this with
> Theorem 143.1 gives a protected
> same-cardinality replacement whenever the two-layer-buffered lattice core has at
> least as many sites as the patch.

This is the first exact source-side transfer in the rectilinear model, but its
hypothesis is materially stronger than the actual Target A data: a monomer cell
records a local three- or four-site conflict region, not a globally coherent
product coordinate patch.  The theorem therefore narrows the missing bridge without
proving that the scaffold supplies it.  In particular, the Target A endpoint

\[
\operatorname{rank}S
\le d_{\rm int}+|C^\partial|-\Delta_\Lambda
\]

and the Level I status remain unchanged.

**LEVEL I STATUS: STILL OPEN. TARGET A REMAINS UNRESOLVED.**
# 143. Boundary-buffered finite exchange

The coordinate-span theorem gives an explicit way to absorb exterior interference
when the rest of the packing lies outside the product hull.  Retain the notation of
Theorem 142.1, put

\[
K_1=\lfloor X\rfloor,\qquad K_2=\lfloor Y\rfloor,
\tag{143.1}
\]

and define the deep candidate core

\[
Q^\circ
=\{x_0e_1+y_0e_2+ae_1+be_2:
2\le a\le K_1-2,\ 2\le b\le K_2-2,\ a,b\in\mathbb Z\}.
\tag{143.2}
\]

An empty index interval contributes no points.  Thus

\[
\boxed{
|Q^\circ|
=\bigl(K_1-3\bigr)_+\bigl(K_2-3\bigr)_+,
}
\qquad (r)_+:=\max\{r,0\}.
\tag{143.3}
\]

> **Theorem 143.1 (automatic exterior protection).** Every point of \(Q^\circ\)
> has Euclidean distance at least \(\sqrt3\) from the boundary of
> \(\operatorname{conv}P\).  If \(E\) is any set contained in the complement of
> \(\operatorname{int}(\operatorname{conv}P)\), then
> \[
> \boxed{\operatorname{dist}(Q^\circ,E)>1}
> \tag{143.4}
> \]
> whenever \(E\) is disjoint from \(Q^\circ\).  In particular, no strict conflict
> can connect \(Q^\circ\) to a point outside the open product hull.

### Proof

Write a point of \(Q^\circ\) as \(x_0e_1+y_0e_2+ae_1+be_2\).  Its perpendicular
distance from the two supporting lines with fixed first coordinate is
\(\frac{\sqrt3}{2}a\) and
\(\frac{\sqrt3}{2}(X-a)\), respectively.  The analogous distances for the second
coordinate are
\(\frac{\sqrt3}{2}b\) and
\(\frac{\sqrt3}{2}(Y-b)\).  The index restrictions and
\(K_1\le X<K_1+1,\ K_2\le Y<K_2+1\) make all four quantities at least
\(\sqrt3\).
The distance to each side segment is no smaller than the distance to its supporting
line, so the distance to the boundary is at least \(\sqrt3\).

If \(e\notin\operatorname{int}(\operatorname{conv}P)\), the segment from a point of
\(Q^\circ\) to \(e\) meets the boundary of the convex hull before reaching \(e\).
The distance from the \(Q^\circ\)-point to that boundary intersection is at most
the full segment length.  Since the former is at least \(\sqrt3>1\), the latter
cannot be less than one.  \(\square\)

The preceding argument yields a finite exchange criterion without checking every
cross-distance individually.

> **Corollary 143.2 (boundary-buffered protected replacement).** Let \(F\) be an
> \(N\)-point unit-separated set, let \(P\subset F\) be the rectilinear patch of
> Theorem 142.1, and suppose \(F\setminus P\) is contained in the complement of
> \(\operatorname{int}(\operatorname{conv}P)\).  If
> \[
> |Q^\circ|\ge L^2
> \tag{143.5}
> \]
> and there is an open set \(\Omega\) of diameter \(<D\) containing
> \((F\setminus P)\cup Q^\circ\), then \(F\) cannot be a global \(N\)-point
> minimizer with \(D(N)=D\).

Indeed, choose \(L^2\) sites from \(Q^\circ\).  They are mutually unit-separated by
the lattice property, and Theorem 143.1 separates them from \(F\setminus P\).  The
replacement has \(N\) points in \(\Omega\), hence diameter \(<D\), a contradiction.

The numerical layer condition is transparent.  If \(r_1,r_2\) are the complete
layers from (142.4), then

\[
|Q^\circ|
=\bigl(L+r_1-4\bigr)_+\bigl(L+r_2-4\bigr)_+.
\tag{143.6}
\]

Therefore \(r_1,r_2\ge4\) is sufficient for a same-cardinality replacement,
independently of \(L\).  In the one-sided square case \(r_1=0\) and \(L>4\), the
exact sufficient threshold is

\[
\boxed{
r_2\ge
\left\lceil4+\frac{4L}{L-4}\right\rceil.
}
\tag{143.7}
\]

For \(L=10\), this is \(r_2\ge11\), matching the executable regression.

This is a genuine finite transfer of accumulated strain into a replacement even in
the presence of arbitrary exterior points, but only under the strong hull-isolation
hypothesis \(F\setminus P\subseteq\operatorname{conv}P\setminus
\operatorname{int}(\operatorname{conv}P)\).  A source-derived monomer domain may
have other source points inside its product hull, and the source-capacity argument
does not currently exclude that.  Thus Theorem 143.1 does not yet imply the Target A
Schur-rank inequality.

The exact remaining endpoint is still

\[
\boxed{
\operatorname{rank}S
\le d_{\rm int}+|C^\partial|-\Delta_\Lambda,
}
\]

equivalently \(h(G)\ge j\).

**LEVEL I STATUS: STILL OPEN. TARGET A REMAINS UNRESOLVED.**

# 142. Exact protected capacity for nonuniform rectilinear strain

The multi-layer calculation of Section 141 does not require equal spacing or a
common homothety.  The following finite statement isolates the coordinate-product
part of a possible gap-concentration argument.

Let \(e_1,e_2\) be unit vectors with \(e_1\cdot e_2=1/2\).  Fix \(L\ge2\), and let

\[
x_0<\cdots<x_{L-1},\qquad y_0<\cdots<y_{L-1},
\tag{142.1}
\]

be real coordinate chains whose consecutive gaps are at least one.  Define the
rectilinear product patch

\[
P=\{x_i e_1+y_j e_2:0\le i,j\le L-1\}.
\tag{142.2}
\]

Put

\[
X=x_{L-1}-x_0,\qquad Y=y_{L-1}-y_0,
\tag{142.3}
\]

and define the integer layer counts

\[
r_1=\lfloor X\rfloor-(L-1),\qquad
r_2=\lfloor Y\rfloor-(L-1).
\tag{142.4}
\]

The gap assumption implies \(r_1,r_2\ge0\).  Translate the integer triangular
lattice to the lower-left corner and set

\[
Q=\{x_0e_1+y_0e_2+ae_1+be_2:
0\le a\le L-1+r_1,\ 0\le b\le L-1+r_2,\ a,b\in\mathbb Z\}.
\tag{142.5}
\]

> **Theorem 142.1 (nonuniform rectilinear capacity).** The source patch \(P\) is
> unit-separated, its convex hull is the coordinate parallelogram
> \[
> \operatorname{conv}P
> =\{x_0e_1+y_0e_2+ae_1+be_2:0\le a\le X,\ 0\le b\le Y\},
> \tag{142.6}
> \]
> and \(Q\subseteq\operatorname{conv}P\) is a unit-separated lattice patch.  Moreover
> \[
> \boxed{|P|=L^2,}\qquad
> \boxed{|Q|=(L+r_1)(L+r_2),}
> \tag{142.7}
> \]
> and therefore
> \[
> \boxed{|Q|-|P|=L(r_1+r_2)+r_1r_2.}
> \tag{142.8}
> \]
> Their exact diameters obey
> \[
> \boxed{\operatorname{diam}(P)^2=X^2+XY+Y^2,}
> \tag{142.9}
> \]
> \[
> \boxed{\operatorname{diam}(Q)^2
> =(L-1+r_1)^2+(L-1+r_1)(L-1+r_2)+(L-1+r_2)^2
> \le\operatorname{diam}(P)^2.}
> \tag{142.10}
> \]

### Proof

The convex-hull formula follows because (142.2) contains all four corners of the
coordinate rectangle and every product point lies in that parallelogram.  From
(142.4),

\[
L-1+r_1=\lfloor X\rfloor\le X,\qquad
L-1+r_2=\lfloor Y\rfloor\le Y,
\]

so (142.5) lies in (142.6).

For a difference \(ae_1+be_2\), the squared norm is

\[
q(a,b)=a^2+ab+b^2.
\tag{142.11}
\]

Every nonzero integer pair has \(q(a,b)\ge1\), so \(Q\) is unit-separated.  The same
coordinate-gap condition makes \(P\) unit-separated: if the two coordinate
differences have the same sign, \(q\ge1\); if they have opposite signs, their
absolute values are at least one and
\(u^2-uv+v^2\ge1\) for \(u,v\ge1\).

The cardinalities are immediate.  To compute the diameter of \(P\), the difference
coordinates lie in \([-X,X]\times[-Y,Y]\).  The convex quadratic \(q\) reaches its
maximum on this rectangle at a corner, and the same-sign corner gives
\(q(X,Y)=X^2+XY+Y^2\), which is no smaller than the opposite-sign corner.  The
identical argument for the integer coordinate rectangle gives the first expression
in (142.10).  Since \(q\) is increasing in each nonnegative coordinate, the floor
inequalities imply its final upper bound. \(\square\)

The one-sided case is already useful.  If \(r_1=0\) and \(r_2\ge1\), the protected
replacement gains \(Lr_2\) sites; if \(r_1=r_2=r\), (142.8) reduces to
\(2Lr+r^2\), recovering Section 141.  Thus a full lattice layer can be released by
accumulated slack in only one coordinate direction, and no uniform pointwise strain
bound is needed.

> **Corollary 142.2 (protected finite exchange).** Let \(\Omega\) be open with
> \(\operatorname{diam}\Omega<D\), and let \(F\subset\Omega\) be a finite
> unit-separated set containing \(P\).  If \(Q\subset\Omega\) and
> \((F\setminus P)\cup Q\) is a disjoint unit-separated union, then
> \[
> |(F\setminus P)\cup Q|=|F|+L(r_1+r_2)+r_1r_2
> \tag{142.12}
> \]
> and its diameter is strictly below \(D\).  Hence \(F\) cannot be an \(N\)-point
> global minimizer with \(D(N)=D\) whenever the displayed replacement has at least
> \(N\) points.

This is a finite, nonuniform version of the free-strain capacity route.  Its exact
remaining hypothesis is also the central obstruction: the lattice candidate \(Q\)
must be protected from \(F\setminus P\).  A source-derived monomer domain has not
been shown to supply that exterior protection, so Theorem 142.1 does not prove the
Target A Hall surplus or close Erdős Problem #99.

The executable exact-arithmetic regression is in
research/rectilinear_capacity.py and research/test_rectilinear_capacity.py.

**LEVEL I STATUS: STILL OPEN. TARGET A REMAINS UNRESOLVED.**
