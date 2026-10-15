# Erdős Problem #99 — Target C continuation prompt v1.2

## Promoted integrator supplement — 2026-09-09

Read `docs/theory/04-ambient-force-and-cap-transport.md` for the additional
cross-target inputs: every selected force hull inherits the source's near-minimal
circumradius, all normalized stresses have `P_*=2D-O(sqrt(D))`, and all actual
diameter-star angles are `O(D^(-1/4))`. Force-hull limits are centrally symmetric
cyclic hulls. Exterior population equals missing force-hull area divided by
`sqrt(3)/2` up to explicit `O(D)` error. These do not imply a matching or eliminate
interior isolates. The integrator's numerical post-ZF consequences remain
conditional on their separately stated hypotheses; do not promote them by proximity.

## Controlling continuation update — 2026-09-09

Read `docs/targets/target-c/56-ci-restored-frontier.md` and its promoted
orientation/dependency audit before the older v1.2 text below. C53 universal
selected-stress PSD and C63 finite integration are restored; C-I is closed.
The alleged pentagon regression mixed the projective cut with an incompatible
orientation. Do not repeat it as a counterexample.

The current task is C-II: exclude sufficiently large triangle-free global
minimizers chosen to minimize contacts and then diameter pairs, with `C=C_*`
and `H=H_*`, while retaining all contact-isolated points. Do not assume this
secondary normalization is simultaneously hull-saturated. The force-bulk
localization/FB4 claim remains rejected by the exact heptagon-center audit.
Later C-II results still need their hypotheses checked; they are not promoted
merely because their PSD premise has been restored.

The older C-I missions and PSD warnings below are historical except for the
continuing prohibition on *generic* PSD without the proved geometric hypotheses.

Work in the repository theorem state. This is a continuation of the audited Target C program, not a fresh attempt.

## Mission

Obtain a Level I proof or disproof of Erdős Problem #99. Prioritize Target C: the KKT force-hull / reciprocal-geometry route.

A Level I affirmative result must rule out triangle-free global minimum-diameter unit-separated configurations for all sufficiently large cardinalities. Local minima, asymptotically dense examples, finite searches, or arbitrary fixed containers do not settle the problem.

## Authoritative reading order

Read completely, in this order:

1. `docs/problem/statement.md`
2. `docs/theory/01-local-structure.md`
3. `docs/theory/02-nonlinear-and-regressions.md`
4. `docs/theory/03-oler-shell.md` when finite-packing bounds are used
5. `docs/targets/target-c/README.md`
6. `docs/targets/target-c/01-force-hull-and-shear.md`
7. `docs/targets/target-c/02-fully-visible-bridge-frontier.md`
8. `docs/targets/target-c/03-pinned-block-and-loaded-boundary-frontier.md`
9. `docs/targets/target-c/04-near-minimal-response-frontier.md`
10. `docs/targets/target-c/05-quadrangulation-defect-frontier.md`
11. any promoted Target C report needed for the theorem under attack

Use `docs/KNOWLEDGE_MAP.md`, `AGENTS.md`, and `docs/RESEARCH_WORKFLOW.md` for repository operation and claim classification. Do not reconstruct Target C from chat transcripts.

### September 9 audit checkpoint

Also read the route map's scoped September 9 corrections. The purported
pentagon counterexample to C53 mixes the orientation of one projective cut with
the ordering of another; it is rejected, not a binding obstruction. The full
`target_c_c53_sign_and_ci_dependency_audit_2026-09-09.md` provides a focused
PSD/C-I derivation for promotion review. Do not promote every downstream C-II
module by association. The September 5 force-bulk proof is withdrawn: pinned
jamming of the nonisolated core does not make every isolated source point
diametral. Its area-gap consequences remain conditional. The route map's
explicit promotion scope controls the older frontier language below.

## Trusted Target C state through C50.2

Treat promoted results as established unless a specific gap is exposed.

