> Generated reading edition · [exact source](../../../docs/reports/target_c_two_direction_boundary_repair_2026-09-14.md) · source SHA-256 `e8ad235e4dbfcebcfb5b256ba4d2630274b8d82620d1777aa26dc433ad227c55`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-A1701D333E3D","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — repaired two-direction boundary exclusion

Date: 2026-09-14
Repository commit: ef941ab2b44aa393bdc461926769247b45754202
State version: 2026-09-14.audit.49
Run type: closing proof / independent audit / conditional branch exclusion
Target: C-II / Level I
Starting status: canonical C-II full-core frontier; an unreviewed fixed-direction candidate was available
Active prompt: docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md
External literature search: used for status only; no theorem imported
Computation: not used as a proof input

## LEVEL I STATUS

STILL OPEN

This report repairs an unreviewed fixed-direction candidate. It proves that a
specific full-source, simply connected, two-direction rhombic branch has bounded
cardinality. It neither asserts that every C-II minimizer has this form nor closes
the macroscopic-container branch, so the original Level-I quantifiers remain open.

## 1. Starting canonical endpoint

The current full-core route still needs a source-level implication from the
aggregate Section-122 detour and Section-123 payment to an exact triangle, a
source-preserving strict diameter decrease, or a global contradiction. The fixed
two-direction idea was a possible source-level route, but its earlier proof used
the following false statement:

    every non-square simple orthogonal polygon has a convex or straight boundary
    vertex that is not a vertex of its convex hull.

The corrected chain is:

    full source = simply connected two-direction rhombic disk
        -> every boundary vertex is a unit-turn vertex
        -> each convex-hull edge has one of at most eight directions and length < √3
        -> the source hull has bounded perimeter
        -> unit-separated disk packing gives |A| < 30.

The proof uses the positive global contact stress only to force low-degree boundary
vertices to be diameter-loaded; no affine-kernel statement is used.

## 2. Strongest genuinely new result

Classification: audited-working candidate; not canonical.

### Theorem — bounded cardinality of a full-support two-direction disk

Let A be a finite unit-separated source. Suppose:

1. A is the vertex set of a finite edge-to-edge topological disk complex R whose
   bounded faces are unit rhombi;
2. every edge of R is parallel to one of two linearly independent unit vectors
   u and v, and, after choosing their orientations,
   θ = angle(u,v) belongs to (π/3, 2π/3);
3. the unit-contact graph of A is exactly the 1-skeleton of R, so there are no
   retained source points outside the complex and no contact-isolated vertices;
4. there is a KKT equilibrium with strictly positive multiplier on every actual
   unit-contact edge; and
5. every vertex incident to a positive diameter multiplier is a vertex of
   conv(A).

Then

    |A| ≤ 29.

In particular, no unbounded sequence of global minimizers can satisfy all five
hypotheses. For every global minimizer with |A| ≥ 30, at least one of the
following occurs: the source is not a pure simply connected two-direction disk,
some source vertex is not in the complex, some actual contact has zero multiplier
in the chosen stress, or the positive diameter support is not restricted as in
hypothesis 5. The conclusion is a branch exclusion, not a Level-I theorem.

### Scope and normalization

The statement is finite and source-level under its explicit hypotheses. All source
vertices are retained; no scaffold is identified with the source and no isolated
source coordinate is placed in an affine kernel. The KKT equilibrium is an
ordinary equilibrium statement at the source vertices. The theorem does not need
the canonical ZR/ZF theorem, and therefore does not extend its core-only affine
kernel to contact-isolated points.

The angle interval is strict. At an endpoint, a unit rhombus has a unit equilateral
triangle, which is outside the triangle-free branch being audited.

### Proof

Let K = conv(A). Apply the invertible affine map T with T(u) = e₁ and
T(v) = e₂. Affine maps preserve incidence, cyclic boundary order, convexity, and
whether a point is an extreme point of a convex hull. Thus the image of R is a
square complex whose boundary edges are unit horizontal or vertical coordinate
segments.

At a vertex x, every contact vector belongs to

    {u, −u, v, −v}.

If x has no positive diameter multiplier, stationarity and positivity of the
contact multipliers give

    α₊u + α₋(−u) + β₊v + β₋(−v) = 0,

where the coefficient of every present contact direction is strictly positive.
Since u and v are linearly independent, this equation requires
α₊ = α₋ and β₊ = β₋. Consequently a non-loaded vertex must contain both members
of every present opposite pair. In a square disk complex, a boundary vertex has
contact degree two, three, or four according as its local material angle is 90°,
180°, or 270°. A degree-two convex corner has two perpendicular contact vectors
and cannot balance positively; a degree-three straight boundary vertex has one
unpaired inward vector and cannot balance positively. Hence every convex corner
and every straight boundary vertex is loaded.

