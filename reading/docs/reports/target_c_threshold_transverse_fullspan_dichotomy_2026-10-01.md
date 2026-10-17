> Generated reading edition · [exact source](../../../docs/reports/target_c_threshold_transverse_fullspan_dichotomy_2026-10-01.md) · source SHA-256 `da8c6715c0a7810364640100ce6c834d31bf5944fd241524629e04c2c4dc44dc`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-664608322863","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — threshold staircase transverse full-span dichotomy

**Phase 2 preservation provenance:** PR #603, branch swarm/sol/threshold-transverse-fullspan-20261001, audited source head caf0348fa4d05a3811a942c77bd837deccc1f339. Preserve as unreviewed conditional full-span/large-extreme-degree source fork; current main contains the hostile audit of the core host-coherence step, but the fork still needs a source-level competitor or triangle.

Date: 2026-10-01
Repository commit: 78a65968d51af7871a0ce5a865bf2db1a2c2e0ec
State version: 2026-09-14.audit.51
Run type: closing-proof research packet
Target: C-II, fixed-star threshold exact-phase branch
Starting status: canonical C-II frontier open; October 1 threshold staircase inputs are proof-only and unpromoted
Active prompt: docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md, plus the October 1 full-settlement swarm instruction
External literature search: not used in the proof
Computation: not used

## LEVEL I STATUS

STILL OPEN.

C-I remains closed and C-II remains open. This report does not promote the October 1
threshold extraction or claim a Level I solution.

## 1. Starting endpoint and implication chain

The current canonical Target C frontier is still the audit.51 C-II split in
docs/targets/target-c/CURRENT.md. On current main, the later proof-only fixed-star
threshold branch has been sharpened as follows.

1. target_c_exact_phase_threshold_paired_staircase_2026-10-01.md gives a paired
   antitone gap tree on one exact-phase shore, with two physical diameter
   representatives over every simple gap edge and one parallel full-support diameter.
2. target_c_exact_phase_threshold_forest_lift_2026-10-01.md lifts those selected
   rows to a physical diameter forest and obtains

       sum from j=0 to m of (n_j - 1) = m + c(F).

The missing bridge named by the latter report is coupling those physical fibers to the
opposite complete O--O shore.

The chain attacked here is:

    threshold paired staircase + complete transverse O--O grid
      -> opposite-shore full-span diameter load OR large extreme quotient degree
      -> source-level diameter-budget / endpoint-fiber obstruction
      -> strict competitor or exact unit triangle.

This report proves the first two arrows through the source-level fork. The final
competitor/triangle implication remains open.

## 2. Setup

Let A = {a_1,...,a_m} and B = {b_1,...,b_n} be the retained complete
outer-to-outer rectangle from the October 1 fixed-star extraction. Trains in each
shore are pairwise disjoint proper crosscuts and every a_i crosses every b_j
exactly once.

Assume the A shore is exact phase and lies in a threshold witness cell. Use the
notation of target_c_exact_phase_threshold_paired_staircase_2026-10-01.md:

- the A-gap vertices are 0,1,...,m;
- T is the collapsed simple paired-staircase gap tree;
- h_0 = za is the actual diameter parallel to the common A-train direction and
  crossing every retained A cut;
- the two boundary arcs from z to a are L and U;
- for every simple tree edge {p,q}, p < q, the selected physical representatives
  are L_p U_q and L_q U_p.

Let F be the physical graph consisting of these 2m paired representatives and h_0,
as in target_c_exact_phase_threshold_forest_lift_2026-10-01.md. Let c(F) be its
number of nontrivial components and let n_j be the number of distinct physical
vertices of F in A-layer j.

For the complete grid, use the four boundary host intervals from
target_c_complete_grid_joint_switch_budget_2026-10-01_r2.md, in cyclic order

    I_A^+, I_B^+, I_A^-, I_B^-.

Every A-crosscut joins I_A^+ to I_A^-, and every B-crosscut joins I_B^+ to
I_B^-. After the standard endpoint resolution away from source vertices, the
A-layer function is constant at its two extreme values on I_B^+ union I_B^-,
and the B-layer function is constant at its two extreme values on
I_A^+ union I_A^-.

All statements below are conditional on the named October 1 proof-only inputs.
No unpromoted statement is silently promoted.

## 3. Interior host coherence

### Lemma 3.1 — the two threshold arcs occupy opposite A-hosts in every interior layer