The base stack includes:

### Detailed base stack and selected-stress audit
- contact-preserving diametral hull saturation;
- maximal KKT support and the canonical force hull;
- exact KKT-support/fixed-diameter-critical-cone duality;
- simultaneous first-order release of every weak active constraint;
- common-angular-rate finite integration;
- the exact diameter-shear separator alternative;
- connectedness and full-diameter span of every positive KKT contact support;
- the contact-network Dirichlet response and Maxwell reciprocal force polygon;
- `2 V(F,F*) = D^2` and the audited force-perimeter endpoint classification;
- the direction-dependent second-order angular-variance inequality;
- Reuleaux-triple exclusion for sufficiently large global minimizers;
- the explicit shared-endpoint diameter-angle bound with asymptotic ceiling
  `5*pi/6-sqrt(3) = 50.7607988... degrees`;
- diameter-cycle length `Omega(sqrt(D))` with the explicit audited bound; and
- exclusion of the one-dimensional canonical force-hull phase for `D>1`.
- C30's response-inertia budget for a selected stress with two-dimensional diameter
  endpoint hull; and
- C31-C32 positivity for the four- and five-endpoint cases of a three-edge diameter
  forest, and the K6 convex six-terminal Kalmanson closure for the remaining
  matching. Thus every three-edge forest has no negative response mode. The
  `rho=1` equality/star mode is now classified by EQ6 as an additive
  effective-resistance metric, and CONC6 forces its weighted barycenter into all
  three matching chords. SEP6 now uses the actual circular-planar contact network:
  star equality makes every size-two circular minor vanish, so Gallai's T-path
  theorem forces a one-vertex terminal separator. C26/C35 degree caps exclude
  that separator in fully force-visible C-II, hence `rho<1` in the six-terminal
  equality subcase. SEPq generalizes the separator argument to every additive
  response on `q>=4` terminals; C34 then makes all additive canonical responses
  impossible for `D>=9` because `|B_+|>=6`. Non-additive larger-support equality
  and direction-dependent support selection remain open.
- TP5 gives the initial complementary non-additive count. CR4 sharpens it using
  connectedness of the deleted-graph quotient: C26/C35 plus Gallai yield
  `nu_(B_+)(C)>=(|B_+|-1)/4` and at least
  `floor(ceil(D)/16)` pairwise terminal-disjoint strict circular minors in C-II.
  The coefficient `1/4` is sharp from degree and connectivity alone. No uniform
  lower bound on an individual minor is available.
- A bounded-degree cycle-with-leaves circular-planar regression converges to a star
  response while retaining CR4-linearly many strict minors of arbitrarily small
  aggregate mass. Any quantitative transport must use unit-contact geometry, KKT
  equilibrium, and `q=Omega(D)`; topology alone is insufficient.
- C34's exact fully force-visible endpoint budget
  `2|B_+| >= ceil(D)+2`, obtained by matching the canonical pinned-core rank bound to
  the connected triangle-free penny-graph deficit.
### Compact canonical base stack
- diametral hull saturation;
- maximal KKT support and the force hull;
- fixed-diameter critical-cone/KKT-support duality;
- simultaneous weak-row first-order release;
- common-angular-rate finite integration and the C9 diameter-shear separator;
- connected positive contact support spanning diameter `D`;
- C10/C11 Maxwell reciprocal and circular-planar response with `2V(F,F*)=D^2`;
- force-perimeter endpoint classification and large-`n` force-perimeter gap;
- C15 Reuleaux-triple exclusion;
- explicit shared-endpoint diameter-angle ceiling tending to `50.7607988...` degrees;
- diameter-cycle length `Omega(sqrt(D))`;
- exclusion of the one-dimensional force hull.
- C50 extends the Kalmanson closure to every strictly convex six-endpoint matching.
  Its equality mode (`K=B^{-1}`) is classified at response level as a weighted star
  metric with concurrent matching chord lines.
