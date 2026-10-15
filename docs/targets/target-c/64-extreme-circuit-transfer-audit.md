# Target C — extreme-circuit transfer audit

This module independently audits the useful part of the old extreme-stress campaign
against the current Sections 57–63 state. It does **not** import the rejected cyclic
Reuleaux-cap detour, does not infer geometric release from zero multipliers, and does
not discard contact-isolated source points.

**LEVEL I STATUS: STILL OPEN. C-II REMAINS OPEN.**

---

# 64. Extreme KKT circuits inherit the post-ZF frontier at low degeneracy

Work with the canonical contact-minimal, then diameter-pair-minimal post-ZF C-II
representative. On its nonisolated equality core write

- `v` for the number of vertices;
- `e` for the actual unit-contact rows;
- `h` for the actual diameter rows; and
- `s_Z=e+h-(2v-2)>=0`.

Section 57 gives

\[
\operatorname{rank}R_{C\cup H}=2v-3,
\]

and the canonical relative-interior normalized KKT stress is strictly positive on
every actual contact and diameter row.

Let

\[
\mathcal P=
\left\{x=(\alpha,\beta)\ge0:
R^T(\alpha,-\beta)=0,
\ \sum_{h\in H}\beta_h=1
\right\}
\]

be the normalized nonnegative KKT stress polytope.

For a vertex `x_*` of `P`, let `S_*` be its positive mixed support. Write

- `v_*` for the number of vertices incident to `S_*`;
- `e_*` and `h_*` for its positive contact and diameter rows;
- `q_*` for the number of positive diameter endpoints;
- `b_*` for the outer-face boundary-walk length of its positive contact graph;
- `Q_*` for the bounded nonquadrilateral face defect;
- `x_*^B:=b_*-q_*` for its selected outer-walk excess; and
- `e_{BB,*}` for positive selected contacts whose two endpoints are in the selected
  loaded set `B_*`.

Define

\[
\boxed{\sigma_*:=2v_*-2-(e_*+h_*)}
\tag{64.1}
\]

and let `z_*` be the number of full actual mixed rows omitted by this extreme stress.
The **excess degeneracy** is

\[
\boxed{\kappa_*:=z_*-s_Z.}
\tag{64.2}
\]

The main exact conclusions are:

\[
\boxed{\dim_{\rm aff}\mathcal P=s_Z,}
\tag{64.3}
\]

\[
\boxed{S_*\text{ is a rigidity-matroid circuit},}
\tag{64.4}
\]

\[
\boxed{\kappa_*=2(v-v_*)+\sigma_*\ge0,}
\tag{64.5}
\]

\[
\boxed{b_*+Q_*=2h_*+2\sigma_*,}
\tag{64.6}
\]

and, with `d_*:=q_*-h_*>=0`,

\[
\boxed{q_*+2\sigma_*=x_*^B+Q_*+2d_*.}
\tag{64.7}
\]

The selected loaded boundary also obeys the exact primitive inequality

\[
\boxed{e_{BB,*}+x_*^B\ge q_*.}
\tag{64.8}
\]

The selected stopped-train and difference-body arguments then give

\[
\boxed{3(2h_*-q_*)+5\sigma_*\ge h_*-2,}
\tag{64.9}
\]

\[
\boxed{
Q_*
\le h_*+2\sigma_*+1
-2D\cos\!\left((h_*-1)\arcsin{1\over2D}\right),
}
\tag{64.10}
\]

and

\[
\boxed{
2h_*-q_*
\ge
D\cos\!\left((h_*-1)\arcsin{1\over2D}\right)
-{5\over2}\sigma_*-{3\over2}.
}
\tag{64.11}
\]

Consequently, along any unbounded sequence of extreme circuits with

\[
\boxed{\kappa_*=o(D),}
\tag{64.12}
\]

one has simultaneously

\[
\boxed{
\liminf {h_*\over D}\ge2\rho,
\qquad \rho=\cos\rho,
}
\tag{64.13}
\]

\[
\boxed{
\liminf {2h_*-q_*\over D}\ge c_*,
\qquad c_*=\cos(3c_*/2),
\qquad 0.6099<c_*<0.61,
}
\tag{64.14}
\]

and the selected analogue of Section 63's primitive boundary split,

\[
\boxed{
\liminf {1\over D}\max\{e_{BB,*},x_*^B\}\ge\rho.
}
\tag{64.15}
\]

Thus a single low-degeneracy extreme KKT circuit already carries the same DB-scale
diameter density, NB-scale nonmatching excess, and loaded-contact/outer-detour split
that Sections 59, 61, and 63 force on the full relative-interior support.

The remaining obstruction is therefore precise: prove the existence of one extreme
circuit with `kappa_*=o(D)`, or derive a whole-source contradiction from the hypothesis
that every extreme circuit has `kappa_*=Omega(D)`.

