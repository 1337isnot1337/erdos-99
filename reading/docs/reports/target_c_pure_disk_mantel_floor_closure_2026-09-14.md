> Generated reading edition · [exact source](../../../docs/reports/target_c_pure_disk_mantel_floor_closure_2026-09-14.md) · source SHA-256 `7d84db43681f3d4f0c2be093365855931609384e48c53da4d8f43ea9075bab88`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-709BBF07C31F","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — pure-disk closure of the full-core Mantel-floor endpoint

**Date:** 2026-09-14
**Repository commit:** ef941ab2b44aa393bdc461926769247b45754202
**State version:** 2026-09-14.audit.49
**Run type:** closing proof / exact conditional branch closure
**Target:** Target C-II / Level I
**Starting status:** report-level Mantel endpoint plus report-level dual-tree and phase-star lemmas
**Active prompt:** docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md
**External literature search:** not used in the proof
**Computation:** not used

## LEVEL I STATUS

STILL OPEN

This report closes one sharply delimited branch only: a full-core floor-endpoint
sequence whose strict-rhombus complex is a simply connected train disk. The
canonical full-core source may have holes, interfaces, and other boundary
components, so the result does not discharge Target C-II or Level I.

The proved implication is:

    full-core train-floor endpoint
      + simply connected proper-train disk
      -> Mantel near-star
      -> almost-full complete phase star
      -> source-point diagonal longer than D
      -> contradiction.

The proof retains the original source diameter D. It does not replace the source
by a scaffold, delete contact-isolated points, or invoke a fixed-container
competitor.

## 1. Exact hypotheses and endpoint input

Consider a sequence of triangle-free global minimizers in the canonical
contact-minimal, then diameter-pair-minimal representative, with D tending to
infinity, in the full-core no-macroscopic-container branch. Assume

    mu_D -> mu_TC,
    mu_TC = (2*pi + 2*sqrt(Delta_2))/5,
    Delta_2 = pi/(2*sqrt(3)).

Let R_D be the number of strict rhombus faces and T_D the number of global train
tracks. The promoted full-core endpoint ledger gives

    R_D / D^2 -> Delta_2,
    T_D / D -> 2*sqrt(Delta_2),
    R_D / T_D^2 -> 1/4.                         (1)

The last equality is the report-level Mantel endpoint consequence of the exact
train-boundary squeeze; it is not an independent density assumption.

Additional hypothesis of this report:

> Pure-disk train hypothesis. After the canonical O(D) phase-circle cut, the
> strict-rhombus complex is a simply connected topological disk, and every
> retained train in the phase classes below is a proper crosscut of that disk.
> Tracks in the same phase class are pairwise disjoint, and any two tracks cross
> at most once.

This is a genuine extra hypothesis. It excludes the holes/interfaces still live
in canonical C-II.

Let the three phase-label classes have sizes M_D >= U_D >= V_D. The phase-star
endpoint calculation gives

    M_D/T_D -> 1/2,
    (U_D+V_D)/T_D -> 1/2.                       (2)

We will prove the stronger pair estimate

    M_D(U_D+V_D) - e(M_D,U_D) - e(M_D,V_D) = o(T_D^2), (3)

where e counts retained actual rhombus crossings.

## 2. Mantel stability and phase-star extraction

For completeness, the needed graph step is stated with its exact scope.

### Lemma 2.1 — endpoint partition and label concentration

Let G_D be the phase-cut train-crossing graph. Under (1), there is a partition
X_D union Y_D with

    |X_D|, |Y_D| = T_D/2 + o(T_D),
    e(G_D[X_D]) + e(G_D[Y_D]) = o(T_D^2),

and o(T_D^2) missing cross edges. If x_i and y_i count label i on X_D and
Y_D, then

    sum_i x_i y_i = o(T_D^2),
    sum_i min(x_i,y_i) = o(T_D).               (4)

Consequently the largest label is concentrated on one partition side, while the
other two labels are concentrated on the other side, and (3) holds.

Proof. For every edge uv in a triangle-free graph,
d(u)+d(v) <= T_D. Summation over edges, with
e(G_D)=T_D^2/4-o(T_D^2), gives

    sum_z (d(z)-T_D/2)^2 = o(T_D^3).

The usual neighborhood partition X=N(x), Y=V-N(x), choosing x with
d(x)=T_D/2+o(T_D), gives the displayed balanced partition and edit estimates.
This is the elementary degree-square proof of Mantel stability.

Equal-label trains cannot cross. Thus every same-label cross pair is a missing
cross edge, so sum_i x_i y_i=o(T_D^2). Cauchy-Schwarz gives

    sum_i min(x_i,y_i) <= sum_i sqrt(x_i y_i)
                         <= sqrt(3 sum_i x_i y_i) = o(T_D).

