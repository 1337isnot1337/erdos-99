> Generated reading edition · [exact source](../../../docs/reports/target_c_inclusive_floor_closure_and_locked_contact_release_2026-10-10.md) · source SHA-256 `25dcc76277cc3382b7334d2c2d748850dcd04a3ddbdc694d4f6729c6fd2ca218`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-D33DAE46A3ED","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Inclusive floor closure and locked contact-preserving releases

**Worker:** Slot 01, Target C-II, source-realized outer-face finite motion.

**Checkpoint date:** 2026-10-11, continuing the run started 2026-10-10.

**Base:** `ab6dd3336f9f8d440f2bada76edb32153391cddc`.

**Authority:** `2026-10-10.audit.234`; PR #947 remains unmerged.

**Classification:** proved candidates awaiting independent audit; finite regressions.
**Status:** C-II and Level I remain open. No canonical promotion is requested by this report alone.

This extends the strict-cut theorem FC in
[the preceding report](target_c_parallel_release_floor_closure_and_isolate_transport_2026-10-10.md).
FC is valid in its stated class, which requires a positive active height to
exceed its contact-opening floor. The equality case is a different finite
endpoint: it can preserve every contact and shorten an old diameter. A weak
diameter equality may permit that height; an inactive pair required to remain
strictly below the diameter may forbid it. Collapsing these two constraints
into a common weak shortest-path cost loses the distinction.

The new results are:

1. **IFC:** exact inclusive-floor feasibility, with strict pair constraints,
   decided by lexicographic shortest paths and a finite zero-closure. Its output
   contains the union of all feasible active supports in the specified class.
2. **CLR:** the weak-upper version detects every contact-loss endpoint in that
   class, including endpoints that lose only some cut contacts at their floor.
3. **LCR:** the strict-inactive-core-upper version turns any surviving proper
   core group into a full-source lexicographic contradiction, even when its
   height merely equals its floor and preserves contacts. Isolates can be
   independently transported and then normalized by canonical Audit.177.
4. **SC:** a canonical survivor must have actual-pair collapse paths with either
   cost strictly below a positive floor or a strict witness on an equal-cost
   path. A weak equal-cost lock alone is insufficient.

The closure chain is

```text
actual contact-independent source groups and a direction
  -> inclusive floor closure with all full-source pair constraints
  -> contact loss, or contact isometry with no new core diameter pairs
  -> contact minimum, or normalized diameter-pair minimum, is contradicted.
```

The unresolved implication is the first source extraction plus survival, not
abstract feasibility or the all-pair endpoint check. None of the finite
examples below supplies a canonical global source or that extraction.

## 1. Exact full-source class

Let P be a finite labelled unit-separated planar source of diameter D>1.
Partition every label into nonempty fixed G_0 and disjoint moving groups
G_1,...,G_r. No old unit contact may join distinct positive groups. Fix a unit
direction v. Keep G_0 fixed and translate G_i by s_i v. Every label, including
every contact isolate, is retained.

For a cut contact p in G_i, q in G_0, put

```math
 \tau_{pq}=-2(p-q)\cdot v,
 \qquad F_i=\max(\{0\}\cup\{\tau_{pq}:pq\in C[G_i,G_0]\}).
```

The allowed heights are

```math
 0\le s_i\le U_i,\qquad s_i=0\ \text{or}\ s_i\ge F_i,
 \qquad s_i>0\ \text{when group }i\text{ is active}.                 \tag{1}
```

Thus a zero-floor active group must still have positive height. The cut squared
length is exactly

```math
 |p-q+s_i v|^2=1+s_i(s_i-\tau_{pq}).                               \tag{2}
```

All old contacts remain unit or open; there are no contacts between different
moving groups. At a positive floor, only cuts with tau=F_i stay unit. Smaller
tau cuts open. No new unit pair is permitted.

For an arbitrary intergroup source pair, oriented from G_i to G_j, write

```math
 a=(p-q)\cdot v,\quad z=(p-q)\cdot Jv,
 \quad u=\sqrt{D^2-z^2},\quad \Delta=s_i-s_j.
```

Every upper bound is the pair of difference inequalities

```math
 s_i-s_j\le u-a,\qquad s_j-s_i\le u+a.                            \tag{3}
```

Both costs are nonnegative since the source pair is at most D. An old
non-diameter pair has strictly positive costs. If it must remain strictly
below D, both inequalities are strict.