## 64.1 Dimension of the normalized stress polytope

Let `W` be the signed mixed self-stress space in KKT multiplier coordinates. Section 57
gives

\[
\dim W
=(e+h)-(2v-3)
=s_Z+1.
\tag{64.16}
\]

Let

\[
L(\alpha,\beta)=\sum_H\beta.
\]

A nonzero nonnegative equilibrium stress cannot have `L=0`. Indeed `L=0` forces
`beta=0`. Dot the contact-only equilibrium equations with the vertex positions and
sum over vertices. Every unit contact contributes its nonnegative multiplier times
squared length one, so

\[
\sum_C\alpha=0.
\]

Hence all contact multipliers also vanish, contradiction.

The canonical relative-interior KKT stress is strictly positive and has `L=1`.
Therefore the nonnegative stress cone has full relative dimension in `W`, and the
normalization hyperplane cuts it transversely. Hence

\[
\dim_{\rm aff}\mathcal P=s_Z,
\]

proving (64.3).

In particular every extreme point of `P` has at least `s_Z` zero coordinates, but the
stronger circuit statement below is what will be used.

## 64.2 Extreme support is one positive rigidity circuit

Fix a vertex `x_*` of `P` and write `S_*=supp(x_*)`. Let

\[
W_{S_*}:=\{w\in W:\operatorname{supp}w\subseteq S_*\}.
\]

Certainly `dim W_{S_*}>=1`. If it were at least two, choose `w` not proportional to
`x_*` and set

\[
w_0=w-L(w)x_*.
\]

Then `w_0` is nonzero, supported in `S_*`, satisfies equilibrium, and has `L(w_0)=0`.
Every coordinate of `x_*` on `S_*` is strictly positive, so for sufficiently small
`t>0` both

\[
x_*+tw_0,
\qquad
x_*-tw_0
\]

remain nonnegative normalized equilibrium stresses. This contradicts extremality.
Thus

\[
\boxed{\dim W_{S_*}=1.}
\tag{64.17}
\]

If a proper subset of `S_*` were row-dependent, its nonzero supported self-stress would
belong to `W_{S_*}` but could not be proportional to `x_*`, because `x_*` is nonzero on
every row of `S_*`. Therefore every proper subset is independent. This proves (64.4).

Circuit minimality gives

\[
\operatorname{rank}R_{S_*}=e_*+h_*-1.
\]

Since the selected realization is two-dimensional,

\[
e_*+h_*-1\le2v_*-3,
\]

so `sigma_*>=0` as claimed in (64.1).

## 64.3 Every selected circuit has one connected contact support spanning `D`

The positive-support connectivity theorem is valid for an arbitrary normalized KKT
stress, not only the full-support stress. For completeness, the load-bearing argument
is as follows.

Every nontrivial positive contact component must meet the positive diameter endpoint
set: a component with no diameter reaction would carry a nonnegative contact-only
self-stress, which the virial argument from Section 64.1 forbids. Summing equilibrium
over one positive contact component shows that its boundary diameter-reaction vectors
sum to zero.

Positive contact components induce a noncrossing partition of the cyclically ordered
positive diameter endpoints: two disjoint unit-contact paths cannot properly cross in
a unit-separated planar set. If there were at least two components, a standard leaf
argument for a finite noncrossing partition gives two component blocks that are cyclic
intervals. The positive diameter reaction at each selected loaded vertex lies in the
relative interior of that force-hull vertex's normal cone, so the reaction directions
occur in strict cyclic order. Two disjoint interval blocks have total angular span
strictly below `2pi`; one block therefore lies in an open half-plane and its positive
reaction vectors cannot sum to zero. Contradiction.

Hence the positive selected contact graph `C_*` has exactly one nontrivial connected
component. Normalization gives at least one positive diameter edge, both endpoints lie
in that component, and their distance is `D`. Thus

\[
\boxed{\operatorname{diam}V(C_*)=D.}
\tag{64.18}
\]

Harmonic trapping of unloaded positive-contact vertices gives

\[
F_*:=\operatorname{conv}V(C_*)=\operatorname{conv}B_*.
\tag{64.19}
\]

Every selected diameter endpoint is a vertex of `F_*`: if `b` with partner `b'` at
distance `D` were a nontrivial convex combination of other points of `F_*`, equality
in the convexity estimate

\[
|b-b'|\le\sum_i\lambda_i|x_i-b'|\le D
\]

would force every `x_i=b`. Thus the selected loaded endpoints occur in strict convex
cyclic order on `F_*`.

## 64.4 Exact omitted-row and selected face ledgers

The full mixed row count is

\[
e+h=2v-2+s_Z.
\]

The selected circuit count is

\[
e_*+h_*=2v_*-2-\sigma_*.
\]

Subtracting gives

