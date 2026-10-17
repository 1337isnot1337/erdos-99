> Generated reading edition · [exact source](../../../docs/reports/target_c_paired_cap_spoke_global_comparison_2026-10-06.md) · source SHA-256 `1895d27ac006139bb164d48151ca2069cf2a6dd2464e2270f865e400782a9b8c`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-244EEBA98887","canonical":false,"claim_ids":["C-PAIRED-CAP-SPOKE-NONGLOBAL-REGRESSION"],"claim_statuses":{"C-PAIRED-CAP-SPOKE-NONGLOBAL-REGRESSION":"regression"},"index":"docs/state/artifact-index.jsonl","status":"regression","target":"target-c"} -->
# Target C: a saturated paired-cap source loses to an exact same-cardinality packing

**Date:** 2026-10-06. **Authority:** main `583203ac`, audit.62.
**Worker:** 2, exterior caps. **Classification:** exact feasible-source
regression and proved restricted comparison; independently audited as
`C-PAIRED-CAP-SPOKE-NONGLOBAL-REGRESSION` in Audit.94.
**C-II / Level I:** open. The family below is explicitly nonglobal and
does not satisfy canonical ZR/ZF or the linear loaded-diameter population.

The implication proved is

```text
actual loaded spoke frame + paired quadratic near-capacity isolate caps
  + explicit lattice vacancies created by the frame
  -> enough sites in a smaller disk for the entire original cardinality
  -> diameter <= D-1/2.
```

This is an exterior counterpart of the nonglobal internal-shell regression.
It keeps positive KKT equilibrium, actual loaded chord endpoints, all source
isolates, exact antipodal caps, boundary-order Oler slack, and deep cap
coverage. It illustrates a global replacement of the old diameter core,
not a cap insertion with that core fixed. It does not establish the
vacancy inequality for a canonical source.

## 1. Exact family

Let M>=20 be an integer. Work in the unit triangular lattice

```math
\Lambda=\{i e_1+j e_2:i,j\in\mathbb Z\},\quad
e_1=(1,0),\quad e_2=(1/2,\sqrt3/2).
```

Let v_0,...,v_5 be its six cyclic unit vectors. Put

```math
T_M=\{k v_j:1\le k\le M,\ 0\le j<6\},\qquad
s=1+\frac1{100M^2},\qquad R_0=M-\frac14.
```

Define the lattice guards and the available cloud indices by

```math
G_M=\{\ell\in\Lambda:\operatorname{dist}(\ell,T_M)\le1\},
\quad L_M=\Lambda\cap\overline B(0,R_0),
\quad I_M=L_M\setminus G_M.
```

The full source is

```math
A_M=T_M\cup s I_M.                             \tag{1}
```

These are rational/algebraic coordinates: the only radical is sqrt(3),
and i^2+ij+j^2 is the squared norm in lattice coordinates. The guard
test uses only differences of lattice indices.

### Unit separation and the exact contact/diameter graphs

The only unit contacts in T_M are the six edges of the central hexagon
and the six radial chains. Thus T_M has 6M vertices, 6M contacts, no
triangle, and is connected. For adjacent ray directions the squared
distance between k v_j and l v_{j+1} is k^2+l^2-kl; it equals one
only for k=l=1. Along one ray it equals one only at consecutive integers;
the other ray pairs create no additional contacts.

Distinct cloud points have distance >=s>1. Every ell in I_M has distance
at least sqrt(3) from every old core point, because the first positive
lattice norm after one is three. Its scaling displacement has size

```math
|s\ell-\ell|\le\frac{R_0}{100M^2}<\frac1{100M},
```

so all cloud-core distances exceed one. Every cloud point is therefore
an actual contact isolate in the *full* source.

Cloud points have radius s R_0<M. All points have radius at most M,
and only the six loaded labels M v_j have radius M. The actual diameter
is D=2M, and its pairs are exactly the three opposite pairs
M v_j,-M v_j. In particular all exterior cloud points have strict upper
slack. The actual loaded hull is the regular hexagon

```math
F_M=\operatorname{conv}\{M v_j:0\le j<6\}.       \tag{2}
```

### Positive equilibrium on every actual core contact and diameter

Give every contact weight alpha=2M/3 and each of the three diameters
weight beta=1/3. The diameter weights sum to one. At an intermediate
radial vertex its two chain contact forces cancel. At a central hexagon
vertex its two hexagon contacts sum to alpha v_j, which cancels the
outward radial-chain contact. At an outer loaded vertex the sole contact
reaction is alpha v_j and the diameter reaction is beta (2M v_j), equal.
Thus the full vertex KKT equations hold, with every contact and diameter
coefficient positive, and zero rows at every retained isolate. The virial
identity is 6M alpha=4M^2=D^2.

