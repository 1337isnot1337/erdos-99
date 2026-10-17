> Generated reading edition · [exact source](../../../docs/reports/population_reserve_independent_reconstruction_2026-10-15.md) · source SHA-256 `280ad14b9ab8e265903cdbb55970934b6cde112e9fda511c9d361fa261b322eb`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-A79C6F204DD7","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# Population reserve: independent audit and an effective twelve-arc strengthening

Status: **unreviewed candidate**. Level I remains open. This document is not a
promotion or a publication artifact.

**Destination lifecycle note:** The source report's request for independent
human mathematical review is source-era wording. This import leaves every new
claim unreviewed. Any consequential promotion must follow the destination's
current exact-commit independent AI-agent audit policy in `docs/REVIEW_POLICY.md`
and update the theorem-state and frontier together. Nothing is promoted here.

Starting scientific commit: `eb51394f371aee958b0d9332f80faf75ae694b9e`.
The original shared checkout was at `596ef075cdae5683bcc3f7c860ca30f2df993e39`;
the isolated worktree starts at freshly fetched `origin/main` instead.
State version: `2026-10-10.audit.234`.

## Reconstruction recorded before reading the existing proofs

Only the statement, state/route records, problem definition, and open-PR metadata
had been read when this section was written. In particular, neither Audit.243,
Audit.199 nor their source proofs had been opened.

Put `a=sqrt(3)/2`. For a translated unit triangular lattice, crop a disk of radius
`R=(D+w)/2`, with `w=c D^(-1/3)`. Join pairs at distance **at least** `D`.
Deleting one endpoint per edge leaves a subset of strict diameter below `D`.
Translation averaging gives

```math
\mathbb E V=\pi R^2/a,\qquad
\mathbb E E={1\over2a}\sum_{v\in\Lambda,\ D\le |v|\le D+w}
 |B_R\cap(B_R-v)|.
```

For `t=2R-|v|` the lens area is
`(4/3)sqrt(R)t^(3/2)(1+O(t/R))`. Replacing the radial lattice measure by
`(2 pi r/a)dr` therefore predicts

```math
\mathbb E(V-E)={\pi D^2\over4a}
 +\left({\pi c\over2a}-{8\pi c^{5/2}\over15\sqrt2 a^2}\right)D^{2/3}
 +O_\theta(D^\theta).
```

The proposed discrepancy error follows if the centered disk count is
`pi r^2/a+O_theta(r^theta)` uniformly over `D<=r<=D+w`: Stieltjes integration
costs at most the discrepancy bound times twice the maximum lens area, and that
area is `O(D^(1/2)w^(3/2))=O(1)`. The lower endpoint must use a left limit;
an exact-radius atom is included in the error, not discarded.

The maximum occurs at

```math
c_*=(3\sqrt2 a/8)^{2/3},\qquad
\max={3\pi c_*\over10a}
 ={3\pi\over5a}(3a/16)^{2/3}=\kappa_0.
```

For a global `n`-point minimizer of diameter `D`, every strict sub-`D`
unit-separated competitor has at most `n-1` points. Thus the construction,
if its analytic estimates hold, has the required all-minimizer quantifiers.
It makes no identification of a lattice competitor with the source.

Independent audit obligations are: the exact discrepancy theorem and its fixed
ellipse applicability, closed-shell endpoint atoms, a uniform lens expansion,
Stieltjes variation, measurable translation averaging, integer deletion and
strictness, and the order of the fixed-parameter/asymptotic quantifiers.

## Independent disposition of the headline theorem

**Verdict: independently established**, with Huxley's published discrepancy
theorem as a literature premise. This is an independent mathematical assessment,
not a lifecycle promotion and not a claim to have reproved Huxley's theorem.

The three requested source artifacts were inspected after the reconstruction.
The source report is absent at its old path on this main commit. Its exact bytes
were recovered from commit `6132201c1d3056ca68a222217094acb819f5b4d7`; SHA-256
`a8e0334ad495eb5e4eefda1d1b4a1a5a1bf3a14e5851ef46e99cd4d2bfca70a2`
agrees with both existing audits. No missing source was silently replaced by an
unrelated current report.

