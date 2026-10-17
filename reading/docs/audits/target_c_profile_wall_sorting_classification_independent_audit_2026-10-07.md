> Generated reading edition · [exact source](../../../docs/audits/target_c_profile_wall_sorting_classification_independent_audit_2026-10-07.md) · source SHA-256 `9d67a3abf8aa088ca5334df868822433fe85b0c4581f20b5cf318dac75a03221`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-5A4F1C453D9C","canonical":true,"claim_ids":["C-SIX-SIDED-WALL-FIXED-CLASS-EXCLUSION","C-SIX-SIDED-WALL-PROFILE-SORTING-CLASSIFICATION"],"claim_statuses":{"C-SIX-SIDED-WALL-FIXED-CLASS-EXCLUSION":"canonical","C-SIX-SIDED-WALL-PROFILE-SORTING-CLASSIFICATION":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit — finite classification of the highest wall population

**Audit base:** `main` at `d71085cd0130941642796d8717d7e9fb2949b718`,
state `2026-10-07.audit.77`.

**Frozen source:** `research/sol/target-c-overnight-closure-20261007` at
`3b595c9f50b4715a4f6ef16d36212c82f8371326`.

At the later source tip `5a4b063711ff055d0fcc387312bda40e2e355ccc`, the
maximum-population report, its verifier, and its saved certificate are
unchanged. That tip adds an unrelated effective-wall-chart report. The frozen
maximum-population verifier was rerun and its output matched the saved JSON
byte-for-byte.

The frozen report contains a later-added Section 8 with an explicit
first-stress correction and a separate finite certificate. This audit does
not rely on or promote that appendix. The classification below follows from
the independent reconstruction of Sections 1--7.

## Exact claims audited

Fix `M>=3` and a strictly decreasing symmetric real profile
`a_0>...>a_(M-1)`, with `a_(M-1-h)=-a_h`. Let `W_(M,theta)` be the specified
six-sided curved unit wall formed by sorting those rates along each side, and
let `N=3M^2-3M+1`.

1. **Finite maximum-population classification.** For every sufficiently small
   positive `theta` (depending on `M` and the profile), every pairwise
   unit-separated placement consisting of all `6M` wall vertices and exactly
   `N` additional points in the closed wall is, after relabeling, one of the
   sorting packets associated with a permutation of the rates. Each packet
   contains an actual unit equilateral triangle.
2. **Complete fixed-wall source exclusion.** For every fixed `M>=4` and fixed
   profile at sufficiently small positive `theta`, no contact-minimal then
   diameter-pair-minimal triangle-free global minimizer contains the full
   specified wall.

The second claim combines the first with canonical Audit.77: finite Oler gives
`z<=N`; Audit.77 excludes `z<=N-1` while retaining all exterior points and
contact isolates; the classification supplies a triangle when `z=N`. The
source-exclusion claim is not asserted for `M=3`, because the all-M one-deficit
packet proof requires `M>=4`.

## Independent proof reconstruction

### Localization to the flat chart and the `O(theta)` rate

As `theta` tends to zero, the wall converges to the regular hexagon `H_M`.
With `N` interior points and all `6M` wall vertices, the total count is

`N+6M=3M^2+3M+1=(2/sqrt(3))*area(H_M)+(1/2)*perimeter(H_M)+1`.

The promoted Audit.74 Oler-equality limit therefore puts every convergent
subsequence, after relabeling, at the complete lattice `P_M`; the additional
points limit to `P_(M-1)`. This statement alone supplies no rate. To get the
rate, suppose along a feasible sequence the largest interior displacement
from `P_(M-1)` divided by `theta` is unbounded. Normalize those displacements
by their largest norm and pass to a subsequence. Wall displacements are
`O(theta)`, so they vanish in this normalization. The first-order lower
constraints give a nonzero feasible infinitesimal motion of the full flat
triangular chart with its boundary fixed.

Put weight one on every flat unit edge incident to a moving point. The six
unit directions at each moving lattice point sum to zero. Consequently the
sum of the nonnegative first rows is zero, so every row vanishes. A fixed
boundary edge and its adjacent triangle then pin the third vertex; propagation
through the connected triangular tiling pins every vertex. The normalized
motion must be zero, a contradiction. Thus every feasible sequence has
interior displacement `O(theta)`.

