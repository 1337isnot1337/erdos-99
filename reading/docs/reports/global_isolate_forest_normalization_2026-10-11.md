> Generated reading edition · [exact source](../../../docs/reports/global_isolate_forest_normalization_2026-10-11.md) · source SHA-256 `5fd3913aee363f1e555b562b1255ecdb71550d09ec4d19158907a889662e1de0`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "unreviewed_noncanonical", "source_blob": "9bc09c9e640ee1daff9e2f213fca5b069ef2b2e5", "source_branch_refs": ["refs/heads/research/sol/global-e99-20261011"], "source_commit": "a17f1755b254d1bdbcd165394a929050cd4c2f69", "source_lifecycle": "unreviewed", "source_path": "docs/reports/global_isolate_forest_normalization_2026-10-11.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "0e7618d91157ee39d74703124263323dae149967af7e990f909831f885d63090"} -->

> **Imported unreviewed branch research.** Source branch status is historical only; no destination claim is promoted.

# Erdős Problem #99 — global isolate normalization and stress-preserving forests

**Date:** 2026-10-11

**Repository base:** `ab6dd3336f9f8d440f2bada76edb32153391cddc`

**Worktree checkpoint:** `f75b300c5d2804d4da83f317c79fef142398581c`

**State version:** `2026-10-10.audit.234`

**Target:** Level I; alternative normalization of a hypothetical global counterexample

**Run type:** independent closing-proof investigation; exact regression

**Active prompt:** `docs/prompts/erdos_problem_99_GPT6_ASTRA_FULL_SOLUTION_PROMPT.md`

**Computation:** `research/verify_global_isolate_forest_normalization.py`

## LEVEL I STATUS

**STILL OPEN.** The existence of a triangle-free global minimizer is reduced
exactly to existence of one without contact isolates. The construction does
not preserve contact-minimality and does not activate the stress on the new
contacts. Thus it does not eliminate the canonical inactive-population branch.

## 1. Global endpoint and alternative route

Write `M_tf(n)` for the triangle-free global minimizers in the exact sense of
`docs/problem/statement.md`. The investigated chain is

```text
M_tf(n) nonempty -> a global triangle-free representative with no contact isolates
-> a full-source stress/rigidity theorem -> a Level I contradiction
```

The first arrow is proved below for every `n>=2`. The stress/rigidity arrow
fails for the constructed representative: all new forest contacts have
universally zero nonnegative equilibrium multipliers. Section 6 states the
additional requirement for genuine stress activation.

The normalization and stress-lifting arguments use the problem definition,
finite convexity, elementary equilibrium, and linear algebra. Section 6.3
also uses the canonical finite Oler inequality in
`docs/theory/03-oler-shell.md`, Lemma 21.1. No Target A/B/C theorem is imported
as a premise.
In particular the source produced here is not substituted into the canonical
contact-minimal ZR/ZF theorem.

## 2. Full-source upper normalization of isolates

**Classification:** proved candidate awaiting promotion; artifact unreviewed.

Let `P` be any finite unit-separated source of diameter `D`, let `V` be its
nonisolated unit-contact vertices, and let `Z` be the contact isolates. Keeping
`V` pointwise fixed, a sufficiently small simultaneous contraction of `Z`
towards the full-source centroid preserves all lower inequalities and makes
every isolate-involving pair strictly shorter than `D`. All isolate-involving
lower distances remain strictly greater than one.

### Proof

For the centroid `c`, every source label `q` has

$$
|c-q|\le{n-1\over n}D<D.
$$

Set `p_z(epsilon)=(1-epsilon)p_z+epsilon c` for `z in Z`. Isolate-isolate
differences contract by the factor `1-epsilon`; isolate-fixed differences
satisfy

$$
|p_z(\epsilon)-p_v|
\le(1-\epsilon)|p_z-p_v|+\epsilon|c-p_v|<D.
$$

There is a positive minimum lower-distance slack among the finitely many
isolate-involving pairs. Moving each isolate by at most `epsilon D` preserves
that slack for sufficiently small positive `epsilon`. Old contacts and all
positions in `V` remain unchanged. If `P` is a global minimizer, the new
diameter equals `D`, since a strict decrease would already contradict global
minimality.

This elementary normalization agrees in effect with the recorded canonical
isolate normalization, but the proof here requires neither its stress nor its
endpoint hypotheses.

