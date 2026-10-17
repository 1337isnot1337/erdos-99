> Generated reading edition · [exact source](../../../docs/reports/target_c_sorted_rate_packet_classification_2026-10-06.md) · source SHA-256 `964e7d9dacd942e8dd5114217f271e79454a9222069fb8e125e882f281271fe4`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-240D361F8E97","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C: sorted-rate packets and the highest curved-wall population

Date: 2026-10-06. Authority: `d65fec2adf136af5337ed177b37d83ac64869640`,
state `2026-10-06.audit.70`. Classification: **proved candidate awaiting
independent audit** for the statements below. The finite sorting packets
are also **regressions** against a strict nested-energy-gap argument.
No theorem-state promotion or exhaustive C-II closure is claimed.

The implication is

`specified 6M-edge wall + highest interior population -> equality-limit
chart -> radial rate permutation -> finite local classification ->
actual unit triangle`.

Combined with the preceding vacancy exchange, this leaves the single
population `z=N-1`, where `N=3M^2-3M+1`. Arbitrary clouds at that count
are still open. The full-core and arbitrary-container branches remain open.

## 1. Wall, charts and exact statements

Fix `M>=3`, `R=M-1`, and the six-direction wall from the preceding
corner-barrier and vacancy reports. Each side consists of the ascending
angular rates `-(M-1),-(M-3),...,M-1`, multiplied by `theta`. Its corner
radius is

`L(theta)=sum_j cos((2j-M+1)theta)=M-C theta^2+O(theta^4)`,
`C=M(M^2-1)/6`.

Use triangular coordinates `p=iu+jv`, `u=(1,0)`,
`v=(1/2,sqrt(3)/2)`, and write `P_R` for the complete interior grid.
The following are fixed-M statements; no threshold uniform in M is claimed.

**Complete-chart classification.** For sufficiently small positive theta,
every unit-separated placement of `N` points inside this actual wall is
one of the sorting packets defined in Section 4, after relabeling. Every
such packet contains exact unit triangles. Consequently no triangle-free
source contains this wall with `z=N` interior points.

**Central-vacancy chart classification.** If a sequence of placements of
`N-1` points converges, after relabeling, to `P_R` with its central site
omitted, then sufficiently small members are sorting packets with that
central site omitted. These still contain exact unit triangles for M>=3.
This statement does not classify arbitrary `N-1`-point limiting placements.

The first claim uses the checked equality statement described in Section 7.
The second assumes its limiting chart explicitly. Neither drops any actual
source point or extends the canonical core rigidity theorem to isolates.

## 2. First-order geometry is a radial permutahedron

The nested positive stresses from the preceding stress report force every
ring-edge and radial-chain first variation to vanish. The full chart also
forces the central velocity to zero. In the central-vacancy chart the
radius-one ring takes the place of the central spoke stress.

On radius r, radial constraints make every corner velocity tangential.
Ring-edge constraints make the tangential corner coefficients equal, so

`d_(r e_k)=alpha_r J e_k`, `alpha_0=alpha_M=0`.

Put `t_r=alpha_(r+1)-alpha_r`, for `0<=r<M`. In one sector, at
`p=(r-j)u+jv`, ring constraints give

`d dot u = a_* s_(r,j)`,
`d dot v = a_* (s_(r,j)+alpha_r)`, `a_*=sqrt(3)/2`.

The two remaining unit-direction lower constraints are exactly

`s_(r,j)>=s_(r-1,j)`,
`s_(r,j)>=s_(r-1,j-1)-t_(r-1)`.

Axis values are `s_(r,0)=0`, `s_(r,r)=-alpha_r`. The prescribed outer
wall velocity `-j(M-j)J(v-u)` gives

`s_(M,j)=j(M-j)`.

Iterating the two inequalities along a path from the center to `(M,j)`
gives, for EVERY j-element subset I of `{0,...,M-1}`,

`-sum_(r in I) t_r <= j(M-j)`.                         (1)

Together with `sum t_r=0`, these are the subset-sum inequalities for the
convex hull of the permutations of

`lambda=(M-1,M-3,...,-M+1)`.                         (2)

For completeness: sort any linear functional's coefficients. Abel
summation expresses its value using the sums over the successive largest
coefficient subsets. Inequality (1), and its complementary-subset version,
bound every such sum by the corresponding sum of the sorted entries of
(2). Thus every linear functional is bounded by its rearrangement maximum
on permutations of (2); separation gives the asserted convex-hull inclusion.

In particular

`sum t_r^2 <= sum lambda_r^2 = M(M^2-1)/3`.           (3)

Equality in (3) requires t to be a permutation of (2): the squared norm is
strictly convex, and all the permutation vertices have the same norm.
This is an energy bound derived from every physical directional row,
not from generic PSD, planarity or a source-level owner contraction.

Conversely every t in this convex hull admits the first-order field

