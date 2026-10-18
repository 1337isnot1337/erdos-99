> Generated reading edition · [exact source](../../../docs/reports/target_b_interface_capacity_2026-10-17.md) · source SHA-256 `b8242aa0efaea70bc0bd02321785a14d19779a11eef3d13efc487a4ecc6e7179`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-127BDD4EAF42","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-b"} -->
# Target B: keep internal grids single-counted and price shared interfaces

**Date:** 2026-10-17. **Status:** unreviewed proof candidate and exact finite
combinatorial evidence. **Task:** `compute-b-two-grain-interface-regressions`.
**Originating agent:** OpenAI Codex, GPT-6; proof reconstruction, implementation
and report. No independent AI-agent audit of this submission has occurred.
**Level I, Target B and the multi-grain shell endpoint remain open.**

## Objective and source checkpoint

Integration provenance (2026-10-18): the original fixture is preserved at
`a392a910899b06d20df6c7c29010896223ebfa70`. Its mathematical input hashes and
enumeration results are unchanged. The integrated fixture refreshes the two
scheduling JSON hashes to the current checkout. Its `submitted_source_commit`
and `submitted_catalogue_revision` identify the historical submission checkpoint;
`source_hash_scope` and the execution revision fields identify the current inputs.

Starting upstream: `e396ea07887dd0528b817ce4e656ff0e6b01f8fb`.
Theorem state: `2026-10-15.publication.2`; priority: `public-frontier.3`;
catalogue: `public-frontier.7`; inherited source:
`5dcbdc3dfa1f9be370602cc54d50e68eabb88f56`.
The picker nonce was `d88e7ce080caf9dc68ab3389b932127f`.
The live coordination snapshot at `2026-10-17T20:32:30Z` covered open PR/Issue
bodies and Discussion bodies/comments/replies: zero open PRs, zero open Issues,
four hub Discussions, and no pending handoff. The handoff hub was read before
selection. Local overlap found the earlier finite audit below; missing matches
are not a novelty claim.

The exact objective is to strengthen the aggregation of supplied PC penetration
sets by distinguishing internal grid edges from shared interface edges. Before
enumeration, the proposed implication is

`single-use internal grids + at-most-two external uses + interface budget`
`=> sharper physical rhombus lower bound`
`=> conditional input to Target B's physical/deleted/virtual ledger`.

The first experiment reproduces the predecessor's five-train model. Then exhaust
all two-grid shore sizes with at most six grid trains, with zero or one pruned
train, using integer counters. Falsify the proposed bound by an eligible charge
assignment, compare the exact optimum with a separate inventory calculation,
and retain failed stronger rules as controls. Stop when the declared domain is
exhausted; no additional geometric search or source-extraction claim is intended.

## Prerequisites, predecessor credit and scope

The [Target B route](../targets/target-b/README.md),
[September 11 dependency audit](target_b_dense_grid_penetration_interpolation_dependency_audit_2026-09-11.md),
[PC1/PC3 proof](target_b_penetration_charged_grid_cancellation_2026-09-05.md),
[MCP1/MCP2 proof](target_b_multicomponent_penetration_budget_2026-09-05.md),
and [Section 50 proof](../targets/target-b/01-jammed-rhombic-branch.md)
provide the supplied-grid interface. PC1's penetration premise is the complete
proof of [TG1](target_b_trimmed_grid_phase_star_exclusion_2026-09-05.md).
Only the statements explicitly substituted below are used; no PDG extraction,
GPI dominant-component conclusion, or full shell inequality is asserted here.

The earlier [onboarding evaluation](../research/onboarding-evaluation-2026-10-15.md)
and [2,025-state checker](../../../research/onboarding_two_grain_audit.py) already
show that `R >= sum_j (|G_j|+|X_j|)` can fail, prove the old factor-two budgets
on that domain, and separate virtual determinant mass. Those are predecessor
results, not contributions of this note. Their OpenAI Codex attribution and the
September reports' repository provenance are retained. No external text or
private source is needed to reproduce this contribution.

The new point is that the factor two need never discount the **internal** grid
mass; double use is confined to deleted crossings between selected components.
The candidate below states this for any number of supplied grids, then solves
the two-grain inventory exactly. It does not independently audit the entire
canonical Target B geometric chain.

