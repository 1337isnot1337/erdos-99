> Generated reading edition · [exact source](../../../docs/audits/target_c_relative_chord_diameter_direction_independent_audit_2026-10-09.md) · source SHA-256 `b8b00551e589ea5a78192d05db4bbeb62ea682b2c06fd5861df03fd39399e065`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-C370CB46FC24","canonical":true,"claim_ids":["C-ADDITIVE-CHART-RELATIVE-CHORD-BOUND","C-RELATIVE-CHORD-DIAMETER-COUNT","C-RELATIVE-CHORD-GROWING-CHART-EXCLUSION"],"claim_statuses":{"C-ADDITIVE-CHART-RELATIVE-CHORD-BOUND":"canonical","C-RELATIVE-CHORD-DIAMETER-COUNT":"canonical","C-RELATIVE-CHORD-GROWING-CHART-EXCLUSION":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit: relative-chord diameter direction exclusion

Date: 2026-10-09. Integration branch starts at Audit.189 PR head
`7bc09563d8475ac6c2b36af52795a5757ab896f1` (state `.184`). Canonical
dependencies were rechecked against `origin/main=1503e109c53d2ffb0dac6b83fc6cd5d22248bb0f`
(state `.183`). C-II and Level I remain open.

## Frozen source and verdict

- Source branch: `origin/research/level-i-closure-20261007`.
- Immutable source tip: `12f6833725f281ce39a6d04ebcb45630b3a6768f`.
- Source report: [`docs/reports/target_c_relative_chord_diameter_direction_exclusion_2026-10-07.md`](../reports/target_c_relative_chord_diameter_direction_exclusion_2026-10-07.md), SHA-256 `9b57a1ba61569c684f1fc1a79c8b21eee9d2e89b344261ed0d796f6431fec769` (introduced at `3233f49b7755c128454f8df19e97955e45d73304`).
- Exact finite verifier: [`research/verify_target_c_relative_chord_arithmetic_2026_10_07.py`](../../../research/verify_target_c_relative_chord_arithmetic_2026_10_07.py), SHA-256 `7cd002c52facab6173e639d27098a2bf03d2bbcc368f9456a7e2b96aac4a77de`.

**PASS — promote three scoped claims.** The relative-chord arithmetic, finite
diameter-edge count, and growing-chart exclusion are correct. Narrow the finite
count and asymptotic contradiction to the canonical C-II source. The source
report's broader finite wording (“any finite planar unit-separated source”)
uses the canonical diameter-edge and Woodall bounds outside their registered
scope. No universal chart extraction is established, so no C-II frontier
obligation is eliminated.

## Exact claims promoted

### 1. `C-ADDITIVE-CHART-RELATIVE-CHORD-BOUND`

Let `u,v` be unit vectors with invertible `T=[u v]` and
`||T^{-1}||<=K`. Let `U_i=sum_{a<i}u_a`, `V_j=sum_{b<j}v_b`, where all
increments are unit vectors and `|u_a-u|, |v_b-v|<=eta` with
`0<=eta<1/(2 sqrt(2) K)`. A represented physical point has the exact form
`p=c+U_i+V_j`; the represented index set may be any subset of a finite
rectangle. For distinct represented points `p,q`, put `z=(i-k,j-l)` and
`r=p-q`. Then

```text
|r-Tz| <= sqrt(2) eta |z|,
|z| < 2 K |r|,
|r-Tz| <= 2 sqrt(2) K eta |r|.
```

For `|r|<=L`, with `L>=1`, `z` lies among at most
`M_L=(2 floor(2 K L)+1)^2-1` nonzero integer vectors. Its physical chord
direction is within
`delta=asin(2 sqrt(2) K eta)` of `Tz`. Thus all such short-chord directions
lie in at most `M_L` closed angular intervals of width `2 delta`. No bound is
needed on the accumulated positional error `|U_i-i u|` or `|V_j-j v|`.

### 2. `C-RELATIVE-CHORD-DIAMETER-COUNT`

Let `A` be a canonical contact-minimal then actual-diameter-pair-minimal
triangle-free C-II source, `D>=9`, with full actual diameter graph `H`, full
loaded endpoint set `B`, `h=|E(H)|`, and
`B=B_0 disjoint-union E_1 ... disjoint-union E_J`. Each `E_j` consists only
of actual loaded endpoints and has an additive chart as above, with a common
bound `K`, increment error `eta_j`,
`delta_j=asin(2 sqrt(2) K eta_j)`, and
`P_j=per(conv(E_j))`. Let
`delta_D=2 asin(1/(2D))`. For every `L>=1`,

```text
h <= |B_0| + (2/L) sum_j P_j
     + J(2 M_L + 2) + (2 M_L/delta_D) sum_j delta_j.
```

For a segment, `P_j` is twice its length; for a singleton, it is zero.
This is a source theorem: it concerns the complete actual diameter graph,
not a selected stress subgraph, and retains every loaded endpoint in `B_0`.

### 3. `C-RELATIVE-CHORD-GROWING-CHART-EXCLUSION`

On any sequence of canonical C-II sources with `D->infinity`, the hypotheses
of the preceding theorem cannot hold together with

```text
uniform K, |B_0|=o(D), J=o(D), sum_j P_j=O(D), and sum_j delta_j=o(1).
```

For fixed `L`, division by `D` gives
`limsup h/D <= 2 C_P/L`, where `C_P` bounds `sum_j P_j/D`, since
`D delta_D->1`. Sending `L` to infinity gives `h=o(D)`, contradicting the
canonical `C-ZRF` bound `h>=ceil(D)`. The result is conditional on the exact
physical additive charts and the four displayed population/error conditions.

