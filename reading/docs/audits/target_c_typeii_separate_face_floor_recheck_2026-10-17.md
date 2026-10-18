> Generated reading edition · [exact source](../../../docs/audits/target_c_typeii_separate_face_floor_recheck_2026-10-17.md) · source SHA-256 `eed8dcdebe7b4e0e8598709b8d05d015fe89d1eee98de50ae81f0896b7d960b6`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-7CC4C3A1B81E","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C: independent re-check of the Type-II separate-face floor

Date: 2026-10-17  
Source base: `e396ea07887dd0528b817ce4e656ff0e6b01f8fb`  
State: `2026-10-15.publication.2`; priorities: `public-frontier.3`; catalogue: `public-frontier.7`  
Classification: independent coefficient, normalization, and scope re-check; no theorem-state promotion.

## Scope and result

I re-derived the incidence and coefficient steps in Audit.174 for the canonical
claim `C-TYPEII-ATOMIC-SEPARATE-FACE-FLOOR`. I found no coefficient or
normalization discrepancy. The claim gives

```math
\liminf\frac{f-k}{D}\ge\frac{6s_2}{5},\qquad
\liminf\frac{2(q-k)-k-z}{D}\ge\pi+\frac{6s_2}{5},
\qquad s_2=\sqrt{\frac{\pi}{2\sqrt3}},
```

for the stated unbounded, canonical, full-source, full-core Type-II near-disk
sequences. It follows that

```math
\liminf\frac{q-k}{D}\ge \frac\pi2+\frac{3s_2}{5}>\frac{2\pi}{3}.
```

This rules out only the positive one-cell collar subrange. It gives no face
width, face area, finite source move, or conclusion for the macroscopic-container
branch. All contact-isolated source points remain included in the global source
hypotheses and counts.

The live overlap query at 2026-10-17 20:55:15 UTC returned no open PR, Issue,
or Discussion match for `audit-target-c-typeii-face-floor`. The four open PRs at
that query had distinct task handoffs; none requested this coefficient audit.

## Exact claim and inputs

Write `f` for the number of bounded nonquadrilateral contact faces, `Q` for the
sum of their degree excesses `deg(F)-4`, `q` for the number of loaded-hull
vertices, `k=d_H+s_Z>=0`, `p` for loaded-hull perimeter, and `z=b-p>=0` for
occurrence-counted outer-walk excess. The audited canonical inputs give:

1. In the full-core Type-II near-disk branch, `p/D -> pi`, `q<=p`, and the
   full source is retained; this conclusion does not cover the macroscopic
   container alternative.
2. The loaded-hull ledger gives `b+Q=2(q-k)` and `b=p+z`.
3. Every bounded nonquadrilateral face has degree at least five, so `Q>=f`.
4. The rhombus population and punctured-phase inputs give total rhombus area
   excess `E_4=o(D^2)` in this branch. The atomic-track boundary-cost claim
   gives atomic mass at least `2s_2` in every fixed joint weak limit of
   normalized actual-track direction measures.
5. The exact train-boundary handshake gives `T_D=q-k+2f` complete physical
   trains when every strict-rhombus track and each contact edge incident to no
   rhombus is counted. Theory 01, Theorem 10.6 gives simple tracks with at most
   one crossing per pair. Each centerline step across a rhombus has transverse
   displacement `sin(theta)<=1`, so a train's terminal-midpoint separation is
   at most its number of crossed rhombi (the width estimate in Theorem 10.8).

These are used within their manifest scopes. In particular, the argument does
not replace the source by its contact core, a scaffold, or a response network.

## Reconstruction of the face-count step

For each sequence member, let `T_D` be the complete trains above and put mass
`1/D` at each train direction. Since `q<=p=O(D)`, `Q<=2(q-k)<=2q`, and
`f<=Q`, the train count is `O(D)`. The actual-rhombus track measure is
dominated by this full-train measure. Along any joint weakly convergent
subsequence, the full-train limit therefore has atomic mass `a>=2s_2`.

