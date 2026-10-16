<!-- theorem-state: {"artifact_id":"ART-5BF1182D395F","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — two-direction boundary-force regression

**Date:** 2026-09-14
**Repository commit:** ef941ab2b44aa393bdc461926769247b45754202
**State version:** 2026-09-14.audit.49
**Run type:** closing proof / adversarial regression
**Target:** Target C-II / Target B / Level I
**Starting status:** canonical full-core and pure-rhombic-disk frontiers; both still open
**Active prompt:** docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md
**External literature search:** not used for the result
**Computation:** exact independent verifier `research/verify_target_c_two_direction_plus_stress.py`

## LEVEL I STATUS

STILL OPEN

An attempted conditional no-go from the preceding research pass was falsified by
an exact finite positive-stress example. This report preserves the valid local
boundary implication, records the counterexample in full, and rejects the invalid
global polygon shortcut. No canonical theorem is changed.

## 1. Starting endpoint and attempted chain

The live C-II full-core endpoint remains

\[
 \liminf {1\over D}\sum_r(L_r+P_{{\rm exc},r}-2d_r)
 \ge {\pi\over2}(2-\sqrt3),
 \qquad
 \sum_rP_{{\rm exc},r}\le10(e_{BB}-k).
\]

The attempted chain was

    full source = simply connected two-direction rhombic disk
        + strictly positive contact stress
        + positive diameter endpoints are source-hull vertices
        -> every low-degree boundary vertex is source-hull
        -> an orthogonal boundary must be one square.

The first implication is valid. The second implication is false: an orthogonal
plus-shaped disk can have all its convex boundary vertices on its convex hull,
while its reflex boundary vertices have degree four and support positive
equilibrium.

## 2. Valid local lemma

Let \(A\) be the full vertex set of a simply connected edge-to-edge complex of
unit rhombi using two unit directions \(u,v\), with
\(\angle(u,v)\in(\pi/3,2\pi/3)\). Assume every actual contact edge has a strictly
positive contact multiplier in a global mixed KKT stress. If a vertex is not an
endpoint of a positive diameter row, then its contact vectors must have a strictly
positive linear combination equal to zero.

The only unit directions in the two-direction lattice are

\[
 u,\ -u,\ v,\ -v.
\]

No set of at most three of these vectors has the origin in the relative interior
of its convex hull. The four directions have cyclic gaps
\(\theta,\pi-\theta,\theta,\pi-\theta\), where
\(\theta=\angle(u,v)\); after deleting any one direction, the remaining set lies
in a closed half-plane with a strict one-sided component. Therefore:

\[
\boxed{\text{every non-loaded vertex of the full two-direction contact graph has
degree four.}}
\tag{2.1}
\]

In particular, a convex \(\pi/2\) boundary corner of the corresponding square
complex, which has degree two, must be loaded. A straight boundary vertex, which
has degree three, must also be loaded. Since every positive diameter endpoint is
a source-hull vertex, every such low-degree boundary vertex is a source-hull
vertex.

This is the complete valid consequence. It does not say that every convex
boundary vertex of an orthogonal polygon is a convex-hull vertex.

## 3. Exact counterexample to the attempted polygon closure

Take the five unit squares whose lower-left corners are

\[
 (0,1),\ (1,1),\ (2,1),\ (1,0),\ (1,2)
\]

in the ordinary square lattice. Their union is a simply connected plus-shaped
square complex. Its twelve source vertices are

\[
\begin{aligned}
A_{\boxplus}=\{&
(1,3),(1,2),(0,2),(0,1),(1,1),(1,0),\\
&(2,0),(2,1),(3,1),(3,2),(2,2),(2,3)\}.
\end{aligned}
\tag{3.1}
\]

The contact graph is exactly the 1-skeleton of the five squares. It is
triangle-free and all unit contacts are horizontal or vertical. The boundary
has eight convex corners, all of which are vertices of
\(\operatorname{conv}(A_{\boxplus})\), and four reflex vertices

\[
 (1,2),(1,1),(2,1),(2,2),
\]

each of degree four. Thus the claim that a non-square orthogonal disk must have a
non-hull convex or straight boundary vertex is false.

The example also passes the relevant positive-stress test. Its four diameter
edges are

\[
\begin{aligned}
&(0,2)(3,1),\qquad (0,1)(3,2),\\
&(1,0)(2,3),\qquad (1,3)(2,0),
\end{aligned}
\tag{3.2}
\]

each of squared length \(10\). These eight endpoints are precisely the eight
convex vertices of the source hull. Give every diameter edge multiplier \(1\).
Give the outer contact edges alternating multipliers \(1\) and \(3\) according to
the following complete list of boundary edge weights:

\[
\begin{array}{c|cccccccccccc}
\text{edge in cyclic boundary order}
&(1,3)(1,2)&(1,2)(0,2)&(0,2)(0,1)&(0,1)(1,1)&
(1,1)(1,0)&(1,0)(2,0)&\\
\text{weight}&3&3&1&3&3&1\\[1mm]
\text{edge in cyclic boundary order}
&(2,0)(2,1)&(2,1)(3,1)&(3,1)(3,2)&(3,2)(2,2)&
(2,2)(2,3)&(2,3)(1,3)\\
\text{weight}&3&3&1&3&3&1
\end{array}
\tag{3.3}
\]

and give each of the four central-square edges

\[
 (1,1)(1,2),\quad (1,2)(2,2),\quad
 (2,2)(2,1),\quad (2,1)(1,1)
\]

multiplier \(3\). At each reflex vertex the opposite horizontal contact weights
are equal and the opposite vertical contact weights are equal, so its contact
force balances exactly. At each convex hull vertex, the two incident contact
forces balance the corresponding diameter force. For example, at \((1,3)\),
the contact weights on the edges to \((1,2)\) and \((2,3)\) are \(3\) and \(1\),
while the diameter partner is \((2,0)\); with the convention

\[
\sum_{y\sim x}\alpha_{xy}(y-x)+
\sum_{z:\,xz\ {\rm diameter}}\beta_{xz}(x-z)=0,
\tag{3.4}
\]

the three contributions are

\[
3(0,-1)+(1,0)+((-1,3))=(0,0).
\]

The other seven convex vertices are the rotations/reflections of this same
calculation. Thus the example has a strictly positive contact/diameter
equilibrium stress on every contact edge and every listed diameter edge.

The exact certificate
`python3 research/verify_target_c_two_direction_plus_stress.py` independently
checks all pairwise source distances, the complete 16-edge contact set, the four
diameter pairs, strict positivity of every displayed multiplier, equilibrium at all
12 vertices, and the 12-point triangular-lattice competitor. It is a finite audit
of the displayed arithmetic, not a global-optimality certificate.

It is not a global minimizer for its cardinality, which is essential. Its
diameter is \(\sqrt{10}\). The following twelve points in the unit triangular
lattice are unit-separated and have diameter \(3\):

\[
\{(a,b):
(a,b)\in
\{(0,1),(0,2),(0,3),(1,0),(1,1),(1,2),(1,3),
(2,0),(2,1),(2,2),(3,0),(3,1)\}\},
\tag{3.5}
\]

where \((a,b)\) denotes \(a(1,0)+b(1/2,\sqrt3/2)\). Their squared distance
form is \(a^2+ab+b^2\), and a direct finite check gives values between \(1\) and
\(9\) on distinct listed pairs. Hence they form a same-cardinality feasible source
of diameter \(3<\sqrt{10}\).

This example therefore refutes the attempted polygon closure while remaining
compatible with the global problem: positive local stress and diametral-hull
support do not imply global optimality.

## 4. Exact frontier effect

The valid boundary-forcing statement (2.1) remains useful, but the proposed
conclusion “pure two-direction disk implies one rhombus” is rejected. The
correct surviving dichotomy is:

    low-degree boundary vertices must be source-hull loaded;
    reflex degree-four boundary vertices can evade this condition;
    therefore a two-direction source can survive locally through orthogonal
    concavities, even with a positive stress.

The plus example is finite and not globally optimal, so it does not disprove
Problem #99. It does show that a source-level proof must use a genuine global
diameter comparison, source capacity, or a quantitative boundary/interface
argument to eliminate the reflex degree-four mechanism.

The report does not change the canonical manifest or route map. The preceding
anisotropic contact-walk detour regression remains valid and becomes more
relevant: orthogonal concavities are precisely a mechanism that can store linear
outer-walk detour without violating local equilibrium.

## 5. Exact remaining lemma

The corrected target is:

> For a quadratic full-core triangle-free global minimizer with a dominant
> two-direction phase, prove that the reflex degree-four boundary mechanism either
> creates a linear exceptional/interface cost that closes Sections 122–123, or
> admits an explicit same-cardinality strict sub-\(D\) deformation. The proof must
> retain all source points, including contact-isolated points, and cannot replace
> the source by the rhombic carrier.

No version of this stability/global-minimality statement is proved here.

## 6. Proof-obligation ledger and claim audit

| Claim | Status | Exact scope and reason |
|---|---|---|
| At most three two-direction contact vectors cannot balance positively | proved finite | Direction gaps force a closed half-plane |
| Non-loaded full-source two-direction vertex has degree four | proved conditional | Requires positive multiplier on every actual contact and no positive diameter row |
| Positive diameter endpoints are source-hull vertices | canonical elementary input | Standard support lemma for diameter pairs |
| Every low-degree boundary vertex is source-hull loaded | proved conditional | Degree two/three plus the preceding rows |
| Every non-square orthogonal disk has a non-hull convex/straight boundary vertex | rejected | Five-square plus counterexample |
| Positive stress eliminates all non-square two-direction disks | rejected | The plus complex has a positive stress |
| Plus complex is globally optimal for \(n=12\) | rejected | Triangular-lattice source of diameter \(3<\sqrt{10}\) |
| General full-core source has one global two-direction phase | unresolved | Current route permits grains and interfaces |
| Level I | open | Original quantifiers remain undischarged |

## 7. Regression checks

| Regression/correction | Result | Exact hypothesis or failure |
|---|---|---|
| Large five-sector positive-stress complex | pass | Boundary pins are not all required to be positive diameter endpoints |
| 11-point pentagonal sun | pass | Not a two-direction disk; its contact directions use five sectors |
| Plus-shaped five-rhombus disk | pass | Exact counterexample to the polygon shortcut; positive stress survives through reflex degree-four vertices |
| Unit-square rigidity | pass | The one-rhombus case is allowed but does not imply a large-source theorem |
| Vanishing-shear lattice disk | pass | Its low-degree boundary staircase is not eliminated by density alone |
| Contact-isolated points | pass | The conditional lemma excludes them by hypothesis; C-II does not |
| Source/scaffold distinction | pass | The counterexample is an actual source, but the corrected theorem does not promote its local stress to global optimality |
| Holes/interfaces | pass | Explicitly outside the conditional branch and not silently removed |

## 8. Literature imports

None. The proof and counterexample use only elementary planar geometry, affine
lattice directions, and the canonical repository diameter-endpoint support fact.

## 9. Computation

No computation is logically required. The twelve-point triangular comparison in
(3.5) is a finite exact quadratic-form check; it is included to certify that the
positive-stress plus is not globally optimal at its own cardinality.

## 10. Corrections / supersessions

This report supersedes the preceding uncommitted attempted report
target_c_two_direction_diametral_boundary_nogo_2026-09-14.md. Its “orthogonal
boundary lemma” and its conclusion that only one rhombus can survive are rejected.
The valid local degree-four implication and the explicit source/global comparison
regression are preserved here.

No canonical theorem was used downstream from the rejected report, so no canonical
state or generated view requires a mathematical rollback.

## 11. Promotion recommendation

**regression/rejection only — do not promote.**

The exact plus stress is a mandatory regression against any future claim that
positive equilibrium plus diametral-hull support alone eliminates non-square
two-direction disks.

## 12. Handoff

1. **Strongest established correction:** the valid local implication is only that
   non-loaded two-direction vertices have degree four; reflex degree-four
   concavities evade the proposed closure.
2. **Exact failed route:** the five-square plus is a triangle-free, positive-stress,
   diametral-hull-supported source with no unit-triangle conclusion, although an
   exact triangular competitor beats it globally.
3. **Exact remaining lemma:** a global source-capacity or strict-deformation
   theorem charging reflex degree-four boundary structure in the quadratic phase.
4. **Binding dead route:** local positive stress and diametral endpoints do not
   imply global diameter optimality.
5. **Files to read next:** docs/targets/target-c/CURRENT.md, Sections 80, 82,
   122–123, the anisotropic detour regression, and the active Target A/B endpoints.
