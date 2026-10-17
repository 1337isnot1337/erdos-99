> Generated reading edition · [exact source](../../../docs/audits/target_c_atomic_one_end_train_boundary_independent_audit_2026-10-08.md) · source SHA-256 `4501c5afc2eaaafe0f76cc636126db37d5a379115161802289be5a94544f0493`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-6D2203BA18D3","canonical":true,"claim_ids":["C-ATOMIC-ONE-END-TRAIN-BOUNDARY"],"claim_statuses":{"C-ATOMIC-ONE-END-TRAIN-BOUNDARY":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C Audit.131 — one-ended train boundary budget

Date: 2026-10-08  
Audit base: `origin/main=2cfa44ede117adac592fbe26351fd3e546969879`, state `2026-10-08.audit.130` (the audit.130 promotion commit is its second parent)  
Source snapshot: `origin/research/target-c-atomic-boundary-audit-20261004` at `9d51e2120d36ba60161975d0de6e9c77786a1c53`  
Classification: independently reconstructed theorem; **PASS — promote**.  
Scope audited: Theorem C, Section 10 only, of `docs/reports/target_c_atomic_boundary_capacity_audit_2026-10-04.md`. The companion sharp-orbit endpoint theorem remains unreviewed.

Frozen source hashes: report `e79dbcfcefcd7a65851e2f7e2307fede023f8860656f0b8979dec2d94b832b2f`; finite verifier `e4d1066e3cfd96e074a50f8780b3614ffb6da1bc3753401adb3f301251adee04`.

## Exact claim

For every unbounded canonical contact-minimal, then diameter-pair-minimal,
triangle-free global-source sequence in the Type-II branch, retain all source
points, including contact isolates. Use Section 63 notation: `q` loaded force-hull
vertices, `k=d_H+s_Z`, `Q` total nonquadrilateral-face excess, `f` the number of
bounded nonquadrilateral faces, `p` loaded-hull perimeter,
`g=p-q`, `z=b-p`, `x_B=b-q=g+z`, `m` nonunit loaded-hull sides, and
`u_B=x_B-m`. Put `s_2=sqrt(pi/(2sqrt(3)))`.

The exact one-ended train claim is
```math
\liminf_{D\to\infty}\frac{2f-k+m}{D}\ge 2s_2. \tag{1}
```
Using Section 63's exact identities, this gives
```math
\boxed{\liminf_{D\to\infty}
\frac{5(q-k)+2g-z-u_B}{D}\ge3\pi+2s_2.} \tag{2}
```
Therefore `x_B=o(D)` forces
```math
\liminf (q-k)/D\ge(3\pi+2s_2)/5
=2.26588071489945\ldots. \tag{3}
```
Combining (2) with Audit.130's outer-route bound, in the branch
`(q-k)/D<=1.860+o(1)`, gives
```math
g\ge\max\{(5\pi+4s_2-18.6)D+4z,
((3\pi+2s_2-9.3)D+z+u_B)/2\}-o(D),
```
and hence `q/D<=2.1268908663411...+o(1)`. This remains compatible with the
canonical lower bound on `q`; it is not a C-II contradiction.

## Canonical inputs

- `C-ATOMIC-TRACK-BOUNDARY-COST` supplies atomic mass at least `2s_2` in every
  fixed joint weak limit of normalized actual rhombus-track directions.
- `C-LOADED-HULL` supplies the exact Section 63 face/outer-walk identities,
  actual loaded-hull order, and `m<=x_B`.
- `C-FULLCORE-NEAR-DISK` gives `p/D->pi` and the disk limit; canonical Section
  67 gives `F=conv(B)=conv(V(G))`, so the complete rhombus complex lies in the
  actual loaded force hull and its vertices on the hull are precisely loaded
  vertices.
- `C-RHOMBUS-POP` and `C-TRAIN-INTERFACE-CURRENCY`, with Theory 01,
  Theorem 10.6, supply actual strict rhombi, simple complete tracks, and a
  simple triangle-free crossing graph.
- `C-ATOMIC-OUTER-ROUTE-EXPOSURE` is used only for the displayed combined
  low-`t_D` corollary, not for (1) or (2).

All inputs are canonical on this Audit.130 base. No report-only theorem,
scaffold, or deletion of contact-isolated source points is used.

## Independent reconstruction

Let `T_D` count the following complete trains in the contact complex:

1. every actual track of bounded strict unit rhombi; and
2. every unit contact edge incident with no rhombus, counted as a one-edge
   singleton train with its two facial terminal occurrences.

The exact endpoint handshake is
```math
2T_D=b+Q+4f=2(q-k)+4f,
\qquad T_D=q-k+2f. \tag{4}
```
For the first equality, count edge-side occurrences on the outer face and all
bounded nonquadrilateral faces. An edge bordering the rhombic complex contributes
one terminal occurrence of its actual track; an edge incident with no rhombus
contributes both occurrences of its singleton train. An edge between two rhombi is
internal and contributes neither. The count includes bridges and repeated facial
occurrences. The second equality is the canonical Section 63 identity
`b+Q=2(q-k)`.

