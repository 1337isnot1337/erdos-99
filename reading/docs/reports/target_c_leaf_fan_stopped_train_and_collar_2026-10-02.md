> Generated reading edition · [exact source](../../../docs/reports/target_c_leaf_fan_stopped_train_and_collar_2026-10-02.md) · source SHA-256 `7ab7d76f59762041a16b4cc7124ef27414b8eb3789a93b3c326fd35253626886`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-A09E01922265","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C: leaf fans force stopped-train face currency

`unique opposite fan support -> distinct stopped rhombus trains ->
5Q >= h-3nu(H)-3x_B -> exclusion of the low-matching, low-outer-excess,
sublinear-face-defect branch; full closure still requires a source-level
contradiction for the surviving linear Q.`

**Date:** 2026-10-02.
**Starting shared checkout:** `539f5187b3cac9287f6b30cdf6b36aafb1763c5a`.
**Research base:** `75aac1464f80ca91256e96dc70ca0c865e0b3b0e`.
**State version:** `2026-09-14.audit.51`.
**Mission:** exact diameter-leaf fans, stopped trains, and inward-spoke collars.
**Branch:** `swarm/sol/leaf-fan-sector-20261002`.
**Classification:** proved candidates awaiting independent audit/promotion;
artifact lifecycle unreviewed. Section 5 is a regression.
**Level I / C-II:** OPEN.
**External literature:** none imported.
**Certificate:** `research/verify_target_c_leaf_fan_sector_2026_10_02.py`.

## 1. Exact inputs and scope

Use the canonical contact-minimal, then diameter-pair-minimal triangle-free
global source, with `D>=9`, `C=C_*`, and `H=H_*`. Retain every source point,
including all contact isolates. Write

$$
H=(B,E_H),\quad q=|B|,\quad h=|E_H|,\quad \nu=\nu(H).
$$

The canonical dependencies are:

- `C-WOODALL`, the full diameter graph classification: odd cycle with pendant
  leaves, or a disjoint union of caterpillars; the diameter-thrackle property;
- Target C Sections 26/35, recorded in `02-fully-visible-bridge-frontier.md`,
  `03-pinned-block-and-loaded-boundary-frontier.md`, and
  `04-near-minimal-response-frontier.md`: loaded extremality, loaded contact
  degree at most three, and unloaded positive harmonicity;
- `57-zr-zf-rigidity-audit.md`: full-support core normalization and `h>=ceil(D)`;
- `61-linear-nonmatching-excess-audit.md`, Sections 61.2--61.4: fixed-direction
  stopped rhombus trains, one crossing per pair, and endpoint-incidence budgets;
- `63-loaded-hull-slack-audit.md`, Section 63.1: distinguished exterior
  occurrences and `x_B=sum_i(ell_i-1)`;
- `67-rhombus-population-transport-audit.md`, Section 67.2 and (67.6), for the
  optional area-excess application in Section 6;
- `58-full-source-geometry-audit.md`, FS.4, only for the eventual small-width
  application in Section 6.

Here `f` is the number of bounded nonquadrilateral contact faces and

$$
Q=\sum_{F\text{ bounded non4}}(\deg F-4),\qquad
Q=f+g_F,\qquad f\le Q.
$$

Degrees and endpoints are occurrence-counted. In particular

$$
\sum_{F\text{ non4}}\deg F=Q+4f.
\tag{1}
$$

The current-main reports `target_c_leaf_fan_outerwalk_fork_2026-10-02.md`
and `target_c_leaf_fan_inward_spoke_kkt_fork_2026-10-02.md` are unpromoted.
The fan-count and local geometry facts needed here are rederived below;
their broader continuation prose is not a theorem premise.

## 2. A fan chord has exactly one opposite supporting vertex

**Theorem LF.1.** Let a diameter-`D` planar source contain distinct `a,p,q`
with `|p-a|=|q-a|=D` and `|p-q|=1`. Put