For an old noncontact, a lower bound is automatic if |z|>1. If |z|<=1, put
ell=sqrt(1-z^2). Unit separation and noncontact give |a|>ell. Preserve its
original projected order and strict lower bound by imposing

```math
 \begin{cases}
 s_i-s_j<-a-\ell,&a<0,\\
 s_j-s_i<a-\ell,&a>0.
 \end{cases}                                                     \tag{4}
```

These costs are strictly positive, including the case |z|=1, ell=0. Pairs
inside a group do not change and are checked in the original source.

Two upper policies will be used. **Contact policy A** leaves every inequality
(3) weak. **Core replacement policy B** leaves actual diameter upper bounds
weak, marks each inactive core-core upper inequality strict, and leaves
isolate-involving upper inequalities weak. Policy B uses the original
nonisolated core V; isolated labels may share a translating core group or
have their own zero-floor groups. Equations (1)--(4) still check every pair.

We deliberately specify the class: nonnegative heights, no contacts between
different moving groups, and original projected order for old noncontacts
with |z|<=1. This is not a decision procedure for arbitrary finite motions.

## 2. IFC: inclusive floors with strict costs

The following finite theorem is independent of canonical source optimality.

Let vertices be 0,1,...,r, with s_0=0, and add a weak bound edge i->0 of cost
U_i. A pair edge i->j has nonnegative cost c_e and mark k_e in {0,1}; it
means s_i-s_j<=c_e when k_e=0 and s_i-s_j<c_e when k_e=1. Assume every marked
edge has c_e>0. Floors F_i are nonnegative and bounds are finite.

Associate the **formal lexicographic cost**

```math
 \widehat c_e=(c_e,-k_e),
```

with ordinary componentwise addition and lexicographic comparison. It encodes
c_e-k_e epsilon for an infinitesimal positive epsilon; the proof below chooses
an actual positive rational epsilon when the data are rational.

Start Z={0}. Compute shortest lexicographic path costs to Z,

```math
 d_i=(a_i,-m_i),\qquad d_z=(0,0)\ (z\in Z).
```

Every vertex reaches 0 through its finite bound. Each edge is lexicographically
nonnegative. A positive-real cycle increases cost; a zero-real cycle has only
weak edges and does not change the strict count. A shortest path can therefore
be chosen simple, and 0<=m_i<=r. Ordinary Dijkstra with pair-valued costs on
the reversed graph computes these paths.

Move i into Z exactly when

```math
 a_i<F_i,\quad\text{or}\quad
 a_i=F_i\ \text{and}\ (F_i=0\ \text{or}\ m_i>0).                  \tag{5}
```

Repeat until no new vertex is removed. At most r rounds remove vertices.
Let I be the final complement of Z.

**Theorem IFC.** I is the unique maximal active support allowed by (1) and all
weak/strict difference constraints. A simultaneous feasible endpoint with
exactly that support is constructed below. In particular, a positive equal-floor
cap with no strict edge on a shortest path survives; it is not discarded.

### Necessity of each elimination

Inductively all vertices already in Z have height zero in every feasible
endpoint. Sum inequalities along a shortest i-to-Z path. They give s_i<=a_i;
the inequality is strict if m_i>0. Hence an active height cannot attain its
floor if a_i<F_i or if a_i=F_i>0 and m_i>0. When a_i=F_i=0, nonnegativity
forces s_i=0. This proves (5), including all recursive eliminations. Every
feasible active support is contained in I.

### Construction and strictness, without an infinitesimal limit

Use the final a_i,m_i, putting both equal to zero on Z. The path inequality

```math
 d_i\le d_j+(c_e,-k_e)
```

holds for every edge, also when i is a zero vertex. Consequently

```math
 w_e=c_e-a_i+a_j\ge0,
 \quad w_e=0\Longrightarrow m_i\ge m_j+k_e.                      \tag{6}
```

Let eta be the minimum of 1, all positive w_e, all costs of strict edges,
and all positive a_i-F_i for i in I. Empty parts of this list are omitted;
the retained 1 makes the list nonempty. Set

```math
 \epsilon={\eta\over2(r+1)},\qquad s_i=a_i-m_i\epsilon.           \tag{7}
```

For any edge,

```math
 (c_e-k_e\epsilon)-(s_i-s_j)
 =w_e+(m_i-m_j-k_e)\epsilon.
```