\[
\boxed{
z_*=2(v-v_*)+s_Z+\sigma_*,}
\]

hence (64.5):

\[
\boxed{\kappa_*=z_*-s_Z=2(v-v_*)+\sigma_*.}
\]

For the connected triangle-free selected contact graph, Euler and face incidence give

\[
e_*=2v_*-2-{b_*+Q_*\over2}.
\tag{64.20}
\]

Comparing with `e_*+h_*=2v_*-2-sigma_*` proves (64.6):

\[
\boxed{b_*+Q_*=2h_*+2\sigma_*.}
\]

The positive selected diameter graph is a straight-line subthrackle of the source
diameter graph. Woodall therefore gives exactly two selected branches:

- `d_*=0`: one connected odd-unicyclic component, with all off-cycle vertices pendant
  on the odd cycle;
- `d_*>0`: a caterpillar forest with exactly `d_*` components.

In both cases `h_*<=q_*`, so `d_*=q_*-h_*>=0`. Put

\[
x_*^B=b_*-q_*.
\]

Substitute `b_*=q_*+x_*^B` and `h_*=q_*-d_*` into (64.6). This gives the exact selected
terminal ledger (64.7):

\[
\boxed{q_*+2\sigma_*=x_*^B+Q_*+2d_*.}
\]

It is useful to write

\[
\boxed{r_*:=2h_*-q_*=x_*^B+Q_*-2\sigma_*\ge0.}
\tag{64.21}
\]

In the forest branch,

\[
r_*=\sum_j(q_j-2).
\tag{64.22}
\]

## 64.5 Selected loaded-boundary split

Choose distinguished occurrences of the selected loaded vertices on one cyclic pass of
the selected outer contact-face walk. Split that walk into `q_*` subwalks between
consecutive selected loaded vertices and let their positive-contact edge-occurrence
lengths be `ell_i>=1`. Then

\[
\sum_i(\ell_i-1)=b_*-q_*=x_*^B.
\tag{64.23}
\]

At most `x_*^B` intervals have `ell_i>=2`. Every remaining interval has `ell_i=1`, so
its unique positive contact edge joins two consecutive vertices of the selected convex
force hull. It is therefore a selected loaded-loaded contact. Hence

\[
e_{BB,*}\ge q_*-x_*^B,
\]

which proves (64.8):

\[
\boxed{e_{BB,*}+x_*^B\ge q_*.}
\]

This argument does not assume that every actual unit contact remains positive at the
extreme stress; it uses only the positive selected outer walk.

## 64.6 Selected stopped-train inequality

Section 61's train construction is local to a connected triangle-free unit-contact
plane graph, so it applies verbatim to `C_*`. Let `f_*` be the number of bounded
nonquadrilateral selected contact faces and put

\[
Q_*=f_*+g_*.
\]

The selected train count is

\[
T_*={b_*+Q_*\over2}+2f_*
=h_*+\sigma_*+2f_*,
\tag{64.24}
\]

where the second equality uses (64.6).

Exactly as in Section 61, at most `2x_*^B` outer train-end incidences lie in bad loaded
intervals, exceptional bounded faces supply at most `5f_*+g_*` train-end incidences,
and at most two trains have two good convex-hull ends. Therefore

\[
T_*-2\le2x_*^B+5f_*+g_*.
\]

Using (64.24),

\[
h_*+\sigma_*-2
\le2x_*^B+3f_*+g_*.
\tag{64.25}
\]

By (64.21),

\[
3r_*+6\sigma_*
=3x_*^B+3f_*+3g_*,
\]

whose right side exceeds the right side of (64.25) by `x_*^B+2g_*>=0`. Hence

\[
\boxed{3r_*+5\sigma_*\ge h_*-2,}
\]

which is (64.9).

## 64.7 Selected difference-body inequality

Section 59 gives projective separation

\[
2a_D,
\qquad
a_D:=\arcsin{1\over2D},
\]

between every two distinct actual diameter directions. A selected subset inherits the
same separation.

For the `h_*` selected projective diameter directions `u_j`,

\[
D\operatorname{conv}\{\pm u_j\}\subseteq F_*-F_*.
\]

Ordering their projective gaps `g_i`, with `g_i>=2a_D` and `sum g_i=pi`, perimeter
monotonicity and the same concave gap minimization as Section 59 give

\[
\operatorname{per}(F_*)
\ge
h_*-1+2D\cos((h_*-1)a_D).
\tag{64.26}
\]

The selected positive contact outer walk has geometric length `b_*`, so

\[
\operatorname{per}(F_*)\le b_*.
\tag{64.27}
\]

Using `b_*=2h_*+2\sigma_*-Q_*` from (64.6), (64.26)–(64.27) give

\[
\boxed{
Q_*
\le h_*+2\sigma_*+1
-2D\cos((h_*-1)a_D),
}
\]

