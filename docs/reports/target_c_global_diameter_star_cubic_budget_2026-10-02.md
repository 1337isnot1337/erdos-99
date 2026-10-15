<!-- theorem-state: {"artifact_id":"ART-3B1ED5A18AE1","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — an additive cubic budget for every actual diameter star

```text
disjoint forced corner/arc intervals in a constant-width completion
-> sum_v (deg_H(v)-1)^3 = O(D^2) for the full actual source
-> every linear diameter-incidence packet has Omega(sqrt(D)) distinct carriers
-> threshold boundary-heavy staircase has Omega(sqrt(D)) carriers in one layer
-> still required: couple that actual carrier packet to contact/face currency
   or a strict same-cardinality competitor; all other C-II branches remain open.
```

**Date:** 2026-10-02.
**Starting checkout:** `78a65968d51af7871a0ce5a865bf2db1a2c2e0ec` (clean, detached).
**Research base after refreshing main:** `fbeae9b3fa18a63e07573676b4e2e512a91ca4d5`.
**State version:** `2026-09-14.audit.51`; unchanged between these commits.
**Branch:** `swarm/root/diameter-rail-convexity-20261002`.
**Mission:** source-wide diameter-rail geometry and aggregate star capacity.
**Classification:** proved candidate awaiting independent audit and promotion;
artifact lifecycle **unreviewed**. The body construction below is a **regression**
against improving the star exponent using the hull area allowance alone.
**Level I / C-II:** **OPEN**. No canonical promotion is made.
**Active prompt:** [current Target C continuation](../prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md).

## 1. Inputs and prior scope

The new universal result needs only the following inputs.

1. A finite planar unit-separated set `A`, its actual diameter `D`, and its
   **full actual** diameter graph `H`. All source points, including contact isolates,
   stay in `A`.
2. The planar completion theorem: a planar diameter-`D` set is contained in a
   convex body of constant width `D`. The exact statement was checked in
   Kupitz--Martini--Wegner, *A Linear-Time Construction of Reuleaux Polygons*,
   Beitr. Algebra Geom. 37 (1996), 415–427, p. 421, in the proof of Theorem 0.1.
   Their text explicitly invokes the general planar completion theorem, citing
   their reference [5], Theorem 54, p. 126. This is separate from their **unique**
   completion theorem, which requires a Hamiltonian diameter graph. We use
   existence only. [Original article](https://emis.de/ft/11518).
3. For a global minimizer, the canonical complete-source area allowance
   from [Section 58, §1](../targets/target-c/58-full-source-geometry-audit.md):
   with `K=conv(A)`,
   \[
   0\le\delta_K:=\pi D^2/4-\operatorname{area}K
   <{\pi\sqrt3\over4}D.                                      \tag{1}
   \]
   Its dependencies are finite Oler, strict translated-lattice comparison,
   and `per(K)<=pi D`. This premise is canonical and does not use C-I, ZR/ZF,
   a full-core hypothesis, or contact minimality.

The September 9 [cyclic cubic-corner report](target_c_cyclic_cubic_corner_deficit_2026-09-09.md)
already gives a pointwise cubic deficit and `O(D^(2/3))` degree bound on the
exact cyclic Reinhardt/Reuleaux endpoint. It is unreviewed, and its application
uses a special composition and area bridge. We reconstruct the support-energy
argument below and extend it to **all actual stars simultaneously**, in any
constant-width completion of any source. We do not claim that the cubic exponent
itself was first discovered in this run.

The threshold application is conditional on main's unpromoted
[paired staircase](target_c_exact_phase_threshold_paired_staircase_2026-10-01.md),
[physical forest lift](target_c_exact_phase_threshold_forest_lift_2026-10-01.md),
and [transverse rail saturation](target_c_exact_phase_threshold_transverse_rail_saturation_2026-10-01.md).
It does not import any of those reports as canonical premises. PR #613's
two populated rail hulls were inspected for scope; its results are not needed
for the universal theorem.

## 2. Forced normal intervals for actual source stars

Choose a constant-width-`D` body `W` containing `A`. Write its support function
as `h(theta)`, and put `R=D/2`, `p=h-R`. Thus

\[
p(\theta+\pi)=-p(\theta).                                   \tag{2}
\]

For a source vertex `v` with `d_v=deg_H(v)>=2`, let `theta_v` be the angular
span of its actual diameter-partner rays. These rays lie in one arc of length
at most `pi/3`: any two partners have distance at most `D`, so their angular
separation at `v` is at most `pi/3`. To see that the whole family is in one such
arc, fix one ray and lift the others to `[-pi/3,pi/3]`; the extremes of this
lift have difference at most `2pi/3<pi`, so their ordinary difference also has
to be at most `pi/3`.

For any diameter partner `q`, the direction `n=(v-q)/D` supports `W` at `v`.
Indeed for every `x` in `W`, `|x-q|<=D=|v-q|`, hence

\[
n\cdot(x-v)\le-{|x-v|^2\over2D}.                            \tag{3}
\]

In particular the support point is unique. Positive combinations of the two
extreme support normals show that `v` is the support point on the intervening
open normal interval `I_v`, of length `theta_v`. There

\[
h(\theta)=v\cdot n(\theta),\qquad \rho:=h+h''=0.             \tag{4}
\]

Constant width gives, in curvature-measure form,

\[
\rho(\theta)+\rho(\theta+\pi)=D.                            \tag{5}
\]

The curvature measure of a convex body is nonnegative. Since its sum with its
antipodal translate is the absolutely continuous measure `D dtheta`, it has
a bounded density `0<=rho<=D`. Therefore `h` is `W^(2,infinity)` and the
support-energy integrations below are legitimate. On `I_v+pi` we have `rho=D`:
this is a circular arc of radius `D` opposite the vertex.

The open intervals `I_v` for distinct source vertices are disjoint, since
they have different unique support points. Also no `I_v` overlaps `I_w+pi`
on an open interval, since one would force `rho=0` and the other `rho=D`.
Consequently **all** pairs `I_v union (I_v+pi)` are pairwise disjoint except
for endpoints. This simultaneous disjointness is the extra ingredient needed
for an additive budget. No diameter Euler-path inference is used.

## 3. Exact additive corner-energy inequality

### Theorem 1 — finite geometric inequality

For any finite planar diameter-`D` set `A`, define `theta_v` as above for every
actual diameter vertex of degree at least two. Then

\[
\boxed{
{D^2\over2}\sum_{v:d_v\ge2}
\left[\tan{\theta_v\over2}-{\theta_v\over2}\right]
\le {\pi D^2\over4}-\operatorname{area}(\operatorname{conv}A).
}                                                           \tag{6}
\]

This needs neither separation nor optimality. In particular

\[
\boxed{{D^2\over48}\sum_v\theta_v^3\le\delta_K.}              \tag{7}
\]

### Proof

For a constant-width body the support-area formula, obtained from the boundary
parametrization `x=h n+h' Jn` and integration by parts, is

\[
\delta_W={\pi D^2\over4}-\operatorname{area}W
={1\over2}\int_0^{2\pi}[(p')^2-p^2].                        \tag{8}
\]

Set `f=p+p''=rho-R` and define

\[
E(g)=\int_0^{2\pi}[(g')^2-g^2].
\]

On the antiperiodic `H^1` space, the Fourier modes are odd. The quadratic form
`E` is nonnegative, with precisely the translation first harmonics in its
kernel. Polarization and Cauchy–Schwarz therefore give

\[
\langle f,g\rangle^2\le2\delta_W E(g)                        \tag{9}
\]

for every antiperiodic `g`. This also follows by integrating
`<f,g>=-int(p'g'-pg)` and applying the same positive semidefinite form.
Translation modes contribute zero to both sides.

For each `v`, rotate so `I_v=(-a_v,a_v)`, `a_v=theta_v/2`, and define `g_v`
on `I_v` by

\[
g_v(t)={\cos t\over\cos a_v}-1,
\]

on `I_v+pi` by its negative antipodal copy, and elsewhere by zero. The function
is continuous and in `H^1`; its derivative may jump at the support endpoints.
On the interior of `I_v`, `-g_v''-g_v=1`. Since its endpoint values vanish,
integration by parts on the two intervals gives, with `k_v=tan(a_v)-a_v>0`,

\[
E(g_v)=4k_v,\qquad \langle f,g_v\rangle=-2Dk_v.              \tag{10}
\]

The second equality uses `f=-R` on `I_v` and `f=R` on `I_v+pi`.
The sign is immaterial in (9), but is the same for every vertex.

By the disjointness proved in §2, for `g=sum_v g_v`,

\[
E(g)=4\sum_v k_v,\qquad
\langle f,g\rangle=-2D\sum_v k_v.
\]

If there is at least one star, substitute these expressions into (9) and
divide by the positive sum to obtain

\[
\delta_W\ge {D^2\over2}\sum_v k_v.
\]

If there are no stars the conclusion is immediate. As `conv(A) subset W`,
`delta_K>=delta_W`, proving (6). Finally `tan(a)-a>=a^3/3` for `a>=0`,
because its derivative is `tan^2(a)>=a^2`. This proves (7). ∎

The Dirichlet bump above slightly strengthens the old single-interval cosine
test, but its simultaneous source-wide use is the main point. We never sum
individual deficit inequalities without proving their supports are disjoint.

## 4. Source-wide degree moment and incidence capacity

### Theorem 2 — every global minimizer

Let `A` be any planar unit-separated global minimum-diameter configuration,
with `D>=1`. Put

\[
a_D=2\arcsin{1\over2D},\qquad
\mathcal B_D={12\pi\sqrt3\over D a_D^3}.
\]

Then its **full actual** diameter graph satisfies

\[
\boxed{\sum_{v:d_v\ge1}(d_v-1)^3<\mathcal B_D
\le12\pi\sqrt3\,D^2.}                                    \tag{11}
\]

Vertices with `d_v=0` are excluded from this sum, rather than assigned a
negative summand. They are not removed from the source configuration.

### Proof

Two consecutive partner rays at `v` are separated by at least `a_D`, by unit
separation on the radius-`D` circle. Thus `theta_v>=(d_v-1)a_D` for `d_v>=2`.
Combine (7) and (1), and use `a_D>=1/D`. Degree-one vertices contribute zero. ∎

In particular `Delta(H)<=1+mathcal B_D^(1/3)=O(D^(2/3))`, uniformly over
all global minimizers, without a cyclic, full-core, or fixed-star hypothesis.
For the weaker pointwise information alone the additive form would be wasted.

### Theorem 3 — incidence packets

Let `S` consist of `N>=1` distinct actual diameter vertices, and suppose a
specified collection of actual diameter edges has at least `J` endpoint
incidences in `S`. An edge with both ends in `S` counts twice. Then

\[
\boxed{(J-N)_+^3<\mathcal B_D N^2.}                         \tag{12}
\]

Indeed `sum_{v in S}(d_v-1)>=J-N`, and Hölder gives
`[sum(d_v-1)]^3<=N^2 sum(d_v-1)^3`. If `J=Omega(D)` and `N<=J/2`, (11) gives

\[
\boxed{
N>{J^{3/2}\over\sqrt{96\pi\sqrt3}\,D}=\Omega(\sqrt D).
}                                                           \tag{13}
\]

If `N>J/2`, the stronger linear lower bound already holds. This is a counting
statement about actual source vertices, not KKT weights or repeated boundary
occurrences.

For several packets on pairwise disjoint actual vertex sets, the same proof
gives the simultaneous bound

\[
\boxed{\sum_i{(J_i-N_i)_+^3\over N_i^2}<\mathcal B_D.}        \tag{13a}
\]

No such sum is justified if two packets reuse a source vertex. Shared paths,
outer-walk occurrences, and phase labels are not disjoint vertex sets.

### Conditional threshold application

In the boundary-heavy alternative of the transverse-rail report, one extreme
`A`-layer has tree degree `d_*>m/4`. The paired staircase supplies two distinct
actual diameter representatives for each incident tree edge. Consequently
that layer contains more than `m/2` actual endpoint incidences. Its `N_*`
distinct diameter vertices satisfy

\[
\boxed{(m/2-N_*)_+^3<\mathcal B_D N_*^2.}                    \tag{14}
\]

Thus either `N_*>m/4`, or

\[
\boxed{N_*>{m^{3/2}\over\sqrt{768\pi\sqrt3}\,D}.}           \tag{15}
\]

For `m>=cD`, the threshold fork strengthens to:

* at least `m` selected actual diameters have full opposite-shore support; or
* one extreme layer contains `Omega(sqrt(D))` distinct actual diameter vertices.

This improves the prior `Omega(D^(1/4))` application. Neither alternative is
eliminated, and the open-cell exact-phase branch is outside that threshold fork.

There is a further exact consequence for the **selected** forest `F`. The
transverse-rail report gives

\[
(n_0-1)+(n_m-1)+\sum_{j=1}^{m-1}(n_j-2)=c(F)+1.
\]

All terms on the left are nonnegative. In the boundary-heavy case,
`n_0` or `n_m` is at least `N_*`; hence `c(F)>=N_*-2=Omega(sqrt(D))`.
This is not a lower bound on the number of components of the **full** actual
diameter graph: diameter edges outside `F` may join its components.

### Next combinatorial attack and its exact limit

We tried to turn the carrier count itself into a contradiction using only
the moment, full diameter-edge count, and the forest/caterpillar topology.
For every integer `k>=2`, take `k` disjoint stars with `k` leaves each, and
set the formal diameter scale to `D=k^2`. Their degree data are

\[
h=k^2=D,\quad q=k^2+k,\quad N_{\rm hubs}=k=\sqrt D,\quad
\sum_v(d_v-1)^3=k(k-1)^3<D^2.
\]

The hub packet has `J=D`, and each component is a caterpillar. The moment
allowance (11), a linear edge floor, and a linear vertex ceiling all survive.
Thus those **abstract numerical/topological constraints alone** cannot force
a linear hub population or eliminate the square-root alternative. This is
an exact arithmetic regression, not a claimed Euclidean diameter realization
or global minimizer. Ordered gap labels, actual diameter vectors, positive
contact reactions, and source minimality are intentionally omitted. They are
precisely the additional data a closing argument would have to use.

## 5. Further attack: an exact body regression at the cubic scale

We next tried to obtain `o(D^(2/3))` pointwise degree from the same area allowance.
The following explicit bodies show why this mechanism alone cannot do so.
They do **not** supply global minimizers, a dense unit-separated source, or
a Level I counterexample.

### Theorem 4 — constant-width near-disk bodies with long diameter stars

For `0<t<=1/4`, let

\[
a=\arcsin t,\quad b=\arcsin(2t),\quad
C=2\cos a-\cos b,\quad R=D/2.
\]

Define `p` on `[-pi/2,pi/2]` by

\[
p(\phi)=
\begin{cases}
R(C\cos\phi-1),&|\phi|\le a,\\
R[1-\cos(b-|\phi|)],&a\le|\phi|\le b,\\
0,&b\le|\phi|\le\pi/2,
\end{cases}
\]

extend antiperiodically, and put `h=R+p`. This is the support function of a
convex constant-width-`D` body `W_t`. It has a corner `v=(RC,0)` whose diameter
partners include the entire circular arc

\[
v-D(\cos\phi,\sin\phi),\qquad |\phi|\le a.                  \tag{16}
\]

Its exact disk-area deficit is

\[
\boxed{
\delta(W_t)={D^2\over2}
\left[2t\bigl(2\sqrt{1-t^2}-\sqrt{1-4t^2}\bigr)
-\arcsin(2t)\right].
}                                                           \tag{17}
\]

Furthermore

\[
\boxed{{D^2t^3\over3}\le\delta(W_t)\le{D^2t^3\over2}.}       \tag{18}
\]

### Proof and sharpness check

At `a` the two formulas for `p` and `p'` match, since
`sin(b-a)=Ct`; at `b` both are zero. Thus `h` is `C^1` and piecewise `C^2`.
Its curvature radius `h+h''` is respectively `0`, `D`, and `R` on the three
central pieces, and `D`, `0`, and `R` on their antipodal pieces. It is
nonnegative everywhere. The standard support parametrization, or integration
of `x'=(h+h'')Jn`, therefore gives a closed convex curve with support `h`.
Antiperiodicity gives `h(phi)+h(phi+pi)=D`, so its diameter is exactly `D`.
On the central interval the support point is `v`; on the antipodal interval
the support point is `v-D n(phi)`, proving (16).

For completeness, `rho-R=-R` on the central interval, `R` on its two
neighboring intervals, and zero outside; its antipodal copy has the opposite
sign. The energy formula gives

\[
\begin{aligned}
\delta(W_t)
&=2R\left[\int_0^a p(\phi)\,d\phi-
                 \int_a^b p(\phi)\,d\phi\right]\\
&=2R^2[Ct-a-(b-a-\sin(b-a))]\\
&=2R^2(2Ct-b),
\end{aligned}
\]

which is (17). To bound it, put `F(t)=2Ct-arcsin(2t)`,
`u=(1-2t^2)/sqrt(1-t^2)`, `w=sqrt(1-4t^2)`. Direct differentiation gives

\[
F'(t)=4(u-w),\qquad
u^2-w^2={t^2\over1-t^2}.
\]

For `0<=t<=1/4`, `7/8<=u<=1` and `3/4<=w<=1`. Hence

\[
2t^2\le F'(t)={4t^2\over(1-t^2)(u+w)}\le3t^2.
\]

Integrate from zero and multiply by `D^2/2` to get (18). ∎

Take `D=L^3`, `t=1/L`, integers `L>=4`. Then the disk-area deficit lies
between `D/3` and `D/2`, inside the canonical numerical allowance
`pi sqrt(3) D/4`. Yet the arc in (16) contains `Theta(D^(2/3))`
unit-separated diameter partners. An exact rational subfamily, translated so
the corner is the origin, is

\[
q_j=D\left({s_j^2-1\over1+s_j^2},
           {-2s_j\over1+s_j^2}\right),\qquad
s_j={j\over D},\quad |j|\le\lfloor L^2/4\rfloor.             \tag{19}
\]

All `|q_j|=D`. For distinct indices

\[
|q_i-q_j|^2={4D^2(s_i-s_j)^2\over(1+s_i^2)(1+s_j^2)}>1,
\]

and it is less than `D^2`. Their angles are in (16), because
`2|s_j|/(1+s_j^2)<=1/(2L)<t`. These finite sets are triangle-free and have
exact actual diameter stars, but their cardinality is only `Theta(D^(2/3))`.
They are not near-dense global sources. The following boundary completion
makes the regression an actual unit-separated source-hull example, rather
than relying on the area of an unsampled containing body.

### A unit-separated source whose actual hull has the small deficit

For integers `L>=8`, include the three body corners, the rational partners
(19), and all endpoints where one of the circular pieces meets another.
Keep the consecutive rational-partner intervals on the central `D`-arc.
Their arclengths are between `19/10` and `2`, since
`2D[atan(s_(j+1))-atan(s_j)]>=2/(1+1/(16L^2))`.
Every other circular interval has length at least four: in particular
`D(b-a)>=L^2`, and the portions between the extreme rational partner and
the end of the central arc have length at least `L^2/2`. Partition each
such interval into `floor(length/2)` equal pieces. All resulting consecutive
boundary arclengths are in `[19/10,4]`. Let `A_L` be their endpoints.

Here is a full separation check. From `C<=5/4`, `|h'|<=D/4`, and the explicit
support function,

\[
B(0,D/3)\subset W_t\subset B(0,3D/4).
\]

Consequently the boundary arclength per unit polar angle is at most `2D`,
because `ds/dphi=|x|^2/h<=27D/16`. Given two sample points, take their
boundary arc along the smaller polar-angle interval, and call its length `S`.
Necessarily `S>=19/10`. If `S<=D/12`, all its tangent directions turn by at
most `2S/D+2b<=1/6+pi/3<pi/2`: smooth curvature is at most `2/D`, and the
three corners have total turning `2b`. Projection onto the middle tangent
direction therefore gives chord length greater than `S/sqrt(2)>1`.
If `S>D/12`, the smaller polar angle is greater than `1/24`, and the two
radial lengths are at least `D/3`; their distance is greater than `D/144>1`.
Thus **every** pair of sample points is strictly more than unit distance.
The corner and its chosen partners ensure `diam(A_L)=D` exactly.

The area between one circular subarc of length `s<=4`, radius `r>=D/2`,
and its chord is at most `s^3/(12r)<=8s/(3D)`, by
`x-sin(x)<=x^3/6`. The corner points are included, so summing the disjoint
segment areas over the entire boundary yields

\[
0\le\operatorname{area}W_t-\operatorname{area}(\operatorname{conv}A_L)
\le{8\pi\over3}.
\]

Combining this with (18), for `D=L^3>=512`,

\[
\boxed{
\delta_{\operatorname{conv}A_L}\le D/2+8\pi/3
<{\pi\sqrt3\over4}D.
}                                                           \tag{20}
\]

Thus the **actual source hull** meets the same numerical area allowance (1),
with a unit-separated actual diameter star of order `D^(2/3)` and only `O(D)`
source points. Perimeter deficit is also small: the arc-minus-chord length
bound gives `pi D-per(conv(A_L))<=8pi/(3D)`.

If minimum separation exactly one is desired, divide all coordinates by the
minimum pair distance `tau`. We have `1<tau<=2` from the rational adjacent
partners. Nonconsecutive cyclic samples have distance greater than two:
in the short-arc case use `S>=2(19/10)`; in the long-arc case use
`D/144>2`. Hence all contacts of the rescaled source are between consecutive
cyclic samples. Its contact graph is a subgraph of a cycle with more than
three vertices, so remains triangle-free. Its area allowance (20) persists
under this rescaling. This normalized source still has only `O(D)` points,
and is not a global minimizer of that cardinality.

These actual source-hull examples refute an inference from **area allowance,
perimeter saturation, unit separation and actual diameter geometry alone**
to a smaller universal star exponent. They do not refute such a theorem if
actual quadratic packing population, contact equilibrium, or global minimality
provides extra input. Their general boundary separation and cap-area checks
are analytic proofs; the finite verifier below checks the rational star
subfamilies, not every boundary sample in `A_L`.

The body also has exact perimeter `pi D`: perimeter saturation alone does not
remove this regression, since integrating a constant-width support function
gives the same perimeter as the disk.

## 6. Computation and adversarial audit

[Exact verifier](../../research/verify_target_c_global_star_cubic_budget_2026_10_02.py):

```text
python3 research/verify_target_c_global_star_cubic_budget_2026_10_02.py
```

It uses `Fraction`, checks all pairs of four rational star witnesses, verifies
the cubic-regression derivative inequalities on rational parameter samples,
and checks the degree-packet Hölder reduction on finite graphs. These checks
certify the listed finite regressions and arithmetic. The general geometric
and functional-analytic theorems have complete proofs above; they do not depend
on sampled numerical survival.

Executed results: four rational stars, 244 partners, 11,692 exact source-pair
checks; 257 rational squared-identity samples; 1,099 finite graphs and 27,978
degree packets; five abstract square-root-carrier forests. Python compilation,
the theorem-state checker with research base `fbeae9b3`, the report-relative-link
check, and whitespace checks passed. Artifact regeneration repaired 28 report
headers/index entries already missing on the starting main and registered this
new report; all are unreviewed, with no manifest, canonical state or prompt change.

| Assertion or attempted extension | Classification | Audit boundary |
| --- | --- | --- |
| Additive corner energy (6) | proved candidate awaiting promotion | General constant-width completion; no unique completion asserted |
| Full-source degree cubic moment (11) | proved candidate awaiting promotion | Canonical complete-source area bound; all actual diameter bars |
| Threshold square-root carrier fork | conditional | Unpromoted paired-staircase and rail extraction |
| Pointwise exponent improvement from the area allowance alone | rejected mechanism / regression | Actual unit-separated source hulls (17)–(20); quadratic source population omitted |
| Simultaneous finite leaf release | not proved | Neither energy nor incidence capacity integrates a source motion |
| C-II or Level I closure | not proved | Both threshold alternatives and all other branches survive |

Stars and paths are allowed by (11); the moment is a capacity bound, not a
contradiction. No isolated source point is deleted. An inactive pair is never
made active. No contact-preserving competitor is inferred from symmetrization,
a completion, an infinitesimal shear, or a KKT zero. No boundary term is
discarded. The old full-source ZR/ZF and Euler-path failures are not used.

## 7. Remaining source-level obligation

The aggregate argument supplies the sharper actual population packet
`N_*=Omega(sqrt(D))` in the boundary-heavy threshold alternative. It does
not supply a positive lower bound on any packet's normalized KKT mass,
contact-path disjointness, an attachment depth, or a convex inactive chamber.

The next closing theorem must couple **that same actual layer packet**, or
the alternative linear full-opposite-support packet, to the retained opposite
shore and the canonical loaded-hull/exceptional-face ledger strongly enough
to force a unit triangle or a simultaneous same-cardinality strict diameter
competitor. The explicit body regression shows that a further area-only
pointwise star estimate is not such a coupling. Open-cell exact phase,
nonconstant phase, split-star, inactive-interface, higher-surplus full-core,
and macroscopic inactive-container branches remain uncovered.

**Promotion recommendation:** retain as unreviewed and request an independent
audit of completion scope, disjoint normal intervals, and the energy inequality.
Only after that audit should (11) replace the old source-wide `D^(3/4)` degree
input in canonical modules and current route dependencies.
