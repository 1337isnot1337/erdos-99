> Generated reading edition · [exact source](../../../docs/reports/target_c_exact_phase_nested_bundle_tree_2026-10-01.md) · source SHA-256 `cbebdbf6396c3120bdf9a67d11d13bbfd9236325889e38917cadb1151dc81857`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-8BF2BF277956","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — exact-phase diameter rows form a nested opposed-bundle tree

`nested opposed-bundle classification -> exact-phase diameter support/rank ->
whole-bundle finite competitor or transverse-grid contradiction -> C-II branch
exclusion -> Level I after all remaining branches are excluded`.

**Date:** 2026-10-01.  
**Starting commit:** `14b2c4cfd7e4ff828fbe62a8cfefebb4ca121e79`.  
**State version:** `2026-09-14.audit.51`.  
**Branch/mission:** `swarm/sol/gap-stress-cycle-20261001`, exact-phase labeled gap
cycles and the proposed tree-leaf release.  
**Classification:** proved candidate awaiting independent audit/promotion.  
**Level I:** OPEN. This is a conditional branch theorem, not C-II closure.

## 1. Hypotheses and exact conclusion

Let P be a finite planar set with two-dimensional hull and diameter D. Select m
ordered disjoint proper crosscuts with nested shores, giving layers `0,...,m`.
On the cyclic order of actual diameter endpoints the layer blocks have the order

$$
0,1^+,\ldots,(m-1)^+,m,(m-1)^-,\ldots,1^-.
\tag{1}
$$

Some interior blocks may be empty. The two appearances of one interior layer are
distinct hull arcs and must not be identified geometrically.

Assume every contact crossing selected cut i has the same oriented unit vector u,
from the lower to the higher layers. Assume positive diameter weights `beta_h`
and positive contact cut masses `A_i` give the exact cut identities

$$
\sum_{h:\,p_h<i\le q_h}\beta_h r_h=A_i u,
\qquad A_i>0,
\tag{2}
$$

where a nonempty-support diameter h is oriented from its layer `p_h` to its
layer `q_h>p_h`, with `r_h=p_y-p_x`. Define

$$
c_h=r_h\cdot Ju,\quad I_h=[p_h+1,q_h],\quad
M_h=c_h\mathbf1_{I_h}.
\tag{3}
$$

Discard zero rows. Then the following conclusions hold.

1. The distinct intervals among positive-c rows form a chain under inclusion;
   the negative-c intervals also form a chain.
2. These two chains have exactly the same interval types. For each type I,
   independently,
   $$
   \boxed{\sum_{h:I_h=I}\beta_h c_h=0.}
   \tag{4}
   $$
   Each interval type therefore contains at least two actual diameter edges with
   opposite strict transverse signs.
3. If `rank M=m`, there are exactly m distinct interval types. Ordered from
   largest to smallest, they start at `[1,m]`, remove exactly one left or right
   endpoint at each step, and end at a singleton `[k,k]`.
4. Consequently the simple support of the gap multigraph is a tree with m edges,
   obtained by recursive deletion of an extreme ordered gap vertex. The full
   multigraph consists of opposed parallel bundles on this tree. In particular,
   $$
   \boxed{|\{h:c_h\ne0,\ I_h\ne\varnothing\}|\ge2m.}
   \tag{5}
   $$
5. Every nonempty-support diameter crosses the same selected cut k, including
   the possible diameter parallel to u. The actual diameter subgraph with
   nonempty support is bipartite and has no cycles; cycles in the gap quotient
   arise from identifying distinct source endpoints, not from actual diameter
   cycles.

The source theorem is (1)--(2) plus full rank. The contact-train extraction is
an explicitly unpromoted input; the geometry/linear algebra below is proved
directly. No statement is made about diameter edges with empty selected support.

## 2. Diameter endpoints and their normal order

For a diameter vector `r=b-a` and any other source point z, the upper distance
bound to b gives

$$
|z-b|^2\le D^2=|r|^2
\quad\Longrightarrow\quad
(z-a)\cdot r\ge |z-a|^2/2>0.
\tag{6}
$$

Similarly `(z-b) dot r <= -|z-b|^2/2<0`. Thus a and b uniquely minimize and
maximize the linear functional with direction r. In particular they are extreme
vertices. As the direction rotates, the minimum and maximum exposed vertices
follow convex-hull cyclic order monotonically. This elementary normal order is
the geometric input; no trail is inferred from incident edge order.

