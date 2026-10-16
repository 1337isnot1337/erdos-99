# Erdos Problem #99 - minimax phase-star atomic gap 0.0021

**Date:** 2026-09-14
**Target:** C-II, canonical full-core Type-II branch
**State version:** `2026-09-14.audit.51`
**Dependencies:** audited-working Sections 163, 164, 168, 171; three-partite phase-star lemma; exact stopped-train ledgers
**Claim class:** proof-only theorem candidate awaiting independent audit
**External literature:** none

## LEVEL I STATUS

`STILL OPEN`

This note strengthens `target_c_phase_star_atomic_gap_0009_2026-09-14.md` by using
both leaf phases of the dominant three-direction orbit simultaneously.  The two
center-leaf missing-edge budgets cannot both be worst-case because triangle-freeness
couples them linearly.  A weighted minimax choice of the better leaf raises the safe
all-Type-II atomic gap to

\[
\boxed{A:=x\sigma\ge2\sqrt{\Delta_2}+0.0021,\qquad
\Delta_2={\pi\over2\sqrt3}.}
\tag{MG.1}
\]

The continuous scalar minimax loses its diameter contradiction only near
`g=0.00212323...`; `0.0021` is certified by exact rational interval arithmetic with a
degree-sum margin greater than `0.00148`.

Audited Section 164 therefore gives

\[
\boxed{\liminf {T-q/2\over D}\ge2\sqrt{\Delta_2}+0.0021.}
\tag{MG.2}
\]

Restricting the same theorem to the rhombic-only train graph gives

\[
\boxed{\liminf {T_R\over D}\ge2\sqrt{\Delta_2}+0.0021,\qquad
\liminf {\sigma_R\over D}\ge0.0042.}
\tag{MG.3}
\]

Feeding `g=0.0021` into audited Section 171 yields

\[
\boxed{\liminf {q-k\over D}\ge {4\over9}\left(\pi+\sqrt{\Delta_2}\right)+0.0017279
>1.82124143795.}
\tag{MG.4}
\]

This supersedes the proof-only `g=0.00042`, `g=0.0009`, and rhombic-only `0.0018`
quantitative checkpoints while retaining them as valid weaker results.

## 1. Dominant orbit and exact deficit control

Use the audited Section-168 all-train measure notation.  Along an arbitrary Type-II
subsequence let `x=lim T/D`, let `sigma` be the total atomic projective-direction mass,
and put `A=x sigma`.  For each `pi/3` projective atom orbit let `M_r` be its absolute
mass and `E_r` its limiting strict-rhombus crossing mass.  Then

\[
E_r\le {M_r^2\over4},\qquad \sum_rE_r=\Delta_2,\qquad \sum_rM_r=A.
\tag{MG.5}
\]

Assume for contradiction

\[
A\le\bar A:=2s+g,\qquad s:=\sqrt{\Delta_2},\qquad g:=0.0021.
\tag{MG.6}
\]

If `W=max_r M_r`, then

\[
W\ge W_0:={4s^2\over\bar A}.
\tag{MG.7}
\]

For the dominant orbit write `delta=W^2/4-E`.  If `R=A-W`, then

\[
\begin{aligned}
{A^2\over4}-s^2-\delta
&={A^2-W^2\over4}-\sum_{r\ne r_*}E_r\\
&\ge {R(2W+R)\over4}-{R^2\over4}={RW\over2}\ge0,
\end{aligned}
\]

because `sum_{r != r_*} E_r <= R^2/4`.  Hence

\[
\boxed{\delta\le {A^2\over4}-s^2\le d_0:={\bar A^2\over4}-s^2=sg+{g^2\over4}.}
\tag{MG.8}
\]

## 2. Three phase classes

Freeze shrinking continuity windows around the at most three dominant-orbit atoms and
pass to a sufficiently far finite source.  Suppressing `o(1)` terms, write

\[
C\ge U\ge V\ge0,\qquad C+U+V=W.
\tag{MG.9}
\]

Same-window train pairs do not cross and the physical train-crossing graph is
triangle-free.  The repository's phase-star lemma gives

\[
E\le C(U+V)=C(W-C),
\]

so

\[
\left(C-{W\over2}\right)^2\le\delta\le d_0.
\tag{MG.10}
\]

Put `z=C-W/2`. Then `|z|<=sqrt(d_0)`.

## 3. Weighted best-leaf lemma

Define center-leaf missing-pair counts

\[
x:=CU-e(C,U),\qquad y:=CV-e(C,V),
\]

and let `e_{UV}=e(U,V)`. Put

\[
h:=C(U+V)-E=x+y-e_{UV}.
\tag{MG.11}
\]

By (MG.10),

\[
0\le h=\delta-z^2\le d_0-z^2.
\tag{MG.12}
\]

For every `UV` crossing, the endpoint neighborhoods in the `C` class are disjoint.
Thus

