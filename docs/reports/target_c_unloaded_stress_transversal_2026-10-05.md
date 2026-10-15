<!-- theorem-state: {"artifact_id":"ART-0A70E2577845","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — the residual stress cage can be cut at unloaded vertices

Date: 2026-10-05. Base main: `3c94a1a93641a5f8fa24d43068d487594d3e38cd`.
State: `2026-10-05.audit.57`. Classification: **proved candidate awaiting
independent audit**; artifact lifecycle remains **unreviewed**.
C-II and Level I remain open.

## 1. Exact consequence and dependencies

```
full-core loaded-chord localization + one nonunit loaded-hull side
-> no normalized stress supported only on loaded vertices
-> <=s_Z+1 unloaded vertices hit every normalized KKT stress
-> a strict contact-opening descent retaining every original diameter edge
-> strict refill pays |S union U|, not |S|+|U| if interiors contain U.
```

The last implication requires actual certified packets; their existence
or finite activation is not supplied. The diameter-only cover theorem
cannot exploit such overlap: its deleted endpoints are hull-extreme and
therefore outside every wall interior. Here U consists of unloaded
positive-contact vertices and can overlap a replacement population.
This is a localization of the cage cost, not an asymptotic closure.

Canonical inputs are full positive C,H and core mixed rank (Section 57),
the normalized stress-polytope dimension s_Z (Section 64), and
`C-FULLCORE-LOADED-CHORD`, which says loaded-loaded unit contacts in the
full-core branch are consecutive loaded-hull sides. The geometric leaf
argument is also used in Section 72's primitive-cycle proof; below it is
applied to a stress supported on the loaded subframework, without
importing the primitive cycle's selected ZR/ZF conclusions. The
polytope face method is prior art in the unpromoted
[stress-transversal report](target_c_stress_transversal_reinsertion_2026-09-12.md).
It is rederived for interior vertex coordinates here, not promoted as a
new general face theorem. The strict signed-row separation is rederived
as in the [contact-opening candidate](target_c_contact_opening_cage_transversal_2026-10-05.md).

## 2. Finite loaded-only obstruction

Let A be a canonical C-II source, V its positive-contact core, B its
actual loaded diameter endpoints, and I=V\B. Write P for the normalized
nonnegative KKT stress polytope on all actual C,H. Define

    P_B={s in P: every contact incident to I has coefficient zero}.

Every actual diameter endpoint belongs to B, so this is precisely the
set of normalized stresses supported entirely on the loaded subframework.
This definition and the transversal criterion below apply in both
branches. The following sufficient geometric test uses full-core scope.

**Theorem U.1.** In the full-core loaded-chord branch, if at least one
side of F=conv(B) is nonunit, then P_B is empty. If P_B is nonempty,
all loaded-hull sides are unit, every stress in P_B has strictly positive
contact weight on the entire hull cycle, and its positive diameter
support is an edge cover of B.

**Proof.** A stress in P_B can have positive contact weight only on the
unit sides of the loaded hull. Suppose its positive contact graph has
a degree-one vertex p, with its sole positive contact neighbor b. Use
an outward normal n to the hull side pb. The contact force has zero
n-component. Every diameter partner q of p is a loaded vertex different
from p,b; D>1 excludes b. Strict hull extremality gives
n dot (p-q)>0. Thus equilibrium at p forbids any positive incident
diameter weight. With none, the remaining nonzero contact force cannot
balance. A degree-one vertex is impossible.

The stress has at least one positive contact: the virial identity is
sum alpha=D^2 sum beta=D^2. A proper nonempty subgraph of a simple
cycle has a path component and hence a degree-one vertex. Its positive
contact graph must therefore be the entire loaded-hull cycle. This
requires every hull side to be a contact and proves the nonunit-side
exclusion. At each cycle vertex its two noncollinear contact vectors
have positive weights and a nonzero sum, so at least one positive
diameter reaction is incident there. This gives the edge cover. QED.

No loaded-chord localization is asserted in the container branch.
There P_B must be tested on the actual loaded subframework; a missing
unit hull side alone is not claimed to decide it.

## 3. Exact interior-transversal criterion

**Theorem U.2.** A vertex set U contained in I whose deletion destroys
every normalized KKT stress exists if and only if P_B is empty. If P_B
is empty, one can choose |U|<=s_Z+1. The resulting reduced source has
a straight sufficiently small motion strictly opening every surviving
unit contact and shortening every original diameter pair. No actual
diameter endpoint or diameter edge is removed.

**Proof.** For u in I let

    f_u(s)=sum of contact coefficients incident to u,
    F_u={s in P:f_u(s)=0}.

These are nonnegative linear functionals and their zero sets are faces.
Their full intersection over I equals P_B. If P_B is nonempty, its
stress survives deletion of any subset of I, proving necessity.

If P_B is empty, take a minimal family of faces F_u with empty
intersection and let U be its index set. For each u in U choose a
stress s_u in all the other faces; minimality guarantees such a stress,
and f_u(s_u)>0. For different u,w, f_w(s_u)=0. The stresses s_u are
affinely independent: apply each f_w to an affine dependence to force
its coefficient at s_w to vanish. Thus |U|<=dim_aff(P)+1=s_Z+1.

A normalized stress on A\U would extend by zero to a stress of A in
all the chosen faces. Conversely any such original stress restricts
to the reduced source. Therefore there is no reduced normalized stress.

On retained core coordinates use signed rows r_c for contact lower
constraints and -r_h for diameter upper constraints. A nonzero
nonnegative relation gives KKT equilibrium; pairing with the position
field gives sum alpha=D^2 sum beta, so it has positive diameter total
and normalizes to the excluded stress. Hence zero is outside the convex
hull of these signed rows. Its nearest point to zero separates all rows
strictly, furnishing a velocity positive on every signed row. The
straight small motion opens contacts and shortens all H. Finitely many
inactive lower and upper slacks persist. Every retained source isolate
is held fixed: it has no active row, and all its inactive constraints
are included in this finite check. QED.

The equivalence is an exact stress criterion, not the assertion that
all finite nonlinear release paths are characterized by first order.
No uniform motion radius or finite activation distance is claimed.

## 4. Replacement demand with overlap

Let actual simple unit-contact walls have disjoint interiors, let S be
the union of their complete old interior populations, including isolates,
and let their certified open wall-safe packets have total size M.
For the U of Theorem U.2 assume

    M>=|S union U|=|S|+|U\S|.                 (4.1)

Then a same-cardinality strict sub-D competitor exists.

Strictify the finite packets by tiny dilation. The canonical wall shield
supplies simultaneous strict new-old clearance against A\S and strict
cross-packet clearance. Interior-hull location gives strict upper bounds
against every old point and between packet sites. Choose exactly
|S union U| sites. Apply the small motion of A\U from Theorem U.2,
choosing its size only after these finite margins have been fixed.
Delete the additional moved labels of S\U and insert the selected sites
at their original positions. Every surviving old diameter was shortened;
every inactive upper constraint and every new pair keeps strict upper
slack. All old lower constraints are strict after opening, and all new
lower constraints keep their margins. Cardinality is unchanged.

Walls need not remain contact walls under this opening motion. They
certify original finite margins, which persist by continuity. Deleted
wall vertices can be ghost guards; all actual retained pairs are checked.
The formula counts an overlapped label once and never drops an isolate.

For packets already available at the original source, the canonical
contact-minimality endpoint may exclude them even sooner. Equation (4.1)
does not create a packet or establish an activating finite motion. Its
possible use is localization of the cage deletion inside populations
being replaced, including packets obtained after a separately certified
nonlocal motion. In that setting all final pair margins must be proved
at that actual endpoint; the initial step theorem alone is insufficient.

## 5. Exact surviving split

In the full-core branch with a nonunit loaded-hull side, cage deletion
can be placed on at most s_Z+1 unloaded core labels. If actual refill
interiors contain them, there is no additional cage population to pay.
The required equal-cardinality strict refill remains unproved.

When P_B is nonempty, no deletion confined to unloaded vertices can
destroy the stress cage. Full-core localization identifies its blocker
as a positive unit loaded-hull cycle with diameter support covering every
loaded vertex. This is sharper than an unspecified residual constraint,
but it does not exclude that cycle in a source containing additional
interior points. Section 72's primitive-source quantifiers are not
silently extended to this selected subframework.

For the container branch, Theorem U.2 and the packet accounting hold
conditional on P_B being empty; Theorem U.1's chord-localization test is
not imported. No exhaustive branch or Level I status is changed.

The universal proofs are finite and analytic. No numerical verifier is
needed; repository consistency checks do not constitute independent
mathematical promotion.

## 6. The new release does not automatically enlarge its vacancies

There is an exact obstruction to a local restoration of the deleted
unloaded labels. Fix the original strictly positive normalized KKT
stress. Let u be a reduced-source velocity supplied by Theorem U.2.
Assign arbitrary velocities to the deleted labels U, and let r_e(u)
be the original contact or diameter length derivative. The retained
active rows have strictly positive signed work:

    W=sum_{c not incident to U} alpha_c*r_c(u)
                         -sum_H beta_h*r_h(u)>0.

All diameter endpoints are retained. Original equilibrium gives

    sum_{c incident to U} alpha_c*r_c(u)=-W<0.       (6.1)

The left side is independent of the assigned velocities at U: their
coefficients are the original equilibrium forces at those unloaded
vertices, and these vanish. Thus every attempted differentiable
restoration with the given reduced velocity shortens at least one old
unit contact incident to U. An unloaded transversal supplies a descent,
not an infinitesimally expanding vacancy. This is a weighted contact
work identity, not a force-bulk localization or a coefficient floor.

More generally the full original core is locally isolated, modulo
Euclidean motions, among realizations satisfying all original contact
lower and diameter upper constraints. To see this, choose a local
Euclidean gauge. Its dimension is 2v-3. The signed active rows r_c,-r_h
span that dual space by canonical mixed rigidity and have a strictly
positive zero relation by canonical full positive KKT support. Therefore
for every nonzero displacement direction one signed row is negative.
Compactness of the unit sphere supplies a source-dependent c>0 with

    min_e a_e(z)<=-c*||z||.

The squared-distance constraint functions have remainders bounded by
||z||^2. For 0<||z||<c the chosen constraint is violated. This proves
a positive finite core neighborhood with no noncongruent feasible
realization of diameter at most D. Source isolates remain unconstrained
by this core conclusion; no full-source affine-kernel theorem is used.

Consequently an equal-cardinality refill obtained after deleting U
must genuinely leave this source-dependent core neighborhood if its
sites can be identified with the original deleted core labels. Neither
(6.1) nor this neighborhood has a uniform asymptotic size. They do not
rule out a far packet or a nonlocal competitor. They identify why the
initial strict release cannot itself be counted as capacity activation.

## 7. A surviving loaded-only cage needs just one boundary deletion

There is a useful improvement in the placement, rather than the total
number, of deleted labels.

**Theorem U.3.** In full-core loaded-chord scope, suppose P_B is nonempty.
Choose any loaded vertex b. There is a set U contained in I with
|U|<=s_Z such that deleting {b} union U destroys every normalized KKT
stress. Thus a reduced strict contact-opening/diameter-shortening motion
exists. All deleted labels except b can lie in a refill population.

**Proof.** Let P_b be the face of P where every positive-coordinate
candidate incident to b, contact or diameter, is zero. The original
full positive stress loads b, so P_b is a proper face. If it is empty,
b alone suffices. Otherwise dim(P_b)<=s_Z-1.

By Theorem U.1 every stress in P_B has a positive diameter reaction at
b. Consequently P_B intersect P_b is empty. Restrict the unloaded
vertex faces F_u of Theorem U.2 to P_b. Their total intersection is
empty. A minimal empty family has at most dim(P_b)+1<=s_Z members,
by the same affine-independence proof. Call its vertices U. A stress
surviving deletion of b and U would extend to a point of P_b in all
those faces, which is impossible. The signed-row separation and finite
small-motion proof applies to the reduced source exactly as before.
No assertion is made that the diameter pairs incident to b survive.
QED.

Theorem U.1 also says every hull side is unit in this case. The cycle
is the actual simple wall of F. All unloaded core labels lie strictly
inside F: at any nonloaded core vertex on a supporting line, positive
contact equilibrium forces every neighbor onto that line, giving at
most two unit neighbors and contradicting the canonical unloaded degree
lower bound three. Thus if S=A intersect int(F), including every
interior isolate, U is automatically a subset of S, while b is not.
The exact packet demand is consequently

    M>=|S union U union {b}|=|S|+1.                 (7.1)

A strict packet at the original source is spent using the same finite
margin proof as Section 4, and gives a strict sub-D competitor after the
reduced motion. Exterior isolates remain fixed and the actual unit wall
shield verifies their lower clearance; the old interior-hull argument
verifies their upper bounds. This reduces the cage payment outside the
replacement population to one, independently of s_Z.

For an arbitrary wall bank containing U the same outside payment is
one; without that containment it is 1+|U\S|. The hull-cycle wall supplies
the containment here, but not the packing capacity. A packet available
only after finite movement still needs its endpoint geometry, all source
constraints and strict pair margins separately certified. Equation (7.1)
is not inferred from positive residual, phase mismatch or the fact that
most of the cage deletions are interior.

At the original normalized source the one-spare contact-minimality
endpoint already excludes such a packet. The new consequence is that a
boundary-only blocker cannot force s_Z+1 boundary labels to be paid for
by a post-motion refill: one boundary deletion and at most s_Z deletions
inside the old refill population suffice to start the reduced descent.
No global motion or activating packet follows from this finite theorem.
The all-unit hull branch remains open.