The elementary tripartite phase bound e <= M(U+V), for M >= U >= V, together
with e=T_D^2/4-o(T_D^2), gives (2). The concentration estimate then puts M_D,
up to o(T_D) trains, on one side and U_D union V_D on the other. Internal edges
on the latter side and missing cross edges are o(T_D^2), proving (3). QED.

### Lemma 2.2 — dense proper-train pairs contain almost-full grids

Let A and B be pairwise-disjoint proper crosscuts in a simply connected disk,
with every pair crossing at most once, and suppose

    e(A,B) = (1-o(1)) |A| |B|.                  (5)

Then there are A' subset A and B' subset B such that

    |A'| = (1-o(1))|A|,
    |B'| = (1-o(1))|B|,

and every A'-track crosses every B'-track.

Proof. Delete o(|A|) rows with more than eta|B| missing crossings, where eta
tends to zero after the density error. Choose a remaining row a_* with at most
eta|B| misses. The complement dual of the pairwise-disjoint B crosscuts is a
tree. The B tracks crossed by a_* form a path in this tree. Every other A row
also crosses a dual-tree path, and its intersection with the a_* path is a
connected subpath. Hence its crossings with the ordered backbone B_0 form an
interval, missing at most eta|B| members.

Delete eta|B| tracks at each end of B_0. The central block is crossed by every
remaining A row and has (1-o(1))|B| tracks. This proves the lemma. QED.

Apply Lemma 2.2 to the two center-to-leaf pairs in (3). If one leaf class is
o(M_D), retain the other and absorb the small class into the external error. If
both are linear, intersect the two (1-o(1)) center subfamilies. We obtain a
complete coherent center-to-leaf star with center size M'_D and leaf sizes b_D
and a_D (possibly a_D=0), satisfying

    M'_D/D -> sqrt(Delta_2),
    (a_D+b_D)/M'_D -> 1,
    0 <= a_D <= b_D.                            (6)

All other train tracks and all contact-isolated source points remain in the
source.

## 3. Complete-star diagonal estimate

The total strict-rhombus acute-angle defect is O(D). On each complete
center-to-leaf product, the defect is the positive reduced-phase difference.
For two linear families, write each defect as

    delta_ij = g + r_i + s_j,  with g,r_i,s_j >= 0.

The O(D) defect sum implies
ab*g + b*sum_i r_i + a*sum_j s_j = O(D).
After deleting o(D) tracks, the reduced phase spread in each linear family is
o(1), and its relative gap is o(1). (For each fixed epsilon, only O(1/epsilon)
tracks can have r_i or s_j at least epsilon.) Thus the retained three phase
classes have directions o(1)-close to

    u=(1,0), v=(1/2,sqrt(3)/2), w=(1/2,-sqrt(3)/2).

We now prove the required source-level estimate.

### Lemma 3.1 — complete coherent phase-star cost

In a simply connected proper-train disk, suppose a complete coherent star has
center size M, leaf sizes b >= a >= 0, and all non-star crossing mass is o(M^2).
Then, with s=a/M and t=b/M,

    D^2 >= (F(s,t)-o(1)) M^2,                   (7)

where

    F(s,t) = 1+t+t^2-s(1-t)+s^2,   if s < (1-t)/2,
              3(1+t)^2/4,           if s >= (1-t)/2.

Proof. Trim a fixed small fraction from both ends of the complete center-B grid.
The four inward grid corners are actual source vertices. Any train outside the
selected star which separates a chosen diagonal must cross a fixed positive
multiple of M selected center or leaf tracks: follow it from the central grid
through the complement dual tree to a disk boundary region. Since the total
non-star crossing mass is o(M^2), only o(M) external trains can separate the
diagonal; their signed vector contribution is o(M).

The center and B contributions to the selected diagonal are M*u+b*v+o(M).
The C contribution is x*w+o(M), with |x| <= a+o(M). Therefore a source-point
difference has squared length at least

    min_{|x| <= a+o(M)} |M*u + b*v + x*w|^2 - o(M^2).

After division by M^2,

    |u+t*v+x*w|^2 = 1+t+t^2+(1-t)x+x^2.

The unconstrained minimizer is x*=-(1-t)/2, which yields (7). The grid
corners are source points, so their distance is at most the original source
diameter D. QED.

The only non-elementary-looking sentence in this proof is the external-separator
count; it uses exactly the pure-disk crosscut hypothesis and the dual-tree path
argument. It is not asserted for a holed/interface complex.

## 4. Contradiction at the floor

In the one-leaf case, a_D/M'_D -> 0 and b_D/M'_D -> 1. In the two-leaf
case, a_D/M'_D+b_D/M'_D -> 1 and b_D/M'_D >= 1/2. In either case the second
line of F applies and

    F(a_D/M'_D,b_D/M'_D) >= 27/16 - o(1).       (8)

