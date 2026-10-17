> Generated reading edition · [exact source](../../../docs/reports/target_c_diameter_ball_hull_lattice_discrepancy_2026-10-02.md) · source SHA-256 `9804deb271da2e2bac95bea94be069666ad3641ae463a5c500b7952bf71f415e`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-C0BC79F49781","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — logarithm-free diameter-endpoint lattice capacity

```text
uniform ball-hull Fourier bound -> actual loaded endpoint atlas capacity
 -> contradiction to q >= ceil(D) if K_D(epsilon_D + D^(-1/3)) -> 0.
The atlas concentration premise is unproved; Level I remains open.
```

- **Date:** 2026-10-02
- **Starting checkout:** `539f5187b3cac9287f6b30cdf6b36aafb1763c5a`
- **Fetched research base / starting branch HEAD:** `fbeae9b3fa18a63e07573676b4e2e512a91ca4d5`
- **Publication main:** `842df1ad675b9420a6b4bb34a816fd46087fc333`;
  the state lock, manifest, Target C route and CURRENT agree with the research base.
- **State version:** `2026-09-14.audit.51`
- **Branch:** `swarm/sol/diameter-curvature-flux-20261002`
- **Mission:** test a source-geometric replacement for packet multiplier floors;
  then attack the actual loaded endpoint atlas obstruction.
- **Classification:** proved candidates awaiting independent audit and promotion;
  conditional C-II application. Artifact lifecycle: unreviewed.
- **Level I / C-II:** STILL OPEN / OPEN.

## 1. Authority and exact scope

The state lock, manifest, Target C route and CURRENT remain authoritative. No
canonical state, route, prompt, or theorem dependency is changed here.

The geometric theorem below concerns **any** finite unit-separated planar source,
and any subset of its **actual diameter endpoints**. Its lattice is

$$
\Lambda=t+\mathbb Zu+\mathbb Zv,
\qquad |u|=|v|=1,\qquad \pi/3\le\angle(u,v)\le2\pi/3.
\tag{1}
$$

The lattice may depend on the source. All constants are uniform in its phase,
angle, orientation and translation. The source need not be a lattice subset,
a global optimum, near a disk, or a connected contact graph. Contact-isolated
source points are retained in every source disk and diameter constraint.

The C-II consequence uses only canonical
[ZR/ZF, Section 4](../targets/target-c/57-zr-zf-rigidity-audit.md), which gives
`h >= ceil(D)` on the nonisolated core, and the canonical
[Woodall topology](target_c_woodall_diameter_topology_2026-09-10.md), which gives
`h <= q`. Thus `q >= ceil(D)` in that scoped canonical source. The weaker
canonical [C34 boundary count](../targets/target-c/03-pinned-block-and-loaded-boundary-frontier.md)
also suffices for the asymptotic contradiction.

Prior work is acknowledged explicitly. The unpromoted
`target_c_diameter_support_atlas_obstruction_2026-09-26.md` on PR #591,
head fetched as `origin/pr-591`, gives
`|S| <= 136 D epsilon (1+log(1/epsilon)) + 33 D^(2/3)` for a more general
minimum-spacing lattice. Its actual-partner support inequality is rederived
below. The present novelty is removal of the logarithm **for (1)** by a uniform
curvature argument. No claim is made to dominate its arbitrary-lattice scope.
The earlier [exact affine boundary exclusion](target_c_affine_lattice_boundary_vertex_exclusion_2026-09-11.md)
already excludes exact charts; this report does not claim that old consequence
as new.

The October witness-cell, finite-swap, complete-grid immunity, gap-connectivity,
paired-staircase, and transverse-rail reports on starting main were inspected.
PRs #618--620 were also inspected. None is a premise for the geometric theorem.
In particular, no lower bound on an individual KKT multiplier is assumed.

## 2. Main theorem

**Theorem BH.1 (uniform thin lattice capacity).** There is an absolute constant
`C` with the following property. Let `A` be a finite unit-separated planar set
of diameter `D >= 1`. Let `S` be any subset of its actual diameter endpoints,
and let `0 <= epsilon <= 1/8`. If every member of `S` is within `epsilon` of
one lattice (1), then

$$
\boxed{|S|\le C\bigl(D\epsilon+D^{2/3}\bigr).}
\tag{BH.1}
$$

The constant does not depend on the number of source points, supporting disks,
boundary corners, or selected endpoints. This is a finite analytic theorem,
not a computation or an optimality certificate.

### 2.1 The genuine source ball hull

Put