Work on F, the convex hull of all actual diameter endpoints. Its vertex order
inherits (1). Other source points, including contact isolates, are not discarded
from the source or from any eventual motion; F is only a device for normal order.

### Lemma 2.1 — a positive cut resultant locates the u-support faces

Suppose I and J are complementary nonempty cyclic vertex intervals of a strictly
convex polygon, and a family of actual diameter vectors joins I to J. If a
positive combination of these vectors is a positive multiple of u, the minimum
u-support face belongs to I and the maximum u-support face belongs to J.

**Proof.** The two finite vertex hulls are strictly separated by a line: a chord
through the relative interiors of the two transition sides separates the two
vertex intervals. Orient its normal phi from I toward J. Every diameter vector
r from I to J has `phi dot r>0`, so their directions admit one lift in an open
angular interval of length less than pi. Let theta_- and theta_+ be its extreme
diameter directions. Their positive combination has direction u between them.

The normal directions whose minimum support vertex belongs to one cyclic vertex
interval form one cyclic angular interval. If, while rotating from theta_- to
theta_+ along their short arc, the minimum support left I and returned to I,
the whole angular interval for minimum support in J would have to lie between
theta_- and theta_+. But the directions theta_-+pi and theta_++pi both have
minimum support in J, because the original maximum diameter endpoints lie in J.
They lie outside that short arc, a contradiction. Hence the minimum support
stays in I throughout. Apply the same argument to the maximum support to obtain
J throughout. Transition normals cause no exception: a face with one endpoint
in each class would have adjacent normal directions exposing J or I on the
forbidden side. The degenerate case theta_-=theta_+ follows directly from (6).
Therefore the assertion also holds at direction u. QED.

Apply the lemma to cut 1 in (2): its lower endpoint block is layer 0, and the
complement is the other layers. Thus the minimum u-support face of F is in layer
0. Apply it to cut m to place the maximum u-support face in layer m.

Both boundary arcs from these support faces to each other therefore have layer
indices nondecreasing from 0 to m, by (1).

## 3. Each transverse sign has nested interval support

Use u as angle zero. Rotate a diameter direction counterclockwise from u to -u.
The minimum support vertex travels on one of the two boundary arcs from layer
0 to layer m, while the maximum travels on the other arc from m to 0. Their
layer indices are respectively nondecreasing and nonincreasing.

Whenever the oriented diameter has positive transverse projection and is oriented
from a smaller to a larger layer, its angle is in `(0,pi)`. As these directions
increase, their endpoint layers `p_h` increase and `q_h` decrease. Hence their
nonempty support intervals `[p_h+1,q_h]` are nested.

Clockwise rotation from u to -u proves the same nesting for the negative-c
diameters. Empty-support diameters do not alter either monotonicity. Distinct
diameters parallel to u are impossible by (6), which identifies both endpoints;
if one exists its endpoint layers are 0 and m, so it has full support.

This proves conclusion 1. It also makes explicit why nesting requires the
positive **axial** cut resultants: transverse circulation alone did not locate
the two u-support faces in the exterior layers.

## 4. Equal nested profiles force bundlewise balance

Take the transverse component of (2). For every coordinate i,

$$
P_i:=\sum_{c_h>0}\beta_h c_h\mathbf1_{I_h}(i)
=\sum_{c_h<0}\beta_h(-c_h)\mathbf1_{I_h}(i)=:N_i.
\tag{7}
$$

We use an elementary uniqueness lemma.

### Lemma 4.1 — positive nested interval decomposition is unique

Suppose `I_1 strictly contains ... strictly contains I_s` are distinct nonempty
integer intervals and `lambda_j>0`. For
`f=sum_j lambda_j 1_(I_j)`, the interval types and their coefficients are
uniquely determined by f.

**Proof.** On `I_j\I_(j+1)`, with `I_(s+1)=empty`, f equals
`lambda_1+...+lambda_j`. All these values occur and increase strictly.
The corresponding nonempty positive superlevel sets are precisely the I_j.
Differences of consecutive positive levels recover the lambda_j. QED.

Combine repeated intervals on each side of (7) and use Section 3 to obtain two
positive nested interval decompositions of the same vector. Lemma 4.1 equates
their interval types and coefficients. This proves (4) and conclusion 2.

No KKT multiplier is discarded. The balance is an identity of the original
positive weights, not a newly chosen sparse stress.

## 5. Full rank forces one-at-a-time interval erosion

