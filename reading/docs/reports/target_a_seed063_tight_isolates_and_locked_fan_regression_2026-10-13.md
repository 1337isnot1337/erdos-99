> Generated reading edition · [exact source](../../../docs/reports/target_a_seed063_tight_isolates_and_locked_fan_regression_2026-10-13.md) · source SHA-256 `b2f5c112443c57181670aec31d46c38f0d6aacef8318e29473c9a6e72e358337`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-5BF32C3D460F","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-a"} -->
# Target A seed 63: Hall-tight isolates and a fully locked neutral response

**Date:** 2026-10-13

**Seed/category:** 63 / Target A: Schur deficiency and response capacity

**Base commit:** `ab6dd3336f9f8d440f2bada76edb32153391cddc`

**State version:** `2026-10-10.audit.234`

**Run type:** closing-proof attempt with exact regressions

**Claim classification:** proved candidates awaiting independent review; regression

**Artifact lifecycle:** unreviewed; no promotion requested or performed

**Dependencies:** Target A Sections 99, 102, 113, 165, 169, 172, 175, 177;
shared Lemma 21.1 only for the chamber capacity certificate

**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_A_CURRENT_CONTINUATION_PROMPT.md`

**External literature:** not used

**Certificate:** `research/verify_target_a_seed063_tight_isolates.py`

**LEVEL I STATUS: STILL OPEN.**

## 1. Exact attack and scope

The canonical locked endpoint is

$$
\Xi_\Sigma=|O_{\rm iso}|+\sum_i(|O_i|-|C_i|)_+
\ge j_*+|T_Z|.
$$

It implies `h(G)>=j_*`, hence `d_sc>=Delta_Lambda`, and the canonical
global competitor. The zero-slack branch remains a separate obligation.

The first attack was to use global optimality, with a permissible secondary
minimum for the response, to free the reaction vertices from the interior basis.
The resulting chain is

```text
Hall-tight neighbors are strict isolates
  -> every contacted boundary reaction vertex is individually terminal-eligible
  -> [missing simultaneous quantitative sector-surplus theorem]
  -> h(G)>=j_* -> canonical global competitor.