$$
W=\bigcap_{a\in A}\overline B(a,D).
\tag{2}
$$

Every source point belongs to `W`. If `p` has an actual diameter partner `y`,
then `p` is on the circle `partial B(y,D)` and therefore on `partial W`.
Indeed, for `n_p=(p-y)/D` and every `x in A`, the actual source constraint
`|x-y| <= D` gives

$$
n_p\cdot(x-p)\le-\frac{|x-p|^2}{2D}.
\tag{3}
$$

The same normal supports all of `W` at `p`, because `W subset B(y,D)`.
This uses partners from the same source, never an independent packing.

Choose a diameter pair `z,a` and its midpoint `o`. For every source point `x`,

$$
2|x-o|^2+D^2/2=|x-z|^2+|x-a|^2\le2D^2.
$$

Consequently

$$
\overline B(o,(1-\sqrt3/2)D)\subset W
\subset\overline B(a,D),\qquad \operatorname{per}(W)\le2\pi D.
\tag{4}
$$

In particular `W` has nonempty interior, without any near-disk assumption.
Its boundary is a finite union of circular arcs of radius `D`, with convex
corners; redundant disks cause no difficulty. In tangent-angle measure its
arclength satisfies

$$
ds\le D\,d\theta.
\tag{5}
$$

At a corner the tangent angle jumps and the arclength contribution is zero.

For `r` smaller than the inradius in (4), write

$$
W_r^+=W+r\overline B(0,1),\qquad
W_r^-=\{x:x+r\overline B(0,1)\subset W\}.
$$

Erosion distributes over intersections, so

$$
W_r^-=\bigcap_{a\in A}\overline B(a,D-r).
\tag{6}
$$

Its boundary satisfies `ds <= (D-r)dtheta`. The outer parallel body has
arcs of radius `D+r` and rounded corner arcs of radius `r`, so it satisfies
`ds <= (D+r)dtheta`. No bound on the number or angles of corners is needed.

### 2.2 Uniform Fourier lemma, including corners

**Lemma BH.F.** Let `E` be a convex body with piecewise smooth boundary and
convex corners, and suppose its boundary arclength in tangent-angle measure
satisfies `ds <= R dtheta`. With Fourier convention

$$
\widehat f(\xi)=\int_{\mathbb R^2} f(x)e^{-2\pi i x\cdot\xi}\,dx,
$$

one has, for `xi != 0`,

$$
|\widehat{\mathbf1_E}(\xi)|\le C_F\sqrt R\,|\xi|^{-3/2},
\tag{7}
$$

where `C_F` is absolute and independent of the corners.

**Proof.** Rotate the integration coordinates so `xi = rho(1,0)`, with
`rho > 0`. The divergence theorem gives

$$
\widehat{\mathbf1_E}(\xi)
=-\frac1{2\pi i\rho}\int_{\partial E}n_1(s)
  e^{-2\pi i\rho x_1(s)}\,ds.
\tag{8}
$$

Let `theta` be a nondecreasing lift of the tangent angle. The stationary
parts, where `|cos(theta)| <= eta`, have total angular measure at most
`C eta` for `0 < eta <= 1/2`. Their total arclength is at most `C R eta`
by the hypothesis. Since `|n_1| <= 1`, their integral in (8) is at most
`C R eta` before the prefactor.

The remaining parts split into a bounded number of arcs, using the quadrant
boundaries and the stationary cuts. On each, the phase derivative
`x_1'(s)=cos(theta(s))` is monotone, has constant sign, and has absolute
value at least `eta`. The amplitude `n_1(s)=-sin(theta(s))` has total
variation at most `2 pi` around the whole boundary. The first derivative
estimate and bounded-variation partial summation therefore bound the
remaining integral by `C/(rho eta)`.

For completeness the first derivative estimate holds also across corners:
on a constant-sign arc, use the phase coordinate `t=x_1(s)`. The reciprocal
derivative `1/x_1'(s)` is monotone and bounded by `1/eta`; integrating the
exponential against this bounded-variation density bounds every partial
integral by `C/(rho eta)`. Partial summation against `n_1` proves the
weighted version. Jumps in `theta` change only these variations, not the
number of pieces. Thus arbitrarily many corners introduce no extra factor.

If `rho R >= 4`, choose `eta=(rho R)^(-1/2)` in
`C R eta + C/(rho eta)`. The boundary integral is
`O(sqrt(R/rho))`, which proves (7) after the prefactor. If `rho R < 4`,
use `per(E) <= 2 pi R`, a consequence of `ds <= R dtheta`; this gives
`O(R/rho) <= O(sqrt(R) rho^(-3/2))`. This covers all frequencies. QED.

