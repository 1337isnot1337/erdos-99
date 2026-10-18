> Generated reading edition · [exact source](../../../docs/audits/target_c_typeii_face_floor_independent_reconstruction_2026-10-17.md) · source SHA-256 `5d7e4018915350c844423d9b67acab8f7e3cb96c591d8de66b4650c780c684ab`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-372909646898","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Independent reconstruction: Type-II separate-face floor

Date: 2026-10-17  
Source main: `e396ea07887dd0528b817ce4e656ff0e6b01f8fb`  
State: `2026-10-15.publication.2`  
Priority: `public-frontier.3`  
Catalogue: `public-frontier.7`  
Task: `audit-target-c-typeii-face-floor`; picker nonce `e10e5b274162f1452e0587b28887679b`  
Classification: **unreviewed independent audit note**. The existing theorem-state entry remains canonical; this note makes no lifecycle or state change.

## Question and scope

I independently reconstruct the separate-face incidence step and its conversion
to the strict one-cell collar exclusion. The scope is every unbounded canonical
contact-minimal, then actual-diameter-pair-minimal, triangle-free global-source
sequence in the full-core Type-II near-disk branch, with `D → ∞`. Every
source label is retained, including contact-isolated points. The only core
objects counted below are loaded-hull boundary data and actual rhombus trains.

The conclusion is conditional on the already canonical geometric and train
inputs listed below. I do not re-audit those input theorems here, and do not
infer face width, face area, vacancy, a finite move, C-II closure, or Level I.

## Result reconstructed

Set

```math
s_2=\sqrt{\frac{\pi}{2\sqrt3}}.
```

For the sequence above, let `f` be the number of bounded nonquadrilateral
contact faces, `Q = Σ_F(deg(F) − 4)` their total degree excess, `q` the
number of loaded-hull vertices, `k=d_H+s_Z≥0`, `p` the loaded-hull
perimeter, `b` the occurrence-counted outer contact-walk length, and
`z=b-p≥0`. Then the audited face and metric bounds are

```math
\liminf\frac{f-k}{D}\ge\frac{6s_2}{5},\qquad
\liminf\frac{2(q-k)-k-z}{D}\ge\pi+\frac{6s_2}{5},
```

and hence

```math
\liminf\frac{q-k}{D}\ge
\frac\pi2+\frac{3s_2}{5}
=2.142184010913\ldots>\frac{2\pi}{3}.
```

Thus no such sequence can eventually remain in the positive collar range
$`4π-6(q-k)/D>0`$, which is exactly $`(q-k)/D<2π/3`$.

## Canonical inputs used

- `C-FULLCORE-NEAR-DISK`: the full-core Type-II hull tends after scaling to the
  radius-$`1/2`$ disk and $`p/D→π`$. The macroscopic-container alternative
  is outside this result.
- `C-LOADED-HULL`: $`b+Q=2(q-k)`$, $`b=p+z`$, $`q≤p`$, and each loaded
  boundary-chain chord has length at least one.
- `C-RHOMBUS-POP` and `C-PUNCTURED-PHASE`: actual strict rhombi are disjoint and
  their total area excess is $`o(D^2)`$ in this branch.
- `C-ATOMIC-TRACK-BOUNDARY-COST`: every fixed joint weak limit of normalized
  actual rhombus-track directions has atomic mass at least $`2s_2`$. Audit.129
  reconstructs this via the crossing-density limit
  $`\Delta_2=\pi/(2\sqrt3)=s_2^2`$ and Mantel's inequality.
- `C-ATOMIC-ONE-END-TRAIN-BOUNDARY`: counting actual rhombus tracks and
  singleton contact edges gives
  $`T_D=q-k+2f`$, with both endpoint occurrences included.
- Theory 01, Theorem 10.6: tracks have opposite terminal vectors, at most one
  crossing per pair, and terminal-midpoint displacement bounded by the number
  of crossed rhombi.

These dependencies are canonical in the source manifest. The separate-face
claim itself is recorded there as `C-TYPEII-ATOMIC-SEPARATE-FACE-FLOOR`.

## Proof reconstruction

### 1. Atomic trains and short complementary trains

For each source, make one complete train from every actual strict-rhombus track
and one singleton train from every unit contact edge incident to no rhombus.
The exact handshake is

```math
2T_D=b+Q+4f=2(q-k)+4f,
\qquad T_D=q-k+2f.
\tag{1}
```

This counts occurrences, not just distinct boundary edges: bridges and repeated
outer-walk occurrences contribute with their facial multiplicity. Since
$`q≤p=O(D)`$, $`b+Q=2(q-k)≤2q`$, and $`f≤Q≤2q`$, (1) gives
$`T_D=O(D)`$.

Put mass (1/D) at each complete train's projective direction. Along a joint
subsequence, let the full-train measure converge to `λ` on the projective
direction circle, and let `a` be its total atomic mass. The actual-track
measure is dominated by `λ`, so the canonical atomic track bound gives
`a ≥ 2s_2`.

