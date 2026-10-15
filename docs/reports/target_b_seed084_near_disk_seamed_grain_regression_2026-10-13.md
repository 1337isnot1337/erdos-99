<!-- theorem-state: {"artifact_id":"ART-6625E591347E","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-b"} -->
# Target B: near-disk seamed grains inside the strict scalar shell window

**Date:** 2026-10-13\
**Research seed:** 84, generated once with `secrets.randbelow(100)+1`\
**Category:** Target B: Global shell stability\
**Base commit:** `ab6dd3336f9f8d440f2bada76edb32153391cddc`\
**State version:** `2026-10-10.audit.234`\
**Run type:** closing attack, exact falsification, hostile scope check\
**Active prompt:** `docs/prompts/erdos_problem_99_GPT6_ASTRA_FULL_SOLUTION_PROMPT.md`\
**Classification:** proved candidate regression awaiting independent review;
repository lifecycle **unreviewed**, noncanonical\
**External literature:** none imported\
**Certificate:** `research/seed084/verify_seamed_grains.py` and
`research/seed084/certificate.json`

## LEVEL I STATUS

**STILL OPEN.** The sources constructed below are explicitly nonglobal. They
are not counterexamples to Erdős #99 or to the canonical jammed shell theorem.

## 1. Closing obligation and three mechanisms

The canonical Target B endpoint is

\[
 G+E\ge c_0B+a_0(t+\chi-1),\qquad
 a_0=\sqrt3/2,\quad c_0=a_0/2.
\]

Section 36 gives the strict reverse inequality for a global minimizer.
The intended chain was

```text
source-level joint physical/interface/virtual transfer
 -> exact topology-corrected shell inequality
 -> contradiction to global optimality in Target B.
```

This still needs actual global optimality and the branch hypotheses; a
Target B result alone must not be promoted to coverage of all Level I cases.

Three mechanisms were tested.

1. **Static interface payment.** Could disk roundness, optimal leading
   population, connected contacts, and even the strict n-1 comparison repair
   the far-from-optimal static determinant regression? The new construction
   proves they cannot. Its scalar window is exactly the canonical one, with
   the actual topology and full population retained.
2. **Common phase contraction.** The acyclic phase potential decreases area
   defects, but supplies no sign for actual diameters. Already the four-point
   unit rhombus has long diagonal squared `2+2 cos(theta)`, which *increases*
   when `theta>pi/3` is flattened toward `pi/3`. This is a diagnostic of this
   attempted mechanism, not a new general theorem or a canonical regression.
   The full-pair seam calculation below handles the same issue explicitly.
3. **Whole-source replacement.** For the constructed sources a triangular
   crop with exactly the same labels is a strict competitor. This succeeds
   and certifies nonglobality. No theorem extracts such a crop from an
   arbitrary canonical multi-grain source. That extraction is the remaining
   bridge, rather than the scalar n-1 allowance.

Open PR #949 was inspected: its zero-deficit aggregate and far-from-optimal
connected two-grain example are not premises here. PR #956's population
reserve and interface payment candidates are also not used. The distinction
of this regression is the simultaneous strict comparator, near-disk shape,
connected contacts, positive grain deficits, and explicit nonglobality.

## 2. Precise new regression theorem

There is an unbounded sequence of finite planar sources `A_k` with
`n_k=|A_k|`, minimum separation exactly one, and `D_k=diam(A_k)->infinity`,
having all the following properties.

1. The unit-contact graph is connected and triangle-free. The population is
   partitioned into two exact nontriangular unit-lattice charts. Every
   contact between the charts is one specified bridge edge. Every bounded
   contact face is a strict unit rhombus within one chart.
2. With `K_k=conv(A_k)`, after translation and division by `D_k`,
   `K_k` tends to the disk of diameter one. Uniformly in direction,
   `w(K_k)=D_k-O(1)`, `pi D_k-per(K_k)=O(1)`, and
   `pi D_k^2/4-area(K_k)=O(D_k)`. Also
   \[
   n_k={\pi\over2\sqrt3}D_k^2+O(D_k),\qquad
   D_k^2<{2\sqrt3\over\pi}(n_k-1).
   \tag{2.1}
   \]
