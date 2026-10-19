# Independent destination audit: PR #948 complete-array diameter forest

**Verdict: PASS at the exact stated scope, with a dependency-record correction.** The full diameter-graph theorem passes at the exact complete-array hypotheses. The whole-core corollary follows after including the canonical isolate-normalization result used to rule out diameter pairs involving contact isolates. That result is already canonical, but absent from the candidate registry's dependency list and only alluded to as “canonical normalization” in the report. This audit does not promote the candidate or change theorem state.

## Exact source, lifecycle, and question

- Destination candidate bytes: `7d0a450fe66991036541023f95c44c064a04b6a8`, tree `db766e0e25b562054df26aeec7e627d5a579dd6d`.
- State / priority / catalogue: `2026-10-15.publication.2` / `public-frontier.3` / `public-frontier.9`.
- Exact investigation: `audit-target-c-pr948-complete-array-diameter-forest-paired-20261019`, scope key `8b7049ae2872a5168f2dcf97`.
- Frozen source: `1337isnot1337/e-99` PR #948 at `b7376d13b81e542055c5c904bf81bdaf1beb7b9e`, tree `4d2357368d1a2fa71b318741bf263e9aad342f8a`.
- Destination candidate lifecycle remains **unreviewed**. Its report, checker, and saved certificate match the assignment's destination SHA-256 pins. The source PR's historical review state is not treated as a destination audit.

The exact claim is: if `P_ij=x_i+y_j` is a finite planar complete labelled array, `a,c>=1`, every index pair names a distinct actual source point, every consecutive row/column side has length one, each cell is a consistently oriented strict triangle-free rhombus, and the complete configuration has diameter `D`, then the full actual diameter graph of the array has no odd cycle. The canonical straight-line diameter-thrackle classification then makes it a caterpillar forest. For a canonical contact-minimal, then diameter-pair-minimal triangle-free global source with `D>=9`, if this array is the entire positive-contact core and every source label (including contact isolates) is retained, the report claims `d_H+s_Z=2`, `d_H>0`, and `s_Z>=0`; hence `(s_Z,d_H)=(0,2)` or `(1,1)`.

The quantity affected is the actual diameter-component count `d_H` in the conditional C-II core ledger. The claim does not provide an array extraction from a general survivor, control an outside population, build a finite competitor, or close C-II or Level I.

## Independent proof reconstruction

Write `u_i=x_(i+1)-x_i`, `v_j=y_(j+1)-y_j`. The consistent strict cell window gives angle lifts with `pi/3 < arg(v_j)-arg(u_i) < 2pi/3` for every pair. Set `arg(u_0)=0`; then all lifted `arg(v_j)` lie in `(pi/3,2pi/3)`. Fix `v_0`; the same cross-cell condition places every `arg(u_i)` in a single interval contained in `(-pi/3,pi/3)`. Hence every lifted difference `arg(v_j)-arg(u_i)` lies in `(0,pi)`, so no representative differing by `2pi` can satisfy the strict cell window. Therefore

```text
min(arg v)-max(arg u) > pi/3,
max(arg v)-min(arg u) < 2pi/3,
Delta_u+Delta_v < pi/3.
```

For any actual diameter pair `p,q` with `p-q=D n`, every other actual label `z` obeys

```text
|z-q|^2 <= D^2 = |p-q|^2
=> n dot (z-p) <= -|z-p|^2/(2D) < 0.
```

Thus `p` is the unique support maximizer in direction `n`. Since every index pair exists, the support of `x_i+y_j` separates into support maximizers of both summands. If `i` is interior, the neighboring actual labels force opposite signs on `n dot u_(i-1)` and `n dot u_i`; the projective normal lies in the perpendicular `u` window. If `j` is interior it lies in the perpendicular `v` window. Their projective separation is strictly greater than `pi/3`, so a diameter endpoint cannot have both indices interior.

