<!-- migration-provenance: {"destination_status": "unreviewed_noncanonical", "source_blob": "7e9fc01926f74fb3358fa47bdcc8a4d8bafeb1a8", "source_branch_refs": ["refs/heads/research/sol/global-e99-20261011"], "source_commit": "c17f8d5eed95f1df57262587219a2c0673365aa7", "source_lifecycle": "unreviewed", "source_path": "docs/reports/global_local_lex_normalization_and_crystalline_obstruction_2026-10-11.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "7ba2bf9678fd53714c3671a6bced51a289f00e940816b8cf9f85bdba68a6a3e8"} -->

> **Imported unreviewed branch research.** Source branch status is historical only; no destination claim is promoted.

# Erdős Problem #99 — local normalization and a global crystalline obstruction

**Date:** 2026-10-11

**Repository commit:** `a17f1755b254d1bdbcd165394a929050cd4c2f69`

**State version:** `2026-10-10.audit.234`

**Run type:** global-quantifier extension and geometric consequence

**Target:** Level I through Target C

**Claim classification:** proved candidates awaiting promotion; report unreviewed

**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md`

**External literature / computation:** Schürmann's 2006 container theorem was
consulted as a near miss; no theorem is newly imported from it. The proof uses
the canonical inputs listed below, and elementary geometric counting.

## 1. Endpoint and scope

`LEVEL I STATUS: STILL OPEN.`

The canonical endpoint is a full-source, same-cardinality strict sub-`D` competitor,
or a feasible same-`D` endpoint contradicting the canonical contact/diameter
lexicographic minimum. This report constructs neither. Its new implication is

```text
arbitrarily close local lexicographic normalization
 -> at least ceil(D) actual diameter pairs/endpoints in every triangle-free optimum
 -> large optima cannot have a bounded coarse-lattice description of those endpoints.
```

Here and throughout, a global optimum is a labelled configuration of all `n` source
points. No contact isolate is discarded. For an arbitrary source `P`, let `C(P)` be
its actual unit-pair set, `H(P)` its actual diameter-pair set, and `B(P)` the endpoint
set of `H(P)`. In particular, `B(P)` means actual diameter endpoints, including any
contact-isolated endpoints; it does not mean the positive endpoints of one stress.

### Main candidate

Every triangle-free global minimum-diameter configuration `P` with `D=D(n)>=9`
satisfies

\[
 |H(P)|\ge\lceil D\rceil,\qquad |B(P)|\ge\lceil D\rceil.       \tag{1}
\]

These statements do not assume that `P` itself is contact-minimal, diameter-pair-minimal,
or fully stress-visible. The distinction is essential to the consequences below:
the configurations in the lattice hypotheses are the original `P`, not a separately
chosen optimum whose point coordinates may leave that lattice.

## 2. Local normalization without adding an active pair

Fix any labelled triangle-free global optimum `P` and any radius `epsilon>0`.
Shrink the radius, if necessary, so that throughout the open ball `U` about `P`
in `R^(2n)` every originally inactive lower or upper pair stays inactive.
There are finitely many pairs and each has positive slack, so such a ball exists.
Consequently every feasible `Q in U` satisfies

\[
 C(Q)\subseteq C(P),\qquad H(Q)\subseteq H(P).                 \tag{2}
\]

Every unit-separated configuration in `U` of diameter at most `D` is a global optimum,
by the definition of `D(n)`. It is also triangle-free by the contact inclusion.

Among the optima in `U`, choose `R` first minimizing `|C(R)|`, then `|H(R)|`.
The choices exist: each count takes values in a finite nonempty set of integers.
No closedness or compactness of the triangle-free optimum set is asserted or needed.
Since `R` lies in the open set `U`, it has a smaller neighbourhood contained in `U`.
Thus `R` is **locally** contact-minimal, then locally diameter-pair-minimal, among
full-source optima.

This construction works in every sufficiently small ball about `P`. It does not
claim global lexicographic minimality, a continuous path from `P` to `R`, or a
uniform stress gap as the radius tends to zero.

## 3. Audit of the locality needed for the diameter count

The following audit extends only the indicated C53/C63, zero-transfer, and ZR/ZF
arguments. It does not replace the global normalization in later canonical
replacement or population theorems.

### 3.1 Full actual support and exact local length preservation

The canonical C53 restoration proves PSD for **every** normalized source KKT stress,
not only for a globally lexicographic source. C63 produces arbitrarily nearby
feasible full-source configurations releasing every weak active row, with no new
active pairs. Global optimality keeps their diameter equal to `D`.

At `R`, opening a weak contact contradicts its local first minimum. Once contacts
are fixed, opening a weak diameter pair contradicts its local second minimum.
Thus

\[
 C(R)=C_*,\qquad H(R)=H_*.                                    \tag{3}
\]

A relative-interior normalized stress is positive on every actual contact and
diameter pair. The positive contact graph is one connected nonisolated core `V`
of diameter `D`; every actual diameter endpoint is in this core. In particular,
the remaining labels are incident to no active contact or diameter constraint.

Every mixed critical velocity integrates by C63. At sufficiently nearby feasible
points, inactive pairs remain strict. The two local minima force every old active
length to remain exactly its old value. This is precisely the local step used in
the canonical common-stress-kernel proof; no distant comparison is used.

The maximal force hull cannot be one-dimensional here. If it were, perpendicular
equilibrium in the connected positive network would put the full core on one line.
Unit separation and connected unit contacts make it a straight unit chain. By (3)
the only actual diameter pair is its two extreme endpoints; isolates have strict
upper slack. For `D>1`, rotate one end point a small nonzero angle about its sole
unit neighbour. That contact remains unit, its old diameter distance strictly
decreases, and every inactive full-source pair stays strictly feasible for a small
enough angle. All source distances are then strictly below `D`, a contradiction.
This supplies the two-dimensional hull condition locally as well.

### 3.2 The pre-ZF endpoint bound is local

Let `v=|V|`, `e=|C(R)|`, and `q=|B(R)|`. Pin all `q` actual diameter endpoints.
The contact rigidity matrix on the remaining `2(v-q)` coordinates has trivial
kernel. Indeed, extend a pinned contact bar flex by zero at the contact isolates.
It is a full-source mixed bar flex, since every diameter endpoint is pinned.
C63 integrates it, and Section 3.1 forces exact preservation of all active lengths.
Pair those identities with a relative-interior stress and divide by the squared
motion parameter. For its velocity `u`, this gives

\[
 u_x^T\Omega_Vu_x+u_y^T\Omega_Vu_y=0.
\]

Because `u` is zero at every diameter endpoint, the negative diameter-Laplacian
terms vanish. The expression is the positive sum

\[
 \sum_{ij\in C(R)}\alpha_{ij}|u_i-u_j|^2.
\]

All contact weights are positive and the core is connected, so `u` is constant
on the core, hence zero at its pinned vertices. Therefore

\[
 e\ge2(v-q).                                                  \tag{4}
\]

The contact core is a connected triangle-free penny graph of graph diameter
`delta>=ceil(D)`. The canonical Eppstein bound gives `e<=2v-delta-2`.
Combining it with (4) yields

\[
 2q\ge\lceil D\rceil+2.                                      \tag{5}
\]

This reconstructs the pre-ZF count without extending the stated scope of the
older globally minimum-contact pinned-rank theorem by assumption.

### 3.3 Zero transfer and ZR/ZF use the same local data

The canonical zero-transfer proof uses full positive contact support, actual
diameter geometry, the circular-planar response and interval-split identities,
(5), and elementary contact degree caps. After its diagonal-transfer reduction,
SEPq produces a vertex separating all loaded terminals. It must have degree at
least `q` if unloaded, or `q-1` if loaded. At `D>=9`, (5) gives `q>=6`.
Triangle-free unit separation caps the first degree at five; convex extremality
caps the second at three. This is the same contradiction at `R`.

No comparison with a distant global contact-minimal representative appears in
that proof. Thus its strict-negative transfer conclusion applies to `R`.
The algebraic ZR argument in the canonical module then gives

\[
 \ker\Omega_V=\operatorname{span}\{\mathbf1,R_x|_V,R_y|_V\}.
\]

For any mixed bar flex on `V`, extend it by zero at every omitted source label,
integrate it by C63, and use the exact local length preservation from Section 3.1.
PSD and the affine kernel show that this flex is affine on `V`. By (5), at least
three distinct projective diameter directions exist; their zero radial variations
force the symmetric part of its affine matrix to vanish. Thus the mixed rigidity
rank on `V` is `2v-3`, exactly as in the canonical ZF proof. A nonzero full-support
stress gives a row dependence, so

\[
 e+|H(R)|\ge2v-2.
\]

Eppstein's bound now yields

\[
 |H(R)|\ge\delta\ge\lceil D\rceil.                           \tag{6}
\]

The diameter graph has at most as many edges as endpoints, by the canonical
Woodall diameter-graph classification, so `|B(R)|>=|H(R)|`. Finally (2) implies
`H(R) subseteq H(P)` and `B(R) subseteq B(P)`. This proves (1) for the original
arbitrary optimum. Neither rigidity nor full stress support is transferred to `P`.

### Exact canonical dependencies

- C53/C63, including universal PSD and nearby finite integration: the scoped
  statements promoted in `docs/targets/target-c/56-ci-restored-frontier.md`.
  Their proof details are Sections 4--6 of
  `docs/reports/target_c_c53_orientation_and_ci_restoration_2026-09-09.md`;
  that report's overall lifecycle is unreviewed, and no other claim in it is imported.
- Positive-support connectivity and the connected triangle-free penny-graph bound:
  `docs/targets/target-c/01-force-hull-and-shear.md`, Sections 6 and 11.
- `C-ZTA`, its interval-split/SEPq proof:
  `docs/reports/target_c_zero_transfer_additive_promotion_2026-09-11.md`.
- `C-ZRF`, the algebraic affine-kernel argument and the mixed-rigidity argument:
  `docs/targets/target-c/57-zr-zf-rigidity-audit.md`, Sections 1--4.
- `C-WOODALL`, used only for `|H(R)|<=|B(R)|`:
  `docs/targets/target-c/README.md` and the current generated Target C ledger.

The new work is the local selection and the audit of the above arguments' scope,
not a promotion of any other historical report.

## 4. A quantitative obstruction in the original configuration

Every diameter endpoint is a strict extreme vertex of the full source hull:
if it were a nontrivial convex combination of other points, the strict
squared-norm convexity identity would make its distance to any source point less
than `D`. Thus the `q=|B(P)|` vertices of `conv B(P)` are in strict convex position.
Its perimeter is at most `pi D` by the convex perimeter/diameter inequality.

Write its oriented side vectors as `w_1,...,w_q`. They are nonzero and distinct,
since their directions turn strictly around a convex polygon. Let

\[
 \eta=\min_{i\ne j}|w_i-w_j|>0.
\]

Disjoint disks of radius `eta/2` centred at side vectors of norm at most `r`
fit in the disk of radius `r+eta/2`. There are therefore at most
`4(r/eta+1/2)^2` such vectors. Ordering their norms gives

\[
 |w|_{(j)}\ge {\eta\over2}(\sqrt j-1).
\]

Sum and use `sum_{j=1}^q sqrt(j)>=(2/3)q^(3/2)`:

\[
 \operatorname{per}(\operatorname{conv}B(P))
 \ge\eta\left({q^{3/2}\over3}-{q\over2}\right).
\]

Since `q>=D>=9`, the positive factor can be divided out to obtain

\[
 \boxed{\eta\le {3\pi\over\sqrt D-3/2}.}                     \tag{7}
\]

In particular, if the actual diameter endpoints lie in a translate of a lattice
with shortest nonzero vector at least `lambda>0`, then their side-vector
differences have norm at least `lambda`. Hence

\[
 \boxed{D\le(3\pi/\lambda+3/2)^2.}                           \tag{8}
\]

The lattice need not have two unit generators. For `lambda>=1`, (8) excludes
every triangle-free optimum in this class once `D>(3pi+3/2)^2`. The hypothesis
can concern just the actual diameter endpoints; other source labels may lie
anywhere. An ambient lattice with arbitrarily short unused vectors does not
satisfy a uniform `lambda` hypothesis.

### Multiple lattice grains

Suppose the `q` actual diameter endpoints are covered by `G` lattice translates,
each having shortest nonzero vector at least `lambda>0`; the lattices may differ
and may be rotated. Assign each endpoint to one covering grain and let `q_g` be
its assigned count. Its convex hull has perimeter at most `pi D`. The same side
vector argument gives

\[
 \lambda\left({q_g^{3/2}\over3}-{q_g\over2}\right)\le\pi D.
\]

For `q_g<=2` the left side is nonpositive, so this inequality holds without a
polygon argument. Sum it and apply Jensen's inequality to the nonnegative `q_g`:

\[
 \lambda\left({q^{3/2}\over3\sqrt G}-{q\over2}\right)
 \le G\pi D.
\]

Divide by `q`, use `q>=D`, and rearrange:

\[
 \boxed{D\le9G(G\pi/\lambda+1/2)^2.}                         \tag{9}
\]

For any fixed positive `lambda`, an unbounded-diameter sequence of triangle-free
global optima therefore needs an unbounded number of exact lattice grains covering
its actual diameter endpoints; quantitatively `G=Omega(D^(1/3))`. The theorem does
not identify such a grain decomposition in a general source, nor charge its
interfaces against a canonical population budget.

## 5. The obstruction survives a vanishing uniform lattice perturbation

There is also a coarse, explicit robustness statement. Suppose every actual
diameter endpoint is within `epsilon<=1/4` of one translate of a lattice with
shortest vector at least one. If `D>=852`, then

\[
 \boxed{\epsilon\ge {1\over2}\sin(1/1704).}                 \tag{10}
\]

To prove this, first bound the turn at an actual diameter endpoint `b`. Let its
two loaded-hull neighbours have distances `a,c>=1` from it, and choose any source
diameter partner `r`. All source points lie in the disk `B(r,D)`, with `b` on its
boundary. For a neighbour displacement `z`, the disk inequality gives

\[
 (r-b)\mathbin{\cdot}z\ge |z|^2/2.
\]

Thus the interior angle at `b` is at most
`pi-arcsin(a/(2D))-arcsin(c/(2D))`. Every exterior turn is at least

\[
 \theta_D=2\arcsin(1/(2D)).                                  \tag{11}
\]

The oriented side directions consequently have circular spacing at least `theta_D`.
Perimeter at most `pi D` leaves at least `q-pi D/(2pi)>=D/2` sides of length at
most `2pi`. Round each endpoint to a lattice point within `epsilon`. A short side
is within `2epsilon` of a nonzero lattice vector of norm at most `2pi+2epsilon`.
The rounded side is nonzero since the original side has length at least one and
`2epsilon<1`.

Unit-separated lattice vectors in a disk have the disjoint-half-disk bound used
above. There are at most

\[
 4(2\pi+2\epsilon+1/2)^2\le4(2\pi+1)^2<213=:N
\]

possible rounded vectors. For each such vector the original side directions lie
in an angular interval of length `2arcsin(2epsilon)`: the side norm is at least
one and its vector error is at most `2epsilon`. By (11), this interval contains
at most

\[
 1+{\arcsin(2\epsilon)\over\arcsin(1/(2D))}
 \le1+2D\arcsin(2\epsilon)
\]

side directions. Therefore

\[
 {D\over2}\le N+2ND\arcsin(2\epsilon).
\]

For `D>=4N=852` this forces `arcsin(2epsilon)>=1/(8N)=1/1704`, proving (10).
The constant is deliberately elementary and is not optimized.

This concerns **uniform proximity of the actual endpoints** to one coarse lattice.
It does not follow from an area-averaged strain estimate, and it does not exclude
nonvanishing cumulative displacement from small per-edge strains.

### A global angular-cluster budget

The turn bound (11) supplies an obstruction without any lattice or coordinate
rounding hypothesis. Let `S_D` be the set of loaded-hull sides of length at most
`2pi`; as above, `|S_D|>=D/2`. Suppose all but `K` of their oriented directions
are covered by `M` circular intervals, each of angular length at most `w<2pi`.
Each interval contains at most `1+w/theta_D<=1+Dw` side directions. Hence

\[
 \boxed{{D\over2}\le K+M(1+Dw).}                             \tag{12}
\]

In particular, for fixed `C` and `w=C/D`, a cover with `K=o(D)` requires

\[
 M\ge\left({1\over2(1+C)}+o(1)\right)D.                    \tag{13}
\]

With intervals of differing lengths `w_j`, the same proof gives

\[
 \boxed{\sum_{j=1}^M w_j\ge {1\over2}-{K+M\over D}.}         \tag{14}
\]

Thus `K=o(D)` and `M=o(D)` force an aggregate angular cover length of at least
`1/2-o(1)` radians. Small phase width for a macroscopic grid does not extend to
this boundary cover automatically. The vectors being covered here are the actual
short sides of the original diameter-endpoint hull.

Equivalently, put a mass `1/D` at each direction in `S_D`. Any subsequential weak
limit of these measures has total mass at least `1/2` and is dominated by angular
Lebesgue measure. Indeed, an open arc of length `ell` contains at most
`1+D ell` side directions, so its mass is at most `1/D+ell`.
The measures have bounded total mass (`q<=per(conv B(P))<=pi D`), and passing
to a weak limit proves the claimed domination on open arcs, hence on Borel sets.
In particular their limiting directions occupy angular measure at least `1/2`.

### Finite accumulation complexity is impossible

Consider any sequence of triangle-free global optima with `D->infinity`, and
apply arbitrary separate isometries to its sources. The union of their point
differences cannot have only finitely many accumulation points in every bounded
region. This is stronger than an exclusion of one fixed lattice direction set.

If it did, the union of short side vectors in the compact annulus
`1<=|z|<=2pi` would have finitely many accumulation points `a_1,...,a_N`.
For any fixed `delta>0`, only finitely many distinct side vectors lie outside
the union of the `delta`-balls about those points, by compactness. Call that
number `K_delta`. Within any one source its oriented side vectors are distinct,
so the same `K_delta` bounds the exceptions in that source, independently of `D`.

For `delta<1/4`, vectors of norm at least one within `delta` of a fixed nonzero
vector have directions in an interval of width at most `2arcsin(delta)`.
Apply (12) with `M=N`, `K=K_delta` and that width. After dividing by `D` and
letting `D->infinity`, it gives

\[
 {1\over2}\le2N\arcsin(\delta).
\]

Choose `delta` sufficiently small to contradict this inequality. If `N=0`,
compactness instead bounds the total number of distinct short side vectors,
which contradicts `|S_D|>=D/2` directly.

For comparison, Schürmann's [*On packing spheres into containers*](https://arxiv.org/pdf/math/0506200),
Definition 1 and Theorems 1--2, excludes lattice or limited-complexity optimal
packings in a **fixed smooth convex container**. The present argument excludes
finite bounded-difference accumulation complexity for triangle-free
minimum-diameter optima without prescribing a container. Neither result says
that every general triangle-free family has finite complexity. No container
theorem is substituted for the Level I quantifiers.

## 6. Claim and regression audit

| Claim | Classification | Decisive scope |
| --- | --- | --- |
| Arbitrarily close local lexicographic representative with active sets contained in the original sets | Proved candidate awaiting promotion | Full labelled global optimum; integer minima in an open neighbourhood |
| Every triangle-free global optimum with `D>=9` has at least `ceil(D)` actual diameter pairs and endpoints | Proved candidate awaiting promotion | Local audit of C53/C63, zero-transfer and ZR/ZF; counts transfer by active-set inclusion |
| Bounds (7)--(9) and the robustness bound (10) | Proved candidates awaiting promotion | Original actual endpoint geometry, conditional only on the stated lattice hypotheses |
| Angular cover bounds (12)--(14) and exclusion of finite bounded-difference accumulation complexity | Proved candidates awaiting promotion | Actual loaded-hull side lengths, the original-source count (1), and the disk-imposed turn bound (11) |
| Full stress visibility or mixed-core rigidity of an arbitrary original optimum | Not claimed | Positive weights/ranks may degenerate in the limit of local representatives |
| General Level I closure from a lattice-grain description | Conditional missing route | No universal grain extraction, interface payment, or finite competitor is supplied |

| Binding regression | Check |
| --- | --- |
| Triangle-free approximations can approach `D(n)` with only one unit pair | They are not global optima; neither (1) nor local fixed-`D` selection applies |
| Large square-wall sources with many isolates and just four diameter endpoints | The sources are nonglobal, as certified in `global_isolate_forest_normalization_2026-10-11.md`; they correctly fail (1) |
| Contact isolates and stress zero rows | Retained throughout; original `B(P)` includes all actual diameter endpoints |
| A separately normalized source can leave the original lattice | No lattice is transferred to it; only its pair/endpoint counts transfer back |
| Strict response minors need not have a uniform gap | No gap or positive stress weight is passed to the original source |
| Drifting phases, multiple grains, and nonlattice rhombic meshes | Survive the stated exact-lattice exclusions; (9) supplies a necessary cover size only |
| Later canonical global lexicographic replacement theorems | Not extended by this locality audit |

## 7. Frontier effect and remaining bridge

These are unpromoted global necessary conditions. They extend the older
force-visible single unit-rhombic-lattice exclusion to arbitrary original
triangle-free optima, more general coarse lattices, and bounded grain covers.
The dependency audit does not change the canonical state or its active prompt.

A closure using this direction would require a source-level theorem that the
actual endpoints of every large triangle-free optimum admit a cover by coarse
lattice grains with `G=o(D^(1/3))`, or an independently adequate bound proving
such a cover incompatible with (9). An alternative exact bridge is to cover all
but `o(D)` actual loaded-hull sides of length at most `2pi` by `o(D)` angular
packets of width `O(1/D)`, contradicting (12). Neither cover is inferred from
local rhombi, near-optimal density, or many approximate grid accesses. Without
such a bridge, the current C-II obligation remains a full-source finite competitor.

**Promotion recommendation:** preserve as an unreviewed report pending an
independent audit of the locality extension and the original-source quantifiers.
No numerical certificate is used as a substitute for that proof audit.