Let `I_1 strictly contains ... strictly contains I_s` be their common chain.
Its indicator vectors are independent: evaluate a dependence on each nonempty
shell `I_j\I_(j+1)` successively. Every nonzero row of M is a nonzero multiple
of one of these indicators, so

$$
\operatorname{rank}M=s.
\tag{8}
$$

If this equals m, the maximal interval contains all m coordinates, since no
column can be zero. Thus `I_1=[1,m]`. A chain of m nonempty proper nested
subintervals of an m-point interval must lose exactly one point at every step
and finish with one point k. Each removal is at a left or right endpoint.

Associate interval `[a,b]` to gap edge `{a-1,b}`. Initially this is `{0,m}`.
Each next edge replaces exactly one extreme endpoint with the adjacent ordered
gap vertex. The removed endpoint belongs to no later edge, so recursive leaf
elimination proves these m edges form a tree on all `m+1` gap vertices. This is
the simple support, not the full multigraph: every edge carries both signs and
at least two original diameter rows by (4). Hence (5).

Every support interval contains the last surviving cut k. Every actual diameter
with nonempty support therefore joins opposite shores of that cut. Those shores
are complementary hull intervals, so the actual diameter subgraph is bipartite.
The canonical diameter-thrackle/Woodall theorem gives no even cycle; see the
canonical `C-WOODALL` entry in the manifest and its registered proof report
`docs/reports/target_c_woodall_diameter_topology_2026-09-10.md`. Thus this
bipartite subgraph has no cycle. This optional forest statement uses that
canonical fact; the bundle and rank statements do not.

### 5.1 Exact axial reaction and strict angular variation

For each of the m bundle types, take its original positive-weight vector sum.
By (4) it is `K_j u`. All nonempty-support diameters cross cut k, whose two
hull intervals are strictly separated by a functional phi. Orient phi from
the lower to the higher shore. Every oriented diameter r has `phi dot r>0`;
(2) gives `phi dot u>0`. Therefore

$$
K_j>0,\qquad A_i=\sum_{j:i\in I_j}K_j.
\tag{13}
$$

Any parallel-u diameter is included in the maximal bundle and contributes
`beta_h D>0`. Since one coordinate is removed at each step, all m contact cut
masses A_i are pairwise distinct. Their level order is the erosion order;
they increase toward k on either side.

There is also a strict variation law that keeps the actual diameter directions.
Let

$$
W_j=\sum_{h:I_h=I_j,\ c_h>0}\beta_h c_h
=\sum_{h:I_h=I_j,\ c_h<0}\beta_h(-c_h)>0.
\tag{14}
$$

For a positive-c bar put `theta_h=arg(r_h)-arg(u)` in `(0,pi)`; for a negative
bar use the absolute clockwise angle in `(0,pi)`. Then

$$
{K_j\over W_j}
=\mathbb E_{j,+}[\cot\theta_h]
+\mathbb E_{j,-}[\cot\theta_h],
\tag{15}
$$

with each expectation weighted by `beta_h |c_h| / W_j`. For j=1 only, add the
nonnegative contribution of the possible parallel-u diameter divided by W_1.

On either sign branch every bar of bundle j precedes every bar of bundle j+1
in rotation away from u, by the strict interval erosion and normal order.
Distinct diameter edges cannot have the same projective direction, by (6).
Cotangent is strictly decreasing on `(0,pi)`. Consequently

$$
\boxed{{K_1\over W_1}>{K_2\over W_2}>\cdots>{K_m\over W_m}>0.}
\tag{16}
$$

Thus for a coordinate removed at stage s,
`A_i/P_i=(K_1+...+K_s)/(W_1+...+W_s)` is a weighted prefix average of a strictly
decreasing sequence, and strictly decreases with s. This is an exact reaction
variation statement, with no spacing or multiplier lower bound asserted.

The doubled-star regression satisfies this law. It therefore supplies a labeled
restriction, not a contradiction by itself.

## 6. Push toward closure: finite local train-shear release is obstructed

The exact laminar shear formula is

$$
p_x(\theta)=p_x+\sum_{i\le\ell(x)}(R_{\theta_i}u-u).
\tag{9}
$$

It preserves every old unit contact under the actual train-cut hypotheses. For
each active diameter its squared length has expansion

$$
L_h(\theta)=D^2+2M_h\theta+O(\|\theta\|^2).
\tag{10}
$$