No external pins or fake diameter labels are used. Positive equilibrium
does not imply mixed rigidity, the affine-kernel property, or global
optimality; those distinctions matter in Section 5.

## 2. Actual antipodal macroscopic caps and their filling

Put K_M=conv(A_M). Both (1) and (2) are centrally symmetric. The six
actual loaded sides give six Section-77 exterior caps C_j, paired exactly
by C_{j+3}=-C_j. Their assigned external isolate populations are exactly
equal in each opposite pair, rather than merely equal to leading order.

Here is an elementary uniform support estimate:

```math
B(0,M-4)\subseteq K_M\subseteq B(0,M)\qquad(M\ge20). \tag{3}
```

For a unit direction n let delta<=pi/6 be its angular distance from the
nearest radial ray. If delta<=4/(M-3), its loaded vertex supplies support
at least M cos(delta)>=M-8M/(M-3)^2>=M-1. Otherwise set x=(M-3)n.
Its distance from every spoke line is greater than 8/pi>2. Pick a lattice
point ell within 1/sqrt(3) of x, using the elementary triangular tiling.
It lies in L_M and is more than one from every spoke, hence is not a guard.
The cloud point s ell has support greater than M-4. This proves (3)
by support functions. The upper inclusion was established above.

Consequently, normalized by D=2M, K_M tends to the radius-1/2 disk and
each cap tends to its circular segment of angle pi/3. Hence

```math
\frac{\operatorname{area}(C_j)}{D^2}
\longrightarrow a_{\rm cap}
=\frac{\pi/3-\sqrt3/2}{8}>0.                  \tag{4}
```

Each cap has perimeter O(D). A triangular-lattice cell count gives,
uniformly over these six convex caps,

```math
z_j=\frac{\operatorname{area}(C_j)}{a_0}+O(D),
\qquad a_0=\sqrt3/2.                          \tag{5}
```

For completeness the lattice count follows by covering cells of bounded
diameter: cells touching the boundary lie in a fixed-width tube of area
O(per(C_j)+1)=O(M); all other cells contribute exactly one. Scaling changes
the area density by a factor s^2=1+O(M^-2), costing O(1) points. The
difference between the clipping disk and K_M has area O(M), by (3);
there are only O(M) guard indices (at most 7*6M). These estimates give (5)
without assuming a lattice equality case. Oler then makes either isolate-
only or endpoint-including cap slack nonnegative and O(D).

The paired actual-isolate hulls are exactly antipodal. A separate
proof-only claim in the companion exterior report asserts an
O(sqrt(D)) support error from (4)--(5); Audit.94 did not need or audit
that claim, and it is not part of this regression's promoted scope.

### The entire depth-one cap is covered by actual isolate unit disks

Let x in C_j have distance >1 from its boundary. Since B(x,1) is contained
in C_j subset K_M subset B(0,M), one has |x|<=M-1. Its height above the
loaded closing line is greater than one.

Use the orthonormal coordinates along its first bounding ray v_j. The
closing normal is (sqrt(3)/2,1/2). Writing x=t v_j+y Jv_j, its height
condition says

```math
y>\sqrt3(M-t)+2>\sqrt3+2.                    \tag{6}
```

The same inequality holds for distance from the other bounding spoke
line. The point is in the angular sector between those rays; those are
the nearest of the three spoke lines. Thus its distance from every core
point exceeds sqrt(3)+2.

Choose an unscaled lattice point ell with |ell-x|<=1/sqrt(3). Then
|ell|<=M-1+1/sqrt(3)<R_0, so ell lies in L_M, and
dist(ell,T_M)>sqrt(3)+2-1/sqrt(3)>1. Thus ell is not a guard. Its actual
source point q=s ell satisfies

```math
|q-x|<=|ell-x|+(s-1)|ell|<=1/sqrt(3)+1/(100M)<3/5,
```

using |ell|<M and M>=20. Therefore q remains in this very cap: x is more
than one from its boundary and |q-x|<3/5.

Therefore

```math
\boxed{(C_j)_{-1}\subseteq\bigcup_{z\in Z_j}B(z,3/5).} \tag{7}
```

This verifies the cap-covering feature with a strict margin. It supplies
no spare strict site in that deep cap. Contacts with the six radial core
spokes cannot be inferred from the near contacts of this isolated cloud.