By (6),

    (M'_D)^2 / D^2 -> Delta_2 = pi/(2*sqrt(3)).

Combining (7) and (8),

    1 >= (27/16)*pi/(2*sqrt(3)) - o(1)
      = 27*pi/(32*sqrt(3)) - o(1) > 1,

where the final strict inequality follows already from pi>3 and sqrt(3)<2:
27*pi/(32*sqrt(3)) > 81/64 > 1. Contradiction.

Therefore:

> Pure-disk floor closure. No full-core triangle-free global-minimizer sequence
> attaining mu_D -> mu_TC can have a simply connected proper-train strict-rhombus
> disk after the phase-circle cut.

This is asymptotic and conditional on the floor endpoint. It is not a finite
threshold theorem for the original problem.

## 5. Frontier effect and exact remaining lemma

The report eliminates the branch

    mu_D -> mu_TC
    + no holes/interfaces in the strict-rhombus train disk.

It does not apply to holes, interfaces, bridges, nonproper train endpoints, the
higher-surplus branch liminf mu_D > mu_TC, or the macroscopic-container branch.
It also does not address Target A or Target B.

The exact remaining C-II endpoint lemma is:

> Under mu_D -> mu_TC with a holed/interface strict-rhombus complex, prove an
> effective dual-tree backbone sufficient for the same complete-star diagonal
> estimate, or derive a direct source-preserving diameter penalty from the
> o(T_D^2)-missing phase-star crossing pattern. All repeated boundary occurrences,
> bridges, and contact-isolated source points must remain in scope.

## 6. Claim audit table

| Claim | Status | Dependencies | Reason |
| --- | --- | --- | --- |
| Floor endpoint (1) | canonical/report-level input | C-FULLCORE-TRAIN-SURPLUS-FLOOR plus Mantel endpoint report | Current scalar floor is canonical; Mantel limit is report-level |
| Mantel partition and label concentration | proved here, report-level | elementary triangle-free graph theory | Degree-square proof and label count are included |
| Near-complete pair extraction | proved here, conditional | simply connected proper-train disk | Dual-tree crosscut proof is included |
| Phase coherence after o(D) deletion | proved here, conditional | global O(D) angular-defect budget | Exact gap-plus-deviation decomposition |
| Complete-star diagonal estimate | proved here, conditional | pure disk; source train coordinates | External separators are charged through the dual tree |
| 27*pi/(32*sqrt(3)) > 1 | elementary exact inequality | pi>3, sqrt(3)<2 | Rational margin 81/64 |
| Pure-disk floor closure | conditional branch theorem | all previous rows | Holes/interfaces are not excluded canonically |
| Level I | open | original quantifiers | Other C-II branches and Targets A/B remain |

## 7. Regression audit

| Regression | Result | Exact reason |
| --- | --- | --- |
| Abstract near-complete random bipartite graph | does not apply | It lacks the proper-crosscut dual-tree structure |
| Branched disjoint crosscuts | pass | No global linear stack is assumed; one almost-spanning backbone is selected |
| Contact-isolated source points | pass | Never deleted; only actual source corners and original D are used |
| Phase-cut edge deletion | pass | O(D)=o(D^2) relations are removed, not source points |
| Holes/interfaces | binding failure of hypothesis | The complement dual need not be a tree |
| Local stress versus global optimality | pass | No stress-to-release inference is used |
| Source/scaffold substitution | pass | The diagonal endpoints are actual source vertices |
| One-leaf class o(M) | pass | Its total possible vector contribution is o(M) |

## 8. Literature and computation

No external theorem or computation is imported. The final numerical margin is
certified symbolically by pi>3 and sqrt(3)<2.

## 9. Promotion recommendation

**conditional** — the pure-disk branch proof is complete under its explicitly
stated topological hypotheses, but those hypotheses are not canonical for all
C-II full-core minimizers. Do not change the Level-I or C-II theorem-state status.

## 10. Handoff

1. Strongest new theorem: the full-core train-floor endpoint is impossible in a
   simply connected proper-train disk; the contradiction is
   D^2 >= (27/16+o(1)) M^2 versus M^2/D^2 -> pi/(2*sqrt(3)).
2. Canonical dependency chain: C-FULLCORE-TRAIN-SURPLUS-FLOOR plus the report-level
   Mantel endpoint, with the pure-disk dual-tree hypothesis added.
3. Exact remaining lemma: holed/interface near-complete phase-star completion or
   a direct source-level diagonal/deformation argument.
4. Binding dead routes: abstract Mantel stability without planar dual-tree control;
   arbitrary hole filling; local stress-to-release arguments.
5. Read next: target_c_fullcore_mantel_endpoint_stability_2026-09-14.md,
   target_c_fullcore_train_mantel_phase_star_endpoint_2026-09-14.md,
   76-hole-stable-complete-grid-order-diameter-audit.md, and
   target_b_dual_tree_dense_grid_extraction_correction_2026-09-05.md.
