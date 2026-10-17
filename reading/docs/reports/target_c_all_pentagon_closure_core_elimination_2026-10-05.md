> Generated reading edition · [exact source](../../../docs/reports/target_c_all_pentagon_closure_core_elimination_2026-10-05.md) · source SHA-256 `3bcffcf76cdd806bd6acd53f648c24619e837a099545ea7166f2c90a91664c43`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-CB8DFEB9D5D9","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — eliminate every pentagon closure core and charge pure corank to higher faces

**Date:** 2026-10-05. **Starting main:** f539af073a691c13327a0a7fef3c746fb7704e5f.
**Run checkpoint:** 93e43e11. **State:** 2026-09-14.audit.51.
**Classification:** proved candidate awaiting independent audit; unreviewed,
noncanonical. **LEVEL I STATUS: STILL OPEN.**

## 1. Exact changed expression

For the canonical triangle-free C-II source, let $f_5$ be the number
of bounded physical pentagonal contact faces and $f_6$ the number of
bounded physical faces of degree at least six. Write $f=f_5+f_6$,
$Q=\sum_F(\deg F-4)$, and

$$
\sigma_C:=\dim\ker R_C^T
=\dim\ker C_{\rm face}^T.
$$

**Theorem P.1.** Restriction to the degree-at-least-six face blocks is
injective on $\ker C_{\rm face}^T$. Consequently

$$
\boxed{\sigma_C\le2f_6\le2(Q-f).}
\tag{P.1}
$$

If $Q-f=o(D)$, then $\sigma_C=o(D)$, with no phase, residual,
degree-tail or terminality hypothesis. If all exceptional faces are
pentagons, then $\sigma_C=0$ exactly and two-anchor elimination
reaches every physical exceptional face. There is no pentagon-only
stalled core of any size.

The implication chain is

$$
\text{internal angular-column independence}
\ \Longrightarrow\ \text{every induced pentagon set has a node of degree at most three}
\ \Longrightarrow\ \text{two nonparallel external pivots}
\ \Longrightarrow\ \text{global pentagon elimination and (P.1)}.
$$

The $s_C$ in the full-core surplus $e_{BB}+2s_C-3k$ is the
**extra pinned-contact** left-nullity of unloaded components. It is not
$\sigma_C$. Equation (P.1) must not be substituted for a bound on
$s_C$; the existing scalar survivor remains live.

## 2. Source class, dependencies and all source points

Use the actual contact-minimal, then diameter-pair-minimal C-II source
in the Section-57 regime, with $C=C_*$ and $H=H_*$. The positive
contact core is connected and contains every diameter endpoint. All
contact isolates remain in the full source.

Canonical inputs are
[Section 57](../targets/target-c/57-zr-zf-rigidity-audit.md),
[Section 67](../targets/target-c/67-rhombus-population-transport-audit.md),
and the complete stopped-train decomposition. The new finite input is
[AR.2](target_c_augmented_train_phase_rank_small_residual_exclusion_2026-10-05.md):
internal train angular columns, with every hull pocket retained, are
independent. Its proof uses mixed rigidity with every loaded hull
velocity fixed; it is an unreviewed candidate, not a promoted premise.
The stronger reciprocal $(2,3)$ bound is available from
[R.6](target_c_positive_reciprocal_internal_train_graph_2026-10-05.md),
but the argument below already follows from AR.2's $(2,2)$ bound.

The original face closure matrix has one two-coordinate row block per
bounded physical exceptional face. Pockets are not rows of this original
matrix: a former outer endpoint remains the zero ground block in its
transpose equations. They were essential auxiliary rows for proving
AR.2, and are not silently discarded from that proof.

## 3. Every physical pentagon is strictly convex and has no parallel sides

Section 67 gives convexity. If a unit pentagon has a flat corner, place
that corner at $0$ and its adjacent vertices at $(-1,0),(1,0)$.
The [flat-pentagon converse](target_c_loaded_flat_pentagon_second_depletion_2026-10-05.md)
uses only unit separation and wall lengths: its remaining vertices are
$(1/2,\pm\sqrt3/2),(-1/2,\pm\sqrt3/2)$ with a common sign. The
flat corner and either adjacent pair then form an exact unit triangle.
Thus a triangle-free physical pentagon cannot have a flat corner.

For completeness, suppose two sides of a strictly convex unit pentagon
are projectively parallel. Same-oriented parallel sides are impossible
in a strictly convex polygon, so their unit vectors are opposite. The
other three unit vectors sum to zero and are spaced by $2\pi/3$.
The two opposite extra directions occupy at most two of the three gaps
between them. One pair of the three directions is therefore consecutive
in the cyclic edge order with turn $2\pi/3$, giving an interior angle
$\pi/3$. Its adjacent wall vertices are at unit distance, creating an
exact triangle. Contradiction.