```

Thus the candidate supplies a source-specific matching reduction, not the
missing inequality. The second attack tried to turn full positive stress and
the three-channel fan into sector surplus. Section 4 gives an unbounded,
fully coembedded regression against that reduced-input implication, including
zero lens basis penalty. The third attack tested simultaneous reaction-terminal
selection and the cardinality restoration implicit in a non-tight exchange.
Section 5 identifies an exact global small-case obstruction; a positive Hall
surplus still costs source labels, and this report supplies no refill theorem.

No assertions from open PR #953 are used. Its one-arm source counting is distinct
from the secondary-optimality exchange below. Recent open/merged PRs were inspected
before creating `research/seed-063-sector-response`.

## 2. Candidate: Hall-tight interior exchanges only remove strict isolates

Let `m>=3`, `d=D(m)`, and `D(m+1)>d`. Choose an `m`-point global optimum
`X` minimizing the number of unit-contact pairs among all `m`-point global
optima, then minimizing the number of diameter pairs among those contact minima.
These integer minima exist: the set of attainable finite pair counts is nonempty.
Let `K=conv X`. It is full-dimensional by canonical Lemma 169.0.

The same conclusions hold if the secondary minima are taken among triangle-free
global optima, whenever that class is nonempty: the replacement used below creates
no contacts at all, so it preserves triangle-freeness. No canonical core or matching
from a different representative is silently carried over.

Let `Z` be any finite unit-separated subset of `int K` such that

$$
|z-x|\ne1\qquad(z\in Z,\ x\in X).
\tag{1}
$$

In particular this includes every admissible generic triangular-lattice interior
shore. Write `N(Q)={x in X: |x-z|<1 for some z in Q}` for `Q subseteq Z`.
A **strict isolate** here has neither a unit-contact pair nor a diameter pair
in the complete physical source `X`.

**Theorem 1 (proved candidate).** For every `Q subseteq Z`,

$$
|N(Q)|\ge |Q|.
\tag{2}
$$

If equality holds, every point of `N(Q)` is a strict isolate. Equivalently,

$$
N(Q)\text{ meets an active source pair}
\quad\Longrightarrow\quad |N(Q)|\ge |Q|+1.
\tag{3}
$$

**Proof.** Set `U=N(Q)`. The finite set `(X\U) union Q` is unit-separated:
the two shores are individually separated, and every cross distance is strictly
greater than one by (1) and the definition of `U`. It lies in `K`, so its diameter
is at most `d`. If `|Q|>|U|`, it contains an `(m+1)`-point feasible packing of
diameter at most `d`, contradicting `D(m+1)>d`. This proves (2).

Suppose `|Q|=|U|>0`. Choose any `c in int K` and put

$$
Q_\epsilon=\{c+(1+\epsilon)(z-c):z\in Q\}.
\tag{4}
$$

For all sufficiently small positive `epsilon`, every point of `Q_epsilon`
remains in `int K`, and every cross distance to `X\U` remains strictly above
one. These are finitely many open conditions that hold at `epsilon=0`.
Internal distances in `Q_epsilon` are multiplied by `1+epsilon`, so every
distinct internal pair is strictly above one. This also covers the singleton case.

Every pair with at least one new point is strictly below `d`. Indeed, if
`z in int K`, `x in K`, and `|z-x|=d=diam K`, moving `z` slightly farther
from `x` while staying in `K` would contradict the diameter of `K`.
Thus `X'=(X\U) union Q_epsilon` retains all `m` labels (use any bijection
`U -> Q_epsilon`), satisfies all lower and upper pair constraints, and creates
no unit contacts or diameter pairs incident to a new point. All other source
points, including every retained isolate, stay fixed.

If its diameter were below `d`, global optimality would already be contradicted.
Otherwise it is another `m`-point global optimum. If `U` met a unit contact,
`X'` would have fewer unit contacts. If it met no unit contact but met a diameter
pair, it would have equal contact count and fewer diameter pairs. Either case
contradicts the chosen secondary minima. Hence all of `U` is strict.
The case `Q=emptyset` is immediate. QED.

The construction is finite and simultaneous. It is not an infinitesimal KKT
argument, and it does not require a uniform clearance over different sources.
Strict interior placement and generic cross clearance are indispensable.

## 3. Candidate: isolate coloop block and terminal eligibility

Let `M_Z` be the transversal matroid on `X` defined by conflicts with `Z`.
By (2) there is a matching saturating `Z`, so its rank is `|Z|`.

**Theorem 2 (proved candidate).** Let `T` be the union of all Hall-tight
right sets (`|N(Q)|=|Q|`) and put `U=N(T)`.

1. `|T|=|U|`; every point of `U` is a strict isolate.
2. `U` is exactly the set of coloops of `M_Z`.
3. After contracting this mandatory matching block, every nonempty remaining
   right set `Q subseteq Z\T` satisfies
   `|N(Q)\U|>=|Q|+1`.
4. Every source point incident with a unit or diameter pair can be omitted
   from some `Z`-perfect left basis. If it is a boundary column, it can be
   omitted while retaining a basis of the entire deep restriction.

**Proof.** The function `f(Q)=|N(Q)|-|Q|` is nonnegative and submodular.
The union and intersection of two zero sets therefore have value zero.
Since `Z` is finite, their total union `T` is tight. Theorem 1 proves (1).

Every `Z`-perfect matching must match `T` bijectively to `U`, so every
point of `U` belongs to every left basis. Conversely, if deleting a point
`x` prevents a `Z`-perfect matching, Hall gives a set `Q` with
`|N(Q)\{x}|<|Q|`. Equation (2) then forces `|N(Q)|=|Q|` and
`x in N(Q) subseteq U`. This proves (2).