If w_e=0, (6) makes this nonnegative. If w_e>0, then
m_i-m_j-k_e>=-(r+1), so it is at least w_e-eta/2>0. Thus a marked edge has
s_i-s_j<=c_e-epsilon<c_e, and an unmarked edge has its weak bound.
The bound edges enforce s_i<=U_i.

For a surviving vertex with a_i>F_i, subtracting m_i epsilon<=r eta/[2(r+1)]
leaves s_i>F_i. For a survivor with a_i=F_i, rule (5) gives F_i>0,m_i=0,
so s_i=F_i exactly. Zero vertices stay zero. This proves positivity and every
floor, and gives a feasible endpoint with support I. Combined with necessity,
it proves maximality. There is no unproved uniform epsilon or limit exchange.

### Signed clipping

For c>=0, x-y<=c implies max(x,0)-max(y,0)<=c. For c>0, the same statement
preserves a strict inequality: if both inputs are nonpositive the new difference
is 0<c; if only x is positive it decreases; if only y is positive it is
nonpositive; if both are positive it is unchanged. Therefore clipping signed
heights at zero preserves all pair difference constraints.

With no contacts between moving groups, a negative group's cut contacts return
to their original lengths when clipped. A positive group is unchanged. In an
arbitrary signed cut-safe endpoint, a positive height lies at least at F_i:
equation (2) forces s_i>=tau for every positive tau. Negative heights are
handled by reversing v. Thus the two inclusive solves cover signed endpoints
in this projected-order class when the relevant bounds include them. With a
fixed reference label, U_i=2D includes every diameter-D endpoint, since the
old and new pair to that reference both have length at most D.

## 3. CLR: completeness for contact loss

Run IFC with contact policy A. The constructed endpoint satisfies every lower
and upper pair constraint, retains cardinality, and has contact graph contained
in the old one. It loses a contact exactly when some cut in (2) has positive
s_i(s_i-tau).

**Theorem CLR.** If any endpoint in this class loses an old contact, IFC's
constructed endpoint also loses an old contact. Conversely an open cut in the
constructed endpoint is an actual feasible full-source contact loss.

To prove the nontrivial direction, consider an open cut in an arbitrary feasible
endpoint. Its owner is in I by necessity. If its height exceeds F_i, the weak
path cap satisfies a_i>=s_i>F_i, so construction (7) also has height greater
than F_i and opens that cut. If its height equals F_i, positivity gives F_i>0
and the open cut has tau<F_i. Every constructed active height is at least F_i,
so this cut remains open. This also covers F_i=0, since any active height is
then strictly greater than its floor.

For a triangle-free canonical source, an actual contact loss with no new
contacts contradicts contact minimality after global optimality ensures the
same-cardinality diameter-at-most-D endpoint has diameter D. New upper equalities
are permitted in this branch; they do not invalidate the contact-count decrease.

## 4. LCR: the locked contact-isometry branch

Now take the canonical C-II source, D>=9. Keep at least one core label fixed;
every moving group meeting V has a nonempty proper core part. Require no
old contact between distinct moving groups. Include all isolates in the
full-source partition. Run IFC with policy B.

**Theorem LCR.** If IFC leaves a moving group with a nonempty core part, its
constructed full-source endpoint contradicts canonical lexicographic
minimality. This includes active heights equal to their positive floor.

If some old contact opens, CLR's elementary contact-minimum argument applies.
Otherwise the exact old contact graph is preserved. Strict old-noncontact lower
bounds ensure there are no new contacts. For the canonical normalized stress,

```math
 \Omega=L_C(\alpha)-L_H(\beta)\succeq0,
 \quad \Omega P=0,\quad \ker\Omega=\operatorname{span}\{1,P_x,P_y\},
 \quad \sum_H\beta_h=1,\quad \sum_C\alpha_e=D^2.
```

Let g_i indicate the core part of moving group i, and set

```math
 \kappa_i=g_i^T\Omega g_i,
 \quad b_{ij}=g_i^T\Omega g_j.
```

Disjoint groups have no cross contacts, so b_ij is the total positive diameter
weight between them and is nonnegative. Each nonempty proper core indicator
has kappa_i>0: if its energy vanished, PSD would put it in the affine kernel.
A nonconstant affine function taking only zero and one on V puts V on two
parallel lines. The core hull would have at most four vertices. Canonical
force-hull geometry puts every loaded endpoint at a core hull vertex, whereas
`C-ZRF`, `C-LOADED-HULL`, and Woodall give q>=h>=ceil(D)>=9. Contradiction.
This is a core argument; no affine assertion is made about isolates.