- C50.1 rules out that equality mode when the selected positive contact graph is a
  tree, since a star resistance metric would force a degree-six contact vertex.
- C50.2 removes the tree hypothesis. A star response has all order-two circular
  minors zero; the block-cut-tree terminal-separator lemma then forces a vertex
  separating the six terminals, and the star metric excludes that vertex being a
  terminal. It therefore has degree at least six, impossible in a triangle-free
  unit-contact graph. Hence the selected six-endpoint branch has strict `rho<1`.
- C51 proves a full selected-response contraction for the next matching topology:
  with eight strictly convex cyclic terminals, `H={04,15,26,37}`, arbitrary
  positive diameter weights, and the circular-planar affine identity,
  `B^{-1}-Q^T Lambda^+Q>=0`. Its proof keeps the unequal chord scale factors
  `a_i` and uses `gamma_i=a_i beta_i`; it does not assume a regular octagon.

The fully force-visible C-II stack additionally includes:

- **C26:** `Q^circ=B_+`; unloaded contact degree is `3,4,5`; no neutral degree-one/two transport;
- **C27-C29:** macroscopic bridge diagonal/cut and loaded-block bridge-depth costs;
- **C30:** `|B_+| >= (ceil(D)+2)/2`;
- **C31:** `delta_X<=2q_X+k_X-2` with a global `O(D)` block-diameter budget;
- **C32:** universal-bridge full core diameter graph = cross-cut caterpillar forest plus at most one cap;
- **C33:** `2|B_+|>=delta+c_I+e_BB+2` from positive self-stress row surplus;
- **C34:** every nontrivial bridge block has `q_X+k_X>=4`;
- **C35:** every loaded vertex has contact degree at most three; every unpinned component has at least three boundary contact edges;
- **C36:** each unpinned component lies in the convex hull of at least three loaded attachments; attachment sets are noncrossing in cyclic order;
- **C37-C38:** planar attachment-incidence and response-quotient connectivity bounds;
- **C39:** `delta_X<=k_X+2q_X-p_X-c_X-2`; nontrivial reaction-free blocks have bridge degree at least five;
- **C40:** `t_r>=delta_r+3`, `delta_r<=3|A_r|-3`, and `sum_r delta_r+3c_I+2e_BB<=3|B_+|`;
- **C41:** if `c_bk=-Lambda_bk`, then
  `(D^2/2)tr(Lambda-L_H)=sum c_bk(D^2-|b-k|^2)>0`;
- **C42:** if `h` is the outer-face walk and `Sigma_4=sum_bounded(deg f-4)`, then
  `h+Sigma_4<=4|B_+|-2c_I-2e_BB-4`, so a core with `m>>D` has `m-O(D)` strict unit-rhombic bounded faces.
- **C49:** with `F=conv V(C)` and attachment-cell area gap `G`, the core population
  satisfies the exact whole-hull/cellwise minimum recorded in the C49 report; the
  theorem does not control contact-isolated source points or provide a uniform area gap.

Do not silently strengthen these statements. In particular:

- C41 is **not** a PSD/Loewner theorem;
- no positive KKT or effective response conductance has a uniform lower bound;
- C42 is not a lattice classification or density gap;
- positive KKT support need not contain contact-isolated source points.
- C49 is a force-visible-core capacity theorem, not a force-bulk theorem; it does
  not control contact-isolated source points or provide a uniform area gap.

## Exact live gates

### C-I — eliminate diameter shear

Prove that every sufficiently large contact-minimal, diametrally saturated, triangle-free global minimizer with a weak unit contact has a relative-interior fixed-diameter critical velocity with common angular rate on all strong diameter chords.

Equivalently, rule out the C9 separator: a nonzero zero-sum tangential load on the strong diameter chords carried by a nonnegative combination of radial active rows with positive mass on a weak row.

A proof forces `C=C_*`.

### C-II — eliminate the fully force-visible branch