Give each ordered physical crossing mass `D^-2`. At most one rhombus crossing
can use any pair of tracks, so this crossing measure is dominated by the
product of the train measures. For every fixed angular gap above `pi/3`, the
rhombus area excess per such crossing is bounded below by a positive constant;
`E_4=o(D^2)` therefore puts zero limiting crossing mass outside the
projective `60-degree` relation. For a finite measure on the projective
direction circle, the product measure charges that relation only at pairs of
atoms. For an atomic first coordinate, the second coordinate must be one of two
directions and must also be an atom. A diffuse first-coordinate measure can
contribute only on the countable `pi/3` translates of the second-coordinate
atom set, which has diffuse measure zero. Exhausting the atoms and
diagonalizing over shrinking neighborhoods selects complete trains `A_D` with

```math
\frac{|A_D|}{D}\longrightarrow a,\qquad
\sum_{\tau\notin A_D}d_\tau=o(D^2),
```

where `d_tau` counts actual rhombi crossed by `tau`. Put
`r_D=(sum d_tau)/D^2`. When `r_D>0`, choose `epsilon_D=sqrt(r_D)`; when
`r_D=0`, choose `epsilon_D=1/D`. Then `epsilon_D->0` and
`r_D/epsilon_D->0`. Markov's inequality leaves only `o(D)` complementary
trains whose terminal midpoints are farther apart than `epsilon_D D`.

Build a multigraph whose vertices are the actual outer chains between
consecutive loaded-hull vertices and the individual bounded nonquadrilateral
faces. Each complementary train is an edge joining its actual terminal
recipients. Keep loops, parallel edges, and repeated outer-walk occurrences.
Let `c_partial` be the number of connected components meeting an outer-chain
vertex, and `f_partial` the number of exceptional faces in those components.

For fixed cutoffs `M,L`, components with more than `M` recipients are at most
`(q+f)/(M+1)`. Components touching a recipient with more than `L` facial
occurrences are at most `(b+4f+Q)/(L+1)`. Both numerators are `O(D)`; components
containing a long complementary train are `o(D)`. In every remaining component,
the terminal recipients and their boundary occurrences lie in a region of
diameter `o(D)`.

For each such boundary component, sum its outer-chain hull chords. Those chords
have length at least one and their directions approach one common tangent of
the limiting disk, so their sum is nonzero and determines that tangent. The
exact facial-boundary vector identity says this sum equals the sum of the
selected atomic terminal vectors in the component: bounded face boundaries
sum to zero and both ends of each complementary train cancel. At fixed `M,L`
there are at most `ML` terminal vectors per component, each drawn in the limit
from the countable atomic direction set. Therefore the limiting chosen-normal
measure is countably supported.

Each retained component selects a different loaded-hull side. Since every side
has length at least one and the hull divided by `D` tends to a disk, the
chosen-normal counting measure is dominated by the perimeter-weighted
tangent-direction measure, whose limit is atomless. It is both atomless and
countably supported, hence zero. The `O(D/M)+O(D/L)` discard bounds, followed
by `M,L->infinity`, give `c_partial=o(D)`.

Now let `N_partial` count complementary-train edges in boundary components,
`N_circle` those in interior-only components, and `Q_circle` the face excess
of the latter. A connected multigraph on its boundary recipients gives

```math
N_{\partial}\ge q+f_{\partial}-c_{\partial}.
```

If `a_partial` is the number of selected atomic terminal occurrences on
boundary recipients, the exact occurrence count and `b+Q=2(q-k)` give

```math
0\le a_{\partial}
=b+4f_{\partial}+Q-Q_{\circ}-2N_{\partial}
\le 2f_{\partial}-Q_{\circ}-2k+2c_{\partial}.
```

Each interior exceptional face contributes at least one unit to `Q_circle`, so
`Q_circle>=f-f_partial`. Consequently

```math
3f_{\partial}\ge f+2k-2c_{\partial}. \tag{1}
```

Across all recipients, each selected train has two terminal occurrences and
each complementary edge consumes two. Thus

