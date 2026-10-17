# Target C-II — every FREE-module core gate contains a nearby actual source-diameter anchor

**Date:** 2026-09-17  
**Status:** proved candidate awaiting promotion; proof-only strengthening of the FREE-MODULE gate branch  
**Scope:** FREE reflection modules at `eta=3/26` after the `CORE-GATE / TRIPLE-GATE` reduction and `Q-DIAMETER` absorption  
**Dependencies:** free-module finite gate process; C26 unloaded-contact barycenter/degree theorem; C65 full diameter visibility; canonical support-cap geometry; full-source diameter midpoint localization; slow-scale module separation; convex diameter-thrackle property  
**Certificate:** `research/verify_target_c_tooth_reflection_core_gate_anchor_2026_09_17.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The `CORE-GATE` endpoint is also not a genuinely separate reflection obstruction. Once a lower repair first touches an original nonisolated contact-core vertex, that core vertex lies in the module's `O(sqrt(D))` support cap. Positive contact equilibrium then forces a strictly outward contact ascent, in the same support coordinate, until an actual source-diameter endpoint is reached. The whole ascent stays inside the same cap.

Hence every CORE-GATE module contains a blocker-side actual source-diameter endpoint within `O(D^(3/4))` of the canonical blocker head. Its actual diameter partner lies within `O(D^(3/4))` of the reflected apex. It therefore contributes exactly the same kind of tagged source-diameter edge as the existing ANCHORED and absorbed `Q-DIAMETER` modules.

Consequently the slow-scale reflection branch has only two effective outcomes:

\[
\boxed{
\text{EXACT-BRAID}
\quad\text{or}\quad
\text{TRIPLE-GATE}.
}
\tag{CG.1}
\]

---

## 1. Support depth of the first core gate

Fix one FREE module. Let `N` be its canonical blocker support direction, let

\[
H=h_A(N),
\qquad
 a_v:=H-N\cdot v
\]

be support depth, and let `B_D=O(sqrt(D))` be the blocker-cap depth from the rigid-gate theorem.

During the finite gate process every original blocker and every absorbed inactive guard satisfies

\[
 a_p\le B_D+O(1)=O(\sqrt D),
\tag{CG.2}
\]

because only a bounded number of gate stages is used before the current `CORE-GATE / TRIPLE-GATE` trichotomy stops.

Suppose a moving point `p(s)` first reaches an original nonisolated contact-core vertex `v` at unit distance:

\[
|p(s)-v|=1.
\tag{CG.3}
\]

The translated point `p(s)` still has support depth `O(sqrt(D))`. Since `|p(s)-v|=1`,

\[
\begin{aligned}
a_v
&=H-N\cdot v\\
&\le H-N\cdot p(s)+1\\
&=a_{p(s)}+1
=O(\sqrt D).
\end{aligned}
\tag{CG.4}
\]

Thus every CORE-GATE endpoint starts inside the same canonical shallow support cap as its reflection module.

---

## 2. An unloaded core vertex has a contact neighbor farther outward in support coordinate

Let `z` be any nonisolated contact-core vertex with

\[
a_z=O(\sqrt D)
\]

and suppose `z` is not an actual source-diameter endpoint.

By C26, `z` has contact degree

\[
3\le\deg_C(z)\le5
\tag{CG.5}
\]

and is a strict positive barycenter of its contact neighbors. Hence there are coefficients

\[
\lambda_{zu}>0
\]

such that

\[
\sum_{u\sim_C z}\lambda_{zu}(u-z)=0.
\tag{CG.6}
\]

Dot (CG.6) with `N`.

Assume no contact neighbor lies farther outward, i.e.

\[
N\cdot(u-z)\le0
\qquad(u\sim_C z).
\tag{CG.7}
\]

Every term in the resulting scalar sum is nonpositive, while every coefficient is positive. Equality of the weighted sum therefore forces

\[
N\cdot(u-z)=0
\qquad\text{for every contact neighbor }u.
\tag{CG.8}
\]

But `|u-z|=1`. A unit vector orthogonal to `N` has only the two possible directions `+JN` and `-JN`. Thus at most two distinct contact neighbors can satisfy (CG.8), contradicting (CG.5).

Therefore every unloaded nonisolated contact vertex has a contact neighbor `u` with

\[
\boxed{
N\cdot u>N\cdot z,
\qquad
a_u<a_z.
}
\tag{CG.9}
\]

This is a strict support-coordinate ascent.

---

## 3. Support ascent terminates at an actual diameter endpoint

Start at the CORE-GATE vertex `v_0=v` from Section 1.

If `v_0` is diameter-loaded, stop. Otherwise apply (CG.9) and choose a contact neighbor `v_1` with

\[
N\cdot v_1>N\cdot v_0.
\]

If `v_1` is not diameter-loaded, repeat.

The source is finite and the scalar coordinate `N dot v_j` strictly increases at every step, so no vertex can repeat and the process must terminate after finitely many steps at a vertex `w` for which the next unloaded ascent is impossible.

That terminal vertex cannot be unloaded and nonisolated, because Section 2 would supply another strictly outward contact neighbor. Hence it is diameter-loaded.

By C65 full diameter visibility, diameter-loaded means exactly that `w` is an endpoint of an actual source diameter edge. Therefore

\[
\boxed{w\in V(H).}
\tag{CG.10}
\]

Moreover support depth decreases along the whole ascent:

\[
a_w<a_{v_j}<\cdots<a_{v_0}=O(\sqrt D).
\]

Thus

\[
\boxed{a_w=O(\sqrt D).}
\tag{CG.11}
\]

The core gate therefore forces an actual diameter endpoint in the same shallow support cap; the ascent cannot escape inward into the bulk.

---

## 4. The loaded sink is `O(D^(3/4))` from the blocker head

The canonical full-source circumradius estimate places the source in a disk

\[
B\!\left(o,{D\over2}+O(\sqrt D)\right).
\tag{CG.12}
\]

The module support line in direction `N` is at signed radius

\[
{D\over2}-O(\sqrt D).
\tag{CG.13}
\]

For any source point `z` with support depth `a_z=O(sqrt(D))`, the radial deficit from the support line is only `O(sqrt(D))`. Intersecting that cap with (CG.12) gives transverse width

\[
O\!\left(\sqrt{D\sqrt D}\right)
=O(D^{3/4}).
\tag{CG.14}
\]

Both the canonical blocker head `y` and the loaded sink `w` lie in this cap. Therefore

\[
\boxed{|w-y|=O(D^{3/4}).}
\tag{CG.15}
\]

Since the blocker head follows the module normal, so does `w-o` up to angular error `O(D^-1/4)`.

---

## 5. The opposite endpoint of the actual diameter lies near the reflected apex

Choose an actual diameter partner `t` of `w`:

\[
|w-t|=D.
\tag{CG.16}
\]

Let

\[
m={w+t\over2}.
\]

The full-source diameter midpoint theorem gives

\[
|m-o|=O(D^{3/4}).
\tag{CG.17}
\]

The simultaneous reflection geometry gives

\[
(w-o)+(q-o)=O(D^{3/4}),
\tag{CG.18}
\]

because `w` is in the same blocker-side cap as `y` and `q` lies in the opposite reflected-apex cap.

Hence

\[
\begin{aligned}
t-q
&=2(m-o)-(w-o)-(q-o),
\end{aligned}
\]

so

\[
\boxed{|t-q|=O(D^{3/4}).}
\tag{CG.19}
\]

Also

\[
\boxed{
\angle(w-t,N)=O(D^{-1/4}).
}
\tag{CG.20}
\]

Thus a CORE-GATE module contributes the same two-cap actual diameter geometry as an ANCHORED or absorbed-Q module.

---

## 6. Core-gate diameter anchors merge into the existing exact braid

For distinct slow-scale modules, the blocker-side caps and reflected-apex caps are separated at scale

\[
\Omega(\kappa_DD^{3/4}),
\qquad
\kappa_D\to\infty,
\tag{CG.21}
\]

while all endpoint localization errors in (CG.15) and (CG.19) are only `O(D^(3/4))`.

Therefore actual diameter edges selected from CORE-GATE modules are pairwise vertex-disjoint for all sufficiently large `D`. They are also vertex-disjoint from the edges already selected from ANCHORED and absorbed-Q modules, by the same two-cap separation argument.

Their directions inherit the module-normal spacing

\[
\Omega(\kappa_DD^{-1/4}).
\tag{CG.22}
\]

The planar diameter graph is a convex geometric thrackle, so every two selected actual diameter edges cross properly. Combining the universal midpoint localization with (CG.22) gives the usual crossing-core estimate

\[
\boxed{
\text{all crossings lie in }B\!\left(o,O(D/\kappa_D)\right)=B(o,o(D)).
}
\tag{CG.23}
\]

Hence ANCHORED, absorbed-Q, and CORE-GATE modules are one common source-diameter braid class.

---

## 7. Source-wide two-way reduction

The slow-scale reflection theorem supplies

\[
M_D>
(c_*-o(1)){D^{1/4}\over\kappa_D},
\qquad
c_*=0.129220199818177\ldots .
\tag{CG.24}
\]

After the earlier module-anchor and `q`-diameter reductions, every selected module now has one of only two effective outcomes:

1. `EXACT-BRAID`: the module is ANCHORED, absorbed-Q, or CORE-GATE and therefore supplies one localized actual source diameter;
2. `TRIPLE-GATE`: the FREE finite repair creates at least three lower gate edges among old fully inactive vertices before reaching the old contact core.

One class therefore contains at least

\[
\boxed{
\left({c_*\over2}-o(1)\right){D^{1/4}\over\kappa_D}
}
\tag{CG.25}
\]

modules, where

\[
\boxed{
{c_*\over2}
=0.0646100999090885\ldots .
}
\tag{CG.26}
\]

If `EXACT-BRAID` wins, all selected edges are vertex-disjoint actual source diameters, pairwise crossing in the common `O(D/kappa_D)` central core.

For every subpolynomial divergent `kappa_D=D^{o(1)}`, the surviving population is

\[
D^{1/4-o(1)}.
\]

The only FREE-module obstruction not yet converted back into the actual diameter system is now the inactive `TRIPLE-GATE` jam.

---

## 8. Frontier effect

The reflection branch has been reduced to

```text
slow-scale shallow-tooth module
    |
    +-- ANCHORED / Q-DIAMETER / CORE-GATE
    |      -> actual source diameter with blocker-side endpoint
    |         in the module O(D^(3/4)) cap
    |      -> opposite endpoint in the reflected-apex O(D^(3/4)) cap
    |      -> all such edges form one exact central braid
    |
    +-- TRIPLE-GATE
           -> at least three newly created lower constraints
              among original fully inactive rattlers
```

The next direct target is therefore the triple-gate geometry itself. Any closure of that finite inactive jam closes the entire FREE reflection branch into the exact source-diameter braid.

**Disposition:** proved a support-coordinate contact ascent from every CORE-GATE endpoint to a nearby actual source-diameter endpoint and merged CORE-GATE into the existing exact-braid class. C-II remains open.