Assume `C=C_*`. The active subfrontiers are now:

1. **macroscopic bridge cut:** exclude a fixed-`c` bridge with `alpha_e>=cD` and crossing positive-diameter weight `w_e>=c`;
2. **near-minimal harmonic response:** use C35-C41 to exclude the noncrossing harmonic-component normal form, preferably through an exact circular-planar response/area/container inequality;
3. **force-bulk/rhombic transport:** prove `n-m=O(D)` or another transport of global packing information into the C42 `m-O(D)` strict-rhombic core;
4. **boundary-surplus phase:** use C18, reciprocal perimeter, C33, C42, and global packing to exclude a positive linear loaded-boundary surplus.
5. **strict-minor transport:** use CR4's linear family of strict circular minors to
   force a quantitative response defect or an exact C42/global-packing inequality.

### Selected-stress response audit
The C30-C32 response reduction is a proved subcase audit, not a closure of C-I: it
does not supply maximal support for the direction-dependent second-order stress and
does not control supports with more than three diameter edges or the equality mode.

The K6 convex six-terminal Kalmanson lemma is an additional selected-stress
subcase. It removes the three-edge six-endpoint response obstruction for arbitrary
strictly convex terminal geometry, but does not remove the maximal-support or
equality-mode obligations.

EQ6 sharpens the equality mode: `rho=1` forces a star-equivalent boundary
response with additive resistance metric. SEP6 gives a source-preserving
contradiction in fully force-visible C-II: the corresponding actual contact graph
would need an unloaded separator of degree at least six or a loaded separator of
degree at least five, while C26/C35 cap those degrees at five and three. SEPq and
C34 extend this to every additive canonical response once `D>=9`. None of this
applies to non-additive larger-support equality or arbitrary selected stresses in
C-I.

TP5 adds the initial non-additive topological complement, and CR4 sharpens it: in
C-II the connected quotient and degree caps force
`nu_(B_+)(C)>=(|B_+|-1)/4`, hence at least `floor(ceil(D)/16)` terminal-disjoint
strict circular minors. Their numerical sizes may still tend to zero, so this is
not yet a C41 trace-gap or global-packing contradiction.

The exact C53 equality alternative is now promoted away for (D\ge9):
`min_{e!=f} K_ef=0` would force a diagonal transfer kernel, an additive
circular-planar resistance metric, and a SEPq separator contradicting the C26/C35
degree caps via C34. The live response branch is therefore strictly negative.
This does not provide a uniform negative magnitude and does not close the
non-additive strict-negative branch.

CONC6 sharpens it further: the weighted boundary barycenter lies in the relative
interior of every selected matching chord. Concurrent diameter chords are not yet
excluded by the canonical stack.

### Target C-II — fully force-visible contradiction

Assume `C=C_*`. Then the entire unit-contact graph is one connected positive network
of Euclidean diameter `D` inside a two-dimensional force hull. Use the reciprocal
mixed-area identity, circular-planar response, force-perimeter restrictions,
second-order angular reduction, explicit diameter-angle bound, diameter-cycle girth,
and global finite-packing inequalities to prove that such a triangle-free global
minimizer cannot exist for all sufficiently large `n`.

A valid endpoint is either:

- a forced unit equilateral triangle; or
- an explicit `n`-point unit-separated competitor with diameter strictly below
  `D(n)`.
### Current endpoint
A valid endpoint is a forced unit equilateral triangle, a strict sub-`D` competitor, or an exact global inequality incompatible with minimum-diameter packing.

## Preferred attack order

1. Attack C-I if an exact separator theorem appears. Generic positive planar statics is too flexible; use the actual unit network, strong-diameter boundary order, and global-optimality geometry.
2. Otherwise attack the C-II near-minimal response normal form. C41 gives a new exact positive currency:
   `sum c_bk(D^2-|b-k|^2)>0`.
   Seek a way to force this currency to vanish or to be quantitatively incompatible with C35-C40/circular-planar structure.