## 3. Exact global cardinality trade

There are at least 12M-18 guard indices in L_M. Two explicit disjoint
families are

```math
\{k v_j:1\le k\le M-1\},
\qquad
\{k v_j+v_{j+1}:1\le k\le M-2\}.              \tag{8}
```

The first has 6(M-1) members. The second has 6(M-2), one group in the
interior of each of the six angular sectors. These groups neither overlap
one another nor lie on a radial ray. Each second-family point is a unit
neighbor of k v_j, and its norm is sqrt(k^2+k+1)<=k+1<=M-1<R_0.
All first-family points also lie in L_M. Hence (8) proves the guard count.

Writing N=|A_M|, the exact count is

```math
N=6M+|L_M|-|G_M\cap L_M|
\le |L_M|-6M+18\le |L_M|.                    \tag{9}
```

Choose exactly N distinct points of the **unscaled** unit lattice L_M.
They are unit-separated, and their diameter is at most

```math
2R_0=2M-\frac12=D-\frac12<D.                 \tag{10}
```

This deletes/replaces the old diameter-carrying frame and the cap cloud
together. It keeps the exact original cardinality. Its unit triangles
are allowed: the contradiction is global diameter optimality, not a
triangle-free contact ledger. There is no area-to-slot reversal in (9):
the extra population is a discrete injection into actual lattice guards.

## 4. Exact computational certificates

Command:

```sh
python3 research/verify_target_c_paired_cap_spoke_comparison_2026_10_06.py \
  --output research/target_c_paired_cap_spoke_comparison_certificate_2026_10_06.json
```

The verifier constructs M=5,8,12,20,32. Every original and competitor pair
is checked by integer arithmetic in the triangular basis, independently
using the Cartesian formula ((2i+j)^2+3j^2)/4. It checks the actual contact
and diameter lists, triangle-freeness, every KKT vertex equation, full-source
isolate lower/upper margins, the explicit vacancy injection, convex source
hulls, and exact opposite cap area/population equalities. The certificate
preserves the full M=8 old source and competitor coordinates, plus counters
and exact margins for all five instances.

Observed exact totals: 6,224,805 original-source pair checks and 6,224,805
competitor pair checks. All pass. The largest checked source has 3,294
points, 192 old contacts and three actual diameter pairs; each cap has 111
actual isolates. Every checked competitor contains a unit triangle, as
permitted by the global-diameter endpoint.

The cap asymptotics and depth-one covering are analytic proofs, not
claims established by this finite enumeration. The samples are not globally
optimal; (9)--(10) prove the opposite for every M>=20 (and the checked small
instances). No canonical loading density is assumed by the script.

## 5. Why this does not close the actual cap branch

This family has h=3, q=6 and v=6M. Its active count is

```math
e+h=6M+3<2v-2=12M-2.
```

It cannot satisfy canonical mixed rigidity or the affine-kernel theorem,
and it violates the canonical h>=ceil(D) and stronger linear density.
Many unloaded radial-chain points have degree two, unlike the canonical
unloaded core. Its normalized KKT polytope therefore cannot be substituted
for the canonical post-ZF polytope. The full-source lattice population
excess of a global minimizer is also absent, as (10) demonstrates.

What survives is a concrete discovery pattern: the inactive cap patches
are densely filled and individually have no deep free site, while the
*whole source* still has enough exact lattice vacancies to replace its
diameter core. The exact guard injection pays the core population rather
than attempting to obtain one exterior insertion after deleting a guard.

The companion candidate E.5 releases the actual canonical diameter core
after <=s_Z+1 unloaded deletions. The missing theorem is to force a nonlocal
cap/core refill or an analogous global discrete population injection in
that full canonical source. Neither quadratic caps, their O(D) slack,
positive KKT equilibrium nor antipodal geometry supplies that injection.

## 6. Disposition and remaining lemma

**Audit.94 disposition:** the explicit paired-cap family and same-cardinality
strict sub-diameter competitor are promoted as
`C-PAIRED-CAP-SPOKE-NONGLOBAL-REGRESSION`. This does not exclude exterior
caps in canonical global minimizers or promote the proof-only cap-extraction
route.
No external literature is a proof dependency.

Exact next obligation: prove the companion report's cap-backed nonlocal
refill with |U| sites and all upper distances <D, or prove a discrete
global vacancy injection paying the entire actual core at the same source
cardinality. The radial-spoke injection (8) is specific to this nonglobal
family and cannot be silently extended to a canonical dense core.