Here is the completed proof, in the radius-increment normalization of Audit.243.
Fix `theta` in `(131/208,2/3)` and `c>0` once and for all, and set
`delta=c D^(-1/3)`, `S=D/2+delta`.

1. Huxley's *Configurations of Lattice Points*, printed pp. 703--704,
   Theorem A, explicitly allows a fixed planar lattice and a smooth oval.
   Its fixed-circle instance gives
   `N(r)=pi r^2/a+O_theta(r^theta)`. Equivalently transform the triangular
   lattice to `Z^2` and the circle to a fixed ellipse, whose curvature is
   everywhere positive. There is no changing family of ovals in this use.
   The endpoint count `N(D-)` obeys the same estimate by taking a limit from
   below; this includes, rather than suppresses, a possible atom at `D`.
2. The exact lens is
   `L_S(2S-d)=4 integral_0^(d/2) sqrt(2St-t^2) dt`. Factoring `sqrt(2St)`
   gives `(4/3)sqrt(S)d^(3/2)(1+O(d/S))`, uniformly for `0<=d<=2delta`.
   Thus `L_S(D)=O_c(1)` and `L_S(2S)=0`.
3. Write `N(r)=pi r^2/a+e(r)`. Stieltjes integration by parts on `[D,2S]`
   uses `e(D-)` at the lower endpoint. Its error has absolute value at most
   `2 sup_[D-,2S]|e| L_S(D)=O_(c,theta)(D^theta)`. The extra factor two
   is harmless; the total variation of the decreasing lens is `L_S(D)`.
   Consequently
   `sum_(D<=|v|<2S) L_S(|v|)=(1/a) integral_D^(2S)2pi r L_S(r)dr
   +O_(c,theta)(D^theta)`.
4. Direct integration gives
   `integral_D^(2S)L_S(r)dr=(32/15)sqrt(D)delta^(5/2)
   (1+O_c(delta/D))`. Replacing `r` by `D` in the other factor has the
   same relative error. The main weighted sum is therefore
   `(64pi/(15a)) c^(5/2)D^(2/3)`. The geometric error is `O_c(D^(-2/3))`,
   smaller than the allowed discrepancy error.
5. Haar-uniform translation modulo the lattice gives exactly
   `E V=pi S^2/a` and `E E=(1/(2a))sum L_S(|v|)`.
   Unfolding the fundamental-domain integral proves these identities;
   every relevant sum is finite. The factor two removes ordered-pair
   duplication. All distance-`D` pairs are edges.
6. Hence
   `E(V-E)=pi D^2/(4a)+F(c)D^(2/3)+O_(c,theta)(D^theta)` where
   `F(c)=pi c/a-32pi c^(5/2)/(15a^2)`.
   Its derivative vanishes exactly at `c^(3/2)=3a/16`;
   it increases before and decreases after that point. Its unique maximum
   is the stated `kappa0`. This optimizes this particular edge-deletion
   estimate, not all independent sets or all planar competitors.
7. Some translate has the integer `V-E` at least its mean. The union of one
   selected endpoint per edge deletes at most `E` distinct vertices. Every
   surviving pair has distance strictly less than `D`, including when
   original distances equal `D`. A finite surviving set has strict diameter.
8. For every global `n`-point minimizer at this `D`, that competitor has at
   most `n-1` points, by taking an `n`-point subset otherwise. Thus
   `g_A>=kappa0 D^(2/3)-C_theta D^theta`. The constants and onset depend
   only on the fixed lattice, fixed optimizing `c`, and fixed `theta`.
   They do not depend on a source configuration or cardinality.

There is no effective numerical Huxley constant or numerical onset certified
by this proof. The strict inequality `theta>131/208` absorbs its logarithmic
loss; this does not establish the endpoint exponent without that loss.
The coefficient is not claimed optimal. No source structure, triangle-freeness,
contact minimization or KKT premise enters this theorem.

