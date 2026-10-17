> Generated reading edition · [exact source](../../../docs/reports/target_c_cii_closure_run_2026-09-11.md) · source SHA-256 `01c379f99f82c14a57acc54313e6a9ce7b6bd468c4e61dc619aee520120a3870`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-C795ECE1179F","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — C-II closure attempt

**Date:** 2026-09-11  
**Repository commit:** `67f66acc54705c7c4131f595633edf34a3705c5e`  
**State version:** `2026-09-11.audit.33`  
**Run type:** closing proof  
**Target:** C-II  
**Claim classification:** proved candidates awaiting promotion; run in progress
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md`  
**External literature search:** used for leads; no external theorem imported in the protected-motion proof
**Computation:** `docs/research/migration/2026-10-16/shards/01/support/research/verify_target_c_protected_contact_creation.py`

## Level I status

STILL OPEN. This run has not established a C-II exclusion.

## Starting endpoint and dependencies

The remote refresh found `main` current at the commit above. The controlling state
is audit.33, including the core-only ZR/ZF correction and the promoted global
container/full-core dichotomy. Unmerged remote branches are not theorem inputs.

The requested theorem is exclusion of every sufficiently large triangle-free global
minimizer after contact-count, then diameter-pair-count minimization. All source
points remain present. The two surviving alternatives are the actual macroscopic
inactive container and the full-core near-disk branch.

The intended proof dependencies are C-ZTA, C-ZRF, C-FS-GEOM, C-FS-STABILITY,
C-RHOMBUS-POP, C-PUNCTURED-PHASE, C-COHERENT-GRAINS,
C-INACTIVE-CHAMBER, C-INACTIVE-HULL-STABILITY, C-INACTIVE-NEAR-MATCHING,
C-INACTIVE-DEEP-MATCHING, C-INACTIVE-DICHOTOMY, C-FULLCORE-NEAR-DISK,
and C-HARMONIC-GRID-LOCAL, under their manifest scopes. No audited-working or
unreviewed report is an unconditional premise.

## Candidate-to-endpoint ledger

| Attempt | Exact implication to test | Status |
| --- | --- | --- |
| Protected inactive-container replacement | Source-preserving feasible replacement and deformation of the retained core -> strict diameter below D -> contradict global minimality | Unreviewed candidate; no replacement/deformation theorem yet |
| Harmonic-grid deformation or interface surplus | Quantitative source-preserving deformation or sufficient full-source packing deficit -> strict diameter below D or nonpositive lattice excess -> contradict global minimality | Unreviewed candidate; exact new bridge pending |
| Isolate pair closing alone | New isolated-point contacts -> no contradiction to minimizing the original contact count | Rejected as a standalone closing inference |

## Audit requirements

Check every contact and diameter pair, preserve contact-isolated population, and
distinguish a finite feasible path from a first-order velocity. A local stress or
dense feasible packing is not a global-optimality certificate. Any result will be
recorded here with a complete proof or exact missing premise before promotion is
considered.

## Promotion recommendation

Unreviewed. No canonical frontier or state-version change is requested by this
initial run record.

## Repository validation at the first checkpoint

The declared validation dependencies were installed in a temporary virtual
environment. The theorem-state check runs but reports two pre-existing Target A
endpoint mismatches: its route map and active prompt do not contain the Section-175
endpoint recorded in the manifest. Those files are unchanged by this run. The
artifact generator also registered a pre-existing unindexed Sections 79/80/82/83/88
audit as unreviewed; its generated metadata does not promote any claim.

`git diff --check` passes. Mathematical work continues from the unchanged Target C
audit.33 state.

The first push raced with upstream commit `0657244` (audit.34). Its state diff was
read before merging: C-HARMONIC-CARRIER-QUAD, C-HARMONIC-CELL-TILING, and
C-HARMONIC-WRAPPING are newly canonical, while C-II and both global alternatives
remain open. Subsequent work may use those results only after reading their active
modules. The two generated-metadata merge conflicts were resolved by regenerating
from the incoming manifest, preserving both the upstream promotion and this report.

## Protected simultaneous contact creation

**Classification:** proved candidate awaiting promotion. The report remains
unreviewed in the artifact registry; this is not a canonical C-II advance.

### Finite statement PSC

Let `A` be a finite unit-separated planar source of diameter `D`, with triangle-free
contact graph. Let `C` be a positive-area compact convex chamber contained in
`K=conv(A)`, with no nonisolated contact vertex in its interior. Fix `w>1` and
`0<epsilon<=1/4`. Suppose `M` vertex-disjoint pairs `(x_i,y_i)` of actual
contact-isolated source points satisfy

$$
x_i,y_i\in C_{-w},\qquad 1<|x_i-y_i|\le1+\epsilon.
$$

Then at least `ceil(M/49)` of the `x_i` can move simultaneously, each by at most
`epsilon` along its segment toward `y_i`, to first contact, with these properties:

1. Every intermediate source is unit-separated and has the same convex hull and
   diameter as `A`.
2. All original contacts and diameter pairs are unchanged.
3. At the terminal source, the new contact graph is a disjoint union of at least
   `ceil(M/49)` nonempty stars on formerly contact-isolated vertices, disjoint from
   the old nonisolated core. In particular, the whole contact graph is triangle-free.
4. If the original normalized KKT polytope is nonempty, the terminal normalized
   KKT polytope is exactly its zero-extension to the new contact coordinates.
   Every newly created contact is zero in every normalized KKT stress.

No uniform lower bound on the displacement to first contact is asserted.

### Proof: select separated moving centers

Orient each matching edge once, taking `x_i` as its proposed moving center. These
centers are unit-separated. At most 49 of them can lie in a closed radius-3 disk:
their open radius-1/2 disks are interior-disjoint and lie in a radius-7/2 disk, so
area comparison bounds the number by `(7/2)^2/(1/2)^2=49`.

Greedily retain one center and discard all remaining centers at distance at most
3 from it. Each choice discards at most 49, including itself. The resulting set
`J` has `|J|>=ceil(M/49)` and pairwise center distances greater than 3.

### Proof: run the independent motions together

For each `i in J`, temporarily keep every other source point fixed and move `x_i`
toward `y_i`. Since `x_i` is initially contact-isolated, a positive initial motion
is feasible. By displacement `|x_i-y_i|-1<=epsilon`, the mate would be at unit
distance, so there is a first-contact time `t_i` in `(0,epsilon]`. Stop there.
Simultaneous first contacts at that same time are allowed.

Parameterize all the stopped motions over one common interval `[0,1]`, moving
center `i` through displacement `s t_i`. Every center remains on `[x_i,y_i]`, hence
in the convex inner parallel body `C_{-w}`. Its distances to every fixed source
point are at least one by the definition of its first-contact time. Two moving
centers stay at distance greater than `3-2epsilon>1` from each other. These checks
exhaust all pair types, so the simultaneous motion is feasible throughout.

Every moved point was and remains in the interior of `K`. Thus all original
extreme vertices remain fixed, and the convex hull stays exactly `K`. The diameter
therefore stays exactly `D`. A point in the interior of a positive-area diameter-D
convex body cannot form a diameter pair with a point of that body: expressing it
as a nontrivial convex combination and using strict convexity of squared distance
gives a strict inequality below `D^2`. Consequently no new diameter pair is made.

Every old contact endpoint is on or outside the chamber boundary. Each moved
point stays at distance at least `w>1` from it. Hence all new contacts join a moving
center to a fixed formerly contact-isolated point. Fixed points have exactly their
old pair distances, so these leaves have no old contact edges. No fixed point can
be a leaf of two new stars: at terminal contact it lies within `1+epsilon` of each
of their original centers, contradicting center separation greater than 3 since
`2+2epsilon<3`. There is no edge between moving centers. The new graph is therefore
a vertex-disjoint union of nonempty stars and remains disjoint from the old core.
This proves claims 1–3.

### Proof: the whole KKT polytope is unchanged

Every new star component has no incident diameter edge. The moved center cannot
be diametral because it remains in the interior of `K`. Every leaf is also in the
chamber interior, since its distance from a terminal center in `C_{-w}` is one
and `w>1`; thus it is not diametral either.

For any nonnegative normalized equilibrium stress on the terminal source, sum
the vertex equilibrium equations of one new component after dotting each with
its vertex position. No external contact or diameter load enters that component.
Each internal contact is counted at both endpoints and contributes its weight
times squared length one. The result is

$$
\sum_{e\text{ in the new component}}\alpha_e=0.
$$

All weights are nonnegative, so every one vanishes. Restricting to the unchanged
old core and old diameter pairs therefore gives an original normalized stress.
Conversely, every original normalized stress extends by zero to every new edge
and satisfies all terminal equilibrium equations. The normalization is identical.
The two maps are inverse. This proves claim 4. `square`

### More general fixed-core obstruction FCO

The KKT argument is not limited to the selected stars. Suppose an arbitrary subset
of originally contact-isolated points **whose original positions lie in `C_{-w}`**
is moved to other positions in `C_{-w}`, with `w>1`, while every other point stays
fixed, and the resulting source is unit-separated. Then the source hull, diameter
pairs, old contact core, and normalized KKT polytope are unchanged (the last by
zero-extension).

The initial-location hypothesis is necessary for this fixed-hull statement. Without
it, an originally contact-isolated point could be an extreme point of the source hull
or an endpoint of an active diameter pair; moving such a point inward could change the
hull or the active diameter set. In the canonical deep-chamber application the moved
isolates already lie in `C_{-w}`, so this correction does not weaken that application.

Indeed no new edge can reach an old contact-core vertex; all new contact components
consist of formerly isolated points. Both the original and terminal moved vertices
lie in `int(K)`, so all old extreme vertices and all old diameter endpoints remain
fixed and the source hull remains `K`. Any fixed vertex in a new component must touch
a moved vertex, since fixed formerly isolated vertices have no edges to each other.
It therefore lies in `int(C)` and has no diameter edge. Apply the same contact-only
virial identity to each new component. The new components need not be stars and need
not be triangle-free for this more general statement.

FCO is an obstruction to a proposed method, not a C-II contradiction: the retained
old diameter pair itself prevents every fixed-core rearrangement from decreasing
the global diameter. Positive new contact count, even a large one, does not force
positive new contact stress.

### Canonical application and implication audit

Take the canonical deep-matching theorem with a fixed `w>1`. It supplies `M>=c_wD`
pairs with `epsilon=K_w/D`, which is at most `1/4` eventually. PSC gives a
same-cardinality, same-diameter, triangle-free global minimizer with at least
`c_wD/49` additional contact stars and **exactly the old KKT polytope**.
It is a global minimizer because feasibility, cardinality, and diameter are
preserved from the original global minimizer. It is contact-richer, and is not
asserted to be the canonical contact-minimal representative.

The actual implication chain is

```text
C-INACTIVE-DEEP-MATCHING
 -> linear number of spatially separated first-contact motions (PSC)
 -> simultaneous linear contact creation is feasible
 -> all new contacts remain universally zero-stress (FCO)
 -> contact creation alone cannot transfer population into the positive core.
