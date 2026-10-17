> Generated reading edition · [exact source](../../../docs/reports/global_joint_stress_strain_phase_mechanism_2026-10-12.md) · source SHA-256 `ae5ede4071475cb9d957b4326dccc5ffcbc2d3297c66e340e3d0b3111d06638b`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-DDFC8A5AC13A","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# Erdős Problem #99 — a joint global stress/strain mechanism

**Date:** 2026-10-12
**Base commit:** `ab6dd3336f9f8d440f2bada76edb32153391cddc`
**State version:** `2026-10-10.audit.234`
**Target:** Level I, whole-source global research
**Classification:** proved formal candidate awaiting promotion; source application conditional
**Lifecycle:** unreviewed, noncanonical
**Active prompt:** current whole-problem launch prompt
**Computation:** `research/verify_global_joint_phase_compatibility.py`

**LEVEL I REMAINS OPEN.** The continuum fields below have not been extracted from
arbitrary global minimizers. Formal stress fields and physical source packings are
different objects.

## 1. The global proposed chain

```text
an arbitrary sufficiently large triangle-free global minimizer
-> a single bounded compatible strain field and equilibrated stress field
   carrying all macroscopic grain populations, interfaces, and boundary work
-> joint phase incompatibility forces one grain or macroscopic transition cost
-> a whole-source strict diameter competitor, or a unit triangle.
```

The formal incompatibility theorem is proved below. The source extraction and the
last implication are missing. This route is exploratory until both are supplied;
neither scalar stress isotropy nor a chart for one grain is sufficient.

## 2. A tempting stress-only implication is false

Let u1=(1,0), u2=(1/2,sqrt(3)/2), u3=(-1/2,sqrt(3)/2), and Lj=uj uj^T.
A phase with one missing direction i has a positive stress

    Si=sum_{j != i} aij Lj,       aij>0.

Different missing directions do **not** imply incompatible equilibrium stresses.
For example,

    A=(5/3)L1+(8/3)L2,      B=(1/3)L1+(8/9)L3,
    A-B=(4/9) (2,sqrt(3))(2,sqrt(3))^T.

Both matrices are positive definite; their determinants are 10/3 and 2/9.
The jump has rank one and annihilates n=(-sqrt(3),2), so stripes with interface
normal n have continuous traction and are divergence free. A fraction 1/4 of A
and 3/4 of B has mean I and mean determinant 1. Thus it also satisfies the usual
determinant null-Lagrangian identity.

This is a **formal global stress regression**, not a penny-graph source. It
rejects stress-only phase incompatibility even with positive coefficients,
isotropic mean, traction continuity, and determinant compatibility. Unequal
weights in the shared direction are essential in this example.

## 3. Joint compatibility changes the conclusion

The symmetric matrices dual to L1,L2,L3 are

    E1=[[1,0],[0,-1/3]],
    E2=[[0,1/sqrt(3)],[1/sqrt(3),2/3]],
    E3=[[0,-1/sqrt(3)],[-1/sqrt(3),2/3]].

Thus Lj:Ei=delta_ij and tr Ei=2/3, where colon is the Frobenius product.
In phase i, an opening strain Fi has symmetric part ti Ei, ti>0; its skew
part is arbitrary. It preserves the two supported unit directions to first
order and strictly opens the omitted one.

Here F is an **infinitesimal displacement gradient in one fixed material
reference frame**, not the actual source-coordinate matrix or a finite rotated
deformation gradient. Stress must be represented in its matching dual frame.
Independent grain rotations, a physical Cauchy stress used as a material stress,
or charts with unrecorded dislocation cuts do not satisfy this formal model.

For a stress Si supported on those same two directions,

    Si:Fi=0.

For two different phases i,j, symmetry removes the skew parts and gives

    (Si-Sj):(Fi-Fj)=-aij tj-aji ti <0.                 (1)

For two points in the same phase the corresponding pairing is zero, even if
their positive coefficients, opening sizes, and skew parts differ.

In particular, no distinct-phase pair can satisfy **both** a kinematic rank-one
jump Fi-Fj=v tensor n and traction continuity (Si-Sj)n=0. Those conditions
would make their product v dot ((Si-Sj)n) equal zero, contradicting (1).
The stress-only laminate above has joint product -32/9 when its two strains
are E3 and E2. It cannot be a jointly compatible laminate of these phases.

## 4. A global rigidity theorem on a periodic domain

Normalize a two-dimensional flat torus to area one. Let F and S be bounded
matrix fields, with F=Fbar+gradient v for a periodic Lipschitz displacement v,
and let S be symmetric, periodic and divergence free in the distributional
sense. Suppose almost every point belongs to one of the
three joint phases of Section 3, with strictly positive finite coefficients and
opening size. Then **only one missing-direction phase has positive measure**.

### Proof

Integration by parts gives

    integral S:F = Sbar:Fbar.

Equivalently,

    integral integral (S(x)-S(y)):(F(x)-F(y)) dx dy =0.     (2)

For nonsmooth fields, periodically mollify v. Distributional divergence freedom
annihilates each smooth gradient, and convergence of the gradients in L1,
together with bounded S, gives the stated integration-by-parts identity.
The integrand is zero for equal phases and strictly negative for different
phases by (1). If two phases each had positive measure, their Cartesian product
would contribute a strictly negative integral, contradicting (2). Boundedness
ensures all integrals exist. The same argument applies on a bounded domain
on a bounded Lipschitz domain when v is Lipschitz with zero trace, using smooth
compactly supported approximation in W^(1,1). Arbitrary source boundary data
do not meet that premise.