3. Let `R_k` be the rhombus count, `B_k` its boundary-edge occurrence
   count, `chi_k` the Euler characteristic of the actual rhombic complex,
   and `t_k` the source population outside that complex. Then
   \[
   n_k=R_k+B_k/2+\chi_k+t_k,\quad
   G_k=O(D_k),\quad E_k=o(1),\quad
   B_k=O(D_k),\quad |\chi_k|+t_k=O(D_k).
   \tag{2.2}
   \]
   In particular the *strict* shell upper side holds:
   \[
   G_k+E_k<c_0B_k+a_0(t_k+\chi_k-1).
   \tag{2.3}
   \]
   The usual Oler lower side holds too, since the sources are unit-separated.
4. For the actual rhombic trains in the two chart regions, put
   \[
   M_{\rm inter}=
   \sum_{\tau\text{ in lower},\ \sigma\text{ in upper}}
       |\det(u_\tau,u_\sigma)|.
   \]
   All these pairs are physically noncrossing. Their mass satisfies
   \[
   {M_{\rm inter}\over D_k^2}\longrightarrow
      {1\over2}+{1\over\sqrt3}>0.
   \tag{2.4}
   \]
   Each chart contains a macroscopic coherent train component; neither
   relies on a vanishing-deficit endpoint. If `M>=b` are its two direction
   populations and `R_j` its rhombus count, then
   \[
   {Mb-R_j\over M^2}\longrightarrow
   {4\sqrt3+6-3\pi\over7\sqrt3+12}\in(1/8,1/6).
   \tag{2.5}
   \]
   Here train counts refer to all rhombic trains in each chart region;
   any boundary components outside its macroscopic component affect the
   normalized quantities by `o(1)`.
5. There is an explicitly identified unit-separated triangular-lattice
   source `A_k^0` with **the same number of labels** and
   \[
      \operatorname{diam}(A_k^0)<D_k.
   \tag{2.6}
   \]
   Thus every `A_k` is rigorously nonglobal.

Consequently, for every fixed constant `C`, the proposed estimate

\[
 M_{\rm inter}\le
 C\bigl(G+E+B+|t+\chi-1|+1\bigr)
 \tag{2.7}
\]

is false on the class just specified, even after imposing connected
contacts, near-disk geometry and (2.1)--(2.3). A static proof using only
these conditions cannot supply the required global transfer. No version
with actual global-minimizer/jammed hypotheses is falsified.

## 3. Complete construction and proof

### 3.1 A full triangular crop with strict scalar allowance

Let `Lambda` be the unit triangular lattice. For each sufficiently large
integer `m`, set

\[
 r=\sqrt{a_0m/\pi}.
\]

Use the translated open-disk counting argument of canonical Target B
Section 36: the lattice count has integer mean `m`, is nonconstant, and
some translation contains at least `m+1` sites. Take **all** those sites
as `A^0`; put `n=|A^0|` and `D_0=diam(A^0)`. Then

\[
 D_0<2r,\qquad 4r^2={2\sqrt3\over\pi}m
      \le {2\sqrt3\over\pi}(n-1).
 \tag{3.1}
\]

An elementary fundamental-cell cover gives
`n=pi r^2/a_0+O(r)`, uniformly in the chosen translation. Represent the
disk center modulo the lattice in one bounded fundamental cell. No labels
are discarded at any later stage.

The crop has hull containing the disk of radius `r-C`, for an absolute
constant `C`: for any supporting direction, a lattice site within bounded
distance of `(r-2)e` lies in the open disk and has support at least `r-C`.
Thus `D_0=2r-O(1)`.

### 3.2 Choose a shear that strictly enlarges an actual old diameter

Take an actual diameter difference of `A^0`. In a triangular basis
`u=(1,0), v_0=(1/2,sqrt(3)/2)`, write it as `a u+b v_0`; its squared
length is `N=a^2+ab+b^2=D_0^2`. Under the three 60-degree changes of
basis, the coefficient products are

\[
 ab,\quad -b(a+b),\quad -a(a+b).
\]

Their sum is `-N`. Choose the basis for which
`ab<=-N/3<0`. In particular the diameter endpoints have different row
indices. This is a change of lattice coordinates, not a rotation or
selection of a different source.

Replace `v_0` by

\[
 v=(\cos\theta,\sin\theta),\qquad
 \theta=\pi/3+\delta,\quad 0<\delta<\pi/12,
\]