$$
m={p+q\over2},\quad
R=|m-a|=\sqrt{D^2-1/4},\quad u={m-a\over R}.
$$

Then `a` uniquely minimizes `u dot x` over the whole source. If `pq` is a
convex-hull side, it is the only hull side parallel to `pq`.

**Proof.** Translate `a` to zero and choose a unit tangent `t` with
`p=Ru+t/2`, `q=Ru-t/2`. Every source point `x` satisfies both upper bounds
`|x-p|^2,|x-q|^2<=D^2=R^2+1/4`. Taking their maximum gives

$$
|x|^2-2R(u\cdot x)+|t\cdot x|\le0.
\tag{2}
$$

If `x!=a`, this forces `u dot x>0`. Thus the opposite supporting face is
the singleton `{a}`. The supporting face on the `pq` side has direction
`t`; when `pq` is a hull side it is the same face as `pq`. A distinct parallel
hull side would have to be an opposite supporting edge, which is impossible.
This uses every source upper bound and no source optimality. QED.

The conclusion holds for any such common-carrier chord; neither endpoint need
be a diameter leaf for LF.1 itself.

## 3. Fan count and the new face-defect inequality

Call a loaded-hull adjacency a **good fan contact** if its two vertices are
degree-one diameter neighbors of the same carrier and its distinguished
outer-walk interval has length one. Let `A` be their number.

### 3.1 Independent fan-count derivation

For a nonleaf diameter vertex `a`, its leaf neighbors form one consecutive
cyclic block. To see this, take leaves `p,q` of `a` and a loaded vertex `z`
on the open `p`-to-`q` hull arc not containing `a`. Any diameter `zw` with
`w!=a` must properly cross both `ap` and `aq`, since it shares no endpoint
with them. Crossing `ap` puts `w` on the open `(a,p)` arc; crossing `aq`
puts it on the disjoint `(q,a)` arc. Therefore every diameter at `z` is
`za`, and `z` is itself a leaf of `a`.

Let `P` be the number of leaf-to-nonleaf diameter edges, let `c` be the
number of their carriers, and let `S` count their internal block adjacencies.
Then `S=P-c`, and choosing one pendant edge at each carrier gives `c<=nu`.

In the forest case let `K` count isolated `K_2` components, let `m` count
nonleaf-to-nonleaf edges, and let `mu` be their matching number. Their graph
is a disjoint union of paths, so `m<=2mu`. The `K` component edges augment
that matching, so `mu+K<=nu`. Consequently

$$
P=h-m-K\ge h-2\nu,\qquad S\ge h-3\nu.
\tag{3}
$$

In the cyclic case, if no leaves exist the desired `S>=h-3nu` follows
from `h=2nu+1` and `nu>=1`. If leaves exist on an odd cycle of length `r`,
one leaf edge and a matching on the cycle with its carrier deleted give
`nu>=(r+1)/2`. All noncycle edges are pendant, so
`P=h-r>=h-2nu+1`, proving (3) again.

At most `x_B` distinguished intervals are bad, because each costs at least
one in `x_B=sum(ell_i-1)`. Hence

$$
\boxed{A\ge\max\{0,h-3\nu-x_B\}.}
\tag{4}
$$

### 3.2 Every good fan contact starts a different stopped train

**Theorem LF.2.** In the canonical source,

$$
\boxed{A\le2x_B+Q+4f.}
\tag{5}
$$

In particular,

$$
\boxed{h\le3\nu+3x_B+Q+4f\le3\nu+3x_B+5Q,}
\tag{6}
$$

and

$$
\boxed{5Q\ge\lceil D\rceil-3\nu-3x_B.}
\tag{7}
$$

**Proof.** Each good fan contact is a unit hull side and therefore an
outer endpoint incidence of a stopped rhombus train. Every contact edge on
that train has the same projective direction. By LF.1 there is no other
parallel hull side. Thus its other endpoint cannot be a different good
outer interval.

