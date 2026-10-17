> Generated reading edition · [exact source](../../../docs/reports/target_c_all_unit_hull_end_currency_2026-10-04.md) · source SHA-256 `506b12c18a749590bfe5eedd1a43abfbb5c81213172cc6ab64e940f2c2ad8904`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-D6BB0FD3F83C","canonical":true,"claim_ids":["C-FINITE-HULL-END-ANGULAR-DEFECT-BOUND","C-PENTAGON-FIVE-HULL-END-REGRESSION"],"claim_statuses":{"C-FINITE-HULL-END-ANGULAR-DEFECT-BOUND":"canonical","C-PENTAGON-FIVE-HULL-END-REGRESSION":"regression"},"index":"docs/state/artifact-index.jsonl","status":"mixed","target":"target-c"} -->
# Target C: all-unit-hull endpoint currency and a pentagon regression

**Date:** 2026-10-04
**Base main:** `419c9bec2ed8fa2cc105a80803a279339e7bea9e`
**State:** `2026-09-14.audit.51`
**Classification:** proved candidates awaiting independent audit and promotion;
the artifact lifecycle is unreviewed. The local two-end pentagon claim is rejected.
**Level I and C-II:** open. C-I is closed.
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md`

## 1. Obligation and coordination

The initial attack was `collar transport <= 2Q -> t >= 3pi/5 -> exclusion of
the October t <= 1.860, x_B=O(sqrt(D)) branch`. The proposed local capacity
is false: an exact 15-point pentagonal flower sends five actual trains from
one pentagon to five supporting hull sides. Section 7 certifies this failure.

While this draft was running, PR #666 opened on the same hull-end depletion
mechanism. This report therefore independently audits its initial finite
obstruction and extends the count from its selected good outer intervals to
**all actual unit hull sides**. This produces an exact identity, a sharper
coefficient of outer-walk surplus, and an independent atomic-measure proof
valid throughout Type II. PR #624 and the deep-port branches are not premises.

The September reports `target_c_outerwalk_surplus_mu_tradeoff_2026-09-25.md`
and `target_c_clean_endpoint_fullcore_boost_2026-09-09.md` are important
predecessors. The former proves the weaker global coefficient `2u_B-3m_B`;
the latter gives the `2sqrt(Delta_2)` atomic obstruction only under
`x_B=o(D)`. Neither is imported as a theorem premise below.

The new implication is

`Type-II quadratic near-triangular rhombi -> atomic train mass`
`-> linearly many trains without any unit hull-side end`
`-> exact all-hull endpoint identity`
`-> large global outer-walk surplus or exclusion`.

## 2. Exact finite identity

Use the canonical positive-contact core, retaining the full source and its
contact isolates. Let `F=conv(B)` be the actual loaded force hull, `q=|B|`,
`b=q+x_B` the occurrence-counted contact outer walk, and `P=per(F)`.
Let `m_B` be the number of nonunit hull sides, `u_B=x_B-m_B>=0`, and
`delta=b-P>=0`. Let `f,Q` count bounded exceptional faces as in Sections
61 and 63, and put `g_F=Q-f>=0`, `k=d_H+s_Z`, `t_D=(q-k)/D`.

Choose exactly one exterior face-side occurrence of every actual unit side
of `F`. Call these the selected ends. Their number is **exactly**

    G=q-m_B.

Let `d` count complete stopped trains with two selected ends, and let `N_0`
count complete stopped trains with no selected end. Singleton trains are
included. Then

    0 <= d <= 2,                                             (1)
    T = G-d+N_0,                                             (2)
    5 t_D D + x_B + m_B + d = 3b + 2g_F + N_0.              (3)

Equivalently, the exact nonnegative-slack identity is

    5 t_D D + x_B + m_B + 2 - 3P
      = 3 delta + 2g_F + N_0 + (2-d).                       (4)

### Proof

The contact graph lies in `F`. Each unit hull side is an actual contact and
has an exterior face incidence. If it is a bridge, it has two outer
incidences; exactly one is selected. Distinct hull sides select distinct
physical edges. A singleton train therefore cannot have two selected ends.

A nonsingleton train with two selected ends is a rhombic midpoint arc
joining two parallel hull sides with opposite induced orientations. All
hull vertices are extreme. Two different such pairs alternate around the
convex hull: their oriented side directions occur as `theta,phi,theta+pi,
phi+pi`. Their arcs must cross. Canonical Section 61.2 makes the train
crossing graph simple and triangle-free, so there are at most two such
trains. This proves (1), including the bridge case.

Every other train has zero or one selected end. Counting selected ends gives
`T=d+(G-2d)+N_0`, proving (2). Canonical Sections 61 and 63 give

    T=(b+Q)/2+2f=t_D D+2f,
    Q=2t_D D-b,
    f=Q-g_F.

Thus `T=5t_D D-2b-2g_F`. Substitute (2) and `G=q-m_B=b-x_B-m_B`
to obtain (3). Replacing `b=P+delta` gives (4).

In particular, `5t_D D+2x_B+2>=3P`. This independently verifies PR #666's
initial obstruction, at commit `f96a036cbb5cc524a0997261025abb765bd5aba2`.
Its proof correctly retains singleton trains and occurrence multiplicity.

## 3. Type-II bulk trains cannot all have hull ends

Write `Delta_2=pi/(2sqrt(3))`. Along **every** unbounded canonical Type-II
source sequence,

    liminf N_0/D >= 2sqrt(Delta_2).                         (5)

There is no small-`x_B` or diameter-matching hypothesis in (5).

### 3.1 Finite direction measures and near-triangular crossings

Canonical Section 80 supplies `F/D -> B_(1/2)`, `R_4/D^2 -> Delta_2`, and
`E_4=o(D^2)`. Translations are understood in the hull convergence.
Canonical Sections 61 and 63 give `T=t_D D+2f<=5q<=5pi D`.

Pass to any subsequence where the finite measures

    nu_D = D^(-1) sum_(all trains tau) delta_(theta_tau)

on the projective direction circle `X=R/(pi Z)` converge weakly to `nu`.
This is a mass measure, not a probability measure. Let `M=nu(X)` and let
`a` be the sum of its atomic masses.

Each rhombus is one edge of the simple triangle-free train crossing graph.
Its acute side separation is in `(pi/3,pi/2]` and its area is the sine of
that separation. For every fixed epsilon>0, rhombi with separation at
least `pi/3+epsilon` number `o(D^2)`, because each costs a fixed positive
amount of `E_4`. Thus all but `o(D^2)` crossings have direction separation
arbitrarily close to `pi/3`.

### 3.2 Atomic mass lower bound, without assuming an atomic graph is triangle-free

Let `A_J` be the first J atoms of `nu`, with total mass `a_J`, and let
`a_tail=a-a_J`. Surround them by a union `U` of small disjoint open arcs
whose boundary has zero `nu` mass. The number of crossing pairs with one
direction outside `U`, divided by `D^2`, has limsup at most

    (nu x nu){dist_X(theta,phi)=pi/3,
              theta outside U or phi outside U}/2
      <= M a_tail.                                        (6)

To justify the first bound, first use the closed epsilon-neighborhood of
the displayed separation relation, weak convergence of product measures,
and the `o(D^2)` exceptional crossings; then let epsilon decrease to zero.
For the second bound, the exact relation has product mass only at pairs of
atoms: for fixed theta its phi fiber consists of two points. If one point
is outside `U`, at least one participating atom belongs to the tail.
There is no contribution from either nonatomic coordinate.

The finite crossing graph induced on trains with directions in `U` is
triangle-free, even if the limiting atoms at `0,pi/3,2pi/3` form an
equilateral direction triple. Mantel therefore gives

    Delta_2 - M a_tail <= nu(U)^2/4.

Shrink the arcs to the J atoms to get the same bound with `a_J` on the
right, then let J increase. Consequently

    a >= 2sqrt(Delta_2).                                   (7)

For finitely many atoms, take all of them. The same argument works with
zero tail. We never apply Mantel to the limiting direction-compatibility
graph, which may itself contain a three-cycle.

### 3.3 Unit hull sides have diffuse directions

For a fixed projective direction window of radius eta<pi/4, the number of
selected ends in that window satisfies

    limsup G_window/D <= 2tan(eta).                        (8)

Here is an elementary justification. If the normalized hull is at
Hausdorff distance h from the radius-1/2 disk, each vertex on a hull side
with unit outer normal n is within `O(sqrt(h))` of `n/2`. This follows
from `n dot p >= 1/2-h` and `|p|<=1/2+h`. Oriented hull sides in a window
of radius eta form one contiguous convex boundary chain. Its endpoint
displacement along the central side direction is at most
`sin(eta)+O(sqrt(h))`; every side in the chain has projection at least
`cos(eta)` times its length. Hence its length is at most
`tan(eta)+o(1)` after normalization. A projective window has two oriented
chains. Each selected side has physical length exactly one, proving (8).
Missing/nonunit hull sides only reduce the selected count.

Among trains directed into the J atomic windows, at most `G_U` trains can
have a selected end. Thus

    liminf N_0/D >= nu(U)-2J tan(eta).

Shrink the windows, obtaining `liminf N_0/D>=a_J`, and then let J increase.
Equation (7) proves (5) on this subsequence. If the uniform liminf assertion
failed, a subsequence realizing the failure would have a weakly convergent
direction subsubsequence and contradict this argument. This supplies the
full sequence quantifier; no rate of convergence is assumed.

### 3.4 Hostile audit of PR #666's finite bridge, and a sharper finite form

The developed PR #666 at `de2fdf1f84fad00115b6f267d0e0998ba01f695f`
proves finite angular capacity and depletion, not just the initial count.
Its near-circle normal bound, injective side assignment, three phase-window
bound, large-angle error and Mantel step pass this independent audit. The
normal estimate in its equations (7)-(9) is the finite form of Section 3.3.
Its `Delta=O(D)` input is correctly supplied by canonical Section 68, not by
an invalid division of an `o(D^2)` area error. There is a further refinement:
actual projective separation needs only **two** windows, and all unit hull
sides may be selected.

Suppose, after translation, for `0<=sigma<1/2`,

    B_( (1/2-sigma)D ) subset F subset B_( (1/2+sigma)D ).

For `0<epsilon<pi/6` define

    C(epsilon,sigma)
      =4[(1/2+sigma)tan(epsilon)+sqrt(2sigma)/cos(epsilon)].

Exactly the support and projected-chain argument of Section 3.3 gives at
most `D C(epsilon,sigma)` unit hull sides in any projective window of
radius epsilon: writing a supported point as `hn+s Jn` gives
`|s|<=sqrt(2sigma)D`, and the two oriented chains each have projected span
at most `2D[(1/2+sigma)sin(epsilon)+sqrt(2sigma)]`.

Let `A_ang=sum_R(acute_angle(R)-pi/3)` and let `E_H` count rhombi incident
to a train with at least one selected end. For each such train assign one
selected hull side; the assigned sides are distinct. A small-defect crossing
with a fixed train direction theta has its partner in the two projective
windows centered at `theta+pi/3` and `theta-pi/3`, each of radius epsilon.
The third modulo-`pi/3` lift, centered at theta, cannot cross this train.
Simplicity of the actual crossing graph therefore proves

    E_H <= A_ang/epsilon + 2 T D C(epsilon,sigma) =: B_eps. (15)

The first term pays crossings with defect exceeding epsilon. Summing over
all T trains can count a crossing with two hull-end trains twice, which is
harmless for this upper bound. Remove all hull-end trains. The remaining
crossing graph has exactly `N_0` vertices and `R_4-E_H` edges, so

    N_0 >= 2sqrt(R_4-E_H)
        >= 2sqrt(max(0,R_4-B_eps)).                       (16)

Combining with (3) gives the explicit finite strengthening

    5t_D D+x_B+m_B+2
      >= 3b+2g_F+2sqrt(max(0,R_4-B_eps)).                (17)

This independently checks and sharpens PR #666's finite inequality (12):
`x_B+m_B=2x_B-u_B`, and `2g_F+3(b-P)` are retained rather than discarded.
Canonical Section 68 gives `A_ang=O(D)`. Taking epsilon=`D^(-1/2)` and
sigma tending to zero in Type II makes `B_eps=o(D^2)` without requiring a
rate for sigma. Thus this finite proof also implies (5), independently of
the atomic proof. The two proofs agree and isolate different possible
failure points; neither depends on an October candidate theorem.

## 4. Global source-currency theorem

Combine (3), (5), and the canonical Type-II limit `P/D->pi`:

    liminf [5t_D + (x_B+m_B-3delta-2g_F)/D]
      >= 3pi + 2sqrt(Delta_2).                             (9)

In particular,

    liminf [5t_D + (x_B+m_B)/D]
      >= 3pi + 2sqrt(Delta_2).                            (10)

The promoted loaded-chord theorem gives `e_BB=q-m_B`. Canonical Section 62
then gives `s_C=m_B+k-c_I-2` and therefore

    mu_D D := e_BB+2s_C-3k = t_D D+m_B-2c_I-4.

Here `mu_D` is the canonical scalar surplus; Section 3's direction measure
is `nu_D`. Canonical Section 75 gives `c_I=o(D)`.
Consequently (9) implies the strengthened surplus tradeoff

    liminf [5mu_D + (u_B-3m_B-3delta-2g_F)/D]
      >= 3pi + 2sqrt(Delta_2).                            (11)

Dropping the nonnegative `delta,g_F` terms gives the simpler version with
`u_B-3m_B`. This improves September OW.2's `2u_B-3m_B` coefficient and
adds the atomic mass term without assuming `x_B=o(D)`.

## 5. Branch eliminated and exact remaining obstruction

If `x_B=o(D)`, then `m_B,delta=o(D)` and (10) gives

    liminf t_D >= (3pi+2sqrt(Delta_2))/5
                = 2.265880714899... .                     (12)

The October high-t collar scope `t_D<=1.860+o(1)`, `x_B=O(sqrt(D))` is
therefore empty for sufficiently large canonical sources. Its matching,
degree-three fan, rhombus collar, and pentagon transport conclusions are
conditional implications under an excluded antecedent. Their local proofs
are not declared false by this audit. This exclusion already follows from
the weaker finite bound `3pi/5`; (12) is not its sole justification.

More generally, if `limsup t_D<=T`, (10) and `m_B<=x_B` force

    liminf x_B/D >= (3pi+2sqrt(Delta_2)-5T)/2.             (13)

At `T=1.860`, the right side is `1.014701787248...`. If instead
`limsup mu_D<=1.860`, (11) forces

    liminf (u_B-3m_B)/D >= 2.029403574497... .             (14)

The new precise source-level obligation is to rule out, or strictly deform,
Type-II sources carrying this much **actual global** outer-walk surplus,
while keeping all source points and all lower and upper constraints. No
identity with the sum of local harmonic-cell walks is asserted. The
macroscopic-container branch and larger-surplus Type-II sources remain.
There is no C-II closure, finite release, or Level I disproof here.

## 6. Hostile checks and dependencies

| Input or failure | Disposition and exact use |
| --- | --- |
| `C-LINEAR-NONMATCH`, Sections 61.2, 61.5 | Canonical finite train paths, simple triangle-free crossings, at most two double hull ends; the exterior-occurrence refinement is proved above |
| `C-LOADED-HULL`, Section 63 | Canonical `b+Q=2(q-k)`, `m_B<=x_B`, `b>=P`, `q<=pi D` |
| `C-RHOMBUS-POP`, Section 67 | Canonical strict rhombus classification, core/force-hull scope, isolates retained |
| `C-PUNCTURED-PHASE`, Section 68 | Canonical `A_ang=O(D)` for Section 3.4's finite-proof asymptotic specialization only; Sections 3.1-3.3 do not need this stronger rate |
| `C-FULLCORE-NEAR-DISK`, Section 80 | Canonical disk convergence, `R_4/D^2->Delta_2`, `E_4=o(D^2)` |
| `C-ATTACH-CURRENCY`, Section 62 | Canonical pinned ledger for (11) only |
| `C-COMP-DEATOMIZATION`, Section 75 | Canonical `c_I=o(D)` for (11) only |
| `C-FULLCORE-LOADED-CHORD` | Canonical `e_BB=q-m_B` for (11) only |
| Limiting 60-degree atom triple | Harmless: Mantel is applied to finite crossing graphs, never to the atom-compatibility graph |
| Isolates outside the force hull | Retained in the source; neither hull-direction counts nor train velocities are assigned to them |
| Bridges, singleton trains, repeated outer vertices | Included through face-side incidences and exactly one selected exterior occurrence per unit hull side |
| `G_loc=o(D^2) => G_loc/d=o(1)` | Not used; no division of local area error by D |
| First-order versus finite motion | No deformation is claimed |

The fixed-window arguments deliberately take the source limit first and the
window radius second. No uniform phase-window rate or multiplier floor is
assumed. All claims remain candidates until independent review/promotion.

## 7. Exact regression and finite certificate

Take a counterclockwise regular unit pentagon with vertices `p_i` and side
vectors `v_i`. For every side add the two points

    a_i=p_i-Jv_i,  b_i=p_(i+1)-Jv_i.

The 15 points have exactly 20 unit contacts, five strict square faces, and
one central pentagonal face. All pair distances are at least one, there is
no unit triangle, and the hull has ten extreme vertices and five unit sides
`a_i b_i`. Each central pentagon side belongs to a distinct square train
whose other end is that supporting hull side. Thus one actual pentagon
absorbs **five** such trains. The generic local two-end capacity fails even
with convex faces and actual strict rhombi. This packet omits the canonical
same-carrier degree-three fan and global-minimizer hypotheses; it is not a
counterexample to (9)-(14).

`python3 research/verify_target_c_all_unit_hull_end_currency_2026_10_04.py`
uses exact arithmetic in `Q(sqrt(5),sqrt((5+sqrt(5))/8))`. It checks every
pair in the flower, the actual contact graph and all plane face walks, hull
extremality/support, train decomposition, five pentagon-to-hull trains, and
the exact identity (3) and the remaining-crossing Mantel inequality. It also
checks a unit square, a unit pentagon, a two-edge bridge path, a nine-point
square grid, and the flower with an additional retained isolate.
The square shows that the additive 2 in (4) is sharp for the finite geometric
identity. These are finite regression checks, not certificates of global
optimality or of the asymptotic argument.

No external literature theorem or numerical search is a proof premise.
The decimals above only evaluate the displayed symbolic constants.

**Promotion recommendation:** independently audit the product-measure atom
capture, hull-direction window bound, all-side occurrence selection, and
surplus normalization before changing theorem state. This PR does not
perform the repository promotion transaction or self-merge.
