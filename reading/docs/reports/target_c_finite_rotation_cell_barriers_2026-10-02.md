> Generated reading edition · [exact source](../../../docs/reports/target_c_finite_rotation_cell_barriers_2026-10-02.md) · source SHA-256 `d19bcc9fe6a829fef840997ce425c3aedd88c5271181c51f51cc45394186c127`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-DEDB57344382","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II — finite rotation walls and erosion-coordinate localization

```text
actual diameter angle separation + paired erosion intervals
-> finite angle barriers without a positive multiplier floor
-> only O(D epsilon) outer erosion coordinates can change in an epsilon window
-> no endpoint within the two cells adjacent to the reference diameter
-> still missing: a phase-changing full-source competitor or an actual-source
   contradiction; the quantitative barrier alone does not close C-II.
```

**Date:** 2026-10-02.\
**Shared starting HEAD:** `fbeae9b3fa18a63e07573676b4e2e512a91ca4d5`.\
**Isolated research base:** `0031d1d932d07ad657bf5efa34cfd16a3d249b02`.\
**State version:** `2026-09-14.audit.51`; authority files unchanged between these bases.\
**Mission:** finite endpoint angle barriers, separate from PRs #624–#627.\
**Branch:** `swarm/sol/diameter-rotation-cells-20261002`.\
**Classification:** proved candidates awaiting independent audit/promotion;
artifact lifecycle **unreviewed**. Section 6 is a **regression**.\
**Level I / C-II:** **OPEN**. No canonical state or prompt is changed.\
**Active prompt:** [current Target C continuation](../prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md).\
**External literature:** none imported.\
**Certificate:** [exact rational verifier](../../../research/verify_target_c_rotation_cell_barriers_2026_10_02.py).

## 1. Dependencies and exact scope

The new finite theorems concern the *actual Euclidean diameter bars* of a
unit-separated source and an explicitly specified contact-preserving endpoint
map. They do not require global optimality, KKT positivity, or PSD.

Canonical context is [the problem statement](../problem/statement.md), the
normal form in [Target C §56](../targets/target-c/56-ci-restored-frontier.md),
and [C-ZRF §57](../targets/target-c/57-zr-zf-rigidity-audit.md). §57 is used only
to interpret the rank input of the earlier extracted branch, never to assert
anything about contact-isolated coordinates. All source points remain present.

The application to the current extracted shore is **conditional on** the
unpromoted [nested-bundle report](target_c_exact_phase_nested_bundle_tree_2026-10-01.md),
especially §§3–5 and its exact endpoint formula (9), and the
[threshold paired staircase](target_c_exact_phase_threshold_paired_staircase_2026-10-01.md).
Their finite consequences are stated as explicit hypotheses below. Inspection
of their normal-order and positive nested-profile arguments gives the ordering
used here; no report is promoted by this application.

The nested-bundle report §6 already proves source-dependent local isolation
using positive KKT cancellation and full column rank. That result is not claimed
as new. The present additions are an explicit finite angle wall, an angular
localization count independent of all stress weights, and an exact sharpness
regression for extending the inverse-diameter window.

## 2. Actual diameter direction spacing, including a disjoint refinement

Write

```math
\delta_D=2\arcsin\frac1{2D}.
```

### Lemma R.1 — two actual diameter bars

In a finite unit-separated planar diameter-`D` set, two distinct diameter bars
have smaller projective angle at least `delta_D`. If they are vertex-disjoint,
their smaller projective angle `phi` satisfies the stronger exact inequality

```math
\boxed{\phi\ge2\delta_D=4\arcsin\frac1{2D}.}                 \tag{R.1}
```

The shared-endpoint `delta_D` bound is an existing repository geometry input
(called C67 in older reports); we include a proof and do not claim it as new.
The proof below independently establishes the disjoint refinement.

**Proof.** For two bars sharing an endpoint, the angle at that endpoint is at
most `pi/3`, since their other endpoints are at distance at most `D`. Those
other endpoints are at distance at least one, so `2D sin(phi/2)>=1`.