The same good fan contact also cannot supply two different good interval
occurrences. With `q>=3`, there is just one forward cyclic loaded adjacency
between its endpoints. If the contact is a bridge and its two sides both
belong to the outer face, its second occurrence therefore belongs to a bad
interval. This is counted as an outer incidence, not as a second source edge.

Two different good fan contacts cannot belong to the same train: they would
be distinct parallel hull sides, again excluded by LF.1. Hence all `A`
trains have distinct other endpoint incidences. Those incidences are either
on bad outer intervals, whose total length is at most `2x_B`, or on bounded
nonquadrilateral faces, whose total degree is `Q+4f` by (1). Singleton
trains and bridge occurrences are included in this endpoint count. This
proves (5). Combine (4) and (5), then `f<=Q`, then `h>=ceil(D)`, to obtain
(6)--(7). QED.

**Corollary LF.3.** A canonical survivor sequence cannot simultaneously have

$$
\nu=o(D),\qquad x_B=o(D),\qquad Q=o(D).
\tag{8}
$$

In fact, the first two hypotheses force `liminf Q/D>=1/5`.
This excludes the formerly compatible low-matching, low-outer-excess branch
whose entire linear defect is paid by `s_Z`. It does not exclude linear `Q`.
The result applies beyond the square-root regime and needs no multiplier floor.

There is also a finite rank-to-face transport. The exact train count
`T=h-s_Z+2f`, together with the `A` distinct trains in (4), gives

$$
\boxed{s_Z\le2f+3\nu+x_B.}
\tag{9}
$$

Thus large mixed surplus under small `nu,x_B` requires many actual exceptional
faces. It cannot be housed solely in a dimension count without face support.

## 4. Third fan neighbors are unloaded

**Theorem LF.4.** Let an internal good fan vertex `p` have adjacent fan
vertices `p_-,p_+`, common carrier `a`, and a third contact neighbor `z`.
For `D>=2`,

$$
z\in\operatorname{int}\operatorname{conv}\{a,p_-,p_+\}.
\tag{10}
$$

In the canonical source, `z` is unloaded and has contact degree three, four,
or five. In particular the spoke reaches the actual unloaded contact graph,
rather than another diameter terminal.

**Proof.** Set `p=0`, `a=-Du`, and choose a tangent `t` so that

$$
p_\pm=-\epsilon u\pm\tau t,\quad
\epsilon={1\over2D},\quad \tau=\sqrt{1-\epsilon^2}.
$$

Write `z=-ru-st`. The source upper bound `|z-a|<=D` gives `r>=epsilon`;
separation from both fan neighbors gives

$$
\epsilon r+\tau |s|\le1/2.
$$

Together with `r^2+s^2=1`, these imply

$$
r\ge{\epsilon+\sqrt3\tau\over2}>\epsilon,\qquad
|s|\le{\tau-\sqrt3\epsilon\over2}<1/2.
\tag{11}
$$

For example, in angular coordinates the two neighboring contact directions
are at `+/-acos(epsilon)` from `u`; the third direction must remain inside
their common 60-degree exclusion cone. This yields (11) directly.

At coordinate `-ru`, the triangle in (10) has half-width

$$
\tau{D-r\over D-\epsilon}.
$$

Here `r<=1<D`. For `D>=2`,

$$
\tau\ge{\sqrt{15}\over4},\qquad
{D-1\over D-1/(2D)}\ge{4\over7},\qquad
\tau{D-r\over D-\epsilon}\ge{\sqrt{15}\over7}>1/2.
\tag{12}
$$

The middle inequality is exactly
`2(3D-1)(D-2)>=0`. Equations (11)--(12) put `z` strictly inside the triangle.
All three triangle vertices belong to the loaded force hull, so `z` is not
extreme. Loaded extremality and unloaded harmonicity give the final claim.
No contact-isolated point is discarded. QED.

## 5. Exact regression: a positive-equilibrium rhombic collar