## 3. Exact single-contact activation

**Classification:** proved candidate awaiting promotion; artifact unreviewed.

In any finite unit-separated source of diameter `D`, an isolate can be moved
to a position with exactly one unit neighbor while all other labels stay
fixed. All moved-label upper distances are strictly below `D`; all old
contacts are retained. The result is still triangle-free if the old source
was triangle-free. A global source remains a global source of the same
cardinality.

### Proof, including the multiple-hit issue

Let `p` be the isolate and `B` the other labels. Its upper-feasible region is
the compact convex set

$$
K_p=\bigcap_{q\in B}\overline B(q,D).
$$

It contains `p`. It has nonempty interior: the centroid `c_B` of `B` has
distance at most `D(|B|-1)/|B|<D` from every label in `B`.

Choose any `q in B`. The open set `U=int(K_p) intersect B(q,1)` is nonempty:
move slightly from `q` towards `c_B`, or use `q` itself when `q=c_B`.

The intersections of the finitely many unit circles centered at labels of
`B` form a finite set. Choose `y in U` so the segment from `p` to `y` misses
every such intersection. This is possible because the forbidden choices of
`y` lie on finitely many rays from `p`, which cannot cover a nonempty planar
open set. No circle intersection equals `p`, since `p` is an isolate.

Follow `p(t)=(1-t)p+t y` to its first unit-circle hit. This happens at some
`0<t_*<1`, because `p` starts outside every closed unit disk while `y` lies
inside one. At the first hit there is exactly one unit neighbor; all other
lower distances are strictly greater than one. Avoiding circle intersections
is essential: a symmetric path can hit two adjacent neighbors and create a
triangle.

For every fixed `r in B` and every `0<t<=1`,

$$
|p(t)-r|\le(1-t)D+t|y-r|<D,
$$

because `y` is in `int(K_p)`. Thus every upper constraint is checked, including
inactive pairs and isolates. The one new edge has the previously isolated
label as an endpoint, so it cannot create a unit triangle. Global minimality
forces the resulting diameter to remain `D` if the starting source was
global. All labels are retained.

## 4. Global no-isolate equivalence

**Classification:** proved candidate awaiting promotion; artifact unreviewed.

For every `n>=2`,

$$
M_{\rm tf}(n)\ne\varnothing
\quad\Longleftrightarrow\quad
M_{\rm tf}(n)\text{ contains a source with no contact isolates}.
$$

Normalize upper distances by Section 2, then repeat Section 3 on a currently
isolated label until none remains. Each step adds exactly one contact and
removes one or two isolates. If initially `|Z|=z`, the number `k` of added
edges therefore satisfies

$$
\lceil z/2\rceil\le k\le z.
$$

All original nonisolated labels stay pointwise fixed. All original contacts
are retained, triangle-freeness is preserved, no new diameter pair appears,
and the global diameter remains `D` throughout.

The added edges form a forest relative to the old contact graph: each joins
a currently isolated singleton to one other component. In particular they
never merge two old nontrivial contact components and never create a cycle.
Each newly added tree has at most one original-core root; some trees may
have no original-core root. Source-wide contact connectivity is not claimed.

An equivalent extremal formulation is that a contact-maximal representative
in `M_tf(n)` has no contact isolates. Such a representative exists whenever
`M_tf(n)` is nonempty because its contact count takes values in a finite set
of integers. Compactness of the open triangle-free class is not assumed.

## 5. The activation preserves the nonnegative stress cone

**Classification:** proved candidate awaiting promotion; artifact unreviewed.

Here assume the diameter remains the original `D`, as it does for a global
source. `H` denotes pairs at that same upper bound before and after the
construction. If a nonglobal source's diameter decreases, recomputing `H`
at its smaller diameter defines a different stress problem and is not covered
by the cone-preservation statement.

Use nonnegative equilibrium coefficients with convention

$$
\sum_{ij\in C}\alpha_{ij}(p_i-p_j)
=\sum_{ij\in H}\beta_{ij}(p_i-p_j),
\qquad \alpha,\beta\ge0.
$$

Every original diameter edge incident to an isolate has coefficient zero in
every such stress. Indeed dot its isolate equilibrium with `c-p_i`. Each
incident actual-diameter term has strictly negative inner product:

$$
(p_i-p_j)\cdot(c-p_i)
={|c-p_j|^2-D^2-|c-p_i|^2\over2}<0.
$$

There is no contact term at the isolate, so all incident `beta` must vanish.
Deleting those universally zero diameter edges in Section 2 consequently
preserves the nonnegative stress cone.

In the final activated source no actual diameter edge touches `Z`. Take a
leaf of an added tree lying in `Z`. Its only remaining incident contact
coefficient must be zero by equilibrium; remove that edge and continue
peeling. Every added tree edge is zero in every nonnegative equilibrium
stress. The old equilibrium equations on `V` are unchanged because their
positions and old active edge vectors are unchanged.

Therefore restriction and extension by zero give inverse bijections of the
old and final nonnegative equilibrium cones, including any normalization
`sum beta=1`. Their full-source stress matrices are identical under the
fixed labeling: old isolate rows remain zero even though those labels now
have actual unit contacts.

If an old stress on `V` has rank `v-3` and affine kernel, its final full-source
matrix still has rank `v-3` and nullity `z+3`. It does **not** acquire rank
`n-3` merely because the physical contact graph has no isolates.

The mixed active rigidity matrix gains exactly `k` independent rows. Here
`R_old` is taken after the upper normalization in Section 2, before any
activation; universally zero diameter rows removed in that normalization
need not have been linearly redundant. Before
each added edge, its moving singleton has zero columns in all active rows;
the new row is nonzero in those columns. No diameter rows involving `Z`
exist, and old rows have unchanged vectors. Consequently

$$
\operatorname{rank}R_{\rm final}=\operatorname{rank}R_{\rm old}+k.
$$

Even if the old core had rank `2v-3`, the final rank is at most
`2n-3-z`, leaving at least `z` additional infinitesimal freedoms. Physical
contact activation is therefore insufficient for full-source rigidity.

## 6. The exact missing global bridge

The alternative normalization replaces physical isolates by inactive contact
forests. It preserves the inactive population at the stress level.

A genuinely stress-expanding replacement must have more than leaf contact
activation. If `z` new labels are to form a pinned infinitesimally rigid
contact network with a strictly positive equilibrium stress at the new
labels, at least `2z+1` new contact rows are necessary: the pinned matrix has
rank `2z`, while its transpose has a nonzero positive null vector. The
forest supplies at most `z` rows.

### 6.1 Absorbing reactions and lifting stress to all labels

**Classification:** proved candidate awaiting promotion as a conditional
theorem; artifact unreviewed.

The reaction coupling to the old source can be proved without an additional
matching or force-inheritance hypothesis. The exact assumptions are these:

Here `D>1`, so old unit contacts and diameter edges are disjoint.

1. The fixed old core `V` spans the plane, and its mixed active rigidity
   matrix has rank `2v-3`.
2. It has an equilibrium stress with strictly positive coefficients on every
   old contact and diameter edge, and its signed stress matrix `Omega_0` is
   PSD with kernel `U=span{1,P_x|V,P_y|V}`.
3. A new placement `Q_Z` is supplied, keeping `P_V` fixed, with all full-source
   lower inequalities, triangle-freeness, and strict upper slack on every pair
   involving `Z`. The old diameter remains `D`.
4. Let `E_+` contain **every** new actual unit contact. It has strictly
   positive weights `a_e` in equilibrium at each new label, treating `V` as
   fixed pins. Its pinned rigidity matrix has rank `2z`.

Then the new full source admits a stress positive on every actual contact and
diameter edge whose signed matrix is PSD of rank `n-3`. Its full mixed active
rigidity matrix has rank `2n-3`. No uniform spectral gap is asserted.

#### Proof

Let `L_+` be the positive weighted Laplacian of the new network. Write its
blocks as

$$
L_+=\begin{pmatrix}A_+&B\\B^T&C\end{pmatrix}.
$$

The pinned rank hypothesis implies that every new component reaches an old
pin, so the Dirichlet block `C` is positive definite. New-label equilibrium
gives `B^T P_V+C Q_Z=0` in both coordinate columns.

The old-pin reaction `f=(L_+ Q)|V` has zero total force and zero total torque.
Indeed Laplacian forces sum to zero; the torque sum is zero edge by edge, and
the new-label forces vanish. Since the old rigidity matrix has precisely the
three Euclidean kernel modes, the range of its transpose is exactly the space
of balanced old-pin force fields. Thus there are signed old-edge coefficient
increments `delta w` satisfying