`s_(r,j)=max_{I subset {0,...,r-1}, |I|=j} -sum_(h in I)t_h`

at interior layers. The two recurrences hold, the axes are correct, and
(1) verifies all edges into the prescribed outer wall. Apply the same
formula in each rotated sector. All sector-axis values agree. Thus the
projected first-order polytope is exactly this permutahedron.

## 3. Energy forces a permutation and its entire velocity field

For the full chart the central radial stress has energy

`E_0(d)=6 sum t_r^2`.

For the central-vacancy chart the radius-one stress has the SAME energy:
its six inner-ring edges contribute `6 alpha_1^2`, and the outer chains
contribute `6 sum_(r>=1)t_r^2`.

The exact stress sum applies without a C2 assumption. For displacements
`delta=theta d+o(theta)`, the moving linear terms cancel. The six actual
corner shifts give `12(L-M)=-12C theta^2+O(theta^4)`. Summing the unit
lower constraints and dividing by theta squared therefore gives

`6 sum t_r^2 >= 12C = 2M(M^2-1)`.

Combine with (3). Every limiting first velocity has t a permutation of
(2). For such a permutation, all the interior sector values are forced.
The forward recurrence gives the prefix-subset maximum as a lower bound.
For the upper bound, extend a path to the prescribed outer wall using
those remaining rates above the threshold between the chosen prefix's
j-th and (j+1)-th entries. The selected prefix and suffix are then exactly
a largest subset of the full rate set, so the outer subset inequality is
an equality and supplies the matching upper bound. Hence

`s_(r,j)=-sum of the j smallest entries of (t_0,...,t_(r-1))`.  (4)

There are at most M! possible first velocities. No unclassified continuous
first-order family survives this step. The argument alone is not yet a
finite triangle theorem; Section 5 supplies that step.

## 4. Finite sorting packets realize every energy equality

Identify the plane with the complex numbers. Fix any permutation t of
(2), set `z_h=exp(i t_h theta)` and `S_r=sum_(h<r)z_h`. Let `U_(r,j)`
be the sum of the j elements of this prefix having the smallest rates.
Define, in one sector,

`p_(r,j)(theta)=S_r u+U_(r,j)(v-u)`, `0<=j<=r<=M`,

and rotate by multiples of pi/3 to obtain the other sectors. Set the
center to zero. At r=M, `S_M=L` and the sorted side edges are exactly
the original wall. Each inner site lies strictly inside that wall for
sufficiently small theta, by its strict limiting containment.

Ring edges are `z_h(v-u)` and have unit length. Between successive layers,
one of the two other triangular neighbor differences is `z_new u` or
`z_new v`, also unit. The other, when present, has squared length

`2-2 cos(pi/3+|t_new-t_old| theta)>1`.

All remaining pairs have strict limiting distances above one. Thus these
are actual finite unit-separated packets, not just first-order assignments.
Each new layer inserts one unit triangle in each sector, with all three
edges using the same z_new. There are six such triangles per layer.
The complete interior chart has six triangles at the center and more in
subsequent layers. Removing the center leaves the triangles from layer
two onward; M>=3 suffices.

Their first velocities are (4). Every ring stress has

`E_r=6 sum_(h<r)t_h^2+6 sum_(h>=r)t_h^2=12C`.

Therefore the proposed strict-gap statement `some E_r<12C` fails for
EVERY M, even with every physical first-order guard inequality. These
finite packets contain unit triangles and are not triangle-free competitors,
canonical sources or global minimizers. The regression identifies the
necessary next premise: equality must force an actual finite triangle.

## 5. Equality gives a finite local classification

Let P be the bounded first-order lower-feasibility polytope in moving-site
coordinates, using only rows incident to at least one moving site. Its affine hull is the zero space of the strong ring/ray
rows. Every other unit row has positive slack in some sorting velocity
(choose the inserted rate on the appropriate side of its predecessor),
so averaging those velocities proves there are no additional universally
zero rows.

Fix a permutation velocity d*. The gradient of `E_0` restricted to this
affine hull uniquely maximizes its linear functional at d*: on projected
t-coordinates this follows from `t* dot t <= |t*|^2`, with equality only
at t=t*, and (4) then fixes all moving coordinates. For the center-vacancy
chart use the radius-one energy instead. Thus this gradient is in the
relative interior of P's normal cone at d*.

The active rows J at d* are precisely the unit contacts of its finite
sorting packet. Their limiting moving-coordinate matrix R_0 has full
column rank: a vector in its kernel would permit both small signs of a
line through d* in P, contradicting the unique maximizer and (4).
This rank is a theorem about this auxiliary pinned packet only.

Take the principal central/radius-one positive stress lambda_0 and add
small positive multiples of all other nested stresses. Its coefficients
are positive on every strong row, zero on the weak rows. Its energy
gradient remains inside the same normal cone. The normal-cone identity
then provides a signed first correction lambda_1, strictly positive on
EVERY active weak row, satisfying