Hall holds for the remaining graph by restricting a perfect matching.
If a nonempty remaining `Q` were tight there, `T union Q` would be tight
in the original graph, since its neighborhood is exactly
`U union (N(Q)\U)`. This contradicts maximality of `T`, proving (3).

An active point is outside `U` and hence is not a coloop. Deleting it
preserves full rank. For a boundary column `x`, the deep restriction is
unchanged upon deleting `x`; choose its basis and extend it to a full
basis in `X\{x}`. This is exactly the permitted deep-first normalization.
QED.

**Exact Schur consequence.** This contraction does not alter `S`. Order rows
as `T,Z\T` and any allowed basis as `U,B\U`. The interior basis matrix is

$$
\begin{pmatrix} A[T,U]&0\\ A[Z\setminus T,U]&A[Z\setminus T,B\setminus U]
\end{pmatrix}.
$$

The upper block is invertible and `A[T,C]=0`, so elimination of nonbasis
columns gives zero coefficients on `U`. The Schur formula is exactly the
formula on the remaining graph, even if `U` has exterior conflict neighbors.
The deep nonbasis count and terminal set are unchanged. This is an algebraic
contraction only: no physical source isolate is dropped, and neither `m`
nor `j_*` is redefined using a reduced cardinality.

For a locked response obtained with this choice of `X`, every positive-contact
reaction vertex is individually eligible to be a Schur terminal. This removes
the possibility that such a vertex is forced into every interior basis.
It does not establish simultaneous eligibility for a prescribed reaction set,
Schur nullity, or the sector-surplus endpoint.

## 4. Exact regression: a saturated, fully locked fan with neutral Schur response

Use `e1=(1,0)`, `e2=(1/2,sqrt(3)/2)` and squared norm
`q(a,b)=a^2+ab+b^2`. For every integer `M>=4`, let

$$
X_M=\{i e_1+j e_2:i,j\ge0,\ i+j\le M\},\qquad K_M=\operatorname{conv}X_M.
\tag{5}
$$

Its cardinality is `n_M=(M+1)(M+2)/2`, separation is one, and diameter is `M`.
The convex hull is an equilateral triangle of side `M`. Oler gives

$$
\alpha_1(K_M)\le M^2/2+3M/2+1=n_M,
$$

so this is **exact fixed-container capacity**, including strict insertion
saturation. It is not a global diameter certificate.

**Full stress and lock.** Assign weight one to every unit contact. At an
interior vertex the six neighbor vectors sum to zero. At an open hull side
their outward force is `sqrt(3)` times its outward unit normal; at a corner
it is `sqrt(3)` times the sum of the two outward unit normals. Thus there
is positive contact stress and nonnegative actual hull-facet reaction.
For a feasible fixed-hull velocity, contact virtual work is nonnegative
while facet virtual work is nonpositive. Equality forces every contact
derivative to vanish. Adjacent elementary triangles share edges, so their
infinitesimal rigid motions agree throughout the patch. The two active
facet normals at each corner force zero corner velocity, so the entire
fixed-hull feasible cone is zero. This is a fully locked packing with
mixed contact/facet rank `2n_M`.

The interior unit triangle `(1,1),(2,1),(1,2)` has these disjoint positive
contact channels to three distinct actual reaction vertices:

- `(1,1) -> (0,1)`;
- `(2,1) -> (2,0)`;
- `(1,2) -> (1,3) -> ... -> (1,M-1)`.

Their union with the triangle is a unicyclic fan with `M+2` vertices and
edges. Thus it realizes the Section-172/173 geometry on the same points
as the actual lattice response.

**Zero left deficiency for every translation of the aligned lattice.** For
every phase of the same triangular lattice, choose a lattice displacement
`u` of norm at most `1/sqrt(3)` representing that phase. The map
`x -> x+u` is an injective strict conflict matching into `K_M+B(0,1)`.
Consequently `nu(G)=n_M`. Fixed-container capacity supplies the
`Z`-perfect matching as above. Deep columns are independent under the
same injection, so