## Prior work inspected before selecting a new direction

PR #955, exact head `d5afc236a7b1de9567dcb6dda65d957ed91c726b`, proves a
near-bipartite cut and matching comparison for annular conflict graphs and
finite savings of order `D^(2/3)` on special sequences. It expressly leaves
translation-averaged matching cost and a universal improved coefficient open.
The new calculation below does not claim that work as a new discovery.

PR #956, exact head `bbc549f36ac964fd7eee211782eb2c979d12af32`, already claims
the stronger order `g_A>=D/320000`, for `D>1280000`, using boundary zigzags.
Its original packet parameters are `h=19/20`, vertical offsets `1/6,1/2`,
one shallow arc, and a uniform one-point gain per qualifying row. Its analytic
proof was reconstructed: the guards, lower/higher row checks, ordered disjoint
intervals, arbitrary vertical phase, averaging and `R`-to-`D/2` limit are valid.
Its separate lattice-defect, periodic and interface theorems are not premises
of this report and receive no blanket verdict here.

The contribution below is a quantitative strengthening of that boundary
construction: new packet parameters, twelve simultaneous arcs, and integration
of the actual row lengths under translation averaging. It is not the discovery
of a linear-order reserve, which is already in PR #956.

## A stronger explicit linear reserve

**Classification: proved candidate awaiting independent human mathematical
review; unreviewed in the project lifecycle.**

Define the following exact constants:

```math
a={\sqrt3\over2},\quad h={56\over65},\quad
p=1-a,\quad q={98\over65}-a,\quad
b=a-q=\sqrt3-{98\over65},\quad k={9\over56},\quad C={65\over28},
```
```math
s={256\over16385},\quad \beta={16383\over16385},
\qquad s^2+\beta^2=1,
```
```math
\boxed{\gamma={6\over a}\{kb s-C(1-\beta)\}
 ={3(576b-65)\over114695a}
 =0.001939936045\ldots.}
\tag{L1}
```

**Theorem.** For every real `R>=8192` a unit-separated finite packing in the
closed radius-`R` disk has population at least

```math
{\pi R^2\over a}+2\gamma R-{\sqrt R\over4}-60.
\tag{L2}
```

Every global unit-separated `n`-point diameter minimizer with `D>16384` therefore
satisfies

```math
\boxed{g_A\ge\gamma D-{\sqrt D\over4\sqrt2}-60
             \ge\gamma D-{\sqrt D\over5}-60.}
\tag{L3}
```

In particular,

```math
\boxed{D\ge10^6\quad\Longrightarrow\quad g_A\ge D/600.}
\tag{L4}
```

The asymptotic linear coefficient exceeds PR #956's `1/320000` by a factor
greater than 620; the convenient effective coefficient `1/600` is greater by
exactly `1600/3`. Both are strictly stronger than any fixed `D^(2/3)`
coefficient asymptotically. The error in (L3) and its range are explicit.
This is not an assertion that `gamma` is best possible.

### Proof: one packet and simultaneous pair constraints

Let `f(z)=sqrt(R^2-z^2)`. Write a translated unit triangular lattice as
`{(t_x+j+l/2,t_y+la):j,l in Z}`. In each of the six coordinate frames obtained
by rotating through multiples of `pi/3`, select every lattice row at height

```math
\beta R\le y\le R-a.
\tag{L5}
```

On its right side put
`u=f(y+a)`, `v=f(y+q)`, `ell=v-u`. Delete the lattice labels on that row in
`[u,v]` and insert

```math
(u+1+ih,\ y+\eta_i),\quad
0\le i\le\lfloor(\ell-2)/h\rfloor,\qquad
\eta_i=\begin{cases}p&i\text{ even},\\q&i\text{ odd}.\end{cases}
\tag{L6}
```

