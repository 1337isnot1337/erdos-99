# Target C-II — coupled matching/reflection floor from the exact tooth/long-side burden

**Date:** 2026-09-15  
**Status:** proved proof-only composition; theorem-state authority unchanged  
**Scope:** no-container/full-core Type-II low-`t` branch  
**Dependencies:** exact tooth/long-side burden; shallow-tooth penetration matching; shallow-tooth reflection blockers and perimeter collapse; occurrence-injective long-side transverse selection; low-`t` network squeeze  
**LEVEL I STATUS:** `STILL OPEN`

The current coupled physical-contact theorem obtains the branch-independent floor

\[
0.202530020131380\ldots D-o(D)
\]

by paying a factor `1/2` when shallow teeth are converted to physical penetration
contacts. The subsequently merged shallow-tooth theorem removes that factor: for every
fixed threshold with `alpha_eta<pi/6`, the selected penetration contacts form an actual
matching and therefore

\[
|M_\eta|=N_{sh}(\eta).
\]

Re-optimizing the same exact tooth/long-side burden with the matching theorem raises
the branch-independent floor by the exact factor `6/5`:

\[
\boxed{
0.2430360241576561830\ldots D-o(D).
}
\]

The reflection/perimeter theorem gives additional geometry in the tooth outcome. All
but `o(D)` shallow teeth have an upper reflection blocker, so the same population is
coupled to `D-O(1)` source pairs aligned with the inward normal of the loaded base.
Moreover, the blocker is near-diametral not only to the unloaded apex but to both
loaded endpoints of the base.

Thus every low-`t` survivor in the stated scope satisfies one of two physical
alternatives:

1. at least `0.2430360241 D-o(D)` shallow teeth carry both a penetration-matching
   edge and a normal-aligned near-diameter blocker; or
2. at least `0.2430360241 D-o(D)` distinct long-side transverse contact edges occur.

No KKT contact-weight floor is used.

---

## 1. Matching-scale tooth physicalization

Fix

\[
\eta={15\over56},
\qquad
\alpha_\eta=\arccos(1-\eta/2).
\tag{CMR.1}
\]

Then

\[
\cos\alpha_\eta={97\over112}>{\sqrt3\over2},
\qquad
\sin\alpha_\eta={\sqrt{3135}\over112},
\qquad
\alpha_\eta<\pi/6.
\tag{CMR.2}
\]

The shallow-tooth penetration matching theorem applies and gives

\[
\boxed{
E_T:=|M_\eta|=N_{sh}(\eta)
\ge N_2-{d_{out}\over\eta}.
}
\tag{CMR.3}
\]

This is the precise point where the older coupled theorem lost a factor two: it used
only endpoint counting and obtained `E_T >= N_sh/2`, whereas the now-available theorem
makes the selected penetration edges a matching.

Every matching edge has inward component greater than

\[
Y_\eta
:=\sin(\pi/3-\alpha_\eta)
={97\sqrt3-\sqrt{3135}\over224}
=0.500079721506711\ldots>{1\over2}.
\tag{CMR.4}
\]

---

## 2. Long-side physicalization

Put

\[
\beta={\pi\over6},
\qquad
c_\beta:=1-\cos\beta=1-{\sqrt3\over2}.
\]

Let `E_L` be the distinct physical transverse contacts selected from the rounded
long-side outer-route occurrences. The existing occurrence-injective selection and
bridge-subtracted isoperimetry give, along a convergent full-core Type-II subsequence,

\[
\boxed{
\liminf {E_L\over D}
\ge {\ell\over2}
-\delta\left({1\over2}+{1\over c_\beta}\right),
}
\tag{CMR.5}
\]

where

\[
\ell:=\lim {L_{>2}\over D},
\qquad
\delta:=\lim {d_{out}\over D}.
\]

Every edge counted by `E_L` has absolute transverse component strictly greater than
`1/2` relative to its associated long loaded-hull side.

---

## 3. Optimize the exact coupled burden with the matching theorem

Along the same convergent subsequence write