The attempted assertion “many consecutive inward fan spokes force an
exceptional face locally” is false. The failure remains after imposing
positive equilibrium at every internal upper and lower vertex.

Let

$$
\theta=2\arcsin{1\over2D},\qquad
p_i=D(\cos(i\theta),\sin(i\theta)),\qquad
z_i=p_i-(1,0),\quad -k\le i\le k.
\tag{13}
$$

Take `k theta` small, for example the exact packets below. Every consecutive
quad `p_i,p_{i+1},z_{i+1},z_i` is a strict convex unit rhombus. The full set
`{a=0} union {p_i,z_i}` is triangle-free, unit-separated, and has diameter
exactly `D`, attained by every `ap_i`.

Set

$$
d_i=p_{i+1}-p_i=(-\sin t_i,\cos t_i),\quad
t_i=(i+1/2)\theta,
$$

and choose positive `K,L` with `L>K max_i sec(t_i)`. Give upper fan edges
multiplier `lambda_i=L-K sec(t_i)`, lower fan edges multiplier
`mu_i=K sec(t_i)`, interior spokes multiplier

$$
\gamma_i=K(\tan t_i-\tan t_{i-1})>0,
\tag{14}
$$

and upper diameter edges multiplier `beta_i=L/D^2>0`.

The lower vertex equations hold exactly because

$$
\mu_{i-1}d_{i-1}-\mu_i d_i=\gamma_i(1,0).
\tag{15}
$$

The upper equations then follow from

$$
\lambda_{i-1}d_{i-1}-\lambda_i d_i+\gamma_i(1,0)
=L(d_{i-1}-d_i)={L\over D^2}p_i.
\tag{16}
$$

Thus internal upper vertices have exactly the fan-leaf/inward-spoke equilibrium;
internal lower vertices are positive harmonic degree-three vertices.
The sum `lambda_i+mu_i=L` is exactly constant despite upper stress variation.

For rational certificates take an integer `s>=8`, put

$$
t={1\over4s},\quad
c={1-t^2\over1+t^2},\quad r={2t\over1+t^2},\quad
D={1\over2r},\quad k=\lfloor s/8\rfloor.
\tag{17}
$$

Then `cos(theta/2)=c`, `sin(theta/2)=r`, and the full rotation matrix,
all coordinates, and all weights with `K=1,L=2` are rational.
This family gives arbitrarily long collars. Indeed `D~s`, `k~s/8`, and
`k theta<1/4`: the elementary bound `theta<=2r/c` gives
`k theta<=1/[8(1-t^2)]<1/4`.
For these angles the upper and lower curves have all horizontal tangents
within `1/4` radians of vertical. Same-row nonneighbor distances increase
with index gap and exceed one; adjacent cross-row diagonals exceed one
because their squared lengths are `2+/-2 sin(t_i)`.
For cross-row index gap at least two, the absolute vertical displacement
is at least `2 cos(1/4)>1`. The entire upper arc spans less than `1/2`
radian, hence has diameter at most `2D sin(1/4)<D/2`; translating one row
by one changes a cross-row distance by at most one. Thus every cross-row
upper bound is strict for `D>2`. Also `|z_i|<D` and `|z_i|>=D-1>1`.
These observations prove the source inequalities for the whole family.
One may instead take `k=floor(sqrt(s))` for `s>=64`, since this still has
`k<=s/8`. Then the collar length is `Theta(sqrt(D))` and its diameter-star
width is `O(D^(-1/2))`, narrower than the canonical `O(D^(-1/4))` ceiling.
The regression therefore survives imposing that small-star-angle condition.

**Omitted hypotheses are essential.** There is no equilibrium at the
carrier `a`, which is contact-isolated in this packet, or at the four row
endpoints. There is no full-source normalized KKT stress, PSD certificate,
rigid-core certificate, or global-optimality proof. This does not falsify
the global problem or any canonical theorem. It falsifies the local
spoke-to-exceptional-face inference, even with exact interior equilibrium.

