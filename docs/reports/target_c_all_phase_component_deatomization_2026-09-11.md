<!-- theorem-state: {"artifact_id":"ART-DDC77A25711F","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — all-phase component bounds from convex-boundary turning

**Date:** 2026-09-11  
**Repository commit:** `fdb7374cf7e2f5b4e63587d3567473b3421d822f`  
**State version:** `2026-09-11.audit.10`  
**Run type:** closing-proof attempt / new geometric bridge  
**Target:** full-source Target C-II, both Woodall branches  
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md`  
**Classification:** proved candidate awaiting promotion; this report is unreviewed and noncanonical  
**Literature:** no external theorem imported; the linked GitHub landing page was unavailable to public browsing; the clean local checkout supplies the state lock  
**Computation:** none needed for the component theorem

## LEVEL I STATUS

`STILL OPEN`. C-II is **not** resolved by this report.

## 1. Locked endpoint and new implication chain

The requested endpoint is exclusion of every sufficiently large triangle-free
global minimizer in the contact-minimal, then diameter-pair-minimal C-II normal
form. All source points, including contact isolates, remain in that endpoint.

This report proves a narrower candidate reduction:

```text
bounded harmonic cell + degree at least three
  -> definite local turning of the loaded convex boundary
  -> bounded components can accumulate only at finitely many large corners
  -> their number is o(D), and a finite turning charge strengthens this to O(M^2)
  -> the canonical O(D) sum of component diameters gives c_I=O(D^(2/3))
  -> remove the linear component-count term from the all-phase ZU/PC ledgers.
```

This chain is a structural reduction, not a contradiction. A further global
source-capacity or response theorem is still required.

Only canonical inputs are used in the new proof. The earlier unreviewed report
`target_c_nearcircle_no_bounded_harmonic_components_2026-09-09.md` is a related
lead: it proves a stronger minimum-size conclusion under a disk-limit hypothesis.
Its claims are not imported as premises. Here the limit may have corners and
flat sides, and the conclusion concerns the **number** of small components.

## 2. Notation and hypotheses

Let a sequence of canonical C-II sources have diameters `D_j -> infinity`.
Write `F_j` for their force hulls and `B_j` for the loaded hull vertices.
Let `I_{j,r}` be the connected components after deleting `B_j` from the
nonisolated positive contact core, with

\[
\delta_{j,r}=\operatorname{diam}_{C[I_{j,r}]}I_{j,r},\qquad
A_{j,r}\subset B_j
\]

their graph diameters and distinct loaded attachment sets. A singleton has
graph diameter zero. Contact-isolated source points are **not** these singleton
components: they are outside the nonisolated contact core.

The proof uses the following exact facts:

1. `B_j=Vert(F_j)` and the source is unit-separated.
2. Every vertex of `I_{j,r}` has at least three unit-contact neighbors, all in
   `I_{j,r} union A_{j,r}` (C26).
3. `I_{j,r} subset conv(A_{j,r})` and
   `diam(A_{j,r}) <= delta_{j,r}+2` (C36/C40).
4. Each loaded vertex has contact degree at most three (C35).
5. After the canonical translation and division by `D_j`, the force hulls
   have subsequential convex limits with nonempty interior.
6. `sum_r delta_{j,r}=O(D_j)` uniformly (the canonical ZK identity).

For (5), the audited FSDB bound supplies

\[
\liminf\operatorname{area}(F_j)/D_j^2>154451/250000>0.
\]

Boundedness follows from diameter one after normalization. Thus a limiting
force hull cannot be a segment. Neither a disk limit nor a smooth limit is
assumed. The source circumcenter is only a translation choice.

## 3. Elementary local lemmas

### Lemma AC.1 — three contacts do not fit in a narrow strip

If a unit-separated set contains a point `x` and three distinct unit neighbors
of `x`, those four points cannot all lie in a strip of width strictly less
than `1/2`.

**Proof.** Let `n` be a unit strip normal. Each unit neighbor direction `u`
satisfies `|n.u|<1/2`. The possible directions form two open arcs, each of
angular width `pi/3`, around the two strip-tangent directions. Two unit
neighbors in the same arc have distance strictly less than one. Thus there
is at most one neighbor in each arc, at most two in total. This contradicts
the assumed three neighbors. No stress-weight lower bound is used. QED.

### Lemma AC.2 — local convex-boundary flattening with a corner allowance

Suppose convex polygons `K_j` converge in Hausdorff distance to a convex body
`K` with nonempty interior. Let `p in partial K`, and let `tau(p)` be the
exterior turning angle at `p` (zero at a point with a unique tangent).
Suppose `X_j subset Vert(D_j K_j)` has diameter at most `L`, and every
`x/D_j`, `x in X_j`, tends uniformly to `p`. If

\[
\tau(p)<\arctan\frac1{4L},
\]

then `conv(X_j)` lies in a strip of width less than `1/2` for all large `j`.

**Proof.** All supporting normals at boundary points of `K_j` tending to
`p` have limit points in the normal cone of `K` at `p`. Indeed, pass to the
limit in `n_j.(y-x_j)<=0` for `y in K_j`. Thus the oriented edge tangents
on the local boundary arc containing `X_j/D_j` lie, for all large `j`, in
a cone of angular width at most `tau(p)+epsilon`.

This is the local arc, not the complementary trip around the polygon.
Its existence follows, for example, by choosing an interior point of `K`:
the nearby polygons contain that point, and their boundaries have continuous
radial parametrizations. Points converging to `p` belong to one shrinking
boundary arc. A nondegenerate limit is essential here.

Choose `epsilon>0` with

\[
\tau(p)+\epsilon<\arctan(1/(2L))<\pi/2.
\]

Use the midpoint direction of the tangent cone as an axis. Projection onto
that axis increases along the local arc. Its total increase between the
first and last selected vertices is at most their distance, hence at most
`L` in the unscaled polygon. The total variation perpendicular to the axis
is at most `L tan(tau(p)+epsilon)`, which is strictly less than `1/2`.
The selected vertices and their convex hull lie in a strip of that width.
QED.

### Lemma AC.3 — few loaded vertices in a small disk

For any disk of radius `R`, the number of loaded vertices in the disk is at
most `2pi R+2`.

**Proof.** Every subset of vertices of a convex polygon is in convex
position. If the disk contains at least three such vertices, their convex
hull has at least one unit of perimeter per vertex, by unit separation.
Its perimeter is at most that of the disk, `2pi R`, by monotonicity of convex
perimeter. The cases of zero, one, or two vertices are covered by `+2`. QED.

## 4. Main bounded-component theorem

### Theorem AC.4 — all-phase bounded-component count

For every fixed nonnegative integer `M`, let

\[
N_M(j)=\#\{r:\delta_{j,r}\le M\}.
\]

Then, under hypotheses 1–5 above,

\[
\boxed{N_M(j)=o(D_j).}
\]

**Proof.** It suffices to prove the statement on every convergent subsequence
of the normalized force hulls. Let its limit be `K`, with nonempty interior.
Put `L=M+2` and

\[
\theta_M=\arctan\frac1{4(M+2)}.
\]

Let `T_M` be the set of corners of `K` with exterior turning angle at least
`theta_M`. This set is finite: the exterior-angle atoms of a convex curve
have sum at most `2pi`, so `|T_M|<=2pi/theta_M`.

For each counted component choose one attachment vertex as its representative.
Every accumulation point of normalized representatives belongs to `T_M`.
To see this, suppose representatives from a sequence of counted components
tend to `p notin T_M`. Their entire attachment sets tend uniformly to `p`,
since their diameters are at most `M+2`. Lemma AC.2 puts each attachment hull,
and hence its unloaded component, in a strip of width less than `1/2`.
All contact neighbors of any vertex of that component lie in the same hull.
Lemma AC.1 contradicts its contact degree at least three.

It follows by compactness that, for every fixed `epsilon>0`, all sufficiently
late representatives lie in the union of the disks of radius `epsilon D_j`
centered at the scaled points of `T_M` (with the chosen translation restored).
Otherwise a subsequence outside that neighborhood has an accumulation point
outside `T_M`.

Each loaded vertex can represent at most three components, since each
represented component uses a distinct incident contact and its contact degree
is at most three. Lemma AC.3 therefore gives

\[
N_M(j)\le 3|T_M|(2\pi\epsilon D_j+2).
\]

First let `j -> infinity`, with `M` and `epsilon` fixed, and then let
`epsilon -> 0`. This gives `N_M(j)/D_j -> 0`. The argument applies to every
convergent subsequence, so it proves the original sequence statement. QED.

### Corollary AC.5 — all-phase sublinear component count

For canonical post-ZF C-II sources in either Woodall branch,

\[
\boxed{c_I=o(D).}
\]

**Proof.** Let `sum_r delta_r <= C D` for large `D`. For every fixed positive
integer `M`,

\[
c_I\le N_M+\frac{CD}{M+1}.
\]

Theorem AC.4 gives `limsup c_I/D <= C/(M+1)`. Letting `M -> infinity`
proves the claim. The limits are taken in this order; there is no assertion
uniform in a growing cutoff `M=M(D)`. QED.

The canonical uniform diameter budget can be checked without any new packing
estimate. ZU gives `c_I+e_BB+s_C=q-2+k`, where `k=d_H+s_Z`, and ZK gives

\[
\sum_r\delta_r\le6+e_{BB}+2s_C-3k
=2+2q-e_{BB}-k-2c_I\le2+2\pi D.
\]

The theorem does **not** give `min_r delta_r -> infinity` for a general
limit with corners. A bounded number, or a sublinear number, of bounded
components near corners is allowed.

## 5. Quantitative strengthening: a finite curvature budget

The compactness proof above can be replaced by a finite argument. This gives
more than `c_I=o(D)` and makes the uniformity of the conclusion explicit.

### Lemma AC.6 — finite count of bounded components in a fat force hull

Suppose the exact hypotheses 1–4 of Section 2 hold, `diam(F)=D`, and for
some center `o` one has

\[
B(o,D/20)\subset F\subset B(o,11D/20).
\]

Then for every nonnegative integer `M`,

\[
\boxed{N_M\le5000\pi(M+2)^2.}
\]

The constant is deliberately coarse. It is uniform in the source,
conductances, number of vertices, and diameter `D`.

**Proof.** Translate `o` to zero and put `L=M+2>=2`. First note
`c_I<=q<=pi D`. Indeed every component has at least three distinct loaded
attachments by C36, each loaded vertex has contact degree at most three,
and the hull is unit-separated. If `L>D/10000`, this already gives

\[
N_M\le\pi D<10000\pi L\le5000\pi L^2.
\]

It remains to handle `L<=D/10000`.

Choose one representative attachment `b` for each counted component. Every
other attachment `a` of that component has `|a-b|<=L`. Since both radii are
at least `r=D/20`, their minor polar separation `alpha` satisfies

\[
2r\sin(\alpha/2)\le|a-b|\le L,
\qquad
\alpha\le 2L/r\le1/250.
\]

Here `arcsin x<=2x` for `0<=x<=1/2` suffices. Since zero is inside `F`,
the attachments belong to one local boundary arc in this polar window.

Let `p` be a point on that local arc and `n` an outward unit normal there.
Writing `R=11D/20` and `e=b/|b|`, the support inequality gives

\[
n\cdot(p/|p|)\ge r/R=1/11,
\]

and therefore

\[
n\cdot e\ge1/11-1/250>1/22.
\]

Consequently the counterclockwise unit tangent has projection greater than
`1/22` onto `Je`. Along the local arc from `b` to any attachment, this
projection is monotone. Its total change is at most `|a-b|<=L`; that arc
has length at most `22L`. All attachments are thus in the boundary-arclength
window of radius

\[
w=22L
\]

centered at the representative.

Each such window has convex-boundary turning at least

\[
\theta=\arctan(1/(4L)).
\]

Otherwise its edge directions lie in a cone of width less than `theta`.
On the subarc between the first and last attachments, the same monotone
projection argument as AC.2 confines their convex hull to a strip of width
at most `L tan(theta)=1/4`. This contradicts AC.1 and C36. Turning here is
the positive exterior-angle measure of the polygon, with an endpoint atom
included when present.

Choose a maximal family of representatives at pairwise circular arclength
distance greater than `2w`. Their closed radius-`w` windows are disjoint,
so the total turning `2pi` bounds the number of chosen representatives by
`2pi/theta`. Maximality ensures every other representative is within
arclength `2w` of a chosen one.

A radius-`2w` arclength window has length `4w` and contains at most `4w+1`
loaded vertices: consecutive such vertices are at least one apart in
arclength. Each loaded vertex represents at most three components. These
windows are proper arcs, since `4w=88L<=88D/10000<2D<=per(F)`.
Thus

\[
N_M\le\frac{2\pi}{\theta}\,3(4w+1).
\]

Using `arctan x>=x/2` for `0<=x<=1` gives `theta>=1/(8L)`, hence

\[
N_M\le48\pi L(88L+1)
\le4248\pi L^2<5000\pi L^2.
\]

This proves the finite bound. QED.

### Corollary AC.7 — quantitative all-phase component count

Every sufficiently large canonical post-ZF C-II source satisfies

\[
\boxed{c_I=O(D^{2/3}).}
\]

**Proof.** The audited FSDB area lower bound implies
`area(F)>3D^2/5` for all sufficiently large survivors. The shared ambient-force
theorem puts the force hull inside the source circumdisk of radius
`D/2+3^(1/4)sqrt(D)`, which is at most `11D/20` for all large `D`.

For every unit direction `u`, the bounding rectangle gives
`area(F)<=D width_F(u)`, so `width_F(u)>3D/5`. With the circumcenter as zero,

\[
h_F(u)=\operatorname{width}_F(u)-h_F(-u)
>3D/5-11D/20=D/20.
\]

Thus `F` contains the centered disk of radius `D/20`, and AC.6 applies.
The exact diameter budget at the end of Section 4 yields, for every `M>=1`,

\[
\boxed{
c_I\le5000\pi(M+2)^2+\frac{2+2\pi D}{M+1}.}
\]

Taking `M=floor(D^(1/3))` proves the stated order bound. This step uses the
finite uniform AC.6 estimate, not the nonuniform fixed-cutoff limit AC.4.
QED.

## 6. Exact effect on the canonical quantities

Retain `k=d_H+s_Z` and the original definitions of every source/core object.
The canonical ZU and PC identities now imply the candidate asymptotic reductions

\[
\boxed{e_{BB}+s_C=q+k+O(D^{2/3}),}
\qquad
\boxed{a+k=c_B+s_C+O(D^{2/3}).}
\]

For the renormalized surplus this gives

\[
\boxed{\mu_D D=2q-e_{BB}-k+O(D^{2/3})
=q+s_C-2k+O(D^{2/3}).}
\]

For example, in the scoped subbranch `k=o(D)`, the audited DB lower bound
`liminf h/D >= 2rho`, `rho=cos rho`, and `q>=h` give

\[
\liminf\mu_D\ge2\rho>1.478.
\]

This is a lower bound, not a contradiction. It shows in particular that a
surplus sequence near the current `0.9604` frontier cannot have `k=o(D)`.
The general macroscopic-defect and high-surplus branches are not excluded.

Also, C37 gives at most `2c_I-2s` loaded vertices shared by multiple attachment
sets. Therefore only `O(D^(2/3))` loaded vertices belong to multiple components.
This does not make the separate component packings independently rearrangeable.

## 7. Dependency and regression audit

| Claim/input | Lifecycle and exact use |
| --- | --- |
| C26/C35/C36/C40 | Canonical active modules 01–04: degree, harmonic containment, attachment diameter, loaded incidence multiplicity |
| C-ZRF and ZK/ZU/PC | Canonical via module 57 and the PR #188 dependency audit: finite identities and `sum delta_r=O(D)` |
| FSDB | Canonical scoped derivation in the PR #188 audit, Sections 4 and 7: nondegenerate normalized force hull; no equality-uniqueness import |
| Ambient-force AG | Canonical shared module `docs/theory/04-ambient-force-and-cap-transport.md`: circumradius used in AC.7 |
| AC.1–AC.7 | Proved candidate awaiting independent audit/promotion; not canonical |
| C-II exclusion | Not proved |

Checks against binding regressions:

- **Contact isolates:** retained in the full source, never counted as `I_r`.
  No bound on `n-v` or permission to discard isolates is inferred.
- **Near-chain vertices:** two directions cannot support three separated unit
  neighbors in a strip thinner than `1/2`; the near-chain regressions include
  an additional contact direction outside such a strip. They do not contradict
  AC.1. No positive lower bound on the turning of a selected two-edge path is
  claimed.
- **Odd shells and the q=13 S1 regression:** with no unloaded component the
  result is vacuous. It says nothing about finite/global shell optimality.
- **Corner limits:** expressly allowed. Only their neighborhoods can support
  bounded components in the limit, and their number is handled separately.
- **Cyclic inward pockets:** not bounded by an exterior cap; neither
  `b-P_F=o(D)` nor `H_out=o(D^2)` is used or concluded.
- **Eppstein equality:** no near-quadrangulation claim is made.
- **KKT weights:** no individual weight or conductance has a uniform floor.
- **Simultaneous moves:** no movement of cells or source points is asserted.

## 8. What remains: one exact closing obligation

The new reduction removes a linear cloud of bounded unloaded components from
both Woodall branches. It does not control the source population in inward
pockets, exceptional faces, or outside the force hull.

One precise sufficient next theorem is still the full-source cell-slack
inequality. In the notation of the independently audited FSCS scope, let
`a0=sqrt(3)/2`, `c0=a0/2`, `K=conv A`,

\[
\delta_K=\pi D^2/4-\operatorname{area}K,\qquad
L=P_F-P_{com}-k_{cap},
\]

and let `W` be the sum of dimensional Oler slacks of **all** augmented contact
cells and exterior caps, including their isolated source populations. Prove

\[
\boxed{\delta_K+W\ge c_0P_K+a_0L}
\]

for the reduced class `c_I=O(D^(2/3))`. The strict global lattice comparison gives
the opposite strict inequality, so this would close the full-source gate.
Here `k_cap` counts exterior caps and is unrelated to `k=d_H+s_Z` above.

Nothing in AC.4–AC.7 proves this boundary-order inequality. In particular,
sublinear component count does not imply sublinear total component diameter
or subquadratic component area.

## 9. Promotion and handoff

**Keep unreviewed pending an independent proof/dependency audit.** The state
lock and live prompt are intentionally unchanged. A later promotion must
perform the complete transaction in `docs/RESEARCH_WORKFLOW.md`.

The strongest new result is the all-phase candidate `c_I=O(D^(2/3))`, with
the uniform finite estimate `N_M<=5000pi(M+2)^2`. The exact remaining task is
the full-source slack inequality above, not another near-zero-transfer audit
or a shell-only PSD calculation.
