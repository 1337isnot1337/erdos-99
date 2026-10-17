> Generated reading edition · [exact source](../../../docs/audits/target_c_atomic_orbit_sharp_detour_independent_audit_2026-10-08.md) · source SHA-256 `7f32b7a8d71883dbe56517e96a0c2286444ad41a3cd9bda5b3f85c6420488211`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-25A2E49DD194","canonical":true,"claim_ids":["C-ATOMIC-ORBIT-SHARP-DETOUR","C-ATOMIC-ORBIT-TRAIN-OBSTRUCTION"],"claim_statuses":{"C-ATOMIC-ORBIT-SHARP-DETOUR":"canonical","C-ATOMIC-ORBIT-TRAIN-OBSTRUCTION":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C Audit.132 — sharp atomic-orbit detour

Date: 2026-10-08
Audit base: `origin/main=a08455236c323c89ef422146055e59c40b324174`, state `2026-10-08.audit.131` (the audit.131 promotion commit is its second parent)
Source snapshot: `origin/research/target-c-atomic-boundary-audit-20261004` at `9d51e2120d36ba60161975d0de6e9c77786a1c53`
Classification: independently reconstructed theorem and source obstruction; **PASS — promote**.
Scope audited: sharp measure Theorem 1 and the limiting-source inequality (13) of `docs/reports/target_c_sharp_orbit_endpoint_detour_2026-10-04.md`. No endpoint-orbit lower bound or C-II closure is claimed.

Frozen source hashes: companion report `25f88179926f1ee57b796429ea1a320ca8d1bfa471979d698f2aff2edaf1f3dd`; verifier `e4d1066e3cfd96e074a50f8780b3614ffb6da1bc3753401adb3f301251adee04`.

## Exact claims

Let `mu` be a finite positive measure on the projective direction circle, of mass
`M=pi+lambda`, satisfying
$$
\int |\cos(\theta-\alpha)|\,d\mu(\theta)\ge2
\quad\text{for every }\alpha.
$$
For one orbit `O={theta_0,theta_0+pi/3,theta_0+2pi/3}` let `A=mu(O)`. Then
$$
\boxed{\lambda\ge\Phi(A),}
$$
where
$$
\Phi(A)=
\begin{cases}
2A-12\arctan(A/6),&0\le A\le6\tan(\pi/12),\\
3-\pi+(1-\sqrt3/2)A,&6\tan(\pi/12)\le A\le2\sqrt3,\\
A-\pi,&A\ge2\sqrt3.
\end{cases}
$$
The bound is sharp for every `A>=0`; `Phi` is continuous, strictly increasing,
and convex, with `Phi(A)=A^3/54+O(A^5)` at zero.

Integrating the width constraints over the projective circle gives
`2M>=2pi`, so `lambda>=0` and `Phi^{-1}(lambda)` is defined.

For any canonical Type-II source limit, let `mu_out` be the limiting normalized
occurrence-counted outer-walk direction measure, let
`lambda=lim (b-p)/D`, `t=lim (q-k)/D`, and
`J=lim (Q+4f)/D`, after taking a joint convergent subsequence. Then the
canonical crossing/endpoint budgets imply the necessary inequality
$$
\boxed{4s_2\le\sqrt{(\pi+\lambda)\Phi^{-1}(\lambda)}+J
\le\sqrt{(\pi+\lambda)\Phi^{-1}(\lambda)}+5(2t-\pi-\lambda),}
$$
where `s_2=sqrt(pi/(2sqrt(3)))`. The final inequality is the source obstruction;
it neither forces a large orbit nor supplies a source deformation.

## Canonical inputs for the source consequence

- The general measure theorem above is independent of packing assumptions.
- `C-ATOMIC-TRACK-BOUNDARY-COST`, `C-RHOMBUS-POP`, `C-PUNCTURED-PHASE`, and
  `C-TRAIN-INTERFACE-CURRENCY` give the limiting crossing mass
  `Delta_2=pi/(2sqrt(3))`, confinement of crossing mass to the
  `+/-pi/3` direction relation, and simple triangle-free actual track graphs.