The repair is to retain the finite train ends in LF.2: a collar can transport
the obstruction away from the fan, but cannot turn its trains into a second
parallel good hull side in a completed canonical source.

## 6. Pushing the collar: exact common-train area surcharge

The local collar survives, but its rotating fan directions also impose a
quantitative area bill if many other actual trains cross the whole fan shore.

**Theorem LF.5.** Let `g>=2` consecutive fan contacts determine `g` distinct
actual trains, with ordered directions `alpha_i=alpha_0+i theta`,
`0<=i<g`, and `W=(g-1)theta<=pi/12`. If `R` other actual trains each cross
all `g` fan trains, the `gR` distinct crossing rhombi satisfy

$$
\boxed{\sum_{\text{these rhombi}}(\operatorname{area}-\sqrt3/2)
\ge {R\theta g(g-1)\over8}
\ge {Rg(g-1)\over8D}.}
\tag{18}
$$

**Proof.** A crossing partner direction has a lift `phi` in
`(alpha_0+W+pi/3,alpha_0+2pi/3)`, since all its acute projective
separations from the fan directions exceed 60 degrees. Its rhombus areas
are `sin(phi-alpha_i)`. Their sum is concave as a function of `phi` on
that interval; its minimum over the closed interval is at an endpoint.
The endpoint values coincide by reversing `i`. Therefore its total excess
is at least

$$
\sum_{i=0}^{g-1}\bigl[\sin(\pi/3+i\theta)-\sqrt3/2\bigr].
\tag{19}
$$

For `0<=x<=pi/12`,
`sin(pi/3+x)-sqrt3/2>=x/4`, since its derivative is at least
`cos(5pi/12)=(sqrt6-sqrt2)/4>1/4`.
Summing gives `theta g(g-1)/8`. Distinct pairs of trains cross at most once,
and every rhombus specifies its two trains, so all `gR` rhombi counted here
are different. Finally `theta>=1/D`. QED.

The same-carrier angular width is eventually small by canonical FS.4, so
the width hypothesis is available for sufficiently large canonical fans.
Under `Z_ext=O(D)`, canonical (67.6) gives `E_4=O(D)`, and (18) implies
`Rg(g-1)=O(D^2)`. Under `Z_ext=o(D^2)` it only gives
`Rg(g-1)=o(D^3)`. These are different scales and must not be conflated.

This attack does not close the square-root case: `g=Theta(sqrt(D))` and
`R=Theta(D)` cost only `Theta(D)`, compatible with the boundary-order
population budget. A complete crossing shore with the needed larger size
is not supplied by the fan-count theorem. No such extraction is assumed.

### 6.1 The remaining scalar ledgers are still compatible

The next attempted closure was to combine LF.2 with the current high-surplus
full-core ledger. That combination alone does not contradict it. The following
explicit family witnesses algebraic compatibility, not an embedded source.
For an integer `N>=15` divisible by five, set

$$
\begin{aligned}
h&=5N^2,&d_H&=\nu=N,&q&=h+N,&x_B&=0,\\
f&=Q=N^2-N/5,&s_Z&=2f,&c_I&=1,&e_{BB}&=q,\\
s_C&=N+2f-3,&k&=N+2f,&D&=q/\pi+1/2.
\end{aligned}
\tag{20}
$$

The identities `h=q-d_H`, `2h-q=x_B+Q+2s_Z`,
`q-x_B=Q+2k`, and `c_I+e_BB+s_C=q-2+k` all hold exactly.
A disjoint union of `N` stars, each with `5N` leaves, realizes the diameter
graph counts alone, including its matching number. Its internal fan-block
count is `A=h-N=5f`. The new stopped-train charge is saturated at the
incidence-count level: `A=Q+4f`. Also `s_Z=2f`, so (9) is satisfied.

In the limit, `h/D->pi`, `nu=Theta(sqrt(D))`, and

$$
{e_{BB}+2s_C-3k\over D}
={h-2f-6\over D}\longrightarrow{3\pi\over5}>1.88.
\tag{21}
$$