### 2.3 A uniform dual-lattice sum

Choose a fixed nonnegative smooth function `psi`, supported in the open unit
disk, with integral one, and put `psi_delta(x)=delta^(-2)psi(x/delta)`.
Its Fourier transform satisfies

$$
|\widehat\psi(\zeta)|\le C_N(1+|\zeta|)^{-N}.
$$

For (1), the basis matrix has squared singular values
`1 +/- |cos(theta)|`, in `[1/2,3/2]`; its determinant is in
`[sqrt(3)/2,1]`. Hence the dual lattice `Lambda_0^*` has minimum spacing
at least `sqrt(2/3)`, uniformly. Disjoint disks around its points give
`#{k: |k| <= T} <= C T^2` for `T >= 1`, and there are only boundedly
many points below one. Dyadic summation, for `0 < delta <= 1`, gives

$$
\sum_{k\in\Lambda_0^*\setminus\{0\}}
|k|^{-3/2}(1+\delta|k|)^{-3}\le C\delta^{-1/2}.
\tag{9}
$$

Indeed shells of radius `2^j <= delta^(-1)` contribute `O(2^(j/2))`;
the later shells contribute `O(delta^(-3)2^(-5j/2))`. Both geometric
sums are `O(delta^(-1/2))`. Constants are uniform in (1).

### 2.4 Poisson sandwich for actual endpoints

Assume first `D >= 64`; set `delta=D^(-1/3)` and `r=epsilon+delta`.
Then `r <= 3/8`, less than the inradius in (4). Round each `p in S` to
a lattice representative `l_p` at distance at most `epsilon`. This map
is injective: otherwise two distinct source points would be at distance
at most `2 epsilon < 1`.

Define smooth compactly supported functions

$$
F_+=\mathbf1_{W_r^+}*\psi_\delta,\qquad
F_-=\mathbf1_{W_r^-}*\psi_\delta.
\tag{10}
$$

They satisfy `F_+ >= F_- >= 0`. At each rounded endpoint `l_p`, every point
in the open delta-ball lies in `W_r^+`, so `F_+(l_p)=1`. On the other
hand the supporting normal at `p` gives
`n_p dot l_p >= h_W(n_p)-epsilon`. Every point of the open delta-ball
around `l_p` has projection strictly greater than `h_W(n_p)-r`, whereas
every point of `W_r^-` has projection at most that quantity. Consequently
`F_-(l_p)=0`. Thus

$$
|S|\le\sum_{l\in\Lambda}(F_+(l)-F_-(l)).
\tag{11}
$$

Poisson summation applies to the smooth functions (10), with absolutely
convergent sums. Translation contributes phases of modulus one. The zero
frequency is the area difference divided by `det Lambda_0`. Steiner's
formula and inner parallel coarea give

$$
\begin{split}
\operatorname{area}(W_r^+)-\operatorname{area}(W_r^-)
&\le 2r\operatorname{per}(W)+\pi r^2\\
&\le C D(\epsilon+\delta).
\end{split}
\tag{12}
$$

For the inner loss, integrate `per(W_t^-) <= per(W)` over `0 <= t <= r`;
all the bodies here have interior. Lemma BH.F applies to both parallel
bodies with `R <= D+r <= 2D`. Equations (7), (9) and the determinant
lower bound control the nonzero frequencies by

$$
C\sqrt D\,\delta^{-1/2}.
\tag{13}
$$

Combining (11)--(13) and `delta=D^(-1/3)` proves BH.1.
For `1 <= D < 64`, the actual endpoints are strictly extreme source-hull
vertices by (3). Unit-separated hull sides and the perimeter-diameter bound
give at most `pi D` endpoints (also valid when there are only two).
Since `D <= 4 D^(2/3)` in this range, increasing the absolute constant
completes the theorem. QED.

## 3. Exact atlas consequence and threshold application

**Corollary BH.2.** In the canonical C-II source, suppose all but `b_D` of
the `q` loaded actual diameter endpoints are within `epsilon_D <= 1/8`
of a union of `K_D` lattices (1). Then

$$
\boxed{q-b_D\le C K_D(D\epsilon_D+D^{2/3}).}
\tag{BH.2}
$$

Assign each covered endpoint to one chart and apply BH.1 to those disjoint
subsets. No contact or co-embedding compatibility between charts is required.
Since canonical `q >= ceil(D)`, there is no survivor sequence with