\[
n_2:=\lim {N_2\over D},
\qquad
\kappa:=\lim {k\over D}.
\]

The exact outer-boundary burden is

\[
\boxed{
n_2+2\ell\ge\pi-t-\kappa-\delta.
}
\tag{CMR.6}
\]

Define

\[
y:=\max\left\{
\liminf {E_T\over D},
\liminf {E_L\over D}
\right\}.
\tag{CMR.7}
\]

From (CMR.3),

\[
n_2\le y+{\delta\over\eta}.
\tag{CMR.8}
\]

From (CMR.5),

\[
\ell\le2y+\delta\left(1+{2\over c_\beta}\right).
\tag{CMR.9}
\]

Insert (CMR.8)--(CMR.9) into (CMR.6). This gives

\[
\boxed{
5y\ge\pi-t-\kappa-K\delta,
}
\tag{CMR.10}
\]

with exactly the same detour coefficient as in the older factor-`1/2` theorem,

\[
\begin{aligned}
K
&=3+{1\over\eta}+{4\over c_\beta}\\
&=3+{56\over15}+8(2+\sqrt3)\\
&={341\over15}+8\sqrt3\\
&=36.5897397938843516\ldots .
\end{aligned}
\tag{CMR.11}
\]

The sole change is the coefficient of `y`: the old theorem had `6y` because it used
`n_2<=2y+delta/eta`; matching gives `n_2<=y+delta/eta`.

---

## 4. Insert the low-`t` network squeeze

The current low-`t` network theorem gives

\[
2\delta+{\kappa\over2}\le R(t),
\qquad
R(t):={9t\over2}-2\pi-C_0.
\tag{CMR.12}
\]

At fixed `delta`, the right side of (CMR.10) is minimized by taking

\[
\kappa=2R(t)-4\delta.
\]

Because `K>4`, the remaining expression decreases as `delta` increases. Hence the
worst feasible point is

\[
\delta={R(t)\over2},
\qquad
\kappa=0.
\]

Therefore

\[
\boxed{
y\ge
{1\over5}\left[
\pi-t-
\left({341\over30}+4\sqrt3\right)R(t)
\right].}
\tag{CMR.13}
\]

At the present endpoint

\[
t_{42}=1.8208886379794447\ldots,
\qquad
R(t_{42})=0.00576795,
\]

this becomes

\[
\boxed{
y\ge0.2430360241576561830\ldots .}
\tag{CMR.14}
\]

The previous coupled floor is the same numerator divided by six, so the improvement
factor is exactly

\[
\boxed{6/5.}
\tag{CMR.15}
\]

---

## 5. Perimeter collapse upgrades the tooth alternative

The reflection theorem for one `eta`-shallow tooth uses coordinates

\[
a=(-c,0),\qquad b=(c,0),\qquad x=(0,h),
\]

with `c=cos alpha`, `h=sin alpha`, and reflects `x` to `x^-=(0,-h)` across its loaded
base. Every shallow tooth has either

- an exterior-isolate reflection witness below the supporting line, or
- an upper blocker `y=(p,q)` satisfying `|y-x^-|>D`.

For every fixed `eta` with `alpha_eta<pi/6`, the exterior-witness branch has only
`o(D)` tooth occurrences. Indeed every exterior witness projects into the relative
interior of its tooth side and belongs to a distinct nondegenerate source-hull cap;
each such cap costs a fixed positive amount of `per(K)-per(F)`, while

\[
\operatorname{per}(F)=\pi D-o(D),
\qquad
\operatorname{per}(K)\le\pi D.
\]

Thus if the tooth term realizes the maximum in (CMR.7), then all but `o(D)` of those
matching teeth have an upper blocker. In particular the tooth alternative in
(CMR.14) strengthens to

\[
\boxed{
U\ge0.2430360241576561830\ldots D-o(D),
}
\tag{CMR.16}
\]

where `U` counts distinct shallow apexes carrying an upper blocker.

At `eta=15/56`, the uniform blocker geometry is

\[
\boxed{
|x-y|>D-{\sqrt{3135}\over56}
=D-0.999840548512101\ldots,
}
\tag{CMR.17}
\]