Because every row weight is positive, `sum_h beta_h M_h=0`, and M has full
column rank, every nonzero theta has some `M_h theta>0`: otherwise positive
weighted cancellation would make every row zero, contradicting rank. Compactness
of the unit sphere gives a finite-source constant

$$
\kappa=\min_{\|z\|=1}\max_h M_hz>0.
\tag{11}
$$

The Taylor remainder is uniform across the finite active set. Therefore every
sufficiently small nonzero theta satisfies

$$
\max_h L_h(\theta)\ge D^2+2\kappa\|\theta\|-C\|\theta\|^2>D^2.
\tag{12}
$$

**Finite isolation conclusion.** No sufficiently small nontrivial endpoint of
the selected contact-preserving train-shear family has diameter at most D.
This rules out integrating a private *basis* leaf motion inside that family.
There is no claimed uniform radius in D, and it does not rule out a remote
feasible endpoint, additional degrees of freedom, or replacing source points.

## 7. The next attempted finite move and its exact failure

An exterior layer has one boundary contact family. With its contacts initially
oriented as u from that layer to the exterior, translating the layer by `2u`
reverses them to -u and preserves every old contact exactly. A moving diameter
r changes to `r-2u`, and shortens precisely when `r dot u>1`.

This is a real finite move, but it does not close the branch. Even when its
moving diameters satisfy that strict inequality, inactive source pairs can
block it. In particular, whenever an actual transverse grid row has the
consecutive exact-phase contact chain

$$
x,\quad x+u,\quad x+2u,
$$

with x in the translated exterior layer and the other two points fixed, the
move sends x **exactly onto** the third source point. The obstruction is a
two-step same-direction grid pair, not a retained rhombus diagonal. Thus the
earlier local diagonal-immunity result cannot justify this reflection move.

The required repaired finite theorem must control these additional pair
constraints or move additional layers/points. The erosion tree and bundle
balance supply no such control by themselves.

## 8. Dependencies, hostile checks, and remaining global scope

Canonical interpretation dependencies:

- `docs/theory/01-local-structure.md`, Theorem 4.1: KKT equilibrium and diameter
  endpoint extremality;
- `docs/targets/target-c/56-ci-restored-frontier.md`: actual contact/diameter
  full support for the lexicographic representative;
- `docs/targets/target-c/57-zr-zf-rigidity-audit.md`: rigidity on the nonisolated
  positive-contact core only;
- the canonical diameter-thrackle no-even-cycle input, only for the optional
  forest consequence in Section 5.

Explicitly unpromoted application dependencies, checked at their stated scopes:

- `research/target_c_laminar_multitrain_interval_shear_2026-09-15.md`: nested
  source shores, contact cutsets, interval supports, and exact formula (9);
- `docs/reports/target_c_complete_grid_rank_switching_2026-10-01.md`: rank m,
  from the preceding shear fields, core ZF, and an unselected train;
- the fixed-star/witness-cell extraction on starting main, only to apply this
  theorem to that extracted branch. This report does not promote that chain.

The preceding geometric regression realizes the extremal lower bound `2m` and
the doubled erosion star, including a common star witness and arbitrarily round
hulls. It therefore blocks an unsupported claim that conclusion 3 is itself a
contradiction. Its missing actual contact equilibrium is stated explicitly.

A discovery-only linear-program search over rational-circle diameter matchings
and cyclic layer blocks found 350 full-rank positive-cut-balanced instances
for m=2,3, all satisfying signwise nesting, the erosion classification, separate
bundle balance, and the strict ratio law. The discovered weights were checked
independently with Fraction arithmetic, including support-face location and
pairwise distinct axial masses. Run

```
python3 research/search_target_c_gap_normal_order_2026_10_01.py
```

It reports `LP_attempts=7168; exact_feasible=210` for m=2 and
`LP_attempts=45472; exact_feasible=140` for m=3, with zero uncertified successes
and zero counterexamples. LP-infeasible cases are not certified, and contacts,
vertex KKT, and global optimality are omitted. This was an adversarial search,
not a proof of absence of regressions or a global-optimality test. No numerical
survival is needed for the arguments above.

No canonical state is changed. The exact next obligation is a finite release
of an **entire opposed parallel bundle**, compatible with all source pairs and
the transverse complete train shore, or a source theorem excluding this bundle
tree using actual unit-contact geometry. A basis leaf and a diameter forest are
insufficient. Nonconstant phase, split-star O-O, inactive interfaces, macroscopic
inactive chambers/exterior caps, and other full-core branches remain open.
