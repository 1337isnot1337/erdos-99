# Target C-II — inactive lower and upper gates can be absorbed simultaneously

**Date:** 2026-09-17  
**Status:** proved candidate awaiting promotion; proof-only strengthening of the FREE reflection repair  
**Scope:** non-anchored FREE modules at `eta=3/26`  
**Dependencies:** FREE rigid repair; retained-tooth lower safety; full-source same-center disk sandwich; canonical support-width blocker; C26 support ascent for active gates; contact-minimal normalization  
**Certificate:** `research/verify_target_c_tooth_reflection_two_sided_gate_absorption_2026_09_17.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The previous repair stops when a moving inactive blocker/guard first creates either a new unit equality or a new diameter equality. A unit equality with an old inactive point can already be absorbed by starting that point with the same velocity. The same is true for a new diameter equality.

The key finite observation is that both kinds of newly tight edge can later be made strict by one common perturbation. If vertices are labeled by their activation times, move later-activated vertices a little farther in the repair direction. First-hit unit edges lengthen; first-hit diameter edges shorten. Thus inactive upper gates are not terminal obstructions.

This allows the FREE repair to be run almost across the full source width. Put

\[
\varepsilon_D=D^{-1/3},
\qquad
t_D=\delta+\varepsilon_D,
\qquad
L=|y-q|=D+\delta,
\]

with

\[
0<\delta<h_*={\sqrt{303}\over52}.
\]

Define the near-opposite support threshold

\[
\boxed{
T_D:=D-1-2\varepsilon_D.
}
\tag{TA.1}
\]

Then every non-anchored FREE module has the following alternative:

\[
\boxed{
\text{ACTIVE-GATE / exact-anchor event}
\quad\text{or}\quad
\text{an all-inactive activation ancestry reaches support depth }>T_D.
}
\tag{TA.2}
\]

In the second branch, the ancestry necessarily contains almost `D` lower-gate edges. More precisely, if `L_D` denotes the number of lower-gate edges on one ancestry reaching the first vertex beyond `T_D`, then

\[
\boxed{L_D\ge D-O(\sqrt D).}
\tag{TA.3}
\]

Their **total original near-unit slack** is bounded by the same clearing-time constant:

\[
\boxed{
\sum_{e\in E_{\rm low}}(|e|-1)
\le t_D<h_*+D^{-1/3}.
}
\tag{TA.4}
\]

Consequently, for every fixed `K>h_*`, one such FREE module already forces a vertex-disjoint matching of old fully inactive original source pairs satisfying

\[
1<|x-y|\le1+{K\over D}
\]

and having size

\[
\boxed{
\left(
{1\over2}-{h_*\over2K}-o(1)
\right)D.
}
\tag{TA.5}

For `K=1`, the coefficient is

\[
\boxed{0.3326260078314499\ldots,}
\tag{TA.6}
\]

and for `K=2` it is

\[
\boxed{0.416313003915725\ldots.}
\tag{TA.7}
\]

If `K_D->infinity` and `K_D=o(D)`, the matching size rises to

\[
\boxed{(1/2-o(1))D}
\tag{TA.8}

with pair lengths at most `1+K_D/D=1+o(1)`.

Unlike the earlier `CENTER-CORRIDOR` statement, (TA.3)--(TA.8) remain valid even if inactive upper-diameter gates occur and are absorbed along the way. The price is that the ancestry need no longer be a single outer-face geometric corridor: an upper gate can jump between faces. The theorem therefore records a source-wide inactive near-unit ladder/matching, not a planar outer-face path.

---

## 1. Two-sided activation process

Start with the entire FREE blocker set `U` moving with velocity `-N` from time zero, exactly as in the rigid repair.

Whenever a moving vertex first reaches a still-fixed source point at distance `1`, inspect the fixed point. If it is fully inactive in the original source, activate it at that time and thereafter move it with velocity `-N`. If it belongs to the old active contact/diameter core, stop with `ACTIVE-GATE`; the existing CORE-GATE/support-ascent mechanism supplies an actual source-diameter anchor.

Do the same at the upper boundary. Whenever a moving vertex first reaches a still-fixed source point at distance `D`, activate the fixed point if it was fully inactive in the original source. If it was active, stop with `ACTIVE-GATE`. An already existing `Q-DIAMETER` or anchored-module event may also be retained as an exact-anchor stop.

Between events all inequalities are strict and hence persist by continuity. Once both endpoints of a newly tight edge are active, they have the same velocity, so their relative vector is frozen until the later strictification step.

Two fixed vertices cannot create a new equality because neither moves. Two already-active vertices cannot create a new equality because their relative velocity is zero. Therefore every first new equality is seen in an active-versus-fixed pair and is captured by this activation rule.

---

## 2. Activation-time strictification opens lower gates and shortens upper gates

For every activated old-inactive vertex `v`, let `s_v` be its activation time. Blocker roots have `s_v=0`.

Suppose `v` is activated at time `s_v` by a previously active vertex `u`, whose activation time is `s_u<s_v`. Put

\[
\Delta=s_v-s_u>0
\]

and let

\[
d=u-\Delta N-v
\tag{TA.9}
\]

be their relative vector at the activation event. After both vertices move together to terminal time, their relative vector is still `d`.

### Lower gate

If `|d|=1`, then before `s_v` the squared distance

\[
f(s)=|u-(s-s_u)N-v|^2
\]

was strictly larger than one. Hence at the first lower hit

\[
f'(s_v)=-2N\cdot d\le0,
\]

so

\[
N\cdot d\ge0.
\tag{TA.10}
\]

### Upper gate

If `|d|=D`, the same squared distance was strictly smaller than `D^2` immediately before the first upper hit. Since `f` is a strictly convex quadratic, its derivative at such a first hit is strictly positive; derivative zero would be its minimum and would force nearby earlier values to be at least `D^2`. Thus

\[
f'(s_v)=-2N\cdot d>0,
\]

and therefore

\[
N\cdot d<0.
\tag{TA.11}
\]

Now perturb the terminal activated configuration by

\[
\boxed{
P_v(\theta)=P_v-\theta s_vN,
\qquad \theta>0.
}
\tag{TA.12}
\]

For the gate edge `uv`,

\[
P_u(\theta)-P_v(\theta)
=d+\theta\Delta N.
\tag{TA.13}
\]

If it is a lower gate, (TA.10) gives

\[
|d+\theta\Delta N|^2
=1+2\theta\Delta N\cdot d+\theta^2\Delta^2
>1
\tag{TA.14}
\]

for every `theta>0`.

If it is an upper gate, (TA.11) gives

\[
|d+\theta\Delta N|^2
=D^2+2\theta\Delta N\cdot d+\theta^2\Delta^2
<D^2
\tag{TA.15}
\]

for all sufficiently small positive `theta`.

There are only finitely many gate equalities in the fixed source. Choose one `theta>0` small enough for every upper gate simultaneously and small enough to preserve every other strict source-source inequality. Then **all** new lower and upper gate equalities become strict at once.

This is the finite strictification step missing from the one-sided absorption proof.

---

## 3. Why the repair can be run to depth `D-1-o(1)`

Let

\[
H=h_A(N),
\qquad
a_v=H-N\cdot v.
\]

The canonical blocker geometry gives

\[
q=y-LN,
\qquad L=D+\delta,
\]

and hence, for every original source point `v`,

\[
N\cdot(v-q)=L-a_v.
\tag{TA.16}
\]

Assume no activated vertex has support depth above `T_D` from (TA.1). Then

\[
N\cdot(v-q)
\ge L-T_D
=1+\delta+2\varepsilon_D
=1+t_D+\varepsilon_D.
\tag{TA.17}
\]

A vertex activated at time `s_v` moves by at most `t_D-s_v` before terminal time. Therefore its terminal `N`-projection from `q` is at least

\[
1+\varepsilon_D+s_v>1.
\tag{TA.18}
\]

So every absorbed guard remains strictly farther than one from the future reflected apex `q`.

The same positive projection shows that the displacement toward `q` decreases `|q-v|`. Since every guard began outside the upper blocker set `U`, its original distance from `q` was at most `D`; an exact equality is the already separated `Q-DIAMETER` branch. Hence every absorbed guard is also strictly below `D` from `q` at terminal time.

The strictification perturbation (TA.12) can be chosen additionally with `theta t_D<varepsilon_D/2`; then (TA.18) retains a positive lower margin and the upper distance from `q` continues to decrease.

The blocker roots themselves are unchanged by (TA.12) because their activation time is zero, and the rigid-clearing theorem already places all of them strictly inside distance `D` from `q` at `t_D`.

Thus, if the two-sided activation process reaches the clearing time without an active-gate stop and without ever activating a point beyond `T_D`, the terminal configuration can be strictified so that:

- every source-source distance is again strict away from the old fixed active constraints;
- every moved/absorbed old-inactive vertex is at distance in `(1,D)` from `q`;
- every old upper blocker is strictly below `D` from `q`;
- the retained reflection has no lower witness away from its two loaded base endpoints.

Replace the old shallow apex `x` by `q`. The two loaded base contacts survive, while every other old contact incident to `x` disappears. Canonical C26 gives `deg_C(x)>=3`, so the contact count drops by at least one. If the new source has diameter below `D`, global minimality fails; if it still has diameter `D`, contact minimality fails. Both are impossible.

Therefore, absent an active/exact-anchor event, some old fully inactive vertex must be activated with

\[
\boxed{a_v>T_D=D-1-2D^{-1/3}}
\tag{TA.19}

before clearing. This proves (TA.2).

The threshold is genuinely available inside the source width: the canonical estimate `D-W<h_*` gives

\[
W>D-h_*>D-1-2D^{-1/3}=T_D
\]

for all sufficiently large `D`.

---

## 4. Any ancestry reaching the threshold contains `D-O(sqrt D)` lower gates

Take an activation ancestry

\[
z_0,z_1,\ldots,z_m
\]

from a blocker root to the first activated vertex with `a_{z_m}>T_D`.
Let

\[
0=s_0<s_1<\cdots<s_m\le t_D,
\qquad
\Delta_j=s_{j+1}-s_j.
\]

The activation-time increments telescope:

\[
\boxed{
\sum_{j=0}^{m-1}\Delta_j=s_m\le t_D.
}
\tag{TA.20}

For an ancestry edge put

\[
d_j=z_j-\Delta_jN-z_{j+1}.
\]

If the edge is a lower gate, `|d_j|=1` and (TA.10) gives `N dot d_j>=0`. Its support-depth increment satisfies

\[
0<a_{z_{j+1}}-a_{z_j}
=N\cdot d_j+\Delta_j
\le1+\Delta_j.
\tag{TA.21}
\]

If the edge is an upper gate, (TA.11) gives

\[
a_{z_{j+1}}-a_{z_j}
=N\cdot d_j+\Delta_j
<\Delta_j.
\tag{TA.22}
\]

Let `L_D` be the number of lower edges on this ancestry. Summing (TA.21)--(TA.22),

\[
a_{z_m}-a_{z_0}
\le L_D+\sum_j\Delta_j
\le L_D+t_D.
\tag{TA.23}
\]

The root depth is `a_{z_0}=O(sqrt D)` by the canonical blocker-cap theorem, while `a_{z_m}>T_D=D-O(1)`. Therefore

\[
\boxed{
L_D\ge D-O(\sqrt D),
}
\]

which is (TA.3).

This estimate is insensitive to upper-gate backtracking. An upper gate can move the ancestry far toward the blocker side, but it can contribute at most `Delta_j` positively to support depth. Almost the entire near-diameter support traverse must therefore be paid for by lower-gate steps.

---

## 5. The lower gates have only `O(1)` total original slack

For a lower ancestry edge,

\[
|d_j|=1,
\qquad
z_j-z_{j+1}=d_j+\Delta_jN.
\]

Both endpoints were fully inactive in the original source, so this original pair was a strict noncontact. Hence

\[
1<|z_j-z_{j+1}|\le1+\Delta_j.
\tag{TA.24}
\]

Writing

\[
\sigma_j=|z_j-z_{j+1}|-1>0,
\]

we get `sigma_j<=Delta_j`. Summing only over lower edges and using (TA.20),

\[
\boxed{
\sum_{j\in E_{\rm low}}\sigma_j
\le t_D<h_*+D^{-1/3},
}
\]

which is (TA.4).

Fix `K>0`. The number of lower edges with

\[
\sigma_j>{K\over D}
\]

is at most

\[
\left({h_*\over K}+o(1)\right)D.
\tag{TA.25}
\]

Combining with (TA.3), the number of good lower edges is at least

\[
\left(1-{h_*\over K}-o(1)\right)D.
\tag{TA.26}
\]

The ancestry is a simple sequence of distinct activated vertices. Partition its edges by index parity. Each parity class is vertex-disjoint, regardless of whether intervening ancestry edges are lower or upper. One parity contains at least half the good lower edges. This proves (TA.5).

For `K=1`,

\[
{1\over2}-{h_*\over2}
=0.3326260078314499\ldots .
\]

For `K=2`,

\[
{1\over2}-{h_*\over4}
=0.416313003915725\ldots .
\]

The fixed-`K` coefficient is positive for every `K>h_*`.

If `K=K_D->infinity`, the bad lower-edge count in (TA.25) is `o(D)`, while (TA.3) gives `(1-o(1))D` good lower edges. Parity thinning proves (TA.8). If also `K_D=o(D)`, their length threshold tends to one.

---

## 6. Active upper gates are a separate force-visible branch

The theorem deliberately does not absorb an old active source point.

If the fixed endpoint of an upper gate is already an actual diameter endpoint, an exact anchor is present immediately. If it is a nonisolated unloaded contact-core vertex `v`, the original gate pair is fixed-slack near-diametral because the moving endpoint has traveled by at most `t_D<h_*+o(1)`. Hence

\[
|v-o|={D\over2}+O(\sqrt D).
\]

Use the radial support direction `(v-o)/|v-o|`. The C26 positive contact equilibrium gives a strictly outward contact neighbor until the support ascent reaches an actual diameter-loaded endpoint. The ascent remains in an `O(sqrt D)` support cap, exactly as in the existing CORE-GATE argument.

Thus an `ACTIVE-GATE` still converts to an actual source-diameter anchor. What is not claimed here is that active upper gates from different slow-scale modules produce distinct or coherently ordered diameter edges after the ancestry has crossed the circumcenter plane.

---

## 7. Relation to the earlier corridor and tangent-gate results

This theorem changes how the earlier reductions should be used.

A pre-center inactive upper gate is still a valid geometric object: the tangent-gate theorem shows that, if one chooses to stop there, it is a pairwise-crossing `D-O(D^-1/4)` inactive near-diameter edge. But it is **not** a terminal finite-repair obstruction. It may instead be absorbed and later strictified by (TA.12).

Likewise the `CENTER-CORRIDOR` branch remains useful because, before any upper gate, it has the stronger simple outer-face path structure. The present theorem trades that planar path structure for much greater support depth. After inactive upper-gate absorptions, the ancestry can jump between outer faces, so only the activation sequence and its lower-gate matching are asserted.

The strongest current FREE alternatives are therefore:

```text
ACTIVE / EXACT ANCHOR
    an old force-visible point is reached, or an existing exact anchor fires;

or

NEAR-OPPOSITE INACTIVE LADDER
    an activation ancestry reaches support depth D-1-o(1);
    D-O(sqrt D) of its ancestry edges are lower gates;
    total original excess of all those lower pairs above one is O(1);
    for every fixed K>h_*:
        (1/2-h_*/(2K)-o(1))D vertex-disjoint old inactive 1+K/D pairs.
```

The second branch gives a source-wide linear inverse-diameter near-unit matching from **one** reflection module. It does not yet make those pairs Horn `LOWER` blockers or prove a protected simultaneous closing motion. That is the next finite-exchange seam.

**Disposition:** proved a two-sided activation/strictification lemma for inactive reflection gates and used it to push a non-anchored FREE repair to support depth `D-1-o(1)`, forcing a `D-O(sqrt D)` lower-gate ladder and a near-half-diameter inactive near-unit matching. C-II remains open.