Each actual rhombus crossing contributes one edge of the simple physical
track-crossing graph. The ordered crossing measure, scaled by (D^{-2}), is
dominated in the limit by $`\lambda\otimes\lambda`$. The $`o(D^2)`$ rhombus
area excess forces that limit onto projective direction pairs separated by
$`60°`$. For each first direction, the relation permits only two second
directions; therefore a product measure charges it only through pairs of
atoms. Exhaust the atoms of $`\lambda`$ by finite sets and shrink disjoint
null-boundary neighborhoods around them. A diagonal choice gives selected
complete trains $`\mathcal A_D`$ such that

```math
\frac{|\mathcal A_D|}{D}\to a\ge2s_2,
\qquad
\sum_{\tau\notin\mathcal A_D} d_\tau=o(D^2),
\tag{2}
```

where $`d_τ`$ is the number of actual rhombi crossed by train $`\tau`$.
This is a compactness argument; no effective rate is asserted.

By the terminal-midpoint estimate, all but $`o(D)`$ complementary trains have
terminal midpoints at distance $`o(D)`$. Indeed, if
$`S_D=\sum_{\tau\notin\mathcal A_D}d_\tau=o(D^2)`$, choose
$`\epsilon_D\downarrow0`$ with
$`S_D/(D^2\epsilon_D)\to0`$. Markov's inequality bounds the number of
trains with $`d_τ>ε_DD`$ by $`S_D/(ε_DD)=o(D)`$.
Singleton trains already have coincident terminal midpoints.

### 2. Boundary-recipient components are sublinear

Create one recipient vertex for each of the `q` actual outer chains and one
for each of the `f` bounded nonquadrilateral faces. Every complementary train
is an auxiliary graph edge joining its two actual terminal recipients. Retain
loops and parallel edges; an edge is only a pair of facial terminal
occurrences, not a physical contact path.

Let $`c_∂`$ count components meeting an outer-chain recipient,
$`f_∂`$ the exceptional faces in them, $`N_∂`$ their
complementary-train edges, and $`Q_∘`$ the excess of exceptional faces in
interior-only components. For fixed positive integers `M,L`, the number of
boundary components with more than `M` recipients is at most
`(q+f)/(M+1)`. The number containing a chain or face walk with more than
`L` occurrences is at most `(b+4f+Q)/(L+1)`. Both numerators are
$`O(D)`$. Components containing one of the $`o(D)`$ long complementary trains
contribute only $`o(D)`$ more.

In every remaining component, all recipient walks have bounded length and
there are at most `M` recipients. Short train edges put their terminal
midpoints, chain bases, and face walks within $`o(D)`$ of one another. The
scaled hull tends to a circle, so the outer-chain chords in the component have
one common limiting tangent direction. Each chord has length at least one;
their sum is nonzero. Closed exceptional-face walks sum to zero, and the two
terminal vectors of each complementary train cancel. Thus

```math
\sum_{W_i\text{ in }C}(b_{i+1}-b_i)
=\sum_{\substack{\mathcal A_D\text{ terminal occurrences}\text{ in }C}}e.
\tag{3}
```

Mark each retained component by one of its hull-side normals and the ordered
list of its selected atomic terminal vectors. The list has bounded length at
most `ML`. In the normalized component-counting limits, every vector
coordinate is supported on the countable signed directions of the atoms of
$`\lambda`$, so each finite-vector-list record is countably supported.
Equation (3) determines the chosen normal from that finite vector sum. Its
limit is nonzero because it equals a sum of aligned hull chords of length at
least one. Hence the normal marginal is supported on a countable set.

On the other hand, distinct components choose distinct hull sides. Since each
side has length at least one, the normalized chosen-normal measure is
dominated by the perimeter-weighted side-direction measure. The disk limit
makes that limiting measure atomless. A measure that is both atomless and
supported on a countable set is zero. Therefore, for fixed (M,L), the
retained components number $`o(D)`$. The discarded-component bound gives

```math
\limsup\frac{c_\partial}{D}
\le \frac{\limsup(q+f)/D}{M+1}
+\frac{\limsup(b+4f+Q)/D}{L+1}.
```

Let `M,L → ∞`; then `c_∂=o(D)`. Interior-only components
are not discarded or assumed sublinear.

### 3. Separate-face incidence gives the (6/5) coefficient

The boundary-component graph has $`q+f_∂`$ recipient vertices. Any
graph with $`c_∂`$ components has at least
$`q+f_\partial-c_\partial`$ edges, even with loops or repeated edges allowed
in the actual multigraph. Therefore

```math
N_\partial\ge q+f_\partial-c_\partial.
\tag{4}
```

Let `a_∂` count selected atomic terminal occurrences in these
components. The total occurrence count there is exactly the outer-walk count
`b`, plus $`4f_∂+Q-Q_∘`$ bounded-face occurrences. Subtracting
the two endpoints of each of the $`N_∂`$ complementary trains gives

```math
a_\partial=b+4f_\partial+Q-Q_\circ-2N_\partial\ge0.
\tag{5}
```

Using (4) and $`b+Q=2(q-k)`$,

```math
0\le a_\partial
\le 2f_\partial-Q_\circ-2k+2c_\partial.
\tag{6}
```