Make the reflected replacement on the left. Since `q-p=33/65`, adjacent
inserted squared distances are exactly `h^2+(33/65)^2=1`; nonadjacent
horizontal distances are at least `2h>1`. Every old lower row has vertical
distance at least `a+p=1`. Every retained point of the same row is at
horizontal distance at least one. Every old higher-row point of the disk
has horizontal coordinate at most `u` on the right, or lies on the left,
so has horizontal separation at least one from a right packet. The left
version follows by reflection. Thus **all** new/old lower constraints hold;
the possible vertical equality at a lower row is allowed.

All new points lie in the original disk: their positive heights are at most
`y+q` and their horizontal coordinates lie in `[u+1,v-1]`, so in particular
have absolute value strictly below `f(y+q)`. Also

```math
\ell=\int_{y+q}^{y+a}{z\over f(z)}\,dz\ge b\beta/s>14>2.
\tag{L7}
```

The packets are well defined. If `y_2>=y_1+a`, then
`v_(y_2)=f(y_2+q)<f(y_1+a)=u_(y_1)`. Hence two right packets of the same
frame are separated horizontally by more than two. A right packet and a
left packet have horizontal separation at least two. This covers all pairs
within one frame, even if their vertical ranges overlap.

Every inserted point is in the cone `|x|<=sR, y>=beta R` of its frame, and
has radius at least `beta R`. Different frame normals differ by at least
`pi/3`. With `phi=arcsin(s)`, their angular separation is at least
`pi/3-2phi`, so their distance is at least

```math
2\beta R\sin(\pi/6-\phi)
=\beta R(\beta-\sqrt3s)>R/2>1.
\tag{L8}
```

For unequal radii this lower bound follows from
`|x-y|^2=(r_1-r_2)^2+4r_1r_2 sin^2(angle/2)`.
The same cone bound keeps different-frame deleted row intervals disjoint.
If two same-frame deletion intervals happen to share a boundary label,
counting it twice only overestimates deletions, which is safe. Thus all
twelve families can be performed together. Unchanged old pairs retain
triangular-lattice separation. This checks the whole packing, not just
individually feasible replacements.

### Proof: translation averaging without endpoint-rounding losses

Average the lattice translation over a fundamental domain. In a given frame,
conditional on its vertical phase, the horizontal row phase is uniform
modulo one. The expected number deleted from `[u,v]` is exactly `ell`;
closed endpoints affect a null set. The inserted count is
`K(y)=floor((ell-2)/h)+1 >= (ell-2)/h`.
Unfolding the vertical phase then gives expected gain, for all twelve
families combined, at least

```math
{12\over a}\int_{\beta R}^{R-a}\{k\ell(y)-C\}\,dy.
\tag{L9}
```

The six frames are automorphisms of the triangular lattice. Their rotated
translation classes have the same uniform distribution; no independence
between frames is needed. The base crop population has expectation
`pi R^2/a`. All functions here are bounded and measurable on a compact
translation domain. An integer output at least its mean exists.

Put `I=integral_(beta R)^(R-a)ell(y)dy`. Substitution in the two terms gives
the exact telescoping identity

```math
I=\int_{\beta R+q}^{\beta R+a}f(z)\,dz
       -\int_{R-b}^R f(z)\,dz.
\tag{L10}
```

The first term is at least `b f(beta R+a)` since `f` decreases. The second
is at most `(2/3)sqrt(2R)b^(3/2)`, since `f(R-t)<=sqrt(2Rt)`.
For `R>=8192` we have `beta R+a<=R` and

```math
f(\beta R+a)\ge sR-{2\beta a\over s}-{a^2\over sR},
\tag{L11}
```

by `sqrt(X-e)>=sqrt(X)-e/sqrt(X)` for `0<=e<=X`.
Combining (L9)--(L11) and dropping the positive term `12C` gives expected
population at least

```math
{\pi R^2\over a}+2\gamma R-A\sqrt R-B_0,
\quad A={8\sqrt2\over a}k b^{3/2},\quad
B_0={12\over a}kb\left({2\beta a\over s}+{a^2\over8192s}\right).
\tag{L12}
```