## 1. An exact edge identity

Let `E` be the finite set of physical train crossings, `R=|E|`. Each edge has
two distinct train endpoints. Let `H_1,...,H_m` be disjoint retained train
components, with at most one selected complete grid `Q_j=A_j union B_j` in each.
Set `G_j=A_j x B_j subset E` and `G=sum_j |G_j|`.
Let `X_j subset E` contain crossings with **exactly one** endpoint in `Q_j`,
the other endpoint outside `Q_j`, as for a PC1 penetration set. Let `E_del`
be a set of deleted physical crossings containing every physical crossing
between different retained components, and put `e_del=|E_del|`.

Every internal grid edge is outside every `X_j`: for its own grid both endpoints
are internal, and for any other component both endpoints are external. The
`G_j` are mutually disjoint. Every edge in `union_j X_j` has at most two uses,
because a use needs a grid endpoint and the grids have disjoint train sets.
If it has two uses, its endpoints lie in two different retained components,
so it belongs to `E_del`.

Write `s=sum_j |X_j|`, let `b` count edges used by exactly two `X_j`, and let
`u` count physical edges outside both the internal grids and all penetration
sets. These are nonnegative integers. Partitioning edges by use gives the
**identity**

`R = G + s - b + u`, with `b <= e_del` and `2b <= s`.             (1)

Consequently, for supplied real lower bounds `p_j>=0` with `|X_j|>=p_j`,

`R >= G + max( (sum_j p_j)/2, sum_j p_j-e_del, max_j p_j )`.     (2)

The last term follows because the penetration union contains every `X_j`.
For integer `p_j`, the first term can be rounded up. In particular,

`2R >= 2G + sum_j p_j`.                                      (3)

MCP1/MCP2 have `G` rather than `2G` on the right of their displayed
factor-two aggregate. Equations (2)-(3) strengthen that aggregate without
changing any individual penetration lower bound. They do not repair a missing
or geometrically invalid penetration bound.

## 2. The two-grain interface correction is exact

For two grids let `I` count the physical crossings with one endpoint in `Q_1`
and one in `Q_2`. These crossings are deleted edges, so `I<=e_del`, but they
need not all be charged. The intersection `X_1 intersect X_2` is contained in
this interface. If only an upper bound `I<=K` is known, then (1) gives

`R >= G + max(p_1,p_2,p_1+p_2-K)`.                           (4)

If the **actual physical count** `I` is known, count all of it even when some
edges are uncharged. Outside that interface, the two penetration sets are
disjoint. Thus

`R >= G + I + (p_1-I)_+ + (p_2-I)_+`
`  = G + max(I,p_1,p_2,p_1+p_2-I)`.                         (5)

The distinction between an upper bound and an actual count matters: replacing
`I` by `K` in the `max(I,...)` part of (5) is invalid for an upper bound alone.

Both inequalities are sharp in the unrestricted incidence inventory, even for
finite simple-edge inventories with distinct eligible slots. Suppose there are
`S` potential shared edges, `T_1` private slots eligible only for grid 1, and
`T_2` private slots eligible only for grid 2. Internal grid edges are fixed;
other physical edges can be omitted. For nonnegative integer demands `p_1,p_2`:

* At exact shared physical count `I<=S`, feasibility is exactly
  `p_j<=I+T_j`. Charge `min(p_j,I)` of the same `I` shared edges to grid `j`
  and use `max(0,p_j-I)` private edges. The two shared charge subsets may
  overlap freely. The number of exterior physical edges is exactly (5).
* Under the upper cap `I<=K<=S`, feasibility is exactly `p_j<=K+T_j`.
  Choose
  `I_* = max(min(K,p_1,p_2), p_1-T_1, p_2-T_2)`.
  It lies between zero and `K`. Substitution into (5) gives exactly
  `max(p_1,p_2,p_1+p_2-K)`, proving (4) is the optimum.

For the second assertion, assume `p_1>=p_2` by symmetry. If `K<=p_2`, then
`I_*=K` and the cost is `p_1+p_2-K`. Otherwise
`p_2<=I_*<=min(K,p_1)` and the cost is `p_1`. This proves the displayed
substitution, including limited private inventories.
These constructions assign edge states only; they do not realize train tracks,
separator diagonals, a rhombic disk, or a global packing.