$$
b_D=o(D),\qquad K_D\epsilon_D\longrightarrow0,
\qquad K_DD^{-1/3}\longrightarrow0.
\tag{14}
$$

This removes the old sufficient condition
`K_D epsilon_D log(1/epsilon_D) -> 0` for the restricted atlas (1).
For example `K_D=D^(1/4)` and
`epsilon_D=D^(-1/4)/sqrt(log D)` meet (14), while the old logarithmic
noise upper bound does not tend to zero after division by `D`.

Conditional on main's unpromoted threshold staircase and rail extraction,
each internal layer contributes a distinct actual endpoint to each extreme
rail. Thus either rail has at least `m-1 >= (c_*-o(1))D` endpoints. The
same argument rules out covering either entire rail, apart from `o(D)`
exceptions, by charts satisfying (14). This is a necessary chart-complexity
condition, **not** a theorem that the rails possess such charts.

## 4. Immediate next attack and exact failure

The next attempted implication was that the nearby complete grid automatically
continues an exact lattice chart to a loaded endpoint with two chart contacts.
That implication is false. The verifier checks six exact cosine values in
the following parameterized family.

Take `u=(1,0)`, `v=(c,s)`, `c^2+s^2=1`, `0 < c < 1/2`, `s > 0`.
Let `w=2u-v`, so `3 < L=|w|^2=5-4c < 5`. Restrict to `c > 1/4`,
so `L < 4`, and set

$$
p=\frac w2+Jw\sqrt{\frac{4-L}{4L}}.
\tag{15}
$$

Then `|p|=|p-w|=1`. Both neighbors `0,w` belong to the one unit-rhombic
chart `Zu+Zv`, but `p` does not: if `p=iu+jv` had norm one, the open
angle range has only the unit lattice vectors `+/-u,+/-v`. None is unit
distance from `w`, since the two formerly unit candidates `u` and `u-v`
at `c=1/2` cease to be such a pair; `u-v` is not itself a unit vector.
To check the unit-vector assertion directly, for `ij>=0` one has
`|iu+jv|^2>=i^2+j^2`, and for `ij<0`, writing `a=|i|,b=|j|`,
one has `|iu+jv|^2=(a-b)^2+2ab(1-c)`. For `c<1/2` this is
greater than one whenever both coefficients are nonzero. Hence only the
four basis unit vectors remain. Testing those four vectors against `w`
verifies the claim.
The three-point source is unit separated and triangle-free, since
`|w|=sqrt(L)>1`.

This can be made an actual diameter-endpoint example for arbitrarily large
`D`. Write `n=(p-w/2)/|p-w/2|` and add `y=p-Dn`. Then `|p-y|=D` and

$$
|y|^2=|y-w|^2=D^2-2D\sqrt{1-L/4}+1<D^2
\tag{16}
$$

for sufficiently large `D`. All lower distance constraints also hold for
large `D`. Thus `p` is an actual diameter endpoint with two contacts to
one exact chart, yet is outside that exact chart. There is no asserted
positive full-source equilibrium, actual retained train, or global optimality.
The regression kills this local continuation implication only.

For `c -> 1/2`, (15) approaches a lattice point; hence this does not reject
an approximate continuation theorem with an explicitly accumulated error.
Such an error theorem must cover the whole linear endpoint population and
meet (14). Neither one grid nor `c_I=O(sqrt(D))` establishes it.

## 5. Repaired local continuation: a quantitative two-port theorem

The failed exact implication in Section 4 has a useful repair.

**Theorem BH.3 (two exact chart ports).** Write a chart as `t+Zu+Zv`
with unit basis vectors and `c=u dot v in [9/20,1/2]`. Suppose a point `p`
has unit contacts to two distinct points of this chart, and those three
points are part of one unit-separated triangle-free source. Then

$$
\boxed{\operatorname{dist}(p,t+\mathbb Zu+\mathbb Zv)
       \le20(1/2-c).}
\tag{BH.3}
$$

The point need not be a diameter endpoint for this local statement. The
endpoint hypothesis enters only when applying BH.1 afterwards. The bound
is exact, uniform, and tends to zero without a square-root loss.

**Proof.** Translate one neighbor to zero, rotate `u=(1,0)`, and take
`v(c)=(c,sqrt(1-c^2))`. Let the other neighbor be `w=iu+jv(c)`.
The two unit circles meet only if `|w|<=2`. The Gram minimum eigenvalue
is at least `1/2`, so `i^2+j^2<=8`. Enumerating this fixed integer disk
gives, up to sign, only