$$
d_{\rm int}=d_{\rm sc}=\zeta=0,
\qquad \operatorname{rank}S=n_M-|Z|
\tag{6}
$$

for every admissible generic translation at this orientation. Rotation of
the response lattice is not asserted.

**An explicit generic phase with zero fan basis penalty and zero coarse Hall
deficiency.** Put `v=(1/5)e1+(1/7)e2`. Each source `(i,j)` has exactly the
three strict lattice neighbors

$$
(i,j)+v,\quad(i-1,j)+v,\quad(i,j-1)+v.
\tag{7}
$$

Indeed the three squared distances are `109/1225,669/1225,739/1225`;
all other lattice displacements have squared norm above one. Hull and
unit-distance equalities do not occur.

For the exclusion of other neighbors, `|v|<1/3`; every nonzero triangular-
lattice displacement outside the six unit directions has length at least
`sqrt(3)` because `a^2+ab+b^2` is never two. Its phase-shifted length is
therefore above `sqrt(3)-1/3>1`. Checking the six unit directions and zero
gives exactly (7). The phase's two coordinates and their sum are nonintegers,
so no lattice row is on a hull facet.

In particular,

$$
Z=\{(i,j)+v:i,j\ge0,\ i+j\le M-1\},\quad |Z|=M(M+1)/2.
$$

Start with the basis `B0={(i,j):i+j<=M-1}` matched to identical row
coordinates. Delete `(0,1),(2,0)` from the basis and add the two top-side
vertices `(2,M-2),(M-1,1)`. Match the following rows differently, leaving
all other rows matched to their identical source coordinates:

$$
\begin{array}{ll}
(0,1)\mapsto(1,1), &(2,0)\mapsto(2,1),\\
(1,j)\mapsto(1,j+1)&(1\le j\le M-3),\\
(1,M-2)\mapsto(2,M-2),&\\
(i,1)\mapsto(i+1,1)&(2\le i\le M-2).
\end{array}
\tag{8}
$$

These are distinct valid matched neighbors by (7). All deep columns
remain in the basis. All three channel endpoints are nonbasis boundary
terminals. The fan's lens rows are exactly

$$
L_\Sigma=\{(1,1),(0,1),(2,0)\}\cup\{(1,j):2\le j\le M-2\}+v.
\tag{9}
$$

They are interior rows, and `|L_Sigma|=M`. Every basis fan vertex is
matched to one of them by (8), so `beta_Sigma=0`.

Every surviving terminal is a top-side vertex distinct from the three
shield terminals. It has its direct conflict edge to the distinct
exterior sink `(i,j)+v`. None of these edges touches the shield or its
contracted lens pairs. They give a matching saturating the entire left
shore of the coarse sector graph. Hence

$$
\boxed{\beta_\Sigma=0,\qquad\delta_\Sigma^{\rm lens}=0,\qquad\zeta=0.}
\tag{10}
$$

Thus even exact saturation, full positive locked stress, pinned rigidity,
an interior three-channel reaction fan, actual source-response coembedding,
and elimination of the fan's basis penalty do not imply positive Schur
nullity or positive coarse Hall deficiency. This strengthens the
disjoint-gadget regression of Section 149 and is distinct from the
triangle-free activation-forest regression of Section 152.

**Explicit global exclusion of this family.** For `M>=33`, put
`r=ceil(2M/3)+1`, `s=ceil(3M/4)+2`, and take the staggered lattice rectangle

$$
P_M=\{(i+(j\bmod2)/2,(\sqrt3/2)j):0\le i<r,\ 0\le j<s\}.
$$

It is unit-separated, has `rs>=n_M`, and has diameter at most

$$
\sqrt{(r-1/2)^2+\tfrac34(s-1)^2}
<\sqrt{\tfrac{499}{576}M^2+\tfrac{17}{4}M+\tfrac{21}{4}}<M.
\tag{11}
$$

