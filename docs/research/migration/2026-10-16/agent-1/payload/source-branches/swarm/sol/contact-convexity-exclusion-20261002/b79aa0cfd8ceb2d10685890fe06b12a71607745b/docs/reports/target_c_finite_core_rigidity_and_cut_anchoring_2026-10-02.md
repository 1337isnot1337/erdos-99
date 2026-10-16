<!-- theorem-state: {"artifact_id":"ART-9013D1E37C5D","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — finite core rigidity and two-puncture diameter anchoring

```text
maximal-rank positive semidefinite source stress
 -> finite rigidity of the mixed core and three-vertex connectivity
 -> every contact component after two punctures still carries an old diameter
 -> contradiction if a physical train/face cut violates that anchoring.
The last physical-cut implication is not proved; Level I remains open.
```

**Date:** 2026-10-02.  
**Starting checkout:** `fbeae9b3fa18a63e07573676b4e2e512a91ca4d5`.  
**Fetched research base:** `3bad7c12bf5133665be466d0396362108fadef2c`.  
**State version:** `2026-09-14.audit.51`.  
**Branch:** `swarm/sol/contact-convexity-exclusion-20261002`.  
**Mission:** finite source moves, then a source-vertex cut obstruction. No open
coordination issue or PR assignment was present at startup. Existing threshold,
reflection, midpoint-energy, bank-defect and cubic-star packets were inspected.  
**Classification:** proved candidates awaiting independent audit and promotion;
artifact lifecycle **unreviewed**. Sections 7–8 are **regressions** against
stronger closure claims.  
**Level I / C-II:** **OPEN / OPEN**. No promotion is made.  
**Active prompt:** [current C continuation](../prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md).  
**Literature:** no import.  
**Certificate:** [exact finite checks](../../research/verify_target_c_finite_core_rigidity_2026_10_02.py).

## 1. Canonical inputs and exact scope

Use a contact-minimal, then diameter-pair-minimal triangle-free global minimizer
with `D>=9`. Retain its whole source `A`, including contact isolates. Write `V`
for its nonisolated contact core, `P` for the `|V|` by 2 coordinate matrix, and
`C,H` for its actual contact and diameter edges on that core. Choose one
relative-interior normalized stress, with every coefficient positive:

\[
 \sum_H\beta_h=1,\qquad \sum_C\alpha_e=D^2,\qquad
 \Omega=L_C(\alpha)-L_H(\beta).
\]

The only load-bearing theorem inputs are:

1. [Theory 01, Theorem 4.1](../theory/01-local-structure.md): equilibrium,
   normalization and the virial identity.
2. [C-I restoration](../targets/target-c/56-ci-restored-frontier.md): `Omega>=0`
   and full actual support in the lexicographic representative.
3. [ZR/ZF, Sections 3–4](../targets/target-c/57-zr-zf-rigidity-audit.md):
   `ker Omega=span{1,P_x,P_y}` **on V**, and mixed planar rigidity rank `2v-3`.
4. For the incidence corollary alone, canonical
   [Woodall topology](target_c_woodall_diameter_topology_2026-09-10.md):
   `h=q-d_H`; for `d_H>0`, there are exactly `d_H` nonisolated caterpillar
   components; for `d_H=0`, there is one odd-unicyclic component with leaves.

The source core spans the plane. The finite theorem below uses these exact
matrix facts, rather than assuming that infinitesimal rigidity alone implies
finite or global rigidity. Contact-isolated points are not added to the
three-dimensional kernel. Their inactive source constraints must still be
checked in every proposed competitor.

The October exact-phase gap graph, threshold staircase, and finite-swap reports
are not premises for the results below. Their objects enter only the closing
attempt in Section 6. In particular, this report makes no claim about the vertex
connectivity of a gap quotient.

## 2. Finite rigidity of the mixed core

**Theorem 1 (finite mixed-length rigidity).** Let `Q_i` be points in any finite
Euclidean dimension, indexed by `V`. If

\[
 |Q_i-Q_j|=|P_i-P_j|\quad(ij\in C\cup H),                 \tag{1}
\]

then every pairwise core distance is preserved. More precisely,

\[
 Q_i=b+T P_i,\qquad T^TT=I_2.                            \tag{2}
\]

No closeness to the source, path joining the placements, or feasibility of
nonedge distances is needed in this theorem.

**Proof.** For every real scalar vector `x`,

\[
 x^T\Omega x=\sum_C\alpha_{ij}(x_i-x_j)^2
             -\sum_H\beta_{ij}(x_i-x_j)^2.
\]

Summing this identity over the coordinate columns of `Q`, (1) gives

\[
 \operatorname{tr}(Q^T\Omega Q)
 =\sum_C\alpha_{ij}-D^2\sum_H\beta_{ij}=0.                \tag{3}
\]

Every summand is nonnegative. A zero quadratic form of a positive semidefinite
matrix lies in its kernel. Hence each column of `Q` is an affine scalar
function of `P`, yielding `Q_i=b+TP_i`.

Put `M=T^TT-I_2`. Every active edge vector `r=P_i-P_j` satisfies `r^TMr=0`.
Thus the planar velocity `u_i=(M/2)P_i` is a mixed infinitesimal bar flex.
ZF says `u_i=a+AP_i` for a skew-symmetric `A`. Because the source affinely
spans the plane, equality at all its vertices forces `a=0` and `M/2=A`.
A matrix that is both symmetric and skew-symmetric is zero. Therefore `M=0`,
proving (2). ∎

This is a finite equality theorem for the **mixed** graph. It does not assert
that preserving only the contacts forces congruence, nor that inequalities
`|Q_h|<=D` can be substituted for equality in (1).

## 3. Three-vertex connectivity and redundant active rows

**Theorem 2.** The actual mixed graph `G=(V,C union H)` is three-vertex
connected: deleting any at most two vertices leaves it connected.

**Proof.** Its vertex count is at least four. Under disconnection choose a
component whose complement has at least two vertices. Independently translating
that component gives a non-Euclidean infinitesimal flex fixing two distinct points.
A cut vertex `s` would permit the velocity `J(P_i-P_s)` on one component of
`G-s` and zero elsewhere. This preserves every bar to first order. It is
not a Euclidean velocity, since it fixes `s` and a distinct vertex in another
component. Both conclusions contradict ZF.

Suppose `S={s,t}` disconnects `G`, and let `L` be the line through its distinct
source points. Every component `W` of `G-S` has a vertex off `L`. Otherwise
give one vertex of `W` a nonzero velocity perpendicular to `L` and fix every
other vertex. Every bar incident to the moving vertex is collinear with `L`,
so this is a flex. The fixed complement contains `s,t` and a point off `L`
because the complete core spans the plane; fixing these three points makes
the flex non-Euclidean, contradicting ZF.

Reflect one component `W` across `L`, fixing all other vertices. All bars in
`G` preserve their lengths: crossing bars can end only at `s,t`. This placement
is not congruent to the source. It moves an off-line point of `W` but fixes
`s,t` and an off-line point in another component. Theorem 1 forbids it. ∎

**Theorem 3 (one-row redundancy).** Deleting any one row from the mixed
rigidity matrix leaves its rank equal to `2v-3`.

**Proof.** Equilibrium is a row dependence with nonzero coefficient on every
actual row: use `+alpha` on contact distance rows and `-beta` on diameter
distance rows. Any one row is therefore in the span of all the others. ∎

Theorems 2–3 concern the actual mixed source framework. They are not assertions
that one can remove a source point or that a deleted diameter has zero KKT
weight. Nor does one-row redundancy imply simultaneous redundancy of an
arbitrary packet of rows.

## 4. Two-puncture loaded anchoring

Let `B` be the actual diameter endpoint set in `V`. It contains at least three
vertices because the force hull is two-dimensional.

**Theorem 4.** For every `S subset V`, `|S|<=2`, every connected component of
the contact graph `C-S` contains a member of `B-S`.

**Proof.** A contact component `W` containing no such endpoint has no remaining
diameter edge incident to it. Thus it is a component of `G-S` as well. There
is a vertex of `B-S` outside `W`, so `G-S` is disconnected, contradicting
Theorem 2. ∎

This strengthens unpunctured positive-contact loading: removing one or two
specified **source vertices** cannot reveal a diameter-free contact island.
It includes deleted unloaded, loaded, and train-interface vertices.

**Corollary 4.1 (bridge endpoints cannot carry the entire crossing load).**
Suppose a contact bipartition `V=X disjoint union Y` has exactly one crossing
contact `ab`, with `a in X,b in Y`, and both `X-{a}` and `Y-{b}` are nonempty.
Some actual diameter crosses `X-{a}` and `Y-{b}`.

**Proof.** Without that diameter, deleting `a,b` separates those two sets in
the mixed graph, contrary to Theorem 2. ∎

A one/two-source-vertex separator certificate is now a contradiction to the
canonical C-II source, without a multiplier floor or integration of a motion.
This applies in any C-II branch satisfying the canonical source normalization,
not only a fixed-star or exact-phase branch.

### 4.2. Diameter leaves pay an extra contact incidence

Let `q=|B|`, let `ell_H` count the degree-one vertices of the **full** diameter
graph, let `e_BB` count loaded-loaded contacts, and let `t_BI` count contacts
from `B` to `V-B`. Three-vertex connectivity implies minimum mixed degree three.
Thus a diameter leaf has at least two contacts; every other loaded vertex has
at least one contact by the positive-source equilibrium theorem. Consequently

\[
 \boxed{t_{BI}+2e_{BB}
 =\sum_{b\in B}\deg_C(b)\ge q+\ell_H\ge q+2d_H.}       \tag{7}
\]

For the last inequality, each of the `d_H` nonisolated tree components in the
forest case has at least two leaves; in the cyclic case `d_H=0`. This is an
exact incidence payment retaining diameter deficiency, not an asymptotic count.
It does not assign those contacts to distinct harmonic components or distinct
train faces. A source vertex can pay both incidences into one component.

The unit square, with all four contact sides and both actual diameter diagonals,
has `q=4,ell_H=4,d_H=2,t_BI=0,e_BB=4` and achieves equality throughout (7).
Its scalar stress is positive semidefinite with the affine kernel and its mixed
graph is rigid. Therefore a universal three-contact lower bound for every
diameter leaf is false. The square has `D=sqrt(2)<9`; it does not disprove a
three-contact claim confined to large canonical sources. A large-source
improvement remains unproved; no such improvement is claimed here.

## 5. The exact finite gain from a contact-isometric move

Let `Q` be any planar core placement preserving every old contact exactly.
Set `U=Q-P`. No inequality on its diameter rows is assumed initially.

**Theorem 5 (finite weighted diameter gain).**

\[
 \boxed{\sum_H\beta_h(D^2-|Q_i-Q_j|^2)
       =\operatorname{tr}(U^T\Omega U)\ge0.}              \tag{4}
\]

Let `Pi` be orthogonal projection in vertex-coordinate space onto
`span{1,P_x,P_y}`. If `v>3` and `lambda_+` is the least positive eigenvalue of
`Omega`, then

\[
 \operatorname{tr}(U^T\Omega U)
 \ge\lambda_+\|(I-Pi)Q\|_F^2.                           \tag{5}
\]

In particular, a contact-isometric placement that is not affine in the source
strictly shortens at least one old diameter, whether or not other diameters
lengthen. If it is also noncongruent and every old diameter is nonlengthened,
then at least one old diameter strictly shortens.

**Proof.** Evaluate the stress quadratic form at `Q`; its contact contribution
is `D^2`. Since `Omega P=0`, its energy is also the energy at `U`, proving (4).
The spectral decomposition on the orthogonal complement of the kernel proves
(5). For the last assertion, if no diameter strictly shortens, all their
lengths are unchanged, so Theorem 1 makes the placement congruent. ∎

There is no uniform lower bound for `lambda_+` here. Its existence is a finite
source fact, not a diameter-independent or inverse-polynomial bound.

**Corollary 5.1 (mandatory diameter replacement).** Let `Q` be a full-source,
unit-separated placement with diameter at most `D`, preserving the old contact
set exactly, creating no new unit contacts, and noncongruent on `V`. Let `L_H`
be the number of old diameter pairs that strictly shorten and `N_H` the number
of formerly inactive pairs that become diameters. Then

\[
 L_H\ge1,\qquad N_H\ge L_H.                             \tag{6}
\]

**Proof.** Theorem 5 gives `L_H>=1`. Since no unit contact is added or lost, the
placement remains triangle-free and has the same contact count. If its diameter
were below `D`, it would already contradict global optimality. At diameter
`D`, secondary diameter-pair minimality gives
`|H|-L_H+N_H>=|H|`, proving (6). All pairs involving source isolates belong to
this accounting; they cannot be omitted. ∎

Thus a finite contact-isometry need not prove strict decrease immediately. If
it nonlengthens all old diameters, excluding **new upper-active pairs** suffices
for a contradiction in this normal form. New lower-active pairs are a separate
obstacle because they change the contact count.

### 5.2. Affine moves and the exact normalized-interpolation threshold

First, a noncongruent contact-isometry that nonlengthens every old diameter
must be **nonaffine** on the core. For an affine placement, `Q=b+TP`, every
coordinate lies in `ker Omega`, so (4) is zero. Positivity of every `beta_h`
and the upper inequalities then make all old diameters unchanged; Theorem 1
forces congruence. This rules out affine rescue without assuming that the
entire source lies in one lattice.

Now consider straight interpolation to any contact-isometric endpoint `Q`,
which need not be upper-feasible. Write

\[
 c_e=|U_i-U_j|^2\ (e\in C),\quad c_* =\max_C c_e,\qquad
 a_h=|U_i-U_j|^2\ (h\in H),\quad
 g_h=|Q_i-Q_j|^2-D^2.
\]

For `0<t<=1` such that `s(t)=1-t(1-t)c_*>0`, restore the shortest old
contact by putting

\[
 R_i(t)=\frac{P_i+tU_i}{\sqrt{s(t)}}.
\]

All old contacts have length at least one because their unscaled squared
lengths are exactly `1-t(1-t)c_e`. Every old diameter is strictly below `D`
if and only if

\[
 \boxed{g_h+(1-t)(D^2c_*-a_h)<0\quad\hbox{for every }h.}  \tag{8}
\]

Indeed its unscaled squared length is
`D^2+t g_h-t(1-t)a_h`; compare this with `D^2 s(t)` and divide by `t>0`.
Thus testing the restored old upper constraints is a finite family of linear
inequalities in `t`, alongside the explicit positivity condition on `s(t)`.
Every inactive source pair still needs its separate lower and upper check.

Set

\[
 E_C=\sum_C\alpha_e c_e,\quad E_H=\sum_H\beta_h a_h,
 \quad G=E_C-E_H=\operatorname{tr}(U^T\Omega U)\ge0,
 \quad A_*=D^2c_*-E_C\ge0.
\]

The `beta`-weighted sum of the left side of (8) is exactly
`A_*-t(A_*+G)`. Therefore, if `A_*+G>0`, simultaneous strict old-diameter
improvement requires the explicit finite threshold

\[
 \boxed{t>\frac{A_*}{A_*+G}.}                            \tag{9}
\]

If `A_*+G=0`, this weighted sum is zero for all `t`, so strict improvement
of every old diameter is impossible. When the old contact relative
displacements have unequal squared lengths, positive contact weights imply
`A_*>0`. In that case infinitesimal interpolation is obstructed even when the
endpoint has positive weighted diameter gain. This is a necessary threshold,
not a sufficient competitor theorem or a uniform barrier independent of source.

For a unit square, take the exact contact-isometric rhombus endpoint
`Q=((0,0),(1,0),(8/5,4/5),(3/5,4/5))`. It is affine, has
`c_*=2/5,E_C=E_H=2/5,A_*=2/5,G=0`, and (9) would require `t>1`.
Its old diameter squared lengths are `16/5` and `4/5`. This certifies precisely
how dilation to restore contacts obstructs the proposed affine interpolation.

### 5.3. A sparse-mass bound and no interpolation rescue for a slab swap

Let `F_C` be the old contacts with nonzero relative displacement at `Q`, and
put `f_C=(sum_(e in F_C) alpha_e)/D^2`. Then `E_C<=f_C D^2 c_*` and
`E_H>=0`. Therefore, whenever the threshold in (9) is defined,

\[
 \boxed{\frac{A_*}{A_*+G}\ge1-f_C.}                     \tag{10}
\]

In particular a move changing only a small fraction of the contact stress
cannot yield a strict restored interpolant until almost its full finite size.
This statement has no lower bound on individual multipliers; the stress fraction
is an explicit property of the chosen move.

There is a stronger conclusion for the actual slab-move form, independent of
the stress fraction. Suppose the endpoint preserves old contacts and all core
point displacements have one of the two values `0,Delta`, with `Delta!=0`, and
some old contact crosses between the two displacement classes. Then
`c_*=|Delta|^2`, and every old diameter has `a_h` equal to either zero or
`|Delta|^2`. For `D>1`,

\[
 D^2c_*-a_h\ge(D^2-1)|\Delta|^2>0.                     \tag{11}
\]

If an old diameter is fixed or lengthened at the finite endpoint (`g_h>=0`),
the left side of (8) is strictly positive for every `0<t<1`. At `t=1`, it
equals `g_h`. Thus a normalized straight interpolation **never rescues an
endpoint diameter blocker** in a two-valued slab move. Any old diameter fixed
at the endpoint also forbids every interior interpolant from attaining diameter
at most `D`.

This applies to a contact-preserving block transposition when its source point
assignment is exactly an unmoved exterior plus one slab translated by `Delta`.
Every source isolate must follow one of those classes and keep its pair slacks;
the theorem does not supply that assignment. No unpromoted extraction is used
as a theorem premise: the application is conditional on these explicit endpoint
properties. It covers both ONE-SIGN and TWO-SIGN endpoint forks; it does not
eliminate either fork itself. A two-axis nonlinear endpoint move remains outside
this obstruction.

## 6. Closing attempts and the exact physical gap

The gap-tree attack first suggested converting a leaf into a physical hinge.
Theorem 2 would immediately exclude an actual hinge involving two source
vertices. This conversion fails: a gap vertex labels a physical layer, which
may contain many source vertices and many crossing unit contacts. A private
row in a spanning-tree basis does not delete those contacts, the other diameter
rows, or the other vertices in the layer. Also Theorem 3 makes clear that no
single actual diameter is essential for infinitesimal rigidity of the full
mixed framework. This is consistent with positive gap circulation; it does not
reopen the already rejected private-leaf release.

The next attack used contact-bridge endpoints. Corollary 4.1 gives an actual
crossing diameter avoiding both endpoints. It does not force that diameter to
be parallel to a forbidden direction, nor contradict the diameter-thrackle
intersection law. A common positive-contact bridge block is not itself a
two-source-vertex separator. No split-star, inactive-interface, or macroscopic
container branch is eliminated by simply relabeling it as one.

Pushing that cut result into the loaded incidence ledger succeeds in (7):
diameter leaves require a second contact, and diameter-component deficiency
pays at least `2d_H` extra incidences. The attempt to turn this into more
distinct cell attachments fails at contact multiplicity. The square gives a
sharp finite stress-compatible witness, while in a harmonic cell both contacts
of a loaded leaf may lead into the same component. No existing upper ledger
makes the extra contact payment contradictory.

The finite contact-isometry attack yields (4)–(6), but the two-sign diameter
obstruction survives: a positive *average* gain does not make every old
diameter nonlengthening. Corollary 5.1 requires simultaneous old upper
feasibility and full-source protection from newly active pairs.
Equations (8)–(9) explicitly test the attempted interpolation rescue. The
contact-restoring dilation contributes `A_*`, so a weighted endpoint gain alone
cannot justify a small feasible interpolant. The affine route has `G=0` and
cannot close; a genuinely nonaffine endpoint and all source constraints remain
necessary.
Pushing the test into a two-valued slab motion gives the exact no-rescue result
(11): every endpoint upper blocker survives every restored straight interpolant.
Thus smoothing the finite TB1 endpoint in this way cannot remove its TWO-SIGN
obstruction or its fixed old diameters. This mechanism is exhausted at an exact
inequality, rather than left as an untested competitor proposal.

The exact next obligation is one of the following source-level statements:

* produce an actual `S subset V`, `|S|<=2`, and a component of `C-S` with no
  surviving actual diameter endpoint; or
* produce a noncongruent finite contact-isometry that preserves every full-source
  lower slack and every old diameter upper bound, and has `N_H<L_H`.

Neither is supplied by abstract gap connectivity or by carrier geometry. This
report changes no canonical frontier. All live C-II and Level I branches remain.

## 7. Regression: local rigidity alone permits a two-point hinge

Take four points

\[
 p_0=(0,0),\ p_1=(2,0),\ p_2=(1,1),\ p_3=(1,-2)
\]

and bars `01,02,12,03,13`. Their exact planar rigidity rank is five. Reflecting
`p_3` to `(1,2)` preserves all five bars but changes `|p_2-p_3|` from three
to one. The graph has the two-vertex cut `{0,1}`.

This rejects deriving Theorem 1 or 2 from ZF rank alone. It is not a canonical
source: its bars are not all actual contact/diameter pairs and its minimally
rigid graph has no nonzero self-stress. The positive semidefinite maximal-rank
stress premise is essential.

## 8. Regression: finite contact preservation can jump to a strict competitor

The regular unit heptagon has exactly its seven sides as contacts and its seven
step-three chords as diameters. Put `t=pi/14`. Its diameter is

\[
 D=\frac1{2\sin t}>2,
\]

since `sin t<t<1/4`. Assign `alpha=D^2/7` to every contact and `beta=1/7` to
every diameter. These weights are strictly positive and equilibrated. Its
stress is positive semidefinite with precisely the three affine kernel modes.
Here is a direct check, so the older unpromoted regular-shell regression is
not used as an unqualified premise. On Fourier mode `j=1,...,6`, its eigenvalue
times `7/4` is

\[
 \frac{\sin^2(2jt)}{4\sin^2t}
 -\sin^2(j\pi/2-jt).
\]

For even `j` this equals
`sin^2(jt)[cos^2(jt)/sin^2(t)-1]`, nonnegative, zero only at `j=6`.
For odd `j` it equals
`cos^2(jt)[sin^2(jt)/sin^2(t)-1]`, nonnegative, zero only at `j=1`.
The constant mode is the other zero mode. Its mixed framework is infinitesimally
rigid by an independent argument: the nondegenerate bar triangles
`(0,1,4), (1,4,5), (1,2,5), (2,5,6), (2,3,6)` successively add one vertex
along an already rigid shared edge and cover all seven vertices. Two fixed
nonparallel bars determine the first-order velocity of each newly added vertex.

Now retain vertex labels and place them at

\[
 q_0=(0,0),\ q_1=(1,0),\ q_2=(1/2,\sqrt3/2),
 q_3=(-1/2,\sqrt3/2),\ q_4=(-1,0),
 q_5=(-1/2,-\sqrt3/2),\ q_6=(1/2,-\sqrt3/2).
\]

Every old cycle contact is still unit. All pairs are at least one and the new
diameter is two, strictly below the heptagon diameter. The squared lengths of
the seven old step-three diameters are exactly

\[
 (1,4,4,4,1,3,3).
\]

The placement creates additional contacts and unit equilateral triangles.
Its finite stress gain is exactly `D^2-20/7>8/7`.

This is a concrete finite jump from a positive-stressed, locally rigid,
triangle-free planar source to a smaller feasible planar source preserving all
old contacts. It rejects one-sided versions of Theorem 1 and the attempted
claim that the stress/rigidity facts alone prevent such finite competitors.
It also proves that the initial heptagon is **not globally optimal**. It is
neither a Level I disproof nor a counterexample to Corollary 5.1 for a global
normal-form source. No interpolation through feasible sources is claimed.

## 9. Exact checks, claim classification, and handoff

Run

```bash
python3 research/verify_target_c_finite_core_rigidity_2026_10_02.py
python3 tools/check_theorem_state.py
git diff --check
```

The certificate uses rational arithmetic (and exact symbolic linear algebra)
for a square stress, its kernel and three-direction metric test, a lifted
contact-isometric placement, the affine rhombus's restored-interpolation
polynomials and two-valued blocker, the hinge rank/flip, and all 21 pairs of the
seven-point triangular-lattice replacement. The analytic heptagon stress and
the general graph/matrix implications are proved above, not inferred from
finite numerical samples.

| Claim | Classification | Remaining limit |
| --- | --- | --- |
| Finite mixed core rigidity | proved candidate awaiting promotion | core only; equal active lengths |
| Three-vertex connectivity and two-puncture anchoring | proved candidates awaiting promotion | source vertices, not gap vertices |
| Leaf/component contact incidence (7) | proved candidate awaiting promotion | counts multiplicity; no new upper ledger |
| Weighted finite gain and mandatory replacement | proved candidates awaiting promotion | simultaneous upper/lower feasibility still required |
| Restored interpolation (8)–(9) | proved candidate awaiting promotion | necessary finite threshold; inactive pairs omitted |
| Two-valued slab interpolation no-rescue (11) | proved candidate awaiting promotion | endpoint hypotheses; nonlinear two-axis moves remain |
| ZF alone implies finite rigidity | regression / rejected attempt | exact two-triangle hinge |
| PSD core stress prevents contact-isometric strict competitors | regression / rejected attempt | exact heptagon-to-seven-point placement |
| Gap-tree leaf gives a physical hinge | unproved attempted bridge | layers are multi-vertex sets; other actual rows survive |

**Promotion recommendation:** retain as unreviewed; request independent audit
before any admission to the canonical stack. Strongest new source consequence:
every contact component remaining after deletion of two core vertices has an
actual surviving diameter endpoint. Required next files are canonical ZR/ZF,
the physical threshold/forest-lift reports, and the full source cutsets. A
future closing proof must produce the physical cut certificate or the finite
placement specified in Section 6, and cover every other surviving C-II branch.
