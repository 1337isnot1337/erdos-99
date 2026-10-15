<!-- theorem-state: {"artifact_id":"ART-BD46025B6F5E","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C: diameter midpoint localization from support energy

```text
full-source area allowance -> cubic control of completion support derivatives
-> every actual diameter midpoint is O(D^(2/3)) from one source circumcenter
-> uniform coordinate-response and reciprocal-force bounds
-> still requires source-specific finite feasibility or a contact/face payment.
```

Date: 2026-10-02.
Starting checkout: `7b3fd8e2ad15532c0d40b761da381ac7d5c36074`.
Fetched research base / starting branch HEAD:
`fbeae9b3fa18a63e07573676b4e2e512a91ca4d5`.
State version: `2026-09-14.audit.51`.
Branch: `swarm/sol/source-stress-geometry-20261002`.
Mission: strengthen actual-source diameter localization, then test its transport
to a closing response estimate. No individual assignment or coordination issue
was present in the fetched GitHub state. Existing threshold, reaction, and
curvature PRs #615--620 were inspected to avoid repeating their main claims.
Classification: **proved candidate awaiting independent audit and promotion**;
artifact lifecycle **unreviewed**. The failed stronger implications below are
**regressions**. Level I and C-II remain **OPEN**.

## 1. Dependencies, scope, and prior results

Canonical inputs are:

- [Section 58](../targets/target-c/58-full-source-geometry-audit.md), §1:
  for the hull K of every unit-separated global minimizer,
  `delta_K=pi D^2/4-area(K)<(pi sqrt(3)/4)D`, and its circumradius and
  inradius satisfy `R_K-r_K<eta`, `eta=3^(1/4)sqrt(D)`.
- [Theory 01, Theorem 4.1](../theory/01-local-structure.md): normalized
  source KKT equilibrium, `sum beta=1`; and the canonical contact Dirichlet
  response identity in [Target C 01, §7](../targets/target-c/01-force-hull-and-shear.md).

The only literature import is existence of a planar constant-width-D completion
containing a diameter-D set. The original Kupitz--Martini--Wegner paper,
*A Linear-Time Construction of Reuleaux Polygons*, Beitr. Algebra Geom. 37
(1996), 415--427, explicitly states this general existence result on p. 421,
in the proof of Theorem 0.1, citing its reference [5], Theorem 54, p. 126.
[Original paper](https://emis.de/ft/11518). Its separate uniqueness theorem
requires a Hamiltonian diameter graph and is not used.

The support-area identity and Fourier inequalities used below are proved here.
PR #615's additive star budget and PR #620's harmonic-component windows use
related support energy; their unpromoted theorems are not premises. The new
quantity here is the midpoint of **every actual diameter**, including a diameter
whose two endpoints have degree one. A star-aperture bound alone does not
control that quantity. The older canonical midpoint estimate FS.6 is
`O(D^(3/4))`; its coordinate-response error FS.8 is `O(D^(-1/4))`.

The finite geometric theorem below requires neither unit separation nor global
optimality. Its minimizer applications use the complete source hull K, retaining
all contact isolates. No full-source affine-kernel claim is made.

## 2. Support energy and a cubic derivative bound

Let W be any constant-width-D completion of K, put R=D/2, and take its Steiner
point s as origin. Equivalently s removes the first cosine and sine harmonics
from the support function. Write

`h(theta)=R+f(theta)`, with `f(theta+pi)=-f(theta)`.

The curvature measure `rho=h+h''` is nonnegative. Constant width gives
`rho(theta)+rho(theta+pi)=D` as measures, so both measures are absolutely
continuous and `0<=rho<=D` almost everywhere. Thus `h` is in `W^(2,infinity)`;
in particular its first derivative is continuous and Lipschitz. Corners cause
zero curvature intervals rather than an omitted singular term.

The unique support point with normal `n=(cos theta,sin theta)` is

`x(theta)=s+h(theta)n+h'(theta)Jn`.

Integrating the signed boundary area, then integrating `h h''` by parts, gives

\[
 \delta_W:=\pi D^2/4-\operatorname{area}W
 =\frac12\int_0^{2\pi}(f'^2-f^2).                    \tag{ME.1}
\]

Only odd Fourier modes k>=3 remain. If their real coefficients are a_k,b_k,
Parseval gives

\[
 \delta_W=\frac\pi2\sum_{k\ge3\text{ odd}}
 (k^2-1)(a_k^2+b_k^2),\qquad
 \int f'^2\le\frac94\delta_W.                      \tag{ME.2}
\]

At any theta, Cauchy--Schwarz in this series and the telescoping identity

`sum_(k>=3 odd) 1/(k^2-1)=sum_(j>=1) 1/(4j(j+1))=1/4`

give

\[
 \|f\|_\infty\le F_W:=\sqrt{\delta_W/(2\pi)}.        \tag{ME.3}
\]

The weighted Cauchy--Schwarz estimate also proves absolute uniform convergence,
so point evaluation of the Fourier series is legitimate. Since
`f''=rho-R-f`, its Lipschitz constant is at most `L_W=R+F_W`.

Put `T=||f'||_infty`. A point attaining T has an antipodal point attaining
its negative, because f' is antiperiodic. Their distance is pi, so
`T<=pi L_W/2`. The two Lipschitz tents of height T and half-width T/L_W
centered at these points have disjoint interiors. Hence

\[
 \int_0^{2\pi}f'^2\ge\frac{4T^3}{3L_W},\qquad
 T^3\le\frac{27}{16}L_W\delta_W.                   \tag{ME.4}
\]

This is a uniform finite inequality, not a numerical observation.

## 3. Every actual diameter midpoint

For a finite planar source A of diameter D, set

\[
 \delta=\pi D^2/4-\operatorname{area}(\operatorname{conv}A),\quad
 F=\sqrt{\delta/(2\pi)},\quad L=D/2+F,
 \quad B=\sqrt{F^2+\left(27L\delta/16\right)^{2/3}}.    \tag{ME.5}
\]

### Theorem ME.1

There is one point s, the Steiner point of any chosen completion, such that
every actual source diameter pq satisfies

\[
 \left|\frac{p+q}{2}-s\right|\le B.                 \tag{ME.6}
\]

**Proof.** Let `n=(p-q)/D`. For every x in W, `|x-q|<=D`, so

`n.(x-p)<=-|x-p|^2/(2D)`.

Thus p is the unique support point with normal n, and q is the unique support
point with normal -n. Antiperiodicity in the boundary formula gives

\[
 \frac{p+q}{2}-s=f(\theta)n+f'(\theta)Jn.           \tag{ME.7}
\]

Apply (ME.3)--(ME.4), and use `delta_W<=delta` since `K subset W`.
All functions defining F,L,B are increasing in the deficit. This proves (ME.6).
It also proves that the chosen completion and its midpoint curve are auxiliary
objects; the constrained pairs in (ME.6) are the original source pairs. ∎

### Corollary ME.2: every global minimizer, with its own circumcenter

For every unit-separated global minimizer with D>=1,

\[
 B<\tfrac32 D^{2/3}.                               \tag{ME.8}
\]

Indeed `F<sqrt(sqrt(3)/8)sqrt(D)<sqrt(D)/2`, hence `L<D`.
The cube-root term in (ME.5) is smaller than `(4/3)D^(2/3)` because
`27 pi sqrt(3)/64<64/27`. Thus `B^2<(1/4+16/9)D^(4/3)<(9/4)D^(4/3)`.

Let o be a circumcenter of the **full source** hull, and j an incenter.
Canonical Bonnesen geometry gives `|j-o|<=R_K-r_K<eta` and
`r_K>D/2-eta`. Since `W subset B(s,D/2+F)` and contains the inball,

`|j-s|+r_K<=D/2+F`, and therefore `|s-o|<F+2eta`.

Consequently every actual diameter midpoint obeys

\[
 \boxed{\left|\frac{p+q}{2}-o\right|<B+F+2\eta
 <\frac{14}{3}D^{2/3}<5D^{2/3}.}                    \tag{ME.9}
\]

Here `3^(1/4)<4/3` and `sqrt(D)<=D^(2/3)` for D>=1. The theorem is
uniform over every global minimizer; contact or diameter minimization is not
required. It improves FS.6's exponent, without proving a new diameter decrease.

## 4. Transport to every normalized KKT stress

For a normalized stress let `s_b=sum_k beta_bk>0` and
`g_b=sum_k beta_bk(p_b-p_k)`, on its positive diameter endpoints. Then
`sum_b s_b=2`. The original source midpoint identity gives

\[
 |g_b-2s_b(p_b-s)|\le2s_bB,\qquad
 \sum_b|g_b-2s_b(p_b-s)|\le4B<6D^{2/3}.             \tag{ME.10}
\]

For its actual contact Dirichlet response, let `X_b=(p_b-s)/D`.
The exact harmonic coordinate identity is `Lambda X=g/D`. Thus

\[
 \boxed{\sum_b|(\Lambda X-2\operatorname{diag}(s_b)X)_b|
 \le4B/D<6D^{-1/3}.}                               \tag{ME.11}
\]

The response acts only on its positive contact core, with grounded unloaded
vertices. Isolated source coordinates stay in the full source constraints;
they are not inserted into its affine kernel.

There is also a stronger norm-of-force estimate. Define

`V_b=sum_(k<l) beta_bk beta_bl |p_k-p_l|^2`.

All partners of b lie in the radius-2B ball centered at `2s-p_b`. Their
beta-normalized variance is at most `4B^2`; hence

\[
 \sum_b V_b/s_b\le8B^2<18D^{4/3}.                  \tag{ME.12}
\]

The exact identity `|g_b|^2=D^2s_b^2-V_b` yields, with `P_*=sum_b|g_b|`,

\[
 \boxed{0\le2D-P_*\le D^{-1}\sum_bV_b/s_b
 \le8B^2/D<18D^{1/3}.}                             \tag{ME.13}
\]

This improves the canonical `O(sqrt(D))` reciprocal perimeter error uniformly
over all normalized stresses, without a lower bound on any individual weight.
The same partner ball gives `d_Haus(F_s-s,-(F_s-s))<=2B` for every selected
force hull F_s. Pairwise partner distance at most 4B also gives a vanishing
`O(D^(-1/3))` diameter-star aperture. The latter exponent was already obtained
by the unpromoted cubic star argument; it is a consequence, not a new claim of
priority here.

## 5. Exact computation

The [certificate](../../research/verify_full_source_midpoint_energy_2026_10_02.py)
checks the finite Fourier coefficient/telescoping identities, the two-tent
integral, the explicit minimizer constants, rational support-bump integrals,
and exact partner-variance / stress identities. General completion existence,
convex support geometry, and the analytic Fourier passage are the proofs above,
not conclusions of the finite computation. Its scope and omissions are also
recorded in [research/README](../../research/README.md).

## 6. Frontier boundary

The new input is uniform actual-diameter localization at a smaller scale, plus
uniform response-coordinate and force-dispersion estimates. Neither (ME.11)
nor a small midpoint disk is an operator estimate or a simultaneous finite
contact-preserving competitor. The next attempted implications and their
regressions are recorded in the follow-up sections.

The open-cell and threshold exact-phase branches, nonconstant-phase swaps,
split-star O--O, inactive interfaces, higher-surplus full core, and macroscopic
inactive-container/exterior-cap branch all remain unresolved. No canonical
state, prompt, theorem graph, or certificate registration is changed.

## 7. Next attack: can geometry alone reduce the midpoint scale to sqrt(D)?

It cannot. The following analytic construction has strict separation, a complete
actual diameter graph, and hull deficit within the canonical numerical allowance.
It has linear population and no asserted global optimality or KKT stress.

Take `D=q^3`, `q>=8`, `R=D/2`, `a=1/q`, and

\[
 \phi(t)=(1-t^2)^2/16\quad(-1\le t\le1).
\]

Define `f(theta)=Ra^2 phi(theta/a)` for `|theta|<=a`, its negative
antipodal copy on `|theta-pi|<=a`, and zero elsewhere. Extend periodically.
The support `h=R+f` is C^(1,1). Since `0<=phi<=1/16` and
`-1/4<=phi''<=1/2`, its curvature obeys

\[
 7R/16\le h+h''\le25R/16.                          \tag{ME.14}
\]

Thus h defines a strictly convex constant-width-D body W. It need not be
translated to its Steiner point for this construction. Direct polynomial
integration gives

\[
 \int\phi=1/15,\quad\int\phi^2=1/315,
 \quad\int\phi'^2=1/105,
 \quad\delta_W=D/420-D^{1/3}/1260.                  \tag{ME.15}
\]

The first-harmonic translation has size at most `2Ra^3/(15pi)=1/(15pi)`.
At `theta=a/2`, the actual antipodal support pair has midpoint m with

\[
 f=9q/512,\quad f'=-3q^2/64,\quad |m|\ge3q^2/64.  \tag{ME.16}
\]

Thus the midpoint is Omega(D^(2/3)) from the Steiner point, even though the
completion's radial support error is only O(D^(1/3)). The first-harmonic
translation cannot absorb it.

### A finite unit-separated source retaining that diameter

Let `k=ceil(pi R/6)`, start the normal mesh at `a/2`, and select the
`2k` boundary support points at angles `a/2+j pi/k`, `0<=j<2k`.
Both endpoints in (ME.16) are selected. The normal spacing `v=pi/k`
satisfies `5/R<=v<=6/R`, because R>=30/pi.

For any two selected points let Delta<=pi be their smaller normal separation.
The chord's projection along the midpoint tangent is at least

`2 rho_min sin(Delta/2)>=2(7R/16) Delta/pi>=35/(8pi)>1`.

This follows by integrating `dx=rho Jn dtheta` along the corresponding minor
normal arc; its midpoint-tangent projection is nonnegative throughout.
Hence **every pair is strictly farther than one**. The source is triangle-free,
retains the diameter D, and has `2k=Theta(D)` points. Its diameter graph is
exactly the antipodal matching: positive curvature gives one normal per boundary
point, and every length-D pair must have opposite support normals. All diameter
vertices have degree one, so a star-aperture budget supplies no midpoint bound.

For an arc with normal width v and arclength ell, the area between that arc
and its closing chord is at most `v ell^2/4`. Indeed its double-integral
formula is `1/2 int_(t<s) sin(theta(s)-theta(t)) dt ds`, bounded by
`v ell^2/4`. Since `ell<=rho_max v`, summing the `2k` arcs gives

\[
 \operatorname{area}W-\operatorname{area}K
 \le\frac\pi2\rho_{\max}^2v^2\le5625\pi/128.        \tag{ME.17}
\]

In addition every normal is within v of a selected mesh normal. The support
loss is at most `rho_max v^2/2<=225/(8R)`, by integrating
`rho(t) sin(theta-t)` from the selected support point. Put `F_0=Ra^2/16=q/32`.
The source hull therefore contains the centered disk of radius
`R-F_0-225/(8R)` and lies in the centered disk of radius `R+F_0`.
Its actual circumcenter o obeys

\[
 |o|\le2F_0+225/(8R)=q/16+225/(4q^3).               \tag{ME.18}
\]

Combining (ME.16) and (ME.18), for q>=8,

\[
 \boxed{|m-o|\ge q^2/32=D^{2/3}/32.}              \tag{ME.19}
\]

Also `delta_K<=delta_W+5625pi/128<D` for q>=8, smaller than
the canonical allowance `(pi sqrt(3)/4)D`. This proves that the exponent
2/3 cannot be improved using that allowance, diameter geometry and source
separation alone. Because all distances are strictly greater than one, uniform
rescaling explicitly improves its diameter. It is **not** a global minimizer.
The example does not rule out a stronger theorem using actual quadratic
population or positive source equilibrium.

## 8. Next attack: can improved radial coordinates control the response operator?

The implication is false even with full positive vertex equilibrium and PSD
stress with precisely the affine kernel. This refines the existing regular-shell
regressions; their general mechanism is not presented as new.

Take the regular unit odd q-gon, `q>=7`, put `t=pi/(2q)`, and retain all
actual contacts and diameters. Its circumradius and diameter are

`R=1/(2sin(2t))`, `D=1/(2sin t)`.

There are q contact sides and q actual diameters of step `(q-1)/2`.
Assign `alpha=D^2/q` to every contact and `beta=1/q` to every diameter.
These strictly positive weights give full vertex equilibrium, since both
Laplacians act on coordinate modes with the same eigenvalue
`4cos^2(t)/q`. Their scalar stress is PSD with kernel exactly
`span{1,P_x,P_y}`. To check the latter claim in every mode `1<=j<=q-1`,
multiply its eigenvalue by q/4. The required inequality is

\[
 \frac{\sin^2(2jt)}{4\sin^2t}
 \ge\sin^2(j\pi/2-jt).                             \tag{ME.20}
\]

For j even its difference is
`sin^2(jt)[cos^2(jt)/sin^2(t)-1]>=0`, with equality only j=q-1.
For j odd it is
`cos^2(jt)[sin^2(jt)/sin^2(t)-1]>=0`, with equality only j=1.
This proves the complete PSD and kernel assertion analytically.

Every source point is loaded; its contact response is simply `Lambda=L_C`.
Let `S=diag(s_b)=(2/q)I` and `X=P/D`. Then

\[
 \sum_b|(\Lambda X-2SX)_b|
 =2\sin^2t/\cos t<10/q^2,                          \tag{ME.21}
\]

while on the high-frequency mode j=(q-1)/2,

\[
 \boxed{\|\Lambda-2S\|_{\rm op}
 \ge(\cot^2t-4)/q>q/4.}                            \tag{ME.22}
\]

For the last bound, `sin t<=t`, `cos t>=1-t^2/2`, and `pi^2<10`
give `(cot^2t-4)/q>=4q/pi^2-5/q>q/4` for q>=7.
All actual diameter midpoints are at distance `1/(4cos t)<1/2` from the
circumcenter. Thus even O(1) midpoint localization and a faster coordinate
residual do not bound the operator on nonaffine data.

The shell's population is q=Theta(D), not the global quadratic population.
These shells are nonglobal for large q. They reject the proposed transport from
midpoints/coordinate response plus stress alone, not a theorem retaining the
actual complete O--O extraction or Erdős's quantifiers. No inference from an
Euler trail, a selected forest to the full diameter graph, or a dropped isolate
is involved.

## 9. Current implication chain and exact remaining gap

The smaller midpoint scale is a new actual-source input to any cut, force,
or finite-motion proof. Its direct transport to force dispersion succeeds in
(ME.10)--(ME.13). The next attempts above fail at exact geometric and spectral
steps: the area allowance admits cubic-scale transverse midpoint excursions,
and two affine response columns leave the nonaffine response uncontrolled.

A closing use therefore needs a **source-specific bound on the nonaffine
response or a feasible finite move on the same actual train source**. It must
use the actual complete two-shore cutsets, positive equilibrium, and every
inactive pair; midpoint localization alone supplies none of those constraints.
An unreviewed strengthening does not eliminate any surviving global branch.

Repository refresh before publication found new main
`50d9ad56682985b744fd1dbc04f5019c4e81d8e9`; the state manifest, STATE,
Target C route map, and CURRENT file are identical to the research base.
The merged star-energy report remains unpromoted and is not a new premise.
The concurrent PR #621 correction-mass packet was inspected for its scope:
it still requires actual vertex/face co-embedding and does not close the
threshold branch. No result from it is imported here.

Executed validation: the exact verifier passed 1000 finite Fourier sums,
100 antipodal tents, 2001 rational bump samples, 993 bump scales,
40 midpoint/variance packets and 62748 shell-mode parity checks.
Python compilation, five local report links, staged whitespace checks, and
the theorem-state checker with the research base passed. The latter used an
isolated Python environment with the repository's declared checker dependencies.
These checks do not certify mathematical promotion or global optimality.

Promotion recommendation: independently audit (ME.1)--(ME.13), especially the
antipodal tents and the comparison of completion and full-source centers.
Then use the complete promotion transaction if accepted. The bounded arithmetic
checks are corroboration, not a substitute for that proof audit.