3. Attack the force-bulk transport needed by C42. Do not assume contact-isolated points are negligible.
4. Keep the macroscopic bridge-cut exclusion separate; crossing matchings remain a binding regression.

## Binding no-go results and regressions

### Selected-stress no-go audit
Do not repeat the following routes without a new hypothesis that escapes the stated
failure.

- Ordinary normalized KKT stress alone is not a universal prestress-stability
  certificate.
- A universally zero KKT multiplier is only a first-order release statement; finite
  integration can fail through diameter shear.
- Generic positive planar statics is too flexible to exclude the shear separator.
- Spider-web interval torque inequalities for the special diameter reactions reduce to
  automatic positive crossing sums and give no contradiction by themselves.
- A generic PSD/Loewner claim for `Lambda-L_H` is unproved.
- Diameter-cycle length alone does not close the problem: high-order Reuleaux polygons
  can approximate the disk.
- Local/jammed regular-shell examples do not contradict Target C because the promoted
  Reuleaux/packing restrictions use global minimum-diameter optimality.
- The one-dimensional force-hull branch is already impossible; do not reanalyze it.
- The C30-C32 response statements are restricted to one selected normalized stress;
  do not confuse their numbering with the current C26-C29 bridge addenda or infer
  PSD for larger-than-three-edge supports without a new proof.
- C33 is an exact abstract six-endpoint sign-cone regression only; it does not provide
  a circular-planar unit-contact response, and its exact circular minor has the wrong
  sign. K6 supplies the missing circular-planar response inequality for the three-edge
  convex matching; larger supports and the equality mode remain live.
- The K6 six-terminal Kalmanson lemma is restricted to the three-edge matching and
  selected stress; its equality/star example blocks any automatic strict inequality.
- EQ6 is a boundary-response classification only; do not replace the actual unit
  contact network by an electrically equivalent star when arguing about geometry.
- CONC6 is a necessary concurrency condition for equality, not a contradiction;
  do not silently assume concurrent diameter chords are impossible.
### Current route no-go results
- Ordinary KKT stress is not a universal prestress-stability certificate.
- Universal zero multiplier is only first-order release; diameter shear is the finite-integration obstruction.
- Generic positive planar statics and spider-web torque inequalities do not eliminate C-I.
- A generic PSD/Loewner claim for `Lambda-L_H` is unproved. Connelly's convex-polygon tensegrity theorem does not directly apply after Kron reduction because positive effective response edges can be crossing interior chords rather than polygon-boundary cables.
- C41's trace gap need not be uniform: its positive terms may carry arbitrarily small conductance.
- TP5/CR4 are topological strictness only; do not convert their linear minor count
  into a trace gap without a quantitative conductance or transport theorem.
- The near-star cycle-with-leaves regression shows that even aggregate strict-minor
  mass can vanish under the abstract degree/circular-planar hypotheses.
- C42's rhombic bulk does not imply a triangle or density gap. Disk-clipped oblique rhombic grids remain binding.
- Diameter-cycle length alone does not close the problem.
- The one-dimensional force-hull branch is already excluded.

## Research discipline

For each proposed lemma, state its exact implication into C-I or C-II. Classify it as proved theorem, conditional implication, conjectural route, regression/counterexample, computational evidence, or literature import.

If literature is used, import exact hypotheses and prove the bridge into Target C. Search-result summaries are not proof.

If computation is used, preserve exact/certified counterexamples and state what global-optimality information it does not provide.

## Output contract

A substantial run should end with:

1. `LEVEL I STATUS`;
2. strongest genuinely new theorem with complete proof;
3. exact effect on C-I/C-II;
4. shortest remaining lemma;
5. regressions/no-go routes;
6. exact files promoted/updated;
7. compact handoff.

Do not claim Target C is solved unless the global quantifier and every C-I/C-II branch are closed.