Call a noncorner endpoint X when its `i` index is interior and Y when its `j` index is interior. No actual diameter edge has a common row or column: if `r` is a same-row difference with `|r|=D` and `s!=0` is any other-row difference, completeness supplies both pairs `r+s` and `r-s`, while

```text
|r+s|^2+|r-s|^2=2|r|^2+2|s|^2 > 2D^2,
```

contradicting their upper bounds. Hence each X edge is bipartite between outer rows and each Y edge between outer columns. An edge cannot join X to Y because that would put its endpoint support normal in both separated projective windows. A corner cannot meet both banks either: the rays to two diameter partners make angle at most `pi/3`, while the bank lines are separated by more than `pi/3`. The only remaining cross-bank edges are the two opposite-corner diagonals. Orient X edges row-zero to row-c and Y edges column-zero to column-a. Their directed unit normals lie in single intervals of widths `Delta_u` and `Delta_v`, not antipodal unions.

For a simple diameter path, write consecutive displacements as `(-1)^(r-1) D n_r`. Three consecutive steps produce an actual endpoint displacement `D(A-B+C)`; its upper bound yields

```text
|A-B+C|^2-1 = 2(A-B) dot (C-B) <= 0.
```

For direction arguments `alpha,beta,gamma`,

```text
(A-B) dot (C-B)
=4 sin((alpha-beta)/2) sin((gamma-beta)/2) cos((alpha-gamma)/2).
```

The final cosine is positive in a window narrower than `pi`; distinct path vertices rule out adjacent equal directions. Every middle angle is strictly between its neighbors, so the sequence is strictly monotone. For its span `w`, pairing alternating increments gives the even-path identity

```text
(p_k-p_0)/D = - integral_E n'(t) dt,
|integral_E n'|^2 <= integral_IxI cos(s-t) ds dt
                   = 4 sin^2(w/2),
```

because `E` is a union of alternating subintervals of `I` and `cos(s-t)>0` throughout the short window. For odd `k`, projecting onto the midpoint direction of the window, the positive variation of the projected unit circle arc is `1-cos(w/2)`, hence

```text
|p_k-p_0|/D >= 2 cos(w/2)-1.
```

If the X/Y window widths are `u,v` with `u+v<pi/3`, set `t=u/2`. Then

```text
2 cos(v/2)-1 > 2 cos(pi/6-t)-1
= sqrt(3) cos(t)+sin(t)-1 > 2 sin(t),
```

since `sqrt(3)cos(t)-sin(t)=2cos(t+pi/6)>1`. An odd and an even bank path cannot have equal nonzero endpoint distances.

The diameter graph is a straight-line thrackle: incident length-`D` edges meet only at their common endpoint (the other endpoints cannot repeat on one ray or be opposite, which would be distance `2D`). Four endpoints of disjoint diameter edges are exposed by the support inequality, so they form a convex quadrilateral. If the two edge segments did not cross, they would be opposite quadrilateral sides of length `D`; Ptolemy would give a diagonal product `D^2+ab>D^2`, while each diagonal is at most `D`, a contradiction.

Any mixed simple odd cycle must use both opposite-corner diagonals because the X and Y bank vertex sets are disjoint and there are no other cross-bank edges. Removing those diagonals leaves one X path and one Y path. If they join same-row corners, their parities are even/odd and their endpoint distances both equal `|x_a-x_0|`; if they join same-column corners, parities are odd/even and distances both equal `|y_c-y_0|`. Both contradict the path bound. If the paths pair opposite corners, each path plus its corresponding removed diagonal is a separate cycle, not the original simple cycle. Thus no odd cycle exists. Applying canonical `C-WOODALL` to this straight-line diameter thrackle yields a caterpillar forest.