After possibly swapping I_A^+ and I_A^-, every source-hull point of L whose
A-layer lies in {1,...,m-1} lies in I_A^+, while every source-hull point of U
whose A-layer lies in {1,...,m-1} lies in I_A^-.

### Proof

The threshold staircase report proves that, on each of the two arcs L and U, the
A-layer is nondecreasing from layer 0 at one endpoint of h_0 to layer m at the
other.

By the four-host decomposition, every point of I_B^+ union I_B^- has an extreme
A-layer: one B-host has layer 0, the other layer m. Therefore an arc whose layer
is monotone from 0 to m cannot leave one A-host interval, pass through a B-host
interval, and later enter the other A-host while carrying an interior layer.
A passage through a B-host can occur only on the initial layer-0 plateau or the
terminal layer-m plateau.

Hence all interior-layer portions of one fixed threshold arc lie in one A-host
interval. The two arcs cannot use the same A-host for their interior portions:
every A-crosscut has one terminal on I_A^+ and one on I_A^-, while h_0 crosses
every A-crosscut, so each of L and U contains exactly one of those two terminals.
Thus the two interior host choices are opposite. QED.

This is the topological information absent from a one-shore gap graph.

## 4. The forest split count has a mandatory two-sided baseline

### Theorem 4.1 — side-resolved fiber identity

For every interior layer 1 <= j <= m-1,

    n_j >= 2.                                             (4.1)

Moreover,

    (n_0 - 1) + (n_m - 1)
      + sum from j=1 to m-1 of (n_j - 2)
      = c(F) + 1.                                         (4.2)

### Proof

The tree T spans all m+1 gap vertices, so every interior gap vertex j is incident
to at least one tree edge. For an edge incident to j, the paired representatives
put one selected diameter endpoint in the L-fiber of layer j and one in the
U-fiber of layer j. For an interior layer the arcs L and U are disjoint, so these
are distinct physical source vertices. This proves (4.1).

The forest-lift theorem on current main gives exactly

    sum from j=0 to m of (n_j - 1) = m + c(F).            (4.3)

Subtract the mandatory contribution m-1 supplied by (4.1) over the interior
layers. The result is (4.2). QED.

### Consequence

The linear quantity m+c(F) in (4.3) should not be interpreted as m+c(F)
independent units of new boundary defect. At least m-1 of it is already forced
by the two physical hull-arc orientations in the paired staircase. The genuinely
additional split excess beyond one L-fiber and one U-fiber per interior layer is
exactly c(F)+1.

This does not invalidate the current-main forest-lift theorem. It removes a
stronger inference that the raw split sum by itself supplies a new linear
transverse defect.

## 5. Interior staircase edges become full-span on the opposite shore

Let E_int(T) be the tree edges {p,q} with 1 <= p < q <= m-1, and let

    e_int = |E_int(T)|.

### Theorem 5.1 — transverse full-span lift

Every edge of E_int(T) supplies two distinct actual diameter edges whose signed
B-support is full. Consequently,

    N_full^B >= 2 e_int,                                  (5.1)

where N_full^B is the number of distinct actual diameter edges crossing all
selected B-cuts.

### Proof

Take {p,q} in E_int(T), with p < q. Its paired physical diameter
representatives are

    L_p U_q  and  L_q U_p.                                (5.2)

All four layer labels are interior. By Lemma 3.1, the L-endpoint of either
representative lies on one A-host interval and its U-endpoint lies on the other
A-host interval.

The four-host theorem says that the B-layer is constant at opposite extreme values
on I_A^+ and I_A^-. Hence each diameter in (5.2) has one endpoint in B-layer 0
and the other in B-layer n. Exact laminar support on the B-shore therefore makes
its signed incidence nonzero on every selected B-cut.

The threshold paired-staircase theorem already proves that the two representatives
over one simple edge are distinct and that the chosen representatives over
distinct simple edges are distinct actual diameter bars. Summing over the
e_int interior edges proves (5.1). QED.

Thus the mandatory two-sided physical splitting from Theorem 4.1 is not merely
bookkeeping: whenever both endpoint layers of a staircase edge are interior, the
two physical copies become genuine full-span constraints on the transverse train
shore.

## 6. Exact tree degree formula

Write

    d_0 = deg_T(0),   d_m = deg_T(m).

### Lemma 6.1