For disjoint bars orient their vectors `r,r'` to have smaller angle
`0<phi<=pi/2`. Let `z` be their midpoint displacement. Put

```math
s=(r+r')/2,\quad w=(r-r')/2,\quad
a=|s|=D\cos(\phi/2),\quad b=|w|=D\sin(\phi/2).
```

The vectors `s,w` are perpendicular. In their orthogonal coordinates write
`z=(x,y)` and replace coordinates by their absolute values. The two opposite
cross-endpoint distances are `|z+s|,|z-s|<=D`, hence

```math
x^2+y^2+2ax\le b^2,\qquad x,y\ge0.                        \tag{R.2}
```

The smaller aligned-endpoint distance has square `x^2+(b-y)^2`, where
`0<=y<=b`. It is at least one by unit separation. Its maximum on (R.2) is

```math
\boxed{\max[x^2+(b-y)^2]=2D(D-a)=4D^2\sin^2(\phi/4).}     \tag{R.3}
```

Here is an explicit optimization proof. For fixed `y` the objective increases
with `x`, so maximize on the curved boundary. There it equals
`2b^2-2ax-2by`. The boundary is
`y=sqrt(b^2-x^2-2ax)`, `0<=x<=D-a`. The function `ax+by(x)` is concave, so
its minimum is at an endpoint. The endpoint values are `b^2` and `a(D-a)`;
the latter is smaller since `b^2=(D-a)(D+a)`. Substitution proves (R.3).
Combining (R.3) with separation proves (R.1). This also excludes a zero angle.
∎

The bound is attained. For `D>= (1+sqrt(5))/2`, set

```math
h=\sqrt{1-\frac1{4D^2}},\quad
P_0=(0,0),\ P_1=(D,0),\quad
P_2=(1/(2D),h),\ P_3=(D-1/(2D),h).
```

The source is unit-separated. Its actual diameters are `P_0P_1`, `P_0P_3`,
and `P_2P_1`. The last two are disjoint and have angle `2delta_D`; the two
short end sides have length one. This is a four-point feasible regression,
not a global-optimality claim. Rational equality packets are certified in §8.

### Lemma R.2 — two opposite cross pairs are quadratically near diameter

For the same two disjoint diameter bars, both opposite cross-endpoint
distances `ell_+,ell_-` satisfy

```math
\boxed{D^2\cos\phi\le\ell_\pm^2\le D^2.}                \tag{R.4}
```

**Proof.** Their squared lengths are
`a^2+|z|^2 +/- 2ax`. By (R.2),
`2a|x|<=b^2-|z|^2`. Each length is therefore at least
`a^2-b^2+2|z|^2>=D^2 cos(phi)`. ∎

Consequently if `phi<=C/D`, with `phi<=pi/2`, both cross pairs obey

```math
0\le D-\ell_\pm\le D(1-\sqrt{\cos\phi})
\le D\phi^2/2\le C^2/(2D).                                \tag{R.5}
```

The penultimate inequality follows from
`1-sqrt(cos(phi))<=1-cos(phi)<=phi^2/2`. This supplies *actual source pairs*
for an augmented near-diameter system. It does not make a strict pair active.

### Lemma R.2b — a definite inactive-deficit bill in a thin double lens

Let `b=D sin(phi/2)`, `q=D(1-cos(phi/2))`, and suppose `q<1`. The opposite
cross pairs in R.2 have total squared diameter deficit

```math
E=(D^2-\ell_+^2)+(D^2-\ell_-^2)
\ge\boxed{4b\sqrt{1-q^2}-2.}                              \tag{R.5b}
```

**Proof.** Use the absolute midpoint coordinates of (R.2). That inequality
gives `0<=x<=q` and `0<=y<=b`. Separation of both aligned endpoint pairs
implies `x^2+(b-y)^2>=1`. Since `x<1`, it follows that
`y<=b-sqrt(1-x^2)`. Consequently

```math
|z|^2\le x^2+(b-\sqrt{1-x^2})^2
=b^2+1-2b\sqrt{1-x^2}.
```

Adding the two cross-pair squared lengths yields
`E=2(b^2-|z|^2)`. Substitute this bound, then use `x<=q`. ∎