- `C-LOADED-HULL` and `C-FULLCORE-NEAR-DISK` give the actual loaded-hull disk
  limit, `p/D->pi`, the full occurrence-counted outer walk, and
  `b+Q=2(q-k)`.
- The finite-neighborhood Mantel argument is the one reconstructed in Audit.129;
  no collapsed graph on three phase labels is assumed triangle-free.

All cited inputs are canonical on the proposed Audit.131 base. Contact-isolated
source points remain in the full-source Type-II hypotheses.

## Independent measure reconstruction

Average `mu` over the three rotations by `pi/3` on the projective circle and
reflection about `theta_0`. This preserves its mass and every width constraint.
It preserves the selected orbit mass `A` and assigns `a=A/3` to each of its
three directions. No direction outside the selected orbit is mapped into it.
The case `A=0` follows from `lambda>=0`; assume `A>0` for the face geometry.

The support function
$$
h(\alpha)=\tfrac12\int|\cos(\theta-\alpha)|\,d\mu(\theta)
$$
is the support function of a centrally symmetric planar zonoid `Z`. The
constraints give `h>=1`, hence `B_1 subset Z`. Cauchy's perimeter formula gives
`per(Z)=2M`. A projective atom of mass `a` creates opposite parallel faces of
length `a`; the imposed symmetries therefore give six equally spaced faces of
length `a`, all at a common support distance `H>=1`, centered on their face
normals.

For the face with normal `(1,0)`, the endpoints are `(H,+/-a/2)`. The adjacent
face endpoint must lie in the supporting half-plane `x<=H`, so
$$
H/2+\sqrt3a/4\le H,
\qquad H\ge\sqrt3a/2.
$$
Thus `H>=H_0=max(1,sqrt(3)a/2)`. Let `K_H` be the convex hull of the unit disk
and all twelve face endpoints. On a 60-degree symmetry sector, its support is
the maximum of `1` and the two endpoint supports
`H cos(psi)+(a/2)sin(psi)` and
`H cos(pi/3-psi)+(a/2)sin(pi/3-psi)`. To see that these are the only endpoint
terms needed, put `beta=atan(a/(2H))<=pi/6`; all endpoint vectors have the same
radius and polar angles `j*pi/3+/-beta`. In `psi in [0,pi/6]`, the nearest
endpoint angles are `beta` and `pi/3-beta`; all others give no larger dot
product. Their coefficients of H are positive; hence `K_H` expands
with H, `Z` contains `K_H`, and
$$
\operatorname{per}(Z)\ge\operatorname{per}(K_H)
\ge\operatorname{per}(K_{H_0}).
$$

The perimeter of the minimal body is determined directly by its boundary:

1. If `a<=2 tan(pi/12)`, then `H_0=1` and
   `beta=atan(a/2)<=pi/12`. Each of the six sectors contributes straight
   length `2a` and unit-circle arc length `pi/3-4 beta`, so
   `per(K_1)=2pi+12a-24 atan(a/2)`.
2. If `2 tan(pi/12)<=a<=2/sqrt(3)`, then `H_0=1` and no unit-circle arc
   remains. The six face edges have length `a`; the six connectors have length
   `1-sqrt(3)a/2` and supporting-line distance `sqrt(3)/2+a/4>=1`. Thus
   `per(K_1)=6a+6(1-sqrt(3)a/2)`.
3. If `a>=2/sqrt(3)`, then `H_0=sqrt(3)a/2`; neighboring endpoints coincide
   and `K_{H_0}` is the regular hexagon of side a, with perimeter `6a`.

Since `A=3a` and `lambda=per(Z)/2-pi`, the three formulas give respectively
`6a-12 atan(a/2)=2A-12 atan(A/6)`,
`3-pi+(1-sqrt(3)/2)A`, and `A-pi`; these are exactly the branches of `Phi`.
For sharpness, each `K_{H_0}` contains the unit disk and is a centrally
symmetric zonoid. More directly, its distributional curvature measure
`h+h''` is nonnegative and antipodally symmetric; after rotating normals to
segment directions, the kernel identity
`(|cos|/2)''+|cos|/2=delta` on the projective circle gives a positive
generating measure. Its mass is
`per(K_{H_0})/2`, has selected orbit mass `3a=A`, and satisfies the width
constraint because its support function is at least one. Thus equality is
attained in every branch. The first derivative is
`2A^2/(36+A^2)` on the first branch and matches the middle slope
`1-sqrt(3)/2` at `6 tan(pi/12)`; at `2sqrt(3)` the slope jumps to one.
This proves continuity, strict increase, and convexity. The Taylor expansion
of the first branch gives `A^3/54+O(A^5)`.