## 3. Conditional substitution into PC1/PC3

For the **actual supplied grids and penetration sets** satisfying all PC1
hypotheses, including `d_j=min(k_j,l_j)-2>0`, take

`p_j=d_j (|U_j+V_j|-D)_+`.

Equation (2) then applies with `G=sum_j M_j b_j`. For the coherent PC3 regime,
its stated uniform error and all of its geometry must also hold. Put

`c=2/sqrt(3)`,
`a_j=d_j(M'_j+b'_j-cD-error_j)`,
`p_j=[a_j-(c-1)E_del(H_j)]_+`.

Because `sum_j E_del(H_j)<=2e_del`, the additive branch of (2) gives

`R >= G + sum_j a_j - (2c-1)e_del`.                        (6)

This is an additive consequence; (2) with the positive parts is stronger.
For fixed Section-50 `lambda>0`, the component count is `O_lambda(1)`,
`d_j=O(D)`, and uniform angular coherence is `o(1)`. Hence the audited error
sum remains `sum_j d_j error_j=o(D^2)` at fixed `lambda`. With the Section-50
bound `e_del<=C_delta D^(2-eta)+C_T lambda D^2`, equation (6) reads

`R >= G + sum_j d_j(M'_j+b'_j-cD)`
`      -(2c-1)(C_delta D^(2-eta)+C_T lambda D^2)-o(D^2)`.  (7)

Fix `eta,lambda` before `D` tends to infinity. The coefficient `2c-1` is
`4/sqrt(3)-1`; no floating-point approximation is used in this implication.
A subsequent small-`lambda` limit needs uniform control of any separately
claimed positive gain. This note supplies no such gain: density-only PDG grids
may remain below the PC3 threshold, with all `p_j=0`. Neither the improved
physical count nor (7) pays virtual determinant mass or topology terms.

## 4. Reproduction and finite evidence

The standard-library [checker](../../../research/verify_target_b_interface_capacity_2026_10_17.py)
imports no predecessor verifier. Its committed
[fixture](../../../research/target_b_interface_capacity_2026_10_17.json) records exact
SHA-256 identities for the public prerequisites, inventory sizes, per-domain
histogram digests and negative controls. Each reproduction recomputes those
source hashes; a changed prerequisite requires scope review before regeneration.
The base commit above and the fixture jointly identify the source snapshot.

The domain has four positive labelled shore sizes `(a,b,c,d)` with
`a+b+c+d<=6`, and `q` pruned trains with `q in {0,1}`. Thus there are 30
configurations. Their train phases are `u^a,v^b,u^c,v^d,w^q`. All same-phase
pairs are absent. Internal crossings are fixed, with `G=ab+cd`; there are
`S=ad+bc` potential shared edges, `T_1=(a+b)q` private slots for the first
grid, and `T_2=(c+d)q` for the second. Each shared pair has five states
(absent, physical uncharged, charged only by 1, only by 2, or by both).
Each private pair has three states (absent, physical uncharged, charged).
This gives exactly `5^S 3^(T_1+T_2)` labelled states per configuration.
All optional physical edges are declared deleted. Absent pairs are virtual;
distinct-phase determinant areas are counted in units `sqrt(3)/2`.

The two engines agree on all **8,336,550 labelled states** and their complete
`(exterior R, |X_1|, |X_2|, I)` histograms. The first engine recursively visits
every labelled edge state. The second enumerates five-category shared and
three-category private occupation vectors with multinomial weights, then
convolves the inventories. Neither engine obtains its histogram by evaluating
the proposed optimum formula. Only after comparing the histograms does the
checker minimize physical edge count and compare with (4)-(5).

All **5,964 exact-I** demand/inventory cases and **5,964 upper-cap** cases
agree with the formulae, including infeasible cases. Exact charge counts are
used in the enumeration; these give the same minimum as lower demands because
unneeded charges can be removed without removing physical edges. A separate
six-train, three-grid set-based enumeration checks (1)-(2) on **15,625 states**;
448 attain the rounded half-use bound, and 64 attain the deletion-budget bound.