If `D->infinity` and `D phi->c<infinity`, R.1 gives `c>=2`, and (R.5b)
implies `liminf E>=2c-2>=2`. Hence at least one of these actual cross pairs
has squared deficit at least `1-o(1)`, and thus length deficit at least
`(1-o(1))/(2D)`. One cannot replace the whole thin lens by four exact
diameter bars, or even by four bars with `o(1/D)` length errors.

This lower bill is attained asymptotically, with *both* cross pairs strict.
Take a rectangle of sides `L,1`, `D=sqrt(L^2+1)`. Its two diagonals are the
only diameters and are disjoint, with `phi=2 asin(1/D)`. Both long sides
have squared deficit exactly one, `D(D-L)->1/2`, and `E=2`. Rational choices
`D=(k^2+1)/(2k)`, `L=(k^2-1)/(2k)` give an exact unbounded family. This is
a regression against activating the near pairs, not a global minimizer family.

There is also exact finite equality in (R.5b): the trapezoids following R.1
have `q=1/(2D)`, `b=sqrt(1-q^2)`, and `z=(q,0)`. Both sides of (R.5b) equal
`2-1/D^2`. The lower bill is therefore a sharp inequality, not merely a
convenient positive estimate.

## 3. Exact finite wall for one changed train coordinate

Let `u=(1,0)`, and let `r=D(cos(phi),sin(phi))` be an actual diameter vector
with `0<phi<pi`. Replacing one contact direction `u` by `R_theta u` changes
that diameter vector to `r+R_theta u-u`. Put

```math
\psi=\operatorname{Arg}(r-u)\in(0,\pi).
```

Since subtracting the positive horizontal vector from `r` increases its
argument, `psi>phi`. The exact upper constraint is

```math
|r+R_\theta u-u|^2-D^2
=2(r-u)\cdot(R_\theta u-u)
=2|r-u|[\cos(\theta-\psi)-\cos\psi].                       \tag{R.6}
```

For `0<theta<pi`, this is nonpositive **if and only if**

```math
\boxed{\theta\ge2\psi.}                                  \tag{R.7}
```

If `2psi>=pi` there is no such feasible positive turn below `pi`. Indeed the
cosine difference is `2 sin(theta/2) sin(psi-theta/2)`, whose sign gives
exactly (R.7). Reflecting across the horizontal axis gives the corresponding
negative-turn wall for a negative-transverse diameter. This is an endpoint
identity, not an integration of a first-order derivative.

## 4. Finite erosion-coordinate localization

Assume the following exact finite hypotheses.

1. The source is unit-separated with actual diameter `D`; there is a reference
   actual diameter with vector `Du`.
2. The selected actual contact-preserving endpoint map has coordinates
   `theta_i in (-pi,pi)`, and an old diameter with support interval `I` changes by
   ```math
   r_h\longmapsto r_h+\sum_{i\in I}(R_{\theta_i}u-u).        \tag{R.8}
   
   ```
   All other selected coordinates are fixed. This assumption must be proved on
   the actual source cuts before applying the theorem to a carrier or chart.
3. There are interval types
   `I_1 supersetneq ... supersetneq I_m`, with `|I_s|=m-s+1`, and
   `I_{m+1}=empty`. Let `i_s` be the unique element of `I_s\I_{s+1}`.
4. For each type `I_s` choose actual diameters `r_s^+,r_s^-` of opposite
   transverse signs. Write their angles as `phi_s^+` counterclockwise and
   `phi_s^-` clockwise from `u`, each in `(0,pi)`. On each sign branch the
   angles strictly increase with `s`. This is exactly the normal-order property
   of the existing paired erosion theorem; chosen bars remain distinct.

### Theorem R.3 — explicit finite endpoint localization

Suppose every old actual diameter is at most `D` at the endpoint. Define

```math
B_s^+=2\operatorname{Arg}(r_s^+-u),\qquad
B_s^-=2\operatorname{Arg}(\overline{r_s^-}-u),              \tag{R.9}
```

where the overline reflects across the `u` axis. If
`|theta_i|<=epsilon<pi`, only the coordinates `i_s` with