and keep `u` unit and horizontal. Map every original label `(i,j)` to
`p_{ij}=t+i u+j v`, with the same fixed translation `t`.
The selected pair has squared length

\[
 |a u+b v|^2=N+2ab(\cos\theta-1/2)>N.
 \tag{3.2}
\]

Every nonzero vector of this lattice has length at least one, and its only
unit vectors are `+/-u,+/-v`: for integers `i,j`,

\[
 i^2+j^2+2ij\cos\theta\ge i^2+j^2-|ij|\ge1,
\]

and equality in the interior angle range requires an axis unit vector.
Thus the sheared source is unit-separated and its contact graph is a
square-grid subgraph, with no triangle.

Since `D_0<2r` is strict and the source is finite, choose `delta>0`
sufficiently small that the full sheared diameter is still below `2r`.
Additionally require `delta<=r^-4`. This guarantees that the positional
change is `O(r delta)=o(1)` and the summed rhombus area surplus is `o(1)`.

### 3.3 Open all seam contacts except one, preserving every source pair

Choose a row cut `s+1/2` between the two selected old diameter endpoints,
within half a row of their row midpoint. The physical midpoint of a
diameter pair is at distance `O(sqrt(r))` from the disk center, because

\[
 |(x+y)/2|^2+|x-y|^2/4=(|x|^2+|y|^2)/2\le r^2,
\]

and `|x-y|=2r-O(1)`. Thus both sides of this cut contain macroscopic
half-disk populations. Partition labels into lower `j<=s` and upper
`j>=s+1`.

The only cross-cut contacts of the sheared source are pairs of difference
`v`. Their upper endpoints lie on row `s+1`, say
`q_i=t+i u+(s+1)v`. Let `q_*` have the **largest** index `i_*` among
such pairs. This contact exists because the cut lies deep inside the crop.
Keep every lower label fixed, and rotate **every upper label** clockwise
by `eta>0` about `q_*`.

For a former cross contact with upper endpoint `q_i=q_*+k u`, `k=i-i_*<=0`,
the new difference is exactly

\[
 v+k w,\qquad w=(R_{-\eta}-I)u.
\]

For `0<eta<pi/2` and `pi/3<theta<pi/2`,

\[
 v\cdot w=\cos\theta(\cos\eta-1)-\sin\theta\sin\eta<0.
\]

Therefore

\[
 |v+k w|^2=1+2k(v\cdot w)+k^2|w|^2
 \begin{cases}=1,&k=0,\\>1,&k<0.\end{cases}
 \tag{3.3}
\]

This is a simultaneous exact check of **all** old seam contacts, not a
collection of one-at-a-time moves. Unit contacts within either chart are
preserved by its rigid rotation (or lack of rotation).

All remaining pairs were strictly above one before the hinge. Define
`ell` as their minimum distance minus one; `ell>0`. Let `M` be the
diameter of the sheared source, `g=2r-M>0`, and let `h>0` be the
selected pair's length increase in (3.2). Rotation about `q_*` moves any
upper label by at most `eta M`; pair distances change by at most `2 eta M`.
Choose

\[
 0<\eta<\min\{\pi/4,\delta r^{-4},\ell/(4M),g/(4M),h/(4M)\}.
 \tag{3.4}
\]

Every remaining pair stays strictly above one; **every** pair stays below
`2r`; the selected old diameter remains strictly above `D_0`. These finite
minimum margins are positive and explicit. There is no uniform slack
assumption, infinitesimal-to-finite inference, or omitted source pair.

The resulting source `A` has exactly one cross-chart contact and retains
all `n` labels. Its only contacts are the internal `u/v` grid contacts
and that bridge, hence it is triangle-free. Equations (3.1)--(3.4) give
both the strict scalar comparison and the smaller-diameter competitor:

\[
 D_0<D<2r\le\sqrt{{2\sqrt3\over\pi}(n-1)}.
 \tag{3.5}
\]

### 3.4 Connectivity and face accounting

