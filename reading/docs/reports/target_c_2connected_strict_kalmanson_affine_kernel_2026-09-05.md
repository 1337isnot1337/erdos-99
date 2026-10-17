> Generated reading edition · [exact source](../../../docs/reports/target_c_2connected_strict_kalmanson_affine_kernel_2026-09-05.md) · source SHA-256 `651fc92c25e97425387180bcf0795fe4f665812b6125b254ec2a110af9c922ba`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-8AC601967B66","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C: 2-connected response forces the affine C53 kernel

**Date:** 2026-09-05  
**Branch:** `research/target-c-c97-adjacent-cut-transition-2026-09-05`  
**Status:** LEVEL I STILL OPEN

## 1. Purpose

C53 proves nonnegativity of every selected two-dimensional KKT stress by reducing its edge-space defect to a weighted Robinson matrix. The preceding Robinson-kernel report shows that a **strict** Robinson similarity has no non-affine equality mode.

This report proves that strictness automatically holds when the selected positive-contact network is 2-connected. Thus, in that case, the C53 equality kernel is exactly the affine coordinate kernel.

The only external input is the standard circular-planar connection theorem already used elsewhere in Target C: for a positive circular-planar electrical network, an order-2 circular response minor is positive exactly when the corresponding two-connection exists. Equivalently, the Kalmanson gaps of the effective-resistance metric are strict when the relevant two-connections exist.

## 2. Strict Kalmanson response from 2-connectivity

Let `G` be a connected positive-conductance circular-planar network with boundary terminals in cyclic order. Assume `G` is 2-vertex-connected.

A 2-connected plane graph has a simple outer-face boundary cycle. Hence every four distinct boundary terminals

`a<b<c<d`

occur on one simple cycle in that cyclic order.

The two complementary pairs of outer-cycle arcs give vertex-disjoint connected paths realizing both noncrossing two-connections

- `{a,b}` together with `{c,d}`;
- `{b,c}` together with `{d,a}`.

By the circular-planar connection/minor theorem, the corresponding order-2 circular minors of the response matrix are strictly positive.

The standard four-terminal Kron reduction used in the Kalmanson proof then gives strict effective-resistance inequalities

`W_ac+W_bd > W_ab+W_cd`,

`W_ac+W_bd > W_ad+W_bc`.                      (2.1)

Thus the boundary effective-resistance metric is **strict Kalmanson**.

Equivalently, in the interval-split decomposition of the Kalmanson metric, every nontrivial circular interval split has strictly positive coefficient. Indeed, the coefficient of an interval split is one half of the corresponding adjacent four-point Kalmanson second difference; both sides of a nontrivial split contain at least two boundary terminals, and (2.1) makes that second difference positive.

### Lemma SK1

For a 2-connected positive circular-planar network, every nontrivial circular interval split coefficient in the effective-resistance Kalmanson decomposition is positive.

## 3. C53 triple signs: finite strictness table

C53 classifies three pairwise-intersecting diameter chords into five endpoint-incidence types. The triangle type is impossible for sufficiently large global minimizers by the promoted Reuleaux-triple exclusion. It remains to treat:

1. a three-edge star on four endpoints;
2. a three-edge path on four endpoints, whose disjoint end edges cross;
3. one shared pair plus a third edge crossing both, on five endpoints;
4. three pairwise-crossing disjoint edges, on six endpoints.

C53 proves that within each abstract type the projective edge order cannot change under a strictly convex deformation. Therefore it suffices to use the same regular-polygon representatives as C53:

| type | unoriented representative edges |
| --- | --- |
| star | `01,02,03` |
| path | `02,03,13` |
| shared pair | `02,03,14` |
| matching | `03,14,25` |

For an oriented projective order `e<f<g` and a circular interval `A`, put

`z_h=1_A(head h)-1_A(tail h)`.

C53's two Robinson differences receive from this split the signed contributions

`A_R=z_g(z_e-z_f)`,

`B_R=z_e(z_g-z_f)`,                             (3.1)

and C53 proves these are always nonpositive.

For each type and each of the three possible placements of the projective-direction cut, the following table gives nontrivial circular intervals whose contribution to the indicated Robinson difference is strictly negative. Labels refer to the cyclic endpoint labels of the representative; an interval such as `01` means the full boundary interval from selected endpoint `0` through selected endpoint `1`, including any unselected boundary terminals that lie between them.

| type | projective-order case | strict interval for `A_R` | resulting `z` | strict interval for `B_R` | resulting `z` |
| --- | --- | --- | --- | --- | --- |
| star | 1 | `01` | `(0,-1,-1)` | `12` | `(1,1,0)` |
| star | 2 | `12` | `(1,0,-1)` | `01` | `(-1,-1,0)` |
| star | 3 | `01` | `(1,0,-1)` | `01` | `(1,0,-1)` |
| path | 1 | `01` | `(1,-1,-1)` | `12` | `(1,1,0)` |
| path | 2 | `12` | `(1,0,-1)` | `12` | `(1,0,-1)` |
| path | 3 | `12` | `(0,1,1)` | `01` | `(1,1,-1)` |
| shared pair | 1 | `01` | `(1,-1,-1)` | `12` | `(1,1,0)` |
| shared pair | 2 | `12` | `(1,0,-1)` | `12` | `(1,0,-1)` |
| shared pair | 3 | `12` | `(0,1,1)` | `01` | `(1,1,-1)` |
| matching | 1 | `01` | `(0,-1,-1)` | `12` | `(1,0,-1)` |
| matching | 2 | `12` | `(0,-1,-1)` | `01` | `(-1,-1,0)` |
| matching | 3 | `01` | `(1,0,-1)` | `01` | `(1,0,-1)` |

The verification is immediate from (3.1). For example `z=(1,0,-1)` gives