```math
s\le K:=\min\left(m,\left\lfloor\frac{\epsilon}{2\delta_D}\right\rfloor\right)
                                                                    \tag{R.10}
```

can change. Thus every coordinate in `I_{K+1}` is exactly zero. In particular,

```math
\boxed{\epsilon\le2\delta_D\quad\Longrightarrow\quad
       \theta_i=0\text{ for every }i.}                   \tag{R.11}
```

For a window `epsilon=C/D`, at most `floor(C/2)` outer erosion coordinates
can change; the bound is uniform in `m` and in all KKT weights.

**Proof.** Lemma R.1 applies between the reference bar and the first chosen
bar, and between consecutive chosen bars of each sign. Ordinary angle
differences are at least their smaller projective separations. Consequently

```math
\phi_s^\pm\ge s\delta_D,\qquad
B_s^\pm>2\phi_s^\pm\ge2s\delta_D.                         \tag{R.12}
```

Start at `s=m` and descend. If all coordinates in `I_{s+1}` are zero, (R.8)
on the two chosen bars of type `I_s` is exactly the single increment
`R_{theta_{i_s}}u-u`. A positive nonzero coordinate requires
`theta_{i_s}>=B_s^+` by (R.7), and a negative one requires
`-theta_{i_s}>=B_s^-`. If both barriers exceed `epsilon`, the coordinate is
zero. This induction freezes every `s>K` and proves (R.10).

For `epsilon<=2delta_D`, even the barriers for `s=1` strictly exceed the
window, giving (R.11). Finally `D delta_D>1`, so `K<=floor(C/2)` in the
`C/D` window. ∎

The same proof gives the exact asymmetric version: if
`-epsilon_-<=theta_i<=epsilon_+`, freeze every terminal interval whose chosen
walls have `B_s^+>epsilon_+` and `B_s^->epsilon_-`. This is useful when the
transverse strict-rhombus constraints allow different turns on the two sides.

### Corollary R.4 — no endpoint within the adjacent diameter cells

Let `eta_+,eta_-` be the distances from the reference projective direction
`u` to the nearest other actual diameter directions on its two sides. These
are positive and have sum at most `pi`. If every selected endpoint direction
has the lift

```math
-\eta_-\le\theta_i\le\eta_+,                              \tag{R.13}
```

then every `theta_i=0`.

**Proof.** Every selected positive ray has `phi_s^+>=eta_+`, and every
negative ray has `phi_s^->=eta_-`; using a projective line can only move a
wall nearer `u`. Therefore (R.9) strictly exceeds the respective widths in
(R.13). Descending induction as above proves the claim. ∎

This covers the union of the two direction cells adjacent to the reference
diameter, including their boundary walls. It does not assume the reference
direction lies in an open cell. A remote endpoint must cross one of these
walls or leave the stated motion family. KKT coefficients are not used.

## 5. Push toward closure and the surviving finite state problem

If the physical transverse shore supplies a `C/D` endpoint window, R.3
reduces this whole selected rotation family to finitely many **outer** erosion
coordinates. It does not prove that every competitor belongs to the family,
or that the transverse shore supplies `C<=2`. In particular an `O(1/D)`
phase statement with an unspecified or larger constant is insufficient.

There is an exact next finite formulation. Put

```math
X_s=\sum_{i\in I_s}(R_{\theta_i}u-u),\quad X_{m+1}=0,
\quad \mathcal L_s=\bigcap_{h:I_h=I_s}\overline B_D(-r_h).
```

Then all old diameter constraints of these interval types are equivalent to

```math
X_s\in\mathcal L_s,\qquad |X_s-X_{s+1}+u|=1.               \tag{R.14}
```

The second identity is exactly the unit length of the changed coordinate.
Conversely each sequence obeying (R.14) determines unit directions by
`v_{i_s}=X_s-X_{s+1}+u`; a stated angle window chooses their lifts. In a
`C/D` window, R.3 gives `X_{K+1}=...=X_{m+1}=0`, leaving only `K<=floor(C/2)`
links. Parallel-reference rows, empty-support bars, and all inactive source
pairs must additionally be checked; (R.14) does not silently drop them.