This is the personally checked
[older no-parallel-side proof](../../research/target_c_bounded_pentagon_no_parallel_sides_2026-09-18.md),
with its strict-convexity premise now explicitly discharged. Determinants
may tend to zero along a sequence; the statement is finite and exact.

## 4. Every pentagon subset has two external pivot trains

Take any nonempty set $U$ of physical pentagon endpoint nodes.
AR.2 gives

$$
e(U)\le2|U|-2.
$$

There are no internal loops, and terminal occurrences are counted.
Thus the average internal degree is less than four. Some face $F\in U$
has internal degree at most three. Its physical valence is five, so at
least two of its train ends go to the actual outer face or to an
exceptional face outside $U$. The two trains are distinct and their
terminal directions at $F$ are nonparallel by Section 3.

Repeatedly remove such an $F$. This gives a complete two-anchor order
for all pentagons, starting with the higher-degree faces and the outer
ground block as fixed blocks. No small-support, generic-position,
bounded-face-degree or uniform-angle assumption enters the order.

## 5. Eliminate every pentagon-supported dual mode

For $y\in\ker C_{\rm face}^T$, an internal train $FG$ gives

$$
(y_F-y_G)\cdot Jw=0,
$$

and an outer-ended train at $F$ gives $y_F\cdot Jw=0$.
Suppose $y$ vanishes on all higher-degree faces. At the first pentagon
in the order above, the two external blocks are zero. Its two nonparallel
train equations force $y_F=0$. Induct in that order. Every pentagon
block is zero, and therefore $y=0$. Restriction to the $2f_6$
higher-face coordinates is injective, proving (P.1).

Equivalently, select two pivot train columns at each removed pentagon.
A train cannot be selected twice: when its earlier endpoint entered,
its later endpoint was still in the inactive set. The pentagon-row/pivot
submatrix is block upper triangular with invertible $2\times2$
diagonal blocks. Hence its rank is exactly $2f_5$.

The equality between pure-contact and face corank can also be checked
directly. For core vertex/edge counts $v,e$, rhombus count $R$,
train count $T=e-2R$, and Euler identity $e-v=R+f-1$, train-angle
integration gives $\dim\ker R_C=\dim\ker C_{\rm face}+2$. Therefore

$$
e-\operatorname{rank}R_C
=e-2v+T-\operatorname{rank}C_{\rm face}+2
=2f-\operatorname{rank}C_{\rm face}.
$$

This is the exact identity of the audited-working
[Section 156](../targets/target-c/156-157-face-closure-and-outer-train-bracing-audited.md).
No statement about isolated coordinates is needed for it.

## 6. Finite contact chart in the all-pentagon case

If $f_6=0$, the exact face closure map in train angles is

$$
\Psi_F(\theta)=\sum_{e\in\partial F}
\operatorname{Rot}(\theta_{\tau(e)})w_e.
$$

The selected pivot Jacobian at the source is the invertible matrix from
Section 5. The implicit function theorem supplies a local exact chart
of dimension $T-2f=q-k$, including common rotation. Integrated edge
vectors preserve every actual unit contact, selected or unselected;
original rhombi remain rhombi in a sufficiently small neighborhood.

Every original contact isolate is kept at its original coordinate.
The finite positive slack on all other lower constraints persists after
shrinking the chart neighborhood. Cardinality is unchanged. Inactive
upper constraints also retain their finite strict slack, but every
**active** diameter constraint still has to be checked separately.
Neither a uniform chart radius nor diameter descent is established.

The earlier
[two-anchor integration candidate](../../research/target_c_free_terminal_two_anchor_elimination_2026-09-18.md)
gave this chart conditionally on elimination reaching all faces.
The new result discharges that condition for every all-pentagon canonical
source, not merely a terminal low-$t$ endpoint. It eliminates the
entire pentagon-only stalled-core alternative and its arbitrarily large
one-anchor closure modes. It does not reopen the superseded numerical
terminal windows.

## 7. Exact finite checks and unresolved source obligation

[The verifier](../../../research/verify_target_c_pentagon_closure_core_elimination_2026_10_05.py)
checks 224 pair constraints in eight unit-separated quadratic-field
packets made from two pentagons glued along one side. The two nonboundary
vertices have exact positive contact equilibrium; all hidden diagonals
are strict. The four face rows are independent, all nine contact rows
are independent and the four pinned interior coordinates have full
contact rank. Their hull pins are not certified diameter loads.

It also checks 26,411 abstract $(2,3)$-sparse endpoint graphs on up to
six nodes and 79,233 complete two-anchor orders. These graphs are
incidence ledgers, not source embeddings. Matrix and graph checks do
not certify the analytic implicit-function theorem or a uniform radius.

The all-pentagon full-core branch can no longer use a pure-contact
closure corank or a stalled pentagon core as an escape. Its remaining
obligation is still a finite same-cardinality feasible competitor or
an exact triangle theorem. The active diameter cage, near-active lower
constraints, positive residual and pinned-contact surplus remain.