Exact arithmetic gives `A<1/4`, `B_0<60`, and `gamma>193/100000`.
These are inequalities between elements of `Q(sqrt(3))` after squaring
the positive `A` comparison. The reproducible verifier checks them with
integer/rational sign predicates. This proves (L2), with no discrepancy
theorem and for every real radius in the stated range.

### Proof: every global minimizer and the effective threshold

For a global `n`-point minimizer at `D>16384`, apply (L2) at **each**
`8192<=R<D/2`. Its integer competitor population is at most `n-1` because
its diameter is at most `2R<D`. Let `R` increase to `D/2`; only the continuous
numerical lower bound is passed to a limit. No diameter-`D` competitor is
used in the contradiction. This proves (L3).

For `x=sqrt(D)>=1000`,

```math
\left({193\over100000}-{1\over600}\right)x^2-{x\over5}-60
={79\over300000}x^2-{x\over5}-60>0.
```

At `x=1000` this is `10/3`, and its derivative is positive for all
`x>=1000`. This proves (L4). All source labels and original lower constraints
are retained in the cardinality comparison; no lattice structure is imposed
on a minimizer. QED.

**Effective confirmation of the original coefficient.** The exact inequality
`kappa0<2/3` follows by cubing: `kappa0^3=243 pi^3/(32000a)` and the classical
bound `pi<22/7` suffices. Thus (L4), for `D>=64000000=400^3`, gives

```math
g_A\ge D/600\ge(2/3)D^{2/3}>\kappa_0D^{2/3}.
\tag{L13}
```

This supplies an elementary effective proof of the headline bound with
**zero** remainder on this explicit range, independently of any effective
Huxley constant. It does not repair a flaw in Audit.243: its proof is valid.
The new input is a stronger, nonlattice comparison packing.

## Literature, originality and the actual research frontier

Primary sources were searched live and their actual statements inspected,
including local primary-paper PDFs/extractions already in the scientific repo.
The following are comparisons of statements, not inferences from matching titles.

