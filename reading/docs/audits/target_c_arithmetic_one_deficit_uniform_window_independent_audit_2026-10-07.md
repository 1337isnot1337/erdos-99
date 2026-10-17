> Generated reading edition · [exact source](../../../docs/audits/target_c_arithmetic_one_deficit_uniform_window_independent_audit_2026-10-07.md) · source SHA-256 `9e62e2fb5e76ed82c186850ddbd6b7265aa37627a7175b959818ebe0b63a17a3`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-597123669A15","canonical":true,"claim_ids":["C-ONE-DEFICIT-ARITHMETIC-WINDOW-OLER-CAP","C-ONE-DEFICIT-ARITHMETIC-WINDOW-SOURCE-EXCLUSION","C-ONE-DEFICIT-ARITHMETIC-WINDOW-STRICT-PACKET"],"claim_statuses":{"C-ONE-DEFICIT-ARITHMETIC-WINDOW-OLER-CAP":"canonical","C-ONE-DEFICIT-ARITHMETIC-WINDOW-SOURCE-EXCLUSION":"canonical","C-ONE-DEFICIT-ARITHMETIC-WINDOW-STRICT-PACKET":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit — arithmetic-profile one-deficit window

**Audit base:** `main` at `02471eb7b663a6dd93b12ccb13f5a49f5d13b7f6`, state
`2026-10-07.audit.79`.

**Frozen source:** `research/sol/target-c-overnight-closure-20261007` at
`8a719ea78d0794124dee73718c70d9abafaa8375`. The explicit-window report first
appeared at `3b595c9f50b4715a4f6ef16d36212c82f8371326` and is unchanged at the
frozen tip. This audit does not include the neighboring effective-wall-chart
report or any later branch additions.

## Exact claims

Let `M>=4`, `A=M-1`, and use the symmetric arithmetic rates

`a_h=A-2h`, for `0<=h<M`,

in the specified six-direction curved wall. For every
`0<theta<=1/(100*M^3)`, with `N=3M^2-3M+1`:

1. The specified punctured-chart construction, with `h=(1,M-2)` omitted and
   wall vertex `v=(1,M-1)` deleted, has a strict `N`-site packet in the wall
   interior. All packet pairs are strictly farther than one, and every packet
   point is strictly farther than one from every retained wall vertex.
2. Every pairwise unit-separated placement of the `6M` wall vertices and its
   `z` additional points in the closed wall satisfies `z<=N`.
3. A contact-minimal, then diameter-pair-minimal triangle-free global
   minimizer containing this actual wall cannot have `z<=N-1` interior source
   points. The exchange retains all exterior points and contact isolates.

The packet-opening amplitude may depend on `M` and `theta`. No uniform
amplitude, no uniform `z=N` classification, no result for general symmetric
profiles, and no extraction of this wall from an arbitrary canonical source
are claimed.

## Uniform chart bounds

Write `u=1`, `v=exp(i*pi/3)`, `w=v-u`, and
`z_h=exp(i*(A-2h)*theta)`. In axial chart coordinates,

`P(a,b)=S_a*u+(S_(a+b)-S_a)*v`, where `S_r=sum_(h<r) z_h`.

Each chart point differs from its flat triangular-lattice location by at most
`(a+b)*A*theta<=M*A*theta<=M^2*theta`. The added root is

`R=V+3*sin(theta)*J(exp(i*(M-2)*theta)*w)`,

where `V=P(1,M-1)`. Since `|w|=1`, its additional displacement is at most
`3*theta`; hence `R` also differs from its flat location by at most
`(M*A+3)*theta<=M^2*theta` for `M>=3`.

Put `delta=M^2*theta<=1/(100*M)`. Every pair whose flat locations are at
least `sqrt(3)` apart therefore remains at distance at least
`sqrt(3)-2*delta>1`: indeed `2*delta<=1/200` for `M>=4`, while
`sqrt(3)>3/2`. This bounds every non-neighbor chart pair and every
non-neighbor root pair at once.

The wall side turns are `2*theta>0`; its six corner turns are
`pi/3-2*A*theta>0`, since `2*A*theta<=1/800<1<pi/3`. Thus the wall is strictly
convex and its perimeter is exactly `6M`. The other flat nearest-neighbor
distances in the chart have the form
`2-2*cos(pi/3+c*theta)`, with `0<c<=2*A` in this arithmetic profile. The
window gives `0<c*theta<pi/3`, so these distances are strictly greater than
one. Consequently the exact moving-involving contact graph is the complete
contact graph used by the canonical sector-peeling proof.

Every flat strict interior lattice site has support margin at least
`sqrt(3)/2` from every side of `H_M`. For such a site and any actual wall
edge, rotation contributes at most `2*M*A*theta`, while moving the site and
edge endpoint contributes at most `2*M^2*theta`. The total is at most
`4*M^2*theta<=1/(25*M)<=1/100<sqrt(3)/2`. Thus all chart sites that start
strictly inside the flat hexagon remain strictly inside the actual wall
throughout the interval. These are the positive support slacks retained by
the finite strict-opening perturbation.

For this graph, Audit.77's no-nonnegative-equilibrium argument applies
throughout the interval: the successive profile gaps are positive, all
angular excesses are below `pi`, and the axis seed used there exists for
`M>=4`. Gordan's alternative supplies a velocity strictly opening every
surviving contact row. At each fixed `(M,theta)`, the remaining finite lower
constraints and wall support inequalities have positive slack, so a
sufficiently small positive finite amplitude opens the packet while
preserving them. The amplitude is not uniform in the parameters.

## Root clearance and wall containment

The deleted vertex is `V`; the absent chart site is `H=(1,M-2)`. The root's
two adjacent retained wall vertices are at squared distance
`1+3*sin(theta)^2` from `R`.