Thus this family lies above the canonical train-coupled floor
`1.6375621841815...` and its excluded exact endpoint. The hull perimeter
count `q=pi(D-1/2)` is within an absolute deficit of `pi D`.
It does not realize the simultaneous diameter/contact geometry, face
incidences, KKT stress, cells, or source population. It proves exactly why
the listed scalar identities and the new face floor do not supply a closing
contradiction. The required extra input is their simultaneous source geometry.

## 7. Exact verification and hostile checks

Command:

```text
python3 research/verify_target_c_leaf_fan_sector_2026_10_02.py
```

Output:

```text
PASS: 5 rational collars; 3053 full-source pair checks; 114 exact interior equilibrium rows; 62 strict rhombi
Scope: local collar regression only; no endpoint/carrier equilibrium, PSD, or global-optimality certificate.
```

The script uses `fractions.Fraction`. It checks all source pair bounds,
the complete contact and diameter edge sets, triangle-freeness, strict unit
rhombi, positive interior coefficients, exact equilibrium, interior-triangle
membership, and the unique support claim on the packets. It also checks
the rational consequence of (18) on each one-row collar by squaring a
positive rational bound against `3g^2/4`.

The analytic statements LF.1--LF.5 are proved above; finite packet survival
does not replace those proofs. In particular the script does not establish
the source normal form, Woodall, the full train-end charge, or global optimality.

| Attempt or regression | Disposition | Exact reason |
| --- | --- | --- |
| Connected gap graph alone is contradictory | Not used | Paths and stars have full graphic rank. |
| Internal inward spokes locally force non4 faces | Rejected local assertion | Rational rhombic collars satisfy positive interior equilibrium. |
| Local positive equilibrium proves global feasibility/optimality | Rejected inference | Carrier and endpoint rows are absent. |
| A fan train can end at a second parallel good hull contact | Excluded by LF.1 | Its opposite support is a singleton actual carrier. |
| A repeated bridge occurrence is a new contact | Not used | All endpoint and outer-walk charges retain multiplicity. |
| Linear s_Z with sublinear Q,x_B and nu | Excluded by LF.2/LF.3 | The actual fan train endpoints require linear face excess. |
| LF.5 alone closes square-root fans | Unproved and not inferred | Its area bill can still be boundary-order. |
| Dense inactive exterior population | Retained | The (67.6) bound keeps Z_ext explicitly. |
| Regular odd shell | Compatible | Its diameter graph has no pendant fans; nu is linear. |
| Universal vanishing-multiplier or private-leaf release | Not used | No multiplier floor or finite motion is assumed. |

## 8. Exact remaining gap and branch accounting

The durable new obstruction is physical:

$$
\nu=o(D),\ x_B=o(D)\quad\Longrightarrow\quad Q\ge(1/5-o(1))D.
$$

One closing obligation is now to rule out this **actual stopped-fan-train
endpoint population** in a completed canonical source, or turn it into a
strict same-cardinality sub-`D` competitor. A mere dimension count for `s_Z`
does not avoid it. The exact positive-equilibrium collar shows why local
spoke or rhombus arguments cannot discharge the remote endpoint obligation.

The common-crossing surcharge provides a second, conditional endpoint:
extract fan/common-shore crossings whose `Rg(g-1)` exceeds the actual
`8D E_4` budget, with the source exterior population retained. The present
run proves no extraction of that strength.

Still surviving are linear `x_B`, linear or larger matching, the linear `Q`
branch itself, nonconstant/exact-phase fixed-star branches not covered by
this fan charge, split-star O--O, inactive interfaces, higher-surplus
full-core sources, and the macroscopic inactive-container/exterior-cap branch.
Therefore no C-II or Level I closure is claimed.

Promotion recommendation: preserve as unreviewed candidates and a local
regression; seek independent audit of the endpoint-incidence proof. No
canonical state, active prompt, or status version is changed here.