The paired staircase contains the edge {0,m}, and therefore

    e_int = m - d_0 - d_m + 1.                            (6.1)

### Proof

The equality case proved in the paired-staircase report writes the distinct left
endpoints as a_i = i-1 and

    B_i = {t_i, t_i+1, ..., t_(i-1)},   with t_0 = m.

For the first left endpoint a_1=0, the set B_1 therefore contains m. Hence
{0,m} is an edge of T.

The tree has m edges. The number of edges incident to at least one of {0,m} is
d_0+d_m-1, because {0,m} is counted twice in the degree sum. Removing those
edges leaves precisely E_int(T), proving (6.1). QED.

Combining (5.1) and (6.1),

    N_full^B >= 2(m - d_0 - d_m + 1).                    (6.2)

## 7. Coupling to the opposite-shore rank requirement

Let h be the total number of actual diameter edges in the source, and let
N_prop^B be the number with nonempty proper support on the selected B-shore.

The October 1 rank-switching report proves

    N_prop^B >= n - 2                                    (7.1)

for an arbitrary retained B-shore, because the opposite complete shore supplies
an unselected complete train. If the B-shore is also exact phase, that report
improves this to

    N_prop^B >= n - 1.                                   (7.2)

A full-support B-diameter cannot be a proper-support B-diameter. Therefore
Theorem 5.1 yields the source-level edge budget

    h >= 2(m - d_0 - d_m + 1) + (n - 2).                (7.3)

If B is exact phase,

    h >= 2(m - d_0 - d_m + 1) + (n - 1).                (7.4)

No KKT multiplier lower bound is used.

## 8. Quantitative fork: transverse full span or extreme quotient concentration

For any 0 < eta < 1, either

    e_int >= eta m,

in which case

    N_full^B >= 2 eta m,                                 (8.1)

or

    e_int < eta m,

in which case (6.1) gives

    d_0 + d_m > (1-eta)m + 1

and hence

    max(d_0,d_m) > ((1-eta)m + 1)/2.                     (8.2)

At eta=1/2, every threshold staircase satisfies the explicit fork

    N_full^B >= m
    OR
    max(d_0,d_m) > m/4 + 1/2.                            (8.3)

The second branch is a quotient statement, so physical fiber splitting must still
be retained. If j is 0 or m and Delta(H) denotes the maximum degree of the complete
actual diameter graph, the d_j incident simple tree edges supply 2d_j distinct
paired diameter incidences in layer j. Therefore

    n_j Delta(H) >= 2 d_j.                               (8.4)

Thus the large-extreme-degree side of (8.3) is already a source-level alternative:

    n_j Delta(H) > m/2 + 1                               (8.5)

for some j in {0,m}.

No assumption that one quotient layer is one physical source vertex is made.

## 9. Adversarial checks

### 9.1 Star staircase

A staircase tree can concentrate most or all simple edges at an extreme gap vertex.
Then e_int can be zero. Theorem 5.1 deliberately does not claim a linear
opposite-shore full-span family in that case. The obstruction is transferred to
(8.4)-(8.5), where physical endpoint multiplicity and actual diameter degree remain
visible.

This is why replacing quotient levels by physical vertices would be invalid.

### 9.2 Path-like staircase

When many tree edges have both endpoints interior, Theorem 5.1 forces the expected
large transverse full-span family. No disjointness of their source endpoints is
assumed; only the actual diameter edges themselves are distinct.

### 9.3 Boundary host ambiguity

The proof does not assume that the whole arc L lies in one A-host interval. Only
interior layers are used. The B-host intervals have extreme A-layer labels, so the
monotone threshold arc cannot switch A-hosts while carrying an interior label.
This is why endpoints in layers 0 and m are excluded from Theorem 5.1.

### 9.4 Raw fiber-count overinterpretation

Equation (4.2) is an exact check against treating

    sum_j(n_j-1) = m+c(F)

as wholly new defect. The current-main equality is correct; the new decomposition
shows which part is automatic.

### 9.5 Scope

No contact-isolated source point is deleted. No inactive pair is promoted to active.
No infinitesimal motion is integrated. No local or jammed source is identified with
a global minimizer. No Euler-trail inference is used.

## 10. Frontier effect

Classification: proved candidate awaiting independent audit, conditional on the
unpromoted October 1 threshold-staircase and complete-grid inputs.

The threshold exact-phase branch is sharpened from

    paired tree + linear raw fiber split

