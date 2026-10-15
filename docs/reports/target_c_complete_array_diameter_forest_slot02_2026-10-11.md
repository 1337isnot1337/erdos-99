<!-- theorem-state: {"artifact_id":"ART-3C9F1FD6D089","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II: the actual diameter graph of a complete bent rhombic array is a forest

**Date:** 2026-10-11. **Worker:** 02.  
**Base main:** `ab6dd3336f9f8d440f2bada76edb32153391cddc`.  
**Theorem state:** `2026-10-10.audit.234`.  
**Starting checkpoint:** `74ed590654e177b2befda828de5d6d7efcc16ccc`.  
**Branch / PR:** `research/sol61-slot02-20261010-integrated-fold`,
[PR #948](../publication/provenance.md#source-records).  
**Classification:** proved candidates awaiting independent mathematical audit;
unreviewed and noncanonical. **C-II AND LEVEL I REMAIN OPEN.**

## 1. Exact theorem and implication chain

Let a finite planar configuration be a complete labelled additive array

`P_ij=x_i+y_j`, `0<=i<=a`, `0<=j<=c`, `a,c>=1`,

with distinct labels at distinct points. Its consecutive row and column edges
are unit contacts and its cells are actual strict triangle-free rhombi, with
one consistent orientation. The directions of the vectors

`u_i=x_(i+1)-x_i`, `v_j=y_(j+1)-y_j`

may vary. Completeness means **every** index pair is an actual source label;
virtual rectangular completion of an incomplete domain is not permitted.

**Theorem 1.1 (proved candidate).** The full actual diameter graph of this array,
on its incident vertex set, has no odd cycle. It is therefore a caterpillar
forest by the canonical straight-line diameter-thrackle classification.

The theorem does not assume source global optimality, KKT equilibrium, or
contact minimality. Those hypotheses enter only its following application.

**Corollary 1.2 (proved candidate).** Suppose the array is the **entire** contact
core of a canonical triangle-free global source with `D>=9`, retaining every
source isolate. Then

`d_H+s_Z=2`, `d_H>=1`,

so only

`(s_Z,d_H)=(0,2)` or `(1,1)`

remain: two caterpillar diameter components or one. The former complete-array
candidate also allowed `(2,0)`; the cyclic case is now excluded. Isolates need
not be absent, moved, or dropped for this source-level diameter conclusion.

```text
actual complete bent array
 -> two tangent windows with total width below pi/3
 -> two disjoint banks of actual diameter edges
 -> a mixed odd cycle must use both opposite-corner diagonals
 -> one bank supplies an even path and the other an odd path
    with exactly the same endpoint distance
 -> short-window path norm bounds are incompatible
 -> no odd diameter cycle
 -> for a canonical whole-core array, s_Z<=1 and d_H in {1,2}
```

This removes one actual diameter-topology class under the complete-array
hypothesis. It does not extract that hypothesis from a general quadrilateral
disk, bound the required outside isolate population, or construct a full-source
finite improvement.

## 2. Canonical inputs and scope

The geometric proof uses only the full finite diameter upper bound and the
strict rhombic angle window. Its forest conclusion uses
[the promoted Woodall diameter topology](target_c_woodall_diameter_topology_2026-09-10.md):
a finite straight-line diameter graph with no odd cycle is a caterpillar
forest. No selected positive support is substituted for the actual graph.

For the canonical application use:

- [Local structure](../theory/01-local-structure.md), Lemma 5.1 and Theorem 6.1:
  a diameter endpoint is strictly exposed; a nonisolated vertex without
  diameter incidence is strictly surrounded.
- [Rhombus population audit](../targets/target-c/67-rhombus-population-transport-audit.md):
  actual contact cells are strict rhombi with angles in `(pi/3,2pi/3)`.
- [ZR/ZF](../targets/target-c/57-zr-zf-rigidity-audit.md): `s_Z>=0`, and all old
  actual diameter endpoints lie in the nonisolated positive-contact core.

The preceding unreviewed
[dual-defect report](target_c_rhombic_quarter_fold_dual_defect_slot02_2026-10-10.md)
proves the complete-array loaded count and isolate burden. Section 7 below
rederives the needed loaded count; Theorem 1.1 does not use that report as an
unqualified canonical premise.

All pairs used in the proof are pairs of actual array labels. Contact-isolated
source labels are retained in the canonical application. They have no old
actual diameter incidence by canonical normalization, so the array's diameter
graph is exactly the old full-source diameter graph in that application.

## 3. A finite diameter-path lemma

Consider distinct vertices `p_0,...,p_k` in a finite planar set of diameter at
most `D>0`. Suppose each consecutive pair has length exactly `D`. Suppose,
after alternating the edge orientations, their unit vectors `n_1,...,n_k`
all lie in one angular interval of width `omega<pi/3`:

`p_j-p_(j-1)=(-1)^(j-1) D n_j`.

The same statement applies with an overall minus sign. No unit-contact,
KKT, or source-density premise is imposed here.

**Lemma 3.1 (proved candidate).** If `k>=2`, the arguments of the `n_j` are
strictly monotone along the path. Moreover

```text
k even: |p_k-p_0| <= 2D sin(omega/2),
k odd:  |p_k-p_0| >= D(2cos(omega/2)-1).
```

For `k=1` the latter bound is immediate.

**Monotonicity proof.** Three consecutive oriented unit vectors `A,B,C` give
an actual source displacement `D(A-B+C)`, up to overall sign. Its endpoint
upper bound gives

`|A-B+C|^2-1=2(A-B) dot (C-B)<=0`.

Writing their arguments as `alpha,beta,gamma`, respectively,

`(A-B) dot (C-B)`
`=4 sin((alpha-beta)/2) sin((gamma-beta)/2) cos((alpha-gamma)/2)`.

The cosine is positive because the interval has width below `pi`. Two
adjacent arguments cannot agree: their diameter edges share a path vertex,
so agreement would repeat the other endpoint. Thus `beta` must be strictly
between `alpha` and `gamma`. Every three consecutive arguments have this
property, so the entire sequence is strictly increasing or strictly decreasing.

Reverse the angular order if necessary. Write `n(t)=(cos t,sin t)` and let
`theta_1<...<theta_k`; put `w=theta_k-theta_1<=omega`.

**Even path.** For `k=2r`,

`(p_k-p_0)/D=-integral_E n'(t) dt`,

where `E` is the union of the disjoint intervals
`[theta_1,theta_2],...,[theta_(2r-1),theta_(2r)]`.
Since `n'(s) dot n'(t)=cos(s-t)>0` over the whole interval `I=[theta_1,theta_k]`,

```text
|integral_E n'|^2
 =integral_(E times E) cos(s-t) ds dt
 <=integral_(I times I) cos(s-t) ds dt
 =|n(theta_k)-n(theta_1)|^2
 =4sin^2(w/2).
```

This proves the even bound without charging path length or counting repeated
increments as independent displacement.

**Odd path.** For `k=2r+1`,

`(p_k-p_0)/D=n(theta_k)-integral_E n'(t) dt`,

with the same first `r` paired intervals. Project on the midpoint direction
`e=n((theta_1+theta_k)/2)`. The scalar function `e dot n(t)` is cosine on
`[-w/2,w/2]`. Its total positive variation is `1-cos(w/2)`, so its increment
over any union of subintervals is at most that number. Therefore

`e dot (p_k-p_0)/D >= cos(w/2)-(1-cos(w/2))=2cos(w/2)-1`.

The right side is positive. Taking norms and using `w<=omega` proves the odd
bound. Every three-edge and endpoint upper bound in this proof is an actual
pair constraint; existence of an abstract diameter path alone would be weaker.

**Lemma 3.2 (proved candidate, parity incompatibility).** An even diameter path
and an odd diameter path cannot have equal nonzero endpoint distances if their
two oriented direction-window widths `u,v` satisfy `u+v<pi/3`.

Indeed, writing `t=u/2`, `v/2<pi/6-t` gives

```text
2cos(v/2)-1
 >2cos(pi/6-t)-1
 =sqrt(3)cos t+sin t-1
 >2sin t,
```

because `sqrt(3)cos t-sin t=2cos(t+pi/6)>1` for `0<=t<pi/6`.
The odd lower bound thus strictly exceeds the even upper bound. The threshold
is sharp: an equilateral diameter triangle gives an even two-edge path with
width `pi/3` and the same endpoint distance as its odd one-edge path of width
zero. At a large scaling this has no unit-contact triangle; the sharpness
concerns diameter geometry, not the forbidden contact triangle.

## 4. The two actual diameter banks

Choose real lifts of the direction arguments such that every cell has

`pi/3<arg(v_j)-arg(u_i)<2pi/3`.

This is possible simultaneously: fix one family vector and use the common
strict angle interval, with the consistent cell orientation. The resulting
provisional lifted differences are between zero and `pi`; no `2pi` wrap
remains, so the strict cell window holds for every lifted pair. Let `I_u,I_v`
be the smallest intervals containing the two families, with widths
`Delta_u,Delta_v`. The all-crossing inequalities imply

```text
min I_v-max I_u>pi/3,
max I_v-min I_u<2pi/3,
Delta_u+Delta_v<pi/3.                         (4.1)
```

For a diameter pair `p,q`, write `n=(p-q)/D`. Squared upper bounds give

`n dot (z-p)<=-|z-p|^2/(2D)<0` for every other actual source label `z`.

Thus `p` uniquely maximizes support in direction `n`. Completeness of the
array makes `x_i` and `y_j` separately maximize their support in that direction
when `p=x_i+y_j`.

If `i` is an interior column index, the two adjacent `x` labels give
`n dot u_(i-1)>0` and `n dot u_i<0`. Hence, projectively, `n` is perpendicular
to a direction between those two vectors in `I_u`. If `j` is an interior
row index, the analogous fact puts its projective normal in `J I_v`.
The two projective normal intervals are disjoint, with their acute separation
strictly greater than `pi/3` by (4.1). A diameter endpoint cannot have both
indices interior.

Classify each noncorner loaded endpoint as `X` if its column index is interior,
or `Y` if its row index is interior. A diameter edge with an `X` endpoint has
direction in `J I_u`; one with a `Y` endpoint has direction in `J I_v`. No edge
can touch both types.

A corner cannot be incident to an edge of each type either. Two diameter
partners of one point have angular separation at most `pi/3`, since their
distance is at most `D`; their projective separation is consequently at most
`pi/3`. The two bank intervals instead have projective separation greater than
`pi/3`. Thus the vertex sets of the edge banks `H_X,H_Y` are disjoint,
including at corners.

No diameter pair has a common row or column index. For example, a putative
same-row diameter `r=x_i-x_k` has `|r|=D`. For any nonzero difference
`s=y_l-y_j`, completeness supplies both cross pairs `r+s,r-s`, whose upper
bounds would give `2|r|^2+2|s|^2<=2D^2`, a contradiction.

The only remaining corner-corner diameter edges are therefore the two
opposite-corner diagonals, denoted `E_0`. Every other actual diameter edge
belongs to one bank. `H_X` is bipartite between rows `0,c`; `H_Y` is bipartite
between columns `0,a`.

We also need actual **oriented** direction windows for Lemma 3.1. Orient an
`X` edge from row zero to row `c`. A perpendicular `Jw` with `arg w in I_u`
has positive dot product with every `v_j`. The support-maximizing row endpoint
is therefore row `c`, and the minimizing one is zero. The oriented diameter
vector belongs to the one interval `J I_u`, not a union of antipodal intervals.
Orient a `Y` edge from column zero to column `a`; the same argument puts it
in the single interval `-J I_v`. Their widths are `Delta_u,Delta_v`.

## 5. An odd cycle would violate path parity

Suppose the full actual diameter graph has an odd simple cycle. It cannot
lie within one bank, which is bipartite. Bank vertex sets are disjoint, so
switching banks requires a corner diagonal. There are at most two such edges;
a mixed simple cycle must use both. Removing them from that cycle leaves one
path in `H_X` and one in `H_Y`, with all four corners as their four endpoints.
A corner with only a diagonal and no bank edge cannot occur on the cycle.

There are three ways to divide four corners into two endpoint pairs:

- If the `X` path joins the two corners in one row, it is even. The `Y` path
  joins the two corners in the other row, so it is odd. Both endpoint distances
  are exactly `|x_a-x_0|`.
- If the `X` path joins the two corners in one column, it is odd. The `Y` path
  joins the two corners in the other column, so it is even. Both endpoint
  distances are exactly `|y_c-y_0|`.
- If the endpoint pairs are diagonal, each pairs the endpoints of one removed
  diagonal. Reattaching it closes a separate cycle, so these paths cannot
  arise from one mixed simple cycle. Their two odd bank-path parities also
  give an even total after adding both diagonals. No parity case is discarded.

The first two cases contradict Lemma 3.2 and (4.1). This proves there is no
odd cycle. Applying the promoted geometric diameter-thrackle classification
gives the forest conclusion. The proof remains valid if one bank is empty:
then no mixed odd cycle is possible at all.

## 6. Hostile scope checks

The proof uses a complete actual array at four separate steps: support in
each summand, the same-index cross-pair contradiction, the identical distances
between paired corners, and the all-crossing angle budget. A partial rhombic
disk need not supply any of these missing labels or constraints. No result for
such a disk is asserted.

The alternating path orientations are essential. Consecutive incident diameter
states alone do not define a path; Lemma 3.1 assumes distinct successive path
vertices and uses their actual three-step endpoint constraints. It is not an
Euler-trail argument.

The path norm bounds do not count each diameter step independently, and require
no common negative gap or stress-weight lower bound. Their constants are
dimensionless and scale with the actual diameter `D`.

No old inactive upper constraint is omitted: monotonicity explicitly uses
`|p_(r+3)-p_r|<=D`; the bank proof uses cross pairs and support against every
actual summand. Isolates are not transported. In the canonical application they
stay in the original source and its global comparisons.

## 7. Canonical application and the remaining full-source obligation

For a canonical whole-core array, interior vertices have degree four and are
unloaded; the four degree-two corners are loaded. At each interior column index,
the two opposite outer vertices have bounded-face angle sums `pi-delta` and
`pi+delta`, where `delta` is the nonzero signed turn of consecutive `u` vectors.
If `delta=0` the vertex is the midpoint of two unit neighbors and fails both
strict exposure and strict surrounding, contrary to contact minimality. Thus
exactly one of the two opposite vertices is loaded. The same holds for every
interior row index. Therefore

`q=4+(a-1)+(c-1)=a+c+2`.

Euler gives `e=2v-2-(a+c)`, so

`d_H+s_Z=q-h+e+h-(2v-2)=2`.

Theorem 1.1 makes `d_H>0`; old ZF makes `s_Z>=0`. Hence only `(s_Z,d_H)=(0,2)`
and `(1,1)` remain. This proves Corollary 1.2.

The earlier complete-array core fold still preserves the full pair-distance
multiset. Any feasible full-source extension, after the canonical isolate
normalization, preserves the number of actual diameter pairs. This new result
does not convert that identity into diameter loss. The exact isolate burden
from the preceding report remains

`|Z|>(pi/(2sqrt(3))-2/3)D^2-sqrt(8/3)D`.

The next precise obligation for this supplied-array branch is an actual-source
capacity bound contradicting that burden, or a same-cardinality finite contact
loss/strict-diameter competitor, now under only the **one- or two-caterpillar**
diameter alternatives. A general source-level array extraction is separately
missing. C-II and the original Level I quantifiers are unchanged.

**Subsequent candidate checkpoint (same day):** the
[source boundary-attachment report](target_c_large_array_boundary_attachment_slot02_2026-10-11.md)
uses global source circumradius to exclude the entire canonical whole-core
complete-array model for sufficiently large `D`, including both forest
alternatives and every isolate population. It therefore replaces the
supplied-array capacity obligation just stated with actual-array extraction
or an endpoint for the complementary incomplete domain. Neither result is
promoted; the finite forest theorem remains independently applicable.

## 8. Reproducible finite checks

Run

`python3 research/verify_target_c_complete_array_diameter_forest_2026_10_11.py`.

Saved output is
[`target_c_complete_array_diameter_forest_certificate_2026_10_11.json`](../../research/target_c_complete_array_diameter_forest_certificate_2026_10_11.json).
The checker verifies the exact three-edge monotonicity identity, every pair
of its finite rational diameter-path fixtures, even/odd endpoint bounds, the
strict combined-window constants, all corner-pair parity allocations, and the
exact 60-degree sharpness case. It also checks the actual full diameter graphs
of 81 rational complete unit-array fixtures. A separate nine-point additive
set has an exact odd diameter triangle but lacks actual unit cells, guarding
against dropping the strict source-cell hypotheses.

These computations use rational arithmetic and `Q(sqrt(3))`. They do not encode
arbitrary source extraction, KKT, canonical globality, universal angular-window
lifting, or the full analytic path integral argument. They certify finite
examples and arithmetic, not a proof by enumeration. The universal proof is
Sections 3--5 above. No canonical dependency or certificate registration is
modified and no independent audit is claimed.