$$
R_{\rm old}^T\delta w=-f.
$$

Let `Delta Omega` be their signed Laplacian. For positive `epsilon`, put

$$
\Omega_\epsilon=
\begin{pmatrix}\Omega_0&0\\0&0\end{pmatrix}
+\epsilon\left[
\begin{pmatrix}\Delta\Omega&0\\0&0\end{pmatrix}+L_+\right].
$$

This is equilibrium at every source label. Its new contact coefficients are
`epsilon a_e>0`. Every old coefficient keeps its required strict sign for
sufficiently small `epsilon`, because all old coefficients were strict.

Eliminating the positive block `epsilon C` gives the old-core Schur matrix

$$
\Omega_0+\epsilon S,\qquad
S=\Delta\Omega+A_+-BC^{-1}B^T.
$$

The full equilibrium and the new-label harmonic identities imply `S U=0`.
On `U`'s orthogonal complement `Omega_0` has a positive smallest eigenvalue
`gamma`. Consequently `Omega_0+epsilon S` is positive definite there for
`epsilon ||S||_2<gamma`, and has kernel exactly `U`. Block congruence then
gives `Omega_epsilon>=0` and rank `(v-3)+z=n-3`. Its kernel consists of the
three full-source affine columns, because the new columns are the unique
Dirichlet harmonic extension of the old ones. Positive diameter coefficients
can be renormalized to sum one if desired.

Finally any mixed bar flex restricts on `V` to a Euclidean motion by the old
rank hypothesis. Subtract that motion on the full source. The remaining old
pin velocities vanish, and pinned rank `2z` forces all new velocities to
vanish. This proves full mixed rank `2n-3`.

The old coefficient strictness is essential to the sign-preserving
perturbation; full old rank alone is not a substitute. The construction is a
stress on the supplied actual source placement, not on a separate scaffold.

### 6.2 Remaining geometric obligation

The reaction and PSD coupling in Section 6.1 is closed under its hypotheses.
The proposed next bridge is a same-cardinality placement of the inactive
population satisfying assumptions 3–4, or a direct strict sub-`D` replacement.
Its existence is **unproved**. It cannot be inferred from no physical isolates,
the forest contact count, pinned rank alone, or a local numerical mesh.

Positive pinned equilibrium plus pinned rank also makes the supplied endpoint
locally isolated in the fixed-pin unit-separated configuration space. If
distinct feasible placements approached it, normalize their displacements to
unit size and take a limit. Every contact's first variation is nonnegative.
The positive equilibrium relation makes their weighted sum zero, hence every
first variation is zero. Full pinned rank then makes the normalized limiting
displacement zero, a contradiction. An isolated feasible endpoint cannot be
reached from a different feasible placement by a continuous path with pins
fixed. Thus starting from strict isolates, this bridge requires a **discrete
replacement**, not a fixed-pin contact-opening motion.

Even a supplied positive pinned activation does not restore contact-minimality:
the resulting global source has more contacts. It therefore does not by itself
authorize importing every canonical contact-minimal Target C theorem or
settle Level I. A closing argument must use the hypotheses it actually has.

### 6.3 Capacity obstruction to fixed-core positive activation

**Classification:** proved candidate awaiting promotion; artifact unreviewed.

There is a global geometric restriction on Section 6.1's fixed-core approach.
Put `F=conv(P_V)`, with area `A_F` and perimeter `P_F`. If all new components
reach old pins and are in positive pinned equilibrium, every new label lies
in `F`. For any linear functional, a new-label maximum above the largest pin
value would propagate along every positively weighted adjacent edge to an
old pin, a contradiction. This is the finite maximum principle.

Unit separation and the canonical Oler inequality therefore force

$$
n-1\le A_F/a_0+P_F/2,\qquad a_0=\sqrt3/2.
$$

Independently, every global unit-separated minimizer has

$$
n-1\ge {\pi D^2\over4a_0}.
$$

To prove this elementary population bound, if it failed choose `r<D/2`
with `pi r^2/a_0>n-1`. Averaging translates of the unit triangular lattice
over one fundamental cell gives that mean number of lattice points in the
open radius-`r` disk. Since the count is integral, some translation has at
least `n` points there. Selecting `n` gives a unit-separated strict sub-`D`
competitor, contradicting global minimality.