At the flat limit, the only other chart point at unit distance from `V`, aside
from `H` and the two wall neighbors, is `X=(0,M-1)`. Put `B=2*M-3` and
`beta=pi/3+B*theta`. Direct axial-coordinate subtraction and rotation by
`-(M-2)*theta` give

`|R-X|^2 = f(theta)`,

`f(theta)=2+3*sin(theta)^2-2*cos(theta)*cos(beta)`
`                 -4*sin(theta)*sin(beta)`.

Differentiation gives `f(0)=1` and `f'(0)=sqrt(3)*(2*M-5)`. Product-rule
bounds give
`|f''(theta)|<=6+6*(B+1)^2<=24*M^2`. Therefore

`f(theta)-1 >= theta*(sqrt(3)*(2*M-5)-12*M^2*theta)>0`.

For the final sign, use `sqrt(3)>3/2` and
`12*M^2*theta<=3/(25*M)`; the resulting lower bound is already positive at
`M=4` and increases thereafter. This accounts for every limiting unit
neighbor of the root; all its other chart and wall pairs are covered by the
`sqrt(3)-2*delta` estimate.

For an edge on the wall side containing `V`, index its oriented unit edges by
`e_j=exp(i*(2*j-A)*theta)*w`, `j=0,...,M-1`, and let `a_j` be the initial
endpoint. With `k=M-1-j`, summing the `k` edges from `a_j` to `V` gives the
exact inward support expression

`cross(e_j,R-a_j)=sum_(ell=0)^(k-1) sin(2*ell*theta)`
`                 +3*sin(theta)*cos((2*k-1)*theta)`.

For `0<=k<=M-1`, all displayed sine terms are nonnegative and the cosine is
strictly positive: their angle magnitudes are below `2*M*theta<pi/2`. This
proves strict support against every edge on that side, including the edge
through `V`.

For the other five sides, the flat point `V` has support margin at least
`sqrt(3)/2`. Edge rotation changes the signed cross product by at most
`2*M*A*theta<=2*M^2*theta`; moving the point and edge endpoint contributes
at most another `2*M^2*theta`. The total is at most `4*M^2*theta`, so the
report's looser `5*M^2*theta<=1/(20*M)<=1/80` bound preserves all five
positive margins. Thus `R` is strictly inside the actual wall. Together with
the opened chart sites, the packet is strictly interior and clear of every
retained wall vertex.

## Oler cap with the same joint quantifiers

Every actual wall vertex lies within `delta` of its flat counterpart, so
`W_theta=conv(wall)` is contained in the Euclidean `delta`-neighborhood of
the flat radius-`M` hexagon `H_M`. Steiner's parallel-body formula gives

`area(W_theta)<=3*sqrt(3)*M^2/2+6*M*delta+pi*delta^2`.

The excess over the flat area is at most
`3/50+pi/(10000*M^2)<3/50+1/40000<1/10<sqrt(3)/2`, using `pi<4` and
`M>=4`. Oler's finite inequality for the `z+6M` separated points in the
closed wall yields

`z+6M <= (2/sqrt(3))*area(W_theta)+3M+1`
`       < 3*M^2+3*M+2 = N+6M+1`.

The left side is integral, hence `z<=N`. No boundary source label is lost:
the strictly convex wall has exactly `6M` unit edges and `6M` actual wall
vertices; a further pairwise-separated point cannot lie in the relative
interior of a unit wall edge.

## Full-source exclusion

Suppose a canonical source contains the wall and has `z<=N-1` interior
points. Delete those `z` labels and `V`, then insert any `z+1` points from
the strict `N`-site packet. The one-vertex convex-wall shield separates
inserted sites from all retained exterior points, including contact
isolates. All new-involving distances are at least one. They are also
strictly below the old diameter `D`: the inserted points lie in the strict
interior of the wall and thus in the interior of the old full-source hull;
an interior point of a convex set cannot be at its diameter distance from
another point of that set, since it can move slightly farther along the
connecting ray while remaining in the hull. Retained old-old pairs are
unchanged.

The packet creates no unit contact, while deleting `V` removes its two
incident unit wall contacts (and may remove additional old contacts). It
creates no triangle. The exact finite contact-budget endpoint therefore
contradicts contact-minimality if the diameter remains `D`, while a smaller
diameter contradicts global minimality. This is the Audit.77 exchange with
the new explicit interval; it retains the complete source.

## Hostile checks, disposition, and limits

The candidate has no dedicated verifier or saved computational certificate;
none is used as evidence. I independently derived the chart perturbation
bounds, root-neighbor formula and Taylor margin, every wall support margin,
the area bound, and the integer Oler rounding. The opening step is exactly
Audit.77's canonical finite-contact theorem after checking its angle and
axis-seed hypotheses on the whole stated interval. Its prior finite
certificates are not treated as uniform evidence.

**Verdict: PASS — promote**, split into an explicit arithmetic-profile packet
claim, an Oler-cap claim, and a full-source `z<=N-1` exclusion claim. This
sharpens the one-deficit branch for a growing-`M` sequence at
`theta<=1/(100*M^3)`. The `z=N` classification still has only fixed-`M`,
fixed-profile onset; the route still lacks extraction of this wall from an
arbitrary canonical source. Target C-II and Level I remain open.

## Audit.242 clarification — interior isolate accounting

The full-source exchange deletes all `z` strict-interior labels, including any
interior contact isolates, together with one wall vertex, then inserts `z+1`
packet points. Interior isolates are counted in `z` and the total source
cardinality is preserved, but their label identities are not retained. All
source points outside the wall, including exterior contact isolates, are
retained. Earlier wording that said “retaining all exterior points and
contact isolates” must be read with this scope. The arithmetic-window
population and source-exclusion conclusions remain unchanged.