$$
u,\quad v,\quad u-v,\quad u+v,\quad 2u-v,\quad u-2v,
\quad 2u,\quad 2v,
\tag{17}
$$

and `2(u-v)` at `c=1/2` only. For example the other mixed vectors have
squared norm at least `5+4c>=34/5>4`, while
`|2(u-v)|^2=8-8c>4` for `c<1/2`. This enumeration does not assume
that the contact point itself is on the chart.

The cases `w=+/-u,+/-v` are impossible: the two neighbors are themselves
at unit distance and would complete a unit triangle with `p`.
For `w=u+v`, both circle intersections are exactly `u,v`.
For `w=2u,2v`, the single intersection is their midpoint, a chart point.
At `c=1/2` the additional touching case also has a chart midpoint.
These cases have zero error.

For each of the remaining types the intersections are

$$
p_\pm(c)=w(c)/2\pm Jw(c)a(L(c)),\qquad
a(L)=\tfrac12\sqrt{(4-L)/L},\qquad L=|w|^2.
\tag{18}
$$

Throughout the allowed interval, `1<=L<=16/5`, `|L'|<=4`,
`|w|<2`, and `|w'|<=12/5`. Also

$$
|v'|=1/\sqrt{1-c^2}<6/5,\qquad
|a|<1,\qquad |a'|=1/(L^{3/2}\sqrt{4-L})<5/4.
$$

Consequently `|p_+'|,|p_-'|<14`. At `c=1/2` their chart coordinates
are, up to sign,

| Neighbor difference | Circle intersections at `c=1/2` |
| --- | --- |
| `u-v` | `u`, `-v` |
| `2u-v` | `u`, `u-v` |
| `u-2v` | `-v`, `u-v` |