Hypothesis 5 therefore makes every convex corner and every straight boundary
vertex an extreme point of K. A straight boundary vertex cannot be extreme: it
lies in the relative interior of the segment joining its two boundary neighbors.
Therefore the square-complex boundary has no straight vertex.

For completeness, a reflex boundary vertex has all four coordinate neighbors in
the disk complex and is not an extreme point: it is the midpoint of one of its
opposite neighbor pairs. Thus the vertices of K are exactly the convex boundary
vertices. In particular, no three successive such hull vertices are collinear.

Now orient the boundary counterclockwise and take two successive convex boundary
vertices cᵢ and cᵢ₊₁ in boundary order. Every boundary vertex strictly between
them is reflex, because there are no straight vertices. Let r be the number of
intermediate reflex vertices. In the affine square coordinates, the first boundary
edge after cᵢ has some unit coordinate direction d. At cᵢ the turn is left by
90°, and at each intermediate reflex vertex the turn is right by 90°. If r ≥ 3,
the first four edge directions are

    d, R d, R² d, R³ d,

where R is a clockwise quarter-turn. Their sum is zero, so the simple boundary
returns to cᵢ before reaching cᵢ₊₁, impossible. Hence r is 0, 1, or 2.

If r = 0 or r = 2, the displacement cᵢ₊₁ − cᵢ in the original coordinates is
one of ±u and ±v, and has length 1. If r = 1, it is one of
±(u + v) and ±(u − v), and therefore

    |cᵢ₊₁ − cᵢ| ≤ √(2 + 2|⟨u,v⟩|) < √3.

Thus every edge of the convex hull K has one of at most eight oriented directions

    ±u, ±v, ±(u + v), ±(u − v)

and length at most √3. The hull K is strictly convex at its vertices, so its
oriented edge directions turn strictly monotonically around the circle; an
oriented direction cannot occur twice. Therefore K has at most eight edges and

    P(K) ≤ 8√3.

The isoperimetric inequality gives

    area(K) ≤ P(K)²/(4π) ≤ 48/π.

The open radius-1/2 disks centred at the points of A are pairwise disjoint and lie
in K + B(0,1/2). Steiner's parallel-body formula for a convex planar set gives

    |A| π/4 ≤ area(K) + P(K)/2 + π/4.

Using the preceding bounds,

    |A| ≤ 192/π² + 16√3/π + 1
        = 29.274929586… < 30.

The final strict sign can be certified without the displayed decimal. The standard
elementary bounds π > 31415/10000 and √3 < 1733/1000 give

    192/π² + 16√3/π + 1
      < 192/(31415/10000)²
        + 16(1733/1000)/(31415/10000) + 1
      = 30 − 28376533/39476089
      < 30.

Since |A| is an integer, |A| ≤ 29. This proves the theorem.

## 3. Exact frontier effect

The result excludes the pure fixed-direction/full-source branch at cardinality
|A| ≥ 30, even when the rhombus angle tends to the triangle endpoint. It does
not require a fixed angular gap. This is stronger than the earlier unreviewed
candidate's intended conclusion for that branch, but it has a materially narrower
and corrected geometric hypothesis boundary.

The exact C-II effect is:

    full-source, simply connected, two-direction, full-positive-contact disk
        -> |A| ≤ 29

The canonical state does not change. The current C-II theorem stack still permits
piecewise phases, holes, exceptional faces, bridges/corridors, contact-isolated
points, and a carrier that is only a subsource. Any surviving near-rhombic source
must evade this branch through one of those mechanisms or through a failure of the
full-support stress hypothesis.

## 4. Exact remaining lemma

A useful next source-level target is the stability analogue:

> If a Type-II full-core source has o(D) exceptional boundary occurrences and
> o(D²) non-rhombic faces, prove that the remaining phase/interface structure
> either contains a pure two-direction subdisk whose boundary low-degree vertices
> are globally diametral, or directly supplies the Section-122/123 detour
> contradiction or a finite source-preserving strict descent.

The present theorem does not claim that a subdisk can be treated as the full source;
the source/scaffold distinction and retained contact-isolated points remain binding.

## 5. Claim audit table