proving (64.10).

To obtain the branching feedback, use (64.21) to write

\[
x_*^B=r_*-Q_*+2\sigma_*.
\]

Then the right side of (64.25) satisfies

\[
2x_*^B+3f_*+g_*
\le2x_*^B+3Q_*
=2r_*+Q_*+4\sigma_*.
\]

Thus

\[
h_*-2\le2r_*+Q_*+3\sigma_*.
\]

Insert (64.10) and cancel `h_*`. The result is (64.11):

\[
\boxed{
r_*
\ge
D\cos((h_*-1)a_D)-{5\over2}\sigma_*-{3\over2}.}
\]

## 64.8 Low-degeneracy transfer of Sections 59, 61, and 63

Assume `kappa_*=o(D)` along an unbounded sequence. Equation (64.5) immediately gives

\[
\sigma_*=o(D).
\tag{64.28}
\]

Pass to a subsequence on which `h_*/D->y`. Divide (64.10) by `D` and use `Q_*>=0` and

\[
a_D={1\over2D}+O(D^{-3}).
\]

Then

\[
y\ge2\cos(y/2).
\]

The smallest nonnegative solution is `y=2rho`, where `rho=cos rho`. Therefore

\[
\liminf {h_*\over D}\ge2\rho,
\]

proving (64.13).

Now divide (64.9) and (64.11) by `D`. Any subsequential limits `y=h_*/D` and
`r=r_*/D` satisfy

\[
r\ge {y\over3},
\qquad
r\ge\cos(y/2).
\]

Hence

\[
r\ge\max\{y/3,\cos(y/2)\}.
\]

The Section 61 optimization has unique crossover

\[
y/3=\cos(y/2),
\]

or `y=3c_*`, and minimum value `c_*`, where

\[
c_*=\cos(3c_*/2),
\qquad 0.6099<c_*<0.61.
\]

Since `3c_*>2rho`, the already-proved restriction `y>=2rho` does not change that
minimum. This proves (64.14).

Finally the selected Woodall bound gives `q_*>=h_*`. By (64.8),

\[
\max\{e_{BB,*},x_*^B\}
\ge {q_*\over2}
\ge {h_*\over2}.
\]

Combine with (64.13):

\[
\boxed{
\liminf {1\over D}\max\{e_{BB,*},x_*^B\}\ge\rho,
}
\]

which proves (64.15).

Thus every low-degeneracy extreme circuit inherits on one support:

\[
\boxed{
 h_*\ge(2\rho-o(1))D,
\quad
2h_*-q_*\ge(c_*-o(1))D,
\quad
\max\{e_{BB,*},x_*^B\}\ge(\rho-o(1))D.
}
\tag{64.29}
\]

## 64.9 Regressions and rejected shortcuts

1. **Zero multiplier is not a geometric release.** An actual row omitted by one extreme
   stress can remain strong under another stress. No selected-support flex is promoted
   to a feasible full-source motion here.
2. **High degeneracy is real.** A straight-chain extreme has `h_*=O(1)` and
   `sigma_*=Theta(D)`; regular even-shell-type positive circuits also show that a
   two-dimensional positive PSD circuit can have linear bar-flex deficit. Section 64
   does not exclude either pattern in isolation.
3. **No invalid cyclic cap theorem is used.** In particular no selected or full
   outer-contact detour is placed in the exterior Reuleaux minor cap, and no
   `b-per(F)=o(D)` conclusion is assumed.
4. **No KKT coefficient floor is used.** All statements are support/count/geometric
   consequences valid with arbitrarily small positive extreme coefficients.
5. **Contact-isolated source points remain.** Section 64 works on selected/full KKT
   cores but makes no identification of those core vertex counts with the full source
   population `n`.

## 64.10 Remaining obstruction

Section 64 turns the `s_Z>0` stress-space ambiguity into one exact ensemble problem.
Every extreme normalized KKT stress is a positive diameter-spanning rigidity circuit.
If even one extreme has `kappa_*=o(D)`, then the complete Sections 59/61/63 diameter-
scale structural frontier already appears on that circuit by (64.29).

What remains is therefore not another selected diameter-density estimate. A closing
argument must prove one of:

1. **low-degeneracy extreme existence:** some extreme circuit satisfies
   `kappa_*=o(D)` and its transferred high loaded-contact / high outer-detour branch can
   then be closed geometrically; or
2. **ensemble degeneracy contradiction:** if every extreme circuit has
   `kappa_*=Omega(D)`, use interactions among the extreme circuits, omitted actual
   rows, or full-source completion capacity to contradict the full-support C-II source.

General polytope dimension alone cannot prove (1); direct-sum linear matroids provide
abstract counterexamples. The missing input must use the planar unit-contact / diameter
geometry or whole-source optimality.
