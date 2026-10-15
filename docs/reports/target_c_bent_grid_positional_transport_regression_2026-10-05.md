<!-- theorem-state: {"artifact_id":"ART-474B8475D298","canonical":false,"claim_ids":["C-BENT-GRID-REDUCED-POSITIONAL-TRANSPORT-REGRESSION"],"claim_statuses":{"C-BENT-GRID-REDUCED-POSITIONAL-TRANSPORT-REGRESSION":"regression"},"index":"docs/state/artifact-index.jsonl","status":"regression","target":"target-c"} -->
# Target C — small train angles do not give vanishing positional transport

Date: 2026-10-05. Base main: `3c94a1a93641a5f8fa24d43068d487594d3e38cd`.
State: `2026-10-05.audit.57`. Classification: **regression**;
artifact lifecycle is **unreviewed** pending independent audit.
C-II and Level I remain open.

## 1. Exact failed bridge and scope

The [loaded-attachment candidate](target_c_loaded_attachment_lattice_obstruction_2026-10-05.md),
Section 8, excludes a canonical source if its actual diameter endpoints
admit a bounded lattice cover with vanishing positional error. The
following reduced-input inference cannot supply that cover:

```
quadratic physical rhombus grain + boundary-order angular excess
+ train phases differing by O(1/D) + positive pinned equilibrium
+ full pinned contact rank
-> vanishing physical positional error from one affine lattice.
```

An explicit triangle-free contact grid below satisfies the antecedent
but remains a fixed positive distance from every single affine lattice
with uniformly bounded inverse basis norm. Its boundary pins are not
certified actual diameter endpoints. It therefore does not refute a
transport theorem using the complete canonical loaded source, does not
rule out a bounded multiple-lattice cover, and supplies no global
minimum-diameter example. It tests the precise bulk-error accumulation
shortcut, not the actual-load route.

## 2. Exact source family

Let M>=8 be even. For 0<=i<M define

    t_i=i/(2M^2),
    u_i=((1-t_i^2)/(1+t_i^2), 2t_i/(1+t_i^2)).

Let v be the rotation of (1/2,sqrt(3)/2) by 2atan(1/M). Set

    U_0=0, U_i=sum_{a<i}u_a,
    p_ij=U_i+j*v,       0<=i,j<=M.

All coordinates lie in Q(sqrt(3)); the u_i coordinates are rational.
Every horizontal contact vector is u_i and every vertical contact
vector is v. Their lengths are exactly one. Write

    theta_i=2atan(i/(2M^2)),
    phi=pi/3+2atan(1/M).

Then 0<=theta_i<1/M, and

    pi/3 < phi-theta_i < pi/3+2/M < pi/2.

Each cell is therefore a strict unit rhombus. The complete unit-contact
graph is precisely the rectangular grid, hence triangle-free.

To check completeness without numerical tolerances, compare a source
point difference with a*u+b*v0, where u=(1,0), v0=(1/2,sqrt(3)/2),
and a,b are its signed index differences. Its error has norm at most
(|a|+2|b|)/M, since each u_i differs from u by at most 1/M and v differs
from v0 by less than 2/M. Moreover

    |a*u+b*v0| >= sqrt((a^2+b^2)/2).

Thus the relative error is at most sqrt(10)/M. Except for the four
basis steps and the two short-diagonal index steps (1,-1),(-1,1), the
integer quadratic form a^2+b^2+ab is at least three. Their lengths are
at least sqrt(3)*(1-sqrt(10)/M)>1 for M>=8. The short-diagonal cases
have vectors u_i-v or its negative and are strictly longer than one
by the displayed angle range. This checks every pair.

The cells form an actual simple rhombus disk: projection onto the
normal n=(v_y,-v_x) increases strictly with i, and adjacent strips
are translations in direction v. There are M^2 cells, (M+1)^2 points,
2M(M+1) contacts and 4M boundary unit edges. The diameter D satisfies
M/2<=D<=2M. All reduced train phases lie in a window of width less
than 2/M. Total acute angular excess and total rhombus area excess
above sqrt(3)/2 per cell are both positive and less than 2M=O(D).
Consequently the full grain is increasingly coherent, not merely
coherent in a fixed-width phase bin.

