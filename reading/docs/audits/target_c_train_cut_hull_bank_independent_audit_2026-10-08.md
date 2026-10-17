> Generated reading edition · [exact source](../../../docs/audits/target_c_train_cut_hull_bank_independent_audit_2026-10-08.md) · source SHA-256 `40a9e1faceb5b5519e8652a4741b61874d2acdbe8bcec0d4f95fce453016851e`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-1A28930623FE","canonical":true,"claim_ids":["C-QUADRATIC-CORE-TRAIN-BANK","C-TRAIN-CUT-HULL-BANK"],"claim_statuses":{"C-QUADRATIC-CORE-TRAIN-BANK":"canonical","C-TRAIN-CUT-HULL-BANK":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C Audit.179 — cut-to-hull train banks and their contact carrier

Date: 2026-10-08
Audit base: `origin/main=0160694f8c27f0e8456c327bb5351794e778efd9`, state `2026-10-08.audit.174`
Frozen source: `origin/research/level-i-closure-20261007` at `12f6833725f281ce39a6d04ebcb45630b3a6768f`; the audited report was introduced at `cc7d4ea58be2dd3b45131e9f03e757af35bdbcd1`.
Classification: independent reconstruction; **PASS — promote the exact finite theorem and its quadratic-core corollary**.
Scope: source report Sections 1–5 only. Section 6 was checked for verifier scope. Section 7's separator and disjoint-return claims are not audited here.

Frozen source hashes:

- Candidate report: `15e2530cbae69f6c43cf0d8dea664e626ded9ce80b216dbf9d1c98de9d58e9`.
- Finite verifier: `fa8e9b25abf7949c61cc77a4ff27e9ee9e486442a885a57ee52a5d3aab86a9c0`.

## Exact promoted statements

Take a canonical contact-minimal, then actual-diameter-pair-minimal triangle-free full-source C-II minimizer in the Section-57 mixed-rigidity regime, with `D>=9`. Retain every source label, including all contact isolates, and form trains only in the actual positive-contact core after force-hull augmentation. Let `R4` be the number of actual bounded strict unit rhombi. Let `T` consist of every complete physical rhombus track and each actual contact edge incident to no rhombus as one singleton train; `d_tau` is the number of rhombi on train `tau`.

Make a recipient graph whose bounded nodes are the original physical bounded nonquadrilateral faces and whose outer nodes are occurrence-counted outer hull chains. The two terminal occurrences of each complete train determine its two endpoints. For any selected train family `A`, put `N=T\setminus A`; let `B(A)` be the selected trains with at least one terminal in an `N`-component that reaches an outer hull chain. Then

```math
|B(A)|\ge |A|/3,
\qquad
|B(A)|\ge {2\over3}\sqrt{[R4-\sum_{\tau\in N}d_\tau]_+}.
```

Every bank train has a terminal source vertex joined by actual unit contacts to an actual loaded vertex. The union `K_N` of the complementary train rails, the bounded nonquadrilateral facial walks in boundary-reaching `N`-components, and the old outer contact walk is an actual contact subgraph satisfying

```math
|E(K_N)|\le \sum_{\tau\in N}d_\tau+2T.
```

The second promoted claim is the asymptotic corollary. Along any unbounded sequence of these canonical sources with `R4/D^2 -> r>0`, for every fixed `0<epsilon<r`, the family `A_L={tau:d_tau>=L}`, `L=floor(epsilon D/(3 pi))`, has

```math
|B(A_L)|\ge \left({2\over3}\sqrt{r-\epsilon}-o(1)\right)D,
```

each selected train's two terminal-edge midpoints are separated by at least `sqrt(3) epsilon D/(6 pi)-O(1)`, and its carrier has at most `epsilon D^2+6 pi D` edges. A slow choice `epsilon_D -> 0` with `epsilon_D D -> infinity` gives `|B| >= (2/3 sqrt(r)-o(1))D`, divergent terminal-midpoint separation, and an `o(D^2)` carrier. This result does not give disjoint routes or a bound on any individual return length.

## Canonical dependencies and object checks

- `C-RECIPROCAL-TRAIN-GRAPH` applies to every bounded endpoint subset of the canonical augmented internal stopped-train graph. It includes all hull pockets and singleton bridge trains; the induced graph on each nontrivial component is `(2,3)`-sparse and has no loops or repeated bounded endpoint pairs.
- `C-LOADED-HULL` supplies the occurrence-counted old outer contact walk, loaded hull endpoints, `b+Q=2(q-k)`, `k>=0`, and `q<=p<=pi D`.
- Theory 01, Lemma 10.1 and Theorems 10.6 and 10.8 supply strict physical rhombi, complete simple tracks, the simple triangle-free crossing graph, and transverse progress at least `sin(theta)>=sqrt(3)/2` per rhombus.

All original source points remain present. The train and carrier constructions use only actual contacts. Auxiliary hull sides are not treated as source paths. The theorem applies reciprocal sparsity only to original bounded physical nonquadrilateral faces; augmentation pockets remain present in the canonical reciprocal theorem but are not incorrectly substituted for those physical recipients. Every face-side and outer-walk occurrence, including bridge repetitions, is counted with multiplicity.

## Independent reconstruction

