<!-- theorem-state: {"artifact_id":"ART-A6F2F48ADC03","canonical":true,"claim_ids":["C-ONE-DEFICIT-ALL-M-SOURCE-EXCLUSION","C-ONE-DEFICIT-ALL-M-STRICT-PACKET","C-ONE-DEFICIT-PROFILE-ROOT","C-SIX-SIDED-WALL-OLER-POPULATION-CAP"],"claim_statuses":{"C-ONE-DEFICIT-ALL-M-SOURCE-EXCLUSION":"canonical","C-ONE-DEFICIT-ALL-M-STRICT-PACKET":"canonical","C-ONE-DEFICIT-PROFILE-ROOT":"canonical","C-SIX-SIDED-WALL-OLER-POPULATION-CAP":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit — Target C all-M one-deficit sector peeling

**Audit base:** `main` at `240c741581d7bbf19ecdf51348008e99a39a1649`, state `2026-10-07.audit.76`.

**Frozen discovery snapshots:** the profile-flexible root lemma and M5 certificate at `research/sol/target-c-overnight-closure-20261007` commit `c0511982e8a62466d5580025c94e750a177e63e2`; the all-M sector-peeling report and verifier at the same branch commit `01328c80`.

At refresh the branch had advanced to `a7da4b06`. The M5 root report, all-M sector-peeling report, sector verifier, and sector certificate were unchanged. The later tip adds a separate maximum-population report; it is not audited here.

## Exact claims audited

For a fixed integer `M>=3`, fix a strictly decreasing symmetric real profile
`a_0>...>a_(M-1)` with `a_(M-1-h)=-a_h`. The rate-sum chart is built from
`z_h=exp(i*a_h*theta)`, `S_r=sum_(h<r) z_h`, and

`p(a,b)=S_a*u+(S_(a+b)-S_a)*v`, `a,b>=0`, `a+b<=M`,

where `u=1`, `v=exp(i*pi/3)`, and the chart is rotated through six sectors.
For every sufficiently small positive `theta` (with onset allowed to depend on
`M` and the profile), the following exact statements survive:

1. **Profile root.** With `A=a_0`, `Delta=a_0-a_1`, `w=v-u`, `h=(1,M-2)`,
   and `v_0=p(1,M-1)`, the point
   `r=v_0+3*sin(Delta*theta/2)*J(exp(i*(a_0+a_1)*theta/2)*w)` lies strictly
   inside the wall and has distance greater than one from every chart/wall
   point except the intentionally omitted `h` and the deleted wall vertex
   `v_0`.
2. **All-M packet.** For every fixed `M>=4`, deleting the auxiliary chart site
   `h`, strictly opening all `N-1` remaining interior sites, and adding that
   root gives `N=3M^2-3M+1` pairwise strictly separated sites strictly inside
   the wall, clear of every wall vertex except `v_0`.
3. **Full-source exclusion.** If a contact-minimal, then diameter-pair-minimal
   triangle-free global minimizer contains this actual wall and has at most
   `N-1` old source points in its interior, no such source exists. The old
    interior cloud is arbitrary; exterior source points and contact isolates
   are retained.
4. **Population cap.** For each fixed `M` and profile, the finite Oler bound
   gives `z<=N` for all sufficiently small positive curvature in this wall
   class.

The exact chain is:

`sector peeling -> no nonnegative dependence among all moving-contact rows -> strict opening -> protected root -> N interior sites -> replace z interior labels and one wall vertex -> zero new contacts and at least two lost contacts -> contact-minimality contradiction`.

## Independent proof reconstruction

### Chart geometry and complete contact graph

Symmetry makes `S_M` real, so the six sectors close. Each side consists of unit
edges with the rates in ascending order. For fixed profile and `M`, all within-
side turns and all six corner turns `pi/3-2*A*theta` are positive for small
positive `theta`; the wall is strictly convex. At `theta=0` the chart is a
finite triangular-lattice hexagon. Every non-neighbor pair has squared length
at least three, so continuity preserves strict lower slack for small `theta`.

For an off-axis interior site `(a,b)`, `r=a+b<M`, the four exact contact
vectors are

- `F = z_(a-1) w`,
- `-z_a w`,
- `D = z_r v`,
- `-z_(r-1) v`.

The other two flat nearest-neighbor vectors have squared lengths
`2-2*cos(pi/3+(a_(a-1)-a_(r-1))*theta)` and
`2-2*cos(pi/3+(a_a-a_r)*theta)`. Strict decrease of the profile makes both
strictly greater than one for sufficiently small positive `theta`. On a
radial axis there are five exact contact vectors; the omitted sixth has squared
length `2-2*cos(pi/3+(a_0-a_r)*theta)>1`. The center has its six exact radial
contacts. This accounts for every potential flat nearest neighbor and leaves
all remaining pairs at a strict limiting gap. Thus the row system includes the
complete moving-involving contact graph, not a selected subset.

### No nonnegative dependence among the contact rows

Let `R` contain every unit-distance gradient with at least one moving endpoint,
with the hole `h` removed and all wall vertices pinned. Suppose
`lambda>=0` and `R^T lambda=0`. At each moving site the incident edge weights
balance the corresponding unit vectors.

At an off-axis site, if `F` has zero weight, the angular gap from `D` to the
inward diagonal is
`pi+(a_(r-1)-a_r)*theta>pi`; the other surviving vectors lie in the
complementary arc of length less than `pi`. If `D` has zero weight, the gap
from the backward ring vector to `F` is
`pi+(a_(a-1)-a_a)*theta>pi`, again leaving every other vector in an open
semicircle. A nonzero nonnegative combination of vectors in an open
semicircle cannot balance to zero. Therefore either zero forces every incident
weight at that off-axis site to zero.

The absent hole supplies such a zero edge for every off-axis site in its
sector: follow `a-1` `F` steps and `M-1-(a+b)` `D` steps to `h`, then propagate
backwards. On the `u` axis, the two transverse edges at each
`2<=r<=M-2` now have zero weight. The three remaining directions lie in an
open semicircle because the gap between `z_r*u` and `-z_(r-1)*u` is
`pi+(a_(r-1)-a_r)*theta>pi`; this range is nonempty exactly for `M>=4`.
This seeds the axis. At `r=1`, the outward axis and one transverse edge are
already zero, leaving three directions spanning `2*pi/3`. At `r=M-1`, the
inward axis and other transverse edge are zero; the remaining directions have
a gap `pi+(a_0-a_(M-1))*theta>pi` and their complementary arc is less than
`pi`. Thus the full axis has zero incident weights. Rotating the argument and
propagating along `F` empties all six sectors; the center edges then vanish
as well. Hence `lambda=0`.

Gordan's strict alternative gives a velocity vector making every row of `R`
strictly positive. For each fixed allowed `theta`, inactive lower pairs and
interior support-line constraints have strict slack. A sufficiently small
positive finite amplitude therefore opens every old contact while preserving
all those constraints. This is not an inference from a weak first-order
motion: every active row is strict and the remaining finite list has positive
slack.

### Profile-flexible root

Symmetry and strict ordering imply `0<=a_1<A`, so `0<Delta<=A`. The two wall
tangents incident with `v_0` have rates `a_1` and `a_0`; the root direction is
their angular midpoint. With `s=sin(Delta*theta/2)`, direct expansion gives
squared distances `1+3*s^2` to both adjacent wall vertices. At zero curvature,
the only other interior unit neighbor is `x=(0,M-1)`. Using
`v_0'=-A*Jw`, `x'=A*Jv`, and `r'=(3*Delta/2-A)*Jw`,

`(v_0-x) dot (r'-x') = (sqrt(3)/2)*(2*A-3*Delta/2)>0`.

The omitted site `h` has the opposite derivative `-3*sqrt(3)*Delta/4`, which
is why it must be absent. Every other chart/wall distance has a strict limiting
margin. For a wall support edge `j` on the side containing `v_0`, let `b_j` be
its ascending rate and `alpha_j=sum_(h<j)b_h`. The inward signed-cross
coefficient is

`3*Delta/2 - A - alpha_j - b_j*(M-1-j)`.

Since `b_h>=b_j` for `j<=h<=M-2` and
`sum_(h=0)^(M-2)b_h=-A`, this coefficient is at least `3*Delta/2>0`.
Every other wall support has positive slack at zero curvature. This proves
strict interior containment and root clearance for each fixed profile. No
uniform onset in `M` or in the profile is used.

### Full-source contact loss and scope

The packet points lie strictly inside the actual wall and are strictly farther
than one from every retained wall vertex. Canonical
`C-ONE-VERTEX-CONVEX-WALL-SHIELD` therefore gives strict unit-clearance from
every retained exterior source point, including contact isolates. If `z<=N-1`,
choose any `z+1` points from the strict `N`-site packet, delete all `z` old
interior labels and `v_0`, and insert those points. Every new point is interior
to `conv(A)`, so its distance to every retained point is strictly below the old
diameter `D`; all old-old constraints remain unchanged. No new unit contact
appears, while the two unit wall edges incident to `v_0` disappear. The
canonical finite contact-budget endpoint then contradicts contact-minimality.
This uses `C-CONTACT-BUDGET-DIAMETER-EXCHANGE-ENDPOINT` and retains the full
source, including isolates.

The result does not exclude `z=N`, does not extract such a wall from an
arbitrary canonical source, and gives no curvature onset uniform in growing
`M`. The `M=3` verifier stall only shows that this particular pruning proof
lacks its axis seed there; it is not an impossibility theorem.

The finite Oler inequality (Lemma 21.1 of
`docs/theory/03-oler-shell.md`) gives
`z+6M <= (2/sqrt(3))*area(W_theta) + (1/2)*perimeter(W_theta)+1` for the
`z+6M` old points in the closed convex wall. Since the wall has perimeter
`6M`, its right side is continuous for each fixed profile and converges as
`theta` tends to zero to
`(2/sqrt(3))*area(H_M)+3M+1=3M^2+3M+1=N+6M`. It is therefore strictly below
`N+6M+1` for all sufficiently small positive `theta`; integer rounding gives
`z<=N`. This is a fixed-`M`, fixed-profile onset and does not assume a
one-sided direction of convergence for the Oler expression.

## Certificate audit

The all-M source verifier was inspected and rerun at `01328c80`; its saved JSON
was reproduced byte-for-byte. Its finite checks use the worker branch's newer
optional-parameter change to a shared chart helper. I built an audit copy with
the exact chart formula inlined; it also reproduces the saved output. An
additional exact audit checker covers two nonuniform profiles, `(5,1,-1,-5)`
for `M=4` and `(8,4,1,-1,-4,-8)` for `M=6`, at `t=1/10000`. It certifies all
92/212 opening rows, respectively, and checks every chart pair, finite packet
lower and upper pair, wall support, and wall diameter comparison at rational
amplitude `10^-24` in `Q(sqrt(3))`.

The already-canonical Audit.76 exact root checker also reproduces its five
registered finite cases. All finite computations here validate only their
listed profiles and parameters; the all-M and all-profile conclusions come
from the analytic proof above.

## Verdict and canonical disposition

**PASS — promoted in Audit.77.** The M5 report is subsumed by the stronger
all-fixed-`M` theorem; no separate M5-only theorem ID is needed. The canonical
stack now records the profile root, all-M strict packet, and its full-source
`z<=N-1` exclusion as separate claims. The M3 stall remains a method-scope
note, not a theorem that no packet exists.

The highest-population `z=N` classification and arbitrary wall extraction
remain open. The global Target C-II and Level I status do not change.

## Audit.242 clarification — interior isolate accounting

The source-exchange wording above that says it retains “exterior source points and contact isolates” is too broad if read to include contact-isolated labels strictly inside the wall. The exchange explicitly deletes all `z` strict-interior labels (including any interior contact isolates) and one wall vertex, then inserts `z+1` packet points. Interior isolates are counted in `z`, so source cardinality is preserved, but their label identities are not retained. All source points outside the wall, including exterior contact isolates, are retained. The all-`M` nonexistence conclusion is unchanged.