Combining the bounds gives the necessary condition

$$
\boxed{\pi D^2/4-A_F\le {a_0\over2}P_F.}
$$

Thus fixed-core positive activation is impossible whenever the old core-hull
area deficit exceeds `(sqrt(3)/4) P_F`. In particular, if the deficit is
`Omega(D^2)`, Cauchy's perimeter bound `P_F<=pi D` makes positive activation
of the entire population impossible for large `D`. This bound follows from
the same convex perimeter formula used with Lemma 21.1: integrate widths,
each at most `D`, over directions in `[0,pi]`.

This is an obstruction to the proposed normalization, not a disproof of the
original source's globality: the original inactive labels can lie outside
`F`. A unified activation proof must therefore move the old core in a
macroscopic exterior-hull deficit regime. Merely adding pinned contacts
while fixing old core positions cannot settle that branch.

## 7. Exact regression family and computation

**Classification:** regression; artifact unreviewed.

For even `m>=4`, use the `4m` unit-spaced boundary labels of `[0,m]^2`, and
the `z=(m/2-1)^2` isolated labels `(2i,2j)`, `1<=i,j<=m/2-1`.
The diameter is `m sqrt(2)` with two opposite-corner diameter pairs. Move the
interior labels row by row, from left to right, to `(i,2j)`. Each adds exactly
one contact, producing rooted unit chains. All source labels remain, the
complete contact graph is triangle-free and has no isolates, and no new
diameter pair appears.

Put weight one on the old boundary contacts and weight `1/m` on each old
diameter pair. This is exact equilibrium. Its stress is PSD with rank `4m-3`:
eliminating each straight boundary path yields effective conductance `1/m`
between its corners, and the four-corner Schur matrix is
`(L_cycle4-L_two_diagonals)/m`, of PSD rank one. Every new chain contact has
weight zero in every nonnegative equilibrium stress. The full stress nullity
remains `z+3` after all physical isolates disappear.

These sources are strictly nonglobal. Their population is
`N=m^2/4+3m+1`. An `N`-point unit square-grid crop with
`w=ceil(sqrt(N))`, `h=ceil(N/w)` has diameter at most
`sqrt((w-1)^2+(h-1)^2)<m sqrt(2)`. For `m>=6`, `N<m^2` implies `w,h<=m`;
for `m=4` the squared bound is `25<32`. No global counterexample is claimed.

The script checks `m=4,6,8,12` using exact integers and fractions, every
source pair after every activation, the full contact and diameter ledgers,
equilibrium, rational PSD elimination, stress rank, mixed-rigidity rank
increments, and the smaller-diameter comparison. A separate rational path
checks avoidance of a symmetric first-hit triangle. These finite checks
support the fixtures; the all-source and global theorems are proved above.
The conditional reaction/Schur lifting and the Oler capacity obstruction are
analytic proofs; the script supplies no source-wide positive pinned packing.

## 8. Claim audit and status

| Claim | Classification | Scope |
| --- | --- | --- |
| Upper normalization of every isolate | Proved candidate awaiting promotion | All labels retained; exact finite lower and upper inequalities |
| Unique-contact isolate activation | Proved candidate awaiting promotion | Generic first hit; full upper feasibility; old contacts retained |
| Global no-isolate equivalence | Proved candidate awaiting promotion | Every cardinality; diameter remains globally minimal |
| Forest activation preserves nonnegative stress cones | Proved candidate awaiting promotion | Diameter unchanged; old core fixed; inactive diameter multipliers universally zero |
| Physical no-isolates imply full-source affine stress kernel | Rejected inference | Activated forest rows carry zero stress |
| Reaction absorption and full-source PSD stress lifting | Conditional proved candidate awaiting promotion | Strict old stress and old mixed rank; supplied feasible positive pinned network |
| Fixed-core positive activation requires only boundary-order hull-area deficit | Proved candidate awaiting promotion | Maximum principle, global lattice population bound, canonical finite Oler inequality |
| Positive pinned activation is available for every large source | Unproved | No network extraction or capacity theorem supplied |
| Level I closure | Unproved | The stress-expanding or strict-diameter bridge remains missing |

**Promotion recommendation:** unreviewed. No canonical state, route prompt,
or Level I status is changed. The inactive-population issue remains binding
under the new normalization, with its zero-stress forest structure explicit.