\[
C e_{UV}\le Vx+Uy.
\]

With

\[
a:=1-{V\over C},\qquad b:=1-{U\over C},
\]

this is

\[
\boxed{ax+by\le h.}
\tag{MG.13}
\]

For one center-leaf pair having leaf population `L` and missing count `m`, the audited
Section-163 pruning/opposite-corner mechanism produces effective degree sum

\[
F(C,L,m):=C+L-6\sqrt m.
\tag{MG.14}
\]

Let

\[
F_U=C+U-6\sqrt x,\qquad F_V=C+V-6\sqrt y.
\]

A maximum dominates every positive weighted average, so

\[
\max(F_U,F_V)\ge {aF_U+bF_V\over a+b}.
\tag{MG.15}
\]

Cauchy-Schwarz and (MG.13) give

\[
a\sqrt x+b\sqrt y\le\sqrt{(a+b)(ax+by)}\le\sqrt{(a+b)h}.
\tag{MG.16}
\]

Let `L=U+V=W-C`.  Since `UV<=L^2/4`,

\[
{aU+bV\over a+b}
={CL-2UV\over2C-L}
\ge {CL-L^2/2\over2C-L}={L\over2}.
\tag{MG.17}
\]

Also `a+b=(3C-W)/C`. Combining (MG.15)--(MG.17) yields

\[
\boxed{\max(F_U,F_V)\ge {W+C\over2}-6\sqrt{h\,{C\over3C-W}}.}
\tag{MG.18}
\]

This is the new step. Equality in the mass relaxation occurs at `U=V`, matching the
numerical worst profile.

## 4. One-dimensional minimax certificate

Substitute `C=W/2+z`. Equations (MG.12) and (MG.18) give

\[
\max(F_U,F_V)
\ge {3W\over4}+{z\over2}
-6\sqrt{(d_0-z^2){W+2z\over W+6z}}.
\tag{MG.19}
\]

For `z<0`, the ratio `(W+2z)/(W+6z)` decreases as either `W` or `z` increases, so
`W>=W_0` gives an upper bound by replacing `W` with `W_0`. For `z>=0` the ratio is at
most one. The raw term is increasing in `W`, so replacing `W` by `W_0` is safe there
as well.

The exact companion verifier covers `[-0.045,0.045]` by 1800 rational intervals of
width `0.00005`; this strictly contains the actual `z` domain. On each interval it
uses the left endpoint for the raw term, the point closest to zero for `d_0-z^2`, the
left endpoint and `W_0` for the negative-`z` ratio, and an integer-ceiling square-root
routine on exact `Fraction` inputs.

The worst certified interval is `[-0.00585,-0.00580]`, and even there

\[
\boxed{\max(F_U,F_V)>1.1561819245>{2\over\sqrt3}+0.00148.}
\tag{MG.20}
\]

No floating-point sign is load-bearing.

## 5. Common-neighbor conditions and diameter contradiction

Choose whichever leaf realizes the maximum in (MG.20), and write its missing-pair
threshold as `p=sqrt(m)`. Since

\[
C+L-6p>{2\over\sqrt3}
\]

and every possible center satisfies `C<2/sqrt(3)`, the leaf satisfies `L>6p`.  The
verifier also gives a uniform `C>5p` for every pair capable of satisfying (MG.20).
Thus after the separate phase-order and degree-pruning losses of `pD+o(D)` on each
shore, both retained families still exceed the `3pD` triple-common-neighbor threshold.

The audited actual-`K_{2,2}` consistency and triple-neighbor transitivity globalize the
crossing orders. The audited opposite-corner path then has degree sum `F_UD-o(D)` or
`F_VD-o(D)`. The two selected phase axes differ by projective angle `pi/3`, so the
common projection tends uniformly to `sqrt(3)/2`. Equation (MG.20) forces source
diameter strictly larger than `D`, contradiction. This proves (MG.1).

Singleton stopped trains do not create an exception. They may occur in the atomic
windows, but they contribute no strict-rhombus crossings and are charged to the same
center-leaf missing budgets `x,y`; a selected near-complete pair cannot retain a
macroscopic singleton subfamily.

## 6. All-train and rhombic propagations

Audited Section 164 gives (MG.2) verbatim. Consequently

\[
\boxed{\liminf {2f-k\over D}\ge2s-{\pi\over2}+0.0021.}
\tag{MG.21}
\]

The Section-146 elimination gain is `2g/9=0.000466666666...`.

The same proof restricted to the non-singleton rhombic crossing graph gives (MG.3).
With `M_R=T_R^2/4-R_4`,

\[
\boxed{\liminf {M_R\over D^2}
\ge {0.0042\over8}\left(4\sqrt{\Delta_2}+0.0021\right)>0.0020009.}
\tag{MG.22}
\]

## 7. Section-171 propagation

Audited Section 171 gives