For completeness the `u/v` contact graph of each half-crop is connected
for sufficiently large `r`. In original triangular coordinates, row `j`
contains an integer interval with center `c_j` and half-length `a_j`;
adjacent centers differ by `1/2`, and physical row heights differ by
`h_0=sqrt(3)/2`. If adjacent occupied rows both have `a_j>=1`, their
coefficient intervals overlap in length at least `3/2` and contain a
common integer, producing a `v` edge. If one has `a_j<1`, it is a cap
row. Its inward neighbor has half-length squared at least
`2h_0 sqrt(r^2-1)-h_0^2`, which exceeds `4` for large `r`, and contains
every integer of the cap row. The outward neighbor is beyond the disk.
All rows except possible terminal cap rows have half-length at least one,
so occupied rows are consecutive. This argument applies to either
contiguous half of the row interval. Each row is connected by `u` edges.
The one retained bridge consequently connects the entire source graph.

The bounded faces inside either half-crop are precisely the elementary
grid rhombi. A larger bounded grid face would enclose an omitted lattice
site; convexity of the original disk and the row half-plane would require
that site and the intervening grid edges to be present. A single bridge
between the two halves creates no additional bounded face. Rigid rotation
of one half and (3.3)--(3.4) preserve this description: unit contact edges
cannot cross in a unit-separated planar source, and no new contact appears.

Let `U` be the union of these actual closed rhombi, with all their edges
and vertices. Count its actual Euler characteristic `chi` and boundary
edge occurrences `B`, and let `t=|A\V(U)|`. Since
`4R=2e_U-B` and `chi=|V(U)|-e_U+R`, exactly

\[
 n=R+B/2+\chi+t.
 \tag{3.6}
\]

This includes any thin extremal rows, bridge residue and vertices outside
the rhombic complex. No source label is thrown away.

### 3.5 Geometry, topology, and the exact shell window

The source remains `o(1)` from its original disk crop. Thus its hull is
between disks of radii `r-C-o(1)` and `r+o(1)`. It has
`D=2r-O(1)`, uniform width `D-O(1)`, perimeter `pi D-O(1)`, and area
`pi D^2/4-O(D)`.

All crop sites/cells away from a fixed-width outer collar and seam collar
belong to the actual rhombic complex. Fundamental-cell counting bounds
these collar populations by `O(r)`, uniformly over translations. Hence
`R=n-O(r)`, `B=O(r)`, `t+|chi|=O(r)`, and `G=area(K)-area(U)=O(r)`.
All rhombi have area `sin(theta)`, so
`E=R[sin(theta)-a_0]=O(r^2 delta)=o(1)`.

Using (3.5), the isodiametric inequality and (3.6),

\[
 G+E=\operatorname{area}(K)-a_0R
 <a_0(n-1-R)=c_0B+a_0(t+\chi-1).
 \tag{3.7}
\]

Oler gives the lower side
`G+E>=c_0(B-per(K))+a_0(t+chi-1)`. Thus these sources satisfy the
entire scalar shell window, not just its leading-order relaxation.

### 3.6 Train counts, positive deficits, and virtual mass

In triangular coordinates the limiting upper half-disk has row-index
range of length `2r/sqrt(3)`. The other coefficient is
`i=x-y/sqrt(3)`; on `x^2+y^2<=r^2, y>=0` its extremes are
`r` and `-2r/sqrt(3)`. Its range has length `(1+2/sqrt(3))r`.
The lower half has the same range lengths. The cut is displaced only
`O(sqrt(r))`, and fundamental-cell/collar errors do not affect normalized
limits.

Each column of elementary rhombi is one `u` train and each row is one
`v` train. The anchor set of cells is an intersection of four translated
disks with the row half-plane, so each such row/column is an interval.
To justify the count without assuming a lattice discrepancy theorem,
shrink the radius by a fixed constant: every integer row/column whose
slice has length at least two then contains an elementary cell. The
discarded slices lie in arbitrarily small normalized neighborhoods of
the projection endpoints. Squeezing, then letting those neighborhoods
shrink, gives

\[
 M=(1+2/\sqrt3)r+o(r),\qquad b=(2/\sqrt3)r+o(r),\qquad
 R_j={\pi\over\sqrt3}r^2+o(r^2).
 \tag{3.8}
\]

For a fixed positive `epsilon`, cell centers at least `epsilon r` inside
the limiting half-disk can be joined to one central cell by lattice
staircase paths staying within a fixed distance of the connecting line
segments. Convexity and the `epsilon r` margin keep these paths inside
the actual cell-anchor domain for large `r`. This gives an edge-connected
central cell region. All rows/columns except an `O(epsilon r)+o(r)`
projection band intersect that region. Letting `epsilon` tend to zero
after `r` tends to infinity shows that peripheral separate train
components have `o(r)` trains. In particular both charts have a coherent
macroscopic train component and a complete linear-by-linear central grid.