and, in base coordinates,

\[
\boxed{
q>0,
\qquad
{|p|\over q}< {\sqrt{3135}\over97}
=0.577227533161625\ldots .
}
\tag{CMR.18}
\]

The eliminated exterior branch has support-line depth greater than `Y_eta` from
(CMR.4) and therefore costs at least

\[
g_\eta
=2\bigl(\sqrt{1+Y_\eta^2}-1\bigr)
=0.236139287130594\ldots
\tag{CMR.19}
\]

of source-hull perimeter per witnessed side.

---

## 6. Upper blockers are near-common antipodes of the loaded base

The upper-blocker geometry contains an additional exact relation that is useful for
the diameter-thrackle interface.

Let

\[
d_x:=|y-x|,
\qquad d_a:=|y-a|,
\qquad d_b:=|y-b|.
\]

Direct expansion gives

\[
d_a^2-d_x^2
=2hq+2cp+\cos(2\alpha),
\tag{CMR.20}
\]

\[
d_b^2-d_x^2
=2hq-2cp+\cos(2\alpha).
\tag{CMR.21}
\]

The reflected diameter violation and the original diameter bounds to `a,b` imply

\[
2hq-2c|p|>\cos(2\alpha).
\tag{CMR.22}
\]

Therefore

\[
\boxed{
\min\{d_a^2,d_b^2\}
>d_x^2+2\cos(2\alpha).
}
\tag{CMR.23}
\]

At the threshold `eta=15/56`,

\[
2\cos(2\alpha_\eta)
={3137\over3136}
=1.000318877551020\ldots>1.
\tag{CMR.24}
\]

So an upper blocker is not merely near-diametral to the unloaded apex: it is strictly
farther from **both loaded base endpoints** by more than one in squared-distance
margin.

Also

\[
d_x^2>D^2-4hq.
\tag{CMR.25}
\]

Since `q<=D`, (CMR.23)--(CMR.25) give the uniform loaded-endpoint estimate

\[
\boxed{
\min\{d_a^2,d_b^2\}
>D^2-{\sqrt{3135}\over28}D+{3137\over3136}.
}
\tag{CMR.26}
\]

Thus every tooth in the surviving blocker branch determines a loaded hull side whose
two endpoints have a common source point at distance `D-O(1)`. This is an approximate
common-antipode fan on the actual loaded boundary.

Equation (CMR.26) does **not** imply that either pair is an exact diameter pair. In the
Woodall cyclic branch exact common diameter partners are already supplied by the
Reuleaux representation; the new content is primarily at the forest/noncyclic
interface.

---

## 7. Updated low-`t` normal form

At the present endpoint every no-container/full-core Type-II survivor satisfies at
least one of:

```text
TOOTH / MATCHING / DIAMETER-BRACE BRANCH
    >= 0.2430360241 D-o(D) pairwise-disjoint penetration contacts,
    inward component > 0.5000797215,
    and all but o(D) associated tooth apexes have an upper blocker
    within 0.999840549 of diameter,
    aligned to the loaded-side inward normal,
    and near-diametral to both loaded base endpoints;

ROUNDED LONG-SIDE BRANCH
    >= 0.2430360241 D-o(D) distinct transverse contacts,
    transverse component > 1/2 relative to their long loaded sides.
```

This strictly supersedes the `0.2025300201D` branch-independent contact floor once the
penetration matching theorem is admitted.

The remaining obstruction is global. On the tooth side, one upper blocker can still
serve many nearby shallow bases and near-diameter does not automatically promote to an
actual Woodall edge. On the long-side side, a coherent rhombic train can absorb many
transverse contacts. A closing theorem now needs to bound **diameter-brace reuse / train
occupancy**, or construct a source-preserving boundary exchange. Further scalar
physicalization alone is not enough.

## 8. Reproducibility

Run

```bash
python3 research/verify_target_c_matching_reflection_coupled_floor.py
```

for the high-precision coupled constant, reflection constants, and finite
upper-blocker regressions.