This uses rigidity of the complete auxiliary chart only. It does not invoke
full-source ZR/ZF or delete contact-isolated source points.

### First-order polytope and permutahedron

Write `u=(1,0)`, `v=(1/2,sqrt(3)/2)`, and `c=sqrt(3)/2`. Nested flat ring
stresses, with their six corner chains continued to pinned wall corners,
force all ring rows and corner-chain rows to vanish. The corner wall shifts
have zero first derivative because the profile is symmetric. The center
velocity is zero; on ring `r`, the six corner velocities are
`alpha_r*J(e_k)`, with `alpha_0=alpha_M=0`. Define
`t_h=alpha_(h+1)-alpha_h`; then `sum_h t_h=0`.

For a sector point `(r-j)u+jv`, ring equalities express its velocity through
one scalar `s_(r,j)`. The other two nearest-neighbor constraints give

`s_(r,j)>=s_(r-1,j)`,
`s_(r,j)>=s_(r-1,j-1)-t_(r-1)`.

The sorted outer wall has `s_(M,j)=-B_j`, where `B_j` is the sum of the `j`
smallest profile rates. Following either recurrence from the center to the
outer side, for every `j`-element subset `I` of the increments, gives

`sum_(h in I) t_h >= B_j`.

Together with `sum_h t_h=0`, these are exactly the majorization inequalities
for `t` to lie in the convex hull of the permutations of `a`. The converse
prefix construction `s_(r,j)=-sum of the j smallest entries of
{t_0,...,t_(r-1)}` satisfies the recurrences and the outer inequalities.
Thus the projected first-order feasible set is the profile permutahedron.

For a fixed permutation of `a`, the full velocity field is unique. The
recurrences give the prefix-smallest formula as a lower bound at every
intermediate ring. For the reverse inequality, choose a threshold between the
`j`th and `(j+1)`th entries in that prefix; extend to the outer ring by taking
the suffix rates below that threshold. The outer subset inequality at the
permutation vertex is equality and supplies the matching upper bound. The
axis values are already pinned. Hence there are no extra first-order degrees
of freedom over a permutation vertex.

### Central energy forces a permutation vertex

Use the positive stress on the six center-to-corner chains. Summing the exact
unit lower inequalities cancels every moving linear term. The six outer
corners have radius

`L(theta)=sum_h cos(a_h*theta)=M-(theta^2/2)*sum_h a_h^2+O(theta^4)`.

It follows that the sum of squared chain displacements is at least
`12*(M-L(theta))`. Along a subsequence with first velocity `d`, the chain
energy is `6*sum_h t_h^2`, so

`sum_h t_h^2 >= sum_h a_h^2`.

On the permutahedron, convexity of squared norm gives the reverse inequality.
Since the rates are distinct, strict convexity makes equality possible only
at a permutation vertex. The preceding recurrence argument then fixes the
entire first velocity field.

### Exact packet and full active rows

For a permutation `t*`, set `z_h=exp(i*t*_h*theta)`,
`S_r=sum_(h<r) z_h`, and let `U_(r,j)` be the sum of the `j` factors of
smallest rate in the first `r` entries. The packet coordinates are

`Q_(r,j)=S_r*u+U_(r,j)*(v-u)`,

rotated through the six sectors, together with the center. At the outer ring
these are exactly the prescribed wall points. Ring edges are unit; across
each pair of successive layers one of the two other neighbor families is a
unit factor times `u` or `v`. The remaining one has squared length
`2-2*cos(pi/3+|t_new-t_old|*theta)>1`. Every non-neighbor pair has a strict
flat gap. This proves exact feasibility and identifies the entire active
contact set `J` for each fixed packet and sufficiently small `theta`.

The limiting active-row matrix `R_0` on `J` has full moving-column rank.
Otherwise a nonzero `x` in its kernel would make both `d*+epsilon*x` and
`d*-epsilon*x` feasible in the first-order polytope for small `epsilon`:
active rows stay equalities and all other weak rows have strict slack.
But the central energy gradient has `d*` as its unique maximizer over that
polytope. In rate coordinates its value is proportional to
`sum_h t*_h*t_h`, whose maximum over the permutahedron is uniquely attained
at `t*`; the fiber there is the unique field just proved. This contradiction
establishes full rank. Averaging the permutation fields gives strict slack in
every weak row, so the affine hull contains no omitted universal equality.