`A_R=(-1)(1-0)=-1`,

`B_R=(1)(-1-0)=-1`.

Every interval displayed in the table is nontrivial: among the selected endpoints it contains at least two and its complement contains at least two. Therefore SK1 says its split coefficient is strictly positive.

Since every other split contribution has the C53 weak sign, the existence of one positive-coefficient strict split gives strict total inequalities.

### Lemma SK2 — strict C53 Robinson order

If the selected positive-contact network is 2-connected and the selected positive diameter graph contains no triangle, then for every three diameter edges in projective order

`e<f<g`,

one has

`K_eg < K_ef`,

`K_eg < K_fg`.                                 (3.2)

Thus the C53 Robinson similarity is strict.

For the sufficiently-large Target C regime, the no-triangle premise is automatic by the Reuleaux-triple theorem.

## 4. Edge-space equality kernel

Use C53 notation. Let

`U=EV`,

where rows of `V` are `(1,t_e)` and the projective slopes are strictly increasing. Let

`N=B_H-B_H K B_H`,

`M=E N E`.

C53 gives

`M 1=0`,

`M t=0`,

and proves `M>=0`.

By SK2 the Robinson inequalities are strict. The preceding Robinson-kernel classification (Corollary RK3) therefore gives

`ker M=span{1,t}`.                              (4.1)

Because `E` is invertible,

`ker N=span{E1,Et}=col(U)`.                    (4.2)

Equivalently,

`ker(I-B_H^(1/2) K B_H^(1/2))`

has dimension exactly two, and it is precisely the two-dimensional chord-coordinate space.

## 5. Boundary response equality kernel

Put

`Y=R^(1/2) Q B_H^(1/2)`

on the centered boundary space, as in C53. Then

`Y^T Y=B_H^(1/2) K B_H^(1/2)`.

The nonzero singular values of `Y^T Y` and `YY^T` agree with multiplicity. Hence (4.2) says the eigenvalue `1` of `YY^T` has multiplicity exactly two.

C53 identifies

`I-YY^T`

(up to the invertible `R^(1/2)` congruence) with the boundary Schur defect

`Lambda-L_H`.

The two centered Euclidean coordinate columns `P_x,P_y` are already in its kernel by the affine response identity

`Lambda P=L_H P`.

Since the positive diameter endpoint hull is two-dimensional, these columns are independent. Therefore

### Theorem SK3 — exact boundary affine kernel

For a 2-connected selected positive-contact network in the sufficiently-large Target C regime,

`ker(Lambda-L_H) cap 1^perp = span{P_x,P_y}`.  (5.1)

Including constants,

`ker(Lambda-L_H)=span{1,P_x,P_y}`              (5.2)

on the boundary terminal space.

## 6. Full selected stress kernel

The C30 Schur congruence eliminates positive-contact interior vertices by a positive-definite Dirichlet block. Hence a scalar vector lies in the kernel of the full selected stress matrix

`Omega_s=L_C(alpha)-L_H(beta)`

iff its boundary values lie in the kernel (5.2), with the interior values given by harmonic extension.

For affine boundary data, harmonic extension is the same affine coordinate function because C11's equilibrium identity holds at every interior positive-contact vertex. Therefore

### Theorem SK4 — affine C53 equality kernel under 2-connectivity

If the selected positive-contact network is 2-connected, then

`ker Omega_s = span{1,x,y}`.                   (6.1)

Consequently every vector-valued zero-energy motion on this selected support is affine:

`v_i=A p_i+b`.                                 (6.2)

## 7. Diameter consequence

All positively stressed active bars are tangent under a C13 relative-interior critical velocity. For the affine field (6.2), put

`S=(A+A^T)/2`.

Tangency on a bar of direction `r` is

`r^T S r=0`.                                   (7.1)

If `S!=0`, a nonzero homogeneous quadratic form in the plane has at most two projective zero directions. Distinct diameter edges of a planar diameter graph are never parallel, so a selected support with at least three positive diameter edges supplies at least three projective zero directions. Therefore `S=0`.

Thus `A` is infinitesimally skew-symmetric, and the selected support moves by one infinitesimal Euclidean motion. In particular all of its positive diameter chords have one common angular rate.

### Corollary SK5

For a zero-energy C13 stress whose positive-contact network is 2-connected:

- either the stress uses at most two positive diameter edges; or
- every positive diameter edge in that stress has one common angular rate under the weak-release velocity.

This is exactly the equality rigidity missing from C53 in the 2-connected response phase.

## 8. Remaining C54 gate

This does **not** yet prove that every strong diameter chord in `H_*` has the same rate, because the direction-dependent zero-energy stress selected by C13.3 need not have maximal KKT support.

Let `Z(v)` be the zero-energy face of the normalized KKT polytope for the relative-interior weak-release velocity, and let `X(v)` be the union of supports of its stresses, as in C25. A relative-interior point of `Z(v)` has support exactly `X(v)`. Applying SK5 to that maximal zero-energy support gives the next exact fork:

1. its positive-contact graph has a cut vertex;
2. it has at most two blocked diameter edges; or
3. all blocked diameter edges have one common angular rate.

Cases 2 and 3 are close to the already-integrated low-diameter/common-rate mechanisms. The remaining genuinely new obstruction is therefore a cut-vertex/block-tree zero-energy response.

This reduces C54 from a general PSD-kernel problem to a block-cut integration problem for the maximal zero-energy stress support.

## References used

- S. Forcey, *Circular planar electrical networks, split systems, and phylogenetic networks*, especially the circular-minor / connection criterion and the Kalmanson resistance theorem already imported elsewhere in Target C.
- The C53 thrackle interval-sign classification and C52.R weighted Robinson lemma in this repository.
