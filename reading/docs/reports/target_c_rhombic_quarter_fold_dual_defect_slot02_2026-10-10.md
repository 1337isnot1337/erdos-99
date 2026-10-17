> Generated reading edition · [exact source](../../../docs/reports/target_c_rhombic_quarter_fold_dual_defect_slot02_2026-10-10.md) · source SHA-256 `12d3a2460d900a016be9944cbd6a3a3b842e6d33e6b09e0ae9c06c7602ebf9b8`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-92FC5BCFE3F0","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II: a four-unit dual defect budget for rhombic quarter-folds

**Date:** 2026-10-10. **Worker:** 02.  
**Base main:** `ab6dd3336f9f8d440f2bada76edb32153391cddc`.  
**Theorem state:** `2026-10-10.audit.234`.  
**Previous checkpoint:** `ff83fd52addb87d733edd619b25f62cfaf547b74`.  
**Branch / PR:** `research/sol61-slot02-20261010-integrated-fold`,
[PR #948](../publication/provenance.md#source-records).  
**Classification:** proved candidates awaiting independent mathematical audit;
unreviewed and noncanonical. **LEVEL I AND C-II REMAIN OPEN.**

## 1. Exact endpoint obstruction

Let `P` be the canonical triangle-free global minimizer, contact-minimal and
then actual-diameter-pair-minimal, with `D>=9`. Retain every source label. Let
`G=(V,C)` be its nonisolated contact core. Suppose `G` is 2-vertex-connected
and every bounded actual contact face is a quadrilateral. Let `Q` be a
same-cardinality, unit-separated placement of diameter at most `D`, with exactly
the same full contact graph, satisfying on each core contact

`Q_j-Q_i=s_ij J(P_j-P_i)`, `s_ij in {-1,+1}`.

**Theorem 1.1 (proved candidate).** Either all signs are equal, or every bounded
face reverses orientation, every interior core vertex has degree four, and no
core vertex has degree five. In the second case normalize the endpoint isolates
by `C-FULL-SOURCE-ISOLATE-NORMALIZATION`, leaving its core fixed, and write

```text
v=|V|, e=|C|, b=length of the simple outer contact cycle,
h_P=|H(P)|, q_P=|B(P)|, d_P=q_P-h_P,
h_Q=|H(Q)|, q_Q=|B(Q)|, d_Q=q_Q-h_Q,
s=e+h_P-(2v-2), Delta_h=h_Q-h_P.
```

`H(Q)` and `B(Q)` here refer to the **normalized full endpoint**, whose actual
diameter pairs all lie in `V`. Then

`2s+d_P+d_Q+Delta_h=4`,                           (1.1)

and all four quantities on the left are nonnegative integers. In particular

```text
s<=2,                  d_P+s<=4,
0<=Delta_h<=4-2s-d_P,  d_Q<=4-2s-d_P,
(d_P+s)+(d_Q+s+Delta_h)=4.
```

There are exactly 22 nonnegative integer classes in (1.1). If `s=2`, both
diameter deficiencies vanish and the normalized endpoint has exactly `h_P`
diameter pairs. The theorem supplies no realization of any of those classes.

The loaded sets have an equally explicit form. If `n_2,n_3,n_4` count the
degrees of old outer-cycle vertices, then

```text
n_2-n_4=4,
B(P) intersection B(Q) = {outer vertices of degree two},
B(P) symmetric_difference B(Q) = {outer vertices of degree three},
q_P+q_Q=b+4,
q_Q-q_P=4-2(d_P+s).
```

These are statements about actual core diameter incidence, after a justified
normalization of every contact isolate; they do not use a hypothetical scaffold
or assume secondary diameter minimality at the endpoint.

```text
full feasible reversing rhombic quarter-fold
 -> exact boundary loaded-role swap
 -> q_P+q_Q=b+4 and e=2v-2-b/2
 -> secondary diameter minimality at P gives h_Q>=h_P
 -> the four-unit budget (1.1)
 -> no such endpoint if s>=3 or d_P+s>=5
```

Combining this result with the preceding candidate
[large-face exclusion](target_c_nonconstant_face_quarter_fold_exclusion_slot02_2026-10-10.md)
gives a sharper gate for any 2-connected source core: a noncongruent full
quarter-fold requires **only quadrilateral bounded faces**, `s_Z<=2`, and
`d_H+s_Z<=4`. Contact articulations/bridges and non-quarter motions are outside
this conclusion. Neither candidate constructs a finite competitor.

## 2. Dependencies and endpoint normalization

Canonical dependencies are:

- [C-I restoration](../targets/target-c/56-ci-restored-frontier.md), item 4:
  contact minimality gives positive support for every actual contact, and hence
  positive contact equilibrium at any vertex with no actual diameter.
- [Local structure](../theory/01-local-structure.md), Lemma 5.1 and Theorem 6.1:
  actual diameter endpoints are strictly exposed hull vertices; nonisolated
  vertices without diameter incidence are strictly surrounded by their contacts.
- [Rhombus population audit](../targets/target-c/67-rhombus-population-transport-audit.md):
  bounded unit quadrilaterals are convex rhombi with angles strictly between
  `pi/3` and `2pi/3`, and contain no additional unit-separated source point.
- [Audit 83](../audits/target_c_face_coupled_quarter_fold_independent_audit_2026-10-07.md):
  two-hop sign compatibility, including uniformity of a degree-five star.
- [ZR/ZF](../targets/target-c/57-zr-zf-rigidity-audit.md):
  `s_Z=e+h_P-(2v-2)>=0` and `h_P>=ceil D` for the canonical **old** source.
- [Audit 177](../audits/target_c_isolate_normalization_independent_audit_2026-10-08.md):
  normalize all endpoint isolates without changing the core, the full contact
  graph, unit separation, cardinality, or the upper bound `D`.
- [Full diameter topology](target_c_woodall_diameter_topology_2026-09-10.md):
  the actual diameter graph is a straight-line thrackle and has at most as
  many edges as incident vertices. This geometric fact also applies at the
  normalized endpoint without secondary minimality there.

For completeness the last normalization uses the endpoint core centroid `w`
and moves every isolate `z` to `(1-t)Q_z+t w`. If `sigma>0` is the minimum
squared lower slack of every isolate-involving pair, choose
`0<t<=sigma/(8D^2)`. All such squared distances remain at least `1+sigma/2`;
core-isolate distances are at most `D(1-t/|V|)` and isolate-isolate distances
at most `D(1-t)`. Every pair is checked simultaneously, every isolate is
retained, and no uniform positive `t` over different sources is claimed.

The normalized endpoint is still a global minimizer because it has `n` labels
and diameter at most `D(n)`. Its exact contact count ties the first minimum.
Therefore `h_Q>=h_P` by the **old source's** second minimum. The new endpoint
need not itself minimize diameter-pair count. This is the only input needed to
deduce `Delta_h>=0`; no new-endpoint ZF theorem is invoked.

For any finite planar diameter graph on its incident vertex set, `h<=q` by
the standard diameter-graph/thrackle edge bound. Thus `d_P,d_Q>=0`. This uses
the whole actual diameter graph, not selected positive rows.

## 3. Every face remains actual, and orientations propagate

A unit-separated four-cycle cannot self-cross: crossing nonincident unit
segments would force two endpoints closer than one. A simple equilateral
quadrilateral is a convex rhombus. In a triangle-free contact graph its angles
lie strictly between 60 and 120 degrees. The strict rhombus disk cover excludes
any additional source point in its interior; a diagonal contact would create
a triangle. Thus the corresponding four-cycle is an actual bounded face at
both `P` and `Q`, including with all isolate labels present.

Let an old face have edge vectors `u,v,-u,-v`. The quarter-fold closure gives

`(s_1-s_3)u+(s_2-s_4)v=0`.

The vectors are independent, so opposite signs agree. If the two remaining
signs agree, the face is a proper quarter-turn and retains orientation. If
they differ, the face reverses orientation and each corner angle `gamma`
becomes `pi-gamma`.

Two actual adjacent bounded faces occupy opposite sides of their shared edge
at both placements. Their orientation changes therefore agree. The weak dual
of bounded faces is connected: the 2-connected outer boundary is a simple
cycle, its interior is the union of the bounded faces, and a path inside that
open disk can be perturbed to avoid vertices and cross edges only. Every edge
lies on a bounded face because there are no bridges. Hence all faces either
retain or reverse orientation. In the first case their constant signs
propagate across shared edges to one common sign on the whole core.

Assume henceforth all faces reverse. Every two consecutive contact edges
around an interior vertex bound a face and have opposite signs. The degree
is even. Unit-separated triangle-free contacts have degree at most five,
and strict surrounding gives interior degree at least three, so it is four.
A degree-five boundary star also cannot occur: Audit 83 forces its signs
uniform, while every incident bounded face would require differing signs.

## 4. Boundary roles and the exact Euler budget

At an outer-cycle vertex of degree `d`, exactly `d-1` angular sectors are
bounded rhombic faces. Let `A` be their total angle. Each individual face
angle is in `(pi/3,2pi/3)`. The corresponding total at `Q` is

`A_Q=(d-1)pi-A`.

- For `d=2`, the two rays do not strictly surround, so contact minimality
  forces actual diameter incidence at both placements.
- For `d=3`, `A` is in `(2pi/3,4pi/3)`. If `A<pi`, its rays lie in an open
  half-plane, so the vertex must be loaded. If `A>pi`, all three cyclic gaps
  are below `pi`, so it is strictly surrounded and cannot be a hull vertex
  or diameter endpoint. The value `A=pi` is impossible: the vertex is the
  midpoint of its two opposite unit neighbors, hence not strictly exposed,
  while its contacts fail strict surrounding. Since `A_Q=2pi-A`, loaded
  status swaps exactly.
- For `d=4`, `pi<A<2pi`, and every cyclic gap is below `pi`. The vertex is
  strictly surrounded and unloaded. The same reasoning applies at `Q`.

Interior degree-four vertices are likewise unloaded. After normalization no
isolate is loaded, so the above lists exhaust both full actual loaded sets.

For a quadrilateral disk Euler and edge-face incidence give

`e=2v-2-b/2`.

Also, summing `4-deg_G(v)` over all vertices gives `b+4`: interior degrees
are four, and the boundary contribution is `2n_2+n_3`. Since
`b=n_2+n_3+n_4`, this yields `n_2-n_4=4`. The loaded-role description gives

`q_P+q_Q=2n_2+n_3=b+4`.

Put `s_Q=e+h_Q-(2v-2)=s+Delta_h`. Then, directly,

```text
(d_P+s)+(d_Q+s_Q)
 =q_P+q_Q+2e-4v+4
 =(b+4)+(4v-4-b)-4v+4
 =4.
```

This is (1.1). Old ZF, normalization, and the old second minimum give
`s>=0`, `Delta_h>=0`; the full diameter-graph edge bound gives the two
nonnegative deficiencies. No asymptotic boundary term has been suppressed.

## 5. Coherent two-vector cores admit no reversing endpoint

Here coherence is an additional exact hypothesis: there are independent unit
vectors `u,v` such that **every** core contact vector is parallel to one of
them. Connectedness then places the entire labelled core in one translate
of `Z u+Z v`. A bounded rhombus makes `x=u dot v` lie in `(-1/2,1/2)`.

**Theorem 5.1 (proved candidate).** Under Theorem 1.1's hypotheses and this
exact two-vector condition, no orientation-reversing full quarter-fold exists.
Consequently every full feasible quarter-fold has one common edge sign.

First, shared-face propagation in a reversing endpoint makes one family
sign `sigma` and the other `-sigma`, throughout the connected weak dual.
After one global rotation/translation the endpoint core is therefore

`Q_i=m_i u-n_i v`, whereas `P_i=m_i u+n_i v`.

Every source pair with coefficient differences `(m,n)` has old square

`F_{m,n}(x)=m^2+n^2+2mn x`

and endpoint square `F_{m,n}(-x)`. Both are at most `D^2`. For `0<=r<=1`
replace `v` by the unit vector `v_r` with `u dot v_r=r x`, choosing the same
side of `u` as the old `v`. Then

`F_{m,n}(r x)=((1+r)/2)F_{m,n}(x)+((1-r)/2)F_{m,n}(-x)<=D^2`. (5.1)

All core lower constraints also hold, with the exact same contact graph.
For integers `(m,n)!=(0,0)` and `|r x|<1/2`, a pair with both coefficients
nonzero has

`m^2+n^2+2mn r x>m^2+n^2-|mn|>=1`.

If a coefficient is zero, equality with one occurs exactly when the other
is `+1` or `-1`, independent of `r`. Thus every inactive core lower pair
remains strict and every actual contact remains unit. This is a change of
the Gram parameter toward zero, not the circular interpolation of two
quarter-fold coordinate fields.

Keep every old isolate fixed. At `P`, every isolate-involving lower and upper
pair has strict finite slack. For all `r<1` sufficiently close to one, finite
continuity preserves all those pairs. Equation (5.1) checks **all** core
upper pairs, not just old diameter edges. Every initially inactive full-source
upper pair remains strict for a small common interval. Thus the shear is a
full-source, same-cardinality feasible placement with exactly `C` and no new
diameter pairs.

The old secondary minimum forces every old diameter edge to remain `D`.
If `x!=0`, its affine length formula then forces `mn=0` for each such edge.
There would be at most two projective diameter directions. Distinct planar
diameter segments in a diameter-`D` set have distinct projective directions
(the two cross-pair upper bounds prove this even for disjoint segments).
But old ZF gives `h_P>=ceil D>=9`. Contradiction. Hence `x=0`.

The remaining orthogonal case is itself impossible for this canonical source,
by the following finite arithmetic lemma. No hypothetical isolate transport is
needed for the shear: isolates were retained and fixed in a sufficiently small,
explicitly slack-dependent neighborhood.

The nonorthogonal affine part is also a direct consequence of the canonical
old equilibrium and finite mixed rigidity: an affine core placement lies in
the old scalar stress kernel; unit contacts and upper bounds on positive old
diameter rows then force equality on every old diameter row. The explicit
Gram shear above records the full finite pair ledger. It is not asserted as
an additional Schur-kernel theorem or an independent repair of ZR/ZF.

## 6. Finite exclusion of a square-lattice contact core

**Lemma 6.1 (proved candidate).** If the entire canonical core is in one
isometric translate of `Z^2` and `D>=9`, there is a contradiction.

An actual old diameter edge in the core gives `N=D^2` a positive integer,
with `N>=81`. Let

`r_2(N)=|{(a,b) in Z^2:a^2+b^2=N}|`.

Each projective integer direction has two representatives on this circle,
and at most one actual diameter pair uses a given projective direction.
Indeed, orient two purported parallel diameter pairs as
`(a,a+D n)` and `(b,b+D n)`. Their cross-pair upper bounds give
`|b-a+D n|^2<=D^2` and `|b-a-D n|^2<=D^2`; adding forces `b=a`.
Thus `h_P<=r_2(N)/2`. We prove the elementary strict estimate

`r_2(N)<2 sqrt(N)` for all `N>=26`.                 (6.1)

The signed, ordered sum-of-two-squares formula is

`r_2(N)=4 product_{p=1 mod 4}(a_p+1)`

when all exponents at primes `3 mod 4` are even, and zero otherwise. Its
normalization and Gaussian factorization proof were checked in the original
[UCSD lecture notes, Definition-Theorem 4.6, pages 2--3](https://mathweb.ucsd.edu/~jmckerna/Teaching/17-18/Spring/104C/l_4.pdf).
For clarity, each conjugate split prime with exponent `a` has `a+1` choices
in the Gaussian integer of norm `N`; the four Gaussian units supply the factor
four, including axis representations. The exponent at `1+i` and the exponents
of inert primes are fixed. These choices count each ordered signed pair once.

For a split prime define `f_p(a)=(a+1)^2/p^a`. For `a>=1`,

`f_p(a+1)/f_p(a)=((a+2)/(a+1))^2/p<=9/20<1`,

and `f_p(1)=4/p<1`. Factors from powers of two and inert prime squares also
only decrease `r_2(N)^2/N`.

If a split prime `p>=17` occurs, this quotient is at most `64/17<4`. Otherwise
only the split primes 5 and 13 can occur. If both occur, the quotient is at
most `256/65<4`. If only 13 occurs with exponent at least two it is at most
`144/169<4`; with exponent one the remaining factor in `N` is at least two
because `N>=26`, giving at most `32/13<4`. If only 5 occurs, exponent at least
three gives at most `256/125<4`; exponent two gives at most `144/50<4` because
the remaining factor is at least two; exponent one gives at most `64/30<4`
because the remaining factor is at least six. With no split prime, `r_2(N)=4`
and the estimate is immediate. This proves (6.1) for every integer `N>=26`.

Consequently `h_P<sqrt(N)=D`, contradicting `h_P>=ceil D`. This is a finite
core obstruction. It uses neither a density-only population cap nor a claim
that arbitrary coherent phase data supply exact lattice positions. Audit 91
already excludes uniformly conditioned exact lattice covers asymptotically;
this elementary orthogonal case additionally removes the finite `x=0` endpoint
left by the shear argument.

## 7. The correction when bridges or articulations survive

The number four cannot be applied to an arbitrary contact core. There is a
useful exact corrected identity, which requires no quadrilateral-disk premise.
Normalize the full endpoint's isolates as before. Count old core degree-one
and degree-five vertices as `n_1,n_5`. Among degree-three vertices whose signs
are uniform, let `L_3` count old loaded vertices and `U_3` old unloaded vertices.

**Proposition 7.1 (proved candidate).** Every full-source feasible exact-graph
quarter-fold of a canonical source satisfies

`2s_Z+d_P+d_Q+(h_Q-h_P)=4-n_1+n_5+L_3-U_3`.       (7.1)

Each term on the left is nonnegative. No sign or size is asserted for the
right without additional actual-source geometry. This is a ledger for the
bridge-linked branch, not its elimination.

To check the role count, a loaded degree-three star has extreme rays spanning
`theta in (2pi/3,pi)`, whose signs agree by two-hop compatibility. A uniform
star stays loaded; flipping its middle ray makes all three new cyclic gaps
strictly below `pi`, so it becomes unloaded. In an unloaded degree-three star
all gaps lie in `(pi/3,pi)`, and at least one gap is at least `2pi/3`. Its
bounding signs agree. If two such gaps exist all signs agree; otherwise
flipping the third ray puts it inside the large gap, making the new star lie
in an open half-plane and forcing actual diameter incidence. Thus every
nonuniform degree-three star contributes exactly one loaded endpoint across
the two placements. Uniform degree-three stars contribute two or zero.
Degrees one and two are loaded at both placements; degrees four and five
are unloaded at both. These are local geometric and contact-minimal facts,
with no assumption about which diameter partners realize the incidences.

Writing `ell_P(i),ell_Q(i)` for the two loaded indicators and using the
handshake lemma gives

```text
(d_P+s_Z)+(d_Q+s_Z+h_Q-h_P)
 =q_P+q_Q+2e-4v+4
 =4+sum_i(ell_P(i)+ell_Q(i)+deg(i)-4).
```

The respective summands for degrees one through five are `-1`, `0`, one of
`+1,0,-1` according to the preceding degree-three cases, `0`, and `+1`.
This proves (7.1). In Theorem 1.1's reversing quadrilateral disk, there are no
leaves or degree-five vertices; all degree-three vertices are boundary vertices
with nonuniform signs. The correction vanishes and (7.1) becomes (1.1).

This also identifies why importing the four-unit budget into a bridge-linked
core without checking its actual stars is invalid. Degree-five vertices and
uniform loaded degree-three stars can add budget; leaves and uniform unloaded
degree-three stars remove it. The isolate population adds no degree term,
because every such label was retained and its diameter equalities opened by
the proved normalization.

## 8. Complete bent arrays: exact core fold and a quadratic isolate burden

A different mechanism applies under a stronger **actual-source** premise.
Suppose the whole contact core is a complete array

`P_ij=x_i+y_j`, `0<=i<=a`, `0<=j<=c`,

whose actual contact graph consists precisely of consecutive row and column
edges, and whose cells are its actual bounded rhombic faces. The use of `c`
avoids confusing a row count with the outer-walk length `b`. Assume `a,c>=1`.
After orienting the parameter disk, put `u_i=x_(i+1)-x_i` and
`v_j=y_(j+1)-y_j`; every such vector is unit and every cell has positive
orientation. The directions may vary along both families. This is not an
assumption of one affine lattice, and is not supplied for an arbitrary
quadrilateral disk by the canonical train/grid extraction theorems.

**Theorem 8.1 (proved candidate).** The integrated field

`Q_ij=J(x_i-y_j)`

has exactly the old core contact graph and preserves the entire multiset of
core pair distances. In particular every core lower and upper constraint
passes, and its number of actual core diameter pairs is exactly the old count.
For a canonical source with this actual whole-core array,

`|Z| > (pi/(2sqrt(3))-2/3)D^2-sqrt(8/3)D`.         (8.1)

Every isolate is outside the old outer contact cycle; the same is true of
any extension at the new core. No full-source isolate extension is constructed.
In particular a canonical isolate-free complete array is impossible for
`D>=9`, even when the array is bent and has more than two contact directions.

**Proposition 8.2 (proved candidate).** The actual whole-core complete-array
premise also forces

`q_P=a+c+2`, `d_H(P)+s_Z=2`.

Hence only `(s_Z,d_H)=(0,2),(1,1),(2,0)` are possible. Any full-source extension
of the displayed fold, after isolate normalization, has `h_Q=h_P`, `q_Q=q_P`,
and the same diameter deficiency and mixed surplus. This asserts no extension.

**Full core pair proof.** For an unordered pair of distinct array labels,

```text
|Q_ij-Q_kl|^2
 =|x_i-x_k-(y_j-y_l)|^2
 =|P_il-P_kj|^2.
```

The map `{(i,j),(k,l)} -> {(i,l),(k,j)}` is an involution on all distinct
unordered pairs. It cannot turn a distinct pair into a repeated label. A
consecutive row or column pair maps to the same type of consecutive pair,
and conversely. Thus the contact graph, every pair lower bound, every pair
upper bound, the diameter, and the count of diameter pairs are verified
exactly. Shortening some old diameters creates an equal number of formerly
inactive diameter pairs. That replacement bank cannot be discarded.

**Source count proof.** Each actual cell is a strict triangle-free unit
rhombus, so the oriented separation of **every** pair `u_i,v_j` is in
`(pi/3,2pi/3)`. Fixing one `v_j` confines all `u_i` to a direction interval
of width strictly below `pi/3`; fixing one `u_i` gives the same for all
`v_j`. Projection on the two respective interval bisectors yields

`|A|>(sqrt(3)/2)a`, `|B|>(sqrt(3)/2)c`,

where `A=x_a-x_0` and `B=y_c-y_0`. The four actual corner labels supply both
diagonals `A+B` and `A-B`, so

`D^2>=max(|A+B|^2,|A-B|^2)>=|A|^2+|B|^2>3(a^2+c^2)/4`.

There are exactly `(a+1)(c+1)` core labels. Since
`ac<=(a^2+c^2)/2` and `a+c<=sqrt(2(a^2+c^2))`,

`|V|<2D^2/3+sqrt(8/3)D+1`.

The canonical strict translated-lattice population comparison, reproduced
in [Section 67](../targets/target-c/67-rhombus-population-transport-audit.md), is
`n>pi D^2/(2sqrt(3))+1`. Subtracting the count of the actual core gives
(8.1). This is an actual label count, not an Oler allowance interpreted as
available empty sites. All source isolates remain in `n` and `Z`.

For the finite isolate-free exclusion, `pi>3`, `sqrt(3)<7/4`, and
`sqrt(8/3)<5/3` give the weaker but elementary bound

`|Z|>(4/21)D^2-(5/3)D>=D/21>0` for `D>=9`.

The old outer disk is the union of actual unit rhombi and their contact
edges. Rhombus disk coverage excludes additional source labels in a cell,
and a point on a contact-edge interior would be less than one from an
endpoint. Hence all isolates are outside that disk. The exact same argument
applies to a full extension of the folded array.

**Loaded-count proof.** Consecutive directions `u_(i-1),u_i` have a signed turn
`delta_i` of magnitude below `pi/3`. It cannot vanish: either old boundary
vertex at that column would then be the midpoint of its two unit row neighbors,
so it is not an actual diameter endpoint, while its three contacts fail strict
surrounding. This contradicts contact minimality. The sums of the two bounded
face angles at the opposite boundary vertices `(i,0)` and `(i,c)` are
`pi-delta_i` and `pi+delta_i`, in some order. As in Section 4, precisely the
vertex with sum below `pi` is actually loaded. Thus each of the `a-1` interior
column indices pays exactly one loaded label across its two boundary copies.
The same argument with consecutive `v_j` pays one for each of the `c-1`
interior row indices. The four degree-two corners are loaded and no interior
vertex is loaded. This gives `q_P=4+(a-1)+(c-1)=a+c+2`.

The outer-cycle length is `2(a+c)`, so the exact Euler ledger gives
`d_H(P)+s_Z=q_P-(a+c)=2`. At a full extension the pair involution fixes the
number of core diameter pairs. Isolate normalization makes that count the full
diameter-pair count. Section 4's swap and `q_P=b/2+2` give `q_Q=q_P`, proving
the last assertion without assuming or inventing a transported isolate packet.

If there are no isolates, the displayed pair involution gives a complete
same-cardinality quarter-fold endpoint, but the independent source count
already excludes that canonical regime. With isolates, it gives only a core
endpoint and an explicit quadratic population whose feasible transport is
still missing. The theorem does not replace actual incomplete domains by
their rectangular completion; omitted corner or cell labels are never
introduced into the source proof.

## 9. Exact guardrails and what remains

The companion
[`verify_target_c_rhombic_dual_defect_2026_10_10.py`](../../../research/verify_target_c_rhombic_dual_defect_2026_10_10.py)
uses only integers and rational arithmetic. Its saved
[certificate](../../../research/target_c_rhombic_dual_defect_certificate_2026_10_10.json)
checks all 22 defect classes; the signed representation formula and the strict
circle bound for `26<=N<=4096`; finite affine Gram identities; and complete
pair ledgers and the pair involution for two bent rhombic grids, including a
finite contact-loss move.
The infinite circle inequality and the source endpoint budget are proved above,
not by extrapolation from that enumeration.

The bent fixtures use `c=12/13`, `s=5/13`, column positions
`x_0=(0,0), x_1=(c,s), x_2=(2c,0)` and row points `x_i+(0,j)` for `0<=j<=L`,
with `L=2` and `L=10`. Their exact fold is `Q_ij=J(x_i-(0,j))`; all horizontal
contacts have sign plus and vertical contacts sign minus. Both full point
sets have the same diameter and the exact same triangle-free contact graph,
and every face reverses. The labelled cores are noncongruent even though row
reversal makes their unlabelled point sets congruent. At `L=10` the diameter
exceeds nine, so a small-source cutoff alone does not remove this guardrail.

These grids **fail contact minimality**: at `L=2` move the top middle vertex
up by `1/100`; at `L=10` move the top left corner by `(-1/100,1/100)`.
Each complete finite ledger retains every lower bound and the old diameter
while losing contacts. In particular, joint diameter feasibility, a rhombic
disk, and matching contact graphs alone do not imply the loaded-role budget
or canonical finite rigidity. No global optimality is asserted for the fixtures.

Three mechanisms were tested. The direct circular quarter-fold interpolation
fails: endpoint pair squares can both be 2 while an intermediate square is 4.
The exact Euler/loaded-role route gives Theorem 1.1. The distinct Gram-parameter
shear closes coherent two-vector cores but cannot be applied to a bent array:
straightening a varying family changes its chord lengths, so (5.1) no longer
checks every upper pair. No coherence extraction is supplied.

The exact next obligation on this branch is to rule out or realize a full-source
endpoint for an **incoherent** quadrilateral disk with `s_Z<=2`, `d_H+s_Z<=4`,
and the boundary loaded-role swap of Section 4. A useful closing result would
derive a feasible contact-loss or strict-diameter competitor from those actual
geometry hypotheses, retaining all outside isolates and testing every newly
active upper pair. A proof that the endpoint exists is still absent; excluding
all quarter-folds would itself not settle C-II without a separate source-level
alternative producing a different finite competitor.

For a supplied actual complete array, the narrower obligation is a rigorous
upper population bound or feasible transport for the outside isolates in (8.1),
under one of Proposition 8.2's three actual diameter-topology classes. The core
pair involution has already supplied every core lower/upper check and preserves
diameter-pair count, so a further claim must add isolate geometry or a different
contact-loss move. A fixed-isolate or weighted-old-diameter argument cannot
supply that missing step.