Track either corresponding chart point `z(c)` with these same integer
coefficients. Its derivative has norm at most `6/5`. Hence integrating
from `c` to `1/2` gives
`|p_+(c)-z(c)|` or `|p_-(c)-z(c)| less than
`(14+6/5)(1/2-c)`, which is at most the claimed bound. Negative
differences are covered by simultaneous reflection. QED.

**Corollary BH.4 (actual two-port collar capacity).** Let `B_2` be any
subset of actual diameter endpoints of a unit-separated triangle-free
source, each having two unit contacts to one fixed chart in the above
angle range. If `delta_c=1/2-c<=1/160`, then BH.1 and BH.3 give

$$
\boxed{|B_2|\le C(20D\delta_c+D^{2/3}).}
\tag{BH.4}
$$

For `delta_c=O(1/D)`, this is `|B_2|=O(D^(2/3))`. In a canonical
source with `q>=D`, linearly many loaded endpoints therefore have
**at most one** contact into any one such exact grain. The same holds
on an extracted actual linear rail, conditional on that extraction.
This is a concrete restriction on the collar rather than a claimed
continuation of the chart to it.

Assigning endpoints to `K_D` exact charts gives the same contradiction
as (14) when all but `o(D)` loaded endpoints have two contacts into
one assigned chart, `K_D delta_c -> 0`, and `K_D=o(D^(1/3))`.
Thus this next attack closes the two-port-dominated subcase, but
does not prove that the canonical source is in that subcase.

### Attempt to continue through one port

One exact chart contact supplies no small error at all. Take the
triangle-free two-point contact `0,p`, with `|p|=1` and `p` outside
the triangular lattice; `p=(3/5,4/5)` is an exact example with
`|p|^2=1`. In the triangular chart `u=(1,0)`,
`v=(1/2,sqrt(3)/2)`, the only unit lattice points are its six unit
neighbors, so this `p` is outside the chart. Add `y=(1-D)p` for
any integer `D>=3`. Then `p,y` are an actual diameter pair,
`|0-y|=D-1`, and `p` still has its one chart contact. The error
does not tend to zero with `D`, even at zero chart-angle excess.
There is no claimed canonical stress or global optimality.

This exact regression rules out using contact adjacency alone to
repair the one-port collar left by BH.4. A source-level restriction
on that collar is necessary. No additional chart-propagation
assertion is made.

## 6. Pushing the port theorem: three ports force an exact chart

**Theorem BH.5 (exact three-port closure).** For `c in [9/20,1/2]`,
a point at unit distance from three distinct members of `t+Zu+Zv`
is itself in that chart. No triangle-free or diameter hypothesis is needed
for this local statement.

**Proof/certificate.** Translate one of the three centers to zero. The
other two have differences `a=(i,j)`, `b=(k,l)` in the integer disk
`0<i^2+j^2<=8` of the preceding proof. The centers cannot be collinear:
a circle and a line have at most two distinct intersection points. Put

$$
Q_c(i,j)=i^2+j^2+2ijc,\qquad d=il-jk\ne0.
$$

Each of `Q_c(a),Q_c(b),Q_c(a-b)` is at most four, and circumradius
one is exactly

$$
Q_c(a)Q_c(b)Q_c(a-b)-4(1-c^2)d^2=0.
\tag{19}
$$

Every factor is affine in `c`. Enumerate the finite integer disk and retain
the unordered independent pairs for which each of the three squared lengths
is at most four somewhere in `[9/20,1/2]`. Checking both interval endpoints
is exact for this necessary filter; it may retain extra pairs, never omit
a genuine one. There are 72 pairs. The certificate computes (19) as a
polynomial with integer coefficients, and verifies the following entire
factor table, normalizing nonzero polynomials to monic form.

| Polynomial, up to nonzero constant | Pair count |
| --- | ---: |
| Identically zero | 12 |
| `(2c-1)^2` | 12 |
| `(c-1)^2` | 6 |
| `(c-1)(2c-1)` | 24 |
| `(c+1)(2c-1)(8c-7)` | 6 |
| `(c+1)(2c-1)` | 6 |
| `(c-1)(2c+1)` | 6 |

The nonzero rows have no root in `[9/20,1/2)`. For each identity,
solving the two linear circumcenter equations symbolically in the basis
`u,v` yields exactly one of `+/-u,+/-v`. Thus that unit-circle center
is a chart point throughout the interval. At `c=1/2`, every candidate
with (19) zero has integer circumcenter coefficients; the certificate
checks these coefficients exactly as well. This covers the endpoint.
The finite polynomial enumeration and identities prove BH.5. QED.

This is a further repair rather than a geometric global-optimality claim.
The certificate proves the finite classification over the continuous angle
interval; it does not sample cosines to infer it. If a candidate theorem
using this finite table is promoted, register this script in its `certificates`
field. It is deliberately not registered as a canonical certificate here.

The next closure attempt was to propagate a chart by repeatedly adding
vertices with three old chart neighbors. Such a rule cannot even leave a
rectangular grid in the square-lattice contact graph: every outside lattice
site adjacent to that rectangle has at most one neighbor in the rectangle.
An exact chart and degree four therefore do not by themselves supply the
three-neighbor extension ordering. Near the triangular angle the contact
graph of the open unit-rhombic chart is the same square grid, so this
combinatorial obstruction applies there too. No bootstrap ordering has
been proved for the actual boundary collar. The surviving one-port collar
is the precise obstruction left by the tested continuation mechanisms.

## 7. Continuing through one port: positive contact leaves

The arbitrary one-port regression omits equilibrium. Actual equilibrium
recovers a different thin-boundary chart charge.

**Theorem BH.6 (one-chart loaded contact-leaf capacity).** Let `A` be a
global minimum-diameter unit-separated source of large diameter `D`, and
fix a normalized KKT stress. Let `L_1` be a set of source vertices `p`
having exactly one actual unit neighbor `l`, with positive contact
multiplier. If every such neighbor lies in one chart (1), then

$$
\boxed{|L_1|=O(D^{2/3}).}
\tag{BH.6}
$$

The estimate is uniform in the source and chart. It needs no floor on
any positive multiplier. It applies to canonical contact leaves, where
full-support positivity supplies the stipulated contact multiplier.
The new global-source dependency is canonical
[FS.1](../targets/target-c/58-full-source-geometry-audit.md), retaining
every source point. KKT equilibrium is canonical
[Theory 01, Theorem 4.1](../theory/01-local-structure.md).

### 7.1 Near-diameter directions at an actual loaded point

Put `eta=3^(1/4)sqrt(D)`, translate the full-source circumcenter to zero,
and use FS.1 to take `R<=D/2+eta`. Positive contact stress at `p`
requires at least one positive diameter edge there by equilibrium and
extremality; alternatively this follows immediately because its one
nonzero contact force cannot equal an empty diameter sum. Thus `p`
is an actual endpoint and `|p|>=D-R`. Write `e=p/|p|`.

For any `a in A` with `d=|p-a|>=D-2`, let `u_a=(p-a)/d`. Since
`|a|<=R`,

$$
u_a\cdot e
=\frac{|p|^2+d^2-|a|^2}{2d|p|}
\ge\frac{D^2/2-D\eta-2D+2}{D^2/2+D\eta}
\ge1-t,\qquad t=\frac{4(\eta+1)}D.
\tag{20}
$$

Use `D>=65536`, so the numerator is positive and `t<1`.
At `p`, the leaf equilibrium is

$$
\alpha(p-l)=\sum_y\beta_{py}(p-y),\qquad \alpha>0.
\tag{21}
$$

All summands on the right are actual diameter vectors with nonnegative
weights. Hence the unit contact direction `n=p-l` satisfies `n dot e>=1-t`:
its unnormalized projection is at least `1-t` times the sum of vector
lengths, while its norm is at most that same sum. For every near-diameter
`u_a`, the triangle inequality between these unit vectors and `e` gives

$$
u_a\cdot n\ge1-4t.
$$

Set `zeta=4t`, `epsilon_1=2 zeta=32(eta+1)/D`. For `d>=D-2`,

$$
|l-a|^2\le(d-1)^2+2d\zeta,
\qquad |l-a|\le d-1+2\zeta\le D-1+\epsilon_1.
\tag{22}
$$

The middle inequality follows by squaring, since `d>=2`. If `d<D-2`,
the triangle inequality gives `|l-a|<=d+1<D-1`. Therefore, for all source
points, including every isolate,

$$
l\in W_{1-\epsilon_1}^-=
\bigcap_{a\in A}\overline B(a,D-1+\epsilon_1),
\qquad \epsilon_1=O(D^{-1/2})<1/2.
\tag{23}
$$

In particular `l` itself cannot be an actual diameter endpoint in this
regime. That latter qualitative exclusion is prior scope of PR #620;
novelty here is the chart-capacity consequence, not that exclusion.

### 7.2 A thin inner parallel boundary, not a wide radial annulus

Let `K=W_1^-`. Each positive diameter vector at `p` is an outward
normal of `W` at `p`, so their positive sum in (21) is also a supporting
normal there. Thus `h_W(n)=n dot p`. Since `K+B(0,1) subset W`,

$$
h_K(n)\le h_W(n)-1=n\cdot l.
\tag{24}
$$

Consequently `l` is on or outside a supporting line of `K`, not in its
interior. Formula (4), with midpoint `o` of any actual diameter pair,
puts a ball of radius
`r_*= (1-sqrt(3)/2)D-1 >= D/8` in `K` for `D>=128`.
For any `x` in the larger body in (23), contract it toward `o` by the
factor `lambda=r_*/(r_*+epsilon_1)`. For every disk center `a`,

$$
|o+\lambda(x-o)-a|
\le\lambda(D-1+\epsilon_1)+(1-\lambda)|o-a|
\le D-1,
$$

because `|o-a| <= (sqrt(3)/2)D` and the last two error terms cancel.
The contracted point is in `K`. Also `|x-o|<2D`, so its displacement
is at most `16 epsilon_1`. Apply this to `x=l`. Together with (24),
this proves

$$
\operatorname{dist}(l,\partial K)\le16\epsilon_1=O(D^{-1/2}).
\tag{25}
$$

This controls distance to the actual inner ball-hull boundary. It does
not replace that boundary by a circumcircle of width `O(sqrt(D))`.

### 7.3 Count exact chart neighbors and their leaf multiplicity

The proof of BH.1 used actual endpoint status only to put a rounded
representative near the boundary of a curved body. Apply exactly its
Poisson sandwich to lattice points within `rho=16 epsilon_1` of
`partial K`, once `rho<=1/8`. Here
`K=intersection_a B(a,D-1)` has curvature radius at most `D-1`,
perimeter at most `2 pi D`, and inradius at least `D/8`. Its relevant
outer/inner parallels therefore meet every uniform Fourier and smoothing
hypothesis. It follows that the number of distinct possible neighbors is

$$
O(D\rho+D^{2/3})=O(D^{2/3}).
$$

A single unit-separated source point has at most six unit neighbors,
by the elementary angle packing on its unit circle. Thus at most six
members of `L_1` share one chart neighbor. This proves BH.6. QED.

### 7.4 The remaining collar has loaded-loaded edges

Suppose, as a **conditional source hypothesis**, every unit neighbor
outside the loaded set is in one exact near-triangular chart with
`1/2-c=O(1/D)`. BH.4 removes all but `O(D^(2/3))` loaded vertices
with two such neighbors; BH.6 removes the contact leaves attached there.
If a remaining loaded vertex has any chart neighbor, it must therefore
also have a loaded unit neighbor. Otherwise its full contact degree would
be one, or at least two into the chart, both already counted.

This forces a linear loaded-loaded collar when the chart reaches a
linear loaded population. It is compatible with canonical high surplus;
the loaded unit-edge graph can contain long paths or a cycle. No uniform
lower bound on its contact multipliers, simultaneous release, or chart
error propagation along those paths has been established. This is the
precise next obstruction after the tested one/two/three-port mechanisms.

## 8. Stress-floor attack disposition

PR #619 already gives a normalized, fully equilibrated regular odd-shell
family with a coercive scalar stress but an arbitrarily small diameter
multiplier. PR #618 gives positive definite formal cut models at arbitrarily
small packet mass; they deliberately omit joint Euclidean realization.
These distinct regressions prevent inferring the required load floor from
positivity, rank, or PSD alone. This report does not repeat them or assert that
they are global minimizers. The ball-hull argument uses no multiplier floor.

## 9. Computation, literature, and hostile audit

`research/verify_target_c_ball_hull_lattice_2026_10_02.py` checks rational
antipodal sources, every encoded pair-distance constraint, the support-margin
inequality (3), midpoint containment (4), representative injectivity, an exact
thin-parabola non-endpoint regression, the dual singular-value normalization,
the complete finite difference classification (17) over the indicated
angle interval, the endpoint chart coordinates used in BH.3, all 72
continuous-angle circumradius polynomials and their exact centers in BH.5,
and the algebraic two-contact and rational one-contact continuation regressions.
These checks corroborate geometry and falsify the stated local implication.
The Fourier and Poisson proof is analytic; finite checks do not certify it
or establish global optimality. Encoded and omitted hypotheses are documented
in the script and `research/README.md`.

Validation performed with Python in `/home/cinna/.cache/e99-ball-hull-venv`:
the exact verifier passed 360 rational source pairs, 720 support margins,
48 midpoint bounds, 48 rounded representatives, 5,947 thin-parabola pairs,
24 difference-alphabet cases, 72 three-port polynomials including 12 identities
and 60 exact triangular centers, 20 rational leaf-location bounds,
12 rational one-port pairs, and 18
algebraic two-port sources with 108 exact pair identities. Python compilation,
six relative report links, `tools/check_theorem_state.py --base-ref fbeae9b3`,
`tools/check_active_route_summaries.py`, and `git diff --check` passed.
Metadata generation also supplies 28 report headers/index entries missing on
starting main, plus this report, all as unreviewed. It does not promote them.
Merging publication main and regenerating the index resolves its generated-file
conflict and supplies five metadata headers missing on that newer base; no
canonical lifecycle or theorem content changes.

The primary paper [Iosevich--Sawyer--Seeger, *Mean lattice point discrepancy
bounds, II: Convex domains in the plane*](https://arxiv.org/html/math/0501113)
was checked for rough-boundary scope and the divergence/Poisson identities,
Section 2, equations (2.7)--(2.8). Its mean-square theorems are **not** imported
as a pointwise estimate. In particular their domain-dependent constants do
not supply the required uniformity across source ball hulls. Lemma BH.F and
the uniform dual sum above supply that missing argument directly.

Hostile checks: paths and stars require no Euler inference; missing arcs in
the loaded hull are allowed; every rounded point is an actual endpoint of
the original source; corner count introduces no factor; the two-sided
Poisson sandwich treats points on boundaries; the smoothing scale fits
inside an explicit ball; the lattice conditioning hypothesis is retained;
isolated points are never dropped. Thin-parabola hull vertices cannot be
substituted for actual diameter endpoints. No infinitesimal motion is called
finite or feasible, and no atlas is silently manufactured from one grain.

## 10. Exact remaining gap and branch ledger

The missing source theorem for this mechanism is:

> Every sufficiently large canonical triangle-free C-II source has a
> loaded-endpoint atlas of unit-rhombic charts with `b_D=o(D)` exceptions
> and `K_D(epsilon_D+D^(-1/3)) -> 0`.

It is not proved, and it is not assumed as a canonical premise. For a
threshold-only application it is enough to prove the same statement for
one actual linear extreme rail. The local two-contact shortcut above fails.
The next valid attack must control accumulated chart error and the actual
boundary collar, or replace chart concentration by a finite source competitor.

Open-cell exact phase, threshold staircase, nonconstant-phase swaps,
split-star O--O, inactive-interface, the higher-surplus full-core branch,
and macroscopic inactive-container/exterior-cap branches remain open.

**Promotion recommendation: unreviewed.** Audit BH.F at corners, erosion and
the boundary sandwich, the uniform dual sum, and the exact source scope.
Only BH.1--BH.6 are candidates for promotion. The missing concentration
theorem and the conditional threshold application are not promotion claims.
