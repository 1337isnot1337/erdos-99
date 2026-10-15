<!-- theorem-state: {"artifact_id":"ART-45E96F746D74","canonical":false,"claim_ids":["C-THREE-DIRECTION-SMOOTH-AFFINE-CORNER-REGRESSION"],"claim_statuses":{"C-THREE-DIRECTION-SMOOTH-AFFINE-CORNER-REGRESSION":"regression"},"index":"docs/state/artifact-index.jsonl","status":"regression","target":"target-c"} -->
# Independent audit — three-direction affine packet corner barrier

**Date:** 2026-10-06
**Audit base:** `147158251175c6bcb76690a3cb7a7f3d9091050e` (`2026-10-06.audit.69`)
**Audited source snapshot:** `research/sol/target-c-owner-order-closure-20261006` at
`2e489dc3dabfa015cf58a0fd0c48f2b404bd07e5`
**Candidate:** `docs/reports/target_c_three_direction_wall_packet_corner_barrier_2026-10-06.md`
**Verdict:** REGRESSION VALID for the near-identity homothety/rotation packet and for every C2 affine packet family in the stated scope.
**Frontier effect:** blocks one tempting full-grid packet route; it does not show that other packets or canonical sources fail.

## Exact regression statement

Let `M>=3`. Start from the regular triangular-lattice hexagon of side `M`
with all `3M^2-3M+1` strictly interior lattice sites. Bend each of the six
wall sides by the same rate sequence `(2j-M+1)theta`, `j=0,...,M-1`, while
keeping every wall edge at unit length. For small positive `theta` the
resulting wall is strictly convex. Its side chord is

`L(theta)=sum_j cos((2j-M+1)theta)=M-C theta^2+O(theta^4)`,
`C=M(M^2-1)/6`.

At a corner with unit radial vector `r`, the old wall corner is `q=Lr` and
the first radial interior lattice site is `p=(M-1)r`. The three retained
unit guards are the corner and its two adjacent wall vertices. The precise
geometry is given in the candidate report.

For a near-identity homothety/rotation
`p_new=(1+epsilon)Rot(phi)(M-1)r`, with `epsilon>=0` and
`theta,phi,epsilon ->0`, expansion of its squared distances to the two
adjacent wall vertices gives, with `m=M-1` and `a*=sqrt(3)/2`,

`Delta_± = 2a*m*(theta ∓ phi)-m*epsilon + O(theta^2+phi^2+epsilon^2)`.

If both lower guards survive, the nonpositive linear epsilon term absorbs
its own quadratic remainder; the two inequalities imply
`|phi|<=theta+O(theta^2)`. The corner guard has

`Delta_0 = M(M-1)phi^2 - 2C theta^2 - 2(M-1)epsilon`
`         + O(theta^4+phi^4+epsilon^2+epsilon*theta^2+epsilon*phi^2)`.

Since `epsilon->0`, its remainder terms proportional to epsilon are
absorbed into the negative linear term. The corner inequality then forces
`epsilon=O(theta^2)`. Substituting the adjacent-guard rotation bound gives

`Delta_0 <= [-M(M-1)(M-2)/3 + o(1)] theta^2 < 0`.

Thus no sufficiently small positive curvature admits this complete-grid
homothety/rotation packet while the three corner guards remain. The same
argument applies at each of the six corners, and integer multiples of
`pi/3` merely permute the lattice directions. The argument is for each
fixed `M`; its remainder constants may depend on `M`.

## Independently reconstructed smooth affine obstruction

The stronger candidate claim also survives. Suppose a C2 family
`p -> T(theta)p+t(theta)` starts with `T(0)=I`, `t(0)=0`, maps the entire
interior lattice, and leaves all six corner guards in place.

Write `S1=Sym T'(0)`. Unit lattice pairs occur in all three unoriented
triangular directions `r_i`, so first-order lower feasibility gives
`r_i^T S1 r_i>=0`. For each of the six radial corners, its unit guard has
first derivative of opposite sign, giving
`(M-1) r^T S1 r + r dot t'(0)<=0`. Summing all six corners cancels the
translation and uses `sum_{six} rr^T=3I`; the pair inequalities force
`tr(S1)=0` and all three quadratic values to vanish. Three directions
determine a symmetric 2-by-2 form, so `S1=0`. Opposite corners then force
`t'(0)=0`. Hence `T'(0)=kappa J`.

The two adjacent wall guards require `|kappa|<=1`. Write

`T(theta)=I+kappa*theta*J+theta^2 B+o(theta^2)`,
`t(theta)=theta^2 w+o(theta^2)`,
`S2=Sym(B)+(kappa^2/2)I`.

The three interior unit-pair directions give `tr(S2)>=0`. For each corner,
expanding its radial guard to second order and summing over all six corners
cancels `w` and gives coefficient

`6*kappa^2*M(M-1) - 6(M-1)tr(S2) - 12C`
`<= -2M(M-1)(M-2) < 0`.

This contradicts the six required lower guards. It excludes any C2 affine
family through the identity, including first-order translation and shear
attempts. It does not exclude a remote finite affine packet, a nonaffine
packet, or deletion/payment of one or more corner guards.

## Certificate and hostile scope checks

The exact verifier
`research/verify_target_c_three_direction_corner_barrier_2026_10_06.py`
was inspected and rerun at the recorded source commit. In `Q(sqrt(3))` it
checks four feasible curved walls (`M=3,4,6,8`), 2,187 wall pairs, strict
convexity, 492 rational homothety proposals against the three local guards,
the `(3/2)I` direction tensor, the rank-three quadratic evaluation matrix,
and both negative coefficients for every integer `M=3,...,100`. These are
finite checks. The universal local homothety and C2 affine conclusions come
from the Taylor arguments above, not sample coverage.

The result is a strategy regression only. It provides no arbitrary-packet
capacity upper bound, no source-realized canonical configuration, no global
optimality claim, and no C-II or Level I implication. Nonaffine interior
rearrangements and exchanges that pay for the corner guards remain outside
its scope.