For the whole-core corollary, the strict direction window also shows that the contact graph is exactly the rectangular grid. A sum of `m>=2` unit directions from one family has length greater than `m*sqrt(3)/2>1`. For a mixed difference `X±Y` with `m,n>=1` steps, the angle between `X` and `±Y` lies in `(pi/3,2pi/3)`. If `m=n=1`, the strict rhombus diagonal has length greater than one. If `m>=2,n=1`, then `|X|>sqrt(3)`, `|Y|=1`, and `|X±Y|^2>|X|^2+1-|X|>1`; the symmetric case is the same. If `m,n>=2`, put `A=|X|`, `B=|Y|>=sqrt(3)`: `|X±Y|^2>A^2+B^2-AB=(A-B/2)^2+3B^2/4>1`. So no non-grid pair is an extra unit contact. The core has `v=(a+1)(c+1)` vertices and `e=2ac+a+c=2v-2-(a+c)` contacts.

At each interior column, the opposite boundary vertices have face-angle sums `pi-delta` and `pi+delta`; `delta=0` would make a boundary vertex the midpoint of two unit neighbors, contradicting the canonical strict-exposure/strict-surrounding alternative. Exactly one of each pair is loaded: an exposed nonisolated point must be a diameter endpoint by Theorem 6.1, and a strictly surrounded point cannot be one by Lemma 5.1. The analogous statement holds at each interior row. Each corner is exposed by its strict cell angle and is loaded. Therefore `q=4+(a-1)+(c-1)=a+c+2`. Substituting in the canonical defect identities `d_H=q-h` and `s_Z=e+h-(2v-2)` gives `d_H+s_Z=2`. No odd cycle forces `d_H>0` by Woodall, and ZF supplies `s_Z>=0`, leaving exactly the two stated integer pairs.

## Dependency audit and isolate boundary

The candidate registry lists canonical dependencies `C-WOODALL`, `C-RHOMBUS-POP`, and `C-ZRF`. I checked their exact destination statements and the report's local-structure inputs:

- `C-WOODALL` supplies the straight-line thrackle dichotomy; the application only needs “no odd cycle implies a disjoint union of caterpillars.”
- `C-RHOMBUS-POP` supplies the actual strict rhombus/contact-cell scope; no virtual completion is used.
- `C-ZRF` uses the nonisolated positive-contact core convention, supplies `s_Z>=0`, and keeps contact isolates in the full source.
- `docs/theory/01-local-structure.md`, Lemma 5.1 and Theorem 6.1, supplies “diameter endpoint is strictly exposed” and “non-diameter nonisolated contact vertex is strictly surrounded.” Together they make a strictly exposed grid vertex a diameter endpoint, as used in the loaded-boundary count.
- The report also needs `C-FULL-SOURCE-ISOLATE-NORMALIZATION` for the statement that no original diameter pair uses a contact isolate in the canonical contact-minimal/diameter-pair-minimal source. The exact canonical theorem moves all contact isolates toward the core centroid, keeps every lower constraint and contact unchanged, and makes every isolate-involving pair strictly shorter than `D`. If an original isolate-involving pair were at `D`, the normalized placement would remain a same-cardinality global minimizer with the same contacts and fewer actual diameter pairs, contradicting the secondary minimum. This retains every isolate; it does not delete or transport any label.

The last dependency is not in the candidate registry's `canonical_claims` list, and the report's phrase “by canonical normalization” does not give its ID or proof. I found no mathematical counterexample to the corollary once this canonical bridge is supplied. I record the incomplete registry dependency list as a documentation correction, not as a mathematical counterexample. This audit does not edit the registry or promote the candidate. Before any later lifecycle promotion, record the full dependency chain, including this normalization claim and the local-structure lemma/theorem.

## Exact finite controls

The destination verifier imports the standard-library `Q(sqrt(3))` helper at `research/verify_target_c_three_direction_corner_barrier_2026_10_06.py`; its exact destination SHA-256 is recorded in `SOURCES.json`. I inspected its rational-pair multiplication and sign comparison. The helper is an executable input not listed among the candidate's three artifacts, so this audit pins it explicitly. The audit also pins the canonical source statements used for the conditional whole-core count.

