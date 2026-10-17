> Generated reading edition · [exact source](../../../docs/reports/integrator_ambient_force_geometry_2026-09-09.md) · source SHA-256 `751ee7b3157cf76f7b0d4f367d7d67d744a00e2d53cc318cbc9cdc1567f0214d`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-65C564B51486","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# Erdős Problem #99 — ambient roundness transports into every force hull

**Date:** 2026-09-09
**Run type:** cross-target bridge proof and scope audit
**Targets:** A global hull geometry; B packing saturation; C force geometry
**State lock:** integrator base `6ed9d78`, subsequently rebased over `cf79015`; the
four intervening post-PI reports do not change the canonical inputs below
**External literature/computation:** no new literature; no computation in proofs

## LEVEL I STATUS

`STILL OPEN`

The main result is unconditional relative to the promoted theorem ledger.
The Target C route map and shared theory module promote **AG/AR/AS/AP only**
(Sections 1–6 and 8). The post-ZF numerical consequence remains explicitly
conditional on its separate report-level inputs.

## 1. The bridge and the distinction it repairs

The global source hull and a selected KKT force hull are generally different.
Nevertheless, inclusion transports an **upper circumradius bound** without any
population theorem. The older discussion after C10.24 in the
[force-polygon report](target_c_force_polygon_2026-08-30.md) left near-minimal force
circumradius conditional on controlling invisible points. That particular obstacle
is unnecessary after [Target A Section 155](../targets/target-a/08-prescribed-phase-alignment.md).
Its source-hull estimate applies to every global source, before its additional
very-super-boundary hypothesis is used to embed a smaller optimum.

The exact implication is

```text
global source packing -> near-minimal source circumradius
  -> every diameter-support hull has near-minimal circumradius
  -> uniform reciprocal-perimeter saturation and small diameter-star angles
  -> approximate centered cyclic model of the force hull
  -> area/perimeter restrictions on the actual force hull.
```

This does not identify source and force hulls, eliminate isolates, or transport
anything into Target A's scaffold Schur matrix.

## 2. Trusted inputs and notation

Let `A` be any planar global minimum-diameter unit-separated configuration, of
diameter `D>16 sqrt(3)`. Triangles are allowed in the geometric results below.
Let `K=conv A`, translate its circumcenter to zero, and set

```math
\eta=3^{1/4}\sqrt D,\qquad R_0=D/2+\eta,
\qquad \mu=\sqrt{D\eta+\eta^2}.
\tag{AG.1}
```

Section 155 gives

```math
K\subseteq B(0,R_0).
\tag{AG.2}
```

Its proof uses full-source Oler/isodiametric saturation and Bonnesen, not the
cardinality of the positive contact core. The same global information appears in
[Target B Sections 24 and 36](../targets/target-b/01-jammed-rhombic-branch.md).
In particular `eta=O(D^(1/2))` and `mu=O(D^(3/4))=o(D)`.

Choose any nonempty collection `J` of actual length-`D` source pairs. Write its
endpoints as `E_J`, and put

```math
F_J=\operatorname{conv}E_J,\qquad
P_J=\frac D2\operatorname{conv}\{\pm u_e:e\in J\},
\tag{AG.3}
```

where `u_e` is either unit direction along edge `e`. Both hulls have diameter `D`.
For a selected normalized KKT stress, take `J=H_+`; C10 identifies `F_J` with its
actual force hull. This is also valid for maximal support.

For degenerate convex sets, perimeter below means the continuous convex-geometric
extension; in particular a segment of length `D` has perimeter `2D`.

## 3. Theorem AG — simultaneous midpoint and force-hull control

For every such source and collection `J`, simultaneously:

```math
\boxed{|(b+k)/2|\le\mu\quad(bk\in J),}
\tag{AG.4}
```

```math
\boxed{d_H(F_J,P_J)\le\mu,\qquad d_H(F_J,-F_J)\le2\mu,}
\tag{AG.5}
```

and

```math
\boxed{D/2\le R(F_J)\le D/2+\eta.}
\tag{AG.6}
```

Every endpoint of `J` additionally satisfies

```math
D/2-\eta\le |b|\le D/2+\eta.
\tag{AG.7}
```

### Proof

For `bk`, put `m=(b+k)/2` and orient `u=(b-k)/D`. Then
`b=m+(D/2)u`, `k=m-(D/2)u`. The parallelogram identity gives

```math
|m|^2+D^2/4=(|b|^2+|k|^2)/2\le R_0^2,
```

proving AG.4. Thus each actual endpoint is within `mu` of its corresponding
centered half-diameter vector, and conversely every generating half-diameter
vector is within `mu` of an actual endpoint. Convex combinations preserve this
distance bound, giving the first part of AG.5. Since `P_J=-P_J`, the triangle
inequality for Hausdorff distance gives its second part.

The enclosing source disk contains `F_J`; its diameter supplies the opposite
bound `R(F_J)>=D/2`. Finally `D=|b-k|<=|b|+|k|` and `|k|<=R_0` give AG.7.
No matching, stress-weight, or source-population assumption was used. QED.

### Consequence: the possible limiting force hulls

