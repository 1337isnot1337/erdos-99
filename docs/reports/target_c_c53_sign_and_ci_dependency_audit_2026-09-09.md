<!-- theorem-state: {"artifact_id":"ART-A4A2FF23264F","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — C53 interval signs and the C-I dependency audit

**Date:** 2026-09-09

**Repository base:** `c0522aa7a039d179dc68856c156d8642c14f30ff`

**Run type:** proof-level audit, not a Level I closure

**Status:** audited derivations below; not yet promoted into the route map

## 1. Status and the conflicting claim

**LEVEL I STATUS: STILL OPEN.**

The [September 8 audit](target_c_force_bulk_and_correction_audit_2026-09-08.md)
says a September 5 pentagon example rejected C53.T. Initially that example was
absent. During publication, `origin/main` advanced to `c26d6ab`, delivering the
exact witness. Section 1A below identifies its inconsistent projective cut and
orientation. Independently, this report proves the exact C53.T statement in the
[C53 report](target_c_arbitrary_thrackle_response_contraction_2026-08-31.md).
Consequently a counterexample cannot satisfy all of that statement's hypotheses
and orientation conventions. The formerly missing example is now resolved: its
ordered oriented triple fails precisely that convention.

The original route map has not promoted C52–C54/C63. The result here is a
dependency audit, not permission to infer closure from numbering. The intended
chain is

```text
convex deformation + exhaustive finite interval-sign proof
  -> C53.T for arbitrary convex diameter-thrackle geometry
  -> Robinson response + affine equilibrium -> every stress is PSD
  -> Farkas/Hoffman finite correction on arbitrary displacement fields
  -> no weak unit contacts in a contact-minimal triangle-free global source.
```

The last conclusion is C-I, not C-II and not Erdős #99. The audit recovers claims
already made in later reports; the new proof detail is the explicit deformation
that certifies the finite geometric reduction, together with a shorter matrix
argument. The independent new path/stress theorems are in the
[near-diameter-path report](target_c_near_diameter_path_unloaded_core_2026-09-09.md).

## 1A. Exact failure of the newly fetched pentagon regression

The [pentagon report](target_c_thrackle_interval_sign_regression_2026-09-05.md)
uses regular pentagon vertices p_j=(cos(2πj/5),sin(2πj/5)), and labelled chords
e=(0,2), f=(0,3), g=(1,3). They are indeed pairwise intersecting equal diameters.
Those parts of its hypotheses are correct.

For i<j, the directed chord p_j−p_i has angle π/2+π(i+j)/5, modulo 2π.
Thus the displayed e,f,g angles are respectively 162°,198°,234°. The regression
sorts angles modulo 180°, obtaining f,g,e. This chooses the half-plane with angles
in [0°,180°): the correctly oriented angles in that order are 18°,54°,162°.
It must reverse f and g, **but not e**. For I={0}, the head-minus-tail signs
are (1,0,−1), whose two products are both −1.

Instead the witness reverses all three edges to obtain positive x projection,
using a different half-plane, with angles in (−90°,90°). In that half-plane the
angles of e,f,g are −18°,18°,54°. The order must therefore be e,f,g. The
head-minus-tail signs in this correct order are (1,1,0), whose two products are
0 and −1. The witness's tail-minus-head convention negates all signs and leaves
these products unchanged.

The claimed violating list (−1,0,−1) uses the latter orientation with the former
order. Its direction list is 18°,54°,−18°, which is not increasing in the
chosen half-plane. Thus it is not an instance of C53.T. All angles above are
exact rational multiples of π; no floating-point sign or margin is used. The
exact regression-against-this-regression is `pentagon_cut_audit()` in the shared
script. It verifies both consistent cuts and the inconsistent order explicitly.

## 2. A complete finite reduction for C53.T

### Lemma 1 — convex realizations can be deformed without direction collisions

Every strictly convex labelled polygon can be continuously deformed, retaining
strict convexity and its cyclic label order, to a regular polygon. During such a
deformation, two intersecting distinct chords never have equal projective direction.

**Proof.** Let the original vertices be p_i in counterclockwise order. Choose a
distinct unit outward normal n_i strictly inside the normal cone at p_i. Put
p_i(t)=(1−t)p_i+t n_i, for 0≤t≤1. For j≠i,

\[
n_i\cdot(p_i(t)-p_j(t))
=(1-t)n_i\cdot(p_i-p_j)+t(1-n_i\cdot n_j)>0.
\]

Thus every p_i(t) remains a uniquely exposed vertex of the convex hull of these
points. In particular all are distinct and no three are collinear. Cyclic order
cannot change. At t=1 they are distinct points on the unit circle. Lift their
angles in cyclic order and interpolate linearly to equally spaced angles, including
the wraparound gap. All successive gaps remain positive, so this is another
strictly convex deformation.

Two chords with disjoint endpoints intersect exactly when their four endpoints
alternate; that is preserved. Intersecting noncollinear segments cannot be
parallel. Two chords sharing an endpoint can be parallel only if three vertices
are collinear. Hence the projective directions of any pair of intersecting chords
remain distinct throughout. □

### Lemma 2 — interval signs

Let e<f<g be three pairwise-intersecting distinct chords whose endpoints belong to
a strictly convex polygon. Choose a projective cut avoiding their directions,
orient all three into its corresponding open half-plane, and order by increasing
direction there. For any circular interval I of polygon vertices, set
z_h=1_I(head h)−1_I(tail h). Then

\[
z_g(z_e-z_f)\le0,\qquad z_e(z_g-z_f)\le0.
\tag{S}
\]

**Proof.** Delete vertices that are not among the three chords' endpoints. There
are m=3,4,5 or 6 remaining vertices. Restriction of I is still a circular interval
(possibly empty or full), and the chord incidences and crossing relations are
unchanged. By Lemma 1 the reduced polygon and the labelled convex-parabola polygon
p_i=(i,i²), 0≤i<m, are connected through strictly convex realizations: deform
each to the same regular polygon and reverse the second deformation.

Track the projective cut continuously in the same gap between the three distinct
directions. Their order and orientations cannot change, except for a possible
simultaneous reversal when compared to a fixed reference half-plane. Such reversal
sends z to −z and leaves both products in (S) unchanged.

It remains a finite integer check. In the parabola representative, orient every
chord ij from smaller to larger index. Its slope is i+j. For intersecting chords
these slopes are distinct. Enumerate all three-element subsets of the
\(\binom m2\) chords whose pairs either share an endpoint or alternate in cyclic
order. Sort by slope. The three projective cuts are its three cyclic rotations,
reversing every edge moved from the beginning to the end. For each start index
0≤a<m and each length 0≤l≤m use I={a,a+1,...,a+l−1} modulo m.

The complete set of resulting signed triples is

```text
(-1,-1,-1) (-1,-1, 0) (-1,-1, 1) (-1, 0, 0) (-1, 0, 1) (-1, 1, 1)
( 0,-1,-1) ( 0,-1, 0) ( 0, 0,-1) ( 0, 0, 0) ( 0, 0, 1)
( 0, 1, 0) ( 0, 1, 1)
( 1,-1,-1) ( 1, 0,-1) ( 1, 0, 0) ( 1, 1,-1) ( 1, 1, 0) ( 1, 1, 1)
```

Both products in (S) are nonpositive for each listed triple. The exact exhaustive
certificate is `chord_types()` in
[near_diameter_path_audit.py](../../research/near_diameter_path_audit.py): its
27,252 checks execute precisely the enumeration just specified, without numerical
geometry, random sampling or an unbounded search. Every geometric instance reduces
to this finite set by the preceding argument. This proves (S). □

## 3. The weighted Robinson implication, with all indices accounted for

### Lemma 3

Let L be a real symmetric m×m matrix with L1=0 and
L_ij=−γ_i γ_j s_ij for i≠j, where γ_i>0 and
s_ik≤min(s_ij,s_jk) whenever i<j<k. If Lt=0 for a strictly increasing vector t,
then L is positive semidefinite.

**Proof.** The cases m≤2 are immediate from the two kernel vectors. Otherwise
put Γ=diag γ and A=Γ⁻¹L. Let (Df)_i=f_{i+1}−f_i, 0≤i<m−1, and let
T_jk=1_{j>k}; thus DT=I and TDf=f−f_0 1. Set H=DAT. Its off-diagonal entries
are nonpositive:

- if k>i, H_ik=Σ_{j>k}(A_{i+1,j}−A_ij)≤0, because
  s_i,j≤s_{i+1,j} for all these j;
- if k<i, use A1=0 to write H_ik=−Σ_{j≤k}(A_{i+1,j}−A_ij)≤0,
  because s_j,i+1≤s_j,i for all these j.

Also H(Dt)=DAt=0 and Dt is strictly positive. The diagonal similarity
diag(Dt)⁻¹H diag(Dt) has nonpositive off-diagonals and zero row sums. Its
Gershgorin disks lie in the closed right half-plane. H represents A on the
quotient by the constant vectors: DA=HD follows from A1=0. The remaining
eigenvalue of A is zero. Finally A is similar to the symmetric matrix
Γ⁻¹/²LΓ⁻¹/². Thus all its eigenvalues are real and nonnegative; that symmetric
matrix, and by congruence L itself, are PSD. □

## 4. Response contraction and the quantifier “every stress”

Fix any normalized KKT stress in the canonical Target C source. Its positive
contact graph is connected by the promoted support-connectivity theorem, and its
loaded diameter endpoints B are exposed vertices of its force hull. Assume first
that B spans two dimensions. The positive unit-contact graph is planar inside
that hull, so its response Λ on B is a connected circular-planar response. Put
R=Λ⁺. Its effective-resistance matrix W has a nonnegative circular-interval split
decomposition. This is the exact electrical input, not an assertion about arbitrary
positive matrices; the external theorem and convention are specified below.

Orient and order the positive diameter edges as in Lemma 2. They are pairwise
intersecting by the planar diameter-thrackle theorem. Let Q be their incidence
matrix, B_H=diag β, U=QᵀP for centered boundary coordinates P, and K=QᵀRQ.
The canonical harmonic coordinate identity is ΛP=QB_HU, hence KB_HU=U.

Choose a positive linear projection of all oriented edge vectors and an independent
second projection so that U=EV, where E=diag a has a_i>0 and V has rows (1,t_i)
with t_i strictly increasing. This is a change of coordinate basis in the two
columns, not an identification with a different source.

The relation W_ij=R_ii+R_jj−2R_ij gives K=−QᵀWQ/2. For a circular split
δ_I, one has Qᵀδ_IQ=−2z_Iz_Iᵀ. Therefore K is a nonnegative sum of
z_Iz_Iᵀ. Lemma 2 gives K_eg≤min(K_ef,K_fg) whenever e<f<g.

Now M=E(B_H−B_HKB_H)E has M1=Mt=0, and
M_ef=−(a_eβ_e)(a_fβ_f)K_ef off the diagonal. Lemma 3 implies M≽0.
Congruence gives B_H⁻¹−K≽0. With Y=R¹/²QB_H¹/² on 1-perp, this means
YᵀY≼I, hence YYᵀ≼I, equivalently L_H≼Λ. Schur complementing the positive
Dirichlet interior block then gives

\[
\Omega=L_C-L_H\succeq0
\]

on all scalar vertex fields, including zero blocks outside the positive component.

If B is one-dimensional, it consists of the two endpoints z,a of the sole positive
diameter. Projection of equilibrium perpendicular to za makes that coordinate
harmonic at every positive-contact vertex, so connectedness makes it constant.
The connected positive unit-contact graph is a straight chain of D unit edges,
all with weight D, and β_za=1. Cauchy–Schwarz gives PSD exactly as in the chain
regression of the near-path report. Thus **every** normalized stress is PSD,
without a selected-support or critical-velocity restriction. This audits the
C53–C54 conclusion from the specified canonical electrical/geometric inputs.

## 5. Exact finite correction, not just a second-order jet

For the actual active contacts and diameter pairs write their signed slack at
displacement x as g(x)=Ax+Q(x), where contact rows have Q_e(x)=|x_i−x_j|²
and diameter rows have Q_h(x)=−|x_i−x_j|². Let * denote maximal KKT support.
Critical-cone duality gives A_*v=0 on every fixed-diameter critical velocity v.

Every nonzero λ≥0 with λᵀA_*=0 has positive total diameter coefficient:
otherwise dotting its pure contact equilibrium with the source coordinates gives
Σα=0. It thus normalizes to one of the stresses in Section 4. Hence
λᵀQ_*(x)≥0 for **every x**, and λᵀg_*(x)≥0. Farkas' lemma now implies
that A_*y≥−g_*(x) is feasible at every iterate x.

For the fixed matrix A_*, Hoffman's error bound provides a finite H, independent
of this feasible right-hand side, allowing a correction with
|y|≤H ε(x), where ε(x)=|[g_*(x)]_-|. Choose Euclidean norms. The fixed quadratic
map obeys |Q_*(x+y)−Q_*(x)|≤L(|x||y|+|y|²), so

\[
\varepsilon(x+y)\le LH|x|\varepsilon(x)+LH^2\varepsilon(x)^2.
\]

Start at x_0=tv with ε(x_0)≤C t². For sufficiently small t (depending on this
fixed configuration and v), the displayed factor is at most 1/2 throughout
|x|≤2(|v|+1)t. The sum of correction norms is at most 2HCt², so this
neighborhood condition is self-consistent. The iterates converge to
x(t)=tv+O(t²), with every strong slack nonnegative.

Choose v in the relative interior of the critical cone. Each weak active row has
strict first derivative by the canonical support duality, so its slack remains
positive after the O(t²) correction. Initially inactive inequalities retain their
strict slack by finiteness and continuity. Thus all pairwise lower and upper
bounds hold for sufficiently small t; no new contact appears. Global optimality
forces the resulting diameter to be exactly D. If a weak unit contact existed,
this would be a triangle-free global minimizer with fewer contacts, contradicting
the chosen contact minimality. Therefore C=C_*.

The argument does not require a constant H uniform in n, one stress controlling
all corrections, a smooth path, or a positive-definite stress. It uses universal
PSD on arbitrary x. C62's formal acceleration theorem is not needed as an extra
dependency for this iteration.

## 6. Regression and dependency audit

| Candidate objection | Exact disposition |
| --- | --- |
| Fetched pentagon counterexample to C53.T | Rejected exactly in Section 1A: after changing the orientation half-plane, its chord order was not updated. Both consistent orders obey C53.T. |
| One selected PSD stress suffices for correction | Rejected: Farkas tests every nonnegative left-null multiplier. Section 4 supplies exactly that universal quantifier. |
| PSD only on critical velocities suffices | Rejected: the September 8 quadratic-program regression has that property but fails finite integration; it lacks the arbitrary-displacement premise used here. |
| Near-star networks with many tiny strict minors | Compatible: only nonnegativity is concluded; no numerical spectral or minor gap is asserted. |
| Diameter stars, small vertex covers and crossing matchings | Included by the three-chord lemma; no matching or degree restriction is imposed. |
| Zero-stress activation and weak constraints | Weak rows are released at order t and strong-row corrections are O(t²); inactive pairs have configuration-specific positive slack. No uniform neighborhood is asserted. |
| Fully inactive rattlers | Retained; their zero columns/blocks cause no Farkas or PSD problem. No force-bulk population bound follows. |
| Long straight positive-stress chains | PSD-compatible, not a counterexample to the contact-minimal global conclusion; explicit smaller-diameter competitors exist. |
| Pure-rhombic chain-face and near-chain survivors | C-II, not excluded by this audit. The near-path report's L3–L5 apply without claiming strip rigidity. |
| Source/scaffold coordinate changes | None: Q,P,Λ,β belong to the same selected actual KKT network; E changes only the two coordinate columns. |

Canonical nontrivial inputs are: support connectivity and its promoted audit;
the force-hull boundary and C11 response identity; the planar diameter-thrackle
property; strong/weak critical-cone duality; and the contact-minimal normalization.
No unpromoted response-contraction theorem is used as a black box in this proof.

External inputs:

- Forcey, [Circular planar electrical networks, Split systems, and Phylogenetic
  networks](https://arxiv.org/pdf/2108.00550), Theorems 4.2 and 3.7: the boundary
  resistance metric of a connected circular-planar positive network has a
  nonnegative circular split representation. Its Laplacian sign convention is
  opposite ours; the effective resistances and split coefficients are unchanged.
  No converse realization or packing statement is imported.
- Peña–Vera–Zuluaga, [New characterizations of Hoffman constants for systems of
  linear constraints](https://arxiv.org/abs/1905.02894), Proposition 1: the
  linear error bound for a fixed matrix is uniform over feasible right-hand
  sides. The matrix is fixed throughout Section 5; no n-uniform estimate is used.

## 7. Actual advance and remaining endpoint

The focused audit supports C-I closure and rejects the interval-sign objection
by identifying the exact error in the now-available witness. It is not a new proof of
Erdős #99 and does not endorse every later numbered C module.

The next gate is used, not merely named: L3–L5 in the near-path report remove
diameter loading from a narrow near-chain and concentrate dominant-edge stress on
non-diametral-to-non-diametral contacts. Their exact remaining near-chain obligation
is a source-level finite release or strict sub-D competitor despite small positive
transverse stresses. Other C-II response/topology/rattler branches remain.

**Promotion recommendation:** retain this dependency-complete focused audit for
review alongside the corrected September 5/8 regression claims. If promoted, index
it in the Target C route map and update its C-I statement, foundational module,
and active prompt together. Do not promote C-II closure, force-bulk transport, or
a quantitative response gap. The full-campaign branch ledger remains explicitly
partial; no exhaustive-route or logical-independence certificate has been obtained.