`R_0^T lambda_1 = -R_1^T lambda_0`.

Here `R_theta=R_0+theta R_1+O(theta^2)` is the actual sorting-packet
contact matrix. Indeed `R_1^T lambda_0` is one half of the chosen energy
gradient. Strong-row coefficients in lambda_1 may have either sign,
since their positive zeroth-order coefficients persist. Interior
normal-cone membership permits positive coefficients on all active weak
rows: subtract a sufficiently small sum of their outward normals before
representing the remaining cone vector.

Full column rank gives a bounded analytic right inverse of R_theta^T.
Correct the residual of `lambda_0+theta lambda_1`, which is O(theta^2),
using this inverse. The resulting exact pinned equilibrium lambda_theta
is positive on every contact, uniformly bounded above, and has minimum
coefficient at least `c theta`, for some c>0 depending on M and the
permutation. This is a constructive existence argument for the auxiliary
stress; no canonical selected-stress extension is assumed.

For any other feasible placement at displacement delta from this packet,
its old unit rows obey

`R_theta delta >= -C_1 |delta|^2` coordinatewise.

The positive equilibrium makes the weighted sum of these linear rows zero.
Hence each positive row is at most `C_2 |delta|^2/theta`. Uniform full
rank implies

`|delta| <= C_3 |delta|^2/theta`.

Thus the sorting packet is the only feasible placement within distance
`c_1 theta` of itself. Constants are local to this finite chart and are
not asserted uniform in M.

Any sequence of feasible placements converging to the limiting chart has
displacement O(theta). Otherwise normalize by a displacement much larger
than theta: the limit would be a nonzero feasible first direction for the
static wall. That cone is zero. For the full chart, uniform weights on
all six-neighbor rows, plus pinned triangular-grid rigidity, prove this.
For the central vacancy, the ring/ray stresses and the sector subset
bounds with static boundary value zero give t=0 and then s=0 directly.

Taking a subsequence of the bounded displacement/theta, Sections 2--3
force one of the finitely many d*. The placement differs from its exact
sorting packet by o(theta), so the preceding local isolation forces exact
equality. A compactness contradiction gives the classification for all
sufficiently small theta, not just a selected sequence. Every resulting
placement contains an exact unit triangle.

## 6. Spending the highest population and the remaining case

A full N-point interior cloud for theta tending to zero has a convergent
subsequence. Add the 6M retained unit wall vertices. At zero the total
`3M^2+3M+1` equals Oler's bound for the regular hexagon of side M.
The checked equality statement requires an equilateral unit triangulation.
The fixed wall determines its triangular lattice, and all lattice sites
are occupied; the interior cloud is exactly P_R after relabeling.
Extra limit points cannot lie on a wall edge, since two consecutive wall
vertices are one apart and already forbid that edge to another source point.
Section 5 now forces the finite sorting packet and a unit triangle.

Therefore z=N is excluded for arbitrary old interior positions. The
previous exact vacancy packet excludes z<=N-2. With its strict-area Oler
bound z<=N, only z=N-1 remains in this specified six-direction wall family.
A cloud at that count with the central-vacancy limiting chart is excluded
as well. General one-deficit clouds have not been classified: Oler deficit
one is not equality and does not imply a missing lattice site. Do not
silently apply the equality theorem to them.

Next obligations: classify or exchange those general one-deficit clouds;
extract an applicable chamber from the actual source; and close the
independent full-core face-coupled endpoint. No exhaustive branch is closed.

## 7. Literature check and certificate scope

The equality statement is checked in the reliable transcription by
K. J. Boroczky and I. Z. Ruzsa, *Note on an inequality of Wegner*, dated
January 2, 2007, printed page 2, inequality (2) and the paragraph immediately
following it: equality is a segment or an equilateral triangulation of the
center hull. Their disks have radius one and center separation two; scaling
all coordinates by one half gives the unit-separated normalization used here.
This is finite Oler/Groemer equality, not Rogalski--Saint Raymond disk equality.

Source: https://users.renyi.hu/~carlos/wegner.pdf . The rendered page was
visually inspected. Local copy:
`papers/related/boroczky-ruzsa-2007-note-on-wegner.pdf`, SHA256
`95db9d8f80f91b4f34ee25e61866b57b6e1676f6326af6b01de88ca29d9d9467`.
The original Groemer 1960 entry was found at EUDML, but its access returned
HTTP 403 and its full text was not inspected. The proof above uses the
explicit reliable transcription, not an inferred original statement.

The companion exact verifier checks finite sorting packets, first rows,
subset inequalities, all ring energies, actual unit triangles and limiting
pinned contact rank. It does not numerically certify arbitrary-cloud
compactness, the normal-cone argument, onset constants or global optimality.
Those are the analytic claims stated above and await independent audit.