For nonnegative heights, the core displacement matrix is
U=sum_i s_i g_i v^T. Expanding the audited contact-isometry energy identity gives

```math
 \sum_{h\in H}\beta_h(D^2-|Q_h|^2)
 =\operatorname{tr}(U^T\Omega U)
 =\sum_i\kappa_i s_i^2+2\sum_{i<j}b_{ij}s_i s_j>0.                \tag{8}
```

The strict inequality holds because an active core group has s_i>0.
Every old diameter has length at most D by the full-source constraints, so at
least one old diameter pair strictly shortens. Policy B prevents all new core
diameter pairs. Isolate-involving pairs are allowed to be at D, but all such
pairs remain strictly above one.

Apply canonical `C-FULL-SOURCE-ISOLATE-NORMALIZATION` (Audit.177) to Q: retain
the core, move every isolate toward the core centroid with
0<t<=sigma/(8D^2), where sigma is the actual minimum isolate-involving squared
lower slack. This preserves every contact and full-source constraint and puts
every isolate-involving distance strictly below D. Core distances, including
the shortened old pair, are unchanged. The final diameter graph is therefore
a strict subset of the old one. Either its diameter is below D, contradicting
globality, or it is D and violates diameter-pair minimality. QED.

Dependencies are canonical C-I PSD, `C-ZRF`, force-hull/loaded-hull and Woodall,
`C-FINITE-CONTACT-ISOMETRY-DIAMETER-GAIN` (Audit.120), and
`C-FULL-SOURCE-ISOLATE-NORMALIZATION` (Audit.177). No pending PR or unreviewed
report is used as a theorem premise. The positive-cone expansion is reproduced
above rather than merely importing the earlier unreviewed Slot 01 claim SG.

The two policies are complementary. Policy A is complete for contact loss
while permitting new core diameter pairs. Policy B accepts locked contact
isometries but restricts those new pairs. A surviving isolate alone gives
neither the contact-loss conclusion nor the strict core energy (8).

## 5. SC: an exact necessary source-level collapse certificate

For any supplied family satisfying LCR's assumptions, canonical survival
requires that every core group be eliminated. A group eliminated in a round
has a directed owner-variable path to a previously forced-zero group with

```math
 \sum_{e\in\pi}c_e<F_i,
 \quad\text{or}\quad
 \sum_{e\in\pi}c_e=F_i>0\text{ with a strict edge},
 \quad\text{or}\quad F_i=\sum_{e\in\pi}c_e=0.                   \tag{9}
```

For positive floors, an all-weak path of cost exactly F_i cannot force zero.
This is the new difference from a strict-cut-only obstruction certificate.
With U_i=2D, no path in (9) uses an artificial bound: every contact floor is
at most 2, while 2D>2. Thus every edge is witnessed by an actual source pair.

A lower witness of cost c has |a|=ell+c and squared length
1+2ell c+c^2<=(1+c)^2, so its original length is at most 1+c. An upper witness
of cost c reaches the circle of radius D by an axial change of magnitude c;
the reverse triangle inequality gives original length at least D-c. A strict
edge in policy B is either an old noncontact lower witness or an inactive
core-core upper witness. Inactive isolate upper pairs are weak and cannot
supply that strict equality witness.

These paths connect owner variables. Successive witness pairs may use different
labels within one owner. They are **not** asserted to be physical unit paths,
train returns, or geometrically short curves. Turning (9) into a population
or loaded-hull contradiction remains a separate mathematical obligation.

## 6. Exact full-source equality and replacement regressions

Here are two six-label sources, both explicitly nonglobal and without the
canonical KKT hypotheses. They demonstrate why the equality rule and upper
policy distinction are mathematically necessary.

Put t=1/100, delta=4t/(1+t^2), a=(1-t^2)/(1+t^2), D in {20,30,50}, and

```math
 w=(-5/13,12/13),\quad f=(-a,\delta/2),\quad
 M_0=0,\ M_1=w,\ F_0=f,\ F_1=w+f,
 \quad Q=(-\sqrt3 D/2,D/2).
```