Pass jointly to weak limits of the normalized measure `lambda_D` placing mass
`1/D` at the direction of each of these `T_D` trains, the actual-rhombus track
measure, and all scalar budgets. The rhombus-track measure is dominated by
`lambda_D`; the fixed-limit atomic-mass theorem above therefore gives total atomic
mass `a>=2s_2` for the limit `lambda` as well. Singleton trains are isolated in
the crossing graph and cannot reduce that lower bound.

There are exactly `q-m` unit sides of the loaded force hull. Put mass `1/D` at
each such side direction. Since each side has length at least one, this measure is
dominated by the perimeter-weighted tangent-direction measure of the loaded hull.
The loaded hull divided by `D` tends to a disk, so its tangent-direction measures
converge to an atomless uniform measure `mu` of total mass `pi`.

Every unit loaded-hull side is a terminal edge of exactly one complete train: it
belongs either to an actual rhombus track or to a singleton contact edge. At most
two actual rhombus tracks can have both terminal edges on the loaded hull. Indeed,
each such track is a simple centerline arc in the convex loaded hull, its terminal
edges are parallel and have opposite boundary orientations, and strict convex
turning makes the terminal-edge direction pairs of two distinct hull-to-hull
tracks distinct. The four boundary edges then alternate cyclically, so the two
centerlines cross. The physical crossing graph is triangle-free, hence it cannot
contain three pairwise crossing hull-to-hull tracks. A singleton has only one
loaded-hull edge and causes no duplicate. Thus among any `N` selected unit hull
sides, at least `N-2` belong to distinct complete trains.

Fix a finite set `A` of atoms of `lambda` and a small direction neighborhood `U`
of `A` with null boundary for both `lambda` and `mu`. At least
`q-m-D mu(U)-o(D)` unit hull sides have directions outside `U`, by the tangent
measure domination. They belong to at least `q-m-D mu(U)-o(D)-2` distinct
trains outside `U`. Consequently, using (4) and weak convergence,
```math
\lambda(U)\le\lim\frac{T_D-q+m}{D}+\mu(U).
```
Shrink `U` to `A`. Since `mu` is atomless, `lambda(A)` is at most the limit on the
right without the `mu(U)` term. Exhausting the countable atom set of `lambda` by
finite `A` gives
```math
a\le\lim\frac{T_D-q+m}{D}
=\lim\frac{2f-k+m}{D}. \tag{5}
```
Together with `a>=2s_2`, this proves (1) along any subsequence attaining the
finite liminf; an infinite liminf is immediate.

Since `Q>=f`, (1) implies
`liminf (2Q-k+m)/D>=2s_2`. Substituting
`Q=2(q-k)-b`, `b=p+z`, `m=g+z-u_B`, and `g=p-q` gives the exact identity
```math
2Q-k+m=5(q-k)-3p+2g-z-u_B.
```
Now `p/D->pi` proves (2). If `x_B=o(D)`, then `g,z,u_B=o(D)` because
`x_B=g+z` and `0<=u_B<=x_B`; (3) follows. The combined low-`t_D` consequence
uses only (2), Audit.130, and nonnegativity of `z,u_B`.

## Adversarial checks and verifier scope

- The side count is `q-m`, not `q`; nonunit loaded-hull sides are retained in the
  exact budget through `m`.
- Only the two-ended duplicate exception is charged. The result does not assume
  every rhombus train reaches the hull or that `m=o(D)`.
- Singleton edges are included in the exact train count, have no crossing edges,
  and can supply at most one distinct unit hull side each.
- The hull argument is applied to the actual force hull containing the positive
  core; it is not applied to a selected stress subgraph or an arbitrary pin set.
- Contact isolates remain in the source and in the full-source near-disk
  hypotheses. They are not incorrectly counted as rhombus or singleton trains.
- The frozen source verifier passed 12 rational constant checks, 1,677 exact
  quadratic-field pair checks, and 462 exact convex-support checks. It checks the
  constants and companion endpoint-body geometry; it does not encode the train
  endpoint count or prove the asymptotic theorem.

## Verdict and frontier effect

**PASS — promote `C-ATOMIC-ONE-END-TRAIN-BOUNDARY`.** The theorem independently
shows that an `o(D)` outer-walk excess cannot survive: it forces
`(q-k)/D>=2.2658807149-o(1)`. In the low-`t_D` range it strengthens the loaded
spacing requirement to `g/D>=1.0147017872-o(1)` and lowers the `q/D` ceiling to
`2.1268908664+o(1)`. The canonical lower bound on `q` remains below this ceiling,
so there is no contradiction, global competitor, C-II closure, or Level I result.
The next exact bridge remains an upper bound or strict-diameter improvement for the
linear loaded-hull spacing deficit.

Promotion transaction: PR #813 merged as `a08455236c323c89ef422146055e59c40b324174`, advancing state to `2026-10-08.audit.131`. Protected `state-consistency` check `37731866463` and post-main workflow `37732302033` both passed.