## Independent reconstruction

For `z=(i-k,j-l)`, telescoping gives
`|r-Tz|<=eta(|z_1|+|z_2|)<=sqrt(2)eta|z|`. Since
`|Tz|>=|z|/K`, the strict eta threshold yields
`|r|>|z|/(2K)`. Substitution gives the relative error bound. It is less than
`|r|`, so `r dot Tz>0`; the angle is acute and its sine is at most
`|r-Tz|/|r|`. This proves the claimed angular interval and integer-vector
count without any accumulated-position estimate.

Every actual diameter endpoint is an extreme point of the full source hull:
otherwise strict convexity of squared Euclidean distance, applied to a convex
representation and its diameter partner, contradicts maximality of `D`.
Consequently each `E_j` is a set of vertices of its own convex hull. In a
carrier with at least three points, at most `P_j/L` hull edges have length at
least `L`, and hence at most `2P_j/L` vertices touch a long edge. The outward
normals of every shorter edge lie in the union `W_j` of at most `M_L` arcs of
width `2 delta_j`, obtained by rotating each chord-direction arc by a quarter
turn. A vertex with two short incident edges whose normal cone is
not contained in `W_j` contains a full component of the complement of `W_j`;
the cone interiors are disjoint, so there are at most `M_L` such vertices.
Carriers with fewer than three points contribute at most two additional bad
vertices. Including `B_0`, the total bad endpoint count is at most

```text
|B_0| + (2/L) sum_j P_j + J(M_L+2).
```

At any remaining endpoint `p` of a diameter pair `pq`, let
`n=(p-q)/D`. For every other source point `x`, expansion of
`|x-q|^2<=D^2` gives
`n dot (x-p)<=-|x-p|^2/(2D)<0`; hence `p` is the unique support point in
direction `n`, and `n` belongs to `W_j`. Canonical `C-DB-DENSITY` separates
distinct actual diameter directions projectively by `delta_D`. There is at
most one actual diameter pair in a projective direction: orient both pairs
as `a,a+Dn` and `b,b+Dn`; the two cross-pair upper bounds, added after
squaring, force `a=b`. Thus each projected arc contains at most
`1+2delta_j/delta_D` diameter directions, and all edges with a good endpoint
are bounded by

```text
J M_L + (2 M_L/delta_D) sum_j delta_j.
```

The remaining edges are induced on bad endpoints. Canonical `C-WOODALL`
gives `e_H(S)<=|S|` for every `S subset B`: in the caterpillar-forest case
this holds for every induced subgraph; in the odd-unicyclic-with-pendant-leaves
case an induced subgraph has at most one cycle and otherwise is a forest.
Adding the good- and bad-edge counts proves the finite estimate. This is the
scope correction: the proof uses `C-DB-DENSITY` and `C-WOODALL` on the
canonical C-II source, not on arbitrary unit-separated inputs.

For the asymptotic claim, fix `L` while `D` tends to infinity. The terms
`|B_0|/D`, `J(2M_L+2)/D`, and
`(2M_L/(D delta_D))sum_j delta_j` tend to zero; the perimeter term is at
most `2C_P/L`. Then send `L` to infinity. The lower bound `h>=ceil(D)` is
canonical `C-ZRF`; this contradiction uses the full actual diameter graph.

## Adversarial scope and regression checks

- If represented chart points were arbitrary interior points, the convex-hull
  vertex count would fail. The theorem requires actual diameter endpoints in
  each `E_j`; every other loaded endpoint stays in `B_0` or another chart.
- The finite estimate is stated only for canonical C-II sources, where both
  projective direction separation and the hereditary induced-edge bound are
  authorized. The source report's arbitrary-source wording is not promoted.
- The bent-grid regression has positive absolute lattice-position error but
  increments satisfying the relative hypothesis. It is compatible with this
  theorem and shows why accumulated position is not assumed. Its pins are not
  actual canonical diameter endpoints and it is not globally optimal.
- The source's Type-II near-port grid subsection is already subsumed by
  Audit.173; it receives no duplicate theorem ID.
- No source-level chart extraction is known. Bulk area or coherent-grain
  extraction does not imply an `o(D)` exceptional loaded set or
  `sum delta_j=o(1)`. No move, capacity, payment, strict-D competitor, C-II
  closure, or Level I result follows.

## Exact verifier boundary

I inspected and reran the source's exact `Q(sqrt(3))` verifier on the frozen
commit. It passed 3,640 boundary-pair checks for `M=8,12,16`, checking the
finite bent-grid source pairs, uniform basis conditioning, increment errors,
short-index bounds, and angular sine inequalities. It establishes only those
finite fixture facts. It does not prove the analytic chart lemma, the
normal-cone count, actual diameter loading, canonical chart coverage, or
global optimality. It is therefore not registered as a certificate for the
three promoted analytic claims.

| Claim | Verdict | Canonical disposition |
| --- | --- | --- |
| Exact relative short-chord arithmetic for additive charts | PASS | Promote `C-ADDITIVE-CHART-RELATIVE-CHORD-BOUND` |
| Finite actual diameter-direction count | PASS — SCOPE NARROWED | Promote `C-RELATIVE-CHORD-DIAMETER-COUNT` on canonical C-II sources |
| Growing-chart contradiction | PASS — CONDITIONAL | Promote `C-RELATIVE-CHORD-GROWING-CHART-EXCLUSION`; no chart extraction |
| Universal full-source chart or direction bridge | NOT ESTABLISHED | Leave as the live research obligation |

The frozen discovery branch and its worktree were not modified.