This repaired finite problem was attacked first at `K=1`. Section 6 exhibits
an exact feasible remote endpoint just beyond the universal wall, with every
source pair retained. It rules out improving R.11 to an arbitrary inverse-
diameter window using the stated finite geometry alone. Positive full-source
KKT and the actual complete transverse shore are genuinely additional inputs.

The near-diameter bridge R.5 was then tested against the same source packets
and the disjoint-lens equality packets. A short geometric pair can supply
strict cross pairs as well as exact ones. Thus the repair “declare every
`O(1/D)`-near pair active” is invalid. An augmented system requires a finite
feasibility theorem or an exact multiplier/constraint argument; proximity alone
does not close it.

The repaired quantitative attack is R.2b: thin, disjoint actual diameter bars
force a nonvanishing squared-slack bill even as their cross-pair lengths
approach diameter. Its exact rectangle regression shows that neither
`O(1/D)` closeness nor a two-edge near-diameter four-cycle removes that bill.
No canonical bound pays or contradicts the sum of these bills; boundary-order
shape allowance alone does not. They must stay in the finite link problem as
strict constraints, rather than becoming extra rows of the old KKT system.

## 6. Exact sharpness regression with all source pairs

For integers `N` sufficiently large, let `D=N`, `u=(1,0)`,

```math
t=1/(2N-1),\quad c=\frac{1-t^2}{1+t^2},\quad
s=\frac{2t}{1+t^2},\quad b_\pm=(Nc,\pm Ns).
```

Use the `N+5` actual source points

```math
A_N=\{ku:0\le k\le N\}\cup\{b_+,b_-,b_+-u,b_--u\}.
                                                                    \tag{R.15}
```

The three actual old diameters are `0--Nu`, `0--b_+`, `0--b_-`. Every source
point has a unit contact: the long horizontal chain and the two end dimers.
The three contacts across the cut with moving side `{Nu,b_+,b_-}` all have
oriented vector `u`. There are no unit triangles.

Write `w=b_+-u=(w_x,w_y)` and rotate `u` to the rational unit vector

```math
v=\left(\frac{w_x^2-w_y^2}{|w|^2},
          \frac{2w_xw_y}{|w|^2}\right),\qquad \Delta=v-u.   \tag{R.16}
```

Translate the three moving points by `Delta`. Every old unit contact is
preserved; all old and new source pairs remain at least one and at most `D`
for all sufficiently large `N`. The upper `b_+` diameter is preserved exactly,
and the other two old diameters strictly shorten. No new contact or diameter
is created. The rotation has

```math
\theta_N=2\operatorname{Arg}(b_+-u),\qquad
\boxed{N\theta_N\longrightarrow2.}                       \tag{R.17}
```

**Complete asymptotic feasibility proof.** `Ns>1` and
`|b_+-Nu|=2N/sqrt((2N-1)^2+1)>1`. Both moving-side and fixed-side pair
distances are unchanged. Crossing contacts have vector `v` and hence length
one. The only other pairs with limiting length one, after subtracting `Nu`
from the end cluster, are the fixed dimer partners with `(N-1)u`; these are
fixed and have vertical distance `Ns>1`. All other noncontact cross pairs in
that end cluster have limiting length at least `sqrt(2)`.

For sufficiently large `N`, moving points have horizontal coordinate greater
than `N-1`. Their distance to each earlier chain point is no smaller than
their distance to `(N-1)u`. Fixed dimer partners with earlier chain points
have vertical distance `Ns>1`. This checks every lower constraint, including
the small unchanged strict lower gaps.

For upper bounds, within the end cluster all distances are bounded as
`N` grows. From fixed dimer partners to the chain the maximum is at an endpoint
and is `N-1+O(1/N)<N`. From moving points to the chain the maximum squared
distance, a convex function of the chain coordinate, is at `0` or `(N-1)u`.
The latter distances are bounded. At `0`, (R.6) and (R.16) give equality for
`b_+`; for `Nu` the squared change is `2(N-1)(cos(theta_N)-1)<0`; for `b_-`
subtracting the `b_+` identity gives `-4Ns Delta_y<0`. This checks every upper
constraint. The unchanged moving distance `|b_+-Nu|>1` and the preserved
contacts show there are no missing limiting-equality lower cases. Equation
(R.17) follows from `N Arg(b_+) -> 1` and
`N Arg(b_+-u) -> 1`. ∎