The conclusion concerns jointly compatible matrix fields. It is not a theorem
that a triangle-free packing has one global grain.

## 5. Quantitative form and the boundary obstruction

The previous argument gives a direct transition-cost estimate. Assume actual
and ideal phase matrices have Frobenius norms at most M. Outside a transition
set of measure delta, suppose actual (S,F) differs from some ideal phase pair
by at most eta in each matrix, with aij>=a0>0 and ti>=t0>0. Let mu_i be the
good-region population of phase i. Assume exact periodic compatibility as in
Section 4. Then

    sum_{i<j} mu_i mu_j <= 2(M eta+M^2 delta)/(a0 t0).     (3)

Indeed, replacing both matrices at two good points changes their difference
product by at most 8M eta. For unequal ideal phases that product is at most
-2a0 t0. Pairs touching the transition region have measure at most 2delta
and product at most 4M^2. Insert these estimates into (2), noting that the
ordered unequal-phase measure is 2 sum_{i<j} mu_i mu_j, to obtain (3).

For arbitrary boundary data define

    B=integral S:F-Sbar:Fbar.

The left side of (2) is then 2B. The same calculation yields

    sum_{i<j} mu_i mu_j
    <= (|B|+4M eta+4M^2 delta)/(2a0 t0).                (4)

Therefore small transition area alone is insufficient. The normalized boundary
work, matrix bounds, and nondegeneracy of both stresses and opening strains
must all be controlled. Moving these costs into a discarded interface is not
allowed. A single grain still needs a source-specific closure argument.

## 6. Literature near miss

### An exact obstruction to extending the theorem across grain rotations

The common reference frame cannot be dropped. Let R be rotation by -pi/6,
let S=2L2+L3, and put W=[[0,-2/3],[2/3,0]]. Then

    S=R(L2+2L3)R^T,
    FA=E1,              FB=R E1 R^T-W,
    FA-FB=(1/3)*(1,sqrt(3)+2) tensor (1,sqrt(3)-2).

Both phases have positive two-direction stress coefficients, strictly positive
opening size one, and zero local stress work S:FA=S:FB=0. Their strain-gradient
jump has rank one and their stress is identical, so they admit an exact
periodic two-phase laminate on a flat torus aligned with that jump normal.
One constructs it by adding the gradient of a one-dimensional periodic
displacement to the phase-average matrix, with the scalar derivative taking
the two phase values and having zero average.

This is a **jointly compatible rotated formal-field regression**, still not an
actual unit-distance packing. It rejects extending the periodic purity theorem
to independently rotated triangular reference directions. Source geometry must
control orientation and material compatibility beyond the curl-F/div-S
conditions alone. Do not pursue a smaller fixed-orientation lemma as if it
removed the global multi-grain obligation.

### Primary source checked

Ball and James, [Incompatible sets of gradients and metastability,
arXiv:1407.5929v2](https://arxiv.org/html/1407.5929v2), study compact incompatible
sets of gradients and transition-layer estimates. Their framework requires
differential compatibility and genuinely incompatible well sets; their
introduction also discusses extensions to other differential constraints.
This motivates checking the joint curl-F/div-S constraints here. Their theorem
is **not imported** as a packing theorem. Stress-only wells in Section 2 are
compatible, and actual source charts, uniform bounds, boundary costs, and
contact-isolated labels have not been supplied. Sections 3–5 instead have the
elementary complete proofs above.

## 7. Exact checks and claim classifications

Run `python3 research/verify_global_joint_phase_compatibility.py`. It checks all
nine dual-basis pairings, all three symbolic cross-phase formulas, the positive
rank-one stress laminate and its isotropic/determinant means, and its -32/9
joint pairing. It also checks the common positive stress and rank-one strain
jump for the independently rotated compatible laminate. Arithmetic is exact
rational/sqrt(3) symbolic algebra.

| Claim | Classification | Limit |
| --- | --- | --- |
| Stress-only two-direction phases can laminate to isotropic mean | Regression | Formal matrix fields only |
| Independently rotated joint phases can have common stress and compatible strain jump | Regression | Formal fields; no unit-distance source |
| Distinct positive opening phases have strictly negative joint jump pairing | Proved formal candidate awaiting promotion | Fixed common triangular reference frame |
| Bounded exact periodic joint fields have one missing-direction phase | Proved formal candidate awaiting promotion | Exact differential/boundary hypotheses |
| Quantitative estimates (3)–(4) | Proved formal candidate awaiting promotion | Requires explicit bounds and boundary work |
| These fields model every large triangle-free global minimizer | Conditional / unproved | Whole-source extraction absent |
| Joint phase purity closes Level I | Conditional / unproved | Single-grain strict source competitor absent |

No canonical promotion or state change is proposed. The script certifies formal
algebra, not unit-distance source geometry, global optimality, or Level I.

## 8. Global next obligation

Determine whether actual **whole-source geometry**, beyond the differential
constraints alone, can rule out the rotated compatible laminate and supply a
common material chart with
joint compatibility and a controlled counterpart of (4), while retaining every
source point and all grain/interface/boundary costs. Contact-isolated points
have no stress but remain part of cardinality and any eventual competitor.
If the extraction needs unbounded transition strains, vanishing stress/opening
products, or macroscopic boundary work, identify those global costs explicitly.
In a cut material chart, integration by parts also has the internal seam term
involving displacement jump times stress traction. Small seam length alone does
not make that term small after opening-strain normalization. Its sign and size
belong to the whole-source obligation.
Do not replace this obligation by proving compatibility for a smaller supplied
chart. Even successful extraction must still pay for a strict n-point planar
competitor or force a unit triangle.