After division by `D`, every Hausdorff subsequential limit of `F_J` is centrally
symmetric about the source circumcenter. It is the convex hull of a nonempty
closed antipodal subset of the radius-`1/2` circle. To see the last assertion,
take a Hausdorff subsequence of the compact generating subsets of that circle;
convex hull and AG.5 preserve the limit.

The limit can be a proper subset of the disk. Exact central symmetry of any
finite source or force hull is not asserted.

## 4. Corollary AR — reciprocal perimeter saturates uniformly over stresses

For every normalized KKT stress of the same source for which C10's reciprocal
polygon is defined, its perimeter `P_*` satisfies

```math
\boxed{\frac{D^2}{D/2+\eta}\le P_*\le2D,}
\tag{AR.1}
```

and hence

```math
\boxed{0\le2D-P_*\le\frac{4D\eta}{D+2\eta}<4\eta.}
\tag{AR.2}
```

In particular `P_*/D -> 2`, uniformly over all normalized stresses along every
unbounded sequence of global sources.

### Proof

C10.16 gives `D^2/R(F_J)<=P_*<=2D`. Substitute AG.6 and subtract. Equivalently,
use the exact virial identity `D^2=sum_b g_b dot b<=R_0 sum_b|g_b|` directly.
The constant is independent of support size and multiplier values. QED.

C10's exact equality classification remains intact: `P_*=2D` holds precisely
for a supported diameter matching. Convergence of `P_*/D` to `2` does **not** imply
that the number of branching diameter edges is small.

## 5. Corollary AS — the shared-endpoint angle ceiling vanishes

For two distinct source diameter pairs `bx,by`, their angle `theta` obeys

```math
\boxed{\sin(\theta/2)\le \min\{1,2\mu/D\}.}
\tag{AS.1}
```

Thus, once `2mu<D`,

```math
\boxed{\theta\le2\arcsin(2\mu/D)=O(D^{-1/4}).}
\tag{AS.2}
```

### Proof

The two midpoints are in `B(0,mu)` by AG.4. Their difference is `(x-y)/2`, so
`|x-y|<=4mu`. On the other hand `|x-y|=2D sin(theta/2)`. QED.

This improves the asymptotic constant ceiling in C18, although the old finite
bound may be stronger at moderate `D`. It applies to **all** actual diameter
pairs of **every** global minimizer, without lexicographic normalization.

## 6. Theorem AP — finite area and perimeter transport

Write `F=F_J`, `P=P_J`, and let `g_1,...,g_h` be the cyclic gaps of the distinct
projective directions of `J`; thus `g_i>0` and `sum g_i=pi`. The formulas also
extend to `h=1` with `g_1=pi`.

The centered polygon has the exact values

```math
\operatorname{per}(P)=2D\sum_i\sin(g_i/2),\qquad
\operatorname{area}(P)=\frac{D^2}{4}\sum_i\sin g_i.
\tag{AP.1}
```

Moreover

```math
|\operatorname{per}(F)-\operatorname{per}(P)|\le2\pi\mu,
\tag{AP.2}
```

```math
|\operatorname{area}(F)-\operatorname{area}(P)|
\le\pi D\mu+\pi\mu^2.
\tag{AP.3}
```

### Proof

The circle has radius `D/2`. The `2h` consecutive angular gaps are two copies
of the projective gaps. Chord lengths and triangle areas give AP.1. AG.5 gives
both inclusions into the other hull's radius-`mu` parallel body. Perimeter
monotonicity and the parallel-body formula prove AP.2. Steiner's area formula,
together with `per(F),per(P)<=pi D`, gives AP.3. QED.

### Area-perimeter stability specific to these force hulls

For `0<=g<=pi`,

```math
g-\sin g\le4\bigl(g-2\sin(g/2)\bigr).
\tag{AP.4}
```

Indeed the difference of right and left sides is
`f(g)=3g+sin g-8sin(g/2)`, with `f(0)=0` and
`f'(g)=2(cos(g/2)-1)^2>=0`. Summing and using AP.1 yields

```math
\operatorname{area}(P)\ge D\operatorname{per}(P)-3\pi D^2/4.
```

Consequently

```math
\boxed{\operatorname{area}(F)\ge D\operatorname{per}(F)-3\pi D^2/4
 -3\pi D\mu-\pi\mu^2.}
\tag{AP.5}
```

In any normalized subsequential limit, writing `a=lim area(F)/D^2` and
`p=lim per(F)/D`,

```math
\boxed{a\ge p-3\pi/4.}
\tag{AP.6}
```

In particular `p=pi` forces `a=pi/4` and the limiting body is the disk, not
an arbitrary body of constant width. This directly strengthens the geometric
limit used in the report-level JN/GS cavity arguments without importing their
external stability theorems.

## 7. Direction-density consequence and its exact status

Suppose the `h` projective gaps satisfy `g_i>=delta_D`, where
`delta_D=2asin(1/(2D))`. This is the elementary diameter-direction separation
proved in [C67 Sections 1](target_c_force_hull_area_floor_2026-08-31.md); only that
finite geometric lemma is needed, not the report's later force-count hypotheses.