Dividing `Mb-R_j` by `M^2` gives (2.5). Its membership in `(1/8,1/6)`
is verified by rational bounds for pi in the certificate. Thus the
regression belongs to a fixed-positive-deficit regime, rather than the
zero-deficit regime of PR #949. Its total train ratio tends to
`T/D=1+4/sqrt(3)`, above the canonical pure-disk train-ratio floor.

There are no physical inter-chart rhombi or inter-chart train crossings:
the only cross contact is the bridge. Identically oriented cross pairs
have determinant `o(1)`, and differently oriented ones have determinant
`a_0+o(1)`. Hence

\[
 M_{\rm inter}=2a_0 Mb+o(r^2)
 =(2+4\sqrt3/3)r^2+o(r^2).
\]

Since `D/r->2`, this proves (2.4). Equations (2.2) and (2.4) disprove
(2.7) for every fixed `C`. Equation (3.5) separately certifies
nonglobality. This completes the regression proof.

## 4. Exact rigidity gate: why the regression is not a jammed source

The following useful finite gate is also proved here, but is not a claim
that canonical phase grains are exact lattices.

Partition an arbitrary finite unit-separated source into nonempty sets
`A_j`, each contained in a unit-separated nontriangular lattice. Let
`q` count all actual diameter endpoints, and let `e_X` count contacts
between distinct sets. A unit-separated nontriangular lattice has at
most two unoriented unit directions: six oriented unit vectors would
force all angular gaps to equal `pi/3`, hence a unit triangular sublattice;
its covering radius is below one, so no other coset can be added.
Central symmetry leaves zero, one, or two directions. With two, count
occupied row and column **path segments**, and denote their total by
`L_j`. With one, put `L_j=|A_j|+(number of path segments)`; with zero,
put `L_j=2|A_j|`. Then

\[
 e_j\le2|A_j|-L_j,\qquad L_j\ge2\sqrt{|A_j|}.
\]

The pinned contact-preserving velocity space has dimension at least

\[
 \sum_j L_j-e_X-2q.
 \tag{4.1}
\]

Indeed there are `2(n-q)` free velocity coordinates and at most
`sum e_j+e_X` contact equations. Each positive kernel vector integrates
as the straight path `p_i+t w_i`: contacts have squared length
`1+t^2|w_i-w_j|^2>=1`, all actual diameters are fixed because their
endpoints are pinned, and all inactive full-source pairs retain their
strict finite slack for small `t`. Thus a strictly positive right side
excludes first-order jamming.

For a bounded number of lattice sets, `q=O(D^(2/3))`, uniformly in
their unit-separated lattices. Here is the short independent proof. Each
loaded point is extreme in its own set. A lattice polygon's distinct
oriented edge vectors shorter than `L` number at most `4(L+1/2)^2`, by
disjoint half-unit disks, while longer edges number at most `pi D/L`.
Choose `L=D^(1/3)` and sum over the bounded number of sets.

For the constructed sources, `e_X=1`, `sum L_j=Theta(D)`, and therefore
(4.1) is positive for large `D`. They fail the actual jammed hypothesis.
This gate identifies the missing information: a bounded exact-chart
jammed source needs **linear independent interface constraints** (or
enough nonchart labels/pins); one graph-connectivity bridge supplies only
one contact row. The gate extends neither exact lattice membership nor
its contact count to curved, approximately coherent phase grains.

The underlying one-lattice contact count also occurs in the unreviewed
September 25 uniform-lattice flex report. No authority is imported from
it; the finite multiple-chart gate above is derived explicitly and used
only to audit the new regression's scope.

## 5. Exact computation and hostile checks

Run from the repository root:

```bash
python3 research/seed084/verify_seamed_grains.py
```

The fixtures are centered triangular crops
`i^2+ij+j^2<=Q` for `Q=7,19,31,61,100,217`. The shear angle is
`2 atan(10^-6)` and the clockwise hinge angle is `2 atan(10^-12)`,
with cut `j=-1/2` and the rightmost seam anchor. All coordinates are
exact in `Q(sqrt(3))`, using a common integer denominator.