\[
F_t(\delta):=10t-5\pi-5\delta
+\bigl(81(\pi+\delta)^2\delta\bigr)^{1/3}
-{8\Delta_2\over {9t\over2}-2\pi-2\delta}\ge0
\tag{MG.23}
\]

with feasible interval

\[
0\le\delta\le {{9\over2}(t-C_{146})-g\over2},
\qquad C_{146}={4\over9}(\pi+s).
\tag{MG.24}
\]

Set `g=0.0021`, `epsilon_0=0.0017279`, and `t_0=C_146+epsilon_0`.  The right endpoint
is exactly `delta_0=0.002837775`.  The exact-rational companion certificate proves

\[
1.8212414379510191<t_0<1.8212414379954636,
\]

`F_{t_0}(delta_0)<-2.5e-5`, and `partial_delta F_{t_0}>142` throughout the feasible
interval. Section 171 also proves monotonicity in `t`, so no feasible Type-II limit can
have `t<=t_0`. This proves (MG.4). A high-precision regression gives the scalar root
`epsilon_*=0.00172797507...`.

## 8. Improved detour-free gate

The detour-free exceptional-train proof depends on the atomic gap through
`C_*=2s+g` and the doubled train-slack term `2g`. Its constant becomes

\[
\boxed{c_{DF}^{(21)}:=s-{\pi\over4}+{5g\over2}
=s-{\pi\over4}+0.00525=0.172164643466509\ldots .}
\tag{MG.25}
\]

Thus every Type-II survivor satisfies

\[
\boxed{{\sigma_R+2S_E\over D}\ge c_{DF}^{(21)}
+{5\over2}{k\over D}+{Q-f\over D}-o(1),}
\tag{MG.26}
\]

and, for every fixed admissible pair of direction windows,

\[
\boxed{{\sigma_R+11(Q-f)+20T_{off}\over D}\ge c_{DF}^{(21)}
+{5\over2}{k\over D}-o(1).}
\tag{MG.27}
\]

In particular,

\[
\boxed{\sigma_R\ge0.0860823217D-o(D)\quad\text{or}\quad
S_E\ge0.0430411608D-o(D),}
\tag{MG.28}
\]

and

\[
\boxed{\max\{\sigma_R,Q-f,T_{off}\}/D\ge0.0053801451-o(1).}
\tag{MG.29}
\]

## 9. Updated low-t endpoint diagnostics

At the new safe scalar floor `t=t_0`, the existing low-t ledgers give, with zero
detour/topology bonuses,

\[
{f\over D}\ge0.498052447369096\ldots,
\qquad
{Q-f\over D}\le0.002837775+o(1),
\tag{MG.30}
\]

\[
{p_5\over D}\ge0.495214672369096\ldots-o(1),
\tag{MG.31}
\]

and

\[
\delta\le0.002837775+o(1),\qquad {k\over D}\le0.01135110+o(1).
\tag{MG.32}
\]

The simultaneous outer-to-outer train floor at this formal endpoint is

\[
{L_{OO}\over D}\ge0.318570770872156\ldots-o(1).
\tag{MG.33}
\]

On the additional `R_F=o(D)` branch, the existing low-t pentagon source-object
extractions become

\[
{V_{flat}\over D}\ge0.09904293447\ldots-o(1),
\]

\[
{H_{tooth}\over D}\ge0.05502385249\ldots-o(1),
\]

\[
{C_{flat}\over D},\ {T_{tooth}\over D}\ge0.03809343634\ldots-o(1).
\tag{MG.34}
\]

These are algebraic propagations only.

## 10. Scope audit

- The theorem starts from the audited all-train atomic mass `A=x sigma`, so (MG.1)
  genuinely supersedes AG42 rather than only strengthening the rhombic subgraph.
- The weighted best-leaf lemma uses only the exact three-partite
  neighborhood-disjointness inequality already proved in the repository.
- The one-dimensional interval certificate is outward: all transcendental constants
  enter through rational brackets; square roots use integer ceiling arithmetic.
- The interval proof enlarges the actual `z` domain and weakens every term in the safe
  direction. Its sign margin exceeds `0.0014`.
- Singleton trains are retained in the all-train windows and paid as missing pairs.
- The selected leaf is chosen after its finite missing count is known; no fixed leaf
  label across the sequence is required.
- Phase-order pruning, degree pruning, actual-`K_{2,2}` consistency, crossing-order
  globalization, and the opposite-corner path are the audited Sections 163/168
  mechanisms.
- Atomic-mass semicontinuity is not used.
- Section-164, Section-146, Section-171, detour-free, and low-t formulas are reused
  algebraically with `g=0.0021`; their original scope restrictions remain unchanged.
- Contact-isolated source points remain in the full source.
- No exact unit equilateral triangle or same-cardinality strict sub-`D` competitor is
  produced.

**Disposition:** new strongest proof-only quantitative theorem; independent hostile
audit required before promotion. C-II and Level I remain open.