The first strict inequality uses `ceil x<x+1`. The last holds at `M=33`
with exact squared gap `5/64`, and its gap is strictly increasing for
`M>=33`. Select any `n_M` labels of `P_M` to obtain a complete-source,
same-cardinality strict competitor. This proves that the large chambers
are nonglobal, rather than merely leaving their optimality unverified.
Neither source roundness nor the large flexible original source is supplied
by this regression; global optimality is precisely an additional restriction
that a successful quantitative transport theorem must exploit.

## 5. Exact global limit on simultaneous eligibility

For `M=1`, the three vertices of the unit equilateral triangle are a global
optimum with `D(3)=1`, and are the right endpoint of the diameter-one plateau:
four separated points of diameter one would all have pair distance one,
which is impossible in the plane (the intersection of the two unit circles
through one unit pair consists of two points at mutual distance `sqrt(3)`).

At the phase (7), `|Z|=1` and its sole row conflicts with all three vertices.
The interior matroid is `U_{1,3}`. Each vertex is individually omittable,
but every basis contains one of them. Thus the three reaction vertices
cannot simultaneously be Schur terminals; the Schur response has rank two
and nullity zero. This is a regression against unrestricted simultaneous
eligibility, not against an asymptotic theorem with an additional hypothesis.

If an interior exchange instead has `|N(Q)|=|Q|+k`, `k>0`, expansion (4)
still produces a completely strict packet, but leaves only `m-k` source
labels. Global optimality at `m` supplies no contradiction. A constructive
restoration of those `k` labels is still required. No first-order release,
individual basis exchange, or reaction connectivity fills that gap.

## 6. Verification, limitations, and remaining theorem

The exact certificate uses rational lattice coordinates and the quadratic
form `a^2+ab+b^2`. It checks all source and packet pairs for listed finite
sizes, every row of (8), deep-first membership, all fan lenses, the direct
surviving terminal-to-sink linkages and their geometric avoidance of the fan,
contact/facet force balance, exact full mixed rank at `M=4,5`, and the
small global regression. It enumerates all right subsets for `M=4` to
check strict Hall expansion in that fixture, and includes equality-clearance
and container-placement negative controls for the exchange construction. The arbitrary-size
and all-phase statements are established by the analytic proofs above;
finite runs alone do not establish them. No global source realization is
claimed for the large chamber family.

Reproduce with

```bash
python3 research/verify_target_a_seed063_tight_isolates.py
python3 -O research/verify_target_a_seed063_tight_isolates.py
python3 tools/check_theorem_state.py
python3 -m unittest tools.test_check_theorem_state tools.test_check_theorem_state_pr tools.test_check_active_route_summaries
```

Both certificate modes passed: 187,200 source pairs, 1,140,415 packet pairs,
42 exchange pairs, and 1,023 right subsets. The 22 repository state/PR/route
tests passed. These are local checks; GitHub Actions status is reported separately
in the PR handoff.

Theorem 1 uses a new secondary choice of the response optimum. Section 165
permits that choice because its placement is uniform over plateau optima.
Neither the original flexible source nor its old contact graph is identified
with this response. In particular no ZR/ZF theorem is extended to isolate
coordinates, no Euler-path inference is used, and no independent source
matchings are identified.

The smallest closing lemma remains the quantitative, global source-response
transport theorem `Xi_Sigma>=j_*+|T_Z|` (or the exact lens criterion) for a
stress-generated fan, together with a resolution of the zero-slack branch.
The new reduction removes active coloops and permits individual reaction
terminals. It does not supply simultaneous surplus or pay the interior tube,
and (10) proves that the listed stress/matching reductions alone cannot do so.

**Promotion recommendation:** independent scrutiny of Theorems 1–2 and the
regressions; retain as unreviewed candidates until that scrutiny. Canonical
state, Target A's endpoint, and Level I status are unchanged.