```

This closes a simultaneous-compatibility subproblem for first-contact creation,
while disproving the proposed implication to force visibility at that step.
It does not close PIHR, C-II, or either global population branch.

## Exact finite motion checks

Run `python3 docs/research/migration/2026-10-16/shards/01/support/research/verify_target_c_protected_contact_creation.py`.

The script takes finite triangular-lattice parallelograms expanded by
`1+1/L^2`, selects deep disjoint horizontal pairs, thins their moving centers by
the radius-3 rule, and moves each selected center by `1/L^2`. Coordinates are in
`Q(sqrt(3))`; all squared distances have integer numerators. For every pair, the
minimum squared distance throughout the entire common time interval is evaluated
exactly as the minimum of a quadratic on `[0,1]`.

| L | Points | Candidate pairs | Simultaneous contacts | Continuous pair checks |
| --- | ---: | ---: | ---: | ---: |
| 12 | 144 | 8 | 2 | 10,296 |
| 20 | 400 | 72 | 15 | 79,800 |
| 32 | 1,024 | 288 | 54 | 523,776 |

Every check passes. The final contact set is exactly the chosen matching; the
diameter is unchanged. These are feasible finite regressions, not globally optimal
sources and not examples satisfying every C-II hypothesis.

The script also certifies a different-first-blocker example:

$$
x=(0,0),\quad y=(21/20,0),\quad
z=(7007/25000,24024/25000).
$$

All three distances initially exceed one. Moving `x` horizontally toward `y`
meets `z` at a time in `(1/300,1/250)`, before the proposed mate closes at
`1/20`. Exact rational polynomial signs and monotonicity certify this bracket.
Thus PSC stops at the actual first blocker and does not assume that a selected
matching mate must be the contact produced.

## Dependency and regression audit of PSC/FCO

| Input or potential failure | Disposition |
| --- | --- |
| C-INACTIVE-DEEP-MATCHING, canonical module 87 | Supplies the actual source pairs only in its stated chamber scope |
| KKT equilibrium, shared theory 01, Theorem 4.1 | Used with nonnegative multipliers and the original normalization |
| Simultaneous versus individual motions | Every pair type checked; center thinning prevents interference |
| Unintended first blockers | Allowed, including simultaneous ties; the exact example confirms the need |
| Contact-isolated source points | Retained with their original labels and cardinality |
| Source versus lattice scaffold | General proof uses actual source points; lattice examples are only finite checks |
| Weak multiplier versus finite release | No release from a zero multiplier is inferred |
| Core rigidity versus full-source rigidity | No rigidity is assigned to isolated coordinates |
| Contact minimality | The terminal source has more contacts; no contradiction is inferred from that |
| External caps | No extension to an exterior-cap application is claimed without checking its protected-pair hypotheses |

## Remaining closure obligation after this checkpoint

The missing chamber-side theorem must move some of the original diameter-carrying
core, or provide a different same-cardinality configuration of diameter below D.
A sequence confined to rearranging protected isolates cannot do either. The
full-core near-disk case still requires its own quantitative aggregation or global
competitor theorem.