Concavity of sine on `[0,pi]` gives

```math
\sum_i\sin g_i\ge(h-1)\sin\delta_D+
\sin((h-1)\delta_D).
\tag{AD.1}
```

For clarity, the feasible simplex has all but one gap at the lower bound at
each extreme point. Its remaining gap is `pi-(h-1)delta_D`; the sine of this
gap is `sin((h-1)delta_D)`. A concave function attains its minimum at an extreme
point. This uses the entire projective circle, with no single-arc assumption.

Therefore

```math
\boxed{\frac{\operatorname{area}(F)}{D^2}\ge
\frac{(h-1)\sin\delta_D+\sin((h-1)\delta_D)}4
-\frac{\pi\mu}{D}-\frac{\pi\mu^2}{D^2}.}
\tag{AD.2}
```

If `h/D -> y`, then `0<=y<=pi`, and

```math
\boxed{\liminf\frac{\operatorname{area}(F)}{D^2}\ge
\frac{y+\sin y}{4}.}
\tag{AD.3}
```

The expression is increasing on `[0,pi]`.

**Conditional post-ZF consequence.** If the additional
[DB report](target_c_post_zf_difference_body_perimeter_2026-09-09.md) hypotheses
hold, then `liminf h/D>=2rho`, where `rho=cos rho` in `(0,1)`. Thus

```math
\boxed{\liminf\frac{\operatorname{area}(F)}{D^2}\ge
A_{\rm int}:=\frac{2\rho+\sin(2\rho)}4
=0.6184708847\ldots .}
\tag{AD.4}
```

This improves PI's `0.4978566363...` floor by using the ambient global source,
not by strengthening the standalone projective-circle statement. The error in
AD.2 is `O(D^(-1/4))`, which is appropriate for this fixed quadratic gain, not
for a one-integer shell contradiction.

## 8. Regression and scope audit

| Test | Result and exact reason |
| --- | --- |
| Heptagon plus isolated center | Compatible. No point is declared diametral; the asymptotic estimates are for large `D`. |
| Noncentrally-symmetric finite matching | Compatible. AG.5 has a nonzero error; exact symmetry is not claimed. |
| Regular odd shells | Compatible. They approach a circle, their diameter-star angles vanish, and `P_*/D` tends to `2` despite branching. Global optimality is not certified by this consistency check. |
| Positive support misses quadratic population | Allowed. Only `F_J subset K` is used for circumradius. No force-hull area fraction follows from that inclusion alone. |
| Near-star electrical networks | No conductance lower bound or response eigenvalue conclusion is inferred. |
| C-II diameter branching of order `D` | Compatible with AR: many almost parallel loads can have small total angular cancellation. |
| Local/jammed packings with nonround ambient hull | Excluded from the theorem's hypotheses by global packing/Section 155, not by an invented local stability condition. |
| Target A monomer and local SDR regressions | Untouched. No lattice matching or response nullity is inferred. |

## 9. Classification and remaining endpoint

- **Proved from canonical inputs:** AG, AR, AS, AP, including the limiting
  centrally symmetric cyclic force-hull class.
- **Proved under an explicit finite geometric hypothesis:** AD.2/AD.3.
- **Conditional on report-level DB:** the numerical floor AD.4.
- **Not proved:** exact symmetry, a matching diameter graph, subquadratic isolated
  population, any Schur-rank inequality, or Level I.

AG/AR/AS/AP are promoted after the integrator proof/scope audit. The conditional
DB specialization and post-ZF topology are not promoted by association.
The newly narrowed C-II question is whether a fully force-visible unit-contact
network can satisfy this asymptotically cyclic, centrally symmetric boundary model,
vanishing diameter-star angles, and the exact source-population constraints.

The next numerical bridge is to combine AP.6 and AD.4 with the *actual-perimeter*
joint cavity budget, rather than replace that perimeter prematurely by `pi D`.

### Explicit regression against a matching inference

For the regular unit-sided odd `N`-gon (`N>=5`), let
`R=1/(2sin(pi/N))` and `D=2Rcos(pi/(2N))`. Its diameter graph is a cycle,
with `N` edges and degree two at every vertex. Assign `beta=1/N` to every
diameter edge and `alpha=D^2/N` to every unit contact. The cyclic vector sums
verify KKT equilibrium and both normalizations directly. Each boundary reaction
has length `4R cos^2(pi/(2N))/N`, so

```math
P_*=2D\cos(\pi/(2N)),\qquad P_*/D\longrightarrow2.
```

Yet converting its diameter graph into a matching requires deleting at least
`(N+1)/2=Omega(D)` edges. This family is not certified globally optimal as
`N` grows. It is an exact regression against extracting a matching count from
the reciprocal ratio and KKT equilibrium alone. The shrinking star angles
explain the small cancellation.

### Reproducible finite checks

`python3 research/integrator_ambient_force_audit.py` checks 48 enclosing-disk
geometry cases, including the finite nonsymmetric matching regression. These
floating-point checks are not used in the analytic proofs and do not encode
global optimality. Its exact rational check also verifies the coarse derivative
margin used in the conditional cavity report.
