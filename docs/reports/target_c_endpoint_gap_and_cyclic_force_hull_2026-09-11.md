<!-- theorem-state: {"artifact_id":"ART-59AC9A5F1DE3","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — endpoint-aware direction gaps and the cyclic force hull

**Date:** 2026-09-11

**Starting state:** `main`, `3f37ef0eab4407a411f9a6d51d016ba600302be7`

**Run type:** closing-proof attempt / geometric bridge / regression audit

**Target:** full-source C-II

**Active prompt:** [Target C continuation](../prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md), with its controlling September 9 update

**External search:** rechecked the already imported Bonnesen statement

**Computation:** exact finite incidence checks and floating-point sanity checks, not proof inputs

## LEVEL I STATUS

**STILL OPEN.** No complete proof or infinite globally optimal counterexample was
obtained. C-I remains closed by the promoted September 9 audit. This report does
not promote the separate Z/ZR/ZF campaign or assume its rank conclusions.

The new proved geometric statements are:

1. Disjoint diameter chords have projective separation at least
   `2/D-8/D^3`, whereas the shared-endpoint floor is `1/D`.
2. Counting which consecutive directions share an endpoint converts the
   direction-gap bounds from an **edge count** into an **endpoint count**.
   If `q/D -> x`, the endpoint hull satisfies
   \[
   \liminf P_F/D\ge x+2\cos(x/2),\qquad
   \liminf A_F/D^2\ge (x+\sin x)/4.
   \tag{EG.1}
   \]
   The perimeter assertion is purely geometric. The area assertion uses the
   full-source near-minimal circumradius, with every isolated point retained.
3. In the fully visible **cyclic diameter-graph phase**, the force hull contains
   the concentric disk of radius `D/2-3*3^(1/4)*sqrt(D)` for sufficiently large
   `D`. Thus its area is `pi D^2/4-O(D^(3/2))`, and only `O(D^(3/2))` source
   points can lie outside it. This does **not** bound isolates inside the hull.

These are working-report theorems with complete proofs and a self-audit, not a
canonical promotion or a claim that the remaining capacity gate has closed.

## 1. Endpoint before tactic; state lock

The controlling [module 56](../targets/target-c/56-ci-restored-frontier.md)
reduces a hypothetical counterexample to a triangle-free global source minimizing
contacts and then diameter pairs, with `C=C_*` and `H=H_*`. All source points remain
present. No contact-preserving hull saturation is performed.

For `K=conv A`, write
\[
a_0=\sqrt3/2,\quad c_0=\sqrt3/4,\quad P=\operatorname{per}K,
\]
\[
\delta_K=\pi D^2/4-\operatorname{area}K,\qquad
\mathscr O_A=\operatorname{area}K+c_0P-a_0(n-1).
\]
The canonical Oler and strict translated-lattice bounds give
\[
\delta_K\ge0,\quad\mathscr O_A\ge0,\qquad
\boxed{\delta_K+\mathscr O_A<c_0P.}                 \tag{1.1}
\]
The intended implication was

```text
endpoint-aware diameter geometry + full-source circumradius
    -> stronger actual force-hull area / localization
    -> full-population capacity exceeding (1.1)
    -> contradiction.
```

Only the first arrow is established here. The last missing comparison is not
replaced by a leading-density estimate or a bar-rigidity assertion.

At the start, `docs/prompts/README.md` was modified and the September 10 Sol launch
prompt and state-review report were untracked. Those changes were preserved.
Relevant active C modules, the promoted orientation/integration audit, C33/C42,
the shared KKT/pinned-core statements, and named recent geometric/rank reports
were inspected. This was not an exhaustive re-audit of the entire theorem library.

## 2. Geometric setup

Let `A` be a finite unit-separated planar set of diameter `D>=3`. Select a family
`H_0` of `h>=2` distinct actual diameter pairs, and let `B` be its `q` distinct
endpoints. Put `F=conv B`, `P_F=per F`, and `A_F=area F`.

Diameter endpoints are extreme, and distinct disjoint diameter chords cross.
Their projective directions are distinct. List them cyclically on the circle
of circumference `pi`, with gaps `g_1,...,g_h`, whose sum is `pi`.

For C-II take `H_0=H`, the full actual diameter graph. Full visibility makes
`F` precisely the force hull of the unchanged source. The intermediate geometric
lemmas do not require contact rigidity, electrical conductance bounds, or weights.

## 3. Different spacing costs for incident and disjoint diameter chords

### Lemma EG.2 — chord separation

Two diameter chords sharing an endpoint have projective separation at least
`2 asin(1/(2D))>=1/D`. Two disjoint diameter chords have projective separation
\[
\boxed{\phi\ge 2/D-8/D^3.}                         \tag{3.1}
\]

**Proof.** The first statement is the chord formula for two radius-`D` vectors,
using unit separation of their other endpoints. Their angle is at most `pi/3`
because the other endpoints are also at distance at most `D`.

For the second, use the actual crossing-chord coordinates
\[
A=(0,0),\quad B=(D,0),\quad C=(x,-u),\quad E=(y,v),
\]
with `u,v>0` and `0<=x<=y<=D`, relabeling and reflecting if necessary.
The projection bounds follow from membership in both radius-`D` endpoint disks.
Writing `phi` for the acute projective angle,
\[
u+v=D\sin\phi,\quad y-x=D\cos\phi,\quad
a=x+(D-y)=D(1-\cos\phi).
\]
If `phi>=2/D`, (3.1) is immediate. Otherwise
`a<=D phi^2/2<2/D<1`. Unit separation of `A,C` and `B,E` gives
\[
u\ge\sqrt{1-x^2}\ge\sqrt{1-a^2},\qquad
v\ge\sqrt{1-(D-y)^2}\ge\sqrt{1-a^2}.
\]
Consequently
\[
D\phi\ge D\sin\phi=u+v
\ge2\sqrt{1-a^2}>2\sqrt{1-4/D^2}\ge2-8/D^2.
\]
This proves (3.1). The estimate is deliberately not claimed sharp at order
`D^-3`. For `D>=3`, its right side is at least `1/D`. ∎

The same lower bounds apply to each cyclic gap: a gap exceeding `pi/2` is
already larger than either bound; otherwise it is the projective distance.
In particular `h<=pi D`.

### Lemma EG.3 — consecutive shared-endpoint count

Let `I` count the cyclic gaps whose two diameter edges share an endpoint,
including both gaps when `h=2`. Then
\[
\boxed{I\le2h-q+1.}                                \tag{3.2}
\]

**Proof.** At an endpoint `b`, let `d_b` be its number of incident selected
edges. If `d_b<h`, a proper subset of `d_b` positions in a cyclic order has at
most `d_b-1` consecutive pairs within the subset. If `d_b=h`, the bound is
`d_b`. At most one vertex can be incident to all selected edges, since the graph
is simple and `h>=2`. Two distinct edges share at most one endpoint, so the
counts do not overlap. Summing gives
\[
I\le\sum_b(d_b-1)+1=2h-q+1.
\]
This argument works also for the length-two cyclic order, where the two
oriented gaps between the same pair are counted separately. ∎

Thus the number `k=h-I` of disjoint-edge gaps satisfies `k>=q-h-1`.
The extra `1` in (3.2) is necessary: an all-edge star attains it.

## 4. Finite endpoint-aware perimeter and direction-polygon area

Define
\[
t=t(D,q):=\max\{0,(q-3)/D-8\pi/D^2\}.              \tag{4.1}
\]
For realizable input, the argument below also shows `0<=t<=pi`.
Let `u_i` be unit vectors in the selected projective directions and set
\[
G_H=\frac D2\operatorname{conv}\{\pm u_i:1\le i\le h\}.
\]

### Theorem EG.4

For every configuration in Section 2,
\[
\boxed{P_F\ge D[t+2\cos(t/2)]-\frac{\pi}{6D},}       \tag{4.2}
\]
\[
\boxed{\operatorname{area}G_H
\ge\frac{D^2}{4}(t+\sin t)-\frac\pi6.}              \tag{4.3}
\]

**Proof.** Assign a gap floor `b_i=1/D` to each incident gap and
`b_i=2/D-8/D^3` to each disjoint gap. All are positive and at most `2/D`.
Lemmas EG.2–3 give
\[
\sum_i b_i=h/D+k(1/D-8/D^3)
\ge(q-1)/D-8\pi/D^2,                              \tag{4.4}
\]
using `h<=pi D` and `k<=h`.

Minimize either concave function `sum sin(g_i)` or `sum sin(g_i/2)` on
`g_i>=b_i`, `sum g_i=pi`. A minimum occurs at an extreme point, where all
but one gap equal their floors. If the exceptional index is `j`, put
`S=sum_(i!=j) b_i`. Then `S>=t`, `S<=pi`, and the remaining gap is `pi-S`.
Since `b_i<=2/D`,
\[
\sum_{i\ne j}b_i^3\le4\pi/D^2.
\]
Using `sin z>=z-z^3/6`,
\[
\sum_i\sin g_i
\ge S+\sin S-2\pi/(3D^2)
\ge t+\sin t-2\pi/(3D^2),                         \tag{4.5}
\]
and
\[
\sum_i\sin(g_i/2)
\ge S/2+\cos(S/2)-\pi/(12D^2)
\ge t/2+\cos(t/2)-\pi/(12D^2).                    \tag{4.6}
\]
The last inequalities use monotonicity on `[0,pi]` of
`s+sin s` and `s+2 cos(s/2)`. The minimizing exceptional index may differ
between the two objectives; the estimates are uniform in that index.

The cyclic polygon formula is
`area G_H=(D^2/4) sum sin g_i`, proving (4.3).
Also `2G_H subset F-F`, so Cauchy's perimeter formula gives
\[
2P_F=\operatorname{per}(F-F)
\ge\operatorname{per}(2G_H)=4D\sum_i\sin(g_i/2).
\]
Equation (4.6) now proves (4.2). ∎

This improves the earlier edge-count direction argument by charging almost
twice as much angular room when a new direction uses two new endpoints.
No assumption that the diameter graph is a matching is made.

## 5. Transfer to actual force-hull area, using all source points

For any containing disk `A subset closed B(o,R)`, let
\[
L=\sqrt{R^2-D^2/4}.
\]
For a selected diameter pair, its midpoint `m` satisfies
\[
|m-o|^2=(|p-o|^2+|q-o|^2)/2-D^2/4\le L^2.
\]
Its endpoints are `m +- (D/2)u`. Every endpoint and every vertex of `G_H`
therefore have corresponding points within `L`. Convex combinations show
\[
\boxed{d_{\rm H}(F-o,G_H)\le L.}                    \tag{5.1}
\]
In particular `G_H subset (F-o)+L closed B`. Steiner's formula and
`P_F<=pi D` give
\[
\boxed{A_F\ge\frac{D^2}{4}(t+\sin t)
-\frac\pi6-\pi DL-\pi L^2.}                      \tag{5.2}
\]
This is a finite statement for arbitrary containing radius `R`.

For a global minimizer, set `eta=3^(1/4) sqrt(D)`. The source-only portion of
[Section 155](../targets/target-a/08-prescribed-phase-alignment.md), also used in
the unpromoted [FS report](target_c_full_source_circumradius_response_2026-09-10.md),
gives a full-source circumcenter with `R<D/2+eta`. To record the exact scope:
Oler on all `n` points and the unconditional strict lattice bound give
`area K>pi D^2/4-c_0 per K`; hence
`per(K)^2-4pi area K<pi^2 sqrt(3) D`. Bonnesen gives `R-r<eta`, and `r<=D/2`.
No source-to-scaffold or shell assumption is imported.

Thus one may replace `L` in (5.2) by
\[
L_D=\sqrt{D\eta+\eta^2}=O(D^{3/4}).                \tag{5.3}
\]
Along any sequence with `D->infinity` and `q/D->x`, (4.2) and (5.2) give
exactly (EG.1). The uniform area error is `O(D^(7/4))`, not boundary order.
It must not be used to decide a one-integer packing comparison.

### Canonical-only C-II consequences

Let `b` be the outer contact-face walk length and `Q` its bounded-face
quadrangulation defect, with multiplicities retained. Promoted C42 gives
\[
b+Q+2c_I+2e_{BB}\le4q-4.                           \tag{5.4}
\]
The connected unit-edge outer walk surrounds the force hull, so `P_F<=b`.
One justification is to select occurrences of all hull vertices along the
closed walk; shortcutting between consecutive selected occurrences gives a
closed tour, whose length is at least the convex-hull perimeter. Combining
(4.2) and (5.4) yields the finite necessary inequality
\[
D[t+2\cos(t/2)]+Q+2c_I+2e_{BB}
\le4q-4+\pi/(6D).                                \tag{5.5}
\]
Let `x_0` be the unique root in `(0,pi)` of
\[
3x_0=2\cos(x_0/2).
\]
Because `q<=pi D`, take subsequences in (5.5). Its nonnegative extra terms
give `3x>=2 cos(x/2)`. Consequently every unbounded C-II sequence satisfies
\[
\boxed{\liminf q/D\ge x_0=0.6335016575\ldots,}       \tag{5.6}
\]
\[
\boxed{\liminf A_F/D^2\ge
(x_0+\sin x_0)/4=0.3063680583\ldots.}              \tag{5.7}
\]
These deductions use promoted C42, not ZF. The decimal evaluations are
illustrations; the defining equation and formula specify the constants exactly.
The proof of C42 uses contact minimality and force visibility, not the separate
hull-saturated normalization; its pinned set is the actual core diameter set.

### Conditional post-ZF comparison

If the separate report-level mixed rigidity input `e+h>=2v-2` is used,
Euler gives `b+Q<=2h`. With `h<=q` for a planar diameter graph, (4.2) then
implies `x>=2 cos(x/2)` in the limit. Thus `x>=2rho`, where `rho=cos rho`.
The new area floor in that explicitly conditional class is
\[
\boxed{(2\rho+\sin(2\rho))/4=0.6184708848\ldots.}    \tag{5.8}
\]
This is larger than the previous report-level PI floor
`sin(2rho)/2=0.4978566363...`. It is not an automatic promotion of ZF.

## 6. Odd diameter cycles force a nearly full disk

### Lemma CY.1 — an angular gap forces bipartiteness

Suppose all angles between outward diameter rays at a common endpoint are
at most `Theta<pi/2`. If the selected graph has an odd cycle, every cyclic
projective direction gap has length at most `Theta`.

**Proof.** Suppose a gap has length greater than `Theta`. Choose a line-direction
cut inside it and a nonzero covector whose kernel is that cut direction.
At one vertex, two incident outward rays cannot have opposite covector signs:
their short angular interval would cross a zero of the covector and project to
an interval of length at most `Theta` containing the cut. Since both of its
endpoints are selected directions, that interval must contain the whole empty
gap, a contradiction. Hence every vertex has all its incident rays of the
same sign. Along an edge the two endpoint rays are opposites, so their signs
give a bipartition. This excludes an odd cycle. ∎

This is a statement about geometric chord angles, not infinitesimal angular
rates or the old C-I shear separator.

### Theorem CY.2 — cyclic force-hull localization

Let `A` be a global source, with the circumcenter and `eta` above. Suppose
the selected actual diameter graph contains an odd cycle. Then, for sufficiently
large `D`,
\[
\boxed{\overline B(o,D/2-3\eta)\subseteq F
\subseteq K\subseteq\overline B(o,D/2+\eta).}        \tag{6.1}
\]

**Proof.** For diameter rays `by,bz` with apex angle `theta`, the triangle
`byz` is acute and has circumradius `D/(2 cos(theta/2))`. It lies in the
source containing disk, so
\[
\theta<2\arccos\frac{D}{D+2\eta}.
\]
Also `theta<=pi/3`. Set
\[
\Theta=\min\{\pi/3,2\arccos(D/(D+2\eta))\}.
\]
By CY.1 the largest selected projective gap is at most `Theta`.

For each unit vector `w`, choose a selected chord oriented as `p-k=D u`
with angle between `u,w` at most `Theta/2`. Since `|k-o|<=R`,
\[
(p-o)\cdot w=D u\cdot w+(k-o)\cdot w
\ge D\cos(\Theta/2)-R
>\frac{D^2}{D+2\eta}-\left(\frac D2+\eta\right)
>\frac D2-3\eta.
\]
The support function of `F-o` is therefore at least `D/2-3eta` in every
direction. Its supporting-half-plane representation proves the inner disk
inclusion. The outer inclusions are the full-source circumradius bound. ∎

In the lexicographic C-II source, `H=H_*`; thus if the actual diameter graph
has a cycle, it has an odd cycle by the canonical diameter-graph theorem,
and CY.2 applies to its actual force hull. In particular
\[
\boxed{A_F=\pi D^2/4-O(D^{3/2}),\qquad
P_F=\pi D-O(\sqrt D).}                            \tag{6.2}
\]
The same conclusion holds for the convex hull of the cycle's own vertices,
by applying the argument just to that cycle.

Let `z_ext=|A\setminus F|`. For `r=D/2-3eta>1/2`, the radius-`1/2` disks
centered at these points have disjoint interiors and lie in the annulus
between radii `r-1/2` and `D/2+eta+1/2`. Therefore
\[
\boxed{z_{\rm ext}\le4(4\eta+1)(D-2\eta)
\le16\eta D+4D=O(D^{3/2}).}                      \tag{6.3}
\]
The full source population is used in this packing estimate. Nothing in
(6.3) bounds the number of contact-isolated points **inside** `F`.

As another canonical-only consequence, (5.4) and (6.2) imply in this phase
\[
\liminf q/D\ge\pi/4.
\tag{6.4}
\]
Conditionally on ZF the analogous lower bound for `h/D` is `pi/2`.

## 7. Why these estimates still do not close C-II

Two further closing attempts fail at identifiable points.

**Area lower bound versus capacity.** A larger `A_F` gives a larger force-hull
carrier and improves a conditional attachment-cell area gap. It does not give
an upper bound on all `n` points. The `O(D^(7/4))` error in (5.2), and even
the cyclic `O(D^(3/2))` error, exceed the boundary-scale allowance in (1.1).

**Cyclic hull localization versus force population.** Equation (6.3) only bounds
points outside `F`, not points outside the nonisolated core. Replacing `z_ext`
by `n-|V(C)|` would revive the rejected force-bulk argument. A regular odd
unit shell with a dense isolated filling has its force hull already equal
to the whole source hull and can still have quadratically many isolates.

The geometric envelope in (EG.1) is asymptotically sharp without the contact/KKT
conditions. Fix `0<x<pi`, take radius `D/2`, and place `m` equally spaced
points at angular step `delta=2 asin(1/D)` in an arc of span
`s=(m-1)delta`, together with their antipodes, where `2m/D->x`. For large
`D`, the two intervening gaps exceed `delta`, so all points are unit-separated.
The diameter graph is an opposite matching and `q=2m`. Direct polygon formulas give
\[
P_F=2(m-1)+2D\cos(s/2),\qquad
A_F=\frac{D^2}{4}[(m-1)\sin\delta+\sin s].
\]
Their normalized limits are exactly (EG.1). The contact graph is two disjoint
paths, so this is **not** a positive connected C-II source or a global minimizer.
It establishes sharpness of the geometric relaxation, not a disproof of Erdős #99.

## 8. Regression and dependency audit

| Test | Disposition |
| --- | --- |
| Cyclic incidence off-by-one | The `+1` in (3.2) is necessary for an all-edge star; retained. |
| Two-edge order | Both cyclic gaps counted; exact finite checks include it. |
| Crossing matching | Pays the larger disjoint gap; never replaced by a star. |
| Regular odd shells | `g_max=Theta=pi/h`; CY.1's threshold is attained. Hulls approach the disk, consistently with CY.2. |
| Dense isolated shell fillings | Compatible; internal isolates are not bounded or deleted. No global certificate inferred. |
| Heptagon plus center | The center remains inside the hull and outside the contact core; no false localization. Small `D` is outside the nonvacuous asymptotic disk bound. |
| Two antipodal arcs | Exactly sharp geometric limit; lacks connected positive contact equilibrium. |
| Near-star electrical examples | No conductance floor or arbitrary-data operator bound is asserted. |
| Oblique rhombic meshes / degree-three and degree-five examples | No pure-rhombic topology or density gap is inferred. |
| Hull saturation versus secondary minimum | No source point is moved; the normalizations are not combined. |

Canonical inputs actually used are the full-source Oler/lattice/Bonnesen bounds,
actual diameter-thrackle geometry, the force-hull identification, and C42's
positive pinned-stress row surplus and Euler identity. The new geometric proofs
do not require C56, ZF, or generic PSD. Conditional uses of ZF are labeled above.

The already imported Bonnesen theorem was checked in Daniel A. Klain,
[*An Error Estimate for the Isoperimetric Deficit*](https://faculty.uml.edu/dklain/Klain-Isoperimetric.pdf),
Section 4, equation (6), page 990. Its hypotheses are a compact convex planar
body with inradius `r` and circumradius `R`; it gives
`P^2-4pi area>=pi^2(R-r)^2`. Only this full-source containing-radius input is
used. No new reconfiguration or packing-optimality theorem was imported.

## 9. Computation and repository disposition

Run

```sh
python3 research/diameter_endpoint_gap_audit.py
python3 -m unittest discover -s research -p 'test_*.py'
```

The new script exhausts ordered edge subsets of `K_4` for (3.2), in integer
arithmetic, and separately checks admissible crossing quadrilaterals,
regular-shell/two-arc geometric formulas, and gap-simplex examples in floating
point. The latter are sanity checks only.
All general proofs above are independent of its output.

The run passed 1,950 exact ordered-edge incidence cases, 15 two-arc cases,
5 regular-shell cases, and 2,000 gap-simplex cases. The pre-existing unit-test
suite also passed all 65 tests. The crossing-quadrilateral check filters its
fixed-seed samples against all four cross-pair separation/diameter inequalities;
its accepted count is printed by the script. None of these runs is a global
packing certificate.

**Hold as report for independent audit.** No route map, active prompt, theorem
module, or model configuration is changed. The only accompanying changes are
the scoped audit script and its entry in `research/README.md`.

## 10. Exact remaining theorem and handoff

The sufficient full-source obligation remains:

> For every sufficiently large lexicographic triangle-free global C-II source,
> with all isolated points retained, derive
> `delta_K+O_A >= (sqrt(3)/4) per(K)`, or construct a same-cardinality,
> unit-separated competitor of diameter strictly below `D`.

The new split makes the required carrier more precise: a forest diameter graph
has the endpoint-aware envelope (4.2), (5.2); a cyclic diameter graph has the
near-full disk (6.1), with exterior population bounded by (6.3). A theorem must
still account for isolated points in the core hull and exact finite capacity.

```text
LEVEL I STATUS: STILL OPEN.
Authority unchanged: Target C module 56; C-I closed, full-source C-II open.

New report-level proofs:
  disjoint diameter direction gap >= 2/D-8/D^3 (D>=3);
  incident consecutive gaps I <= 2h-q+1;
  t=max(0,(q-3)/D-8pi/D^2);
  P_F >= D[t+2cos(t/2)]-pi/(6D);
  A_F >= D^2(t+sin t)/4-pi/6-pi D L_D-pi L_D^2,
      L_D=sqrt(D eta+eta^2), eta=3^(1/4)sqrt(D).
  Canonical C42 gives liminf q/D >= 0.6335016575...,
      liminf A_F/D^2 >= 0.3063680583... .
  Conditional on separate ZF: area floor >=0.6184708848... .

Odd-cycle phase:
  a projective gap wider than every diameter-star angle forces bipartiteness;
  hence B(o,D/2-3eta) subset F subset K subset B(o,D/2+eta);
  A_F=pi D^2/4-O(D^(3/2)); outside-F population O(D^(3/2)).
  Internal contact-isolated points remain uncontrolled.

No Level I closure, no promotion, no stress-weight floor, no source relocation.
Next: exact full-population capacity in these carriers, not another leading
area bound or the false identification of force hull with force-visible population.
```