The replay checks **416,295 full-source pairs**, exact contacts and
triangle absence, graph connectivity, the sole inter-chart bridge,
actual maximum pair distance, a strict smaller-diameter comparator,
the strict n-1 inequality, all rhombi and the full Euler/population
identity, exact hull area and strict shell upper side, inter-chart
determinants, and a positive pinned-nullity floor.

| Q | n | lower/upper rhombi | B | chi | t | actual loaded points | pinned nullity floor |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 7 | 31 | 5 / 9 | 28 | 2 | 1 | 2 | 14 |
| 19 | 73 | 19 / 26 | 50 | 2 | 1 | 2 | 25 |
| 31 | 121 | 38 / 48 | 64 | 2 | 1 | 2 | 32 |
| 61 | 223 | 79 / 93 | 96 | 2 | 1 | 2 | 48 |
| 100 | 367 | 142 / 161 | 120 | 2 | 2 | 2 | 61 |
| 217 | 793 | 334 / 362 | 188 | 2 | 1 | 2 | 94 |

An independent Fraction-based expansion replays every pair of the
31-point fixture. Negative controls show that reversing the hinge sign
contracts a former seam unit pair, and removing the shear restores a unit
triangle inside a chart. Pi is bounded using exact alternating-series
intervals in Machin's identity; no floating-point tolerance is used.
The finite examples are not assumed to certify the infinite construction;
Sections 3--4 prove the quantified statements.

Relevant regression boundaries:

- Raw support depth still cancels against support turning. It is not
  charged as independent area surplus here.
- The physical contact graph is planar, but its train intersection graph
  is not assumed planar. No facial gain localization or Euler trail is used.
- A single contact bridge gives graph connectivity, not simultaneous
  rigidity or a global force/stress bridge.
- The bridge edge and every outside-complex source label are counted in
  the full-source graph and topology bookkeeping. The fixtures have no
  physical contact isolates; the proof discards no label.
- These sources have only sublinear possible loaded populations and a
  positive pinned kernel, so canonical jammed pinned-rank and exposed-hull
  restrictions cannot be imported to them.
- The rhombic complex has two chart regions and bridge/outside residue;
  it is not asserted to be a pure topological rhombic disk. The canonical
  pure-disk GPI/CR results are not falsified.
- No contact-minimal ZR/ZF, source-specific Schur, C-II, or Level I claim
  is made. Local nonglobality is proved by an actual global competitor.

## 6. Claim status and exact remaining gap

| Claim | Classification | Scope / consequence |
|---|---|---|
| Sections 2--3 construction | proved candidate regression, unreviewed | Kills scalar/roundness repair of static inter-grain payment |
| Fixed positive grain deficit and virtual-mass limits | proved candidate, unreviewed | Explicit asymptotic counts, not constant improvement toward closure |
| Section 4 interface rigidity gate | proved candidate, unreviewed | Exact lattice partitions only; audits absence of jamming |
| Scalar assumptions imply (2.7) | rejected by the new regression | Does not reject a theorem using actual global optimality |
| Phase-area contraction always shortens diameter | rejected attempted mechanism | A unit rhombus's long diagonal grows |
| Whole-source triangular replacement for these sources | proved candidate, unreviewed | Strict nonglobality at exactly the original cardinality |
| General canonical source-to-competitor extraction | open | No actual compatible replacement constructed |
| Target B and Level I closure | open | Canonical frontier unchanged |

The smallest unchanged canonical obligation is the actual-source joint
shell inequality with its topology correction, or an equally strong
same-cardinality strict-diameter competitor. In this attack, the precise
missing bridge is:

> Prove that a triangle-free jammed *global* survivor with several
> macroscopic fixed-positive-deficit grains has an actual compatible
> full-source replacement, or an interface-rank/geometry payment strong
> enough to force `G+E>=c_0B+a_0(t+chi-1)`.

Roundness, leading density, the strict n-1 allowance, the scalar Oler
window, phase coherence, and contact connectivity do not establish that
bridge. Section 4 does not bound the shell cost of the required interface
rank and supplies no exact lattice cover for a canonical curved grain.

**Promotion recommendation:** preserve as an unreviewed regression and
request independent mathematical scrutiny. Do not update the canonical
state or active endpoint. Review should focus on the full-pair hinge
identity, strict two-sided diameter comparison, half-crop train counts,
and the distinction between connected contact graphs and jammed sources.