## Transfer and orbitwise crossing-budget reconstruction

For a fixed subsequential outer-walk limit, its total mass is
`lim b/D=pi+lambda`, since `p/D->pi`. Each outer-walk edge has length one.
For every projection direction, the total variation around the closed walk is
at least twice the width of the loaded hull: the walk visits its loaded extreme
vertices and returns to its start. The scaled loaded hull tends to the unit
diameter disk, so every limiting projection variation is at least two. Hence
`mu_out` satisfies the sharp measure theorem. If `A_r` is the outer terminal
track-end mass in a three-direction orbit, it is no greater than that orbit's
full outer-walk mass; monotonicity of `Phi` therefore gives
`A_r<=Phi^{-1}(lambda)`. Also `sum_r A_r<=pi+lambda`.

Let `m_r` be the atomic track mass in orbit r, and `J_r` the exceptional-face
terminal mass there. Each track has two terminal occurrences, so
`2m_r<=A_r+J_r`, with `sum_r J_r<=J`. Every limiting crossing pair is atomic
and its two directions lie in the same orbit under addition by `pi/3`. For any
finite family of those orbits, freeze disjoint neighborhoods of their direction
atoms and apply Mantel to the induced finite **physical** track-crossing graphs.
The graphs are triangle-free; singleton or otherwise unused vertices do not
change that. Passing to the limit and exhausting the orbit family gives
$$
\Delta_2\le\sum_r m_r^2/4.
$$
No quotient graph on the three orbit labels is used.

The inequalities above imply
$$
4\sqrt{\Delta_2}\le2\|m\|_2
\le\|A+J_\bullet\|_2
\le\|A\|_2+\|J_\bullet\|_2
\le\sqrt{(\pi+\lambda)\Phi^{-1}(\lambda)}+J,
$$
where `J_bullet=(J_r)` and `||J_bullet||_2<=sum J_r<=J`. Since
`Delta_2=s_2^2`, this is the first source inequality. Finally,
`Q/D=2t-(pi+lambda)` by Section 63, and `f<=Q`, so
`J=(Q+4f)/D<=5(2t-pi-lambda)`. This proves the stated necessary source
obstruction.

## Verifier scope, regressions, and disposition

The frozen verifier was inspected and rerun. It checks 12 rational constant
claims (including the endpoint value `Phi(2)=5-pi-sqrt(3)`), exact
`Q(sqrt(3))` pair geometry for the collapsed-phase regression, and 462 exact
support comparisons for selected body parameters/directions. These checks do
not establish the continuous support maximization or all three perimeter
formulas; those are proved analytically above. The collapsed-phase matching
regression refutes only an invalid graph-quotient inference and does not affect
finite-neighborhood Mantel on actual track graphs.

**PASS — promote `C-ATOMIC-ORBIT-SHARP-DETOUR` and
`C-ATOMIC-ORBIT-TRAIN-OBSTRUCTION`.** The result supplies a sharp per-orbit
detour function and an all-limit functional constraint, but no theorem forces
an outer endpoint orbit to have mass two (or any other positive amount).
Therefore the linear loaded-hull spacing escape and C-II remain open. Type I
and Level I are unchanged.

Promotion transaction: PR #814 merged as
`8440641068c20a58c2f0a83679773f5303351d3a` on 2026-10-08, from head
`19b88c9442cb7e398fffe30d7aa620811c8c6eaf`. The current theorem state
registers both promoted claims. This merge/provenance record was checked
again during the 2026-10-15 preservation reconciliation; it does not assert
that expired historical hosted checks were rerun or supply human peer review.
