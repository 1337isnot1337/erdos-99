<!-- theorem-state: {"artifact_id":"ART-5DAE8768F2A0","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — threshold boundary fan forces physical side-fiber rank

**Phase 2 preservation provenance:** PR #603, branch swarm/sol/threshold-transverse-fullspan-20261001, audited source head caf0348fa4d05a3811a942c77bd837deccc1f339. Preserve as unreviewed threshold fan/rank candidate. Current main contains its hostile audit, which passes host coherence at the exact conditional scope; neither report promotes the October 1 route or closes C-II.

Date: 2026-10-01
Starting commit: 78a65968d51af7871a0ce5a865bf2db1a2c2e0ec
Branch: swarm/sol/threshold-transverse-fullspan-20261001
State version: 2026-09-14.audit.51
Run type: exact rank / physical-fiber refinement
Target: C-II fixed-star threshold exact-phase branch
Status: unreviewed proved candidate conditional on the October 1 proof-only extraction
Computation: not used
External literature: not used

LEVEL I STATUS: STILL OPEN.

This report continues
target_c_threshold_transverse_fullspan_dichotomy_2026-10-01.md.
It does not use any active-PR theorem as a premise.

The candidate chain is

    one-sided threshold boundary fan
      -> few physical extreme side-fibers imply few transverse interval classes
      -> transverse mixed-rigidity rank forces many physical extreme side-fibers
      -> genuine side-fiber split lower bound
      -> combine with loaded-endpoint capacity
      -> exact exclusion criterion.

The resulting criterion is not yet strong enough at the present extraction constant,
so C-II remains open.

## 1. Inputs

Use one retained threshold exact-phase shore

    A = {a_1,...,a_m}

of the complete O--O rectangle, together with the paired staircase tree T on gap
vertices 0,...,m.

For each simple tree edge {p,q}, p<q, retain the two distinct actual diameter
representatives

    L_p U_q  and  L_q U_p.

Let H_pair be the resulting 2m-edge physical diameter graph. Let h0=za be the
parallel threshold diameter, so H_pair union {h0} contains 2m+1 distinct actual
diameter edges.

Retain the transverse complete O--O shore

    B = {b_1,...,b_n}

and let M_B be its actual-diameter shear matrix. Current main proves

    rank(M_B)=n.                                          (1.1)

Every diameter row has signed consecutive-interval support on B. Rows with full
support span a space of dimension at most two. If B is exact phase, every selected
B train has one common oriented unit direction and every fixed support interval
class has dimension at most one.

The preceding report proves the following host-coherence statement, conditional on
the same October 1 complete-grid and threshold inputs:

    every interior point of L lies on one A-host interval,
    every interior point of U lies on the opposite A-host interval.

Consequently every paired representative over an internal staircase edge is
full-span on B.

## 2. One-sided boundary fan

The equality classification of the paired staircase contains the full edge {0,m}.
Call a remaining tree edge internal when both endpoints lie in {1,...,m-1}.
Call a remaining edge boundary-touching when exactly one endpoint lies in {0,m}.

### Lemma 2.1 — all proper boundary edges lie at one extreme

There cannot be both an edge {0,b} with b<m and an edge {a,m} with a>0.

Proof.

Write the two edges in increasing-left-endpoint order. Antitonicity of the
staircase says that increasing the left endpoint cannot increase the right endpoint.
Thus 0<a would force b>=m, contrary to b<m. QED.

Hence all proper boundary-touching tree edges form a one-sided fan at one extreme
layer j_* in {0,m}.

Let

    e_int = number of internal simple tree edges,
    f     = number of proper boundary-fan edges.

Since T is a tree with m edges and {0,m} is one additional edge,

    e_int + f = m-1.                                     (2.1)

## 3. Side-labelled physical fibers

For X in {L,U} and j in {0,...,m}, let n_(X,j) be the number of distinct
physical H_pair vertices lying on arc X in A-layer j.

Every layer is incident to a tree edge, and the paired representatives supply an
endpoint on both L and U. Therefore

    n_(L,j)>=1,  n_(U,j)>=1.                              (3.1)

Define the genuine side-fiber split excess

    S = sum over X,j of (n_(X,j)-1).                      (3.2)

Let o be the number of literal threshold endpoints z,a that are counted in both
corresponding side fibres. Since L and U meet only at z,a,

    |V(H_pair)| = 2(m+1)+S-o,   with 0<=o<=2.            (3.3)

Every H_pair vertex is an actual diameter endpoint, so it is one of the q loaded
diameter vertices. Therefore

    2(m+1)+S-o <= q,

and hence the coarse exact capacity bound

    S <= q-2m.                                            (3.4)

No forest component count is needed for (3.4).

Now focus on the boundary-fan extreme j_*. Put

    g_* = n_(L,j_*) + n_(U,j_*).                          (3.5)

The contribution of this one extreme layer to S is exactly g_*-2, so

    S >= g_*-2.                                           (3.6)

The point of the next section is to lower-bound g_* from the rank of M_B.

## 4. Fan rows are indexed by physical extreme side-fibers

Assume for notation that j_*=0. The j_*=m case is symmetric.

A proper fan edge has the form {0,b}, 1<=b<m, with paired representatives

    L_0 U_b  and  L_b U_0.                                (4.1)

The endpoints U_b and L_b are in interior A-layers. By host coherence they lie on
the two A-host intervals, where the B-layer is constant at its two extreme values
0 and n.

Consider one physical side-labelled extreme endpoint x occurring as L_0. Every
fan row using that same occurrence x has its other endpoint on the same opposite
A-host and therefore in the same extreme B-layer. The B-support interval of every
such row is determined solely by the B-layer of x: it is the same suffix interval,
possibly empty or full.

Similarly, every physical side-labelled occurrence y as U_0 determines one common
prefix interval for all fan rows using y.

Thus the fan rows split into at most g_* fixed B-support interval classes.

### Lemma 4.1 — fixed interval rank

For one fixed nonempty B-support interval I, all diameter rows having exactly I as
their signed support span a space of dimension at most two.

If B is exact phase, they span a space of dimension at most one.

Proof.

For a row h with diameter vector r_h, its entries on I are

    M_(h,i) = sigma_h (r_h dot J u_i),

and zero outside I. As r_h varies in R^2, these rows lie in the span of the two
coordinate sequences of J u_i restricted to I. This gives dimension at most two.

If all oriented u_i are equal, the coordinate sequence is constant up to one scalar
r_h dot J u, so the interval class is one-dimensional. QED.

Therefore the complete selected fan contributes rank at most

    2 g_*                                                 (4.2)

on an arbitrary B shore, and at most

    g_*                                                   (4.3)

when B is exact phase.

Empty-support fan rows contribute zero; full-support fan rows only make these upper
bounds looser.

## 5. Partition every actual diameter row

Partition the full actual diameter edge set into four groups.

1. Internal paired rows: 2 e_int selected rows. By the transverse full-span theorem,
   all are B-full-span. Their combined row rank is at most two, or at most one if
   B is exact phase.

2. Boundary-fan paired rows: 2f selected rows. By Section 4 their combined row rank
   is at most 2g_*, or g_* if B is exact phase.

3. The two paired representatives over the full simple edge {0,m}, together with
   h0. These three rows contribute rank at most three.

4. Every other actual diameter edge. Since the selected system
   H_pair union {h0} contains 2m+1 distinct actual diameter edges, this group has
   exactly h-(2m+1) edges and contributes rank at most h-(2m+1).

Using rank(M_B)=n gives the following finite inequalities.

### Theorem 5.1 — transverse rank forces physical extreme fibers

For an arbitrary transverse B shore,

    n <= 2 + 2g_* + 3 + h-(2m+1)
      = h-2m+4+2g_*,

so

    g_* >= (2m+n-h-4)/2.                                 (5.1)

If B is exact phase,

    n <= 1 + g_* + 3 + h-(2m+1)
      = h-2m+3+g_*,

so

    g_* >= 2m+n-h-3.                                     (5.2)

These are physical endpoint bounds. They do not identify an unsigned quotient layer
with one source vertex.

## 6. Genuine split lower bounds and exclusion criteria

Combine (3.6) with Theorem 5.1.

For arbitrary B,

    S >= (2m+n-h-8)/2.                                   (6.1)

If B is exact phase,

    S >= 2m+n-h-5.                                       (6.2)

Combine these with the loaded-endpoint upper bound S<=q-2m.

### Corollary 6.1 — finite fan feasibility inequalities

Every surviving boundary-fan branch must satisfy

    6m+n <= h+2q+8                                       (6.3)

for an arbitrary transverse shore.

If the transverse shore is exact phase, it must satisfy

    4m+n <= h+q+5.                                       (6.4)

Since the complete convex diameter graph has h<=q, the weaker source-only forms are

    6m+n <= 3q+8,                                        (6.5)

and, for exact B,

    4m+n <= 2q+5.                                        (6.6)

Therefore any future extraction violating the corresponding inequality eliminates
the one-sided threshold boundary-fan mechanism without requiring a KKT weight floor.

At the present fixed-star rectangle constant these inequalities are not yet
contradictory. They are a source-level transfer from transverse rank to genuine
physical side splitting, not a C-II closure.

## 7. Why this is stronger than raw fan-edge counting

A linear one-sided quotient fan does not by itself force linearly many physical
source endpoints: many tree edges may reuse one physical extreme endpoint.

The rank argument above charges reuse correctly.

If many fan bars share one physical side-labelled extreme endpoint, all of their
B rows have one common prefix or suffix support interval. Such a whole family costs
at most two rank dimensions, or one in exact phase, regardless of how many quotient
tree edges it represents.

Thus transverse mixed rigidity detects physical endpoint multiplicity rather than
only quotient fan size.

This is exactly the type of correction required after observing that the raw
unsigned forest-lift split sum has a mandatory doubled-arc baseline.

## 8. Adversarial audit

1. Same physical point on both L and U.
   The proof counts side-labelled occurrences. A literal endpoint z or a may belong
   to both fibres and can therefore contribute two interval classes. This is safe:
   g_* is deliberately side-labelled, and S uses the same convention before the
   overlap correction in (3.3).

2. Empty/full fan rows.
   They only reduce actual fan rank. Lemma 4.1 is an upper bound and remains valid.

3. Internal rows.
   The theorem uses the preceding transverse full-span result. If hostile audit
   downgrades that result to only t_B=0, the internal group can still have empty or
   full support; its rank is still at most two (one exact), so Theorem 5.1 survives.
   Thus the new rank/fiber inequality needs only nonswitching on B, not the stronger
   full-span conclusion.

4. Full edge and h0.
   No support pattern is assumed. They are paid individually by the additive rank
   allowance three.

5. Unselected diameter rows.
   Every such row is paid individually. No hidden assumption says the selected
   staircase exhausts the diameter graph.

6. Contact-isolated source points.
   None are deleted. The argument only counts loaded actual diameter endpoints.

7. Pure-tooth train coordinates.
   Not used. The exact displacement reconstruction from proof-only Section 159
   requires the pure-tooth train-angle isomorphism and does not automatically extend
   to the present rectangle.

8. KKT weights.
   No multiplier lower bound or stress-mass statement is used.

## 9. Frontier effect

Classification: unreviewed proved candidate, conditional on the October 1
complete-grid / paired-staircase / threshold extraction.

New information:

    boundary fan
      -> repeated physical extreme endpoint
      -> repeated transverse prefix/suffix interval
      -> at most two rank dimensions per side-fiber
      -> full transverse rank forces many physical extreme side-fibers
      -> genuine split lower bound (6.1)/(6.2).

This is the first direct use of the opposite-shore rank theorem to force the
physical side-fiber currency that the threshold forest lift by itself did not force.

It still does not eliminate the current extraction constants.

## 10. Exact remaining attack

The surviving threshold mechanisms are now separated cleanly.

A. Internal-rich staircase:
   many paired rows are nonswitching on the transverse shore, and under host
   coherence are actually transverse full-span.

B. Boundary-fan-rich staircase:
   transverse rank forces many physical extreme side-fibers through (5.1)/(5.2),
   but the present loaded-endpoint capacity still permits them.

The next source-specific theorem should improve one of the two capacities:

1. prove that distinct physical extreme fan endpoints must occupy substantially
   separated transverse B-layers, then use unit-rhombus path bandwidth and exact
   diameter geometry to get a stronger star/fiber cap; or
2. show that a linear transverse full-span diameter family cannot coexist with the
   strict unit-rhombus complete grid and the required proper-support rank rows; or
3. integrate a source-preserving finite move that shortens the internal-rich family.

Any closure still must produce an exact unit triangle or a same-cardinality strict
sub-D competitor.

## 11. Handoff

Strongest new theorem:
transverse rank forces g_* >= (2m+n-h-4)/2 physical side-labelled extreme endpoints
in the general boundary-fan branch, improved to g_* >= 2m+n-h-3 when B is exact
phase.

Exact finite consequence:
the fan branch must satisfy 6m+n<=h+2q+8, improved to 4m+n<=h+q+5 for exact B.

Binding warning:
a linear quotient fan is not a linear physical star and raw unsigned layer splitting
is not genuine side-fiber splitting. The rank proof keeps those distinctions explicit.