## 3. Positive pinned equilibrium and full pinned rank

Pin every grid boundary vertex. Put

    alpha_i=1/(u_i dot n)>0.

At an interior column i, the difference
alpha_i*u_i-alpha_(i-1)*u_(i-1) has zero n-projection, so it equals
c_i*v for a real c_i. Give each horizontal edge in column interval i
weight alpha_i, independent of j. Set

    B=1+M*max_i|c_i|,
    beta_ij=B-j*c_i,

on the vertical edge from (i,j) to (i,j+1) of an interior column.
These weights are strictly positive. Give the two boundary columns
any positive vertical weights. At every unpinned vertex the horizontal
force is c_i*v and the vertical force is
(beta_ij-beta_i,j-1)*v=-c_i*v. Hence all unpinned vertices have exact
positive contact equilibrium.

For full pinned rank, let a contact flex vanish on the boundary. The
vertical contact equations make its v-projection constant along each
column, and the pinned endpoints make that projection zero. Every
velocity is therefore lambda_ij*n. A horizontal contact equation is

    (u_i dot n)*(lambda_(i+1,j)-lambda_ij)=0.

Its positive coefficient makes lambda constant along every row.
The pinned row endpoints force all velocities to vanish. This proves
full pinned contact rank analytically, without a generic-rank premise.

## 4. A fixed positional obstruction to every single lattice

Let an affine lattice have inverse basis norm at most K. Distinct
lattice vectors are then separated by at least 1/K. Suppose each
bottom-row point U_i has a lattice approximant a_i with error at most
epsilon. The increment z_i=a_i+1-a_i is a lattice vector and
|z_i-u_i|<=2epsilon. Since |u_i-u_j|<1/M,

    |z_i-z_j|<=4epsilon+1/M.

If M>2K and epsilon<1/(8K), all z_i must be the same vector. The
a_i are an arithmetic progression. In particular

    a_(M/2)=(a_0+a_M)/2.

But the rational vertical coordinates of the U_i satisfy

    (U_M)_y/2-(U_(M/2))_y >= 1/8-1/(4M^2)>1/10.

Indeed (u_i)_y=(i/M^2)/(1+i^2/(4M^4)) differs from i/M^2 by at most
1/(4M^3). The corresponding half-sum minus first-half sum for i/M^2
is exactly 1/8; the total error is at most 1/(4M^2). Approximating the
three points by the arithmetic progression bounds their midpoint
residual by 2epsilon, so epsilon>1/20. Therefore, for M>2K, no
single such lattice approximates the whole source with error less than

    min(1/(8K),1/20).

The bound permits the lattice, its orientation and its translate to
vary with M. The failure is a physical bow of constant size accumulated
from train rotations of order 1/M; a different uniformly conditioned
lattice cannot absorb it as a uniform shear.

## 5. Consequence for the live attack

This kills the stated reduced-input bridge to single-lattice positional
transport. Positive pinned equilibrium and full pinned rank do not fix
it. To apply the branch-independent diameter-normal theorem, an argument
must use the actual loaded endpoint constraints, control accumulated
transport beyond these angular budgets, or establish a suitable bounded
multiple-lattice cover. No packet capacity follows from the bow or from
failure of single-lattice transport.

The example's pins are never identified with canonical loads. Its
actual diameter population and global optimality are not certified.
No statement here eliminates either exhaustive canonical branch or
changes theorem lifecycle.

## 6. Exact verifier

`research/verify_target_c_bent_grid_transport_2026_10_05.py` uses Fraction
arithmetic in Q(sqrt(3)). For M=8,12,16 it checks every source pair,
exact unit contacts, strict noncontacts, the contact count, the rational
bow bound and 0<E4<2M. The infinite-family separation and lattice
obstruction, positive equilibrium, pinned rank and asymptotic scope
are proved analytically above. The script does not certify actual
diameter loading, global optimality or failure of multiple-lattice
transport. No numerical search is a proof premise.