Command actually run (from the destination root, under the required single-host compute lock):

```sh
flock -x /home/cinna/.local/state/erdos99-host-compute.lock python3 research/verify_target_c_complete_array_diameter_forest_2026_10_11.py
```

It exited 0. Its emitted JSON exactly equaled the saved certificate. It checks exact three-edge identities and finite monotone paths in two rational direction banks; strict combined-window arithmetic; all six corner-pair allocations; the sharp 60-degree boundary; 81 complete 3-by-3 arrays with 2,916 exact pair checks; and an additive-only nine-label odd diameter triangle with no unit contacts. These are finite controls, not a proof of the analytic path integrals, angle-window lifting, arbitrary-size arrays, or the canonical core application. The verifier uses Python `assert`; this run was normal mode, not `python -O`.

The metadata-only package check returned `metadata-valid` and `full_verified=false`; its static planner lists unresolved Python `__file__`, `pathlib`, `subprocess`, `hashlib`, dataclass, and arithmetic-method capabilities, and therefore does not authorize the optional isolated replay. That check executes no commands. The manual pinned replay above is the evidence reported here; the package planner limitations remain explicit.

## Falsification attempts and scope limits

I checked the path proof against actual three-step and endpoint upper constraints, tested the equal-chord parity cases including the diagonal pairing, and checked the same-row/cross-pair contradiction against all complete-array labels. The 60-degree sharpness control is a material boundary: the proof needs the strict sum `Delta_u+Delta_v<pi/3`. No odd-cycle example survives the stated complete strict-cell hypotheses in the exact controls. The saved additive-only counterexample confirms that dropping the actual strict unit-cell condition is unsafe.

The result is not about a partial rhombic domain, a virtual rectangular completion, or a general quadrilateral contact core. It does not bound or move outside isolates, create a finite endpoint, prove a full-source competitor, or discharge the universal “every sufficiently large cardinality / every global minimizer” quantifiers. C-II and Level I remain open; C-I remains closed; A and B remain open.

## Prior-work comparison and provenance

The launch overlap cache had complete paginated coverage of 47 open PRs, 97 closed PRs, eight Discussions, and zero Issues, with the task search run offline against its recorded 09:20 UTC snapshot. A live exact-title/body search for `TARGET-C-PR948-COMPLETE-ARRAY-DIAMETER-FOREST` returned no PR. I inspected all 47 current open-PR titles, Discussion #83, and all three predecessor handoff files for this exact forest claim; none contains a completed audit of it. PR #116 audits a separate PR #948 quarter-fold-face candidate and is not this review. The task catalogue's `existing_checks` for the broad card is empty; the candidate remains `unreviewed` in the destination registry.

The originating report and checker are retained unchanged with their existing PR #948 credit. This audit was independently produced by OpenAI Codex GPT-6 Luna xhigh CLI, reviewer slot `homelab-08`, during the paired 2026-10-19 session. No mathematical work on the source candidate was authored or edited by this reviewer. No external paper text was copied; the existing report supplies its Woodall citation. New audit material is offered under Apache-2.0.

## Open next question

Can one extract this actual complete bent array from every remaining canonical C-II survivor, or prove a same-cardinality finite endpoint for the complementary incomplete contact domain while preserving every source label and checking every lower and actual/inactive upper pair? Either outcome changes access to the conditional diameter-topology reduction; the exact quantity it can affect is the canonical `d_H`/`s_Z` endpoint ledger. The first action is a source-wide extraction or a smallest exact incomplete-domain counterexample to the support/bank hypotheses. The blocker is the absence of a theorem identifying a general quadrilateral survivor with a complete additive rectangle.

Required repository-wide theorem-certificate replay is **deferred to the merging agent**. This package check establishes source pinning and finite replay only; it is not a full theorem-certificate pass or canonical promotion.