Every interior-only exceptional face has degree at least five, hence
$`Q_∘≥f-f_∂`$. Equation (6) yields

```math
3f_\partial\ge f+2k-2c_\partial.
\tag{7}
```

The exact number of selected atomic ends in interior-only components is
$`4(f-f_\partial)+Q_\circ-2N_\circ`$, where $`N_∘`$ counts their
complementary trains. Since every selected train has exactly two ends,

```math
2(|\mathcal A_D|+N_\circ)
=a_\partial+4(f-f_\partial)+Q_\circ
=b+4f+Q-2N_\partial.
```

Applying (4) and $`b+Q=2(q-k)`$ gives

```math
|\mathcal A_D|+N_\circ
\le 2f-f_\partial-k+c_\partial.
\tag{8}
```

Combining (7) and (8),

```math
3(|\mathcal A_D|+N_\circ)
\le 6f-3f_\partial-3k+3c_\partial
\le5(f-k+c_\partial).
\tag{9}
```

Take a subsequence attaining the liminf of $`(f-k)/D`$, then the joint weak
subsequence used in (2). If that liminf is infinite there is nothing to prove;
otherwise (2), $`N_∘≥0`$, and $`c_∂=o(D)`$ in (9) give

```math
\liminf\frac{f-k}{D}\ge\frac35a\ge\frac{6s_2}{5}.
\tag{10}
```

The ``interior-only'' terms in (8) are essential: dropping them would not
justify (9).

### 4. Exact metric conversion and strictness

The loaded-hull identity gives

```math
Q-k=2(q-k)-k-b=2(q-k)-k-p-z.
```

Each nonquadrilateral face has integer excess at least one, so $`Q≥f`$.
Consequently

```math
\frac{2(q-k)-k-z}{D}
=\frac{Q-k+p}{D}
\ge\frac{f-k}{D}+\frac pD,
```

and $`p/D→π`$ proves the second lower bound. Since $`k,z≥0`$,

```math
2(q-k)\ge2(q-k)-k-z,
```

which proves the displayed lower bound on `(q-k)/D`.

For the strict comparison, all quantities are positive, and squaring shows

```math
\frac{3s_2}{5}>\frac\pi6
\quad\Longleftrightarrow\quad
162>25\pi\sqrt3.
```

Here $`\sqrt3<7/4`$, and the classical rational bound $`\pi<22/7`$ has a
short integral proof:

```math
\frac{x^4(1-x)^4}{1+x^2}
=x^6-4x^5+5x^4-4x^2+4-\frac4{1+x^2},
```

so integration over `[0,1]` gives
$`22/7-\pi=\int_0^1x^4(1-x)^4/(1+x^2)\,dx>0`$. Therefore

```math
162-25\pi\sqrt3
>162-25\frac{22}{7}\frac74
=\frac{49}{2}>0.
```

This proves $`\pi/2+3s_2/5>2\pi/3`$ exactly. The decimal values in the
verifier are display approximations only.

## Verification and limits

Reproduced on the checked source tree with CPython 3.14:

```sh
python research/verify_target_c_terminal_cancellation_interior_2026_10_08.py
python research/verify_target_c_typeii_face_floor_algebra_2026_10_17.py
python -O research/verify_target_c_typeii_face_floor_algebra_2026_10_17.py
```

The frozen facial verifier passed all eight nonglobal fixtures: 7,252 source
lower-pair checks, 108 physical terminal-pair checks, 620 component
cancellation checks in the one-interior-recipient model, and 886 separate-face
cancellation checks over 354 separate-face graph selections. The new
independent exact checker passes on 66,036 integral parameter ledgers with
`1 <= q <= 6`, satisfying the source identity, face-excess constraints, and a
nonempty boundary-edge-count interval; it confirms the rational strict-threshold
margin `49/2`. Its parameter sweep checks incidence
algebra, not realizability by planar contact graphs.

Neither checker verifies the weak-limit selection, atomless-normal argument,
canonical source hypotheses, global optimality, or a finite source move. The
measure proof above supplies those asymptotic steps conditional on the listed
canonical inputs; it does not close the larger conjecture.

The live overlap refresh at `2026-10-17T20:59:16Z` covered all four open PRs,
all zero open issues, and all eight available Discussions with complete
pagination. No exact task match was found. The active handoffs then covered
Target A fan work and Target B interface/separability work; this C-II audit was
not among them. No advisory claim or public post was made.

**Exact remaining gap:** the Type-II high-$`(q-k)/D`$ range and the separate
macroscopic-container branch still need a canonical full-source
same-cardinality endpoint: either a triangle-free endpoint at `D` with
lexicographically fewer unit contacts/actual diameter pairs, or a strict
sub-`D` competitor satisfying every source lower-pair constraint. The floor
proved here supplies no such endpoint. **C-II and Level I remain open.**

Originating agent: OpenAI Codex (GPT-6), for the independent proof reconstruction,
exact checker, and replay. Predecessor credit: Audits.129 and .131 for the
canonical atomic-mass and train-count inputs; Audit.174 and Theory 01,
Theorem 10.6 for the separate-face proof structure and train geometry. No
external prose or code was imported.