### Positive stress continuation gives the required isolation scale

The central energy gradient is in the relative interior of the normal cone
at `d*`, because it exposes that vertex uniquely. Add sufficiently small
positive multiples of the other nested stresses: the resulting limiting
stress `lambda_0` is positive on every strong row and zero on weak rows, while
its associated gradient remains in the same relative interior. For lower
inequalities `R_0 d>=b`, a relative-interior normal has a representation by
the active weak-row normals with strictly positive coefficients, modulo the
strong-row affine normals. Therefore one can choose `lambda_1`, positive on
every active weak row, so that

`R_0^T lambda_1 = -R_1^T lambda_0`.

Here `R_theta=R_0+theta*R_1+O(theta^2)`. The identity between the central
energy gradient and `2*R_1^T lambda_0` follows by differentiating the
stress-work identity; on the stress support the first contact rows are zero,
so the relative velocities are tangent to the unit rows. Since `R_0` has
full column rank, `R_theta^T` has a bounded analytic right inverse near zero.
Use it to correct the `O(theta^2)` residual of
`lambda_0+theta*lambda_1`. The exact stress `lambda_theta` is positive on all
packet contacts: strong-row coefficients have positive order-one margins and
weak-row coefficients have positive order-theta margins.

For any competing feasible placement at displacement `x` from this packet,
an active unit row obeys

`R_theta x >= -|x_p-x_q|^2/2 >= -C*|x|^2`.

Stress equilibrium makes the weighted sum of its linear rows zero. Since each
weak coefficient is at least `c_1*theta`, this bounds every active row above
by `C'*|x|^2/theta`. Full rank of `R_theta` then gives

`|x| <= C''*|x|^2/theta`.

Thus a distinct feasible placement must be at least `c_2*theta` from the
packet. This scale is essential: qualitative local rigidity alone would not
contradict a competing cloud whose displacement from the packet is `o(theta)`.

If classification failed for arbitrarily small `theta`, the `O(theta)` rate,
the first-order polytope, and the central energy argument would give a
subsequence converging after rescaling to one permutation field. The matching
exact packet has the same first field, so the difference is `o(theta)`, in
conflict with the local isolation radius. Therefore every sufficiently small
positive-curvature placement is exactly a sorting packet. The center and two
adjacent first-ring points form an exact unit equilateral triangle.

### Full fixed-wall source exclusion for `M>=4`

The canonical Audit.77 population cap gives `z<=N` for the fixed wall. If
`z=N`, the finite classification yields a unit triangle. If `z<=N-1`, the
Audit.77 strict one-deficit packet replaces the full old interior population
and one deleted wall vertex, retaining all exterior points and contact
isolates while losing wall contacts and adding none. Hence no
contact-minimal triangle-free global minimizer can contain this wall for the
stated `M>=4` and fixed profile. No claim follows for arbitrary wall
extraction, for growing `M` with a common onset, or for Level I.

## Certificate scope

The frozen exact verifier was inspected and rerun. It checks four arithmetic
profiles of lengths `3,4,5,6`, all 870 rate permutations in the combinatorial
prefix/extension identities, and 11 exact packet instances in
`Q(sqrt(3))` at half-angle tangent `1/100000`. It checks 43,110 pair
distances, 1,800 unit contacts, strict containment, an actual triangle, and
full limiting rank using nonzero modular minors. Output matches the saved
certificate byte-for-byte.

The finite code does not verify the normal-cone continuation, arbitrary-cloud
classification, arbitrary real profiles, or global optimality. The universal
profile theorem follows from the analytic argument above; the finite checks
are regressions and formula checks only. The separate Section 8 stress
correction appendix is not required for this proof and is not promoted.

## Verdict and frontier effect

**PASS — promote at the stated scopes.** The finite highest-population cloud
is exactly a sorting packet and necessarily has a unit triangle. Combining
with Audit.77 excludes the complete specified fixed-wall source class for
every fixed `M>=4` and fixed symmetric strictly decreasing profile at
sufficiently small positive curvature. `M=3` has the top-population
classification only; its `z<=N-1` source population is not covered by this
all-M one-deficit theorem.

The fixed wall family is exhausted for `M>=4`. The live C-II obligation is
arbitrary-source extraction or a source-realized replacement; no such wall
is inferred from a macroscopic chamber. C-II and Level I remain open.
