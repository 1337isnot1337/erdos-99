<!-- theorem-state: {"artifact_id":"ART-DA83393AC1D9","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Hostile audit — dominant-pentagon through-splicing and quadratic orbit deficit

**Phase 2 preservation provenance:** PR #522, branch research/c2-pair14-g00522-sol-20260915, audited source head 2346fb9c3047f26525579df9aced37bc9759e7f6. This source audit records PASS only at the stated proof-only fully force-visible full-core Type-II scope; its artifact lifecycle remains unreviewed and it makes no C-II or Level I closure claim.

**Date:** 2026-09-15<br>
**Reviewed:**
- `research/target_c_dominant_pentagon_through_splicing_2026-09-15.md`
- `research/verify_target_c_dominant_pentagon_through_splicing.py`

**Disposition:** **PASS at proof-only fully force-visible full-core Type-II scope.**<br>
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The candidate claims that all-dominant pentagonal stopping faces create
phase-preserving through-splices, and that `P D` such splices force dominant-orbit
Mantel deficit at least `P^2 D^2/2`.  The main audit risks are: non-simple bounded
faces, false local phase classification, U-turn rather than through continuation,
splice cycles, multiple crossings between spliced paths, and incorrect conversion of
bounded endpoint incidence into all-dominant pentagons.

---

## 1. Degree-five bounded faces are genuine convex pentagons

C51 proves, in the fully force-visible core used here, that every bounded contact face
has a simple strictly convex unit-edge boundary.  Its proof also excludes bridges from
bounded face boundaries.  Therefore a degree-five exceptional face has five distinct
unit sides and five distinct boundary vertices.

The audited endpoint-host theorem separately excludes both a nontrivial train returning
to one bounded face and a bounded singleton loop.  Hence the five stopping-train
incidences of a pentagon belong to five distinct complete trains.

The candidate therefore does not confuse facial-walk degree with a simple polygon.

**Verdict:** PASS.

---

## 2. The lattice-limit phase classification is exact

Choose triangular directions

\[
a=(1,0),\qquad b=(1/2,\sqrt3/2),\qquad c=b-a.
\]

For a limiting all-dominant pentagon let `r_a,r_b,r_c` be the oriented ray imbalances
inside the three projective phase classes.  Closure gives

\[
r_a a+r_b b+r_c c=0,
\]

hence

\[
r_a=r_c=-r_b=r.
\]

Each phase total is congruent to `r mod 2` and at least `|r|`; the three totals sum to
five.  Thus `r` cannot be zero and cannot have absolute value at least two.  Therefore
`|r|=1` and the phase totals are exactly `3,1,1`.  In the size-three phase the two
opposite rays occur with multiplicities `2,1`.

The committed verifier independently enumerates all nonnegative six-ray count vectors
of total mass five and zero vector sum.  There are exactly six, related by rotation,
and every one has this `3,1,1` projective pattern.

**Verdict:** PASS.

---

## 3. The chosen local splice is through-going, not a U-turn

For the representative oriented pattern

\[
a,b,c,-b,-b,
\]

the `+b` side midpoint is `a+b/2`, while the two `-b` side midpoints are `3b/2` and
`b/2`.  Their connector vectors from the `+b` midpoint are

\[
c=b-a,
\qquad -a.
\]

Both are unit vectors making angle exactly `pi/6` with `Jb`, and both have positive
`Jb` projection `sqrt(3)/2`.

The face is convex, so these midpoint chords stay inside the face.  Under shrinking
phase windows every all-dominant pentagon has one of the finitely many lattice-limit
patterns above.  Compactness therefore makes the connector angle
`pi/6+o_rho(1)` uniformly and keeps a positive normal projection.

For a counterclockwise face boundary, rhombi adjacent to a `+b` side lie on its right,
so a train oriented in the positive `Jb` direction approaches that side from the
rhombic region.  At a `-b` side the positive `Jb` orientation leaves the face.  The
connector hence joins an arriving end to a leaving end.

The explicit pentagon regression was also checked numerically in Pyroam before this
candidate was written: for perturbation parameters `0.1,0.05,0.01,0.001`, the two
possible connector directions stay strictly inside the `+-30 degree` cone about the
positive train normal and tend to its boundary as the lattice limit is approached.

**Verdict:** PASS.

---

## 4. Simultaneous splicing creates paths, not cycles

Orient every train in phase `j` by positive projection on the fixed atom normal `n_j`.
The finite stopped-train theorem puts every rhombic midpoint step within `pi/6+o(1)` of
that normal.  Section 3 gives the same sign for every selected connector.

At each selected face the splice joins one incoming train end to one outgoing train end.
Thus the directed splice graph has indegree and outdegree at most one at every train.
A directed cycle would concatenate train pieces and face connectors into a closed curve
with strictly positive `n_j` projection on every nonzero segment, which is impossible.

Therefore a splice graph with `M_D` train vertices and `P_D` splice edges is a forest of
directed paths and has exactly `M_D-P_D` components.

A singleton train contributes only a zero-length midpoint piece.  Any cycle containing
it still contains positive-projection face connectors, so the no-cycle argument is
unchanged.

**Verdict:** PASS.

---

## 5. Spliced supertrains are pseudosegments

This is the most delicate step.

Take two distinct atom phases.  Their central train normals differ by `pi/3`.  Choose
the bisector of those normals as a common coordinate direction.  Every constituent
train step and every splice connector lies within `pi/6+o(1)` of its own normal, so
for sufficiently small frozen windows its projection on the common coordinate is
strictly positive.  Each supertrain is therefore a graph over that coordinate.

Connector interiors lie in distinct bounded-face interiors.  The contact graph, and
hence every rhombic train centerline, is disjoint from those interiors.  Only one
connector is chosen per pentagon.  Thus intersections of two supertrains are exactly
original strict-rhombus train crossings.

For adjacent atom labels write the contact directions as

\[
\phi_i+x_i,
\qquad
\phi_i+\pi/3+x_j.
\]

An actual strict-rhombus crossing requires projective separation strictly greater than
`pi/3`, hence `x_j>x_i`.  With the positive-normal orientations, the first train's
centerline tangent in that rhombus is the positive second side direction while the
second train's tangent is the negative first side direction.  Their oriented
intersection determinant consequently has one fixed sign.  This is the local crossing
sign used in the existing phase-order arguments.

Two graphs over one coordinate cannot cross transversely twice with the same sign:
their vertical order must alternate after successive intersections.  Hence two
supertrains meet at most once.

Same-phase supertrains have no rhombic intersections because their projective contact
directions lie in one window of diameter less than `pi/3`, whereas a strict-rhombus
crossing requires separation greater than `pi/3`.  Their connectors lie in disjoint
faces.  Thus the full supertrain intersection graph is simple.

**Verdict:** PASS.

---

## 6. The graph-theoretic deficit is correct

After `P_D` forest contractions there are

\[
N_D=M_D-P_D
\]

supertrains.  Let `r_D<=P_D` be the number of nonsingleton components and
`s_D=N_D-r_D` the singleton components.  The singleton induced graph is a subgraph of
the original stopped-train crossing graph and is therefore triangle-free, giving at
most `s_D^2/4` edges.

The whole quotient is simple, so edges incident to a nonsingleton component are at
most

\[
r_Ds_D+{r_D(r_D-1)\over2}.
\]

Hence

\[
E_D\le{s_D^2\over4}+r_Ds_D+{r_D(r_D-1)\over2}.
\]

At fixed `N_D` this is increasing in `r_D` throughout the linear regime up to
`r_D=P_D`; substituting `r_D=P_D` and `N_D=M_D-P_D` gives the slightly stronger finite
bound

\[
E_D\le {M_D^2\over4}-{P_D^2\over2}-{P_D\over2}.
\]

Dropping the favorable linear term yields the candidate's asymptotic

\[
d\ge p^2/2.
\]

**Verdict:** PASS.

---

## 7. All-dominant pentagon incidence count is not overcounted

Let `f_5` be the number of pentagonal exceptional faces.  Since

\[
Q-f=\sum_F(\deg F-5),
\]

the number of faces of degree at least six is at most `Q-f`, so

\[
f_5\ge2f-Q.
\]

Total bounded train-terminal incidence is exactly `Q+4f`.  Dominant trains contribute
`2M_D-K_D` bounded incidences, because every complete train has exactly two terminal
incidences and `K_D` of the dominant incidences are outer.

Each pentagon that is not all-dominant uses at least one distinct non-dominant bounded
terminal incidence.  Therefore

\[
H_D\ge2M_D-K_D-2Q-2f.
\]

No bounded endpoint incidence is charged to two faces.

**Verdict:** PASS.

---

## 8. Elimination to the new `K` constraint has the correct directions

The standard orbit inequalities give

\[
m\ge4\Delta_2/C,
\qquad
d\le C^2/4-\Delta_2,
\qquad C\le U.
\]

The exact ledgers are

\[
\chi=2t-\pi-\delta,
\qquad
2\varphi=C-t/2+\kappa/2.
\]

Substitution gives

\[
p\ge8\Delta_2/C-K-C+t-U-\kappa.
\]

The function `8Delta_2/C-C` is decreasing, so replacing `C` by the larger `U` weakens
the lower bound safely.  Meanwhile `d<=C^2/4-Delta_2<=U^2/4-Delta_2`.  Combining with
`d>=p^2/2` gives exactly

\[
K\ge {8\Delta_2\over U}-2U+t-\kappa
-\sqrt{U^2/2-2\Delta_2}.
\]

The radical is real throughout the current low-`t` region because the matched atomic
floor already has `U>2sqrt(Delta_2)`.

**Verdict:** PASS.

---

## 9. Scope and remaining obligation

The through-splice is a topological counting construction, not a source motion and not
a new unit contact.  Therefore it introduces no unit-separation feasibility claim.

The theorem supplies a genuinely new lower constraint on the dominant outer-terminal
allocation `K`.  It does not by itself prove a new `t` floor until combined with the
current direct dominant/complement edge-energy functional.  That scalar propagation is
handled separately so that no hidden monotonicity claim is bundled into the structural
proof.

**Final disposition:** PASS at proof-only fully force-visible full-core Type-II scope.
C-II remains open.