| Source and precise locator | What it establishes | Comparison with this session |
| --- | --- | --- |
| Bateman--Erdős, *Geometrical Extrema Suggested by a Lemma of Besicovitch*, American Mathematical Monthly 58 (1951), 306--314, final section | Small cases and leading-dimensional asymptotic discussion. | Does not state an all-cardinality positive reserve of the displayed order. |
| [Bezdek--Fodor (1999)](https://doi.org/10.1006/jcta.1998.2889), printed p. 106 and Theorem 1.1 | The introduction derives `D(n)>=sqrt(4an/pi)-1` and the leading planar asymptotic. The exact theorem determines `D(8)`. | The asymptotic leading term is classical. Neither the introduction nor the theorem supplies the positive population correction here. |
| [Bondarenko--Hardin--Saff, *Minimal N-Point Diameters and f-Best-Packing Constants in R^d*](https://arxiv.org/abs/1204.4403), Theorem 2 and proof | `N^(1/d) Delta_d^(-1/d)-2 <= D_d(N) <= N^(1/d) Delta_d^(-1/d)` for all `N>=2`, and the planar Bezdek--Fodor improvement in the following remark. The function is the same separation/diameter ratio. | This is a directly comparable general published bound. Its upper bound has no negative correction to diameter. Integer translation averaging also immediately gives the familiar `n-1` baseline; no originality is claimed for that step. |
| [Oler, *A Finite Packing Problem* (1961)](https://doi.org/10.4153/CMB-1961-018-7), pp. 153--155 | Finite area/perimeter inequality. For a unit-separated set in its convex hull `K`, `n<=area(K)/a+per(K)/2+1`. | Isodiametry and the Cauchy perimeter bound give `g_A<=pi D/2` for every packing of diameter `D`. This is an immediate classical upper bound, in the opposite direction to a positive reserve. It explains why linear reserve is the largest possible order. It does not distinguish triangle-free minimizers. |
| [Schürmann, *On Extremal Finite Packings* (2002)](https://doi.org/10.1007/s00454-002-0747-6), Lemma 8, Theorem 9, and its proof on printed p. 401 | Eventual nonlattice optimality, including minimum diameter; a loose boundary edge permits sequential rearrangements. The asymptotic-shape argument obtains an eventual qualitative conclusion. | A prior boundary-improvement method and a stronger qualitative exclusion of all lattice minimizers are already known. The theorem/proof inspected does not state a power-law population margin or the effective constants above. The new result belongs to this established finite-boundary tradition. |
| [Lubachevsky--Graham, *Curved Hexagonal Packings of Equal Disks in a Circle* (1997)](https://mathweb.ucsd.edu/~ronspubs/97_02_curved_hexagonal.pdf), abstract and equations (1)--(4) | Explicit families at hexagonal cardinalities with limiting covering density `pi^2/12`, strictly below optimal planar density. | These special constructions cannot yield the present all-cardinality correction at the optimal leading density. They are a relevant near miss, not an equivalent theorem. |
| [Huxley, *Configurations of Lattice Points*, Oberwolfach Report 14/2008](https://publications.mfo.de/bitstream/handle/mfo/3058/OWR_2008_14.pdf?isAllowed=y&sequence=1), printed pp. 703--704, Theorem A; [original 2003 article](https://doi.org/10.1112/S0024611503014485) | The fixed smooth-oval discrepancy exponent `131/208` with a logarithmic loss absorbed by a fixed positive epsilon. The report itself allows an arbitrary fixed planar lattice. | A published input to Audit.243, not a packing-reserve theorem. No best-current-circle-exponent claim is needed or made. The full 2003 proof was not reconstructed. |
| [Li--Yang, *An improvement on Gauss's Circle Problem and Dirichlet's Divisor Problem*](https://arxiv.org/abs/2308.14859), version 2 (2023), Theorem 1.2 and Definition 1.1, pp. 1--2 | The preprint states `R(X)=O_epsilon(X^(theta_*+epsilon))`, `theta_*=0.3144831759741...`, for `m^2+n^2<=X`, hence radius exponent `2theta_*=0.6289663519482...`. | Stronger than Huxley for the standard square-lattice circle. Its proof was not audited, and a triangular-lattice circle becomes an ellipse in integer coordinates. No extension to that quadratic form is established here; no imported improvement is claimed. |
| [Bourgain--Watt, *Mean square of zeta function, circle problem and divisor problem revisited*](https://arxiv.org/abs/1709.04340), current version 2 (July 16, 2023) | The authors' current primary record says the paper is withdrawn and its Theorems 1--3 no longer have theorem status because of gaps in the spacing/decoupling arguments. | The frequently quoted radius exponent `517/824` from this item must not be imported as an established replacement. A 2024 thin-sector article still cites it, demonstrating why checking the current primary record matters. This does not affect either proof in this report. |

The literature search also followed finite-packing boundary terms, parametric
density, strict-diameter competitors, curved hexagonal families and citations
from the direct diameter papers. The official Erdős problem page returned HTTP
403 during this session; its inaccessible contents are not cited as live evidence.
The project's own 2026 preprint is not independent external corroboration.

**Priority assessment:** no inspected external theorem was found with equivalent
quantifiers and this reserve bound. That is not a proof of novelty. The original
`D^(2/3)` statement is a short packing deduction from a deep known discrepancy
estimate once the conflict-deletion construction is supplied. Its priority, and
whether this deduction occurs elsewhere, remain unresolved. The linear-order
boundary approach is already present in private PR #956; this session's precise
contribution is its substantially stronger explicit constant, error and threshold.
No claim of a new packing method or a settled literature priority is made.

### Level I attempt and rigorous stopping point

The natural attempted bridge is to upper-bound the reserve of a triangle-free
global minimizer using its contact graph or a source lattice realization. The
new comparison supplies a larger boundary budget, but still supplies no such
realization. The remaining sufficient implication can be stated quantitatively:

```math
\text{every sufficiently large triangle-free global minimizer has}
\quad g_A\le cD+o(D)\quad\text{for some fixed }c<\gamma.
\tag{GAP}
```

An admissible source-specific replacement of all `n` labels with strict diameter
improvement would also suffice. Neither implication was proved in this session.

There is a rigorous obstruction to dropping global optimality from (GAP).
Choose any `0<c<gamma`. By (L2), for every sufficiently large `D`, a disk of
radius `R=D/2-epsilon_D` with positive `epsilon_D` sufficiently small contains
at least `pi D^2/(4a)+cD` labels. For this *finite* packing, stretch its vertical
coordinate by `1+eta`, with `eta>0` small enough that `2R(1+eta)<D`. Every
distance weakly increases, and every old unit pair with a nonzero vertical
component becomes longer than one. Remaining unit edges are horizontal, and
three distinct collinear points cannot be mutually unit-separated by equality.
The contact graph is triangle-free. Untouched central lattice rows include
horizontal unit pairs, so the minimum distance remains exactly one. Its actual
diameter is below `D`. In terms of its actual diameter `d`, its population
excess `N-1-pi d^2/(4a)` is at least `c d` after choosing a slightly larger
intermediate coefficient between `c` and `gamma` to absorb the `-1`.
This is a feasible-source regression, not a sequence of global minimizers.

Thus neither arbitrary triangle-free density nor an independently constructed
triangular-lattice crop can be identified with the original source. This
session provides no new source-realization theorem. **Level I remains open.**

### Publication-critical disposition

No false inference was found in the headline coefficient theorem. Its coefficient
is an optimized value for one edge-count estimate, not an optimal packing
coefficient, and it is asymptotically weaker than the unpromoted linear candidate
already in PR #956. The stronger result in this report is also unpromoted and
requires independent human mathematical review. A release should neither claim
optimality of `kappa0`, present literature priority as established, nor promote
either AI-derived linear result by implication. No publication-repository file,
canonical theorem status, active route or unrelated PR is changed here.
If discussing improved discrepancy exponents, the withdrawal above must also
be respected. No claim about the best current exponent for every ellipse is
made on the basis of square-lattice circle results.

## Reproduction and actual verification

The dependency-free exact verifier is
`research/verify_population_reserve_twelve_arc_2026_10_15.py`. Run from the
scientific worktree:

```bash
python3 research/verify_population_reserve_twelve_arc_2026_10_15.py --extended \
  --output /tmp/population-reserve-twelve-arc.json
```

The committed output is
`research/population_reserve_twelve_arc_2026_10_15.json`. The completed extended
run passed these finite cases:

| R | Lattice basis translation | Packets | Deleted | Inserted | Net gain |
| ---: | --- | ---: | ---: | ---: | ---: |
| 8192 | (0,0) | 0 | 0 | 0 | 0 |
| 16385 | (1/3,1/5) | 18 | 502 | 548 | 46 |
| 65540 | (0,0) | 108 | 3420 | 3780 | 360 |
| 65540 | (1/7,2/5) | 98 | 2533 | 2762 | 229 |
| 500000 | (2/7,3/11) | 828 | 22205 | 24284 | 2079 |

Totals: 1052 packets, 31374 inserted labels, 19659 retained-neighbor checks,
and 42969 inserted-neighbor checks. The `R=8192` zero-packet case is deliberate:
the universal lower bound (L2) has a negative correction there, and the
translation-average theorem does not require a positive gain for every phase.
The integer arithmetic also verifies 169 sign controls, 150 rotation identities,
the coefficient comparison, error constants, and effective threshold. Exact-`D`
conflict tests at `D=8,16,32` include ties and leave strict residual diameter.
Two deliberate new/new and new/retained collisions are rejected by their
respective distance validators.

The finite constructor rounds the analytic `u` upward and `v` downward by
rational square-root brackets of width `2^-24`. These inward roundings preserve
the geometric argument; the report's exact real endpoints are used for the
analytic average. The verifier enumerates every potentially close old label,
including all original labels retained anywhere in the disk. Unchanged old/old
pairs use exact lattice separation. It does not allocate or enumerate the
quadratic-size old crop at large radii, and does not claim finite evidence is a
proof of the all-radius average or of minimizer optimality.