to the exact source-level fork

    linear family of actual diameter bars full-span on the opposite shore

or

    linear extreme quotient degree paid by physical fiber multiplicity and/or
    actual diameter-star degree.

In the first branch, the opposite shore simultaneously requires n-2 distinct
proper-support diameter rows, giving (7.3). In the second branch, (8.4) prevents
collapsing the quotient star to one physical endpoint for free.

No canonical branch is eliminated. Split-star O--O, open-cell exact phase,
nonconstant phase, inactive-interface, macroscopic-container/exterior-cap, and
other full-core branches remain open.

## 11. Exact remaining lemma

The next threshold theorem should use the actual strict-rhombus contact grid to
eliminate one of the two alternatives below for m,n = Omega(D):

1. N_full^B = Omega(D) actual diameter edges cross every selected B-train while
   at least n-2 = Omega(D) further actual diameter edges have proper B-support; or
2. one extreme A-layer satisfies

       n_j Delta(H) = Omega(D)

   through paired staircase incidences.

A valid closure must turn that physical source fork into an exact unit triangle or
a finite same-cardinality strict sub-D competitor. Convex-thrackle geometry or
quotient rank alone is insufficient; the already-known geometry-only shell
regressions warn against that shortcut.

## 12. Claim audit table

| Claim | Status | Dependencies | Reason |
| --- | --- | --- | --- |
| Interior threshold fibers lie on opposite A-hosts | unreviewed proved candidate | complete-grid four-host topology; threshold monotone arcs | direct boundary-order proof |
| n_j >= 2 for 1 <= j <= m-1 | unreviewed proved candidate | paired physical representatives | L/U endpoints are distinct in interior layers |
| residual split identity (4.2) | unreviewed proved candidate | current-main forest-lift identity | exact algebra |
| interior tree edge gives two B-full-span actual diameters | unreviewed proved candidate | four-host topology + exact laminar support | endpoints lie in opposite B-extreme layers |
| e_int = m-d_0-d_m+1 | unreviewed proved candidate | exact staircase equality case | {0,m} is forced |
| edge budget (7.3)-(7.4) | conditional proved candidate | preceding claims + rank-switching report | full and proper support classes are disjoint |
| raw split count is a new linear defect beyond paired sides | rejected inference | (4.2) | m-1 units are mandatory two-sided baseline |
| C-II / Level I closure | open | all global branches | source-level fork not yet eliminated |

## 13. Regression and correction checks

| Regression/correction | Result | Exact hypothesis or failure |
| --- | --- | --- |
| incident-diameter sequence implies Euler trail/path | not used | forbidden repository inference |
| quotient level implies one physical source vertex | rejected | fiber multiplicity retained in n_j |
| geometry/stress-only gap closure | not used | actual transverse contact grid remains the missing source coupling |
| contact-isolated point deletion | not used | all source points retained |
| current-main forest-lift theorem | survives | refined, not contradicted, by (4.2) |

## 14. Literature and computation

No external theorem is imported and no computation is load-bearing. The result is
finite boundary topology plus exact support bookkeeping.

## 15. Promotion recommendation

Unreviewed.

The theorem should not be promoted before an independent audit of:

1. Lemma 3.1 against the precise endpoint-resolution convention of the complete
   O--O grid;
2. the use of the paired physical representatives in interior layers;
3. the opposite-shore full-support conclusion;
4. the exact staircase equality implication {0,m} in E(T).

Because all route applications depend on unpromoted October 1 reports, promotion of
this report alone would be premature.

## 16. Handoff

1. Strongest new theorem: every interior staircase edge lifts to two actual
   diameter bars full-span across the opposite complete O--O shore; otherwise the
   staircase must concentrate linearly at an extreme quotient layer.
2. Dependency chain: canonical audit.51 normal form -> proof-only complete O--O
   rectangle/four-host topology -> proof-only exact-phase rank -> proof-only
   threshold paired staircase -> proof-only threshold forest lift -> this report.
3. Exact remaining lemma: eliminate the two alternatives in Section 11 using the
   actual strict-rhombus contact grid and source minimality.
4. Binding dead route: raw gap rank, convex-thrackle geometry, or raw fiber count
   without the transverse unit-contact embedding cannot by themselves close the
   branch.
5. Read next: the two October threshold reports, the complete-grid joint switch
   budget, the rank-switching report, and any independent audit of this packet.