For every fixed `C>2`, this yields a nontrivial feasible endpoint with
`|theta_N|<C/D` for all sufficiently large `N`. Thus the leading constant
two in the **universal finite** identity window cannot be increased.

The packet is explicitly **nonglobal**: place `N+5` points on a unit square
grid with side `ceil(sqrt(N+5))`. Its diameter is at most
`sqrt(2)(ceil(sqrt(N+5))-1)<N` for all sufficiently large `N`. It also fails
positive full-source KKT: at `b_+`, its only contact force is horizontal,
whereas its only diameter force has nonzero vertical component. The diameter
weight at that vertex must be zero. Finally the three cut contacts are not
proved to be a complete O--O train shore, and `m=1` is not a linear extracted
shore. None of those missing hypotheses is silently supplied by this example.

## 7. Claim audit and remaining global gap

| Claim | Classification | Exact limit |
| --- | --- | --- |
| R.1, disjoint angle `2delta_D` | proved candidate awaiting promotion | actual finite geometry; no optimality needed |
| R.2, actual cross pairs near diameter | proved candidate awaiting promotion | proximity does not activate a constraint |
| R.2b, definite thin-lens squared deficit | proved candidate awaiting promotion | requires the stated thin-lens limit; no global payment theorem |
| R.3, finite erosion localization | proved candidate awaiting promotion | explicit actual endpoint-map and ordered paired-interval hypotheses |
| R.4, adjacent-cell identity | proved candidate awaiting promotion | selected motion family; no arbitrary-competitor statement |
| any `C/D` window forces identity | rejected finite assertion / regression | R.15–R.17 for every `C>2`; lacks full KKT/transverse shore |
| local isolation implies C-II | rejected inference | a phase-changing competitor and other source branches remain |

The exact next obligation is to use the **actual transverse shore and all
inactive source pairs** to exclude or exploit the at-most-`floor(C/2)` outer
erosion links in (R.14). A strict same-cardinality sub-`D` competitor, or a
contact/diameter-count contradiction with every newly active pair controlled,
would change the global frontier. A carrier window or mere near activity would
not. Nonconstant-phase TB1, split-star O--O outside the stated extraction,
inactive interfaces, higher-surplus full-core sources, and macroscopic inactive
chambers/exterior caps all remain open.

## 8. Exact computation and checks

Run:

```text
python3 research/verify_target_c_rotation_cell_barriers_2026_10_02.py
```

The certificate uses `Fraction` only. Five rotation packets
`N=10,16,32,64,128` pass **36,315** full-source/competitor pair checks and
**15** exact preserved cut-contact checks. It checks all old/new contacts,
diameters, triangle-freeness, zero contact-isolate count, both shortened old
diameters, the exact active angular boundary and its two sides, and a strict
same-cardinality square-grid competitor.

Five rational lens-equality packets use
`D=(k^2+1)/(4k)`, `h=(k^2-1)/(k^2+1)`,
`k=9,17,33,65,129`. They pass **30** exact pair checks and the algebraic
identity for angle `2delta_D`. They certify sharpness of R.1, not an
unbounded global-minimizer family. The analytic arguments, rather than finite
enumeration, prove the general theorems and eventual packet feasibility.

Five further rational rectangles, using `k=9,17,33,65,129`, pass **30** exact
pair checks. Both opposite cross pairs are strict and each has squared
diameter deficit exactly one. This certifies the inactive-pair regression and
the asymptotic sharpness of R.2b; it does not promote a near-active pair.

Positive KKT, PSD, full-core population, actual O--O train extraction, and a
linear complete transverse shore are omitted from these finite regression
packets. No canonical certificate registration or theorem-state promotion is
requested. Promotion recommendation: **unreviewed** pending independent audit.