| Claim | Status | Dependencies | Reason |
| --- | --- | --- | --- |
| Positive contact equilibrium at an unloaded vertex | proved in this report | two independent directions; positive contact multipliers | Opposite-direction coefficients must match |
| Convex/straight low-degree boundary vertices are loaded | proved in this report | preceding equilibrium; disk-complex local degrees | Their contact vectors cannot positively balance |
| Straight boundary vertices are non-extreme | proved in this report | two boundary neighbors in the source | The vertex lies between those neighbors |
| No straight boundary vertex | proved in this report | loaded-to-hull support hypothesis | Loaded points are hull extremes |
| At most two reflex vertices between successive convex vertices | proved in this report | unit square-coordinate boundary; no straight turns | Three right turns return after four unit edges |
| At most eight hull directions | proved in this report | preceding turn count; strict convex hull | The displacement set has eight elements at most |
| |A| ≤ 29 | proved in this report | isoperimetry, Steiner parallel-body formula | Exact numerical bound |
| Earlier orthogonal-boundary lemma | rejected | none | The L-shaped polygon below is a counterexample |
| Every C-II full-core source satisfies hypotheses 1–5 | unresolved | canonical C-II stack | Current route permits holes, interfaces, carriers, and isolates |
| Level I | open | original quantifiers | This is only a conditional branch exclusion |

## 6. Regression checks

| Regression/correction | Result | Exact hypothesis or failure |
| --- | --- | --- |
| L-shaped orthogonal polygon | fails the old lemma | Vertices (0,0), (3,0), (3,1), (1,1), (1,3), (0,3) have a reflex corner, but every convex vertex is a vertex of the convex hull; the old “reflex implies hidden convex vertex” assertion is false |
| Straight boundary point on a long square-complex side | excluded by the repaired proof | It lies between two source neighbors, so it cannot be a hull extreme, while positive equilibrium makes it loaded |
| Five-cell plus-shaped square complex | retained | It shows the repaired theorem does not incorrectly force a single square; the bounded-cardinality argument allows small non-square examples |
| Vanishing-shear two-direction lattice disk | outside the theorem | Its staircase/long boundary contains non-hull low-degree boundary vertices and is not a full-support source satisfying hypothesis 5 |
| Holes and exceptional faces | outside the theorem | Hypothesis 1 is intentionally a topological disk of rhombi |
| Contact-isolated source points | outside the theorem | Hypothesis 3 explicitly makes the complex the entire source |
| Positive stress on a selected carrier | insufficient | The theorem requires the full source and positive contact support; a scaffold cannot be substituted |
| Global optimality versus local stress | retained | The theorem uses a global KKT equilibrium only as an explicit premise and makes no claim that local stress alone solves C-II |
| ZR/ZF affine-kernel scope | respected | No affine kernel is asserted for any omitted or isolated source coordinate |

## 7. Literature imports

No external theorem is imported. The only geometric ingredients beyond the stated
KKT equilibrium are elementary affine geometry, the planar isoperimetric inequality,
and the standard Steiner parallel-body formula; their hypotheses are stated in the
proof. The official problem page was checked only for status and is not a proof
dependency.

## 8. Computation

No computation is logically required. During the audit, small inline enumeration of
unit-cell polyominoes was used only as a diagnostic sanity check; it was not
load-bearing, no numerical output is used in the proof, and no script certificate is
claimed. The exact counterexample to the old orthogonal lemma and the bound above
are analytic.

## 9. Corrections / supersessions

This report corrects the unreviewed candidate
docs/reports/target_c_two_direction_diametral_boundary_nogo_2026-09-14.md.
Its theorem-level orthogonal-boundary lemma is rejected as stated. The repaired
report does not use that lemma and proves the weaker but rigorous conclusion
|A| ≤ 29 under the same full-source/two-direction/full-support setting, with an
explicit source-level hypothesis boundary. The old report remains unreviewed and
should not be promoted. No canonical theorem depends on it.

## 10. Promotion recommendation

Audited-working

The proof and its hypothesis audit are complete, but this is still a conditional
branch theorem and not a canonical C-II closure. Independent review should check the
KKT sign convention used for “loaded,” the boundary degree classification for the
chosen edge-to-edge disk-complex definition, and the parallel-body estimate. No
state-version, route-map, prompt, or canonical dependency change is made here.

## 11. Handoff

1. Strongest new theorem: a full-support, simply connected two-direction
   triangle-free rhombic source has |A| ≤ 29.
2. Canonical dependency chain: elementary KKT equilibrium plus the elementary
   diameter-endpoint support fact; no ZR/ZF extension and no source deletion.
3. Exact remaining lemma: promote the bounded-boundary argument to a
   phase/interface stability theorem for the actual full Type-II source, or pay the
   canonical aggregate detour through a source-preserving deformation.
4. Binding dead routes: the old orthogonal-boundary lemma, carrier/source
   identification, deletion of isolates, and local stress without global source
   hypotheses.
5. Files to read next: docs/targets/target-c/CURRENT.md, canonical Sections
   79–85 and 122–123, plus the full-core phase/interface modules.