The repaired lower bound strictly exceeds the rounded displayed MCP1 bound
in all 8,336,550 states, and exceeds the maximum of that bound, the trivial
internal count, and the two individual PC1 grid-plus-charge counts in
8,335,751 states. These figures compare finite bookkeeping bounds; the demands
are arbitrary eligible charges, not geometrically established penetration.

Failure controls and limits:

* The predecessor's minimal `R=3` witness has internal edges `01,23` and the
  physical shared edge `03` charged by both grids. Naive addition demands four;
  (5) gives exactly three. Without any pruned train, four grid trains suffice.
  Positive shores require at least these four trains; exceeding `R` by double
  charge requires at least one more physical edge beyond the two internal ones.
  This proves minimality in the declared model, not in geometric packings.
* With the same demands but two distinct private physical edges `04,24`, the
  exact minimum is four. The interface correction distinguishes the inventories.
* With `K=1`, actual `I=0` and zero demands, the physical count can be `R=G=2`.
  The mutation that treats the cap as an actual count incorrectly demands three.
* Removing the distinct-retained-component/deleted-interface hypothesis permits
  a double charge without any deletion payment; the same `R=3` charge pattern
  rejects the resulting uncorrected sum. It is a hypothesis control only.
* A separate determinant ledger has eight total area units, partitioned into
  two internal, one deleted and five virtual units on the minimal five-train
  witness. The repaired physical count does not pay the five virtual units.
* For two complete `n by n` incidence grids with no external edges, the encoded
  demands may be zero and `R=G=2n^2`. The bound is equality for every integer
  `n>=1`; the checker retains examples `n=1,2,3,10,100`. Thus aggregation alone
  supplies no positive excess or eventual global-minimizer contradiction.

From the repository root, with Python 3.12.3 on Linux x86_64:

```sh
python3 research/onboarding_two_grain_audit.py
python3 research/verify_target_b_interface_capacity_2026_10_17.py --check research/target_b_interface_capacity_2026_10_17.json
python3 -O research/verify_target_b_interface_capacity_2026_10_17.py --check research/target_b_interface_capacity_2026_10_17.json
python3 tools/check_public.py
python3 tools/local_ci.py --base-ref origin/main
```

The verifier uses explicit exceptions, so optimization cannot disable its checks.
The committed fixture is an output, not a source of expected optimum values
inside either enumeration engine. A deliberately altered fixture must fail.
Both the normal and optimized commands matched the committed fixture. A copy
with its two-grain state count increased by one was rejected with exit 1 and
`fixture differs from independently recomputed evidence`.

The pre-submission refresh at `2026-10-17T20:38:40Z` still found upstream
`e396ea07887dd0528b817ce4e656ff0e6b01f8fb`; state, priority and catalogue
were unchanged. The refreshed overlap snapshot again covered all open PR/Issue
bodies and Discussion bodies/comments/replies, with no remote match or pending
handoff. The host uses Python 3.12.3 rather than the hosted Python 3.14
environment. Its GitHub CLI 2.45.0 lacks `--slurp`; a temporary external adapter
removed that flag, decoded the CLI's concatenated paginated JSON responses, and
supplied the same array-of-pages interface for the read-only overlap command.
No adapter or CLI change is part of this contribution.

Exact submission head/tree, final public-integrity output and planner scope are
recorded in the PR to avoid a self-referential commit pin in this report.
Required repository-wide certificate replay is **deferred to the merging
agent** on the final integration candidate; it has not been claimed as a pass.
All statements in this contribution remain unreviewed, and the theorem manifest
and canonical route statements are unchanged.

## Open next questions

Can source-derived two-grain grids force a positive total PC3 excess while
retaining enough internal grid mass and paying the actual shared interface?
A first action is to use one explicit pure rhombic disk, select retained
components and deep diagonals, and compute `G_j`, every actual separator-induced
`X_j`, shared `I`, deleted incidences, and the virtual determinant ledger before
substituting (2) or (5). The blocker is source extraction and geometric payment,
not the now-explicit finite counting optimum. A small graph model with arbitrary
charge assignments supplies none of those geometric hypotheses.