```math
2|A_D|=b+4f+Q-2N_{\partial}-2N_{\circ}.
```

Using the boundary-edge lower bound again yields

```math
|A_D|+N_{\circ}\le2f-f_{\partial}-k+c_{\partial}.
```

Combining with (1),

```math
3(|A_D|+N_{\circ})\le5(f-k+c_{\partial}). \tag{2}
```

Divide (2) by `D`, use `N_circle>=0`, `c_partial=o(D)`, and
`|A_D|/D->a>=2s_2`. This proves
`liminf (f-k)/D >= 6s_2/5`. The proof applies to every fixed subsequential
limit, so the bound holds along the original sequence.

## Coefficient and limit checks

Substituting `b=p+z` into `b+Q=2(q-k)` gives

```math
Q=2(q-k)-p-z.
```

The second numerator decomposes exactly as

```math
2(q-k)-k-z
=p+(f-k)+(Q-f).
```

Since `Q-f>=0`, `p/D->pi`, and the first limit gives
`liminf (f-k)/D>=6s_2/5`, it follows that

```math
\liminf\frac{2(q-k)-k-z}{D}\ge\pi+\frac{6s_2}{5}.
```

As `k,z>=0`, the numerator is at most `2(q-k)`, so

```math
\liminf\frac{q-k}{D}\ge\frac\pi2+\frac{3s_2}{5}.
```

The strict comparison with the collar threshold is exact. Since both sides
are positive,

```math
\frac{3s_2}{5}>\frac\pi6
\Longleftrightarrow 18s_2>5\pi
\Longleftrightarrow 162>25\pi\sqrt3.
```

Using `pi<22/7` and `sqrt(3)<7/4` gives
`25*pi*sqrt(3)<25*(22/7)*(7/4)=275/2<162`. Hence the lower bound is strictly
above `2*pi/3`, excluding exactly the range where `4*pi-6(q-k)/D` is positive.
The exact algebra and rational-bound application replay in
[`verify_target_c_face_floor_coefficients_2026_10_17.py`](../../../research/verify_target_c_face_floor_coefficients_2026_10_17.py).

The original finite facial verifier was also hash-checked against Audit.174:
`research/verify_target_c_terminal_cancellation_interior_2026_10_08.py` has SHA-256
`ec287768485076f01b49ea361e7ae08e71206cc1f46a04658c123db883b5cb9e`. Its
finite fixtures check facial occurrence identities and vector cancellation;
they do not verify the weak-limit argument, global optimality, or the universal
asymptotic quantifiers.

## Verification and remaining gap

Reproduce from the repository root:

```sh
python research/verify_target_c_face_floor_coefficients_2026_10_17.py
python research/verify_target_c_terminal_cancellation_interior_2026_10_08.py
python tools/check_public.py
git diff --check
```

The new verifier checks only exact linear identities and the rational strict
comparison. The frozen verifier checks only its finite geometric fixtures.
Neither establishes the limiting compactness/selection argument; that is
verified here by proof reconstruction against the stated canonical premises.
No theorem-state, route status, or certificate registration is changed.

The exact remaining C-II endpoint is still a source-preserving finite move or
discrete replacement with every source label, lower pair bound, and actual
diameter upper pair checked: at `D`, the endpoint must remain triangle-free and
strictly lower the lexicographic count of unit contacts and actual diameter
pairs, or it must be a same-cardinality strict sub-`D` competitor. The surviving
high-`(q-k)/D` Type-II train/face range and the separate macroscopic-container
branch are still open. This audit does not close Target C-II or Level I.

Predecessor credit: Audit.174 and its cited canonical inputs provide the
original theorem and finite checker. This re-check adds an exact algebra replay
and a separate reconstruction; it claims no new global source theorem.

Originating AI agent: OpenAI Codex (GPT-6), for the proof reconstruction,
verifier, and report. No second audit of this new report is claimed. The source
corpus is offered under the repository's Apache-2.0 contribution terms.