Move only {M_0,M_1} upward. Its four old contacts are M_0M_1, F_0F_1,
M_0F_0, M_1F_1; the complete contact graph is a triangle-free rhombus.
The floor is delta. The remaining two anchors are contact isolates and are
fixed in these finite regressions.

**Weak actual lock.** Choose

```math
 P=(-\sqrt{D^2-\delta^2/4},\delta/2).
```

The original actual diameters are M_0P and M_0Q. The former gives the exact
weak height cap delta. At height delta every contact remains unit, M_0P stays
at D, and

```math
 |M_0(\delta)-Q|^2=D^2-D\delta+\delta^2<D^2.
```

All other pairs are strictly between one and D. The diameter-pair count drops
from two to one. A strict-cut solver discards this locked height; inclusive
policy B correctly retains it.

**Strict inactive lock.** Instead choose

```math
 P=(-\sqrt{D^2-25\delta^2/16},-\delta/4).
```

Initially |M_0-P|^2=D^2-3delta^2/2<D^2 and M_0Q is the only diameter.
At height delta, M_0P becomes a new diameter and M_0Q shortens by the same
formula above. Contacts remain exactly the same and all pairs stay feasible,
but the diameter-pair count is one before and after. The old-diameter weighted
gain does not give a lexicographic improvement. Policy A permits this endpoint
but reports no contact loss; policy B marks the cap strict and eliminates the
group. Replacing all cap tests by a naive a_i>=F_i test would be unsound here.

The executable enumerates all 15 pairs at both heights in each of the six
fixtures, proves all declared equalities symbolically, and proves strict
inequalities by directed rational algebraic enclosures. These are 180
pair-state checks, including every isolate pair and every newly active upper
constraint. They do not certify a global minimizer: six integer-grid points
fit at squared diameter at most 5, much smaller than D^2. No universal or
infinite-family conclusion is drawn from the three checked D values.

## 7. Validation and rejected simplifications

Run:

```bash
/tmp/e99-slot01-venv/bin/python research/verify_target_c_inclusive_floor_release_2026_10_10.py \
  --graphs 80 --seed 1001001 --diameters 20 30 50
```

The independent finite graph check enumerates every support of 80 rational
graphs with one to four moving variables, using exact Fourier--Motzkin
elimination with strict inequalities. It compares the union of feasible
supports, and feasibility of that union itself, against IFC. It separately
checks every inequality of IFC's constructed rational endpoint. This validates
finite implementation cases; the general theorem is proved in Section 2.
Three additional exact graphs check a weak equal-floor path, the same path
with a strict edge, and a two-round zero cascade. There are 620 enumerated
support checks in total. The six geometric fixtures add 180 full pair-state
checks.

The general implementation uses exact rational costs. For the algebraic
fixtures it retains the exact rational locking costs and zero costs, and
rounds other costs downward with directed rational enclosures. Success is
checked against every original geometric pair. The strict fixture's failure
also has its exact locking-pair obstruction. A failure of such a conservative
compilation on an arbitrary algebraic source would not prove infeasibility.

The earlier common-displacement strategy is obstructed by the exact guarded
source in the preceding report. Unequal strict releases solve that source but
miss floor-preserving endpoints. The present inclusive construction addresses
that missing endpoint class. A third simplification, allowing floor equality
while forgetting strict inactive uppers, is rejected by the second six-point
fixture. These failures concern distinct mathematical implications.

Ruff, theorem-state PR checks, active-route summaries, generated artifact
metadata, and full-branch whitespace checks are run before the checkpoint.
No theorem-state dependency or canonical certificate registration is changed;
the registered canonical certificate suite is therefore not claimed as a
new independent mathematical audit. The saved JSONL is finite evidence only.

## 8. Exact next theorem

Prove that there is D_0 such that every canonical triangle-free C-II source
with D>=D_0 admits an actual direction v and disjoint moving groups with
nonempty proper core parts, at least one fixed core label, no contact between
different moving groups, and a full-source assignment of its isolates, for
which the policy B inclusive floor closure retains a core group. Alternatively
policy A may suffice if its constructed endpoint opens a cut contact.

IFC makes either proposed family immediately checkable against all original
source pairs; LCR or CLR then supplies the finite full-source contradiction.
No theorem in this report extracts that family or proves its survival from
the terminal O--O owner-capacity and train-depletion statements. Consequently
neither C-II nor Erdős Problem #99 is settled.