Let `I` be the union of bounded-face nodes whose `N`-component does not reach an outer chain. Put `f_I=|I|` and `Q_I=sum_{F in I}(deg(F)-4)>=f_I`. Let `E_I` count all complete trains with both ends in `I`; let `X_I` count those with exactly one end in `I`. Counting terminal occurrences on physical bounded nonquadrilateral faces gives

```math
4f_I+Q_I=2E_I+X_I.
```

For each singleton component of the induced internal train graph on `I`, reciprocal sparsity gives zero internal edges; for each nontrivial component `U_j`, it gives at most `2|U_j|-3`. Thus, with `sigma_I=2` per singleton and `3` per nontrivial component,

```math
E_I\le2f_I-\sigma_I,
\qquad
X_I\ge Q_I+2\sigma_I\ge f_I+2\sigma_I.
```

An `N`-train cannot leave the union `I`: it would join its interior component to an outer-reaching component, contradicting the definition of `I`. Hence every cut train is selected and is counted by `B(A)`, so `X_I<=|B(A)|`. A selected train outside `B(A)` has both endpoints in `I`; writing its count as `A_I` and the internal complementary count as `N_I`, one has `|A|=|B(A)|+A_I` and `A_I+N_I=E_I`. The displayed bounds yield

```math
|A|+N_I+5\sigma_I
=|B(A)|+E_I+5\sigma_I
\le3|B(A)|.
```

This proves the one-third bound, including the empty-interior case. It does not infer a bank from a terminal-occurrence count; it counts distinct trains throughout.

For a track, orient its common unit vector and choose the same low-coordinate endpoint on each opposite terminal edge. Across each strict unit rhombus these chosen vertices are joined by one of its other unit sides. Chaining those sides gives a literal contact rail of `d_tau` edges. A singleton train's two chosen terminal vertices coincide. A complete bounded facial walk joins all terminal vertices incident to that face; the old outer contact walk connects its occurrence chains to actual loaded vertices. Therefore the stated union is an actual contact carrier. If `f` and `Q` count the bounded nonquadrilateral faces and their total degree excess, then the exact occurrence handshake `2T=b+4f+Q` bounds its non-rail part:

```math
b+\sum_{F\text{ in boundary-reaching }I}\deg(F)
\le b+4f+Q=2T.
```

The bound counts carrier edges once even when many returns reuse a bottleneck. It gives no disjointness or individual path-length estimate.

For the square-root bound, the rhombus crossing graph has `R4` edges. Removing the vertices `N` deletes at most `sum_N d_tau` crossing edges; the remaining graph on `A` is triangle-free and hence has at most `|A|^2/4` edges by Mantel. Thus `R4<=sum_N d_tau+|A|^2/4`; combine this with `|A|<=3|B(A)|`.

For the asymptotic corollary, the occurrence identities give `T=q-k+2f`. Since `f<=Q`, `b>=q`, and `b+Q=2(q-k)`, one has `Q<=q-2k<=q`, so `T<=3q<=3 pi D`. With `L=floor(epsilon D/(3 pi))`, `sum_{N_L}d_tau<=LT<=epsilon D^2`; substitute in the square-root bound. The terminal-midpoint separation follows by summing `sin(theta)>=sqrt(3)/2` across each selected train. Taking `epsilon_D` to zero sufficiently slowly establishes the final diagonal form.

## Hostile checks and verifier boundary

- Disconnected rhombus complexes and holes are allowed by Theorem 10.6; no disk assumption is used.
- Bridge edges and repeated outer-face occurrences are retained in the terminal handshake.
- Contact-isolated source labels remain in the global source; they are not put into the core graph or silently discarded from source optimality.
- The carrier may have shared edges, repeated vertices across routes, and bottlenecks. No simultaneous movement or independent return currency is inferred.
- `A=empty`, `I=empty`, singleton components, tracks with two endpoints at one recipient, and long or overlapping face walks do not invalidate the inequalities; internal bounded-endpoint loops are excluded by the canonical reciprocal theorem.
- The frozen exact-rational verifier passed: 10 nonglobal fixtures; 13,259 source lower-pair checks; 164 physical train rails; 506 selections; reciprocal antecedent passed in 459 and failed in 47; 4,714 bank-end contact returns; 8,906 unit steps; 27 long-terminal flow checks; and 113 vertex-disjoint full-contact returns. Its 24 failures of the pinned-count antecedent are explicitly counted. It verifies finite conditional ledgers and paths only: fixture roots are not certified diameter-loaded, and the code does not verify KKT, global optimality, the asymptotic argument, or Level I.
- No numerical output is used as a proof of the analytic statements. The report's Section 7 claims about endpoint-inclusive separators and disjoint returns are outside this audit and remain unreviewed.

## Verdict and frontier effect

**PASS — promote `C-TRAIN-CUT-HULL-BANK` and `C-QUADRATIC-CORE-TRAIN-BANK`.** The exact finite theorem creates a hull-reaching bank and one common actual-contact carrier for any selected family. Its quadratic-core corollary gives a linear bank of long trains inside a subquadratic-edge carrier. It does not supply a motion, mutually disjoint returns, per-return length, a strict diameter improvement, or a Level I consequence. Target C-II and Level I remain open; the active finite-move/payment obligation is unchanged.
